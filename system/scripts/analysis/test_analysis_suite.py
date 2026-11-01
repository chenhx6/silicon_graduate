#!/usr/bin/env python3
"""
Unit & Regression Test Suite for Nuclear Analysis Tools.

Tests:
  1. heavy_ion_kinematics: checks Coulomb barrier, CM energy, recoil velocity.
  2. angular_distribution_solver: checks Legendre fit, dual root solver, and degeneracy preservation.
  3. digital_trapezoidal_filter: checks Jordanov recursion and amplitude preservation.
  4. gamma_peak_fitting: checks Gaussian + Step model convergence and area extraction.
  5. dco_polarization_analyzer: checks DCO ratio for dipole/quadrupole and polarization sensitivity.
  6. lifetime_lineshape_calculator: checks stopping time, DSAM attenuation inversion, and B(E2).
  7. coincidence_intensity_balancer: checks 3-point background subtraction and intensity balancing.
  8. routhian_alignment_analyzer: checks rotational frequency, alignment ix, and Harris baseline.
  9. ensdf_crosswalk_parser: checks ENSDF fixed-width parsing and in-beam crosswalk matching.
  10. excitation_function_calculator: checks target energy loss, yield-to-cross-section inversion, and resonance fit.
  11. magnetic_rotation_shears_calculator: checks shears angle, B(M1) quenching, and band termination.
  12. shape_coexistence_e0_calculator: checks electronic Omega_K factor, rho^2(E0) extraction, and two-state mixing.
  13. moment_of_inertia_spin_analyzer: checks J1, J2 moments of inertia and floating band spin inversion.
  14. coulex_kumar_invariant_calculator: checks safe Coulex energy, reorientation Q_s, and Kumar invariants.
  15. tpsm_band_diagram_calculator: checks 3D projected energy, band crossing Ic, and alignment.
  16. octupole_parity_doublet_calculator: checks parity splitting delta_E, B(E1)/B(E2), and intrinsic D0.
  17. signature_inversion_analyzer: checks signature splitting Delta_E, inversion crossing I_inv, and S(I).
  18. superdeformation_decayout_calculator: checks SD/TSD J2 plateau flatness and decay-out barrier tunneling.
  19. ibm_dynamical_symmetry_analyzer: checks R4/2 ratio, Casten triangle phase, and O(6) degeneracy.
  20. ado_polarization_joint_analyzer: checks ADO ratio, Clover asymmetry conversion, and joint profile fit.
  21. side_feeding_deconvolution_calculator: checks effective F-factor, side-feeding delay deconvolution, and Qt bias.
  22. internal_conversion_bricc_calculator: checks ICC multipolarity hierarchy, mixed transition alpha, and discrimination.
  23. vacuum_deorientation_calculator: checks G2/G4 attenuation factors and angular distribution deorientation restoration.
  24. tidal_wave_dynamics_calculator: checks tidal wave surface velocity, B(E2) linear scaling, and dynamic beta2.
"""

import sys
import numpy as np

from heavy_ion_kinematics import calculate_kinematics, doppler_shift, doppler_broadening
from angular_distribution_solver import angular_distribution_model, fit_angular_distribution, solve_delta_dual_roots
from digital_trapezoidal_filter import synthesize_preamp_pulse, apply_trapezoidal_filter, extract_trapezoid_amplitude
from gamma_peak_fitting import single_peak_model, fit_single_gamma_peak
from dco_polarization_analyzer import calculate_dco_ratio, calculate_linear_polarization, joint_dco_polarization_fit
from lifetime_lineshape_calculator import calculate_stopping_time_alpha, dsam_invert_lifetime, calculate_absolute_transition_strengths
from coincidence_intensity_balancer import three_point_background_subtraction, hpge_efficiency_radware, check_level_intensity_balance
from routhian_alignment_analyzer import calculate_alignment_and_routhians, fit_harris_reference
from ensdf_crosswalk_parser import parse_ensdf_records, crosswalk_match
from excitation_function_calculator import calculate_target_energy_loss, extract_cross_section_from_yield, fit_excitation_function
from magnetic_rotation_shears_calculator import calculate_shears_angle, calculate_magnetic_rotation_bm1, shears_band_profile
from shape_coexistence_e0_calculator import calculate_omega_k_e0, extract_rho2_e0_from_lifetime, invert_two_state_mixing
from moment_of_inertia_spin_analyzer import calculate_moments_of_inertia, invert_floating_band_spin
from coulex_kumar_invariant_calculator import calculate_safe_coulex_energy, reorientation_static_quadrupole, calculate_kumar_invariants
from tpsm_band_diagram_calculator import calculate_effective_moi_tpsm, generate_tpsm_band_diagram
from octupole_parity_doublet_calculator import calculate_parity_splitting, calculate_b_e1_over_b_e2, extract_intrinsic_dipole_moment
from signature_inversion_analyzer import calculate_staggering_parameter_s, calculate_signature_splitting, detect_inversion_crossing
from superdeformation_decayout_calculator import evaluate_superdeformation_flatness, model_decayout_tunneling
from ibm_dynamical_symmetry_analyzer import calculate_ibm_energy_ratios, classify_casten_triangle_phase
from ado_polarization_joint_analyzer import calculate_ado_ratio, convert_clover_counts_to_polarization, joint_ado_polarization_scan
from side_feeding_deconvolution_calculator import calculate_effective_f_factor, deconvolve_side_feeding_lifetime
from internal_conversion_bricc_calculator import calculate_bricc_icc, calculate_mixed_icc, discriminate_multipolarity
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


def test_heavy_ion_kinematics():
    print("Testing heavy_ion_kinematics...")
    res = calculate_kinematics(36, 16, 100, 42, 150.0)
    assert 110.0 < res["E_cm_MeV"] < 111.0, f"Unexpected E_cm: {res['E_cm_MeV']}"
    assert 85.0 < res["V_B_MeV"] < 95.0, f"Unexpected V_B: {res['V_B_MeV']}"
    assert res["beta_v_over_c"] > 0.015, f"Unexpected beta: {res['beta_v_over_c']}"

    E0 = 1000.0
    E_forward = doppler_shift(E0, res["beta_v_over_c"], 0.0)
    E_backward = doppler_shift(E0, res["beta_v_over_c"], 180.0)
    assert E_forward > E0, f"Forward Doppler shift should be > E0: {E_forward}"
    assert E_backward < E0, f"Backward Doppler shift should be < E0: {E_backward}"
    print("  ✓ heavy_ion_kinematics passed.")


def test_angular_distribution_and_dual_roots():
    print("Testing angular_distribution_solver...")
    thetas = [30.0, 55.0, 90.0, 125.0, 150.0]
    y_true = angular_distribution_model(thetas, 5000.0, 0.30, -0.10)
    errors = np.sqrt(y_true)
    fit_res = fit_angular_distribution(thetas, y_true, errors)
    assert abs(fit_res["a2"] - 0.30) < 0.02, f"Fitted a2 mismatch: {fit_res['a2']}"
    assert abs(fit_res["a4"] - (-0.10)) < 0.02, f"Fitted a4 mismatch: {fit_res['a4']}"

    F2_11, F2_12, F2_22 = -0.3742, 0.4472, 0.1265
    roots = solve_delta_dual_roots(-0.40, F2_11, F2_12, F2_22, alpha2=0.85)
    assert roots is not None, "Roots should exist for a2 = -0.40"
    d1 = roots["delta_small_root (M1 dominated)"]
    d2 = roots["delta_large_root (E2 dominated)"]
    assert abs(d1) < abs(d2), "Root ordering failed"

    a2_from_d1 = 0.85 * (F2_11 + 2*d1*F2_12 + d1**2*F2_22) / (1 + d1**2)
    a2_from_d2 = 0.85 * (F2_11 + 2*d2*F2_12 + d2**2*F2_22) / (1 + d2**2)
    assert abs(a2_from_d1 - a2_from_d2) < 1e-7, "Dual root mathematical degeneracy violated!"
    print("  ✓ angular_distribution_solver passed.")


def test_digital_trapezoidal_filter():
    print("Testing digital_trapezoidal_filter...")
    true_amp = 800.0
    tau = 400.0
    k = 40
    m = 25
    trig = 100
    length = 1000
    step_wave = np.zeros(length)
    step_wave[trig:] = true_amp * np.exp(-np.arange(length - trig) / tau)
    shaped_step = apply_trapezoidal_filter(step_wave, k=k, m=m, tau_decay=tau)
    meas_amp = extract_trapezoid_amplitude(shaped_step)
    assert abs(meas_amp - true_amp) / true_amp < 0.005, f"Step trapezoid error: {meas_amp} vs {true_amp}"

    syn_wave = synthesize_preamp_pulse(length=1500, t_rise=15, tau_decay=tau,
                                       amplitude=true_amp, noise_sigma=0.0,
                                       baseline=0.0, trigger_pos=trig)
    shaped_syn = apply_trapezoidal_filter(syn_wave, k=k, m=m, tau_decay=tau)
    plateau = shaped_syn[trig + k + 15 : trig + k + m]
    assert len(plateau) > 5, "Plateau width should be positive"
    assert np.std(plateau) < 1e-4, f"Plateau is not flat: std={np.std(plateau)}"
    print("  ✓ digital_trapezoidal_filter passed.")


