#!/usr/bin/env python3
"""
Nuclear Physics Experimental Data Analysis Suite (CLI & Library).

A unified, zero-external-dependency (NumPy + SciPy only) nuclear spectroscopy toolkit.
Designed to run seamlessly across all lab devices, clusters, and offline computers.

Commands:
  kinematics  : Heavy-ion fusion kinematics, Coulomb barrier, recoil velocity, Doppler shift.
  angdist     : In-beam gamma-ray angular distribution fit (A0, a2, a4).
  dualroots   : Solve quadratic dual roots for multipole mixing ratio delta(E2/M1).
  trapezoid   : Digital pulse processing with Jordanov recursive trapezoidal filter.
  peakfit     : High-precision photopeak fit (Gaussian + Erfc Step + Linear Baseline).
  selftest    : Run complete suite of unit tests.
"""

import sys
import os
import argparse
import numpy as np

from heavy_ion_kinematics import calculate_kinematics, doppler_shift, doppler_broadening
from angular_distribution_solver import angular_distribution_model, fit_angular_distribution, solve_delta_dual_roots
from digital_trapezoidal_filter import synthesize_preamp_pulse, apply_trapezoidal_filter, extract_trapezoid_amplitude
from gamma_peak_fitting import single_peak_model, fit_single_gamma_peak
from dco_polarization_analyzer import joint_dco_polarization_fit, calculate_dco_ratio, calculate_linear_polarization
from lifetime_lineshape_calculator import calculate_stopping_time_alpha, dsam_invert_lifetime, calculate_absolute_transition_strengths
from routhian_alignment_analyzer import calculate_alignment_and_routhians, fit_harris_reference
from ensdf_crosswalk_parser import parse_ensdf_records, crosswalk_match
from excitation_function_calculator import calculate_target_energy_loss, extract_cross_section_from_yield, fit_excitation_function
from magnetic_rotation_shears_calculator import calculate_shears_angle, calculate_magnetic_rotation_bm1, shears_band_profile
from shape_coexistence_e0_calculator import calculate_omega_k_e0, extract_rho2_e0_from_lifetime, invert_two_state_mixing
from moment_of_inertia_spin_analyzer import calculate_moments_of_inertia, invert_floating_band_spin
from coulex_kumar_invariant_calculator import calculate_safe_coulex_energy, reorientation_static_quadrupole, calculate_kumar_invariants
from tpsm_band_diagram_calculator import calculate_effective_moi_tpsm, generate_tpsm_band_diagram
from octupole_parity_doublet_calculator import calculate_parity_splitting, calculate_b_e1_over_b_e2, extract_intrinsic_dipole_moment, estimate_octupole_beta3
from signature_inversion_analyzer import calculate_staggering_parameter_s, calculate_signature_splitting, detect_inversion_crossing
from superdeformation_decayout_calculator import evaluate_superdeformation_flatness, model_decayout_tunneling


def cmd_kinematics(args):
    res = calculate_kinematics(args.Ap, args.Zp, args.At, args.Zt, args.Elab, args.dE)
    print("\n=======================================================")
    print(f" Heavy-Ion Fusion Kinematics: {args.Ap}X({args.Zp}) + {args.At}Y({args.Zt})")
    print("=======================================================")
    print(f"  Beam Energy (Lab)       : {res['Elab_MeV']:.2f} MeV")
    print(f"  Center-of-Mass Energy   : {res['E_cm_MeV']:.2f} MeV")
    print(f"  Bass Interaction Radius : {res['R_B_fm']:.3f} fm")
    print(f"  Coulomb Barrier (V_B)   : {res['V_B_MeV']:.2f} MeV")
    print(f"  E_cm / V_B Ratio        : {res['E_cm_over_VB']:.3f}")
    print(f"  Grazing Ang. Momentum   : {res['l_max_hbar']:.1f} hbar")
    print(f"  Total Fusion Cross Sec  : {res['sigma_fus_mb']:.1f} mb")
    print(f"  Recoil Velocity (beta)  : {res['beta_v_over_c']:.4f} ({res['recoil_velocity_percent_c']:.2f}% of c)")
    print("=======================================================")
    if args.Egamma:
        print(f"\nDoppler Shift for E_gamma = {args.Egamma:.1f} keV:")
        for th in [30, 45, 90, 135, 150]:
            shifted = doppler_shift(args.Egamma, res['beta_v_over_c'], th)
            dE = doppler_broadening(args.Egamma, res['beta_v_over_c'], th, args.opening_angle)
            print(f"  Theta = {th:3d} deg : E_shift = {shifted:8.2f} keV ({shifted-args.Egamma:+6.2f} keV), Broadening = {dE:5.2f} keV")


