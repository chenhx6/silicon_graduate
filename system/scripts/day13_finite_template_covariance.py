#!/usr/bin/env python3
"""Synthetic DAY13 finite weighted templates and shared simulation events.

Uses independent proper-time, entry-feeding and Gaussian-response variates.
Reusing them at two lifetime hypotheses couples the normalized templates.
Ratio-estimator covariance is a leading 1/N calculation, checked against
finite template ensembles. No experimental template bank or Barlow-Beeston
implementation is reproduced.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

import day13_finite_bin_lineshape as bins


ANGLE_DEG = 150.0
EDGES = bins.make_edges(5.0)
K = len(EDGES)-1
TAU_A_PS = 0.070
TAU_B_PS = 0.072


def base_variates(rng, shape):
    # The same base variables will be reused at both parameter hypotheses.
    return (rng.exponential(1.0, shape),
            rng.random(shape) < bins.KNOWN_ENTRY_FEED_FRACTION,
            rng.exponential(bins.history.TAU3_PS, shape),
            rng.normal(0.0, bins.SIGMA_KEV, shape))


def generated_observation(base, tau):
    direct_unit, feed, upper_wait, noise = base
    time = tau*direct_unit+feed*upper_wait
    beta = bins.history.BETA_IN+(bins.history.BETA_EXIT-bins.history.BETA_IN)*np.minimum(
        time/bins.history.T_EXIT_PS, 1.0)
    cosine = math.cos(math.radians(ANGLE_DEG))
    d = (1-beta*cosine)/np.sqrt(1-beta**2)
    d_exit = (1-bins.history.BETA_EXIT*cosine)/math.sqrt(1-bins.history.BETA_EXIT**2)
    energy = bins.TRUE_E_KEV*d_exit/d+noise
    index = np.searchsorted(EDGES, energy, side="right")-1
    selected = (index >= 0) & (index < K)
    weight = np.where(selected, 1/d**2, 0.0)
    return index, weight


def single_event_covariance(index, weight):
    n = len(index)
    selected = weight > 0
    mean_weight = float(weight.mean())
    r = np.bincount(index[selected], weights=weight[selected], minlength=K)/n
    q = r/mean_weight
    v = np.bincount(index[selected], weights=weight[selected]**2, minlength=K)/n
    moment = (np.diag(v)-np.outer(v, q)-np.outer(q, v)
              + float(v.sum())*np.outer(q, q))/mean_weight**2
    assert abs(float(q.sum())-1) < 1e-12
    assert np.max(np.abs(moment.sum(axis=0))) < 1e-12
    assert np.linalg.eigvalsh(moment).min() > -1e-12
    return q, moment, mean_weight


def cross_event_covariance(index_a, weight_a, index_b, weight_b, qa, qb):
    both = (weight_a > 0) & (weight_b > 0)
    joint_index = K*index_a[both]+index_b[both]
    joint = np.bincount(joint_index,
                        weights=weight_a[both]*weight_b[both], minlength=K*K)
    joint = joint.reshape(K, K)/len(index_a)
    row, column = joint.sum(axis=1), joint.sum(axis=0)
    covariance = (joint-np.outer(row, qb)-np.outer(qa, column)
                  + float(joint.sum())*np.outer(qa, qb)) / (
                      weight_a.mean()*weight_b.mean())
    assert np.max(np.abs(covariance.sum(axis=0))) < 1e-12
    assert np.max(np.abs(covariance.sum(axis=1))) < 1e-12
    return covariance


def ensemble_probabilities(index, weight):
    repeats, count = index.shape
    selected = weight > 0
    row_index = np.broadcast_to(np.arange(repeats)[:, None], index.shape)
    joint = row_index[selected]*K+index[selected]
    numerator = np.bincount(joint, weights=weight[selected], minlength=repeats*K)
    numerator = numerator.reshape(repeats, K)
    denominator = weight.sum(axis=1)
    assert np.min(denominator) > 0
    q = numerator/denominator[:, None]
    assert np.max(np.abs(q.sum(axis=1)-1)) < 1e-12
    return q


def calculate():
    rng = np.random.default_rng(131427)
    pilot_count = 800000
    base = base_variates(rng, pilot_count)
    ia, wa = generated_observation(base, TAU_A_PS)
    ib, wb = generated_observation(base, TAU_B_PS)
    qa, va, mean_wa = single_event_covariance(ia, wa)
    qb, vb, mean_wb = single_event_covariance(ib, wb)
    cab = cross_event_covariance(ia, wa, ib, wb, qa, qb)
    shared_difference = va+vb-cab-cab.T
    independent_difference = va+vb
    assert np.linalg.eigvalsh(shared_difference).min() > -1e-12
    caa = cross_event_covariance(ia, wa, ia, wa, qa, qa)
    same_hypothesis_difference = 2*va-caa-caa.T
    assert np.max(np.abs(same_hypothesis_difference)) < 1e-12

    # An unweighted template with fixed accepted N has multinomial covariance.
    # At fixed generated N with ROI loss, account for the acceptance fraction.
    unit_weight = (wa > 0).astype(float)
    unit_q, unit_v, _ = single_event_covariance(ia, unit_weight)
    accepted_fraction = float(unit_weight.mean())
    assert np.max(np.abs(unit_v*accepted_fraction-(
        np.diag(unit_q)-np.outer(unit_q, unit_q)))) < 1e-12

    analytic_a, _ = bins.conditional(bins.raw_bin_probabilities(
        EDGES, bins.TRUE_E_KEV, TAU_A_PS, ANGLE_DEG))
    analytic_b, _ = bins.conditional(bins.raw_bin_probabilities(
        EDGES, bins.TRUE_E_KEV, TAU_B_PS, ANGLE_DEG))
    pilot_valid = np.diag(va) > 1e-5
    assert np.max(np.abs(qa[pilot_valid]-analytic_a[pilot_valid])/np.sqrt(
        np.diag(va)[pilot_valid]/pilot_count)) < 5

    # Independent template ensembles, with common events within each bank.
    repeats, template_count, batch_size = 8000, 2000, 100
    ensemble_rng = np.random.default_rng(131428)
    samples_a, samples_b, independent_b = [], [], []
    for start in range(0, repeats, batch_size):
        size = min(batch_size, repeats-start)
        shared_base = base_variates(ensemble_rng, (size, template_count))
        xa, ya = generated_observation(shared_base, TAU_A_PS)
        xb, yb = generated_observation(shared_base, TAU_B_PS)
        samples_a.append(ensemble_probabilities(xa, ya))
        samples_b.append(ensemble_probabilities(xb, yb))
        separate_base = base_variates(ensemble_rng, (size, template_count))
        xi, yi = generated_observation(separate_base, TAU_B_PS)
        independent_b.append(ensemble_probabilities(xi, yi))
    samples_a = np.concatenate(samples_a)
    samples_b = np.concatenate(samples_b)
    independent_b = np.concatenate(independent_b)
    empirical_a = np.cov(samples_a, rowvar=False)
    empirical_b = np.cov(samples_b, rowvar=False)
    empirical_difference = np.cov(samples_b-samples_a, rowvar=False)
    empirical_independent = np.cov(independent_b-samples_a, rowvar=False)
    expected = [va/template_count, vb/template_count,
                shared_difference/template_count, independent_difference/template_count]
    empirical = [empirical_a, empirical_b, empirical_difference, empirical_independent]
    errors = [float(np.linalg.norm(m-e)/np.linalg.norm(e))
              for m, e in zip(empirical, expected)]
    assert max(errors) < 0.10
    empirical_trace_ratio = float(np.trace(empirical_difference)/np.trace(empirical_independent))
    predicted_trace_ratio = float(np.trace(shared_difference)/np.trace(independent_difference))
    assert abs(empirical_trace_ratio/predicted_trace_ratio-1) < 0.06
    assert predicted_trace_ratio < 1

    # Finite templates add uncertainty to an independently sampled fixed-N data
    # histogram. Project onto a local lifetime-sensitive score, avoiding the
    # singular normalization direction of both probability covariance matrices.
    step = 1e-4
    lower, _ = bins.conditional(bins.raw_bin_probabilities(
        EDGES, bins.TRUE_E_KEV, TAU_A_PS*math.exp(-step), ANGLE_DEG))
    upper, _ = bins.conditional(bins.raw_bin_probabilities(
        EDGES, bins.TRUE_E_KEV, TAU_A_PS*math.exp(step), ANGLE_DEG))
    derivative = (upper-lower)/(2*step)
    score = np.zeros(K)
    valid = analytic_a > 1e-12
    score[valid] = derivative[valid]/analytic_a[valid]
    data_count = 10000
    data_covariance = data_count*(np.diag(analytic_a)-np.outer(analytic_a, analytic_a))
    data_variance = float(score @ data_covariance @ score)
    inflation = []
    for n in (1000, 2000, 10000, 100000, 10**12):
        template_variance = data_count**2*float(score @ va @ score)/n
        inflation.append(dict(chosen_template_count=n,
                              data_projection_variance=data_variance,
                              template_projection_variance=template_variance,
                              SD_inflation=math.sqrt(1+template_variance/data_variance)))
    assert abs(inflation[-1]["SD_inflation"]-1) < 1e-7

    peak_index = int(np.argmax(analytic_a))
    return dict(schema_version=1, kind="synthetic normalized weighted finite-template covariance",
                source_inspiration="BC84 finite-bin/counting boundary; all covariance derivations are our inference",
                chosen_parameters=dict(angle_deg=ANGLE_DEG, bin_edges_keV=EDGES.tolist(),
                                       lifetime_hypotheses_ps=[TAU_A_PS, TAU_B_PS],
                                       rest_energy_keV=bins.TRUE_E_KEV,
                                       entry_feeding_fraction=bins.KNOWN_ENTRY_FEED_FRACTION,
                                       templates_share=["unit exponential direct wait", "entry feed tag",
                                                        "upper wait", "Gaussian response noise"],
                                       pilot_count=pilot_count, pilot_seed=131427,
                                       ensemble_repeats=repeats, ensemble_template_count=template_count,
                                       ensemble_seed=131428),
                template_probabilities=dict(analytic_a=analytic_a.tolist(), analytic_b=analytic_b.tolist(),
                                            pilot_a=qa.tolist(), pilot_b=qb.tolist()),
                covariance_diagnostics=dict(shared_difference_to_independent_trace_ratio=predicted_trace_ratio,
                                            empirical_trace_ratio=empirical_trace_ratio,
                                            peak_bin_index=peak_index,
                                            peak_probability=float(analytic_a[peak_index]),
                                            peak_template_SE_a=math.sqrt(va[peak_index, peak_index]/template_count),
                                            same_hypothesis_difference_max_covariance=float(
                                                np.max(np.abs(same_hypothesis_difference))),
                                            normalized_covariance_row_sum_max=float(
                                                np.max(np.abs(va.sum(axis=0)))),
                                            pilot_mean_weights=[mean_wa, mean_wb],
                                            expected_shared_difference_variance=np.diag(
                                                shared_difference/template_count).tolist(),
                                            expected_independent_difference_variance=np.diag(
                                                independent_difference/template_count).tolist()),
                data_template_projection_inflation=inflation,
                verification=dict(ensemble_covariance_Frobenius_relative_errors=errors,
                                  common_event_contrast_covariance_passed=True,
                                  fixed_accepted_N_multinomial_identity_passed=True,
                                  normalization_null_direction_passed=True,
                                  same_hypothesis_common_event_zero_difference_passed=True,
                                  independent_template_control_passed=True,
                                  infinite_template_limit_passed=True,
                                  all_passed=True),
                dependencies=dict(binning_script_sha256=hashlib.sha256(
                    Path(bins.__file__).read_bytes()).hexdigest()),
                boundaries=["Normalized weighted probabilities have leading 1/N ratio-estimator covariance, not exact finite-N unbiasedness.",
                            "Common random numbers correlate parameter templates; they do not increase independent simulated-event count.",
                            "A small variance of neighboring template differences is not zero uncertainty in either template.",
                            "The data/template projection assumes independent data and simulation and a fixed true-model score.",
                            "Unweighted fixed-N covariance differs from independent Poisson simulation-bin counts.",
                            "Generated and accepted template counts differ when ROI selection loses events.",
                            "No Barlow-Beeston source implementation or paper conclusion is attributed without full text.",
                            "No actual Geant4/transport template bank, selection covariance, nonlinear fit or interval is reproduced."])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"verification": result["verification"],
                      "covariance": result["covariance_diagnostics"],
                      "inflation": result["data_template_projection_inflation"]}))


if __name__ == "__main__":
    main()
