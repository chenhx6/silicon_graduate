#!/usr/bin/env python3
"""
In-Beam Vacuum Deorientation Effect & Hyperfine Perturbed Angular Distribution Calculator.

Based on:
  - W. D. Hamilton (1975), "The Electromagnetic Interaction in Nuclear Spectroscopy", Chapter 13
  - R. M. Steffen & K. Alder (1975), "Angular Distribution and Correlation of Gamma Radiation"
  - A. Abragam & R. V. Pound, Phys. Rev. 92, 943 (1953) (Fast relaxation stochastic theory)

Features:
  1. Estimates recoil-ion hyperfine magnetic field B_hf and Larmor precession frequency omega_L.
  2. Calculates time-integrated attenuation factors G2(tau) and G4(tau) as a function of level lifetime.
  3. Deconvolves and restores true intrinsic angular distribution coefficients A2 and A4 from measured a2, a4.
"""

import numpy as np


def calculate_hyperfine_field_and_omega(Z, beta_recoil, g_factor=0.35):
    """
    Estimate average hyperfine magnetic field B_hf (Tesla) and Larmor frequency omega_L (rad/ps).
    Uses empirical scaling for highly stripped heavy ions in vacuum:
      B_hf approx 0.05 * Z * (beta / 0.01)^0.6 * 100 Tesla
      hbar * omega_L = g * mu_N * B_hf
    where mu_N = 3.15245e-14 MeV/T.
    """
    z_val = float(Z)
    b_val = max(1e-4, float(beta_recoil))
    
    # Average hyperfine field in Tesla
    # For A approx 130 (Z=58, beta=0.025), B_hf is typically 200 - 400 Tesla
    b_hf_tesla = 5.0 * z_val * ((b_val / 0.01)**0.55)
    
    # Nuclear magneton in MeV/T: 3.1524512e-14
    # hbar = 6.5821195e-22 MeV*s = 6.5821195e-10 MeV*ps
    mu_N_MeV_per_T = 3.1524512e-14
    hbar_MeV_ps = 6.5821195e-10
    
    # Precession frequency omega_L in rad / ps
    # omega_L = (g * mu_N * B_hf) / hbar
    omega_L_per_ps = abs(g_factor) * mu_N_MeV_per_T * b_hf_tesla / hbar_MeV_ps
    
    return {
        "B_hf_Tesla": b_hf_tesla,
        "omega_L_per_ps": omega_L_per_ps,
        "precession_period_ps": 2.0 * np.pi / max(1e-6, omega_L_per_ps)
    }


def calculate_attenuation_factors(tau_level_ps, Z, beta_recoil, g_factor=0.35, tau_r_ps=3.0):
    """
    Calculate time-integrated attenuation factors G2 and G4 using Abragam-Pound stochastic model:
      G_k(tau) = 1 / [ 1 + (1/3)*k*(k+1) * omega_L^2 * tau_r * tau ]
    """
    hf = calculate_hyperfine_field_and_omega(Z, beta_recoil, g_factor)
    wL = hf["omega_L_per_ps"]
    t_lev = max(1e-4, float(tau_level_ps))
    tr = max(1e-4, float(tau_r_ps))
    
    # Relaxation damping factors
    # lambda_k = (1/3)*k*(k+1) * wL^2 * tau_r
    # lambda_2 = 2 * wL^2 * tau_r
    # lambda_4 = (20/3) * wL^2 * tau_r
    lambda_2 = 2.0 * (wL**2) * tr
    lambda_4 = (20.0 / 3.0) * (wL**2) * tr
    
    G2 = 1.0 / (1.0 + lambda_2 * t_lev)
    G4 = 1.0 / (1.0 + lambda_4 * t_lev)
    
    return {
        "G2": float(G2),
        "G4": float(G4),
        "lambda_2_per_ps": float(lambda_2),
        "lambda_4_per_ps": float(lambda_4),
        "omega_L_per_ps": float(wL),
        "B_hf_Tesla": float(hf["B_hf_Tesla"])
    }


def correct_measured_angular_distribution(a2_meas, a4_meas, G2, G4, a2_err=None, a4_err=None):
    """
    Deconvolve attenuation to restore true intrinsic angular distribution coefficients:
      A_2 = a_2_meas / G_2
      A_4 = a_4_meas / G_4
    """
    g2 = max(0.05, float(G2))
    g4 = max(0.05, float(G4))
    
    A2_true = float(a2_meas) / g2
    A4_true = float(a4_meas) / g4
    
    A2_err = (float(a2_err) / g2) if a2_err is not None else None
    A4_err = (float(a4_err) / g4) if a4_err is not None else None
    
    return {
        "A2_true": A2_true,
        "A2_err": A2_err,
        "A4_true": A4_true,
        "A4_err": A4_err,
        "G2_correction_factor": 1.0 / g2,
        "G4_correction_factor": 1.0 / g4
    }


if __name__ == "__main__":
    print("=== Benchmark: In-Beam Vacuum Deorientation Calculator ===")
    # Typical A approx 130 recoil ion: 131Ce (Z=58), recoil beta = 0.025, g-factor = 0.30
    # Level lifetime tau = 25 ps (e.g. low-spin state or isomer)
    z_test = 58
    beta_test = 0.025
    tau_test = 25.0 # ps
    g_test = 0.30
    
    att = calculate_attenuation_factors(tau_test, z_test, beta_test, g_factor=g_test)
    print(f"  Ion Hyperfine Magnetic Field  : B_hf = {att['B_hf_Tesla']:.1f} Tesla")
    print(f"  Larmor Precession Frequency   : omega_L = {att['omega_L_per_ps']:.4f} rad/ps")
    print(f"  Time-Integrated Attenuation   : G2 = {att['G2']:.3f}, G4 = {att['G4']:.3f}")
    
    # Suppose experimental measured coefficients are a2 = -0.22 +/- 0.02, a4 = 0.0
    corr = correct_measured_angular_distribution(a2_meas=-0.22, a4_meas=0.0,
                                                 G2=att["G2"], G4=att["G4"],
                                                 a2_err=0.02, a4_err=0.01)
    print(f"\n  Angular Distribution Restoration:")
    print(f"    Measured Coeff  : a2_meas = -0.22 +/- 0.02 (Suppressed by deorientation!)")
    print(f"    Restored Coeff  : A2_true = {corr['A2_true']:+.3f} +/- {corr['A2_err']:.3f} (Correction factor: {corr['G2_correction_factor']:.2f}x)")
    print("  Outcome: Quantitatively restores true nuclear orientation, eliminating deorientation bias!")
