#!/usr/bin/env python3
"""Declared two-state E2 amplitude controls, never a fitted nuclear mechanism.

Real rotations and a diagonal unmixed amplitude operator define the entire
toy model. Relative signs, off-diagonal intrinsic elements, actual mixing
angles and experimental likelihoods are not recovered here.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np


def rotation(theta):
    return np.array([[math.cos(theta), -math.sin(theta)],
                     [math.sin(theta), math.cos(theta)]])


def mixed_operator(qg, qs, theta_i, theta_f):
    return rotation(theta_f).T @ np.diag([qg, qs]) @ rotation(theta_i)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    checks = []

    def check(name, ok):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            raise AssertionError(name)

    # A falsifiable correction of the old printed claim, preserving old result.
    old_qg, old_qs = 5.675780039564039, 4.95
    theta_i = math.radians(26.5)
    actual = mixed_operator(old_qg, old_qs, theta_i, 0)[0, 0]
    check('old26p5deg actual result is5p07945, not5p38',
          math.isclose(actual, 5.0794505863007595, rel_tol=1e-13)
          and not math.isclose(actual, 5.38, abs_tol=.1))
    check('pure final state makes qs irrelevant to selected amplitude',
          mixed_operator(old_qg, 100, theta_i, 0)[0, 0] == actual)
    inverse_theta = math.acos(5.38 / old_qg)
    inverse_probability = math.sin(inverse_theta) ** 2
    check('tuning one free angle matches one center by construction',
          math.isclose(mixed_operator(old_qg, old_qs, inverse_theta, 0)[0, 0], 5.38))
    # Independent scalar expressions and full orthogonal matrix invariants.
    for qi, qf in [(5., 5.), (5., 3.), (5., -3.)]:
        for ti, tf in [(0., 0.), (.3, .7), (-.6, .2)]:
            mat = mixed_operator(qi, qf, ti, tf)
            scalar = qi * math.cos(ti) * math.cos(tf) + qf * math.sin(ti) * math.sin(tf)
            check(f'scalar/matrix {qi},{qf},{ti},{tf}', math.isclose(mat[0, 0], scalar))
            check(f'Frobenius sum {qi},{qf},{ti},{tf}',
                  math.isclose(float(np.sum(mat ** 2)), qi ** 2 + qf ** 2))
            check(f'same-parent daughter sum {qi},{qf},{ti},{tf}',
                  math.isclose(float(np.sum(mat[:, 0] ** 2)),
                               qi ** 2 * math.cos(ti) ** 2 + qf ** 2 * math.sin(ti) ** 2))
    # A unit-normalized 3/5,4/5 rotation gives exact amplitudes 3 and4 for q=5.
    theta = math.atan2(4, 3)
    equal = mixed_operator(5, 5, theta, 0)
    check('equal intrinsic amplitudes permit3/4 fragmentation and total25',
          np.allclose(np.abs(equal[:, 0]), [3, 4])
          and math.isclose(float(np.sum(equal[:, 0] ** 2)), 25))
    result = {
        'kind': 'declared two-state amplitude counterexample and correction of old model claim',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'old_assumption_replay': {
            'qg': old_qg, 'qs': old_qs, 'theta_i_deg': 26.5, 'theta_f_deg': 0,
            'actual_selected_amplitude': float(actual), 'old_claimed_amplitude': 5.38,
            'residual_from_old_claim': float(actual - 5.38),
            'qs_unidentifiable_with_pure_final': True,
        },
        'one_center_inverse_not_a_fit': {
            'target_center': 5.38, 'tuned_theta_deg': math.degrees(inverse_theta),
            'tuned_probability': inverse_probability,
            'meaning': 'One freely chosen angle can reproduce one number; no independent mechanism test, original fit or confidence interval.'},
        'equal_intrinsic_example': {
            'declared_qg_qs': [5, 5], 'theta_i_deg': math.degrees(theta),
            'theta_f_deg': 0, 'daughter_amplitudes_abs': np.abs(equal[:, 0]).tolist(),
            'daughter_strengths_relative': (equal[:, 0] ** 2).tolist(),
            'same_parent_strength_sum': float(np.sum(equal[:, 0] ** 2)),
            'meaning': 'Mixing can redistribute strength at fixed intrinsic amplitudes under this complete declared operator.'},
        'checks': checks,
        'all_mathematical_controls_passed': all(c['passed'] for c in checks),
        'boundaries': [
            'Not a Babra or Klemme experimental fit, mixing-angle measurement or mechanism attribution',
            'Actual multipole operators may have nonzero off-diagonal entries and phases',
            'Strength sums require complete daughter states, the same initial state and normalization; missing branches break empirical closure',
            'Transition moments from different spins/bands cannot be treated as one intrinsic shape without their own geometry contract',
            'This establishes a counterexample to uniqueness; it does not prove which mechanism occurred in a nucleus'],
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'controls': len(checks), 'old_actual': actual,
                     'one_center_tuned_probability': inverse_probability,
                     'status': 'mathematical-controls-only'}))


if __name__ == '__main__':
    main()
