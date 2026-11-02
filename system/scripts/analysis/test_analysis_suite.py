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
import math
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
from dipole_polarizability_neutron_skin_calculator import calculate_polarizability_from_sigma_minus2, integrate_dipole_polarizability_from_spectrum, droplet_model_polarizability_estimate, extract_neutron_skin_from_polarizability, extract_symmetry_energy_slope_L, predict_neutron_star_radius_from_L
from gilbert_cameron_level_density_calculator import solve_gilbert_cameron_matching, compute_level_density, calculate_s_wave_resonance_spacing, cumulative_level_count
from davydov_wobbling_rotor_calculator import davydov_filippov_energies_and_be2, frauendorf_wobbling_frequency, extract_experimental_wobbling_sequence, classify_wobbling_trend, falsify_wobbling_vs_signature_partner
from particle_identification_delta_e_calculator import calculate_stopping_power, simulate_telescope_response, evaluate_pulse_height_defect, evaluate_energy_straggling
from compound_nucleus_evaporation_calculator import calculate_fusion_barrier, calculate_fusion_cross_section, simulate_statistical_evaporation_cascade
from experimental_uncertainty_covariance_calculator import propagate_linear_covariance, synthesize_correlated_systematics, calculate_baker_cousins_deviance, resolve_double_root_delta_mixing
from collective_quadrupole_pes_calculator import scan_potential_energy_surface
from hpge_pulse_processing_pole_zero_calculator import calculate_ballistic_deficit, simulate_pole_zero_compensation, calculate_high_rate_pileup
from chiral_geometry_tac_calculator import calculate_chiral_geometry, evaluate_chiral_doublet_criteria
from beta_decay_log_ft_phase_space_calculator import calculate_log_ft, verify_superallowed_cvc_vud
from gallagher_moszkowski_coupling_calculator import evaluate_gallagher_moszkowski_rule, calculate_newby_shift_spectrum
from nilsson_model_hamiltonian_diagonalizer import solve_nilsson_subblock
from fission_fragment_mass_yield_calculator import calculate_viola_tke, calculate_fission_fragment_distribution
from pulse_shape_discrimination_psd_calculator import calculate_charge_comparison_psd, calculate_figure_of_merit, simulate_zero_crossing_timing
from multi_quasiparticle_blocked_bcs_calculator import calculate_multi_quasiparticle_energy
from internal_pair_creation_ipc_calculator import calculate_ipc_coefficient, calculate_angular_correlation
from rmf_deformed_constrained_calculator import calculate_rmf_spherical_ground_state, scan_rmf_constrained_pes
from isobaric_analog_state_ced_calculator import calculate_coulomb_displacement_energy, analyze_mirror_ced_sequence
from gamma_cascade_calorimetry_calculator import simulate_gamma_cascade, compare_evaporation_channel_entry_points
from wigner_supermultiplet_su4_calculator import calculate_wigner_energy, calculate_su4_casimir
from linear_momentum_transfer_incomplete_fusion_calculator import calculate_linear_momentum_transfer, scan_folding_angle_vs_lmt
from rdds_plunger_lifetime_calculator import calculate_flight_time_and_shifts, fit_exponential_rdds_lifetime, convert_lifetime_to_be2_and_qt
from double_beta_decay_nme_calculator import invert_majorana_mass_limit, predict_half_life_for_target_mass
from heavy_ion_elastic_rainbow_scattering_calculator import calculate_scattering_kinematics, scan_nuclear_rainbow
from core_polarization_effective_charge_calculator import calculate_microscopic_polarization_charges, invert_effective_charge_from_be2
from fission_isomer_double_hump_transmission_calculator import calculate_fission_isomer_properties, evaluate_double_barrier_transmission
from abrasion_ablation_fragmentation_calculator import calculate_geometric_abrasion, simulate_ablation_cooling
from chiral_vibrational_tunneling_calculator import evaluate_chiral_potential_at_spin, scan_chiral_band_splitting_sequence
from clover_compton_addback_polarization_calculator import calculate_clover_addback_factor, analyze_clover_polarization
from strutinsky_shell_correction_calculator import calculate_strutinsky_shell_correction
from nilsson_magnetic_moment_gk_calculator import calculate_nilsson_gk, calculate_magnetic_dipole_moment, invert_gk_from_bm1_be2
from angular_momentum_projection_amp_calculator import project_rotational_spectrum
from spin_dipole_resonance_sdr_calculator import calculate_sdr_sum_rule, invert_neutron_skin_from_sdr
from gamma_gamma_matrix_slicer_calculator import generate_synthetic_cascade_matrix, slice_matrix_gate
from nolen_schiffer_isospin_anomaly_calculator import evaluate_nolen_schiffer_anomaly
from multiphonon_wobbling_anharmonic_calculator import evaluate_multiphonon_wobbling_energies, audit_multiphonon_wobbling_candidate
from rmf_symmetry_energy_slope_calculator import calculate_rmf_symmetry_energy, scan_symmetry_energy_curve
from wigner_racah_algebra_9j_calculator import wigner_9j, calculate_ls_to_jj_recoupling
from charge_exchange_gt_quenching_calculator import deconvolve_gt_quenching
from alignment_attenuation_coefficients_calculator import calculate_alignment_attenuation_factors, invert_sigma_over_I_from_stretched_e2
from r_process_waiting_point_flow_calculator import calculate_waiting_point_separation_energy, calculate_isotopic_saha_equilibrium
from wobbling_branching_ratio_phase_calculator import calculate_theoretical_wobbling_delta, compare_wobbling_with_experimental_roots
from gdr_lorentzian_trk_sumrule_calculator import calculate_trk_sum_rule, calculate_deformed_gdr_splitting, invert_beta2_from_gdr_peaks
from isovector_giant_resonance_splitting_calculator import calculate_isovector_splitting
from detector_deadtime_pileup_correction_calculator import calculate_deadtime_models, invert_observed_rate
from heavy_ion_fusion_evaporation_channel_calculator import analyze_heavy_ion_fusion
from poisson_likelihood_peak_fitting_bias_calculator import evaluate_peak_fitting_methods
from coriolis_attenuation_bandcrossing_calculator import calculate_coriolis_matrix_elements, analyze_backbending_alignment
from directional_correlation_f_coefficients_calculator import calculate_f_coefficient, calculate_angular_distribution_coefficients, invert_delta_dual_roots, calculate_dco_and_ado_ratios
from decoupling_parameter_khalf_band_calculator import calculate_pure_j_decoupling_parameter, calculate_khalf_spectrum, invert_khalf_band_parameters
from alpha_decay_gamow_wkb_calculator import calculate_gamow_factor_wkb, evaluate_alpha_hindrance
from triaxial_wobbling_tip_chiral_analyzer import calculate_triaxial_rotor_moi_parameters, calculate_transverse_wobbling_spectrum, classify_tip_vs_phonon_wobbling, analyze_chiral_doublet_staggering
from feldman_cousins_unified_confidence_interval_calculator import calculate_poisson_fc_interval, calculate_gaussian_fc_interval
from hpge_coaxial_electric_field_ballistic_deficit_calculator import calculate_coaxial_depletion_and_field, calculate_shockley_ramo_collection, calculate_coaxial_ballistic_deficit, reconcile_neutron_damage_p_vs_n
from heavy_ion_fusion_spin_distribution_wong_calculator import calculate_heavy_ion_fusion_wong
from dsam_doppler_attenuation_lss_blaugrund_lifetime_calculator import calculate_dsam_f_tau_value, invert_lifetime_from_f_tau, calculate_lss_stopping_constants
from mariscotti_vmi_rotational_stretching_calculator import solve_vmi_cubic_moi, calculate_vmi_spectrum, invert_vmi_parameters
from seniority_scheme_half_filled_isomer_calculator import calculate_seniority_fractional_factor, evaluate_seniority_isomer_properties
from constant_fraction_discriminator_fast_timing_calculator import simulate_cfd_walk_elimination, calculate_fast_timing_resolution
from grodzins_deformation_beta2_quadrupole_inverter import invert_beta2_and_quadrupole
from cranked_shell_model_band_crossing_v12_inverter import calculate_two_band_crossing_csm, invert_v12_from_experimental_routhians
from optical_model_potential_reaction_cross_section_calculator import calculate_optical_model_reaction_cross_section
from in_beam_doppler_broadening_array_correction_calculator import calculate_doppler_broadening_budget, compare_detector_rings
from triaxial_cranking_single_j_routhian_diagram_calculator import diagonalize_triaxial_cranked_high_j, scan_routhian_frequency_trajectory
from in_beam_experiment_analysis_pipeline import run_full_in_beam_pipeline
from schiffer_true_two_body_matrix_elements_calculator import calculate_schiffer_true_pp_spectrum, calculate_schiffer_true_ph_pandya_spectrum, evaluate_nordheim_coupling_rule
from tac_3d_chiral_orientation_energy_surface_calculator import find_chiral_equilibrium_and_barrier, scan_chiral_spin_evolution
from gamma_band_mixing_z_gamma_alaga_inverter import invert_z_gamma_from_branching
from level_scheme_loop_residual_intensity_balancer import evaluate_ritz_combination_loop, calculate_level_intensity_balance
from davydov_chaban_beta_stretching_triaxial_calculator import calculate_davydov_chaban_spectrum, solve_chaban_stretching_parameter_p
from double_root_dco_polarization_statistical_arbitrator import solve_dco_quadratic, analyze_double_roots
from multi_quasiparticle_mchid_chirality_calculator import evaluate_chiral_geometry, analyze_mchid
from heavy_ion_dic_wilczynski_energy_loss_calculator import calculate_dic_kinematics, run_dic_analysis
from octupole_collective_ewsr_parity_doublet_analyzer import calculate_octupole_ewsr, calculate_parity_splitting_ewsr
from digital_psd_charge_comparison_optimizer import optimize_gate_widths, evaluate_fom_energy_dependence
from tac_pairing_self_consistent_chiral_engine import calculate_self_consistent_pairing_gap, find_tac_pairing_chiral_barrier
from cascade_deorientation_coefficient_uk_calculator import calculate_single_step_uk, evaluate_cascade_deorientation
from mwpc_drift_chamber_field_avalanche_simulator import calculate_electrostatic_field, run_mwpc_simulation
from coriolis_band_mixing_matrix_diagonalizer import construct_coriolis_matrix, diagonalize_coriolis_mixing
from spontaneous_fission_wkb_action_calculator import calculate_sf_hill_wheeler_transmission, calculate_double_hump_sf_half_life
from particle_triaxial_rotor_model_ptrm_diagonalizer import evaluate_ptrm_matrix_elements, diagonalize_ptrm_spectrum
from digital_mwd_baseline_restorer_filter import run_mwd_blr_analysis
from in_beam_fast_timing_gcd_lifetime_calculator import calculate_prf_walk, calculate_gcd_lifetime
from chiral_doublet_g_factor_equality_calculator import calculate_theoretical_chiral_gfactor, arbitrate_chiral_gfactor_equality
from in_beam_true_coincidence_summing_tcs_calculator import calculate_total_efficiency, calculate_tcs_corrections
from chiral_octupole_quartet_bands_analyzer import evaluate_quartet_properties
from heavy_ion_optical_rainbow_scattering_analyzer import calculate_kinematics_and_sommerfeld, find_rainbow_singularity_and_airy_minima
from in_beam_time_spectrum_convolution_fitter import convoluted_decay_model, fit_convoluted_time_spectrum
from two_quasiparticle_even_even_wobbling_analyzer import calculate_two_quasiparticle_wobbling_energies, evaluate_wobbling_slope_and_criteria
from hpge_efficiency_curve_covariance_fitter import fit_efficiency_curve_wls, evaluate_efficiency_with_covariance
from in_beam_gated_matrix_multiplet_deconvolution_fitter import multiplet_model_function, fit_gated_multiplet
from triaxial_superdeformed_wobbling_decayout_analyzer import calculate_transition_widths_and_tunneling, evaluate_decayout_threshold
from heavy_ion_mcintyre_s_matrix_reaction_cross_section_analyzer import calculate_kinematics as calc_mcintyre_kin, calculate_reaction_cross_sections as calc_mcintyre_xs
from three_dimensional_tac_chiral_pitchfork_bifurcation_inverter import calculate_pitchfork_bifurcation
from in_beam_array_fold_multiplicity_entry_state_unfolder import calculate_binomial_response_matrix, map_to_entry_spin_and_energy
from chiral_doublet_selection_rules_m1_staggering_arbitrator import calculate_m1_staggering, arbitrate_chiral_selection_rules
from in_beam_prompt_delayed_time_gating_random_subtractor import calculate_window_width, perform_random_subtraction
from triaxial_hexadecapole_deformation_wobbling_modifier import calculate_hexadecapole_modified_moi, calculate_wobbling_frequency_with_beta4
from chiral_vibrational_quartic_schrodinger_diagonalizer import diagonalize_chiral_schrodinger
from hpge_detector_solid_angle_attenuation_qk_integrator import calculate_solid_angle_attenuation_qk
from in_beam_pulser_injection_live_time_corrector import calculate_pulser_live_time, correct_peaks
from triaxial_superdeformed_pes_strutinsky_engine import calculate_ldm_energy_surface, find_pes_minima_and_saddle
from coriolis_anti_pairing_gap_quenching_moi_engine import calculate_cap_pairing_gap, solve_spin_state_cap
from in_beam_array_coincidence_efficiency_angular_matrix_inverter import calculate_mutual_pair_angle, evaluate_directional_correlation_weight
from tpsm_3d_angular_momentum_projection_diagonalizer import calculate_effective_moi_tpsm, diagonalize_spin_tpsm
from in_beam_rdds_ddcm_lifetime_inverter import evaluate_ddcm_curve, extract_plateau_lifetime_and_be2
from davydov_rostovsky_triaxial_band_mixing_solver import invert_gamma_mixing_parameter, calculate_davydov_rostovsky_parameters
from in_beam_2d_snip_matrix_background_estimator import generate_synthetic_2d_matrix, execute_2d_snip_algorithm
from odd_odd_3d_tac_recoil_chiral_orientator import evaluate_recoil_coupled_energy, find_optimal_orientation
from hpge_energy_non_linearity_inl_dnl_calibrator import fit_energy_polynomial, evaluate_calibrated_energy
from odd_odd_chiral_mep_instanton_tunneling_solver import OddOddChiralMEPInstantonSolver
from in_beam_hpge_tfa_crossover_walk_jitter_optimizer import HPGeTFACrossoverOptimizer
from heavy_ion_triaxial_fusion_barrier_distribution_inverter import TriaxialFusionBarrierInverter
from odd_a_transverse_longitudinal_wobbling_stability_solver import OddAWobblingStabilitySolver
from in_beam_dsam_zbl_stopping_lifetime_inverter import InBeamDSAMZBLInverter
from cranked_triaxial_shape_coexistence_pes_engine import CrankedShapeCoexistencePESEngine
from in_beam_spin_alignment_sigma_mixing_ratio_extractor import SpinAlignmentMixingExtractor
from multiple_chiral_doublets_mchid_discriminator import MultipleChiralDoubletsDiscriminator, PRESETS as MCHID_PRESETS
from in_beam_charged_particle_pid_delta_e_telescope_inverter import ChargedParticlePIDInverter
from triaxial_two_rotor_scissors_mode_m1_solver import TriaxialScissorsModeM1Solver


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


