#!/usr/bin/env python3
"""Biswas Table 1 central-value arithmetic; no experimental fit or CI."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def fraction(delta):
    return delta * delta / (1 + delta * delta)


def main():
    pdf = ROOT / 'raw/papers/2019_Biswas et al_Longitudinal wobbling in 133La.pdf'
    rows = []
    for energy, spin, delta, plus, minus, printed, ratio in [
        (758, '17/2- -> 15/2-', -2.05, .39, .30, 80.8, 1.127),
        (874, '21/2- -> 19/2-', -2.60, .46, .47, 87.1, .716),
        (982, '25/2- -> 23/2-', -3.07, .47, .65, 90.4, .545),
    ]:
        f = fraction(delta)
        endpoints = sorted([fraction(delta + plus), fraction(delta - minus)])
        rows.append(dict(energy_keV=energy, spin=spin, reported_delta=delta,
                         delta_plus=plus, delta_minus=minus,
                         calculated_E2_percent=100*f, printed_E2_percent=printed,
                         absolute_rounding_residual_percentage_points=abs(100*f-printed),
                         transformed_printed_delta_endpoints_percent=[100*x for x in endpoints],
                         endpoint_status='algebraic images only; not re-estimated CI; printed fraction errors retained separately',
                         reported_BE2out_BE2in=ratio, locator='PDF p.5 Table 1'))
    axes = []
    for gamma in [22, 26]:
        # Declare the convention before assigning geometric names. Axis length
        # is monotone in cos(angle) for positive quadrupole amplitude.
        triples = [(angle, math.cos(math.radians(angle)), math.sin(math.radians(angle))**2)
                   for angle in [gamma, gamma-120, gamma+120]]
        ordered = sorted(triples, key=lambda x: x[1])
        named = {name: {'angle_deg': t[0], 'relative_shape_cos': t[1], 'inertia_factor': t[2]}
                 for name, t in zip(['short', 'medium', 'long'], ordered)}
        axes.append({'gamma_deg': gamma, 'convention': 'R_k=R0[1+c beta cos(gamma-2pi k/3)], c beta>0; J_k proportional sin^2(same angle)',
                     'axes': named, 'scope': 'declared irrotational rotor, not extracted La moments of inertia'})
    counterfactual = {'chosen_delta': -.4, 'E2_percent':100*fraction(-.4),
                      'scope':'illustration only; not a reported or statistically compatible experimental branch'}
    checks = {
        'all_three_printed_central_fractions_round_to_one_decimal':all(x['absolute_rounding_residual_percentage_points']<.05 for x in rows),
        'medium_largest_in_declared_irrotational_convention':all(x['axes']['medium']['inertia_factor']>x['axes']['short']['inertia_factor']>x['axes']['long']['inertia_factor'] for x in axes),
        'counterfactual_is_not_fitted':counterfactual['scope'].startswith('illustration only'),
    }
    result = {'schema_version':1,'scope':'literal central arithmetic and explicit axis convention only',
              'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'rows':rows,
              'axis_convention_controls':axes,'counterfactual':counterfactual,'checks':checks,
              'scientific_certification':False,'experimental_fit_executed':False,
              'missing_inputs':['joint DCO-polarization likelihood','matching alignment and detector response','joint covariance'],
              'all_arithmetic_checks_pass':all(checks.values())}
    (RUN/'literal-scope-audit-042.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':checks,'scientific_certification':False},ensure_ascii=False))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
