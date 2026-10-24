#!/usr/bin/env python3
"""Replay saved public-calculator controls; --fetch explicitly queries current NNDC.

All levels, mass Q values, and intensities below are constructed single-channel
controls, not new nuclear measurements. No input uncertainties or experimental
confidence interval are manufactured. Current server code version is unknown.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'
URL = 'https://www.nndc.bnl.gov/logft/LogFTDataServlet'
ME_KEV = 510.99895  # declared constant as in checkpoint099
CASES = [
    ('endpoint329', 3290, 1.16, 0, 100),
    ('endpoint374', 3740, 1.17, 0, 100),
    ('endpoint374_shifted', 3740, 1.17, 1000, 100),
    ('endpoint374_branch50', 3740, 1.17, 0, 50),
]


def payload(endpoint, half_life, ex, intensity):
    return {
        'nuclide': '100SN', 'decay_mode': 'B+',
        'parent_energy_value': '0', 'parent_energy_error': None,
        'parent_half_life_value': str(half_life), 'parent_half_life_unit': 's',
        'parent_half_life_error': None,
        'parent_q_value': f'{endpoint + ex + 2 * ME_KEV:.4f}', 'parent_q_error': None,
        'daughter_energy_value': str(ex), 'daughter_energy_error': None,
        'transition_intensity_value': str(intensity), 'transition_intensity_error': None,
        'uniqueness': None,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--fetch', action='store_true')
    args = ap.parse_args()
    records = []
    for name, endpoint, half_life, ex, intensity in CASES:
        p = RUN / f'logft-current-{name}-102.json'
        expected = payload(endpoint, half_life, ex, intensity)
        if args.fetch and not p.exists():
            rec = {
                'case': name, 'at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'url': URL, 'payload': expected, 'scope': 'constructed central-only single-channel control',
                'mass_Q_measured': False, 'intensity_measured': False, 'historical_replay': False,
            }
            try:
                request = urllib.request.Request(URL, data=json.dumps(expected).encode(),
                    headers={'Content-Type': 'application/json'}, method='POST')
                with urllib.request.urlopen(request, timeout=30) as response:
                    body = response.read()
                    rec.update(http_status=response.status, response_sha256=hashlib.sha256(body).hexdigest(),
                        response=json.loads(body), raw_response_utf8=body.decode())
            except Exception as exc:
                rec['error'] = str(exc)
            p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + '\n')
        rec = json.loads(p.read_text())
        assert rec['payload'] == expected, f'input changed: {name}'
        assert rec.get('http_status') == 200 and rec['response'].get('success') is True, rec
        assert hashlib.sha256(rec['raw_response_utf8'].encode()).hexdigest() == rec['response_sha256']
        rec['response_file'] = str(p.relative_to(ROOT))
        records.append(rec)
    values = [r['response']['values'] for r in records]
    assert values[1] == values[2], 'Common shift of Q and Ex must preserve endpoint'
    # Server publishes rounded logft values, so no unrounded f/CI is inferred.
    assert abs(values[3]['logft_value'] - values[1]['logft_value'] - .30103) < .011
    for v in values[:3]:
        assert abs(v['iec_value'] + v['ibp_value'] - 100) < .11
    assert abs(values[3]['iec_value'] + values[3]['ibp_value'] - 50) < .11
    out = {
        'scope': 'current NNDC numerical interface controls, not historical data/producer replay',
        'cases': [{'case': r['case'], 'values': r['response']['values'],
            'file': r['response_file'], 'response_sha256': r['response_sha256']} for r in records],
        'controls': {'same_endpoint_translation': True, 'absolute_branch_normalization': True,
            'EC_plus_beta_sum': True, 'saved_response_identity': True},
        'server_version': None, 'input_uncertainties': None, 'experimental_CI': None,
        'missing': ['historical LOGFT executable/options', 'actual parent branch and joint experimental covariance'],
        'independence': 'A new implementation calculation is not an independent nuclear experiment',
        'scientific_certification': False,
    }
    p = RUN / 'logft-contract-result-102.json'
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