def test_dipole_polarizability_neutron_skin_calculator():
    print("Testing dipole_polarizability_neutron_skin_calculator...")
    # 208Pb polarizability from sigma_-2 = 20.1 mb/MeV
    pol = calculate_polarizability_from_sigma_minus2(sigma_minus2_mb_MeV_inv=20.1)
    assert abs(pol["alpha_D_fm3"] - 20.09) < 0.1, f"alpha_D mismatch: {pol['alpha_D_fm3']}"

    # Neutron skin extraction: 208Pb
    skin = extract_neutron_skin_from_polarizability(pol["alpha_D_fm3"], target_nucleus="208Pb")
    assert abs(skin["delta_r_np_fm"] - 0.157) < 0.01, f"Skin mismatch: {skin['delta_r_np_fm']}"

    # Symmetry energy slope L and pure neutron matter pressure
    l_slope = extract_symmetry_energy_slope_L(skin["delta_r_np_fm"])
    assert 40.0 < l_slope["L_slope_MeV"] < 55.0, f"Slope L out of range: {l_slope['L_slope_MeV']}"
    assert l_slope["P_PNM_rho0_MeV_fm3"] > 2.0, "PNM pressure unexpectedly low"

    # Neutron star radius prediction
    r_ns = predict_neutron_star_radius_from_L(l_slope["L_slope_MeV"])
    assert 11.5 < r_ns["predicted_radius_R_NS_km"] < 13.0, f"Neutron star radius out of range: {r_ns['predicted_radius_R_NS_km']}"

    # Droplet model estimate
    drop = droplet_model_polarizability_estimate(A=208, Z=82)
    assert 22.0 < drop["alpha_D_droplet_fm3"] < 30.0, "Droplet alpha_D out of range"
    print("  ✓ dipole_polarizability_neutron_skin_calculator passed.")

def test_gilbert_cameron_level_density_calculator():
    print("Testing gilbert_cameron_level_density_calculator...")
    match = solve_gilbert_cameron_matching(56, 130)
    assert 4.5 < match["E_x"] < 7.0, f"Matching energy E_x unexpected: {match['E_x']}"
    assert 0.4 < match["T_0"] < 0.9, f"Nuclear temperature T_0 unexpected: {match['T_0']}"

    # Constant temperature regime
    res_ct = compute_level_density(2.0, 56, 130, match_params=match)
    assert res_ct["regime"] == "Constant_Temperature", "Should be CT regime at 2 MeV"

    # Fermi gas regime
    res_fg = compute_level_density(10.0, 56, 130, match_params=match)
    assert res_fg["regime"] == "Back_Shifted_Fermi_Gas", "Should be BSFG regime at 10 MeV"
    assert res_fg["rho_total_MeV_inv"] > res_ct["rho_total_MeV_inv"], "Density must grow with excitation"

    # S-wave spacing for Pb-208 (magic nucleus spacing suppression)
    d0_pb = calculate_s_wave_resonance_spacing(7.37, 82, 208, target_I0=0.0)
    assert d0_pb["average_s_wave_spacing_D_0_eV"] > 50000.0, "Pb-208 D0 must be large (~keV)"
    print("  ✓ gilbert_cameron_level_density_calculator passed.")


def test_davydov_wobbling_rotor_calculator():
    print("Testing davydov_wobbling_rotor_calculator...")
    df = davydov_filippov_energies_and_be2(25.0, E2_1_keV=100.0)
    assert df["E2_2_keV"] > df["E2_1_keV"], "E(2_2) must be above E(2_1)"
    assert 2.5 < df["R_42"] < 3.333, f"R42 out of Davydov bounds: {df['R_42']}"
    assert df["B_E2_22_to_21_over_21_to_01"] > 1.0, "B(E2; 2_2->2_1) should be strong in triaxial rotor"

    # Transverse wobbling
    wob = frauendorf_wobbling_frequency(I=13.5, j=6.5, A1=12.0, A2=25.0, A3=45.0, mode="TW")
    assert wob["status"] == "stable", "Wobbling should be stable"
    assert 300.0 < wob["omega_wob_keV"] < 700.0, f"Wobbling frequency out of range: {wob['omega_wob_keV']}"

    # Falsification check
    fals = falsify_wobbling_vs_signature_partner(be2_out_over_in=0.35, b_m1_out_w_u=0.04, delta_mixing_ratio=2.5)
    assert fals["verdict"] == "ROBUST_WOBBLING_CONFIRMED", "Should pass all wobbling tests"
    print("  ✓ davydov_wobbling_rotor_calculator passed.")


def test_particle_identification_delta_e_calculator():
    print("Testing particle_identification_delta_e_calculator...")
    sp = calculate_stopping_power("alpha", 20.0, "Si")
    assert 0.05 < sp["dE_dx_MeV_per_um"] < 0.20, f"Alpha stopping power out of range: {sp['dE_dx_MeV_per_um']}"

    # Telescope response
    tele = simulate_telescope_response("alpha", 25.0, delta_e_thickness_um=30.0)
    assert tele["transmitted_delta_E"], "25 MeV alpha should punch through 30 um Si"
    assert tele["goulding_PID_index"] > 20.0, "PID index for alpha must be large"

    # Straggling regime: thick vs thin
    strag_thick = evaluate_energy_straggling("alpha", 20.0, absorber_thickness_um=30.0)
    assert "Gaussian" in strag_thick["straggling_regime"], "Should be Gaussian Bohr regime for thick absorber"

    strag_thin = evaluate_energy_straggling("p", 30.0, absorber_thickness_um=15.0)
    assert "Vavilov" in strag_thin["straggling_regime"], "Should be Vavilov regime for thin absorber"
    print("  ✓ particle_identification_delta_e_calculator passed.")


def test_compound_nucleus_evaporation_calculator():
    print("Testing compound_nucleus_evaporation_calculator...")
    fus = calculate_fusion_cross_section(8, 18, 48, 116, E_lab_MeV=75.0)
    assert 50.0 < fus["barrier_V_B_MeV"] < 55.0, f"Coulomb barrier out of range: {fus['barrier_V_B_MeV']}"
    assert fus["sigma_fusion_mb"] > 400.0, f"Fusion cross section too small: {fus['sigma_fusion_mb']}"
    assert fus["l_crit_hbar"] > 20.0, "Should populate high spin states"

    # Evaporation residues
    residues = simulate_statistical_evaporation_cascade(56, 134, fus["compound_excitation_E_ex_MeV"], fus["sigma_fusion_mb"])
    assert len(residues) > 0, "Must produce evaporation residues"
    top_channel = residues[0]["channel"]
    assert "n" in top_channel, f"Neutron evaporation should dominate: {top_channel}"
    print("  ✓ compound_nucleus_evaporation_calculator passed.")


def test_experimental_uncertainty_covariance_calculator():
    print("Testing experimental_uncertainty_covariance_calculator...")
    # Linear covariance propagation
    cov_x = [[0.04, 0.0], [0.0, 0.09]]
    jac = [[1.0, 2.0], [3.0, -1.0]]
    res_prop = propagate_linear_covariance(cov_x, jac)
    assert abs(res_prop["cov_y"][0][0] - (0.04 + 4.0 * 0.09)) < 1e-5

    # Baker-Cousins deviance vs Neyman in low counts
    obs = [0, 2, 5]
    exp = [0.5, 2.1, 4.8]
    bc = calculate_baker_cousins_deviance(obs, exp)
    assert bc["chi2_baker_cousins"] > 0.0, "Deviance must be positive"
    assert bc["chi2_neyman"] == "Undefined (n_i = 0)", "Neyman must flag zero counts"

    # Double-root triage
    dr = resolve_double_root_delta_mixing(
        A2_exp=-0.28, A2_uncert=0.04, F11=-0.448, F12=-0.418, F22=-0.190,
        alpha_K_exp=0.033, alpha_K_M1=0.035, alpha_K_E2=0.012
    )
    assert "Root 1" in dr["recommended_root"], "Root 1 must be selected by alpha_K triage"
    print("  ✓ experimental_uncertainty_covariance_calculator passed.")


def test_collective_quadrupole_pes_calculator():
    print("Testing collective_quadrupole_pes_calculator...")
    pes_tri = scan_potential_energy_surface(-20.0, 0.0, 30.0, 0.0, 10.0, 80.0)
    assert pes_tri["shape_classification"] == "Triaxial", "Should detect triaxial minimum"
    assert pes_tri["gamma_barrier_Delta_V_MeV"] > 1.0, "Triaxial well should have significant barrier"
    assert pes_tri["rigidity_ratio"] > 1.2, "Rigidity ratio must reflect stable triaxial well"

    pes_soft = scan_potential_energy_surface(-15.0, 0.0, 35.0, 0.0, 15.0, 0.0)
    assert pes_soft["gamma_stiffness_C_gamma_MeV"] == 0.0, "Gamma-soft potential must have zero gamma stiffness"
    assert "Gamma-Soft" in pes_soft["softness_verdict"], "Should identify Wilets-Jean gamma-softness"
    print("  ✓ collective_quadrupole_pes_calculator passed.")


def test_hpge_pulse_processing_pole_zero_calculator():
    print("Testing hpge_pulse_processing_pole_zero_calculator...")
    # Zero ballistic deficit when flat top >= collection time
    bd_zero = calculate_ballistic_deficit(charge_collection_time_ns=400.0, trapezoid_rise_time_ns=2000.0, trapezoid_flat_top_ns=500.0)
    assert bd_zero["ballistic_deficit_fraction"] == 0.0, "BD must be zero when flat top covers collection time"

    # Active ballistic deficit when flat top < collection time
    bd_act = calculate_ballistic_deficit(charge_collection_time_ns=500.0, trapezoid_rise_time_ns=2000.0, trapezoid_flat_top_ns=300.0)
    assert bd_act["ballistic_deficit_fraction"] > 0.0, "BD must be non-zero when flat top is insufficient"

    # PZ cancellation
    pz_perf = simulate_pole_zero_compensation(tau_preamp_us=50.0, tau_pz_setting_us=50.0)
    assert "Perfect" in pz_perf["cancellation_verdict"], "Must confirm exact cancellation"

    # Pileup throughput
    pu = calculate_high_rate_pileup(input_count_rate_cps=50000.0, trapezoid_rise_time_us=2.0, trapezoid_flat_top_us=0.8)
    assert pu["non_paralyzable_throughput_cps"] > 35000.0, "Throughput calculation sanity check"
    print("  ✓ hpge_pulse_processing_pole_zero_calculator passed.")


def test_chiral_geometry_tac_calculator():
    print("Testing chiral_geometry_tac_calculator...")
    geom = calculate_chiral_geometry(j_p=5.5, j_n=5.5, R_m=8.0, R_s=0.5, R_l=0.5)
    assert geom["chiral_volume_metric"] > 0.8, "Should have near-maximum chiral aplanarity"
    assert "Static_Chiral_Rotation" in geom["chiral_phase"], "Intermediate R must produce static chirality"

    # Chiral doublet criteria
    audit = evaluate_chiral_doublet_criteria(delta_energy_keV=42.0, bm1_in_over_out=1.1, be2_band1_over_band2=1.05, I_spin=12.0)
    assert audit["verdict"] == "ROBUST_CHIRAL_DOUBLET_CONFIRMED", "Should pass 4/4 chiral criteria"
    print("  ✓ chiral_geometry_tac_calculator passed.")


def test_beta_decay_log_ft_phase_space_calculator():
    print("Testing beta_decay_log_ft_phase_space_calculator...")
    # Superallowed 0+ -> 0+
    res = calculate_log_ft(Q_beta_MeV=3.211, half_life_sec=6.345, Z_daughter=12, A=26, decay_mode="beta_plus")
    assert 3.40 < res["log10_ft"] < 3.55, f"Unexpected superallowed log(ft): {res['log10_ft']}"
    assert "Superallowed" in res["forbiddenness_classification"], "Must classify 0+->0+ correctly"

    cvc = verify_superallowed_cvc_vud(res["ft_value_sec"])
    assert 0.96 < cvc["extracted_V_ud"] < 1.00, f"Extracted V_ud out of physical range: {cvc['extracted_V_ud']}"
    print("  ✓ beta_decay_log_ft_phase_space_calculator passed.")


def test_gallagher_moszkowski_coupling_calculator():
    print("Testing gallagher_moszkowski_coupling_calculator...")
    gm = evaluate_gallagher_moszkowski_rule(Omega_p=2.5, Lambda_p=2, Omega_n=2.5, Lambda_n=3, A_mass=130)
    assert gm["GM_favored_K"] == 0.0, "K=0 must be favored when spins have opposite signs"
    assert gm["is_K_zero_band"], "Must flag K=0 band"
    assert gm["predicted_GM_splitting_keV"] > 30.0, "Doublet splitting must be positive"

    # Newby shift spectrum
    newby = calculate_newby_shift_spectrum(A_rot_keV=20.0, Newby_aN_keV=30.0, max_spin=4)
    assert len(newby) == 5, "Should compute 5 levels"
    # For I=0, shift is -a_N = -30
    assert newby[0]["newby_shift_keV"] == -30.0
    print("  ✓ gallagher_moszkowski_coupling_calculator passed.")


def test_nilsson_model_hamiltonian_diagonalizer():
    print("Testing nilsson_model_hamiltonian_diagonalizer...")
    res = solve_nilsson_subblock(N=4, Omega=0.5, epsilon_2=0.20, A_mass=130)
    assert len(res) == 5, f"Shell N=4, Omega=1/2 should have 5 basis states, got {len(res)}"
    assert res[0]["energy_MeV"] < res[-1]["energy_MeV"], "Eigenvalues must be sorted"
    assert "Down-sloping" in res[0]["slope_prolate_driving"], "Lowest state should be prolate-stabilizing"
    print("  ✓ nilsson_model_hamiltonian_diagonalizer passed.")


def test_fission_fragment_mass_yield_calculator():
    print("Testing fission_fragment_mass_yield_calculator...")
    tke = calculate_viola_tke(Z_cn=92, A_cn=236)
    assert 165.0 < tke["mean_viola_TKE_MeV"] < 175.0, f"Viola TKE unexpected: {tke['mean_viola_TKE_MeV']}"
    assert tke["TKE_Standard_I_MeV"] > tke["TKE_Superlong_MeV"], "ST-I TKE must exceed Superlong"

    dist = calculate_fission_fragment_distribution(92, 236)
    assert 130 < dist["peak_heavy_fragment_A"] < 145, f"Heavy peak unexpected: {dist['peak_heavy_fragment_A']}"
    assert 2.0 < dist["mean_prompt_neutron_multiplicity"] < 4.5, "Prompt neutron multiplicity sanity check"
    print("  ✓ fission_fragment_mass_yield_calculator passed.")


def test_pulse_shape_discrimination_psd_calculator():
    print("Testing pulse_shape_discrimination_psd_calculator...")
    ccm = calculate_charge_comparison_psd(f_slow_gamma=0.12, f_slow_neutron=0.28)
    assert ccm["psd_ratio_neutron"] > ccm["psd_ratio_gamma"], "Neutron tail charge must exceed gamma"
    assert ccm["psd_centroid_separation"] > 0.08, "PSD centroids must be separated"

    fom = calculate_figure_of_merit(ccm["psd_ratio_gamma"], 0.020, ccm["psd_ratio_neutron"], 0.028, energy_MeVee=1.5)
    assert fom["fom_at_current_energy"] > 1.20, "FOM at 1.5 MeVee should provide clean separation"
    print("  ✓ pulse_shape_discrimination_psd_calculator passed.")


