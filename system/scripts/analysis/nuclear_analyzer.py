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
from two_nucleon_transfer_pairing_vibration_calculator import calculate_bcs_transfer_enhancement, calculate_pairing_vibration_energies, evaluate_kinematic_q_matching, calculate_josephson_transfer_probability
from multi_nucleon_transfer_dic_calculator import calculate_wilczynski_energy_loss_and_orbiting, calculate_charge_equilibration, calculate_driving_potential, calculate_fragment_thermal_excitation_and_evaporation, predict_mnt_cross_section
from rmf_spin_orbit_pseudospin_calculator import calculate_rmf_potentials, estimate_spin_orbit_splitting, map_pseudospin_partner, evaluate_pseudospin_symmetry_quality, diagnose_pseudospin_chiral_quartet_manifold
from isotope_shift_charge_radii_calculator import calculate_normal_mass_shift, extract_delta_r2_from_isotope_shift, decompose_charge_radius_components, perform_king_plot_analysis, calculate_charge_radius_odd_even_staggering
from drip_line_radioactivity_cluster_calculator import calculate_proton_decay_wkb_lifetime, check_goldanskii_true_2p_condition, model_two_proton_jacobi_distribution, calculate_cluster_radioactivity_wkb, diagnose_drip_line_decay_competition
from thermonuclear_rate_gamow_factor_calculator import calculate_gamow_peak_and_window, calculate_sommerfeld_parameter, convert_cross_section_to_s_factor, calculate_nonresonant_reaction_rate, calculate_resonant_reaction_rate
from qrpa_matrix_vibrational_calculator import solve_qrpa_eigenvalues_and_amplitudes, solve_analytic_single_mode_qrpa, scan_pnqrpa_gpp_sensitivity, diagnose_qrpa_stability
from surface_delta_interaction_pandya_calculator import calculate_clebsch_gordan, calculate_wigner_6j, calculate_sdi_matrix_element, calculate_single_j_sdi_spectrum, perform_pandya_transformation, benchmark_sc42_k40_pandya
from k_isomer_hindrance_calculator import calculate_k_forbiddenness, calculate_reduced_hindrance, model_triaxial_gamma_tunneling_hindrance, classify_isomer_mechanism
from dipole_polarizability_neutron_skin_calculator import calculate_polarizability_from_sigma_minus2, integrate_dipole_polarizability_from_spectrum, droplet_model_polarizability_estimate, extract_neutron_skin_from_polarizability, extract_symmetry_energy_slope_L, predict_neutron_star_radius_from_L
from gilbert_cameron_level_density_calculator import solve_gilbert_cameron_matching, compute_level_density, calculate_s_wave_resonance_spacing, format_text_report as format_gc_report
from davydov_wobbling_rotor_calculator import davydov_filippov_energies_and_be2, frauendorf_wobbling_frequency, falsify_wobbling_vs_signature_partner, format_text_report as format_wob_report
from particle_identification_delta_e_calculator import calculate_stopping_power, simulate_telescope_response, evaluate_pulse_height_defect, evaluate_energy_straggling, format_text_report as format_pid_report
from compound_nucleus_evaporation_calculator import calculate_fusion_cross_section, simulate_statistical_evaporation_cascade, format_text_report as format_evap_report
from experimental_uncertainty_covariance_calculator import calculate_baker_cousins_deviance, synthesize_correlated_systematics, resolve_double_root_delta_mixing, format_text_report as format_uncert_report
from collective_quadrupole_pes_calculator import scan_potential_energy_surface, format_text_report as format_pes_report
from hpge_pulse_processing_pole_zero_calculator import calculate_ballistic_deficit, simulate_pole_zero_compensation, calculate_high_rate_pileup, format_text_report as format_hpge_report
from chiral_geometry_tac_calculator import calculate_chiral_geometry, evaluate_chiral_doublet_criteria, format_text_report as format_chiral_report
from beta_decay_log_ft_phase_space_calculator import calculate_log_ft, verify_superallowed_cvc_vud, format_text_report as format_beta_report
from gallagher_moszkowski_coupling_calculator import evaluate_gallagher_moszkowski_rule, calculate_newby_shift_spectrum, format_text_report as format_gm_report


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


def cmd_pairvib(args):
    print("\n=======================================================")
    print(" Two-Nucleon Transfer, Pairing Vibrations & Josephson Effect")
    print("=======================================================")
    if args.bcs_orbitals is not None:
        pairs = [x.strip().split(":") for x in args.bcs_orbitals.split(",")]
        orb_list = [(float(p[0]), float(p[1])) for p in pairs]
        bcs = calculate_bcs_transfer_enhancement(orb_list)
        print(f"  BCS Pair Transfer Superfluid Coherence ({bcs['orbitals_count']} active orbitals):")
        print(f"    Coherent Amplitude A_coh     : {bcs['coherent_amplitude_A']:.4f}")
        print(f"    Coherent Cross Section sigma : {bcs['sigma_coherent']:.3f} | Incoherent baseline: {bcs['sigma_incoherent']:.3f}")
        print(f"    Collective Enhancement Factor: {bcs['enhancement_factor']:.2f}x single-particle expectation")

    if args.s2n_plus is not None and args.s2n_core is not None:
        pv = calculate_pairing_vibration_energies(args.s2n_plus, args.s2n_core)
        print("-------------------------------------------------------")
        print(f"  Closed-Shell Pairing Vibrational Spectrum (S2n(A+2)={args.s2n_plus:.2f}, S2n(A)={args.s2n_core:.2f} MeV):")
        print(f"    Pair-Addition Mode Phonon hw+ : {pv['hw_plus_addition_phonon_MeV']:.3f} MeV (e.g. (t,p) on core)")
        print(f"    Pair-Removal Mode Phonon hw-  : {pv['hw_minus_removal_phonon_MeV']:.3f} MeV (e.g. (p,t) on core)")
        print(f"    Double-Phonon (1,1) State Ex  : {pv['Ex_double_phonon_1_1_MeV']:.3f} MeV (Collective 0+ vibrational state)")

    if args.q_actual is not None and args.Elab is not None:
        qm = evaluate_kinematic_q_matching(args.Elab, args.q_actual, args.Zp or 8, args.Ap or 18, args.Zt or 6, args.At or 12, args.Ze or 8, args.Ae or 16)
        print("-------------------------------------------------------")
        print(f"  Kinematic Q-Matching in Transfer (E_lab = {args.Elab:.1f} MeV, E_cm = {qm['E_cm_MeV']:.1f} MeV):")
        print(f"    Optimal Q-Value Q_opt        : {qm['Q_optimal_MeV']:.2f} MeV | Actual Q = {qm['Q_actual_MeV']:.2f} MeV")
        print(f"    Q-Mismatch                   : DeltaQ = {qm['Q_mismatch_MeV']:.2f} MeV")
        print(f"    Transmission Status          : {qm['matching_status']}")

    if args.p1_pair is not None:
        jos = calculate_josephson_transfer_probability(args.p1_pair, n_pairs=args.npairs or 2, enhancement_factor=args.enh_j or 15.0)
        print("-------------------------------------------------------")
        print(f"  Nuclear Josephson Multi-Pair Tunneling ({jos['n_pairs']} pairs):")
        print(f"    Uncorrelated Transfer Prob   : P_uncorr = {jos['P_uncorrelated']:.4e} ({args.p1_pair}^{jos['n_pairs']})")
        print(f"    Superfluid Josephson Prob    : P_Joseph = {jos['P_Josephson']:.4e} (Enhancement: {jos['enhancement_factor']:.1f}x)")
    print("=======================================================")