def test_gamma_peak_fitting():
    print("Testing gamma_peak_fitting...")
    ch = np.linspace(300.0, 325.0, 125)
    centroid_true = 312.4
    fwhm_true = 2.0
    area_true = 8000.0
    step_true = 15.0
    b0_true = 50.0
    b1_true = -0.2

    sigma_true = fwhm_true / 2.35482
    y = single_peak_model(ch, centroid_true, sigma_true, area_true * (ch[1]-ch[0]), step_true, b0_true, b1_true)
    res = fit_single_gamma_peak(ch, y)
    assert abs(res["centroid"] - centroid_true) < 0.05, f"Centroid mismatch: {res['centroid']}"
    assert abs(res["fwhm"] - fwhm_true) < 0.05, f"FWHM mismatch: {res['fwhm']}"
    assert abs(res["net_area"] - area_true) / area_true < 0.02, f"Area mismatch: {res['net_area']}"
    print("  ✓ gamma_peak_fitting passed.")


def test_dco_polarization_analyzer():
    print("Testing dco_polarization_analyzer...")
    F2_11, F2_12, F2_22, F4_22 = -0.3742, 0.4472, 0.1265, -0.4286
    r_e2 = calculate_dco_ratio(30.0, 90.0, delta=100.0, F2_11=F2_11, F2_12=F2_12, F2_22=F2_22, F4_22=F4_22)
    assert 0.90 < r_e2 < 1.30, f"Stretched E2 DCO ratio should be approx 1.0: {r_e2}"
    r_m1 = calculate_dco_ratio(30.0, 90.0, delta=0.0, F2_11=F2_11, F2_12=F2_12, F2_22=F2_22, F4_22=F4_22)
    assert 0.50 < r_m1 < 0.80, f"Dipole DCO ratio should be approx 0.6: {r_m1}"
    print("  ✓ dco_polarization_analyzer passed.")


def test_lifetime_lineshape_calculator():
    print("Testing lifetime_lineshape_calculator...")
    alpha = calculate_stopping_time_alpha(131, 58, 0.025, "Au")
    assert 0.8 < alpha < 1.3, f"Stopping time alpha out of range: {alpha}"
    tau = dsam_invert_lifetime(0.50, alpha)
    assert abs(tau - alpha) < 1e-4, f"F=0.5 must yield tau == alpha: {tau} vs {alpha}"
    strengths = calculate_absolute_transition_strengths(tau_ps=1.0, E_gamma_keV=500.0, delta=100.0, I_initial=10)
    assert strengths["B_E2_e2b2"] > 0.1, "B(E2) calculation error"
    print("  ✓ lifetime_lineshape_calculator passed.")


def test_coincidence_intensity_balancer():
    print("Testing coincidence_intensity_balancer...")
    p = np.array([100.0, 100.0, 500.0, 100.0, 100.0])
    bl = np.array([50.0, 50.0, 50.0, 50.0, 50.0])
    br = np.array([50.0, 50.0, 50.0, 50.0, 50.0])
    sub, err, fB = three_point_background_subtraction(p, bl, br, w_peak=5, w_bg_left=5, w_bg_right=5)
    assert abs(fB - 0.5) < 1e-5, f"Background factor fB error: {fB}"
    assert abs(sub[2] - 450.0) < 1e-4, f"Subtracted peak error: {sub[2]}"

    inflows = [{"name": "in1", "net_area": 1000.0, "efficiency": 0.1, "alpha_tot": 0.0}]
    outflows = [{"name": "out1", "net_area": 1000.0, "efficiency": 0.1, "alpha_tot": 0.0}]
    bal = check_level_intensity_balance(inflows, outflows)
    assert bal["is_balanced_within_3sigma"] == True, "Balanced node failed test"
    assert abs(bal["difference_out_minus_in"]) < 1e-4, "Difference should be zero"
    print("  ✓ coincidence_intensity_balancer passed.")


def test_routhian_alignment_analyzer():
    print("Testing routhian_alignment_analyzer...")
    spins = [2.0, 4.0, 6.0, 8.0, 10.0]
    energies = [25.0 * I * (I + 1.0) for I in spins]
    res = calculate_alignment_and_routhians(spins, energies, J0=20.0, J1=0.0)
    assert len(res["omega_MeV"]) == 4, "Should have 4 cascade transitions"
    assert res["omega_MeV"][0] < res["omega_MeV"][-1], "Omega should increase with spin"
    assert abs(res["ix_hbar"][0]) < 5.0, "Alignment baseline sanity check"
    print("  ✓ routhian_alignment_analyzer passed.")


def test_ensdf_crosswalk_parser():
    print("Testing ensdf_crosswalk_parser...")
    ensdf_sample = """
 131CE  L           0.0                 (7/2+)      10.2 M
 131CE  L         161.8               1 (11/2-)     4.8 PS
 131CE  G         161.8       1      100              M2+E3     -0.15          0.235
 131CE  L         450.2               2 (15/2-)
 131CE  G         288.4       2      100              E2                       0.045
"""
    levels = parse_ensdf_records(ensdf_sample)
    assert len(levels) == 3, f"Parsed levels should be 3: got {len(levels)}"
    cw = crosswalk_match([162.0, 500.0], levels, tolerance_keV=1.0)
    assert len(cw["matched"]) == 1, "Should match 1 transition"
    assert cw["unmatched_new_candidates"] == [500.0], "500 keV should be unmatched"
    print("  ✓ ensdf_crosswalk_parser passed.")


def test_excitation_function_calculator():
    print("Testing excitation_function_calculator...")
    eloss = calculate_target_energy_loss(150.0, 36, 16, 100, 42, 1.0)
    assert 1.0 < eloss["delta_E_MeV"] < 20.0, f"Target energy loss error: {eloss['delta_E_MeV']}"
    cs = extract_cross_section_from_yield(peak_area=10000.0, efficiency=0.05, branching_ratio=1.0,
                                          beam_current_pnA=1.0, duration_hours=1.0,
                                          target_thickness_mg_cm2=1.0, target_mass_A=100.0)
    assert cs["sigma_mb"] > 0.0, "Cross section must be positive"
    e_pts = [140.0, 150.0, 160.0]
    s_pts = [100.0, 300.0, 80.0]
    errs = [10.0, 20.0, 10.0]
    fit_res = fit_excitation_function(e_pts, s_pts, errs)
    assert 145.0 < fit_res["E_opt_MeV"] < 155.0, f"Peak position error: {fit_res['E_opt_MeV']}"
    print("  ✓ excitation_function_calculator passed.")


def test_magnetic_rotation_shears_calculator():
    print("Testing magnetic_rotation_shears_calculator...")
    j_pi = 10.5
    j_nu = 5.5
    bm1_head, _ = calculate_magnetic_rotation_bm1(12.0, j_pi, j_nu)
    assert bm1_head > 3.0, f"Bandhead B(M1) should be large: {bm1_head}"
    bm1_max, _ = calculate_magnetic_rotation_bm1(16.0, j_pi, j_nu)
    assert abs(bm1_max) < 1e-4, f"Band termination B(M1) must be zero: {bm1_max}"
    print("  ✓ magnetic_rotation_shears_calculator passed.")


def test_shape_coexistence_e0_calculator():
    print("Testing shape_coexistence_e0_calculator...")
    omega_k = calculate_omega_k_e0(Z=56, A=130, delta_E_keV=850.0)
    assert omega_k > 1e6, f"Omega_K out of reasonable bounds: {omega_k}"
    res = extract_rho2_e0_from_lifetime(tau_ps=100.0, Z=56, A=130, delta_E_keV=850.0)
    assert res["rho2"] > 0.0, "Monopole strength must be positive"
    mix = invert_two_state_mixing(0.0, 850.0, res["rho2"], Z=56, beta1=0.15)
    assert mix["beta2"] > mix["beta1"], "Deformation jump must be positive"
    print("  ✓ shape_coexistence_e0_calculator passed.")