def test_multi_quasiparticle_blocked_bcs_calculator():
    print("Testing multi_quasiparticle_blocked_bcs_calculator...")
    qps = [
        {"name": "p1", "energy_MeV": 0.2, "Omega": 3.5, "parity": 1},
        {"name": "p2", "energy_MeV": 0.4, "Omega": 4.5, "parity": -1}
    ]
    mqp = calculate_multi_quasiparticle_energy(qps, core_G_pairing_MeV=0.18, target_particles=10)
    assert mqp["total_K"] == 8.0, "K must sum to 8.0"
    assert mqp["total_parity"] == "-", "Parity must be odd (-)"
    assert mqp["blocked_pairing_gap_Delta_b_MeV"] < mqp["unblocked_pairing_gap_Delta0_MeV"], "Blocking must quench gap"
    print("  ✓ multi_quasiparticle_blocked_bcs_calculator passed.")


def test_internal_pair_creation_ipc_calculator():
    print("Testing internal_pair_creation_ipc_calculator...")
    ipc_below = calculate_ipc_coefficient(E_gamma_MeV=0.8, multipolarity="E1")
    assert "Below" in ipc_below["status"], "Must reject E < 1.022 MeV"

    ipc_e0 = calculate_ipc_coefficient(E_gamma_MeV=6.05, multipolarity="E0")
    assert "Forbidden" in ipc_e0["status"], "Single gamma must be forbidden for E0"

    ipc_m1 = calculate_ipc_coefficient(E_gamma_MeV=18.15, multipolarity="M1")
    assert ipc_m1["alpha_pi"] > 0.001, "High-energy M1 must have active IPC"

    ang = calculate_angular_correlation(18.15, "M1", theta_deg=139.0, m_X_boson_MeV=17.0)
    assert ang["exotic_boson_resonance"]["is_near_peak"], "ATOMKI 17 MeV boson peak should align with ~139 deg"
    print("  ✓ internal_pair_creation_ipc_calculator passed.")


def test_rmf_deformed_constrained_calculator():
    print("Testing rmf_deformed_constrained_calculator...")
    sph = calculate_rmf_spherical_ground_state(Z=56, A=130)
    assert 500.0 < sph["effective_mass_Mstar_MeV"] < 600.0, "Effective mass M* out of NL3 range"
    assert sph["scalar_potential_depth_MeV"] < -350.0, "Scalar potential depth check"
    assert sph["vector_potential_depth_MeV"] > 280.0, "Vector potential depth check"

    pes = scan_rmf_constrained_pes(56, 130)
    assert pes["equilibrium_beta_2"] > 0.20, "130Ba must have deformed ground state"
    assert pes["spherical_barrier_height_MeV"] > 5.0, "Deformation barrier sanity check"
    print("  ✓ rmf_deformed_constrained_calculator passed.")


def test_isobaric_analog_state_ced_calculator():
    print("Testing isobaric_analog_state_ced_calculator...")
    de = calculate_coulomb_displacement_energy(Z_parent=24, A_mass=49)
    assert 8.0 < de["Coulomb_displacement_empirical_MeV"] < 9.5, f"Unexpected Coulomb displacement: {de['Coulomb_displacement_empirical_MeV']}"

    spins = [3.5, 5.5, 7.5, 9.5, 11.5, 13.5]
    ep = [261.0, 1073.0, 1982.0, 3173.0, 4679.0, 6420.0]
    en = [272.0, 1083.0, 1970.0, 3130.0, 4580.0, 6380.0]
    ced = analyze_mirror_ced_sequence(spins, ep, en)
    assert abs(ced["maximum_CED_jump_keV"]) > 30.0, "Must detect alignment jump in CED"
    print("  ✓ isobaric_analog_state_ced_calculator passed.")


def test_gamma_cascade_calorimetry_calculator():
    print("Testing gamma_cascade_calorimetry_calculator...")
    casc = simulate_gamma_cascade(entry_spin_I=20.0, entry_excitation_MeV=22.0, A_mass=130)
    assert casc["collective_E2_multiplicity"] == 10.0, "Collective E2 multiplicity must equal I/2"
    assert casc["statistical_E1_multiplicity"] > 0, "Must have statistical cooling photons"
    assert casc["measured_mean_fold"] < casc["total_true_multiplicity"], "Calorimeter fold < true M due to efficiency"

    triage = compare_evaporation_channel_entry_points(compound_excitation_MeV=58.0, A_cn=134)
    assert len(triage) == 3, "Should compute 3n, 4n, 5n channels"
    assert triage[0]["entry_excitation_MeV"] > triage[1]["entry_excitation_MeV"], "Fewer evaporated neutrons -> higher entry energy"
    print("  ✓ gamma_cascade_calorimetry_calculator passed.")


def test_wigner_supermultiplet_su4_calculator():
    print("Testing wigner_supermultiplet_su4_calculator...")
    we = calculate_wigner_energy(Z=24, A=48)
    assert we["is_N_equals_Z"], "48Cr must be recognized as N=Z"
    assert we["su4_casimir_C2"] == 0.0, "Even-even T=0 ground state has C2 = 0"

    su4_odd = calculate_su4_casimir(Z=23, A=47)
    assert su4_odd["casimir_C2"] > 0.0, "Odd-A has positive Casimir invariant"
    print("  ✓ wigner_supermultiplet_su4_calculator passed.")


def test_linear_momentum_transfer_incomplete_fusion_calculator():
    print("Testing linear_momentum_transfer_incomplete_fusion_calculator...")
    lmt_cf = calculate_linear_momentum_transfer(A_p=16, Z_p=8, A_t=238, Z_t=92, E_lab_MeV=160.0, fractional_LMT=1.0)
    assert "Complete_Fusion" in lmt_cf["reaction_regime"], "Must identify CF at rho=1"
    assert 145.0 < lmt_cf["predicted_folding_angle_deg"] < 165.0, f"Folding angle out of range: {lmt_cf['predicted_folding_angle_deg']}"

    lmt_icf = calculate_linear_momentum_transfer(A_p=16, Z_p=8, A_t=238, Z_t=92, E_lab_MeV=160.0, fractional_LMT=0.6)
    assert lmt_icf["predicted_folding_angle_deg"] > lmt_cf["predicted_folding_angle_deg"], "ICF must have wider folding angle than CF"
    print("  ✓ linear_momentum_transfer_incomplete_fusion_calculator passed.")


def test_rdds_plunger_lifetime_calculator():
    print("Testing rdds_plunger_lifetime_calculator...")
    kin = calculate_flight_time_and_shifts(distance_um=50.0, beta_v_over_c=0.015, E_0_keV=400.0)
    assert kin["Doppler_shift_keV"] > 0, "Doppler shift must be positive at forward angle"
    assert kin["flight_time_ps"] > 1000.0, "Flight time sanity check"

    # Inversion test
    dist = [10.0, 25.0, 50.0, 80.0, 120.0]
    iu = [90.0, 75.0, 52.0, 32.0, 16.0]
    iss = [10.0, 25.0, 48.0, 68.0, 84.0]
    fit_res = fit_exponential_rdds_lifetime(dist, iu, iss, beta_v_over_c=0.015)
    assert fit_res["extracted_lifetime_ps"] > 0, "Extracted lifetime must be positive"

    em = convert_lifetime_to_be2_and_qt(tau_ps=15.0, E_gamma_keV=400.0)
    assert em["B_E2_e2_b2"] > 0, "B(E2) must be positive"
    assert em["transition_quadrupole_moment_Qt_eb"] > 0, "Qt must be positive"
    print("  ✓ rdds_plunger_lifetime_calculator passed.")


def test_double_beta_decay_nme_calculator():
    print("Testing double_beta_decay_nme_calculator...")
    res_ge = invert_majorana_mass_limit(isotope_key="76Ge", half_life_limit_yr=1.8e26)
    assert 100.0 < res_ge["effective_majorana_mass_upper_bound_meV"] < 300.0, "76Ge mass bound out of expected range"
    assert "Degenerate" in res_ge["neutrino_mass_hierarchy_regime"], "Should be in degenerate hierarchy"

    pred = predict_half_life_for_target_mass(isotope_key="76Ge", target_mass_meV=20.0)
    assert pred["predicted_required_half_life_yr"] > 1.0e27, "Must require > 1e27 yr to cover inverted hierarchy"
    print("  ✓ double_beta_decay_nme_calculator passed.")


def test_heavy_ion_elastic_rainbow_scattering_calculator():
    print("Testing heavy_ion_elastic_rainbow_scattering_calculator...")
    kin = calculate_scattering_kinematics(Z_p=8, A_p=16, Z_t=82, A_t=208, E_lab_MeV=100.0)
    assert kin["grazing_angular_momentum_hbar"] > 10.0, "Grazing angular momentum sanity check"
    assert 120.0 < kin["blair_quarter_point_angle_deg"] < 150.0, "Blair quarter point angle check"

    rb = scan_nuclear_rainbow(kin)
    assert rb["is_rainbow_active"], "Nuclear rainbow should be active for 16O+208Pb"
    assert rb["rainbow_angle_deg"] < kin["blair_quarter_point_angle_deg"], "Rainbow angle is inside quarter point"
    print("  ✓ heavy_ion_elastic_rainbow_scattering_calculator passed.")


def test_core_polarization_effective_charge_calculator():
    print("Testing core_polarization_effective_charge_calculator...")
    th = calculate_microscopic_polarization_charges(Z_core=82, A_core=208)
    assert th["theoretical_proton_effective_charge_e"] > 1.20, "Proton effective charge should be ~ 1.3-1.5 e"
    assert 0.35 < th["theoretical_neutron_effective_charge_e"] < 0.65, "Neutron effective charge should be ~ 0.4-0.6 e"

    inv = invert_effective_charge_from_be2(B_E2_e2_fm4=45.0, j_initial=4.5, j_final=2.5, A_mass=209, is_neutron=True)
    assert 0.5 < inv["extracted_effective_charge_e"] < 1.0, "Empirical effective charge sanity check"
    print("  ✓ core_polarization_effective_charge_calculator passed.")


def test_fission_isomer_double_hump_transmission_calculator():
    print("Testing fission_isomer_double_hump_transmission_calculator...")
    iso = calculate_fission_isomer_properties(V_A=6.0, hw_A=0.9, E_II=2.5, V_B=5.5, hw_B=0.6)
    assert iso["isomer_half_life_seconds"] > 0, "Isomer half-life must be positive"
    assert "ns" in iso["formatted_half_life"] or "us" in iso["formatted_half_life"], "Should be in ns or us range"

    trans_res = evaluate_double_barrier_transmission(energy_MeV=4.5, V_A=6.0, hw_A=0.9, E_II=2.5, V_B=5.5, hw_B=0.6)
    assert trans_res["is_intermediate_resonance"], "4.5 MeV should hit intermediate resonance in second well"
    assert trans_res["total_transmission_T"] > 0.5, "Resonant transmission should be near 1.0"
    print("  ✓ fission_isomer_double_hump_transmission_calculator passed.")


def test_abrasion_ablation_fragmentation_calculator():
    print("Testing abrasion_ablation_fragmentation_calculator...")
    abr = calculate_geometric_abrasion(A_p=136, Z_p=54, A_t=9, Z_t=4, impact_parameter_fm=4.0)
    assert abr["pre_fragment_mass_A_pre"] > 80.0, "Pre-fragment mass sanity check"
    assert abr["pre_fragment_excitation_MeV"] > 100.0, "Pre-fragment should carry significant excitation"

    abl = simulate_ablation_cooling(abr["pre_fragment_mass_A_pre"], abr["pre_fragment_charge_Z_pre"], abr["pre_fragment_excitation_MeV"], A_projectile=136)
    assert abl["final_fragment_A"] < abr["pre_fragment_mass_A_pre"], "Ablation must cool by evaporating nucleons"
    assert abl["goldhaber_momentum_width_MeV_c"] > 200.0, "Goldhaber width check"
    print("  ✓ abrasion_ablation_fragmentation_calculator passed.")


def test_chiral_vibrational_tunneling_calculator():
    print("Testing chiral_vibrational_tunneling_calculator...")
    # Low spin: vibrational splitting
    pt_vib = evaluate_chiral_potential_at_spin(spin_I=10.0, I_crit=11.0, I_rest=18.0)
    assert not pt_vib["is_double_well"], "I=10 should be single well"
    assert pt_vib["predicted_chiral_splitting_DeltaE_keV"] > 200.0, "Vibrational splitting should be large"

    # Mid spin: double well static chirality
    pt_static = evaluate_chiral_potential_at_spin(spin_I=16.0, I_crit=11.0, I_rest=18.0)
    assert pt_static["is_double_well"], "I=16 must develop double well"
    assert pt_static["predicted_chiral_splitting_DeltaE_keV"] < 60.0, "Static chirality should have degenerate splitting"
    print("  ✓ chiral_vibrational_tunneling_calculator passed.")


def test_clover_compton_addback_polarization_calculator():
    print("Testing clover_compton_addback_polarization_calculator...")
    ab = calculate_clover_addback_factor(E_gamma_keV=1000.0)
    assert 1.30 < ab["addback_factor_F"] < 1.60, f"Addback factor unexpected: {ab['addback_factor_F']}"

    pol = analyze_clover_polarization(N_perp=14200.0, N_parallel=10500.0, E_gamma_keV=846.0, a_geom=1.0)
    assert pol["linear_polarization_P"] > 0.5, "Perpendicular excess should yield strong positive polarization"
    assert "Electric" in pol["electromagnetic_character"], "Positive P must diagnose Electric multipolarity"
    print("  ✓ clover_compton_addback_polarization_calculator passed.")


def test_strutinsky_shell_correction_calculator():
    print("Testing strutinsky_shell_correction_calculator...")
    levels = [-40.0 + i * 0.9 for i in range(50)]
    res = calculate_strutinsky_shell_correction(levels, particle_number=40, gamma_smoothing_MeV=8.0)
    assert abs(res["shell_correction_delta_U_MeV"]) < 50.0, "Shell correction sanity check"
    assert res["smooth_energy_MeV"] < 0, "Smooth energy should be negative"
    print("  ✓ strutinsky_shell_correction_calculator passed.")


def test_nilsson_magnetic_moment_gk_calculator():
    print("Testing nilsson_magnetic_moment_gk_calculator...")
    gk = calculate_nilsson_gk(Omega=2.5, Lambda=2, A_mass=131, Z_charge=56, is_neutron=True)
    assert gk["g_l"] == 0.0, "Neutron orbital g-factor is 0"
    assert gk["g_s_effective"] < 0.0, "Neutron spin g-factor is negative"

    mu_head = calculate_magnetic_dipole_moment(spin_I=2.5, Omega_K=2.5, g_K=gk["g_K"], g_R=gk["g_R"])
    assert abs(mu_head) < 5.0, "Magnetic moment sanity check"

    inv = invert_gk_from_bm1_be2(spin_I=4.5, E_gamma_cross_keV=750.0, E_gamma_step_keV=380.0, I_gamma_cross=40.0, I_gamma_step=100.0)
    assert inv["extracted_abs_gK_minus_gR"] > 0.0, "Must extract non-zero |gK - gR|"
    print("  ✓ nilsson_magnetic_moment_gk_calculator passed.")


