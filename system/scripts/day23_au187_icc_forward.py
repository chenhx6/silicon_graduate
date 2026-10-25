"""Offline capture of four frozen BrIcc responses and a nominal K-ICC forward check.

No network, delta inversion, statistical interval or nuclear assignment is performed.
"""
import argparse
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

from bs4 import BeautifulSoup


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def number(value, digits):
    d = Decimal(value)
    return {'value': float(d), 'quoted_error': float(Decimal(digits) * Decimal(10) ** d.as_tuple().exponent),
            'printed': value, 'error_digits': digits}


def mixed(a, e, delta):
    fraction = delta ** 2 / (1 + delta ** 2)
    return (1 - fraction) * a + fraction * e


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--contract', type=Path, required=True)
    p.add_argument('--receipt', type=Path, required=True)
    p.add_argument('--observations', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    cfg = json.loads(args.contract.read_text())
    rec = json.loads(args.receipt.read_text())
    assert rec['contract_sha256'] == digest(args.contract)
    assert len(rec['requests']) == cfg['max_queries'] == 4
    components = {}
    for r in rec['requests']:
        prm = r['parameters']
        assert prm in cfg['requests'] and r['http_status'] == 200 and r['automatic_retries'] == 0
        body = Path(r['path'])
        assert digest(body) == r['sha256']
        soup = BeautifulSoup(body.read_text(), 'html.parser')
        rows = [[td.get_text(' ', strip=True) for td in tr.find_all(['td', 'th'], recursive=False)]
                for tr in soup.find('table').find_all('tr', recursive=False)]
        flat = ' '.join(' '.join(row) for row in rows)
        assert 'Z=79 (Au, Gold)' in flat and f"γ-energy:  {prm['energy']} keV" in flat
        assert 'BrIccFO' in flat and 'BrIccNH' not in flat
        version = next(row[0] for row in rows if row and row[0].startswith('BrIccS'))
        assert next(row[2] for row in rows if row[:2] == ['Shell', 'E(ce)']) == prm['multipole']
        selected = {}
        for label in ['K', 'Tot']:
            row = next(row for row in rows if row and row[0] == label)
            error = re.fullmatch(r'\((\d+)\)', row[3])
            assert error is not None
            selected[label] = number(row[2], error[1])
            selected[label]['electron_energy_string'] = row[1]
        key = prm['energy'] + '/' + prm['multipole']
        assert key not in components
        components[key] = {'parameters': prm, 'program_version': version,
                           'response_sha256': r['sha256'], 'rows': selected}
    expected = {'376.3/M1': '0.1483', '376.3/E2': '0.0360',
                '462.1/M1': '0.0859', '462.1/E2': '0.0225'}
    assert all(components[key]['rows']['K']['printed'] == value for key, value in expected.items())
    old = json.loads(args.observations.read_text())
    assert old['all_controls_pass']
    observations = {}
    for target in old['records']['hg24']['targets']:
        quotes = [r for r in target['records'] if '|a(K)exp=' in r['raw']]
        assert len(quotes) == 1
        q = quotes[0]
        values = re.findall(r'(\d+\.\d+) \{I(\d+)\} \((\d{4}[A-Z][a-z]\d{2})\)', q['raw'])
        assert {v[2] for v in values} == {'1998Ru04', '1978Bo05'}
        observations[target['gamma_energy_string']] = [dict(number(v, e), reference=source,
                                                         source_role='ENSDF quotation of experiment, primary method not verified',
                                                         record_line=q['line']) for v, e, source in values]
    points = {}
    for energy, ds in cfg['comparison_points'].items():
        m = components[energy + '/M1']['rows']['K']['value']
        e = components[energy + '/E2']['rows']['K']['value']
        predictions = {}
        for name, delta in ds.items():
            alpha = mixed(m, e, delta)
            predictions[name] = {'source_delta_centre': delta, 'nominal_alphaK': alpha,
                                 'point_only_not_branch_family': True,
                                 'central_differences_prediction_minus_reported': [
                                     {'reference': v['reference'], 'difference': alpha - v['value']}
                                     for v in observations[energy]]}
        points[energy] = {'nominal_energy_keV': float(energy),
                          'observations_as_secondary_quotes': observations[energy],
                          'predictions': predictions,
                          'sign_invariance_error': max(abs(mixed(m, e, d) - mixed(m, e, -d)) for d in ds.values())}
    controls = {
        'four_frozen_requests_hashes_and_actual_response_roles_checked': True,
        'Z_energy_multipolarity_FO_and_program_version_echo_checked': True,
        'all_four_K_central_and_error_fields_read_not_total': True,
        'historical_alpha_quotes_parsed_from_actual029_records': True,
        'primary_methods_not_promoted_from_annotation': True,
        'two_historical_energies_remain_distinct_from_new461point8_source': True,
        'mixing_sign_unobservable_in_standard_scalar_ICC': all(v['sign_invariance_error'] == 0 for v in points.values()),
        'each_point_is_in_declared_pure_component_envelope': all(
            min(components[en + '/M1']['rows']['K']['value'], components[en + '/E2']['rows']['K']['value'])
            <= p['nominal_alphaK'] <= max(components[en + '/M1']['rows']['K']['value'], components[en + '/E2']['rows']['K']['value'])
            for en, v in points.items() for p in v['predictions'].values()),
        'no_energy_error_or_covariance_silently_propagated': all(not r['parameters']['eerror'] for r in rec['requests']),
    }
    out = {'scope': cfg['scope'], 'formal_day_index': 23,
           'contract_sha256': digest(args.contract), 'receipt_sha256': digest(args.receipt),
           'observation_record_sha256': digest(args.observations),
           'implementation_sha256': digest(Path(__file__)),
           'theory_components': components, 'forward_points': points,
           'controls': controls, 'all_controls_pass': all(controls.values()),
           'limitations': ['Pure theoretical input is not an experimental conversion measurement.',
                          'Printed marginal theory errors are captured; their joint covariance is unknown and no likelihood or interval is assigned.',
                          'Legacy .2keV uncertainty is not propagated; source delta central values are not full allowed families.',
                          'No delta inversion or sign selection, fitted normalization, exclusion significance or nuclear assignment.',
                          'Historical normalizers, shell efficiency, angular response and shared calibration remain unverified.',
                          'Public responses are tmp staging; formal raw archive is deferred.']}
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'],
                      'K_components': {k: v['rows']['K'] for k, v in components.items()},
                      'predicted_alphaK': {e: {n: p['nominal_alphaK'] for n, p in v['predictions'].items()} for e, v in points.items()},
                      'controls': controls}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