def test_moment_of_inertia_spin_analyzer():
    print("Testing moment_of_inertia_spin_analyzer...")
    gammas = [150.0, 250.0, 350.0]
    data = calculate_moments_of_inertia(gammas, initial_spin=4.0)
    assert len(data["J2_dynamical_hbar2_per_MeV"]) == 2, "Should have 2 J2 points"
    assert abs(data["J2_dynamical_hbar2_per_MeV"][0] - 40.0) < 1e-4, f"J2 error: {data['J2_dynamical_hbar2_per_MeV'][0]}"
    inv = invert_floating_band_spin(gammas, is_half_integer=False, J0_expected=40.0)
    assert abs(inv["best_candidate_spin_I0"] - 4.0) <= 1.0, f"Inverted spin error: {inv['best_candidate_spin_I0']}"
    print("  ✓ moment_of_inertia_spin_analyzer passed.")


def test_coulex_kumar_invariant_calculator():
    print("Testing coulex_kumar_invariant_calculator...")
    safe = calculate_safe_coulex_energy(130, 56, 208, 82)
    assert 500.0 < safe["E_lab_safe_MeV"] < 650.0, f"Safe energy out of bounds: {safe['E_lab_safe_MeV']}"
    reorient = reorientation_static_quadrupole(56, 130, M22_diagonal_eb=-0.55)
    assert reorient["Q_s_eb"] < 0.0, "Negative diagonal matrix element must yield prolate Q_s < 0"
    inv = calculate_kumar_invariants([1.15, 0.35], -0.55, Z=56, A=130)
    assert 15.0 < inv["gamma_eff_deg"] < 30.0, f"Effective gamma angle error: {inv['gamma_eff_deg']}"
    assert 0.15 < inv["beta_eff_rms"] < 0.35, f"Effective beta error: {inv['beta_eff_rms']}"
    print("  ✓ coulex_kumar_invariant_calculator passed.")


def test_tpsm_band_diagram_calculator():
    print("Testing tpsm_band_diagram_calculator...")
    spins = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    diag = generate_tpsm_band_diagram(spins, epsilon2=0.22, gamma_deg=25.0, A=132)
    assert diag["J_eff_core"] > 20.0, f"J_eff_core error: {diag['J_eff_core']}"
    assert diag["crossing_spin_Ic"] is not None, "Should detect microscopic band crossing"
    assert 14.0 < diag["crossing_spin_Ic"] < 20.0, f"Crossing spin Ic out of expected bounds: {diag['crossing_spin_Ic']}"
    print("  ✓ tpsm_band_diagram_calculator passed.")


def test_octupole_parity_doublet_calculator():
    print("Testing octupole_parity_doublet_calculator...")
    pos_spins = [0, 2, 4]
    pos_energies = [0.0, 100.0, 300.0]
    neg_spins = [1, 3]
    neg_energies = [150.0, 320.0]
    split = calculate_parity_splitting(pos_spins, pos_energies, neg_spins, neg_energies)
    assert len(split) == 2, f"Should match 2 parity doublet points: got {len(split)}"
    assert abs(split[0]["delta_E_keV"] - 100.0) < 1e-4, f"Parity splitting error: {split[0]['delta_E_keV']}"
    ratios = calculate_b_e1_over_b_e2(E_gamma_E1_keV=200.0, I_gamma_E1=50.0, E_gamma_E2_keV=400.0, I_gamma_E2=100.0)
    assert ratios["B_E1_over_B_E2_fm2"] > 0.0, "B(E1)/B(E2) must be positive"
    D0 = extract_intrinsic_dipole_moment(ratios["B_E1_over_B_E2_fm2"], I_initial=5.0, Qt_eb=3.0)
    assert D0 > 0.0, "D0 must be positive"
    print("  ✓ octupole_parity_doublet_calculator passed.")


def test_signature_inversion_analyzer():
    print("Testing signature_inversion_analyzer...")
    fav_spins = [8, 10, 12, 14, 16]
    fav_energies = [0.0, 300.0, 700.0, 1200.0, 1800.0]
    unfav_spins = [9, 11, 13, 15]
    unfav_energies = [120.0, 480.0, 960.0, 1550.0]
    split = calculate_signature_splitting(fav_spins, fav_energies, unfav_spins, unfav_energies)
    assert len(split) == 4, f"Should match 4 splitting points: got {len(split)}"
    diag = detect_inversion_crossing(split)
    assert diag["has_inversion"] == True, "Should detect signature inversion"
    assert diag["I_inv"] is not None, "Should locate crossing spin"
    assert 11.0 < diag["I_inv"] < 15.0, f"Crossing spin out of bounds: {diag['I_inv']}"
    print("  ✓ signature_inversion_analyzer passed.")


def test_superdeformation_decayout_calculator():
    print("Testing superdeformation_decayout_calculator...")
    gammas = [780.0, 840.0, 900.0, 960.0, 1020.0]
    flat = evaluate_superdeformation_flatness(gammas)
    assert flat["is_superdeformed"] == True, "Should identify SD plateau"
    assert flat["relative_std_percent"] < 1.0, f"RSD error: {flat['relative_std_percent']}"
    spins = [20.0, 22.0, 24.0]
    intens = [0.1, 0.9, 1.0]
    dec = model_decayout_tunneling(spins, intens, gammas[:3])
    assert dec["I_decay"] == 20.0, f"Decay spin error: {dec['I_decay']}"
    print("  ✓ superdeformation_decayout_calculator passed.")


def test_ibm_dynamical_symmetry_analyzer():
    print("Testing ibm_dynamical_symmetry_analyzer...")
    r_u5 = calculate_ibm_energy_ratios(500.0, 1000.0)
    c_u5 = classify_casten_triangle_phase(r_u5["R42"])
    assert "U(5)" in c_u5["phase_name"], f"U(5) error: {c_u5['phase_name']}"

    r_o6 = calculate_ibm_energy_ratios(357.2, 908.1, E_2_2_keV=901.7)
    c_o6 = classify_casten_triangle_phase(r_o6["R42"], r_o6["R22"])
    assert "O(6)" in c_o6["phase_name"], f"O(6) error: {c_o6['phase_name']}"

    r_su3 = calculate_ibm_energy_ratios(100.0, 333.0)
    c_su3 = classify_casten_triangle_phase(r_su3["R42"])
    assert "SU(3)" in c_su3["phase_name"], f"SU(3) error: {c_su3['phase_name']}"
    print("  ✓ ibm_dynamical_symmetry_analyzer passed.")


def test_ado_polarization_joint_analyzer():
    print("Testing ado_polarization_joint_analyzer...")
    F2_11, F2_12, F2_22, F4_22 = -0.3742, 0.4472, 0.1265, -0.4286
    r_e2 = calculate_ado_ratio(30.0, 90.0, delta=100.0, F2_11=F2_11, F2_12=F2_12, F2_22=F2_22, F4_22=F4_22)
    assert 1.15 < r_e2 < 1.45, f"Stretched E2 ADO error: {r_e2}"
    r_m1 = calculate_ado_ratio(30.0, 90.0, delta=0.0, F2_11=F2_11, F2_12=F2_12, F2_22=F2_22, F4_22=F4_22)
    assert 0.60 < r_m1 < 0.90, f"Dipole ADO error: {r_m1}"
    clov = convert_clover_counts_to_polarization(N_perp=2000, N_par=2000, Q_factor=0.20)
    assert abs(clov["polarization_P"]) < 1e-4, "Zero polarization error"
    print("  ✓ ado_polarization_joint_analyzer passed.")


def test_side_feeding_deconvolution_calculator():
    print("Testing side_feeding_deconvolution_calculator...")
    f_eff_0 = calculate_effective_f_factor(tau_level_ps=1.0, tau_feed_ps=0.0, f_feed=0.5, alpha_ps=1.0)
    assert abs(f_eff_0 - 0.5) < 1e-4, f"Zero feed time error: {f_eff_0}"
    alpha = 1.05
    f_exp = 0.55
    res = deconvolve_side_feeding_lifetime(f_exp, tau_feed_ps=0.35, f_feed=0.40, alpha_ps=alpha)
    assert res["tau_intrinsic_ps"] < res["tau_apparent_ps"], "Intrinsic lifetime must be shorter than apparent"
    assert abs(res["F_measured"] - 0.55) < 1e-4, "F_measured preservation error"
    print("  ✓ side_feeding_deconvolution_calculator passed.")


