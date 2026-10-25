#!/usr/bin/env python3
"""Reconstruct JE02 Table II central ratios; no lifetime or experimental CI fit."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / 'raw/papers/2002_Jensen et al_Evidence for Second-Phonon Nuclear Wobbling.pdf'
EXPECTED_SHA = 'c6fd99c17c09763f742cbe36443f7039f21b3e28a5caa548748bdf0718630a8a'


def reconstruct():
    digest = hashlib.sha256(RAW.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA:
        raise ValueError('JE02 raw identity mismatch')
    branch = 0.14
    energy_out, energy_in = 476.0, 627.0
    common = branch * (energy_in / energy_out) ** 5
    rows = []
    for label, delta, printed_e2, printed_m1 in [
        ('large', -3.60, 0.51, 0.006),
        ('small', -0.19, 0.019, 0.083),
    ]:
        fraction = delta ** 2 / (1 + delta ** 2)
        r_e2 = common * fraction
        r_m1 = (0.835 * energy_out / 1000) ** 2 * r_e2 / delta ** 2
        # Half of the last printed unit, a rounding box, not an experimental CI.
        low_d, high_d = abs(delta) - .005, abs(delta) + .005
        e2_bounds = [
            .135 * (626.5 / 476.5) ** 5 * low_d ** 2 / (1 + low_d ** 2),
            .145 * (627.5 / 475.5) ** 5 * high_d ** 2 / (1 + high_d ** 2),
        ]
        m1_bounds = [
            .135 * .8345 ** 2 * (626.5 / 1000) ** 5 / (476.5 / 1000) ** 3 / (1 + high_d ** 2),
            .145 * .8355 ** 2 * (627.5 / 1000) ** 5 / (475.5 / 1000) ** 3 / (1 + low_d ** 2),
        ]
        rows.append({
            'branch': label, 'delta_printed_center': delta,
            'e2_photon_fraction': fraction,
            'rE2_reconstructed': r_e2, 'rE2_printed': printed_e2,
            'rM1_reconstructed_muN2_per_e2b2': r_m1,
            'rM1_printed_muN2_per_e2b2': printed_m1,
            'rounding_box_rE2': e2_bounds,
            'rounding_box_rM1': m1_bounds,
            'scope': 'rounded central-value arithmetic, no joint covariance or confidence fit',
        })
    controls = {
        'rE2_large_center_in_input_rounding_box': rows[0]['rounding_box_rE2'][0] <= .51 <= rows[0]['rounding_box_rE2'][1],
        'rE2_small_center_in_input_rounding_box': rows[1]['rounding_box_rE2'][0] <= .019 <= rows[1]['rounding_box_rE2'][1],
        'rM1_large_center_in_input_rounding_box': rows[0]['rounding_box_rM1'][0] <= .006 <= rows[0]['rounding_box_rM1'][1],
        'rM1_small_center_in_input_rounding_box': rows[1]['rounding_box_rM1'][0] <= .083 <= rows[1]['rounding_box_rM1'][1],
    }
    return {
        'raw_sha256': digest,
        'inputs': {
            'same_parent': 'TSD3 45/2+',
            'out': '476 keV to TSD2 43/2+',
            'in': '627 keV to TSD3 41/2+',
            'photon_branch_ratio': branch,
            'locator': '142503-2 Fig.1; 142503-3 Table II; 142503-4 small-root paragraph',
            'denominator_assumption': 'pure stretched E2 as assigned in the source',
        },
        'results': rows, 'controls': controls,
        'printed_rE2_large_to_small_ratio': .51 / .019,
        'printed_normalized_two_to_one_central_ratio': .51 / .21,
        'same_parent_TSD3_45half_two_exit_comparison': {
            'parent': 'TSD3 45/2+',
            'to_TSD1': '1119.2keV to41/2+',
            'to_TSD2': '476keV to43/2+',
            'common_in': '627keV toTSD3 41/2+',
            'photon_branch_ratios_to_in': [.33,.14],
            'printed_rE2_out20_over_out21_large': .018/.51,
            'printed_rE2_out20_over_out21_small': .018/.019,
            'photon_formula_large': (.33/.14)*(476/1119.2)**5/(3.60**2/(1+3.60**2)),
            'photon_formula_small': (.33/.14)*(476/1119.2)**5/(.19**2/(1+.19**2)),
            'scope': 'same-parent/common-in cancels tau and normalizer; delta branch and photon-efficiency covariance remain',
        },
        'delta_n_approx_2_table_I': {
            'source': '142503-2 Table I, six printed ratio rows among eight established links',
            'Egamma_keV': [1018.1, 1070.8, 1119.2, 1165.3, 1209.5, 1253.8],
            'rE2': [.021, .022, .018, .017, .022, .020],
        },
        'boundaries': [
            'No absolute B(E2), B(M1), W.u. or lifetime is inferred.',
            'TableI1119.2 andTableII476 shareTSD3 45/2+ parent and627in; quotient is not an independent new experiment or a new root-selection observable.',
            'No sign or significance of polarization is inferred.',
            'Two printed solutions are alternatives, not an observed physical strength collapse.',
            'The ratio .51/.21 divides normalized strengths with different in-band denominators.',
            'No shared-response or branch covariance is available; these controls do not reproduce experimental confidence intervals.',
            'The gamma-rate mixing constant uses MeV, e2b2 and muN2; its rounding limits the reconstruction.',
            'Initial central residual .005407 for the large rE2 exceeded .005; input rounding must be propagated as a box, not confused with an experimental uncertainty.',
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = (ROOT / args.output).resolve()
    if not out.is_relative_to(ROOT / 'outputs'):
        parser.error('output must be inside repository outputs/')
    data = reconstruct()
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'controls': data['controls'], 'no_absolute_strength_inference': True}))
    return 0 if all(data['controls'].values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
