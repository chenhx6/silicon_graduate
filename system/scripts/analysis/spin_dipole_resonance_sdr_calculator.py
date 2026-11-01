#!/usr/bin/env python3
"""
spin_dipole_resonance_sdr_calculator.py
=======================================
Nuclear Charge-Exchange Spin-Dipole Resonance (SDR), 0-, 1-, 2- Multipole
Decomposition & Neutron Skin Sum Rule Calculator.

Physics & Formulation:
----------------------
1. Spin-Dipole Operator S_pm(lambda):
   S_pm^mu(lambda) = sum_k r_k * [ Y_1(r_k) (x) sigma_k ]_lambda^mu * tau_pm(k)
   Multipolarities:
     lambda = 0^-: (sigma . r) mode
     lambda = 1^-: (sigma x r) mode
     lambda = 2^-: rank-2 tensor mode

2. Universal Model-Independent SDR Sum Rule:
   S_- - S_+ = sum_{lambda=0,1,2} [ B(SDR_-, lambda) - B(SDR_+, lambda) ]
             = (9 / (4 * pi)) * [ N * <r_n^2> - Z * <r_p^2> ]   (in fm^2)

3. Direct Extraction of Neutron Skin Thickness Delta_r_np:
   N * <r_n^2> - Z * <r_p^2> = (N - Z) * <r_p^2> + N * ( <r_n^2> - <r_p^2> )
   Inverting:
     <r_n^2> - <r_p^2> = (1 / N) * [ (4*pi / 9) * (S_- - S_+) - (N - Z) * <r_p^2> ]
     Delta_r_np = sqrt(<r_n^2>) - sqrt(<r_p^2>) ~ ( <r_n^2> - <r_p^2> ) / (2 * sqrt(<r_p^2>))

4. (2J + 1) Statistical Weight Multipole Splitting:
   Unperturbed macroscopic distribution:
     B(0^-) : B(1^-) : B(2^-) = 1 : 3 : 5
     Fractional shares: 1/9 (11.1%), 3/9 (33.3%), 5/9 (55.6%).

References:
  - F. Osterfeld, Rev. Mod. Phys. 64, 491 (1992).
  - H. Sagawa et al., Phys. Lett. B 247, 197 (1990).
  - A. Krasznahorkay et al., Phys. Rev. Lett. 82, 3216 (1999) [SDR in 208Pb].
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_sdr_sum_rule(
    Z: int,
    A: int,
    r_point_p_fm: Optional[float] = None,
    delta_r_np_fm: float = 0.16
) -> Dict[str, Any]:
    """
    Computes theoretical Spin-Dipole (SDR) sum rule S_- - S_+ in fm^2.
    """
    N = A - Z
    r0 = 1.20 * (A ** (1.0 / 3.0))

    # Point proton rms radius ~ 0.88 * R0 if not provided
    rp = r_point_p_fm if r_point_p_fm is not None else math.sqrt(0.6) * r0
    rn = rp + delta_r_np_fm

    rp2 = rp ** 2
    rn2 = rn ** 2

    # Universal sum rule: S_- - S_+ = (9 / 4pi) * [ N * <rn^2> - Z * <rp^2> ]
    bracket = N * rn2 - Z * rp2
    s_diff = (9.0 / (4.0 * math.pi)) * bracket

    # (2J + 1) Multipole decomposition: 0-, 1-, 2-
    # Total degeneracy sum = 1 + 3 + 5 = 9
    s_0_minus = (1.0 / 9.0) * s_diff
    s_1_minus = (3.0 / 9.0) * s_diff
    s_2_minus = (5.0 / 9.0) * s_diff

    return {
        "A": A,
        "Z": Z,
        "N": N,
        "proton_rms_radius_fm": round(rp, 3),
        "neutron_rms_radius_fm": round(rn, 3),
        "neutron_skin_fm": round(delta_r_np_fm, 3),
        "total_SDR_sum_rule_fm2": round(s_diff, 2),
        "multipole_SDR_0_minus_fm2": round(s_0_minus, 2),
        "multipole_SDR_1_minus_fm2": round(s_1_minus, 2),
        "multipole_SDR_2_minus_fm2": round(s_2_minus, 2)
    }


def invert_neutron_skin_from_sdr(
    S_minus_exp_fm2: float,
    S_plus_exp_fm2: float,
    Z: int,
    A: int,
    r_point_p_fm: Optional[float] = None
) -> Dict[str, Any]:
    """
    Inverts the neutron skin thickness Delta_r_np from experimental S_- and S_+ strength.
    """
    N = A - Z
    r0 = 1.20 * (A ** (1.0 / 3.0))
    rp = r_point_p_fm if r_point_p_fm is not None else math.sqrt(0.6) * r0
    rp2 = rp ** 2

    s_diff_exp = S_minus_exp_fm2 - S_plus_exp_fm2

    # <rn^2> - <rp^2> = (1 / N) * [ (4*pi / 9) * s_diff - (N - Z) * <rp^2> ]
    bracket = (4.0 * math.pi / 9.0) * s_diff_exp - (N - Z) * rp2
    rn2_minus_rp2 = bracket / float(N)

    rn2 = rp2 + rn2_minus_rp2
    rn = math.sqrt(max(rn2, 0.1))
    delta_r = rn - rp

    return {
        "A": A,
        "Z": Z,
        "N": N,
        "S_minus_exp_fm2": S_minus_exp_fm2,
        "S_plus_exp_fm2": S_plus_exp_fm2,
        "measured_SDR_difference_fm2": round(s_diff_exp, 2),
        "extracted_neutron_skin_fm": round(delta_r, 3),
        "neutron_rms_radius_fm": round(rn, 3),
        "proton_rms_radius_fm": round(rp, 3)
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   SPIN-DIPOLE RESONANCE (SDR) & NEUTRON SKIN SUM RULE ANALYZER")
    lines.append("=" * 72)

    if "theory" in summary:
        th = summary["theory"]
        lines.append(f" NUCLEUS: Z = {th['Z']}, N = {th['N']}, A = {th['A']}")
        lines.append(f"   Proton Radius <r_p>            : {th['proton_rms_radius_fm']} fm")
        lines.append(f"   Neutron Radius <r_n>           : {th['neutron_rms_radius_fm']} fm (Skin = {th['neutron_skin_fm']} fm)")
        lines.append(f"   Total SDR Sum Rule (S_- - S_+) : {th['total_SDR_sum_rule_fm2']} fm^2")
        lines.append("-" * 72)
        lines.append(" MULTIPOLE STRENGTH DECOMPOSITION (2J + 1):")
        lines.append(f"   J^pi = 0^- (sigma . r)         : {th['multipole_SDR_0_minus_fm2']} fm^2 (11.1%)")
        lines.append(f"   J^pi = 1^- (sigma x r)         : {th['multipole_SDR_1_minus_fm2']} fm^2 (33.3%)")
        lines.append(f"   J^pi = 2^- (tensor)            : {th['multipole_SDR_2_minus_fm2']} fm^2 (55.6%)")
        lines.append("-" * 72)

    if "experiment" in summary:
        exp = summary["experiment"]
        lines.append(" EXPERIMENTAL INVERSION OF NEUTRON SKIN:")
        lines.append(f"   Charge-Exchange S_- Strength   : {exp['S_minus_exp_fm2']} fm^2")
        lines.append(f"   Charge-Exchange S_+ Strength   : {exp['S_plus_exp_fm2']} fm^2")
        lines.append(f"   Extracted Neutron Skin Thickness: Delta_r_np = {exp['extracted_neutron_skin_fm']} fm")
        lines.append(f"   Derived Neutron Radius <r_n>   : {exp['neutron_rms_radius_fm']} fm")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - Model-independent sum rule directly constrains nuclear neutron skin.")
    lines.append("   - Spin-dipole (p,n) and (n,p) cross sections probe isovector spin-orbit modes.")
    lines.append("   - Vital calibration point for nuclear matter symmetry energy slope L.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Spin-Dipole Resonance (SDR) & Neutron Skin Analyzer."
    )
    parser.add_argument("-Z", type=int, default=82, help="Proton number Z (default: 82 for 208Pb)")
    parser.add_argument("-A", type=int, default=208, help="Mass number A (default: 208)")
    parser.add_argument("--skin", type=float, default=0.16, help="Assumed neutron skin in fm (default: 0.16)")
    parser.add_argument("--s-minus", type=float, default=None, help="Experimental S_- in fm^2")
    parser.add_argument("--s-plus", type=float, default=0.0, help="Experimental S_+ in fm^2 (default: 0.0)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    th_res = calculate_sdr_sum_rule(args.Z, args.A, delta_r_np_fm=args.skin)
    summary = {"theory": th_res}

    if args.s_minus is not None:
        exp_res = invert_neutron_skin_from_sdr(args.s_minus, args.s_plus, args.Z, args.A)
        summary["experiment"] = exp_res
    elif args.Z == 82 and args.A == 208:
        # Benchmark 208Pb: Krasznahorkay 1999 (p,n) experiment S_- ~ 1030 fm^2
        exp_res = invert_neutron_skin_from_sdr(1030.0, 0.0, 82, 208)
        summary["experiment"] = exp_res

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
