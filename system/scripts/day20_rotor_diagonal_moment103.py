#!/usr/bin/env python3
"""Solve a declared I=2 D2-even rotor, not a model of an experimental nuclide.

H=sum A_i (I_i/hbar)^2, A in MeV; intrinsic electric tensor Q20=Q cos(gamma),
Q2,+/-2=Q sin(gamma)/sqrt(2), Q=1 eb. No law ties A_i to charge gamma here.
Only the two-state even-K/symmetric sector is used, exactly (no truncation in
that sector). Signed CG comes from the previously corrected factorial sum.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from day19_evidence_repair_audit import signed_cg


def operators():
    spin = 2
    ks = np.arange(-spin, spin+1)
    plus = np.zeros((5, 5))
    for index, k in enumerate(ks[:-1]):
        plus[index+1, index] = math.sqrt(spin*(spin+1)-k*(k+1))
    jx, jy, jz = (plus+plus.T)/2, (plus-plus.T)/(2j), np.diag(ks)
    sector = np.zeros((5, 2))
    sector[2, 0] = 1
    sector[0, 1] = sector[4, 1] = 1/math.sqrt(2)
    return ks, (jx, jy, jz), sector


def tensor(ks, gamma):
    intrinsic = {0: math.cos(gamma),
                 2: math.sin(gamma)/math.sqrt(2),
                 -2: math.sin(gamma)/math.sqrt(2)}
    stretch = signed_cg(2, 2, 2, 2, 0, 2)
    return np.array([[sum(stretch*signed_cg(2, 2, 2, int(kp), nu, int(k))*val
                         for nu, val in intrinsic.items()) for kp in ks] for k in ks])


def solve(coefficients, gamma_deg):
    ks, angular, sector = operators()
    gamma = math.radians(gamma_deg)
    hamiltonian = sum(a*(j@j) for a, j in zip(coefficients, angular))
    quadrupole = tensor(ks, gamma)
    small_h, small_q = sector.T@hamiltonian@sector, sector.T@quadrupole@sector
    energies, vectors = np.linalg.eigh(small_h)
    states = sector@vectors
    moments = np.diag(states.conj().T@quadrupole@states).real
    ax, ay, az = coefficients
    h0 = 2*(ax+ay+az)
    hz, hx = ax+ay-2*az, math.sqrt(3)*(ax-ay)
    gap = math.hypot(hz, hx)
    analytic_moment = 2/7*(math.cos(gamma)*hz-math.sin(gamma)*hx)/gap
    return {'A_MeV': list(coefficients), 'gamma_deg': gamma_deg,
            'energies_MeV': energies.tolist(), 'Qs_eb': moments.tolist(),
            'analytic_energies_MeV': [h0-gap, h0+gap],
            'analytic_ground_Qs_eb': analytic_moment,
            'eigen_residual': float(np.linalg.norm(hamiltonian@states-states@np.diag(energies))),
            'sector_H': small_h.real.tolist(), 'sector_Q': small_q.tolist()}, (hamiltonian, quadrupole, states, angular)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    checks = []

    def check(name, condition):
        checks.append({'name': name, 'passed': bool(condition)})
        if not condition:
            raise AssertionError(name)

    ks, (jx, jy, jz), sector = operators()
    check('angular algebra commutator', np.allclose(jx@jy-jy@jx, 1j*jz))
    check('fixed I=2 Casimir', np.allclose(jx@jx+jy@jy+jz@jz, 6*np.eye(5)))
    check('D2 basis orthonormal', np.allclose(sector.T@sector, np.eye(2)))
    cases = {}
    for label, coeff, gamma in [
        ('triaxial_charge_independent_inertias', (.02, .05, .09), 30),
        ('same_charge_special_Ay_equals_Az', (.02, .08, .08), 30),
        ('axial_charge_axial_inertia_limit', (.02, .02, .05), 0),
    ]:
        data, matrices = solve(coeff, gamma)
        h, q, states, angular = matrices
        check(label+' Hermitian operators', np.allclose(h, h.conj().T) and np.allclose(q, q.T))
        check(label+' exact-sector eigenstate residual', data['eigen_residual'] < 1e-13)
        check(label+' independent 2x2 analytic spectrum', np.allclose(data['energies_MeV'], data['analytic_energies_MeV']))
        check(label+' analytic diagonal moment', np.isclose(data['Qs_eb'][0], data['analytic_ground_Qs_eb']))
        scaled, _ = solve(tuple(3*a for a in coeff), gamma)
        check(label+' common inertia-energy scale leaves moments',
              np.allclose(scaled['Qs_eb'], data['Qs_eb'])
              and np.allclose(scaled['energies_MeV'], np.array(data['energies_MeV'])*3))
        # Passive unitary basis change: transform both operators and states.
        change = expm(-1j*.731*angular[1])
        rotated_states = change@states
        rotated_q = change@q@change.conj().T
        check(label+' simultaneous passive rotation leaves moment',
              np.allclose(np.diag(rotated_states.conj().T@rotated_q@rotated_states).real, data['Qs_eb']))
        cases[label] = data
    check('gamma30 zero cubic invariant but finite eigenstate Qs',
          abs(math.cos(math.pi/2)) < 1e-14
          and abs(cases['triaxial_charge_independent_inertias']['Qs_eb'][0]) > .1)
    check('special inertia symmetry restores gamma30 zero',
          abs(cases['same_charge_special_Ay_equals_Az']['Qs_eb'][0]) < 1e-13)
    check('axial ground K0 reproduces -2/7 moment',
          np.isclose(cases['axial_charge_axial_inertia_limit']['Qs_eb'][0], -2/7))
    result = {'checkpoint': '103', 'kind': 'declared solvable rotor counterexample',
              'experimental_fit': False, 'actual_Ce_wavefunction': False,
              'controls': checks, 'all_controls_passed': all(c['passed'] for c in checks),
              'cases': cases,
              'analytic_condition': 'In this I=2 D2 sector, nondegenerate gamma=30 eigenstates have Qs=0 iff Ay=Az; charge gamma alone does not imply that inertia symmetry.',
              'boundaries': ['Q=1eb and three A_i are chosen independently; no actual nuclear data used.',
                             'No irrotational-inertia law is imposed or tested as an empirical law.',
                             'This counterexample rejects a universal operator statement; it does not reject a specified Davydov-Filippov solution.',
                             'No dynamic gamma-soft potential, odd-particle coupling, magnetic observable or CI modeled.'],
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'CG_helper_sha256': hashlib.sha256(Path(__file__).with_name('day19_evidence_repair_audit.py').read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'controls': len(checks), 'cases': {k:v['Qs_eb'] for k,v in cases.items()}}))


if __name__ == '__main__':
    main()
