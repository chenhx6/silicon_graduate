#!/usr/bin/env python3
"""Variance envelope of a FIXED linear contrast with specified marginal errors.

The error symmetrization is a task choice. PSD correlation matrices below are
declared mathematical constructions, not recovered experimental covariances.
No refitted GLS, MINOS interval, event simulation or new source reading.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np


def pair_vectors(a, b, resultant):
    """Two vectors of lengths a,b summing to (resultant,0)."""
    ca = (resultant**2 + a*a - b*b)/(2*resultant*a)
    assert abs(ca) <= 1 + 1e-12
    x = a*ca
    h = math.sqrt(max(0, a*a-x*x))
    return np.array([[x, h], [resultant-x, -h]])


def closed_vectors(lengths):
    """Construct an exact closing triangle or quadrilateral for these data."""
    order = np.argsort(lengths)[::-1]
    ell = lengths[order]
    if len(ell) == 3:
        vertices = np.vstack([pair_vectors(ell[0], ell[1], ell[2]), [-ell[2], 0]])
    elif len(ell) == 4:
        low = max(abs(ell[0]-ell[1]), abs(ell[2]-ell[3]))
        high = min(ell[0]+ell[1], ell[2]+ell[3])
        assert low <= high
        resultant = (low+high)/2
        vertices = np.vstack([pair_vectors(ell[0], ell[1], resultant),
                              -pair_vectors(ell[2], ell[3], resultant)])
    else:
        raise ValueError('This construction covers only the actual 3/4 finite rows')
    result = np.empty_like(vertices)
    result[order] = vertices
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    ledger = json.loads(args.input.read_text())
    cases = {}
    checks = []

    def check(name, value):
        checks.append({'name': name, 'passed': bool(value)})
        if not value:
            raise AssertionError(name)

    for key in ['case_Ce131', 'case_Pr133']:
        rows = [r for r in ledger[key]['rows'] if r['Qt']['kind'] == 'finite']
        spin = np.array([r['spin'] for r in rows])
        moment = np.array([r['Qt']['value'] for r in rows])
        sigma = np.array([(r['Qt']['minus']+r['Qt']['plus'])/2 for r in rows])
        weights = sigma**-2
        centered = spin - np.average(spin, weights=weights)
        contrast = weights*centered / np.sum(weights*centered**2)
        estimate = float(contrast@moment)
        lengths = abs(contrast)*sigma
        upper_se = float(sum(lengths))
        lower_se = float(max(0, 2*max(lengths)-sum(lengths)))
        check(key+' contrast ignores constant offset and has unit slope',
              np.isclose(sum(contrast), 0) and np.isclose(contrast@spin, 1))

        # Maximal covariance: signed perfectly correlated errors.
        response_max = sigma*np.sign(contrast)
        cov_max = np.outer(response_max, response_max)
        check(key+' upper envelope attained by signed rank1 Gram matrix',
              np.isclose(contrast@cov_max@contrast, upper_se**2))

        # Minimum covariance: polygon closure of contrast-weighted noise vectors.
        check(key+' lower bound permits closure', lower_se == 0)
        vectors = closed_vectors(lengths)
        unit_noise = np.sign(contrast)[:, None] * vectors/lengths[:, None]
        cov_min = np.outer(sigma, sigma)*(unit_noise@unit_noise.T)
        check(key+' closing construction retains every marginal variance',
              np.allclose(np.diag(cov_min), sigma**2))
        check(key+' lower envelope covariance is PSD and slope variance zero',
              min(np.linalg.eigvalsh(cov_min)) > -1e-12
              and abs(contrast@cov_min@contrast) < 1e-14)

        independent_variance = float(np.sum(lengths**2))
        eps = 1e-5
        diagonal = np.diag(sigma**2)
        strict_max = (1-eps)*cov_max+eps*diagonal
        strict_min = (1-eps)*cov_min+eps*diagonal
        check(key+' positive definite approximations preserve diagonals',
              np.allclose(np.diag(strict_min), sigma**2)
              and np.allclose(np.diag(strict_max), sigma**2)
              and min(np.linalg.eigvalsh(strict_min)) > 0
              and min(np.linalg.eigvalsh(strict_max)) > 0)
        check(key+' positive definite limits obey convex variance formulas',
              np.isclose(contrast@strict_min@contrast, eps*independent_variance)
              and np.isclose(contrast@strict_max@contrast,
                             (1-eps)*upper_se**2+eps*independent_variance))
        cases[key] = {
            'selected_spins': spin.tolist(), 'fixed_contrast': contrast.tolist(),
            'slope_eb_per_hbar': estimate,
            'chosen_symmetrized_sigmas_eb': sigma.tolist(),
            'independent_SE': math.sqrt(independent_variance),
            'PSD_correlation_SE_envelope': [lower_se, upper_se],
            'slope_over_max_SE': estimate/upper_se,
            'max_variance_correlation': (cov_max/np.outer(sigma, sigma)).tolist(),
            'min_variance_correlation': (cov_min/np.outer(sigma, sigma)).tolist(),
            'positive_definite_epsilon': eps,
            'source_locator': ledger[key]['locator'],
        }
    result = {
        'checkpoint': '102',
        'kind': 'fixed-estimator covariance sensitivity with declared marginal errors',
        'experimental_CI': False, 'refitted_GLS': False,
        'cases': cases, 'controls': checks,
        'all_controls_passed': all(r['passed'] for r in checks),
        'theorem': 'For lengths |a_i|sigma_i, SD(a^T y) ranges over [max(2max(length)-sum(length),0), sum(length)] across PSD correlation Gram matrices.',
        'limits': [
            'Unknown experimental joint Cov is not estimated by extremizing over designs.',
            'The same fixed WLS contrast is used in every case; GLS would refit weights.',
            'Gaussian marginal symmetrization is an assumed task model; no MINOS or limit likelihood reconstructed.',
            'Zero-variance endpoints may be singular; positive definite approximations are provided.',
            'No timing spectrum, exponential waiting time, alignment or stopping simulation is performed.',
        ],
        'input_sha256': hashlib.sha256(args.input.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({'controls': len(checks), 'cases': {
        k: {'SE_interval': v['PSD_correlation_SE_envelope'],
            'slope_over_max_SE': v['slope_over_max_SE']} for k, v in cases.items()}}))


if __name__ == '__main__':
    main()
