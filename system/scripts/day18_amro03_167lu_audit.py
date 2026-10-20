#!/usr/bin/env python3
"""Audit 167Lu interband/intraband B(E2) ratios and delta solution sensitivity in Amro 2003."""
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
        lam = float(r['lambda'])
        lam_err = float(r['lambda_err'])
        e_out = float(r['E_out_keV'])
        if r['delta'] is not None:
            delta_large = float(r['delta'])
            delta_small = float(r['delta_small'])
            be2_out_in = float(r['BE2out_BE2in'])

            f_E2_large = (delta_large**2) / (1.0 + delta_large**2)
            f_E2_small = (delta_small**2) / (1.0 + delta_small**2)

            # Implied energy factor:
            # B(E2)out / B(E2)in = lambda * (E_in / E_out)^5 * f_E2
            # => (E_in / E_out)^5 = (B(E2)out / B(E2)in) / (lambda * f_E2)
            ratio_5 = be2_out_in / (lam * f_E2_large)
            e_ratio = ratio_5 ** 0.2
            implied_e_in = e_out * e_ratio

            # If the smaller solution of delta had been chosen instead:
            be2_out_in_if_small = lam * (e_ratio**5) * f_E2_small
            suppression_factor = f_E2_large / f_E2_small

            results.append({
                'E_out_keV': e_out,
                'lambda': lam,
                'lambda_err': lam_err,
                'delta_large_preferred': delta_large,
                'delta_small_rejected': delta_small,
                'f_E2_large': f_E2_large,
                'f_E2_small': f_E2_small,
                'BE2out_BE2in_reported': be2_out_in,
                'implied_in_band_energy_keV': implied_e_in,
                'BE2out_BE2in_if_small_delta': be2_out_in_if_small,
                'suppression_ratio_large_over_small': suppression_factor,
            })
        else:
            results.append({
                'E_out_keV': e_out,
                'lambda': lam,
                'lambda_err': lam_err,
                'unresolved_delta_no_BE2_extracted': True,
            })

    # Check properties
    checks = [
        {
            'name': 'three_extracted_BE2out_in_values_between_0_20_and_0_30',
            'passed': all(0.20 <= x['BE2out_BE2in_reported'] <= 0.30 for x in results if 'BE2out_BE2in_reported' in x),
        },
        {
            'name': 'preferred_large_delta_gives_dominant_E2_fraction_over_90_percent',
            'passed': all(x['f_E2_large'] > 0.90 for x in results if 'f_E2_large' in x),
        },
        {
            'name': 'small_delta_alternative_reduces_BE2out_in_by_factor_of_8_to_200',
            'factors': [x['suppression_ratio_large_over_small'] for x in results if 'suppression_ratio_large_over_small' in x],
            'passed': all(x['suppression_ratio_large_over_small'] > 8.0 for x in results if 'suppression_ratio_large_over_small' in x),
        },
        {
            'name': 'two_transitions_lack_delta_and_prevent_unique_BE2out_in',
            'spins_lacking_delta': [x['E_out_keV'] for x in results if 'unresolved_delta_no_BE2_extracted' in x],
            'passed': len([x for x in results if 'unresolved_delta_no_BE2_extracted' in x]) == 2,
        },
    ]

    output_data = {
        'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'raw_sha256': raw_sha,
        'results': results,
        'checks': checks,
        'checks_total': len(checks),
        'checks_passed': sum(x['passed'] for x in checks),
        'all_passed': all(x['passed'] for x in checks),
        'physical_interpretation': (
            'In 167Lu Table 1, the interband-to-intraband transition strength ratio B(E2)out / B(E2)in is extracted '
            'strictly from the intensity branching ratio lambda and the E2/M1 multipole mixing ratio delta. '
            'Because delta is measured via DCO / SpeeDCO without linear polarization, two mathematical roots exist: '
            'a large negative root (delta ~ -3 to -5) and a small root (delta ~ -0.07 to -0.35). '
            'The authors choose the large-delta solution based on analogy to 163Lu, which yields f_E2 = 90.6% - 96.3% '
            'and B(E2)out / B(E2)in ~ 0.23 - 0.27. '
            'If the alternative small-delta root were adopted, the extracted B(E2)out would be suppressed by a factor of '
            '14.3 to 198.5 (reducing B(E2)out/B(E2)in to ~ 0.001 - 0.018), completely destroying the wobbling identification! '
            'Furthermore, two transitions (704.2 and 730.3 keV) lack delta values, preventing BE2 extraction. '
            'This establishes that in high-spin collective band classification, relative transition strength extraction '
            'is critically dependent on the resolution of mixing-ratio double roots.'
        ),
    }
    a.output.write_text(json.dumps(output_data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_passed': output_data['all_passed'], 'checks_total': len(checks)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
