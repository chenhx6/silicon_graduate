"""Fixed-operator inertia-only model ablation; no experiment or configuration fit."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import linear_sum_assignment

from day23_unpaired_ph_prm import model, solve
from day23_prm_em_tensors import intrinsic, amplitude
from day23_prm_exchange_symmetry import symmetry_action


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    assert all(sha(Path(p)) == h for p, h in cfg['frozen_code_hashes'].items())
    hc = Path(cfg['H_contract']); assert sha(hc) == cfg['H_contract_sha256']
    source = json.loads(hc.read_text()); p = source['fixed_input']
    assert sha(Path(source['source_pdf'])) == source['source_sha256']
    ii, ff = cfg['Ii'], cfg['If']; gamma = math.pi / 6
    rng = np.random.default_rng(48000); cache = {}; reference = {}
    max_eigen = max_symmetry_map = max_even_e = max_even_b = 0.0
    def get(spin, epsilon):
        key = (spin, epsilon)
        if key not in cache:
            inertias = [30., 7.5 * (1 + epsilon), 7.5 * (1 - epsilon)]
            m = model(spin, p['two_jp'], p['two_jn'], p['C_MeV'], gamma, inertias)
            vals, vectors = solve(m['H'], 48000 + spin + int(round(epsilon * 1e6)), 1e-11, 72)
            cache[key] = m, vals, vectors
        return cache[key]
    for spin in [ii, ff]:
        reference[spin] = get(spin, 0.)[2]
    rank, operator = intrinsic(p['two_jp'], p['two_jn'], 'E2', gamma)
    scale = 5 * 3.5 ** 2 / (16 * math.pi)
    rows = []
    for epsilon in cfg['epsilon']:
        current = {}
        for spin in [ii, ff]:
            m, vals, vectors = get(spin, epsilon)
            max_eigen = max(max_eigen, float(max(np.linalg.norm(m['H'] @ vectors - vectors * vals, axis=0))))
            overlaps = abs(reference[spin].T.conj() @ vectors) ** 2
            ri, ci = linear_sum_assignment(-overlaps)
            order = np.empty(6, int); order[ri] = ci
            ordered = vectors[:, order]; en = vals[order]
            state_labels = []
            for n in range(2):
                state = m['E'] @ ordered[:, n]
                state_labels.append(float(np.vdot(state, symmetry_action(state, spin, p['two_jp'])).real))
            partner = get(spin, -epsilon)[0]
            v = rng.normal(size=m['E'].shape[1]) + 1j * rng.normal(size=m['E'].shape[1]); v /= np.linalg.norm(v)
            full = m['E'] @ v
            left = (partner['Hcoll_full'] + partner['Hintr_full']) @ symmetry_action(full, spin, p['two_jp'])
            right = symmetry_action((m['Hcoll_full'] + m['Hintr_full']) @ full, spin, p['two_jp'])
            max_symmetry_map = max(max_symmetry_map, float(np.linalg.norm(left - right)))
            current[spin] = {'m': m, 'vectors': ordered, 'energies': en, 'order': order,
                             'retained_overlaps': overlaps[np.arange(6), order], 'S_expectations': state_labels}
        left, right = current[ff], current[ii]
        op, _ = amplitude(right['m'], left['m'], ii, ff, rank, operator)
        low = left['vectors'][:, :2].T.conj() @ (op @ right['vectors'][:, :2])
        strengths = abs(low) ** 2 * scale
        rows.append({'epsilon': epsilon, 'inertias': [30., 7.5 * (1 + epsilon), 7.5 * (1 - epsilon)],
                     'initial_matched_energies_MeV': right['energies'][:2].tolist(),
                     'final_matched_energies_MeV': left['energies'][:2].tolist(),
                     'initial_low6_matching_to_epsilon0_indices': right['order'].tolist(),
                     'final_low6_matching_to_epsilon0_indices': left['order'].tolist(),
                     'initial_retained_overlaps': right['retained_overlaps'][:2].tolist(),
                     'final_retained_overlaps': left['retained_overlaps'][:2].tolist(),
                     'initial_S_expectations_not_quantum_numbers_at_nonzero_eps': right['S_expectations'],
                     'final_S_expectations_not_quantum_numbers_at_nonzero_eps': left['S_expectations'],
                     'model_coreE2_B_e2b2_rows_final_columns_initial': strengths.tolist(),
                     'formerly_forbidden00_B_over_epsilon_squared': float(strengths[0, 0] / epsilon ** 2) if epsilon else None})
    by = {r['epsilon']: r for r in rows}
    for epsilon in [.001, .003, .01]:
        positive, negative = by[epsilon], by[-epsilon]
        for key in ['initial_matched_energies_MeV', 'final_matched_energies_MeV']:
            max_even_e = max(max_even_e, float(max(abs(np.array(positive[key]) - np.array(negative[key])))))
        max_even_b = max(max_even_b, float(np.max(abs(np.array(positive['model_coreE2_B_e2b2_rows_final_columns_initial']) - np.array(negative['model_coreE2_B_e2b2_rows_final_columns_initial'])))))
    q1, q3 = [by[e]['formerly_forbidden00_B_over_epsilon_squared'] for e in [.001, .003]]
    scaling = abs(q3 / q1 - 1) if abs(q1) > 1e-15 else None
    min_overlap = min(v for r in rows for key in ['initial_retained_overlaps', 'final_retained_overlaps'] for v in r[key])
    controls = {'frozen_H_operator_and_ablation_scope': True,
                'all_D2_Hermitian_basis_checks': all(max(m['basis_checks'].values()) < 1e-10 for m, vals, vectors in cache.values()),
                'low_eigenvectors_residual': max_eigen < 1e-8,
                'S_maps_epsilon_to_minus_epsilon_H': max_symmetry_map < 1e-9,
                'tracked_states_keep_large_reference_overlap': min_overlap > .9,
                'paired_epsilon_spectra_even': max_even_e < 1e-8,
                'paired_epsilon_strengths_even': max_even_b < 1e-8,
                'zero_epsilon_forbidden_channel_nearzero': by[0.]['model_coreE2_B_e2b2_rows_final_columns_initial'][0][0] < 1e-20,
                'nonzero_epsilon_forbidden_channel_activated': all(by[e]['model_coreE2_B_e2b2_rows_final_columns_initial'][0][0] > 1e-12 for e in [.001, .003, .01]),
                'small_epsilon_quadratic_strength_scaling': scaling is not None and scaling < .05}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'only_uncredited_preview': 24, 'conditions': cfg,
           'contract_sha256': sha(a.contract), 'implementation_sha256': sha(Path(__file__)),
           'rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()),
           'diagnostics': {'eigen_residual_MeV': max_eigen, 'S_parameter_mapping_error_MeV': max_symmetry_map,
                           'plus_minus_energy_difference_MeV': max_even_e, 'plus_minus_strength_difference_e2b2': max_even_b,
                           'minimum_retained_state_overlap': min_overlap, 'relative_B_over_eps2_change_0point001_to_0point003': scaling},
           'limitations': ['Changing J2/J3 breaks the source irrotational gamma30 equality and is explicitly a task ablation, not configuration-only assignment or an experimental parameter fit.',
                          'S is not an exact quantum number at nonzero epsilon; reference overlap labels are model-state tracking, not measured bands.',
                          'Opening a model channel does not establish actual nuclear transition strengths or experimental non-observation significance.',
                          'No delta, lifetime, physical fitted g/Q, covariance, confidence, facility rate or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'summary': [{'epsilon': r['epsilon'], 'B00': r['model_coreE2_B_e2b2_rows_final_columns_initial'][0][0],
        'B00_over_eps2': r['formerly_forbidden00_B_over_epsilon_squared']} for r in rows], 'diagnostics': out['diagnostics'], 'controls': controls}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