def test_angular_momentum_projection_amp_calculator():
    print("Testing angular_momentum_projection_amp_calculator...")
    spec = project_rotational_spectrum(max_spin_I=6, Jy2_expectation=30.0, E_intrinsic_MeV=-120.0, A_rot_peierls_MeV=0.020)
    assert len(spec) == 4, "Should project I = 0, 2, 4, 6"
    assert spec[0]["spin_I"] == 0, "First state must be I=0"
    assert spec[0]["projected_norm_N_I"] > 0, "Norm must be positive"
    print("  ✓ angular_momentum_projection_amp_calculator passed.")


def test_spin_dipole_resonance_sdr_calculator():
    print("Testing spin_dipole_resonance_sdr_calculator...")
    th = calculate_sdr_sum_rule(Z=82, A=208, delta_r_np_fm=0.16)
    assert 900.0 < th["total_SDR_sum_rule_fm2"] < 1300.0, f"208Pb SDR sum rule unexpected: {th['total_SDR_sum_rule_fm2']}"
    assert th["multipole_SDR_2_minus_fm2"] > th["multipole_SDR_1_minus_fm2"], "2- multipole has largest 2J+1 weight"

    inv = invert_neutron_skin_from_sdr(S_minus_exp_fm2=1030.0, S_plus_exp_fm2=0.0, Z=82, A=208)
    assert 0.05 < inv["extracted_neutron_skin_fm"] < 0.20, f"Extracted neutron skin out of range: {inv['extracted_neutron_skin_fm']}"
    print("  ✓ spin_dipole_resonance_sdr_calculator passed.")


def test_gamma_gamma_matrix_slicer_calculator():
    print("Testing gamma_gamma_matrix_slicer_calculator...")
    mat = generate_synthetic_cascade_matrix(cascade_energies_keV=[200.0, 350.0, 500.0, 650.0], matrix_dim=100)
    assert mat["total_matrix_counts"] > 100000.0, "Matrix counts sanity check"

    sl = slice_matrix_gate(mat, gate_energy_keV=350.0, gate_width_keV=12.0)
    assert sl["peak_to_background_ratio"] > 0.3, "P/B ratio check"
    assert len(sl["coincident_cascade_peaks"]) == 3, "Should find 3 coincident cascade peaks"
    assert sl["coincident_cascade_peaks"][0]["net_coincident_area"] > 1000.0, "Coincidence area check"
    print("  ✓ gamma_gamma_matrix_slicer_calculator passed.")


def test_nolen_schiffer_isospin_anomaly_calculator():
    print("Testing nolen_schiffer_isospin_anomaly_calculator...")
    res = evaluate_nolen_schiffer_anomaly(Z_core=20, A_mass=41, Delta_E_C_exp_MeV=7.278, r_charge_fm=3.48)
    assert 150.0 < res["nolen_schiffer_anomaly_keV"] < 350.0, f"41Sc NSA unexpected: {res['nolen_schiffer_anomaly_keV']}"
    assert res["underestimation_percentage"] > 2.0, "Theoretical underestimation must be positive"
    assert "CSB" in res["csb_mechanism_verdict"], "Must diagnose CSB force need"
    print("  ✓ nolen_schiffer_isospin_anomaly_calculator passed.")


def test_multiphonon_wobbling_anharmonic_calculator():
    print("Testing multiphonon_wobbling_anharmonic_calculator...")
    th = evaluate_multiphonon_wobbling_energies(omega_wob_keV=320.0, Delta_anharm_keV=-40.0)
    assert th["energy_ratio_R21"] < 2.0, "Subharmonic softening check"
    assert "Subharmonic" in th["classification"], "Should classify as subharmonic softening"

    aud = audit_multiphonon_wobbling_candidate(E0_keV=0.0, E1_keV=320.0, E2_keV=600.0, be2_2_to_1=0.62, be2_1_to_0=0.32, be2_2_to_0=0.015)
    assert aud["score"] == "3/3", "Must satisfy all 3 multi-phonon wobbling checks"
    assert "CONFIRMED" in aud["verdict"], "Should confirm two-phonon wobbling candidate"
    print("  ✓ multiphonon_wobbling_anharmonic_calculator passed.")


def test_rmf_symmetry_energy_slope_calculator():
    print("Testing rmf_symmetry_energy_slope_calculator...")
    eos_ddme2 = calculate_rmf_symmetry_energy(rho=0.153, J_val_MeV=32.3, L_val_MeV=51.2)
    assert 30.0 < eos_ddme2["symmetry_energy_S_MeV"] < 35.0, "Symmetry energy at saturation check"
    assert 11.5 < eos_ddme2["predicted_NS_radius_1p4Msun_km"] < 13.5, "Neutron star radius check"
    assert eos_ddme2["crust_core_transition_density_fm3"] > 0.05, "Crust-core transition density check"

    curve = scan_symmetry_energy_curve(J_val_MeV=32.3, L_val_MeV=51.2)
    assert len(curve) > 10, "Density scan check"
    print("  ✓ rmf_symmetry_energy_slope_calculator passed.")


def test_wigner_racah_algebra_9j_calculator():
    print("Testing wigner_racah_algebra_9j_calculator...")
    # Zero-entry 9j identity: 9j(1 1 2; 1 1 2; 2 2 0) = 1/150 ~ 0.006667
    val_zero = wigner_9j(1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 2.0, 2.0, 0.0)
    assert abs(val_zero - 1.0 / 150.0) < 1e-6, f"9j zero-entry reduction failed: {val_zero}"

    rec = calculate_ls_to_jj_recoupling(1, 0.5, 1.5, 1, 0.5, 1.5, 2, 0, 2)
    assert abs(rec["recoupling_coefficient"] - 1.0 / math.sqrt(3.0)) < 1e-5, "LS to jj recoupling bracket check"
    assert abs(rec["recoupling_probability"] - 1.0 / 3.0) < 1e-5, "Recoupling probability check"
    print("  ✓ wigner_racah_algebra_9j_calculator passed.")


def test_charge_exchange_gt_quenching_calculator():
    print("Testing charge_exchange_gt_quenching_calculator...")
    res = deconvolve_gt_quenching(Z=82, A=208)
    assert res["ikeda_sum_rule_3N_minus_Z"] == 132, "Ikeda sum rule for 208Pb must be 132"
    assert 50.0 < res["peak_observed_fraction"] < 65.0, "Observed peak fraction check"
    assert 10.0 < res["delta_isobar_quenching_fraction"] < 25.0, "Delta isobar fraction check"
    assert res["effective_axial_coupling_g_A_eff"] < 1.10, "In-medium g_A must be quenched"
    print("  ✓ charge_exchange_gt_quenching_calculator passed.")


def test_alignment_attenuation_coefficients_calculator():
    print("Testing alignment_attenuation_coefficients_calculator...")
    att = calculate_alignment_attenuation_factors(spin_I=6.0, sigma_over_I=0.30)
    assert 0.70 < att["alpha_2_attenuation"] < 0.90, "alpha_2 attenuation factor check"
    assert att["alpha_4_attenuation"] < att["alpha_2_attenuation"], "alpha_4 must be smaller than alpha_2"

    inv = invert_sigma_over_I_from_stretched_e2(a2_measured=0.28, spin_I=6.0, a2_max_theoretical=0.357)
    assert 0.25 < inv["inverted_sigma_over_I"] < 0.35, "Inverted sigma/I sanity check"
    print("  ✓ alignment_attenuation_coefficients_calculator passed.")


def test_r_process_waiting_point_flow_calculator():
    print("Testing r_process_waiting_point_flow_calculator...")
    s_n_0 = calculate_waiting_point_separation_energy(temperature_T9=1.5, neutron_density_cm3=1.0e24)
    assert 2.0 < s_n_0 < 4.0, f"Waiting point S_n^0 out of expected r-process range: {s_n_0}"

    A_vals = [126, 127, 128, 129, 130, 131, 132, 133]
    Sn_vals = [4.8, 3.8, 4.2, 3.2, 3.0, 1.2, 1.5, 0.9]
    res_saha = calculate_isotopic_saha_equilibrium(Z_element=48, A_list=A_vals, S_n_list=Sn_vals, temperature_T9=1.5, neutron_density_cm3=1.0e24)
    assert res_saha["waiting_point_isotope_A"] in [129, 130], "Waiting point should stall at 129Cd/130Cd"
    print("  ✓ r_process_waiting_point_flow_calculator passed.")


def test_wobbling_branching_ratio_phase_calculator():
    print("Testing wobbling_branching_ratio_phase_calculator...")
    th = calculate_theoretical_wobbling_delta(spin_I=15.5, spin_j=5.5, gamma_deg=26.0, E_gamma_keV=720.0, Q_0_eb=5.0, g_j=1.25, g_R=0.40, wobbling_mode="TW")
    assert th["theoretical_delta_E2_M1"] is None, "Intrinsic inputs cannot specify transition matrix elements"

    comp = compare_wobbling_with_experimental_roots(th["theoretical_delta_E2_M1"], root_1_exp=-0.15, root_2_exp=3.10)
    assert not comp["is_wobbling_confirmed"], "Model preference is not independent experimental evidence"
    assert comp["selected_matching_root"] is None, "Both candidate roots must remain"
    assert len(comp["candidates"]) == 2
    print("  ✓ wobbling_branching_ratio_phase_calculator passed.")


def test_gdr_lorentzian_trk_sumrule_calculator():
    print("Testing gdr_lorentzian_trk_sumrule_calculator...")
    trk = calculate_trk_sum_rule(Z=82, A=208, kappa_mec=0.25)
    assert 2900.0 < trk["classical_TRK_sum_MeV_mb"] < 3000.0, "Classical TRK sum rule check"
    assert trk["total_enhanced_sum_MeV_mb"] > 3600.0, "MEC enhanced sum rule check"

    gdr_split = calculate_deformed_gdr_splitting(Z=82, A=208, beta_2=0.30)
    assert gdr_split["E1_low_mode_MeV"] < gdr_split["E2_high_mode_MeV"], "Prolate splitting check"
    assert abs(gdr_split["energy_ratio_E2_over_E1"] - 1.285) < 0.05, "Danos frequency ratio check"

    rec_beta = invert_beta2_from_gdr_peaks(E1_MeV=11.54, E2_MeV=14.83)
    assert abs(rec_beta - 0.30) < 0.05, "GDR beta2 inversion check"
    print("  ✓ gdr_lorentzian_trk_sumrule_calculator passed.")


def test_isovector_giant_resonance_splitting_calculator():
    print("Testing isovector_giant_resonance_splitting_calculator...")
    res = calculate_isovector_splitting(Z=82, A=208, resonance_type="IVGDR", V_1_lane_MeV=65.0)
    assert res["isospin_T0"] == 22.0, "208Pb isospin check"
    assert 6.0 < res["isospin_splitting_Delta_E_MeV"] < 8.0, "Lane potential splitting check"
    assert res["T_greater_strength_fraction_percent"] < 6.0, "T_> branch should be heavily suppressed in 208Pb"
    assert res["T_lesser_strength_fraction_percent"] > 94.0, "T_< branch should dominate"
    print("  ✓ isovector_giant_resonance_splitting_calculator passed.")


def test_detector_deadtime_pileup_correction_calculator():
    print("Testing detector_deadtime_pileup_correction_calculator...")
    fwd = calculate_deadtime_models(true_rate=30000.0, tau_nonpar=10e-6, tau_par=10e-6, tau_hybrid_p=5e-6, tau_hybrid_n=5e-6, peaking_time=4e-6)
    assert 22000.0 < fwd["non_paralyzable"]["observed_rate_cps"] < 24000.0, "Non-paralyzable rate check"
    assert 21000.0 < fwd["paralyzable"]["observed_rate_cps"] < 23000.0, "Paralyzable rate check"
    assert fwd["pileup_diagnostics"]["pileup_loss_fraction"] > 0.15, "Pileup loss fraction check"

    inv = invert_observed_rate(observed_rate=22000.0, tau_nonpar=10e-6, tau_par=10e-6)
    assert inv["paralyzable_dual_root_inversion"]["is_physically_admissible"], "Must find dual roots"
    assert inv["paralyzable_dual_root_inversion"]["dual_root_discrepancy_ratio"] > 5.0, "Paralyzed branch must be much higher"
    print("  ✓ detector_deadtime_pileup_correction_calculator passed.")


def test_heavy_ion_fusion_evaporation_channel_calculator():
    print("Testing heavy_ion_fusion_evaporation_channel_calculator...")
    res = analyze_heavy_ion_fusion(
        Z_p=16, A_p=36, Z_t=42, A_t=100, E_lab_MeV=155.0, illustrative_xn=True
    )
    assert res["entrance_channel"]["compound_nucleus"] == "Z=58, A=136", "Compound nucleus check"
    assert 78.0 < res["barrier_and_fusion"]["V_barrier_MeV"] < 85.0, "Coulomb barrier check"
    assert res["barrier_and_fusion"]["schematic_wong_cross_section_mb"] > 900.0, "Schematic Wong cross section check"
    assert res["barrier_and_fusion"]["sigma_fusion_mb"] is None, "Physical cross section must not be fabricated"
    assert res["in_beam_spectroscopy"]["recoil_velocity_pct_c"] > 2.0, "Recoil velocity check"
    assert "4n" in res["evaporation_channels"] and "5n" in res["evaporation_channels"], "Evaporation channels check"
    assert res["evaporation_channels"]["4n"]["cross_section_mb"] is None
    assert res["evaporation_channels"]["4n"]["illustrative"]["normalized_weight_within_displayed_xn"] is not None
    print("  ✓ heavy_ion_fusion_evaporation_channel_calculator passed.")


def test_poisson_likelihood_peak_fitting_bias_calculator():
    print("Testing poisson_likelihood_peak_fitting_bias_calculator...")
    res = evaluate_peak_fitting_methods(true_area=60.0, centroid=50.0, sigma=2.0, bg_counts=2.0, seed=42)
    poi = res["poisson_mle_baker_cousins"]
    assert poi["fitted_area_counts"] >= 0.0, "Nonnegative area constraint"
    assert poi["min_deviance_chi_lambda2"] <= poi["null_deviance_A0"] + 1e-8, "MLE includes the null"
    interval = poi["profile_likelihood_interval"]
    assert interval["lower_counts"] <= poi["fitted_area_counts"] <= interval["upper_counts"]
    assert res["simulation"]["kind"] == "single-realization-not-ensemble-bias"
    print("  ✓ poisson_likelihood_peak_fitting_bias_calculator passed.")


def test_coriolis_attenuation_bandcrossing_calculator():
    print("Testing coriolis_attenuation_bandcrossing_calculator...")
    mat = calculate_coriolis_matrix_elements(j=5.5, I=15.5, A_rot_keV=15.0, xi=0.75)
    assert len(mat) == 5, "K-manifold elements count check"
    assert mat[0]["attenuated_matrix_element_keV"] < mat[0]["unattenuated_matrix_element_keV"], "Attenuation check"

    demo_spins = [5.5, 7.5, 9.5, 11.5, 13.5, 15.5, 17.5, 19.5, 21.5, 23.5]
    demo_energies = [0.0, 180.0, 480.0, 910.0, 1470.0, 2160.0, 2980.0, 3650.0, 4200.0, 4850.0]
    bb = analyze_backbending_alignment(spins=demo_spins, energies_keV=demo_energies, J0_harris=25.0, J1_harris=35.0)
    assert bb["backbending_diagnostics"]["backbending_observed"], "Backbending should be identified"
    assert bb["backbending_diagnostics"]["maximum_quasiparticle_alignment_ix"] > 8.0, "Quasiparticle alignment check"
    print("  ✓ coriolis_attenuation_bandcrossing_calculator passed.")


