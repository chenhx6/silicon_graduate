#!/usr/bin/env python3
"""Audit 135Nd DSAM level lifetime vs in-band transition strength in Mukhopadhyay 2007."""
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

    dict_A = {x['spin']: x for x in d['rows_Band_A']}
    dict_B = {x['spin']: x for x in d['rows_Band_B']}
    spins = ['31/2', '33/2', '35/2', '37/2', '39/2']

    results = []
    for spin in spins:
        row_a = dict_A[spin]
        row_b = dict_B[spin]
        tau_a = F(row_a['tau_ps'])
        tau_b = F(row_b['tau_ps'])
        bm1_a = F(row_a['BM1'])
        bm1_b = F(row_b['BM1'])
        be2_a = F(row_a['BE2'])
        be2_b = F(row_b['BE2'])

        tau_ratio = tau_b / tau_a
        bm1_ratio = bm1_b / bm1_a
        be2_ratio = be2_b / be2_a
        double_ratio = (bm1_b / be2_b) / (bm1_a / be2_a)

        # Under B = C * p_gamma / (tau * E^n):
        # tau * B = C * p_gamma / E^n is the partial-width-equivalent numerator.
        # Ratio of (tau * B)_B / (tau * B)_A indicates the ratio of p_gamma / E^n
        tau_x_be2_ratio = (tau_b * be2_b) / (tau_a * be2_a)
        tau_x_bm1_ratio = (tau_b * bm1_b) / (tau_a * bm1_a)

        results.append({
            'spin': spin,
            'tau_A_ps': float(tau_a),
            'tau_B_ps': float(tau_b),
            'tau_ratio_B_over_A': float(tau_ratio),
            'tau_ratio_exact': str(tau_ratio),
            'BE2_A': float(be2_a),
            'BE2_B': float(be2_b),
            'BE2_ratio_B_over_A': float(be2_ratio),
            'BE2_ratio_exact': str(be2_ratio),
            'BM1_A': float(bm1_a),
            'BM1_B': float(bm1_b),
            'BM1_ratio_B_over_A': float(bm1_ratio),
            'BM1_ratio_exact': str(bm1_ratio),
            'double_ratio_B_over_A': float(double_ratio),
            'double_ratio_exact': str(double_ratio),
            'tau_x_BE2_ratio_B_over_A': float(tau_x_be2_ratio),
            'tau_x_BE2_ratio_exact': str(tau_x_be2_ratio),
            'tau_x_BM1_ratio_B_over_A': float(tau_x_bm1_ratio),
            'tau_x_BM1_ratio_exact': str(tau_x_bm1_ratio),
        })

    checks = [
        {
            'name': 'low_spin_tau_ratio_exceeds_1_9',
            'spins': ['31/2', '33/2', '35/2', '37/2'],
            'passed': all(F(x['tau_ratio_exact']) > F(19, 10) for x in results[:4]),
        },
        {
            'name': 'low_spin_BE2_ratio_near_constant',
            'spins': ['31/2', '33/2', '35/2'],
            'passed': all(F(x['BE2_ratio_exact']) == F(7, 8) for x in results[:3]),
        },
        {
            'name': 'tau_x_BE2_ratio_compensates_lifetime_difference',
            'note': 'tau_B ~ 2*tau_A while BE2_B ~ 0.875*BE2_A requires partial rate numerator (p_gamma/E^5) in B to be ~ 1.7-2.0 times A',
            'passed': all(F(x['tau_x_BE2_ratio_exact']) > F(16, 10) for x in results[:4]),
        },
        {
            'name': 'high_spin_39_2_lifetime_ratio_drops_to_near_unity',
            'spin': '39/2',
            'tau_ratio': float(results[4]['tau_ratio_B_over_A']),
            'passed': abs(results[4]['tau_ratio_B_over_A'] - 1.090909) < 1e-4,
        },
    ]

    output_data = {
        'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'raw_sha256': raw_sha,
        'contrasts': results,
        'checks': checks,
        'checks_total': len(checks),
        'checks_passed': sum(x['passed'] for x in checks),
        'all_passed': all(x['passed'] for x in checks),
        'physical_interpretation': (
            'In 135Nd Table I, B(E2) is nearly identical between Bands A and B (~0.32 vs ~0.28 e2b2) '
            'even though the total mean lifetime tau is ~2 times longer in Band B at low spins (e.g. 1.46 vs 0.75 ps at 31/2-). '
            'Because B(E2) is proportional to p_gamma / (tau * E^5), maintaining equal B(E2) with double tau requires '
            'the partial rate factor p_gamma / E^5 in Band B to be approximately 1.7 to 2.0 times larger than in Band A. '
            'This illustrates that identical B(E2) strengths between partner bands does not imply identical level lifetimes, '
            'and that level lifetimes alone cannot be directly equated to transition strengths without branching and energy compensation.'
        ),
    }
    a.output.write_text(json.dumps(output_data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_passed': output_data['all_passed'], 'checks_total': len(checks)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
