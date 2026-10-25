"""Single-j spectrum and BCS M1 pairing-factor components, not a full PRM."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import spin_matrices


def bcs(energies, fermi, gap):
    energies = np.asarray(energies, float)
    if gap < 0:
        raise ValueError('Declared gap must be nonnegative')
    xi = energies - fermi
    qp = np.hypot(xi, gap)
    if np.any(qp == 0):
        raise ValueError('Exactly zero gap at the Fermi level requires a separate occupation/blocking convention')
    v2 = (1 - xi / qp) / 2
    u, v = np.sqrt(1 - v2), np.sqrt(v2)
    return qp, u, v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    c = json.loads(a.contract.read_text())
    assert hashlib.sha256(Path(c['source_pdf']).read_bytes()).hexdigest() == c['source_sha256']
    p = c['component_inputs']
    tj, coupling, fermi, gap = p['two_j'], p['C_MeV'], p['lambda_MeV'], p['Delta_MeV']
    j = tj / 2
    axes = spin_matrices(tj)
    plus = axes[0] + 1j * axes[1]
    minus = axes[0] - 1j * axes[1]
    rows = []
    errors = {'Hermiticity': 0., 'trace': 0., 'Kramers_split_MeV': 0., 'axial_analytic_MeV': 0.,
              'BCS_norm': 0., 'canonical_transform': 0., 'factor_diag': 0., 'factor_PSD_defect': 0., 'factor_rank_tail': 0.}
    casimir = float(np.max(abs(sum(op @ op for op in axes) - j * (j + 1) * np.eye(tj + 1))))
    for degrees in p['gamma_deg']:
        gamma = math.radians(degrees)
        h = p['Hsp_particle_sign'] * coupling / 2 * (math.cos(gamma) * (axes[2] @ axes[2] - j * (j + 1) / 3 * np.eye(tj + 1))
            + math.sin(gamma) / (2 * math.sqrt(3)) * (plus @ plus + minus @ minus))
        e, basis = np.linalg.eigh(h)
        errors['Hermiticity'] = max(errors['Hermiticity'], float(np.max(abs(h - h.T.conj()))))
        errors['trace'] = max(errors['trace'], abs(float(np.trace(h).real)))
        errors['Kramers_split_MeV'] = max(errors['Kramers_split_MeV'], float(max(abs(e[::2] - e[1::2]))))
        if degrees == 0:
            ml = np.arange(-tj, tj + 1, 2) / 2
            analytic = np.sort(coupling / 2 * (ml * ml - j * (j + 1) / 3))
            errors['axial_analytic_MeV'] = float(max(abs(e - analytic)))
        ep, u, v = bcs(e, fermi, gap)
        factor = np.outer(u, u) + np.outer(v, v)
        errors['BCS_norm'] = max(errors['BCS_norm'], float(max(abs(u * u + v * v - 1))))
        for ui, vi in zip(u, v):
            transform = np.array([[ui, -vi], [vi, ui]])
            errors['canonical_transform'] = max(errors['canonical_transform'], float(np.max(abs(transform @ transform.T - np.eye(2)))))
        values = np.linalg.eigvalsh(factor)
        errors['factor_diag'] = max(errors['factor_diag'], float(max(abs(np.diag(factor) - 1))))
        errors['factor_PSD_defect'] = max(errors['factor_PSD_defect'], float(max(0, -min(values))))
        errors['factor_rank_tail'] = max(errors['factor_rank_tail'], float(max(abs(values[:-2]))))
        support = np.zeros(factor.shape, bool)
        for op in axes:
            supported = abs(basis.T.conj() @ op @ basis) > 1e-8
            np.fill_diagonal(supported, False)
            support |= supported
        supported_factors = factor[support]
        rows.append({'gamma_deg': degrees, 'bare_single_particle_energies_MeV': e.tolist(),
                     'quasiparticle_energies_MeV': ep.tolist(), 'v_squared': (v * v).tolist(),
                     'Fplus_full_pair_range': [float(min(factor.flat)), float(max(factor.flat))],
                     'Fplus_on_nonzero_bare_j_offdiagonal_support': [float(min(supported_factors)), float(max(supported_factors))],
                     'factor_gram_eigenvalues': values.tolist(),
                     'minimum_qp_energy_MeV': float(min(ep))})
    analytic_factor_error = 0.
    for x, delta in [(1., 1.), (2., .5), (.2, 1.)]:
        _, u, v = bcs([-x, x], 0., delta)
        analytic_factor_error = max(analytic_factor_error, abs(float(u[0] * u[1] + v[0] * v[1]) - delta / math.hypot(x, delta)))
    _, u0, v0 = bcs([-2., -1., 1., 2.], 0., 0.)
    zero_factor = np.outer(u0, u0) + np.outer(v0, v0)
    expected = np.array([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]])
    guarded = False
    try:
        bcs([0.], 0., 0.)
    except ValueError:
        guarded = True
    controls = {'original_source_hash_checked': True,
                'bare_spin_Casimir_only': casimir < 1e-12,
                'bareH_Hermiticity_zero_trace_Kramers': max(errors[k] for k in ['Hermiticity', 'trace', 'Kramers_split_MeV']) < 1e-12,
                'axial_Hsp_analytic_energies': errors['axial_analytic_MeV'] < 1e-12,
                'BCS_norm_and_canonical_transform': max(errors['BCS_norm'], errors['canonical_transform']) < 1e-12,
                'quasiparticle_gap_lower_bound': all(r['minimum_qp_energy_MeV'] >= gap - 1e-12 for r in rows),
                'Fplus_Gram_PSD_unit_diagonal_rank_atmost2': max(errors['factor_diag'], errors['factor_PSD_defect'], errors['factor_rank_tail']) < 1e-12,
                'Fplus_nonnegative_and_atmost1_in_declared_gauge': all(r['Fplus_full_pair_range'][0] >= 0 and r['Fplus_full_pair_range'][1] <= 1 + 1e-12 for r in rows),
                'opposite_xi_analytic_pairing_factor': analytic_factor_error < 1e-12,
                'Delta0_occupation_class_factors': np.max(abs(zero_factor - expected)) < 1e-12,
                'zero_gap_exact_Fermi_guard': guarded,
                'pairing_factor_varies_on_nonzero_bare_j_support': any(r['Fplus_on_nonzero_bare_j_offdiagonal_support'][1] - r['Fplus_on_nonzero_bare_j_offdiagonal_support'][0] > .01 for r in rows)}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': c['scope'], 'formal_day_index': 23, 'only_uncredited_preview': 24,
           'conditions': c, 'contract_sha256': hashlib.sha256(a.contract.read_bytes()).hexdigest(),
           'implementation_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()), 'errors': errors,
           'additional_errors': {'bare_Casimir': casimir, 'symmetric_pair_formula': analytic_factor_error},
           'limitations': ['Only the source single-j Hsp and declared BCS factor are calculated; no rotor-coupled nuclear state, band mapping or full PRM.',
                          'Eigenbasis rotations within Kramers-degenerate subspaces are arbitrary; pair ranges on tiny elements are not nuclear transition predictions.',
                          'No commutator/Casimir requirement is imposed on a truncated one-quasiparticle operator without pair-changing sectors.',
                          'Source pure proton at zero gap has a separate occupation/configuration statement; the exact Fermi singularity is not filled arbitrarily.',
                          'No actual physical g, B(M1), B(E2), delta, lifetime, covariance, confidence, rates or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'rows_summary': [{k: r[k] for k in ['gamma_deg', 'Fplus_full_pair_range', 'Fplus_on_nonzero_bare_j_offdiagonal_support', 'minimum_qp_energy_MeV']} for r in rows], 'controls': controls, 'errors': errors}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