def cmd_mnt(args):
    print("\n=======================================================")
    print(" Multi-Nucleon Transfer (MNT) & Deep Inelastic (DIC)")
    print("=======================================================")
    if args.Elab is not None and args.Ap is not None and args.Zp is not None and args.At is not None and args.Zt is not None:
        wil = calculate_wilczynski_energy_loss_and_orbiting(args.Elab, args.Ap, args.Zp, args.At, args.Zt, d_scission_fm=args.dsciss)
        ce = calculate_charge_equilibration(args.Ap, args.Zp, args.At, args.Zt)
        print(f"  Reaction: {args.Ap}X({args.Zp}) + {args.At}Y({args.Zt}) at E_lab = {args.Elab:.1f} MeV/u (E_cm = {wil['E_cm_MeV']:.1f} MeV)")
        print(f"  Coulomb Barriers: V_contact = {wil['V_Coul_contact_MeV']:.1f} MeV | V_exit = {wil['V_exit_barrier_MeV']:.1f} MeV")
        print(f"  Energy Above Barrier   : E_cm - V_coul = {wil['energy_above_barrier_MeV']:+.1f} MeV (L_graz = {wil['L_grazing_hbar']:.0f} hbar)")
        print(f"  Max Kinetic Energy Loss: TKEL_max = {wil['TKEL_max_MeV']:.1f} MeV (Full Wilczynski damping)")
        print("-------------------------------------------------------")
        print(f"  Fast Charge Equilibration (tau_N/Z ~ 10^-22 s):")
        print(f"    (N/Z)_proj = {ce['N_over_Z_projectile']:.3f} | (N/Z)_targ = {ce['N_over_Z_target']:.3f} -> (N/Z)_sys = {ce['N_over_Z_system_equilibrated']:.3f}")
        print(f"    Equilibrated Charges   : Z_proj_eq = {ce['Z1_equilibrated_for_Ap']:.1f} | Z_targ_eq = {ce['Z2_equilibrated_for_At']:.1f}")

        if args.tkel is not None:
            tkel_val = args.tkel
        else:
            tkel_val = wil['TKEL_max_MeV']

        evap = calculate_fragment_thermal_excitation_and_evaporation(tkel_val, args.Ap, args.Zp, args.At, args.Zt)
        print("-------------------------------------------------------")
        print(f"  Thermal Excitation & Post-Collision Neutron Evaporation (TKEL = {tkel_val:.1f} MeV):")
        print(f"    Projectile Fragment: E1* = {evap['E1_star_MeV']:.1f} MeV (T1={evap['T1_temperature_MeV']:.2f} MeV) -> Evaporates ~ {evap['neutrons_evaporated_frag1']:.1f} neutrons")
        print(f"    Target Fragment    : E2* = {evap['E2_star_MeV']:.1f} MeV (T2={evap['T2_temperature_MeV']:.2f} MeV) -> Evaporates ~ {evap['neutrons_evaporated_frag2']:.1f} neutrons")

    if args.dZ is not None and args.dN is not None:
        sig_dic = args.sig_dic if args.sig_dic is not None else 1200.0
        tkel_v = args.tkel if args.tkel is not None else 80.0
        cs = predict_mnt_cross_section(sig_dic, args.dZ, args.dN, TKEL_MeV=tkel_v)
        print("-------------------------------------------------------")
        print(f"  MNT Production Cross Section (dZ = {args.dZ:+d}, dN = {args.dN:+d}, dA = {args.dZ+args.dN:+d}):")
        print(f"    sigma_MNT = {cs['sigma_MNT_mb']:.3f} mb ({cs['sigma_MNT_microbarn']:.1f} microbarns) [Transfer prob = {cs['transfer_probability']:.3e}]")
    print("=======================================================")


def cmd_rmf(args):
    print("\n=======================================================")
    print(" RMF Theory, Spin-Orbit & Pseudospin Symmetry (PSS)")
    print("=======================================================")
    if args.pot:
        r_grid = np.linspace(0.0, 10.0, 21)
        pot = calculate_rmf_potentials(r_grid, S0_MeV=args.S0 or -420.0, V0_MeV=args.V0 or 350.0, R0_fm=args.R0 or 6.5)
        print(f"  RMF Woods-Saxon Potentials (S0 = {args.S0 or -420.0:.1f} MeV, V0 = {args.V0 or 350.0:.1f} MeV):")
        print(f"    Central Binding Depth V+S    : {pot['central_depth_origin_MeV']:+.1f} MeV (Weak attractive well)")
        print(f"    Spin-Orbit Driving Sum V-S   : {pot['diff_potential_origin_MeV']:+.1f} MeV (Enormous relativistic gradient)")

    if args.l_so is not None and args.A is not None:
        so = estimate_spin_orbit_splitting(args.l_so, args.A)
        print("-------------------------------------------------------")
        print(f"  Relativistic Spin-Orbit Energy Splitting (l = {args.l_so}, A = {args.A}):")
        print(f"    Subshell Splitting (j = {so['j_lower']} vs {so['j_higher']}) : Delta E_SO = {so['Delta_E_SO_estimated_MeV']:.2f} MeV")

    if args.n_pss is not None and args.l_pss is not None:
        ps_map = map_pseudospin_partner(args.n_pss, args.l_pss)
        print("-------------------------------------------------------")
        print(f"  Pseudospin Partner Mapping (Input: n={args.n_pss}, l={args.l_pss}):")
        print(f"    State 1 (j = l + 1/2)        : {ps_map['state_1']}")
        print(f"    State 2 (j = l + 3/2)        : {ps_map['state_2']}")
        print(f"    Pseudo-Orbital Quantum Number: tilde(l) = {ps_map['pseudo_orbital_tilde_l']} [{ps_map['pseudo_spectroscopic']}]")
        print(f"    Pseudospin Quantum Numbers   : j = {ps_map['pseudospin_j1']} and {ps_map['pseudospin_j2']}")

    if args.pss_e1 is not None and args.pss_e2 is not None:
        so_val = args.pss_so if args.pss_so is not None else 3.5
        qual = evaluate_pseudospin_symmetry_quality(args.pss_e1, args.pss_e2, so_val)
        print("-------------------------------------------------------")
        print(f"  Pseudospin Symmetry Quality Evaluation (E1 = {args.pss_e1:.2f}, E2 = {args.pss_e2:.2f} MeV):")
        print(f"    PSS Energy Splitting DeltaE  : {qual['Delta_E_PSS_MeV']*1000.0:.1f} keV")
        print(f"    Relative Quality Factor Q_PSS: {qual['Q_PSS_ratio']*100.0:.1f}% of normal spin-orbit split")
        print(f"    Diagnosis                    : {qual['diagnosis']}")
    print("=======================================================")


def cmd_radius(args):
    print("\n=======================================================")
    print(" Nuclear Charge Radii, Isotope Shifts & King Plot")
    print("=======================================================")
    if args.dnu is not None and args.A is not None and args.Aref is not None:
        k_ms = args.Kms if args.Kms is not None else 800.0
        f_fs = args.Ffs if args.Ffs is not None else -4.5
        inv = extract_delta_r2_from_isotope_shift(args.dnu, args.A, args.Aref, k_ms, f_fs)
        dec = decompose_charge_radius_components(args.A, args.Aref, inv['delta_r2_fm2'])
        print(f"  Isotope Shift Analysis: {args.A}X vs Reference {args.Aref}X (delta_nu = {args.dnu:.4f} GHz)")
        print(f"    Total Mass Shift Contribution: {inv['delta_nu_MS_GHz']:+.4f} GHz (K_ms = {k_ms:.1f} GHz*amu)")
        print(f"    Field Shift Contribution     : {inv['delta_nu_FS_GHz']:+.4f} GHz (F = {f_fs:.2f} GHz/fm^2)")
        print(f"    Extracted delta<r^2>         : {inv['delta_r2_fm2']:+.4f} fm^2")
        print("-------------------------------------------------------")
        print(f"  Decomposition into Spherical Volume vs Deformation:")
        print(f"    Spherical Droplet Expansion  : {dec['delta_r2_spherical_fm2']:+.4f} fm^2")
        print(f"    Quadrupole Deformation Contrib: {dec['delta_r2_deformation_fm2']:+.4f} fm^2")
        print(f"    Induced delta<beta_2^2>      : {dec['delta_mean_square_beta2']:+.4f}")

    if args.king_masses is not None and args.king_s1 is not None and args.king_s2 is not None and args.Aref is not None:
        m_list = [float(x.strip()) for x in args.king_masses.split(",")]
        s1_list = [float(x.strip()) for x in args.king_s1.split(",")]
        s2_list = [float(x.strip()) for x in args.king_s2.split(",")]
        kp = perform_king_plot_analysis(m_list, args.Aref, s1_list, s2_list)
        print("-------------------------------------------------------")
        print(f"  King Plot 2D Linear Regression (Line 2 vs Line 1):")
        print(f"    Field Shift Ratio F2 / F1    : {kp['slope_F2_over_F1']:.4f}")
        print(f"    Combined Mass Shift Offset   : {kp['intercept_GHz_amu']:+.2f} GHz*amu")
        print(f"    Linearity Coefficient R^2    : {kp['R_squared']:.6f} (Strict Linearity: {kp['is_strictly_linear']})")
        print(f"    Maximum Linearity Residual   : {kp['max_residual_GHz_amu']:.2e} GHz*amu")

    if args.oes_n is not None and args.oes_r2 is not None:
        n_list = [int(x.strip()) for x in args.oes_n.split(",")]
        r2_list = [float(x.strip()) for x in args.oes_r2.split(",")]
        oes = calculate_charge_radius_odd_even_staggering(n_list, r2_list)
        print("-------------------------------------------------------")
        print(f"  Charge Radius Odd-Even Staggering (OES) Diagnostics:")
        for pt in oes:
            print(f"    Odd N = {pt['N_odd']:3d} : gamma_r = {pt['gamma_r']:.3f} -> {pt['interpretation']}")
    print("=======================================================")


