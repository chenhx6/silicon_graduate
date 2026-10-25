"""Map printed coordinate endpoints; intersections have no coverage meaning."""
import argparse
import hashlib
import json
from pathlib import Path


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def alpha(m, e, d):
    return (m + d * d * e) / (1 + d * d)


def image(m, e, lo, hi):
    assert lo <= hi
    candidates = [alpha(m, e, lo), alpha(m, e, hi)]
    if lo <= 0 <= hi:
        candidates.append(m)
    return [min(candidates), max(candidates)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert len(cfg['inputs']) == 1
    f, h = next(iter(cfg['inputs'].items()))
    assert sha(Path(f)) == h
    previous = json.loads(Path(f).read_text())
    assert previous['all_controls_pass']
    rows = {}
    for energy, bound in cfg['delta_bounds'].items():
        m = previous['theory_components'][energy + '/M1']['rows']['K']['value']
        e = previous['theory_components'][energy + '/E2']['rows']['K']['value']
        lo, hi = bound['centre'] - bound['minus'], bound['centre'] + bound['plus']
        out = image(m, e, lo, hi)
        comparisons = []
        for old in previous['forward_points'][energy]['observations_as_secondary_quotes']:
            obs = [old['value'] - old['quoted_error'], old['value'] + old['quoted_error']]
            left, right = max(out[0], obs[0]), min(out[1], obs[1])
            comparisons.append({'reference': old['reference'], 'quoted_alphaK_coordinate_range': obs,
                                'intersection': [left, right] if left <= right else None,
                                'meaning': 'individual coordinate ranges only; no CI, joint feasibility or likelihood'})
        rows[energy] = {'source_bound': bound, 'printed_delta_coordinate_range': [lo, hi],
                        'nominal_alphaK_image': out, 'historical_comparisons': comparisons,
                        'mirrored_delta_image': image(m, e, -hi, -lo),
                        'centre_inside_image': out[0] <= alpha(m, e, bound['centre']) <= out[1]}
    controls = {
        'frozen030_theory_and_secondary_quote_inputs_checked': True,
        'actual_printed_delta_asymmetry_preserved': rows['376.3']['printed_delta_coordinate_range'] == [-.41000000000000003, -.15000000000000002] and rows['462.1']['printed_delta_coordinate_range'] == [-.97, -.05000000000000002],
        'central_points_inside_images': all(r['centre_inside_image'] for r in rows.values()),
        'scalar_ICC_sign_mirror_preserved': all(r['nominal_alphaK_image'] == r['mirrored_delta_image'] for r in rows.values()),
        'all_four_individual_intersections_nonempty': all(v['intersection'] is not None for r in rows.values() for v in r['historical_comparisons']),
    }
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'rows': rows, 'controls': controls,
           'all_controls_pass': all(controls.values()), 'implementation_sha256': sha(Path(__file__)),
           'contract_sha256': sha(args.contract),
           'limitations': ['No intervals are assigned a confidence level or joint probability.',
                          'Nonempty individual intersections are not a shared multivariate fit or experimental certification.',
                          'The nominal theory components are fixed; theoretical and energy errors and their covariance are not propagated.',
                          'No delta was inferred; source endpoints were supplied, including their printed asymmetry.',
                          'No supporting-source delta uncertainties, new counts, lifetime, ICC measurement, rate or time were invented.']}
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'rows': rows, 'controls': controls}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