def test_internal_conversion_bricc_calculator():
    print("Testing internal_conversion_bricc_calculator...")
    icc_e1 = calculate_bricc_icc(Z=58, E_gamma_keV=150.0, multipolarity="E1")
    icc_m1 = calculate_bricc_icc(Z=58, E_gamma_keV=150.0, multipolarity="M1")
    icc_e2 = calculate_bricc_icc(Z=58, E_gamma_keV=150.0, multipolarity="E2")
    assert icc_e1["alpha_K"] < icc_m1["alpha_K"] < icc_e2["alpha_K"], "ICC multipolarity hierarchy error"
    mixed = calculate_mixed_icc(Z=58, E_gamma_keV=150.0, delta=1.0)
    expected = 0.5 * (icc_m1["alpha_total"] + icc_e2["alpha_total"])
    assert abs(mixed["alpha_total_mixed"] - expected) < 1e-4, "Mixed ICC calculation error"
    disc = discriminate_multipolarity(Z=58, E_gamma_keV=150.0, alpha_exp=icc_e2["alpha_total"])
    assert disc["best_multipolarity"] == "E2", f"Multipolarity discrimination error: {disc['best_multipolarity']}"
    print("  ✓ internal_conversion_bricc_calculator passed.")


def test_vacuum_deorientation_calculator():
    print("Testing vacuum_deorientation_calculator...")
    att_short = calculate_attenuation_factors(tau_level_ps=1.0, Z=58, beta_recoil=0.025)
    assert att_short["G2"] > 0.99, f"Short lifetime G2 error: {att_short['G2']}"
    att_long = calculate_attenuation_factors(tau_level_ps=1000.0, Z=58, beta_recoil=0.025)
    assert att_long["G2"] < att_short["G2"], "G2 should decrease with lifetime"
    corr = correct_measured_angular_distribution(a2_meas=-0.20, a4_meas=0.0, G2=0.50, G4=0.50)
    assert abs(corr["A2_true"] - (-0.40)) < 1e-4, f"Restoration error: {corr['A2_true']}"
    print("  ✓ vacuum_deorientation_calculator passed.")


def test_tidal_wave_dynamics_calculator():
    print("Testing tidal_wave_dynamics_calculator...")
    spins = [2, 4, 6, 8, 10]
    be2_linear = [0.10, 0.20, 0.30, 0.40, 0.50]
    scaling = test_b_e2_linear_scaling(spins, be2_linear)
    assert scaling["is_tidal_wave_scaling"] == True, "Should identify tidal wave linear scaling"
    assert scaling["R_squared"] > 0.99, f"R^2 should be near 1.0: {scaling['R_squared']}"
    dyn = reconstruct_dynamic_beta2(spins, be2_linear, Z=46, A=102)
    assert dyn["beta2_final"] > dyn["beta2_initial"], "Dynamic stretching must be positive"
    print("  ✓ tidal_wave_dynamics_calculator passed.")



def test_gamow_teller_ikeda_quenching_calculator():
    print("Testing gamow_teller_ikeda_quenching_calculator...")
    # Target 130Te: Z=52, A=130, N=78, N-Z=26, S_Ikeda = 3 * 26 = 78.0
    ik = calculate_ikeda_sum_rule(52, 130)
    assert ik["ikeda_sum_rule_limit"] == 78.0, f"Expected 78.0, got {ik['ikeda_sum_rule_limit']}"

    # Typical experimental quenching test: S_exp = 43.0, S_plus = 0.0
    ev = evaluate_ga_quenching(52, 130, S_minus_exp=43.0, S_plus_exp=0.0)
    assert abs(ev["recovery_fraction"] - (43.0 / 78.0)) < 1e-4
    assert 0.70 < ev["quenching_factor_q"] < 0.80, f"Quenching factor should be in 0.70-0.80, got {ev['quenching_factor_q']}"
    assert ev["0nu_half_life_prolongation"] > 2.5, "0nu2beta prolongation should be > 2.5x"

    # Cross-section conversion test
    cs = convert_cross_section_to_b_gt(diff_sigma_0deg_mb_sr=15.0, unit_sigma_hat_mb_sr=3.0)
    assert abs(cs["B_GT"] - 5.0) < 1e-5
    print("  ✓ gamow_teller_ikeda_quenching_calculator passed.")


def test_halo_breakup_momentum_calculator():
    print("Testing halo_breakup_momentum_calculator...")
    # 11Li: S_2n = 369 keV, Ac=9, Ah=2
    hj = calculate_hansen_jonson_fwhm(S_n_keV=369.0, A_core=9.0, A_halo=2.0)
    assert 40.0 < hj["fwhm_MeV_c"] < 46.0, f"Expected FWHM ~43 MeV/c, got {hj['fwhm_MeV_c']}"
    assert 5.0 < hj["decay_length_fm"] < 6.5, f"Expected decay length ~5.8 fm, got {hj['decay_length_fm']}"

    # Inversion test
    inv = invert_separation_energy_from_fwhm(fwhm_MeV_c=hj["fwhm_MeV_c"], A_core=9.0, A_halo=2.0)
    assert abs(inv["extracted_S_n_keV"] - 369.0) < 0.1, f"Inversion mismatch: {inv['extracted_S_n_keV']}"

    # Goldhaber baseline comparison
    gold = calculate_goldhaber_width(A_projectile=11.0, A_fragment=9.0, sigma_0_MeV_c=90.0)
    assert gold["fwhm_Goldhaber_MeV_c"] > 250.0, "Goldhaber width should be > 250 MeV/c"

    diag = diagnose_halo_signature(hj["fwhm_MeV_c"], gold["fwhm_Goldhaber_MeV_c"])
    assert diag["is_halo_signature"] == True, "Should identify prominent halo"

    # Soft E1 cluster sum rule
    soft = calculate_cluster_soft_e1_sum_rule(Z_core=3, A_core=9.0, Z_halo=0, A_halo=2.0, r_rms_halo_fm=5.5)
    assert soft["B_E1_cluster_sum_e2_fm2"] > 1.0, "Cluster soft E1 sum should be large"

    # Glauber matter radius inversion
    rad = estimate_matter_radius_from_reaction_cross_section(sigma_R_mb=1060.0, A_p=11.0, A_t=12.0)
    assert rad["R_rms_projectile_fm"] > 2.7, "11Li matter radius should be > 2.7 fm"
    assert rad["relative_radius_expansion_percent"] > 25.0, "Radius expansion should be > 25%"
    print("  ✓ halo_breakup_momentum_calculator passed.")


def test_fission_barrier_superheavy_calculator():
    print("Testing fission_barrier_superheavy_calculator...")
    # 238U: Z=92, A=238
    u = calculate_liquid_drop_fissility(92, 238)
    assert 0.75 < u["fissility_x"] < 0.80, f"U-238 fissility mismatch: {u['fissility_x']}"
    assert 5.5 < u["liquid_drop_barrier_MeV"] < 7.0, f"U-238 LDM barrier mismatch: {u['liquid_drop_barrier_MeV']}"

    # 298Fl superheavy: Z=114, A=298
    fl = calculate_liquid_drop_fissility(114, 298)
    assert fl["fissility_x"] > 0.90, "Fl-298 fissility should be > 0.9"
    assert fl["liquid_drop_barrier_MeV"] < 0.5, "Fl-298 LDM barrier should be nearly zero"

    # Hill-Wheeler transmission symmetry at barrier peak
    hw_peak = calculate_hill_wheeler_penetration(E_excitation_MeV=6.0, V_barrier_MeV=6.0)
    assert abs(hw_peak["transmission_probability"] - 0.5) < 1e-4, "T(E=V) must be exactly 0.5"

    # Vandenbosch-Huizenga Gamma_n / Gamma_f with thermal damping
    comp = calculate_gamma_n_over_gamma_f(E_star_MeV=38.0, B_n_MeV=7.2, B_f_nominal_MeV=6.5, A=292, B_f_ldm_MeV=0.5)
    assert comp["gamma_n_over_gamma_f"] < 0.01, f"Gamma_n / Gamma_f should be strongly suppressed, got {comp['gamma_n_over_gamma_f']}"

    # Superheavy synthesis multi-step estimation
    synth = estimate_superheavy_cross_section(sigma_cap_mb=10.0, P_cn=2e-4, E_star_initial_MeV=38.0,
                                             B_n_list_MeV=[7.2, 7.0, 6.8], B_f_list_MeV=[6.5, 6.5, 6.5],
                                             A_compound=292, B_f_ldm_MeV=0.5, xn=3)
    assert synth["P_surv_total"] > 0.0, "Survival probability must be strictly positive"
    assert synth["sigma_ER_pb"] > 0.0, "Residue cross section must be strictly positive"
    print("  ✓ fission_barrier_superheavy_calculator passed.")