def cmd_dualroots(args):
    roots = solve_delta_dual_roots(args.a2, args.F11, args.F12, args.F22, alpha2=args.alpha2)
    print("\n=======================================================")
    print(f" Multipole Mixing Ratio delta Dual-Root Solution")
    print("=======================================================")
    print(f"  Experimental a2         : {args.a2:+.4f}")
    print(f"  Orientation alpha2      : {args.alpha2:.4f}")
    print(f"  F-coefficients (11,12,22): {args.F11:.4f}, {args.F12:.4f}, {args.F22:.4f}")
    if roots is None:
        print("  Status: No real roots exist for this a2 (unphysical or bad calibration).")
    else:
        d1 = roots["delta_small_root (M1 dominated)"]
        d2 = roots["delta_large_root (E2 dominated)"]
        e2_pct1 = 100.0 * (d1**2) / (1.0 + d1**2)
        e2_pct2 = 100.0 * (d2**2) / (1.0 + d2**2)
        print(f"  Root 1 (M1 dominated)   : delta = {d1:+.4f} (E2 fraction: {e2_pct1:.1f}%, M1 fraction: {100-e2_pct1:.1f}%)")
        print(f"  Root 2 (E2 dominated)   : delta = {d2:+.4f} (E2 fraction: {e2_pct2:.1f}%, M1 fraction: {100-e2_pct2:.1f}%)")
        print("\n  [EXPERT NOTICE]")
        print("  Both roots yield the EXACT SAME a2 value!")
        print("  Do NOT select Root 2 (wobbling) without independent Linear Polarization (P) measurement!")
    print("=======================================================")


def cmd_dco(args):
    res = joint_dco_polarization_fit(
        R_dco_exp=args.Rdco, R_dco_err=args.Rdco_err,
        P_exp=args.P, P_err=args.P_err,
        theta1_deg=args.th1, theta2_deg=args.th2, theta_pol_deg=args.th_pol,
        F2_11=args.F11, F2_12=args.F12, F2_22=args.F22, F4_22=args.F44,
        alpha2=args.alpha2
    )
    print("\n=======================================================")
    print(" Joint DCO Ratio & Linear Polarization Fit")
    print("=======================================================")
    print(f"  Input Exp R_DCO         : {args.Rdco:.3f} +/- {args.Rdco_err:.3f} (angles: {args.th1:.0f}/{args.th2:.0f} deg)")
    print(f"  Input Exp Polarization  : {args.P:+.3f} +/- {args.P_err:.3f} (at {args.th_pol:.0f} deg)")
    print(f"  Best-fit delta          : {res['best_delta']:+.4f} (+{res['delta_err_high']:.4f} / -{res['delta_err_low']:.4f})")
    print(f"  Model R_DCO at best-fit : {res['r_dco_theo']:.3f}")
    print(f"  Model Pol P at best-fit : {res['p_theo']:+.3f}")
    print(f"  Minimum Chi2            : {res['min_chi2']:.2f}")
    print("=======================================================")


def cmd_lifetime(args):
    alpha = calculate_stopping_time_alpha(args.A, args.Z, args.beta, args.stopper)
    print("\n=======================================================")
    print(f" Nuclear Excited-State Lifetime & DSAM Analysis")
    print("=======================================================")
    print(f"  Recoil Nucleus          : A={args.A}, Z={args.Z} (beta={args.beta:.4f})")
    print(f"  Stopper Material        : {args.stopper} (slowing-down time alpha = {alpha:.3f} ps)")
    if args.F is not None:
        tau = dsam_invert_lifetime(args.F, alpha)
        print(f"  Measured Attenuation F  : {args.F:.3f}")
        print(f"  Inverted Lifetime tau   : {tau:.3f} ps ({tau*1000.0:.1f} fs, T_1/2 = {tau*0.693147*1000.0:.1f} fs)")
    else:
        tau = args.tau
        print(f"  Input Lifetime tau      : {tau:.3f} ps")

    if args.Egamma:
        strengths = calculate_absolute_transition_strengths(
            tau_ps=tau, E_gamma_keV=args.Egamma, delta=args.delta,
            I_initial=args.I, branching_ratio=args.br
        )
        print("-------------------------------------------------------")
        print(f"  Gamma Transition Energy : {args.Egamma:.1f} keV (br = {args.br:.2f}, delta = {args.delta:+.2f})")
        print(f"  Absolute B(E2)          : {strengths['B_E2_e2b2']:.4f} e^2 b^2 ({strengths['B_E2_W_u']:.1f} W.u.)")
        print(f"  Absolute B(M1)          : {strengths['B_M1_muN2']:.4f} mu_N^2 ({strengths['B_M1_W_u']:.3f} W.u.)")
        print(f"  Intrinsic Quadrupole Qt : {strengths['Qt_eb']:.2f} e b")
    print("=======================================================")


