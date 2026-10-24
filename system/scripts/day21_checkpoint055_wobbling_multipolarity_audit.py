#!/usr/bin/env python3
"""Quantitative comparative audit of 135Pr wobbling multipolarity and branching.

Contrasts:
1. Matta 2015: large mixing ratio |delta| > 1 (E2 fractions 60.6% and 70.3%) from angular distribution fits;
2. Lv 2022: joint P-Rac measurement locking small root |delta| < 1 (M1 fractions 81.9% to 91.2%);
3. Branching ratio B(E2; 747)/B(E2; 526) = 0.7(+0.7/-0.5) violates wobbling selection rules;
4. Formal correction: clarifies that neither paper measured level lifetimes tau or absolute B(E2) in W.u.
"""
import json
from pathlib import Path

def audit():
    transitions = [
        {
            "energy_keV": 747.3,
            "initial_state": "17/2-",
            "final_state": "15/2-",
            "matta_2015": {
                "delta": -1.24,
                "delta_err": 0.13,
                "E2_fraction": 1.24**2 / (1 + 1.24**2),
                "M1_fraction": 1 / (1 + 1.24**2),
                "asymmetry": 0.047
            },
            "lv_2022": {
                "delta": -0.47,
                "delta_err_pos": 0.09,
                "delta_err_neg": 0.22,
                "E2_fraction": 0.47**2 / (1 + 0.47**2),
                "M1_fraction": 1 / (1 + 0.47**2),
                "polarization_P": 0.04,
                "Rac": 0.37
            }
        },
        {
            "energy_keV": 813.2,
            "initial_state": "21/2-",
            "final_state": "19/2-",
            "matta_2015": {
                "delta": -1.54,
                "delta_err": 0.09,
                "E2_fraction": 1.54**2 / (1 + 1.54**2),
                "M1_fraction": 1 / (1 + 1.54**2),
                "asymmetry": 0.054
            },
            "lv_2022": {
                "delta": -0.37,
                "delta_err_pos": 0.10,
                "delta_err_neg": 0.14,
                "E2_fraction": 0.37**2 / (1 + 0.37**2),
                "M1_fraction": 1 / (1 + 0.37**2),
                "polarization_P": -0.03,
                "Rac": 0.48,
                "BE2_out_over_in": 0.12
            }
        },
        {
            "energy_keV": 450.2,
            "initial_state": "19/2-",
            "final_state": "17/2-",
            "matta_2015": None,
            "lv_2022": {
                "delta": -0.31,
                "delta_err_pos": 0.10,
                "delta_err_neg": 0.13,
                "E2_fraction": 0.31**2 / (1 + 0.31**2),
                "M1_fraction": 1 / (1 + 0.31**2),
                "polarization_P": -0.07,
                "Rac": 0.49
            }
        }
    ]

    branching_check = {
        "ratio_BE2_747_over_526": {
            "value": 0.7,
            "err_pos": 0.7,
            "err_neg": 0.5,
            "pure_wobbling_expectation": ">> 1 (decay to signature partner forbidden)",
            "physical_implication": "comparable transition strength to signature partner band directly contradicts pure 1-phonon wobbling selection rules"
        }
    }

    evidence_boundary_corrections = {
        "absolute_lifetimes_measured": False,
        "absolute_BE2_in_Wu_measured": False,
        "correction_of_prior_draft": "Prior claim that B(E2; 747) < 0.05 W.u. was ungrounded in primary text; Lv 2022 refutation rests on M1 dominance (82-91%) and finite B(E2; 747)/B(E2; 526) branching, not on absolute lifetime measurement in W.u."
    }

    return {
        "scope": "135Pr multipole mixing ratio and wobbling selection rule comparative audit",
        "transitions": transitions,
        "branching_check": branching_check,
        "evidence_boundary_corrections": evidence_boundary_corrections,
        "reproducibility": {
            "matta_747_E2_dominant": transitions[0]["matta_2015"]["E2_fraction"] > 0.5,
            "lv_747_M1_dominant": transitions[0]["lv_2022"]["M1_fraction"] > 0.8,
            "lv_813_M1_dominant": transitions[1]["lv_2022"]["M1_fraction"] > 0.85,
            "lv_450_M1_dominant": transitions[2]["lv_2022"]["M1_fraction"] > 0.9
        },
        "scientific_certification": False
    }

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    out_file = root / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/wobbling-multipolarity-audit-055.json'
    res = audit()
    out_file.write_text(json.dumps(res, ensure_ascii=False, indent=2) + chr(10))
    print(json.dumps({'output': str(out_file.relative_to(root)), 'transitions': len(res['transitions']), 'matta_747_E2': round(res['transitions'][0]['matta_2015']['E2_fraction'], 3), 'lv_747_M1': round(res['transitions'][0]['lv_2022']['M1_fraction'], 3)}, ensure_ascii=False))
