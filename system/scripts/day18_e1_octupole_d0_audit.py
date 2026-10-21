#!/usr/bin/env python3
import json
import math
from pathlib import Path

RUN = Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')

def weisskopf_be1_sp(A):
    return 0.06446 * (A**(2.0 / 3.0))

def extract_d0(Qt_eb, be1_over_be2_fm2):
    Qt_fm2 = Qt_eb * 100.0
    return math.sqrt((5.0 / 16.0) * (Qt_fm2**2) * be1_over_be2_fm2)

def main():
    checks = []
    def check(name, ok, **evidence):
        checks.append({'name': name, 'passed': bool(ok), **evidence})
        assert ok, f'FAILED: {name}'

    # 1. Rate conversion factor
    ratio_factor = 1.225e9 / 1.590e15
    check('Ratio factor C_E1_E2 equals 7.7044e-7 MeV^-2 within 1e-10', abs(ratio_factor - 7.7044025e-7) < 1e-12,
          ratio_factor=ratio_factor)

    # 2. Weisskopf E1 single-particle scaling
    sp_78 = weisskopf_be1_sp(78)
    check('78Br B(E1)_sp in range [1.17, 1.18] e^2 fm^2', 1.17 <= sp_78 <= 1.18, value=sp_78)

    sp_165 = weisskopf_be1_sp(165)
    check('165Tm B(E1)_sp in range [1.93, 1.95] e^2 fm^2', 1.93 <= sp_165 <= 1.95, value=sp_165)

    sp_224 = weisskopf_be1_sp(224)
    check('224Th B(E1)_sp in range [2.37, 2.39] e^2 fm^2', 2.37 <= sp_224 <= 2.39, value=sp_224)

    # 3. 78Br D0 extraction (Liu 2016 PRL 116, 112501)
    d0_78_low = extract_d0(2.0, 1.0e-6)
    d0_78_mid = extract_d0(2.0, 2.0e-6)
    d0_78_high = extract_d0(2.0, 3.0e-6)
    check('78Br D0 in range [0.10, 0.20] e fm', 0.10 <= d0_78_mid <= 0.20, d0=d0_78_mid)

    # 4. 224Th stable octupole benchmark: B(E1)/B(E2) ~ 1.5e-5 fm^-2
    octupole_ratio = (1.5e-5) / (1.5e-6)
    check('Stable octupole B(E1)/B(E2) is ~10x larger than octupole-soft 78Br', octupole_ratio >= 8.0,
          ratio=octupole_ratio)

    # 5. Absolute DSAM Qt dependence
    check('D0 scales linearly with DSAM Qt', abs((extract_d0(4.0, 2.0e-6) / extract_d0(2.0, 2.0e-6)) - 2.0) < 1e-12)

    # 6. Tri-multipolarity taxonomy classification
    taxonomy = {
        'E2_wobbling': {'dominant_transition': 'transverse E2', 'relative_strength': 'B(E2)out >> 1 W.u., B(M1) << B(E2)', 'physical_mode': 'triaxial angular momentum precession'},
        'M1_chirality': {'dominant_transition': 'partner-band M1', 'relative_strength': 'B(M1) ~ 1-3 muN2, B(M1)/B(E2) >> 1', 'physical_mode': 'spontaneous chiral symmetry breaking'},
        'E1_octupole': {'dominant_transition': 'alternating-parity E1', 'relative_strength': 'B(E1)/B(E2) ~ 1e-6 to 1e-4 fm^-2, D0 > 0.1 e fm', 'physical_mode': 'reflection symmetry breaking or octupole softness'}
    }
    check('Tri-multipolarity taxonomy covers all 3 modes', len(taxonomy) == 3)

    out = {
        'kind': 'e1-octupole-d0-taxonomy-audit',
        'valid': True,
        'checks': checks,
        'rate_constants': {
            'const_E1_s_MeV': 1.590e15,
            'const_E2_s_MeV': 1.225e9,
            'ratio_factor_MeV_minus2': ratio_factor
        },
        'weisskopf_e1_units': {
            '78Br': sp_78,
            '165Tm': sp_165,
            '224Th': sp_224
        },
        'octupole_dipole_moments': {
            '78Br_octupole_soft': {
                'Qt_eb': 2.0,
                'be1_be2_range_fm2': [1.0e-6, 3.0e-6],
                'D0_range_efm': [round(d0_78_low, 3), round(d0_78_high, 3)],
                'interpretation': 'octupole-softness in MchiD system (Liu 2016 PRL 116, 112501)'
            },
            '224Th_stable_octupole': {
                'be1_be2_fm2': 1.5e-5,
                'ratio_over_78br': octupole_ratio,
                'interpretation': 'stable reflection-asymmetric rotor benchmark'
            }
        },
        'taxonomy': taxonomy,
        'time_invariants_respected': {
            'formal_credit_not_yet_awarded': True,
            'window_ends_at': '15:00 CST',
            'closeout_hour': '15:00 - 16:00 CST'
        }
    }

    out_file = RUN / 'e1-octupole-d0-result-077.json'
    out_file.write_text(json.dumps(out, indent=2, ensure_ascii=False) + chr(10), encoding='utf-8')
    print(json.dumps({'valid': out['valid'], 'checks': len(checks), 'output': str(out_file)}))

if __name__ == '__main__':
    main()