def cmd_align(args):
    spins = [float(x.strip()) for x in args.spins.split(",")]
    energies = [float(x.strip()) for x in args.energies.split(",")]
    if len(spins) != len(energies):
        raise ValueError("Number of spins must equal number of energies.")

    res = calculate_alignment_and_routhians(spins, energies, J0=args.J0, J1=args.J1, K=args.K)
    print("\n=======================================================")
    print(" Nuclear Rotational Alignment & Routhian Analysis")
    print("=======================================================")
    print(f"  Harris Reference Core   : J0 = {args.J0:.1f} hbar^2/MeV, J1 = {args.J1:.1f} hbar^4/MeV^3, K = {args.K:.1f}")
    print("  Spin (hbar) | hbar*omega (MeV) | Alignment i_x (hbar) | e' (MeV)")
    print("  --------------------------------------------------------------")
    for sp, w, ix, ep in zip(res["spin_mid"], res["omega_MeV"], res["ix_hbar"], res["eprime_MeV"]):
        print(f"    {sp:5.1f}     |     {w:.4f}     |      {ix:+6.2f}        |  {ep:+.3f}")
    if res["critical_omega_crossing"]:
        print(f"\n  [BAND CROSSING DETECTED]")
        print(f"  Critical Frequency omega_c approx {res['critical_omega_crossing']:.3f} MeV/hbar")
        print(f"  Alignment Gain Delta(i_x) approx {res['alignment_gain']:.1f} hbar")
    print("=======================================================")


def cmd_ensdf(args):
    with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    levels = parse_ensdf_records(content)
    print("\n=======================================================")
    print(f" NNDC ENSDF Dataset Parser: {args.file}")
    print("=======================================================")
    print(f"  Successfully parsed {len(levels)} levels.")
    total_gammas = sum(len(l["gammas"]) for l in levels)
    print(f"  Total gamma transitions : {total_gammas}")

    if args.peaks:
        meas_peaks = [float(x.strip()) for x in args.peaks.split(",")]
        cw = crosswalk_match(meas_peaks, levels, tolerance_keV=args.tol)
        print(f"\n  Crosswalk Matched Known Transitions ({len(cw['matched'])}):")
        for m in cw["matched"]:
            print(f"    Exp {m['exp_energy_keV']:6.1f} keV <-> ENSDF {m['ensdf_energy_keV']:6.1f} keV (diff: {m['diff_keV']:+4.1f} keV), J_pi = {m['parent_jpi']}, Mult = {m['mult']}")
        print(f"\n  Unmatched New Transitions ({len(cw['unmatched_new_candidates'])}):")
        for u in cw["unmatched_new_candidates"]:
            print(f"    Candidate new peak: {u:6.1f} keV")
    print("=======================================================")


def cmd_yield2cs(args):
    cs = extract_cross_section_from_yield(
        peak_area=args.area, efficiency=args.eff, branching_ratio=args.br,
        beam_current_pnA=args.pnA, duration_hours=args.hours,
        target_thickness_mg_cm2=args.target_mg, target_mass_A=args.target_A,
        peak_area_err=args.area_err
    )
    print("\n=======================================================")
    print(" Experimental Yield -> Absolute Cross Section Inversion")
    print("=======================================================")
    print(f"  Integrated Projectiles  : {cs['N_projectiles']:.3e} ions")
    print(f"  Target Areal Density    : {cs['N_target_per_cm2']:.3e} nuclei/cm^2")
    print(f"  Absolute Cross Section  : {cs['sigma_mb']:.2f} +/- {cs['sigma_err_mb']:.2f} mb")
    print("=======================================================")


def cmd_shears(args):
    spins = [float(x.strip()) for x in args.spins.split(",")]
    prof = shears_band_profile(spins, args.jpi, args.jnu, B_E2_const_e2b2=args.BE2, g_pi=args.gpi, g_nu=args.gnu)
    print("\n=======================================================")
    print(" Magnetic Rotation Shears Mechanism Profile")
    print("=======================================================")
    print(f"  Configuration           : j_pi = {args.jpi:.1f}, j_nu = {args.jnu:.1f} (I_max = {args.jpi+args.jnu:.1f} hbar)")
    print(f"  Effective g-factors     : g_pi = {args.gpi:.2f}, g_nu = {args.gnu:.2f}, Core B(E2) = {args.BE2:.4f} e^2b^2")
    print("  Spin (hbar) | Shears Angle (deg) | B(M1) (mu_N^2) | B(M1)/B(E2)")
    print("  --------------------------------------------------------------")
    for sp, th, m1, rat in zip(prof['spins'], prof['theta_deg'], prof['B_M1_muN2'], prof['B_M1_over_B_E2']):
        print(f"    {sp:5.1f}     |      {th:5.1f}         |     {m1:5.2f}      |   {rat:6.1f}")
    print("=======================================================")


def cmd_e0(args):
    e0_res = extract_rho2_e0_from_lifetime(args.tau, args.Z, args.A, args.dE, branching_ratio=args.br)
    print("\n=======================================================")
    print(" Nuclear Electric Monopole (E0) & Shape Coexistence")
    print("=======================================================")
    print(f"  Nucleus (Z, A)          : Z={args.Z}, A={args.A}")
    print(f"  Transition Energy (dE)  : {args.dE:.1f} keV (lifetime tau = {args.tau:.1f} ps, br = {args.br:.2f})")
    print(f"  Electronic Omega_K(E0)  : {e0_res['Omega_K_s^-1']:.2e} s^-1")
    print(f"  Reduced Monopole rho^2  : {e0_res['rho2']:.4e} (rho^2 * 10^3 = {e0_res['rho2_x1000']:.2f})")

    mix = invert_two_state_mixing(0.0, args.dE, e0_res['rho2'], args.Z, beta1=args.beta1)
    print("-------------------------------------------------------")
    print("  Two-State Mixing Model Inversion:")
    print(f"    Coupling Matrix V_mix : {mix['V_mix_keV']:.1f} keV (Unperturbed gap = {mix['unperturbed_gap_keV']:.1f} keV)")
    print(f"    Coexisting Shapes     : State 1 (beta = {mix['beta1']:.2f}) <-> State 2 (beta = {mix['beta2']:.2f})")
    print(f"    Deformation Jump      : Delta(beta) = {mix['delta_beta']:+.2f}")
    print("=======================================================")