def test_oslo_method_nld_gsf_analyzer():
    print("Testing oslo_method_nld_gsf_analyzer...")
    # Target 133I: D0=60 eV, It=0, Sn=7.8 MeV, A=133
    sn_calc = calculate_rho_at_sn(D0_eV=60.0, I_target=0.0, S_n_MeV=7.8, A=133)
    assert sn_calc["rho_Sn_MeV_inv"] > 1e5, f"Expected high level density at Sn, got {sn_calc['rho_Sn_MeV_inv']}"
    assert 4.5 < sn_calc["spin_cutoff_sigma"] < 7.0, f"Spin cutoff out of range: {sn_calc['spin_cutoff_sigma']}"

    # 3-Parameter Lie Group Invariance verification
    ex = np.linspace(1.0, 8.0, 15)
    eg = np.linspace(0.5, 7.5, 15)
    r = np.exp(0.5 * ex)
    t = 0.01 * (eg ** 2)
    inv = verify_oslo_lie_transformation_invariance(r, t, ex, eg, A_factor=1.8, alpha_slope=0.35, B_factor=2.4)
    assert inv["is_strictly_invariant"] == True, "Primary matrix must be strictly invariant under Lie transformation"
    assert inv["max_absolute_difference"] < 1e-12, f"Matrix difference exceeds tolerance: {inv['max_absolute_difference']}"

    # Low-Energy Enhancement (LEE) detection
    eg_lee = np.linspace(0.5, 3.5, 10)
    gsf_lee = 1e-7 * np.exp(-1.5 * eg_lee) + 1e-9
    lee = diagnose_low_energy_enhancement(eg_lee, gsf_lee)
    assert lee["has_lee"] == True, "Should detect distinct low-energy enhancement (upbend)"
    assert lee["enhancement_ratio"] > 2.0, "Enhancement ratio should be > 2x"
    print("  ✓ oslo_method_nld_gsf_analyzer passed.")


def test_band_termination_cns_calculator():
    print("Testing band_termination_cns_calculator...")
    # Valence max spin test: 109Sb configuration
    val = calculate_valence_maximum_spin(valence_orbitals_protons=[(5.5, 1)],
                                         valence_orbitals_neutrons=[(5.5, 2), (3.5, 4), (2.5, 2)])
    assert val["I_max_protons"] == 5.5, f"Expected 5.5, got {val['I_max_protons']}"
    assert val["I_max_neutrons"] == 22.0, f"Expected 22.0, got {val['I_max_neutrons']}"
    assert val["I_max_total"] == 27.5, f"Expected 27.5, got {val['I_max_total']}"

    # Transition quadrupole moment collapse test
    spins = [14.5, 16.5, 18.5, 20.5, 22.5, 24.5]
    qt_res = model_transition_quadrupole_collapse(spins, Q0_eb=2.85, I_start=14.5, I_term=24.5)
    assert qt_res["Q_t_drop_percent"] > 99.0, "Qt should drop by ~100% at termination"
    assert qt_res["trajectory"][-1]["Q_t_eb"] < 1e-10, "Qt at 60 deg oblate must be 0"

    # Rigid rotor cusp test
    energies = [2500, 3300, 4300, 5600, 7200, 9100, 11500]
    sp_rr = [10, 12, 14, 16, 18, 20, 22]
    rr = calculate_rigid_rotor_subtraction(sp_rr, energies, A=109)
    assert rr["cusp_spin"] == 20.0, f"Cusp spin mismatch: {rr['cusp_spin']}"

    # Diagnosis test
    diag = diagnose_smooth_band_termination(q_drop_percent=qt_res["Q_t_drop_percent"], j2_steep_dive=True, e_diff_cusp_found=True)
    assert diag["is_band_termination"] == True, "Should identify smooth band termination"
    print("  ✓ band_termination_cns_calculator passed.")


def test_tdpad_hyperfine_precession_calculator():
    print("Testing tdpad_hyperfine_precession_calculator...")
    # 128Cs: g = +0.59, B = 2.145 T
    larm = calculate_larmor_frequency(g_factor=0.59, B_external_Tesla=2.145)
    assert abs(larm["omega_L_rad_s"] - 6.061e7) < 1e5, f"omega_L mismatch: {larm['omega_L_rad_s']}"
    assert abs(larm["modulation_period_T_mod_ns"] - 51.83) < 0.05, f"T_mod mismatch: {larm['modulation_period_T_mod_ns']}"

    # Inversion test
    inv = invert_g_factor_from_period(T_mod_ns=larm["modulation_period_T_mod_ns"], B_external_Tesla=2.145)
    assert abs(inv["g_factor_magnitude"] - 0.59) < 1e-4, f"Inverted g mismatch: {inv['g_factor_magnitude']}"

    # R(t) time series test
    r_t = generate_tdpad_r_of_t(times_ns=[0.0, 10.0, 20.0], g_factor=0.59, B_Tesla=2.145, A2B2=0.25)
    assert abs(r_t["R_of_t"][0]) < 1e-10, "R(t=0) must be zero"
    assert r_t["amplitude_A"] > 0.15, "Amplitude out of range"

    # Three-vector chiral test
    pl = calculate_three_vector_chiral_gfactor(geometry="planar")
    apl = calculate_three_vector_chiral_gfactor(geometry="aplanar")
    assert pl["calculated_g_factor"] > apl["calculated_g_factor"], "Planar g must exceed aplanar g"

    # Quadrupole interaction test: 131Ce in Sn host
    qi = calculate_electric_quadrupole_frequency(Qs_eb=0.92, Vzz_1e21_V_m2=3.0, spin_I=4.5)
    assert 60.0 < qi["nu_Q_MHz"] < 75.0, f"nu_Q out of expected range: {qi['nu_Q_MHz']}"
    print("  ✓ tdpad_hyperfine_precession_calculator passed.")


def test_pairing_gap_separation_energy_calculator():
    print("Testing pairing_gap_separation_energy_calculator...")
    # S2n series test
    s2n_series = [
        {"N": 78, "S_2n_MeV": 14.5},
        {"N": 80, "S_2n_MeV": 13.8},
        {"N": 82, "S_2n_MeV": 13.1},
        {"N": 84, "S_2n_MeV": 9.2},   # 3.9 MeV magic cliff!
        {"N": 86, "S_2n_MeV": 8.3},
        {"N": 88, "S_2n_MeV": 7.5},
        {"N": 90, "S_2n_MeV": 7.4},   # 0.1 MeV anomalous flattening!
        {"N": 92, "S_2n_MeV": 6.5}
    ]
    magic = detect_shell_closure_drop(s2n_series, expected_magic=[82])
    assert magic[0]["is_shell_closure"] == True, "N=82 should be identified as shell closure"
    assert abs(magic[0]["shell_drop_delta_2n_MeV"] - 3.9) < 1e-4, f"Mismatch in shell drop: {magic[0]['shell_drop_delta_2n_MeV']}"

    # Shape transition detection
    trans = detect_shape_transition_anomaly(s2n_series)
    assert len(trans) > 0, "Should detect shape transition anomaly"
    assert trans[0]["N_transition"] == 90, f"Expected anomaly at N=90, got {trans[0]['N_transition']}"

    # 3-point and 5-point pairing gap
    gap3 = calculate_pairing_gap_3point(B_minus=1100.0, B_center=1107.0, B_plus=1116.2, is_odd_N=True)
    assert abs(gap3["delta_3point_MeV"] - 1.1) < 1e-4, f"3-point gap mismatch: {gap3['delta_3point_MeV']}"

    gap5 = calculate_pairing_gap_5point(B_m2=1091.5, B_m1=1100.0, B_0=1107.0, B_p1=1116.2, B_p2=1124.0, is_odd_N=True)
    assert 0.8 < gap5["delta_5point_MeV"] < 1.0, f"5-point gap mismatch: {gap5['delta_5point_MeV']}"

    # Empirical BCS comparison
    bcs = compare_empirical_bcs_gap(A=132)
    assert 0.9 < bcs["Delta_12_over_sqrt_A_MeV"] < 1.2, "Empirical gap out of range"
    print("  ✓ pairing_gap_separation_energy_calculator passed.")


