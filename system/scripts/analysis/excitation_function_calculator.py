#!/usr/bin/env python3
"""
Nuclear Reaction Excitation Function & Thin/Thick Target Cross-Section Inverter.

Based on:
  - Lin Chengjian (2017), "Heavy Ion Nuclear Reactions" (Chapter 6)
  - Wu Zhihua (2005), "Nuclear Physics Experimental Methods" (Chapter 13)

Features:
  1. Calculates heavy-ion projectile energy loss Delta_E in thin target foil.
  2. Inverts experimental gamma-ray peak yield to absolute production cross section (mb).
  3. Fits asymmetric Gaussian resonance model to excitation function data points.
"""

import numpy as np
from scipy.optimize import curve_fit


def calculate_target_energy_loss(E_beam_MeV, Ap, Zp, At, Zt, thickness_mg_cm2):
    """
    Estimate heavy-ion beam energy loss Delta_E (MeV) in target foil.
    Uses effective Bethe-Bloch stopping power scaling:
      -dE/dx approx (Z_p_eff^2 / beta^2) * (Z_t / A_t) * L_corr
    """
    # Initial beta
    E_per_u = E_beam_MeV / Ap
    beta2 = 2.0 * E_per_u / 931.494
    beta = np.sqrt(max(1e-6, beta2))
    
    # Effective projectile charge (Barkas / Northcliffe formula)
    # Z_eff = Zp * (1 - exp(-125 * beta / Zp^(2/3)))
    z_eff = Zp * (1.0 - np.exp(-125.0 * beta / (Zp**(2.0/3.0))))
    
    # Stopping power parameterization in MeV / (mg/cm^2)
    # Typically for heavy ions at 3-5 MeV/u, stopping is approx 5 - 15 MeV / (mg/cm^2)
    dEdx_approx = 0.307075 * (z_eff**2 / max(1e-5, beta2)) * (Zt / At) * 0.001
    # Apply low-energy empirical correction
    dEdx = dEdx_approx * np.log(max(1.1, 1000.0 * beta2))
    dEdx = np.clip(dEdx, 0.5, 30.0)
    
    delta_E_MeV = dEdx * thickness_mg_cm2
    E_eff_MeV = E_beam_MeV - delta_E_MeV / 2.0
    
    return {
        "dEdx_MeV_per_mg_cm2": dEdx,
        "delta_E_MeV": delta_E_MeV,
        "E_effective_MeV": max(0.0, E_eff_MeV)
    }


def extract_cross_section_from_yield(peak_area, efficiency, branching_ratio,
                                     beam_current_pnA, duration_hours,
                                     target_thickness_mg_cm2, target_mass_A,
                                     peak_area_err=None):
    """
    Invert measured gamma peak counts to absolute cross section sigma (mb).
    sigma (mb) = [ N_gamma / (N_p * N_target * eff * br) ] * 1e27
    """
    if peak_area_err is None:
        peak_area_err = np.sqrt(max(1.0, peak_area))
        
    # 1. Number of incident projectiles N_p
    # 1 pnA = 1e-9 A / 1.602e-19 C = 6.242e9 ions/sec
    # N_p = 6.242e9 * I_pnA * (t_hours * 3600) = 2.247e13 * I_pnA * t_hours
    N_p = 2.24719e13 * beam_current_pnA * duration_hours
    
    # 2. Number of target nuclei per cm^2 N_target
    # N_target = (thickness_mg * 1e-3 g) * N_A / A_target
    N_target = (target_thickness_mg_cm2 * 1e-3) * 6.02214e23 / target_mass_A
    
    # 3. Denominator
    denom = N_p * N_target * efficiency * branching_ratio
    if denom <= 0:
        raise ValueError("Invalid experimental parameters leading to non-positive denominator.")
        
    # Cross section in cm^2 -> convert to mb (1 b = 1e-24 cm^2, 1 mb = 1e-27 cm^2)
    sigma_mb = (peak_area / denom) * 1e27
    sigma_err_mb = (peak_area_err / denom) * 1e27
    
    return {
        "sigma_mb": sigma_mb,
        "sigma_err_mb": sigma_err_mb,
        "N_projectiles": N_p,
        "N_target_per_cm2": N_target
    }


