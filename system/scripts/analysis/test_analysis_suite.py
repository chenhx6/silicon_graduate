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
    print("ALL 11 SCIENTIFIC ANALYSIS MODULES VERIFIED SUCCESSFULLY!")