def test_isgmr_breathing_mode_incompressibility_calculator():
    print("Testing isgmr_breathing_mode_incompressibility_calculator...")
    # 208Pb: E_gmr = 13.5 MeV, A=208, Z=82
    ka = calculate_ka_from_isgmr_energy(E_gmr_MeV=13.5, A=208)
    assert 128.0 < ka["K_A_MeV"] < 138.0, f"Expected Ka ~133 MeV, got {ka['K_A_MeV']}"

    # Leptodermous expansion for 208Pb
    lep = leptodermous_expansion_ka(A=208, Z=82)
    assert abs(lep["K_A_theoretical_MeV"] - ka["K_A_MeV"]) < 3.0, "Leptodermous expansion should match empirical Ka within 3 MeV"

    # Deformation splitting: 154Sm (beta2 = 0.30)
    split = model_deformation_splitting_two_state(E0_unpert_MeV=14.5, beta2=0.30, A=154)
    assert split["splitting_energy_MeV"] > 4.0, "Deformation splitting should exceed 4 MeV"
    assert split["E_low_peak_MeV"] < 11.5, "Lower split peak should be < 11.5 MeV"
    assert split["E_high_peak_MeV"] > 14.5, "Upper split peak should be > 14.5 MeV"

    # QPVC self-energy shift
    qpvc = calculate_qpvc_self_energy_shift(E_gmr_unpert_MeV=16.7, E_phonon_MeV=1.17, g_coupling_MeV=1.65)
    assert qpvc["self_energy_shift_MeV"] < 0.0, "QPVC self energy must produce a downward shift"

    # Diagnosis
    diag = diagnose_incompressibility_status(K_vol_extracted=240.0, K_tau_extracted=-550.0)
    assert diag["is_standard_eos_stiffness"] == True, "Should identify standard EOS stiffness"
    print("  ✓ isgmr_breathing_mode_incompressibility_calculator passed.")


def test_relativistic_coulex_virtual_photon_calculator():
    print("Testing relativistic_coulex_virtual_photon_calculator...")
    # 32Mg on 208Pb at 49.2 MeV/u
    kin = calculate_relativistic_coulex_kinematics(E_lab_MeV_u=49.2, A_proj=32, Z_proj=12, A_targ=208, Z_targ=82)
    assert 0.30 < kin["beta"] < 0.33, f"Expected beta ~0.31, got {kin['beta']}"
    assert 12.5 < kin["b_min_fm"] < 14.5, f"Expected b_min ~13.4 fm, got {kin['b_min_fm']}"

    # Virtual photon numbers
    v_phot = calculate_virtual_photon_numbers(E_x_MeV=0.885, b_min_fm=kin["b_min_fm"], Z_targ=82, beta=kin["beta"], gamma=kin["gamma"])
    assert v_phot["N_E1"] > 50.0, f"Expected large N_E1, got {v_phot['N_E1']}"
    assert v_phot["N_E2"] > 1e4, f"Expected large N_E2, got {v_phot['N_E2']}"

    # Relativistic E2 Coulex cross section
    cs = calculate_relativistic_e2_coulex_cross_section(B_E2_e2b2=0.045, E_x_MeV=0.885, E_lab_MeV_u=49.2, A_proj=32, Z_proj=12, A_targ=208, Z_targ=82)
    assert 50.0 < cs["sigma_E2_mb"] < 75.0, f"Expected sigma_E2 ~60 mb, got {cs['sigma_E2_mb']}"

    # Round-trip B(E2) inversion
    inv = invert_b_e2_from_coulex_cross_section(sigma_E2_mb=cs["sigma_E2_mb"], E_x_MeV=0.885, E_lab_MeV_u=49.2, A_proj=32, Z_proj=12, A_targ=208, Z_targ=82)
    assert abs(inv["extracted_B_E2_e2b2"] - 0.045) < 1e-4, f"Inversion mismatch: {inv['extracted_B_E2_e2b2']}"

    # Lorentz boost angular transformation: 0 deg vs 180 deg
    boost = transform_gamma_angular_distribution_lorentz(theta_lab_deg_list=[0.0, 180.0], beta=kin["beta"])
    assert boost[0]["jacobian_solid_angle"] > 1.5, "Forward Jacobian must compress solid angle (> 1.5)"
    assert boost[1]["jacobian_solid_angle"] < 0.6, "Backward Jacobian must expand solid angle (< 0.6)"
    print("  ✓ relativistic_coulex_virtual_photon_calculator passed.")


def test_electromagnetic_transition_alaga_calculator():
    print("Testing electromagnetic_transition_alaga_calculator...")
    # Weisskopf unit test for A=132
    wu = calculate_weisskopf_unit(A=132, multipolarity="E2")
    assert abs(wu["B_sp_value"] - 39.92) < 0.1, f"B_sp(E2) mismatch: {wu['B_sp_value']}"

    # Lifetime to B(E2) conversion: 131Ce tau = 1.235 ps, E_gamma = 465 keV
    conv = convert_lifetime_to_b_e2(tau_ps=1.235, E_gamma_keV=465.0, A=131)
    assert 2.5 < conv["B_E2_e2b2"] < 3.5, f"B(E2) out of range: {conv['B_E2_e2b2']}"
    assert conv["B_E2_W_u"] > 500.0, "Collective enhancement should exceed 500 W.u."
    assert conv["Q0_intrinsic_eb"] > 5.0, "Q0 should exceed 5 eb"

    # Alaga ratio test: 4+ -> 2+ vs 2+ -> 0+
    al = calculate_alaga_ratio_e2(I_initial=4, K_band=0)
    assert abs(al["alaga_ratio_to_2_0"] - (10.0 / 7.0)) < 1e-4, f"Alaga ratio mismatch: {al['alaga_ratio_to_2_0']}"

    # In-band B(M1)/B(E2) and |gK - gR| / Q0 extraction
    bm1 = calculate_bm1_over_be2(E_gamma_dI1_keV=465.0, E_gamma_dI2_keV=820.0, I_gamma_dI1=100.0, I_gamma_dI2=80.0, delta_mixing=0.1, spin_I=8.5, K_val=5.5)
    assert 3.0 < bm1["B_M1_over_B_E2_muN2_e2b2"] < 3.5, f"B(M1)/B(E2) out of range: {bm1['B_M1_over_B_E2_muN2_e2b2']}"
    assert 1.5 < bm1["abs_gK_minus_gR_over_Q0_muN_eb"] < 2.0, "gK-gR / Q0 out of range"
    print("  ✓ electromagnetic_transition_alaga_calculator passed.")


def test_two_nucleon_transfer_pairing_vibration_calculator():
    print("Testing two_nucleon_transfer_pairing_vibration_calculator...")
    # BCS coherent enhancement test
    bcs = calculate_bcs_transfer_enhancement([(5.5, 0.5), (3.5, 0.5), (2.5, 0.5), (1.5, 0.5), (0.5, 0.5)])
    assert bcs["enhancement_factor"] > 4.0, f"Expected BCS enhancement > 4x, got {bcs['enhancement_factor']}"
    assert bcs["sigma_coherent"] > 15.0, "Coherent cross section should exceed 15"

    # 208Pb pairing vibrations
    pv = calculate_pairing_vibration_energies(S2n_A_plus_2_MeV=9.12, S2n_A_MeV=14.11)
    assert abs(pv["hw_plus_addition_phonon_MeV"] - 2.495) < 0.01, "Addition phonon mismatch"
    assert abs(pv["hw_minus_removal_phonon_MeV"] - 2.495) < 0.01, "Removal phonon mismatch"
    assert abs(pv["Ex_double_phonon_1_1_MeV"] - 4.99) < 0.01, "Double phonon Ex mismatch"

    # Kinematic Q-matching
    qm = evaluate_kinematic_q_matching(E_lab_MeV=84.0, Q_actual_MeV=-3.2, Z_proj=8, A_proj=18, Z_targ=6, A_targ=12, Z_ejec=8, A_ejec=16)
    assert qm["Q_optimal_MeV"] == 0.0, "Q_optimal mismatch"

    # Josephson multi-pair transfer
    jos = calculate_josephson_transfer_probability(P_1pair=0.05, n_pairs=2, enhancement_factor=15.0)
    assert abs(jos["P_uncorrelated"] - 0.0025) < 1e-6, "P_uncorr mismatch"
    assert abs(jos["P_Josephson"] - 0.0375) < 1e-6, "P_Josephson mismatch"
    assert jos["supercurrent_signature"] == True, "Should identify Josephson supercurrent signature"
    print("  ✓ two_nucleon_transfer_pairing_vibration_calculator passed.")


