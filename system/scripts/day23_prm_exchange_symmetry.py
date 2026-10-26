"""Extra unitary symmetry of a special unpaired p-hole PRM, not physical signature."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm

from day23_prm_basis_rotor import spin_matrices
from day23_unpaired_ph_prm import model, solve
from day23_prm_em_tensors import intrinsic, amplitude


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def symmetry_action(vector, spin, two_j):
    n = two_j + 1
    arr = np.asarray(vector).reshape(2 * spin + 1, n, n).swapaxes(1, 2)
    ui = expm(1j * math.pi / 2 * spin_matrices(2 * spin)[0])
    up = expm(-1j * math.pi / 2 * spin_matrices(two_j)[0])
    value = np.einsum('ak,kbc->abc', ui, arr)
    value = np.einsum('db,abc->adc', up, value)
    value = np.einsum('ec,adc->ade', up, value)
    return value.reshape(-1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    hc = Path(cfg['H_contract'])
    assert sha(hc) == cfg['H_contract_sha256']
    assert sha(Path('system/scripts/day23_unpaired_ph_prm.py')) == cfg['H_code_sha256']
    assert sha(Path('system/scripts/day23_prm_em_tensors.py')) == cfg['EM_code_sha256']
    source = json.loads(hc.read_text()); p = source['fixed_input']
    assert sha(Path(source['source_pdf'])) == source['source_sha256']
    assert p['two_jp'] == p['two_jn'] and p['gamma_deg'] == 30
    gamma = math.pi / 6
    inertias = [30., 7.5, 7.5]
    cache = {}; rng = np.random.default_rng(47000)
    errors = {'norm_unitarity': 0., 'D2_mapping': 0., 'S_square': 0., 'H_commutator_MeV': 0.,
              'low_state_S_eigenvalue': 0., 'low_state_S_residual': 0., 'tensor_covariance': 0., 'selection_forbidden_amplitude': 0.}
    def get(spin):
        if spin not in cache:
            m = model(spin, p['two_jp'], p['two_jn'], p['C_MeV'], gamma, inertias)
            energies, vectors = solve(m['H'], 47000 + spin, 1e-11, 64)
            full_h = m['Hcoll_full'] + m['Hintr_full']
            for _ in range(3):
                v = rng.normal(size=m['E'].shape[1]) + 1j * rng.normal(size=m['E'].shape[1]); v /= np.linalg.norm(v)
                state = m['E'] @ v
                sv = symmetry_action(state, spin, p['two_jp'])
                errors['norm_unitarity'] = max(errors['norm_unitarity'], abs(float(np.linalg.norm(sv)) - 1))
                errors['D2_mapping'] = max(errors['D2_mapping'], float(np.linalg.norm(sv - m['E'] @ (m['E'].T @ sv))))
                errors['S_square'] = max(errors['S_square'], float(np.linalg.norm(symmetry_action(sv, spin, p['two_jp']) - state)))
                errors['H_commutator_MeV'] = max(errors['H_commutator_MeV'], float(np.linalg.norm(full_h @ sv - symmetry_action(full_h @ state, spin, p['two_jp']))))
            signs = []
            for n in range(2):
                state = m['E'] @ vectors[:, n]
                ss = symmetry_action(state, spin, p['two_jp'])
                exp = np.vdot(state, ss)
                sign = 1 if exp.real >= 0 else -1
                errors['low_state_S_eigenvalue'] = max(errors['low_state_S_eigenvalue'], abs(complex(exp) - sign))
                errors['low_state_S_residual'] = max(errors['low_state_S_residual'], float(np.linalg.norm(ss - sign * state)))
                signs.append(sign)
            cache[spin] = m, energies, vectors, signs
        return cache[spin]
    rows = []
    for ii in p['I']:
        mi, ei, vi, si = get(ii)
        for kind, step, eta, gp, gn in [('E2', 2, -1, 0., 0.), ('M1_sum', 1, 1, 1., 1.), ('M1_diff', 1, -1, 1., -1.)]:
            ff = ii - step
            mf, ef, vf, sf = get(ff)
            rank, tensor = intrinsic(p['two_jp'], p['two_jn'], 'E2' if kind == 'E2' else 'M1', gamma, gp, gn)
            aa, _ = amplitude(mi, mf, ii, ff, rank, tensor)
            for _ in range(2):
                vector = rng.normal(size=mi['E'].shape[1]) + 1j * rng.normal(size=mi['E'].shape[1]); vector /= np.linalg.norm(vector)
                si_vector = mi['E'].T @ symmetry_action(mi['E'] @ vector, ii, p['two_jp'])
                lhs = mf['E'].T @ symmetry_action(mf['E'] @ (aa @ vector), ff, p['two_jp'])
                errors['tensor_covariance'] = max(errors['tensor_covariance'], float(np.linalg.norm(lhs - eta * aa @ si_vector)))
            low = vf[:, :2].T.conj() @ (aa @ vi[:, :2])
            for f in range(2):
                for i in range(2):
                    if sf[f] * si[i] != eta:
                        errors['selection_forbidden_amplitude'] = max(errors['selection_forbidden_amplitude'], float(abs(low[f, i])))
            rows.append({'kind': kind, 'Ii': ii, 'If': ff, 'tensor_S_parity': eta,
                         'initial_ordinal_S_labels': si, 'final_ordinal_S_labels': sf,
                         'normalized_angular_strength_rows_final_columns_initial': (abs(low) ** 2).tolist()})
    controls = {'frozen_H_and_EM_implementations': True,
                'special_S_unitary_and_D2_mapping': max(errors['norm_unitarity'], errors['D2_mapping']) < 1e-10,
                'Ssquare_one_in_physical_D2_sector': errors['S_square'] < 1e-10,
                'S_commutes_with_fixed_special_H': errors['H_commutator_MeV'] < 1e-9,
                'resolved_low_states_S_labels_plus_minus1': max(errors['low_state_S_eigenvalue'], errors['low_state_S_residual']) < 1e-7,
                'coreE2odd_M1sum_even_M1diff_odd_covariance': errors['tensor_covariance'] < 1e-9,
                'forbidden_entries_match_special_S_selection': errors['selection_forbidden_amplitude'] < 1e-8}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'only_uncredited_preview': 24, 'conditions': cfg,
           'contract_sha256': sha(a.contract), 'implementation_sha256': sha(Path(__file__)),
           'rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()), 'errors': errors,
           'limitations': ['S is a derived extra unitary exchange/rotation of this special equal-j unpaired Hamiltonian, not measured signature, pseudospin or the antiunitary chiral operation.',
                          'Ssquare1 labels sectors and does not require energy degeneracy.',
                          'Changing gamma, inertias, particle/hole spectra, pairing or model space can break these selection relations.',
                          'Source g coefficients split .05 times jp+jn and .65 times jp-jn; they are model inputs, not newly measured g factors.',
                          'No actual nuclear assignment, experimental forbidden line, delta/W.u. hard gate, covariance, confidence, rates or time.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'rows': rows, 'errors': errors}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
