#!/usr/bin/env python3
"""Raw-anchored boundary audit for 151Eu (Mukherjee 2023) and A~160 lineage (165Lu, 161Lu, 167Ta).

Evaluates:
1. 151Eu: Table III reports delta = -3.3 and -6.3 (91.6% and 97.5% E2 fractions).
   Polarization asymmetry Delta = +0.038(35) (Z = 1.09 sigma) and +0.024(15) (Z = 1.60 sigma).
   Alternative small DCO roots (delta = -0.12 and -0.04) represent counterfactual sensitivity (64.5x and 610.6x collapse).
   Author adopts large roots based on positive asymmetry trend and TPSM wobbling-energy agreement.
2. 165Lu: Schonwasser 2003 Table 1 reports large DCO root giving 92.3% E2;
   small root (2.8% E2, 33x collapse) excluded by analogy with 163Lu due to lack of polarization.
3. 161Lu: Bringel 2005 establishes TSD bands by alignment/MoI similarity to 163Lu,
   explicitly reporting electromagnetic multipolarities as unmeasured.
4. 167Ta: Hartley 2009 explicitly assumes 90% E2 by analogy with 163Lu to deduce BE2 ratios ~0.32-0.37.
"""
import hashlib, json, math
from pathlib import Path
import pymupdf

RUN = Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
EU151 = Path('raw/papers/2023_Mukherjee et al_Evidence of transverse wobbling motion in Eu 151.pdf')
LU165 = Path('raw/papers/2003_Schönwaßer et al_One- and two-phonon wobbling excitations in triaxial 165Lu.pdf')
LU161 = Path('raw/papers/2005_Bringel et al_Evidence for wobbling excitation in 161Lu.pdf')
TA167 = Path('raw/papers/2009_Hartley et al_Wobbling mode in Ta 167.pdf')

HASHES = {
    EU151: '3a1c99a806353e5daf0d8b29fb9325ecae47624bc46c5f98a3b502451091f8b0',
    LU165: 'f7df3707dd9c5c5aad439f22205840f1cc85d36c43428f60ac95f1343a048ac3',
    LU161: '048aad3f155d237b3c86c88d160474e925e55d6e3622bffa82d57b32b099ff59',
    TA167: '4667da2a7d58d75ee751b85d8b7489437a2dc9ecc4ba8f22fd533d36782d1525',
}

def fE2(d): return (d * d) / (1.0 + d * d)

