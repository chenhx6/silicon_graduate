#!/usr/bin/env python3
"""Independently check DR70's printed Gaussian example by photon trace."""
import hashlib
import json
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import brentq
from sympy.physics.wigner import clebsch_gordan, wigner_d_small

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def gaussian(j, sigma):
    m = np.arange(-j, j + 1)
    p = np.exp(-m * m / (2 * sigma * sigma))
    return p / p.sum()


@lru_cache(None)
def transfer(j):
    jf = j - 2
    a = np.zeros((2 * jf + 1, 2 * j + 1))
    qweights = np.zeros((5, 2 * j + 1))
    for i, m in enumerate(range(-j, j + 1)):
        for k, mf in enumerate(range(-jf, jf + 1)):
            q = m - mf
            if abs(q) <= 2:
                c = float(clebsch_gordan(jf, 2, j, mf, q, m) ** 2)
                a[k, i] += c
                qweights[2 - q, i] += c
    assert np.max(abs(a.sum(axis=0) - 1)) < 2e-14
    return a, qweights


@lru_cache(None)
def angular_kernel(order):
    x, weights = np.polynomial.legendre.leggauss(order)
    theta = sp.symbols('theta', real=True)
    small = sp.lambdify(theta, wigner_d_small(2, theta), 'numpy')
    kernel = np.array([[2.5 * (small(float(np.arccos(xx)))[q, 1] ** 2
                               + small(float(np.arccos(xx)))[q, 3] ** 2)
                       for xx in x] for q in range(5)])
    assert np.max(abs(kernel @ weights / 2 - 1)) < 1e-13
    return x, weights, kernel


def coefficients(j, p, order=16):
    assert np.min(p) >= 0 and abs(p.sum() - 1) < 1e-14
    _, qw = transfer(j)
    x, weights, kernel = angular_kernel(order)
    w = (qw @ p) @ kernel
    result = []
    for k in [0, 2, 4]:
        pk = np.polynomial.legendre.legval(x, [0] * k + [1])
        result.append(float((2 * k + 1) * np.dot(weights, w * pk) / 2))
    return result


def j2_analytic(p):
    # Pure photon E2 angular functions, independent of CG transfer/projection.
    x = sp.symbols('x', real=True)
    w0 = sp.Rational(15, 2) * (x ** 2 - x ** 4)
    w1 = sp.Rational(5, 4) * (1 - 3 * x ** 2 + 4 * x ** 4)
    w2 = sp.Rational(5, 4) * (1 - x ** 4)
    w = p[2] * w0 + (p[1] + p[3]) * w1 + (p[0] + p[4]) * w2
    return [float((2 * k + 1) * sp.integrate(w * sp.legendre(k, x), (x, -1, 1)) / 2)
            for k in [0, 2, 4]]


def main():
    p = gaussian(12, 5)
    initial = coefficients(12, p)
    cascade = []
    for j in range(12, 1, -2):
        a = coefficients(j, p)
        assert max(abs(np.array(a) - initial)) < 1e-13
        assert max(abs(np.array(a) - coefficients(j, p, 32))) < 1e-13
        cascade.append({'Ji': j, 'coefficients_A0_A2_A4': a, 'population': p.tolist()})
        p = transfer(j)[0] @ p
    sigma_for_printed_a2 = brentq(lambda s: coefficients(2, gaussian(2, s))[1] - .225, .05, 10)
    sigma_for_exact_a2 = brentq(lambda s: coefficients(2, gaussian(2, s))[1] - initial[1], .05, 10)
    candidates = []
    for sigma in [.143, 1.43, sigma_for_printed_a2, sigma_for_exact_a2]:
        p = gaussian(2, sigma)
        a = coefficients(2, p)
        independent = j2_analytic(p)
        assert max(abs(np.array(a) - independent)) < 3e-14
        candidates.append({'sigma': sigma, 'A0_A2_A4': a,
                           'independent_polynomial_A0_A2_A4': independent,
                           'A4_difference_from_exact_cascade': a[2] - initial[2]})
    for j in [2, 4, 12]:
        assert max(abs(np.array(coefficients(j, np.ones(2*j+1)/(2*j+1))) - [1, 0, 0])) < 1e-13
    p0 = np.array([0., 0., 1., 0., 0.])
    assert np.max(abs(np.array(coefficients(2, p0)) - [1, 5/7, -12/7])) < 1e-13
    table_path = RUN / 'draper1970-table1-contract.json'
    table = json.loads(table_path.read_text())
    table_checks = []
    for nucleus, values in table['rows'].items():
        cumulative = [sum(values['smoothed_side'][i:]) for i in range(len(values['J']))]
        differences = [a-b for a, b in zip(values['I_gamma'], values['I_gamma'][1:])]
        inverse = []
        for i, j in enumerate(values['J'][:-1]):
            fraction = values['smoothed_side'][i] / cumulative[i]
            inverse.append({'J': j, 'declared_smoothed_fraction': fraction,
                            'd_A_side_d_A_lower': 1/fraction,
                            'd_A_side_d_A_upper': -(1-fraction)/fraction,
                            'boundary': 'conditional table-input amplification, no propagated experimental CI'})
        table_checks.append({'nucleus': nucleus, 'raw_adjacent_differences': differences,
                             'smoothed_side_input': values['smoothed_side'],
                             'cumulative_smoothed_table_input': cumulative,
                             'raw_Igamma': values['I_gamma'], 'conditional_Eq8_inverse_jacobian': inverse})
    assert abs(table_checks[2]['raw_adjacent_differences'][2] + .17) < 1e-14
    (RUN / 'draper1970-table1-result.json').write_text(json.dumps({
        'at': datetime.now(timezone.utc).isoformat(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256': hashlib.sha256(table_path.read_bytes()).hexdigest(),
        'table_checks': table_checks, 'no_negative_physical_feeding_claim': True,
        'no_smoothfit_covariance_or_IC_imputed': True, 'ok': True}, indent=2)+'\n')
    result = {'at': datetime.now(timezone.utc).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_example': {'Ji': 12, 'sigma': 5, 'printed_A2': .225, 'printed_equivalent_sigma2': .143},
              'exact_cascade': cascade, 'gaussian_comparisons': candidates,
              'positive_sigma_for_printed_A2': sigma_for_printed_a2,
              'positive_sigma_for_exact_cascade_A2': sigma_for_exact_a2,
              'pure_M0_J2_A0_A2_A4': coefficients(2, p0),
              'literal_sigma0143_does_not_reproduce_printed_A2': abs(candidates[0]['A0_A2_A4'][1] - .225) > .4,
              'full_trace_cascade_A2_A4_invariance': True,
              'independent_J2_polynomial_and_quadrature_controls': True,
              'not_an_official_erratum_or_new_measured_alignment': True,
              'no_new_experimental_tau_delta_P_or_Q': True,
              'ok': True}
    (RUN / 'draper1970-gaussian-result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'exact_cascade'}, indent=2))


if __name__ == '__main__':
    main()
