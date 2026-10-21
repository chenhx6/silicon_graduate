#!/usr/bin/env python3
"""Quantitative audit of Mukhopadhyay 2008 Table II transition quadrupole moment formula.

Evaluates:
1. The candidate geometric factor G(I) = (2I - 3) / (2I + 1) = CG(I, 2, I-2, I, -2, I-2)^2.
2. Closed-form conversion: Qt_calc = sqrt( (16*pi / 5) * ((2I + 1)/(2I - 3)) * B(E2) ).
3. Comparison across all 9 printed (B(E2), Qt) pairs in Table II:
   Band 1: I = 16, 17, 18, 19
   Band 2: I = 15, 16, 17, 18, 19
4. Maximum discrepancy between calculated and printed Qt is < 0.0054 eb (within rounding).
5. Contrast with standard symmetric rotor K=0 formula, which gives Qt ~ 1.58x larger.
6. Boundary: Mukhopadhyay 2008 did not explicitly print the Qt formula or define the axis;
   this algebraic match identifies the probable conversion kernel without asserting it as unique.
"""
import hashlib, json, math
from pathlib import Path
import pymupdf

RUN = Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
MU08 = Path('raw/papers/gpt/high-spin-20260920/三轴/手征/2008_Mukhopadhyay et al_Electromagnetic transition rates in high-spin bands in Nd 136.pdf')
MU08_HASH = 'ea77d7d033051369d19aad2f82a542e91e262eb490d518b246f7f04c2d0dcd2c'

def G_candidate(I):
    return (2.0 * I - 3.0) / (2.0 * I + 1.0)

def G_k0(I):
    # Standard K=0 Clebsch-Gordan squared: <I 0 2 0 | I-2 0>^2
    # = 3 * I * (I - 1) / (2 * (2I - 1) * (2I + 1))
    return 3.0 * I * (I - 1.0) / (2.0 * (2.0 * I - 1.0) * (2.0 * I + 1.0))

factor_16pi_5 = 16.0 * math.pi / 5.0

# Table II data: (band, I, BE2, Qt_rep, Qt_err)
TABLE_II_DATA = [
    (1, 16, 0.26, 1.73, 0.10),
    (1, 17, 0.08, 0.95, 0.06),
    (1, 18, 0.14, 1.26, 0.09),
    (1, 19, 0.11, 1.11, 0.10),
    (2, 15, 0.54, 2.50, 0.19),
    (2, 16, 0.51, 2.42, 0.17),
    (2, 17, 0.44, 2.24, 0.15),
    (2, 18, 0.04, 0.67, 0.08),
    (2, 19, 0.05, 0.75, 0.08),
]

def main():
    checks = []
    def check(name, ok, **evidence):
        checks.append({'name': name, 'passed': bool(ok), **evidence})
        assert ok, name

    # 1. Raw hash check
    check('MU08 raw hash check', hashlib.sha256(MU08.read_bytes()).hexdigest() == MU08_HASH)

    # 2. PDF Table II verification
    with pymupdf.open(MU08) as doc:
        t = ''.join(p.get_text() for p in doc).replace('−', '-')
        check('MU08 Table II present', 'TABLE II' in t)
        for band, I, be2, qt_rep, _ in TABLE_II_DATA:
            check(f'Band {band} I={I} printed Qt={qt_rep}', str(qt_rep) in t)

    # 3. Quantitative conversion audit
    results = []
    max_abs_diff = 0.0
    for band, I, be2, qt_rep, qt_err in TABLE_II_DATA:
        g_cand = G_candidate(I)
        qt_cand = math.sqrt(factor_16pi_5 * be2 / g_cand)
        diff_cand = qt_cand - qt_rep
        abs_diff = abs(diff_cand)
        if abs_diff > max_abs_diff:
            max_abs_diff = abs_diff

        g_0 = G_k0(I)
        qt_k0 = math.sqrt(factor_16pi_5 * be2 / g_0)

        results.append({
            'band': band,
            'initial_spin': I,
            'BE2_reported': be2,
            'Qt_reported': qt_rep,
            'Qt_reported_err': qt_err,
            'G_candidate': round(g_cand, 6),
            'Qt_calculated_candidate': round(qt_cand, 4),
            'diff_candidate': round(diff_cand, 4),
            'Qt_calculated_K0': round(qt_k0, 4),
            'ratio_K0_over_candidate': round(qt_k0 / qt_cand, 3),
        })

    check('All 9 candidate Qt match printed values within 0.0055 eb', max_abs_diff < 0.0055)
    check('K=0 formula gives systematically ~1.58x larger Qt', all(1.57 <= r['ratio_K0_over_candidate'] <= 1.59 for r in results))

    out = {
        'kind': 'raw-anchored-mu08-table-ii-rotor-formula-audit',
        'source': {'path': str(MU08), 'sha256': MU08_HASH},
        'candidate_formula': {
            'description': 'B(E2; I -> I-2) = (5 / 16pi) * e^2 * Qt^2 * ((2I - 3) / (2I + 1))',
            'algebraic_origin': 'Equivalently CG(I, 2, I-2, I, -2, I-2)^2 = (2I - 3) / (2I + 1)',
            'closed_form_Qt': 'Qt = sqrt( (16pi / 5) * ((2I + 1)/(2I - 3)) * B(E2) )',
            'max_absolute_discrepancy_eb': round(max_abs_diff, 4),
        },
        'states_audit': results,
        'boundary_conclusion': (
            'The candidate geometric factor G = (2I-3)/(2I+1) reproduces all 9 published Qt values in Mukhopadhyay 2008 Table II '
            'with maximum discrepancy < 0.0054 eb (pure rounding). Standard K=0 Clebsch-Gordan yields Qt ~ 1.58x larger (e.g. 2.73 vs 1.73 eb). '
            'Because Mukhopadhyay 2008 did not print the formula or define the quantization axis in the text, '
            'this algebraic match provides a diagnostic signature of the conversion code used by the authors, '
            'without establishing an experimentally certified unique formula or independent measurement.'
        ),
        'checks': checks,
        'valid': all(c['passed'] for c in checks),
        'independent_fit_or_CI': False,
    }
    out_path = RUN / 'mu08-table-ii-rotor-formula-result-056.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'valid': out['valid'], 'checks': len(checks), 'max_diff_eb': round(max_abs_diff, 4), 'output': str(out_path)}))

if __name__ == '__main__':
    main()
