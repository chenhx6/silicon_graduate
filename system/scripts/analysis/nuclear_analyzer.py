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
from ibm_dynamical_symmetry_analyzer import calculate_ibm_energy_ratios, classify_casten_triangle_phase
from ado_polarization_joint_analyzer import calculate_ado_ratio, convert_clover_counts_to_polarization, joint_ado_polarization_scan
from side_feeding_deconvolution_calculator import calculate_effective_f_factor, deconvolve_side_feeding_lifetime
from internal_conversion_bricc_calculator import calculate_bricc_icc, calculate_mixed_icc, correct_gamma_intensity_for_conversion, discriminate_multipolarity
from vacuum_deorientation_calculator import calculate_attenuation_factors, correct_measured_angular_distribution
from tidal_wave_dynamics_calculator import calculate_tidal_wave_kinematics, test_b_e2_linear_scaling, reconstruct_dynamic_beta2
from gamow_teller_ikeda_quenching_calculator import calculate_ikeda_sum_rule, evaluate_ga_quenching, convert_cross_section_to_b_gt
from halo_breakup_momentum_calculator import calculate_hansen_jonson_fwhm, invert_separation_energy_from_fwhm, calculate_goldhaber_width, diagnose_halo_signature, calculate_cluster_soft_e1_sum_rule, estimate_matter_radius_from_reaction_cross_section
from fission_barrier_superheavy_calculator import calculate_liquid_drop_fissility, calculate_hill_wheeler_penetration, calculate_gamma_n_over_gamma_f, estimate_superheavy_cross_section
from oslo_method_nld_gsf_analyzer import calculate_rho_at_sn, verify_oslo_lie_transformation_invariance, calibrate_oslo_nld_and_gsf, diagnose_low_energy_enhancement
from band_termination_cns_calculator import calculate_valence_maximum_spin, model_transition_quadrupole_collapse, calculate_rigid_rotor_subtraction, calculate_dynamic_moment_of_inertia_j2, diagnose_smooth_band_termination
from tdpad_hyperfine_precession_calculator import calculate_larmor_frequency, invert_g_factor_from_period, generate_tdpad_r_of_t, calculate_three_vector_chiral_gfactor, calculate_electric_quadrupole_frequency
from pairing_gap_separation_energy_calculator import calculate_s2n_series, calculate_pairing_gap_3point, calculate_pairing_gap_5point, detect_shell_closure_drop, detect_shape_transition_anomaly, compare_empirical_bcs_gap
from isgmr_breathing_mode_incompressibility_calculator import calculate_ka_from_isgmr_energy, leptodermous_expansion_ka, model_deformation_splitting_two_state, calculate_qpvc_self_energy_shift, diagnose_incompressibility_status
from relativistic_coulex_virtual_photon_calculator import calculate_relativistic_coulex_kinematics, calculate_virtual_photon_numbers, calculate_relativistic_e2_coulex_cross_section, invert_b_e2_from_coulex_cross_section, transform_gamma_angular_distribution_lorentz
from electromagnetic_transition_alaga_calculator import calculate_weisskopf_unit, convert_lifetime_to_b_e2, calculate_alaga_ratio_e2, calculate_bm1_over_be2


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


def cmd_ibm(args):
    ratios = calculate_ibm_energy_ratios(args.E21, args.E41, E_0_2_keV=args.E02, E_2_2_keV=args.E22)
    phase = classify_casten_triangle_phase(ratios['R42'], ratios['R22'])
    print("\n=======================================================")
    print(" IBM Symmetry & Casten Triangle Phase Classifier")
    print("=======================================================")
    print(f"  Input Level Energies    : E(2_1+) = {args.E21:.1f} keV, E(4_1+) = {args.E41:.1f} keV")
    if args.E22:
        print(f"                            E(2_2+) = {args.E22:.1f} keV")
    if args.E02:
        print(f"                            E(0_2+) = {args.E02:.1f} keV")
    print("-------------------------------------------------------")
    print(f"  Energy Ratio R4/2       : {ratios['R42']:.3f} (U(5)=2.00, O(6)=2.50, SU(3)=3.33)")
    if ratios['R22']:
        print(f"  Energy Ratio R22/21     : {ratios['R22']:.3f}")
    if ratios['O6_degeneracy_diff'] is not None:
        print(f"  |E(4_1) - E(2_2)| / E(2): {ratios['O6_degeneracy_diff']:.3f}")
    print("-------------------------------------------------------")
    print(f"  Classified Phase        : {phase['phase_name']}")
    print(f"  Description             : {phase['description']}")
    print("=======================================================")


def cmd_ado(args):
    print("\n=======================================================")
    print(" In-Beam ADO Ratio & Linear Polarization Joint Fit")
    print("=======================================================")
    pol_P = args.P
    pol_err = args.P_err
    if args.Nperp and args.Npar:
        clov = convert_clover_counts_to_polarization(args.Nperp, args.Npar, Q_factor=args.Q)
        pol_P = clov['polarization_P']
        pol_err = clov['polarization_P_err']
        print(f"  Clover Asymmetry Delta  : {clov['asymmetry_Delta']:+.3f} +/- {clov['asymmetry_err']:.3f}")
        print(f"  Deduced Polarization P : {pol_P:+.3f} +/- {pol_err:.3f}")
        print("-------------------------------------------------------")

    res = joint_ado_polarization_scan(
        R_ado_exp=args.Rado, R_ado_err=args.Rado_err,
        P_exp=pol_P, P_err=pol_err,
        theta1_deg=args.th1, theta2_deg=args.th2,
        F2_11=args.F11, F2_12=args.F12, F2_22=args.F22, F4_22=args.F44,
        alpha2=args.alpha2
    )
    print(f"  Exp ADO Ratio ({args.th1:.0f}/{args.th2:.0f}) : {args.Rado:.3f} +/- {args.Rado_err:.3f}")
    print(f"  Exp Linear Polarization : {pol_P:+.3f} +/- {pol_err:.3f}")
    print(f"  Best-fit delta          : {res['best_delta']:+.3f} (+{res['delta_err_high']:.3f} / -{res['delta_err_low']:.3f})")
    print(f"  Theoretical R_ADO       : {res['r_ado_at_best']:.3f}")
    print(f"  Theoretical Pol P       : {res['p_at_best']:+.3f}")
    print(f"  Joint Chi2 Minimum      : {res['min_chi2']:.2f}")
    print("=======================================================")


def cmd_feed(args):
    res = deconvolve_side_feeding_lifetime(args.F, args.tau_feed, args.f_feed, args.alpha)
    print("\n=======================================================")
    print(" DSAM Side-Feeding Lifetime Deconvolution")
    print("=======================================================")
    print(f"  Measured Attenuation F  : {res['F_measured']:.3f} (Stopper alpha = {args.alpha:.2f} ps)")
    print(f"  Side-Feeding Fraction   : {res['f_feed']*100:.1f}%")
    print(f"  Side-Feeding Time Delay : {res['tau_feed_ps']:.3f} ps ({res['tau_feed_ps']*1000:.0f} fs)")
    print("-------------------------------------------------------")
    print(f"  Apparent Lifetime       : {res['tau_apparent_ps']:.3f} ps ({res['tau_apparent_ps']*1000:.1f} fs)  [INFLATED]")
    print(f"  True Intrinsic Lifetime : {res['tau_intrinsic_ps']:.3f} ps ({res['tau_intrinsic_ps']*1000:.1f} fs)  [CORRECTED]")
    print(f"  Lifetime Bias Ratio     : {res['lifetime_overestimation_ratio']:.2f}x")
    print(f"  Resulting Qt Correction : Quadrupole moment was underestimated by {res['Qt_underestimation_percent']:.1f}%")
    print("=======================================================")


