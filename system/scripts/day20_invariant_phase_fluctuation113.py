#!/usr/bin/env python3
"""Declared tensor and commuting-shape witnesses; never an experimental fit.

Finite Hilbert space: one J=0 and two complete J=2 multiplets. E2 reduced
matrix elements are chosen real inputs in an arbitrary fixed quadrupole unit.
No claim of a microscopic charge-coordinate realization for this projected
tensor. A separate commuting positive-Q probability model tests moment ratios.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as Rational
from pathlib import Path

import numpy as np
from day19_evidence_repair_audit import signed_cg as clebsch_gordan


def racah_6j(a: int, b: int, c: int, d: int, e: int, f: int):
    """Independent exact integer-spin Racah sum, returning sign and square."""
    triples = [(a,b,c),(a,e,f),(d,b,f),(d,e,c)]
    delta_product = Rational(1)
    for x,y,z in triples:
        delta_product *= Rational(math.factorial(x+y-z)*math.factorial(x-y+z)
                                  *math.factorial(-x+y+z), math.factorial(x+y+z+1))
    lower = [a+b+c,a+e+f,d+b+f,d+e+c]
    upper = [a+b+d+e,a+c+d+f,b+c+e+f]
    total = sum((Rational((-1)**z*math.factorial(z+1),
                 math.prod(math.factorial(z-x) for x in lower)
                 *math.prod(math.factorial(x-z) for x in upper))
                 for z in range(max(lower),min(upper)+1)), Rational(0))
    return total, delta_product*total**2


STATES = [(0, 0, 0)] + [(n, 2, m) for n in [1, 2] for m in range(-2, 3)]


def tensors(edge: float) -> tuple[dict[int, np.ndarray], np.ndarray]:
    # <J_f,n_f||T||J_i,n_i>; even spin differences make real RMEs symmetric.
    reduced = np.array([[0., .8, .6], [.8, -.4, edge], [.6, edge, .2]])
    ts = {}
    for mu in range(-2, 3):
        t = np.zeros((11, 11))
        for f, (nf, jf, mf) in enumerate(STATES):
            for i, (ni, ji, mi) in enumerate(STATES):
                cg = float(clebsch_gordan(ji, 2, jf, mi, mu, mf))
                t[f, i] = cg * reduced[nf, ni] / np.sqrt(2*jf+1)
        ts[mu] = t
    return ts, reduced


def contractions(ts: dict[int, np.ndarray]) -> tuple[float, float]:
    s2 = np.zeros((11, 11))
    s3 = np.zeros((11, 11))
    for mu in range(-2, 3):
        s2 += float(clebsch_gordan(2, 2, 0, mu, -mu, 0)) * ts[mu] @ ts[-mu]
        for nu in range(-2, 3):
            k = mu + nu
            if abs(k) > 2:
                continue
            weight = float(clebsch_gordan(2, 2, 2, mu, nu, k)
                           * clebsch_gordan(2, 2, 0, k, -k, 0))
            s3 += weight * ts[mu] @ ts[nu] @ ts[-k]
    return float(np.sqrt(5)*s2[0, 0]), float(-np.sqrt(35/2)*s3[0, 0])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise SystemExit('Refusing to overwrite an existing result')
    checks = []

    def check(name: str, error: float, tol: float = 2e-13) -> None:
        checks.append({'name': name, 'max_absolute_error': float(error), 'tolerance': tol})
        if not np.isfinite(error) or abs(error) > tol:
            raise AssertionError(checks[-1])

    jz = np.diag([m for _, _, m in STATES])
    jp = np.zeros((11, 11))
    for i, (n, j, m) in enumerate(STATES):
        if m < j:
            f = STATES.index((n, j, m+1))
            jp[f, i] = np.sqrt((j-m)*(j+m+1))
    ts, r = tensors(.3)
    tm, rm = tensors(-.3)
    check('spherical Hermiticity', max(np.max(abs(ts[m].T-(-1.)**m*ts[-m])) for m in ts))
    check('rank2 Jz commutator', max(np.max(abs(jz@ts[m]-ts[m]@jz-m*ts[m])) for m in ts))
    check('rank2 raising commutator', max(np.max(abs(jp@ts[m]-ts[m]@jp-np.sqrt((2-m)*(3+m))*ts[m+1])) for m in range(-2, 2)))
    sixj_sign, sixj_square = racah_6j(2,2,2,0,2,2)
    assert sixj_sign > 0 and sixj_square == Rational(1,25)
    sixj = math.sqrt(float(sixj_square))
    check('6j I0 coefficient exact squared rational', sixj-.2, 0.)
    q2, q3 = contractions(ts)
    q2m, q3m = contractions(tm)
    a = r[0,1:]
    check('tensor versus reduced q2', q2-float(a@a))
    check('tensor versus signed reduced cubic loop', q3+np.sqrt(35/2)*sixj*float(a@r[1:,1:]@a))
    check('edge reversed tensor versus reduced cubic', q3m+np.sqrt(35/2)*sixj*float(a@rm[1:,1:]@a))
    # Rephase the entire second J2 multiplet: this is a basis change, not an edge change.
    phase = np.diag([1 if n != 2 else -1 for n, _, _ in STATES])
    q2p, q3p = contractions({m: phase@t@phase for m,t in ts.items()})
    check('whole-multiplet phase keeps q2,q3', max(abs(q2p-q2), abs(q3p-q3)))
    check('single edge sign keeps every Bmodulus', np.max(abs(r*r-rm*rm)))
    check('single edge sign keeps q2', q2m-q2)
    if abs(q3-q3m) < .1:
        raise AssertionError('chosen cubic witness did not separate')
    check('common tensor scale q2,q3 and normalized ratio', max(
        abs(contractions({m:2*t for m,t in ts.items()})[0]-4*q2),
        abs(contractions({m:2*t for m,t in ts.items()})[1]-8*q3)))

    # Distinct model: a bona fide positive probability distribution of commuting shapes.
    # Q=(1,2), equal probabilities, and C=cos(3delta)=1 at both points.
    p = [Rational(1,2), Rational(1,2)]
    q = [Rational(1), Rational(2)]
    moment = lambda power: sum(pi*qi**power for pi,qi in zip(p,q))
    m2, m3, m6 = moment(2), moment(3), moment(6)
    constant_c = [Rational(1), Rational(1)]
    mean_q = moment(1)
    mean_constant_c = sum(pi*ci for pi,ci in zip(p,constant_c))
    cov_q_c = sum(pi*qi*ci for pi,qi,ci in zip(p,q,constant_c))-mean_q*mean_constant_c
    true_constant_c_variance = sum(pi*ci**2 for pi,ci in zip(p,constant_c))-mean_constant_c**2
    ratio_squared = m3**2/m2**3
    variance27 = 1-ratio_squared
    assert ratio_squared == Rational(162,125)
    assert variance27 == -Rational(37,125)
    check('probability normalized', float(sum(p)-1), 0.)
    check('constant C true variance and Cov(Q,C)', float(abs(cov_q_c)+abs(true_constant_c_variance)), 0.)
    # Constant-amplitude limit: exact angle moments recovered, variance nonnegative.
    c = [Rational(1), Rational(-1,2)]
    mean_c = sum(pi*ci for pi,ci in zip(p,c))
    second_c = sum(pi*ci**2 for pi,ci in zip(p,c))
    check('constant Q Eq27 reduces to true C variance', float((second_c-mean_c**2)-Rational(9,16)), 0.)

    result = {
        'checkpoint': '113',
        'kind': 'declared tensor and commuting-shape contracts only',
        'source_formula_locators': ['HE20-D20-1 Eq7-10', 'HE20-D20-2 Eq11/27'],
        'finite_tensor': {'states': STATES, 'RME_plus': r.tolist(), 'RME_minus': rm.tolist(),
                          'q2_plus':q2, 'q2_minus':q2m, 'q3_plus':q3, 'q3_minus':q3m,
                          'q3_loop_formula':'-sqrt(7/10) a.T D a for declared I0 sector',
                          'all_Bmoduli_identical':True,
                          'units':'arbitrary fixed quadrupole unit; q2 squared/q3 cubed'},
        'commuting_shape': {'probabilities':['1/2','1/2'], 'Q':[1,2], 'C':[1,1],
                            'Q_delta_independent':True, 'true_mean_C':1, 'true_variance_C':0,
                            'q2':str(m2),'q3':str(m3),'q6':str(m6),
                            'ratio_q3_over_q2_3half':math.sqrt(float(ratio_squared)),
                            'ratio_squared':str(ratio_squared), 'Eq27_radicand':str(variance27),
                            'general_independent_formula':'R=E(Q^3)/E(Q^2)^1.5 * E(C); independent does not remove amplitude-moment factor'},
        'checks': checks, 'controls_executed':len(checks),
        'scientific_certification':False,
        'boundaries':['No actual isotope or fitted nuclear Hamiltonian',
                      'No measured matrix element phase or original shell-model input recovered',
                      'Projected tensor need not be commuting charge coordinates; shape distribution is a separate explicit model',
                      'Does not demonstrate the actual Henderson34-nucleus outputs violate their stated numeric domain',
                      'No event simulation, experimental covariance or CI'],
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'controls_executed':len(checks),'q2':q2,'q3_plus':q3,'q3_minus':q3m,
                      'moment_ratio':result['commuting_shape']['ratio_q3_over_q2_3half'],
                      'Eq27_radicand':str(variance27),'scientific_certification':False}))


if __name__ == '__main__':
    main()
