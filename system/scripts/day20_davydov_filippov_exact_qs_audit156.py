#!/usr/bin/env python3
"""Exact first-principles derivation and audit of Davydov-Filippov triaxial rotor observables.

Derives and audits:
1. 2x2 collective Hamiltonian diagonalization for I=2 under hydrodynamical moments of inertia;
2. Exact algebraic formula for spectroscopic quadrupole moment Qs(2_1^+):
   Qs(2_1^+) = -(2/7) Q0 * (3 cos 3gamma) / sqrt(9 - 8 sin^2 3gamma);
3. Axial prolate limit at gamma -> 0 (Qs = -2/7 Q0);
4. Triaxial zero-crossing at gamma = 30 deg (Qs = 0);
5. Axial oblate limit at gamma -> 60 deg (Qs = +2/7 Q0);
6. Energy ratio E(2_2^+)/E(2_1^+) = 2.000 at gamma = 30 deg;
7. B(E2; 2_2^+ -> 2_1^+) / B(E2; 2_1^+ -> 0_1^+) = 10/7 at gamma = 30 deg;
8. Strict vanishing of B(E2; 2_2^+ -> 0_1^+) = 0 at gamma = 30 deg.

Requires --output PATH. Uses only Python standard library.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import math
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='Output JSON path')
    args = parser.parse_args()

    checks = []
    def check(name, ok, details=''):
        checks.append({'name': name, 'passed': bool(ok), 'details': str(details)})
        if not ok:
            raise AssertionError(f'Check failed: {name}: {details}')

    # Test grid of angles
    angles_deg = [0.0, 1.0, 5.0, 10.0, 15.0, 20.0, 25.0, 28.0, 29.0, 30.0, 35.0, 40.0, 45.0, 50.0, 55.0, 59.0, 60.0]
    grid_results = []
    max_diff_qs = 0.0

    for deg in angles_deg:
        g = math.radians(deg)
        s3 = math.sin(3 * g)
        c3 = math.cos(3 * g)
        disc = math.sqrt(9.0 - 8.0 * s3**2)

        # Analytic closed forms
        analytic_qs_ratio = (3.0 * c3) / disc
        analytic_qs_over_q0 = (-2.0 / 7.0) * analytic_qs_ratio
        analytic_be2_21_01 = 0.5 * (1.0 + (3.0 - 2.0 * s3**2) / disc)
        analytic_be2_22_01 = 0.5 * (1.0 - (3.0 - 2.0 * s3**2) / disc)
        analytic_be2_22_21 = (10.0 / 7.0) * (s3**2) / (disc**2)
        analytic_e_ratio = (3.0 + disc) / (3.0 - disc) if disc < 3.0 else float('inf')

        # Numerical diagonalization of 2x2 Hamiltonian
        # eps avoids division by zero at gamma=0 and gamma=60
        eps = 1e-12 if (deg in (0.0, 60.0)) else 0.0
        g_num = g + eps
        j1 = math.sin(g_num - 2*math.pi/3)**2
        j2 = math.sin(g_num + 2*math.pi/3)**2
        j3 = math.sin(g_num)**2
        ax = 1.0 / (2.0 * j1)
        ay = 1.0 / (2.0 * j2)
        az = 1.0 / (2.0 * j3)

        h00 = 3.0 * (ax + ay)
        h11 = ax + ay + 4.0 * az
        h01 = math.sqrt(3.0) * (ax - ay)

        # Robust analytic eigenvector for smaller eigenvalue (h00 < h11)
        theta = 0.5 * math.atan2(2.0 * h01, h00 - h11)
        phi = theta + math.pi / 2.0
        c0 = math.cos(phi)
        c2 = math.sin(phi)

        diag_qs_over_q0 = (2.0 / 7.0) * (-math.cos(g) * c0**2 + 2.0 * math.sin(g) * c0 * c2 + math.cos(g) * c2**2)
        diff_qs = abs(diag_qs_over_q0 - analytic_qs_over_q0)
        if diff_qs > max_diff_qs:
            max_diff_qs = diff_qs

        grid_results.append({
            'gamma_deg': deg,
            'analytic_qs_over_q0': analytic_qs_over_q0,
            'diag_qs_over_q0': diag_qs_over_q0,
            'diff_qs': diff_qs,
            'e_ratio': analytic_e_ratio,
            'be2_21_01': analytic_be2_21_01,
            'be2_22_01': analytic_be2_22_01,
            'be2_22_21': analytic_be2_22_21
        })

    # 1. Analytic formula matches diagonalization across all angles to machine precision
    check('Analytic Qs formula matches 2x2 Hamiltonian diagonalization within 1e-13 across all angles',
          max_diff_qs < 1e-13, f'Max diff: {max_diff_qs:.2e}')

    # 2. Axial prolate limit at gamma = 0
    res_0 = grid_results[0]
    check('Axial prolate limit gamma=0 gives exact Qs = -2/7 Q0',
          abs(res_0['analytic_qs_over_q0'] - (-2.0 / 7.0)) < 1e-15)

    # 3. Triaxial zero-crossing at gamma = 30
    res_30 = next(r for r in grid_results if r['gamma_deg'] == 30.0)
    check('Maximal triaxiality gamma=30 deg gives exact Qs = 0.0',
          abs(res_30['analytic_qs_over_q0']) < 1e-15)

    # 4. Axial oblate limit at gamma = 60
    res_60 = grid_results[-1]
    check('Axial oblate limit gamma=60 deg gives exact Qs = +2/7 Q0',
          abs(res_60['analytic_qs_over_q0'] - (2.0 / 7.0)) < 1e-15)

    # 5. Energy ratio E(2_2)/E(2_1) = 2.000 at gamma = 30
    check('Energy ratio E(2_2)/E(2_1) = 2.00000 at gamma=30 deg',
          abs(res_30['e_ratio'] - 2.0) < 1e-15)

    # 6. B(E2; 2_2 -> 2_1) / B(E2; 2_1 -> 0_1) = 10/7 at gamma = 30
    check('B(E2; 2_2 -> 2_1) / B_axial = 10/7 at gamma=30 deg',
          abs(res_30['be2_22_21'] - 10.0 / 7.0) < 1e-15)

    # 7. Vanishing B(E2; 2_2 -> 0_1) = 0 at gamma = 30
    check('B(E2; 2_2 -> 0_1) = 0.0 strictly at gamma=30 deg',
          abs(res_30['be2_22_01']) < 1e-15)

    result = {
        'observed_at_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Davydov-Filippov 1958 rigid triaxial rotor first-principles audit and exact closed forms',
        'formalism': {
            'hamiltonian': 'H = sum_k I_k^2 / (2 J_k) with J_k = 4 B beta^2 sin^2(gamma - 2pi/3 * k)',
            'exact_qs_formula': 'Qs(2_1^+) = -(2/7) Q0 * (3 cos 3gamma) / sqrt(9 - 8 sin^2 3gamma)',
            'exact_be2_21_01': 'B(E2; 2_1 -> 0_1) / B_axial = 0.5 * (1 + (3 - 2 sin^2 3gamma) / sqrt(9 - 8 sin^2 3gamma))',
            'exact_be2_22_01': 'B(E2; 2_2 -> 0_1) / B_axial = 0.5 * (1 - (3 - 2 sin^2 3gamma) / sqrt(9 - 8 sin^2 3gamma))',
            'exact_be2_22_21': 'B(E2; 2_2 -> 2_1) / B_axial = (10/7) * sin^2 3gamma / (9 - 8 sin^2 3gamma)',
            'exact_e_ratio': 'E(2_2^+) / E(2_1^+) = (3 + sqrt(9 - 8 sin^2 3gamma)) / (3 - sqrt(9 - 8 sin^2 3gamma))'
        },
        'key_points': {
            'gamma_0_prolate': {'Qs_over_Q0': -2.0/7.0, 'E2_over_E1': float('inf'), 'be2_21': 1.0, 'be2_22': 0.0},
            'gamma_30_triaxial': {'Qs_over_Q0': 0.0, 'E2_over_E1': 2.0, 'be2_21': 1.0, 'be2_22_21': 10.0/7.0, 'be2_22_01': 0.0},
            'gamma_60_oblate': {'Qs_over_Q0': 2.0/7.0, 'E2_over_E1': float('inf'), 'be2_21': 1.0, 'be2_22': 0.0}
        },
        'grid_results': grid_results,
        'checks': checks,
        'all_checks_passed': all(c['passed'] for c in checks),
        'boundary': 'Rigid triaxial rotor with hydrodynamical moments of inertia; does not include gamma-softness fluctuations or microscopic quasiparticle degrees of freedom.'
    }

    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f'All {len(checks)} checks passed: {result["all_checks_passed"]}')

if __name__ == '__main__':
    main()
