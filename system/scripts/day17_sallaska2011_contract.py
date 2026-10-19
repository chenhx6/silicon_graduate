#!/usr/bin/env python3
"""Rounded published partial-strength budget and normalization algebra, not a fit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    p = RUN / 'sallaska2011-exercise-contract.json'
    c = json.loads(p.read_text())
    assert c['identity'] == 'S11-ACTUAL-PARTIAL-STRENGTH-BUDGET-01'
    assert sha(ROOT / c['pdf']) == c['pdf_sha256']
    rows = []
    for r in c['rows']:
        total = sum(x[0] for x in r['partials'])
        var_stat = sum(x[1] ** 2 for x in r['partials'])
        minus = math.sqrt(var_stat + (total * r['systematic_minus_pct'] / 100) ** 2)
        plus_quadrature = math.sqrt(var_stat + (total * r['systematic_plus_pct'] / 100) ** 2)
        plus = plus_quadrature + sum(r['added_upper_meV'])
        rows.append({'Ep': r['Ep'], 'sum_printed_partial_meV': total,
                     'conditional_stat_quadrature_meV': math.sqrt(var_stat),
                     'conditional_lower_scale_meV': minus,
                     'conditional_upper_before_one_sided_additions_meV': plus_quadrature,
                     'allowed_upper_additions_meV': sum(r['added_upper_meV']),
                     'conditional_upper_scale_meV': plus,
                     'reported_total_minus_plus': r['reported_total'],
                     'nominal_residuals_meV': [total-r['reported_total'][0],
                                               minus-r['reported_total'][1],
                                               plus-r['reported_total'][2]],
                     'not_joint_CI_or_actual_covariance_recovered': True})
    f = c['tail_fraction_total']
    factor = 1 / (1 - f)
    tail = {'fraction_of_total': f, 'total_over_observed': factor,
            'tail_over_observed': f / (1-f),
            'conditional_relative_scale_from_fraction_only': c['tail_fraction_scale']/(1-f),
            'boundary': 'local derivative holding observed area fixed; reference data shared, not an independent experimental sigma'}
    # A shared multiplicative efficiency scale cancels between activity and capture.
    # Dimensionless declared sensitivity control; no event or detector model.
    ng, na, eh, el, rho, decay = 17., 23., .003, .021, 2.58, .7
    def strength(scale):
        atoms = na / (scale * el * decay)
        return (ng / (scale * eh)) / (atoms * rho)
    scales = [.25, .7, 1., 1.3, 4.]
    values = [strength(s) for s in scales]
    assert max(abs(x-values[2]) for x in values) < 1e-13
    exact_magic = math.degrees(math.acos(1/math.sqrt(3)))
    x = math.cos(math.radians(55))
    angle = {'source_nominal_lab_angle_deg': 55, 'exact_P2_zero_deg': exact_magic,
             'P2_at_literal55': (3*x*x-1)/2, 'P4_at_literal55': (35*x**4-30*x*x+3)/8,
             'boundary': 'point Legendre only; actual finite geometry/boost studied by authors, not new efficiency correction'}
    result = {'at': datetime.now(timezone.utc).isoformat(), 'script_sha256': sha(Path(__file__)),
              'contract_sha256': sha(p), 'pdf_sha256': c['pdf_sha256'], 'rows': rows,
              '213_tail_normalization': tail,
              'shared_efficiency_scale_control': {'scales': scales, 'conditional_strengths': values,
                   'log_derivatives': {'eta_high': -1, 'eta1275': 1, 'common_scale': 0},
                   'variance_log_efficiency_ratio': 'Var(log eta1275)+Var(log etaHigh)-2Cov(log eta1275,log etaHigh)',
                   'not_a_claim_of_source_double_counting': True},
              'nominal_angle_control': angle,
              'unclosed_454_nominal_error_is_preserved': True,
              'no_new_experimental_strength_branch_or_CI': True,
              'ok': True}
    (RUN / 'sallaska2011-exercise-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
