#!/usr/bin/env python3
"""Audit the written angle potential; withdraw unsupported isotope TAC predictions."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np


ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01'
ARCHIVE = RUN / 'scientific-corrections-047/superseded-chiral-artifacts.json'
LIU_SOURCE = ROOT / 'knowledge/sources/liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br.md'


def finite_coefficients(*values):
    if not all(math.isfinite(x) for x in values):
        raise ValueError('potential coefficients must be finite')


def written_potential(phi, a, b):
    """Literal old note: -A*cos(2phi)/2 + B*cos(phi)**2. Radians; MeV."""
    return -0.5 * a * np.cos(2 * phi) + b * np.cos(phi) ** 2


def written_gradient(phi, a, b):
    return (a - b) * np.sin(2 * phi)


def written_curvature(phi, a, b):
    return 2 * (a - b) * np.cos(2 * phi)


def written_minimum(a, b):
    finite_coefficients(a, b)
    # Equality here is algebraic, not a fitted physical critical tolerance.
    if a == b:
        return {'kind': 'flat', 'angles_deg': None, 'energy_MeV': b / 2,
                'energy_span_MeV': 0.0, 'isotope_shape': None}
    angle = 0.0 if a > b else math.pi / 2
    return {'kind': 'endpoint', 'angles_deg': [math.degrees(angle)],
            'energy_MeV': float(written_potential(angle, a, b)),
            'energy_span_MeV': abs(b - a), 'isotope_shape': None}


def different_potential(phi, a, b):
    """A distinct synthetic even-angle potential; not the old note's potential."""
    x = np.cos(2 * phi)
    return a * x ** 2 - b * x


def different_gradient(phi, a, b):
    return 2 * np.sin(2 * phi) * (b - 2 * a * np.cos(2 * phi))


def different_curvature(phi, a, b):
    return 4 * np.cos(2 * phi) * (b - 2 * a * np.cos(2 * phi)) + 8 * a * np.sin(2 * phi) ** 2


def different_minimum(a, b):
    finite_coefficients(a, b)
    if a <= 0:
        raise ValueError('this synthetic quadratic-in-cosine demonstration requires a > 0')
    r = b / (2 * a)
    if -1 < r < 1:
        theta = 0.5 * math.acos(r)
        return {'kind': 'paired-interior', 'angles_deg': [-math.degrees(theta), math.degrees(theta)],
                'energy_MeV': -(b ** 2) / (4 * a),
                'barrier_through_zero_MeV': (2 * a - b) ** 2 / (4 * a),
                'isotope_shape': None}
    theta = 0.0 if r >= 1 else math.pi / 2
    return {'kind': 'endpoint', 'angles_deg': [math.degrees(theta)],
            'energy_MeV': float(different_potential(theta, a, b)),
            'barrier_through_zero_MeV': None, 'isotope_shape': None}


def solve_chiral_octupole_equilibrium(beta2, gamma_deg, beta3, j_nu):
    """Compatibility guard: the former classifier was not a TAC solver."""
    raise NotImplementedError('withdrawn isotope classifier: no common TAC Hamiltonian or nuclear inputs verified')


def finite_difference_gradient(function, phi, a, b, step=2e-6):
    return float((function(phi + step, a, b) - function(phi - step, a, b)) / (2 * step))


