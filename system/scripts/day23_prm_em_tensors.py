"""Source-specified core-E2/particle-M1 for the fixed unpaired PRM variant."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse

from day23_prm_basis_rotor import clebsch_gordan as cg, spin_matrices
from day23_multij_m1_operator import spherical
from day23_unpaired_ph_prm import model, solve, maximum


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def intrinsic(tjp, tjn, kind, gamma=0., gp=1., gn=0.):
    ip, inn = sparse.eye(tjp + 1, format='csr'), sparse.eye(tjn + 1, format='csr')
    dimension = (tjp + 1) * (tjn + 1)
    if kind == 'scalar':
        return 0, {0: sparse.eye(dimension, format='csr')}
    if kind == 'E2':
        return 2, {0: sparse.eye(dimension, format='csr') * math.cos(gamma),
                   -2: sparse.eye(dimension, format='csr') * math.sin(gamma) / math.sqrt(2),
                   2: sparse.eye(dimension, format='csr') * math.sin(gamma) / math.sqrt(2)}
    if kind == 'M1':
        ps, ns = spherical(spin_matrices(tjp)), spherical(spin_matrices(tjn))
        return 1, {q: gp * sparse.kron(sparse.csr_matrix(ps[q + 1]), inn, format='csr')
                   + gn * sparse.kron(ip, sparse.csr_matrix(ns[q + 1]), format='csr') for q in [-1, 0, 1]}
    raise ValueError(kind)


def amplitude(mi, mf, ii, ff, rank, tensors):
    full = sparse.csr_matrix((mf['E'].shape[0], mi['E'].shape[0]), dtype=complex)
    for q, intrinsic_op in tensors.items():
        rows, cols, values = [], [], []
        for ix, k in enumerate(range(-ii, ii + 1)):
            kp = k + q
            if -ff <= kp <= ff:
                val = cg(ii, k, rank, q, ff, kp)
                if val:
                    rows.append(kp + ff); cols.append(ix); values.append(val)
        rotation = sparse.csr_matrix((values, (rows, cols)), shape=(2 * ff + 1, 2 * ii + 1))
        full += sparse.kron(rotation, intrinsic_op, format='csr')
    a = (mf['E'].T @ full @ mi['E']).tocsr()
    leakage = maximum(full @ mi['E'] - mf['E'] @ a)
    return a, leakage


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    hc = Path(cfg['H_contract'])
    assert sha(hc) == cfg['H_contract_sha256']
    assert sha(Path('system/scripts/day23_unpaired_ph_prm.py')) == cfg['H_implementation_sha256']
    source = json.loads(hc.read_text()); p = source['fixed_input']
    assert sha(Path(source['source_pdf'])) == source['source_sha256']
    free = {i: model(i, 1, 1, 0., 0., [30., 30., 30.]) for i in range(4)}
    fv = {i: solve(m['H'], 1, 1e-12, 10)[1][:, 0] for i, m in free.items()}
    rank, op = intrinsic(1, 1, 'M1', gp=1., gn=0.)
    a10, leak = amplitude(free[1], free[0], 1, 0, rank, op)
    proton_transition = float(abs(np.vdot(fv[0], a10 @ fv[1])) ** 2)
    rank, total_j = intrinsic(1, 1, 'M1', gp=1., gn=1.)
    j10, _ = amplitude(free[1], free[0], 1, 0, rank, total_j)
    generator_transition = float(abs(np.vdot(fv[0], j10 @ fv[1])) ** 2)
    vector_closure = sum(float(np.linalg.norm(amplitude(free[1], free[ff], 1, ff, 1, op)[0] @ fv[1]) ** 2) for ff in [0, 1, 2])
    rank, q2 = intrinsic(1, 1, 'E2', gamma=math.pi / 6)
    core_closure = sum(float(np.linalg.norm(amplitude(free[1], free[ff], 1, ff, rank, q2)[0] @ fv[1]) ** 2) for ff in [1, 2, 3])
    rank, scalar = intrinsic(1, 1, 'scalar')
    scalar_a, _ = amplitude(free[1], free[1], 1, 1, rank, scalar)
    errors = {'free_proton_B': abs(proton_transition - .25), 'free_total_j_interI_B': generator_transition,
              'free_proton_closure': abs(vector_closure - .75), 'free_coreC2_closure': abs(core_closure - 1),
              'scalar_identity': maximum(scalar_a - sparse.eye(scalar_a.shape[0])),
              'D2_tensor_leakage': leak, 'Hermitian_reverse': 0., 'eigen_residual_MeV': 0.}
    assert max(errors.values()) < 1e-10
    gamma = math.radians(p['gamma_deg'])
    inertias = [p['J0_hbar2_per_MeV'] * math.sin(gamma - 2 * math.pi * k / 3) ** 2 for k in [1, 2, 3]]
    cache = {}
    def get(spin):
        if spin not in cache:
            m = model(spin, p['two_jp'], p['two_jn'], p['C_MeV'], gamma, inertias)
            energy, vectors = solve(m['H'], 46000 + spin, 1e-11, 64)
            errors['eigen_residual_MeV'] = max(errors['eigen_residual_MeV'], float(max(np.linalg.norm(m['H'] @ vectors - vectors * energy, axis=0))))
            cache[spin] = m, energy, vectors
        return cache[spin]
    rows = []
    for ii in cfg['target_initial_I']:
        mi, ei, vi = get(ii)
        for kind, step, scale in [('M1', 1, 3 / (4 * math.pi)), ('E2', 2, 5 * 3.5 ** 2 / (16 * math.pi))]:
            ff = ii - step
            mf, ef, vf = get(ff)
            rank, ops = intrinsic(p['two_jp'], p['two_jn'], kind, gamma, .7, -.6)
            aa, leakage = amplitude(mi, mf, ii, ff, rank, ops)
            reverse, reverse_leak = amplitude(mf, mi, ff, ii, rank, ops)
            reverse_expected = (-1) ** (ii - ff) * math.sqrt((2 * ii + 1) / (2 * ff + 1)) * aa.T.conj()
            errors['Hermitian_reverse'] = max(errors['Hermitian_reverse'], maximum(reverse - reverse_expected))
            errors['D2_tensor_leakage'] = max(errors['D2_tensor_leakage'], leakage, reverse_leak)
            low = vf[:, :2].T.conj() @ (aa @ vi[:, :2])
            strengths = abs(low) ** 2 * scale
            closure = np.array([np.linalg.norm(aa @ vi[:, n]) ** 2 * scale for n in range(2)])
            fractions = [float(sum(strengths[:, n]) / closure[n]) if closure[n] > 1e-15 else None for n in range(2)]
            rows.append({'kind': kind, 'Ii': ii, 'If': ff, 'model_B_unit': 'muN^2' if kind == 'M1' else 'e^2 b^2',
                         'source_adopted_scale_only': scale, 'matrix_rows_final_columns_initial_ordinal0_1': strengths.tolist(),
                         'all_final_states_at_fixed_If_total_strength': closure.tolist(),
                         'low_two_final_states_fraction_at_fixed_If': fractions,
                         'model_Egamma_MeV_rows_final_columns_initial': (ei[None, :2] - ef[:2, None]).tolist(),
                         'closure_scope': 'all formal final states at this If, not complete gamma outlets or an experimental width'})
    controls = {'same_fixed_sourceH_and_operator_scope': True,
                'scalar_rank0_identity': errors['scalar_identity'] < 1e-12,
                'free_R0_proton_triplet_singlet_B_quarter': errors['free_proton_B'] < 1e-12,
                'free_R0_total_particle_generator_interI_zero': errors['free_total_j_interI_B'] < 1e-12,
                'free_proton_complete_vector_closure_three_quarters': errors['free_proton_closure'] < 1e-12,
                'free_coreC2_complete_angular_closure_one': errors['free_coreC2_closure'] < 1e-12,
                'tensor_source_target_D2_mapping': errors['D2_tensor_leakage'] < 1e-10,
                'full_matrix_Hermitian_reverse_and_detailed_balance': errors['Hermitian_reverse'] < 1e-10,
                'eigenvectors_converged': errors['eigen_residual_MeV'] < 1e-8,
                'low_subset_fraction_between0and1': all(v is None or -1e-12 <= v <= 1 + 1e-12 for r in rows for v in r['low_two_final_states_fraction_at_fixed_If'])}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'only_uncredited_preview': 24, 'conditions': cfg,
           'contract_sha256': sha(a.contract), 'implementation_sha256': sha(Path(__file__)),
           'free_benchmarks': {'proton_B_triplet_to_singlet': proton_transition, 'total_j_B_interI': generator_transition,
                               'proton_vector_closure': vector_closure, 'coreC2_closure': core_closure},
           'rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()), 'errors': errors,
           'limitations': ['The only physical units come from source-adopted Q0/g model inputs, not measured strengths or new physical nuclear parameters.',
                          'No paired/multiquasiparticle author producer, experimental band mapping, particle E2 or detector response is reproduced.',
                          'Lowest ordinal labels are model eigenstates; no wobbling/chiral/signature assignment is certified.',
                          'Complete angular closure includes formal upward or same-spin states in benchmarks and is not a complete gamma exit inventory.',
                          'No delta, lifetime, covariance, confidence, facility count rate or beamtime calculated.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'free': out['free_benchmarks'], 'rows': rows, 'errors': errors}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