def cmd_radioact(args):
    print("\n=======================================================")
    print(" Drip-Line Proton, True 2p & Cluster Radioactivity")
    print("=======================================================")
    if args.Qp is not None and args.Zd is not None and args.Ad is not None:
        p1 = calculate_proton_decay_wkb_lifetime(args.Qp, args.lp or 0, args.Zd, args.Ad, r0_fm=args.r0 or 1.2)
        print(f"  Single-Proton Radioactivity (Q_p = {args.Qp:.3f} MeV, l = {args.lp or 0} hbar):")
        print(f"    Daughter Nucleus         : {args.Ad}Z({args.Zd}) [R_in = {p1['R_in_fm']:.2f} fm -> R_out = {p1['R_out_fm']:.2f} fm]")
        print(f"    Gamow Action Integral G  : {p1['Gamow_integral_G']:.2f}")
        print(f"    WKB Penetration Factor P : {p1['penetration_factor_P']:.3e}")
        print(f"    Calculated Half-Life T1/2: {p1['T12_s']:.3e} s")

    if args.Q2p is not None and args.Sp is not None:
        g2p = check_goldanskii_true_2p_condition(args.Q2p, args.Sp)
        print("-------------------------------------------------------")
        print(f"  Goldanskii True Two-Proton Condition Check:")
        print(f"    Q_2p = {args.Q2p:.3f} MeV | S_p = {args.Sp:.3f} MeV (Q_1p = {-args.Sp:.3f} MeV)")
        print(f"    Is True 2p Radioactivity : {g2p['is_true_two_proton_decay']}")
        print(f"    Diagnosis                : {g2p['diagnosis']}")

    if args.Qc is not None and args.Ac is not None and args.Zc is not None and args.Zd is not None and args.Ad is not None:
        cl = calculate_cluster_radioactivity_wkb(args.Qc, args.Ac, args.Zc, args.Ad, args.Zd, P_preformation=args.Ppref or 1e-9)
        print("-------------------------------------------------------")
        print(f"  Exotic Heavy Cluster Radioactivity ({cl['cluster_nucleus']} emission):")
        print(f"    Decay Q-value            : Q_c = {args.Qc:.2f} MeV into {cl['daughter_nucleus']}")
        print(f"    WKB Barrier Penetration  : P_WKB = {cl['P_WKB']:.3e} (Gamow G = {cl['Gamow_factor_G']:.2f})")
        print(f"    Preformation Probability : P_pref = {cl['P_preformation']:.1e}")
        print(f"    Predicted Half-Life      : T1/2 = {cl['T12_s']:.3e} s ({cl['T12_years']:.2e} years)")

    if args.t12_p is not None or args.t12_beta is not None:
        comp = diagnose_drip_line_decay_competition(T12_p_s=args.t12_p, T12_2p_s=args.t12_2p, T12_beta_s=args.t12_beta, T12_alpha_s=args.t12_alpha)
        print("-------------------------------------------------------")
        print(f"  Decay Competition Analysis:")
        print(f"    Dominant Mode            : {comp['dominant_channel']} ({comp['dominant_branching_percent']:.1f}%)")
        print(f"    Total Effective T1/2     : {comp['total_half_life_s']:.3e} s")
    print("=======================================================")


def cmd_astro(args):
    print("\n=======================================================")
    print(" Thermonuclear Reaction Rates & Gamow Peak Analyzer")
    print("=======================================================")
    if args.T9 is not None and args.Z1 is not None and args.A1 is not None and args.Z2 is not None and args.A2 is not None:
        gp = calculate_gamow_peak_and_window(args.T9, args.Z1, args.A1, args.Z2, args.A2)
        print(f"  Reaction: {args.A1}Z({args.Z1}) + {args.A2}Z({args.Z2}) at Stellar T_9 = {args.T9:.4f} (T = {args.T9*1e9:.1e} K)")
        print(f"  Gamow Peak Energy        : E_0 = {gp['E0_Gamow_peak_keV']:.2f} keV")
        print(f"  Gamow Window Width       : Delta = {gp['Delta_window_width_keV']:.2f} keV")
        print(f"  Effective Burning Window : [{gp['Gamow_window_lower_keV']:.2f}, {gp['Gamow_window_upper_keV']:.2f}] keV")

        if args.S0 is not None:
            nonres = calculate_nonresonant_reaction_rate(args.T9, args.S0, args.Z1, args.A1, args.Z2, args.A2)
            print("-------------------------------------------------------")
            print(f"  Non-Resonant Reaction Rate (S_0 = {args.S0:.2f} keV*b):")
            print(f"    N_A <sigma v> = {nonres['reaction_rate_cm3_mol_s']:.4e} cm^3 / (mol * s)")

    if args.sigma is not None and args.Ecm is not None and args.Z1 is not None and args.A1 is not None and args.Z2 is not None and args.A2 is not None:
        s_res = convert_cross_section_to_s_factor(args.sigma, args.Ecm, args.Z1, args.A1, args.Z2, args.A2)
        print("-------------------------------------------------------")
        print(f"  Astrophysical S-Factor Conversion (E_cm = {args.Ecm:.2f} keV, sigma = {args.sigma:.3e} b):")
        print(f"    Sommerfeld Parameter eta : {s_res['sommerfeld_eta']:.4f}")
        print(f"    Extracted S(E)           : {s_res['S_factor_keV_b']:.4e} keV*b ({s_res['S_factor_MeV_b']:.4e} MeV*b)")

    if args.T9 is not None and args.E_res is not None and args.omega_gamma is not None and args.A1 is not None and args.A2 is not None:
        res = calculate_resonant_reaction_rate(args.T9, args.omega_gamma, args.E_res, args.A1, args.A2)
        print("-------------------------------------------------------")
        print(f"  Resonant Reaction Rate (Breit-Wigner Narrow Resonance):")
        print(f"    Resonance Energy E_r     : {args.E_res:.2f} keV | Strength omega*gamma = {args.omega_gamma:.2f} eV")
        print(f"    Resonant N_A <sigma v>   : {res['resonant_rate_cm3_mol_s']:.4e} cm^3 / (mol * s)")
    print("=======================================================")


