"""Declared ideal singles response to a source reduced vector, no data fit."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_halfspin_singles_response import population, response


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def coefficients(two_i, two_f, d_rb, weights, order):
    nodes, quadrature = np.polynomial.legendre.leggauss(order)
    y = np.array([response(two_i, two_f, d_rb, math.acos(float(x)), weights)[0] for x in nodes])
    return np.array([(2 * k + 1) / 2 * np.dot(quadrature * y, np.polynomial.legendre.legval(nodes, [0] * k + [1]))
                     for k in range(7)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    c = json.loads(a.contract.read_text())
    assert all(sha(Path(p)) == h for p, h in c['kernel_files'].items())
    rows = []
    max_projection = max_norm = max_forbidden = max_tensor_variation = 0.0
    for source in c['design_points']:
        two_i, two_f = source['two_I'], source['two_If']
        assert two_i % 2 == 1 and two_f == two_i - 2
        m = np.arange(-two_i, two_i + 1, 2) / 2
        reference = np.where(abs(m) == .5, .5, 0.0)
        gaussian = population(two_i, .2)
        alphas = []
        predictions = {}
        for label in ['support', 'counter']:
            delta = source[label + '_delta']
            d_rb = -delta
            whole = coefficients(two_i, two_f, d_rb, reference, 24)
            gauss = coefficients(two_i, two_f, d_rb, gaussian, 24)
            whole12 = coefficients(two_i, two_f, d_rb, reference, 12)
            gauss12 = coefficients(two_i, two_f, d_rb, gaussian, 12)
            max_projection = max(max_projection, float(max(abs(whole - whole12))), float(max(abs(gauss - gauss12))))
            max_norm = max(max_norm, abs(whole[0] - 1), abs(gauss[0] - 1))
            max_forbidden = max(max_forbidden, float(max(abs(whole[[1, 3, 5, 6]]))), float(max(abs(gauss[[1, 3, 5, 6]]))))
            assert min(abs(whole[[2, 4]])) > 1e-8
            alphas.append(gauss[[2, 4]] / whole[[2, 4]])
            empirical = whole[[2, 4]] * np.array([.84, .81])
            observed = np.array([source['reported_A2'], source['reported_A4']])
            extra = {}
            if source['source_energy_keV'] == 376.3:
                fig = c['source_Fig4point12_376']
                fig_vector = np.array([fig['A2'], fig['A4']])
                extra = {'Fig4point12_source_A2_A4': fig_vector.tolist(),
                         'complete_prediction_minus_Fig4point12_centre': (whole[[2, 4]] - fig_vector).tolist(),
                         'Gaussian_prediction_minus_Fig4point12_centre': (gauss[[2, 4]] - fig_vector).tolist(),
                         'empirical_prediction_minus_Fig4point12_centre': (empirical - fig_vector).tolist()}
            predictions[label] = {'source_delta_centre': delta, 'assumed_d_RB': d_rb,
                                  'complete_absMhalf_A2_A4': whole[[2, 4]].tolist(),
                                  'Gaussian_sigma_over_I_point2_A2_A4': gauss[[2, 4]].tolist(),
                                  'empirical_alpha_transfer_A2_A4': empirical.tolist(),
                                  'Gaussian_prediction_minus_published_centre': (gauss[[2, 4]] - observed).tolist(),
                                  'empirical_prediction_minus_published_centre': (empirical - observed).tolist(), **extra}
        max_tensor_variation = max(max_tensor_variation, float(max(abs(alphas[0] - alphas[1]))))
        rows.append({'source_identity': source, 'actual_discrete_Gaussian_RMS_M_over_I': float(math.sqrt(np.dot(gaussian, m * m)) / (two_i / 2)),
                     'Gaussian_alpha2_alpha4_relative_to_absMhalf': alphas[0].tolist(),
                     'predictions': predictions})
    controls = {'frozen_kernel_hashes_preserved': True,
                '12_vs24_angular_projection_converged': max_projection < 1e-12,
                'full_singles_C0_normalized': max_norm < 1e-12,
                'M1E2_angular_rank024_only': max_forbidden < 1e-12,
                'tensor_attenuation_independent_of_delta': max_tensor_variation < 1e-12,
                'source_DCO_like_r_not_used_as_Rac': True,
                'no_marginal_errors_used_as_independent_likelihood': True,
                'actual_Fig4point12_and_Table4point4_layers_preserved_separately': c['source_Fig4point12_376']['A2'] != c['design_points'][0]['reported_A2'] and c['source_Fig4point12_376']['A4'] != c['design_points'][0]['reported_A4']}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': c['scope'], 'formal_day_index': 23, 'contract_sha256': sha(a.contract),
           'implementation_sha256': sha(Path(__file__)), 'conditions': c,
           'rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()),
           'numerical_errors': {'projection': max_projection, 'norm': max_norm, 'forbidden': max_forbidden, 'tensor_invariance': max_tensor_variation},
           'limitations': ['Applying quoted delta as emission KS is an extra unverified source-producer assumption.',
                          'Gaussian .2 and transfer of empirical .84/.81 are separate declared ideal models, neither is certified original array/gate response.',
                          'Table4.1 reference belongs to a different J; transfer does not establish a physical target density or covariance.',
                          'Published coefficients are reduced observations sharing source inputs; their covariance is unknown.',
                          'Differences are conditional centre residuals, not chi-square, original calibration bias or a fitted delta.',
                          'Fig4.12 and Table4.4 coefficient roles are not fully mapped; numerical near-equality to a complete-alignment curve does not certify table deattenuation.',
                          'No fullprofile, equal minima, mode decision, new physical quantities, rates or beamtime.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'rows': rows, 'numerical_errors': out['numerical_errors']}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
