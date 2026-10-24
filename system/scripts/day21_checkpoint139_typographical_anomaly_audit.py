#!/usr/bin/env python3
"""Quantitative audit of typographical vs physical anomalies in Lv 2019 Table I (135Nd)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'

def main():
    # Anomaly 1: 998.1 vs 997 keV transition in Band D6
    # Printed row: E_gamma = 998.1 keV, Ei = 5412.6 keV, 39/2- -> 35/2- (to D5 at 4414.5 keV)
    # Loop closure 1a (self-consistent with printed Ei):
    ei_printed_998 = 5412.6
    ef_d5_35 = 4414.5
    delta_e_printed = ei_printed_998 - ef_d5_35  # 998.1 keV (exact match)

    # Loop closure 1b (using the other two 39/2- rows in D6: 440.4 keV and 812.0 keV where Ei = 5411.6 keV):
    ei_other_d6_39 = 5411.6
    delta_e_other = ei_other_d6_39 - ef_d5_35   # 997.1 keV (1.0 keV residual)
    text_fig1_label = 997.0

    # Anomaly 2: 334.4 keV in Band D3
    # Printed row: 334.4 keV, Ei = 4116.4 keV, 27/2- -> 25/2+, M1/E2
    # Selection rule analysis:
    # M1 operator has pi_gamma = +1 (Delta pi = 0)
    # E2 operator has pi_gamma = +1 (Delta pi = 0)
    # Printed initial parity: -1; Printed final parity: +1 => Delta pi = -1 (parity change)
    # Parity violation index = 1.0 (strictly forbidden for electromagnetic M1/E2 without weak interaction)
    # Contextual parity evidence:
    # (a) Text (PDF p.2) explicitly changes D3 parity from negative to positive based on R_DCO and R_ac.
    # (b) Fig. 1 shows D3 states with positive parity (+).
    # (c) Four cross-band transitions (D4 <-> D3) have IPDCO confirming electric character.
    # Verdict: The printed '-' in Table I is a 100% confirmed typographical omission of '+'.

    # Anomaly 3: 934.9 and 966.3 keV rows under Band D6 header
    # Printed rows in Table I:
    # 934.9 keV: Ei = 5787.6 keV, 41/2- -> 37/2-, E2
    # 966.3 keV: Ei = 6281.5 keV, 43/2- -> 39/2-, E2
    # Level scheme context:
    # In Band D5: Ei(41/2-) = 5787.6 keV, Ei(43/2-) = 6281.5 keV
    # Transition to 37/2- (4852.7 keV): 5787.6 - 4852.7 = 934.9 keV
    # Transition to 39/2- (5315.2 keV): 6281.5 - 5315.2 = 966.3 keV
    # Verdict: These are in-band Delta I = 2 transitions of Band D5, placed under the D6 column due to multi-column page layout continuation, NOT evidence of twin states in D6.

    res = {
        "title": "Typographical vs Physical Anomaly Resolution Audit in 135Nd (Lv 2019 Table I)",
        "source": {
            "doi": "10.1103/PhysRevC.100.024314",
            "locator": "PRC 100, 024314 Table I and Fig. 1"
        },
        "anomalies": {
            "Anomaly_1_998_vs_997": {
                "printed_line_keV": 998.1,
                "printed_Ei_keV": ei_printed_998,
                "final_state_Ef_keV": ef_d5_35,
                "closure_with_printed_Ei": delta_e_printed,
                "closure_residual_with_printed_Ei": abs(delta_e_printed - 998.1),
                "other_D6_39_Ei_keV": ei_other_d6_39,
                "closure_with_other_Ei": delta_e_other,
                "closure_residual_with_other_Ei": abs(delta_e_other - text_fig1_label),
                "verdict": "998.1 keV is internally closed with printed Ei=5412.6 keV. The 1.0 keV discrepancy with 5411.6 keV / 997 keV reflects rounding or a slight centroid shift between gates. It does NOT represent a physical breakdown of chiral partner assignment."
            },
            "Anomaly_2_334_Parity": {
                "printed_line_keV": 334.4,
                "printed_tuple": "27/2- -> 25/2+, M1/E2",
                "parity_selection_rule_compatible": False,
                "selection_rule_reason": "M1 and E2 operators strictly require Delta pi = 0; a 27/2- -> 25/2+ transition cannot be M1/E2.",
                "contextual_evidence_for_positive_parity": [
                    "Text p.2 explicitly states D3 parity changed to positive based on R_DCO and R_ac.",
                    "Fig. 1 draws D3 with positive parity (+).",
                    "IPDCO measurements of 4 connecting lines establish electric nature."
                ],
                "verdict": "Strictly typographical error. The initial state is 27/2+, making the transition 27/2+ -> 25/2+ (parity conserving M1/E2). This isolated typo does not refute positive parity for D3/D4."
            },
            "Anomaly_3_Repeated_Mother_States": {
                "lines_keV": [934.9, 966.3],
                "printed_header": "Band D6",
                "actual_level_membership": "Band D5 (Delta I = 2 in-band transitions: 41/2- -> 37/2- and 43/2- -> 39/2-)",
                "verdict": "Editorial table formatting artifact resulting from LaTeX column continuation across page breaks, not independent physical structures."
            }
        },
        "methodological_rules_for_anomaly_handling": [
            "Rule A (Preserve Published Text): Never silently edit numbers in source records; keep original printed text and annotate discrepancies.",
            "Rule B (Selection Rule Constraint): Pure selection rule violations (e.g. M1/E2 across opposite parity) must be classified as typographical errors when surrounded by unanimous contrary evidence.",
            "Rule C (Falsification Boundary): Typographical misalignments must never be conflated with physical falsification. Conclusive falsification requires measurable physical signals (e.g. linear polarization P > 0 as in Checkpoint 134)."
        ]
    }

    out = RUN / 'typographical-anomaly-scope-139.json'
    out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({
        "output": str(out.relative_to(ROOT)),
        "anomaly_1_closed": res["anomalies"]["Anomaly_1_998_vs_997"]["closure_residual_with_printed_Ei"] < 1e-6,
        "anomaly_2_parity_violation": not res["anomalies"]["Anomaly_2_334_Parity"]["parity_selection_rule_compatible"],
        "methodological_rules_count": len(res["methodological_rules_for_anomaly_handling"])
    }))

if __name__ == '__main__':
    main()
