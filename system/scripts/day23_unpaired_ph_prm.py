"""Finite-I unpaired proton-hole PRM variant with exact D2 embedding and checks."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

from day23_prm_basis_rotor import spin_matrices


def maximum(matrix):
    return float(max(abs(matrix.data))) if matrix.nnz else 0.0


def embedding(spin, tjp, tjn):
    ni, npart, nneut = 2 * spin + 1, tjp + 1, tjn + 1
    phase = (-1) ** (spin - (tjp + tjn) // 2)
    rows, cols, vals, labels = [], [], [], []
    for ki, k in enumerate(range(-spin, spin + 1)):
        for pi, tp in enumerate(range(-tjp, tjp + 1, 2)):
            for nn, tn in enumerate(range(-tjn, tjn + 1, 2)):
                if (2 * k - tp - tn) % 4:
                    continue
                if k < 0 or k == 0 and tp < 0:
                    continue
                col = len(labels)
                labels.append((k, tp / 2, tn / 2))
                forward = (ki * npart + pi) * nneut + nn
                backward = ((ni - 1 - ki) * npart + npart - 1 - pi) * nneut + nneut - 1 - nn
                rows.extend([forward, backward]); cols.extend([col, col]); vals.extend([1 / math.sqrt(2), phase / math.sqrt(2)])
    expected = ni * npart * nneut // 4
    assert len(labels) == expected
    return sparse.csr_matrix((vals, (rows, cols)), shape=(ni * npart * nneut, expected)), labels


def hsp(tj, coupling, gamma):
    axes = spin_matrices(tj)
    j = tj / 2
    plus, minus = axes[0] + 1j * axes[1], axes[0] - 1j * axes[1]
    return coupling / 2 * (math.cos(gamma) * (axes[2] @ axes[2] - j * (j + 1) / 3 * np.eye(tj + 1))
        + math.sin(gamma) / (2 * math.sqrt(3)) * (plus @ plus + minus @ minus))


def model(spin, tjp, tjn, coupling, gamma, inertias):
    assert isinstance(spin, int) and spin >= 0 and tjp % 2 == 1 and tjn % 2 == 1
    assert min(inertias) > 0
    e, labels = embedding(spin, tjp, tjn)
    ei, ep, en = [sparse.eye(n, format='csr') for n in [2 * spin + 1, tjp + 1, tjn + 1]]
    ia = spin_matrices(2 * spin); ia[1] = -ia[1]
    pa, na = spin_matrices(tjp), spin_matrices(tjn)
    iops = [sparse.kron(sparse.csr_matrix(op), sparse.kron(ep, en), format='csr') for op in ia]
    pops = [sparse.kron(ei, sparse.kron(sparse.csr_matrix(op), en), format='csr') for op in pa]
    nops = [sparse.kron(ei, sparse.kron(ep, sparse.csr_matrix(op)), format='csr') for op in na]
    rops = [i - p - n for i, p, n in zip(iops, pops, nops)]
    hcoll = sum((r @ r) / (2 * moment) for r, moment in zip(rops, inertias))
    hp, hn = hsp(tjp, coupling, gamma), -hsp(tjn, coupling, gamma)
    hintr = sparse.kron(ei, sparse.kron(sparse.csr_matrix(hp), en) + sparse.kron(ep, sparse.csr_matrix(hn)), format='csr')
    full = hcoll + hintr
    projected = (e.T @ full @ e).tocsr()
    checks = {'embedding_orthogonality': maximum(e.T @ e - sparse.eye(e.shape[1])),
              'H_Hermiticity': maximum(projected - projected.T.conj()),
              'D2_sector_leakage_MeV': maximum(full @ e - e @ projected),
              'H_imaginary_part': maximum(sparse.csr_matrix(projected.imag))}
    assert max(checks.values()) < 1e-10
    return {'E': e, 'H': projected.real.tocsr(), 'Hcoll_full': hcoll, 'Hintr_full': hintr,
            'operators_full': {'I': iops, 'jp': pops, 'jn': nops, 'R': rops},
            'basis_checks': checks, 'basis_labels': labels}


def solve(h, seed, tolerance, ncv):
    if h.shape[0] <= 48:
        e, v = np.linalg.eigh(h.toarray())
        return e, v
    v0 = np.random.default_rng(seed).normal(size=h.shape[0])
    e, v = eigsh(h, k=6, which='SA', tol=tolerance, v0=v0, ncv=min(ncv, h.shape[0]))
    ix = np.argsort(e)
    return e[ix], v[:, ix]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    assert hashlib.sha256(Path(cfg['source_pdf']).read_bytes()).hexdigest() == cfg['source_sha256']
    limits = []
    max_free = 0.0
    for case in cfg['free_limits']:
        m = model(case['I'], case['two_jp'], case['two_jn'], 0., 0., case['inertias'])
        vals, _ = np.linalg.eigh(m['H'].toarray())
        error = float(max(abs(vals - np.array(case['expected_spectrum_MeV']))))
        max_free = max(max_free, error)
        limits.append({'case': case, 'calculated_MeV': vals.tolist(), 'max_error_MeV': error, 'basis_checks': m['basis_checks']})
    assert max_free < 1e-10
    p = cfg['fixed_input']
    gamma = math.radians(p['gamma_deg'])
    inertias = [p['J0_hbar2_per_MeV'] * math.sin(gamma - 2 * math.pi * k / 3) ** 2 for k in [1, 2, 3]]
    rows = []
    max_residual = max_orth = max_repeat = max_casimir = max_energy = 0.0
    for spin in p['I']:
        m = model(spin, p['two_jp'], p['two_jn'], p['C_MeV'], gamma, inertias)
        vals, vectors = solve(m['H'], 44000 + spin, 1e-11, 48)
        repeat, _ = solve(m['H'], 54000 + spin, 3e-12, 72)
        residual = float(max(np.linalg.norm(m['H'] @ vectors - vectors * vals, axis=0)))
        orth = float(np.max(abs(vectors.T @ vectors - np.eye(len(vals)))))
        repeated = float(max(abs(vals - repeat)))
        max_residual = max(max_residual, residual); max_orth = max(max_orth, orth); max_repeat = max(max_repeat, repeated)
        states = []
        for n in range(2):
            state = m['E'] @ vectors[:, n]
            msq = {name: [float(np.linalg.norm(op @ state) ** 2) for op in ops] for name, ops in m['operators_full'].items()}
            for name, jvalue in [('I', spin), ('jp', p['two_jp'] / 2), ('jn', p['two_jn'] / 2)]:
                max_casimir = max(max_casimir, abs(sum(msq[name]) - jvalue * (jvalue + 1)))
            coll = sum(value / (2 * moment) for value, moment in zip(msq['R'], inertias))
            intrinsic = float(np.vdot(state, m['Hintr_full'] @ state).real)
            max_energy = max(max_energy, abs(coll + intrinsic - vals[n]))
            states.append({'ordinal': n, 'model_energy_MeV': float(vals[n]),
                           'RMS_components_hbar': {key: [math.sqrt(v) for v in values] for key, values in msq.items()},
                           'Hcoll_MeV': coll, 'Hintr_MeV': intrinsic})
        rows.append({'I': spin, 'full_product_dimension': m['E'].shape[0], 'D2_dimension': m['E'].shape[1],
                     'basis_checks': m['basis_checks'], 'lowest_model_energies_MeV': vals.tolist(),
                     'ordinal0_1_gap_keV': float((vals[1] - vals[0]) * 1000),
                     'eigen_residual_MeV': residual, 'orthogonality_error': orth,
                     'different_seed_tolerance_ncv_max_shift_MeV': repeated, 'states': states})
        print(json.dumps({'I': spin, 'dimension': m['E'].shape[1], 'gap_keV': rows[-1]['ordinal0_1_gap_keV'], 'residual_MeV': residual}), flush=True)
    controls = {'source_hash_and_fixed_unpaired_scope': True,
                'D2_dimension_orthogonal_and_H_invariant': all(max(r['basis_checks'].values()) < 1e-10 for r in rows),
                'two_free_rotor_spectra_analytic': max_free < 1e-10,
                'low_eigenvectors_residual': max_residual < 1e-8,
                'low_eigenvectors_orthonormal': max_orth < 1e-9,
                'different_seed_tolerance_ncv_low_spectrum_stable': max_repeat < 1e-8,
                'full_operator_squared_norm_Casimirs': max_casimir < 1e-8,
                'Hcoll_plus_Hintr_reconstructs_energy': max_energy < 1e-8}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'only_uncredited_preview': 24,
           'conditions': cfg, 'inertias_hbar2_per_MeV': inertias,
           'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
           'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'free_limits': limits, 'spin_rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()),
           'max_errors': {'free_MeV': max_free, 'eigen_residual_MeV': max_residual, 'orthogonality': max_orth,
                          'repeat_spectrum_MeV': max_repeat, 'Casimir_hbar2': max_casimir, 'energy_reconstruction_MeV': max_energy},
           'limitations': ['Explicit unpaired source-H variant only; not the source Delta1 curves, actual author code or a fit to Pr/Au/Nd data.',
                          'Model energy offset is arbitrary; no experimental level or nuclear band mapping is assigned.',
                          'RMS components lose signs and do not prove handedness or static chirality.',
                          'No actual electromagnetic strength, delta, g/Q, lifetime, covariance, confidence or facilities rate/time calculated.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'max_errors': out['max_errors']}), flush=True)
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