def cmd_icc(args):
    print("\n=======================================================")
    print(" Nuclear Internal Conversion (ICC / BrIcc) Analysis")
    print("=======================================================")
    print(f"  Target Nucleus Z={args.Z}, Gamma Transition E = {args.Egamma:.1f} keV")
    if args.delta is not None and abs(args.delta) > 1e-4:
        mixed = calculate_mixed_icc(args.Z, args.Egamma, args.delta)
        print(f"  M1 + E2 Mixed Transition (delta = {args.delta:+.3f}):")
        print(f"    alpha_K(mixed)        : {mixed['alpha_K_mixed']:.4f}")
        print(f"    alpha_tot(mixed)      : {mixed['alpha_total_mixed']:.4f}  [BrIcc Parameterized]")
        print(f"    Pure alpha_tot(M1)    : {mixed['alpha_tot_M1']:.4f}")
        print(f"    Pure alpha_tot(E2)    : {mixed['alpha_tot_E2']:.4f}")
    else:
        res = calculate_bricc_icc(args.Z, args.Egamma, args.mult)
        print(f"  Single Multipolarity: {res['multipolarity']}")
        print(f"    K-Shell Binding B_K   : {res['B_K_binding_keV']:.2f} keV")
        print(f"    Theoretical alpha_K   : {res['alpha_K']:.4f}")
        print(f"    Theoretical alpha_tot : {res['alpha_total']:.4f}")

    if args.Igamma:
        corr = correct_gamma_intensity_for_conversion(args.Igamma, args.Z, args.Egamma, delta=args.delta if args.delta else 0.0, multipolarity=args.mult)
        print("-------------------------------------------------------")
        print(f"  Intensity Correction:")
        print(f"    Observed I_gamma      : {corr['I_gamma']:.1f}")
        print(f"    Total Transition I_tot: {corr['I_total_transition']:.1f} ({corr['conversion_multiplier']:.3f}x multiplier)")
    print("=======================================================")


def cmd_deorient(args):
    att = calculate_attenuation_factors(args.tau, args.Z, args.beta, g_factor=args.g, tau_r_ps=args.taur)
    print("\n=======================================================")
    print(" In-Beam Vacuum Deorientation & Attenuation Correction")
    print("=======================================================")
    print(f"  Recoil Ion (Z={args.Z}, beta={args.beta:.4f}), Level Lifetime tau = {args.tau:.1f} ps")
    print(f"  Estimated Hyperfine B_hf: {att['B_hf_Tesla']:.1f} Tesla (omega_L = {att['omega_L_per_ps']:.4f} rad/ps)")
    print(f"  Attenuation Factors     : G2(tau) = {att['G2']:.3f}, G4(tau) = {att['G4']:.3f}")

    if args.a2 is not None:
        a4_val = args.a4 if args.a4 is not None else 0.0
        corr = correct_measured_angular_distribution(args.a2, a4_val, att['G2'], att['G4'], a2_err=args.a2_err, a4_err=args.a4_err)
        print("-------------------------------------------------------")
        print(f"  Measured a2 (Suppressed): {args.a2:+.3f}" + (f" +/- {args.a2_err:.3f}" if args.a2_err else ""))
        print(f"  Restored True Intrinsic : A2_true = {corr['A2_true']:+.3f}" + (f" +/- {corr['A2_err']:.3f}" if corr['A2_err'] else ""))
        print(f"  Deorientation Multiplier: {corr['G2_correction_factor']:.2f}x")
    print("=======================================================")


def cmd_tidal(args):
    spins = [float(x.strip()) for x in args.spins.split(",")]
    b_values = [float(x.strip()) for x in args.be2.split(",")]
    if len(spins) != len(b_values):
        raise ValueError("Number of spins must equal number of B(E2) values.")

    scaling = test_b_e2_linear_scaling(spins, b_values)
    dyn = reconstruct_dynamic_beta2(spins, b_values, args.Z, args.A)

    print("\n=======================================================")
    print(" Nuclear Tidal Wave Dynamics & B(E2) Scaling Analyzer")
    print("=======================================================")
    print(f"  Target Nucleus Z={args.Z}, A={args.A} (Spins: {spins[0]:.0f} -> {spins[-1]:.0f} hbar)")
    print(f"  B(E2) Linear Slope c1   : {scaling['slope_c1']:.4f} e^2 b^2 / hbar (R^2 = {scaling['R_squared']:.4f})")
    print(f"  Is Tidal Wave Mode?     : {scaling['is_tidal_wave_scaling']} (Growth per spin: +{scaling['growth_percent_per_spin']:.1f}%)")
    print("-------------------------------------------------------")
    print("  Dynamic Quadrupole Deformation Stretching beta_2(I):")
    for sp, b2 in zip(dyn["spins"], dyn["dynamic_beta2"]):
        print(f"    Spin {sp:2.0f} hbar : beta_2(I) = {b2:.3f}")
    print(f"  Total Centrifugal Stretching : +{dyn['relative_stretching_percent']:.1f}%")
    print("=======================================================")



def cmd_gt(args):
    res = evaluate_ga_quenching(args.Z, args.A, args.s_minus, args.s_plus, g_a_free=args.ga_free)
    print("\n=======================================================")
    print(" Gamow-Teller Resonance, Ikeda Sum Rule & g_A Quenching")
    print("=======================================================")
    print(f"  Target Nucleus : Z={res['Z']}, A={res['A']}, N={res['N']} (N - Z = {res['N'] - res['Z']})")
    print(f"  Theoretical Ikeda Limit : S_Ikeda = 3(N - Z) = {res['S_ikeda_theo']:.1f}")
    print(f"  Measured Net GT Strength: S_exp = {res['S_net_exp']:.2f} (S- = {res['S_minus_exp']:.2f}, S+ = {res['S_plus_exp']:.2f})")
    print(f"  Strength Recovery Ratio : {res['recovery_fraction']*100.0:.1f}%")
    print(f"  Quenching Factor q      : {res['quenching_factor_q']:.3f}")
    print(f"  Effective Axial Vector  : g_A^eff = {res['g_a_eff']:.4f} (Free nucleon: {res['g_a_free']:.4f})")
    print(f"  0nu2beta Half-Life Ratio: R(T_1/2) = {res['0nu_half_life_prolongation']:.2f}x prolongation")
    print(f"  Regime Diagnosis        : {res['diagnosis']}")
    if args.dsigma is not None and args.sigma_hat is not None:
        b_gt = convert_cross_section_to_b_gt(args.dsigma, args.sigma_hat)
        print("-------------------------------------------------------")
        print(f"  Zero-Degree dsigma/dOmega : {b_gt['dsigma_dOmega_0deg_mb_sr']:.2f} mb/sr")
        print(f"  Unit Cross Section sigma^ : {b_gt['unit_cross_section_sigma_hat_mb_sr']:.2f} mb/sr")
        print(f"  Extracted Microscopic B(GT): {b_gt['B_GT']:.3f}")
    print("=======================================================")


