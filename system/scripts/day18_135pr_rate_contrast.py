#!/usr/bin/env python3
"""Audit 135Pr interband B(E2)out/B(E2)in collapse between Matta 2015 and Lv 2022."""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--contract', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    d = json.loads(a.contract.read_text())
    sha_m = hashlib.sha256(Path(d['raw_matta']).read_bytes()).hexdigest()
    sha_l = hashlib.sha256(Path(d['raw_lv']).read_bytes()).hexdigest()
    if sha_m != d['raw_sha_matta'] or sha_l != d['raw_sha_lv']:
        raise ValueError('raw file SHA256 mismatch')

    t747 = d['transitions'][0]
    t813 = d['transitions'][1]
    t450 = d['transitions'][2]

    # 747.0 keV
    m_d747 = float(t747['matta_delta'])
    l_d747 = float(t747['lv_delta'])
    m_fe2_747 = (m_d747**2) / (1.0 + m_d747**2)
    l_fe2_747 = (l_d747**2) / (1.0 + l_d747**2)
    ratio_fe2_747 = m_fe2_747 / l_fe2_747

    # 813.0 keV
    m_d813 = float(t813['matta_delta'])
    l_d813 = float(t813['lv_delta'])
    m_fe2_813 = (m_d813**2) / (1.0 + m_d813**2)
    l_fe2_813 = (l_d813**2) / (1.0 + l_d813**2)
    ratio_fe2_813 = m_fe2_813 / l_fe2_813

    # 450.0 keV
    l_d450 = float(t450['lv_delta'])
    l_fe2_450 = (l_d450**2) / (1.0 + l_d450**2)

    # 813-keV reported B(E2)out/in contrast
    m_be2_813 = float(t813['matta_BE2out_in'])
    l_be2_813 = float(t813['lv_BE2out_in'])
    factor_diff_be2_813 = m_be2_813 / l_be2_813

    checks = [
        {
            'name': '747_keV_E2_fraction_drops_from_over_60_percent_to_under_20_percent',
            'matta_fe2_percent': m_fe2_747 * 100.0,
            'lv_fe2_percent': l_fe2_747 * 100.0,
            'factor_drop': ratio_fe2_747,
            'passed': (m_fe2_747 > 0.60) and (l_fe2_747 < 0.20),
        },
        {
            'name': '813_keV_E2_fraction_drops_from_over_70_percent_to_near_12_percent',
            'matta_fe2_percent': m_fe2_813 * 100.0,
            'lv_fe2_percent': l_fe2_813 * 100.0,
            'factor_drop': ratio_fe2_813,
            'passed': (m_fe2_813 > 0.70) and (l_fe2_813 < 0.15),
        },
        {
            'name': '813_keV_reported_BE2out_in_collapses_by_factor_of_7',
            'matta_reported': m_be2_813,
            'lv_reported': l_be2_813,
            'factor_difference': factor_diff_be2_813,
            'passed': factor_diff_be2_813 > 6.5,
        },
        {
            'name': 'two_phonon_connecting_line_450_keV_E2_fraction_collapses_to_under_10_percent',
            'lv_fe2_percent': l_fe2_450 * 100.0,
            'passed': l_fe2_450 < 0.10,
        }
    ]

    output_data = {
        'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'raw_sha_matta': sha_m,
        'raw_sha_lv': sha_l,
        'contrast_747': {
            'matta_delta': m_d747, 'matta_f_E2': m_fe2_747,
            'lv_delta': l_d747, 'lv_f_E2': l_fe2_747,
            'f_E2_ratio_matta_over_lv': ratio_fe2_747,
        },
        'contrast_813': {
            'matta_delta': m_d813, 'matta_f_E2': m_fe2_813, 'matta_BE2out_in': m_be2_813,
            'lv_delta': l_d813, 'lv_f_E2': l_fe2_813, 'lv_BE2out_in': l_be2_813,
            'f_E2_ratio_matta_over_lv': ratio_fe2_813,
            'BE2out_in_factor_difference': factor_diff_be2_813,
        },
        'contrast_450': {
            'lv_delta': l_d450, 'lv_f_E2': l_fe2_450,
        },
        'checks': checks,
        'checks_total': len(checks),
        'checks_passed': sum(x['passed'] for x in checks),
        'all_passed': all(x['passed'] for x in checks),
        'physical_interpretation': (
            'In low-spin wobbling landmark nucleus 135Pr, Matta et al. 2015 claimed discovery of transverse wobbling based on '
            'large E2/M1 mixing ratios (|delta| > 1) giving E2 dominance (60.6% and 70.3% for 747 and 813 keV) and a massive '
            'B(E2)out/B(E2)in ratio of 0.843(32) for the 813-keV line. '
            'However, Lv et al. 2022 performed high-statistics linear polarization (P) and angular correlation (Rac) measurements in JUROGAM II, '
            'conclusively proving that the true solutions are |delta| < 1 (-0.47 and -0.37), which collapses the E2 fraction down to only 18.1% and 12.0%, '
            'and reduces the extracted B(E2)out/B(E2)in for 813 keV from 0.843 down to 0.12(8) — a CATASTROPHIC FACTOR-OF-7.0 COLLAPSE! '
            'Similarly, the 450-keV line connecting the putative two-phonon band drops to just 8.8% E2. '
            'This collapse of E2 strength below single-particle levels completely ruled out the transverse wobbling interpretation of 135Pr, '
            'resolving it into tilted precession / single-particle alignment competition. '
            'This provides the ultimate Day 18 cautionary benchmark: transition strength extraction and collective band classification '
            'are entirely hostage to multipole-mixing determination; a false assignment of delta roots can fabricate phantom collective excitations.'
        ),
    }
    a.output.write_text(json.dumps(output_data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_passed': output_data['all_passed'], 'checks_total': len(checks)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
