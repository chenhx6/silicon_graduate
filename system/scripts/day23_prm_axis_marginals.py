"""Separate noncommuting spin-axis marginals for a fixed PRM variant; not geometry data."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import spin_matrices
from day23_unpaired_ph_prm import model, solve


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    hc = Path(cfg['source_H_contract'])
    assert sha(hc) == cfg['source_H_contract_sha256']
    assert sha(Path('system/scripts/day23_unpaired_ph_prm.py')) == cfg['implementation_H_sha256']
    source = json.loads(hc.read_text()); p = source['fixed_input']
    assert sha(Path(source['source_pdf'])) == source['source_sha256']
    gamma = math.radians(p['gamma_deg'])
    inertias = [p['J0_hbar2_per_MeV'] * math.sin(gamma - 2 * math.pi * k / 3) ** 2 for k in [1, 2, 3]]
    err = {'rho_Hermiticity': 0., 'rho_trace': 0., 'rho_PSD_defect': 0., 'probability_imaginary': 0.,
           'probability_negative_defect': 0., 'probability_sum': 0., 'm_reflection': 0., 'mean_m': 0.,
           'second_moment_hbar2': 0., 'axis3_direct_K': 0.}
    rows = []
    for spin in p['I']:
        m = model(spin, p['two_jp'], p['two_jn'], p['C_MeV'], gamma, inertias)
        energy, vectors = solve(m['H'], 45000 + spin, 1e-11, 64)
        axes = spin_matrices(2 * spin); axes[1] = -axes[1]
        eig = [np.linalg.eigh(op) for op in axes]
        states = []
        for ordinal in range(2):
            full = m['E'] @ vectors[:, ordinal]
            amp = full.reshape(2 * spin + 1, (p['two_jp'] + 1) * (p['two_jn'] + 1))
            rho = amp @ amp.T.conj()
            err['rho_Hermiticity'] = max(err['rho_Hermiticity'], float(np.max(abs(rho - rho.T.conj()))))
            err['rho_trace'] = max(err['rho_trace'], abs(float(np.trace(rho).real) - 1))
            err['rho_PSD_defect'] = max(err['rho_PSD_defect'], float(max(0, -min(np.linalg.eigvalsh(rho)))))
            probs = {}
            for axis, (values, basis) in enumerate(eig):
                diag = np.diag(basis.T.conj() @ rho @ basis)
                err['probability_imaginary'] = max(err['probability_imaginary'], float(max(abs(diag.imag))))
                pr = diag.real
                err['probability_negative_defect'] = max(err['probability_negative_defect'], float(max(0, -min(pr))))
                err['probability_sum'] = max(err['probability_sum'], abs(float(sum(pr)) - 1))
                err['m_reflection'] = max(err['m_reflection'], float(max(abs(pr - pr[::-1]))))
                err['mean_m'] = max(err['mean_m'], abs(float(np.dot(values, pr))))
                full_norm = float(np.linalg.norm(m['operators_full']['I'][axis] @ full) ** 2)
                err['second_moment_hbar2'] = max(err['second_moment_hbar2'], abs(float(np.dot(values ** 2, pr)) - full_norm))
                if axis == 2:
                    err['axis3_direct_K'] = max(err['axis3_direct_K'], float(max(abs(pr - np.diag(rho).real))))
                probs[str(axis + 1)] = {'m_values': values.tolist(), 'probabilities': pr.tolist(),
                                        'P_m_zero': float(pr[spin]),
                                        'peak_abs_m': float(abs(values[np.argmax(pr)])),
                                        'RMS_m': math.sqrt(max(0, float(np.dot(values ** 2, pr))))}
            states.append({'ordinal': ordinal, 'model_energy_MeV': float(energy[ordinal]), 'separate_axis_marginals': probs})
        distances = {}
        for axis in ['1', '2', '3']:
            pa = np.array(states[0]['separate_axis_marginals'][axis]['probabilities'])
            pb = np.array(states[1]['separate_axis_marginals'][axis]['probabilities'])
            assert min(pa) > -1e-12 and min(pb) > -1e-12
            distances[axis] = {'total_variation': float(sum(abs(pa - pb)) / 2),
                               'Bhattacharyya': float(sum(np.sqrt(np.maximum(pa, 0) * np.maximum(pb, 0))))}
        rows.append({'I': spin, 'D2_dimension': m['E'].shape[1],
                     'ordinal_gap_keV': float((energy[1] - energy[0]) * 1000), 'states': states,
                     'partner_axis_distances_descriptive_only': distances})
    controls = {'same_fixed_H_contract_and_code_hashes': True,
                'reduced_spin_density_Hermitian_trace1_PSD': max(err[k] for k in ['rho_Hermiticity', 'rho_trace', 'rho_PSD_defect']) < 1e-10,
                'separate_probabilities_real_nonnegative_normalized': max(err[k] for k in ['probability_imaginary', 'probability_negative_defect', 'probability_sum']) < 1e-10,
                'D2_axis_reflection_and_zero_first_moments': max(err['m_reflection'], err['mean_m']) < 1e-9,
                'second_moments_match_full_operator_norm': err['second_moment_hbar2'] < 1e-8,
                'axis3_spectral_projection_matches_direct_K_diagonal': err['axis3_direct_K'] < 1e-10,
                'descriptive_probability_distances_in_bounds': all(-1e-10 <= d['total_variation'] <= 1 + 1e-10 and -1e-10 <= d['Bhattacharyya'] <= 1 + 1e-10 for r in rows for d in r['partner_axis_distances_descriptive_only'].values())}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'only_uncredited_preview': 24, 'conditions': cfg,
           'contract_sha256': sha(a.contract), 'implementation_sha256': sha(Path(__file__)),
           'spin_rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()), 'errors': err,
           'limitations': ['Three spectral projection distributions are separate marginals of noncommuting operators, not a joint classical orientation distribution.',
                          'The fixed variant uses integer spins, so m=0 is a valid grid point here; no transfer to half-integer exact zero probability.',
                          'Near-equal marginals/RMS or a small ordinal energy gap do not prove relative phases, handedness or a tunneling mechanism.',
                          'These are model wavefunctions, not experimentally measured axes or actual author states.',
                          'No physical g/B/delta/Q/lifetime/CI, facilities rate or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'summary': [{'I': r['I'], 'gap_keV': r['ordinal_gap_keV'], 'distances': r['partner_axis_distances_descriptive_only'],
        'axis1_P0': [s['separate_axis_marginals']['1']['P_m_zero'] for s in r['states']]} for r in rows], 'errors': err}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
