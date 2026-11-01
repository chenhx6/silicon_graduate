#!/usr/bin/env python3
"""
Relativistic Coulomb Excitation, Virtual Photon Theory & Lorentz Boost Calculator.

Based on:
  - A. Winther & K. Alder, Nucl. Phys. A 319, 518 (1979) (Relativistic Coulomb excitation)
  - C. A. Bertulani & G. Baur, Phys. Rep. 163, 299 (1988) (Virtual photon method in heavy-ion collisions)
  - T. Glasmacher, Annu. Rev. Nucl. Part. Sci. 48, 1 (1998) (In-beam spectroscopy with radioactive beams)
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions, Ch. 9 (Relativistic collisions)

Features:
  1. Computes relativistic projectile kinematics (gamma, beta, velocity v) and safe impact parameter b_min.
  2. Evaluates the adiabaticity cutoff parameter xi_0 and virtual photon numbers N_E1, N_E2.
  3. Calculates the integrated relativistic Coulomb excitation cross section sigma_E2 (in mb) from B(E2).
  4. Inverts the reduced transition probability B(E2; 0+ -> 2+) from measured Coulex cross section sigma_E2.
  5. Computes in-beam gamma-ray relativistic Lorentz boost angle aberration, solid-angle Jacobian, and Doppler shift.
"""

import numpy as np
import scipy.special as sp

# Physical constants
HBAR_C_MEV_FM = 197.3269804   # MeV * fm
AMU_MEV = 931.49410242        # MeV / c^2
ALPHA_FINE = 1.0 / 137.035999 # Fine structure constant


def calculate_relativistic_coulex_kinematics(E_lab_MeV_u, A_proj, Z_proj, A_targ, Z_targ, d_safe_fm=2.5):
    """
    Compute relativistic heavy-ion collision kinematics, safe impact parameter b_min,
    and safe grazing scattering angle theta_safe.
    """
    if E_lab_MeV_u <= 0:
        raise ValueError("Beam energy E_lab_MeV_u must be strictly positive.")

    gamma = 1.0 + float(E_lab_MeV_u) / AMU_MEV
    beta = np.sqrt(1.0 - 1.0 / (gamma ** 2))

    # Projectile and target radii
    r_p = 1.2 * (float(A_proj) ** (1.0 / 3.0))
    r_t = 1.2 * (float(A_targ) ** (1.0 / 3.0))
    b_min_fm = r_p + r_t + float(d_safe_fm)

    # Grazing scattering angle in center-of-mass (radians)
    # tan(theta_cm / 2) approx (Z_p * Z_t * alpha * hbar*c) / (gamma * mu * beta^2 * c^2 * b_min)
    mu_amu = (float(A_proj) * float(A_targ)) / (float(A_proj) + float(A_targ))
    mu_c2 = mu_amu * AMU_MEV

    tan_half_theta = (float(Z_proj) * float(Z_targ) * ALPHA_FINE * HBAR_C_MEV_FM) / (gamma * mu_c2 * (beta ** 2) * b_min_fm)
    theta_cm_rad = 2.0 * np.arctan(tan_half_theta)
    theta_cm_deg = np.degrees(theta_cm_rad)

    # In laboratory frame: theta_lab approx theta_cm / (1 + A_proj / A_targ)
    theta_lab_deg = theta_cm_deg / (1.0 + float(A_proj) / float(A_targ))

    return {
        "E_lab_MeV_u": float(E_lab_MeV_u),
        "A_proj": int(A_proj),
        "Z_proj": int(Z_proj),
        "A_targ": int(A_targ),
        "Z_targ": int(Z_targ),
        "gamma": float(gamma),
        "beta": float(beta),
        "R_proj_fm": float(r_p),
        "R_targ_fm": float(r_t),
        "b_min_fm": float(b_min_fm),
        "theta_safe_cm_deg": float(theta_cm_deg),
        "theta_safe_lab_deg": float(theta_lab_deg)
    }


