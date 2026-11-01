#!/usr/bin/env python3
"""
Heavy-Ion Fusion-Evaporation Kinematics & Reaction Calculator.

Based on:
  - Lin Chengjian (2017), "Heavy Ion Nuclear Reactions" (Science Press)
  - Wu Zhihua (2005), "Nuclear Physics Experimental Methods" (Atomic Energy Press)

Features:
  1. Center-of-mass energy (E_cm) and Q-value calculations.
  2. Bass Coulomb barrier (V_B) and contact radius (R_B).
  3. Maximum grazing angular momentum (l_max) and total fusion cross section.
  4. Residual recoil nucleus velocity (beta = v/c) and lab momentum.
  5. Doppler shift and Doppler energy broadening at HPGe detector angles.
"""

import numpy as np


def calculate_kinematics(Ap, Zp, At, Zt, Elab_MeV, dE_lab_loss=0.0):
    """
    Calculate heavy-ion fusion reaction kinematics.

    Parameters:
        Ap (int): Projectile mass number
        Zp (int): Projectile charge number
        At (int): Target mass number
        Zt (int): Target charge number
        Elab_MeV (float): Beam energy in laboratory frame (MeV)
        dE_lab_loss (float): Beam energy loss in target (default 0.0)

    Returns:
        dict: Kinematics parameters
    """
    E_effective = Elab_MeV - dE_lab_loss / 2.0
    # Reduced mass (in atomic mass units u)
    mu_u = (Ap * At) / (Ap + At)
    # Center of mass energy
    E_cm = E_effective * (At / (Ap + At))
    
    # Bass interaction radius: R_B = 1.07*(Ap^(1/3) + At^(1/3)) + 2.72 fm
    R_B = 1.07 * (Ap**(1.0/3.0) + At**(1.0/3.0)) + 2.72
    # Coulomb barrier V_B in MeV (e^2 / 4pi*eps0 = 1.439965 MeV*fm)
    V_B = 1.439965 * (Zp * Zt) / R_B
    
    # Grazing angular momentum l_max (hbar)
    # hbar*c = 197.327 MeV*fm, 1 u = 931.494 MeV/c^2
    if E_cm > V_B:
        # 2 * mu * (E_cm - V_B) / hbar^2
        # = 2 * (mu * 931.494) * (E_cm - V_B) / (197.327^2)
        factor = 2.0 * (mu_u * 931.494) * (E_cm - V_B) / (197.327**2)
        l_max = R_B * np.sqrt(max(0.0, factor))
        # Total classical fusion cross section (mb): 1 fm^2 = 10 mb
        sigma_fus_mb = 10.0 * np.pi * (R_B**2) * (1.0 - V_B / E_cm)
    else:
        l_max = 0.0
        sigma_fus_mb = 0.0
        
    # Recoil velocity beta = v/c
    # P_recoil = P_proj = sqrt(2 * M_p * E_lab)
    # M_CN = (Ap + At) * 931.494 MeV
    M_p_MeV = Ap * 931.494
    M_CN_MeV = (Ap + At) * 931.494
    P_proj = np.sqrt(2.0 * M_p_MeV * E_effective)
    beta = P_proj / M_CN_MeV
    
    return {
        "Ap": Ap, "Zp": Zp, "At": At, "Zt": Zt,
        "Elab_MeV": Elab_MeV,
        "E_cm_MeV": E_cm,
        "R_B_fm": R_B,
        "V_B_MeV": V_B,
        "E_cm_over_VB": E_cm / V_B,
        "l_max_hbar": l_max,
        "sigma_fus_mb": sigma_fus_mb,
        "beta_v_over_c": beta,
        "recoil_velocity_percent_c": beta * 100.0
    }


def doppler_shift(E_gamma0_keV, beta, theta_deg):
    """
    Calculate Doppler-shifted gamma energy.
    E(theta) = E0 * sqrt(1 - beta^2) / (1 - beta * cos(theta))
    """
    theta_rad = np.radians(theta_deg)
    gamma_lorentz = 1.0 / np.sqrt(1.0 - beta**2)
    return E_gamma0_keV / (gamma_lorentz * (1.0 - beta * np.cos(theta_rad)))


def doppler_broadening(E_gamma0_keV, beta, theta_deg, detector_opening_angle_deg):
    """
    Calculate kinematic Doppler broadening due to finite detector opening angle.
    Delta E_D approx E0 * beta * sin(theta) * Delta_theta
    """
    theta_rad = np.radians(theta_deg)
    delta_theta_rad = np.radians(detector_opening_angle_deg)
    return E_gamma0_keV * beta * np.sin(theta_rad) * delta_theta_rad


if __name__ == "__main__":
    # Benchmark example: 100Mo(36S, 5n)131Ce reaction at Elab = 150 MeV
    print("=== Benchmark: 100Mo + 36S -> 136Ce* at 150 MeV ===")
    res = calculate_kinematics(Ap=36, Zp=16, At=100, Zt=42, Elab_MeV=150.0)
    for k, v in res.items():
        print(f"  {k:28s}: {v:.4f}" if isinstance(v, float) else f"  {k:28s}: {v}")
        
    E0 = 1000.0 # 1 MeV gamma ray
    print(f"\nDoppler shift & broadening for E_gamma = {E0} keV (opening angle = 8 deg):")
    for th in [30, 45, 90, 135, 150]:
        E_shift = doppler_shift(E0, res["beta_v_over_c"], th)
        dE = doppler_broadening(E0, res["beta_v_over_c"], th, 8.0)
        print(f"  Theta = {th:3d} deg: E_shift = {E_shift:8.2f} keV (shift = {E_shift - E0:+6.2f} keV), Broadening = {dE:5.2f} keV")
