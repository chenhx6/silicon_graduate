"""Pauli spin capacity of an explicit aligned subset; not a microscopic AMR fit."""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import spin_matrices


def pair(two_j):
    n = two_j + 1; j = two_j / 2
    labels = [(i, k) for i in range(n) for k in range(i + 1, n)]
    e = np.zeros((n * n, len(labels)))
    for col, (i, k) in enumerate(labels):
        e[i * n + k, col] = 1 / math.sqrt(2)
        e[k * n + i, col] = -1 / math.sqrt(2)
    single = spin_matrices(two_j)
    full = [np.kron(a, np.eye(n)) + np.kron(np.eye(n), a) for a in single]
    projected = [e.T @ a @ e for a in full]
    leakage = max(float(np.max(abs(a @ e - e @ b))) for a, b in zip(full, projected))
    casimir = sum(a @ a for a in projected)
    values = np.linalg.eigvalsh(casimir)
    implied = (np.sqrt(np.maximum(0, 1 + 4 * values)) - 1) / 2
    rounded = np.rint(implied).astype(int)
    counts = Counter(int(v) for v in rounded)
    comm = max(float(np.max(abs(projected[a] @ projected[b] - projected[b] @ projected[a] - 1j * projected[c])))
               for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 0, 1)])
    mzmax = float(max(np.linalg.eigvalsh(projected[2])))
    return {'two_j': two_j, 'dimension': len(labels), 'allowed_J_multiplicities_in_Jsquare_spectrum': dict(sorted(counts.items())),
            'maximum_Mz': mzmax, 'expected_Pauli_maximum_J': 2 * j - 1,
            'errors': {'embedding_orthogonality': float(np.max(abs(e.T @ e - np.eye(len(labels))))),
                       'vector_sector_leakage': leakage,
                       'projected_J_Hermiticity': max(float(np.max(abs(a - a.T.conj()))) for a in projected),
                       'commutator': comm, 'integer_J_from_Casimir': float(max(abs(implied - rounded))),
                       'Casimir_eigenvalue': float(max(abs(values - rounded * (rounded + 1))))}}


def coupled_values(two_a, two_b):
    return range(abs(two_a - two_b), two_a + two_b + 1, 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    pairs = [pair(p['two_j']) for p in cfg['pairs']]
    for row, expected in zip(pairs, cfg['pairs']):
        row['role'] = expected['role']
        assert row['dimension'] == expected['dimension']
        assert set(row['allowed_J_multiplicities_in_Jsquare_spectrum']) == set(expected['expected_J'])
    neutron = Counter()
    for jg in cfg['pairs'][1]['expected_J']:
        for jn in coupled_values(2 * jg, cfg['remaining_explicit_single_neutron_two_j']):
            neutron[jn] += 1
    total = Counter()
    for jp in cfg['pairs'][0]['expected_J']:
        for jn, multiplicity in neutron.items():
            for angular in coupled_values(2 * jp, jn):
                total[angular] += multiplicity
    dimension = sum((two_j + 1) * count for two_j, count in total.items())
    expected_dimension = pairs[0]['dimension'] * pairs[1]['dimension'] * (cfg['remaining_explicit_single_neutron_two_j'] + 1)
    maximum = max(total) / 2
    examples = [{'source': s, 'conditional_additional_angular_momentum_floor_hbar': max(0, s['two_I'] / 2 - maximum),
                 'meaning': 'necessary only if specified occupancy/spin and all remaining degrees J0 or explicit core partition are valid; not a measured core'}
                for s in cfg['target_spin_examples']]
    controls = {'wedge_dimensions_and_expected_even_J_set': True,
                'wedge_orthonormal_and_invariant_under_total_J': all(max(r['errors'][k] for k in ['embedding_orthogonality', 'vector_sector_leakage']) < 1e-12 for r in pairs),
                'closed_sector_J_Hermiticity_and_commutators': all(max(r['errors'][k] for k in ['projected_J_Hermiticity', 'commutator']) < 1e-12 for r in pairs),
                'Casimir_integer_J_and_eigenvalue': all(max(r['errors'][k] for k in ['integer_J_from_Casimir', 'Casimir_eigenvalue']) < 1e-10 for r in pairs),
                'each_pair_irrep_once_with_2Jplus1_states': all(all(v == 2 * j + 1 for j, v in r['allowed_J_multiplicities_in_Jsquare_spectrum'].items()) for r in pairs),
                'maximum_Mz_is_2j_minus1_not_2j': all(abs(r['maximum_Mz'] - r['expected_Pauli_maximum_J']) < 1e-12 for r in pairs),
                'two_pair_plus_single_coupling_dimension': dimension == expected_dimension == 15120,
                'explicit_neutron_maximum23half_total39half': max(neutron) == 23 and max(total) == 39}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'conditions': cfg,
           'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
           'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'pair_representations': pairs, 'neutron_total_twoJ_multiplicities': dict(sorted(neutron.items())),
           'explicit_valence_total_twoJ_multiplicities': dict(sorted(total.items())),
           'coupled_dimension': dimension, 'maximum_explicit_valence_J_hbar': maximum,
           'conditional_spin_examples': examples, 'controls': controls, 'all_controls_pass': all(controls.values()),
           'limitations': ['The angular capacity applies only to the explicitly named frozen subset; the full105Cd system contains other active nucleons.',
                          'A self-consistent model with neutron mixing/core-like response is not excluded by an inert-remainder conditional bound.',
                          'Additional angular momentum is not a uniquely defined or newly measured core rotor in a microscopic density.',
                          'The highest-source spins are tentative and no new spin or configuration is assigned.',
                          'No physical g/B/delta/Q/lifetime/CI, facility count rate or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'pairs': pairs,
                      'dimension': dimension, 'explicit_maximum_J': maximum, 'examples': examples}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
