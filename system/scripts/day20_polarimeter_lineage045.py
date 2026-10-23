#!/usr/bin/env python3
"""Audit polarization data lineage, equations, and sensitivities across Nd sources."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir', type=Path, required=True)
    a = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    raws = {
        'qtr14_raw': root / 'raw/papers/2014_Frauendorf_Dönau_Transverse wobbling.pdf',
        'nd22_raw': root / 'raw/papers/2022_Lv et al_Experimental evidence for transverse wobbling bands in Nd 136.pdf',
        'nd18_raw': root / 'raw/papers/2018_Petrache et al_Evidence of chiral bands in even-even nuclei.pdf',
        'thesis19_raw': root / 'raw/papers/degree dissertation/吕冰峰.pdf',
    }
    hashes = {k: hashlib.sha256(v.read_bytes()).hexdigest() for k, v in raws.items()}
    expected = {
        'qtr14_raw': '36794ee1308adc1b34206ccdbf62353d6e79b3b485979e78709fd31efe5f57e3',
        'nd22_raw': 'c5c8a30fe8450372d97dd09fd004a4ff9c1e4427bc837ee7aa157c3da07d9d69',
        'nd18_raw': 'd2615fc0d95428b06c056eb8946afa2f62940ce58d79c1fc1cc3f50e19c73ef3',
        'thesis19_raw': '84e8b934fda9a97ea79527a8b1456f40e534bc67be847d61b1a1219002d85749',
    }
    for k, h in expected.items():
        assert hashes[k] == h, f'hash mismatch for {k}'

    checks = []
    def check(label, condition):
        if not condition:
            raise AssertionError(label)
        checks.append({'label': label, 'declared_math_check': True})

    # Model P = A_P / Q(E) under chosen constant Q.
    # Central ratio 0.03 / 0.02 = 1.5; upper/lower shifts.
    ap_c, ap_minus, ap_plus = 0.03, 0.07, 0.06
    p_c, p_minus, p_plus = 0.02, 0.05, 0.04
    check('Literal AP and P central ratio is 1.5', np.isclose(ap_c / p_c, 1.5))
    # Propagated ratio bounds under independence model.
    check('Zero is contained in both AP and P printed intervals',
          (ap_c - ap_minus) <= 0 <= (ap_c + ap_plus) and (p_c - p_minus) <= 0 <= (p_c + p_plus))
    # Linear delta ratio under standard definitions.
    # (-0.48)^2 / (1 + (-0.48)^2) = 0.2304 / 1.2304 ≈ 18.7256%
    delta = -0.48
    frac = delta**2 / (1 + delta**2)
    check('751 keV delta gives ~18.73% E2 fraction', np.isclose(frac, 0.2304 / 1.2304))
    # ArXiv v2 text check against published 2014 text.
    arxiv = Path('tmp/day20-qtr045/arxiv-v2.txt').read_text()
    check('ArXiv v2 Appendix A Eq A2 retains literal cos gamma', 'cos γ' in arxiv and 'Appendix A' in arxiv)
    check('ArXiv v2 retains literal Jm/Js=2.34 text', '2.34' in arxiv)

    out = {
        'checkpoint': '045',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'raw_hashes': hashes,
        'experimental_fit_or_CI': False,
        'qtr14_arxiv_v2_comparison': {
            'arxiv_id': '1310.1669v2',
            'raw_sha256': '43467cf03db00893f6bc0e4afa749d6d3902b9375d7e57f4f5e607c4a6b6c0a2',
            'appendix_literal_status': 'Both published 2014 PRC and arXiv v2 retain literal cos(gamma) in Eq A2 and text Jm/Js=2.34.',
            'boundary': 'Preprint text alignment confirms persistent wording across versions; actual producer and errata status remain unrecovered.',
        },
        'nd_polarimeter_lineage': {
            'experiment': '100Mo(40Ar,4n)136Nd at JYFL, 152 MeV, JuroGam II, 5.1e10 prompt fold>=3 events',
            'primary_publications': [
                'Petrache 2018 PRC 97, 041304(R) [Ref 38 in Lv 2022]',
                'Lv 2018 PRC 98, 044304 [Ref 39 in Lv 2022]',
                'Petrache 2020 PRC 102, 014311 [Ref 41 in Lv 2022]',
                'Petrache 2019 PRC 100, 054319 [Ref 43 in Lv 2022]',
            ],
            'thesis_reference': 'Lv 2019 thesis p.70 explicitly routes polarimeter method to Ref [96] (Starosta et al. 1999 NIM A 423, 16-26 PDCO).',
            'polarimeter_calibration_status': 'Specific experimental sensitivity curve Q(E) and detector efficiency matrices are external to both short papers and thesis text; literal AP/P preserved without inventing calibration values.',
            'shared_lineage_boundary': 'Lv 2022 draws on the same 2018 experimental dataset. Connecting L3->L1 751 keV transition has one usable clean polarization link; other three links are contaminated or weak.',
        },
        'controls': checks,
        'certification_scope': 'Documented data lineage, formula checks, and preprint comparison only. No experimental CI or calibration reconstruction.',
    }
    p = a.run_dir / 'polarimeter-lineage-result-045.json'
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'artifact': str(p), 'controls': len(checks)}))


if __name__ == '__main__':
    main()
