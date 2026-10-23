#!/usr/bin/env python3
"""Conditional intrinsic charge quadrupole for an explicitly specified surface.

R(theta)=c R0[1+b2 Y20+b4 Y40]. Compare constant-volume/constant-density
with c=1 and density adjusted to conserve charge. These are different model
families, not two implementations of an identified experimental producer.
No lab-state CG, lifetime refit, actual beta4, parameter CI or author algorithm.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json
import math

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq


def multiply(a, b):
    result = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def exact_integral(poly):
    return sum((2*x/F(i+1) for i, x in enumerate(poly) if i % 2 == 0), F(0))


def gaunt_coefficients():
    p2 = [F(-1, 2), F(0), F(3, 2)]
    p4 = [F(3, 8), F(0), F(-30, 8), F(0), F(35, 8)]
    i222 = exact_integral(multiply(multiply(p2, p2), p2))
    i224 = exact_integral(multiply(multiply(p2, p2), p4))
    i244 = exact_integral(multiply(multiply(p4, p4), p2))
    n2, n4 = math.sqrt(5/(4*math.pi)), 3/math.sqrt(4*math.pi)
    return {'Legendre_integrals_exact': {'222': str(i222), '224': str(i224), '244': str(i244)},
            'c22': 2*2*math.pi*n2**3*float(i222),
            'c24': 4*2*math.pi*n2**2*n4*float(i224),
            'c44': 2*2*math.pi*n2*n4**2*float(i244)}


def moment_normalized(b2, b4, family='constant_volume', order=32):
    x, weights = leggauss(order)
    y2 = math.sqrt(5/(16*math.pi))*(3*x*x-1)
    y4 = 3/(16*math.sqrt(math.pi))*(35*x**4-30*x*x+3)
    u = 1+b2*y2+b4*y4
    if np.min(u) <= 0:
        raise ValueError('surface radius must remain positive')
    volume_ratio = float(np.dot(weights, u**3)/2)
    angular_q = float(2*math.pi*np.dot(weights, y2*u**5)/5)
    if family == 'constant_volume':
        scale = volume_ratio**(-1/3)
        density_factor = 1.
    elif family == 'density_rescaled':
        scale = 1.
        density_factor = 1/volume_ratio
    else:
        raise ValueError(family)
    return {'q_over_prefactor': density_factor*scale**5*angular_q,
            'volume_ratio': scale**3*volume_ratio,
            'charge_ratio': density_factor*scale**3*volume_ratio,
            'radius_scale': scale, 'density_factor': density_factor}


def prefactor_eb(z, a, r0):
    return 3*z*(r0*a**(1/3))**2/(math.sqrt(5*math.pi)*100)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    checks = []

    def check(name, value):
        checks.append({'name': name, 'passed': bool(value)})
        if not value:
            raise AssertionError(name)

    coefficients = gaunt_coefficients()
    c22, c24, c44 = (coefficients[k] for k in ['c22', 'c24', 'c44'])
    # Independent closed Gaunt forms versus exact Legendre-product integration.
    check('quadratic Gaunt closed forms', np.allclose(
        [c22, c24, c44], [2/7*math.sqrt(5/math.pi),
                         12/(7*math.sqrt(math.pi)),
                         20/77*math.sqrt(5/math.pi)], rtol=1e-14))
    cases = []
    for b2, b4 in [(0, 0), (.2, -.03), (.35, 0), (.4, .25)]:
        for family in ['constant_volume', 'density_rescaled']:
            q16 = moment_normalized(b2, b4, family, 16)
            q64 = moment_normalized(b2, b4, family, 64)
            check(f'{family} {b2},{b4} angular quadrature convergence',
                  abs(q16['q_over_prefactor']-q64['q_over_prefactor']) < 1e-12)
            check(f'{family} {b2},{b4} total charge conserved',
                  math.isclose(q64['charge_ratio'], 1, abs_tol=1e-14))
            if family == 'constant_volume':
                check(f'{family} {b2},{b4} volume conserved',
                      math.isclose(q64['volume_ratio'], 1, abs_tol=1e-14))
            cases.append({'b2': b2, 'b4': b4, 'family': family, **q64})
    check('spherical quadrupole zero', abs(moment_normalized(0, 0)['q_over_prefactor']) < 1e-14)
    small = 1e-5
    check('first-order limit', abs(moment_normalized(small, 0)['q_over_prefactor']/small-1) < 1e-5)

    scaling = []
    for family in ['constant_volume', 'density_rescaled']:
        errors = []
        for scale in [.2, .1, .05, .025]:
            b2, b4 = .2*scale, -.03*scale
            quadratic = b2+c22*b2*b2+c24*b2*b4+c44*b4*b4
            exact = moment_normalized(b2, b4, family)['q_over_prefactor']
            errors.append(abs(exact-quadratic))
        ratios = [a/b for a, b in zip(errors[:-1], errors[1:])]
        check(f'{family} truncation error approaches cubic scaling',
              all(7.5 < ratio < 8.5 for ratio in ratios))
        scaling.append({'family': family, 'scale_values': [.2, .1, .05, .025],
                        'absolute_errors': errors, 'successive_error_ratios': ratios})
    v = moment_normalized(.35, 0, 'constant_volume')['q_over_prefactor']
    d = moment_normalized(.35, 0, 'density_rescaled')['q_over_prefactor']
    check('different exact model families disagree at finite deformation', abs(v-d) > .001)

    inversions = []
    # A reported Q0 central number is only a target for this declared exercise.
    for r0 in [1.2, 1.25]:
        pref = prefactor_eb(60, 134, r0)
        target = 6.8/pref
        quadratic_beta = 2*target/(1+math.sqrt(1+4*c22*target))
        row = {'Z': 60, 'A': 134, 'r0_fm': r0, 'chosen_target_Q_eb': 6.8,
               'prefactor_eb': pref, 'second_order_Gaunt_beta2': quadratic_beta,
               'Singh_printed_0p36_control_beta2': 2*target/(1+math.sqrt(1+4*.36*target))}
        for family in ['constant_volume', 'density_rescaled']:
            beta = brentq(lambda b: moment_normalized(b, 0, family)['q_over_prefactor']-target,
                          0, .8, xtol=1e-14)
            check(f'{family} r0={r0} chosen-bracket inverse residual',
                  abs(pref*moment_normalized(beta, 0, family)['q_over_prefactor']-6.8) < 1e-11)
            row[family+'_beta2'] = beta
        inversions.append(row)
    check('radius prefactor scales as r0 squared',
          math.isclose(inversions[1]['prefactor_eb']/inversions[0]['prefactor_eb'], (1.25/1.2)**2))
    result = {'checkpoint': '110', 'kind': 'declared static uniform-charge surface model',
              'experimental_CI': False, 'author_algorithm_identified': False,
              'coefficients': coefficients, 'surface_cases': cases,
              'asymptotic_checks': scaling, 'conditional_inversions': inversions,
              'controls': checks, 'all_controls_passed': all(c['passed'] for c in checks),
              'exact_contract': 'Q/[3ZeR0^2/sqrt(5pi)] = density_factor*c^5/5 * integral Y20*(1+b2Y20+b4Y40)^5 dOmega; charge conserved in each declared family.',
              'quadratic_contract': 'b2+c22*b2^2+c24*b2*b4+c44*b4^2; volume/density corrections enter at cubic order.',
              'boundaries': ['No lab-state matrix element, K, gamma dynamics, actual beta4, lifetime fit or experimental likelihood is modeled.',
                             'Different exact families reflect different physical assumptions, not an uncertainty interval.',
                             'Using the target6.8eb or obtaining beta near.35 does not identify the Petrache1998 radius/algorithm.',
                             'Singh2016 explicitly prints r0=1.2 and rounded.36 under its own assumptions; higher beta4 terms are this task model only.',
                             'Quadrature is exact for the finite angular polynomials above sufficient order; no time-step evolution or experimental event simulation.'],
              'source_locators': ['SI16-D20-F05/PDF9 Eq4', 'PE98-D20-F03 and R47 corrected101'],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'controls': len(checks), 'coefficients': coefficients,
                      'conditional_inversions': inversions}))


if __name__ == '__main__':
    main()
