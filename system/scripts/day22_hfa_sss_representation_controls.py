#!/usr/bin/env python3
"""Conditional HFA algebra and finite-angle SSS normalization, not nuclear data."""
import argparse
import json
import math
from pathlib import Path

import numpy as np
from day22_frozen_alignment_domain import hfa_at_j

ROOT = Path(__file__).resolve().parents[2]


def calculate():
    # LAW20 Table I(vii), ordered as LAW axes (m,s,l).
    law_a, j = (.0078, .0089, .0385), 6.5
    f14_a = (law_a[2], law_a[0], law_a[1])
    rows = []
    for spin in np.arange(6.5, 43.0, 1.0):
        x = hfa_at_j(float(spin), j, f14_a)
        if not x['stable_yrast_expansion']:
            continue
        f1 = x['eq23_lhs_over_J']
        scaled = hfa_at_j(float(spin), j, tuple(v / (1 + .1 * spin) for v in f14_a))
        rows.append({'I_used_in_LAW_equations': float(spin), 'f1': f1,
                     'f2': f1 * 5 / 3, 'AMGM_floor_n1': 3 / float(spin),
                     'common_scale_f_difference': scaled['eq23_lhs_over_J'] - f1})
    minimum = min(rows, key=lambda r: r['f1'])
    # F24 Eqs.(26)-(27): a continuous, nonorthogonal finite-j phase basis.
    # This I is an arbitrary representation control, not a 163Lu state.
    spin = 5.5
    k = np.arange(-spin, spin + 1)
    dimension = len(k)
    phi = np.arange(4096) * 2 * np.pi / 4096
    phase = np.exp(-1j * k[:, None] * phi[None, :])
    uniform = np.ones(dimension) / math.sqrt(dimension)
    rho_local = np.outer(uniform, uniform)
    rho_diag = np.eye(dimension) / dimension
    def density(rho):
        return np.einsum('kp,kl,lp->p', phase, rho, phase.conj()) / (2 * np.pi)
    p_local, p_diag = density(rho_local), density(rho_diag)
    phi_zero = 2 * np.pi / dimension
    first_zero = abs(np.sum(np.exp(-1j * k * phi_zero))) ** 2 / (2 * np.pi * dimension)
    controls = {
        'positive_curvature_f_obeys_AMGM_bound': all(r['f1'] >= r['AMGM_floor_n1'] - 1e-12 for r in rows),
        'common_spin_scale_preserves_f': max(abs(r['common_scale_f_difference']) for r in rows) < 1e-12,
        'SSS_phase_density_unit_integral': abs(p_local.real.mean() * 2 * np.pi - 1) < 1e-12,
        'SSS_phase_density_nonnegative': p_local.real.min() >= -1e-12,
        'diagonal_density_uniform_phase': float(np.max(np.abs(p_diag.real - 1 / (2 * np.pi)))) < 1e-12,
        'uniform_superposition_first_zero': first_zero < 1e-24,
    }
    controls = {key: bool(value) for key, value in controls.items()}
    return {
        'scope': 'Source-parameter HFA reconstruction and arbitrary finite-basis representation controls only',
        'HFA': {
            'source': 'LAW20 034306-7 Eq.34; 034306-8 Table I(vii)',
            'A_LAW_axes123': law_a, 'j': j, 'reported_grid_max_I': 42.5,
            'notation': 'I is used literally as in LAW20, not F14 sqrt(I(I+1))',
            'minimum_on_restricted_grid': minimum,
            'analytic_bound': 'f(n,I)>=(2n+1)/I only for both local curvatures positive',
            'no_numerical_validity_threshold_assumed': True,
        },
        'SSS': {
            'source': 'F24 PDF p14 Eqs.26-27, finite-angle probability density',
            'arbitrary_control_I': spin, 'dimension': dimension,
            'integral': float(p_local.real.mean() * 2 * np.pi),
            'peak_at_zero': float(p_local[0].real),
            'peak_formula_D_over_2pi': dimension / (2 * np.pi),
            'first_zero_phi_radians': phi_zero,
            'kernel': 'sin(D*phi/2)^2 / (2*pi*D*sin(phi/2)^2), with its continuous limit at phi=0',
            'representation_not_measured_nuclear_squeezing': True,
        },
        'controls': controls,
        'boundaries': [
            'No full PTR/QTR eigenstates, physical transition operators or experimental likelihood were computed.',
            'A large HFA diagnostic challenges a specified harmonic approximation, not all topological wobbling definitions.',
            'SSS basis localization differs from Bogoliubov squeezing of a Hamiltonian eigenstate.',
            'No new data or independence is created by changing the representation of a given density matrix.',
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = (ROOT / args.output).resolve()
    if not out.is_relative_to(ROOT / 'outputs'):
        parser.error('output must be under outputs/')
    result = calculate()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'controls': result['controls'], 'HFA_minimum': result['HFA']['minimum_on_restricted_grid']}))
    return 0 if all(result['controls'].values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
