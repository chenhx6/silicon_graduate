#!/usr/bin/env python3
"""
Nuclear Excited-State Lifetime & Doppler Shift Attenuation (DSAM/RDM) Calculator.

Based on:
  - Wu Zhihua (2005), "Nuclear Physics Experimental Methods" (Chapter 15)
  - T. K. Alexander & J. S. Forster, Adv. Nucl. Phys. 10, 197 (1978)
  - Differential Decay Curve Method (DDCM), A. Dewald et al., Z. Phys. A 334, 163 (1989)

Features:
  1. Doppler attenuation factor F(tau) for electronic/nuclear stopping models.
  2. Analytic lifetime extraction from measured centroid shift F(tau).
  3. RDM plunger method: distance-dependent decay curve and lifetime fitting.
  4. Absolute transition probabilities: B(E2), B(M1), and transition quadrupole moment Qt.
"""

import numpy as np


def calculate_stopping_time_alpha(A_recoil, Z_recoil, beta_0, stopper_material="Au"):
    """
    Estimate characteristic electronic stopping slowing-down time alpha (ps).
    In low-velocity regime (beta < 0.03), v(t) approx v_0 * exp(-t / alpha).
    Typical slowing down times in heavy stoppers (Au, Pb, Ta) are 0.8 - 1.5 ps.
    """
    stopper_constants = {
        "Au": {"Z": 79, "A": 197, "density": 19.32, "alpha_ref": 1.05},
        "Pb": {"Z": 82, "A": 207, "density": 11.34, "alpha_ref": 1.25},
        "Ta": {"Z": 73, "A": 181, "density": 16.65, "alpha_ref": 0.95},
    }
    mat = stopper_constants.get(stopper_material, stopper_constants["Au"])
    # Scaling with recoil mass: heavier recoil slows down slightly slower (longer alpha)
    alpha_ps = mat["alpha_ref"] * (A_recoil / 130.0) * (0.02 / max(1e-4, beta_0))**0.1
    return alpha_ps


def dsam_attenuation_factor_f(tau_ps, alpha_ps):
    """
    Calculate Doppler shift attenuation factor F(tau) = <v> / v0.
    F(tau) = 1 / tau * int_0^inf (v(t)/v0) * exp(-t/tau) dt
    For exponential velocity slowing-down v(t) = v0 * exp(-t/alpha):
      F(tau) = alpha / (alpha + tau)
    """
    return alpha_ps / (alpha_ps + tau_ps)


def dsam_invert_lifetime(F_meas, alpha_ps):
    """
    Invert measured attenuation factor F to extract lifetime tau (ps).
    tau = alpha * (1 / F - 1)
    """
    if F_meas <= 0.0 or F_meas >= 1.0:
        raise ValueError(f"F_meas must be strictly between 0 and 1, got {F_meas}")
    return alpha_ps * (1.0 / F_meas - 1.0)


def rdm_plunger_lifetime(distances_um, stopped_counts, shifted_counts, beta_0):
    """
    Fit recoil distance method (RDM) decay curve.
    R0(d) = I_stopped / (I_stopped + I_shifted) = exp(-d / (v0 * tau))
    d in micrometers (1 um = 1e-6 m). v0 = beta_0 * c (in um/ps).
    v0 (um/ps) approx beta_0 * 299.792 um/ps
    """
    v0_um_per_ps = beta_0 * 299.792458
    d = np.array(distances_um, dtype=float)
    n_stop = np.array(stopped_counts, dtype=float)
    n_shift = np.array(shifted_counts, dtype=float)
    
    total = n_stop + n_shift
    R = n_stop / total
    
    # Linear regression on ln(R) = -d / (v0 * tau)
    valid = R > 0.01
    ln_R = np.log(R[valid])
    d_valid = d[valid]
    
    # Slope m = -1 / (v0 * tau)
    slope, intercept = np.polyfit(d_valid, ln_R, 1)
    tau_ps = -1.0 / (slope * v0_um_per_ps)
    return {
        "tau_ps": tau_ps,
        "v0_um_per_ps": v0_um_per_ps,
        "slope": slope,
        "decay_constant_per_um": -slope
    }