def run_study(output=None):
    archive = json.loads(ARCHIVE.read_text())
    source = LIU_SOURCE.read_text(encoding='utf-8-sig')
    raw_name = re.search(r'^raw_file: "([^"]+)"', source, re.MULTILINE).group(1)
    expected = re.search(r'^raw_sha256: ([A-Fa-f0-9]+)', source, re.MULTILINE).group(1).lower()
    raw_hash = hashlib.sha256((ROOT / raw_name).read_bytes()).hexdigest()
    if raw_hash != expected:
        raise ValueError('Liu2016 source raw hash mismatch')

    isotope_audits = []
    for row in archive['legacy_witnesses']:
        a, b = row['written_A_MeV'], row['written_B_MeV']
        phi = math.radians(row['legacy_phi_deg'])
        isotope_audits.append({
            'nucleus': row['nucleus'], 'input_status': 'legacy-unverified',
            'legacy_reported_angle_deg': row['legacy_phi_deg'],
            'literal_written_gradient_MeV_per_rad': float(written_gradient(phi, a, b)),
            'literal_written_curvature_MeV_per_rad2': float(written_curvature(phi, a, b)),
            'literal_written_extremum': written_minimum(a, b),
            'diagnostic_scope': 'literal old formula only; not a fit to the named nucleus',
            'nuclear_equilibrium_angle_deg': None, 'nuclear_barrier_keV': None,
            'universal_beta3_cutoff': None, 'chiral_or_quartet_classification': None,
            'readiness': 'not-ready',
            'missing_inputs': ['common spin/frequency and configuration', 'three inertias or self-consistent fields',
                'single-particle Hamiltonian and octupole coupling', 'angle-coordinate convention',
                'quantized spectrum/parity and transition operators for any quartet claim'],
        })

    a, b = 1.0, 0.2  # Synthetic energy coefficients, without nuclear identity.
    alleged_phi = 0.5 * math.acos(b / a)
    literal = written_minimum(a, b)
    alternative = different_minimum(a / 2, b)
    coarse_grid = np.linspace(-math.pi / 2, math.pi / 2, 181)
    fine_grid = np.linspace(-math.pi / 2, math.pi / 2, 1441)
    exact_energy = alternative['energy_MeV']
    coarse_error = abs(float(np.min(different_potential(coarse_grid, a / 2, b))) - exact_energy)
    fine_error = abs(float(np.min(different_potential(fine_grid, a / 2, b))) - exact_energy)
    derivative_points = [-0.7, -0.23, 0.13, 0.51, 1.1]
    max_fd_error = max(abs(finite_difference_gradient(written_potential, p, a, b) -
                           written_gradient(p, a, b)) for p in derivative_points)
    max_other_fd_error = max(abs(finite_difference_gradient(different_potential, p, a / 2, b) -
                                 different_gradient(p, a / 2, b)) for p in derivative_points)
    cutoff = archive['injected_j_cutoff_witness']
    guard_rejects = False
    try:
        solve_chiral_octupole_equilibrium(0.28, 26, 0.045, 4.5)
    except NotImplementedError:
        guard_rejects = True
    checks = {
        'positive_cos_squared_term_minimum_at_pi_over_2': b * math.cos(math.pi / 2) ** 2 < b,
        'literal_zero_octupole_minimum_is_zero_not_45deg': written_minimum(1, 0)['angles_deg'] == [0.0],
        'literal_arccos_claim_not_stationary': abs(float(written_gradient(alleged_phi, a, b))) > 0.1,
        'literal_A_gt_B_endpoint_curvature_positive': written_curvature(0, a, b) > 0,
        'literal_B_gt_A_endpoint_curvature_positive': written_curvature(math.pi / 2, b, a) > 0,
        'literal_A_equals_B_flat': np.ptp(written_potential(fine_grid, 1, 1)) < 1e-12,
        'literal_reflection_even': all(math.isclose(float(written_potential(p, a, b)),
                                      float(written_potential(-p, a, b))) for p in derivative_points),
        'literal_gradient_vs_finite_difference': max_fd_error < 1e-8,
        'distinct_potential_gradient_vs_finite_difference': max_other_fd_error < 1e-8,
        'distinct_potential_arccos_stationary': abs(float(different_gradient(alleged_phi, a / 2, b))) < 1e-12,
        'distinct_potential_interior_curvature_positive': different_curvature(alleged_phi, a / 2, b) > 0,
        'distinct_potential_barrier_from_energy_difference': math.isclose(
            float(different_potential(0, a / 2, b)) - exact_energy, alternative['barrier_through_zero_MeV']),
        'distinct_potential_grid_refinement': fine_error < coarse_error and fine_error < 1e-6,
        'legacy_j_cutoff_is_injected_discontinuity': cutoff['11.999'][0] > 0 and cutoff['12.0'][0] == 0,
        'old_isotope_solver_disabled': guard_rejects,
        'all_isotope_scientific_predictions_withdrawn': all(x['nuclear_equilibrium_angle_deg'] is None
                                                          for x in isotope_audits),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    if not all(checks.values()):
        raise ArithmeticError(f'potential audit failed: {checks}')
    theory_manifest = ROOT / 'outputs/literature-acquisition/20261030-day27-wang2019-rat78br.json'
    theory = json.loads(theory_manifest.read_text())
    theory_hash = hashlib.sha256((ROOT / theory['staged_file']).read_bytes()).hexdigest()
    if theory_hash != theory['sha256']:
        raise ValueError('RAT-PRM primary preprint staging hash mismatch')
    result = {
        'schema_version': 2,
        'observed_at': datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'investigation': 'Literal potential extrema, injected cutoff and quartet attribution audit',
        'scientific_status': 'legacy TAC/nuclear predictions withdrawn; mathematical audit only',
        'literal_formula': 'V=-A*cos(2phi)/2+B*cos(phi)^2=B/2+(B-A)*cos(2phi)/2',
        'literal_gradient': '(A-B)*sin(2phi)',
        'literal_curvature': '2*(A-B)*cos(2phi)',
        'source_78Br': {'knowledge': LIU_SOURCE.relative_to(ROOT).as_posix(), 'raw_file': raw_name,
            'raw_sha256': raw_hash, 'reading_scope': 'PDF1-5 main text; PDF5 visually checked Fig6 and future-quartet paragraph',
            'claims': ['L16-9', 'L16-13', 'L16-14'],
            'reported': 'two chiral-doublet interpretations plus eight E1 links and octupole softness',
            'quartet_observation_in_this_paper': 'future proposal, not established quartet'},
        'source_rat2019': {
            'knowledge': 'knowledge/sources/wang-2019-rat-prm-78br-octupole-correlations.md',
            'arxiv': '1902.00191v1', 'manuscript_sha256': theory_hash,
            'reported_inputs_not_new_measurements': {'beta2': 0.28, 'gamma_deg': 16.3,
                'MDC_CDFT_beta3': 0.0, 'adopted_RAT_PRM_beta3': 0.02,
                'core_parity_splitting_MeV': 3.0},
            'tests_beta3_above_0_1': False,
            'source_boundary': 'no quantitative large-beta3 counterexample or universal cutoff supplied',
        },
        'legacy_isotope_formula_audit': isotope_audits,
        'injected_j_cutoff': cutoff,
        'synthetic_two_potential_comparison': {'input_status': 'no nuclear identity; no parameter inference',
            'A_MeV': a, 'B_MeV': b, 'legacy_arccos_angle_deg': math.degrees(alleged_phi),
            'literal_minimum': literal, 'literal_gradient_at_arccos': float(written_gradient(alleged_phi, a, b)),
            'different_formula': 'U=A*cos(2phi)^2/2-B*cos(2phi)',
            'different_minimum': alternative,
            'boundary': 'U is explicitly a different demonstration; paired angle minima do not establish nuclear chirality'},
        'numerical_controls': {'literal_max_gradient_fd_error': max_fd_error,
            'different_max_gradient_fd_error': max_other_fd_error,
            'different_grid_energy_error_coarse': coarse_error, 'different_grid_energy_error_fine': fine_error},
        'checks': checks,
        'no_experimental_upper_limit_or_confidence_generated': True,
        'no_curriculum_credit_applied': True,
    }
    output = Path(output or RUN / 'continuation-studies/chiral-octupole-tac/chiral_octupole_potential_audit_corrected.json')
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'output': str(output), 'synthetic_literal_gradient_at_claimed_angle':
                      result['synthetic_two_potential_comparison']['literal_gradient_at_arccos'],
                      'numerical_controls': result['numerical_controls'], 'checks': checks}, indent=2))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    run_study(parser.parse_args().output)
