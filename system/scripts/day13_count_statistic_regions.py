#!/usr/bin/env python3
"""Synthetic count-statistic and joint-region checks for DAY13 line shapes.

The uniform Poisson-rate model has closed-form minimizers. It is deliberately
not a lifetime line-shape model. Gaussian two-parameter regions are a separate
regular control model, not a conversion of published lifetime uncertainties.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def calculate():
    rng = np.random.default_rng(131410)
    repetitions, bins = 200000, 32
    rate_cases = []
    for rate in (50.0, 100.0, 200.0):
        n = rng.poisson(rate, (repetitions, bins)).astype(float)
        assert np.min(n) >= 10  # This particular counterexample satisfies the count rule.
        neyman = bins / np.sum(1/n, axis=1)
        pearson = np.sqrt(np.mean(n*n, axis=1))
        poisson = np.mean(n, axis=1)
        rate_cases.append(dict(chosen_true_rate_per_bin=rate, actual_minimum_observed_bin=int(n.min()),
                               all_observed_bins_at_least10=True,
                               estimators=[dict(name=name, mean=float(values.mean()),
                                                bias=float(values.mean()-rate),
                                                mean_MC_standard_error=float(values.std()/math.sqrt(repetitions)),
                                                relative_bias=float(values.mean()/rate-1))
                                           for name, values in [('Neyman harmonic mean', neyman),
                                                                ('Pearson RMS', pearson),
                                                                ('Poisson arithmetic mean', poisson)]]))
        # Independently substitute the closed-form estimators into score equations.
        assert np.max(np.abs(neyman*np.sum(1/n,axis=1)-bins)) < 1e-12
        assert np.max(np.abs(np.sum(n*n,axis=1)/pearson**2-bins)) < 1e-12
        assert np.max(np.abs(np.sum(n,axis=1)/poisson-bins)) < 1e-12
        se = math.sqrt(rate/(bins*repetitions))
        assert abs(poisson.mean()-rate) < 5*se
        assert neyman.mean() < rate and pearson.mean() > rate

    # Correlated regular Gaussian control model in coordinates (tau, energy).
    sigma_tau_fs, sigma_E_keV, rho = 10.0, 0.4, -0.8
    cov = np.array([[sigma_tau_fs**2, rho*sigma_tau_fs*sigma_E_keV],
                    [rho*sigma_tau_fs*sigma_E_keV, sigma_E_keV**2]])
    draws = rng.multivariate_normal([0.0,0.0], cov, 1000000)
    inv = np.linalg.inv(cov)
    joint_q = np.einsum('ni,ij,nj->n', draws, inv, draws)
    tau_z2 = (draws[:,0]/sigma_tau_fs)**2
    diagonal_q = tau_z2+(draws[:,1]/sigma_E_keV)**2
    region_cases = []
    for threshold in (1.0, 2.3, -2*math.log(0.2), 4.6):
        joint_expected = 1-math.exp(-threshold/2)
        projected_expected = math.erf(math.sqrt(threshold/2))
        joint_mc = float(np.mean(joint_q <= threshold))
        projected_mc = float(np.mean(tau_z2 <= threshold))
        assert abs(joint_mc-joint_expected) < 0.002
        assert abs(projected_mc-projected_expected) < 0.002
        region_cases.append(dict(chosen_delta_q=threshold,
                                 joint_two_parameter_probability=joint_expected,
                                 joint_MC_probability=joint_mc,
                                 projected_tau_probability=projected_expected,
                                 projected_tau_MC_probability=projected_mc,
                                 wrong_diagonal_metric_MC_probability=float(np.mean(diagonal_q<=threshold))))
    # Profile out the energy coordinate; q_profile(tau)=tau^2/sigma_tau^2.
    e_profile = rho*sigma_E_keV/sigma_tau_fs*draws[:,0]
    profiled = np.column_stack([draws[:,0],e_profile])
    q_profile = np.einsum('ni,ij,nj->n',profiled,inv,profiled)
    assert np.max(np.abs(q_profile-tau_z2)) < 1e-11
    return dict(schema_version=1,
                kind='synthetic uniform count fit and regular Gaussian joint-region exercise',
                source_motivation='ZA23-10 and CM21-17; own derivations, not source fit rerun',
                chosen_uniform_rate_model=dict(repetitions=repetitions, bins=bins,
                                               expected_same_Poisson_mean_per_bin=True),
                rate_cases=rate_cases,
                chosen_Gaussian_region_model=dict(tau_sigma_fs=sigma_tau_fs,
                                                  energy_sigma_keV=sigma_E_keV,
                                                  correlation=rho, covariance=cov.tolist(),
                                                  repetitions=len(draws)),
                region_cases=region_cases,
                verification=dict(closed_form_score_equations_passed=True,
                                  unbiased_Poisson_MC_mean_passed=True,
                                  all_count_examples_observed_atleast10=True,
                                  joint_and_projection_MC_vs_analytic_passed=True,
                                  energy_profile_identity_passed=True,
                                  all_passed=True),
                boundaries=['Uniform-rate normalization bias does not establish a bias in lifetime or transition energy.',
                            'Count examples show >=10 alone does not guarantee an unbiased estimator; source did not claim a theorem.',
                            'No data-dependent rebinning, background subtraction or finite-template uncertainty is simulated.',
                            'Gaussian regular controls do not convert published intervals or prove their coverage.',
                            'Actual histogram, normalization/background/response covariance and chi-square templates remain missing.'],
                numpy_version=np.__version__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output), 'verification':result['verification'],
                      'rates':result['rate_cases'],'regions':result['region_cases']}))


if __name__ == '__main__':
    main()
