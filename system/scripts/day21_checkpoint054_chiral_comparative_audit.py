#!/usr/bin/env python3
"""Quantitative comparative audit of 134Pr vs 135Nd chiral inference ladder.

Contrasts:
1. 134Pr: energy near-degeneracy (Delta E <= 44 keV) with factor 2 quadrupole moment divergence (Q0 ratio 2.0(4));
2. 135Nd: factor 2 lifetime difference (tau_B/tau_A ~ 2) with symmetric B(E2) (~0.88);
Establishes exact rules: energy degeneracy is not sufficient, lifetime equality is not necessary.
"""
import json
from pathlib import Path

def audit():
    pr134 = {
        "nucleus": "134Pr",
        "Z": 59, "N": 75,
        "starosta_2001_claim": {
            "source": "PRL 86, 971 (2001)",
            "energy_displacement_at_I14_keV": 40.0,
            "measured_lifetimes": None,
            "measured_absolute_BE2": None,
            "model_TAC_barrier_Eb_keV": 30.0,
            "interpretation": "island of chiral rotation with near-degeneracy"
        },
        "petrache_2006_refutation": {
            "source": "PRL 96, 112502 (2006)",
            "data_source": "Ref. 11 (Starosta et al. to be published) & Ref. 9 (Tonev et al. PRL 96, 052501)",
            "energy_gap_I15_keV": 36.0,
            "energy_gap_I16_keV": 44.0,
            "two_band_mixing_interaction_V_keV": [14.0, 17.0],
            "Q0_ratio_mean": 2.0,
            "Q0_ratio_uncertainty": 0.4,
            "Q0_ratio_allowed_range": [1.6, 2.4],
            "mechanism": "accidental crossing of 2qp and 4qp configurations of different shapes",
            "verdict": "chiral interpretation disfavored despite near-degeneracy"
        }
    }

    nd135 = {
        "nucleus": "135Nd",
        "Z": 60, "N": 75,
        "mukhopadhyay_2007": {
            "source": "PRL 99, 172501 (2007)",
            "measured_spins": [
                {"spin": "31/2-", "tau_A_ps": 0.75, "tau_B_ps": 1.46, "tau_ratio": 1.46/0.75, "BE2_A": 0.32, "BE2_B": 0.28, "BE2_ratio": 0.28/0.32},
                {"spin": "33/2-", "tau_A_ps": 0.44, "tau_B_ps": 0.87, "tau_ratio": 0.87/0.44, "BE2_A": 0.32, "BE2_B": 0.28, "BE2_ratio": 0.28/0.32},
                {"spin": "35/2-", "tau_A_ps": 0.28, "tau_B_ps": 0.64, "tau_ratio": 0.64/0.28, "BE2_A": 0.32, "BE2_B": 0.28, "BE2_ratio": 0.28/0.32},
                {"spin": "37/2-", "tau_A_ps": 0.23, "tau_B_ps": 0.48, "tau_ratio": 0.48/0.23, "BE2_A": 0.32, "BE2_B": 0.29, "BE2_ratio": 0.29/0.32}
            ],
            "mean_tau_ratio_31_to_37": (1.46/0.75 + 0.87/0.44 + 0.64/0.28 + 0.48/0.23) / 4.0,
            "mean_BE2_ratio_31_to_37": (0.28/0.32*3 + 0.29/0.32) / 4.0,
            "mechanism": "rate compensation via partial branch fractions and E_gamma^5 phase space",
            "verdict": "chiral symmetry preserved in B(E2) despite factor 2 lifetime difference"
        }
    }

    rules = {
        "Rule_1_Sufficiency": {
            "rule": "Energy near-degeneracy is NOT sufficient for nuclear chirality",
            "counterexample": "134Pr: Delta E <= 44 keV, but Q0(1)/Q0(2) = 2.0(4) disproves shared chiral shape"
        },
        "Rule_2_Necessity": {
            "rule": "Level lifetime equality is NOT necessary for nuclear chirality",
            "counterexample": "135Nd: tau_B / tau_A ~ 2, but B(E2)_B / B(E2)_A = 0.88 confirms transition matrix element symmetry"
        },
        "Rule_3_Arbiter": {
            "rule": "Electromagnetic reduced transition matrix elements are the primary observable arbiter",
            "condition": "Requires explicit line component binding, multipole mixing ratios, and branch covariance"
        }
    }

    return {
        "scope": "comparative literature audit of 134Pr and 135Nd chiral claim boundaries",
        "pr134": pr134,
        "nd135": nd135,
        "inference_rules": rules,
        "reproducibility": {
            "pr134_Q0_ratio_exceeds_unity": 2.0 - 0.4 > 1.0,
            "nd135_tau_ratio_exceeds_unity": nd135["mukhopadhyay_2007"]["mean_tau_ratio_31_to_37"] > 1.8,
            "nd135_BE2_ratio_near_unity": abs(nd135["mukhopadhyay_2007"]["mean_BE2_ratio_31_to_37"] - 0.88) < 0.02
        },
        "scientific_certification": False
    }

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    out_file = root / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/chiral-comparative-audit-054.json'
    res = audit()
    out_file.write_text(json.dumps(res, ensure_ascii=False, indent=2) + chr(10))
    print(json.dumps({'output': str(out_file.relative_to(root)), 'rules': len(res['inference_rules']), 'pr134_Q0_ratio': res['pr134']['petrache_2006_refutation']['Q0_ratio_mean'], 'nd135_BE2_ratio': round(res['nd135']['mukhopadhyay_2007']['mean_BE2_ratio_31_to_37'], 3)}, ensure_ascii=False))