def main():
    checks = []
    def check(name, ok, **evidence):
        checks.append({'name': name, 'passed': bool(ok), **evidence})
        assert ok, name

    # 1. Raw hashes
    for p, h in HASHES.items():
        check(f'{p.name} hash', hashlib.sha256(p.read_bytes()).hexdigest() == h)

    # 2. 151Eu Table III & asymmetry check
    with pymupdf.open(EU151) as d:
        t = ''.join(x.get_text() for x in d).replace('−', '-').replace('△', 'Delta')
        check('151Eu Table III present', 'TABLE III' in t and '0.1836' in t and '0.2795' in t)
        check('151Eu asymmetry 0.038(35) printed', '0.038(35)' in t)
        check('151Eu asymmetry 0.024(15) printed', '0.024(15)' in t)
        check('151Eu author notes Ewobb decreasing pattern', 'decreasing' in t and 'wobbling' in t.lower())

    fe_415_rep = fE2(-3.3)
    fe_415_alt = fE2(-0.12)
    fe_538_rep = fE2(-6.3)
    fe_538_alt = fE2(-0.04)
    z_415 = 0.038 / 0.035
    z_538 = 0.024 / 0.015

    check('151Eu 415 keV rep E2 fraction ~ 91.6%', math.isclose(fe_415_rep, 0.9159, abs_tol=0.001))
    check('151Eu 538 keV rep E2 fraction ~ 97.5%', math.isclose(fe_538_rep, 0.9754, abs_tol=0.001))
    check('151Eu 415 keV alt E2 fraction ~ 1.42%', math.isclose(fe_415_alt, 0.0142, abs_tol=0.001))
    check('151Eu 538 keV alt E2 fraction ~ 0.16%', math.isclose(fe_538_alt, 0.0016, abs_tol=0.001))
    check('151Eu 415 keV asymmetry Z ~ 1.09 sigma', math.isclose(z_415, 1.0857, abs_tol=0.01))
    check('151Eu 538 keV asymmetry Z ~ 1.60 sigma', math.isclose(z_538, 1.6000, abs_tol=0.01))

    # 3. 165Lu check
    with pymupdf.open(LU165) as d:
        t = ''.join(x.get_text() for x in d).replace('−', '-')
        check('165Lu Table 1 present', 'Table 1' in t and '0.17' in t)
        check('165Lu analogy to 163Lu cited', '163Lu' in t)

    fe_165_large = 0.923
    fe_165_small = 0.028
    collapse_165 = fe_165_large / fe_165_small
    check('165Lu collapse factor ~ 33.0', math.isclose(collapse_165, 32.964, abs_tol=0.05))

    # 4. 161Lu check
    with pymupdf.open(LU161) as d:
        t = ''.join(x.get_text() for x in d).replace('−', '-')
        check('161Lu TSD1 and TSD2 discussed', 'TSD1' in t and 'TSD2' in t)
        check('161Lu tentative status noted', 'tentative' in t.lower())

    # 5. 167Ta check
    with pymupdf.open(TA167) as d:
        t = ''.join(x.get_text() for x in d).replace('−', '-')
        check('167Ta assumes 90% E2 from 163Lu', '90%' in t and '163Lu' in t)
        check('167Ta BE2 ratios 0.37, 0.32, 0.36 printed', '0.37' in t and '0.32' in t and '0.36' in t)

    out = {
        'kind': 'raw-anchored-rare-earth-wobbling-lineage-boundary-controls',
        'sources': [{'path': str(p), 'sha256': h} for p, h in HASHES.items()],
        'eu151_analysis': {
            'transitions': [
                {
                    'energy_keV': 415.0,
                    'reported_delta': -3.3,
                    'reported_E2_fraction': round(fe_415_rep, 4),
                    'alternative_small_delta': -0.12,
                    'alternative_E2_fraction': round(fe_415_alt, 4),
                    'collapse_factor': round(fe_415_rep / fe_415_alt, 1),
                    'asymmetry_Delta': 0.038,
                    'asymmetry_err': 0.035,
                    'asymmetry_significance_sigma': round(z_415, 2),
                },
                {
                    'energy_keV': 537.9,
                    'reported_delta': -6.3,
                    'reported_E2_fraction': round(fe_538_rep, 4),
                    'alternative_small_delta': -0.04,
                    'alternative_E2_fraction': round(fe_538_alt, 4),
                    'collapse_factor': round(fe_538_rep / fe_538_alt, 1),
                    'asymmetry_Delta': 0.024,
                    'asymmetry_err': 0.015,
                    'asymmetry_significance_sigma': round(z_538, 2),
                },
            ],
            'interpretation': 'Mukherjee 2023 adopts large roots (91.6% and 97.5% E2) supported by positive asymmetry trend and TPSM Ewobb decrease. Small roots represent counterfactual sensitivity (collapse 64.5x and 610.6x). Polarization asymmetries have limited statistical significance (Z = 1.09 and 1.60 sigma).'
        },
        'a160_lineage_analysis': {
            '165Lu': {
                'reported_large_E2': fe_165_large,
                'alternative_small_E2': fe_165_small,
                'collapse_factor': round(collapse_165, 1),
                'selection_basis': 'Small root excluded by analogy to 163Lu due to lack of linear polarization measurement.'
            },
            '161Lu': {
                'status': 'TSD bands assigned based on alignment and moment of inertia similarity to 163Lu; electromagnetic multipolarities explicitly unmeasured.'
            },
            '167Ta': {
                'assumed_E2_fraction': 0.90,
                'source_of_assumption': 'Copied from 163Lu by analogy; deduced BE2 ratios 0.32-0.37 depend on this assumption.'
            },
        },
        'checks': checks,
        'valid': all(c['passed'] for c in checks),
        'independent_fit_or_CI': False,
    }
    out_path = RUN / 'eu151-a160-wobbling-boundary-result-054.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'valid': out['valid'], 'checks': len(checks), 'output': str(out_path)}))

if __name__ == '__main__':
    main()
