#!/usr/bin/env python3
"""Quantitative comparative audit of 133Ce MchD and cross-nuclear lifetime borrowing.

Contrasts:
1. 133Ce (Ayangeakaa 2013): Bands 2-3 splitting ~100 keV, Bands 5-6 splitting ~400 keV;
   Lifetimes not measured; chirality inferred by borrowing from 135Nd;
2. N=75 isotone series: 133Ce (Z=58, no lifetimes), 134Pr (Z=59, Q0 ratio 2.0(4), nonchiral),
   135Nd (Z=60, B(E2) symmetric ~0.88, chiral);
3. Borrowing failure: Borrowing across Delta Z = 2 skips over the proven 134Pr nonchiral counterexample;
   establishes exact rule: Cross-nuclear borrowing cannot substitute for measured lifetimes.
"""
import json
from pathlib import Path

def audit():
    ce133 = {
        "nucleus": "133Ce",
        "Z": 58, "N": 75,
        "ayangeakaa_2013_prl": {
            "source": "PRL 110, 172504 (2013)",
            "positive_parity_bands_2_3": {
                "bandhead": "21/2+",
                "energy_splitting_keV": 100.0,
                "coriolis_attenuation_xi_needed": 0.7
            },
            "negative_parity_bands_5_6": {
                "bandhead": "23/2-",
                "energy_splitting_keV": 400.0,
                "model_interpretation": "0- and 1-phonon chiral vibrations"
            },
            "measured_lifetimes": None,
            "measured_absolute_BE2": None,
            "cross_nuclear_borrowing_statement": "identical configuration of chiral band-pair in 135Nd and Bands 5-6 in 133Ce provides further credence to these bands being chiral"
        }
    }

    n75_series = [
        {
            "nucleus": "133Ce", "Z": 58, "N": 75,
            "lifetime_measured": False,
            "symmetric_BE2_demonstrated": None,
            "status": "MchD candidate (unverified lifetimes)"
        },
        {
            "nucleus": "134Pr", "Z": 59, "N": 75,
            "lifetime_measured": True,
            "symmetric_BE2_demonstrated": False,
            "Q0_ratio": 2.0,
            "status": "Chirality disproven by Petrache 2006 (shape divergence Q0 ratio 2.0(4))"
        },
        {
            "nucleus": "135Nd", "Z": 60, "N": 75,
            "lifetime_measured": True,
            "symmetric_BE2_demonstrated": True,
            "BE2_ratio": 0.88,
            "status": "Chirality supported by Mukhopadhyay 2007 (symmetric BE2 despite 2x lifetime)"
        }
    ]

    methodological_rules = {
        "Rule_Cross_Nuclear_Borrowing": {
            "rule": "Cross-nuclear borrowing of electromagnetic transition symmetry is strictly prohibited",
            "counterexample_proof": "134Pr lies between 133Ce and 135Nd with identical N=75 and Delta Z=1, yet exhibits 2x shape divergence (Q0 ratio 2.0(4)); borrowing 135Nd symmetry across 134Pr to 133Ce is mathematically and physically ungrounded."
        },
        "Rule_Energy_Scale_Non_Exclusivity": {
            "rule": "A ~400 keV band splitting is not exclusive to chiral vibrations",
            "physical_context": "400 keV is a standard single-particle orbital rearrangement and gamma-vibrational energy scale in A~130; absent absolute B(E2_out), classifying it as chiral vibration is an unconstrained model label."
        }
    }

    return {
        "scope": "133Ce MchD cross-nuclear lifetime borrowing and N=75 isotone series audit",
        "ce133": ce133,
        "n75_isotone_series": n75_series,
        "methodological_rules": methodological_rules,
        "scientific_certification": False
    }

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    out_file = root / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/mchd-ce133-audit-057.json'
    res = audit()
    out_file.write_text(json.dumps(res, ensure_ascii=False, indent=2) + chr(10))
    print(json.dumps({'output': str(out_file.relative_to(root)), 'n75_nuclei': len(res['n75_isotone_series']), 'ce133_bands5_6_split_keV': res['ce133']['ayangeakaa_2013_prl']['negative_parity_bands_5_6']['energy_splitting_keV']}, ensure_ascii=False))