def cmd_moi(args):
    gammas = [float(x.strip()) for x in args.gammas.split(",")]
    data = calculate_moments_of_inertia(gammas, initial_spin=args.spin)
    print("\n=======================================================")
    print(" Moments of Inertia (J1, J2) & Spin Inversion Analysis")
    print("=======================================================")
    print(f"  Input Cascade Gammas    : {len(gammas)} transitions ({gammas[0]:.1f} -> {gammas[-1]:.1f} keV)")
    if args.spin is not None:
        print(f"  Initial State Spin      : I = {args.spin:.1f} hbar")
        print("  E_gamma (keV) | Delta_Eg (keV) | hbar*w (MeV) | J2 (hbar^2/MeV) | J1 (hbar^2/MeV)")
        print("  -----------------------------------------------------------------------------")
        for i in range(len(data['delta_E_gamma_keV'])):
            print(f"    {data['gamma_energies_keV'][i]:7.1f}     |     {data['delta_E_gamma_keV'][i]:6.1f}     |    {data['omega_mid_MeV'][i]:.4f}    |     {data['J2_dynamical_hbar2_per_MeV'][i]:5.1f}       |     {data['J1_kinematical_hbar2_per_MeV'][i]:5.1f}")
    else:
        print("  Initial Spin Unknown -> Displaying Dynamical Moment of Inertia J2 only:")
        print("  E_gamma (keV) | Delta_Eg (keV) | hbar*w (MeV) | J2 (hbar^2/MeV)")
        print("  --------------------------------------------------------------")
        for i in range(len(data['delta_E_gamma_keV'])):
            print(f"    {data['gamma_energies_keV'][i]:7.1f}     |     {data['delta_E_gamma_keV'][i]:6.1f}     |    {data['omega_mid_MeV'][i]:.4f}    |     {data['J2_dynamical_hbar2_per_MeV'][i]:5.1f}")

        inv = invert_floating_band_spin(gammas, is_half_integer=args.half_int, J0_expected=args.J0)
        print(f"\n  [INVERTED CANDIDATE BANDHEAD SPIN]")
        print(f"  Most Likely Spin I0     : {inv['best_candidate_spin_I0']} hbar (Optimization Score: {inv['min_score']:.2f})")
    print("=======================================================")


def cmd_coulex(args):
    safe = calculate_safe_coulex_energy(args.Ap, args.Zp, args.At, args.Zt, d_safe_fm=args.dsafe)
    print("\n=======================================================")
    print(" Coulomb Excitation (Coulex) Kinematics & Invariants")
    print("=======================================================")
    print(f"  Projectile : A={args.Ap}, Z={args.Zp}  --> Target: A={args.At}, Z={args.Zt}")
    print(f"  Safe Surface Distance   : d_min = {safe['d_min_fm']:.2f} fm (margin = {args.dsafe:.1f} fm)")
    print(f"  Max Safe Energy (Lab)   : E_lab_safe = {safe['E_lab_safe_MeV']:.1f} MeV (E_cm = {safe['E_cm_safe_MeV']:.1f} MeV)")

    if args.M22 is not None:
        reorient = reorientation_static_quadrupole(args.Zt, args.At, args.M22)
        print("-------------------------------------------------------")
        print(f"  Reorientation Matrix <2||M(E2)||2> : {args.M22:+.3f} e*b")
        print(f"  Static Quadrupole Moment Q_s(2_1+) : {reorient['Q_s_eb']:+.3f} e*b")
        print(f"  Polarity Diagnostic                : {reorient['shape_polarity']}")

    if args.M02:
        m02_vals = [float(x.strip()) for x in args.M02.split(",")]
        m22_val = args.M22 if args.M22 is not None else 0.0
        inv = calculate_kumar_invariants(m02_vals, m22_val, args.Zt, args.At)
        print("-------------------------------------------------------")
        print(f"  Kumar Quadrupole Invariant Q^2     : {inv['q2_invariant_e2b2']:.3f} e^2 b^2")
        print(f"  Asymmetry Invariant cos(3*delta)   : {inv['cos_3delta']:+.3f}")
        print(f"  Effective Triaxial Angle gamma_eff : {inv['gamma_eff_deg']:.1f} deg")
        print(f"  Effective RMS Deformation beta_eff : {inv['beta_eff_rms']:.3f}")
    print("=======================================================")