def cmd_halo(args):
    print("\n=======================================================")
    print(" Neutron Halo, Borromean Breakup & Soft E1 Analyzer")
    print("=======================================================")
    if args.fwhm is not None:
        inv = invert_separation_energy_from_fwhm(args.fwhm, A_core=args.Ac, A_halo=args.Ah)
        gold = calculate_goldhaber_width(args.Ac + args.Ah, args.Ac)
        diag = diagnose_halo_signature(args.fwhm, gold["fwhm_Goldhaber_MeV_c"])
        print(f"  Measured Fragment FWHM   : {args.fwhm:.2f} MeV/c")
        print(f"  Extracted Separation S_n : {inv['extracted_S_n_keV']:.1f} keV")
        print(f"  Asymptotic Decay Length  : {inv['decay_length_fm']:.2f} fm")
        print(f"  Goldhaber Normal FWHM    : {gold['fwhm_Goldhaber_MeV_c']:.2f} MeV/c (Core Fermi motion)")
        print(f"  Narrowing Factor         : {gold['fwhm_Goldhaber_MeV_c'] / args.fwhm:.2f}x narrower than core")
        print(f"  Halo Signature Diagnosis : {diag['diagnosis']}")
    elif args.sn is not None:
        fwd = calculate_hansen_jonson_fwhm(args.sn, A_core=args.Ac, A_halo=args.Ah)
        gold = calculate_goldhaber_width(args.Ac + args.Ah, args.Ac)
        diag = diagnose_halo_signature(fwd["fwhm_MeV_c"], gold["fwhm_Goldhaber_MeV_c"])
        print(f"  Input Separation S_n     : {args.sn:.1f} keV")
        print(f"  Predicted Breakup FWHM   : {fwd['fwhm_MeV_c']:.2f} MeV/c")
        print(f"  Asymptotic Decay Length  : {fwd['decay_length_fm']:.2f} fm")
        print(f"  Goldhaber Normal FWHM    : {gold['fwhm_Goldhaber_MeV_c']:.2f} MeV/c")
        print(f"  Halo Signature Diagnosis : {diag['diagnosis']}")

    if args.sigma_r is not None:
        rad = estimate_matter_radius_from_reaction_cross_section(args.sigma_r, A_p=args.Ac + args.Ah, A_t=args.At)
        print("-------------------------------------------------------")
        print(f"  Reaction Cross Section   : {args.sigma_r:.1f} mb on target A_t={args.At:.0f}")
        print(f"  Extracted Projectile Rrms: {rad['R_rms_projectile_fm']:.2f} fm")
        print(f"  Standard Core Reference  : {rad['R_rms_normal_reference_fm']:.2f} fm")
        print(f"  Relative Radius Increase : +{rad['relative_radius_expansion_percent']:.1f}%")

    if args.Zc is not None:
        soft = calculate_cluster_soft_e1_sum_rule(args.Zc, args.Ac, args.Zh, args.Ah, r_rms_halo_fm=args.r_halo)
        print("-------------------------------------------------------")
        print(f"  Cluster Soft E1 Dipole   : B(E1)_cluster = {soft['B_E1_cluster_sum_e2_fm2']:.3f} e^2 fm^2 (r_halo = {args.r_halo:.1f} fm)")
        print(f"  Effective Dipole Charge  : e_eff = {soft['e_eff']:.3f} e")
    print("=======================================================")


def cmd_fission(args):
    print("\n=======================================================")
    print(" Nuclear Fission Barrier & Superheavy Synthesis Analyzer")
    print("=======================================================")
    if args.Z is not None and args.A is not None:
        ldm = calculate_liquid_drop_fissility(args.Z, args.A)
        print(f"  Target Nucleus : Z={ldm['Z']}, A={ldm['A']}, N={ldm['N']} (Asymmetry: {ldm['asymmetry']:.3f})")
        print(f"  Z^2 / A Ratio  : {ldm['Z2_over_A']:.2f} (Critical Limit: {ldm['Z2_over_A_crit']:.2f})")
        print(f"  Fissility Param: x = {ldm['fissility_x']:.4f}")
        print(f"  LDM Macroscopic: B_f(LDM) = {ldm['liquid_drop_barrier_MeV']:.2f} MeV")
        if ldm['fissility_x'] >= 1.0:
            print("  Stability Status: Macroscopic LDM barrier completely vanished (x >= 1.0)!")
            print("                   Stability exclusively sustained by Quantum Shell Corrections!")

    if args.hw_E is not None and args.hw_V is not None:
        hw = calculate_hill_wheeler_penetration(args.hw_E, args.hw_V, hbar_omega_MeV=args.hw_hw)
        print("-------------------------------------------------------")
        print(f"  Hill-Wheeler Penetration : T(E={args.hw_E:.2f} MeV, V={args.hw_V:.2f} MeV) = {hw['transmission_probability']:.4e}")

    if args.E_star is not None and args.Bn is not None and args.Bf is not None:
        comp = calculate_gamma_n_over_gamma_f(args.E_star, args.Bn, args.Bf, args.A, B_f_ldm_MeV=args.Bf_ldm)
        print("-------------------------------------------------------")
        print(f"  Excitation Energy E*     : {args.E_star:.1f} MeV")
        print(f"  Neutron Separation B_n   : {args.Bn:.2f} MeV")
        print(f"  Effective Barrier B_f    : {comp['B_f_effective_MeV']:.2f} MeV (Thermal damping: {comp['shell_damping_factor']:.3f})")
        print(f"  Branching Ratio G_n/G_f  : {comp['gamma_n_over_gamma_f']:.4e}")
        print(f"  Single-Step Survival P1  : {comp['survival_fraction_step']:.4e}")

    if args.cap_mb is not None and args.p_cn is not None and args.xn is not None:
        bn_list = [float(x) for x in args.bn_list.split(",")] if args.bn_list else [args.Bn or 7.0] * args.xn
        bf_list = [float(x) for x in args.bf_list.split(",")] if args.bf_list else [args.Bf or 6.5] * args.xn
        est = estimate_superheavy_cross_section(args.cap_mb, args.p_cn, args.E_star, bn_list, bf_list, args.A, B_f_ldm_MeV=args.Bf_ldm, xn=args.xn)
        print("-------------------------------------------------------")
        print(f"  Superheavy Residue Cross Section: sigma_ER({args.xn}n) = {est['sigma_ER_pb']:.4f} pb ({est['sigma_ER_mb']:.4e} mb)")
        print(f"  Total Survival Probability P_surv: {est['P_surv_total']:.4e}")
    print("=======================================================")


def cmd_oslo(args):
    print("\n=======================================================")
    print(" Oslo Method: Level Density (NLD) & Gamma Strength (gSF)")
    print("=======================================================")
    if args.D0 is not None and args.Sn is not None and args.A is not None:
        sn_res = calculate_rho_at_sn(args.D0, args.It, args.Sn, args.A)
        print(f"  Target Nucleus A={args.A}, S_n = {args.Sn:.2f} MeV (Target spin I_t = {args.It:.1f})")
        print(f"  Neutron Resonance Spacing: D_0 = {args.D0:.2f} eV")
        print(f"  Spin Cutoff Parameter    : sigma(S_n) = {sn_res['spin_cutoff_sigma']:.3f}")
        print(f"  Extracted Level Density  : rho(S_n) = {sn_res['rho_Sn_MeV_inv']:.2e} MeV^-1")

    if args.check_invariance:
        ex = np.linspace(1.0, 8.0, 15)
        eg = np.linspace(0.5, 7.5, 15)
        r = np.exp(0.5 * ex)
        t = 0.01 * (eg ** 2)
        inv = verify_oslo_lie_transformation_invariance(r, t, ex, eg, A_factor=args.A_factor, alpha_slope=args.alpha, B_factor=args.B_factor)
        print("-------------------------------------------------------")
        print(f"  3-Parameter Lie Invariance Check: Verified = {inv['is_strictly_invariant']}")
        print(f"  Transformation Parameters: A={args.A_factor:.2f}, alpha={args.alpha:.3f}, B={args.B_factor:.2f}")
        print(f"  Max Normalized Matrix Diff: {inv['max_absolute_difference']:.2e} (Strictly < 1e-12)")

    if args.lee_gsf is not None:
        gsf_vals = [float(x.strip()) for x in args.lee_gsf.split(",")]
        eg_vals = [float(x.strip()) for x in args.lee_eg.split(",")] if args.lee_eg else np.linspace(0.5, 0.5 + 0.3 * (len(gsf_vals) - 1), len(gsf_vals))
        lee = diagnose_low_energy_enhancement(eg_vals, gsf_vals)
        print("-------------------------------------------------------")
        print(f"  Low-Energy Enhancement (LEE) Check: Has Upbend = {lee['has_lee']}")
        print(f"  Enhancement Ratio at Low E_gamma  : {lee['enhancement_ratio']:.2f}x")
        print(f"  Diagnosis                         : {lee['diagnosis']}")
    print("=======================================================")


