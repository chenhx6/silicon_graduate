#!/usr/bin/env python3
"""
Proton Drip-Line Radioactivity, True Two-Proton Decay & Cluster Radioactivity Calculator.

Based on:
  - V. I. Goldanskii, Nucl. Phys. 19, 482 (1960) (Two-proton radioactivity hypothesis)
  - M. Pfutzner et al., Rev. Mod. Phys. 84, 567 (2012) (Radioactive decays at limits of stability)
  - H. J. Rose & G. A. Jones, Nature 307, 245 (1984) (Discovery of 14C cluster radioactivity)
  - B. Dey et al., Phys. Rev. Lett. (2026) (116Cs multifaceted decay near proton drip line)
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions, Ch. 4-5

Features:
  1. Computes single-proton decay WKB barrier penetration half-life across Coulomb + centrifugal barrier.
  2. Evaluates the Goldanskii true two-proton condition (S_p > 0 and S_2p < 0 / Q_2p > 0 and Q_1p < 0).
  3. Models two-proton energy sharing distribution (Jacobi coordinates) distinguishing simultaneous vs sequential decay.
  4. Calculates WKB Gamow tunneling probabilities and partial lifetimes for heavy cluster radioactivity (e.g. 14C, 20O, 24Ne).
  5. Diagnoses competition between proton emission, 2p decay, alpha decay, and beta+/EC decay near the drip line.
"""

import numpy as np

# Physical constants
HBAR_C_MEV_FM = 197.3269804   # MeV * fm
E2_CONST_MEV_FM = 1.439965    # e^2 in MeV * fm
M_PROTON_MEV = 938.272088     # MeV / c^2
AMU_MEV = 931.49410242        # MeV / c^2


def calculate_proton_decay_wkb_lifetime(Q_p_MeV, l_orbital, Z_daughter, A_daughter, r0_fm=1.2, assault_nu0=1e21):
    """
    Calculate single-proton WKB tunneling penetration factor and partial half-life:
      V(r) = (Z_d * e^2) / r + [l(l+1) * (hbar*c)^2] / [2 * mu * c^2 * r^2].
    """
    qp = float(Q_p_MeV)
    l_val = float(l_orbital)
    zd = float(Z_daughter)
    ad = float(A_daughter)

    if qp <= 0:
        return {
            "Q_p_MeV": qp,
            "is_energetically_allowed": False,
            "T12_s": float("inf"),
            "diagnosis": "Sub-threshold: Q_p <= 0 (Proton bound against decay)"
        }

    # Reduced mass in MeV / c^2
    mu_c2 = (1.007825 * ad) / (1.007825 + ad) * AMU_MEV

    # Inner turning point
    r_in = float(r0_fm) * (ad ** (1.0 / 3.0))

    # Centrifugal factor
    cent_c2 = (HBAR_C_MEV_FM ** 2) * l_val * (l_val + 1.0) / (2.0 * mu_c2)

    # Outer turning point: solve qp * r^2 - E2*Zd * r - cent_c2 = 0
    b_quad = - E2_CONST_MEV_FM * zd
    r_out = (-b_quad + np.sqrt(b_quad ** 2 + 4.0 * qp * cent_c2)) / (2.0 * qp)

    if r_out <= r_in:
        # Tunneling not required (above barrier)
        return {
            "Q_p_MeV": qp,
            "is_energetically_allowed": True,
            "T12_s": 1e-21,
            "penetration_factor_P": 1.0,
            "diagnosis": "Above-barrier prompt proton emission (T1/2 ~ 10^-21 s)"
        }

    # WKB integral
    r_pts = np.linspace(r_in, r_out, 300)
    v_eff = (E2_CONST_MEV_FM * zd / r_pts) + (cent_c2 / (r_pts ** 2))
    integrand = np.sqrt(np.maximum(0.0, 2.0 * mu_c2 * (v_eff - qp)))

    # Use trapezoid compatible with all numpy versions
    trapezoid_func = getattr(np, 'trapezoid', getattr(np, 'trapz', None))
    g_integral = trapezoid_func(integrand, r_pts) / HBAR_C_MEV_FM
    p_wkb = np.exp(-2.0 * g_integral)

    # Decay half-life T1/2 = ln(2) / (nu_0 * P)
    t12_s = np.log(2.0) / max(1e-300, float(assault_nu0) * p_wkb)

    return {
        "Q_p_MeV": qp,
        "l_orbital": int(l_val),
        "Z_daughter": int(zd),
        "A_daughter": int(ad),
        "R_in_fm": float(r_in),
        "R_out_fm": float(r_out),
        "Gamow_integral_G": float(g_integral),
        "penetration_factor_P": float(p_wkb),
        "T12_s": float(t12_s),
        "is_energetically_allowed": True,
        "diagnosis": f"WKB Calculated proton decay half-life: T1/2 = {t12_s:.3e} s"
    }