def cmd_qrpa(args):
    print("\n=======================================================")
    print(" Quasiparticle Random-Phase Approximation (QRPA)")
    print("=======================================================")
    if args.analytic_A is not None and args.analytic_B is not None:
        sm = solve_analytic_single_mode_qrpa(args.analytic_A, args.analytic_B)
        print(f"  Analytic Single-Mode QRPA (A = {args.analytic_A:.2f} MeV, B = {args.analytic_B:.2f} MeV):")
        print(f"    Phonon Energy omega      : {sm['omega_MeV']:.3f} MeV (Unperturbed A = {args.analytic_A:.2f} MeV)")
        print(f"    Forward Amplitude X      : {sm['X']:.4f}")
        print(f"    Backward Amplitude Y     : {sm['Y']:.4f} (Y^2 = {sm['Y_squared']:.4f})")
        print(f"    Bose Metric Normalization: X^2 - Y^2 = {sm['X_squared_minus_Y_squared']:.4f}")
        print(f"    Transition Enhancement   : (X + Y)^2 = {sm['coherent_enhancement']:.3f}")

    if args.matrix_2x2 is not None:
        vals = [float(x.strip()) for x in args.matrix_2x2.split(",")]
        A = [[vals[0], vals[1]], [vals[1], vals[2]]]
        B = [[vals[3], vals[4]], [vals[4], vals[5]]]
        sol = solve_qrpa_eigenvalues_and_amplitudes(A, B)
        diag = diagnose_qrpa_stability(A, B)
        print("-------------------------------------------------------")
        print(f"  2x2 QRPA Supermatrix Diagonalization (Dimension = 2):")
        print(f"    Vacuum Stability Status  : {diag['diagnosis']}")
        for idx, m in enumerate(sol['modes']):
            print(f"    Mode {idx+1}: omega = {m['omega_MeV']:.3f} MeV | X = {m['X_amplitudes']}, Y = {m['Y_amplitudes']} | Coherent Enhancement = {m['coherent_enhancement_factor']:.2f}x")

    if args.scan_gpp:
        scan = scan_pnqrpa_gpp_sensitivity(E_unpert_MeV=args.E0 or 4.0)
        print("-------------------------------------------------------")
        print(f"  pnQRPA Particle-Particle Interaction g_pp Scan:")
        print(f"    Double Beta Decay M^2nu Zero-Crossing: g_pp = {scan['zero_crossing_gpp']:.2f}")
        print(f"    Vogel-Zirnbauer Suppression Mechanism successfully demonstrated.")
    print("=======================================================")


def cmd_pandya(args):
    print("\n=======================================================")
    print(" Surface Delta Interaction (SDI) & Pandya Transformation")
    print("=======================================================")
    if args.sdi_j is not None and args.sdi_l is not None:
        v0 = args.V0 if args.V0 is not None else 1.0
        sdi = calculate_single_j_sdi_spectrum(args.sdi_j, args.sdi_l, V0_MeV=v0)
        print(f"  SDI Pairing Spectrum in Single-j Shell (j = {args.sdi_j:.1f}, l = {args.sdi_l}, V_0 = {v0:.2f} MeV):")
        print(f"    Ground State J=0 Pairing Energy : E(J=0) = {sdi['E_J0_actual_MeV']:.4f} MeV (Exact -V0*(j+1/2) = {sdi['E_J0_expected_MeV']:.4f} MeV)")
        print(f"    Exact Linear Pairing Verified   : {sdi['is_exact_pairing_energy']}")
        print("    Two-Body Interaction Energies by Spin:")
        for pt in sdi['spectrum']:
            print(f"      J = {pt['J']:2d} : V_SDI = {pt['V_SDI_MeV']:+7.4f} MeV")

    if args.benchmark_sc42:
        bm = benchmark_sc42_k40_pandya()
        print("-------------------------------------------------------")
        print(f"  Pandya Benchmark: {bm['benchmark']}")
        print(f"    Particle-Particle Ground State Spin : J_pp = {bm['ground_state_pp_spin']}+ (Pairing attraction)")
        print(f"    Particle-Hole Inverted Ground State : J_ph = {bm['ground_state_ph_spin']}+ (High-spin ground state)")
        print(f"    Unitary Involution P^2 = I Verified : {bm['P2_verified']}")
        print("    Transformed Particle-Hole Spectrum:")
        for J, en in sorted(bm['ph_spectrum_keV'].items()):
            print(f"      J_ph = {J:2d} : E_ph = {en:7.1f} keV")
    print("=======================================================")


def cmd_isomer(args):
    print("\n=======================================================")
    print(" Nuclear K-Isomers, Reduced Hindrance & Gamma-Tunneling")
    print("=======================================================")
    if args.Ki is not None and args.Kf is not None and args.mult_lambda is not None:
        forb = calculate_k_forbiddenness(args.Ki, args.Kf, args.mult_lambda)
        print(f"  K-Selection Rule: K_i = {args.Ki:.1f} -> K_f = {args.Kf:.1f} (Multipolarity lambda = {args.mult_lambda})")
        print(f"    Delta K                  : |Ki - Kf| = {forb['Delta_K']:.1f}")
        print(f"    Degree of Forbiddenness  : nu = |Delta K| - lambda = {forb['degree_of_forbiddenness_nu']}")
        print(f"    Is Transition Forbidden  : {forb['is_K_forbidden']}")

    if args.tau_ps is not None and args.Eg is not None and args.A is not None:
        dK = abs(args.Ki - args.Kf) if (args.Ki is not None and args.Kf is not None) else (args.dK or 7)
        rh = calculate_reduced_hindrance(args.tau_ps, args.Eg, args.A, multipolarity=args.mult or "E1", delta_K=dK)
        print("-------------------------------------------------------")
        print(f"  Reduced Hindrance Analysis (tau = {args.tau_ps:.2e} ps, E_gamma = {args.Eg:.1f} keV, {args.mult or 'E1'}):")
        print(f"    Weisskopf Single-Particle T1/2: {rh['T12_sp_s']:.3e} s | Measured T1/2: {rh['T12_exp_s']:.3e} s")
        print(f"    Total Hindrance Factor F_W    : {rh['hindrance_F_W']:.3e}")
        print(f"    Degree of Forbiddenness nu    : {rh['degree_of_forbiddenness_nu']}")
        print(f"    Reduced Hindrance f_nu        : {rh['reduced_hindrance_f_nu']:.2f}")
        print(f"    Diagnosis                     : {rh['diagnosis']}")

    if args.gamma_deg is not None:
        tun = model_triaxial_gamma_tunneling_hindrance(args.gamma_deg)
        print("-------------------------------------------------------")
        print(f"  Triaxial Gamma-Tunneling Model (gamma = {args.gamma_deg:.1f} deg):")
        print(f"    Predicted Reduced Hindrance   : f_nu(gamma) = {tun['predicted_reduced_hindrance_f_nu']:.1f}")
        print(f"    Is Hindrance Collapsed (<10)  : {tun['is_hindrance_collapsed']}")

    if args.classify:
        t12 = (args.tau_ps * 1e-12 * np.log(2.0)) if args.tau_ps is not None else 0.01
        cls_info = classify_isomer_mechanism(t12, delta_I=args.dI or 0, delta_K=args.dK or 0, seniority_isomer=args.seniority, is_shape_isomer=args.shape_iso)
        print("-------------------------------------------------------")
        print(f"  Nuclear Isomer Mechanism Classification:")
        print(f"    Category                      : {cls_info['classification']}")
        print(f"    Physical Origin               : {cls_info['physical_mechanism']}")
    print("=======================================================")


def cmd_polariz(args):
    print("\n=======================================================")
    print(" Dipole Polarizability (alpha_D) & Neutron Skin Calculator")
    print("=======================================================")
    if args.sigma_m2 is not None:
        pol = calculate_polarizability_from_sigma_minus2(args.sigma_m2)
        print(f"  Photoabsorption Inverse Sum Rule: sigma_-2 = {args.sigma_m2:.2f} mb/MeV")
        print(f"  Electric Dipole Polarizability  : alpha_D = {pol['alpha_D_fm3']:.3f} fm^3")
        alpha_val = pol['alpha_D_fm3']
    elif args.alpha_D is not None:
        alpha_val = args.alpha_D
        print(f"  Input Dipole Polarizability     : alpha_D = {alpha_val:.3f} fm^3")
    else:
        alpha_val = None

    if alpha_val is not None:
        target = args.target if args.target is not None else "208Pb"
        skin = extract_neutron_skin_from_polarizability(alpha_val, target_nucleus=target)
        l_res = extract_symmetry_energy_slope_L(skin['delta_r_np_fm'])
        r_ns = predict_neutron_star_radius_from_L(l_res['L_slope_MeV'])
        print("-------------------------------------------------------")
        print(f"  Target Nucleus: {skin['target_nucleus']}")
        print(f"    Neutron Skin Thickness Delta_r_np : {skin['delta_r_np_fm']:.3f} +/- {skin['uncertainty_fm']:.3f} fm")
        print(f"    Symmetry Energy Slope Parameter L : {l_res['L_slope_MeV']:.1f} MeV")
        print(f"    Pure Neutron Matter Pressure P_0  : {l_res['P_PNM_rho0_MeV_fm3']:.3f} MeV/fm^3 ({l_res['P_PNM_rho0_dyn_cm2']:.2e} dyn/cm^2)")
        print(f"    Predicted 1.4 M_sun Neutron Star R: {r_ns['predicted_radius_R_NS_km']:.2f} km")

    if args.droplet and args.A is not None and args.Z is not None:
        drop = droplet_model_polarizability_estimate(args.A, args.Z, J_bulk_MeV=args.J or 32.0, Q_surf_MeV=args.Q or 35.0)
        print("-------------------------------------------------------")
        print(f"  Macroscopic Droplet Model Prediction for {args.A}Z({args.Z}):")
        print(f"    Bulk Symmetry J = {drop['J_bulk_MeV']:.1f} MeV, Surface Q = {drop['Q_surf_MeV']:.1f} MeV")
        print(f"    Droplet alpha_D = {drop['alpha_D_droplet_fm3']:.2f} fm^3")
    print("=======================================================")