def cmd_tpsm(args):
    spins = [float(x.strip()) for x in args.spins.split(",")]
    diag = generate_tpsm_band_diagram(spins, epsilon2=args.eps2, gamma_deg=args.gamma, A=args.A)
    print("\n=======================================================")
    print(" Triaxial Projected Shell Model (TPSM) Band Diagram")
    print("=======================================================")
    print(f"  Mass Number A={args.A}, Deformation eps2={args.eps2:.2f}, gamma={args.gamma:.1f} deg")
    print(f"  TPSM Core J_eff         : {diag['J_eff_core']:.2f} hbar^2/MeV (S-band J_eff: {diag['J_eff_sband']:.2f})")
    print("  Spin (hbar) | E_gband (keV) | E_sband (keV) | Favored Yrast")
    print("  -------------------------------------------------------------")
    for sp, eg, es in zip(diag['spins'], diag['E_gband_keV'], diag['E_sband_keV']):
        fav = "g-band" if eg <= es else "s-band (ALIGNED)"
        print(f"     {sp:4.0f}     |    {eg:7.1f}    |    {es:7.1f}    |  {fav}")
    if diag['crossing_spin_Ic']:
        print(f"\n  [MICRO-CROSSING DETECTED]")
        print(f"  Backbending Critical Spin I_c approx {diag['crossing_spin_Ic']:.1f} hbar")
    print("=======================================================")


def cmd_octupole(args):
    print("\n=======================================================")
    print(" Octupole Parity Doublets & Intrinsic Dipole Moment")
    print("=======================================================")
    if args.pos_spins and args.neg_spins:
        p_spins = [float(x.strip()) for x in args.pos_spins.split(",")]
        p_energies = [float(x.strip()) for x in args.pos_energies.split(",")]
        n_spins = [float(x.strip()) for x in args.neg_spins.split(",")]
        n_energies = [float(x.strip()) for x in args.neg_energies.split(",")]
        splits = calculate_parity_splitting(p_spins, p_energies, n_spins, n_energies)
        print("  Parity Splitting Displacement delta_E(I):")
        print("    Spin I- (hbar) | E(I-) (keV) | E_pos_avg (keV) | delta_E (keV)")
        print("    ----------------------------------------------------------")
        for s in splits:
            print(f"         {s['spin_neg']:2.0f}        |   {s['E_neg_keV']:7.1f}   |     {s['E_pos_avg_keV']:7.1f}     |   {s['delta_E_keV']:+6.1f}")

    if args.E1 and args.E2 and args.IE1 and args.IE2:
        ratios = calculate_b_e1_over_b_e2(args.E1, args.IE1, args.E2, args.IE2)
        d0 = extract_intrinsic_dipole_moment(ratios["B_E1_over_B_E2_fm2"], I_initial=args.I, Qt_eb=args.Qt)
        b3 = estimate_octupole_beta3(d0, args.Z, args.A, beta2=args.beta2)
        print("-------------------------------------------------------")
        print(f"  Branching Ratio B(E1)/B(E2) : {ratios['B_E1_over_B_E2_10m4_fm2']:.4f} x 10^-4 fm^-2")
        print(f"  Inverted Dipole Moment D0   : {d0:.3f} e*fm")
        print(f"  Estimated Octupole beta3    : {b3:.3f}")
    print("=======================================================")


def cmd_inversion(args):
    f_spins = [float(x.strip()) for x in args.fav_spins.split(",")]
    f_energies = [float(x.strip()) for x in args.fav_energies.split(",")]
    u_spins = [float(x.strip()) for x in args.unfav_spins.split(",")]
    u_energies = [float(x.strip()) for x in args.unfav_energies.split(",")]

    splits = calculate_signature_splitting(f_spins, f_energies, u_spins, u_energies)
    diag = detect_inversion_crossing(splits)

    print("\n=======================================================")
    print(" Signature Splitting & Inversion Diagnostic")
    print("=======================================================")
    print(f"  Favored Band Sequence   : {len(f_spins)} states ({f_spins[0]:.1f} -> {f_spins[-1]:.1f})")
    print(f"  Unfavored Band Sequence : {len(u_spins)} states ({u_spins[0]:.1f} -> {u_spins[-1]:.1f})")
    print("  Spin (hbar) | E_unfav (keV) | E_fav_interp (keV) | Delta_E (keV) | Status")
    print("  -------------------------------------------------------------------------")
    for s in splits:
        stat = "INVERTED (Anomalous)" if s['is_inverted'] else "Normal"
        print(f"    {s['spin']:5.1f}     |   {s['E_unfav_keV']:7.1f}   |      {s['E_fav_interp_keV']:7.1f}       |    {s['delta_E_keV']:+6.1f}   | {stat}")
    print("-------------------------------------------------------")
    print(f"  Has Signature Inversion : {diag['has_inversion']}")
    if diag['has_inversion']:
        print(f"  Max Inversion Depth     : {diag['max_inversion_depth_keV']:.1f} keV")
        if diag['I_inv']:
            print(f"  Crossing Spin I_inv     : approx {diag['I_inv']:.1f} hbar")
        print("  Physical Interpretation : Clear fingerprint of triaxial gamma deformation and strong p-n interaction!")
    print("=======================================================")