def test_directional_correlation_f_coefficients_calculator():
    print("Testing directional_correlation_f_coefficients_calculator...")
    # 2+ -> 0+ stretched E2 (Hamilton Table Appendix 2)
    f2 = calculate_f_coefficient(2, 2, 2, If=0.0, Ii=2.0)
    assert abs(f2 - (-0.5976)) < 1e-3, "F2(2 2 0 2) Hamilton benchmark"

    # Ii = 15/2 -> If = 13/2 dipole/quadrupole mixed transition
    dist = calculate_angular_distribution_coefficients(Ii=7.5, If=6.5, delta=-0.15, alpha2=0.85)
    a2_theo = dist["attenuated_a_k"]["a2"]
    inv = invert_delta_dual_roots(a2_theo, Ii=7.5, If=6.5, alpha2=0.85)
    assert inv["has_real_roots"], "Must yield real roots for physical a2"
    assert abs(inv["root1_small_magnitude"] - (-0.15)) < 1e-3, "Dual root inversion must recover delta=-0.15"

    dco = calculate_dco_and_ado_ratios(Ii=7.5, If=6.5, delta=-0.15, theta1_deg=30.0, theta2_deg=90.0)
    assert dco["R_DCO"] > 1.0, "DCO ratio test"
    print("  ✓ directional_correlation_f_coefficients_calculator passed.")


def test_feldman_cousins_unified_confidence_interval_calculator():
    print("Testing feldman_cousins_unified_confidence_interval_calculator...")
    # 1. Poisson b=0.0 benchmarks (Feldman-Cousins Table IV)
    p0 = calculate_poisson_fc_interval(n_obs=0, background=0.0, cl=0.90)
    assert p0["fc_interval_lower"] == 0.0
    assert abs(p0["fc_interval_upper"] - 2.435) < 0.05, "Poisson b=0 n=0 upper limit ~ 2.44"

    # 2. Poisson b=3.0 benchmarks (Zhu Yongsheng Table 10.2)
    p3 = calculate_poisson_fc_interval(n_obs=0, background=3.0, cl=0.90)
    assert p3["fc_interval_lower"] == 0.0
    assert p3["fc_interval_upper"] < 1.15, "Poisson b=3 n=0 upper limit ~ 0.95 - 1.08"

    # 3. Gaussian observable benchmark with boundary mu >= 0 (Feldman-Cousins Table X)
    g_neg = calculate_gaussian_fc_interval(x_obs=-1.5, sigma=1.0, cl=0.90)
    assert g_neg["mu_fc_lower"] == 0.0
    assert abs(g_neg["mu_fc_upper"] - 0.555) < 0.05, "Gaussian x=-1.5 upper limit ~ 0.55"
    print("  ✓ feldman_cousins_unified_confidence_interval_calculator passed.")


def test_heavy_ion_fusion_wong_calculator():
    print("Testing heavy_ion_fusion_spin_distribution_wong_calculator...")
    res = calculate_heavy_ion_fusion_wong(Z_p=8, A_p=16, Z_t=50, A_t=122, E_lab_MeV=80.0)
    assert abs(res["Wong_cross_section_mb"] - 1030.0) < 5.0, "Wong analytical cross section"
    assert abs(res["partial_wave_sum_cross_section_mb"] - 1030.2) < 5.0, "Partial wave sum cross section"
    assert res["wong_sum_agreement_pct"] > 99.9, "Wong vs partial wave sum convergence > 99.9%"
    assert res["critical_angular_momentum_l_crit_hbar"] == 40
    print("  ✓ heavy_ion_fusion_spin_distribution_wong_calculator passed.")


def test_mariscotti_vmi_rotational_stretching_calculator():
    print("Testing mariscotti_vmi_rotational_stretching_calculator...")
    # 1. Rigid rotor limit: C -> large => R_4/2 = 3.333
    spec_rigid = calculate_vmi_spectrum(J0=35.0, C=2500.0, spins=[2.0, 4.0, 6.0])
    assert abs(spec_rigid["R_4_2_ratio"] - 3.3333) < 0.001, "VMI rigid rotor limit R_4/2 ~ 3.333"

    # 2. Inversion for 168Er
    spins = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
    e_exp = [79.8, 264.1, 548.7, 912.0, 1344.0, 1830.0]
    inv = invert_vmi_parameters(spins, e_exp)
    assert abs(inv["J0_fitted_hbar2_MeV"] - 35.8) < 1.0, "168Er J0 fitted"
    assert inv["rms_residual_keV"] < 5.0, "168Er VMI RMS residual < 5 keV"
    print("  ✓ mariscotti_vmi_rotational_stretching_calculator passed.")


def test_constant_fraction_discriminator_calculator():
    print("Testing constant_fraction_discriminator_fast_timing_calculator...")
    # CFD walk elimination across 10:1 amplitude range
    res = simulate_cfd_walk_elimination(amplitudes_V=[0.5, 1.0, 2.0, 5.0], rise_time_ns=2.0, fraction=0.20)
    assert res["cfd_walk_ps"] < 0.01, "CFD zero walk (< 0.01 ps)"
    assert res["led_walk_ps"] > 250.0, "LED time walk > 250 ps"
    assert res["walk_reduction_factor"] > 10000.0

    # Fast-timing resolution
    timing = calculate_fast_timing_resolution(scint_decay_time_ns=16.0, pmt_tts_fwhm_ns=0.35, N_photoelectrons=2500.0)
    assert timing["total_timing_resolution_FWHM_ps"] < 1000.0, "Sub-nanosecond fast-timing resolution"
    print("  ✓ constant_fraction_discriminator_fast_timing_calculator passed.")


def test_cranked_shell_model_band_crossing_calculator():
    print("Testing cranked_shell_model_band_crossing_v12_inverter...")
    # 164Er two-band avoided crossing benchmark
    csm = calculate_two_band_crossing_csm(omega_c_MeV=0.280, V12_keV=90.0, i_align_hbar=10.0)
    assert abs(csm["minimum_splitting_Delta_e_keV"] - 180.0) < 0.1, "Avoided crossing splitting Delta_e = 2*|V12|"
    assert csm["crossing_classification"].startswith("Smooth Upbending")

    # Verify 50/50 mixing at crossing
    for pt in csm["profile"]:
        if abs(pt["omega_MeV"] - 0.280) < 1e-4:
            assert abs(pt["g_band_percentage"] - 50.0) < 0.5, "50/50 configuration mixing at crossing"
            assert abs(pt["splitting_keV"] - 180.0) < 0.5

    # Inversion test
    w_list = [0.26, 0.27, 0.28, 0.29, 0.30]
    e_yr = [-1156.5, -1271.2, -1404.3, -1558.5, -1729.4]
    e_yrar = [-912.6, -1073.7, -1224.3, -1361.9, -1491.2]
    inv = invert_v12_from_experimental_routhians(w_list, e_yr, e_yrar)
    assert abs(inv["inverted_V12_keV"] - 90.0) < 0.1, "Inverted |V12| = 90 keV"
    print("  ✓ cranked_shell_model_band_crossing_v12_inverter passed.")


def test_in_beam_doppler_broadening_calculator():
    print("Testing in_beam_doppler_broadening_array_correction_calculator...")
    # 134Ce in-beam benchmark at 90 deg: opening angle broadening dominates
    res = calculate_doppler_broadening_budget(E0_keV=1000.0, beta_recoil=0.020, theta_deg=90.0, opening_angle_deg=8.0)
    assert abs(res["broadening_detector_angle_dE_theta_keV"] - 2.79) < 0.1, "90-deg angle broadening"
    assert res["total_observed_fwhm_keV"] > res["intrinsic_detector_fwhm_keV"]

    # AGATA tracking array benchmark with narrow 1.2 deg opening angle
    res_agata = calculate_doppler_broadening_budget(E0_keV=1000.0, beta_recoil=0.025, theta_deg=90.0, opening_angle_deg=1.2)
    assert res_agata["broadening_detector_angle_dE_theta_keV"] < 1.0, "AGATA sub-1 keV angle broadening"
    print("  ✓ in_beam_doppler_broadening_array_correction_calculator passed.")


def test_in_beam_experiment_analysis_pipeline():
    print("Testing in_beam_experiment_analysis_pipeline...")
    # 135Pr wobbling audit pipeline execution
    res = run_full_in_beam_pipeline(
        Z_p=7, A_p=14, Z_t=50, A_t=124, E_lab_MeV=65.0,
        E_gamma_keV=726.5, a2_exp=-0.18, F_tau_exp=0.55
    )
    assert res["pipeline_version"] == "1.0-Production"
    assert res["stage1_entrance_reaction"]["Wong_cross_section_mb"] > 800.0
    assert abs(res["stage4_lifetime_dsam"]["tau_ps"] - 0.677) < 0.05
    assert "delta_root1" in res["stage6_mode_diagnostic"]
    print("  ✓ in_beam_experiment_analysis_pipeline passed.")


def test_tac_3d_chiral_orientation_calculator():
    print("Testing tac_3d_chiral_orientation_energy_surface_calculator...")
    # 134Pr chiral tripod benchmark: planar at J=10, aplanar chiral at J=18
    eq_10 = find_chiral_equilibrium_and_barrier(J_tot=10.0, J_m=25.0, J_s=15.0, J_l=5.0)
    assert eq_10["is_chiral_geometry"] is False, "J=10 must be planar (no chirality)"
    assert eq_10["phi_min_deg"] < 5.0

    eq_18 = find_chiral_equilibrium_and_barrier(J_tot=18.0, J_m=25.0, J_s=15.0, J_l=5.0)
    assert eq_18["is_chiral_geometry"] is True, "J=18 must be aplanar chiral"
    assert eq_18["chiral_barrier_keV"] > 50.0, "Substantial chiral planar barrier at J=18"
    assert eq_18["aplanarity_volume_metric"] > 0.4
    print("  ✓ tac_3d_chiral_orientation_energy_surface_calculator passed.")


def test_level_scheme_loop_balancer():
    print("Testing level_scheme_loop_residual_intensity_balancer...")
    # 1. Consistent Ritz loop
    l_fwd = [("2_g+ -> 2+", 556.0, 0.2), ("2+ -> 0+", 409.2, 0.2)]
    l_bwd = [("2_g+ -> 0+", 965.2, 0.3)]
    lp = evaluate_ritz_combination_loop("Loop 1", l_fwd, l_bwd)
    assert lp["delta_E_residual_keV"] == 0.0, "Ritz loop consistency"
    assert lp["normalized_z_score"] < 0.1

    # 2. Side-feeding extraction
    levels = [{"level_id": "4+", "energy_keV": 1048.9}]
    trans = [{"from": "6+", "to": "4+", "I_gamma": 40.0}, {"from": "4+", "to": "2+", "I_gamma": 80.0}]
    bal = calculate_level_intensity_balance(levels, trans)
    assert bal[0]["extracted_side_feeding_I_side"] == 40.0, "Extracted side-feeding 40.0 units"
    assert bal[0]["side_feeding_fraction_pct"] == 50.0
    print("  ✓ level_scheme_loop_residual_intensity_balancer passed.")


def test_heavy_ion_optical_rainbow():
    print("Testing heavy_ion_optical_rainbow_scattering_analyzer...")
    kin = calculate_kinematics_and_sommerfeld(16, 8, 16, 8, 350.0)
    assert kin["E_cm_MeV"] == 175.0
    res = find_rainbow_singularity_and_airy_minima(kin["sommerfeld_eta"], kin["k_fm_minus1"], 25.0, 70.0, 12.0)
    assert res["observed_rainbow_angle_deg"] > 50.0
    print("  ✓ heavy_ion_optical_rainbow_scattering_analyzer passed.")


def test_time_spectrum_convolution():
    print("Testing in_beam_time_spectrum_convolution_fitter...")
    y = convoluted_decay_model(np.array([0.0, 1.0, 2.0]), 1000.0, 1.0, 0.5, 0.2, 5.0)
    assert len(y) == 3
    assert y[1] > y[0]
    print("  ✓ in_beam_time_spectrum_convolution_fitter passed.")


def test_two_quasiparticle_wobbling():
    print("Testing two_quasiparticle_even_even_wobbling_analyzer...")
    yrast = [{"I": 10, "energy_keV": 3280.0}, {"I": 12, "energy_keV": 3950.0}, {"I": 14, "energy_keV": 4720.0}]
    wob = [{"I": 11, "energy_keV": 4120.0, "be2_out_in_ratio": 0.48}]
    res = calculate_two_quasiparticle_wobbling_energies(yrast, wob)
    assert len(res) == 1
    assert abs(res[0]["E_wob_keV"] - 505.0) < 1.0
    print("  ✓ two_quasiparticle_even_even_wobbling_analyzer passed.")


def test_hpge_efficiency_covariance():
    print("Testing hpge_efficiency_curve_covariance_fitter...")
    pts = [
        {"E_keV": 121.8, "efficiency": 0.0245, "sigma_eff": 0.00045},
        {"E_keV": 344.3, "efficiency": 0.0135, "sigma_eff": 0.00025},
        {"E_keV": 778.9, "efficiency": 0.0068, "sigma_eff": 0.00015},
        {"E_keV": 1408.0, "efficiency": 0.0040, "sigma_eff": 0.00010}
    ]
    fit_res = fit_efficiency_curve_wls(pts, poly_order=2)
    eval_pt = evaluate_efficiency_with_covariance(344.3, fit_res)
    assert abs(eval_pt["efficiency"] - 0.0135) < 0.001
    assert eval_pt["covariance_overestimate_ratio"] > 1.2
    print("  ✓ hpge_efficiency_curve_covariance_fitter passed.")


def test_gated_multiplet_deconvolution():
    print("Testing in_beam_gated_matrix_multiplet_deconvolution_fitter...")
    E = [638.0, 640.0, 642.0]
    y = multiplet_model_function(E, 1000.0, 638.0, 800.0, 641.0, 0.9, 10.0, 0.0)
    assert len(y) == 3
    assert y[0] > 100.0
    print("  ✓ in_beam_gated_matrix_multiplet_deconvolution_fitter passed.")


def test_tsd_wobbling_decayout():
    print("Testing triaxial_superdeformed_wobbling_decayout_analyzer...")
    trans = [{"I": 39.5, "E_in_keV": 890.0, "E_wob_keV": 720.0, "Delta_E_ND_MeV": 1.10, "B_E2_in_W_u": 620.0, "B_E2_wob_W_u": 125.0}]
    barr = {"V_B_MeV": 1.85, "hbar_omega_barr_MeV": 0.42, "D_TSD_keV": 45.0}
    res = calculate_transition_widths_and_tunneling(trans, barr)
    assert len(res) == 1
    assert res[0]["branching_in"] > 0.50
    print("  ✓ triaxial_superdeformed_wobbling_decayout_analyzer passed.")


def test_mcintyre_s_matrix():
    print("Testing heavy_ion_mcintyre_s_matrix_reaction_cross_section_analyzer...")
    kin = calc_mcintyre_kin(16, 8, 208, 82, 129.5)
    xs = calc_mcintyre_xs(kin, 55.4, 3.25, 0.45, 90)
    assert xs["sigma_reaction_mb"] > 1000.0
    print("  ✓ heavy_ion_mcintyre_s_matrix_reaction_cross_section_analyzer passed.")


