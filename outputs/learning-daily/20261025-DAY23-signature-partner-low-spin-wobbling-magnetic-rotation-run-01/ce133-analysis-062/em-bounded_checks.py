#!/usr/bin/env python3
"""Conditional arithmetic on printed central values; no fit, CI or producer replay."""
from pathlib import Path
import json
import math

OUT = Path(__file__).resolve().parent
C = 0.7  # Thesis Eq 3.24: delta = sqrt(.7)*E_gamma(MeV)*E2/M1 matrix ratio.


def implied_energy(delta, r_e2, r_m1):
    return math.sqrt(delta * delta * r_m1 / (C * r_e2))


def main():
    rows = [
        dict(line='624.6 keV', printed_label_keV=625, e_mev=.6246,
             parent='Band4 13/2-', final='Band1 11/2-', delta=-1.5,
             delta_minus=5.7, delta_plus=.97, r_outout_e2=1.15, r_outout_m1=.14,
             intensity_out=3.3, e_reference_mev=.7948, intensity_reference=8.0,
             reference_identity='Band4 13/2- -> Band1 9/2-, 794.8keV E2',
             conditional_intensity_denominator='out/out'),
        dict(line='582.7 keV', printed_label_keV=582, e_mev=.5827,
             parent='Band4 17/2-', final='Band1 15/2-', delta=-.55,
             delta_minus=.25, delta_plus=.12, r_outout_e2=5.06, r_outout_m1=3.95,
             r_outin_e2=.33, r_outin_m1=.25, intensity_out=3.53,
             e_reference_mev=.5778, intensity_reference=3.22,
             reference_identity='Band4 17/2- -> Band4 13/2-, 577.8keV E2',
             conditional_intensity_denominator='out/in'),
        dict(line='464.4 keV', printed_label_keV=465, e_mev=.4644,
             parent='Band4 19/2-', final='Band1 17/2-', delta=-.17,
             delta_minus=.2, delta_plus=.09, r_outout_e2=1.06, r_outout_m1=5.54,
             r_outin_e2=.09, r_outin_m1=.47, intensity_out=1.89,
             e_reference_mev=.6083, intensity_reference=1.89,
             reference_identity='Band4 19/2- -> Band4 15/2-, 608.3keV E2',
             conditional_intensity_denominator='out/in'),
    ]
    for r in rows:
        d2 = r['delta'] ** 2
        r['central_E2_photon_fraction_from_delta'] = d2 / (1 + d2)
        endpoints = [r['delta']-r['delta_minus'], r['delta']+r['delta_plus']]
        squares = [v*v for v in endpoints]
        if endpoints[0] <= 0 <= endpoints[1]:
            squares.append(0)
        r['printed_delta_endpoint_image_NOT_new_CI'] = [min(squares)/(1+min(squares)),
                                                       max(squares)/(1+max(squares))]
        for denominator in ['outout', 'outin']:
            if f'r_{denominator}_e2' not in r:
                continue
            predicted_d2 = C*r['e_mev']**2*r[f'r_{denominator}_e2']/r[f'r_{denominator}_m1']
            r[f'{denominator}_central_ratio_delta_closure'] = {
                'delta_squared_printed': d2,
                'delta_squared_from_ratio_and_observed_Egamma': predicted_d2,
                'relative_central_discrepancy': predicted_d2/d2-1,
                'meaning': 'Algebraic dependence/rounding check, NOT independent evidence or a significance test'}
        q = r['intensity_out']/r['intensity_reference']
        k = q*(r['e_reference_mev']/r['e_mev'])**5
        r['conditional_same_parent_printed_intensity_reconstruction'] = {
            'r_e2': k*d2/(1+d2), 'r_m1': C*r['e_mev']**2*k/(1+d2),
            'assumptions': ['Table5.2 intensities are efficiency-corrected photon intensities for the same sample/gates',
                            'reference is pure E2 and shares the exact parent',
                            'Table6.11 central delta is applicable to these intensity estimates',
                            'No separately introduced internal-conversion factor for a direct photon-rate ratio'],
            'boundary': 'These are conditional recombinations of printed summaries, not recovered author inputs. No Cov, likelihood, significance or CI is supplied.'}
    model_rows = [
        dict(table='6.9', model='nine-orbital QTR', spin='17/2-', delta=-2.24, r_e2=.75, r_m1=.01),
        dict(table='6.9', model='nine-orbital QTR', spin='19/2-', delta=-2.72, r_e2=.32, r_m1=.03),
        dict(table='6.10', model='single-orbital FA', spin='17/2-', delta=-.49, r_e2=.44, r_m1=.19),
        dict(table='6.10', model='single-orbital FA', spin='19/2-', delta=-.49, r_e2=.11, r_m1=.062),
    ]
    for r in model_rows:
        r['conditional_algebraic_Egamma_MeV_implied_by_printed_triple'] = implied_energy(r['delta'],r['r_e2'],r['r_m1'])
        r['boundary'] = 'Consistency target only; model-predicted transition energies/producer unknown. Do NOT insert experimental Egamma to declare a model algebra error.'
    result = {'units': {'Egamma':'MeV','r_e2':'dimensionless','r_m1':'mu_N^2 / (e^2 b^2)'},
              'coefficient': C, 'coefficient_locator':'Thesis Eq3.24, printed37/PDF48',
              'experimental_rows': rows, 'model_rows': model_rows,
              'Table6_3_9over2plus_partial_normalization': {
                  'locator':'Table6.3, printed71/PDF82',
                  'printed_amplitudes':[.982,-.202,.185],
                  'sum_of_three_squares':.982**2+.202**2+.185**2,
                  'minimum_with_half_last_decimal_rounding':.9815**2+.2015**2+.1845**2,
                  'boundary':'Under the stated orthonormal strong-coupling basis and squared-amplitude interpretation, this partial sum exceeds 1. Actual producer/basis normalization missing; do not repair or renormalize the printed row.'},
              'scope': 'No independent experiments; no parameter fitting; no confidence intervals; no actual model-producer replay; no physics mode classification.'}
    for r in rows:
        assert 0 <= r['central_E2_photon_fraction_from_delta'] <= 1
        # Sign of delta must not change any rate/fraction result.
        assert r['delta']**2 == (-r['delta'])**2
    (OUT/'bounded_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