def cmd_sd(args):
    gammas = [float(x.strip()) for x in args.gammas.split(",")]
    flat = evaluate_superdeformation_flatness(gammas)
    print("\n=======================================================")
    print(" Superdeformation (SD/HD/TSD) Plateau & Decay-Out")
    print("=======================================================")
    print(f"  Input Cascade           : {len(gammas)} transitions ({gammas[0]:.1f} -> {gammas[-1]:.1f} keV)")
    print(f"  Mean J2 Moment of Inert : {flat['mean_J2_hbar2_per_MeV']:.2f} hbar^2/MeV (std = {flat['std_J2']:.2f})")
    print(f"  J2 Relative Std (RSD)   : {flat['relative_std_percent']:.2f}%")
    print(f"  Plateau Classification  : {flat['classification']}")

    if args.spins and args.intensities:
        s_arr = [float(x.strip()) for x in args.spins.split(",")]
        i_arr = [float(x.strip()) for x in args.intensities.split(",")]
        dec = model_decayout_tunneling(s_arr, i_arr, gammas[:len(s_arr)], Qt_sd_eb=args.Qt)
        print("-------------------------------------------------------")
        print(f"  Critical Decay-out Spin : I_decay = {dec['I_decay']:.1f} hbar (E_decay = {dec['E_decay_keV']:.1f} keV)")
        print(f"  In-band SD B(E2)        : {dec['in_band_B_E2_eb2']:.2f} e^2 b^2 (Qt = {args.Qt:.1f} e*b)")
        print(f"  Estimated Tunnel Width  : Gamma_tunnel = {dec['estimated_Gamma_tunnel_eV']:.2e} eV")
    print("=======================================================")


