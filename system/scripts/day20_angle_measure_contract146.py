#!/usr/bin/env python3
"""Exact declared angle-measure counterexample, not an experimental fit or CI.

Uniform gamma and uniform cos(3 gamma) are distinct measures on [0, pi/3].
This does not identify the measure of any nucleus or a particular Hamiltonian.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import math
from scipy.integrate import quad


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing overwrite')
    pi = math.pi
    # Antiderivatives: integral x^2 sin(x) dx =
    # -x^2 cos(x) + 2x sin(x) + 2 cos(x).
    # The following moments are analytic, checked against independent quadrature.
    measures = {
        'uniform_gamma': ('3/pi', lambda g: 3/pi,
                          [1, 0, 1/2, pi/6, pi*pi/27],
                          ['1', '0', '1/2', 'pi/6', 'pi^2/27']),
        'uniform_cos3gamma': ('(3/2) sin(3g)', lambda g: 1.5*math.sin(3*g),
                              [1, 0, 1/3, pi/6, pi*pi/18-2/9],
                              ['1', '0', '1/3', 'pi/6', 'pi^2/18-2/9'])}
    results = {}
    functions = [lambda g: 1, lambda g: math.cos(3*g),
                 lambda g: math.cos(3*g)**2, lambda g: g, lambda g: g*g]
    for name, (expression, density, moments, exact_strings) in measures.items():
        numerical = []
        for f, exact in zip(functions, moments):
            value, error = quad(lambda g: density(g)*f(g), 0, pi/3, epsabs=1e-12)
            if abs(value-float(exact)) > max(1e-11, 5*error):
                raise ArithmeticError('Analytic and quadrature routes disagree')
            numerical.append(value)
        variance_g = moments[4]-moments[3]**2
        results[name] = {'density_per_radian': expression,
                         'moments_exact': exact_strings,
                         'quadrature_moments': numerical,
                         'var_cos3gamma_exact': exact_strings[2],
                         'var_gamma_radians_squared': variance_g,
                         'sd_gamma_degrees': math.sqrt(variance_g)*180/pi}
    # At zero mean cubic invariant: variance uses a sixth-order scalar.
    results['order_contract'] = {'quadrupole_degree': 1,
                                'cubic_scalar_degree': 3,
                                'cubic_scalar_squared_degree': 6,
                                'amplitude_scalar_squared_degree': 4}
    results['boundary'] = ('Declared commuting constant-amplitude model only. '
                           'Both measures have mean cos(3gamma)=0, but different '
                           'variances. A flat potential alone does not specify a '
                           'probability density. No experimental CI or rigidity '
                           'claim is calculated. Poves 18–36 deg is a mapped range, '
                           'not a measured angular standard deviation.')
    args.output.write_text(json.dumps(results, indent=2)+'\n')
    print(json.dumps({k:v['sd_gamma_degrees'] for k,v in results.items()
                      if isinstance(v, dict) and 'sd_gamma_degrees' in v}))


if __name__ == '__main__':
    main()
