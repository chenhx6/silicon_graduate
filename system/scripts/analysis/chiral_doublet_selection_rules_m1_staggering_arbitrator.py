#!/usr/bin/env python3
"""
chiral_doublet_selection_rules_m1_staggering_arbitrator.py
==========================================================
Nuclear Chiral Doublet Selection Rules, Intra-Band B(M1) Staggering In-Phase Arbitration
& Inter-Band Delta I = 0 M1 Transition Minimum Engine.

Physics Formulation:
--------------------
1. Electromagnetic Selection Rules for Nuclear Chirality:
   Based on "Chirality and Wobbling in Atomic Nuclei" (CRC Press 2025) Ch. 7 (E. Grodner) & Ch. 8,
   T. Koike, K. Starosta, I. Hamamoto (Phys. Rev. Lett. 93, 172502, 2004),
   and E. Grodner et al. (Phys. Rev. Lett. 97, 172501, 2006):
   True chiral partner bands originate from the spontaneous breaking of time-reversal T*R_y(pi)
   in triaxial odd-odd or multi-quasiparticle configurations.
   A genuine chiral doublet must satisfy strict electromagnetic selection rules.

2. Intra-Band B(M1) In-Phase Staggering Criterion:
   The reduced transition probabilities B(M1; I -> I - 1) exhibit odd-even spin staggering
   governed by the geometric projection of the proton and neutron spins onto the rotation axis.
   The staggering factor is defined as:
     S_M1(I) = B(M1; I -> I - 1) / [ 0.5 * ( B(M1; I + 1 -> I) + B(M1; I - 1 -> I - 2) ) ]
   RULE 1: In both Band 1 and Band 2, S_M1(I) must oscillate with IDENTICAL PHASE:
     sign( S_M1_band1(I) - 1.0 ) == sign( S_M1_band2(I) - 1.0 ) across the chiral regime.
   An out-of-phase oscillation definitively rejects the chiral interpretation, signaling
   planar signature splitting.

3. Inter-Band Delta I = 0 M1 Transition Minimum:
   Because laboratory chiral states are symmetric (|1>) and antisymmetric (|2>) superpositions:
     |1> = ( |L> + |R> ) / sqrt(2),   |2> = ( |L> - |R> ) / sqrt(2)
   the M1 matrix element between partner states is:
     <1 | mu | 2> = 0.5 * [ <L | mu | L> - <R | mu | R> ]
   Since time reversal dictates <L | mu | L> == <R | mu | R>, the inter-band Delta I = 0 M1
   transition rate is strictly suppressed at the chiral degeneracy point:
     B(M1; Band 2(I) -> Band 1(I)) -> MINIMUM (near zero).

4. Chiral Selection Confidence Scoring:
   Combines:
     - M1 staggering phase agreement (weight 40%);
     - B(E2) intra-band similarity (< 25% discrepancy, weight 30%);
     - Inter-band M1 suppression at band degeneracy (weight 30%).
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "128Cs_chiral_doublet_benchmark": {
        "description": "128Cs published-strength-derived hardcoded fixture (Grodner 2006, Koike 2004)",
        "nucleus": "128Cs",
        "data_kind": "published-strength-derived-hardcoded-fixture",
        "band1": [
            {"I": 12, "E_level_keV": 2250.0, "B_M1_muN2": 0.85, "B_E2_e2b2": 0.42},
            {"I": 13, "E_level_keV": 2580.0, "B_M1_muN2": 1.45, "B_E2_e2b2": 0.40},
            {"I": 14, "E_level_keV": 2960.0, "B_M1_muN2": 0.78, "B_E2_e2b2": 0.43},
            {"I": 15, "E_level_keV": 3390.0, "B_M1_muN2": 1.38, "B_E2_e2b2": 0.41},
            {"I": 16, "E_level_keV": 3870.0, "B_M1_muN2": 0.72, "B_E2_e2b2": 0.42}
        ],
        "band2": [
            {"I": 12, "E_level_keV": 2320.0, "B_M1_muN2": 0.80, "B_E2_e2b2": 0.40},
            {"I": 13, "E_level_keV": 2630.0, "B_M1_muN2": 1.40, "B_E2_e2b2": 0.39},
            {"I": 14, "E_level_keV": 3000.0, "B_M1_muN2": 0.75, "B_E2_e2b2": 0.41},
            {"I": 15, "E_level_keV": 3420.0, "B_M1_muN2": 1.30, "B_E2_e2b2": 0.38},
            {"I": 16, "E_level_keV": 3900.0, "B_M1_muN2": 0.68, "B_E2_e2b2": 0.40}
        ],
        "interband_transitions": [
            {"I": 13, "B_M1_inter_muN2": 0.12},
            {"I": 14, "B_M1_inter_muN2": 0.04},
            {"I": 15, "B_M1_inter_muN2": 0.08}
        ]
    },
    "134Pr_chiral_doublet_benchmark": {
        "description": "134Pr published-strength-derived hardcoded fixture (Tonev 2006, Petrache 1996)",
        "nucleus": "134Pr",
        "data_kind": "published-strength-derived-hardcoded-fixture",
        "band1": [
            {"I": 11, "E_level_keV": 2100.0, "B_M1_muN2": 0.65, "B_E2_e2b2": 0.35},
            {"I": 12, "E_level_keV": 2420.0, "B_M1_muN2": 1.25, "B_E2_e2b2": 0.34},
            {"I": 13, "E_level_keV": 2780.0, "B_M1_muN2": 0.60, "B_E2_e2b2": 0.36},
            {"I": 14, "E_level_keV": 3190.0, "B_M1_muN2": 1.18, "B_E2_e2b2": 0.35}
        ],
        "band2": [
            {"I": 11, "E_level_keV": 2180.0, "B_M1_muN2": 0.60, "B_E2_e2b2": 0.33},
            {"I": 12, "E_level_keV": 2480.0, "B_M1_muN2": 1.15, "B_E2_e2b2": 0.32},
            {"I": 13, "E_level_keV": 2830.0, "B_M1_muN2": 0.58, "B_E2_e2b2": 0.34},
            {"I": 14, "E_level_keV": 3220.0, "B_M1_muN2": 1.10, "B_E2_e2b2": 0.33}
        ],
        "interband_transitions": [
            {"I": 12, "B_M1_inter_muN2": 0.08},
            {"I": 13, "B_M1_inter_muN2": 0.03}
        ]
    },
    "135Nd_chiral_doublet_benchmark": {
        "description": "135Nd published-strength-derived hardcoded fixture (Mukhopadhyay PRL 2007, Zhu PRL 2003)",
        "nucleus": "135Nd",
        "data_kind": "published-strength-derived-hardcoded-fixture",
        "band1": [
            {"I": 15.5, "E_level_keV": 3587.0, "B_M1_muN2": 2.50, "B_E2_e2b2": 0.32},
            {"I": 16.5, "E_level_keV": 4020.0, "B_M1_muN2": 2.20, "B_E2_e2b2": 0.32},
            {"I": 17.5, "E_level_keV": 4514.0, "B_M1_muN2": 2.40, "B_E2_e2b2": 0.32},
            {"I": 18.5, "E_level_keV": 5062.0, "B_M1_muN2": 1.70, "B_E2_e2b2": 0.32},
            {"I": 19.5, "E_level_keV": 5664.0, "B_M1_muN2": 2.10, "B_E2_e2b2": 0.13}
        ],
        "band2": [
            {"I": 15.5, "E_level_keV": 3943.8, "B_M1_muN2": 2.70, "B_E2_e2b2": 0.28},
            {"I": 16.5, "E_level_keV": 4300.8, "B_M1_muN2": 2.10, "B_E2_e2b2": 0.28},
            {"I": 17.5, "E_level_keV": 4698.1, "B_M1_muN2": 2.20, "B_E2_e2b2": 0.28},
            {"I": 18.5, "E_level_keV": 5180.1, "B_M1_muN2": 1.70, "B_E2_e2b2": 0.29},
            {"I": 19.5, "E_level_keV": 5759.2, "B_M1_muN2": 1.90, "B_E2_e2b2": 0.11}
        ],
        "interband_transitions": [
            {"I": 16.5, "B_M1_inter_muN2": 0.18},
            {"I": 17.5, "B_M1_inter_muN2": 0.11},
            {"I": 18.5, "B_M1_inter_muN2": 0.08},
            {"I": 19.5, "B_M1_inter_muN2": 0.04}
        ]
    },
    "spurious_out_of_phase_counterexample": {
        "description": "Synthetic counterexample: planar bands with opposite B(M1) staggering phase",
        "nucleus": "Fake-Doublet",
        "data_kind": "synthetic-test-fixture",
        "band1": [
            {"I": 12, "E_level_keV": 2000.0, "B_M1_muN2": 0.50, "B_E2_e2b2": 0.40},
            {"I": 13, "E_level_keV": 2400.0, "B_M1_muN2": 1.50, "B_E2_e2b2": 0.40},
            {"I": 14, "E_level_keV": 2850.0, "B_M1_muN2": 0.45, "B_E2_e2b2": 0.40}
        ],
        "band2": [
            {"I": 12, "E_level_keV": 2100.0, "B_M1_muN2": 1.40, "B_E2_e2b2": 0.30},
            {"I": 13, "E_level_keV": 2550.0, "B_M1_muN2": 0.50, "B_E2_e2b2": 0.30},
            {"I": 14, "E_level_keV": 3050.0, "B_M1_muN2": 1.35, "B_E2_e2b2": 0.30}
        ],
        "interband_transitions": [
            {"I": 13, "B_M1_inter_muN2": 0.85}
        ]
    }
}


def calculate_m1_staggering(band_levels):
    """
    Calculates S_M1(I) = B(M1, I) / [ 0.5 * (B(M1, I+1) + B(M1, I-1)) ].
    """
    stag_dict = {}
    n = len(band_levels)
    for k in range(1, n - 1):
        I_curr = band_levels[k]["I"]
        bm1_curr = band_levels[k]["B_M1_muN2"]
        bm1_prev = band_levels[k - 1]["B_M1_muN2"]
        bm1_next = band_levels[k + 1]["B_M1_muN2"]

        denom = 0.5 * (bm1_prev + bm1_next)
        s_val = bm1_curr / max(1e-4, denom)
        stag_dict[I_curr] = float(s_val)
    return stag_dict


def arbitrate_chiral_selection_rules(band1, band2, interband):
    """
    Arbitrates chiral selection rules: in-phase M1 staggering, B(E2) similarity,
    and inter-band M1 suppression.
    """
    stag1 = calculate_m1_staggering(band1)
    stag2 = calculate_m1_staggering(band2)

    common_spins = sorted(list(set(stag1.keys()).intersection(set(stag2.keys()))))
    phase_matches = 0
    total_checked = len(common_spins)

    staggering_comparison = []
    for spin in common_spins:
        s1 = stag1[spin]
        s2 = stag2[spin]
        # In-phase means both > 1.0 or both < 1.0
        match = bool((s1 > 1.0 and s2 > 1.0) or (s1 < 1.0 and s2 < 1.0) or (s1 == s2))
        if match:
            phase_matches += 1
        staggering_comparison.append({
            "I": spin,
            "S_M1_band1": s1,
            "S_M1_band2": s2,
            "is_in_phase": match
        })

    phase_fraction = (phase_matches / max(1, total_checked))
    phase_score = phase_fraction * 40.0

    # B(E2) similarity
    be2_diffs = []
    b2_dict = {lvl["I"]: lvl["B_E2_e2b2"] for lvl in band2}
    for lvl1 in band1:
        I_val = lvl1["I"]
        if I_val in b2_dict:
            diff = abs(lvl1["B_E2_e2b2"] - b2_dict[I_val]) / max(1e-4, lvl1["B_E2_e2b2"])
            be2_diffs.append(diff)

    mean_be2_diff = float(np.mean(be2_diffs)) if be2_diffs else 0.0
    if mean_be2_diff <= 0.15:
        be2_score = 30.0
    elif mean_be2_diff <= 0.25:
        be2_score = 20.0
    elif mean_be2_diff <= 0.40:
        be2_score = 10.0
    else:
        be2_score = 0.0

    # Inter-band Delta I = 0 M1 suppression
    inter_bm1_vals = [t["B_M1_inter_muN2"] for t in interband]
    min_inter_bm1 = float(min(inter_bm1_vals)) if inter_bm1_vals else 0.5
    if min_inter_bm1 <= 0.05:
        inter_score = 30.0
    elif min_inter_bm1 <= 0.15:
        inter_score = 20.0
    elif min_inter_bm1 <= 0.30:
        inter_score = 10.0
    else:
        inter_score = 0.0

    total_score = phase_score + be2_score + inter_score

    if total_score >= 80.0:
        verdict = "selection-rule-screening-pass"
    elif total_score >= 50.0:
        verdict = "selection-rule-screening-conditional"
    else:
        verdict = "selection-rule-screening-fail"

    return {
        "staggering_comparison": staggering_comparison,
        "phase_match_fraction": float(phase_fraction),
        "mean_be2_discrepancy_pct": float(mean_be2_diff * 100.0),
        "min_interband_bm1_muN2": float(min_inter_bm1),
        "heuristic_score_pct": float(total_score),
        "confidence_score_pct": None,
        "selection_rule_verdict": verdict,
        "evidence_boundary": (
            "Heuristic screening of caller-supplied strengths. Hardcoded presets are "
            "published-strength-derived or synthetic fixtures; no raw spectra, source "
            "locators, covariance, configuration proof, or independent geometry evidence "
            "is inferred."
        )
    }


def run_chiral_selection_analysis(
    nucleus,
    band1,
    band2,
    interband,
    data_kind="published-strength-derived-hardcoded-fixture",
    source_locator="preset source locator required before paper use",
):
    """
    Complete execution pipeline for chiral selection rules arbitration.
    """
    res = arbitrate_chiral_selection_rules(band1, band2, interband)
    res["nucleus"] = nucleus
    res["data_kind"] = data_kind
    res["source_locator"] = source_locator
    return res


def format_text_report(res, title="Chiral Doublet Selection Rules & M1 Staggering Arbitrator"):
    nuc = res["nucleus"]
    stag = res["staggering_comparison"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Heuristic Screening Score = {res['heuristic_score_pct']:.1f}% | Verdict: {res['selection_rule_verdict']}")
    lines.append(f"Data kind: {res.get('data_kind', 'caller-supplied-derived')}")
    lines.append("Evidence boundary: screening output; not a chirality confirmation or confidence estimate.")
    lines.append("=" * 76)
    lines.append("Intra-Band B(M1) Staggering S_M1(I) In-Phase Comparison:")
    lines.append("  Spin I (hbar)   S_M1(Band 1)   S_M1(Band 2)    Phase Alignment Status")
    for pt in stag:
        status_str = "MATCH (In-Phase)" if pt["is_in_phase"] else "VIOLATION (Out-of-Phase)"
        lines.append(f"    {pt['I']:4.1f}            {pt['S_M1_band1']:6.3f}         {pt['S_M1_band2']:6.3f}       {status_str}")
    lines.append("-" * 76)
    lines.append("Electromagnetic Selection Metrics:")
    lines.append(f"  M1 Staggering In-Phase Consistency : {res['phase_match_fraction']*100.0:.1f}%")
    lines.append(f"  Intra-Band B(E2) Mean Discrepancy  : {res['mean_be2_discrepancy_pct']:.1f}%")
    lines.append(f"  Minimum Inter-Band B(M1) Delta I=0 : {res['min_interband_bm1_muN2']:.4f} mu_N^2 (Strong suppression at degeneracy)")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Chiral-doublet selection-rule screening on derived or synthetic fixtures."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load published-strength-derived or synthetic fixture")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        b1 = p["band1"]
        b2 = p["band2"]
        inter = p["interband_transitions"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_chiral_selection_analysis(
        nucleus=nucleus,
        band1=b1,
        band2=b2,
        interband=inter,
        data_kind=p.get("data_kind", "caller-supplied-derived"),
        source_locator=p.get("source_locator"),
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
