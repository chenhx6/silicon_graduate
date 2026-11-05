#!/usr/bin/env python3
"""
beta_decay_log_ft_phase_space_calculator.py
===========================================
Beta Decay Phase Space Factor f(Z, Q), Comparative Half-Life log(ft) &
Transition Selection Rule Classifier.

Physics & Formulation:
----------------------
1. Relativistic Phase Space Factor f(Z, W_0):
   Total endpoint energy in electron mass units:
     W_0 = 1.0 + Q_beta / (m_e * c^2)   (m_e * c^2 = 0.5109989 MeV)
   Integration:
     f = integral_{1}^{W_0} p * W * (W_0 - W)^2 * F(Z, W) dW
   where p = sqrt(W^2 - 1).

2. Relativistic Fermi Function F(Z, W):
   F(Z, W) = 2 * (1 + gamma_D) * (2*p*R)^(2*gamma_D - 2) * exp(pi * eta) * |Gamma(gamma_D + i*eta)|^2 / [Gamma(2*gamma_D + 1)]^2
   where:
     gamma_D = sqrt(1 - (alpha * Z)^2)
     eta = +/- alpha * Z * W / p   (+ for beta^-, - for beta^+)
     R = 1.2 * A^(1/3) * (m_e * c / hbar) ~ 0.0031 * A^(1/3)

3. Comparative Half-Life (ft value):
   Partial half-life: t_12_sec = T_12_sec / Branching_Ratio
   ft = f * t_12_sec
   log_ft = log10(ft)

4. Transition Selection Rule Classification:
   - Superallowed 0+ -> 0+ (pure Fermi): Delta_I = 0, Delta_pi = no, log_ft ~ 3.48 - 3.50 (CVC test, V_ud).
   - Allowed (Gamow-Teller / Fermi): Delta_I = 0, 1 (no 0->0), Delta_pi = no, log_ft ~ 4.0 - 6.0.
   - First-Forbidden Non-Unique: Delta_I = 0, 1, Delta_pi = yes, log_ft ~ 6.0 - 9.0.
   - First-Forbidden Unique: Delta_I = 2, Delta_pi = yes, log_ft ~ 8.5 - 10.5.
   - Second-Forbidden: Delta_I = 2, Delta_pi = no, log_ft ~ 11.0 - 14.0.
   - Third-Forbidden: Delta_I = 3, Delta_pi = yes, log_ft ~ 15.0 - 21.0 (e.g. 40K, 115In).

References:
  - 卢希庭, 《原子核物理（修订版）》, 第6章 Beta衰变.
  - J. C. Hardy and I. S. Towner, Phys. Rev. C 102, 045501 (2020).
  - N. B. Gove and M. J. Martin, Nucl. Data Tables 10, 205 (1971).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

M_E_C2_MEV = 0.51099895
ALPHA_QED = 1.0 / 137.035999


def relativistic_fermi_function(Z_daughter: int, W: float, A: int, decay_mode: str = "beta_minus") -> float:
    """
    Computes relativistic Fermi function F(Z, W) for electron (beta-) or positron (beta+).
    """
    if W <= 1.0001:
        W = 1.0001
    p = math.sqrt(W ** 2 - 1.0)

    # Sign of eta: + for beta-, - for beta+
    sign = +1.0 if decay_mode == "beta_minus" else -1.0
    eta = sign * ALPHA_QED * Z_daughter * W / p

    # Relativistic gamma_D = sqrt(1 - (alpha*Z)^2)
    az = ALPHA_QED * Z_daughter
    gamma_d = math.sqrt(max(1.0 - az ** 2, 0.1))

    # Primakoff-Rosen relativistic Coulomb factor
    if abs(eta) < 1e-4:
        coul = 1.0
    else:
        twopi_eta = 2.0 * math.pi * eta
        if twopi_eta > 100.0:
            coul = twopi_eta
        elif twopi_eta < -100.0:
            coul = 0.0
        else:
            coul = twopi_eta / (1.0 - math.exp(-twopi_eta))

    # Finite nuclear size radius R in Compton wavelengths
    R_c = 0.0031 * (A ** (1.0 / 3.0))
    # Radius correction factor: (2 * p * R_c)^(2*gamma_d - 2)
    rad_factor = (2.0 * p * R_c) ** (2.0 * gamma_d - 2.0)

    f_val = coul * rad_factor
    return max(f_val, 1e-4)


def integrate_phase_space_f(
    Z_daughter: int,
    A: int,
    Q_beta_MeV: float,
    decay_mode: str = "beta_minus",
    steps: int = 500
) -> float:
    """
    Integrates f = integral_{1}^{W_0} p * W * (W_0 - W)^2 * F(Z, W) dW.
    """
    W_0 = 1.0 + (Q_beta_MeV / M_E_C2_MEV)
    if W_0 <= 1.005:
        return 1e-12

    dW = (W_0 - 1.0) / float(steps)
    f_integral = 0.0

    for i in range(1, steps):
        W = 1.0 + i * dW
        p = math.sqrt(W ** 2 - 1.0)
        q = W_0 - W
        F_val = relativistic_fermi_function(Z_daughter, W, A, decay_mode)

        # Simpson/Trapezoidal integration
        weight = 2.0 if (i % 2 == 0) else 4.0
        term = p * W * (q ** 2) * F_val
        f_integral += weight * term

    f_integral = (dW / 3.0) * f_integral
    return max(f_integral, 1e-12)


def calculate_log_ft(
    Q_beta_MeV: float,
    half_life_sec: float,
    Z_daughter: int,
    A: int,
    branching_ratio: float = 1.0,
    decay_mode: str = "beta_minus"
) -> Dict[str, Any]:
    """
    Calculates phase space factor f, partial half life, ft value, and log10(ft).
    """
    br = max(min(branching_ratio, 1.0), 1e-6)
    t_partial = half_life_sec / br

    f_factor = integrate_phase_space_f(Z_daughter, A, Q_beta_MeV, decay_mode)
    ft = f_factor * t_partial
    log_ft = math.log10(max(ft, 1e-12))

    # Classification based on log ft
    if log_ft < 3.8:
        classification = "Superallowed (0+ -> 0+ pure Fermi or mirror allowed)"
    elif log_ft <= 5.9:
        classification = "Allowed (Gamow-Teller / Fermi, Delta_I = 0, 1, Delta_pi = no)"
    elif log_ft <= 8.5:
        classification = "First-Forbidden Non-Unique (Delta_I = 0, 1, Delta_pi = yes)"
    elif log_ft <= 10.5:
        classification = "First-Forbidden Unique (Delta_I = 2, Delta_pi = yes)"
    elif log_ft <= 14.0:
        classification = "Second-Forbidden (Delta_I = 2, Delta_pi = no)"
    else:
        classification = "Third-Forbidden or Highly Retarded (Delta_I = 3, Delta_pi = yes)"

    return {
        "Q_beta_MeV": Q_beta_MeV,
        "half_life_sec": half_life_sec,
        "branching_ratio": br,
        "partial_half_life_sec": round(t_partial, 4),
        "Z_daughter": Z_daughter,
        "A": A,
        "decay_mode": decay_mode,
        "phase_space_f": round(f_factor, 4),
        "log10_f": round(math.log10(max(f_factor, 1e-12)), 3),
        "ft_value_sec": round(ft, 2),
        "log10_ft": round(log_ft, 3),
        "forbiddenness_classification": classification
    }


def verify_superallowed_cvc_vud(
    ft_value: float,
    delta_R_prime: float = 0.0149,
    delta_C: float = 0.0035,
    delta_NS: float = -0.0020
) -> Dict[str, Any]:
    """
    Evaluates corrected Ft value and tests CKM unitarity V_ud matrix element
    for superallowed 0+ -> 0+ Fermi decays (Towner & Hardy 2020).
    Ft = ft * (1 + delta_R') * (1 - (delta_C - delta_NS))
    """
    Ft = ft_value * (1.0 + delta_R_prime) * (1.0 - (delta_C - delta_NS))

    # Fundamental constants
    K_over_2Gf2 = 2984.48  # Hardy & Towner universal Fermi constant in seconds
    delta_R_V = 0.02454     # Inner radiative correction

    # V_ud^2 = K / [2 * G_F^2 * (1 + delta_R_V) * Ft]
    denom = (1.0 + delta_R_V) * Ft
    V_ud_sq = K_over_2Gf2 / denom
    V_ud = math.sqrt(max(V_ud_sq, 0.0))

    # CKM First Row Unitarity: |V_ud|^2 + |V_us|^2 + |V_ub|^2 ~ 1
    # Standard PDG V_us = 0.2245, V_ub = 0.00382
    V_us = 0.2245
    V_ub = 0.00382
    unitarity_sum = (V_ud ** 2) + (V_us ** 2) + (V_ub ** 2)

    return {
        "uncorrected_ft_sec": round(ft_value, 2),
        "corrected_Ft_sec": round(Ft, 2),
        "extracted_V_ud": round(V_ud, 5),
        "V_ud_standard_reference": 0.97373,
        "ckm_first_row_unitarity_sum": round(unitarity_sum, 5),
        "unitarity_deviation": round(unitarity_sum - 1.0, 5),
        "cvc_hypothesis_status": "CONDITIONAL COMPATIBILITY (Ft near the reference ~3072 s)" if abs(Ft - 3072.0) < 20.0 else "Deviation detected"
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   BETA DECAY PHASE SPACE, LOG(FT) & FORBIDDENNESS CLASSIFIER")
    lines.append("=" * 72)

    lf = summary["log_ft"]
    lines.append(f" TRANSITION PARAMETERS (Mode: {lf['decay_mode']}, A={lf['A']}, Z_d={lf['Z_daughter']}):")
    lines.append(f"   Decay Energy Q_beta            : {lf['Q_beta_MeV']} MeV")
    lines.append(f"   Total Half-Life                : {lf['half_life_sec']:.3e} s (BR = {lf['branching_ratio']*100:.1f}%)")
    lines.append(f"   Partial Half-Life t_1/2        : {lf['partial_half_life_sec']:.3e} s")
    lines.append(f"   Phase Space Factor f           : {lf['phase_space_f']:.4e} (log10(f) = {lf['log10_f']})")
    lines.append(f"   Comparative Lifetime ft        : {lf['ft_value_sec']:.2e} s")
    lines.append(f"   Log(ft) Value                  : {lf['log10_ft']}")
    lines.append(f"   Classification                 : {lf['forbiddenness_classification']}")
    lines.append("-" * 72)

    if "cvc_audit" in summary:
        cvc = summary["cvc_audit"]
        lines.append(" SUPERALLOWED 0+ -> 0+ FERMI DECAY & CKM V_ud AUDIT:")
        lines.append(f"   Corrected Ft Value             : {cvc['corrected_Ft_sec']} s")
        lines.append(f"   Extracted CKM Element |V_ud|   : {cvc['extracted_V_ud']} (Ref: {cvc['V_ud_standard_reference']})")
        lines.append(f"   CKM First Row Unitarity Sum    : {cvc['ckm_first_row_unitarity_sum']} (Dev: {cvc['unitarity_deviation']:+.5f})")
        lines.append(f"   CVC Hypothesis Status          : {cvc['cvc_hypothesis_status']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - log(ft) is independent of decay energy and isolates transition matrix element.")
    lines.append("   - Superallowed 0+ -> 0+ provides the most precise test of CKM unitarity.")
    lines.append("   - Allowed vs forbidden classification guides spin-parity assignments.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Beta Decay Phase Space f(Z,Q), Log(ft) & Forbiddenness Classifier."
    )
    parser.add_argument("-Q", "--q-beta", type=float, required=True, help="Beta decay Q-value in MeV")
    parser.add_argument("-T", "--t12", type=float, required=True, help="Total half-life in seconds")
    parser.add_argument("-Z", "--zdaughter", type=int, required=True, help="Daughter atomic number Z_daughter")
    parser.add_argument("-A", "--mass", type=int, required=True, help="Mass number A")
    parser.add_argument("--br", type=float, default=1.0, help="Branching ratio (default: 1.0)")
    parser.add_argument("--mode", type=str, default="beta_minus", choices=["beta_minus", "beta_plus"],
                        help="Decay mode: beta_minus or beta_plus")
    parser.add_argument("--cvc-check", action="store_true", help="Perform superallowed 0+->0+ CVC & V_ud audit")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    res = calculate_log_ft(args.q_beta, args.t12, args.zdaughter, args.mass, args.br, args.mode)
    summary = {"log_ft": res}

    if args.cvc_check or res["log10_ft"] < 3.8:
        cvc = verify_superallowed_cvc_vud(res["ft_value_sec"])
        summary["cvc_audit"] = cvc

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
