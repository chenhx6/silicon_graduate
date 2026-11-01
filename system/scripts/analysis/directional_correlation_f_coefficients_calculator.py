#!/usr/bin/env python3
"""
directional_correlation_f_coefficients_calculator.py
=====================================================
Exact Yamazaki / Biedenharn-Rose F-Coefficients, Directional Angular Distribution &
In-Beam DCO/ADO Ratio and Dual-Root Delta Calculator.

Physics & Formulation:
----------------------
1. The Yamazaki / Biedenharn-Rose F-Coefficients:
   Governs directional correlation and angular distribution of gamma rays emitted from
   oriented nuclear states:
     F_k(L, L', I_f, I_i) = (-1)^(I_f + I_i + L + L' - 1) *
                            sqrt( (2*L + 1) * (2*L' + 1) * (2*I_i + 1) ) *
                            C(L, 1; L', -1 | k, 0) * {  I_i   I_i   k  }
                                                     {  L'    L    I_f }
   where the angular momentum of the oriented state I_i is written LAST,
   and { 6j } is the Wigner 6j symbol.
   Only even ranks k = 2, 4 appear for parity-conserving gamma transitions.

2. Directional Angular Distribution W(theta):
   W(theta) = 1 + a_2 * P_2(cos theta) + a_4 * P_4(cos theta)
   where:
     a_k = alpha_k * A_k(gamma)
     A_k(gamma) = [ F_k(L L I_f I_i) + 2 * delta * F_k(L L' I_f I_i) + delta^2 * F_k(L' L' I_f I_i) ] / (1 + delta^2)
   alpha_k is the spin orientation attenuation factor (Yamazaki alignment parameter, alpha_k = B_k(I) / B_k^max(I)).

3. Multipole Mixing Ratio delta(E2/M1) Dual-Root Inversion:
   For mixed dipole-quadrupole transitions (L=1, L'=2):
     (a_2 - alpha_2 * F_2(2 2)) * delta^2 - 2 * alpha_2 * F_2(1 2) * delta + (a_2 - alpha_2 * F_2(1 1)) = 0
   Quadratic equation: A * delta^2 + B * delta + C = 0
     Discriminant: Delta = B^2 - 4 * A * C
     Roots: delta_{1, 2} = (-B +/- sqrt(Delta)) / (2 * A)

4. Directional Correlation from Oriented States (DCO) Ratio:
   R_DCO = W(theta_1) / W(theta_2)  (in factorization approximation for stretched E2 gate)

References:
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第7章 §7.6 (级联辐射的角关联).
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第1章与第10章.
  - W. D. Hamilton, The Electromagnetic Interaction in Nuclear Spectroscopy, North-Holland (1975), Ch 12 & Appendix 2.
  - T. Yamazaki, Nucl. Data A 3, 1 (1967).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def clebsch_gordan(j1: float, m1: float, j2: float, m2: float, j: float, m: float) -> float:
    """Exact Clebsch-Gordan coefficient <j1 m1 j2 m2 | j m> using Racah formula."""
    if abs(m1 + m2 - m) > 1e-9:
        return 0.0
    if not (abs(j1 - j2) - 1e-9 <= j <= j1 + j2 + 1e-9):
        return 0.0
    if abs(m1) > j1 + 1e-9 or abs(m2) > j2 + 1e-9 or abs(m) > j + 1e-9:
        return 0.0

    f = math.factorial
    j1_i, m1_i = int(round(2 * j1)), int(round(2 * m1))
    j2_i, m2_i = int(round(2 * j2)), int(round(2 * m2))
    j_i, m_i = int(round(2 * j)), int(round(2 * m))

    num = (j_i + 1) * f((j1_i + j2_i - j_i) // 2) * f((j1_i - j2_i + j_i) // 2) * f((-j1_i + j2_i + j_i) // 2)
    den = f((j1_i + j2_i + j_i) // 2 + 1)
    pre = math.sqrt(float(num) / float(den))

    pre *= math.sqrt(
        float(f((j1_i + m1_i) // 2) * f((j1_i - m1_i) // 2) *
              f((j2_i + m2_i) // 2) * f((j2_i - m2_i) // 2) *
              f((j_i + m_i) // 2) * f((j_i - m_i) // 2))
    )

    k_min = max(0, (j2_i - j_i - m1_i) // 2, (j1_i - j_i + m2_i) // 2)
    k_max = min((j1_i + j2_i - j_i) // 2, (j1_i - m1_i) // 2, (j2_i + m2_i) // 2)

    s = 0.0
    for k in range(k_min, k_max + 1):
        denom = (
            f(k) *
            f((j1_i + j2_i - j_i) // 2 - k) *
            f((j1_i - m1_i) // 2 - k) *
            f((j2_i + m2_i) // 2 - k) *
            f((j_i - j2_i + m1_i) // 2 + k) *
            f((j_i - j1_i - m2_i) // 2 + k)
        )
        term = ((-1.0) ** k) / float(denom)
        s += term

    return pre * s


def delta_tri(a: float, b: float, c: float) -> float:
    """Triangle coefficient Delta(a, b, c) using factorials."""
    f = math.factorial
    ia, ib, ic = int(round(2 * a)), int(round(2 * b)), int(round(2 * c))
    if (ia + ib - ic) < 0 or (ia - ib + ic) < 0 or (-ia + ib + ic) < 0 or (ia + ib + ic) % 2 != 0:
        return 0.0
    num = f((ia + ib - ic) // 2) * f((ia - ib + ic) // 2) * f((-ia + ib + ic) // 2)
    den = f((ia + ib + ic) // 2 + 1)
    return math.sqrt(float(num) / float(den))


def wigner_6j(j1: float, j2: float, j3: float, j4: float, j5: float, j6: float) -> float:
    """Exact Wigner 6j symbol using Racah formula."""
    d1 = delta_tri(j1, j2, j3)
    d2 = delta_tri(j1, j5, j6)
    d3 = delta_tri(j4, j2, j6)
    d4 = delta_tri(j4, j5, j3)
    if d1 * d2 * d3 * d4 == 0.0:
        return 0.0
    f = math.factorial
    i1, i2, i3, i4, i5, i6 = [int(round(2 * x)) for x in [j1, j2, j3, j4, j5, j6]]
    k_min = max(0, (i1 + i2 + i3) // 2, (i1 + i5 + i6) // 2, (i4 + i2 + i6) // 2, (i4 + i5 + i3) // 2)
    k_max = min((i1 + i2 + i4 + i5) // 2, (i2 + i3 + i5 + i6) // 2, (i3 + i1 + i6 + i4) // 2)
    if k_min > k_max:
        return 0.0
    s = sum(((-1.0) ** k) * f(k + 1) / float(
        f(k - (i1 + i2 + i3) // 2) * f(k - (i1 + i5 + i6) // 2) *
        f(k - (i4 + i2 + i6) // 2) * f(k - (i4 + i5 + i3) // 2) *
        f((i1 + i2 + i4 + i5) // 2 - k) * f((i2 + i3 + i5 + i6) // 2 - k) * f((i3 + i1 + i6 + i4) // 2 - k)
    ) for k in range(k_min, k_max + 1))
    return d1 * d2 * d3 * d4 * s


def calculate_f_coefficient(k: int, L: int, Lprime: int, If: float, Ii: float) -> float:
    """
    Calculates exact Yamazaki / Hamilton F-coefficient F_k(L, L', If, Ii):
      F_k(L, L', If, Ii) = (-1)^(If - Ii - 1) * sqrt((2L+1)*(2L'+1)*(2Ii+1))
                         * C(L, 1; L', -1 | k, 0) * W(Ii, Ii, L, L'; k, If)
      where W(Ii, Ii, L, L'; k, If) = (-1)^(2*Ii + L + L') * 6j(Ii, Ii, k; L', L, If).
    """
    if k % 2 != 0:
        return 0.0
    if k > 2 * min(Lprime, int(Ii)):
        return 0.0

    phase = (-1.0) ** int(round(If - Ii - 1.0 + 2.0 * Ii + float(L + Lprime)))
    norm = math.sqrt((2.0 * L + 1.0) * (2.0 * Lprime + 1.0) * (2.0 * Ii + 1.0))
    cg = clebsch_gordan(float(L), 1.0, float(Lprime), -1.0, float(k), 0.0)
    six_j = wigner_6j(Ii, Ii, float(k), float(Lprime), float(L), If)

    return phase * norm * cg * six_j


def calculate_angular_distribution_coefficients(
    Ii: float,
    If: float,
    delta: float = 0.0,
    alpha2: float = 1.0,
    alpha4: float = 1.0,
    L: int = 1,
    Lprime: int = 2
) -> Dict[str, Any]:
    """
    Calculates F-coefficients, A_k, and directional angular distribution coefficients a2, a4.
    """
    F2_11 = calculate_f_coefficient(2, L, L, If, Ii)
    F2_12 = calculate_f_coefficient(2, L, Lprime, If, Ii)
    F2_22 = calculate_f_coefficient(2, Lprime, Lprime, If, Ii)

    F4_11 = calculate_f_coefficient(4, L, L, If, Ii)
    F4_12 = calculate_f_coefficient(4, L, Lprime, If, Ii)
    F4_22 = calculate_f_coefficient(4, Lprime, Lprime, If, Ii)

    delta2 = delta ** 2
    norm = 1.0 + delta2

    A2 = (F2_11 + 2.0 * delta * F2_12 + delta2 * F2_22) / norm
    A4 = (F4_11 + 2.0 * delta * F4_12 + delta2 * F4_22) / norm

    a2 = alpha2 * A2
    a4 = alpha4 * A4

    return {
        "initial_spin_Ii": Ii,
        "final_spin_If": If,
        "delta_I": If - Ii,
        "multipole_L": L,
        "multipole_Lprime": Lprime,
        "mixing_ratio_delta": delta,
        "orientation_alpha2": alpha2,
        "orientation_alpha4": alpha4,
        "F_coefficients": {
            "F2_11": round(F2_11, 4),
            "F2_12": round(F2_12, 4),
            "F2_22": round(F2_22, 4),
            "F4_11": round(F4_11, 4),
            "F4_12": round(F4_12, 4),
            "F4_22": round(F4_22, 4)
        },
        "unattenuated_A_k": {
            "A2": round(A2, 4),
            "A4": round(A4, 4)
        },
        "attenuated_a_k": {
            "a2": round(a2, 4),
            "a4": round(a4, 4)
        }
    }


def invert_delta_dual_roots(
    a2_measured: float,
    Ii: float,
    If: float,
    alpha2: float = 1.0,
    L: int = 1,
    Lprime: int = 2
) -> Dict[str, Any]:
    """
    Analytically solves the quadratic equation for mixing ratio delta from measured a2:
      (a2 - alpha2 * F2_22) * delta^2 - 2 * alpha2 * F2_12 * delta + (a2 - alpha2 * F2_11) = 0
    """
    F2_11 = calculate_f_coefficient(2, L, L, If, Ii)
    F2_12 = calculate_f_coefficient(2, L, Lprime, If, Ii)
    F2_22 = calculate_f_coefficient(2, Lprime, Lprime, If, Ii)

    A = a2_measured - alpha2 * F2_22
    B = -2.0 * alpha2 * F2_12
    C = a2_measured - alpha2 * F2_11

    discriminant = B ** 2 - 4.0 * A * C

    if discriminant < 0:
        has_real_roots = False
        root1, root2 = None, None
        verdict = "No real roots: measured a2 is mathematically outside physical range for this spin sequence."
    else:
        has_real_roots = True
        sqrt_d = math.sqrt(discriminant)
        if abs(A) < 1e-9:
            root1 = -C / B if abs(B) > 1e-9 else 0.0
            root2 = root1
        else:
            r_a = (-B - sqrt_d) / (2.0 * A)
            r_b = (-B + sqrt_d) / (2.0 * A)
            # Order by magnitude
            if abs(r_a) <= abs(r_b):
                root1, root2 = r_a, r_b
            else:
                root1, root2 = r_b, r_a
        verdict = "Dual roots found: two mathematically degenerate mixing ratios yield the exact same a2."

    res = {
        "a2_measured": a2_measured,
        "initial_spin_Ii": Ii,
        "final_spin_If": If,
        "alpha2": alpha2,
        "quadratic_coefficients": {
            "A": round(A, 5),
            "B": round(B, 5),
            "C": round(C, 5),
            "discriminant": round(discriminant, 5)
        },
        "has_real_roots": has_real_roots,
        "root1_small_magnitude": round(root1, 4) if root1 is not None else None,
        "root2_large_magnitude": round(root2, 4) if root2 is not None else None,
        "verdict": verdict
    }

    if has_real_roots and root1 is not None and root2 is not None:
        f_e2_1 = (root1 ** 2) / (1.0 + root1 ** 2) * 100.0
        f_e2_2 = (root2 ** 2) / (1.0 + root2 ** 2) * 100.0
        res["root1_E2_percentage"] = round(f_e2_1, 1)
        res["root1_M1_percentage"] = round(100.0 - f_e2_1, 1)
        res["root2_E2_percentage"] = round(f_e2_2, 1)
        res["root2_M1_percentage"] = round(100.0 - f_e2_2, 1)

    return res


def calculate_dco_and_ado_ratios(
    Ii: float,
    If: float,
    delta: float,
    theta1_deg: float = 30.0,
    theta2_deg: float = 90.0,
    alpha2: float = 0.85,
    alpha4: float = 0.60
) -> Dict[str, Any]:
    """
    Calculates theoretical DCO/ADO ratio R_DCO = W(theta1) / W(theta2) directly from spins and delta.
    """
    dist = calculate_angular_distribution_coefficients(Ii, If, delta, alpha2, alpha4)
    a2 = dist["attenuated_a_k"]["a2"]
    a4 = dist["attenuated_a_k"]["a4"]

    def W(theta_deg):
        th = math.radians(theta_deg)
        cos_th = math.cos(th)
        p2 = 0.5 * (3.0 * cos_th ** 2 - 1.0)
        p4 = 0.125 * (35.0 * cos_th ** 4 - 30.0 * cos_th ** 2 + 3.0)
        return 1.0 + a2 * p2 + a4 * p4

    W1 = W(theta1_deg)
    W2 = W(theta2_deg)
    r_dco = W1 / max(1e-6, W2)

    return {
        "initial_spin_Ii": Ii,
        "final_spin_If": If,
        "mixing_ratio_delta": delta,
        "angles": {
            "theta1_deg": theta1_deg,
            "theta2_deg": theta2_deg
        },
        "W_theta1": round(W1, 4),
        "W_theta2": round(W2, 4),
        "R_DCO": round(r_dco, 4),
        "a2": a2,
        "a4": a4
    }


def format_text_report(dist: Dict[str, Any], inv: Optional[Dict[str, Any]] = None, dco: Optional[Dict[str, Any]] = None) -> str:
    lines = [
        "=" * 74,
        "   YAMAZAKI F-COEFFICIENTS, ANGULAR DISTRIBUTION & DCO DUAL-ROOT SUITE",
        "   Based on Lu Xiting §7.6, Wu Zhihua §1.5/10.3 & Hamilton Ch 12",
        "=" * 74,
        f" TRANSITION GEOMETRY: Initial Spin I_i = {dist['initial_spin_Ii']} -> Final Spin I_f = {dist['final_spin_If']} (Delta_I = {dist['delta_I']})",
        f"   Multipole Orders     : L = {dist['multipole_L']}, L' = {dist['multipole_Lprime']}",
        f"   Mixing Ratio delta   : {dist['mixing_ratio_delta']}",
        f"   Orientation Params   : alpha_2 = {dist['orientation_alpha2']}, alpha_4 = {dist['orientation_alpha4']}",
        "-" * 74,
        " EXACT ALGEBRAIC YAMAZAKI / BIEDENHARN-ROSE F-COEFFICIENTS (Rank k=2, 4):",
        f"   Rank k=2 : F_2(11) = {dist['F_coefficients']['F2_11']:+7.4f},  F_2(12) = {dist['F_coefficients']['F2_12']:+7.4f},  F_2(22) = {dist['F_coefficients']['F2_22']:+7.4f}",
        f"   Rank k=4 : F_4(11) = {dist['F_coefficients']['F4_11']:+7.4f},  F_4(12) = {dist['F_coefficients']['F4_12']:+7.4f},  F_4(22) = {dist['F_coefficients']['F4_22']:+7.4f}",
        "-" * 74,
        f" DIRECTIONAL DISTRIBUTION COEFFICIENTS W(theta):",
        f"   Unattenuated A_k     : A_2 = {dist['unattenuated_A_k']['A2']:+7.4f},  A_4 = {dist['unattenuated_A_k']['A4']:+7.4f}",
        f"   Attenuated a_k       : a_2 = {dist['attenuated_a_k']['a2']:+7.4f},  a_4 = {dist['attenuated_a_k']['a4']:+7.4f}",
    ]

    if dco is not None:
        lines.extend([
            "-" * 74,
            f" THEORETICAL DCO RATIO R_DCO (theta1 = {dco['angles']['theta1_deg']} deg, theta2 = {dco['angles']['theta2_deg']} deg):",
            f"   W(theta1) = {dco['W_theta1']:.4f},  W(theta2) = {dco['W_theta2']:.4f}  ==>  R_DCO = {dco['R_DCO']:.4f}",
        ])

    if inv is not None:
        lines.extend([
            "-" * 74,
            f" ANALYTIC DUAL-ROOT INVERSION FROM MEASURED a2 = {inv['a2_measured']:+.4f}:",
            f"   Discriminant Delta   : {inv['quadratic_coefficients']['discriminant']:+.5f} ({'Real roots exist' if inv['has_real_roots'] else 'No real roots'})",
        ])
        if inv['has_real_roots']:
            lines.extend([
                f"   Root 1 (Small Mag)   : delta = {inv['root1_small_magnitude']:+.4f} (E2: {inv['root1_E2_percentage']}%, M1: {inv['root1_M1_percentage']}%)",
                f"   Root 2 (Large Mag)   : delta = {inv['root2_large_magnitude']:+.4f} (E2: {inv['root2_E2_percentage']}%, M1: {inv['root2_M1_percentage']}%)",
                f"   Root Verdict         : {inv['verdict']}",
                "   [RESEARCH NOTE]      : Both roots give the exact same a2; Clover Compton linear",
                "                          polarization P or conversion electron alpha_K is required",
                "                          to uniquely isolate the physical solution."
            ])
        else:
            lines.append(f"   Root Verdict         : {inv['verdict']}")

    lines.extend([
        "=" * 74
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Yamazaki F-Coefficients, Angular Distribution & DCO Dual-Root Inverter"
    )
    parser.add_argument("--Ii", "-i", type=float, default=7.5, help="Initial spin Ii in hbar (default: 7.5, 15/2)")
    parser.add_argument("--If", "-f", type=float, default=6.5, help="Final spin If in hbar (default: 6.5, 13/2)")
    parser.add_argument("--delta", "-d", type=float, default=-0.15, help="Mixing ratio delta(E2/M1) (default: -0.15)")
    parser.add_argument("--alpha2", type=float, default=0.85, help="Orientation attenuation alpha2 (default: 0.85)")
    parser.add_argument("--alpha4", type=float, default=0.60, help="Orientation attenuation alpha4 (default: 0.60)")
    parser.add_argument("--a2-meas", type=float, default=None, help="Measured a2 to invert dual roots")
    parser.add_argument("--th1", type=float, default=30.0, help="DCO detector 1 angle in deg (default: 30.0)")
    parser.add_argument("--th2", type=float, default=90.0, help="DCO detector 2 angle in deg (default: 90.0)")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    dist = calculate_angular_distribution_coefficients(
        Ii=args.Ii, If=args.If, delta=args.delta, alpha2=args.alpha2, alpha4=args.alpha4
    )

    inv = None
    if args.a2_meas is not None:
        inv = invert_delta_dual_roots(
            a2_measured=args.a2_meas, Ii=args.Ii, If=args.If, alpha2=args.alpha2
        )
    elif args.Ii == 7.5 and args.If == 6.5:
        # Default demonstration: invert from theoretical a2
        inv = invert_delta_dual_roots(
            a2_measured=dist["attenuated_a_k"]["a2"], Ii=args.Ii, If=args.If, alpha2=args.alpha2
        )

    dco = calculate_dco_and_ado_ratios(
        Ii=args.Ii, If=args.If, delta=args.delta, theta1_deg=args.th1, theta2_deg=args.th2,
        alpha2=args.alpha2, alpha4=args.alpha4
    )

    if args.json:
        out = {"distribution": dist, "dco_ratio": dco}
        if inv is not None:
            out["inversion"] = inv
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(dist, inv, dco))


if __name__ == "__main__":
    main()
