#!/usr/bin/env python3
"""Chosen DAY13 on/off spectra with a shared background normalization.

Two disjoint on streams have independent Poisson counts. One independent off
count is reused for both spectra; a known background shape is assumed. Local
GLS/Fisher and linear-estimator Monte Carlo checks are not nonlinear data
fits, confidence intervals or an experimental sideband implementation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.special import ndtr

import day13_finite_bin_lineshape as bins


SIGNAL_COUNT_PER_GROUP = 10000.0
BACKGROUND_COUNT_PER_GROUP = 4000.0
ANGLES = (150.0, 170.0)
EDGES = bins.TRUE_E_KEV + np.linspace(-100.0, 10.0, 23)


def signal(e0, tau):
    return [bins.conditional(bins.raw_bin_probabilities(EDGES, e0, tau, a))[0]
            for a in ANGLES]


def design_matrix():
    p = signal(bins.TRUE_E_KEV, bins.TRUE_TAU_PS)
    derivative = []
    for coordinate in (0, 1):
        step = 1e-4
        pair = []
        for sign in (-1, 1):
            tau = bins.TRUE_TAU_PS * math.exp(sign*step) if coordinate == 0 else bins.TRUE_TAU_PS
            e0 = bins.TRUE_E_KEV + sign*step if coordinate == 1 else bins.TRUE_E_KEV
            pair.append(np.concatenate(signal(e0, tau)))
        derivative.append(SIGNAL_COUNT_PER_GROUP*(pair[1]-pair[0])/(2*step))
    matrix = np.zeros((2*(len(EDGES)-1), 4))
    matrix[:, :2] = np.column_stack(derivative)
    for g, probability in enumerate(p):
        matrix[g*len(probability):(g+1)*len(probability), 2+g] = SIGNAL_COUNT_PER_GROUP*probability
    return p, matrix


def linear_gls(matrix, covariance):
    solved = np.linalg.solve(covariance, matrix)
    fisher = matrix.T @ solved
    parameter_covariance = np.linalg.inv(fisher)
    operator = parameter_covariance @ solved.T
    assert np.max(np.abs(operator @ matrix-np.eye(matrix.shape[1]))) < 1e-8
    return parameter_covariance, operator


def summarize_covariance(covariance):
    return dict(local_tau_SE_fs=1000*bins.TRUE_TAU_PS*math.sqrt(covariance[0, 0]),
                local_energy_SE_keV=math.sqrt(covariance[1, 1]),
                log_signal_normalization_SE=[math.sqrt(covariance[i, i]) for i in (2, 3)],
                tau_energy_correlation=float(covariance[0, 1]/math.sqrt(
                    covariance[0, 0]*covariance[1, 1])))


def calculate():
    p, matrix = design_matrix()
    # Chosen, exactly known smooth background; not a measured source template.
    center, sigma = bins.TRUE_E_KEV-50.0, 20.0
    shaped = ndtr((EDGES[1:]-center)/sigma)-ndtr((EDGES[:-1]-center)/sigma)
    q = 0.2/len(shaped) + 0.8*shaped/shaped.sum()
    shared_shape = np.tile(q, len(ANGLES))
    mu = SIGNAL_COUNT_PER_GROUP*np.concatenate(p) + BACKGROUND_COUNT_PER_GROUP*shared_shape
    on_covariance = np.diag(mu)
    scenarios = []
    exact_equivalence_error = 0.0
    for exposure in (0.25, 1.0, 4.0, 1e8):
        variance_background = BACKGROUND_COUNT_PER_GROUP/exposure
        full = on_covariance + variance_background*np.outer(shared_shape, shared_shape)
        diagonal_only = np.diag(np.diag(full))
        parameter_covariance, optimal = linear_gls(matrix, full)
        naive_reported, naive_operator = linear_gls(matrix, diagonal_only)
        naive_actual = naive_operator @ full @ naive_operator.T
        # Independent derivation: profile B in the joint on/off Poisson Fisher.
        inverse_on = np.diag(1/mu)
        cross = matrix.T @ inverse_on @ shared_shape
        background_information = float(shared_shape @ inverse_on @ shared_shape
                                       + exposure/BACKGROUND_COUNT_PER_GROUP)
        profiled_fisher = (matrix.T @ inverse_on @ matrix
                           - np.outer(cross, cross)/background_information)
        from_joint = np.linalg.inv(profiled_fisher)
        difference = float(np.max(np.abs(from_joint-parameter_covariance)))
        exact_equivalence_error = max(exact_equivalence_error, difference)
        assert difference < 1e-10
        assert np.linalg.eigvalsh(full).min() > 0
        scenarios.append(dict(off_to_on_exposure=exposure,
                              expected_off_count=exposure*BACKGROUND_COUNT_PER_GROUP,
                              background_estimate_variance=variance_background,
                              full_covariance=summarize_covariance(parameter_covariance),
                              diagonal_only_reported=summarize_covariance(naive_reported),
                              diagonal_only_actual=summarize_covariance(naive_actual),
                              naive_actual_to_reported_variance_ratio=(
                                  np.diag(naive_actual)/np.diag(naive_reported)).tolist(),
                              joint_Poisson_profile_covariance_max_difference=difference))
    # Infinite off exposure removes this shared uncertainty, not on-count noise.
    limiting, _ = linear_gls(matrix, on_covariance)
    assert abs(scenarios[-1]["full_covariance"]["local_tau_SE_fs"]
               - summarize_covariance(limiting)["local_tau_SE_fs"]) < 1e-7

    exposure = 0.25
    full = on_covariance + BACKGROUND_COUNT_PER_GROUP/exposure*np.outer(shared_shape, shared_shape)
    parameter_covariance, optimal = linear_gls(matrix, full)
    naive_reported, naive = linear_gls(matrix, np.diag(np.diag(full)))
    naive_actual = naive @ full @ naive.T
    rng = np.random.default_rng(131426)
    repeats = 120000
    on = rng.poisson(mu, (repeats, len(mu)))
    off = rng.poisson(exposure*BACKGROUND_COUNT_PER_GROUP, repeats)
    residual = on-mu-(off/exposure-BACKGROUND_COUNT_PER_GROUP)[:, None]*shared_shape
    estimated = residual @ optimal.T
    estimated_naive = residual @ naive.T
    empirical = np.cov(estimated, rowvar=False)
    empirical_naive = np.cov(estimated_naive, rowvar=False)
    diagonal_relative_error = float(np.max(np.abs(
        np.diag(empirical)/np.diag(parameter_covariance)-1)))
    naive_relative_error = float(np.max(np.abs(
        np.diag(empirical_naive)/np.diag(naive_actual)-1)))
    assert diagonal_relative_error < 0.025 and naive_relative_error < 0.025
    assert np.max(np.abs(estimated.mean(axis=0))/np.sqrt(
        np.diag(parameter_covariance)/repeats)) < 5
    # Cross-group same-bin covariance has no on-stream overlap here.
    index = int(np.argmax(q))
    partner = len(q)+index
    measured_cross = float(np.cov(residual[:, [index, partner]], rowvar=False)[0, 1])
    expected_cross = float(full[index, partner])
    assert abs(measured_cross-expected_cross)/expected_cross < 0.05
    subtracted = on - (off/exposure)[:, None]*shared_shape
    negative_fraction = float(np.mean(subtracted < 0))
    assert negative_fraction > 0

    # Covariance can reduce a contrast's error; dropping cross terms has no
    # universal sign. A common scalar cancels from two equal responses.
    v, common = 100.0, 400.0
    pair_covariance = np.array([[v+common, common], [common, v+common]])
    difference_vector = np.array([1.0, -1.0])
    sum_vector = np.array([1.0, 1.0])
    assert difference_vector @ pair_covariance @ difference_vector == 2*v
    assert sum_vector @ pair_covariance @ sum_vector == 2*v+4*common

    return dict(schema_version=1, kind="synthetic shared-sideband normalization covariance",
                source_inspiration="BC84 counting-model/likelihood boundary; covariance is our derivation",
                chosen_parameters=dict(signal_mean_per_angle=SIGNAL_COUNT_PER_GROUP,
                                       background_mean_per_angle=BACKGROUND_COUNT_PER_GROUP,
                                       angles_deg=list(ANGLES), bin_edges_keV=EDGES.tolist(),
                                       background_bin_probabilities=q.tolist(),
                                       parameter_coordinates=["log_tau", "energy_shift_keV",
                                                              "log_signal_150", "log_signal_170"]),
                scenarios=scenarios,
                independent_count_MC=dict(seed=131426, repeats=repeats,
                                           off_exposure=exposure,
                                           empirical_optimal=summarize_covariance(empirical),
                                           empirical_naive=summarize_covariance(empirical_naive),
                                           shared_bin_indices=[index, partner],
                                           shared_bin_cross_covariance_expected=expected_cross,
                                           shared_bin_cross_covariance_MC=measured_cross,
                                           negative_subtracted_bin_fraction=negative_fraction),
                contrast_control=dict(independent_variance=v, shared_variance=common,
                                      full_difference_variance=2*v,
                                      diagonal_difference_variance=2*(v+common),
                                      full_sum_variance=2*v+4*common,
                                      diagonal_sum_variance=2*(v+common)),
                verification=dict(joint_Poisson_profile_GLS_max_covariance_difference=exact_equivalence_error,
                                  MC_optimal_max_variance_relative_error=diagonal_relative_error,
                                  MC_naive_sandwich_max_variance_relative_error=naive_relative_error,
                                  shared_off_cross_covariance_passed=True,
                                  infinite_off_exposure_limit_passed=True,
                                  contrast_cancellation_passed=True,
                                  all_passed=True),
                dependencies=dict(binning_script_sha256=hashlib.sha256(
                    Path(bins.__file__).read_bytes()).hexdigest()),
                boundaries=["On streams are disjoint and independent; overlapping gamma gates need their extra covariance.",
                            "One off count measures B with known transfer/exposure and known background shape.",
                            "Background-shape uncertainty, template statistics and calibration covariance are omitted.",
                            "Signal normalizations are nuisance parameters; local Fisher/GLS does not establish nonlinear interval coverage.",
                            "MC applies fixed linear estimators at the true model, not a full likelihood refit.",
                            "The sign of a neglected correlation's effect depends on the fitted contrast."])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"verification": result["verification"],
                      "scenarios": result["scenarios"],
                      "count_MC": result["independent_count_MC"]}))


if __name__ == "__main__":
    main()
