#!/usr/bin/env python3
"""
in_beam_array_coincidence_efficiency_angular_matrix_inverter.py
==============================================================
In-Beam Multi-Detector Array Gamma-Gamma Coincidence Absolute Efficiency Matrix,
Angular Correlation Modulation & Geometric Attenuation Inversion Suite.

Physics Formulation:
--------------------
1. True Gamma-Gamma Coincidence Absolute Efficiency:
   Based on 吴治华《原子核物理实验方法》第 10 章 §10.4–10.5 (pp. 265–285), 汪晓莲《粒子探测技术》第 5 章,
   朱永生《实验物理中的概率和统计》第 6 章, and K. Debertin & R. G. Helmer (1988):
   In a multi-detector array of M_det crystals, the net measured coincidence yield between cascade
   transitions gamma_1 and gamma_2 is:
     N_12 = N_0 * b_1 * b_2 * eps_coin(E_1, E_2).
   The true coincidence efficiency is NOT merely the scalar product of single-photon total efficiencies!

2. Directional Correlation Weighted Sum over Detector Pairs:
   Each detector pair (i, j) subtends a mutual spatial angle theta_ij:
     cos(theta_ij) = sin(theta_i) * sin(theta_j) * cos(phi_i - phi_j) + cos(theta_i) * cos(theta_j).
   The true array coincidence efficiency is a sum weighted by the attenuated directional correlation W(theta_ij):
     eps_coin(E_1, E_2) = sum_{i=1}^{M_det} sum_{j != i}^{M_det} eps_i(E_1) * eps_j(E_2) * W(theta_ij)
   where:
     W(theta) = 1 + [ Q_2(E_1) * Q_2(E_2) * A_2 ] * P_2(cos theta) + [ Q_4(E_1) * Q_4(E_2) * A_4 ] * P_4(cos theta)
     and Q_k are the finite solid-angle Rose attenuation factors.

3. Geometric Modulation Factor F_geom:
   Compared to the naive unweighted scalar product eps_naive = (sum eps_i) * (sum eps_j) - sum (eps_i * eps_j),
   the geometric modulation ratio is:
     F_geom = eps_coin(E_1, E_2) / eps_naive.
   For stretched E2-E2 cascades (A_2 ~ +0.102, A_4 ~ +0.009), the forward/backward angular enhancement
   modulates the coincidence efficiency by 5% - 25% depending on array geometry!
   Ignoring this effect introduces direct systematic error into extracted branching ratios b_1 * b_2.
"""

import sys
import json
import math
import argparse
import numpy as np
import scipy.special as sp


