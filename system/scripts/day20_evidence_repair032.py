#!/usr/bin/env python3
"""Reproducible conditional controls; never an experimental fit or CI.

Inputs: this run's literal Singh ledger, Klemme Table III printed energies,
and Lv accepted-copy Table I same-parent photon intensities. No digitized
plot values, fitted stopping histories or unpublished covariance are assumed.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.constants import alpha, c, electron_volt, hbar
from scipy.stats import norm, nct, t


def gls(x, y, sigma):
    x = np.asarray(x, float)
    design = np.column_stack([np.ones(len(x)), x - x.mean()])
    precision = np.linalg.inv(sigma)
    covariance = np.linalg.inv(design.T @ precision @ design)
    estimate = covariance @ design.T @ precision @ y
    residual = y - design @ estimate
    return estimate, covariance, float(residual @ precision @ residual)


def power(delta, df=None):
    if df is None:
        critical = norm.ppf(.975)
        return float(norm.sf(critical - delta) + norm.cdf(-critical - delta))
    critical = t.ppf(.975, df)
    return float(nct.sf(critical, df, delta) + nct.cdf(-critical, df, delta))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir', type=Path, required=True)
    args = parser.parse_args()
    ledger = json.loads((args.run_dir / 'singh-table-ledger-001.json').read_text())
    controls = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        controls.append(name)

    bands = {}
    for key in ['case_Ce131', 'case_Pr133']:
        rows = [r for r in ledger[key]['rows'] if r['Qt']['kind'] == 'finite']
        x = np.array([r['spin'] for r in rows])
        y = np.array([r['Qt']['value'] for r in rows])
        s = np.array([(r['Qt']['minus'] + r['Qt']['plus']) / 2 for r in rows])
        sigma = np.diag(s*s)
        estimate, covariance, chi2 = gls(x, y, sigma)
        se = math.sqrt(covariance[1, 1])
        weights = s**-2 / np.sum(s**-2)
        omitted = []
        for i in range(len(x)):
            keep = np.arange(len(x)) != i
            b, cov, _ = gls(x[keep], y[keep], np.diag(s[keep]**2))
            omitted.append({'omitted_spin': float(x[i]), 'slope': float(b[1]),
                            'known_error_se': math.sqrt(cov[1, 1])})
        # Independent scalar formula checks the GLS slope variance.
        mean = np.sum(x/s**2)/np.sum(s**-2)
        check(key + ': scalar vs GLS variance', np.isclose(covariance[1, 1], 1/np.sum((x-mean)**2/s**2)))
        gradient = .02 * (x - x.mean())
        _, grad_cov, _ = gls(x, y, sigma + np.outer(gradient, gradient))
        check(key + ': slope-nuisance variance adds a squared', np.isclose(grad_cov[1, 1], covariance[1, 1] + .02**2))
        check(key + ': Gaussian null size', np.isclose(power(0), .05))
        check(key + ': Student null size', np.isclose(power(0, len(x)-2), .05))
        bands[key] = {'scope': 'Present finite rows only; errors averaged; independent Gaussian control',
                      'spins': x.tolist(), 'Qt_eb': y.tolist(), 'sigma_eb': s.tolist(),
                      'normalized_inverse_variance_weights': weights.tolist(),
                      'slope': float(estimate[1]), 'known_error_se': se,
                      'chi2': chi2, 'residual_df': len(x)-2, 'leave_one_out': omitted,
                      'chosen_alternative_slope_eb_per_hbar': -.05,
                      'chosen_end_to_end_drop_eb': .05*float(np.ptp(x)),
                      'Gaussian_power_for_chosen_alternative': power(.05/se),
                      'Student_power_if_covariance_shape_known_scale_estimated_true_scale_one': power(.05/se, len(x)-2),
                      'gradient_nuisance_slope_se': math.sqrt(grad_cov[1, 1]),
                      'limitations': 'The alternative is a design choice, not a shared 15% experimental or theoretical prediction; no universal sample/span limit.'}

    # General E2 radiation formula: B in e^2 b^2, E in MeV, rate in ps^-1.
    hbar_mev_s = hbar / (electron_volt * 1e6)
    hbar_c_mev_fm = hbar_mev_s * c * 1e15
    coeff = (4*math.pi/75)*alpha*1e4/(hbar_mev_s*hbar_c_mev_fm**4)*1e-12
    check('E2 units independently derived', 12.24 < coeff < 12.26)
    ce = {}
    for mass, e2, e4, tau2, s2, tau4, s4 in [(130,254,456,181.3,7.0,7.65,.31),(132,325,533,70.1,3.2,3.9,1.0)]:
        b2 = 1/(coeff*(e2/1000)**5*tau2)
        b4 = 1/(coeff*(e4/1000)**5*tau4)
        ratio = b4/b2
        relative = [math.sqrt((s2/tau2)**2+(s4/tau4)**2-2*rho*(s2/tau2)*(s4/tau4)) for rho in [-1,0,1]]
        ce[str(mass)] = {'printed_E_keV': [e2,e4], 'mean_tau_ps': [tau2,tau4],
                         'B_down_e2b2_if_photon_branch_one': [b2,b4], 'B42_same_control': ratio,
                         'linearized_ratio_se_at_rho_minus1_0_plus1': [ratio*v for v in relative],
                         'boundary': 'Photon-branch-one/pure-E2 calculation, not the adopted source strength. ICC, precise energies, branches and joint covariance not reconstructed. No experimental sigma rejection or gamma-soft classification.'}

    # Same parent ratios cancel total lifetime; assumed pure M1 numerator.
    d4 = []
    for spin, parent, em, im, ee, ie in [(16,4210.8,273.6,7.0,481.0,.4),(17,4581.6,370.8,8.1,644.1,.8),(18,4990.9,409.3,4.9,780.3,1.0),(19,5430.9,440.0,3.7,849.4,1.0),(20,5934.5,503.6,1.8,943.8,.6),(21,6444.8,510.3,1.0,1014.2,.5),(22,6974.9,530.1,.5,1040.0,.2),(23,7562.3,587.4,.2,1117.9,.2)]:
        # Standard rate ratio coefficient, a stated conventional approximation.
        ratio = .697*(ee/1000)**5/(em/1000)**3*im/ie
        d4.append({'spin': spin, 'parent_keV': parent, 'M1_candidate_E_keV': em,
                   'I_gamma_candidate': im, 'E2_candidate_E_keV': ee, 'I_gamma_E2': ie,
                   'ratio_if_delta_zero_and_crossover_pure_E2': ratio})
    check('D4 assumed-purity central ratios are not monotone', any(d4[i+1]['ratio_if_delta_zero_and_crossover_pure_E2'] > d4[i]['ratio_if_delta_zero_and_crossover_pure_E2'] for i in range(7)))
    result = {'checkpoint': '032', 'kind': 'source corrections and explicit mathematical controls',
              'experimental_fit_or_CI': False, 'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'regression': bands, 'E2_coefficient_per_ps': coeff, 'Klemme_TableIII_conditional': ce,
              'Lv_TableI_D4_conditional': d4,
              'D4_boundary': 'No plot digitization. Table M blank at 481/370.8/587.4/1117.9; spin23 tentative. M1+E2 entries require delta; ratios above assume delta=0 and are not author values or absolute B. No measured shears angles or mode exclusion.',
              'Petrache2006': {'literal_spins': [15,16], 'literal_gap_keV': [36,44],
                               'V_odd_even_keV': [14,17], 'Q_ratio_allowed_range': [1.6,2.4],
                               'Gaussian_sigma_or_p': None, 'boundary': 'Allowed parameter range, not a specified Gaussian sampling error. Table I amplitudes .894 at15y and .427 at16ny have branch/sign identity; arcsin returns only one branch.'},
              'controls': controls, 'interpretation': 'Controls validate only the declared algebra. Scientific support comes from read original locators; no global science certification.'}
    target = args.run_dir / 'evidence-repair-result-032.json'
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'result': str(target), 'controls': len(controls), 'experimental_fit_or_CI': False}))


if __name__ == '__main__':
    main()