def calculate_absolute_transition_strengths(tau_ps, E_gamma_keV, delta, I_initial,
                                            branching_ratio=1.0, alpha_tot=0.0):
    """
    Calculate absolute B(E2), B(M1), and transition quadrupole moment Qt.
    
    Formula:
      B(E2) = 0.08156 * b_gamma / [tau(ps) * (E_gamma/1000)^5 * (1 + alpha_tot)] * [delta^2 / (1 + delta^2)] (e^2 b^2)
      B(M1) = 0.05679 * b_gamma / [tau(ps) * (E_gamma/1000)^3 * (1 + alpha_tot)] * [1 / (1 + delta^2)] (mu_N^2)
      Q_t = sqrt(16 * pi / 5 * B(E2) / <I K 2 0 | I-2 K>^2) / e
    """
    E_MeV = E_gamma_keV / 1000.0
    delta2 = delta**2
    
    # Decay rate components
    factor_e2 = 0.08156 * branching_ratio / (tau_ps * (E_MeV**5) * (1.0 + alpha_tot))
    factor_m1 = 0.05679 * branching_ratio / (tau_ps * (E_MeV**3) * (1.0 + alpha_tot))
    
    B_E2 = factor_e2 * (delta2 / (1.0 + delta2))
    B_M1 = factor_m1 * (1.0 / (1.0 + delta2))
    
    # Single-particle Weisskopf units (W.u.)
    # For A approx 130:
    # B(E2)_sp approx 5.94e-6 * A^(4/3) e^2 b^2 approx 0.0039 e^2 b^2
    # B(M1)_sp approx 1.79 mu_N^2
    b_e2_wu = B_E2 / 0.0039
    b_m1_wu = B_M1 / 1.79
    
    # Intrinsic quadrupole moment estimate for Delta I = 2 (in-band E2)
    # <I 0 2 0 | I-2 0>^2 approx 3/8 for high spin
    Qt_eb = np.sqrt(max(0.0, (16.0 * np.pi / 5.0) * B_E2 / 0.375))
    
    return {
        "B_E2_e2b2": B_E2,
        "B_E2_W_u": b_e2_wu,
        "B_M1_muN2": B_M1,
        "B_M1_W_u": b_m1_wu,
        "Qt_eb": Qt_eb
    }


if __name__ == "__main__":
    print("=== Benchmark: Nuclear Lifetime & DSAM Inversion ===")
    # 131Ce typical high-spin state: recoil beta = 0.025 in Au stopper
    alpha = calculate_stopping_time_alpha(A_recoil=131, Z_recoil=58, beta_0=0.025, stopper_material="Au")
    print(f"  Au Stopper Characteristic Slowing-down Time: alpha = {alpha:.3f} ps")
    
    # Suppose measured attenuation factor F = 0.65 (Doppler shift is 65% of full v0 shift)
    F_exp = 0.65
    tau_extracted = dsam_invert_lifetime(F_exp, alpha)
    print(f"  Measured Attenuation F = {F_exp:.2f} --> Inverted Lifetime tau = {tau_extracted:.3f} ps ({tau_extracted*1000:.1f} fs)")
    
    # Calculate absolute B(E2) for E_gamma = 650 keV in-band transition (pure E2, delta -> inf)
    strengths = calculate_absolute_transition_strengths(tau_extracted, E_gamma_keV=650.0, delta=100.0, I_initial=21/2)
    print(f"  Absolute B(E2)       : {strengths['B_E2_e2b2']:.4f} e^2 b^2 ({strengths['B_E2_W_u']:.1f} W.u.)")
    print(f"  Intrinsic Quad. Qt   : {strengths['Qt_eb']:.2f} e b (Demonstrates clear collective deformation!)")
