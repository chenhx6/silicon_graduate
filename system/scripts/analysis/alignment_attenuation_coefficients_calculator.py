#!/usr/bin/env python3
"""
alignment_attenuation_coefficients_calculator.py
================================================
In-Beam Nuclear Spin Alignment Attenuation Coefficients (alpha_2, alpha_4) &
Substate Distribution sigma/I Inverter.

Physics & Formulation:
----------------------
1. Magnetic Substate Population Distribution P(m):
   In heavy-ion fusion-evaporation reactions, spin vectors are aligned perpendicular
   to the beam axis z (favoring m ~ 0):
     P(m) = (1 / (sqrt(2*pi) * sigma_m)) * exp(- m^2 / (2 * sigma_m^2))
   Dimensionless alignment width: sigma_m / I (typically 0.20 - 0.35).

2. Statistical Orientation Tensors B_k(I) & Attenuation Factors alpha_k:
   B_k(I, sigma) = sqrt(2*I + 1) * sum_m (-1)^(I - m) * <I m I -m | k 0> * P(m)
   alpha_k(I, sigma) = B_k(I, sigma) / B_k_max(I)
   Approximation (Yamazaki 1967 / Hamilton 1975):
     alpha_2 ~ exp[ - 3.0 * sigma_m^2 / (I * (I + 1)) ]
     alpha_4 ~ exp[ - 10.0 * sigma_m^2 / (I * (I + 1)) ]

3. Angular Distribution Coefficients a_k:
   a_k = alpha_k(I, sigma) * A_k_max(I, I_f, delta)
   - Complete alignment (sigma = 0): alpha_2 = alpha_4 = 1.0.
   - Complete unaligned isotropy (sigma -> inf): alpha_2 = alpha_4 = 0.0.

4. Empirical Inversion of Alignment Width sigma_m / I:
   Given measured a_2 of a known pure stretched E2 transition (I -> I - 2):
     A_2_max = F_2(I, 2, 2, I-2) * B_2_max
     alpha_2_meas = a_2_exp / A_2_max
     (sigma_m / I) = sqrt[ - ln(alpha_2_meas) * (I + 1) / (3.0 * I) ]
   Calibrates the reaction alignment to extract true mixing ratios delta for unknown transitions!

References:
  - T. Yamazaki, Nucl. Data Tables A 3, 1 (1967).
  - W. D. Hamilton, The Electromagnetic Interaction in Nuclear Spectroscopy, North-Holland (1975).
  - H. Morinaga and T. Yamazaki, In-Beam Gamma-Ray Spectroscopy, North-Holland (1976).
  - 卢希庭, 《原子核物理（修订版）》, 第5章.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_alignment_attenuation_factors(
    spin_I: float,
    sigma_over_I: float = 0.30
) -> Dict[str, float]:
    """
    Computes attenuation coefficients alpha_2 and alpha_4 for spin I.
    """
    sigma_m = max(sigma_over_I * spin_I, 0.1)

    # I * (I + 1)
    ii1 = spin_I * (spin_I + 1.0)

    # Yamazaki Gaussian approximations
    arg2 = 3.0 * (sigma_m ** 2) / max(ii1, 1.0)
    arg4 = 10.0 * (sigma_m ** 2) / max(ii1, 1.0)

    alpha_2 = math.exp(- min(arg2, 20.0))
    alpha_4 = math.exp(- min(arg4, 20.0))

    return {
        "spin_I": spin_I,
        "sigma_over_I": round(sigma_over_I, 3),
        "sigma_m_substate_width": round(sigma_m, 2),
        "alpha_2_attenuation": round(alpha_2, 4),
        "alpha_4_attenuation": round(alpha_4, 4),
        "attenuation_ratio_alpha4_over_alpha2": round(alpha_4 / max(alpha_2, 1e-4), 4)
    }


def invert_sigma_over_I_from_stretched_e2(
    a2_measured: float,
    spin_I: float = 4.0,
    a2_max_theoretical: float = 0.357
) -> Dict[str, Any]:
    """
    Inverts the physical substate alignment width (sigma_m / I) from measured a_2
    of a stretched E2 transition.
    """
    if a2_measured <= 0 or a2_measured > a2_max_theoretical * 1.05:
        return {
            "error": "Measured a_2 outside physical range for stretched E2",
            "a2_measured": a2_measured,
            "a2_max_theoretical": a2_max_theoretical
        }

    alpha_2_eff = min(a2_measured / a2_max_theoretical, 0.9999)

    # alpha_2 ~ exp(- 3.0 * sigma_m^2 / (I*(I+1)))
    # ln(alpha_2) = - 3.0 * (sigma_m/I)^2 * [ I / (I + 1) ]
    # (sigma_m / I)^2 = - ln(alpha_2) * (I + 1) / (3.0 * I)
    arg = - math.log(alpha_2_eff) * (spin_I + 1.0) / (3.0 * spin_I)
    sigma_over_i = math.sqrt(max(arg, 0.0))

    # Predict corresponding alpha_4
    att = calculate_alignment_attenuation_factors(spin_I, sigma_over_i)

    return {
        "spin_initial_I": spin_I,
        "measured_a2": a2_measured,
        "theoretical_a2_max": a2_max_theoretical,
        "extracted_alpha_2": round(alpha_2_eff, 4),
        "inverted_sigma_over_I": round(sigma_over_i, 3),
        "predicted_alpha_4": att["alpha_4_attenuation"],
        "alignment_quality": "Strong Alignment (sigma/I < 0.25)" if sigma_over_i < 0.25 else ("Standard Heavy-Ion Alignment (0.25 <= sigma/I <= 0.35)" if sigma_over_i <= 0.35 else "Weak Alignment (sigma/I > 0.35)")
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   IN-BEAM SPIN ALIGNMENT ATTENUATION (alpha_2, alpha_4) ANALYZER")
    lines.append("=" * 72)

    att = summary["attenuation"]
    lines.append(f" ALIGNMENT ATTENUATION FACTORS AT SPIN I = {att['spin_I']} hbar:")
    lines.append(f"   Alignment Width (sigma_m / I)  : {att['sigma_over_I']} (sigma_m = {att['sigma_m_substate_width']})")
    lines.append(f"   Dipole/Quadrupole alpha_2      : {att['alpha_2_attenuation']}")
    lines.append(f"   Hexadecapole alpha_4           : {att['alpha_4_attenuation']}")
    lines.append(f"   Ratio alpha_4 / alpha_2        : {att['attenuation_ratio_alpha4_over_alpha2']}")
    lines.append("-" * 72)

    if "inversion" in summary:
        inv = summary["inversion"]
        lines.append(" INVERSION FROM MEASURED STRETCHED E2 TRANSITION:")
        lines.append(f"   Initial Spin I                 : {inv['spin_initial_I']} hbar")
        lines.append(f"   Measured a_2 Coefficient       : {inv['measured_a2']} (Max Theoretical = {inv['theoretical_a2_max']})")
        lines.append(f"   Extracted alpha_2 Factor       : {inv['extracted_alpha_2']}")
        lines.append(f"   Derived (sigma_m / I) Width    : {inv['inverted_sigma_over_I']}")
        lines.append(f"   Predicted alpha_4 Factor       : {inv['predicted_alpha_4']}")
        lines.append(f"   Alignment Classification       : {inv['alignment_quality']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Non-zero sigma_m/I attenuates experimental angular distribution anisotropy.")
    lines.append("   - Precision delta mixing extraction requires calibrated alpha_2 and alpha_4.")
    lines.append("   - Stretched E2 transitions serve as internal thermometers for spin alignment.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Spin Alignment Attenuation & Substate Width Inverter."
    )
    parser.add_argument("-I", "--spin", type=float, default=6.0, help="Initial spin I in hbar (default: 6.0)")
    parser.add_argument("--sigma-i", type=float, default=0.30, help="Assumed sigma_m / I width (default: 0.30)")
    parser.add_argument("--invert", action="store_true", help="Perform inversion from measured a2")
    parser.add_argument("--a2-exp", type=float, default=0.28, help="Measured a2 of stretched E2 (default: 0.28)")
    parser.add_argument("--a2-max", type=float, default=0.357, help="Theoretical a2_max (default: 0.357)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    att_res = calculate_alignment_attenuation_factors(args.spin, args.sigma_i)
    summary = {"attenuation": att_res}

    if args.invert or args.a2_exp != 0.28:
        inv_res = invert_sigma_over_I_from_stretched_e2(args.a2_exp, args.spin, args.a2_max)
        summary["inversion"] = inv_res
    elif args.spin == 6.0:
        inv_res = invert_sigma_over_I_from_stretched_e2(0.28, 6.0, 0.357)
        summary["inversion"] = inv_res

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