def test_3d_tac_pitchfork_bifurcation():
    print("Testing three_dimensional_tac_chiral_pitchfork_bifurcation_inverter...")
    pt = calculate_pitchfork_bifurcation(16.0, 5.5, 5.5, 30.0, 12.0, 6.0)
    assert pt["is_chiral_phase"]
    assert pt["chiral_barrier_keV"] > 100.0
    print("  ✓ three_dimensional_tac_chiral_pitchfork_bifurcation_inverter passed.")


def test_fold_multiplicity_unfolding():
    print("Testing in_beam_array_fold_multiplicity_entry_state_unfolder...")
    resp = calculate_binomial_response_matrix(16, 0.80, 16, 20)
    assert resp.shape == (17, 21)
    info = map_to_entry_spin_and_energy(20.0, 3.0, 20.0, 4.0, 0.5)
    assert abs(info["mean_entry_spin_hbar"] - 34.0) < 1e-3
    print("  ✓ in_beam_array_fold_multiplicity_entry_state_unfolder passed.")


def test_chiral_selection_rules():
    print("Testing chiral_doublet_selection_rules_m1_staggering_arbitrator...")
    b1 = [{"I": 12, "B_M1_muN2": 0.8, "B_E2_e2b2": 0.4}, {"I": 13, "B_M1_muN2": 1.4, "B_E2_e2b2": 0.4}, {"I": 14, "B_M1_muN2": 0.7, "B_E2_e2b2": 0.4}]
    b2 = [{"I": 12, "B_M1_muN2": 0.7, "B_E2_e2b2": 0.4}, {"I": 13, "B_M1_muN2": 1.3, "B_E2_e2b2": 0.4}, {"I": 14, "B_M1_muN2": 0.6, "B_E2_e2b2": 0.4}]
    res = arbitrate_chiral_selection_rules(b1, b2, [{"I": 13, "B_M1_inter_muN2": 0.05}])
    assert res["phase_match_fraction"] == 1.0
    print("  ✓ chiral_doublet_selection_rules_m1_staggering_arbitrator passed.")


def test_prompt_delayed_time_gating():
    print("Testing in_beam_prompt_delayed_time_gating_random_subtractor...")
    p_win = {"t_start": -4.0, "t_stop": 8.0}
    r_win = {"t_start": 25.0, "t_stop": 75.0}
    peaks = [{"energy_keV": 409.0, "prompt_counts": 14200, "random_counts": 6400}]
    res = perform_random_subtraction(peaks, p_win, r_win)
    assert abs(res["subtracted_peaks"][0]["net_true_counts"] - 12664.0) < 1.0
    print("  ✓ in_beam_prompt_delayed_time_gating_random_subtractor passed.")


def test_hexadecapole_wobbling():
    print("Testing triaxial_hexadecapole_deformation_wobbling_modifier...")
    moi = calculate_hexadecapole_modified_moi(0.25, 22.0, 0.0, 30.0)
    wob = calculate_wobbling_frequency_with_beta4(moi, 19.5, 5.5)
    assert abs(wob["delta_wobbling_freq_keV"]) < 1e-4
    print("  ✓ triaxial_hexadecapole_deformation_wobbling_modifier passed.")


def test_chiral_quartic_schrodinger():
    print("Testing chiral_vibrational_quartic_schrodinger_diagonalizer...")
    res = diagonalize_chiral_schrodinger(-3.5, 18.0, 12.0)
    assert res["chiral_splitting_keV"] > 100.0
    print("  ✓ chiral_vibrational_quartic_schrodinger_diagonalizer passed.")


def test_hpge_solid_angle_qk():
    print("Testing hpge_detector_solid_angle_attenuation_qk_integrator...")
    res = calculate_solid_angle_attenuation_qk(3.5, 7.0, 15.0, 1332.5)
    assert res["Q2_attenuation_factor"] > 0.95
    assert res["Q4_attenuation_factor"] > 0.85
    print("  ✓ hpge_detector_solid_angle_attenuation_qk_integrator passed.")


def test_pulser_live_time():
    print("Testing in_beam_pulser_injection_live_time_corrector...")
    lt = calculate_pulser_live_time(100.0, 50.0, 4000)
    assert abs(lt["live_time_fraction"] - 0.80) < 1e-4
    corr = correct_peaks([{"energy_keV": 500.0, "measured_area": 800.0, "sigma_area": 10.0}], lt)
    assert abs(corr[0]["true_area"] - 1000.0) < 1.0
    print("  ✓ in_beam_pulser_injection_live_time_corrector passed.")


def test_tsd_pes_strutinsky():
    print("Testing triaxial_superdeformed_pes_strutinsky_engine...")
    b_arr = np.array([0.1, 0.2, 0.4])
    g_arr = np.array([10.0, 20.0])
    E_ldm = calculate_ldm_energy_surface(71, 163, b_arr, g_arr)
    assert E_ldm.shape == (3, 2)
    assert E_ldm[2, 0] > E_ldm[0, 0]
    print("  ✓ triaxial_superdeformed_pes_strutinsky_engine passed.")


def test_coriolis_anti_pairing():
    print("Testing coriolis_anti_pairing_gap_quenching_moi_engine...")
    gap = calculate_cap_pairing_gap(0.0, 1.0, 0.5)
    assert gap["delta_MeV"] == 1.0
    pt = solve_spin_state_cap(35.0, 0.95, 0.45, {"J_s": 45.0, "J_m": 72.0, "J_l": 20.0}, 0.4)
    assert pt["pairing_gap_MeV"] < 0.1
    print("  ✓ coriolis_anti_pairing_gap_quenching_moi_engine passed.")


def test_array_coincidence_efficiency():
    print("Testing in_beam_array_coincidence_efficiency_angular_matrix_inverter...")
    d1 = {"theta_deg": 90.0, "phi_deg": 0.0}
    d2 = {"theta_deg": 90.0, "phi_deg": 180.0}
    _, cos_th = calculate_mutual_pair_angle(d1, d2)
    assert abs(cos_th - (-1.0)) < 1e-4
    w = evaluate_directional_correlation_weight(cos_th, 0.0, 0.0, 1.0, 1.0)
    assert abs(w - 1.0) < 1e-4
    print("  ✓ in_beam_array_coincidence_efficiency_angular_matrix_inverter passed.")


def test_tpsm_3d_projection():
    print("Testing tpsm_3d_angular_momentum_projection_diagonalizer...")
    moi = calculate_effective_moi_tpsm(0.23, 25.0, 130)
    assert moi > 20.0
    res = diagonalize_spin_tpsm(4, [0, 2, 4], moi, 25.0, 42.0)
    assert res["E_gamma_band_keV"] > res["E_yrast_keV"]
    print("  ✓ tpsm_3d_angular_momentum_projection_diagonalizer passed.")


def test_rdds_ddcm_lifetime():
    print("Testing in_beam_rdds_ddcm_lifetime_inverter...")
    meas = [{"d_um": 25.0, "stopped_counts": 4350.0, "shifted_counts": 16100.0}, {"d_um": 50.0, "stopped_counts": 7900.0, "shifted_counts": 12400.0}]
    pts, v = evaluate_ddcm_curve(meas, 0.0210)
    assert len(pts) == 2
    assert v > 6.0
    print("  ✓ in_beam_rdds_ddcm_lifetime_inverter passed.")


def test_davydov_rostovsky_mixing():
    print("Testing davydov_rostovsky_triaxial_band_mixing_solver...")
    z = invert_gamma_mixing_parameter(0.700)
    assert abs(z) < 1e-4
    res = calculate_davydov_rostovsky_parameters(121.8, 1085.9, 684.7, 0.540)
    assert res["z_gamma_mixing_parameter"] > 0.03
    print("  ✓ davydov_rostovsky_triaxial_band_mixing_solver passed.")


def test_2d_snip_background():
    print("Testing in_beam_2d_snip_matrix_background_estimator...")
    peaks = [{"E1_keV": 500.0, "E2_keV": 500.0, "amplitude": 1000.0, "sigma_keV": 2.0}]
    _, M_raw, _, _, _ = generate_synthetic_2d_matrix(30, 450.0, 550.0, peaks, 50.0)
    B_snip, S_net, stats = execute_2d_snip_algorithm(M_raw, p_max=3)
    assert stats["background_fraction_pct"] > 30.0
    print("  ✓ in_beam_2d_snip_matrix_background_estimator passed.")


def test_odd_odd_recoil_chiral():
    print("Testing odd_odd_3d_tac_recoil_chiral_orientator...")
    pt = find_optimal_orientation(16.0, 5.5, 5.5, 30.0, 12.0, 6.0, 0.15)
    assert pt["is_chiral_phase"]
    assert pt["chiral_barrier_keV"] > 300.0
    print("  ✓ odd_odd_3d_tac_recoil_chiral_orientator passed.")


def test_odd_odd_chiral_mep():
    print("Testing odd_odd_chiral_mep_instanton_tunneling_solver...")
    solver = OddOddChiralMEPInstantonSolver(spin=17.0, j_p=5.5, j_n=5.5, gamma_deg=30.0,
                                            moi_s=15.0, moi_i=38.0, moi_l=12.0)
    res = solver.solve_instanton_action(n_nodes=15)
    assert res["minima_info"]["is_chiral_broken"]
    assert res["barrier_height_MeV"] > 0.2
    assert res["instanton_action_hbar"] > 2.0
    print("  ✓ odd_odd_chiral_mep_instanton_tunneling_solver passed.")


def test_hpge_tfa_crossover_walk():
    print("Testing in_beam_hpge_tfa_crossover_walk_jitter_optimizer...")
    opt = HPGeTFACrossoverOptimizer(t_rise_mean_ns=180.0, t_rise_sigma_ns=40.0)
    res = opt.optimize_shaping_constants(511.0)
    assert res["optimal"]["total_fwhm_ns"] < res["wu_zhihua_comparison"]["total_fwhm_ns"]
    assert res["optimization_improvement_pct"] > 0.0
    print("  ✓ in_beam_hpge_tfa_crossover_walk_jitter_optimizer passed.")


def test_triaxial_fusion_barrier():
    print("Testing heavy_ion_triaxial_fusion_barrier_distribution_inverter...")
    inv = TriaxialFusionBarrierInverter(V_B0_MeV=72.5, beta2=0.23, gamma_deg=22.0)
    res = inv.evaluate_barrier_distribution(np.linspace(66.0, 80.0, 15))
    cb = res["characteristic_barriers"]
    assert cb["triaxial_belly_splitting_MeV"] > 3.0
    assert res["is_triaxial_fingerprint"]
    print("  ✓ heavy_ion_triaxial_fusion_barrier_distribution_inverter passed.")


def test_odd_a_wobbling_stability():
    print("Testing odd_a_transverse_longitudinal_wobbling_stability_solver...")
    solver = OddAWobblingStabilitySolver(wobbling_mode="TW", inertia_model="rigid", j_qp=5.5, gamma_deg=22.0)
    res = solver.evaluate_spin_series([8.5, 10.5, 12.5])
    assert res["frequency_slope_dOmega_dI"] < 0.0
    assert res["mode_confirmed"]
    print("  ✓ odd_a_transverse_longitudinal_wobbling_stability_solver passed.")


def test_dsam_zbl_stopping():
    print("Testing in_beam_dsam_zbl_stopping_lifetime_inverter...")
    inv = InBeamDSAMZBLInverter(Ar=130, Zr=56, As=197, Zs=79)
    res = inv.invert_lifetime(0.62, 0.04, 0.05)
    assert 0.3 < res["tau_level_ps"] < 0.7
    props = inv.calculate_transition_properties(res["tau_level_ps"], 712.5, 8.0)
    assert props["B_E2_e2b2"] > 0.5
    print("  ✓ in_beam_dsam_zbl_stopping_lifetime_inverter passed.")


def test_cranked_shape_coexistence_pes():
    print("Testing cranked_triaxial_shape_coexistence_pes_engine...")
    shell = [
        {"name": "Triaxial-Min", "beta": 0.24, "gamma_deg": 24.0, "depth_MeV": -2.6, "w_beta": 0.08, "w_gamma_deg": 12.0},
        {"name": "Oblate-Min",   "beta": 0.17, "gamma_deg": 58.0, "depth_MeV": -2.8, "w_beta": 0.07, "w_gamma_deg": 10.0}
    ]
    engine = CrankedShapeCoexistencePESEngine(C2=15.0, C3=-8.0, C4=25.0, J0=34.0, beta0=0.20, shell_minima=shell)
    res = engine.evaluate_frequency_evolution([0.0, 0.15, 0.25, 0.35])
    assert res["has_shape_transition"]
    assert 0.15 < res["critical_crossing_frequency_omega_cross_MeV"] < 0.35
    print("  ✓ cranked_triaxial_shape_coexistence_pes_engine passed.")


def test_spin_alignment_mixing():
    print("Testing in_beam_spin_alignment_sigma_mixing_ratio_extractor...")
    ext = SpinAlignmentMixingExtractor(I_ref_i=4.0, I_ref_f=2.0, a2_ref=0.285, sigma_a2_ref=0.015,
                                       a4_ref=-0.075, sigma_a4_ref=0.020)
    cal = ext.extract_sigma_over_I()
    assert 0.3 < cal["sigma_over_I"] < 0.6
    res = ext.invert_mixing_ratio(9.0, 8.0, 0.420, 0.025, -0.010, 0.030)
    assert res["min_chi2"] < 10.0
    assert abs(res["best_fit_delta"]) > 0.5
    print("  ✓ in_beam_spin_alignment_sigma_mixing_ratio_extractor passed.")


def test_multiple_chiral_doublets_mchid():
    print("Testing multiple_chiral_doublets_mchid_discriminator...")
    p = MCHID_PRESETS["133Ce_classic_mchid"]
    discrim = MultipleChiralDoubletsDiscriminator(harris_J0=p["harris_J0"], harris_J1=p["harris_J1"])
    res = discrim.arbitrate_mchid(p["pair_A"], p["pair_B"], p["cross_doublet_branching_ratio"])
    assert res["is_mchid_confirmed"]
    assert res["alignment_separation_Delta_ix_hbar"] > 2.0
    print("  ✓ multiple_chiral_doublets_mchid_discriminator passed.")


def test_charged_particle_pid():
    print("Testing in_beam_charged_particle_pid_delta_e_telescope_inverter...")
    inv = ChargedParticlePIDInverter(thickness_T0_um=65.0, angle_incidence_deg=45.0)
    pi_p = inv.calculate_pid_value(1.20, 14.5)
    pi_a = inv.calculate_pid_value(8.50, 18.2)
    assert pi_a > 5.0 * pi_p
    fom = inv.evaluate_separation_fom(proton_ref_pi=pi_p)
    assert fom["1H (Proton) vs 4He (Alpha)"]["FOM"] > 3.0
    print("  ✓ in_beam_charged_particle_pid_delta_e_telescope_inverter passed.")


def test_triaxial_scissors_mode():
    print("Testing triaxial_two_rotor_scissors_mode_m1_solver...")
    solver = TriaxialScissorsModeM1Solver(A=134, Z=56, beta2=0.22, gamma_deg=24.0)
    res = solver.solve_scissors_modes()
    assert res["is_scissors_doublet_split"]
    assert res["scissors_splitting_MeV"] > 0.5
    assert res["total_B_M1_muN2"] > 0.8
    print("  ✓ triaxial_two_rotor_scissors_mode_m1_solver passed.")


