#!/usr/bin/env python3
"""
cascade_deorientation_coefficient_uk_calculator.py
==================================================
In-Beam Gamma-Ray Spectroscopy Unobserved Cascade Deorientation Coefficients U_k(I1, I2, L)
& Attenuated Angular Distribution Cascade Analysis Engine.

Physics & Formalism:
--------------------
1. Deorientation Effect of Intermediate Unobserved Transitions:
   Based on W. D. Hamilton "The Electromagnetic Interaction in Nuclear Spectroscopy" (1975)
   Chapter 14 (pp. 580–625), 吴治华《原子核物理实验方法》第 10 章 §10.3,
   and B. Herskind et al. (Nucl. Phys. A 108, 385, 1968):
   When an oriented nuclear state I_1 emits an unobserved gamma-ray (or fast unobserved
   side-feeding cascade) of multipolarity L populating level I_2, the nuclear orientation
   tensor B_k(I_1) is attenuated by the deorientation coefficient U_k(I_1, I_2, L):
     B_k(I_2) = B_k(I_1) * U_k(I_1, I_2, L)

2. Racah W-Algebra & Wigner 6j Symbol Formulation:
   The deorientation coefficient is mathematically defined as:
     U_k(I_1, I_2, L) = (-1)^(I_1 + I_2 + L + k) * sqrt( (2*I_1 + 1)*(2*I_2 + 1) ) * { I_1  I_1  k }
                                                                                        { I_2  I_2  L }
   Exact identities:
     - U_0(I_1, I_2, L) == 1.0 (Total probability conservation)
     - For k > 0, U_k <= 1.0, systematically washing out angular distribution anisotropy.

3. Mixed Multipolarity (L + (L+1)) Unobserved Transitions:
   For mixed transitions (e.g. M1 + E2 with mixing ratio delta_u):
     U_k(I_1, I_2) = [ U_k(I_1, I_2, L) + delta_u^2 * U_k(I_1, I_2, L+1) ] / ( 1.0 + delta_u^2 )

4. Multi-Step Cascade Chain Propagation:
   For an n-step unobserved cascade I_0 -> I_1 -> I_2 ... -> I_n -> I_{n+1} (observed):
     Total attenuation: U_k_tot = prod_{i=1}^n U_k(I_{i-1}, I_i, L_i)
   The observed angular distribution coefficients a_k are given by:
     a_k_obs = a_k_initial * U_k_tot
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "yrast_stretched_e2_cascade": {
        "description": "Yrast stretched E2 cascade: 6+ -> 4+ -> 2+ (observed) -> 0+",
        "I_initial": 6.0,
        "steps": [
            {"from_spin": 6.0, "to_spin": 4.0, "L": 2.0, "delta": 0.0},
            {"from_spin": 4.0, "to_spin": 2.0, "L": 2.0, "delta": 0.0}
        ],
        "a2_initial": 0.350,
        "a4_initial": -0.090
    },
    "chiral_mixed_m1e2_cascade": {
        "description": "Chiral band intermediate feeding: 13+ -> 12+ (M1+E2, delta=-0.15) -> 10+ (E2)",
        "I_initial": 13.0,
        "steps": [
            {"from_spin": 13.0, "to_spin": 12.0, "L": 1.0, "delta": -0.15}
        ],
        "a2_initial": -0.220,
        "a4_initial": 0.000
    },
    "dipole_unobserved_feed": {
        "description": "Odd-A fast dipole feeding: 17/2 -> 15/2 (M1) -> 11/2 (E2)",
        "I_initial": 8.5,
        "steps": [
            {"from_spin": 8.5, "to_spin": 7.5, "L": 1.0, "delta": 0.0}
        ],
        "a2_initial": 0.400,
        "a4_initial": -0.120
    }
}


def _triangle_check(a, b, c):
    return (abs(a - b) <= c <= a + b) and (abs(int(round(2 * (a + b + c)))) % 2 == 0)


def _delta_coeff(a, b, c):
    f = math.factorial
    num = f(int(round(a + b - c))) * f(int(round(a - b + c))) * f(int(round(-a + b + c)))
    den = f(int(round(a + b + c + 1)))
    return math.sqrt(num / den)


def wigner_6j(j1, j2, j3, j4, j5, j6):
    """
    Exact Racah formula for Wigner 6j symbol.
    """
    if not (_triangle_check(j1, j2, j3) and _triangle_check(j1, j5, j6) and
            _triangle_check(j4, j2, j6) and _triangle_check(j4, j5, j3)):
        return 0.0

    d1 = _delta_coeff(j1, j2, j3)
    d2 = _delta_coeff(j1, j5, j6)
    d3 = _delta_coeff(j4, j2, j6)
    d4 = _delta_coeff(j4, j5, j3)

    prefactor = d1 * d2 * d3 * d4
    f = math.factorial

    z_min = max(0,
                int(round(j1 + j2 + j3)),
                int(round(j1 + j5 + j6)),
                int(round(j4 + j2 + j6)),
                int(round(j4 + j5 + j3)))
    z_max = min(int(round(j1 + j2 + j4 + j5)),
                int(round(j2 + j3 + j5 + j6)),
                int(round(j3 + j1 + j6 + j4)))

    sum_val = 0.0
    for z in range(z_min, z_max + 1):
        num = ((-1)**z) * f(z + 1)
        den = (f(z - int(round(j1 + j2 + j3))) *
               f(z - int(round(j1 + j5 + j6))) *
               f(z - int(round(j4 + j2 + j6))) *
               f(z - int(round(j4 + j5 + j3))) *
               f(int(round(j1 + j2 + j4 + j5)) - z) *
               f(int(round(j2 + j3 + j5 + j6)) - z) *
               f(int(round(j3 + j1 + j6 + j4)) - z))
        sum_val += num / den

    return float(prefactor * sum_val)


def calculate_single_step_uk(I1, I2, L, k):
    """
    Calculates U_k(I1, I2, L) for a pure multipole L transition:
      U_k(I1, I2, L) = (-1)^(I1 + I2 + L + k) * sqrt((2*I1+1)*(2*I2+1)) * { I1 I1 k }
                                                                         { I2 I2 L }
    """
    if k == 0:
        return 1.0

    w6j = wigner_6j(I1, I1, k, I2, I2, L)
    phase = (-1)**int(round(I1 + I2 + L + k))
    val = phase * math.sqrt((2.0 * I1 + 1.0) * (2.0 * I2 + 1.0)) * w6j
    return float(val)


def calculate_mixed_step_uk(I1, I2, L, delta, k):
    """
    Calculates U_k for a mixed L / L+1 transition.
    """
    u_L = calculate_single_step_uk(I1, I2, L, k)
    u_Lp1 = calculate_single_step_uk(I1, I2, L + 1.0, k)
    d2 = delta**2
    return float((u_L + d2 * u_Lp1) / (1.0 + d2))


def evaluate_cascade_deorientation(steps, a2_init=1.0, a4_init=1.0):
    """
    Evaluates the cumulative U_2 and U_4 attenuation across an n-step cascade.
    """
    u2_tot = 1.0
    u4_tot = 1.0

    step_details = []
    for idx, s in enumerate(steps):
        I1 = float(s["from_spin"])
        I2 = float(s["to_spin"])
        L = float(s.get("L", 2.0))
        delta = float(s.get("delta", 0.0))

        u2_step = calculate_mixed_step_uk(I1, I2, L, delta, k=2)
        u4_step = calculate_mixed_step_uk(I1, I2, L, delta, k=4)

        u2_tot *= u2_step
        u4_tot *= u4_step

        step_details.append({
            "step_index": idx + 1,
            "from_spin": I1,
            "to_spin": I2,
            "L": L,
            "delta": delta,
            "U2_step": u2_step,
            "U4_step": u4_step,
            "cumulative_U2": u2_tot,
            "cumulative_U4": u4_tot
        })

    a2_final = a2_init * u2_tot
    a4_final = a4_init * u4_tot

    return {
        "total_U2": float(u2_tot),
        "total_U4": float(u4_tot),
        "a2_initial": float(a2_init),
        "a4_initial": float(a4_init),
        "a2_attenuated": float(a2_final),
        "a4_attenuated": float(a4_final),
        "steps": step_details
    }


def format_text_report(res, title="Cascade Deorientation Coefficient Engine"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Cumulative Deorientation Factors: U_2(tot) = {res['total_U2']:.4f}, U_4(tot) = {res['total_U4']:.4f}")
    lines.append("=" * 76)
    lines.append(f"  Initial Distribution Coefficients : a2 = {res['a2_initial']:+.4f}, a4 = {res['a4_initial']:+.4f}")
    lines.append(f"  Attenuated Observed Coefficients  : a2 = {res['a2_attenuated']:+.4f}, a4 = {res['a4_attenuated']:+.4f}")
    lines.append("-" * 76)
    lines.append("Cascade Step-by-Step Deorientation Breakdown:")
    lines.append("   Step   Transition   L (delta)     U2(step)   U4(step)   Cumul_U2   Cumul_U4")
    for s in res["steps"]:
        trans_str = f"{s['from_spin']:4.1f} -> {s['to_spin']:4.1f}"
        l_str = f"{s['L']:.0f}" if abs(s["delta"]) < 1e-4 else f"{s['L']:.0f}+{s['L']+1:.0f} (d={s['delta']:+.2f})"
        lines.append(
            f"    {s['step_index']:2d}    {trans_str:11s}  {l_str:11s}   {s['U2_step']:8.4f}   {s['U4_step']:8.4f}   {s['cumulative_U2']:8.4f}   {s['cumulative_U4']:8.4f}"
        )
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Gamma Spectroscopy Cascade Deorientation Coefficients U_k & Attenuation Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--a2", type=float, default=0.35, help="Initial a2 coefficient")
    parser.add_argument("--a4", type=float, default=-0.10, help="Initial a4 coefficient")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        steps = p["steps"]
        a2_init = p.get("a2_initial", 0.35)
        a4_init = p.get("a4_initial", -0.10)
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        # Default 2-step cascade 6+ -> 4+ -> 2+
        steps = PRESETS["yrast_stretched_e2_cascade"]["steps"]
        a2_init = args.a2
        a4_init = args.a4
        title = "Default 6+ -> 4+ -> 2+ Cascade"

    res = evaluate_cascade_deorientation(steps, a2_init=a2_init, a4_init=a4_init)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
