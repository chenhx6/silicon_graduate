#!/usr/bin/env python3
"""
wigner_racah_algebra_9j_calculator.py
=====================================
Wigner-Racah Angular Momentum Algebra, Wigner 9j Symbol & L-S to j-j
Recoupling Coefficient Calculator.

Physics & Formulation:
----------------------
1. Wigner 9j Symbol Definition:
   Re-couples four angular momenta (j1, j2, j3, j4) coupled in two different orders:
     |((j1 j2)j12, (j3 j4)j34) J> <-> |((j1 j3)j13, (j2 j4)j24) J>
   Expressed as sum over Wigner 6j symbols:
     { j1  j2  j12 }
     { j3  j4  j34 } = sum_k (-1)^(2k) * (2k + 1) * { j1  j3  j13 } * { j2  j4  j24 } * { j12  j34  J }
     { j13 j24  J  }                                { j24  J    k  }   { j3   k   j13 }   {  k    j1  j2 }

2. Symmetries of 9j Symbol:
   - Invariant under reflection along either diagonal.
   - Invariant under even permutations of rows or columns.
   - Acquires phase factor (-1)^Sigma under an odd permutation of rows or columns,
     where Sigma is the sum of all 9 elements.

3. Special Reduction when One Entry is Zero:
   { j1  j2  j12 }
   { j3  j4  j12 } = delta_j13,j24 * [ (-1)^(j2 + j3 + j12 + j13) / sqrt((2*j12+1)*(2*j13+1)) ] *
   { j13 j13   0 }   { j1  j2  j12 }
                     { j4  j3  j13 }

4. L-S to j-j Nuclear Shell Model Transformation:
   < (l1 s1)j1, (l2 s2)j2; J | (l1 l2)L, (s1 s2)S; J > =
     sqrt( (2*j1+1)*(2*j2+1)*(2*L+1)*(2*S+1) ) * { l1  s1  j1 }
                                                  { l2  s2  j2 }
                                                  { L   S   J  }
   Fundamental for two-body shell model matrix elements and spectroscopic factors.

References:
  - A. R. Edmonds, Angular Momentum in Quantum Mechanics, Princeton (1957).
  - D. A. Varshalovich et al., Quantum Theory of Angular Momentum, World Scientific (1988).
  - J. Suhonen, From Nucleons to Nucleus, Springer (2007).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def delta_tri(a: float, b: float, c: float) -> float:
    """Triangle coefficient Delta(a, b, c) using factorials."""
    f = math.factorial
    ia = int(round(2 * a))
    ib = int(round(2 * b))
    ic = int(round(2 * c))
    if (ia + ib - ic) < 0 or (ia - ib + ic) < 0 or (-ia + ib + ic) < 0:
        return 0.0
    if (ia + ib + ic) % 2 != 0:
        return 0.0
    num = f((ia + ib - ic) // 2) * f((ia - ib + ic) // 2) * f((-ia + ib + ic) // 2)
    den = f((ia + ib + ic) // 2 + 1)
    return math.sqrt(num / den)


def wigner_6j(j1: float, j2: float, j3: float, j4: float, j5: float, j6: float) -> float:
    """Computes exact Wigner 6j symbol using Racah sum formula."""
    # Triangular conditions: (j1, j2, j3), (j1, j5, j6), (j4, j2, j6), (j4, j5, j3)
    d1 = delta_tri(j1, j2, j3)
    d2 = delta_tri(j1, j5, j6)
    d3 = delta_tri(j4, j2, j6)
    d4 = delta_tri(j4, j5, j3)

    if d1 == 0.0 or d2 == 0.0 or d3 == 0.0 or d4 == 0.0:
        return 0.0

    f = math.factorial

    # Half-integers to integers
    i1, i2, i3 = int(round(2 * j1)), int(round(2 * j2)), int(round(2 * j3))
    i4, i5, i6 = int(round(2 * j4)), int(round(2 * j5)), int(round(2 * j6))

    # Racah sum limits
    k_min = max(
        0,
        (i1 + i2 + i3) // 2,
        (i1 + i5 + i6) // 2,
        (i4 + i2 + i6) // 2,
        (i4 + i5 + i3) // 2
    )
    k_max = min(
        (i1 + i2 + i4 + i5) // 2,
        (i2 + i3 + i5 + i6) // 2,
        (i3 + i1 + i6 + i4) // 2
    )

    if k_min > k_max:
        return 0.0

    s = 0.0
    for k in range(k_min, k_max + 1):
        num = ((-1.0) ** k) * f(k + 1)
        den = (
            f(k - (i1 + i2 + i3) // 2) *
            f(k - (i1 + i5 + i6) // 2) *
            f(k - (i4 + i2 + i6) // 2) *
            f(k - (i4 + i5 + i3) // 2) *
            f((i1 + i2 + i4 + i5) // 2 - k) *
            f((i2 + i3 + i5 + i6) // 2 - k) *
            f((i3 + i1 + i6 + i4) // 2 - k)
        )
        s += num / den

    return d1 * d2 * d3 * d4 * s


def wigner_9j(
    j1: float, j2: float, j12: float,
    j3: float, j4: float, j34: float,
    j13: float, j24: float, J: float
) -> float:
    """
    Computes exact algebraic Wigner 9j symbol via Racah contraction of three 6j symbols:
      { j1  j2  j12 }
      { j3  j4  j34 } = sum_k (-1)^(2k) * (2k+1) * { j1  j2  j12 } * { j3  j4  j34 } * { j13 j24  J  }
      { j13 j24  J  }                              { j34  J    k  }   { j2   k   j24 }   {  k   j1  j3 }
    """
    # Maximum possible k
    k_max = j1 + j2 + j3 + j4 + j12 + j34 + j13 + j24 + J

    val_9j = 0.0
    for step in range(int(round(2 * k_max)) + 1):
        k = 0.5 * step
        w1 = wigner_6j(j1, j2, j12, j34, J, k)
        if abs(w1) < 1e-12:
            continue
        w2 = wigner_6j(j3, j4, j34, j2, k, j24)
        if abs(w2) < 1e-12:
            continue
        w3 = wigner_6j(j13, j24, J, k, j1, j3)
        if abs(w3) < 1e-12:
            continue
        phase = (-1.0) ** int(round(2.0 * k))
        val_9j += phase * (2.0 * k + 1.0) * w1 * w2 * w3

    return val_9j


def calculate_ls_to_jj_recoupling(
    l1: int, s1: float, j1: float,
    l2: int, s2: float, j2: float,
    L: int, S: int, J: int
) -> Dict[str, Any]:
    """
    Computes exact transformation coefficient < (l1 s1)j1, (l2 s2)j2; J | (l1 l2)L, (s1 s2)S; J >.
    """
    w9j = wigner_9j(float(l1), s1, j1, float(l2), s2, j2, float(L), float(S), float(J))

    prefactor = math.sqrt(
        (2.0 * j1 + 1.0) * (2.0 * j2 + 1.0) * (2.0 * L + 1.0) * (2.0 * S + 1.0)
    )
    bracket = prefactor * w9j

    return {
        "orbitals_1": f"l1={l1}, s1={s1}, j1={j1}",
        "orbitals_2": f"l2={l2}, s2={s2}, j2={j2}",
        "coupled_L_S_J": f"L={L}, S={S}, J={J}",
        "wigner_9j_symbol": round(w9j, 6),
        "recoupling_coefficient": round(bracket, 6),
        "recoupling_probability": round(bracket ** 2, 6)
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   WIGNER 9j SYMBOL & L-S TO j-j RECOUPLING COEFFICIENT ANALYZER")
    lines.append("=" * 72)

    lines.append(" 9j SYMBOL ARRAY CONFIGURATION:")
    lines.append(f"   Row 1 : [ {summary['j1']:<4} {summary['j2']:<4} {summary['j12']:<4} ]")
    lines.append(f"   Row 2 : [ {summary['j3']:<4} {summary['j4']:<4} {summary['j34']:<4} ]")
    lines.append(f"   Row 3 : [ {summary['j13']:<4} {summary['j24']:<4} {summary['J']:<4} ]")
    lines.append("-" * 72)
    lines.append(f" CALCULATED WIGNER 9j VALUE        : {summary['wigner_9j_value']:.6f}")
    lines.append("-" * 72)

    if "recoupling" in summary:
        rec = summary["recoupling"]
        lines.append(" L-S TO j-j SHELL MODEL RECOUPLING BRACKET:")
        lines.append(f"   Single-Particle 1              : {rec['orbitals_1']}")
        lines.append(f"   Single-Particle 2              : {rec['orbitals_2']}")
        lines.append(f"   Total Coupled Channel          : {rec['coupled_L_S_J']}")
        lines.append(f"   Recoupling Bracket <jj | LS; J>: {rec['recoupling_coefficient']:+.6f}")
        lines.append(f"   Weight / Probability           : {rec['recoupling_probability']*100:.2f}%")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Wigner 9j symbols govern the recoupling of four angular momenta.")
    lines.append("   - Transforms central/tensor two-body forces between L-S and j-j schemes.")
    lines.append("   - Essential algebraic foundation for microscopic shell-model and transfer codes.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Wigner 9j Symbol & L-S to j-j Recoupling Calculator."
    )
    parser.add_argument("--j1", type=float, default=1.0, help="j1 (default: 1.0)")
    parser.add_argument("--j2", type=float, default=0.5, help="j2 (default: 0.5)")
    parser.add_argument("--j12", type=float, default=1.5, help="j12 (default: 1.5)")
    parser.add_argument("--j3", type=float, default=1.0, help="j3 (default: 1.0)")
    parser.add_argument("--j4", type=float, default=0.5, help="j4 (default: 0.5)")
    parser.add_argument("--j34", type=float, default=1.5, help="j34 (default: 1.5)")
    parser.add_argument("--j13", type=float, default=2.0, help="j13 (default: 2.0)")
    parser.add_argument("--j24", type=float, default=1.0, help="j24 (default: 1.0)")
    parser.add_argument("-J", "--total-j", type=float, default=2.0, help="Total J (default: 2.0)")
    parser.add_argument("--recouple-demo", action="store_true", help="Run classic (p3/2)^2 to L=2, S=0 benchmark")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    val_9j = wigner_9j(args.j1, args.j2, args.j12, args.j3, args.j4, args.j34, args.j13, args.j24, args.total_j)

    summary = {
        "j1": args.j1, "j2": args.j2, "j12": args.j12,
        "j3": args.j3, "j4": args.j4, "j34": args.j34,
        "j13": args.j13, "j24": args.j24, "J": args.total_j,
        "wigner_9j_value": round(val_9j, 6)
    }

    if args.recouple_demo or (args.j1 == 1.0 and args.j2 == 0.5):
        # Benchmark: two p-nucleons (l1=1, s1=1/2 -> j1=3/2), (l2=1, s2=1/2 -> j2=3/2) to L=2, S=0, J=2
        rec = calculate_ls_to_jj_recoupling(1, 0.5, 1.5, 1, 0.5, 1.5, 2, 0, 2)
        summary["recoupling"] = rec

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
