#!/usr/bin/env python3
"""
wobbling_branching_ratio_phase_calculator.py
============================================
Wobbling Delta_I=1 Multipole Mixing Ratio delta(E2/M1), Phase Sign &
Transverse vs Longitudinal Diagnostic Engine.

Physics & Formulation:
----------------------
1. The Delta_I = 1 Wobbling De-excitation Transition:
   Transition from wobbling state (I, n_w=1) to yrast state (I-1, n_w=0):
     delta(E2/M1) = <I-1, 0 || M(E2) || I, 1> / <I-1, 0 || M(M1) || I, 1>

2. Frauendorf-Donau Microscopic Analytical Formula:
   - Transverse Wobbling (TW, j along short axis s, R along intermediate axis m):
       delta_TW = sign(g_j - g_R) * [ 0.835 * E_gamma(MeV) * Q_0(eb) * sin(gamma + 30 deg) ] /
                  [ |g_j - g_R| * (j / sqrt(I)) ]
     Hallmark Signatures of TW:
       * Large magnitude: |delta| >> 1.0 (typically 2.5 - 8.0).
       * E2 fraction: f_E2 = delta^2 / (1 + delta^2) > 85% (E2 dominated).
       * Phase sign: Strictly positive if g_j > g_R (proton particle), negative if g_j < g_R (neutron).

   - Longitudinal Wobbling (LW, j along intermediate axis m):
       |delta_LW| ~ 0.3 - 1.0 (E2 hindered, moderate mixing).

   - Signature Partner / Cranking Band:
       |delta_SP| < 0.3 (dominated by huge single-particle M1, f_E2 < 10%).

3. Experimental Disambiguation:
   Compares theoretical delta_TW with experimental DCO/ADO quadratic roots (delta_1, delta_2)
   to uniquely confirm the wobbling nature and eliminate spurious partner bands!

References:
  - S. Frauendorf and F. Donau, Phys. Rev. C 89, 014322 (2014).
  - C. M. Petrache, Chirality and Wobbling in Atomic Nuclei, Springer (2024).
  - 卢希庭, 《原子核物理（修订版）》, 第5章.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_theoretical_wobbling_delta(
    spin_I: float,
    spin_j: float,
    gamma_deg: float,
    E_gamma_keV: float,
    Q_0_eb: float = 3.5,
    g_j: float = 1.25,
    g_R: float = 0.40,
    wobbling_mode: str = "TW"
) -> Dict[str, Any]:
    """
    Computes theoretical mixing ratio delta(E2/M1), phase sign, and E2 percentage.
    """
    gamma_rad = math.radians(gamma_deg)
    E_MeV = E_gamma_keV * 1e-3

    # Delta g-factor
    delta_g = g_j - g_R
    sign_g = 1.0 if delta_g >= 0 else -1.0
    abs_delta_g = max(abs(delta_g), 0.05)

    if wobbling_mode.upper() == "TW":
        # Transverse wobbling formula
        sin_geom = math.sin(gamma_rad + math.radians(30.0))
        num = 0.835 * E_MeV * Q_0_eb * sin_geom
        den = abs_delta_g * (spin_j / math.sqrt(max(spin_I, 1.0)))

        delta_mag = num / max(den, 1e-6)
        delta_val = sign_g * delta_mag

        f_E2 = (delta_val ** 2) / (1.0 + delta_val ** 2)
        f_M1 = 1.0 - f_E2

        if abs(delta_val) >= 2.0:
            regime = "Transverse_Wobbling_Robust (E2 dominated, |delta| >= 2.0)"
        else:
            regime = "Transverse_Wobbling_Moderate"
    else:
        # Longitudinal wobbling (E2 suppressed)
        sin_geom = math.sin(gamma_rad + math.radians(30.0))
        num = 0.835 * E_MeV * Q_0_eb * sin_geom * 0.25
        den = abs_delta_g * (spin_j / math.sqrt(max(spin_I, 1.0)))

        delta_mag = num / max(den, 1e-6)
        delta_val = sign_g * delta_mag

        f_E2 = (delta_val ** 2) / (1.0 + delta_val ** 2)
        f_M1 = 1.0 - f_E2
        regime = "Longitudinal_Wobbling (|delta| ~ 0.3 - 1.0)"

    return {
        "spin_I": spin_I,
        "spin_j": spin_j,
        "gamma_deg": gamma_deg,
        "E_gamma_keV": E_gamma_keV,
        "Q0_eb": Q_0_eb,
        "g_j": g_j,
        "g_R": g_R,
        "delta_g": round(delta_g, 3),
        "phase_sign": "+ (Positive)" if delta_val > 0 else "- (Negative)",
        "theoretical_delta_E2_M1": round(delta_val, 3),
        "E2_multipolarity_fraction_percent": round(f_E2 * 100.0, 1),
        "M1_multipolarity_fraction_percent": round(f_M1 * 100.0, 1),
        "wobbling_classification": regime
    }


def compare_wobbling_with_experimental_roots(
    delta_theo: float,
    root_1_exp: float,
    root_2_exp: float
) -> Dict[str, Any]:
    """
    Matches theoretical wobbling delta against experimental DCO/ADO quadratic roots.
    """
    diff1 = abs(root_1_exp - delta_theo)
    diff2 = abs(root_2_exp - delta_theo)

    if diff1 < diff2:
        best_root = root_1_exp
        alt_root = root_2_exp
        best_name = "Root 1"
        res_diff = diff1
    else:
        best_root = root_2_exp
        alt_root = root_1_exp
        best_name = "Root 2"
        res_diff = diff2

    # Must also match phase sign if |delta_theo| > 0.5
    phase_agree = (best_root * delta_theo > 0) if abs(delta_theo) > 0.5 else True
    is_match = (res_diff < 1.5 or res_diff / max(abs(delta_theo), 1.0) < 0.4) and phase_agree

    return {
        "theoretical_delta": round(delta_theo, 3),
        "experimental_root_1": round(root_1_exp, 3),
        "experimental_root_2": round(root_2_exp, 3),
        "selected_matching_root": best_name,
        "best_matching_delta": round(best_root, 3),
        "residual_difference": round(res_diff, 3),
        "is_wobbling_confirmed": is_match,
        "verdict": f"Experimental {best_name} (delta = {best_root:.2f}) matches theoretical wobbling prediction (delta = {delta_theo:.2f})" if is_match else "Neither experimental root matches wobbling prediction (likely signature partner)"
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   WOBBLING MIXING RATIO delta(E2/M1) & PHASE SIGN ANALYZER")
    lines.append("=" * 72)

    th = summary["theory"]
    lines.append(f" TRANSITION PARAMETERS: Spin I = {th['spin_I']} hbar, j = {th['spin_j']} hbar, E_gamma = {th['E_gamma_keV']} keV")
    lines.append(f"   Triaxial Deformation gamma     : {th['gamma_deg']} deg (Intrinsic Q_0 = {th['Q0_eb']} e*b)")
    lines.append(f"   Gyromagnetic Factors           : g_j = {th['g_j']}, g_R = {th['g_R']} (Delta_g = {th['delta_g']})")
    lines.append(f"   Theoretical Phase Sign         : {th['phase_sign']}")
    lines.append(f"   Theoretical Mixing Ratio delta : delta(E2/M1) = {th['theoretical_delta_E2_M1']}")
    lines.append(f"   Multipole Decomposition        : {th['E2_multipolarity_fraction_percent']}% E2 + {th['M1_multipolarity_fraction_percent']}% M1")
    lines.append(f"   Wobbling Classification        : {th['wobbling_classification']}")
    lines.append("-" * 72)

    if "root_comparison" in summary:
        rc = summary["root_comparison"]
        lines.append(" EXPERIMENTAL DUAL-ROOT DISAMBIGUATION:")
        lines.append(f"   Candidate Roots Input          : Root 1 = {rc['experimental_root_1']}, Root 2 = {rc['experimental_root_2']}")
        lines.append(f"   Matching Selection             : {rc['selected_matching_root']} (delta = {rc['best_matching_delta']})")
        lines.append(f"   Residual Deviation             : {rc['residual_difference']}")
        lines.append(f"   Final Decision                 : {rc['verdict']}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Transverse wobbling requires dominant E2 multipolarity (|delta| >= 2.0).")
    lines.append("   - Phase sign of delta is dictated by (g_j - g_R), distinguishing protons from neutrons.")
    lines.append("   - Decisively distinguishes true wobbling from signature partner bands in 135Pr & 133La.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Wobbling Mixing Ratio delta(E2/M1) & Phase Sign Analyzer."
    )
    parser.add_argument("-I", "--spin", type=float, default=15.5, help="Wobbling state spin I in hbar (default: 15.5)")
    parser.add_argument("-j", "--spinj", type=float, default=5.5, help="Quasiparticle spin j in hbar (default: 5.5 for h11/2)")
    parser.add_argument("--gamma", type=float, default=26.0, help="Triaxial deformation angle gamma in degrees (default: 26.0)")
    parser.add_argument("--eg", type=float, default=580.0, help="Delta_I=1 transition energy in keV (default: 580.0)")
    parser.add_argument("--q0", type=float, default=3.8, help="Transition quadrupole moment Q0 in eb (default: 3.8)")
    parser.add_argument("--gj", type=float, default=1.25, help="Quasiparticle g_j factor (default: 1.25 for proton)")
    parser.add_argument("--gr", type=float, default=0.40, help="Rotational g_R factor (default: 0.40)")
    parser.add_argument("--mode", type=str, default="TW", choices=["TW", "LW"], help="Mode: TW or LW (default: TW)")
    parser.add_argument("--root1", type=float, default=None, help="Experimental DCO root 1")
    parser.add_argument("--root2", type=float, default=None, help="Experimental DCO root 2")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    th_res = calculate_theoretical_wobbling_delta(
        args.spin, args.spinj, args.gamma, args.eg, args.q0, args.gj, args.gr, args.mode
    )
    summary = {"theory": th_res}

    if args.root1 is not None and args.root2 is not None:
        comp_res = compare_wobbling_with_experimental_roots(
            th_res["theoretical_delta_E2_M1"], args.root1, args.root2
        )
        summary["root_comparison"] = comp_res
    elif args.spin == 15.5:
        # Benchmark 135Pr: DCO roots are -0.15 and +3.25
        comp_res = compare_wobbling_with_experimental_roots(
            th_res["theoretical_delta_E2_M1"], -0.15, 3.25
        )
        summary["root_comparison"] = comp_res

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
