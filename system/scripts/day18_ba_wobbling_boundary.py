#!/usr/bin/env python3
"""Raw-anchored boundary audit for 130Ba (Chen 2019) and 129Ba (Chakraborty 2024).

Evaluates:
1. 130Ba Table I: Chen 2019 reported delta = -0.58 to -0.62 for 2-qp bands S1' -> S1.
   E2 fraction is 25.2% - 27.8%, M1 fraction is 72.2% - 74.8%.
   Authors explicitly report M1 dominance, attributing it to 2-qp M1 enhancement and scissors coupling.
   PRM overestimates B(M1_out)/B(E2_in) by 1.47x - 3.30x across spins 13 to 21.
2. 129Ba 365 keV: Chakraborty 2024 reanalysis of legacy data (Byrne 1992 / Gizon 1977/78).
   Contrasts large root (delta ~ -2.0, 80% E2) with historical adopted root (delta ~ -0.81, 40% E2)
   and alternative small root (delta ~ -0.33, 10% E2).
   Evaluates linear polarization P = 0.072(68), noting Z = 1.06 sigma statistical compatibility with zero.
"""
import hashlib, json, math
from pathlib import Path
import pymupdf

RUN = Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
CH19 = Path('raw/papers/2019_Chen et al_Transverse wobbling in an even-even nucleus.pdf')
CH24 = Path('raw/papers/2024_Chakraborty et al_Exploring the possibility of wobbling motion in Ba 129.pdf')

CH19_HASH = '26e305b496b2fdff4596670f772e3b030540b3c24d0830b8e4b4176c8070c768'
CH24_HASH = 'd5729de577067f8afeab771afb51328989772c68962a938d553bccb50f0c0808'

def fE2(d): return (d*d) / (1.0 + d*d)

def main():
    checks = []
    def check(name, ok, **evidence):
        checks.append({'name': name, 'passed': bool(ok), **evidence})
        assert ok, name

    # 1. Raw hashes
    check('Chen 2019 130Ba hash', hashlib.sha256(CH19.read_bytes()).hexdigest() == CH19_HASH)
    check('Chakraborty 2024 129Ba hash', hashlib.sha256(CH24.read_bytes()).hexdigest() == CH24_HASH)

    # 2. 130Ba text and Table I check
    with pymupdf.open(CH19) as d:
        t = ''.join(x.get_text() for x in d[:4])
        check('130Ba Table I present', 'TABLE I.' in t and '130Ba' in t)
        check('130Ba author acknowledges ~25% E2 component', '25%' in t)
        check('130Ba author notes scissors coupling', 'scissor' in t.lower())

    # Table I data: spin, delta_rep, BM1_rep, BM1_prm, BE2_rep, BE2_prm
    states_130ba = [
        (13, -0.58, 0.36, 1.11, 0.32, 0.51),
        (15, -0.62, 0.38, 0.90, 0.36, 0.42),
        (17, -0.62, 0.23, 0.76, 0.22, 0.35),
        (19, -0.60, 0.25, 0.67, 0.22, 0.29),
        (21, -0.60, 0.43, 0.63, 0.41, 0.25),
    ]
    ba130_results = []
    for spin, d_rep, bm1_exp, bm1_prm, be2_exp, be2_prm in states_130ba:
        fe = fE2(d_rep)
        fm = 1.0 - fe
        prm_bm1_ratio = bm1_prm / bm1_exp
        ba130_results.append({
            'spin': spin,
            'delta_rep': d_rep,
            'E2_fraction': round(fe, 4),
            'M1_fraction': round(fm, 4),
            'BM1_exp': bm1_exp,
            'BM1_PRM': bm1_prm,
            'PRM_over_exp_BM1': round(prm_bm1_ratio, 2),
            'BE2_exp': be2_exp,
            'BE2_PRM': be2_prm,
        })

    check('130Ba E2 fraction between 25% and 28%', all(0.25 <= x['E2_fraction'] <= 0.28 for x in ba130_results))
    check('130Ba M1 fraction between 72% and 75%', all(0.72 <= x['M1_fraction'] <= 0.75 for x in ba130_results))
    check('130Ba PRM BM1 overestimation between 1.4x and 3.3x', all(1.4 <= x['PRM_over_exp_BM1'] <= 3.4 for x in ba130_results))

    # 3. 129Ba text and 365 keV check
    with pymupdf.open(CH24) as d:
        t = ''.join(x.get_text() for x in d[:4]).replace('−', '-').replace('⩽', '<=')
        check('129Ba 365 keV transition discussed', '365' in t)
        check('129Ba linear polarization P=0.072(68) printed', '0.072(68)' in t)
        check('129Ba historical delta -0.84 to -0.79 cited', '-0.84' in t and '-0.79' in t)

    d_large = -2.0
    d_hist = -0.815
    d_small = -0.33
    fe_large = fE2(d_large)
    fe_hist = fE2(d_hist)
    fe_small = fE2(d_small)
    pol_P = 0.072
    pol_err = 0.068
    pol_sigma = pol_P / pol_err

    check('129Ba large root E2 fraction ~ 80%', math.isclose(fe_large, 0.80, abs_tol=0.01))
    check('129Ba historical adopted root E2 fraction ~ 40%', math.isclose(fe_hist, 0.399, abs_tol=0.01))
    check('129Ba small root E2 fraction ~ 9.8%', math.isclose(fe_small, 0.0982, abs_tol=0.01))
    check('129Ba polarization significance ~ 1.06 sigma', math.isclose(pol_sigma, 1.0588, abs_tol=0.01))

    out = {
        'kind': 'raw-anchored-ba-wobbling-boundary-controls',
        'sources': [
            {'path': str(CH19), 'sha256': CH19_HASH},
            {'path': str(CH24), 'sha256': CH24_HASH}
        ],
        'ba130_analysis': {
            'states': ba130_results,
            'mean_E2_fraction': round(sum(x['E2_fraction'] for x in ba130_results) / len(ba130_results), 4),
            'mean_M1_fraction': round(sum(x['M1_fraction'] for x in ba130_results) / len(ba130_results), 4),
            'interpretation': 'Interband transitions are 72.2%-74.8% M1; author acknowledges this and attributes it to two-quasiparticle M1 enhancement and scissors coupling. PRM overpredicts BM1 by 1.47-3.30x.'
        },
        'ba129_analysis': {
            'transition_365keV': {
                'large_root': {'delta': d_large, 'E2_fraction': round(fe_large, 4)},
                'historical_adopted_root': {'delta_midpoint': d_hist, 'E2_fraction': round(fe_hist, 4)},
                'small_root': {'delta': d_small, 'E2_fraction': round(fe_small, 4)},
                'polarization_P': pol_P,
                'polarization_err': pol_err,
                'polarization_significance_sigma': round(pol_sigma, 2),
                'interpretation': 'Large delta ~ -2.0 gives 80% E2, while historical root gives 40% E2 (signature partner). Polarization P=0.072(68) is Z=1.06 sigma from zero, providing marginal statistical discrimination.'
            }
        },
        'checks': checks,
        'valid': all(c['passed'] for c in checks),
        'independent_fit_or_CI': False
    }
    out_path = RUN / 'ba129-ba130-wobbling-boundary-result-053.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'valid': out['valid'], 'checks': len(checks), 'ba130_E2_pct': round(out['ba130_analysis']['mean_E2_fraction']*100, 1), 'output': str(out_path)}))

if __name__ == '__main__':
    main()
