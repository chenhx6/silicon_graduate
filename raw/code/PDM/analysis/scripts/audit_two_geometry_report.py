"""Independently integrate saved report PDFs; never regenerate or invert a response."""

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.integrate import trapezoid


def integral_to(x, y, value):
    inside = (x > x[0]) & (x < value)
    axis = np.r_[x[0], x[inside], value]
    return float(trapezoid(np.interp(axis, x, y), axis))


def check_marginal(x, y, stats):
    y = y / trapezoid(y, x)
    # Two-node Gauss quadrature exactly integrates x^2 times each linear PDF cell.
    width = np.diff(x)
    center = (x[:-1] + x[1:]) / 2
    node = np.array([-1 / np.sqrt(3), 1 / np.sqrt(3)])
    samples = center[:, None] + width[:, None] * node / 2
    heights = (y[:-1] + y[1:])[:, None] / 2 + np.diff(y)[:, None] * node / 2
    weights = width[:, None] * heights / 2
    mean = float(np.sum(weights * samples))
    std = float(np.sqrt(np.sum(weights * (samples - mean) ** 2)))
    np.testing.assert_allclose([mean, std], [stats['mean'], stats['std']], atol=2e-12, rtol=2e-12)
    quantiles = [stats['eti'][0], stats['median'], stats['eti'][1]]
    np.testing.assert_allclose([integral_to(x, y, q) for q in quantiles], [.16, .5, .84], atol=2e-12)
    masses = []
    for segment in stats['hdi_segments']:
        lo, hi = segment['bounds']
        mass = integral_to(x, y, hi) - integral_to(x, y, lo)
        np.testing.assert_allclose(mass, segment['mass'], atol=2e-12)
        axis = np.r_[lo, x[(x > lo) & (x < hi)], hi]
        peak = np.interp(axis, x, y).max()
        for left, right in segment['mode_ranges']:
            assert lo - 1e-12 <= left <= right <= hi + 1e-12
            np.testing.assert_allclose(np.interp([left, right], x, y), peak, atol=2e-10, rtol=2e-10)
        masses.append(mass)
    np.testing.assert_allclose(sum(masses), .68, atol=2e-12)
    np.testing.assert_allclose([s['mass_fraction'] for s in stats['hdi_segments']],
                               np.array(masses) / sum(masses), atol=2e-12)
    return {'pdf_area': float(trapezoid(y, x)), 'hdi_integrated_mass': sum(masses),
            'hdi_components': len(masses), 'mean': mean, 'std': std}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('results', type=Path)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.results.read_text())
    checks = []
    for group in ('old_injections', 'new_injections', 'literature'):
        assert len(data[group]) == 30
        for r in data[group]:
            with np.load(args.root / r['source_npz']) as z:
                x, s, pdf = z['angle'], z['sigma_over_i'], z['parameter_density']
                area = float(trapezoid(trapezoid(pdf, x, axis=1), s))
                np.testing.assert_allclose(area, 1., atol=2e-12)
                metrics = {'id': r['id'], 'pdf_area': area}
                for coordinate, axis, marginal in (
                    ('arctan_delta', x, trapezoid(pdf, s, axis=0)),
                    ('sigma_over_i', s, trapezoid(pdf, x, axis=1)),
                ):
                    metrics[coordinate] = check_marginal(axis, marginal, r['statistics'][coordinate])
                a = r['statistics']['arctan_delta']
                t = r['statistics']['tan_angle_statistics']
                np.testing.assert_allclose(np.tan([a['mode'], a['median'], a['mean'], *a['eti']]),
                                           [t['mode'], t['median'], t['mean'], *t['eti']], atol=2e-12, rtol=2e-12)
                for aa, tt in zip(a['hdi_segments'], t['hdi_segments']):
                    np.testing.assert_allclose(np.tan(aa['bounds']), tt['bounds'], atol=2e-12, rtol=2e-12)
                    np.testing.assert_allclose(np.tan(aa['mode_ranges']), tt['mode_ranges'], atol=2e-12, rtol=2e-12)
                    assert aa['mass'] == tt['mass'] and aa['mass_fraction'] == tt['mass_fraction']
                assert (args.results.parent.parents[1] / r['figure']).is_file()
                checks.append(metrics)
    report = {'status': 'passed', 'cases': len(checks), 'inversions_executed': 0,
              'interval_mass': .68, 'quadrature': 'independent two-node Gaussian integration of linear cells',
              'tolerance': 2e-12, 'checks': checks}
    args.output.write_text(json.dumps(report, indent=2) + '\n')
    print('90 saved PDFs: normalization, moments, quantiles, all HDI masses/modes/fractions and tan transforms passed.')


if __name__ == '__main__':
    main()
