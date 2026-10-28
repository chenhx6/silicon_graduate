#!/usr/bin/env python3
"""Diagnose the nullspace in historical 015 with a dimensionless toy model.

No HFB states, EDF calculation, angular-momentum projection, production
SCCM kernel, or physical E1/E3 prediction is supplied by this calculation.
Coefficients use a discrete nonorthogonal basis; no extra quadrature factors
are inserted into f^dagger N f or f^dagger O f.
"""
import json
from pathlib import Path

import numpy as np


def solve(npoints, relative_cut, absolute_cut=False):
    x = np.linspace(-0.25, 0.25, npoints)
    diff = x[:, None] - x[None, :]
    sigma = 0.05
    norm = np.exp(-diff**2 / (2 * sigma**2))
    potential = 400 * x**4 - 800 * 0.11**2 * x**2
    potential -= potential.min()
    kinetic = -(diff**2 / sigma**4 - 1 / sigma**2) * norm / 100
    ham = (potential[:, None] + potential[None, :]) * norm / 2 + kinetic
    parity = np.eye(npoints)[::-1]
    states, records = {}, {}
    for name, sign in [('even', 1), ('odd', -1)]:
        n = (norm + sign * norm @ parity) / 2
        h = (ham + sign * ham @ parity) / 2
        n = (n + n.T) / 2
        h = (h + h.T) / 2
        values, vectors = np.linalg.eigh(n)
        threshold = relative_cut if absolute_cut else relative_cut * values.max()
        retained = values > threshold
        u = vectors[:, retained]
        b = u / np.sqrt(values[retained])
        # The eigenproblem has dimension rank(N), not the original grid size.
        reduced = b.T @ h @ b
        energies, coeff = np.linalg.eigh((reduced + reduced.T) / 2)
        f = b @ coeff[:, 0]
        # Historical 015 instead diagonalized a full-size matrix with null modes.
        invsqrt = b @ u.T
        full = invsqrt @ h @ invsqrt
        old_energies, old_vectors = np.linalg.eigh((full + full.T) / 2)
        old_f = invsqrt @ old_vectors[:, 0]
        f_norm = float(f @ n @ f)
        projected_residual = b.T @ (h @ f - energies[0] * n @ f)
        records[name] = {
            'retained_rank': int(retained.sum()),
            'grid_dimension': npoints,
            'natural_ground_energy_toy_units': float(energies[0]),
            'natural_state_norm_fNf': f_norm,
            'natural_parity_residual': float(np.linalg.norm(parity @ f - sign * f) / np.linalg.norm(f)),
            'natural_reduced_eigen_residual': float(np.linalg.norm(projected_residual)),
            'legacy_full_size_lowest_energy': float(old_energies[0]),
            'legacy_selected_state_norm_fNf': float(old_f @ n @ old_f),
            'legacy_full_size_near_zero_count': int(np.count_nonzero(abs(old_energies) < 1e-8)),
        }
        states[name] = f
    operator = (x[:, None] + x[None, :]) * norm / 2
    transition = float(states['odd'] @ operator @ states['even'])
    return {
        'grid_points': npoints, 'norm_cut': relative_cut,
        'cut_mode': 'absolute-legacy015' if absolute_cut else 'relative-to-max-eigenvalue',
        'parity_sectors': records,
        'odd_coordinate_transition_squared_toy_units': transition**2,
        'operator_parity_residual': float(np.linalg.norm(parity @ operator @ parity + operator)),
    }


def main():
    results = {
        'evidence_status': 'toy-numerical-diagnostic-not-SCCM-or-experiment',
        'method_source': 'Bernard2016 Eq3 natural basis and Eqs4-5; toy kernels explicitly invented in legacy015.',
        'normalization_contract': 'Discrete coefficients, f^dagger N f=1; all operators are full discrete kernels.',
        'legacy_input_diagnostic': solve(41, 1e-4, absolute_cut=True),
        'parameter_scan': [solve(n, cut) for n in (41, 61) for cut in (1e-8, 1e-6, 1e-4)],
        'limitation': 'No physical energy calibration, good-J projection, effective charges, or E1/E3 laboratory probabilities. Norm cutoff dependence retained.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(results, indent=2)+'\n')
    for row in results['parameter_scan']:
        print(row['grid_points'], row['norm_cut'], {
            name: (r['natural_ground_energy_toy_units'], r['natural_state_norm_fNf'], r['legacy_selected_state_norm_fNf'])
            for name, r in row['parity_sectors'].items()
        })


if __name__ == '__main__':
    main()
