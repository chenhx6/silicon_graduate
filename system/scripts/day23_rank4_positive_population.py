"""Ideal photon-rank4 convex population bounds; no experimental delta inference."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_halfspin_singles_response import photon_parts, population
from day23_au187_source_F_bridge import source_F, source_rho


def projected_components(two_i, two_f, order):
    x, wx = np.polynomial.legendre.leggauss(order)
    moment = np.zeros((3, two_i + 1))
    norm = np.zeros((2, two_i + 1))
    for node, weight in zip(x, wx):
        d, q = photon_parts(two_i, two_f, math.acos(float(node)))
        p4 = np.polynomial.legendre.legval(node, [0, 0, 0, 0, 1])
        dd = np.sum(abs(d) ** 2, axis=(0, 1))
        qq = np.sum(abs(q) ** 2, axis=(0, 1))
        cross = 2 * np.real(np.sum(d.conj() * q, axis=(0, 1)))
        moment += 9 / 2 * weight * p4 * np.array([dd, qq, cross])
        norm += weight / 2 * np.array([dd, qq])
    return moment, norm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    c = json.loads(a.contract.read_text())
    rows = {}
    max_convergence = max_norm = max_forbidden = max_source = max_reflection = max_fraction = max_convex = 0.0
    for pair in c['spins']:
        ti, tf = pair['two_I'], pair['two_If']
        moments, norm = projected_components(ti, tf, 24)
        moments12, _ = projected_components(ti, tf, 12)
        max_convergence = max(max_convergence, float(np.max(abs(moments - moments12))))
        max_norm = max(max_norm, float(np.max(abs(norm - 1))))
        max_forbidden = max(max_forbidden, float(max(abs(moments[0]))), float(max(abs(moments[2]))))
        max_reflection = max(max_reflection, float(max(abs(moments[1] - moments[1, ::-1]))))
        for index in range(ti + 1):
            one = np.eye(ti + 1)[index]
            direct = source_rho(ti, 4, one) * source_F(ti, tf, 2, 2, 4)
            max_source = max(max_source, abs(direct - moments[1, index]))
        amin, amax = float(min(moments[1])), float(max(moments[1]))
        w = population(ti, .2)
        for d in c['design_mixing_coordinates']:
            mixed = np.dot((moments[0] + d * moments[2] + d * d * moments[1]) / (1 + d * d), w)
            frac = d * d / (1 + d * d)
            max_fraction = max(max_fraction, abs(mixed - frac * np.dot(moments[1], w)))
        # Fixed deterministic positive populations, not inferred from nuclear data.
        for n in range(1, 7):
            weights = np.arange(1, ti + 2, dtype=float) ** n
            weights /= sum(weights)
            value = float(np.dot(weights, moments[1]))
            max_convex = max(max_convex, amin - value, value - amax)
        rows[str(ti)] = {'two_I': ti, 'two_If': tf,
                         'pure_E2_C4_for_each_M': [{'M': m / 2, 'C4': float(v)} for m, v in zip(range(-ti, ti + 1, 2), moments[1])],
                         'pure_E2_positive_population_C4_range': [amin, amax]}
    examples = []
    for source in c['source_coordinate_examples']:
        maximum = rows[str(source['two_I'])]['pure_E2_positive_population_C4_range'][1]
        examples.append({'source_coordinate': source, 'conditional_necessary_fraction_floor': source['A4'] / maximum,
                         'meaning': 'necessary mathematical condition IF source coordinate is the physical ideal C4 layer; not an experimental fraction/CI/delta'})
    controls = {'pure_each_M_angular_normalization': max_norm < 1e-12,
                '12_vs24_projection_converged': max_convergence < 1e-12,
                'rank4_M1square_and_interference_zero': max_forbidden < 1e-12,
                'rank4_E2_direct_source_F_matches_photon_projection': max_source < 1e-12,
                'Mreflection_same_C4': max_reflection < 1e-12,
                'mixed_C4_equals_fE2_times_pure_E2': max_fraction < 1e-12,
                'positive_population_convex_hull_controls': max_convex < 1e-12}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': c['scope'], 'formal_day_index': 23, 'conditions': c,
           'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
           'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'spin_rows': rows, 'coordinate_examples_only': examples,
           'controls': controls, 'all_controls_pass': all(controls.values()),
           'errors': {'norm': max_norm, 'projection': max_convergence, 'forbidden_rank4': max_forbidden,
                      'source_F': max_source, 'reflection': max_reflection, 'fraction_relation': max_fraction, 'convex_hull': max_convex},
           'limitations': ['Scalar polar-angle distribution after complete azimuth mean, positive populations and only M1/E2 multipoles.',
                          'No actual finitearray/gate/acceptance or fitted P4 coefficient transfer is supplied.',
                          'Source Fig4.12 and Table4.4 stages remain unbound; examples do not reconstruct measured E2 fractions or delta bounds.',
                          'No source covariance, confidence coverage, likelihood, actual root selection or equal-minimum assertion.',
                          'No physical operator scale, lifetime, count rate or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'],
                      'ranges': {k: v['pure_E2_positive_population_C4_range'] for k, v in rows.items()},
                      'examples': examples, 'errors': out['errors']}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