def test_hpge_energy_non_linearity():
    print("Testing hpge_energy_non_linearity_inl_dnl_calibrator...")
    from scipy.interpolate import UnivariateSpline
    chs = [200.0, 1000.0, 2000.0, 4000.0]
    es = [60.0, 320.0, 640.0, 1280.0]
    sigs = [0.01, 0.01, 0.01, 0.01]
    fit = fit_energy_polynomial(chs, es, sigs, degree=2, ch_center=2000.0)
    spline = UnivariateSpline(chs, fit["residuals_keV"], k=2, s=0.0)
    eval_pt = evaluate_calibrated_energy(1000.0, fit, spline)
    assert abs(eval_pt["final_calibrated_energy_keV"] - 320.0) < 0.05
    print("  ✓ hpge_energy_non_linearity_inl_dnl_calibrator passed.")


def test_tcs_coincidence_summing():
    print("Testing in_beam_true_coincidence_summing_tcs_calculator...")
    eps_t = calculate_total_efficiency(0.025, 0.25)
    assert abs(eps_t - 0.10) < 1e-4
    pairs = [{"E_target_keV": 1000.0, "E_coincident_keV": 500.0, "branching": 1.0}]
    res = calculate_tcs_corrections(pairs, {1000.0: 0.03, 500.0: 0.04}, {1000.0: 0.25, 500.0: 0.20})
    assert res["summing_out_corrections"][0]["correction_factor_C_out"] > 1.20
    print("  ✓ in_beam_true_coincidence_summing_tcs_calculator passed.")


def test_chiral_octupole_quartet():
    print("Testing chiral_octupole_quartet_bands_analyzer...")
    spins = [8.0, 9.0, 10.0, 11.0, 12.0]
    p1 = [1850.0, 2260.0, 2730.0, 3260.0, 3850.0]
    p2 = [1920.0, 2330.0, 2795.0, 3320.0, 3905.0]
    n1 = [2050.0, 2440.0, 2890.0, 3400.0, 3970.0]
    n2 = [2115.0, 2500.0, 2945.0, 3450.0, 4015.0]
    res = evaluate_quartet_properties(spins, p1, p2, n1, n2)
    assert res["is_chiral_octupole_confirmed"] is True
    print("  ✓ chiral_octupole_quartet_bands_analyzer passed.")


def test_fast_timing_gcd():
    print("Testing in_beam_fast_timing_gcd_lifetime_calculator...")
    w_feed = calculate_prf_walk(600.0)
    w_decay = calculate_prf_walk(400.0)
    delta_w = w_feed - w_decay
    res = calculate_gcd_lifetime(C1_ps=delta_w + 50.0, C2_ps=-delta_w - 50.0,
                                 sigma_C1_ps=1.0, sigma_C2_ps=1.0,
                                 E_feed_keV=600.0, E_decay_keV=400.0)
    assert abs(res["tau_extracted_ps"] - 50.0) < 1e-2
    print("  ✓ in_beam_fast_timing_gcd_lifetime_calculator passed.")


def test_chiral_gfactor_equality():
    print("Testing chiral_doublet_g_factor_equality_calculator...")
    theo = calculate_theoretical_chiral_gfactor(128, 55, 11.0, 5.5, 5.5)
    assert theo["g_chiral_theoretical"] > 0.40
    arb = arbitrate_chiral_gfactor_equality(0.58, 0.04, 0.56, 0.05)
    assert arb["status"] == "chiral_equality_confirmed"
    print("  ✓ chiral_doublet_g_factor_equality_calculator passed.")


def test_ptrm_diagonalizer():
    print("Testing particle_triaxial_rotor_model_ptrm_diagonalizer...")
    H, basis = evaluate_ptrm_matrix_elements(7.5, 5.5, 15.0, 26.0, 6.0, 35.0, 26.0)
    assert H.shape[0] > 0
    traj = diagonalize_ptrm_spectrum([7.5, 8.5], 5.5, 15.0, 26.0, 6.0, 35.0, 26.0)
    assert len(traj) == 2
    print("  ✓ particle_triaxial_rotor_model_ptrm_diagonalizer passed.")


def test_mwd_baseline_restorer():
    print("Testing digital_mwd_baseline_restorer_filter...")
    res = run_mwd_blr_analysis(10.0, 50.0, 30.0, 2.0, 0.8, [3.0, 5.5], [1000.0, 1000.0])
    assert res["resolution_summary"]["resolution_improvement_factor"] > 10.0
    print("  ✓ digital_mwd_baseline_restorer_filter passed.")


def test_coriolis_band_mixing():
    print("Testing coriolis_band_mixing_matrix_diagonalizer...")
    H, basis = construct_coriolis_matrix(2.5, [0.5, 1.5, 2.5], [0.0, 150.0, 380.0], 13.0, 5.5, a_decouple=-3.5)
    assert H.shape == (3, 3)
    levels = diagonalize_coriolis_mixing([1.5, 2.5, 3.5], [0.5, 1.5, 2.5], [0.0, 150.0, 380.0], 13.0, 5.5)
    assert len(levels) == 3
    print("  ✓ coriolis_band_mixing_matrix_diagonalizer passed.")


def test_spontaneous_fission_action():
    print("Testing spontaneous_fission_wkb_action_calculator...")
    P, arg = calculate_sf_hill_wheeler_transmission(6.0, 1.0, 1.0)
    assert P < 1e-10
    res = calculate_double_hump_sf_half_life(6.3, 1.0, 5.65, 0.51, 0.80)
    assert res["log10_T_half_years"] > 10.0
    print("  ✓ spontaneous_fission_wkb_action_calculator passed.")


def test_cascade_deorientation_uk():
    print("Testing cascade_deorientation_coefficient_uk_calculator...")
    u0 = calculate_single_step_uk(6.0, 4.0, 2.0, k=0)
    assert u0 == 1.0
    u2 = calculate_single_step_uk(6.0, 4.0, 2.0, k=2)
    assert abs(u2 - 0.9000) < 1e-3
    print("  ✓ cascade_deorientation_coefficient_uk_calculator passed.")


def test_mwpc_drift_chamber():
    print("Testing mwpc_drift_chamber_field_avalanche_simulator...")
    fld = calculate_electrostatic_field(2.0, 5.0, 10.0, 2600.0)
    assert fld["E_surface_V_cm"] > 1e5
    res = run_mwpc_simulation(2.0, 5.0, 10.0, 2600.0)
    assert res["avalanche_gain"]["gas_gain_M"] > 1e3
    print("  ✓ mwpc_drift_chamber_field_avalanche_simulator passed.")


def test_digital_psd_optimizer():
    print("Testing digital_psd_charge_comparison_optimizer...")
    opt = optimize_gate_widths(1.5, 3.2, 270.0, 0.12, 0.32)
    assert opt["max_delta_PSD"] > 0.03
    fom = evaluate_fom_energy_dependence(500.0, 1.45, [200.0, 500.0])
    assert fom[1]["FOM"] == 1.45
    print("  ✓ digital_psd_charge_comparison_optimizer passed.")


def test_tac_pairing_chiral():
    print("Testing tac_pairing_self_consistent_chiral_engine...")
    pair = calculate_self_consistent_pairing_gap(134, 4.0, 30.0)
    assert pair["Delta_J_MeV"] > 0.0
    chiral = find_tac_pairing_chiral_barrier(18.0, 5.5, 5.5, 15.0, 25.0, 6.0)
    assert chiral["barrier_keV"] > 10.0
    print("  ✓ tac_pairing_self_consistent_chiral_engine passed.")


def test_heavy_ion_dic_wilczynski():
    print("Testing heavy_ion_dic_wilczynski_energy_loss_calculator...")
    kin = calculate_dic_kinematics(Ap=86, Zp=36, At=166, Zt=68, Elab_MeV=703.0)
    assert kin["L_grazing_hbar"] > 300.0
    res = run_dic_analysis(86, 36, 166, 68, 703.0)
    assert res["max_spin_transfer_hbar"] > 50.0
    print("  ✓ heavy_ion_dic_wilczynski_energy_loss_calculator passed.")


def test_octupole_collective_ewsr():
    print("Testing octupole_collective_ewsr_parity_doublet_analyzer...")
    ewsr = calculate_octupole_ewsr(208, 82, 2614.5, 34.0)
    assert ewsr["EWSR_exhaustion_percent"] > 5.0
    pos_s = [0.0, 2.0, 4.0, 6.0]
    pos_e = [0.0, 84.4, 254.0, 479.0]
    neg_s = [1.0, 3.0, 5.0]
    neg_e = [216.0, 290.0, 433.0]
    ps = calculate_parity_splitting_ewsr(pos_s, pos_e, neg_s, neg_e)
    assert len(ps["splittings"]) == 3
    print("  ✓ octupole_collective_ewsr_parity_doublet_analyzer passed.")


def test_double_root_arbitrator():
    print("Testing double_root_dco_polarization_statistical_arbitrator...")
    A = [1.0, 0.45, 0.90]
    B = [1.4, -0.70, 1.80]
    sol = solve_dco_quadratic(A, B, 0.45)
    assert sol["status"] == "two_real_roots"
    assert len(sol["roots"]) == 2
    res = analyze_double_roots(
        A_coeffs=A, B_coeffs=B, R_exp=0.45, sigma_R=0.04,
        P_coeffs=[-0.15, 0.10, 0.55], Q_coeffs=[1.0, 0.45, 0.90],
        P_exp=0.22, sigma_P=0.05
    )
    assert res["arbitration"]["status"] == "resolved_by_3sigma_statistical_exclusion"
    print("  ✓ double_root_dco_polarization_statistical_arbitrator passed.")


def test_multi_quasiparticle_mchid():
    print("Testing multi_quasiparticle_mchid_chirality_calculator...")
    geom = evaluate_chiral_geometry(j_pi=8.0, j_nu=8.0, total_spin=18.0)
    assert geom["aplanarity_volume_metric"] > 0.50
    doublets = [{
        "doublet_id": "Doublet_1", "configuration": "pi h11/2^2 (x) nu h11/2^-2",
        "parity": "+", "j_pi": 8.0, "j_nu": 8.0,
        "spins": [15, 16, 17, 18, 19, 20],
        "E_band1_keV": [5180.0, 5680.0, 6220.0, 6800.0, 7420.0, 8080.0],
        "E_band2_keV": [5260.0, 5740.0, 6270.0, 6840.0, 7450.0, 8105.0]
    }, {
        "doublet_id": "Doublet_2", "configuration": "pi h11/2^2 (x) nu [h11/2^-1 d5/2^-1]",
        "parity": "-", "j_pi": 8.0, "j_nu": 5.5,
        "spins": [15, 16, 17, 18, 19, 20],
        "E_band1_keV": [5350.0, 5840.0, 6370.0, 6940.0, 7550.0, 8200.0],
        "E_band2_keV": [5440.0, 5910.0, 6420.0, 6980.0, 7580.0, 8225.0]
    }]
    res = analyze_mchid(doublets, nucleus_name="136Nd")
    assert res["is_mchid_verified"] is True
    print("  ✓ multi_quasiparticle_mchid_chirality_calculator passed.")


def test_davydov_chaban_stretching_calculator():
    print("Testing davydov_chaban_beta_stretching_triaxial_calculator...")
    # 112Ru triaxial Chaban benchmark
    res = calculate_davydov_chaban_spectrum(E_2plus_keV=237.2, gamma_deg=22.0, mu_nonadiabatic=0.28)
    assert len(res["levels"]) == 5
    # Check 2_1+ energy equals input
    assert abs(res["levels"][0]["energy_keV"] - 237.2) < 0.2
    # Verify dynamic beta-stretching p > 1.0
    for lv in res["levels"]:
        assert lv["stretching_factor_p"] >= 1.0, "Beta stretching p >= 1.0"
    print("  ✓ davydov_chaban_beta_stretching_triaxial_calculator passed.")


def test_gamma_band_mixing_z_gamma_calculator():
    print("Testing gamma_band_mixing_z_gamma_alaga_inverter...")
    # 168Er gamma band benchmark: R_exp = 0.540 -> z_gamma ~ 0.0203
    res_168 = invert_z_gamma_from_branching(R_exp_B_E2=0.540, E_2gamma_keV=821.1, E_2g_keV=79.8)
    assert abs(res_168["inverted_z_gamma"] - 0.02028) < 0.001, "168Er z_gamma ~ 0.0203"
    assert abs(res_168["rotational_vibrational_h2_keV"] - 6.14) < 0.2, "168Er h2 ~ 6.14 keV"
    assert res_168["structural_classification"].startswith("Well-Deformed")

    # 130Ba gamma-soft benchmark: R_exp = 0.320 -> large z_gamma > 0.05
    res_130 = invert_z_gamma_from_branching(R_exp_B_E2=0.320, E_2gamma_keV=908.1, E_2g_keV=357.4)
    assert res_130["inverted_z_gamma"] > 0.05, "130Ba gamma-soft z_gamma > 0.05"
    print("  ✓ gamma_band_mixing_z_gamma_alaga_inverter passed.")


def test_schiffer_true_two_body_matrix_elements_calculator():
    print("Testing schiffer_true_two_body_matrix_elements_calculator...")
    # 1. Particle-particle h11/2^2 pairing gap at J=0
    pp = calculate_schiffer_true_pp_spectrum(5.5, 5.5)
    assert pp["ground_state_spin_J"] == 0, "p-p ground state must be J=0+"
    assert pp["spectrum"][0]["angle_theta_12_deg"] == 180.0
    assert pp["spectrum"][0]["V_pp_MeV"] < -3.0

    # 2. Particle-hole Pandya inversion (134Pr chiral configuration)
    ph = calculate_schiffer_true_ph_pandya_spectrum(5.5, 5.5)
    assert len(ph["spectrum"]) == 12, "12 states in h11/2 (x) h11/2^-1 multiplet"

    # 3. Nordheim coupling rule
    nord = evaluate_nordheim_coupling_rule(j_p=5.5, l_p=5, j_n=5.5, l_n=5)
    assert nord["nordheim_number_N"] == 1
    assert nord["predicted_favored_spin_J"] == 11
    print("  ✓ schiffer_true_two_body_matrix_elements_calculator passed.")


def test_triaxial_cranking_routhian_calculator():
    print("Testing triaxial_cranking_single_j_routhian_diagram_calculator...")
    # h11/2 triaxial chiral intruder benchmark (gamma = -30 deg)
    diag = diagonalize_triaxial_cranked_high_j(j_orbital=5.5, gamma_deg=-30.0, omega_MeV=0.20, kappa_MeV=3.0)
    assert len(diag["levels"]) == 12, "12 single-particle Routhians for j=11/2"
    # Aligned state at bottom of well
    lowest_lv = diag["levels"][0]
    assert abs(lowest_lv["alignment_jx_hbar"] - 5.47) < 0.1, "Strong alignment along rotation axis"
    assert diag["is_signature_inverted"] is True, "Signature inversion in triaxial high-j shell"
    print("  ✓ triaxial_cranking_single_j_routhian_diagram_calculator passed.")


