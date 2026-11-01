#!/usr/bin/env python3
"""
isovector_giant_resonance_splitting_calculator.py
=================================================
Nuclear Isovector Giant Resonance (IVGMR, IVGDR) Isospin Splitting (T_>, T_<) &
Lane Symmetry Potential Analyzer.

Physics & Formulation:
----------------------
1. Isovector Operator Isospin Clebsch-Gordan Coupling:
   Operating on parent ground state |T_0, T_0> (where T_0 = (N - Z)/2):
   Isovector operator (Delta_T = 1, Delta_Tz = 0) couples to two branches:
     - T_< = T_0     (main isospin branch)
     - T_> = T_0 + 1 (upper isospin branch)

2. Lane Symmetry Potential Energy Splitting Delta_E_T:
   Energy difference between T_> and T_< states:
     Delta_E_T = E(T_0 + 1) - E(T_0) = (V_1 / A) * (T_0 + 1)
   where V_1 ~ 60 - 100 MeV is the Lane potential strength.

3. Clebsch-Gordan Strength Ratio & Pauli Blocking:
   Ratio of transition strengths:
     S(T_>) / S(T_<) = (1 / T_0) * [ 1 - 1.5 * (T_0 / A) ]
   Fraction of total strength in upper T_> branch:
     Fraction(T_>) ~ 1 / (T_0 + 1)
   - In light N ~ Z nuclei (T_0 ~ 1): T_> holds ~ 50% of cross section.
   - In heavy neutron-rich nuclei (208Pb, T_0 = 22): T_> holds only ~ 4.3%!

4. Supported Resonances:
   - IVGDR (Isovector Giant Dipole, L=1, S=0): E_centroid ~ 78 * A^(-1/3) MeV.
   - IVGMR (Isovector Giant Monopole, L=0, S=0): E_centroid ~ 170 * A^(-1/3) MeV.

References:
  - S. Fallieros, B. Goulard, and R. H. Venter, Phys. Lett. 19, 398 (1965).
  - A. M. Lane, Nucl. Phys. 35, 676 (1962).
  - C. A. Bertulani, Introduction to Nuclear Reactions, CRC Press.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_isovector_splitting(
    Z: int,
    A: int,
    resonance_type: str = "IVGDR",
    V_1_lane_MeV: float = 65.0
) -> Dict[str, Any]:
    """
    Computes isospin splitting Delta_E_T, peak energies E(T_<) and E(T_>),
    and strength fractions for IVGDR or IVGMR.
    """
    N = A - Z
    T_0 = (N - Z) / 2.0
    A13 = A ** (1.0 / 3.0)

    if T_0 <= 0:
        return {
            "error": "Isospin splitting requires neutron excess T_0 = (N-Z)/2 > 0",
            "T_0": T_0
        }

    res_type = resonance_type.upper()
    if res_type == "IVGMR":
        # Isovector Giant Monopole Resonance
        E_centroid = 170.0 / A13
        V_lane = V_1_lane_MeV if V_1_lane_MeV != 65.0 else 85.0
    else:
        # Isovector Giant Dipole Resonance
        E_centroid = 31.2 / A13 + 20.6 / (A ** (1.0 / 6.0))
        V_lane = V_1_lane_MeV

    # Lane energy splitting Delta_E_T = (V_1 / A) * (T_0 + 1)
    Delta_E_T = (V_lane / float(A)) * (T_0 + 1.0)

    # Fractional strengths: Fraction(T_>) ~ 1 / (T_0 + 1)
    frac_T_greater = 1.0 / (T_0 + 1.0)
    frac_T_lesser = 1.0 - frac_T_greater

    # Peak positions: E_centroid = frac_lesser * E_< + frac_greater * E_>
    # E_> - E_< = Delta_E_T -> E_< = E_centroid - frac_greater * Delta_E_T
    E_lesser = E_centroid - frac_T_greater * Delta_E_T
    E_greater = E_lesser + Delta_E_T

    return {
        "A": A,
        "Z": Z,
        "N": N,
        "isospin_T0": T_0,
        "resonance_type": res_type,
        "centroid_energy_MeV": round(E_centroid, 2),
        "Lane_potential_V1_MeV": round(V_lane, 1),
        "isospin_splitting_Delta_E_MeV": round(Delta_E_T, 2),
        "T_lesser_isospin": T_0,
        "T_lesser_energy_MeV": round(E_lesser, 2),
        "T_lesser_strength_fraction_percent": round(frac_T_lesser * 100.0, 1),
        "T_greater_isospin": T_0 + 1.0,
        "T_greater_energy_MeV": round(E_greater, 2),
        "T_greater_strength_fraction_percent": round(frac_T_greater * 100.0, 1)
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   ISOVECTOR GIANT RESONANCE ISOSPIN SPLITTING (T_>, T_<) ANALYZER")
    lines.append("=" * 72)
    lines.append(f" NUCLEUS: Z = {summary['Z']}, N = {summary['N']}, A = {summary['A']} (Parent Isospin T_0 = {summary['isospin_T0']})")
    lines.append(f"   Resonance Mode                 : {summary['resonance_type']} (Centroid = {summary['centroid_energy_MeV']} MeV)")
    lines.append(f"   Lane Symmetry Potential V_1    : {summary['Lane_potential_V1_MeV']} MeV")
    lines.append(f"   Isospin Energy Splitting Delta : Delta_E_T = {summary['isospin_splitting_Delta_E_MeV']} MeV")
    lines.append("-" * 72)
    lines.append(" ISOSPIN MULTIPLET BRANCH DECOMPOSITION:")
    lines.append(f"   T_< Branch (T = {summary['T_lesser_isospin']:.1f})             : E_< = {summary['T_lesser_energy_MeV']} MeV (Share: {summary['T_lesser_strength_fraction_percent']}%)")
    lines.append(f"   T_> Branch (T = {summary['T_greater_isospin']:.1f})             : E_> = {summary['T_greater_energy_MeV']} MeV (Share: {summary['T_greater_strength_fraction_percent']}%)")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Non-zero isospin T_0 splits isovector modes into T_< and T_> branches.")
    lines.append("   - Energy separation directly measures the Lane isovector symmetry potential.")
    lines.append("   - Pauli blocking severely suppresses the T_> branch in heavy neutron-rich nuclei.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Isovector Giant Resonance Isospin Splitting Analyzer."
    )
    parser.add_argument("-Z", type=int, default=82, help="Proton number Z (default: 82 for 208Pb)")
    parser.add_argument("-A", type=int, default=208, help="Mass number A (default: 208)")
    parser.add_argument("--mode", type=str, default="IVGDR", choices=["IVGDR", "IVGMR"],
                        help="Resonance type: IVGDR (Dipole) or IVGMR (Monopole)")
    parser.add_argument("--V1", type=float, default=65.0, help="Lane potential strength in MeV (default: 65.0)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    summary = calculate_isovector_splitting(args.Z, args.A, args.mode, args.V1)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
