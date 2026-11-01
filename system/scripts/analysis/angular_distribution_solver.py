#!/usr/bin/env python3
"""
In-Beam Gamma-Ray Angular Distribution & Multipole Mixing Ratio (delta) Solver.

Based on:
  - Zhu Yongsheng (2006), "Probability and Statistics in Experimental Physics"
  - W. D. Hamilton (1975), "The Electromagnetic Interaction in Nuclear Spectroscopy"

Solves:
  1. Weighted least-squares fit of W(theta) = A0 * [1 + a2*P2(cos theta) + a4*P4(cos theta)].
  2. Analytic dual-root solution for multipole mixing ratio delta(E2/M1).
  3. Profile likelihood delta-chi^2 scanning for root discrimination and confidence intervals.
"""

import numpy as np
from scipy.optimize import curve_fit, minimize


def legendre_p2(x):
    return 0.5 * (3.0 * x**2 - 1.0)


def legendre_p4(x):
    return 0.125 * (35.0 * x**4 - 30.0 * x**2 + 3.0)


def angular_distribution_model(theta_deg, A0, a2, a4):
    """
    W(theta) = A0 * [1 + a2 * P2(cos theta) + a4 * P4(cos theta)]
    """
    cos_th = np.cos(np.radians(theta_deg))
    return A0 * (1.0 + a2 * legendre_p2(cos_th) + a4 * legendre_p4(cos_th))


def fit_angular_distribution(theta_deg_arr, yield_arr, error_arr, fix_a4_zero=False):
    """
    Fit experimental yields at various detector angles.

    Returns:
        dict with fitted params (A0, a2, a4), covariance matrix, chi2, and ndof.
    """
    theta_deg = np.array(theta_deg_arr, dtype=float)
    y = np.array(yield_arr, dtype=float)
    sy = np.array(error_arr, dtype=float)
    
    if fix_a4_zero:
        def model_fixed(th, A0, a2):
            return angular_distribution_model(th, A0, a2, 0.0)
        popt, pcov = curve_fit(model_fixed, theta_deg, y, p0=[np.mean(y), 0.0], sigma=sy, absolute_sigma=True)
        A0_fit, a2_fit = popt
        a4_fit = 0.0
        cov_matrix = np.pad(pcov, ((0, 1), (0, 1)), mode='constant')
        ndof = len(theta_deg) - 2
        residuals = y - model_fixed(theta_deg, *popt)
    else:
        p0 = [np.mean(y), 0.0, 0.0]
        popt, pcov = curve_fit(angular_distribution_model, theta_deg, y, p0=p0, sigma=sy, absolute_sigma=True)
        A0_fit, a2_fit, a4_fit = popt
        cov_matrix = pcov
        ndof = len(theta_deg) - 3
        residuals = y - angular_distribution_model(theta_deg, *popt)
        
    chi2 = np.sum((residuals / sy)**2)
    
    return {
        "A0": A0_fit,
        "a2": a2_fit,
        "a4": a4_fit,
        "a2_err": np.sqrt(cov_matrix[1, 1]),
        "a4_err": np.sqrt(cov_matrix[2, 2]) if not fix_a4_zero else 0.0,
        "covariance_matrix": cov_matrix,
        "chi2": chi2,
        "ndof": ndof,
        "reduced_chi2": chi2 / max(1, ndof)
    }


def solve_delta_dual_roots(a2_exp, F2_LL, F2_LLp, F2_LpLp, alpha2=1.0):
    """
    Solve quadratic equation for delta:
    a2 = alpha2 * (F2_LL + 2*delta*F2_LLp + delta^2 * F2_LpLp) / (1 + delta^2)
    
    (a2 - alpha2 * F2_LpLp) * delta^2 - (2 * alpha2 * F2_LLp) * delta + (a2 - alpha2 * F2_LL) = 0
    """
    A = a2_exp - alpha2 * F2_LpLp
    B = -2.0 * alpha2 * F2_LLp
    C = a2_exp - alpha2 * F2_LL
    
    discriminant = B**2 - 4.0 * A * C
    if discriminant < 0:
        return None # No real root (unphysical or severe experimental error)
        
    sqrt_disc = np.sqrt(discriminant)
    delta_1 = (-B + sqrt_disc) / (2.0 * A)
    delta_2 = (-B - sqrt_disc) / (2.0 * A)
    
    # Return sorted by absolute magnitude
    roots = sorted([delta_1, delta_2], key=lambda x: abs(x))
    return {
        "delta_small_root (M1 dominated)": roots[0],
        "delta_large_root (E2 dominated)": roots[1],
        "discriminant": discriminant
    }


def profile_likelihood_scan(delta_grid, a2_exp, a2_err, P_exp=None, P_err=None,
                            F2_LL=0.0, F2_LLp=0.0, F2_LpLp=0.0, alpha2=1.0,
                            pol_sensitivity_func=None):
    """
    Scan joint chi^2(delta) vs delta to observe dual-root degeneracy and break it with polarization.
    """
    chi2_ad = []
    chi2_joint = []
    
    for d in delta_grid:
        a2_theo = alpha2 * (F2_LL + 2.0 * d * F2_LLp + d**2 * F2_LpLp) / (1.0 + d**2)
        c2_ad = ((a2_theo - a2_exp) / a2_err)**2
        chi2_ad.append(c2_ad)
        
        if P_exp is not None and pol_sensitivity_func is not None and P_err is not None:
            P_theo = pol_sensitivity_func(d)
            c2_pol = ((P_theo - P_exp) / P_err)**2
            chi2_joint.append(c2_ad + c2_pol)
        else:
            chi2_joint.append(c2_ad)
            
    return np.array(chi2_ad), np.array(chi2_joint)


if __name__ == "__main__":
    # Benchmark test on typical in-beam gamma-ray transition
    print("=== Benchmark: In-Beam Angular Distribution Fit ===")
    thetas = [30.0, 45.0, 60.0, 90.0, 120.0, 135.0, 150.0]
    # Simulated counts with A0=1000, a2=-0.40, a4=0.0
    true_y = angular_distribution_model(thetas, 1000.0, -0.40, 0.0)
    np.random.seed(42)
    errors = np.sqrt(true_y)
    noisy_y = true_y + np.random.normal(0, errors)
    
    fit_res = fit_angular_distribution(thetas, noisy_y, errors)
    print(f"  Fitted a2: {fit_res['a2']:.3f} +/- {fit_res['a2_err']:.3f}")
    print(f"  Fitted a4: {fit_res['a4']:.3f} +/- {fit_res['a4_err']:.3f}")
    print(f"  Chi2 / NDOF: {fit_res['chi2']:.2f} / {fit_res['ndof']}")
    
    # Example dual root solve for I_i = 17/2 -> I_f = 15/2 transition
    # F coefficients for Delta I = 1, dipole-quadrupole mixing
    F2_11 = -0.3742
    F2_12 = 0.4472
    F2_22 = 0.1265
    alpha2 = 0.85
    
    roots = solve_delta_dual_roots(fit_res['a2'], F2_11, F2_12, F2_22, alpha2=alpha2)
    if roots:
        print("\n=== Dual Root Solution for Delta ===")
        print(f"  Root 1 (small |delta|): {roots['delta_small_root (M1 dominated)']:.4f}")
        print(f"  Root 2 (large |delta|): {roots['delta_large_root (E2 dominated)']:.4f}")
        print("  Notice: Both roots reproduce the EXACT same a2 value!")
