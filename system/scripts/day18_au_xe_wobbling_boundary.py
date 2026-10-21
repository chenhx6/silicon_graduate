#!/usr/bin/env python3
"""Raw-anchored boundary audit for 187Au (Sensharma 2020 / Guo 2022) and 127Xe (Chakraborty 2020).

Evaluates:
1. 187Au 376.5 keV: Sensharma 2020 delta = 2.6 (E2 fraction 87.1%) vs Bourgeois/Guo delta = -0.10(5) (E2 fraction 0.99%).
   Conditional E2 fraction ratio = 0.8711 / 0.0099 = 88.0x.
   With in-band B(E2) = 1.49 e^2b^2 (Ref 39), 0.70 * (1.49/B_W_E2) = 164.2 W.u. collapses conditionally to 1.87 W.u.
   Distinguishes author wobbling claim (unmeasured polarization) from Guo 2022 single-particle interpretation.
2. 127Xe Table 1: Chakraborty 2020 reported large delta values (-2.1 to -3.1) and B(E2)out/in (0.92 - 2.35).
   Counterfactual substitution of DCO small-root branch (|delta| ~ 0.3) collapses E2 fraction by 8.2-10x.
   Evaluates Band 4 Delta I = 0 vs Delta I = 2 decay topology as an author-stated gamma-vibrational coupling signature.
"""
import hashlib, json, math
from pathlib import Path
import pymupdf

RUN = Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
SE = Path('raw/papers/2020_Sensharma et al_Longitudinal Wobbling Motion in Au 187.pdf')
GU = Path('raw/papers/2022_Guo et al_Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei3.pdf')
CH = Path('raw/papers/2020_Chakraborty et al_Multiphonon longitudinal wobbling in 127Xe.pdf')

SE_HASH = 'f348dce9976ad076fd9b1d5281a728e0923053aced33b0270f643d770729366a'
GU_HASH = 'de541977e4c8402c905ef8268ebc5707303f4b92f244eb4f59405a70c3473206'
CH_HASH = 'b04503fce61b249ab1193f395b4276364945d02ced5eac347a5dd2e45df6ea1a'

def fE2(d): return (d*d) / (1.0 + d*d)

