#!/usr/bin/env python3
"""Literal thesis tables and conditional covariance arithmetic, not a new CI."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
from scipy.stats import chi2

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp = RUN / 'fougeres2022-thesis-ch6-exercise-contract.json'
    c = json.loads(cp.read_text())
    assert sha(ROOT / c['pdf']) == c['pdf_sha256']
    hbar = c['hbar_meV_fs']
    widths = []
    for x in c['lifetime_width_rows']:
        t, plus, minus = x['tau_fs'], x['tau_plus_fs'], x['tau_minus_fs']
        g = hbar / t
        widths.append({**x, 'recalculated_Gamma_meV': g,
                       'recalculated_plus_meV': hbar / (t - minus) - g,
                       'recalculated_minus_meV': g - hbar / (t + plus),
                       'central_minus_printed_meV': g - x['printed_Gamma_meV'],
                       'boundary': 'literal marginal endpoint mapping; not a joint confidence interval'})
    a, b = c['betaM'], c['DCLM']
    s1 = (a['plus'] + a['minus']) / 2
    s2 = (b['plus'] + b['minus']) / 2
    w1 = s2*s2 / (s1*s1 + s2*s2)
    w2 = 1 - w1
    independent_var = (w1*s1)**2 + (w2*s2)**2
    cross = 2*w1*w2*s1*s2
    rho_critical = (min(s1, s2)**2 - independent_var) / cross
    scenarios = [{'rho': rho, 'variance_fs2': independent_var + cross*rho,
                  'sigma_fs': math.sqrt(max(0, independent_var + cross*rho)),
                  'covariance_determinant_fs4': s1*s1*s2*s2*(1-rho*rho)}
                 for rho in [-1, 0, .5, .9, 1]]
    assert scenarios[-2]['sigma_fs'] > min(s1, s2)
    assert all(x['covariance_determinant_fs4'] >= 0 for x in scenarios)
    cov = {'declared_symmetrization': 'arithmetic average of printed upper/lower errors',
           'sigma_inputs_fs': [s1, s2], 'fixed_weights': [w1, w2],
           'central_fs': w1*a['tau'] + w2*b['tau'], 'min_sigma_policy_fs': min(s1, s2),
           'rho_above_which_fixed_weight_sigma_exceeds_min_policy': rho_critical,
           'scenarios': scenarios,
           'boundary': 'conditional Gaussian covariance, unknown actual rho/asymmetric likelihood; no experimental CI revision'}
    p = c['BRp_percent'] / 100
    final_g = hbar / c['final_tau_fs']
    branch = {'BRp_fraction': p, 'Gamma_p_meV_at_final_tau': p*final_g,
              'tau_fixed_branch_only_sigma_meV': final_g*c['BRp_percent_sigma']/100,
              'F23_branch_only_sigma_meV_with_same_Gamma': final_g*c['F23_BRp_percent_sigma']/100,
              'boundary': 'arithmetic only; no unknown lifetime-branch covariance filled'}
    thresholds = [{'CL': cl, 'parameters': m, 'chi2_quantile': float(chi2.ppf(cl, m)),
                   'printed': val} for cl, vals in [(.68, c['Table6p1_68']), (.95, c['Table6p1_95'])]
                  for m, val in enumerate(vals, 1)]
    out = {'at': datetime.now(timezone.utc).isoformat(), 'script_sha256': sha(Path(__file__)),
           'contract_sha256': sha(cp), 'literal_width_crosschecks': widths,
           'Eq6p2_conditional_covariance': cov, 'branch_scale_crosscheck': branch,
           'Table6p1_thresholds': thresholds,
           'literal_inputs_preserved': True, 'no_new_experimental_lifetime_branch_or_CI': True,
           'ok': True}
    (RUN / 'fougeres2022-thesis-ch6-exercise-result.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