def calculate_virtual_photon_numbers(E_x_MeV, b_min_fm, Z_targ, beta, gamma):
    """
    Calculate Winther-Alder virtual photon numbers N_E1 and N_E2 for excitation energy E_x.
    Adiabaticity parameter xi_0 = (E_x * b_min) / (hbar*c * gamma * beta).
    """
    if E_x_MeV <= 0 or b_min_fm <= 0 or beta <= 0:
        raise ValueError("Ex, b_min and beta must be strictly positive.")

    ex = float(E_x_MeV)
    b_min = float(b_min_fm)
    zt = float(Z_targ)
    b = float(beta)
    g = float(gamma)

    xi0 = (ex * b_min) / (HBAR_C_MEV_FM * g * b)

    k0 = sp.k0(xi0)
    k1 = sp.k1(xi0)

    # N_E1
    term1 = xi0 * k0 * k1
    term2 = 0.5 * (b ** 2) * (xi0 ** 2) * (k1 ** 2 - k0 ** 2)
    n_e1 = (2.0 / np.pi) * (zt ** 2) * ALPHA_FINE * (1.0 / (b ** 2)) * (term1 - term2)

    # N_E2
    t1_e2 = 2.0 * (k1 ** 2)
    t2_e2 = (xi0 ** 2) * (k0 ** 2)
    t3_e2 = (b ** 2) * (xi0 ** 2) * (k1 ** 2 - k0 ** 2)
    n_e2 = (2.0 / np.pi) * (zt ** 2) * ALPHA_FINE * (1.0 / (b ** 4)) * (1.0 / (xi0 ** 2)) * (t1_e2 + t2_e2 - t3_e2)

    return {
        "E_x_MeV": ex,
        "xi_0": float(xi0),
        "N_E1": float(n_e1),
        "N_E2": float(n_e2),
        "K0_val": float(k0),
        "K1_val": float(k1)
    }


def calculate_relativistic_e2_coulex_cross_section(B_E2_e2b2, E_x_MeV, E_lab_MeV_u, A_proj, Z_proj, A_targ, Z_targ, d_safe_fm=2.5):
    """
    Compute total relativistic E2 Coulomb excitation cross section sigma_E2 (in mb):
    sigma_E2 = (Z_t * alpha / beta)^2 * [B(E2) / (e^2 * b_min^2)] * f_E2(xi_0, beta) * 10.0 mb/fm^2.
    """
    kin = calculate_relativistic_coulex_kinematics(E_lab_MeV_u, A_proj, Z_proj, A_targ, Z_targ, d_safe_fm=d_safe_fm)
    beta = kin["beta"]
    gamma = kin["gamma"]
    b_min = kin["b_min_fm"]
    zt = float(Z_targ)

    xi0 = (float(E_x_MeV) * b_min) / (HBAR_C_MEV_FM * gamma * beta)

    # f_E2 adiabatic scaling factor
    f_e2 = 0.5 * (1.0 + 1.0 / (gamma ** 2)) * np.exp(-2.0 * xi0)

    # Coupling strength
    coupling_factor = (zt * ALPHA_FINE / beta) ** 2
    # B(E2) in e^2 b^2 -> convert to e^2 fm^4 (1 b^2 = 10000 fm^4)
    b_e2_fm4 = float(B_E2_e2b2) * 10000.0
    geom_factor = b_e2_fm4 / (b_min ** 2) # fm^2

    # Cross section in mb (1 fm^2 = 10 mb)
    sigma_e2_mb = coupling_factor * geom_factor * f_e2 * 10.0

    return {
        "B_E2_e2b2": float(B_E2_e2b2),
        "E_x_MeV": float(E_x_MeV),
        "beta": beta,
        "gamma": gamma,
        "b_min_fm": b_min,
        "xi_0": float(xi0),
        "f_E2": float(f_e2),
        "sigma_E2_mb": float(sigma_e2_mb)
    }