def cmd_density(args):
    match = solve_gilbert_cameron_matching(args.Z, args.A, args.delta_w, args.gamma)
    eval_res = compute_level_density(args.energy, args.Z, args.A, args.spin, args.parity, match_params=match)
    summary = {
        "Z": args.Z, "A": args.A, "pairing_shift_MeV": match["delta_pair"],
        "shell_correction_delta_W_MeV": match["delta_W"], "asymptotic_a_MeV_inv": match["a_tilde"],
        "E_x_MeV": match["E_x"], "U_x_MeV": match["U_x"], "T_0_MeV": match["T_0"],
        "E_0_MeV": match["E_0"], "rho_match_MeV_inv": match["rho_at_match"],
        "evaluated_energy": eval_res
    }
    if args.sn is not None:
        summary["resonance_spacing_D0"] = calculate_s_wave_resonance_spacing(
            args.sn, args.Z, args.A, args.target_spin, args.delta_w, args.gamma
        )
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_gc_report(summary))


def cmd_wobbling(args):
    df_res = davydov_filippov_energies_and_be2(args.gamma, args.E2_1)
    wob_res = frauendorf_wobbling_frequency(args.spin_I, args.spin_j, args.A1, args.A2, args.A3, args.mode)
    fals_res = falsify_wobbling_vs_signature_partner(args.be2_ratio, args.bm1_out, args.delta_mix)
    summary = {"davydov": df_res, "wobbling_model": wob_res, "falsification": fals_res}
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_wob_report(summary))


def cmd_pid(args):
    sp_res = calculate_stopping_power(args.projectile, args.energy, "Si")
    tele_res = simulate_telescope_response(args.projectile, args.energy, args.delta_thick, args.window_nm)
    phd_res = evaluate_pulse_height_defect(args.projectile, args.energy, args.bias_V, args.window_nm)
    strag_res = evaluate_energy_straggling(args.projectile, args.energy, args.delta_thick)
    summary = {"stopping_power": sp_res, "telescope_response": tele_res, "pulse_height_defect": phd_res, "straggling": strag_res}
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_pid_report(summary))


def cmd_evap(args):
    fus_res = calculate_fusion_cross_section(args.Zp, args.Ap, args.Zt, args.At, args.elab)
    residues = simulate_statistical_evaporation_cascade(
        args.Zp + args.Zt, args.Ap + args.At, fus_res["compound_excitation_E_ex_MeV"], fus_res["sigma_fusion_mb"]
    )
    summary = {"fusion_kinematics": fus_res, "residues": residues}
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_evap_report(summary))


def cmd_stats(args):
    summary = {}
    if args.demo_baker or (not args.demo_cov and not args.solve_roots):
        obs = [0, 1, 2, 4, 3, 5, 8, 12, 10, 6, 2, 1]
        exp = [0.4, 0.9, 1.8, 3.5, 4.2, 5.8, 8.1, 11.2, 9.8, 5.5, 2.1, 0.8]
        summary["baker_cousins"] = calculate_baker_cousins_deviance(obs, exp)
    if args.demo_cov:
        summary["correlated_systematics"] = synthesize_correlated_systematics([100.0, 150.0, 80.0, 220.0], [5.0, 6.5, 4.2, 8.0], 0.04)
    if args.solve_roots or args.A2 != -0.25:
        summary["double_root"] = resolve_double_root_delta_mixing(args.A2, args.A2_err, args.F11, args.F12, args.F22, args.B2, args.alpha_exp, args.alpha_M1, args.alpha_E2)
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_uncert_report(summary))

def cmd_pes(args):
    c2, c3, c4, c5, c6, c6p = args.C2, args.C3, args.C4, args.C5, args.C6, args.C6_prime
    if args.preset == "prolate":
        c2, c3, c4, c5, c6, c6p = -18.0, -12.0, 45.0, 0.0, 20.0, 0.0
    elif args.preset == "oblate":
        c2, c3, c4, c5, c6, c6p = -18.0, +12.0, 45.0, 0.0, 20.0, 0.0
    elif args.preset == "gamma_soft":
        c2, c3, c4, c5, c6, c6p = -15.0, 0.0, 35.0, 0.0, 15.0, 0.0
    elif args.preset == "triaxial_rigid":
        c2, c3, c4, c5, c6, c6p = -20.0, 0.0, 30.0, 0.0, 10.0, 80.0
    summary = scan_potential_energy_surface(c2, c3, c4, c5, c6, c6p)
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_pes_report(summary))


def cmd_hpge(args):
    bd_res = calculate_ballistic_deficit(args.tc_ns, args.trise_ns, args.tflat_ns)
    pz_res = simulate_pole_zero_compensation(args.tau_preamp, args.tau_pz)
    pu_res = calculate_high_rate_pileup(args.rate_cps, args.trise_ns * 1e-3, args.tflat_ns * 1e-3)
    summary = {"ballistic_deficit": bd_res, "pole_zero": pz_res, "pileup": pu_res}
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_hpge_report(summary))


def cmd_chiral(args):
    geom = calculate_chiral_geometry(args.jp, args.jn, args.Rm, args.Rs, args.Rl)
    summary = {"geometry": geom}
    if args.delta_e_keV is not None:
        audit = evaluate_chiral_doublet_criteria(args.delta_e_keV, args.bm1_ratio, args.be2_ratio, geom["total_spin_I"])
        summary["doublet_audit"] = audit
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_chiral_report(summary))


def cmd_beta(args):
    res = calculate_log_ft(args.q_beta, args.t12, args.zdaughter, args.mass, args.br, args.mode)
    summary = {"log_ft": res}
    if args.cvc_check or res["log10_ft"] < 3.8:
        summary["cvc_audit"] = verify_superallowed_cvc_vud(res["ft_value_sec"])
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_beta_report(summary))


