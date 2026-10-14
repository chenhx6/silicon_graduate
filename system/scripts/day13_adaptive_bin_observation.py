#!/usr/bin/env python3
"""Chosen DAY13 observed bin boundaries and informative adaptive coarsening.

Each independent histogram has N=40 photons in two bins with probability p.
Retain two bins iff both have >=10 counts, otherwise merge into one. Treating
the reported boundary as fixed discards a parameter-dependent observation.
This abstract shape parameter is not a Doppler lifetime or a source rule.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import binom


PHOTONS_PER_HISTOGRAM = 40
MIN_COUNTS = 10
TRUE_P = 0.25
HISTOGRAMS_PER_EXPERIMENT = 64


def retained_probability(p):
    return float(binom.cdf(PHOTONS_PER_HISTOGRAM-MIN_COUNTS,
                          PHOTONS_PER_HISTOGRAM, p)
                 - binom.cdf(MIN_COUNTS-1, PHOTONS_PER_HISTOGRAM, p))


def merged_probability(p):
    return float(binom.cdf(MIN_COUNTS-1, PHOTONS_PER_HISTOGRAM, p)
                 + binom.sf(PHOTONS_PER_HISTOGRAM-MIN_COUNTS,
                            PHOTONS_PER_HISTOGRAM, p))


def negative_log_likelihood(p, retained_groups, retained_first_counts,
                            total_groups=HISTOGRAMS_PER_EXPERIMENT):
    first = retained_first_counts
    second = PHOTONS_PER_HISTOGRAM*retained_groups-first
    # The binomial combinatorial factor for kept X is p-independent.
    return -(first*math.log(p)+second*math.log1p(-p)
             +(total_groups-retained_groups)*math.log(merged_probability(p)))


def correct_fit(retained_groups, retained_first_counts):
    result = minimize_scalar(lambda p: negative_log_likelihood(
        p, retained_groups, retained_first_counts), bounds=(0.02, 0.98),
        method="bounded", options={"xatol": 1e-12})
    assert result.success
    return float(result.x)


def summarize(values, truth=TRUE_P):
    return dict(mean=float(values.mean()), bias=float(values.mean()-truth),
                standard_deviation=float(values.std(ddof=1)),
                mean_standard_error=float(values.std(ddof=1)/math.sqrt(len(values))),
                minimum=float(values.min()), maximum=float(values.max()))


def calculate():
    n, k, p = PHOTONS_PER_HISTOGRAM, MIN_COUNTS, TRUE_P
    retained = retained_probability(p)
    # E[X 1{k<=X<=N-k}] = Np P(k-1<=Bin(N-1,p)<=N-k-1).
    expected_first_keep = n*p*float(binom.cdf(n-k-1, n-1, p)-binom.cdf(k-2, n-1, p))
    asymptotic_naive_p = expected_first_keep/(n*retained)
    assert asymptotic_naive_p > p
    assert abs(retained+merged_probability(p)-1) < 1e-12
    # Normalize every possible output: individual kept counts plus the merged
    # marker. The merged output is an event, not merely a p-independent bin.
    normalized = sum(float(binom.pmf(x, n, p)) for x in range(k, n-k+1)) + merged_probability(p)
    assert abs(normalized-1) < 1e-12
    expected_groups = HISTOGRAMS_PER_EXPERIMENT*retained
    expected_first = HISTOGRAMS_PER_EXPERIMENT*expected_first_keep
    expected_fit = minimize_scalar(lambda value: negative_log_likelihood(
        value, expected_groups, expected_first), bounds=(0.02, 0.98),
        method="bounded", options={"xatol": 1e-13})
    assert expected_fit.success and abs(expected_fit.x-p) < 1e-7

    rng = np.random.default_rng(131429)
    repeats = 8000
    raw_first = rng.binomial(n, p, (repeats, HISTOGRAMS_PER_EXPERIMENT))
    keep = (raw_first >= k) & (raw_first <= n-k)
    number_keep = keep.sum(axis=1)
    first_keep = np.where(keep, raw_first, 0).sum(axis=1)
    assert np.min(number_keep) > 0
    # Every reported main-exercise bin has >=10 counts by construction.
    assert np.min(raw_first[keep]) >= k and np.min((n-raw_first)[keep]) >= k
    assert n >= k
    naive = first_keep/(n*number_keep)
    oracle = raw_first.sum(axis=1)/(n*HISTOGRAMS_PER_EXPERIMENT)
    # Cache integer sufficient summaries; each objective includes the merge
    # event's probability. Keep a coarse-grid comparison as an optimizer check.
    frequency = Counter(zip(number_keep.tolist(), first_keep.tolist()))
    fits = {}
    grid = np.linspace(0.02, 0.98, 97)
    max_grid_disadvantage = 0.0
    for kept_count, first_sum in frequency:
        fitted = correct_fit(kept_count, first_sum)
        objective = negative_log_likelihood(fitted, kept_count, first_sum)
        grid_best = min(negative_log_likelihood(value, kept_count, first_sum) for value in grid)
        max_grid_disadvantage = max(max_grid_disadvantage, objective-grid_best)
        assert objective <= grid_best+1e-7
        fits[(kept_count, first_sum)] = fitted
    correct = np.array([fits[(int(a), int(b))] for a, b in zip(number_keep, first_keep)])

    # An independent pilot chooses keep/merge; its selection is independent of
    # the science counts, so kept science proportions are not truncated.
    pilot_first = rng.binomial(n, p, raw_first.shape)
    pilot_keep = (pilot_first >= k) & (pilot_first <= n-k)
    science_first = rng.binomial(n, p, raw_first.shape)
    pilot_number_keep = pilot_keep.sum(axis=1)
    assert np.min(pilot_number_keep) > 0
    independent_pilot = np.where(pilot_keep, science_first, 0).sum(axis=1)/(
        n*pilot_number_keep)
    correct_summary = summarize(correct)
    naive_summary = summarize(naive)
    oracle_summary = summarize(oracle)
    pilot_summary = summarize(independent_pilot)
    assert abs(correct_summary["bias"]) < 0.003
    assert abs(naive_summary["mean"]-asymptotic_naive_p) < 0.002
    assert abs(pilot_summary["bias"]) < 5*pilot_summary["mean_standard_error"]
    assert abs(oracle_summary["bias"]) < 5*oracle_summary["mean_standard_error"]
    # Symmetry is a counter-control: this particular naive bias is zero at .5.
    retained_half = retained_probability(0.5)
    mean_half = 0.5*float(binom.cdf(n-k-1, n-1, 0.5)-binom.cdf(k-2, n-1, 0.5))/retained_half
    assert abs(mean_half-0.5) < 1e-12

    return dict(schema_version=1, kind="synthetic informative adaptive histogram boundary",
                source_inspiration="BC84 counting likelihood/finiteN; no source adaptive algorithm reproduced",
                chosen_parameters=dict(fixed_photons_per_histogram=n, first_bin_probability=p,
                                       minimum_reported_count=k,
                                       independent_histograms_per_experiment=HISTOGRAMS_PER_EXPERIMENT,
                                       repeats=repeats, seed=131429,
                                       fit_bounds=[0.02, 0.98],
                                       rule="retain two bins if10<=X<=30; otherwise merge all40 photons"),
                exact_expected_results=dict(retained_probability=retained,
                                            merged_probability=merged_probability(p),
                                            asymptotic_naive_p=asymptotic_naive_p,
                                            expected_complete_observation_fit_p=float(expected_fit.x),
                                            normalized_observation_probability=normalized),
                Monte_Carlo=dict(naive_fixed_boundary_likelihood=naive_summary,
                                  complete_observation_likelihood=correct_summary,
                                  uncoarsened_oracle=oracle_summary,
                                  independent_pilot_boundary=pilot_summary,
                                  mean_retained_histograms=float(number_keep.mean()),
                                  unique_integer_summaries=len(frequency)),
                verification=dict(all_reported_main_bins_at_least10=True,
                                  merged_event_likelihood_normalized=True,
                                  expected_complete_likelihood_recovers_truth=True,
                                  coarse_grid_optimum_check_max_disadvantage=max_grid_disadvantage,
                                  independent_pilot_bias_control_passed=True,
                                  symmetric_p_half_zero_naive_bias_passed=True,
                                  all_passed=True),
                boundaries=["This rule coarsens each independent fixed40-photon histogram; actual source rebinning is unknown.",
                            "p is an abstract shape fraction, not tau, isotope population or experimental branching ratio.",
                            "The complete likelihood includes all kept counts and the merge decision; it does not condition away the selection rate.",
                            "Independent-pilot bin choice does not guarantee>=10 science counts; its control tests independence only.",
                            "Correct likelihood is not claimed exactly unbiased for finite64 groups or to have verified interval coverage.",
                            "Optimizer flags/coarse-grid checks do not prove a globally unique maximum for arbitrary inputs."])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"verification": result["verification"],
                      "exact": result["exact_expected_results"],
                      "MC": result["Monte_Carlo"]}))


if __name__ == "__main__":
    main()
