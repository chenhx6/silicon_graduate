#!/usr/bin/env python3
"""
Thermonuclear Reaction Rates, Gamow Peak Window & Astrophysical S-Factor Calculator.

Based on:
  - G. Gamow, Z. Phys. 51, 204 (1928) (Quantum barrier tunneling & Gamow peak)
  - E. E. Salpeter, Phys. Rev. 88, 547 (1952) (Astrophysical S-factor & pp chain)
  - C. E. Rolfs & W. S. Rodney, Cauldrons in the Cosmos (Univ. Chicago Press, 1988)
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions, Ch. 7

Features:
  1. Computes the location of the Gamow peak E_0 (keV) and effective energy window width Delta (keV).
  2. Evaluates the dimensionless Sommerfeld parameter eta(E) and Coulomb barrier penetration exp(-2*pi*eta).
  3. Converts experimental cross section sigma(E) to the astrophysical S-factor S(E) in keV*b.
  4. Calculates non-resonant thermonuclear reaction rates N_A <sigma v> in cm^3 / (mol * s).
  5. Computes resonant reaction rates for narrow Breit-Wigner isolated resonances with resonance strength omega*gamma.
"""

import numpy as np

# Physical constants
AMU_MEV = 931.49410242        # MeV / c^2
HBAR_C_MEV_FM = 197.3269804   # MeV * fm
ALPHA_FINE = 1.0 / 137.035999 # Fine structure constant


def calculate_gamow_peak_and_window(T9, Z1, A1, Z2, A2):
    """
    Compute Gamow peak energy E_0 (in keV) and effective window width Delta (in keV)
    at plasma temperature T9 (in 10^9 K):
      E_0 = 122.04 * (Z1^2 * Z2^2 * A_red)^(1/3) * T9^(2/3) keV.
      Delta = 236.8 * (Z1^2 * Z2^2 * A_red)^(1/6) * T9^(5/6) keV.
    """
    if T9 <= 0:
        raise ValueError("Temperature T9 must be strictly positive.")

    z1 = float(Z1)
    z2 = float(Z2)
    a1 = float(A1)
    a2 = float(A2)
    a_red = (a1 * a2) / (a1 + a2)

    factor = (z1 ** 2) * (z2 ** 2) * a_red
    e0_keV = 122.04 * (factor ** (1.0 / 3.0)) * (float(T9) ** (2.0 / 3.0))
    delta_keV = 236.8 * (factor ** (1.0 / 6.0)) * (float(T9) ** (5.0 / 6.0))

    e_low = max(0.01, e0_keV - delta_keV / 2.0)
    e_high = e0_keV + delta_keV / 2.0

    # Gamow energy E_G in keV
    e_g_keV = 978.5 * factor

    return {
        "T9": float(T9),
        "Z1": int(z1),
        "A1": float(a1),
        "Z2": int(z2),
        "A2": float(a2),
        "A_reduced": float(a_red),
        "E_Gamow_constant_keV": float(e_g_keV),
        "E0_Gamow_peak_keV": float(e0_keV),
        "Delta_window_width_keV": float(delta_keV),
        "Gamow_window_lower_keV": float(e_low),
        "Gamow_window_upper_keV": float(e_high)
    }


def calculate_sommerfeld_parameter(E_cm_keV, Z1, A1, Z2, A2):
    """
    Compute Sommerfeld parameter eta(E) and Coulomb transmission probability exp(-2*pi*eta):
      eta = 4.980 * Z1 * Z2 * sqrt(A_red / E_cm_keV).
    """
    e_cm = float(E_cm_keV)
    if e_cm <= 0:
        raise ValueError("Center of mass energy E_cm_keV must be strictly positive.")

    z1 = float(Z1)
    z2 = float(Z2)
    a_red = (float(A1) * float(A2)) / (float(A1) + float(A2))

    eta = 4.980 * z1 * z2 * np.sqrt(a_red / e_cm)
    two_pi_eta = 2.0 * np.pi * eta

    if two_pi_eta > 200.0:
        p_coulomb = 0.0
    else:
        p_coulomb = np.exp(-two_pi_eta)

    return {
        "E_cm_keV": e_cm,
        "sommerfeld_eta": float(eta),
        "two_pi_eta": float(two_pi_eta),
        "coulomb_penetration_factor": float(p_coulomb)
    }