def cmd_selftest(args):
    print("\nExecuting comprehensive test suite...")
    ret = os.system(f"{sys.executable} system/scripts/analysis/test_analysis_suite.py")
    if ret != 0:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Nuclear Physics Spectroscopy Analysis Suite")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Kinematics
    p_kin = subparsers.add_parser("kinematics", help="Heavy-ion fusion kinematics")
    p_kin.add_argument("--Ap", type=int, required=True, help="Projectile mass number")
    p_kin.add_argument("--Zp", type=int, required=True, help="Projectile charge number")
    p_kin.add_argument("--At", type=int, required=True, help="Target mass number")
    p_kin.add_argument("--Zt", type=int, required=True, help="Target charge number")
    p_kin.add_argument("--Elab", type=float, required=True, help="Lab beam energy (MeV)")
    p_kin.add_argument("--dE", type=float, default=0.0, help="Target energy loss (MeV)")
    p_kin.add_argument("--Egamma", type=float, default=1000.0, help="Gamma energy for Doppler test (keV)")
    p_kin.add_argument("--opening_angle", type=float, default=8.0, help="Detector half-opening angle (deg)")
    p_kin.set_defaults(func=cmd_kinematics)

    # Dual roots
    p_dual = subparsers.add_parser("dualroots", help="Solve delta dual roots")
    p_dual.add_argument("--a2", type=float, required=True, help="Fitted a2 coefficient")
    p_dual.add_argument("--F11", type=float, required=True, help="F2(L=1, L=1)")
    p_dual.add_argument("--F12", type=float, required=True, help="F2(L=1, L=2)")
    p_dual.add_argument("--F22", type=float, required=True, help="F2(L=2, L=2)")
    p_dual.add_argument("--alpha2", type=float, default=1.0, help="Orientation parameter B2/B0")
    p_dual.set_defaults(func=cmd_dualroots)

    # DCO & Polarization
    p_dco = subparsers.add_parser("dco", help="Joint DCO ratio and linear polarization fit")
    p_dco.add_argument("--Rdco", type=float, required=True, help="Measured DCO ratio")
    p_dco.add_argument("--Rdco_err", type=float, default=0.05, help="DCO ratio error")
    p_dco.add_argument("--P", type=float, required=True, help="Measured linear polarization degree")
    p_dco.add_argument("--P_err", type=float, default=0.05, help="Polarization error")
    p_dco.add_argument("--th1", type=float, default=30.0, help="Detector 1 angle (deg)")
    p_dco.add_argument("--th2", type=float, default=90.0, help="Detector 2 angle (deg)")
    p_dco.add_argument("--th_pol", type=float, default=90.0, help="Polarimeter angle (deg)")
    p_dco.add_argument("--F11", type=float, required=True, help="F2(11)")
    p_dco.add_argument("--F12", type=float, required=True, help="F2(12)")
    p_dco.add_argument("--F22", type=float, required=True, help="F2(22)")
    p_dco.add_argument("--F44", type=float, default=0.0, help="F4(22)")
    p_dco.add_argument("--alpha2", type=float, default=0.85, help="Alignment parameter")
    p_dco.set_defaults(func=cmd_dco)

    # Lifetime & DSAM
    p_life = subparsers.add_parser("lifetime", help="Excited state lifetime and DSAM stopping analysis")
    p_life.add_argument("--A", type=int, default=131, help="Recoil mass number")
    p_life.add_argument("--Z", type=int, default=58, help="Recoil atomic number")
    p_life.add_argument("--beta", type=float, default=0.025, help="Initial recoil velocity v/c")
    p_life.add_argument("--stopper", type=str, default="Au", help="Stopper foil material (Au, Pb, Ta)")
    p_life.add_argument("--F", type=float, default=None, help="Measured DSAM attenuation factor F(tau)")
    p_life.add_argument("--tau", type=float, default=1.0, help="Lifetime tau in ps (if F is not provided)")
    p_life.add_argument("--Egamma", type=float, default=None, help="Gamma energy (keV)")
    p_life.add_argument("--delta", type=float, default=100.0, help="Mixing ratio delta (E2/M1)")
    p_life.add_argument("--I", type=float, default=10.0, help="Initial state spin")
    p_life.add_argument("--br", type=float, default=1.0, help="Gamma branching ratio")
    p_life.set_defaults(func=cmd_lifetime)

    # Rotational Alignment & Routhian
    p_align = subparsers.add_parser("align", help="Rotational frequency, alignment i_x, and Routhians")
    p_align.add_argument("--spins", type=str, required=True, help="Comma-separated list of spins (e.g. 5.5,7.5,9.5,11.5)")
    p_align.add_argument("--energies", type=str, required=True, help="Comma-separated list of energies in keV (e.g. 0,350,800,1350)")
    p_align.add_argument("--J0", type=float, default=15.0, help="Harris core parameter J0")
    p_align.add_argument("--J1", type=float, default=30.0, help="Harris core parameter J1")
    p_align.add_argument("--K", type=float, default=0.0, help="K quantum number")
    p_align.set_defaults(func=cmd_align)

    # ENSDF Crosswalk
    p_ensdf = subparsers.add_parser("ensdf", help="Parse ENSDF file and crosswalk match experimental gamma peaks")
    p_ensdf.add_argument("--file", type=str, required=True, help="Path to ENSDF text file")
    p_ensdf.add_argument("--peaks", type=str, default="", help="Comma-separated experimental peak energies in keV")
    p_ensdf.add_argument("--tol", type=float, default=1.0, help="Energy matching tolerance (keV)")
    p_ensdf.set_defaults(func=cmd_ensdf)

    # Yield to Cross Section Inverter
    p_y2c = subparsers.add_parser("yield2cs", help="Invert peak counts to absolute cross section (mb)")
    p_y2c.add_argument("--area", type=float, required=True, help="Net peak area counts")
    p_y2c.add_argument("--area_err", type=float, default=None, help="Peak area error")
    p_y2c.add_argument("--eff", type=float, required=True, help="Detector array peak efficiency")
    p_y2c.add_argument("--br", type=float, default=1.0, help="Gamma emission branching ratio")
    p_y2c.add_argument("--pnA", type=float, required=True, help="Beam current in pnA")
    p_y2c.add_argument("--hours", type=float, required=True, help="Beam irradiation duration in hours")
    p_y2c.add_argument("--target_mg", type=float, required=True, help="Target thickness in mg/cm^2")
    p_y2c.add_argument("--target_A", type=float, required=True, help="Target mass number A")
    p_y2c.set_defaults(func=cmd_yield2cs)

    # Shears Mechanism Magnetic Rotation
    p_shears = subparsers.add_parser("shears", help="Shears mechanism angle, B(M1) and B(M1)/B(E2) profile")
    p_shears.add_argument("--spins", type=str, required=True, help="Comma-separated list of spins")
    p_shears.add_argument("--jpi", type=float, required=True, help="Proton blade angular momentum j_pi")
    p_shears.add_argument("--jnu", type=float, required=True, help="Neutron blade angular momentum j_nu")
    p_shears.add_argument("--BE2", type=float, default=0.03, help="Assumed constant B(E2) in e^2b^2")
    p_shears.add_argument("--gpi", type=float, default=1.25, help="Proton g-factor")
    p_shears.add_argument("--gnu", type=float, default=-0.25, help="Neutron g-factor")
    p_shears.set_defaults(func=cmd_shears)

    # Electric Monopole E0 & Shape Coexistence
    p_e0 = subparsers.add_parser("e0", help="Electric monopole E0 strength rho^2 and shape coexistence mixing")
    p_e0.add_argument("--Z", type=int, required=True, help="Atomic number Z")
    p_e0.add_argument("--A", type=int, required=True, help="Mass number A")
    p_e0.add_argument("--dE", type=float, required=True, help="Transition energy in keV")
    p_e0.add_argument("--tau", type=float, required=True, help="State lifetime in ps")
    p_e0.add_argument("--br", type=float, default=1.0, help="E0 branching ratio")
    p_e0.add_argument("--beta1", type=float, default=0.15, help="Assumed deformation of State 1")
    p_e0.set_defaults(func=cmd_e0)

    # Moments of Inertia & Spin Inversion
    p_moi = subparsers.add_parser("moi", help="Kinematical J1, dynamical J2 moments of inertia and floating band spin inversion")
    p_moi.add_argument("--gammas", type=str, required=True, help="Comma-separated cascade gamma energies in keV")
    p_moi.add_argument("--spin", type=float, default=None, help="Decaying state spin of first gamma (if known)")
    p_moi.add_argument("--half_int", action="store_true", default=True, help="Grid search half-integer spins for odd-A nuclei")
    p_moi.add_argument("--J0", type=float, default=15.0, help="Expected bandhead core J0")
    p_moi.set_defaults(func=cmd_moi)

    # Coulomb Excitation & Kumar Invariants
    p_coulex = subparsers.add_parser("coulex", help="Coulomb excitation safe energy, reorientation Q_s, and Kumar invariants")
    p_coulex.add_argument("--Ap", type=int, required=True, help="Projectile mass number")
    p_coulex.add_argument("--Zp", type=int, required=True, help="Projectile atomic number")
    p_coulex.add_argument("--At", type=int, required=True, help="Target mass number")
    p_coulex.add_argument("--Zt", type=int, required=True, help="Target atomic number")
    p_coulex.add_argument("--dsafe", type=float, default=5.0, help="Cline safe distance margin (default 5.0 fm)")
    p_coulex.add_argument("--M22", type=float, default=None, help="Diagonal matrix element <2||M(E2)||2> in e*b")
    p_coulex.add_argument("--M02", type=str, default="", help="Comma-separated transitional <0||M(E2)||2_i> in e*b")
    p_coulex.set_defaults(func=cmd_coulex)

    # Triaxial Projected Shell Model Band Diagram
    p_tpsm = subparsers.add_parser("tpsm", help="TPSM microscopic band diagram, crossing spin Ic, and alignment")
    p_tpsm.add_argument("--spins", type=str, default="0,2,4,6,8,10,12,14,16,18,20", help="Comma-separated list of spins")
    p_tpsm.add_argument("--eps2", type=float, default=0.22, help="Quadrupole deformation epsilon2")
    p_tpsm.add_argument("--gamma", type=float, default=25.0, help="Triaxial angle gamma (deg)")
    p_tpsm.add_argument("--A", type=int, default=132, help="Nuclear mass number A")
    p_tpsm.set_defaults(func=cmd_tpsm)

    # Octupole Parity Doublets & D0
    p_oct = subparsers.add_parser("octupole", help="Parity doublet splitting, B(E1)/B(E2), and intrinsic dipole D0")
    p_oct.add_argument("--pos_spins", type=str, default="", help="Positive parity band spins")
    p_oct.add_argument("--pos_energies", type=str, default="", help="Positive parity band energies in keV")
    p_oct.add_argument("--neg_spins", type=str, default="", help="Negative parity band spins")
    p_oct.add_argument("--neg_energies", type=str, default="", help="Negative parity band energies in keV")
    p_oct.add_argument("--E1", type=float, default=None, help="E1 transition energy (keV)")
    p_oct.add_argument("--IE1", type=float, default=None, help="E1 peak intensity")
    p_oct.add_argument("--E2", type=float, default=None, help="E2 crossover energy (keV)")
    p_oct.add_argument("--IE2", type=float, default=None, help="E2 peak intensity")
    p_oct.add_argument("--I", type=float, default=7.0, help="Decaying state spin")
    p_oct.add_argument("--Qt", type=float, default=3.5, help="Intrinsic quadrupole moment Qt in e*b")
    p_oct.add_argument("--Z", type=int, default=58, help="Atomic number Z")
    p_oct.add_argument("--A", type=int, default=146, help="Mass number A")
    p_oct.add_argument("--beta2", type=float, default=0.22, help="Quadrupole deformation beta2")
    p_oct.set_defaults(func=cmd_octupole)

    # Signature Inversion & Splitting
    p_inv = subparsers.add_parser("inversion", help="Signature splitting Delta_E(I), staggering S(I), and inversion crossing")
    p_inv.add_argument("--fav_spins", type=str, required=True, help="Favored band spins (e.g. 8,10,12,14,16)")
    p_inv.add_argument("--fav_energies", type=str, required=True, help="Favored band energies in keV")
    p_inv.add_argument("--unfav_spins", type=str, required=True, help="Unfavored band spins (e.g. 9,11,13,15)")
    p_inv.add_argument("--unfav_energies", type=str, required=True, help="Unfavored band energies in keV")
    p_inv.set_defaults(func=cmd_inversion)

    # Superdeformation & Decay-Out
    p_sd = subparsers.add_parser("sd", help="Superdeformation J2 plateau flatness and decay-out tunneling")
    p_sd.add_argument("--gammas", type=str, required=True, help="Comma-separated list of cascade gamma energies in keV")
    p_sd.add_argument("--spins", type=str, default="", help="Comma-separated list of spins corresponding to low transitions")
    p_sd.add_argument("--intensities", type=str, default="", help="Relative cascade intensities (e.g. 0.05,0.4,0.9,1.0)")
    p_sd.add_argument("--Qt", type=float, default=7.5, help="Assumed SD transition quadrupole moment Qt in e*b")
    p_sd.set_defaults(func=cmd_sd)

    # Selftest
    p_test = subparsers.add_parser("selftest", help="Run regression test suite")
    p_test.set_defaults(func=cmd_selftest)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