def check_goldanskii_true_2p_condition(Q_2p_MeV, S_p_MeV):
    """
    Check the Goldanskii (1960) condition for true simultaneous two-proton radioactivity:
      1. Q_2p > 0 (Two-proton emission is energetically allowed)
      2. S_p > 0  (Single-proton emission is energetically forbidden / sub-threshold)
    """
    q2p = float(Q_2p_MeV)
    sp = float(S_p_MeV)
    q1p = - sp

    if q2p > 0.0 and sp > 0.0:
        is_true_2p = True
        diag = (f"Goldanskii True 2p Condition Satisfied: Q_2p = {q2p:.3f} MeV > 0, "
                f"while intermediate 1p emission is sub-threshold (S_p = {sp:.3f} MeV > 0, Q_1p = {q1p:.3f} MeV < 0). "
                f"Decay proceeds via true three-body continuum tunneling.")
    elif q2p > 0.0 and sp <= 0.0:
        is_true_2p = False
        diag = (f"Sequential 2p Emission Allowed: Q_2p = {q2p:.3f} MeV > 0 and 1p channel is open (S_p = {sp:.3f} MeV <= 0). "
                f"Decay proceeds via sequential one-proton steps or broad democratic resonance.")
    else:
        is_true_2p = False
        diag = f"2p Emission Forbidden: Q_2p = {q2p:.3f} MeV <= 0 (2p bound)."

    return {
        "Q_2p_MeV": q2p,
        "S_p_MeV": sp,
        "Q_1p_MeV": q1p,
        "is_true_two_proton_decay": is_true_2p,
        "diagnosis": diag
    }


def model_two_proton_jacobi_distribution(Q_2p_MeV, mode="simultaneous"):
    """
    Model the two-proton energy sharing distribution epsilon = E_p1 / Q_2p:
      Simultaneous (true 2p): bell-shaped distribution peaking at epsilon = 0.5 (equal sharing).
      Sequential: discrete delta-like or narrow Breit-Wigner peaks at Q_1p and Q_2p - Q_1p.
    """
    eps = np.linspace(0.05, 0.95, 50)
    q = float(Q_2p_MeV)

    if mode == "simultaneous":
        # Broad 3-body phase space modified by Coulomb: approx sin^2(pi * eps)
        prob = np.sin(np.pi * eps) ** 2
        prob /= np.sum(prob)
        peak_energy_p1 = q * 0.5
        peak_energy_p2 = q * 0.5
    else:
        # Sequential peak near 0.2 and 0.8
        prob = np.exp(-((eps - 0.25) ** 2) / 0.005) + np.exp(-((eps - 0.75) ** 2) / 0.005)
        prob /= np.sum(prob)
        peak_energy_p1 = q * 0.25
        peak_energy_p2 = q * 0.75

    return {
        "mode": mode,
        "Q_2p_MeV": q,
        "epsilon_grid": eps.tolist(),
        "probability_density": prob.tolist(),
        "peak_energy_p1_MeV": float(peak_energy_p1),
        "peak_energy_p2_MeV": float(peak_energy_p2)
    }


