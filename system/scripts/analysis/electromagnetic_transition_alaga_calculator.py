#!/usr/bin/env python3
"""
Nuclear Electromagnetic Transition Rates, Weisskopf Units & Alaga Rules Calculator.

Based on:
  - V. F. Weisskopf, Phys. Rev. 83, 1073 (1951) (Single-particle transition probabilities)
  - G. Alaga, K. Alder, A. Bohr, B. R. Mottelson, K. Dan. Vidensk. Selsk. Mat. Fys. Medd. 29, 1 (1955) (Alaga rules)
  - A. Bohr & B. R. Mottelson, Nuclear Structure Vol. I (Ch. 3) & Vol. II (Ch. 4)
  - W. D. Hamilton, The Electromagnetic Interaction in Nuclear Spectroscopy, Ch. 1-2

Features:
  1. Computes single-particle Weisskopf units (W.u.) for E1, E2, E3, M1, M2 transitions.
  2. Converts experimental level lifetimes (in ps or ns) to absolute B(E2), B(M1) and W.u.
  3. Tests rotational band Alaga branching rules against Clebsch-Gordan theoretical predictions.
  4. Inverts experimental in-band cascade intensity ratios to B(M1)/B(E2) in mu_N^2 / (e^2 b^2).
  5. Extracts the intrinsic structure parameter |g_K - g_R| / Q_0 from B(M1)/B(E2) ratios.
"""

import numpy as np


def calculate_weisskopf_unit(A, multipolarity="E2"):
    """
    Calculate Weisskopf single-particle reduced transition probability B_sp(sigma lambda):
      E1: 0.06446 * A^(2/3) e^2 fm^2
      E2: 0.05940 * A^(4/3) e^2 fm^4 (or * 1e-4 e^2 b^2)
      E3: 0.05940 * A^(2)   e^2 fm^6
      M1: 1.7905 mu_N^2
      M2: 1.6501 * A^(2/3) mu_N^2 fm^2
    """
    a_f = float(A)
    mult = multipolarity.upper()

    if mult == "E1":
        b_sp = 0.06446 * (a_f ** (2.0 / 3.0))
        unit_str = "e^2 fm^2"
        rate_factor = 1.587e15 # s^-1 * MeV^-3 * (e^2 fm^2)^-1
        energy_power = 3
    elif mult == "E2":
        b_sp = 0.05940 * (a_f ** (4.0 / 3.0))
        unit_str = "e^2 fm^4"
        rate_factor = 1.225e9  # s^-1 * MeV^-5 * (e^2 fm^4)^-1
        energy_power = 5
    elif mult == "E3":
        b_sp = 0.05940 * (a_f ** 2.0)
        unit_str = "e^2 fm^6"
        rate_factor = 5.709e2  # s^-1 * MeV^-7 * (e^2 fm^6)^-1
        energy_power = 7
    elif mult == "M1":
        b_sp = 1.7905
        unit_str = "mu_N^2"
        rate_factor = 1.758e13 # s^-1 * MeV^-3 * mu_N^-2
        energy_power = 3
    elif mult == "M2":
        b_sp = 1.6501 * (a_f ** (2.0 / 3.0))
        unit_str = "mu_N^2 fm^2"
        rate_factor = 1.350e7  # s^-1 * MeV^-5 * (mu_N^2 fm^2)^-1
        energy_power = 5
    else:
        raise ValueError(f"Unsupported multipolarity {multipolarity}. Choose from E1, E2, E3, M1, M2.")

    return {
        "A": int(A),
        "multipolarity": mult,
        "B_sp_value": float(b_sp),
        "unit": unit_str,
        "transition_rate_factor": float(rate_factor),
        "energy_power": energy_power
    }