def test_multi_nucleon_transfer_dic_calculator():
    print("Testing multi_nucleon_transfer_dic_calculator...")
    # 136Xe + 208Pb at 6.0 MeV/u
    wil = calculate_wilczynski_energy_loss_and_orbiting(Elab_MeV_u=6.0, Ap=136, Zp=54, At=208, Zt=82)
    assert 480.0 < wil["E_cm_MeV"] < 505.0, f"E_cm out of expected range: {wil['E_cm_MeV']}"
    assert 75.0 < wil["TKEL_max_MeV"] < 100.0, f"TKEL_max out of range: {wil['TKEL_max_MeV']}"
    assert wil["energy_above_barrier_MeV"] > 5.0, "Reaction must be above Coulomb barrier"

    # Fast charge equilibration test
    ce = calculate_charge_equilibration(Ap=136, Zp=54, At=208, Zt=82)
    assert abs(ce["N_over_Z_system_equilibrated"] - 1.5294) < 1e-3, "Equilibrated N/Z mismatch"

    # Driving potential calculation
    vdr = calculate_driving_potential(Z1=56, N1=82, Z_proj=54, N_proj=82, Z_targ=82, N_targ=126)
    assert abs(vdr["V_driving_potential_MeV"]) < 10.0, "V_dr out of physical range"

    # Fragment thermal excitation and evaporation test
    evap = calculate_fragment_thermal_excitation_and_evaporation(TKEL_MeV=wil["TKEL_max_MeV"], A1_prim=136, Z1_prim=54, A2_prim=208, Z2_prim=82)
    assert evap["neutrons_evaporated_frag2"] > 3.0, "Heavy fragment should evaporate multiple neutrons"

    # Cross section prediction
    cs = predict_mnt_cross_section(sigma_dic_mb=1200.0, delta_Z=-2, delta_N=2, TKEL_MeV=wil["TKEL_max_MeV"])
    assert cs["sigma_MNT_mb"] > 5.0, "MNT cross section unexpectedly low"
    print("  ✓ multi_nucleon_transfer_dic_calculator passed.")


def test_rmf_spin_orbit_pseudospin_calculator():
    print("Testing rmf_spin_orbit_pseudospin_calculator...")
    # RMF potential test
    pot = calculate_rmf_potentials([0.0, 5.0, 10.0])
    assert pot["central_depth_origin_MeV"] < -60.0, f"Central depth mismatch: {pot['central_depth_origin_MeV']}"
    assert pot["diff_potential_origin_MeV"] > 700.0, f"Difference potential mismatch: {pot['diff_potential_origin_MeV']}"

    # Spin-orbit splitting: 16O p-wave
    so = estimate_spin_orbit_splitting(l_orbital=1, A=16)
    assert abs(so["Delta_E_SO_estimated_MeV"] - 6.14) < 0.1, "16O spin-orbit split mismatch"

    # Pseudospin mapping: (2s1/2, 1d3/2)
    ps = map_pseudospin_partner(n_principal=2, l_orbital=0)
    assert ps["state_1"] == "2s_1/2", "State 1 mismatch"
    assert ps["state_2"] == "1d_3/2", "State 2 mismatch"
    assert ps["pseudo_orbital_tilde_l"] == 1, "Tilde l mismatch"

    # Pseudospin quality
    qual = evaluate_pseudospin_symmetry_quality(E_state1_MeV=-7.94, E_state2_MeV=-8.27, Delta_E_SO_MeV=3.33)
    assert qual["is_good_pseudospin_symmetry"] == True, "Should identify high-grade pseudospin symmetry"
    assert qual["Q_PSS_ratio"] < 0.15, "Quality ratio should be < 0.15"

    # Quartet diagnosis
    sp = [11.5, 12.5, 13.5]
    b1 = [2500, 2900, 3400]
    b2 = [2600, 3050, 3520]
    b3 = [2720, 3180, 3680]
    b4 = [2850, 3300, 3790]
    quart = diagnose_pseudospin_chiral_quartet_manifold(sp, b1, b2, b3, b4)
    assert quart["is_quartet_candidate"] == True, "Should identify candidate quartet"
    print("  ✓ rmf_spin_orbit_pseudospin_calculator passed.")


def test_isotope_shift_charge_radii_calculator():
    print("Testing isotope_shift_charge_radii_calculator...")
    # Normal mass shift test
    nms = calculate_normal_mass_shift(transition_freq_GHz=1.2e6, mass_A=132, mass_A_ref=130)
    assert abs(nms["delta_nu_NMS_MHz"] - 76.72) < 0.1, f"NMS mismatch: {nms['delta_nu_NMS_MHz']}"

    # Inversion test
    inv = extract_delta_r2_from_isotope_shift(delta_nu_exp_GHz=-0.44676, mass_A=132, mass_A_ref=130, K_mass_shift_GHz_amu=800.0, F_field_shift_GHz_fm2=-4.5)
    assert abs(inv["delta_r2_fm2"] - 0.12) < 1e-4, f"Extracted delta<r^2> mismatch: {inv['delta_r2_fm2']}"

    # Deformation decomposition
    dec = decompose_charge_radius_components(A=132, A_ref=130, delta_r2_total_fm2=0.12)
    assert abs(dec["delta_r2_spherical_fm2"] - 0.2268) < 0.01, "Spherical radius expansion mismatch"
    assert dec["delta_r2_deformation_fm2"] < 0.0, "Deformation contribution should be negative"

    # King plot regression test
    masses = [132, 134, 136]
    s1 = [-0.44676, -0.85, -1.22]
    mu_test = (np.array(masses) - 130.0) / (np.array(masses) * 130.0)
    s2 = (1.5 * (np.array(s1) / mu_test) + 50.0) * mu_test
    king = perform_king_plot_analysis(masses_A=masses, mass_A_ref=130, shifts_line1_GHz=s1, shifts_line2_GHz=s2)
    assert abs(king["slope_F2_over_F1"] - 1.5) < 1e-4, f"King slope mismatch: {king['slope_F2_over_F1']}"
    assert king["is_strictly_linear"] == True, "King plot must be linear"

    # OES staggering test
    oes = calculate_charge_radius_odd_even_staggering(N_list=[74, 75, 76], r2_series_fm2=[24.0, 24.35, 24.8])
    assert abs(oes[0]["gamma_r"] - 0.875) < 1e-3, "OES gamma_r mismatch"
    print("  ✓ isotope_shift_charge_radii_calculator passed.")


def test_drip_line_radioactivity_cluster_calculator():
    print("Testing drip_line_radioactivity_cluster_calculator...")
    # Proton decay WKB test
    p1 = calculate_proton_decay_wkb_lifetime(Q_p_MeV=1.05, l_orbital=5, Z_daughter=68, A_daughter=146)
    assert abs(p1["Gamow_integral_G"] - 26.95) < 0.1, f"Gamow G mismatch: {p1['Gamow_integral_G']}"
    assert p1["is_energetically_allowed"] == True, "1p decay should be allowed"

    # True 2p Goldanskii condition test
    g2p = check_goldanskii_true_2p_condition(Q_2p_MeV=1.15, S_p_MeV=0.05)
    assert g2p["is_true_two_proton_decay"] == True, "Should identify true 2p decay"

    seq2p = check_goldanskii_true_2p_condition(Q_2p_MeV=1.15, S_p_MeV=-0.10)
    assert seq2p["is_true_two_proton_decay"] == False, "Sequential 2p should not be classified as true 2p"

    # Cluster decay test: 14C from 223Ra
    c14 = calculate_cluster_radioactivity_wkb(Q_c_MeV=31.83, A_c=14, Z_c=6, A_d=209, Z_d=82, P_preformation=1e-9)
    assert abs(c14["Gamow_factor_G"] - 33.64) < 0.1, f"Cluster Gamow G mismatch: {c14['Gamow_factor_G']}"
    assert c14["T12_s"] > 1e15, "Cluster decay half-life should exceed 10^15 s"

    # Competition test
    comp = diagnose_drip_line_decay_competition(T12_p_s=0.005, T12_beta_s=0.86)
    assert comp["dominant_channel"] == "1p_emission", "1p should be dominant"
    assert comp["dominant_branching_percent"] > 95.0, "1p branching should exceed 95%"
    print("  ✓ drip_line_radioactivity_cluster_calculator passed.")


def test_thermonuclear_rate_gamow_factor_calculator():
    print("Testing thermonuclear_rate_gamow_factor_calculator...")
    # Solar pp fusion
    pp = calculate_gamow_peak_and_window(T9=0.015, Z1=1, A1=1, Z2=1, A2=1)
    assert abs(pp["E0_Gamow_peak_keV"] - 5.89) < 0.05, f"Sun pp E0 mismatch: {pp['E0_Gamow_peak_keV']}"
    assert abs(pp["Delta_window_width_keV"] - 6.37) < 0.05, f"Sun pp Delta mismatch: {pp['Delta_window_width_keV']}"

    # 12C + alpha at T9 = 0.2
    c12 = calculate_gamow_peak_and_window(T9=0.2, Z1=2, A1=4, Z2=6, A2=12)
    assert abs(c12["E0_Gamow_peak_keV"] - 315.5) < 0.5, f"12C+alpha E0 mismatch: {c12['E0_Gamow_peak_keV']}"

    # Sommerfeld parameter test
    somm = calculate_sommerfeld_parameter(E_cm_keV=10.0, Z1=1, A1=1, Z2=1, A2=1)
    assert somm["sommerfeld_eta"] > 1.0, "Sommerfeld eta unexpectedly low"

    # Non-resonant reaction rate test: 3He+3He
    rate_3he = calculate_nonresonant_reaction_rate(T9=0.015, S0_keV_b=5300.0, Z1=2, A1=3, Z2=2, A2=3)
    assert rate_3he["reaction_rate_cm3_mol_s"] > 0.0, "Non-resonant rate must be positive"

    # Resonant reaction rate test
    res = calculate_resonant_reaction_rate(T9=0.5, omega_gamma_eV=1.5, E_res_keV=200.0, A1=1, A2=14)
    assert abs(res["resonant_rate_cm3_mol_s"] - 6980.0) < 50.0, f"Resonant rate mismatch: {res['resonant_rate_cm3_mol_s']}"
    print("  ✓ thermonuclear_rate_gamow_factor_calculator passed.")


