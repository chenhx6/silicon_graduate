"""Two-pair Fock-space check of quasiparticle one-body factors and projection loss."""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np


def creation(mode, count=4):
    dim = 1 << count
    op = np.zeros((dim, dim))
    for n in range(dim):
        if not n & (1 << mode):
            op[n | (1 << mode), n] = (-1) ** ((n & ((1 << mode) - 1)).bit_count())
    return op


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    cd = [creation(i) for i in range(4)]
    annih = [v.T for v in cd]
    ident = np.eye(16)
    empty = np.eye(16)[:, 0]
    err = {'CAR': 0., 'T_square': 0., 'T_unitarity': 0., 'time_parities': 0., 'qp_CAR': 0.,
           'BCS_vacuum': 0., 'qp_basis': 0., 'odd_sector_complete': 0., 'projected_factors': 0.,
           'closure': 0., 'total_norm_one': 0., 'analytic_complement': 0.}
    for i, j in itertools.product(range(4), repeat=2):
        err['CAR'] = max(err['CAR'], float(np.max(abs(annih[i] @ cd[j] + cd[j] @ annih[i] - (ident if i == j else 0)))))
    transform = np.zeros((16, 16))
    mapped, signs = [1, 0, 3, 2], [1, -1, 1, -1]
    for n in range(16):
        state = empty.copy()
        occupied = [i for i in range(4) if n & (1 << i)]
        for i in reversed(occupied):
            state = signs[i] * cd[mapped[i]] @ state
        transform[:, n] = state
    parity = np.diag([(-1) ** n.bit_count() for n in range(16)])
    odd_projector = (ident - parity) / 2
    err['T_square'] = float(np.max(abs(transform @ transform.conj() - parity)))
    err['T_unitarity'] = float(np.max(abs(transform.T @ transform - ident)))
    unbar = cd[0] @ annih[2] + cd[2] @ annih[0]
    barred = cd[1] @ annih[3] + cd[3] @ annih[1]
    ops = {'odd': unbar - barred, 'even': unbar + barred}
    for name, op in ops.items():
        sign = -1 if name == 'odd' else 1
        err['time_parities'] = max(err['time_parities'], float(np.max(abs(transform @ op.conj() @ transform.T - sign * op))))
    rows = []
    designs = list(itertools.product([0., .2, .5, 1., math.pi / 2], repeat=2))
    for ta, tb in designs:
        ua, va, ub, vb = math.cos(ta), math.sin(ta), math.cos(tb), math.sin(tb)
        vacuum = (ua * ident + va * cd[0] @ cd[1]) @ (ub * ident + vb * cd[2] @ cd[3]) @ empty
        qd = [ua * cd[0] - va * annih[1], ua * cd[1] + va * annih[0],
              ub * cd[2] - vb * annih[3], ub * cd[3] + vb * annih[2]]
        for i, j in itertools.product(range(4), repeat=2):
            err['qp_CAR'] = max(err['qp_CAR'], float(np.max(abs(qd[i].T @ qd[j] + qd[j] @ qd[i].T - (ident if i == j else 0)))))
        err['BCS_vacuum'] = max(err['BCS_vacuum'], abs(float(np.dot(vacuum, vacuum)) - 1),
                                max(float(np.linalg.norm(op.T @ vacuum)) for op in qd))
        one = np.column_stack([op @ vacuum for op in qd])
        three = np.column_stack([qd[i] @ qd[j] @ qd[k] @ vacuum for i, j, k in itertools.combinations(range(4), 3)])
        full_odd = np.column_stack([one, three])
        err['qp_basis'] = max(err['qp_basis'], float(np.max(abs(full_odd.T @ full_odd - np.eye(8)))))
        err['odd_sector_complete'] = max(err['odd_sector_complete'], float(np.max(abs(full_odd @ full_odd.T - odd_projector))))
        factors = {'odd': ua * ub + va * vb, 'even': ua * ub - va * vb}
        complement = {'odd': ua * vb - va * ub, 'even': ua * vb + va * ub}
        values = {}
        for name, op in ops.items():
            qp_matrix = one.T @ op @ one
            err['projected_factors'] = max(err['projected_factors'], abs(float(qp_matrix[0, 2]) - factors[name]))
            state = op @ one[:, 0]
            total = float(np.dot(state, state))
            in_one = float(np.linalg.norm(one.T @ state) ** 2)
            in_three = float(np.linalg.norm(three.T @ state) ** 2)
            err['closure'] = max(err['closure'], abs(total - in_one - in_three))
            err['total_norm_one'] = max(err['total_norm_one'], abs(total - 1))
            err['analytic_complement'] = max(err['analytic_complement'], abs(in_one - factors[name] ** 2), abs(in_three - complement[name] ** 2),
                                              abs(factors[name] ** 2 + complement[name] ** 2 - 1))
            values[name] = {'one_qp_matrix_AB': float(qp_matrix[0, 2]),
                            'one_qp_projected_norm': in_one, 'three_qp_norm': in_three, 'full_odd_norm': total}
        if (ta, tb) in [(0., 0.), (0., math.pi / 2), (.2, 1.), (.5, .5)]:
            rows.append({'thetaA_design': ta, 'thetaB_design': tb, 'operators': values})
    controls = {'physical_fermion_CAR': err['CAR'] < 1e-12,
                'antiunitary_Tsquare_is_fermion_parity_and_U_unitary': max(err['T_square'], err['T_unitarity']) < 1e-12,
                'declared_onebody_time_parities': err['time_parities'] < 1e-12,
                'Bogoliubov_qp_CAR': err['qp_CAR'] < 1e-12,
                'normalized_BCS_vacuum_annihilated_by_qp': err['BCS_vacuum'] < 1e-12,
                'oneqp_threeqp_basis_orthonormal': err['qp_basis'] < 1e-12,
                'oneqp_plus_threeqp_complete_odd_Fock_sector': err['odd_sector_complete'] < 1e-12,
                'exact_oneqp_plus_and_minus_factors': err['projected_factors'] < 1e-12,
                'full_odd_norm_closure': max(err['closure'], err['total_norm_one']) < 1e-12,
                'analytic_pairchanging_complement': err['analytic_complement'] < 1e-12}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'only_uncredited_preview': 24, 'conditions': cfg,
           'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
           'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'design_count': len(designs), 'selected_design_rows': rows, 'controls': controls,
           'all_controls_pass': all(controls.values()), 'errors': err,
           'limitations': ['Declared four-mode algebra only; no nuclear Hamiltonian, physical M1/E2 operator or eigenstate is assigned.',
                          'A time-even single-particle operator has a minus factor in this gauge; this does not modify the source core E2 tensor.',
                          'Oneqp/threeqp norm closure is Fock-space bookkeeping, not a complete gamma branch or experimental width inventory.',
                          'T-square identity is a calibration of this fermion convention, not proof of chiral degeneracy or actual Kramers bands.',
                          'No physical g/B/delta/Q/lifetime/CI, facilities count rate or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'design_count': len(designs), 'rows': rows, 'errors': err}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