def cmd_term(args):
    print("\n=======================================================")
    print(" High-Spin Band Termination & CNS Valence Alignment")
    print("=======================================================")
    if args.spins is not None and args.q0 is not None:
        sp_list = [float(x.strip()) for x in args.spins.split(",")]
        iterm = args.iterm if args.iterm is not None else sp_list[-1]
        istart = sp_list[0]
        qt_mod = model_transition_quadrupole_collapse(sp_list, args.q0, istart, iterm)
        print(f"  Start Spin : I_start = {istart:.1f} hbar -> Terminating Spin I_term = {iterm:.1f} hbar")
        print(f"  Initial Qt : {qt_mod['trajectory'][0]['Q_t_eb']:.2f} eb -> Final Qt : {qt_mod['trajectory'][-1]['Q_t_eb']:.3f} eb")
        print(f"  Qt Collapse Percentage: -{qt_mod['Q_t_drop_percent']:.1f}% (gamma: 0 deg prolate -> 60 deg oblate)")
        print("-------------------------------------------------------")
        print("  Trajectory across Triaxial Space (gamma, Qt, B(E2)):")
        for pt in qt_mod["trajectory"]:
            print(f"    Spin {pt['spin']:4.1f} hbar : gamma={pt['gamma_deg']:4.1f} deg, Qt={pt['Q_t_eb']:.3f} eb, B(E2)={pt['B_E2_e2b2']:.4f} e^2b^2")

    if args.energies is not None and args.spins is not None and args.A is not None:
        sp_list = [float(x.strip()) for x in args.spins.split(",")]
        en_list = [float(x.strip()) for x in args.energies.split(",")]
        if len(sp_list) == len(en_list):
            rr = calculate_rigid_rotor_subtraction(sp_list, en_list, args.A)
            j2 = calculate_dynamic_moment_of_inertia_j2(sp_list, en_list)
            print("-------------------------------------------------------")
            print(f"  Rigid Rotor Reference Cusp : Minimum at Spin I = {rr['cusp_spin']:.1f} hbar")
            print(f"  Energy Excess (E - E_RR)   : {rr['cusp_min_E_diff_MeV']:.3f} MeV at cusp")
            if len(j2) > 0:
                print(f"  Dynamic MOI J^(2) at End   : {j2[-1]['J2_hbar2_MeV']:.2f} hbar^2/MeV (Delta E_gamma = {j2[-1]['Delta_E_gamma_MeV']*1000.0:.1f} keV)")
            diag = diagnose_smooth_band_termination(q_drop_percent=qt_mod['Q_t_drop_percent'] if 'qt_mod' in locals() else None,
                                                    j2_steep_dive=len(j2)>0 and j2[-1]['J2_hbar2_MeV'] < 15.0,
                                                    e_diff_cusp_found=True)
            print(f"  Diagnosis                  : {diag['diagnosis']}")
    print("=======================================================")


def cmd_tdpad(args):
    print("\n=======================================================")
    print(" Time-Differential Perturbed Angular Distribution (TDPAD)")
    print("=======================================================")
    if args.g is not None and args.B is not None:
        larm = calculate_larmor_frequency(args.g, args.B)
        print(f"  Input g-Factor           : g = {args.g:+.3f}")
        print(f"  External Magnetic Field  : B = {args.B:.3f} Tesla")
        print(f"  Larmor Precession Freq   : omega_L = {larm['omega_L_rad_s']:.3e} rad/s (nu_L = {larm['Larmor_frequency_nu_MHz']:.2f} MHz)")
        print(f"  Modulation Period (pi/w) : T_mod = {larm['modulation_period_T_mod_ns']:.2f} ns (2*omega_L oscillation)")
    elif args.tmod is not None and args.B is not None:
        inv = invert_g_factor_from_period(args.tmod, args.B)
        print(f"  Measured Modulation Period: T_mod = {args.tmod:.2f} ns in B = {args.B:.3f} Tesla")
        print(f"  Inverted Nuclear g-Factor : |g| = {inv['g_factor_magnitude']:.4f}")

    if args.chiral_check:
        pl = calculate_three_vector_chiral_gfactor(geometry="planar")
        apl = calculate_three_vector_chiral_gfactor(geometry="aplanar")
        print("-------------------------------------------------------")
        print(f"  Three-Vector Chiral Geometry Benchmark (e.g. 128Cs):")
        print(f"    Planar Limit (Proton-aligned)   : g_planar  = {pl['calculated_g_factor']:.3f}")
        print(f"    Aplanar Limit (Mutually perp)   : g_aplanar = {apl['calculated_g_factor']:.3f}")

    if args.qs is not None and args.vzz is not None:
        qi = calculate_electric_quadrupole_frequency(args.qs, args.vzz, spin_I=args.I if args.I is not None else 4.5)
        print("-------------------------------------------------------")
        print(f"  Electric Quadrupole Interaction (QI) in Host:")
        print(f"    Static Quadrupole Moment |Qs| : {abs(args.qs):.2f} eb (Spin I = {args.I or 4.5})")
        print(f"    Host Electric Field Gradient : V_zz = {args.vzz:.2f} x 10^21 V/m^2")
        print(f"    Quadrupole Coupling Constant : nu_Q = {qi['nu_Q_MHz']:.2f} MHz")
        print(f"    Fundamental Precession Period: T_0 = {qi['fundamental_period_T0_ns']:.1f} ns")
    print("=======================================================")