PRESETS = {
    "12_clover_array_60Co_cascade": {
        "description": "12-Clover HPGe array (48 crystals) for 60Co 1173-1332 keV E2-E2 cascade (Debertin 1988)",
        "array_name": "12-Clover Array (48-crystal geometry)",
        "E1_keV": 1173.2,
        "E2_keV": 1332.5,
        "A2_coef": 0.1020,
        "A4_coef": 0.0090,
        "Q2_factor": 0.965,
        "Q4_factor": 0.890,
        "detector_rings": [
            {"theta_deg": 45.0, "phi_deg": 0.0, "eff_E1": 0.0035, "eff_E2": 0.0031},
            {"theta_deg": 45.0, "phi_deg": 90.0, "eff_E1": 0.0035, "eff_E2": 0.0031},
            {"theta_deg": 45.0, "phi_deg": 180.0, "eff_E1": 0.0035, "eff_E2": 0.0031},
            {"theta_deg": 45.0, "phi_deg": 270.0, "eff_E1": 0.0035, "eff_E2": 0.0031},
            {"theta_deg": 90.0, "phi_deg": 45.0, "eff_E1": 0.0036, "eff_E2": 0.0032},
            {"theta_deg": 90.0, "phi_deg": 135.0, "eff_E1": 0.0036, "eff_E2": 0.0032},
            {"theta_deg": 90.0, "phi_deg": 225.0, "eff_E1": 0.0036, "eff_E2": 0.0032},
            {"theta_deg": 90.0, "phi_deg": 315.0, "eff_E1": 0.0036, "eff_E2": 0.0032},
            {"theta_deg": 135.0, "phi_deg": 0.0, "eff_E1": 0.0035, "eff_E2": 0.0031},
            {"theta_deg": 135.0, "phi_deg": 90.0, "eff_E1": 0.0035, "eff_E2": 0.0031},
            {"theta_deg": 135.0, "phi_deg": 180.0, "eff_E1": 0.0035, "eff_E2": 0.0031},
            {"theta_deg": 135.0, "phi_deg": 270.0, "eff_E1": 0.0035, "eff_E2": 0.0031}
        ]
    },
    "in_beam_134Ce_stretched_quadrupole_cascade": {
        "description": "In-beam 134Ce 4+ -> 2+ -> 0+ cascade (638 - 409 keV) in HPGe array",
        "array_name": "In-Beam High-Spin Spectrometer",
        "E1_keV": 638.0,
        "E2_keV": 409.0,
        "A2_coef": 0.1020,
        "A4_coef": 0.0090,
        "Q2_factor": 0.950,
        "Q4_factor": 0.860,
        "detector_rings": [
            {"theta_deg": 37.0, "phi_deg": 0.0, "eff_E1": 0.0052, "eff_E2": 0.0071},
            {"theta_deg": 37.0, "phi_deg": 120.0, "eff_E1": 0.0052, "eff_E2": 0.0071},
            {"theta_deg": 37.0, "phi_deg": 240.0, "eff_E1": 0.0052, "eff_E2": 0.0071},
            {"theta_deg": 90.0, "phi_deg": 0.0, "eff_E1": 0.0055, "eff_E2": 0.0074},
            {"theta_deg": 90.0, "phi_deg": 90.0, "eff_E1": 0.0055, "eff_E2": 0.0074},
            {"theta_deg": 90.0, "phi_deg": 180.0, "eff_E1": 0.0055, "eff_E2": 0.0074},
            {"theta_deg": 90.0, "phi_deg": 270.0, "eff_E1": 0.0055, "eff_E2": 0.0074},
            {"theta_deg": 143.0, "phi_deg": 0.0, "eff_E1": 0.0052, "eff_E2": 0.0071},
            {"theta_deg": 143.0, "phi_deg": 120.0, "eff_E1": 0.0052, "eff_E2": 0.0071},
            {"theta_deg": 143.0, "phi_deg": 240.0, "eff_E1": 0.0052, "eff_E2": 0.0071}
        ]
    },
    "isotropic_unpolarized_reference": {
        "description": "Isotropic unpolarized reference cascade (A2 = A4 = 0, exact baseline)",
        "array_name": "Isotropic Calibration Array",
        "E1_keV": 500.0,
        "E2_keV": 500.0,
        "A2_coef": 0.0,
        "A4_coef": 0.0,
        "Q2_factor": 1.0,
        "Q4_factor": 1.0,
        "detector_rings": [
            {"theta_deg": 90.0, "phi_deg": 0.0, "eff_E1": 0.010, "eff_E2": 0.010},
            {"theta_deg": 90.0, "phi_deg": 180.0, "eff_E1": 0.010, "eff_E2": 0.010}
        ]
    }
}


def calculate_mutual_pair_angle(det1, det2):
    """
    Calculates mutual spatial opening angle theta_ij between detector 1 and detector 2.
    """
    th1 = math.radians(det1["theta_deg"])
    ph1 = math.radians(det1["phi_deg"])
    th2 = math.radians(det2["theta_deg"])
    ph2 = math.radians(det2["phi_deg"])

    cos_theta = math.sin(th1) * math.sin(th2) * math.cos(ph1 - ph2) + math.cos(th1) * math.cos(th2)
    cos_theta = float(np.clip(cos_theta, -1.0, 1.0))
    theta_rad = math.acos(cos_theta)
    return theta_rad, cos_theta


def evaluate_directional_correlation_weight(cos_theta, A2, A4, Q2, Q4):
    """
    Evaluates attenuated directional correlation W(theta).
    """
    p2 = float(sp.legendre(2)(cos_theta))
    p4 = float(sp.legendre(4)(cos_theta))
    w_val = 1.0 + (Q2 * A2) * p2 + (Q4 * A4) * p4
    return float(max(0.01, w_val))