def invert_b_e2_from_coulex_cross_section(sigma_E2_mb, E_x_MeV, E_lab_MeV_u, A_proj, Z_proj, A_targ, Z_targ, d_safe_fm=2.5):
    """
    Invert reduced transition probability B(E2; 0+ -> 2+) in e^2 b^2
    from measured intermediate-energy Coulomb excitation cross section sigma_E2 (in mb).
    """
    kin = calculate_relativistic_coulex_kinematics(E_lab_MeV_u, A_proj, Z_proj, A_targ, Z_targ, d_safe_fm=d_safe_fm)
    beta = kin["beta"]
    gamma = kin["gamma"]
    b_min = kin["b_min_fm"]
    zt = float(Z_targ)

    xi0 = (float(E_x_MeV) * b_min) / (HBAR_C_MEV_FM * gamma * beta)
    f_e2 = 0.5 * (1.0 + 1.0 / (gamma ** 2)) * np.exp(-2.0 * xi0)

    coupling_factor = (zt * ALPHA_FINE / beta) ** 2

    # sigma_E2_mb = coupling_factor * (B_E2_fm4 / b_min^2) * f_e2 * 10.0
    denom = coupling_factor * (1.0 / (b_min ** 2)) * f_e2 * 10.0
    b_e2_fm4 = float(sigma_E2_mb) / max(1e-12, denom)
    b_e2_e2b2 = b_e2_fm4 / 10000.0

    return {
        "measured_sigma_E2_mb": float(sigma_E2_mb),
        "E_x_MeV": float(E_x_MeV),
        "extracted_B_E2_e2b2": float(b_e2_e2b2),
        "extracted_B_E2_e2fm4": float(b_e2_fm4),
        "beta": beta,
        "xi_0": float(xi0)
    }


def transform_gamma_angular_distribution_lorentz(theta_lab_deg_list, beta, a2_cm=0.35, a4_cm=-0.1):
    """
    Transform in-beam gamma-ray angular distribution from center-of-mass frame to laboratory frame:
      1. Aberration angle: cos(theta*) = [cos(theta_lab) - beta] / [1 - beta * cos(theta_lab)].
      2. Doppler factor: D(theta_lab) = sqrt(1 - beta^2) / [1 - beta * cos(theta_lab)].
      3. Solid angle Jacobian: J(theta_lab) = (1 - beta^2) / [1 - beta * cos(theta_lab)]^2.
      4. W_lab(theta_lab) = W_cm(theta*) * J(theta_lab).
    """
    b = float(beta)
    if b <= 0.0 or b >= 1.0:
        raise ValueError("Beta must be in range (0, 1).")

    res = []
    for deg in theta_lab_deg_list:
        th_lab = np.radians(float(deg))
        c_lab = np.cos(th_lab)

        # Aberration
        c_cm = (c_lab - b) / (1.0 - b * c_lab)
        c_cm = min(1.0, max(-1.0, c_cm))
        th_cm_deg = np.degrees(np.arccos(c_cm))

        # Doppler factor
        doppler = np.sqrt(1.0 - b ** 2) / (1.0 - b * c_lab)

        # Solid angle Jacobian
        jacobian = (1.0 - b ** 2) / ((1.0 - b * c_lab) ** 2)

        # CM Angular distribution: W*(theta*) = 1 + a2*P2 + a4*P4
        p2 = 0.5 * (3.0 * (c_cm ** 2) - 1.0)
        p4 = 0.125 * (35.0 * (c_cm ** 4) - 30.0 * (c_cm ** 2) + 3.0)
        w_cm = 1.0 + float(a2_cm) * p2 + float(a4_cm) * p4

        # Laboratory distribution
        w_lab = w_cm * jacobian

        res.append({
            "theta_lab_deg": float(deg),
            "theta_cm_deg": float(th_cm_deg),
            "doppler_shift_factor": float(doppler),
            "jacobian_solid_angle": float(jacobian),
            "W_cm": float(w_cm),
            "W_lab": float(w_lab)
        })

    return res
