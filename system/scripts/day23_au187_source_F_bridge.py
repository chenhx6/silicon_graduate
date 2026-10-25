"""Source Eq2.43 Racah contraction vs photon amplitudes, not producer replay."""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import factorial_integer as fact, clebsch_gordan as cg
from day23_au187_ad_vector_forward import coefficients
from day23_halfspin_singles_response import population


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def triangle(a, b, c):
    if 2 * max(a, b, c) > a + b + c:
        return Fraction(0)
    return Fraction(fact(a + b - c) * fact(a - b + c) * fact(-a + b + c), fact(a + b + c + 1))


def sixj(a, b, c, d, e, f):
    delta = triangle(a, b, c) * triangle(a, e, f) * triangle(d, b, f) * triangle(d, e, c)
    if not delta:
        return 0.0
    xs = [a + b + c, a + e + f, d + b + f, d + e + c]
    ys = [a + b + d + e, a + c + d + f, b + c + e + f]
    terms = Fraction(0)
    for z in range(int(round(max(xs))), int(round(min(ys))) + 1):
        den = math.prod(fact(z - x) for x in xs) * math.prod(fact(y - z) for y in ys)
        terms += Fraction((-1) ** z * fact(z + 1), den)
    return math.sqrt(delta) * float(terms)


def racah(a, b, c, d, e, f):
    return (-1) ** int(round(a + b + c + d)) * sixj(a, b, e, d, c, f)


def source_F(two_i, two_f, l1, l2, k):
    i, f = two_i / 2, two_f / 2
    return ((-1) ** int(round(f - i - 1)) * math.sqrt((2 * l1 + 1) * (2 * l2 + 1) * (2 * i + 1))
            * cg(l1, 1, l2, -1, k, 0) * racah(i, i, l1, l2, k, f))


def source_B(two_i, k):
    i = two_i / 2
    return math.sqrt(2 * i + 1) * (-1) ** ((two_i - 1) // 2) * cg(i, .5, i, -.5, k, 0)


def source_rho(two_i, k, weights):
    i = two_i / 2
    return math.sqrt(2 * i + 1) * sum((-1) ** int(round(i - m)) * cg(i, m, i, -m, k, 0) * p
                                   for m, p in zip(np.arange(-two_i, two_i + 1, 2) / 2, weights))


def source_coefficients(two_i, delta, tensors):
    return np.array([tensors[k] * (source_F(two_i, two_i - 2, 1, 1, k)
                                  + 2 * delta * source_F(two_i, two_i - 2, 1, 2, k)
                                  + delta ** 2 * source_F(two_i, two_i - 2, 2, 2, k))
                     / (1 + delta ** 2) for k in [0, 2, 4]])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--contract', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    c = json.loads(a.contract.read_text())
    assert all(sha(Path(p)) == h for p, h in c['frozen_input'].items())
    known = [(sixj(.5, .5, 0, .5, .5, 0), -.5),
             (sixj(1, 1, 0, 1, 1, 0), 1 / 3),
             (sixj(1, 1, 1, 1, 1, 1), 1 / 6)]
    max_known = max(abs(x - y) for x, y in known)
    max_reference = max_gaussian = max_tensor = max_norm = wrong_coordinate_difference = 0.0
    rows = []
    for ti in c['design_spins']:
        m = np.arange(-ti, ti + 1, 2) / 2
        reference = np.where(abs(m) == .5, .5, 0.0)
        gaussian = population(ti, .2)
        tb = {k: source_B(ti, k) for k in [0, 2, 4]}
        tr = {k: source_rho(ti, k, reference) for k in [0, 2, 4]}
        tg = {k: source_rho(ti, k, gaussian) for k in [0, 2, 4]}
        max_tensor = max(max_tensor, max(abs(tb[k] - tr[k]) for k in tb))
        for d in c['design_deltas']:
            src = source_coefficients(ti, d, tb)
            sg = source_coefficients(ti, d, tg)
            amp = coefficients(ti, ti - 2, -d, reference, 12)[[0, 2, 4]]
            ag = coefficients(ti, ti - 2, -d, gaussian, 12)[[0, 2, 4]]
            wrong = coefficients(ti, ti - 2, d, reference, 12)[[0, 2, 4]]
            max_reference = max(max_reference, float(max(abs(src - amp))))
            max_gaussian = max(max_gaussian, float(max(abs(sg - ag))))
            max_norm = max(max_norm, abs(src[0] - 1), abs(sg[0] - 1))
            wrong_coordinate_difference = max(wrong_coordinate_difference, float(max(abs(src - wrong))))
            if (ti, d) in [(11, -2.67), (11, -2.6637), (15, -2.98)]:
                rows.append({'two_I': ti, 'source_equation_delta': d,
                             'source_equation_complete_C0_A2_A4': src.tolist(),
                             'source_equation_Gaussian_C0_A2_A4': sg.tolist(),
                             'photon_amplitude_complete_C0_A2_A4': amp.tolist()})
    controls = {'frozen_source_layer_input_hash_checked': True,
                'three_analytic_6j_rows': max_known < 1e-14,
                'halfspin_B_equals_symmetric_Mhalf_density_tensor': max_tensor < 1e-13,
                'source_F_complete_equals_RB_with_dRB_minus_delta': max_reference < 1e-12,
                'source_F_Gaussian_equals_RB_with_dRB_minus_delta': max_gaussian < 1e-12,
                'source_C0_is_one': max_norm < 1e-13,
                'unmapped_same_sign_coordinate_changes_interference': wrong_coordinate_difference > .1}
    controls = {k: bool(v) for k, v in controls.items()}
    out = {'scope': c['scope'], 'formal_day_index': 23, 'contract_sha256': sha(a.contract),
           'implementation_sha256': sha(Path(__file__)), 'conditions': c,
           'contraction_scope': 'Racah sum vs photon matrix contraction; both reuse one existing CG primitive, not independent all libraries',
           'comparison_count_per_alignment': len(c['design_spins']) * len(c['design_deltas']),
           'rows': rows, 'controls': controls, 'all_controls_pass': all(controls.values()),
           'errors': {'analytic_6j': max_known, 'B_vs_rho': max_tensor,
                      'complete_F_vs_amplitude': max_reference, 'Gaussian_F_vs_amplitude': max_gaussian,
                      'C0': max_norm, 'unmapped_coordinate_max_difference': wrong_coordinate_difference},
           'limitations': ['Mathematical mapping is established for the printed source equations and declared kernel, not an original analysis interface.',
                          'No actual polarization axis/finitearray/gate/efficiency response or global likelihood is certified.',
                          'Fig4.12 vs Table4.4 coefficient processing remains unbound.',
                          'No raw-count fit, inferred delta, confidence or nuclear assignment/rate/time.']}
    a.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'all_controls_pass': out['all_controls_pass'], 'comparison_count_per_alignment': out['comparison_count_per_alignment'],
                      'rows': rows, 'errors': out['errors']}))
    raise SystemExit(0 if out['all_controls_pass'] else 1)


if __name__ == '__main__':
    main()
