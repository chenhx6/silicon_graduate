#!/usr/bin/env python3
"""
Gamow-Teller Resonance (GTGR), Ikeda Sum Rule & g_A Quenching Calculator.

Based on:
  - K. Ikeda et al., Phys. Lett. 3, 271 (1963) (Model-independent sum rule: S_- - S_+ = 3(N-Z))
  - F. Osterfeld, Rev. Mod. Phys. 64, 861 (1992) (Nuclear spin-isospin excitations & charge exchange)
  - A. Bohr & B. R. Mottelson, Nuclear Structure Vol. I, Ch. 3 (Isovector & Gamow-Teller modes)
  - H. Ejiri, J. Suhonen, K. Zuber, Phys. Rep. 797, 1 (2019) (g_A quenching in 0nu beta beta decay)

Features:
  1. Computes exact model-independent Ikeda sum rule theoretical value: S_Ikeda = 3(N - Z).
  2. Evaluates Gamow-Teller strength recovery fraction and quenching factor q = sqrt(S_exp / S_theo).
  3. Reconstructs effective axial-vector weak coupling constant g_A^eff in nuclear medium.
  4. Calculates neutrinoless double beta decay (0nu beta beta) half-life prolongation factor ~ 1/q^4.
  5. Converts forward-angle (theta = 0 deg) charge-exchange differential cross section to B(GT).
"""

import numpy as np


def calculate_ikeda_sum_rule(Z, A):
    """
    Compute theoretical Ikeda sum rule limit: S_- - S_+ = 3 * (N - Z).
    """
    N = A - Z
    if N < Z:
        # Proton-rich nuclei where N < Z
        ikeda_val = 3.0 * (N - Z)
    else:
        ikeda_val = 3.0 * (N - Z)
    return {
        "Z": int(Z),
        "A": int(A),
        "N": int(N),
        "N_minus_Z": int(N - Z),
        "ikeda_sum_rule_limit": float(ikeda_val)
    }


def evaluate_ga_quenching(Z, A, S_minus_exp, S_plus_exp=0.0, g_a_free=1.2754):
    """
    Evaluate Gamow-Teller strength recovery fraction, quenching factor q,
    effective g_A, and 0nu beta beta half-life prolongation ratio.
    """
    ikeda_info = calculate_ikeda_sum_rule(Z, A)
    s_ikeda = ikeda_info["ikeda_sum_rule_limit"]
    s_exp_net = float(S_minus_exp - S_plus_exp)

    if s_ikeda <= 0:
        raise ValueError(f"Ikeda sum rule theoretical value <= 0 for Z={Z}, A={A} (N <= Z).")

    recovery_fraction = s_exp_net / s_ikeda
    # Quenching factor q = sqrt(S_exp / S_theo)
    q = np.sqrt(max(0.0, recovery_fraction))
    g_a_eff = q * g_a_free

    # 0nu beta beta half life is inversely proportional to (g_A^eff)^4
    # Prolongation factor R = (g_A_free / g_A_eff)^4 = 1 / q^4
    if q > 1e-4:
        half_life_prolongation_ratio = 1.0 / (q ** 4)
    else:
        half_life_prolongation_ratio = float("inf")

    if recovery_fraction < 0.40:
        diagnosis = "Severe strength deficit (sub-threshold, potential large missing resonance strength)"
    elif recovery_fraction <= 0.65:
        diagnosis = "Canonical experimental quenching regime (Delta-isobar mixing + 2BC meson currents)"
    elif recovery_fraction <= 0.85:
        diagnosis = "Mild quenching (high-energy tail partially recovered)"
    elif recovery_fraction <= 1.05:
        diagnosis = "Full strength recovery (free nucleon limit / unquenched)"
    else:
        diagnosis = "Sum rule overshoot (check multi-step reaction background subtraction)"

    return {
        "Z": int(Z),
        "A": int(A),
        "N": int(A - Z),
        "S_minus_exp": float(S_minus_exp),
        "S_plus_exp": float(S_plus_exp),
        "S_net_exp": s_exp_net,
        "S_ikeda_theo": s_ikeda,
        "recovery_fraction": recovery_fraction,
        "quenching_factor_q": float(q),
        "g_a_free": float(g_a_free),
        "g_a_eff": float(g_a_eff),
        "0nu_half_life_prolongation": float(half_life_prolongation_ratio),
        "diagnosis": diagnosis
    }


def convert_cross_section_to_b_gt(diff_sigma_0deg_mb_sr, unit_sigma_hat_mb_sr):
    """
    Convert zero-degree forward differential cross section (dsigma/dOmega at 0 deg)
    to microscopic B(GT) using the reaction unit cross section sigma_hat:
    dsigma/dOmega(0 deg) = sigma_hat * B(GT).
    """
    if unit_sigma_hat_mb_sr <= 0:
        raise ValueError("Unit cross section sigma_hat must be strictly positive.")
    b_gt = diff_sigma_0deg_mb_sr / unit_sigma_hat_mb_sr
    return {
        "dsigma_dOmega_0deg_mb_sr": float(diff_sigma_0deg_mb_sr),
        "unit_cross_section_sigma_hat_mb_sr": float(unit_sigma_hat_mb_sr),
        "B_GT": float(b_gt)
    }