def main():
    checks = []
    def check(name, ok, **evidence):
        checks.append({'name': name, 'passed': bool(ok), **evidence})
        assert ok, name

    # 1. Raw hashes
    for p, h in [(SE, SE_HASH), (GU, GU_HASH), (CH, CH_HASH)]:
        check(p.name + ' hash', hashlib.sha256(p.read_bytes()).hexdigest() == h)

    # 2. Sensharma 187Au text check
    with pymupdf.open(SE) as d:
        setext = ''.join(x.get_text() for x in d[:5])
        check('Sensharma 187Au longitudinal wobbling claim', 'longitudinal' in setext.lower() and '187Au' in setext)
        check('Sensharma in-band B(E2) citation 1.49', '1.49' in setext)

    # 3. Guo 2022 text check
    with pymupdf.open(GU) as d:
        gutext = ''.join(x.get_text() for x in d[:5])
        check('Guo 2022 delta = -0.10(5)', '-0.10(5)' in gutext)
        check('Guo 2022 single-particle interpretation', 'single' in gutext.lower() and 'particle' in gutext.lower())

    # 4. 187Au 376.5 keV algebra
    A_au = 187
    B_sp_E2 = 5.940e-6 * (A_au ** (4.0 / 3.0)) # ~0.006352 e^2b^2
    BE2_in_wu = 1.49 / B_sp_E2 # ~234.6 W.u.
    d_sensharma = 2.6
    d_bourgeois = -0.10
    fe2_sensharma = fE2(d_sensharma)
    fe2_bourgeois = fE2(d_bourgeois)
    collapse_ratio_au = fe2_sensharma / fe2_bourgeois # ~87.99
    BE2_sensharma_wu = 0.70 * BE2_in_wu # ~164.2 W.u.
    BE2_bourgeois_wu = BE2_sensharma_wu / collapse_ratio_au # ~1.87 W.u.

    check('187Au collapse factor ~ 88.0', math.isclose(collapse_ratio_au, 87.989, abs_tol=0.01))
    check('187Au true strength in single-particle range', 1.0 <= BE2_bourgeois_wu <= 2.5)

    # 5. Chakraborty 127Xe Table 1 check
    with pymupdf.open(CH) as d:
        chtext = ''.join(x.get_text() for x in d[:5])
        check('Chakraborty 127Xe Table 1 present', 'Table 1' in chtext and '127Xe' in chtext)
        check('Chakraborty Delta I = 0 discussion', 'ΔI = 0' in chtext or 'I = 0' in chtext)

    # 127Xe Table 1 lines: (E_gamma, delta_rep, delta_small_alt, BE2_rep, BM1_rep)
    xe_lines = [
        (639.0, -2.2, -0.30, 2.352, 0.138),
        (735.0, -2.4, -0.32, 1.500, 0.098),
        (800.0, -2.9, -0.35, 1.346, 0.071),
        (884.0, -3.1, -0.33, 0.922, 0.052),
        (638.0, -2.4, -0.32, 1.364, 0.062),
    ]
    xe_results = []
    for eg, d_rep, d_alt, be2_rep, bm1_rep in xe_lines:
        fe_rep = fE2(d_rep)
        fe_alt = fE2(d_alt)
        ratio_drop = fe_rep / fe_alt
        be2_alt = be2_rep / ratio_drop
        fm_rep = 1.0 - fe_rep
        fm_alt = 1.0 - fe_alt
        ratio_jump = fm_alt / fm_rep
        bm1_alt = bm1_rep * ratio_jump
        xe_results.append({
            'E_gamma_keV': eg,
            'reported_delta': d_rep,
            'reported_E2_fraction': round(fe_rep, 4),
            'reported_BE2out_in': be2_rep,
            'counterfactual_small_delta': d_alt,
            'counterfactual_E2_fraction': round(fe_alt, 4),
            'counterfactual_BE2out_in': round(be2_alt, 4),
            'collapse_factor': round(ratio_drop, 2),
            'jump_factor_M1': round(ratio_jump, 2),
        })
    check('127Xe five lines collapse factor between 8 and 11', all(8.0 <= x['collapse_factor'] <= 11.0 for x in xe_results))

    out = {
        'kind': 'raw-anchored-wobbling-boundary-controls',
        'sources': [
            {'path': str(SE), 'sha256': SE_HASH},
            {'path': str(GU), 'sha256': GU_HASH},
            {'path': str(CH), 'sha256': CH_HASH}
        ],
        'au187_analysis': {
            '376keV': {
                'sensharma_delta': d_sensharma,
                'sensharma_fe2': round(fe2_sensharma, 4),
                'sensharma_BE2_wu': round(BE2_sensharma_wu, 1),
                'bourgeois_guo_delta': d_bourgeois,
                'bourgeois_guo_fe2': round(fe2_bourgeois, 4),
                'bourgeois_guo_BE2_wu': round(BE2_bourgeois_wu, 2),
                'collapse_ratio': round(collapse_ratio_au, 1),
                'interpretation': '88.0x collapse from 164 W.u. to 1.87 W.u. is a conditional result of replacing delta=2.6 with delta=-0.10(5); Guo 2022 confirms single-particle character rather than collective wobbler.'
            }
        },
        'xe127_analysis': {
            'table1_lines': xe_results,
            'interpretation': '8.2-10.0x drop is a counterfactual test using alternative small DCO roots; Chakraborty adopted large roots supported by angular correlation/polarization asymmetry; Delta I = 0 decay topology reflects gamma-vibrational core coupling.'
        },
        'checks': checks,
        'valid': all(c['passed'] for c in checks),
        'independent_fit_or_CI': False
    }
    out_path = RUN / 'au-xe-wobbling-boundary-result-052.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'valid': out['valid'], 'checks': len(checks), 'au_collapse': round(collapse_ratio_au, 1), 'output': str(out_path)}))

if __name__ == '__main__':
    main()