def test_optical_model_potential_reaction_calculator():
    print("Testing optical_model_potential_reaction_cross_section_calculator...")
    # 40 MeV p + 58Ni reaction cross section benchmark (~ 1090 mb)
    omp = calculate_optical_model_reaction_cross_section(
        Z_p=1, A_p=1, Z_t=28, A_t=58, E_lab_MeV=40.0,
        V0_MeV=45.0, W0_volume_MeV=10.0, Ws_surface_MeV=3.0
    )
    assert abs(omp["total_reaction_cross_section_sigma_R_mb"] - 1094.0) < 20.0, "40 MeV p+58Ni reaction cross section"
    assert omp["nuclear_opacity_ratio"] > 1.0, "Nuclear opacity ratio > 1.0"
    print("  ✓ optical_model_potential_reaction_cross_section_calculator passed.")


def test_grodzins_deformation_inverter():
    print("Testing grodzins_deformation_beta2_quadrupole_inverter...")
    # 154Sm rotor benchmark
    sm = invert_beta2_and_quadrupole(Z=62, A=154, B_E2_e2_b2=4.35, E_2plus_keV=82.0)
    assert abs(sm["quadrupole_deformation_beta2"] - 0.341) < 0.005, "154Sm beta2 ~ 0.341"
    assert abs(sm["grodzins_ratio"] - 1.037) < 0.01, "154Sm Grodzins ratio ~ 1.0"
    assert abs(sm["superfluid_pairing_reduction_ratio"] - 0.543) < 0.01, "Pairing reduction ~ 0.54"

    # 132Sn spherical benchmark
    sn = invert_beta2_and_quadrupole(Z=50, A=132, B_E2_e2_b2=0.011, E_2plus_keV=4041.0)
    assert sn["quadrupole_deformation_beta2"] < 0.05, "132Sn near-spherical beta2 < 0.05"
    print("  ✓ grodzins_deformation_beta2_quadrupole_inverter passed.")


def test_seniority_scheme_half_filled_isomer_calculator():
    print("Testing seniority_scheme_half_filled_isomer_calculator...")
    # 1. Exact B(E2) cancellation at half-filled shell n = j + 1/2
    # For h11/2: j = 5.5, shell capacity = 12, n_half = 6
    frac_half = calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=6, v_seniority=2)
    assert frac_half["fractional_parentage_factor"] == 0.0, "Seniority parentage factor zero at n=6"
    assert frac_half["b_e2_scaling_factor"] == 0.0, "B(E2) scaling exactly 0 at half-filled shell"
    assert frac_half["is_seniority_cancellation"] is True

    # 2. Seniority isomer lifetime cancellation
    iso = evaluate_seniority_isomer_properties(j_orbital=5.5, n_particles=6, E_gamma_keV=100.0)
    assert math.isinf(iso["T12_actual_sec"]), "Infinite T1/2 in pure single-j half-filled shell"

    # 3. Particle-hole symmetry: n=2 and n=10 have identical B(E2) scaling
    frac_2 = calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=2, v_seniority=2)
    frac_10 = calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=10, v_seniority=2)
    assert abs(frac_2["b_e2_scaling_factor"] - frac_10["b_e2_scaling_factor"]) < 1e-6, "Particle-hole symmetry in B(E2)"
    print("  ✓ seniority_scheme_half_filled_isomer_calculator passed.")


def test_dsam_doppler_attenuation_lifetime_calculator():
    print("Testing dsam_doppler_attenuation_lss_blaugrund_lifetime_calculator...")
    # Invert 134Ce in Au: F_exp = 0.52 -> tau ~ 0.75 ps
    inv = invert_lifetime_from_f_tau(F_exp=0.52, F_err=0.03, alpha_stop_ps=0.82)
    assert abs(inv["tau_ps"] - 0.749) < 0.05, "DSAM lifetime inversion ~ 0.75 ps"
    assert abs(inv["tau_fs"] - 748.7) < 10.0
    assert inv["tau_lower_ps"] < inv["tau_ps"] < inv["tau_upper_ps"]

    # LSS constants check
    lss = calculate_lss_stopping_constants(Z_recoil=58, M_recoil=134.0, Z_backing=79, M_backing=197.0)
    assert abs(lss["lss_k_e"] - 0.2103) < 0.01, "LSS electronic stopping coefficient ke"
    print("  ✓ dsam_doppler_attenuation_lss_blaugrund_lifetime_calculator passed.")


def test_hpge_coaxial_electric_field_ballistic_deficit_calculator():
    print("Testing hpge_coaxial_electric_field_ballistic_deficit_calculator...")
    # 1. Depletion voltage and electric field
    dep = calculate_coaxial_depletion_and_field(r1_mm=5.0, r2_mm=35.0, N_net_cm3=3.0e9, V_bias_V=4000.0)
    assert abs(dep["depletion_voltage_V"] - 3026.0) < 10.0, "HPGe depletion voltage ~ 3026 V"
    assert dep["is_fully_depleted"] is True
    assert dep["is_velocity_saturated"] is True

    # 2. Shockley-Ramo collection times
    ramo = calculate_shockley_ramo_collection(r0_mm=25.0, r1_mm=5.0, r2_mm=35.0)
    assert abs(ramo["total_collection_time_ns"] - 200.0) < 5.0, "HPGe collection time at r0=25mm"
    assert abs(ramo["max_possible_collection_time_ns"] - 300.0) < 5.0, "Max collection time"

    # 3. Ballistic deficit: flat-top immunity
    bal = calculate_coaxial_ballistic_deficit(tc_ns=200.0, flat_top_ns=800.0)
    assert bal["trapezoidal_ballistic_deficit_pct"] == 0.0, "Digital trapezoid flat-top immunity"
    print("  ✓ hpge_coaxial_electric_field_ballistic_deficit_calculator passed.")


def test_triaxial_wobbling_tip_chiral_analyzer():
    print("Testing triaxial_wobbling_tip_chiral_analyzer...")
    # 1. Triaxial MOI & kappa
    moi = calculate_triaxial_rotor_moi_parameters(J_m=64.0, J_s=56.0, J_l=13.0)
    assert abs(moi["asymmetry_parameter_kappa"] - 0.9272) < 0.01, "163Lu asymmetry kappa"

    # 2. Pr-135 Transverse wobbling slope
    tw_pr = calculate_transverse_wobbling_spectrum(J_m=21.0, J_s=13.0, J_l=4.0, j_single=5.5, spins=[6.5, 8.5, 10.5, 12.5, 14.5])
    assert tw_pr["wobbling_slope_keV_per_hbar"] < 0.0, "Pr-135 transverse wobbling negative slope"
    assert abs(tw_pr["critical_spin_Ic"] - 14.438) < 0.05, "Pr-135 critical spin Ic"

    # 3. Lawrie TiP sum rule
    tip = classify_tip_vs_phonon_wobbling([1, 2], [867.0, 1980.0], E_2g_keV=205.8, E_2gamma_keV=489.1, E_3gamma_keV=690.5, B_E2_delta2_Wu=15.0)
    assert tip["sum_rule_test"]["delta_sum_keV"] < 10.0, "192Os TiP sum rule vanishing"

    # 4. Chiral doublet splitting
    chiral = analyze_chiral_doublet_staggering([9.0, 10.0, 11.0, 12.0], [0.0, 235.0, 520.0, 856.0], [280.0, 450.0, 680.0, 960.0])
    assert chiral["band_levels"][0]["energy_splitting_DeltaE_keV"] == 280.0
    print("  ✓ triaxial_wobbling_tip_chiral_analyzer passed.")


def test_alpha_decay_gamow_wkb_calculator():
    print("Testing alpha_decay_gamow_wkb_calculator...")
    res_212po = calculate_gamow_factor_wkb(Z_parent=84, A_parent=212, Q_alpha_MeV=8.954, L=0)
    assert abs(res_212po["Gamow_factor_2G"] - 30.961) < 0.05, "212Po Gamow factor 2G"
    assert res_212po["T12_WKB_unhindered_sec"] < 1.0e-7, "212Po unhindered half-life scale"
    hin_212po = evaluate_alpha_hindrance(2.99e-7, res_212po["T12_WKB_unhindered_sec"])
    assert 10.0 < hin_212po["hindrance_factor_HF"] < 100.0, "212Po hindrance factor"

    res_238u = calculate_gamow_factor_wkb(Z_parent=92, A_parent=238, Q_alpha_MeV=4.270, L=0)
    assert abs(res_238u["Gamow_factor_2G"] - 86.38) < 0.1, "238U Gamow factor 2G"
    assert res_238u["T12_WKB_unhindered_sec"] > 1.0e15, "238U unhindered half-life scale"
    print("  ✓ alpha_decay_gamow_wkb_calculator passed.")


def test_decoupling_parameter_khalf_band_calculator():
    print("Testing decoupling_parameter_khalf_band_calculator...")
    # Pure j decoupling parameters
    assert calculate_pure_j_decoupling_parameter(5.5) == -6.0, "h11/2 pure intruder decoupling parameter"
    assert calculate_pure_j_decoupling_parameter(6.5) == 7.0, "i13/2 pure intruder decoupling parameter"

    # Invert 169Tm [411 1/2] ground band
    spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    energies = [0.0, 8.41, 118.19, 138.93, 332.08, 368.21]
    inv = invert_khalf_band_parameters(spins, energies)
    assert abs(inv["decoupling_parameter_a"] - (-0.743)) < 0.05, "169Tm decoupling parameter inversion"
    assert abs(inv["A_rot_keV"] - 12.35) < 0.1, "169Tm rotational parameter inversion"
    print("  ✓ decoupling_parameter_khalf_band_calculator passed.")



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
    test_dipole_polarizability_neutron_skin_calculator()
    test_gilbert_cameron_level_density_calculator()
    test_davydov_wobbling_rotor_calculator()
    test_particle_identification_delta_e_calculator()
    test_compound_nucleus_evaporation_calculator()
    test_experimental_uncertainty_covariance_calculator()
    test_collective_quadrupole_pes_calculator()
    test_hpge_pulse_processing_pole_zero_calculator()
    test_chiral_geometry_tac_calculator()
    test_beta_decay_log_ft_phase_space_calculator()
    test_gallagher_moszkowski_coupling_calculator()
    test_nilsson_model_hamiltonian_diagonalizer()
    test_fission_fragment_mass_yield_calculator()
    test_pulse_shape_discrimination_psd_calculator()
    test_multi_quasiparticle_blocked_bcs_calculator()
    test_internal_pair_creation_ipc_calculator()
    test_rmf_deformed_constrained_calculator()
    test_isobaric_analog_state_ced_calculator()
    test_gamma_cascade_calorimetry_calculator()
    test_wigner_supermultiplet_su4_calculator()
    test_linear_momentum_transfer_incomplete_fusion_calculator()
    test_rdds_plunger_lifetime_calculator()
    test_double_beta_decay_nme_calculator()
    test_heavy_ion_elastic_rainbow_scattering_calculator()
    test_core_polarization_effective_charge_calculator()
    test_fission_isomer_double_hump_transmission_calculator()
    test_abrasion_ablation_fragmentation_calculator()
    test_chiral_vibrational_tunneling_calculator()
    test_clover_compton_addback_polarization_calculator()
    test_strutinsky_shell_correction_calculator()
    test_nilsson_magnetic_moment_gk_calculator()
    test_angular_momentum_projection_amp_calculator()
    test_spin_dipole_resonance_sdr_calculator()
    test_gamma_gamma_matrix_slicer_calculator()
    test_nolen_schiffer_isospin_anomaly_calculator()
    test_multiphonon_wobbling_anharmonic_calculator()
    test_rmf_symmetry_energy_slope_calculator()
    test_wigner_racah_algebra_9j_calculator()
    test_charge_exchange_gt_quenching_calculator()
    test_alignment_attenuation_coefficients_calculator()
    test_r_process_waiting_point_flow_calculator()
    test_wobbling_branching_ratio_phase_calculator()
    test_gdr_lorentzian_trk_sumrule_calculator()
    test_isovector_giant_resonance_splitting_calculator()
    test_detector_deadtime_pileup_correction_calculator()
    test_heavy_ion_fusion_evaporation_channel_calculator()
    test_poisson_likelihood_peak_fitting_bias_calculator()
    test_coriolis_attenuation_bandcrossing_calculator()
    test_directional_correlation_f_coefficients_calculator()
    test_decoupling_parameter_khalf_band_calculator()
    test_alpha_decay_gamow_wkb_calculator()
    test_triaxial_wobbling_tip_chiral_analyzer()
    test_feldman_cousins_unified_confidence_interval_calculator()
    test_hpge_coaxial_electric_field_ballistic_deficit_calculator()
    test_heavy_ion_fusion_wong_calculator()
    test_dsam_doppler_attenuation_lifetime_calculator()
    test_mariscotti_vmi_rotational_stretching_calculator()
    test_seniority_scheme_half_filled_isomer_calculator()
    test_constant_fraction_discriminator_calculator()
    test_grodzins_deformation_inverter()
    test_cranked_shell_model_band_crossing_calculator()
    test_optical_model_potential_reaction_calculator()
    test_in_beam_doppler_broadening_calculator()
    test_triaxial_cranking_routhian_calculator()
    test_in_beam_experiment_analysis_pipeline()
    test_schiffer_true_two_body_matrix_elements_calculator()
    test_tac_3d_chiral_orientation_calculator()
    test_gamma_band_mixing_z_gamma_calculator()
    test_level_scheme_loop_balancer()
    test_davydov_chaban_stretching_calculator()
    test_double_root_arbitrator()
    test_multi_quasiparticle_mchid()
    test_heavy_ion_dic_wilczynski()
    test_octupole_collective_ewsr()
    test_digital_psd_optimizer()
    test_tac_pairing_chiral()
    test_cascade_deorientation_uk()
    test_mwpc_drift_chamber()
    test_coriolis_band_mixing()
    test_spontaneous_fission_action()
    test_ptrm_diagonalizer()
    test_mwd_baseline_restorer()
    test_fast_timing_gcd()
    test_chiral_gfactor_equality()
    test_tcs_coincidence_summing()
    test_chiral_octupole_quartet()
    test_heavy_ion_optical_rainbow()
    test_time_spectrum_convolution()
    test_two_quasiparticle_wobbling()
    test_hpge_efficiency_covariance()
    test_gated_multiplet_deconvolution()
    test_tsd_wobbling_decayout()
    test_mcintyre_s_matrix()
    test_3d_tac_pitchfork_bifurcation()
    test_fold_multiplicity_unfolding()
    test_chiral_selection_rules()
    test_prompt_delayed_time_gating()
    test_hexadecapole_wobbling()
    test_chiral_quartic_schrodinger()
    test_hpge_solid_angle_qk()
    test_pulser_live_time()
    test_tsd_pes_strutinsky()
    test_coriolis_anti_pairing()
    test_array_coincidence_efficiency()
    test_tpsm_3d_projection()
    test_rdds_ddcm_lifetime()
    test_davydov_rostovsky_mixing()
    test_2d_snip_background()
    test_odd_odd_recoil_chiral()
    test_hpge_energy_non_linearity()
    test_odd_odd_chiral_mep()
    test_hpge_tfa_crossover_walk()
    test_triaxial_fusion_barrier()
    test_odd_a_wobbling_stability()
    test_dsam_zbl_stopping()
    test_cranked_shape_coexistence_pes()
    test_spin_alignment_mixing()
    test_multiple_chiral_doublets_mchid()
    test_charged_particle_pid()
    test_triaxial_scissors_mode()
    print("Regression checks passed. Scientific validation and book-reading coverage require separate evidence.")
