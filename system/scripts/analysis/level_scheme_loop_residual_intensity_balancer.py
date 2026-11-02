#!/usr/bin/env python3
"""
level_scheme_loop_residual_intensity_balancer.py
================================================
In-Beam Level Scheme Ritz Loop Energy Residuals, Level Intensity Balancer,
Internal Conversion (BrIcc) Correction & Reaction Side-Feeding Extractor.

Physics & Formulation:
----------------------
1. Ritz Combination Principle & Energy Closed Loops:
   In in-beam gamma spectroscopy (Wu Zhihua Ch. 10 §10.6; Radford 1995 ESCL8R):
   For any closed loop connecting nuclear levels A -> B -> C -> A:
     Delta_E_loop = sum_{forward} E_gamma_i - sum_{backward} E_gamma_j == 0.0
   The experimental loop uncertainty is:
     sigma_loop = sqrt[ sum_i (delta_E_gamma_i)^2 ]
   The normalized residual:
     Z_loop = |Delta_E_loop| / sigma_loop
   - Z_loop <= 2.0 : Physically consistent, validates gamma-ray placement.
   - Z_loop > 3.0  : Significant discrepancy (misassigned gamma ray or doublets).

2. Level Intensity Balance & Transition Total Intensity:
   Gamma detectors measure gamma photon intensity I_gamma. The total transition intensity I_tot
   includes internal conversion electrons:
     I_tot = I_gamma * (1.0 + alpha_tot)
   where alpha_tot is the total internal conversion coefficient (from BrIcc).

3. Side-Feeding Intensity from Reaction Continuum:
   For an excited nuclear level k in an in-beam fusion-evaporation reaction:
     Total Feeding from above: I_in(k) = sum_{j} I_tot(j -> k)
     Total Depopulating decay: I_out(k) = sum_{m} I_tot(k -> m)
   By conservation of intensity:
     I_in(k) + I_side(k) = I_out(k)
   The direct reaction side-feeding intensity populating level k is:
     I_side(k) = max(0.0, I_out(k) - I_in(k))
     Fractional side-feeding: f_side(k) = I_side(k) / I_out(k)
   - High-spin states have f_side ~ 50 - 90% (populated directly by prompt reaction entry).
   - Low-spin yrast states have f_side ~ 0 - 15% (predominantly fed by cascades from above).

References:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第10章 §10.6 (印刷 pp. 285–303).
  - D. C. Radford, Nucl. Instrum. Methods Phys. Res. A 361, 297 (1995) [Radware software package].
  - J. K. Tuli, *Evaluated Nuclear Structure Data File (ENSDF) Manual*, BNL-NCS-51654 (2001).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def evaluate_ritz_combination_loop(
    loop_name: str,
    forward_transitions: List[Tuple[str, float, float]],   # [(name, E_keV, err_keV), ...]
    backward_transitions: List[Tuple[str, float, float]]
) -> Dict[str, Any]:
    """
    Evaluates energy closed-loop residual Delta_E and normalized discrepancy Z_loop.
    """
    sum_fwd = sum(t[1] for t in forward_transitions)
    var_fwd = sum((t[2] ** 2) for t in forward_transitions)

    sum_bwd = sum(t[1] for t in backward_transitions)
    var_bwd = sum((t[2] ** 2) for t in backward_transitions)

    delta_E_keV = sum_fwd - sum_bwd
    sigma_loop_keV = math.sqrt(max(1e-6, var_fwd + var_bwd))
    z_score = abs(delta_E_keV) / sigma_loop_keV

    if z_score <= 1.5:
        verdict = "Excellent Consistency (Z <= 1.5 sigma)"
    elif z_score <= 3.0:
        verdict = "Acceptable Agreement (1.5 < Z <= 3.0 sigma)"
    else:
        verdict = f"Discrepant Placement (Z = {z_score:.1f} sigma > 3.0: Possible misassignment!)"

    return {
        "loop_name": loop_name,
        "forward_sum_keV": round(sum_fwd, 2),
        "backward_sum_keV": round(sum_bwd, 2),
        "delta_E_residual_keV": round(delta_E_keV, 2),
        "loop_uncertainty_keV": round(sigma_loop_keV, 2),
        "normalized_z_score": round(z_score, 2),
        "verdict": verdict
    }


def calculate_level_intensity_balance(
    levels: List[Dict[str, Any]],         # [{"level_id": "4+", "energy_keV": 678.8}, ...]
    transitions: List[Dict[str, Any]]     # [{"from": "6+", "to": "4+", "I_gamma": 85.0, "I_err": 3.0, "alpha_tot": 0.02}, ...]
) -> List[Dict[str, Any]]:
    """
    Calculates total feeding, depopulating intensity, and extracted direct side-feeding for each level.
    """
    results = []

    for lv in levels:
        lid = lv["level_id"]
        e_lvl = lv.get("energy_keV", 0.0)

        # Ingoing transitions (feeding)
        in_trans = [t for t in transitions if t["to"] == lid]
        # Outgoing transitions (depopulating)
        out_trans = [t for t in transitions if t["from"] == lid]

        total_I_in = sum(t["I_gamma"] * (1.0 + t.get("alpha_tot", 0.0)) for t in in_trans)
        total_I_out = sum(t["I_gamma"] * (1.0 + t.get("alpha_tot", 0.0)) for t in out_trans)

        net_delta_I = total_I_in - total_I_out
        side_feeding = max(0.0, total_I_out - total_I_in)
        side_fraction_pct = (side_feeding / total_I_out * 100.0) if total_I_out > 0 else 0.0

        results.append({
            "level_id": lid,
            "energy_keV": e_lvl,
            "feeding_transitions_count": len(in_trans),
            "depopulating_transitions_count": len(out_trans),
            "total_feeding_I_in": round(total_I_in, 2),
            "total_depopulating_I_out": round(total_I_out, 2),
            "net_delta_I": round(net_delta_I, 2),
            "extracted_side_feeding_I_side": round(side_feeding, 2),
            "side_feeding_fraction_pct": round(side_fraction_pct, 1)
        })

    return results


def format_text_report(loops_res: List[Dict[str, Any]], balances_res: List[Dict[str, Any]]) -> str:
    lines = [
        "=" * 76,
        "   IN-BEAM LEVEL SCHEME RITZ LOOPS & LEVEL INTENSITY BALANCER",
        "   Based on Wu Zhihua Ch. 10 §10.6, Radford (1995) & ENSDF Standards",
        "=" * 76,
        " RITZ COMBINATION PRINCIPLE ENERGY LOOP CONSISTENCY:",
        "   Loop Name            Fwd Sum (keV)   Bwd Sum (keV)   Delta_E (keV)   Z-Score   Verdict",
    ]

    for lp in loops_res:
        lines.append(f"   {lp['loop_name']:<18}  {lp['forward_sum_keV']:12.2f}    {lp['backward_sum_keV']:12.2f}    {lp['delta_E_residual_keV']:+8.2f}    {lp['normalized_z_score']:5.2f}s   {lp['verdict']}")

    lines.extend([
        "-" * 76,
        " LEVEL FEEDING, DEPOPULATING & REACTION SIDE-FEEDING BALANCE:",
        "   Level    E (keV)     I_in (feed)    I_out (decay)    Delta_I    Side-Feeding %",
    ])

    for b in balances_res:
        lines.append(f"   {b['level_id']:<6}  {b['energy_keV']:8.1f}      {b['total_feeding_I_in']:10.2f}       {b['total_depopulating_I_out']:10.2f}     {b['net_delta_I']:+8.2f}       {b['side_feeding_fraction_pct']:6.1f}%")

    lines.extend([
        "-" * 76,
        " Methodological Guidelines for Level Scheme Construction:",
        "   - Z-Score > 3.0 in a closed energy loop signals a doublet or misassigned gamma line.",
        "   - Net Delta_I < 0 indicates prompt side-feeding population directly from reaction entry.",
        "   - Low-spin yrast states typically receive <= 10% direct side-feeding (mostly fed from above).",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Level Scheme Loop Residuals & Intensity Balancer"
    )
    parser.add_argument("--preset", type=str, default="134Ce_triaxial_scheme",
                        choices=["134Ce_triaxial_scheme", "135Pr_yrast_cascade", "loop_conflict_demo"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    loops = []
    levels = []
    transitions = []

    if args.preset == "134Ce_triaxial_scheme":
        # 134Ce levels: 0+, 2+ (409.2), 4+ (1048.9), 6+ (1819.3), 2_gamma+ (965.2), 3_gamma+ (1380.0)
        levels = [
            {"level_id": "0+", "energy_keV": 0.0},
            {"level_id": "2+", "energy_keV": 409.2},
            {"level_id": "4+", "energy_keV": 1048.9},
            {"level_id": "6+", "energy_keV": 1819.3},
            {"level_id": "2_g+", "energy_keV": 965.2},
            {"level_id": "3_g+", "energy_keV": 1380.0}
        ]
        # Transitions
        transitions = [
            {"from": "6+", "to": "4+", "I_gamma": 42.0, "alpha_tot": 0.005},
            {"from": "4+", "to": "2+", "I_gamma": 78.0, "alpha_tot": 0.012},
            {"from": "2+", "to": "0+", "I_gamma": 100.0, "alpha_tot": 0.035},
            {"from": "3_g+", "to": "2_g+", "I_gamma": 15.0, "alpha_tot": 0.010},
            {"from": "3_g+", "to": "2+", "I_gamma": 8.0, "alpha_tot": 0.015},
            {"from": "2_g+", "to": "2+", "I_gamma": 22.0, "alpha_tot": 0.020},
            {"from": "2_g+", "to": "0+", "I_gamma": 12.0, "alpha_tot": 0.008}
        ]
        # Loops
        # Loop 1: 2_g+ -> 2+ -> 0+ vs 2_g+ -> 0+
        # E(2_g -> 2) = 556.0, E(2 -> 0) = 409.2 => Sum = 965.2 vs E(2_g -> 0) = 965.2
        l1_fwd = [("2_g+ -> 2+", 556.0, 0.2), ("2+ -> 0+", 409.2, 0.2)]
        l1_bwd = [("2_g+ -> 0+", 965.2, 0.3)]
        loops.append(evaluate_ritz_combination_loop("Loop 1 (2_g+ cross)", l1_fwd, l1_bwd))

        # Loop 2: 3_g+ -> 2_g+ -> 2+ vs 3_g+ -> 2+
        # E(3_g -> 2_g) = 414.8, E(2_g -> 2) = 556.0 => Sum = 970.8 vs E(3_g -> 2) = 970.8
        l2_fwd = [("3_g+ -> 2_g+", 414.8, 0.3), ("2_g+ -> 2+", 556.0, 0.2)]
        l2_bwd = [("3_g+ -> 2+", 970.8, 0.3)]
        loops.append(evaluate_ritz_combination_loop("Loop 2 (3_g+ cross)", l2_fwd, l2_bwd))

    elif args.preset == "loop_conflict_demo":
        levels = [{"level_id": "0+", "energy_keV": 0.0}, {"level_id": "2+", "energy_keV": 500.0}, {"level_id": "4+", "energy_keV": 1200.0}]
        transitions = [{"from": "4+", "to": "2+", "I_gamma": 60.0}, {"from": "2+", "to": "0+", "I_gamma": 100.0}]
        # Erroneous cross-over transition with 8 keV error
        l_fwd = [("4+ -> 2+", 700.0, 0.5), ("2+ -> 0+", 500.0, 0.5)]
        l_bwd = [("4+ -> 0+ (wrong)", 1208.0, 0.8)]
        loops.append(evaluate_ritz_combination_loop("Conflict Loop", l_fwd, l_bwd))
    else:
        levels = [{"level_id": "0+", "energy_keV": 0.0}, {"level_id": "2+", "energy_keV": 300.0}]
        transitions = [{"from": "2+", "to": "0+", "I_gamma": 100.0}]

    balances = calculate_level_intensity_balance(levels, transitions)

    if args.json:
        out = {"ritz_loops": loops, "level_intensity_balances": balances}
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(loops, balances))


if __name__ == "__main__":
    main()
