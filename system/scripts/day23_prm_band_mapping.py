"""E2-only model family mapping; relative odd/even pairing remains separate input."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_unpaired_ph_prm import model, solve
from day23_prm_em_tensors import intrinsic, amplitude


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    cfg = json.loads(a.contract.read_text())
    assert all(sha(Path(p)) == h for p, h in cfg['code_hashes'].items())
    hc = Path(cfg['H_contract']); assert sha(hc) == cfg['H_contract_sha256']
    source = json.loads(hc.read_text()); p = source['fixed_input']
    assert sha(Path(source['source_pdf'])) == source['source_sha256']
    gamma = math.pi / 6; inertias = [30., 7.5, 7.5]
    states = {}; e2 = {}; m1 = {}; max_residual = 0.0
    for spin in cfg['spin_range']:
        m = model(spin, p['two_jp'], p['two_jn'], p['C_MeV'], gamma, inertias)
        en, vectors = solve(m['H'], 50000 + spin, 1e-11, 64)
        max_residual = max(max_residual, float(max(np.linalg.norm(m['H'] @ vectors - vectors * en, axis=0))))
        states[spin] = {'model': m, 'energies': en[:2], 'vectors': vectors[:, :2]}
        for kind, step, scale in [('E2', 2, 5 * 3.5 ** 2 / (16 * math.pi)), ('M1', 1, 3 / (4 * math.pi))]:
            ff = spin - step
            if ff not in states:
                continue
            rank, ops = intrinsic(p['two_jp'], p['two_jn'], kind, gamma, .7, -.6)
            aa, _ = amplitude(m, states[ff]['model'], spin, ff, rank, ops)
            low = states[ff]['vectors'].T.conj() @ (aa @ vectors[:, :2])
            photon_energy = en[None, :2] - states[ff]['energies'][:, None]
            record = {'Ii': spin, 'If': ff, 'formal_model_B_rows_final_columns_initial': abs(low) ** 2 * scale,
                      'Egamma_MeV_rows_final_columns_initial': photon_energy,
                      'open_mask': photon_energy > 0,
                      'open_model_B_rows_final_columns_initial': abs(low) ** 2 * scale * (photon_energy > 0)}
            (e2 if kind == 'E2' else m1)[spin] = record
    mapping = {12: [0, 1], 13: [0, 1]}
    decisions = []
    for spin in cfg['spin_range'][2:]:
        ff = spin - 2; b = e2[spin]['open_model_B_rows_final_columns_initial']; target = mapping[ff]
        scores = [sum(b[target[family], order[family]] for family in range(2)) for order in [[0, 1], [1, 0]]]
        chosen = [0, 1] if scores[0] >= scores[1] else [1, 0]
        mapping[spin] = chosen
        decisions.append({'I': spin, 'E2_open_inband_scores_identity_vs_swap': [float(s) for s in scores], 'chosen_family_to_energy_ordinal': chosen})
    flipped = {spin: order[::-1] if spin % 2 else order[:] for spin, order in mapping.items()}
    maps = {'pairingA': mapping, 'pairingB_odd_family_flip': flipped}
    max_e2_equal = max_norm = max_det = max_m1_exchange = 0.0
    rows = []
    for kind, transitions in [('E2', e2), ('M1', m1)]:
        for spin, record in transitions.items():
            ff = record['If']; raw = record['open_model_B_rows_final_columns_initial']; versions = {}
            for name, mp in maps.items():
                bb = raw[np.ix_(mp[ff], mp[spin])]
                versions[name] = {'model_B_family_rows_final_columns_initial': bb.tolist(),
                                  'inband_sum': float(np.trace(bb)), 'interband_sum': float(bb.sum() - np.trace(bb)),
                                  'family_energies_initial_MeV': states[spin]['energies'][mp[spin]].tolist(),
                                  'family_energies_final_MeV': states[ff]['energies'][mp[ff]].tolist()}
                max_norm = max(max_norm, abs(float(sum(bb.flat)) - float(sum(raw.flat))))
                max_det = max(max_det, abs(float(abs(np.linalg.det(bb))) - float(abs(np.linalg.det(raw)))))
            va, vb = versions.values()
            if kind == 'E2':
                max_e2_equal = max(max_e2_equal, abs(va['inband_sum'] - vb['inband_sum']))
            else:
                max_m1_exchange = max(max_m1_exchange, abs(va['inband_sum'] - vb['interband_sum']), abs(va['interband_sum'] - vb['inband_sum']))
            rows.append({'kind': kind, 'Ii': spin, 'If': ff, 'versions': versions,
                         'source_energy_ordinal_open_mask': record['open_mask'].tolist(),
                         'source_energy_ordinal_Egamma_MeV': record['Egamma_MeV_rows_final_columns_initial'].tolist(),
                         'note': 'Fixed model strengths only; family names and scoring do not create new physical data.'})
    controls = {'fixed_H_and_EM_hashes_and_scope': True,
                'eigenvectors_converged': max_residual < 1e-8,
                'each_family_map_is_a_permutation': all(sorted(v) == [0, 1] for mp in maps.values() for v in mp.values()),
                'E2_score_identical_under_relative_odd_chain_flip': max_e2_equal < 1e-12,
                'full_open_strength_sum_permutation_invariant': max_norm < 1e-12,
                'absolute_determinant_of_strength_matrix_permutation_invariant': max_det < 1e-12,
                'M1_in_out_sums_exchange_under_odd_flip': max_m1_exchange < 1e-12,
                'photon_masks_reported_not_assumed': True}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': cfg['scope'], 'formal_day_index': 23, 'only_uncredited_preview': 24, 'conditions': cfg,
           'contract_sha256': sha(a.contract), 'implementation_sha256': sha(Path(__file__)),
           'maps': maps, 'E2_only_decisions': decisions, 'rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()),
           'errors': {'eigen_residual_MeV': max_residual, 'E2_score_pairing_difference': max_e2_equal,
                      'total_strength_invariant': max_norm, 'absdet_strength_invariant': max_det, 'M1_in_out_exchange': max_m1_exchange},
           'limitations': ['Family mappings describe model-label association only, not actual configuration alternatives or experimental band identities.',
                          'E2 used to construct the map cannot then serve as an independent validation of that map.',
                          'Energy continuity, actual observed links or unused M1 information may constrain relative pairing, with their calibration role recorded.',
                          'No low-two-state projector completeness, actual nucleus, paired author producer or source Koike numerical reproduction.',
                          'No new physical g/delta/Q/lifetime/CI, facilities rate or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'maps': maps, 'E2_decisions': decisions,
                      'M1_summary': [{'I': r['Ii'], 'A_in': r['versions']['pairingA']['inband_sum'], 'A_out': r['versions']['pairingA']['interband_sum'],
                                      'B_in': r['versions']['pairingB_odd_family_flip']['inband_sum']} for r in rows if r['kind'] == 'M1'], 'errors': out['errors']}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
