#!/usr/bin/env python3
"""Synthesis and closure audit of the 135Nd chirality experimental and theoretical lineage.

Lineage sequence:
1. Zhu 2003 (PRL 91, 132501): Initial observation of negative-parity twin bands in 110Pd(30Si,5n)135Nd;
2. Mukhopadhyay 2007 (PRL 99, 172501): Gammasphere DSAM lifetime measurement in 100Mo(40Ar,5n)135Nd;
   Unique published primary experimental source for 135Nd lifetimes;
3. Qi 2009 (PLB 675, 175): Fully quantal triaxial PRM calculation, beta=0.235, gamma=22.4, J0=29.0;
4. Almehed 2011 (PRC 83, 054308): Microscopic TAC+RPA formalism, formally closing Ref. [32] of MU07;
5. Lv 2019 (PRC 100, 024314): JUROGAM II in-beam spectroscopy, new positive-parity pair D3/D4 (MchD),
   reusing MU07 negative-parity lifetimes without new lifetime measurements.
"""
import json
from pathlib import Path

def audit():
    lineage = [
        {
            "step": 1,
            "paper": "Zhu 2003",
            "citation": "PRL 91, 132501",
            "role": "Level scheme discovery (Bands A & B)",
            "experiment": "110Pd(30Si,5n) at 133 MeV, Gammasphere",
            "lifetimes_measured": False
        },
        {
            "step": 2,
            "paper": "Mukhopadhyay 2007",
            "citation": "PRL 99, 172501",
            "role": "DSAM lifetime measurement, B(E2) symmetry (~0.88)",
            "experiment": "100Mo(40Ar,5n) at 175 MeV, Gammasphere",
            "lifetimes_measured": True,
            "ref32_promise": "D. Almehed and S. Frauendorf (to be published)"
        },
        {
            "step": 3,
            "paper": "Qi 2009",
            "citation": "PLB 675, 175",
            "role": "Fully quantal PRM (pi h11/2^2 x nu h11/2^-1)",
            "model": "PRM, beta=0.235, gamma=22.4 deg, J0=29.0 hbar^2/MeV",
            "lifetimes_measured": False
        },
        {
            "step": 4,
            "paper": "Almehed 2011",
            "citation": "PRC 83, 054308",
            "role": "Microscopic TAC+RPA theory closure of Ref. [32]",
            "model": "TAC+RPA with QQ force, harmonic limits and instability boundaries",
            "lifetimes_measured": False,
            "closure_of_mu07_ref32": True
        },
        {
            "step": 5,
            "paper": "Lv 2019",
            "citation": "PRC 100, 024314",
            "role": "JUROGAM II reexamination, positive-parity MchD (D3/D4)",
            "experiment": "100Mo(40Ar,5n) at 152 MeV, JUROGAM II",
            "lifetimes_measured": False,
            "reused_lifetimes_from": "Mukhopadhyay 2007 (Ref. 36)"
        }
    ]

    closure_status = {
        "primary_experimental_lifetime_source": "Mukhopadhyay 2007 PRL 99, 172501 Table I (unique published record)",
        "mu07_ref32_resolved_to": "Almehed, Donau, Frauendorf, PRC 83, 054308 (2011) / arXiv:0709.0969v2",
        "separate_nd135_prc_experiment_paper": "None (author published PRC 78, 034311 on 136Nd instead)",
        "independent_lifetime_replications": 0,
        "reused_lifetime_citations": 2  # Qi 2009, Lv 2019
    }

    return {
        "scope": "135Nd chirality multi-paper lineage and experimental evidence closure audit",
        "lineage_chain": lineage,
        "closure_status": closure_status,
        "scientific_certification": False
    }

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    out_file = root / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01/nd135-lineage-closure-060.json'
    res = audit()
    out_file.write_text(json.dumps(res, ensure_ascii=False, indent=2) + chr(10))
    print(json.dumps({'output': str(out_file.relative_to(root)), 'lineage_steps': len(res['lineage_chain']), 'primary_source': res['closure_status']['primary_experimental_lifetime_source']}, ensure_ascii=False))