def cmd_pair(args):
    print("\n=======================================================")
    print(" Nuclear Pairing Gaps, S_2n Systematics & Shell Closures")
    print("=======================================================")
    if args.s2n is not None and args.n_list is not None:
        n_vals = [int(x.strip()) for x in args.n_list.split(",")]
        s_vals = [float(x.strip()) for x in args.s2n.split(",")]
        series = [{"N": n, "S_2n_MeV": s} for n, s in zip(n_vals, s_vals)]

        magic_gaps = detect_shell_closure_drop(series)
        anomalies = detect_shape_transition_anomaly(series)

        print("  Two-Neutron Separation Energy Profile S_2n(N):")
        for item in series:
            print(f"    N = {item['N']:3d} : S_2n = {item['S_2n_MeV']:6.2f} MeV")

        if len(magic_gaps) > 0:
            print("-------------------------------------------------------")
            print("  Magic Shell Closure Diagnostics:")
            for g in magic_gaps:
                status = "PROMINENT SHELL GAP" if g['is_shell_closure'] else "WEAK/QUENCHED"
                print(f"    N = {g['N_magic']:3d} : Drop delta_2n = {g['shell_drop_delta_2n_MeV']:.2f} MeV -> {status}")

        if len(anomalies) > 0:
            print("-------------------------------------------------------")
            print("  Shape Phase Transition / Flattening Anomalies:")
            for a in anomalies:
                print(f"    {a['diagnosis']}")

    if args.b_3p is not None:
        b_vals = [float(x.strip()) for x in args.b_3p.split(",")]
        gap3 = calculate_pairing_gap_3point(b_vals[0], b_vals[1], b_vals[2], is_odd_N=args.is_odd)
        print("-------------------------------------------------------")
        print(f"  3-Point Odd-Even Staggering Gap : Delta^(3) = {gap3['delta_3point_MeV']:.3f} MeV")

    if args.A is not None:
        bcs = compare_empirical_bcs_gap(args.A)
        print(f"  Empirical BCS Baseline (A={args.A}) : Delta = 12/sqrt(A) = {bcs['Delta_12_over_sqrt_A_MeV']:.3f} MeV (4.8/A^1/3 = {bcs['Delta_4.8_over_cbrt_A_MeV']:.3f} MeV)")
    print("=======================================================")


def cmd_isgmr(args):
    print("\n=======================================================")
    print(" Isoscalar Giant Monopole Resonance (ISGMR) & EOS Analyzer")
    print("=======================================================")
    if args.Egmr is not None and args.A is not None:
        ka = calculate_ka_from_isgmr_energy(args.Egmr, args.A, R0_fm=args.R0)
        print(f"  Target Nucleus A={args.A} (R0 = {args.R0:.2f} fm, <r^2>^(1/2) = {ka['rms_radius_fm']:.2f} fm)")
        print(f"  Measured ISGMR Centroid  : E_GMR = {args.Egmr:.2f} MeV")
        print(f"  Finite Nucleus Stiffness : K_A = {ka['K_A_MeV']:.2f} MeV")
        if args.Z is not None:
            lep = leptodermous_expansion_ka(args.A, args.Z, K_vol=args.Kvol, K_tau=args.Ktau)
            print("-------------------------------------------------------")
            print(f"  Leptodermous Expansion   : K_A(theory) = {lep['K_A_theoretical_MeV']:.2f} MeV")
            print(f"    Volume term (K_inf)    : {lep['K_vol_MeV']:+.1f} MeV")
            print(f"    Surface penalty term   : {lep['K_surf_contribution_MeV']:+.1f} MeV")
            print(f"    Asymmetry term (K_tau) : {lep['K_tau_contribution_MeV']:+.1f} MeV (Asymmetry = {lep['asymmetry']:.3f})")
            print(f"    Coulomb repulsion term : {lep['K_coul_contribution_MeV']:+.1f} MeV")

    if args.beta2 is not None and args.A is not None:
        e0 = args.Egmr if args.Egmr is not None else 14.5
        split = model_deformation_splitting_two_state(e0, args.beta2, args.A)
        print("-------------------------------------------------------")
        print(f"  Deformation-Induced Monopole-Quadrupole Mixing (beta_2 = {args.beta2:.3f}):")
        print(f"    Unperturbed Breathing E0 : {split['E0_unperturbed_MeV']:.2f} MeV | Quadrupole E2(K=0) : {split['E2_unperturbed_MeV']:.2f} MeV")
        print(f"    Lower Resonance Peak E1  : {split['E_low_peak_MeV']:.2f} MeV (EWSR: {split['EWSR_fraction_low']*100.0:.1f}%)")
        print(f"    Upper Resonance Peak E2  : {split['E_high_peak_MeV']:.2f} MeV (EWSR: {split['EWSR_fraction_high']*100.0:.1f}%)")
        print(f"    Deformation Energy Split : Delta E = {split['splitting_energy_MeV']:.2f} MeV")

    if args.qpvc_ph is not None:
        e0 = args.Egmr if args.Egmr is not None else 16.7
        qpvc = calculate_qpvc_self_energy_shift(e0, args.qpvc_ph, g_coupling_MeV=args.qpvc_g)
        print("-------------------------------------------------------")
        print(f"  QPVC Dynamic Self-Energy Downward Shift:")
        print(f"    Low-Energy Phonon Energy : hbar*omega_ph = {args.qpvc_ph:.2f} MeV (Coupling g = {args.qpvc_g:.2f} MeV)")
        print(f"    Self-Energy Shift DeltaE : {qpvc['self_energy_shift_MeV']:+.2f} MeV")
        print(f"    Shifted ISGMR Energy     : E_GMR(shifted) = {qpvc['E_gmr_shifted_MeV']:.2f} MeV (Tin softness resolved)")
    print("=======================================================")


def cmd_relcoulex(args):
    print("\n=======================================================")
    print(" Relativistic Coulomb Excitation & Lorentz Boost")
    print("=======================================================")
    if args.Elab is not None and args.Ap is not None and args.Zp is not None and args.At is not None and args.Zt is not None:
        kin = calculate_relativistic_coulex_kinematics(args.Elab, args.Ap, args.Zp, args.At, args.Zt, d_safe_fm=args.dsafe)
        print(f"  Reaction: {args.Ap}X({args.Zp}) + {args.At}Y({args.Zt}) at E_lab = {args.Elab:.1f} MeV/u")
        print(f"  Relativistic Kinematics  : beta = {kin['beta']:.4f} (v = {kin['beta']*100.0:.1f}% c), gamma = {kin['gamma']:.4f}")
        print(f"  Safe Impact Parameter    : b_min = {kin['b_min_fm']:.2f} fm (Rp={kin['R_proj_fm']:.2f} fm, Rt={kin['R_targ_fm']:.2f} fm)")
        print(f"  Maximum Safe Lab Angle   : theta_safe(lab) = {kin['theta_safe_lab_deg']:.2f} deg (CM: {kin['theta_safe_cm_deg']:.2f} deg)")

        if args.be2 is not None and args.Ex is not None:
            cs = calculate_relativistic_e2_coulex_cross_section(args.be2, args.Ex, args.Elab, args.Ap, args.Zp, args.At, args.Zt, d_safe_fm=args.dsafe)
            print("-------------------------------------------------------")
            print(f"  Excitation Energy E_x    : {args.Ex:.3f} MeV | Input B(E2) = {args.be2:.4f} e^2b^2")
            print(f"  Adiabatic Parameter xi_0 : {cs['xi_0']:.4f} (f_E2 scaling = {cs['f_E2']:.4f})")
            print(f"  Predicted Coulex sigma_E2: {cs['sigma_E2_mb']:.2f} mb")

        elif args.sigma is not None and args.Ex is not None:
            inv = invert_b_e2_from_coulex_cross_section(args.sigma, args.Ex, args.Elab, args.Ap, args.Zp, args.At, args.Zt, d_safe_fm=args.dsafe)
            print("-------------------------------------------------------")
            print(f"  Measured Cross Section   : sigma_E2 = {args.sigma:.2f} mb at E_x = {args.Ex:.3f} MeV")
            print(f"  Inverted B(E2; 0+ -> 2+) : {inv['extracted_B_E2_e2b2']:.4f} e^2b^2 ({inv['extracted_B_E2_e2fm4']:.1f} e^2fm^4)")

    if args.lorentz_angles is not None:
        deg_list = [float(x.strip()) for x in args.lorentz_angles.split(",")]
        beta_val = args.beta if args.beta is not None else (kin['beta'] if 'kin' in locals() else 0.35)
        boost = transform_gamma_angular_distribution_lorentz(deg_list, beta_val, a2_cm=args.a2, a4_cm=args.a4)
        print("-------------------------------------------------------")
        print(f"  In-Beam Gamma Lorentz Boost Transformation (beta = {beta_val:.3f}):")
        for pt in boost:
            print(f"    Lab {pt['theta_lab_deg']:5.1f} deg -> CM {pt['theta_cm_deg']:5.1f} deg | Doppler={pt['doppler_shift_factor']:.3f} | Jacobian J={pt['jacobian_solid_angle']:.2f} | W_lab={pt['W_lab']:.3f}")
    print("=======================================================")