def test_qrpa_matrix_vibrational_calculator():
    print("Testing qrpa_matrix_vibrational_calculator...")
    # Analytic single-mode QRPA test
    sm = solve_analytic_single_mode_qrpa(A_val=3.0, B_val=1.0)
    assert abs(sm["omega_MeV"] - np.sqrt(8.0)) < 1e-4, f"Omega mismatch: {sm['omega_MeV']}"
    assert abs(sm["X_squared_minus_Y_squared"] - 1.0) < 1e-4, "Bose normalization violated"
    assert sm["coherent_enhancement"] > 0.0, "Enhancement factor must be positive"

    # 2x2 matrix QRPA test
    A = [[3.0, 0.4], [0.4, 3.5]]
    B = [[0.5, 0.2], [0.2, 0.6]]
    sol = solve_qrpa_eigenvalues_and_amplitudes(A, B)
    assert sol["modes_found"] == 2, f"Expected 2 physical modes, got {sol['modes_found']}"
    assert sol["is_stable_vacuum"] == True, "QRPA vacuum should be stable"
    assert sol["modes"][0]["omega_MeV"] < sol["modes"][1]["omega_MeV"], "Modes should be sorted ascending"

    # pnQRPA gpp sensitivity scan test
    scan = scan_pnqrpa_gpp_sensitivity(E_unpert_MeV=4.0)
    assert scan["zero_crossing_gpp"] is not None, "Zero crossing not found"
    assert abs(scan["zero_crossing_gpp"] - 0.95) < 0.1, f"Zero crossing mismatch: {scan['zero_crossing_gpp']}"

    # Stability diagnosis test
    diag = diagnose_qrpa_stability(A, B)
    assert diag["is_stable"] == True, "Stability diagnosis mismatch"
    print("  ✓ qrpa_matrix_vibrational_calculator passed.")


def test_surface_delta_interaction_pandya_calculator():
    print("Testing surface_delta_interaction_pandya_calculator...")
    # Clebsch-Gordan and 6j exactness tests
    cg = calculate_clebsch_gordan(0.5, 0.5, 0.5, -0.5, 0.0, 0.0)
    assert abs(cg - 1.0 / np.sqrt(2.0)) < 1e-10, "Clebsch-Gordan calculation mismatch"

    w6 = calculate_wigner_6j(3.5, 3.5, 0.0, 3.5, 3.5, 0.0)
    assert abs(w6 - (-0.125)) < 1e-10, f"Wigner 6j calculation mismatch: {w6}"

    # SDI single-j pairing spectrum test
    sdi = calculate_single_j_sdi_spectrum(j_val=3.5, l_val=3, V0_MeV=1.0)
    assert sdi["is_exact_pairing_energy"] == True, "J=0 state must exhibit exact -V0*(j+1/2) pairing energy"
    assert abs(sdi["E_J0_actual_MeV"] - (-4.0)) < 1e-4, f"E(J=0) mismatch: {sdi['E_J0_actual_MeV']}"
    assert abs(sdi["spectrum"][1]["V_SDI_MeV"] - (-0.9524)) < 1e-3, "E(J=2) mismatch"

    # Pandya involution P^2 = I test
    bm = benchmark_sc42_k40_pandya()
    assert bm["P2_verified"] == True, "Pandya matrix must satisfy P^2 = I (unitary involution)"
    assert bm["ground_state_pp_spin"] == 0, "42Sc ground state must be J=0+"
    assert bm["ground_state_ph_spin"] != 0, "Particle-hole ground state must invert to J!=0"
    print("  ✓ surface_delta_interaction_pandya_calculator passed.")


def test_k_isomer_hindrance_calculator():
    print("Testing k_isomer_hindrance_calculator...")
    # K-forbiddenness test
    forb = calculate_k_forbiddenness(Ki=8, Kf=0, multipolarity_lambda=1)
    assert forb["Delta_K"] == 8.0, "Delta K mismatch"
    assert forb["degree_of_forbiddenness_nu"] == 7, "nu mismatch"
    assert forb["is_K_forbidden"] == True, "Should be K-forbidden"

    # Reduced hindrance test: 130Ba 8- isomer
    rh = calculate_reduced_hindrance(tau_gamma_ps=13.705e9, E_gamma_keV=54.0, A=130, multipolarity="E1", delta_K=8)
    assert rh["degree_of_forbiddenness_nu"] == 7, "nu mismatch in reduced hindrance"
    assert 20.0 < rh["reduced_hindrance_f_nu"] < 30.0, f"f_nu out of expected range: {rh['reduced_hindrance_f_nu']}"
    assert rh["hindrance_F_W"] > 1e9, "Total hindrance factor F_W unexpectedly low"

    # Triaxial gamma tunneling collapse test
    tun_0 = model_triaxial_gamma_tunneling_hindrance(gamma_deg=0.0)
    assert tun_0["predicted_reduced_hindrance_f_nu"] == 80.0, "Axial f_nu mismatch"
    assert tun_0["is_hindrance_collapsed"] == False, "Axial f_nu should not be collapsed"

    tun_25 = model_triaxial_gamma_tunneling_hindrance(gamma_deg=25.0)
    assert tun_25["predicted_reduced_hindrance_f_nu"] < 10.0, "Triaxial f_nu should collapse < 10"
    assert tun_25["is_hindrance_collapsed"] == True, "Triaxial f_nu should be flagged as collapsed"

    # Classification test
    c1 = classify_isomer_mechanism(T12_s=0.0095, delta_I=0, delta_K=8)
    assert "K-Isomer" in c1["classification"], "Should classify as K-isomer"
    print("  ✓ k_isomer_hindrance_calculator passed.")

if __name__ == "__main__":
    print("=== Running Nuclear Analysis Suite Regression Tests ===")
    test_heavy_ion_kinematics()
    test_angular_distribution_and_dual_roots()
    test_digital_trapezoidal_filter()
    test_gamma_peak_fitting()
    test_dco_polarization_analyzer()
    test_lifetime_lineshape_calculator()
    test_coincidence_intensity_balancer()
    test_routhian_alignment_analyzer()
    test_ensdf_crosswalk_parser()
    test_excitation_function_calculator()
    test_magnetic_rotation_shears_calculator()
    test_shape_coexistence_e0_calculator()
    test_moment_of_inertia_spin_analyzer()
    test_coulex_kumar_invariant_calculator()
    test_tpsm_band_diagram_calculator()
    test_octupole_parity_doublet_calculator()
    test_signature_inversion_analyzer()
    test_superdeformation_decayout_calculator()
    test_ibm_dynamical_symmetry_analyzer()
    test_ado_polarization_joint_analyzer()
    test_side_feeding_deconvolution_calculator()
    test_internal_conversion_bricc_calculator()
    test_vacuum_deorientation_calculator()
    test_tidal_wave_dynamics_calculator()
    test_gamow_teller_ikeda_quenching_calculator()
    test_halo_breakup_momentum_calculator()
    test_fission_barrier_superheavy_calculator()
    test_oslo_method_nld_gsf_analyzer()
    test_band_termination_cns_calculator()
    test_tdpad_hyperfine_precession_calculator()
    test_pairing_gap_separation_energy_calculator()
    test_isgmr_breathing_mode_incompressibility_calculator()
    test_relativistic_coulex_virtual_photon_calculator()
    test_electromagnetic_transition_alaga_calculator()
    test_two_nucleon_transfer_pairing_vibration_calculator()
    test_multi_nucleon_transfer_dic_calculator()
    test_rmf_spin_orbit_pseudospin_calculator()
    test_isotope_shift_charge_radii_calculator()
    test_drip_line_radioactivity_cluster_calculator()
    test_thermonuclear_rate_gamow_factor_calculator()
    test_qrpa_matrix_vibrational_calculator()
    test_surface_delta_interaction_pandya_calculator()
    test_k_isomer_hindrance_calculator()
    print("ALL 43 SCIENTIFIC ANALYSIS MODULES VERIFIED SUCCESSFULLY!")
