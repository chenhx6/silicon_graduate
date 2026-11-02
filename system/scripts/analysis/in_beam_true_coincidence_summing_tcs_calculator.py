#!/usr/bin/env python3
"""
in_beam_true_coincidence_summing_tcs_calculator.py
==================================================
In-Beam True Coincidence Summing (TCS) Summing-Out / Summing-In Correction,
Peak-to-Total Ratio & Close-Geometry Solid Angle Efficiency Analysis Suite.

Physics Formulation:
--------------------
1. True Coincidence Summing (TCS) in Close-Geometry Spectroscopy:
   Based on 吴治华《原子核物理实验方法》第 10 章 §10.5 (pp. 275–285), 汪晓莲等《粒子探测技术》第 5 章,
   and K. Debertin & R. G. Helmer (Gamma- and X-Ray Spectrometry, 1988):
   In compact high-efficiency gamma arrays (e.g. Clover HPGe crystals at distance d ~ 5 - 15 cm),
   two or more cascade photons emitted in prompt sequence within the detector resolving time
   can strike the same crystal simultaneously:
     - Summing-Out (Photopeak Loss): Gamma_1 deposits full energy while Gamma_2 simultaneously
       scatters or absorbs in the same crystal, moving the event out of the photopeak of Gamma_1.
     - Summing-In (Apparent Sum Peak): Gamma_1 and Gamma_2 both deposit full energy in the crystal,
       producing a spurious virtual peak at E_sum = E_1 + E_2.

2. Analytical Summing-Out Correction Factor C_out:
   For cascade transition Gamma_1 feeding Gamma_2:
     Observed photopeak count: N_1_obs = N_0 * b_1 * eps_p(E_1) * [ 1.0 - alpha_tot,2 ] * [ 1.0 - eps_t(E_2) * W(0) ]
   where:
     eps_p(E_1) = full-energy photopeak efficiency;
     eps_t(E_2) = total interaction efficiency (photoelectric + Compton + pair creation);
     W(0) = directional correlation factor at zero relative angle.
   The summing-out correction factor C_out >= 1.0 is:
     C_out(E_1) = N_1_true / N_1_obs = 1.0 / [ 1.0 - eps_t(E_2) * W(0) ]
   If neglected in close geometry, true gamma intensities are underestimated by 10% - 25%!

3. Virtual Summing-In Peak Yield:
   The apparent count rate in the sum peak at E_sum = E_1 + E_2:
     N_sum_in = N_0 * b_1 * b_2 * eps_p(E_1) * eps_p(E_2) * W(0).

4. Peak-to-Total (P/T) Ratio & Total Efficiency:
   Total efficiency is related to peak efficiency via the P/T ratio:
     eps_t(E) = eps_p(E) / ( P/T(E) )
   where typical HPGe P/T ratios range from 0.18 to 0.35 in the 0.5 - 2.0 MeV energy range.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "60Co_close_geometry_clover": {
        "description": "60Co calibration source in close geometry (1173.2 keV -> 1332.5 keV, d=10 cm)",
        "nucleus": "60Co",
        "cascade_pairs": [
            {"E_target_keV": 1173.2, "E_coincident_keV": 1332.5, "branching": 1.0},
            {"E_target_keV": 1332.5, "E_coincident_keV": 1173.2, "branching": 1.0}
        ],
        "peak_efficiencies": {1173.2: 0.025, 1332.5: 0.022},
        "pt_ratios": {1173.2: 0.22, 1332.5: 0.20},
        "total_decays": 1.0e6,
        "W0_correlation": 1.0
    },
    "134Ce_in_beam_cascade": {
        "description": "134Ce in-beam yrast cascade (4+ -> 2+ -> 0+, 638 keV -> 409 keV)",
        "nucleus": "134Ce",
        "cascade_pairs": [
            {"E_target_keV": 638.0, "E_coincident_keV": 409.0, "branching": 1.0},
            {"E_target_keV": 409.0, "E_coincident_keV": 638.0, "branching": 1.0}
        ],
        "peak_efficiencies": {638.0: 0.038, 409.0: 0.048},
        "pt_ratios": {638.0: 0.28, 409.0: 0.32},
        "total_decays": 5.0e5,
        "W0_correlation": 1.02
    },
    "152Eu_multi_cascade_summing": {
        "description": "152Eu complex cascade summing (122 keV -> 344 keV -> 964 keV)",
        "nucleus": "152Eu",
        "cascade_pairs": [
            {"E_target_keV": 121.8, "E_coincident_keV": 344.3, "branching": 0.28},
            {"E_target_keV": 344.3, "E_coincident_keV": 121.8, "branching": 0.28}
        ],
        "peak_efficiencies": {121.8: 0.065, 344.3: 0.052},
        "pt_ratios": {121.8: 0.42, 344.3: 0.35},
        "total_decays": 1.0e6,
        "W0_correlation": 1.0
    }
}


def calculate_total_efficiency(peak_eff, pt_ratio):
    """
    Calculates total interaction efficiency eps_t from peak efficiency and P/T ratio.
    """
    if pt_ratio <= 0:
        return peak_eff
    return min(1.0, peak_eff / pt_ratio)


def calculate_tcs_corrections(cascade_pairs, peak_effs, pt_ratios, W0=1.0, total_decays=1e6):
    """
    Calculates summing-out correction factors and virtual sum-peak counts.
    """
    results = []
    for pair in cascade_pairs:
        E_t = float(pair["E_target_keV"])
        E_c = float(pair["E_coincident_keV"])
        b = float(pair.get("branching", 1.0))

        eps_p_t = float(peak_effs.get(E_t, 0.03))
        eps_p_c = float(peak_effs.get(E_c, 0.03))

        pt_t = float(pt_ratios.get(E_t, 0.25))
        pt_c = float(pt_ratios.get(E_c, 0.25))

        eps_t_c = calculate_total_efficiency(eps_p_c, pt_c)

        # Summing-out probability = eps_t(E_coincident) * W(0)
        p_sum_out = eps_t_c * W0
        # Correction factor C_out = 1 / (1 - P_sum_out)
        if p_sum_out < 0.99:
            c_out = 1.0 / (1.0 - p_sum_out)
        else:
            c_out = 100.0

        # Observed vs True counts
        n_true = total_decays * b * eps_p_t
        n_obs = n_true * (1.0 - p_sum_out)
        pct_loss = p_sum_out * 100.0

        results.append({
            "E_target_keV": E_t,
            "E_coincident_keV": E_c,
            "peak_efficiency": eps_p_t,
            "coincident_total_efficiency": eps_t_c,
            "summing_out_loss_percent": float(pct_loss),
            "correction_factor_C_out": float(c_out),
            "true_photopeak_counts": float(n_true),
            "observed_attenuated_counts": float(n_obs)
        })

    # Evaluate summing-in peak if two transitions form a pair
    sum_peaks = []
    if len(cascade_pairs) >= 2:
        E1 = cascade_pairs[0]["E_target_keV"]
        E2 = cascade_pairs[0]["E_coincident_keV"]
        e_sum = E1 + E2
        eps1 = peak_effs.get(E1, 0.03)
        eps2 = peak_effs.get(E2, 0.03)
        n_sum_in = total_decays * eps1 * eps2 * W0
        sum_peaks.append({
            "E_sum_peak_keV": float(e_sum),
            "sum_in_yield_counts": float(n_sum_in),
            "components": [float(E1), float(E2)]
        })

    return {
        "summing_out_corrections": results,
        "summing_in_peaks": sum_peaks
    }


def run_tcs_analysis(nucleus, cascade_pairs, peak_effs, pt_ratios, W0=1.0, total_decays=1e6):
    """
    Complete execution pipeline for TCS analysis.
    """
    res = calculate_tcs_corrections(cascade_pairs, peak_effs, pt_ratios, W0, total_decays)
    res["nucleus"] = nucleus
    res["total_decays"] = float(total_decays)
    res["W0_angular_correlation"] = float(W0)
    return res


def format_text_report(res, title="In-Beam True Coincidence Summing (TCS) Engine"):
    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {res['nucleus']} | Total Cascade Decays: {res['total_decays']:.2e} | W(0) = {res['W0_angular_correlation']:.2f}")
    lines.append("=" * 76)
    lines.append("Summing-Out Photopeak Attenuation & Correction Factors:")
    lines.append("   E_target   E_coinc    eps_peak   eps_total(coinc)   Loss (%)   C_out Factor")
    for c in res["summing_out_corrections"]:
        lines.append(
            f"   {c['E_target_keV']:7.1f}   {c['E_coincident_keV']:7.1f}     {c['peak_efficiency']*100:5.2f}%        {c['coincident_total_efficiency']*100:5.2f}%       {c['summing_out_loss_percent']:5.1f}%       {c['correction_factor_C_out']:6.4f} (+{(c['correction_factor_C_out']-1)*100:4.1f}%)"
        )
    lines.append("-" * 76)
    if res["summing_in_peaks"]:
        lines.append("Virtual Summing-In Peaks:")
        for sp in res["summing_in_peaks"]:
            lines.append(f"  Sum Peak Energy: {sp['E_sum_peak_keV']:.1f} keV (from {sp['components'][0]:.1f} + {sp['components'][1]:.1f} keV)")
            lines.append(f"  Expected False Count Yield: {sp['sum_in_yield_counts']:.1f} counts")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam True Coincidence Summing (TCS) Summing-Out/In Correction Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--nucleus", type=str, default="Nucleus", help="Nucleus name")
    parser.add_argument("--e1", type=float, help="First transition energy in keV")
    parser.add_argument("--e2", type=float, help="Second transition energy in keV")
    parser.add_argument("--ep1", type=float, default=0.03, help="Peak efficiency for E1")
    parser.add_argument("--ep2", type=float, default=0.03, help="Peak efficiency for E2")
    parser.add_argument("--pt", type=float, default=0.25, help="Peak-to-total ratio")
    parser.add_argument("--w0", type=float, default=1.0, help="Zero-degree correlation factor")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        cascade_pairs = p["cascade_pairs"]
        peak_effs = p["peak_efficiencies"]
        pt_ratios = p["pt_ratios"]
        total_decays = p.get("total_decays", 1e6)
        W0 = p.get("W0_correlation", 1.0)
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.e1 and args.e2:
        nucleus = args.nucleus
        cascade_pairs = [
            {"E_target_keV": args.e1, "E_coincident_keV": args.e2, "branching": 1.0},
            {"E_target_keV": args.e2, "E_coincident_keV": args.e1, "branching": 1.0}
        ]
        peak_effs = {args.e1: args.ep1, args.e2: args.ep2}
        pt_ratios = {args.e1: args.pt, args.e2: args.pt}
        total_decays = 1e6
        W0 = args.w0
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_tcs_analysis(
        nucleus=nucleus,
        cascade_pairs=cascade_pairs,
        peak_effs=peak_effs,
        pt_ratios=pt_ratios,
        W0=W0,
        total_decays=total_decays
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