def cmd_alaga(args):
    print("\n=======================================================")
    print(" Electromagnetic Transition Rates, Weisskopf & Alaga Rules")
    print("=======================================================")
    if args.A is not None:
        wu_e1 = calculate_weisskopf_unit(args.A, "E1")
        wu_e2 = calculate_weisskopf_unit(args.A, "E2")
        wu_m1 = calculate_weisskopf_unit(args.A, "M1")
        print(f"  Weisskopf Units for Target A={args.A}:")
        print(f"    B_sp(E1) = {wu_e1['B_sp_value']:.4f} {wu_e1['unit']}")
        print(f"    B_sp(E2) = {wu_e2['B_sp_value']:.3f} {wu_e2['unit']} ({wu_e2['B_sp_value']*1e-4:.6f} e^2b^2)")
        print(f"    B_sp(M1) = {wu_m1['B_sp_value']:.4f} {wu_m1['unit']}")

    if args.tau is not None and args.Eg is not None and args.A is not None:
        b2 = convert_lifetime_to_b_e2(args.tau, args.Eg, args.A, branch_fraction=args.branch, alpha_icc=args.icc)
        print("-------------------------------------------------------")
        print(f"  Level Lifetime Conversion (tau = {args.tau:.3f} ps, E_gamma = {args.Eg:.1f} keV):")
        print(f"    B(E2) = {b2['B_E2_e2b2']:.4f} e^2b^2 ({b2['B_E2_e2fm4']:.1f} e^2fm^4)")
        print(f"    Collective Enhancement   : {b2['B_E2_W_u']:.1f} W.u.")
        print(f"    Intrinsic Quadrupole Q_0 : {b2['Q0_intrinsic_eb']:.3f} eb")

    if args.alaga_spin is not None:
        al = calculate_alaga_ratio_e2(args.alaga_spin, K_band=args.alaga_K)
        print("-------------------------------------------------------")
        print(f"  Axial Rotor Alaga Ratio B(E2; {args.alaga_spin:.0f} -> {args.alaga_spin-2:.0f}) / B(E2; 2 -> 0):")
        print(f"    Theoretical Clebsch-Gordan Ratio: R_Alaga = {al['alaga_ratio_to_2_0']:.4f} (K = {args.alaga_K:.0f})")

    if args.Eg1 is not None and args.Eg2 is not None and args.I1 is not None and args.I2 is not None:
        bm1_be2 = calculate_bm1_over_be2(args.Eg1, args.Eg2, args.I1, args.I2, delta_mixing=args.delta, spin_I=args.I, K_val=args.K)
        print("-------------------------------------------------------")
        print(f"  In-Band Branching Ratio Extraction (dI=1: {args.Eg1:.1f} keV, dI=2: {args.Eg2:.1f} keV):")
        print(f"    B(M1; I -> I-1) / B(E2; I -> I-2) = {bm1_be2['B_M1_over_B_E2_muN2_e2b2']:.4f} mu_N^2 / (e^2b^2)")
        if "abs_gK_minus_gR_over_Q0_muN_eb" in bm1_be2:
            print(f"    Intrinsic Parameter |g_K - g_R| / Q_0 = {bm1_be2['abs_gK_minus_gR_over_Q0_muN_eb']:.4f} mu_N / (e b) (Spin I={args.I:.1f}, K={args.K:.1f})")
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

    # Interacting Boson Model & Casten Triangle
    p_ibm = subparsers.add_parser("ibm", help="IBM dynamical symmetry (U(5), SU(3), O(6)) and Casten triangle phase")
    p_ibm.add_argument("--E21", type=float, required=True, help="Energy of 2_1+ state in keV")
    p_ibm.add_argument("--E41", type=float, required=True, help="Energy of 4_1+ state in keV")
    p_ibm.add_argument("--E22", type=float, default=None, help="Energy of 2_2+ state in keV")
    p_ibm.add_argument("--E02", type=float, default=None, help="Energy of 0_2+ state in keV")
    p_ibm.set_defaults(func=cmd_ibm)

    # ADO Ratio & Linear Polarization
    p_ado = subparsers.add_parser("ado", help="In-beam ADO ratio R_ADO and Clover polarization joint fit")
    p_ado.add_argument("--Rado", type=float, required=True, help="Measured ADO ratio")
    p_ado.add_argument("--Rado_err", type=float, default=0.04, help="ADO ratio error")
    p_ado.add_argument("--P", type=float, default=0.0, help="Direct linear polarization P (if known)")
    p_ado.add_argument("--P_err", type=float, default=0.05, help="Polarization error")
    p_ado.add_argument("--Nperp", type=float, default=None, help="Clover perpendicular scattering counts")
    p_ado.add_argument("--Npar", type=float, default=None, help="Clover parallel scattering counts")
    p_ado.add_argument("--Q", type=float, default=0.20, help="Clover polarization sensitivity Q")
    p_ado.add_argument("--th1", type=float, default=30.0, help="Forward/backward detector angle in deg")
    p_ado.add_argument("--th2", type=float, default=90.0, help="Perpendicular detector angle in deg")
    p_ado.add_argument("--F11", type=float, required=True, help="F2(11)")
    p_ado.add_argument("--F12", type=float, required=True, help="F2(12)")
    p_ado.add_argument("--F22", type=float, required=True, help="F2(22)")
    p_ado.add_argument("--F44", type=float, default=0.0, help="F4(22)")
    p_ado.add_argument("--alpha2", type=float, default=0.85, help="Alignment factor alpha2")
    p_ado.set_defaults(func=cmd_ado)

    # Side-Feeding Deconvolution
    p_feed = subparsers.add_parser("feed", help="Deconvolve side-feeding time delay from measured DSAM attenuation factor F")
    p_feed.add_argument("--F", type=float, required=True, help="Measured DSAM attenuation factor F(tau)")
    p_feed.add_argument("--tau_feed", type=float, default=0.30, help="Side-feeding cascade delay time in ps")
    p_feed.add_argument("--f_feed", type=float, default=0.40, help="Fraction of feeding from side quasicontinuum (0 to 1)")
    p_feed.add_argument("--alpha", type=float, default=1.05, help="Stopper foil slowing down time in ps")
    p_feed.set_defaults(func=cmd_feed)

    # Internal Conversion Coefficients & BrIcc
    p_icc = subparsers.add_parser("icc", help="Internal conversion coefficients (alpha_K, alpha_tot) and intensity correction")
    p_icc.add_argument("--Z", type=int, required=True, help="Atomic number Z")
    p_icc.add_argument("--Egamma", type=float, required=True, help="Gamma transition energy in keV")
    p_icc.add_argument("--mult", type=str, default="E2", help="Multipolarity (E1, M1, E2, M2, E3, M3)")
    p_icc.add_argument("--delta", type=float, default=None, help="Mixing ratio delta for M1+E2 transitions")
    p_icc.add_argument("--Igamma", type=float, default=None, help="Measured gamma peak intensity to correct for conversion")
    p_icc.set_defaults(func=cmd_icc)

    # Vacuum Deorientation Correction
    p_deor = subparsers.add_parser("deorient", help="Vacuum deorientation attenuation G2, G4 and angular distribution restoration")
    p_deor.add_argument("--Z", type=int, required=True, help="Atomic number Z of recoil nucleus")
    p_deor.add_argument("--beta", type=float, default=0.025, help="Recoil velocity beta = v/c")
    p_deor.add_argument("--tau", type=float, required=True, help="Excited level lifetime in ps")
    p_deor.add_argument("--g", type=float, default=0.35, help="Nuclear g-factor of state")
    p_deor.add_argument("--taur", type=float, default=3.0, help="Atomic electron relaxation time in ps")
    p_deor.add_argument("--a2", type=float, default=None, help="Measured attenuated a2 coefficient")
    p_deor.add_argument("--a2_err", type=float, default=None, help="a2 uncertainty")
    p_deor.add_argument("--a4", type=float, default=0.0, help="Measured a4 coefficient")
    p_deor.add_argument("--a4_err", type=float, default=None, help="a4 uncertainty")
    p_deor.set_defaults(func=cmd_deorient)

    # Tidal Waves & Dynamic Stretching
    p_tidal = subparsers.add_parser("tidal", help="Tidal wave B(E2) linear scaling law and dynamic beta2 stretching")
    p_tidal.add_argument("--spins", type=str, required=True, help="Comma-separated list of spins")
    p_tidal.add_argument("--be2", type=str, required=True, help="Comma-separated list of in-band B(E2) in e^2b^2")
    p_tidal.add_argument("--Z", type=int, default=46, help="Atomic number Z")
    p_tidal.add_argument("--A", type=int, default=102, help="Mass number A")
    p_tidal.set_defaults(func=cmd_tidal)

    # Gamow-Teller & Ikeda Quenching
    p_gt = subparsers.add_parser("gt", help="Gamow-Teller resonance, Ikeda sum rule, and g_A quenching analyzer")
    p_gt.add_argument("--Z", type=int, required=True, help="Atomic number Z")
    p_gt.add_argument("--A", type=int, required=True, help="Mass number A")
    p_gt.add_argument("--s-minus", type=float, required=True, help="Measured S_-(GT) strength")
    p_gt.add_argument("--s-plus", type=float, default=0.0, help="Measured S_+(GT) strength")
    p_gt.add_argument("--ga-free", type=float, default=1.2754, help="Free nucleon g_A (default: 1.2754)")
    p_gt.add_argument("--dsigma", type=float, default=None, help="Forward (0 deg) dsigma/dOmega in mb/sr")
    p_gt.add_argument("--sigma-hat", type=float, default=None, help="Reaction unit cross section sigma_hat in mb/sr")
    p_gt.set_defaults(func=cmd_gt)

    # Halo Nuclei Breakup & Soft E1
    p_halo = subparsers.add_parser("halo", help="Neutron halo breakup momentum distribution and soft E1 analyzer")
    p_halo.add_argument("--fwhm", type=float, default=None, help="Measured fragment longitudinal momentum FWHM in MeV/c")
    p_halo.add_argument("--sn", type=float, default=None, help="Valence separation energy S_n or S_2n in keV")
    p_halo.add_argument("--Ac", type=float, default=9.0, help="Core mass number A_core (default: 9.0 for 11Li core 9Li)")
    p_halo.add_argument("--Ah", type=float, default=2.0, help="Halo mass number A_halo (default: 2.0 for 11Li halo 2n)")
    p_halo.add_argument("--Zc", type=int, default=3, help="Core charge number Z_core (default: 3)")
    p_halo.add_argument("--Zh", type=int, default=0, help="Halo charge number Z_halo (default: 0 for neutron halo)")
    p_halo.add_argument("--r-halo", type=float, default=5.5, help="Estimated halo rms radius in fm")
    p_halo.add_argument("--sigma-r", type=float, default=None, help="High-energy reaction cross section in mb")
    p_halo.add_argument("--At", type=float, default=12.0, help="Target mass number (default: 12.0 for carbon target)")
    p_halo.set_defaults(func=cmd_halo)

    # Nuclear Fission & Superheavy Synthesis
    p_fiss = subparsers.add_parser("fission", help="Nuclear fission barriers, Hill-Wheeler penetration and superheavy element synthesis")
    p_fiss.add_argument("--Z", type=int, default=None, help="Atomic number Z")
    p_fiss.add_argument("--A", type=int, default=None, help="Mass number A")
    p_fiss.add_argument("--hw-E", type=float, default=None, help="Excitation energy for Hill-Wheeler in MeV")
    p_fiss.add_argument("--hw-V", type=float, default=None, help="Barrier height for Hill-Wheeler in MeV")
    p_fiss.add_argument("--hw-hw", type=float, default=0.7, help="Barrier curvature hbar*omega in MeV")
    p_fiss.add_argument("--E-star", type=float, default=None, help="Compound nucleus excitation energy E* in MeV")
    p_fiss.add_argument("--Bn", type=float, default=None, help="Neutron separation energy in MeV")
    p_fiss.add_argument("--Bf", type=float, default=None, help="Nominal low-energy fission barrier in MeV")
    p_fiss.add_argument("--Bf-ldm", type=float, default=0.5, help="Macroscopic liquid drop barrier in MeV")
    p_fiss.add_argument("--cap-mb", type=float, default=None, help="Capture cross section in mb")
    p_fiss.add_argument("--p-cn", type=float, default=None, help="Compound nucleus formation probability P_CN")
    p_fiss.add_argument("--xn", type=int, default=None, help="Number of emitted neutrons (xn channel)")
    p_fiss.add_argument("--bn-list", type=str, default=None, help="Comma-separated list of Bn for steps")
    p_fiss.add_argument("--bf-list", type=str, default=None, help="Comma-separated list of Bf for steps")
    p_fiss.set_defaults(func=cmd_fission)

    # Oslo Method NLD & gSF
    p_oslo = subparsers.add_parser("oslo", help="Oslo method level density, gamma strength function and Lie group analyzer")
    p_oslo.add_argument("--D0", type=float, default=None, help="s-wave neutron resonance spacing D_0 in eV")
    p_oslo.add_argument("--Sn", type=float, default=None, help="Neutron separation energy S_n in MeV")
    p_oslo.add_argument("--It", type=float, default=0.0, help="Target ground state spin I_target (default: 0.0)")
    p_oslo.add_argument("--A", type=int, default=None, help="Compound nucleus mass number A")
    p_oslo.add_argument("--check-invariance", action="store_true", help="Verify 3-parameter Lie group transformation invariance")
    p_oslo.add_argument("--A-factor", type=float, default=1.8, help="Lie transformation scale parameter A (default: 1.8)")
    p_oslo.add_argument("--alpha", type=float, default=0.35, help="Lie transformation slope parameter alpha (default: 0.35)")
    p_oslo.add_argument("--B-factor", type=float, default=2.4, help="Lie transformation scale parameter B (default: 2.4)")
    p_oslo.add_argument("--lee-gsf", type=str, default=None, help="Comma-separated gSF values for LEE diagnosis")
    p_oslo.add_argument("--lee-eg", type=str, default=None, help="Comma-separated E_gamma values in MeV for LEE diagnosis")
    p_oslo.set_defaults(func=cmd_oslo)

    # Band Termination & CNS Alignment
    p_term = subparsers.add_parser("term", help="Rotational band termination, Qt collapse and CNS alignment analyzer")
    p_term.add_argument("--spins", type=str, default=None, help="Comma-separated list of spins")
    p_term.add_argument("--energies", type=str, default=None, help="Comma-separated level energies in keV")
    p_term.add_argument("--q0", type=float, default=None, help="Low-spin collective intrinsic/transition quadrupole moment Q0 in eb")
    p_term.add_argument("--iterm", type=float, default=None, help="Terminating maximum spin I_term")
    p_term.add_argument("--A", type=int, default=None, help="Mass number A")
    p_term.set_defaults(func=cmd_term)

    # TDPAD Hyperfine Precession & g-Factor
    p_tdpad = subparsers.add_parser("tdpad", help="Time-differential perturbed angular distribution, g-factor and hyperfine precession")
    p_tdpad.add_argument("--g", type=float, default=None, help="Nuclear Lande g-factor")
    p_tdpad.add_argument("--B", type=float, default=None, help="External magnetic field in Tesla")
    p_tdpad.add_argument("--tmod", type=float, default=None, help="Measured modulation period T_mod in ns")
    p_tdpad.add_argument("--chiral-check", action="store_true", help="Compare three-vector planar vs aplanar chiral g-factor predictions")
    p_tdpad.add_argument("--qs", type=float, default=None, help="Static electric quadrupole moment in eb")
    p_tdpad.add_argument("--vzz", type=float, default=None, help="Host electric field gradient in 10^21 V/m^2")
    p_tdpad.add_argument("--I", type=float, default=None, help="State spin I")
    p_tdpad.set_defaults(func=cmd_tdpad)

    # Pairing Gaps & S_2n Systematics
    p_pair = subparsers.add_parser("pair", help="Two-neutron separation energy, pairing gaps and shell closure analyzer")
    p_pair.add_argument("--s2n", type=str, default=None, help="Comma-separated list of S_2n values in MeV")
    p_pair.add_argument("--n-list", type=str, default=None, help="Comma-separated list of neutron numbers N")
    p_pair.add_argument("--b-3p", type=str, default=None, help="Three binding energies B(N-1), B(N), B(N+1) in MeV")
    p_pair.add_argument("--is-odd", action="store_true", default=True, help="Center state has odd N (default: True)")
    p_pair.add_argument("--A", type=int, default=None, help="Mass number A for empirical BCS comparison")
    p_pair.set_defaults(func=cmd_pair)

    # ISGMR Breathing Mode & Incompressibility
    p_isgmr = subparsers.add_parser("isgmr", help="Isoscalar giant monopole resonance (breathing mode), incompressibility and deformation splitting")
    p_isgmr.add_argument("--Egmr", type=float, default=None, help="Measured ISGMR centroid energy in MeV")
    p_isgmr.add_argument("--A", type=int, default=None, help="Mass number A")
    p_isgmr.add_argument("--Z", type=int, default=None, help="Atomic number Z")
    p_isgmr.add_argument("--R0", type=float, default=1.2, help="Nuclear radius parameter R_0 in fm (default: 1.2)")
    p_isgmr.add_argument("--Kvol", type=float, default=240.0, help="Nuclear matter incompressibility K_infinity in MeV (default: 240.0)")
    p_isgmr.add_argument("--Ktau", type=float, default=-550.0, help="Asymmetry incompressibility K_tau in MeV (default: -550.0)")
    p_isgmr.add_argument("--beta2", type=float, default=None, help="Quadrupole deformation parameter beta_2")
    p_isgmr.add_argument("--qpvc-ph", type=float, default=None, help="Low-energy phonon energy in MeV for QPVC calculation")
    p_isgmr.add_argument("--qpvc-g", type=float, default=1.65, help="QPVC phonon-resonance coupling constant g in MeV (default: 1.65)")
    p_isgmr.set_defaults(func=cmd_isgmr)

    # Relativistic Coulex & Lorentz Boost
    p_relc = subparsers.add_parser("relcoulex", help="Relativistic Coulomb excitation, virtual photon and in-beam Lorentz boost analyzer")
    p_relc.add_argument("--Elab", type=float, default=None, help="Beam energy in MeV/u")
    p_relc.add_argument("--Ap", type=int, default=None, help="Projectile mass number A")
    p_relc.add_argument("--Zp", type=int, default=None, help="Projectile atomic number Z")
    p_relc.add_argument("--At", type=int, default=None, help="Target mass number A")
    p_relc.add_argument("--Zt", type=int, default=None, help="Target atomic number Z")
    p_relc.add_argument("--dsafe", type=float, default=2.5, help="Safe distance parameter in fm (default: 2.5)")
    p_relc.add_argument("--Ex", type=float, default=None, help="Excitation energy E_x in MeV")
    p_relc.add_argument("--be2", type=float, default=None, help="B(E2; 0+ -> 2+) in e^2b^2")
    p_relc.add_argument("--sigma", type=float, default=None, help="Measured Coulex cross section in mb")
    p_relc.add_argument("--lorentz-angles", type=str, default=None, help="Comma-separated laboratory detector angles in deg")
    p_relc.add_argument("--beta", type=float, default=None, help="Recoil/projectile velocity v/c")
    p_relc.add_argument("--a2", type=float, default=0.35, help="CM a2 angular distribution coefficient")
    p_relc.add_argument("--a4", type=float, default=-0.1, help="CM a4 angular distribution coefficient")
    p_relc.set_defaults(func=cmd_relcoulex)

    # Electromagnetic Transitions & Alaga Rules
    p_alaga = subparsers.add_parser("alaga", help="Electromagnetic transition rates, Weisskopf units and Alaga branching rules")
    p_alaga.add_argument("--A", type=int, default=None, help="Mass number A")
    p_alaga.add_argument("--tau", type=float, default=None, help="Excited state lifetime in ps")
    p_alaga.add_argument("--Eg", type=float, default=None, help="Gamma transition energy in keV")
    p_alaga.add_argument("--branch", type=float, default=1.0, help="Branching fraction (default: 1.0)")
    p_alaga.add_argument("--icc", type=float, default=0.0, help="Internal conversion coefficient alpha (default: 0.0)")
    p_alaga.add_argument("--alaga-spin", type=float, default=None, help="Initial spin for Alaga ratio calculation")
    p_alaga.add_argument("--alaga-K", type=float, default=0.0, help="Band K quantum number for Alaga ratio (default: 0.0)")
    p_alaga.add_argument("--Eg1", type=float, default=None, help="Delta I = 1 gamma energy in keV")
    p_alaga.add_argument("--Eg2", type=float, default=None, help="Delta I = 2 gamma energy in keV")
    p_alaga.add_argument("--I1", type=float, default=None, help="Delta I = 1 gamma intensity")
    p_alaga.add_argument("--I2", type=float, default=None, help="Delta I = 2 gamma intensity")
    p_alaga.add_argument("--delta", type=float, default=0.0, help="Delta I = 1 multipole mixing ratio delta(E2/M1)")
    p_alaga.add_argument("--I", type=float, default=None, help="Initial state spin I for |gK-gR|/Q0 extraction")
    p_alaga.add_argument("--K", type=float, default=None, help="Band K value for |gK-gR|/Q0 extraction")
    p_alaga.set_defaults(func=cmd_alaga)

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