def convert_lifetime_to_b_e2(tau_ps, E_gamma_keV, A, branch_fraction=1.0, alpha_icc=0.0):
    """
    Convert experimental excited level lifetime tau (in ps) to reduced transition probability B(E2):
      tau_gamma = tau * (1 + alpha_icc) / branch_fraction
      T_gamma = 1 / tau_gamma
      B(E2) [e^2 fm^4] = T_gamma / [1.225e9 * (E_gamma_MeV)^5]
      B(E2) [e^2 b^2]  = B(E2) [e^2 fm^4] * 1e-4
      B(E2) [W.u.]     = B(E2) [e^2 fm^4] / B_sp(E2)
    """
    if tau_ps <= 0 or E_gamma_keV <= 0:
        raise ValueError("Lifetime and gamma energy must be strictly positive.")

    tau_gamma_s = float(tau_ps) * 1e-12 * (1.0 + float(alpha_icc)) / float(branch_fraction)
    t_gamma_rate = 1.0 / tau_gamma_s
    eg_MeV = float(E_gamma_keV) / 1000.0

    b_e2_fm4 = t_gamma_rate / (1.225e9 * (eg_MeV ** 5))
    b_e2_b2 = b_e2_fm4 * 1e-4

    wu_info = calculate_weisskopf_unit(A, multipolarity="E2")
    b_e2_wu = b_e2_fm4 / wu_info["B_sp_value"]

    # Inferred intrinsic quadrupole moment Q_0 for K=0 band: B(E2; 2+ -> 0+) = (5 / 16pi) * e^2 * Q0^2
    q0_eb = np.sqrt((16.0 * np.pi / 5.0) * b_e2_b2)

    return {
        "tau_ps": float(tau_ps),
        "E_gamma_keV": float(E_gamma_keV),
        "A": int(A),
        "B_E2_e2fm4": float(b_e2_fm4),
        "B_E2_e2b2": float(b_e2_b2),
        "B_E2_W_u": float(b_e2_wu),
        "Q0_intrinsic_eb": float(q0_eb)
    }


def calculate_alaga_ratio_e2(I_initial, K_band=0.0):
    """
    Calculate theoretical Alaga ratio B(E2; I -> I-2) / B(E2; 2+ -> 0+) for axial rotor:
    For K=0 ground state band:
      R_Alaga = (15/2) * [ I*(I-1) / ((2I-1)*(2I+1)) ].
    """
    spin = float(I_initial)
    if spin < 2.0:
        raise ValueError("Initial spin must be at least 2.")

    if abs(K_band) < 1e-5:
        # K=0 ground state band
        r_alaga = (15.0 / 2.0) * (spin * (spin - 1.0)) / ((2.0 * spin - 1.0) * (2.0 * spin + 1.0))
    else:
        # Generic K Clebsch-Gordan ratio
        # <I K 2 0 | I-2 K>^2 / <2 K 2 0 | 0 K>^2
        # Simplified approximate rotor scaling
        r_alaga = (spin * (spin - 1.0)) / ((spin + 1.0) * (spin + 2.0))

    return {
        "I_initial": spin,
        "K_band": float(K_band),
        "alaga_ratio_to_2_0": float(r_alaga)
    }


def calculate_bm1_over_be2(E_gamma_dI1_keV, E_gamma_dI2_keV, I_gamma_dI1, I_gamma_dI2, delta_mixing=0.0, spin_I=None, K_val=None):
    """
    Invert in-band branching ratio to reduced transition probability ratio B(M1)/B(E2):
      B(M1; I -> I-1) / B(E2; I -> I-2) = 0.697 * (E_gamma_dI2^5 / E_gamma_dI1^3) * (I_dI1 / I_dI2) * [1 / (1 + delta^2)]
      in units of mu_N^2 / (e^2 b^2).
    If spin I and K are provided, extracts |g_K - g_R| / Q_0:
      |g_K - g_R| / Q_0 = sqrt[ (5/12) * ((I^2 - 1) / K^2) * (B(M1)/B(E2)) ] in mu_N / (e b).
    """
    if E_gamma_dI1_keV <= 0 or E_gamma_dI2_keV <= 0 or I_gamma_dI2 <= 0:
        raise ValueError("Energies and cross-over intensity must be strictly positive.")

    e1_MeV = float(E_gamma_dI1_keV) / 1000.0
    e2_MeV = float(E_gamma_dI2_keV) / 1000.0
    delta_sq = float(delta_mixing) ** 2

    # Ratio in mu_N^2 / (e^2 b^2)
    ratio_bm1_be2 = 0.697 * ((e2_MeV ** 5) / (e1_MeV ** 3)) * (float(I_gamma_dI1) / float(I_gamma_dI2)) * (1.0 / (1.0 + delta_sq))

    result = {
        "E_gamma_dI1_keV": float(E_gamma_dI1_keV),
        "E_gamma_dI2_keV": float(E_gamma_dI2_keV),
        "I_gamma_dI1": float(I_gamma_dI1),
        "I_gamma_dI2": float(I_gamma_dI2),
        "delta_mixing": float(delta_mixing),
        "B_M1_over_B_E2_muN2_e2b2": float(ratio_bm1_be2)
    }

    if spin_I is not None and K_val is not None:
        i_f = float(spin_I)
        k_f = float(K_val)
        if k_f > 0.1 and i_f > 1.0:
            gk_gr_over_q0 = np.sqrt((5.0 / 12.0) * ((i_f ** 2 - 1.0) / (k_f ** 2)) * ratio_bm1_be2)
            result["spin_I"] = i_f
            result["K_val"] = k_f
            result["abs_gK_minus_gR_over_Q0_muN_eb"] = float(gk_gr_over_q0)

    return result
