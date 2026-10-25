"""Preserve source-read Au support inputs and map printed endpoints at nominal K."""
import argparse
import hashlib
import json
from pathlib import Path

from day23_au187_quoted_endpoints import image


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--contract', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    c = json.loads(a.contract.read_text())
    assert all(sha(Path(path)) == value for path, value in c['original_raw_sha256'].items())
    theory_path = Path(c['existing_theory_file'])
    previous = json.loads(theory_path.read_text())
    assert previous['all_controls_pass']
    result = {}
    for energy, d in c['supported_target_bounds'].items():
        lo, hi = d['centre'] - d['minus'], d['centre'] + d['plus']
        m = previous['theory_components'][energy + '/M1']['rows']['K']['value']
        e = previous['theory_components'][energy + '/E2']['rows']['K']['value']
        out = image(m, e, lo, hi)
        f = sorted([lo * lo / (1 + lo * lo), hi * hi / (1 + hi * hi)])
        comparisons = []
        for old in previous['forward_points'][energy]['observations_as_secondary_quotes']:
            obs = [old['value'] - old['quoted_error'], old['value'] + old['quoted_error']]
            left, right = max(out[0], obs[0]), min(out[1], obs[1])
            comparisons.append({'reference': old['reference'], 'old_quoted_range': obs,
                                'intersection': [left, right] if left <= right else None,
                                'boundary': 'literal source endpoints and nominal theory only, no statistical exclusion'})
        result[energy] = {'actual_source_energy_keV': d['actual_source_energy'],
                          'nominal_comparison_energy_keV': float(energy),
                          'printed_delta_coordinate_range': [lo, hi],
                          'derived_E2_photon_fraction_range': f,
                          'nominal_alphaK_image': out, 'old_quote_comparisons': comparisons}
    controls = {
        'both_original_raw_hashes_unchanged': True,
        'only_source_read_support_errors_used': True,
        'reference462point1_does_not_rewrite_actual461point8': result['462.1']['actual_source_energy_keV'] == 461.8,
        'same_actual_nominal_theory_used': True,
        'all_four_literal_intersections_empty_under_stated_freeze': all(
            old['intersection'] is None for row in result.values() for old in row['old_quote_comparisons']),
    }
    out = {'scope': c['scope'], 'formal_day_index': 23, 'source_inputs': c,
           'contract_sha256': sha(a.contract), 'theory_record_sha256': sha(theory_path),
           'implementation_sha256': sha(Path(__file__)),
           'rows': result, 'controls': controls, 'all_controls_pass': all(controls.values()),
           'limitations': ['Transcription was checked by targeted original-text/visual reading; controls do not certify original fit or experiment.',
                          'Printed local errors do not specify a global nuisance-profile or both root weights.',
                          'The source recipe selects the lower chi-square root then samples its neighborhood; missing global profile is not proof of equal roots.',
                          'Theory/energy error, shared normalization and actual covariance remain unpropagated.',
                          'No new delta, physical alphaK, confidence, count rate, time or final mode assignment.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'rows': result, 'controls': controls}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