def calculate_cluster_radioactivity_wkb(Q_c_MeV, A_c, Z_c, A_d, Z_d, r0_fm=1.2, P_preformation=1e-9, assault_nu0=1e21):
    """
    Calculate WKB penetration probability and partial half-life for heavy cluster radioactivity
    (e.g. 14C decay from 223Ra into 209Pb):
      G_cluster = (sqrt(2*mu*c^2) / hbar*c) * [1.44*Zc*Zd / sqrt(Qc)] * [ arccos(sqrt(x)) - sqrt(x*(1-x)) ]
      where x = R_in / R_out.
    """
    qc = float(Q_c_MeV)
    ac = float(A_c)
    zc = float(Z_c)
    ad = float(A_d)
    zd = float(Z_d)

    if qc <= 0:
        raise ValueError("Cluster decay Q-value must be strictly positive.")

    mu_c2 = (ac * ad) / (ac + ad) * AMU_MEV
    r_in = float(r0_fm) * ((ac ** (1.0 / 3.0)) + (ad ** (1.0 / 3.0)))
    r_out = (E2_CONST_MEV_FM * zc * zd) / qc

    if r_out <= r_in:
        return {"T12_s": 1e-21, "diagnosis": "Above barrier cluster emission."}

    x = r_in / r_out
    # Analytical Gamow integral for pure Coulomb potential
    g_integral = (np.sqrt(2.0 * mu_c2) / HBAR_C_MEV_FM) * ((E2_CONST_MEV_FM * zc * zd) / np.sqrt(qc)) * (np.arccos(np.sqrt(x)) - np.sqrt(x * (1.0 - x)))
    p_wkb = np.exp(-2.0 * g_integral)

    p_pref = float(P_preformation)
    nu0 = float(assault_nu0)
    lambda_c = nu0 * p_pref * p_wkb
    t12_s = np.log(2.0) / max(1e-300, lambda_c)
    t12_years = t12_s / (365.25 * 24.0 * 3600.0)

    return {
        "cluster_nucleus": f"{int(ac)}Z({int(zc)})",
        "daughter_nucleus": f"{int(ad)}Z({int(zd)})",
        "Q_c_MeV": qc,
        "R_in_fm": float(r_in),
        "R_out_fm": float(r_out),
        "Gamow_factor_G": float(g_integral),
        "P_WKB": float(p_wkb),
        "P_preformation": p_pref,
        "T12_s": float(t12_s),
        "T12_years": float(t12_years)
    }


def diagnose_drip_line_decay_competition(T12_p_s=None, T12_2p_s=None, T12_beta_s=None, T12_alpha_s=None):
    """
    Diagnose dominant decay mode among competing channels:
      p-emission, 2p-emission, beta+/EC, and alpha decay.
    """
    channels = {}
    if T12_p_s is not None and T12_p_s > 0:
        channels["1p_emission"] = float(T12_p_s)
    if T12_2p_s is not None and T12_2p_s > 0:
        channels["2p_emission"] = float(T12_2p_s)
    if T12_beta_s is not None and T12_beta_s > 0:
        channels["beta_plus_EC"] = float(T12_beta_s)
    if T12_alpha_s is not None and T12_alpha_s > 0:
        channels["alpha_decay"] = float(T12_alpha_s)

    if len(channels) == 0:
        return {"dominant_channel": "Unknown", "diagnosis": "No valid half-lives provided."}

    # Partial decay rates: lambda_i = ln(2) / T12_i
    rates = {name: np.log(2.0) / t for name, t in channels.items()}
    total_rate = sum(rates.values())

    branchings = {name: (r / total_rate) * 100.0 for name, r in rates.items()}
    dominant = max(branchings, key=branchings.get)

    total_T12_s = np.log(2.0) / total_rate

    return {
        "total_half_life_s": float(total_T12_s),
        "dominant_channel": dominant,
        "dominant_branching_percent": float(branchings[dominant]),
        "all_branching_percentages": branchings
    }