def asymmetric_gaussian_model(E, E0, sigma_max, width_low, width_high):
    """
    Asymmetric Gaussian model for excitation function resonance peak:
      sigma(E) = sigma_max * exp( -0.5 * ((E - E0) / width)^2 )
    where width = width_low for E < E0, and width_high for E >= E0.
    """
    E_arr = np.array(E, dtype=float)
    res = np.zeros_like(E_arr)
    
    mask_low = E_arr < E0
    res[mask_low] = sigma_max * np.exp(-0.5 * ((E_arr[mask_low] - E0) / max(0.1, width_low))**2)
    res[~mask_low] = sigma_max * np.exp(-0.5 * ((E_arr[~mask_low] - E0) / max(0.1, width_high))**2)
    return res


def fit_excitation_function(energies_MeV, cross_sections_mb, errors_mb):
    """
    Fit measured excitation function data points with asymmetric Gaussian model.
    """
    E = np.array(energies_MeV, dtype=float)
    s = np.array(cross_sections_mb, dtype=float)
    es = np.array(errors_mb, dtype=float)
    
    p0 = [E[np.argmax(s)], np.max(s), 5.0, 7.0]
    bounds = (
        [np.min(E) - 10.0, 0.0, 0.5, 0.5],
        [np.max(E) + 10.0, np.max(s) * 3.0, 30.0, 30.0]
    )
    
    popt, pcov = curve_fit(asymmetric_gaussian_model, E, s, p0=p0, sigma=es, bounds=bounds, absolute_sigma=True)
    E0_fit, smax_fit, w_low, w_high = popt
    errs = np.sqrt(np.diag(pcov))
    
    residuals = s - asymmetric_gaussian_model(E, *popt)
    chi2 = np.sum((residuals / es)**2)
    ndof = len(E) - len(popt)
    
    return {
        "E_opt_MeV": E0_fit,
        "E_opt_err": errs[0],
        "sigma_max_mb": smax_fit,
        "sigma_max_err": errs[1],
        "width_low_MeV": w_low,
        "width_high_MeV": w_high,
        "fwhm_approx_MeV": 1.1774 * (w_low + w_high),
        "chi2": chi2,
        "ndof": max(1, ndof)
    }


if __name__ == "__main__":
    print("=== Benchmark: Target Energy Loss & Cross-Section Inversion ===")
    # Reaction: 36S (Z=16, A=36) at 150 MeV on 100Mo target (Z=42, A=100) of thickness 1.0 mg/cm2
    eloss = calculate_target_energy_loss(150.0, 36, 16, 100, 42, thickness_mg_cm2=1.0)
    print(f"  Target Stopping Power dE/dx: {eloss['dEdx_MeV_per_mg_cm2']:.2f} MeV/(mg/cm^2)")
    print(f"  Energy Loss in 1.0 mg/cm^2 : {eloss['delta_E_MeV']:.2f} MeV")
    print(f"  Effective Reaction Energy  : {eloss['E_effective_MeV']:.2f} MeV")
    
    # Suppose 10 hours beam at 2.0 pnA yielded 25000 peak counts at eff=0.03, br=0.8
    cs = extract_cross_section_from_yield(peak_area=25000.0, efficiency=0.03, branching_ratio=0.8,
                                          beam_current_pnA=2.0, duration_hours=10.0,
                                          target_thickness_mg_cm2=1.0, target_mass_A=100.0)
    print(f"\n  Inverted Absolute Cross Section: {cs['sigma_mb']:.1f} +/- {cs['sigma_err_mb']:.1f} mb")
    
    # Fit synthetic 5n excitation function
    test_energies = [135.0, 142.0, 150.0, 158.0, 165.0]
    test_sigmas = [45.0, 180.0, 310.0, 195.0, 60.0]
    test_errs = [8.0, 15.0, 20.0, 16.0, 10.0]
    
    fit_res = fit_excitation_function(test_energies, test_sigmas, test_errs)
    print("\n  Excitation Function Fit Results:")
    print(f"    Optimal Beam Energy E_opt : {fit_res['E_opt_MeV']:.2f} +/- {fit_res['E_opt_err']:.2f} MeV")
    print(f"    Peak Cross Section        : {fit_res['sigma_max_mb']:.1f} +/- {fit_res['sigma_max_err']:.1f} mb")
    print(f"    FWHM of Energy Window     : {fit_res['fwhm_approx_MeV']:.2f} MeV")
