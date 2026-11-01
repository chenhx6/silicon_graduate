#!/usr/bin/env python3
"""
wigner_supermultiplet_su4_calculator.py
=======================================
Wigner Supermultiplet SU(4) Symmetry, Casimir Invariants & N=Z Mass Cusp
Wigner Energy Calculator.

Physics & Formulation:
----------------------
1. Wigner SU(4) Spin-Isospin Supermultiplets (Wigner 1937):
   Combined spin-isospin group: SU(2)_spin x SU(2)_isospin in SU(4).
   Represented by partition [P, P', P''] related to spatial symmetry.
   Quadratic Casimir invariant:
     <C_2(SU(4))> = 0.5 * [ P*(P + 4) + P'*(P' + 2) + P''^2 ]

2. Ground State Partitions [P, P', P'']:
   - Even-even (T_z = |N-Z|/2 = T): [T, 0, 0]
       <C_2> = 0.5 * T * (T + 4)
   - Odd-A: [T, 1/2, +/- 1/2]
       <C_2> = 0.5 * T * (T + 4) + 0.75
   - Odd-odd (N != Z): [T, 1, 0]
       <C_2> = 0.5 * T * (T + 4) + 1.5
   - Odd-odd (N = Z, T = 0, S = 1): [1, 0, 0]
       <C_2> = 2.5

3. Wigner Energy Term in Nuclear Binding Energies:
   Explains the prominent "cusp" in nuclear masses at N = Z:
     E_W(A, T) = (a_W / A) * <C_2(SU(4))>   (a_W ~ 35 - 47 MeV)
   Phenomenological form:
     E_W(A, |N-Z|) = (W_0 / A) * |N - Z| + Delta_W(N=Z)
   Physical origin: Isoscalar (T=0, S=1) proton-neutron pairing correlation
   acting between nucleons in identical spatial orbitals.

References:
  - E. P. Wigner, Phys. Rev. 51, 106 (1937).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. I, Benjamin (1969).
  - W. Satula, D. J. Dean, J. Gary, S. Mizutori, and W. Nazarewicz, Phys. Lett. B 407, 103 (1997).
  - 卢希庭, 《原子核物理（修订版）》, 第3章 同位旋与超多重态.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_su4_casimir(Z: int, A: int) -> Dict[str, Any]:
    """
    Computes SU(4) Wigner partition [P, P', P'] and quadratic Casimir <C_2>.
    """
    N = A - Z
    T_z = abs(N - Z) / 2.0
    T = T_z  # lowest isospin for ground state

    is_even_A = (A % 2 == 0)
    is_even_Z = (Z % 2 == 0)

    if is_even_A and is_even_Z:
        # Even-even nucleus
        P, Pp, Ppp = T, 0.0, 0.0
        c2 = 0.5 * P * (P + 4.0)
        nucleus_type = "Even-Even (T, 0, 0)"
    elif not is_even_A:
        # Odd-A nucleus
        P, Pp, Ppp = T, 0.5, 0.5
        c2 = 0.5 * P * (P + 4.0) + 0.5 * Pp * (Pp + 2.0) + 0.5 * (Ppp ** 2)
        nucleus_type = "Odd-A (T, 1/2, 1/2)"
    else:
        # Odd-odd nucleus
        if N == Z:
            # Self-conjugate N=Z odd-odd (deuteron-like S=1, T=0 ground state)
            P, Pp, Ppp = 1.0, 0.0, 0.0
            c2 = 0.5 * 1.0 * (1.0 + 4.0)  # = 2.5
            nucleus_type = "Odd-Odd N=Z (1, 0, 0, Deuteron-like S=1, T=0)"
        else:
            P, Pp, Ppp = T, 1.0, 0.0
            c2 = 0.5 * P * (P + 4.0) + 0.5 * Pp * (Pp + 2.0)
            nucleus_type = "Odd-Odd N!=Z (T, 1, 0)"

    return {
        "A": A,
        "Z": Z,
        "N": N,
        "isospin_T": T,
        "nucleus_type": nucleus_type,
        "wigner_partition_P_Pp_Ppp": [round(P, 1), round(Pp, 1), round(Ppp, 1)],
        "casimir_C2": round(c2, 3)
    }


def calculate_wigner_energy(
    Z: int,
    A: int,
    a_W_MeV: float = 42.0
) -> Dict[str, Any]:
    """
    Computes Wigner energy E_W(A, T) contributing to nuclear binding energy.
    """
    su4 = calculate_su4_casimir(Z, A)
    c2 = su4["casimir_C2"]

    # Microscopic SU(4) Wigner energy
    E_wigner_su4 = (a_W_MeV / float(A)) * c2

    # Phenomenological cusp form: E_W = (W0 / A) * |N - Z|
    N = A - Z
    E_wigner_cusp = (a_W_MeV / float(A)) * abs(N - Z)
    if N == Z:
        E_wigner_cusp += (a_W_MeV / float(A)) * 1.5  # N=Z extra enhancement

    return {
        "A": A,
        "Z": Z,
        "N": N,
        "isospin_T": su4["isospin_T"],
        "nucleus_type": su4["nucleus_type"],
        "su4_partition": su4["wigner_partition_P_Pp_Ppp"],
        "su4_casimir_C2": c2,
        "wigner_energy_su4_MeV": round(E_wigner_su4, 3),
        "wigner_energy_cusp_MeV": round(E_wigner_cusp, 3),
        "is_N_equals_Z": (N == Z)
    }


def scan_isobaric_wigner_cusp(
    A: int = 48,
    a_W_MeV: float = 42.0
) -> List[Dict[str, Any]]:
    """
    Scans Wigner energy along an isobaric chain to reveal the N=Z mass cusp.
    """
    results = []
    z_center = A // 2
    for dZ in range(-6, 7):
        Z_curr = z_center + dZ
        N_curr = A - Z_curr
        if Z_curr > 0 and N_curr > 0:
            res = calculate_wigner_energy(Z_curr, A, a_W_MeV)
            results.append(res)
    return results


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   WIGNER SUPERMULTIPLET SU(4) & N=Z MASS CUSP ANALYZER")
    lines.append("=" * 72)

    we = summary["wigner_energy"]
    lines.append(f" NUCLEUS: Z = {we['Z']}, N = {we['N']}, A = {we['A']} (Isospin T = {we['isospin_T']})")
    lines.append(f"   Classification                 : {we['nucleus_type']}")
    lines.append(f"   Wigner Partition [P, P', P'']  : {we['su4_partition']}")
    lines.append(f"   SU(4) Quadratic Casimir <C_2>  : {we['su4_casimir_C2']}")
    lines.append(f"   SU(4) Microscopic Wigner Energy: {we['wigner_energy_su4_MeV']} MeV")
    lines.append(f"   Phenomenological Cusp Energy   : {we['wigner_energy_cusp_MeV']} MeV")
    lines.append(f"   Self-Conjugate N = Z Nucleus   : {we['is_N_equals_Z']}")
    lines.append("-" * 72)

    if "isobaric_scan" in summary:
        lines.append(" ISOBARIC CHAIN WIGNER CUSP PROFILE:")
        lines.append(f"   {'Z':<6} {'N':<6} {'|N-Z|':<8} {'Isospin T':<12} {'<C_2>':<10} {'E_W (MeV)':<12}")
        lines.append("   " + "-" * 54)
        for pt in summary["isobaric_scan"]:
            lines.append(f"   {pt['Z']:<6} {pt['N']:<6} {abs(pt['N']-pt['Z']):<8} {pt['isospin_T']:<12.1f} {pt['su4_casimir_C2']:<10.2f} {pt['wigner_energy_su4_MeV']:<12.3f}")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - SU(4) spin-isospin symmetry explains the non-differentiable mass cusp at N=Z.")
    lines.append("   - Isoscalar T=0 proton-neutron pairing adds extra binding for N ~ Z nuclei.")
    lines.append("   - Crucial correction term in macroscopic-microscopic mass models (FRDM, HFB).")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Wigner Supermultiplet SU(4) & N=Z Mass Cusp Calculator."
    )
    parser.add_argument("-Z", type=int, required=True, help="Proton number Z")
    parser.add_argument("-A", type=int, required=True, help="Mass number A")
    parser.add_argument("--aW", type=float, default=42.0, help="Wigner energy strength parameter in MeV (default: 42.0)")
    parser.add_argument("--scan-isobar", action="store_true", help="Scan isobaric chain across N=Z")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    we_res = calculate_wigner_energy(args.Z, args.A, args.aW)
    summary = {"wigner_energy": we_res}

    if args.scan_isobar or abs(args.A - 2 * args.Z) <= 4:
        summary["isobaric_scan"] = scan_isobaric_wigner_cusp(args.A, args.aW)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