def calculate_array_coincidence_efficiency(detectors, A2, A4, Q2, Q4):
    """
    Integrates all detector pairs to calculate true coincidence efficiency and geometric modulation.
    """
    M_det = len(detectors)
    eps_coin_total = 0.0
    eps_naive_total = 0.0

    pair_details = []

    for i in range(M_det):
        d_i = detectors[i]
        eff1 = d_i["eff_E1"]
        for j in range(M_det):
            if i == j:
                continue  # True coincidence requires distinct crystals
            d_j = detectors[j]
            eff2 = d_j["eff_E2"]

            th_rad, cos_th = calculate_mutual_pair_angle(d_i, d_j)
            w_weight = evaluate_directional_correlation_weight(cos_th, A2, A4, Q2, Q4)

            coin_term = eff1 * eff2 * w_weight
            naive_term = eff1 * eff2

            eps_coin_total += coin_term
            eps_naive_total += naive_term

            if i < j:
                pair_details.append({
                    "pair": f"({i+1}, {j+1})",
                    "angle_deg": float(math.degrees(th_rad)),
                    "W_weight": float(w_weight),
                    "pair_efficiency": float(coin_term * 2.0)
                })

    geom_modulation_F = (eps_coin_total / max(1e-15, eps_naive_total))
    modulation_bias_pct = (geom_modulation_F - 1.0) * 100.0

    return {
        "num_detectors": int(M_det),
        "num_detector_pairs": int(M_det * (M_det - 1)),
        "true_coincidence_efficiency": float(eps_coin_total),
        "naive_scalar_efficiency": float(eps_naive_total),
        "geometric_modulation_factor_F": float(geom_modulation_F),
        "angular_correlation_bias_pct": float(modulation_bias_pct),
        "sample_pairs": pair_details[:8]
    }


def run_coincidence_matrix_analysis(array_name, E1, E2, A2, A4, Q2, Q4, detectors):
    """
    Complete execution pipeline for array coincidence efficiency matrix analysis.
    """
    res = calculate_array_coincidence_efficiency(detectors, A2, A4, Q2, Q4)
    return {
        "array_name": array_name,
        "cascade_parameters": {
            "E1_keV": float(E1),
            "E2_keV": float(E2),
            "A2_coef": float(A2),
            "A4_coef": float(A4),
            "Q2_attenuation": float(Q2),
            "Q4_attenuation": float(Q4)
        },
        "coincidence_results": res
    }


def format_text_report(res, title="In-Beam Array Coincidence Efficiency Matrix Inverter"):
    arr = res["array_name"]
    cas = res["cascade_parameters"]
    cr = res["coincidence_results"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Array: {arr} (M_det = {cr['num_detectors']}, Pairs = {cr['num_detector_pairs']})")
    lines.append("=" * 76)
    lines.append(f"Cascade: E1 = {cas['E1_keV']:.1f} keV, E2 = {cas['E2_keV']:.1f} keV | Correlation: A2 = {cas['A2_coef']:+.4f}, A4 = {cas['A4_coef']:+.4f}")
    lines.append(f"Finite Solid Angle Attenuation  : Q2 = {cas['Q2_attenuation']:.3f}, Q4 = {cas['Q4_attenuation']:.3f}")
    lines.append("-" * 76)
    lines.append("Array Coincidence Efficiency Integration:")
    lines.append(f"  True Coincidence Efficiency eps : {cr['true_coincidence_efficiency']:10.4e} ({cr['true_coincidence_efficiency']*1e4:.3f} x 10^-4)")
    lines.append(f"  Naive Unweighted Efficiency     : {cr['naive_scalar_efficiency']:10.4e} ({cr['naive_scalar_efficiency']*1e4:.3f} x 10^-4)")
    lines.append(f"  Geometric Modulation Factor F   : F_geom = {cr['geometric_modulation_factor_F']:.4f}")
    lines.append(f"  Angular Correlation Mod. Bias   : {cr['angular_correlation_bias_pct']:+5.2f}% ({'Enhanced' if cr['angular_correlation_bias_pct'] > 0 else 'Suppressed'})")
    lines.append("-" * 76)
    lines.append("Sample Pair Angular Distribution Weights W(theta_ij):")
    lines.append("  Pair (i, j)    Opening Angle    W(theta_ij)    Pair Coincidence eps")
    for p in cr["sample_pairs"]:
        lines.append(f"    {p['pair']:10}      {p['angle_deg']:5.1f} deg         {p['W_weight']:.4f}           {p['pair_efficiency']:10.4e}")
    lines.append("-" * 76)
    lines.append("Experimental Takeaway: Directional correlation modulates total array coincidence")
    lines.append("yield by several percent; must be included for precision branching ratio measurements.")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Array Gamma-Gamma Coincidence Efficiency Matrix Inverter."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        arr = p["array_name"]
        e1 = p["E1_keV"]
        e2 = p["E2_keV"]
        a2 = p["A2_coef"]
        a4 = p["A4_coef"]
        q2 = p["Q2_factor"]
        q4 = p["Q4_factor"]
        dets = p["detector_rings"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_coincidence_matrix_analysis(
        array_name=arr,
        E1=e1, E2=e2,
        A2=a2, A4=a4,
        Q2=q2, Q4=q4,
        detectors=dets
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
