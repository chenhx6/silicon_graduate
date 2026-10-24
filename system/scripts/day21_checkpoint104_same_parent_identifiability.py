#!/usr/bin/env python3
"""Exact conditional information requirements from selected LV19 VoR inputs.

No assumed experimental mixing ratios, new lifetime, covariance or CI. Algebra
assumes matching same-parent photon intensities and an E2 / M1+E2 truncation.
"""
import hashlib
import json
from pathlib import Path
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def audit():
    # u=delta225^2, v=delta649^2. The symbolic relations are derived in
    # the knowledge note; exact Fraction checks below are declared algebra
    # controls, not assumed experimental parameter points or a CAS proof.
    Cval = F(79, 100) / F(38, 10) * (F(2258, 10) / F(8968, 10)) ** 5
    Dval = F(18, 10) / F(38, 10) * (F(2258, 10) / F(6489, 10)) ** 3
    assert 0 < float(Cval) < .001 and 0 < float(Dval) < .1
    controls = []
    for u, v in [(F(1, 10), F(2, 3)), (F(1), F(1)), (F(10), F(7))]:
        re2 = Cval * (1 + u) / u
        rm1 = Dval * (1 + u) / (1 + v)
        assert Cval / (re2 - Cval) == u
        assert re2 - Cval == Cval / u
        j11, j12 = -1 / (u * (1 + u)), F(0)
        j21, j22 = 1 / (1 + u), -1 / (1 + v)
        assert j11 * j22 - j12 * j21 == 1 / (u * (1 + u) * (1 + v))
        # Independent direct rate ratio cancels arbitrary common tau and scale.
        for tau, scale in [(F(1), F(1)), (F(7), F(13))]:
            b_out = F(79, 100) * scale / (tau * F(8968, 10) ** 5)
            b_in = F(38, 10) * scale * u / (1 + u) / (tau * F(2258, 10) ** 5)
            assert b_out / b_in == re2
        controls.append({'u': str(u), 'v': str(v), 'E2_ratio_over_C': str(re2 / Cval),
            'M1_ratio_over_D': str(rm1 / Dval), 'exact_rational_checks': True})
    source_pdf = ROOT / 'tmp/day21-checkpoint103/lv2019-vor.pdf'
    return {
        'scope': 'L2 exact conditional algebra and L3 measurement design, not experimental inference',
        'source': {'DOI': '10.1103/PhysRevC.100.024314', 'locator': '024314-5 Table I Band D6',
            'pdf_sha256': hashlib.sha256(source_pdf.read_bytes()).hexdigest(),
            'parent_keV': 4007.8, 'parent_spin_parity': '31/2-',
            'relative_photon_intensities': {'225.8': 3.8, '648.9': 1.8, '896.8': .79}},
        'assumptions': ['Same parent/line identities as Table I and Fig1',
            'Intensities represent matching photon rates after gate/response corrections',
            '896.8 treated as pure assigned E2; 225.8 and648.9 restricted to M1/E2',
            'delta is the radiation amplitude ratio in a consistent phase convention',
            'No claim that 2019 values reconstruct 2007 producer'],
        'coefficients': {'C_E2': float(Cval), 'D_M1': float(Dval)},
        'derived_relations': {'E2_ratio': 'C*(1+u)/u', 'M1_ratio': 'D*(1+u)/(1+v)',
            'log_ratio_jacobian': [['-1/(u*(1+u))', '0'], ['1/(1+u)', '-1/(1+v)']],
            'jacobian_determinant': '1/(u*(1+u)*(1+v)) > 0 for u,v > 0',
            'E2_inverse_u': 'C/(R_E2-C)', 'E2_minus_C': 'C/u',
            'common_lifetime_cancels': True, 'verification_scope': 'analytic derivation and declared rational controls; not CAS proof'},
        'declared_algebra_controls_not_experimental_parameters': controls,
        'identifiability': {
            'intensities_alone_determine_C_D_only': True,
            'unique_measured_B_ratios_obtained': False,
            'E2_ratio_requires_magnitude_of_delta225': True,
            'M1_ratio_also_requires_magnitude_of_delta649': True,
            'strength_ratios_alone_determine_signs': False,
            'absolute_tau_alone_resolves_u_v': False,
            'conditional_E2_lower_bound_C': float(Cval),
            'finite_upper_bound_without_mixing_constraint': None,
            'caution': 'Bound holds only for the stated pure-E2/matching-photon contract, not a universal mode criterion'},
        'recommended_next_inputs': ['joint calibrated delta225/relative photon ratio for E2 ratio',
            'also calibrated delta649 for M1 ratio', 'shared gate/efficiency/background and covariance',
            'absolute lifetime and complete branch/IC only if absolute strengths are required',
            'specific model prediction domain and detector counts for power calculation'],
        'experimental_delta225': None, 'experimental_delta649': None, 'actual_B_ratios': None,
        'actual_covariance': None, 'experimental_CI': None, 'exposure_or_power': None,
        'scientific_certification': False,
    }


if __name__ == '__main__':
    result = audit()
    p = RUN / 'same-parent-identifiability-104.json'
    p.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'output': str(p.relative_to(ROOT)), 'coefficients': result['coefficients'],
        'experimental_CI': None, 'exposure_or_power': None}, ensure_ascii=False))
