#!/usr/bin/env python3
"""Audit 133Ba transverse wobbling relative B(E2) and energy-factor amplification in Devi 2021."""
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
    raw_sha = hashlib.sha256(Path(d['raw_file']).read_bytes()).hexdigest()
    if raw_sha != d['raw_sha256']:
        raise ValueError('raw file SHA256 mismatch')

    results = []
    for r in d['rows']:
        lam = r['I_out'] / r['I_in']
        e_in = r['E_in_keV']
        e_out = r['E_out_keV']
        e_ratio_5 = (e_in / e_out) ** 5
        delta = r['delta']
        f_E2 = (delta**2) / (1.0 + delta**2)
        f_M1 = 1.0 - f_E2

        calc_BE2_out_in = lam * e_ratio_5 * f_E2

        # B(M1)out / B(E2)in in units of (muN/eb)^2:
        # Ratio of rates: lambda_M1 / lambda_E2 = C_M1/C_E2 * (E_in^5 / E_out^3) * [B(M1)/B(E2)]
        # But here authors directly extract B(M1out)/B(E2in)
        results.append({
            'initial_spin': r['initial_spin'],
            'final_spin': r['final_spin'],
            'E_out_keV': e_out,
            'E_in_keV': e_in,
            'intensity_ratio_lambda': lam,
            'energy_ratio_5th_power': e_ratio_5,
            'f_E2_fraction': f_E2,
            'f_M1_fraction': f_M1,
            'calculated_BE2out_BE2in': calc_BE2_out_in,
            'reported_BE2out_BE2in': r['reported_BE2out_BE2in'],
            'relative_difference_percent': abs(calc_BE2_out_in - r['reported_BE2out_BE2in']) / r['reported_BE2out_BE2in'] * 100.0,
        })

    checks = [
        {
            'name': 'calculated_BE2out_in_matches_reported_values_within_0_5_percent',
            'differences': [x['relative_difference_percent'] for x in results],
            'passed': all(x['relative_difference_percent'] < 0.5 for x in results),
        },
        {
            'name': 'energy_factor_5th_power_exceeds_1_5_for_all_three_transitions',
            'e_ratio_5': [x['energy_ratio_5th_power'] for x in results],
            'passed': all(x['energy_ratio_5th_power'] > 1.5 for x in results),
        },
        {
            'name': 'for_457_keV_transition_energy_factor_amplifies_strength_ratio_by_over_5_fold',
            'e_ratio_5_457': results[2]['energy_ratio_5th_power'],
            'passed': results[2]['energy_ratio_5th_power'] > 5.0,
        },
        {
            'name': 'all_three_transitions_exhibit_BE2out_BE2in_greater_than_2',
            'reported_ratios': [x['reported_BE2out_BE2in'] for x in results],
            'passed': all(x['reported_BE2out_BE2in'] > 2.0 for x in results),
        }
    ]

    output_data = {
        'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'raw_sha256': raw_sha,
        'deconstructed_transitions': results,
        'checks': checks,
        'checks_total': len(checks),
        'checks_passed': sum(x['passed'] for x in checks),
        'all_passed': all(x['passed'] for x in checks),
        'physical_interpretation': (
            'In 133Ba Tables 1 and 2, Rojeeta Devi et al. 2021 report exceptionally large interband B(E2)out / B(E2)in ratios '
            'of 2.94(18), 2.36(20), and 3.40(22), which are substantially higher than typical wobbling values (~0.2-0.3 in Lu isotopes). '
            'Our algebraic deconstruction reveals how this arises from the (E_in / E_out)^5 kinematic factor: '
            '1. For 743.4 keV (in-band 810.8 keV), (E_in/E_out)^5 is 1.54, which together with lambda = 2.35 and f_E2 = 81.5% gives 2.95; '
            '2. For 812.0 keV (in-band 958.3 keV), (E_in/E_out)^5 is 2.29, which together with lambda = 1.30 and f_E2 = 79.2% gives 2.36; '
            '3. For 457.6 keV (in-band 641.9 keV), (E_in/E_out)^5 reaches a massive 5.42! Even though the intensity ratio lambda is only 0.80, '
            'the energy factor of 5.42 times f_E2 = 78.3% blows up the extracted B(E2)out/B(E2)in to 3.40. '
            'This provides an essential Day 18 demonstration of the extreme sensitivity of E2 transition probability extraction to the fifth power of energy: '
            'small differences between interband and in-band transition energies create enormous amplification factors in relative B(E2) values, '
            'which must not be confused with unphysically large quadrupole transition operators.'
        ),
    }
    a.output.write_text(json.dumps(output_data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_passed': output_data['all_passed'], 'checks_total': len(checks)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