def convert_cross_section_to_s_factor(sigma_barn, E_cm_keV, Z1, A1, Z2, A2):
    """
    Convert laboratory cross section sigma(E) in barns to astrophysical S-factor S(E):
      S(E) = sigma(E) * E_cm_keV * exp(2 * pi * eta).
    Units: S(E) in keV * b (and in MeV * b).
    """
    somm = calculate_sommerfeld_parameter(E_cm_keV, Z1, A1, Z2, A2)
    two_pi_eta = somm["two_pi_eta"]

    sig = float(sigma_barn)
    e_cm = float(E_cm_keV)

    # S(E) in keV * b
    # Use log to prevent numerical overflow in exp(2*pi*eta)
    log_s = np.log(max(1e-300, sig * e_cm)) + two_pi_eta
    if log_s > 600.0:
        s_keV_b = float("inf")
    else:
        s_keV_b = np.exp(log_s)

    s_MeV_b = s_keV_b / 1000.0

    return {
        "E_cm_keV": e_cm,
        "sigma_barn": sig,
        "sommerfeld_eta": somm["sommerfeld_eta"],
        "S_factor_keV_b": float(s_keV_b),
        "S_factor_MeV_b": float(s_MeV_b)
    }


def calculate_nonresonant_reaction_rate(T9, S0_keV_b, Z1, A1, Z2, A2):
    """
    Compute non-resonant thermonuclear reaction rate N_A <sigma v> in cm^3 / (mol * s):
      N_A <sigma v> = 7.83e9 * (Z1*Z2 / A_red)^(1/3) * T9^(-2/3) * S_0[MeV*b] * exp[ -4.248 * ((Z1^2*Z2^2*A_red)/T9)^(1/3) ].
    """
    t9 = float(T9)
    z1 = float(Z1)
    z2 = float(Z2)
    a1 = float(A1)
    a2 = float(A2)
    a_red = (a1 * a2) / (a1 + a2)

    # S0 in MeV * b
    s0_MeV_b = float(S0_keV_b) / 1000.0

    factor = (z1 ** 2) * (z2 ** 2) * a_red
    exponent = - 4.248 * ((factor / t9) ** (1.0 / 3.0))

    if exponent < -200.0:
        rate = 0.0
    else:
        prefactor = 7.83e9 * ((z1 * z2 / a_red) ** (1.0 / 3.0)) * (t9 ** (-2.0 / 3.0)) * s0_MeV_b
        rate = prefactor * np.exp(exponent)

    return {
        "T9": t9,
        "S0_keV_b": float(S0_keV_b),
        "S0_MeV_b": float(s0_MeV_b),
        "reaction_rate_cm3_mol_s": float(rate)
    }


def calculate_resonant_reaction_rate(T9, omega_gamma_eV, E_res_keV, A1, A2):
    """
    Compute narrow Breit-Wigner single-resonance reaction rate N_A <sigma v> in cm^3 / (mol * s):
      N_A <sigma v>_res = 1.539e11 * (A_red * T9)^(-3/2) * (omega*gamma)[MeV] * exp[ -11.605 * E_r[MeV] / T9 ].
    """
    t9 = float(T9)
    er_MeV = float(E_res_keV) / 1000.0
    wg_MeV = float(omega_gamma_eV) * 1e-6
    a_red = (float(A1) * float(A2)) / (float(A1) + float(A2))

    exponent = - 11.605 * er_MeV / t9

    if exponent < -200.0:
        rate = 0.0
    else:
        prefactor = 1.539e11 * ((a_red * t9) ** (-1.5)) * wg_MeV
        rate = prefactor * np.exp(exponent)

    return {
        "T9": t9,
        "omega_gamma_eV": float(omega_gamma_eV),
        "E_res_keV": float(E_res_keV),
        "E_res_MeV": float(er_MeV),
        "resonant_rate_cm3_mol_s": float(rate)
    }