def cmd_gm(args):
    gm_res = evaluate_gallagher_moszkowski_rule(args.omega_p, args.lambda_p, args.omega_n, args.lambda_n, args.A, args.A_rot)
    summary = {"gm_rule": gm_res}
    if gm_res["is_K_zero_band"]:
        summary["newby_spectrum"] = calculate_newby_shift_spectrum(args.A_rot, args.newby_shift)
    if args.json:
        import json
        print(json.dumps(summary, indent=2))
    else:
        print(format_gm_report(summary))

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

    # Two-Nucleon Transfer & Pairing Vibrations
    p_pv = subparsers.add_parser("pairvib", help="Two-nucleon transfer, pairing vibrations and nuclear Josephson supercurrent")
    p_pv.add_argument("--bcs-orbitals", type=str, default=None, help="Comma-separated j:v2 pairs (e.g. 5.5:0.5,3.5:0.5,2.5:0.5)")
    p_pv.add_argument("--s2n-plus", type=float, default=None, help="S_2n of nucleus A+2 in MeV")
    p_pv.add_argument("--s2n-core", type=float, default=None, help="S_2n of closed-shell core A in MeV")
    p_pv.add_argument("--Elab", type=float, default=None, help="Beam energy in MeV for Q-matching")
    p_pv.add_argument("--q-actual", type=float, default=None, help="Actual reaction Q-value in MeV")
    p_pv.add_argument("--Zp", type=int, default=8, help="Projectile Z (default: 8)")
    p_pv.add_argument("--Ap", type=int, default=18, help="Projectile A (default: 18)")
    p_pv.add_argument("--Zt", type=int, default=6, help="Target Z (default: 6)")
    p_pv.add_argument("--At", type=int, default=12, help="Target A (default: 12)")
    p_pv.add_argument("--Ze", type=int, default=8, help="Ejectile Z (default: 8)")
    p_pv.add_argument("--Ae", type=int, default=16, help="Ejectile A (default: 16)")
    p_pv.add_argument("--p1-pair", type=float, default=None, help="Single-pair transfer probability")
    p_pv.add_argument("--npairs", type=int, default=2, help="Number of transferred pairs (default: 2)")
    p_pv.add_argument("--enh-j", type=float, default=15.0, help="Josephson enhancement factor (default: 15.0)")
    p_pv.set_defaults(func=cmd_pairvib)

    # Multi-Nucleon Transfer & DIC
    p_mnt = subparsers.add_parser("mnt", help="Multi-nucleon transfer (MNT), deep inelastic collisions and Wilczynski plot analyzer")
    p_mnt.add_argument("--Elab", type=float, default=None, help="Beam energy in MeV/u")
    p_mnt.add_argument("--Ap", type=int, default=None, help="Projectile mass number A")
    p_mnt.add_argument("--Zp", type=int, default=None, help="Projectile atomic number Z")
    p_mnt.add_argument("--At", type=int, default=None, help="Target mass number A")
    p_mnt.add_argument("--Zt", type=int, default=None, help="Target atomic number Z")
    p_mnt.add_argument("--dsciss", type=float, default=2.5, help="Scission distance neck extension in fm (default: 2.5)")
    p_mnt.add_argument("--tkel", type=float, default=None, help="Total kinetic energy loss TKEL in MeV")
    p_mnt.add_argument("--dZ", type=int, default=None, help="Net proton transfer number Delta Z to target")
    p_mnt.add_argument("--dN", type=int, default=None, help="Net neutron transfer number Delta N to target")
    p_mnt.add_argument("--sig-dic", type=float, default=1200.0, help="Total deep inelastic cross section in mb (default: 1200)")
    p_mnt.set_defaults(func=cmd_mnt)

    # RMF Spin-Orbit & Pseudospin Symmetry
    p_rmf = subparsers.add_parser("rmf", help="Relativistic mean field (RMF), spin-orbit splitting and pseudospin symmetry (PSS)")
    p_rmf.add_argument("--pot", action="store_true", help="Display RMF scalar/vector potentials and central/spin-orbit depth")
    p_rmf.add_argument("--S0", type=float, default=None, help="Scalar potential depth S0 in MeV (default: -420)")
    p_rmf.add_argument("--V0", type=float, default=None, help="Vector potential depth V0 in MeV (default: +350)")
    p_rmf.add_argument("--R0", type=float, default=None, help="Radius parameter R0 in fm (default: 6.5)")
    p_rmf.add_argument("--l-so", type=int, default=None, help="Orbital angular momentum l for spin-orbit splitting")
    p_rmf.add_argument("--A", type=int, default=None, help="Mass number A")
    p_rmf.add_argument("--n-pss", type=int, default=None, help="Principal quantum number n for pseudospin mapping")
    p_rmf.add_argument("--l-pss", type=int, default=None, help="Orbital quantum number l for pseudospin mapping")
    p_rmf.add_argument("--pss-e1", type=float, default=None, help="Energy of state 1 in MeV")
    p_rmf.add_argument("--pss-e2", type=float, default=None, help="Energy of state 2 in MeV")
    p_rmf.add_argument("--pss-so", type=float, default=None, help="Normal spin-orbit splitting baseline in MeV")
    p_rmf.set_defaults(func=cmd_rmf)

    # Nuclear Charge Radii & Isotope Shifts
    p_rad = subparsers.add_parser("radius", help="Nuclear charge radii, optical isotope shifts and King plot linearity")
    p_rad.add_argument("--dnu", type=float, default=None, help="Measured optical isotope shift in GHz")
    p_rad.add_argument("--A", type=int, default=None, help="Target isotope mass number A")
    p_rad.add_argument("--Aref", type=int, default=None, help="Reference isotope mass number A_ref")
    p_rad.add_argument("--Kms", type=float, default=None, help="Atomic mass shift constant in GHz*amu")
    p_rad.add_argument("--Ffs", type=float, default=None, help="Electronic field shift factor in GHz/fm^2")
    p_rad.add_argument("--king-masses", type=str, default=None, help="Comma-separated mass numbers for King plot")
    p_rad.add_argument("--king-s1", type=str, default=None, help="Comma-separated shifts for Line 1 in GHz")
    p_rad.add_argument("--king-s2", type=str, default=None, help="Comma-separated shifts for Line 2 in GHz")
    p_rad.add_argument("--oes-n", type=str, default=None, help="Comma-separated neutron numbers for OES test")
    p_rad.add_argument("--oes-r2", type=str, default=None, help="Comma-separated <r^2> values in fm^2 for OES test")
    p_rad.set_defaults(func=cmd_radius)

    # Drip-Line Radioactivity & Cluster Decay
    p_rad_act = subparsers.add_parser("radioact", help="Proton drip-line radioactivity, true 2p decay and cluster emission")
    p_rad_act.add_argument("--Qp", type=float, default=None, help="Proton decay energy Q_p in MeV")
    p_rad_act.add_argument("--lp", type=int, default=0, help="Proton orbital angular momentum l (default: 0)")
    p_rad_act.add_argument("--Zd", type=int, default=None, help="Daughter atomic number Z_d")
    p_rad_act.add_argument("--Ad", type=int, default=None, help="Daughter mass number A_d")
    p_rad_act.add_argument("--r0", type=float, default=1.2, help="Radius parameter r0 in fm (default: 1.2)")
    p_rad_act.add_argument("--Q2p", type=float, default=None, help="Two-proton decay energy Q_2p in MeV")
    p_rad_act.add_argument("--Sp", type=float, default=None, help="Single-proton separation energy S_p in MeV")
    p_rad_act.add_argument("--Qc", type=float, default=None, help="Cluster decay energy Q_c in MeV")
    p_rad_act.add_argument("--Ac", type=int, default=None, help="Emitted cluster mass number A_c")
    p_rad_act.add_argument("--Zc", type=int, default=None, help="Emitted cluster atomic number Z_c")
    p_rad_act.add_argument("--Ppref", type=float, default=1e-9, help="Cluster preformation probability (default: 1e-9)")
    p_rad_act.add_argument("--t12-p", type=float, default=None, help="Partial 1p half-life in s")
    p_rad_act.add_argument("--t12-2p", type=float, default=None, help="Partial 2p half-life in s")
    p_rad_act.add_argument("--t12-beta", type=float, default=None, help="Partial beta+/EC half-life in s")
    p_rad_act.add_argument("--t12-alpha", type=float, default=None, help="Partial alpha half-life in s")
    p_rad_act.set_defaults(func=cmd_radioact)

    # Nuclear Astrophysics & Gamow Peak
    p_astro = subparsers.add_parser("astro", help="Thermonuclear reaction rates, Gamow peak window and astrophysical S-factor")
    p_astro.add_argument("--T9", type=float, default=None, help="Stellar temperature in 10^9 K")
    p_astro.add_argument("--Z1", type=int, default=None, help="Nucleus 1 atomic number Z")
    p_astro.add_argument("--A1", type=float, default=None, help="Nucleus 1 mass number A")
    p_astro.add_argument("--Z2", type=int, default=None, help="Nucleus 2 atomic number Z")
    p_astro.add_argument("--A2", type=float, default=None, help="Nucleus 2 mass number A")
    p_astro.add_argument("--S0", type=float, default=None, help="Astrophysical S-factor S(0) in keV*b")
    p_astro.add_argument("--sigma", type=float, default=None, help="Reaction cross section in barns")
    p_astro.add_argument("--Ecm", type=float, default=None, help="Center-of-mass energy in keV")
    p_astro.add_argument("--E-res", type=float, default=None, help="Resonance energy E_res in keV")
    p_astro.add_argument("--omega-gamma", type=float, default=None, help="Resonance strength omega*gamma in eV")
    p_astro.set_defaults(func=cmd_astro)

    # QRPA & pnQRPA Matrix Analyzer
    p_qrpa = subparsers.add_parser("qrpa", help="Quasiparticle random-phase approximation (QRPA) and pnQRPA matrix analyzer")
    p_qrpa.add_argument("--analytic-A", type=float, default=None, help="Unperturbed diagonal A matrix element in MeV")
    p_qrpa.add_argument("--analytic-B", type=float, default=None, help="Off-diagonal ground-state correlation B in MeV")
    p_qrpa.add_argument("--matrix-2x2", type=str, default=None, help="Comma-separated 2x2 elements: a11,a12,a22,b11,b12,b22 in MeV")
    p_qrpa.add_argument("--scan-gpp", action="store_true", help="Perform pnQRPA g_pp sensitivity scan for double beta decay")
    p_qrpa.add_argument("--E0", type=float, default=4.0, help="Unperturbed 1+ state energy in MeV (default: 4.0)")
    p_qrpa.set_defaults(func=cmd_qrpa)

    # Surface Delta Interaction & Pandya Transformation
    p_pandya = subparsers.add_parser("pandya", help="Surface delta interaction (SDI) two-body matrix elements and Pandya transformation")
    p_pandya.add_argument("--sdi-j", type=float, default=None, help="Single-particle angular momentum j (e.g. 3.5 for f7/2)")
    p_pandya.add_argument("--sdi-l", type=int, default=None, help="Single-particle orbital angular momentum l (e.g. 3 for f-wave)")
    p_pandya.add_argument("--V0", type=float, default=1.0, help="SDI strength constant V0 in MeV (default: 1.0)")
    p_pandya.add_argument("--benchmark-sc42", action="store_true", help="Run classic 42Sc (pp) vs 48Sc/40K (ph) Pandya benchmark")
    p_pandya.set_defaults(func=cmd_pandya)

    # K-Isomers & Reduced Hindrance
    p_iso = subparsers.add_parser("isomer", help="Nuclear K-isomers, reduced hindrance f_nu and triaxial gamma-tunneling")
    p_iso.add_argument("--Ki", type=float, default=None, help="Initial state K quantum number")
    p_iso.add_argument("--Kf", type=float, default=None, help="Final state K quantum number")
    p_iso.add_argument("--mult-lambda", type=int, default=None, help="Transition multipolarity lambda (1 for dipole, 2 for quadrupole)")
    p_iso.add_argument("--tau-ps", type=float, default=None, help="Excited level lifetime in ps")
    p_iso.add_argument("--Eg", type=float, default=None, help="Gamma transition energy in keV")
    p_iso.add_argument("--A", type=int, default=None, help="Mass number A")
    p_iso.add_argument("--mult", type=str, default="E1", help="Multipolarity string (E1, E2, M1, M2, E3)")
    p_iso.add_argument("--dK", type=float, default=None, help="Delta K value")
    p_iso.add_argument("--dI", type=float, default=0.0, help="Delta I spin change")
    p_iso.add_argument("--gamma-deg", type=float, default=None, help="Triaxial deformation angle gamma in degrees")
    p_iso.add_argument("--classify", action="store_true", help="Classify the physical mechanism of the isomer")
    p_iso.add_argument("--seniority", action="store_true", help="Flag as potential seniority isomer")
    p_iso.add_argument("--shape-iso", action="store_true", help="Flag as potential shape/fission isomer")
    p_iso.set_defaults(func=cmd_isomer)

    # Dipole Polarizability & Neutron Skin
    p_pol = subparsers.add_parser("polariz", help="Electric dipole polarizability alpha_D, neutron skin and EOS slope L")
    p_pol.add_argument("--sigma-m2", type=float, default=None, help="Inverse energy-weighted photoabsorption cross section in mb/MeV")
    p_pol.add_argument("--alpha-D", type=float, default=None, help="Electric dipole polarizability in fm^3")
    p_pol.add_argument("--target", type=str, default="208Pb", help="Target nucleus name (208Pb, 120Sn, 48Ca)")
    p_pol.add_argument("--droplet", action="store_true", help="Compute droplet model polarizability estimate")
    p_pol.add_argument("--A", type=int, default=None, help="Mass number A for droplet calculation")
    p_pol.add_argument("--Z", type=int, default=None, help="Atomic number Z for droplet calculation")
    p_pol.add_argument("--J", type=float, default=32.0, help="Bulk symmetry energy in MeV (default: 32.0)")
    p_pol.add_argument("--Q", type=float, default=35.0, help="Surface symmetry stiffness in MeV (default: 35.0)")
    p_pol.set_defaults(func=cmd_polariz)

    # Gilbert-Cameron Level Density & Shell Damping
    p_ld = subparsers.add_parser("density", help="Gilbert-Cameron composite level density with Ignatyuk shell damping")
    p_ld.add_argument("-Z", type=int, required=True, help="Proton number Z")
    p_ld.add_argument("-A", type=int, required=True, help="Mass number A")
    p_ld.add_argument("-E", "--energy", type=float, default=8.0, help="Excitation energy in MeV (default: 8.0)")
    p_ld.add_argument("-J", "--spin", type=float, default=None, help="Spin J for spin-dependent density")
    p_ld.add_argument("-p", "--parity", type=int, default=None, choices=[1, -1], help="Parity (+1 or -1)")
    p_ld.add_argument("--sn", type=float, default=None, help="Neutron separation energy S_n in MeV for D_0 calculation")
    p_ld.add_argument("--target-spin", type=float, default=0.0, help="Target ground state spin I_0 (default: 0.0)")
    p_ld.add_argument("--delta-w", type=float, default=None, help="Shell correction delta_W in MeV")
    p_ld.add_argument("--gamma", type=float, default=0.054, help="Ignatyuk damping factor gamma in MeV^-1 (default: 0.054)")
    p_ld.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_ld.set_defaults(func=cmd_density)

    # Davydov-Filippov Rotor & Wobbling Motion
    p_wob = subparsers.add_parser("wobbling", help="Davydov-Filippov triaxial rotor and Frauendorf transverse/longitudinal wobbling")
    p_wob.add_argument("--gamma", type=float, default=25.0, help="Triaxial deformation angle gamma in degrees (default: 25.0)")
    p_wob.add_argument("--E2-1", type=float, default=100.0, help="E(2_1^+) energy in keV (default: 100.0)")
    p_wob.add_argument("--spin-I", type=float, default=13.5, help="Total spin I for odd-A nucleus")
    p_wob.add_argument("--spin-j", type=float, default=6.5, help="Quasiparticle spin j (default: 6.5)")
    p_wob.add_argument("--A1", type=float, default=12.0, help="Rotational constant A1 in keV (default: 12.0)")
    p_wob.add_argument("--A2", type=float, default=25.0, help="Rotational constant A2 in keV (default: 25.0)")
    p_wob.add_argument("--A3", type=float, default=45.0, help="Rotational constant A3 in keV (default: 45.0)")
    p_wob.add_argument("--mode", type=str, default="TW", choices=["TW", "LW"], help="Wobbling mode: TW or LW (default: TW)")
    p_wob.add_argument("--be2-ratio", type=float, default=None, help="B(E2)_out / B(E2)_in ratio")
    p_wob.add_argument("--bm1-out", type=float, default=None, help="B(M1)_out in W.u.")
    p_wob.add_argument("--delta-mix", type=float, default=None, help="Mixing ratio delta(E2/M1)")
    p_wob.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_wob.set_defaults(func=cmd_wobbling)

    # Particle Identification & Stopping Power
    p_pid = subparsers.add_parser("pid", help="Charged-particle Delta_E - E telescope identification and Bethe-Bloch stopping power")
    p_pid.add_argument("-p", "--projectile", type=str, default="alpha", help="Projectile particle (p, d, t, 3He, alpha, 6Li, 7Li, 12C, 16O)")
    p_pid.add_argument("-E", "--energy", type=float, default=20.0, help="Kinetic energy in MeV (default: 20.0)")
    p_pid.add_argument("--delta-thick", type=float, default=30.0, help="Delta_E detector thickness in um (default: 30.0)")
    p_pid.add_argument("--window-nm", type=float, default=100.0, help="Front dead layer thickness in nm (default: 100.0)")
    p_pid.add_argument("--bias-V", type=float, default=100.0, help="Detector reverse bias in V (default: 100.0)")
    p_pid.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_pid.set_defaults(func=cmd_pid)

    # Heavy-Ion Fusion-Evaporation Cross Sections
    p_ev = subparsers.add_parser("evap", help="Statistical heavy-ion fusion-evaporation cascade and residue cross sections")
    p_ev.add_argument("-Zp", type=int, required=True, help="Projectile atomic number Z_p")
    p_ev.add_argument("-Ap", type=int, required=True, help="Projectile mass number A_p")
    p_ev.add_argument("-Zt", type=int, required=True, help="Target atomic number Z_t")
    p_ev.add_argument("-At", type=int, required=True, help="Target mass number A_t")
    p_ev.add_argument("-E", "--elab", type=float, required=True, help="Beam energy E_lab in MeV")
    p_ev.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_ev.set_defaults(func=cmd_evap)

    # Statistical Uncertainty & Double-Root Resolver
    p_st = subparsers.add_parser("stats", help="Advanced experimental uncertainty propagation, covariance and double-root resolver")
    p_st.add_argument("--demo-baker", action="store_true", help="Demonstrate Baker-Cousins deviance in low counts")
    p_st.add_argument("--demo-cov", action="store_true", help="Demonstrate correlated systematic scale covariance")
    p_st.add_argument("--solve-roots", action="store_true", help="Solve double-root mixing ratio ambiguity")
    p_st.add_argument("--A2", type=float, default=-0.25, help="Experimental A2 angular distribution coefficient")
    p_st.add_argument("--A2-err", type=float, default=0.03, help="Uncertainty on A2")
    p_st.add_argument("--F11", type=float, default=-0.448, help="Theoretical F11 coefficient")
    p_st.add_argument("--F12", type=float, default=-0.418, help="Theoretical F12 coefficient")
    p_st.add_argument("--F22", type=float, default=-0.190, help="Theoretical F22 coefficient")
    p_st.add_argument("--B2", type=float, default=0.85, help="Orientation alignment parameter B2")
    p_st.add_argument("--alpha-exp", type=float, default=None, help="Experimental internal conversion coefficient alpha_K")
    p_st.add_argument("--alpha-M1", type=float, default=0.035, help="Theoretical alpha_K for M1")
    p_st.add_argument("--alpha-E2", type=float, default=0.012, help="Theoretical alpha_K for E2")
    p_st.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_st.set_defaults(func=cmd_stats)

    # 5D Bohr Collective Hamiltonian Quadrupole Potential Energy Surface (PES)
    p_pes = subparsers.add_parser("pes", help="5D Bohr collective Hamiltonian quadrupole potential energy surface (PES)")
    p_pes.add_argument("--C2", type=float, default=-15.0, help="C2 coefficient in MeV (default: -15.0)")
    p_pes.add_argument("--C3", type=float, default=-8.0, help="C3 coefficient in MeV (default: -8.0)")
    p_pes.add_argument("--C4", type=float, default=40.0, help="C4 coefficient in MeV (default: 40.0)")
    p_pes.add_argument("--C5", type=float, default=0.0, help="C5 coefficient in MeV (default: 0.0)")
    p_pes.add_argument("--C6", type=float, default=20.0, help="C6 coefficient in MeV (default: 20.0)")
    p_pes.add_argument("--C6-prime", type=float, default=0.0, help="C6' triaxial coefficient in MeV (default: 0.0)")
    p_pes.add_argument("--preset", type=str, choices=["prolate", "oblate", "triaxial_rigid", "gamma_soft"], help="Preset scenario")
    p_pes.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_pes.set_defaults(func=cmd_pes)

    # HPGe Digital Pulse Processing, PZC & Ballistic Deficit
    p_hp = subparsers.add_parser("hpge", help="HPGe digital pulse processing, pole-zero cancellation and ballistic deficit")
    p_hp.add_argument("--tc-ns", type=float, default=350.0, help="Charge collection time in ns (default: 350.0)")
    p_hp.add_argument("--trise-ns", type=float, default=2000.0, help="Trapezoid rise time in ns (default: 2000.0)")
    p_hp.add_argument("--tflat-ns", type=float, default=800.0, help="Trapezoid flat-top in ns (default: 800.0)")
    p_hp.add_argument("--tau-preamp", type=float, default=50.0, help="Preamp decay time in us (default: 50.0)")
    p_hp.add_argument("--tau-pz", type=float, default=50.0, help="PZ time setting in us (default: 50.0)")
    p_hp.add_argument("--rate-cps", type=float, default=50000.0, help="Input count rate in cps (default: 50000.0)")
    p_hp.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_hp.set_defaults(func=cmd_hpge)

    # 3D TAC Chiral Geometry & Volume Metric
    p_ch = subparsers.add_parser("chiral", help="3D tilted axis cranking (TAC) chiral geometry and aplanarity volume metric")
    p_ch.add_argument("--jp", type=float, default=5.5, help="Valence proton j_p (default: 5.5 for h11/2)")
    p_ch.add_argument("--jn", type=float, default=5.5, help="Valence neutron j_n (default: 5.5 for h11/2)")
    p_ch.add_argument("--Rm", type=float, default=8.0, help="Intermediate axis core rotation R_m (default: 8.0)")
    p_ch.add_argument("--Rs", type=float, default=0.5, help="Short axis core rotation R_s (default: 0.5)")
    p_ch.add_argument("--Rl", type=float, default=0.5, help="Long axis core rotation R_l (default: 0.5)")
    p_ch.add_argument("--delta-e-keV", type=float, default=None, help="Energy difference between doublet bands in keV")
    p_ch.add_argument("--bm1-ratio", type=float, default=1.1, help="B(M1)_in / B(M1)_out ratio (default: 1.1)")
    p_ch.add_argument("--be2-ratio", type=float, default=1.05, help="B(E2)_Band1 / B(E2)_Band2 ratio (default: 1.05)")
    p_ch.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_ch.set_defaults(func=cmd_chiral)

    # Beta Decay Phase Space & log(ft)
    p_bt = subparsers.add_parser("beta", help="Beta decay phase space factor f(Z,Q), comparative half-life log(ft) and CVC audit")
    p_bt.add_argument("-Q", "--q-beta", type=float, required=True, help="Beta decay Q-value in MeV")
    p_bt.add_argument("-T", "--t12", type=float, required=True, help="Total half-life in seconds")
    p_bt.add_argument("-Z", "--zdaughter", type=int, required=True, help="Daughter atomic number Z_daughter")
    p_bt.add_argument("-A", "--mass", type=int, required=True, help="Mass number A")
    p_bt.add_argument("--br", type=float, default=1.0, help="Branching ratio (default: 1.0)")
    p_bt.add_argument("--mode", type=str, default="beta_minus", choices=["beta_minus", "beta_plus"], help="Decay mode")
    p_bt.add_argument("--cvc-check", action="store_true", help="Perform superallowed 0+->0+ CVC & V_ud audit")
    p_bt.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_bt.set_defaults(func=cmd_beta)

    # Gallagher-Moszkowski (GM) Rules & Newby Shift
    p_gm = subparsers.add_parser("gm", help="Gallagher-Moszkowski (GM) coupling rules and Newby shift for deformed odd-odd nuclei")
    p_gm.add_argument("--omega-p", type=float, default=2.5, help="Proton Omega_p (default: 2.5)")
    p_gm.add_argument("--lambda-p", type=int, default=2, help="Proton Lambda_p (default: 2)")
    p_gm.add_argument("--omega-n", type=float, default=2.5, help="Neutron Omega_n (default: 2.5)")
    p_gm.add_argument("--lambda-n", type=int, default=3, help="Neutron Lambda_n (default: 3)")
    p_gm.add_argument("--A", type=int, default=130, help="Mass number A (default: 130)")
    p_gm.add_argument("--A-rot", type=float, default=20.0, help="Rotational constant A_rot in keV (default: 20.0)")
    p_gm.add_argument("--newby-shift", type=float, default=30.0, help="Newby shift a_N in keV for K=0 (default: 30.0)")
    p_gm.add_argument("--json", action="store_true", help="Output results in JSON format")
    p_gm.set_defaults(func=cmd_gm)

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
