#!/usr/bin/env python3
"""Conditional C uncertainty geometry from LV19 printed inputs; not a fitted Cov/CI."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def quad(g, matrix):
    return sum(g[i]*matrix[i][j]*g[j] for i in range(len(g)) for j in range(len(g)))


def main():
    pdf = ROOT/'tmp/day21-checkpoint103/lv2019-vor.pdf'
    sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert sha == '450a3032d7fecfdbc16f5a848be3d63842a536b0508dda73f3de55270fbf2066'
    # Order is I225, I896, E225, E896. The quoted energy-error rule is footnote a.
    x = [F('3.8'), F('.79'), F('225.8'), F('896.8')]
    sig = [F('.4'), F('.06'), F('.2'), F('.2')]

    def coefficient(values):
        i1, i3, e1, e3 = values
        return i3/i1*(e1/e3)**5

    g = [-1/x[0], 1/x[1], 5/x[2], -5/x[3]]
    lengths = [abs(a*b) for a, b in zip(g, sig)]
    total = sum(lengths)
    largest = max(lengths)
    minimum = max(F(0), 2*largest-total)
    largest_index = lengths.index(largest)
    witnesses = {}
    for label in ['maximum', 'minimum']:
        v = []
        for j, (gj, sj) in enumerate(zip(g, sig)):
            sign = 1 if gj > 0 else -1
            target = 1 if label == 'maximum' or j == largest_index else -1
            v.append(sj*sign*target)
        covariance = [[a*b for b in v] for a in v]
        assert all(covariance[i][i] == sig[i]**2 for i in range(4))
        variance = quad(g, covariance)
        expected = total**2 if label == 'maximum' else minimum**2
        assert variance == expected
        # The matrix is vv^T, so positive semidefiniteness is algebraic, no eigenvalue cutoff.
        witnesses[label] = {'rank_one_vector': [float(a) for a in v],
                            'g_Sigma_g': float(variance), 'PSD_reason': 'Sigma=v*v^T',
                            'is_actual_experimental_covariance': False}
    diagonal_variance = sum((a*b)**2 for a, b in zip(g, sig))
    # Nuisance invariants independent of the covariance exercise.
    c = coefficient(x)
    for gain, normalization in [(F('1.02'), F('1.4')), (F('2'), F('7'))]:
        y = [x[0]*normalization, x[1]*normalization, x[2]*gain, x[3]*gain]
        assert coefficient(y) == c
    common_offset_derivative = g[2]+g[3]
    assert common_offset_derivative > 0
    # Conditional rectangle image; no assertion that printed +/- define joint coverage.
    low = coefficient([x[0]+sig[0], x[1]-sig[1], x[2]-sig[2], x[3]+sig[3]])
    high = coefficient([x[0]-sig[0], x[1]+sig[1], x[2]+sig[2], x[3]-sig[3]])
    assert low < c < high
    # The bounded radiative fraction avoids delta-coordinate tails, but not f=0 singularity.
    control_f = [F('1/10'), F('1/5')]  # declared controls, never experimental mixing values
    image = [low/control_f[1], high/control_f[0]]
    assert image[0] < image[1]
    result = {
        'source': {'doi': '10.1103/PhysRevC.100.024314', 'sha256': sha,
                   'locator': '024314-5 Table I D6 and footnotes a,b'},
        'assumptions': ['Same parent and matching corrected photon rates/response',
                        '896.8 pure E2 and 225.8 restricted M1/E2 as in104',
                        'For local covariance geometry only: printed errors interpreted as marginal SD',
                        'Energies in keV; intensity normalization arbitrary but common'],
        'variable_order': ['I225', 'I896', 'E225_keV', 'E896_keV'],
        'printed_centers': [float(a) for a in x], 'printed_error_magnitudes': [float(a) for a in sig],
        'C_center': float(c), 'gradient_logC_wrt_absolute_variables': [float(a) for a in g],
        'local_logC_SD_envelope_over_all_PSD_with_declared_diagonal': [float(minimum), float(total)],
        'local_logC_SD_if_diagonal': math.sqrt(float(diagonal_variance)),
        'rank_one_endpoint_witnesses': witnesses,
        'common_intensity_normalization_cancels_exactly': True,
        'common_multiplicative_energy_gain_cancels_exactly': True,
        'common_additive_energy_offset_logC_derivative_per_keV': float(common_offset_derivative),
        'conditional_rectangle_C_image': [float(low), float(high)],
        'radiative_fraction_contract': {'f': 'delta225^2/(1+delta225^2)', 'R_E2': 'C/f',
                                        'dlogR': 'dlogC-dlogf',
                                        'example_f_interval_not_experimental': [float(a) for a in control_f],
                                        'conditional_R_image_for_example_f_interval': [float(a) for a in image],
                                        'R_unbounded_if_f_can_approach_zero': True},
        'actual_f': None, 'actual_Cov': None, 'new_CI': None, 'power_or_exposure': None,
        'scientific_boundary': 'Declared covariance/rectangle design, not original count analysis, reported CI, or chiral verdict',
    }
    out = RUN/'same-parent-covariance-scope-127.json'
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'output': str(out.relative_to(ROOT)),
                      'conditional_SD_envelope': result['local_logC_SD_envelope_over_all_PSD_with_declared_diagonal'],
                      'diagonal_case': result['local_logC_SD_if_diagonal'],
                      'offset_derivative_per_keV': float(common_offset_derivative), 'new_CI': None}))


if __name__ == '__main__':
    main()
