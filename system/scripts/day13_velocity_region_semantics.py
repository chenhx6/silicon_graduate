#!/usr/bin/env python3
"""Same DAY13 synthetic velocity experiments: joint, profile and projection.

Reconstructs the preceding count streams and independent beta observations.
For the calibrated model, their hashes must match. Compares the joint tau/E
truth test, one-interest tau profile and projection of the joint region.
It is an additional statistic on dependent data, not independent evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy.stats import beta, chi2

import day13_nonlinear_interval_closure as intervals
import day13_velocity_nuisance_interval as velocity


def coverage(values, threshold):
    total = len(values)
    successes = int(np.sum(values <= threshold))
    return dict(successes=successes, repeats=total, observed_fraction=successes/total,
                MC_exact95_two_sided_interval=[
                    float(beta.ppf(0.025, successes, total-successes+1)) if successes else 0.0,
                    float(beta.ppf(0.975, successes+1, total-successes)) if successes < total else 1.0])


def analyze(counts, model, beta_observation, deadline):
    profile_q, joint_q = [], []
    failed_attempts = []
    is_calibrated = beta_observation is not None
    for index, observed in enumerate(counts):
        if index % 100 == 0:
            intervals.deadline_check(deadline)
        if is_calibrated:
            objective = lambda x: model.likelihood(x, observed, beta_observation[index])
            starts = ([0.0, 0.0, float(np.clip(beta_observation[index], -5, 5))],
                      [math.log(0.1/intervals.REFERENCE_TAU_PS), -1.0, 0.0])
            bounds = velocity.BOUNDS
        else:
            objective = lambda x: model.likelihood(x, observed)
            starts = ([0.0, -2.0], [math.log(0.1/intervals.REFERENCE_TAU_PS), -1.0])
            bounds = intervals.PARAMETER_BOUNDS
        fits = [minimize(objective, start, jac=True, method="L-BFGS-B", bounds=bounds,
                         options={"ftol": 1e-12, "gtol": 1e-6, "maxiter": 180})
                for start in starts]
        successes = [fit for fit in fits if fit.success]
        for start_index, fit in enumerate(fits):
            if not fit.success:
                failed_attempts.append(dict(index=index, start=start_index, message=str(fit.message)))
        if not successes:
            fallback = minimize(lambda x: objective(x)[0], starts[0], method="Powell",
                                bounds=bounds, options={"ftol": 1e-12, "xtol": 1e-8, "maxiter": 250})
            if fallback.success:
                successes.append(fallback)
        assert successes, (index, failed_attempts[-2:])
        best = min(successes, key=lambda fit: fit.fun)
        if is_calibrated:
            def tau_constrained(y):
                value, gradient = objective(np.array([0.0, y[0], y[1]]))
                return value, gradient[1:]
            constrained_fits = [minimize(tau_constrained, start, jac=True, method="L-BFGS-B",
                                        bounds=bounds[1:],
                                        options={"ftol": 1e-12, "gtol": 1e-6, "maxiter": 180})
                               for start in (best.x[1:], np.array([0.0, beta_observation[index]]))]
            valid = [fit for fit in constrained_fits if fit.success]
            assert valid, index
            tau_objective = min(fit.fun for fit in valid)
            joint_truth = minimize_scalar(lambda value: objective(np.array([0.0, 0.0, value]))[0],
                                          bounds=(-6, 6), method="bounded", options={"xatol": 1e-10})
            assert joint_truth.success
            joint_objective = joint_truth.fun
        else:
            constrained = minimize_scalar(lambda value: objective(np.array([0.0, value]))[0],
                                          bounds=(-8, 8), method="bounded", options={"xatol": 1e-10})
            assert constrained.success
            tau_objective = constrained.fun
            joint_objective = objective(np.array([0.0, 0.0]))[0]
        assert best.fun <= tau_objective+1e-6
        assert tau_objective <= joint_objective+1e-6
        profile_q.append(max(0.0, 2*float(tau_objective-best.fun)))
        joint_q.append(max(0.0, 2*float(joint_objective-best.fun)))
    profile_q, joint_q = np.array(profile_q), np.array(joint_q)
    rows = []
    for probability in (0.683, 0.95):
        joint_threshold = float(chi2.ppf(probability, 2))
        profile_threshold = float(chi2.ppf(probability, 1))
        rows.append(dict(nominal_probability=probability,
                         joint_pair=coverage(joint_q, joint_threshold),
                         one_interest_tau_profile=coverage(profile_q, profile_threshold),
                         joint_region_tau_projection=coverage(profile_q, joint_threshold),
                         thresholds=dict(joint_two=joint_threshold, profile_one=profile_threshold)))
    return dict(coverage=rows, numerical_failed_attempts=failed_attempts,
                profile_q_quantiles=np.quantile(profile_q, [.5, .683, .95, .99]).tolist(),
                joint_q_quantiles=np.quantile(joint_q, [.5, .683, .95, .99]).tolist())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--deadline", type=intervals.datetime.fromisoformat)
    args = parser.parse_args()
    previous = json.loads(args.input.read_text())
    assert previous['verification']['all_passed']
    assert hashlib.sha256(Path(velocity.__file__).read_bytes()).hexdigest() == previous['dependencies']['analysis_script_sha256_at_execution']
    result = dict(schema_version=1, status="running", kind="dependent replay of velocity region definitions",
                  previous_run=str(args.input), previous_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  wrong_fixed_cases=[], calibrated_cases=[],
                  independent_evidence=False,
                  MC_interval_definition="95% two-sided Clopper-Pearson for the Monte Carlo success fraction only",
                  boundaries=["Same simulated count streams, not additional independent experiments.",
                              "Joint pair coverage differs from one-interest tau profile and projection of the joint region.",
                              "Zero observed successes are reported as0/R with a finite exact binomial upper bound.",
                              "No source confidence definition or actual beta systematic is reassigned."])
    def save():
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    save()
    generating = intervals.LineShape()
    wrong = intervals.LineShape(beta_in=velocity.WRONG_FIXED_BETA_IN)
    p = generating.probability_and_gradient(np.array([0.0, 0.0]))[0]
    rng = np.random.default_rng(previous['chosen_parameters']['wrong_fixed_seed'])
    for old in previous['wrong_fixed_cases']:
        n, repeats = old['fixed_selected_count_per_angle'], old['repeats']
        counts = np.stack([rng.multinomial(n, probability, repeats) for probability in p], axis=1)
        analyzed = analyze(counts, wrong, None, args.deadline)
        for row, original in zip(analyzed['coverage'], old['coverage']):
            assert abs(row['joint_pair']['observed_fraction']-original['observed_joint_truth_coverage']) <= 1/repeats+1e-12
        analyzed.update(count_per_angle=n, repeats=repeats,
                        counts_sha256=hashlib.sha256(counts.astype('<i8').tobytes()).hexdigest())
        result['wrong_fixed_cases'].append(analyzed)
        save()
        print(json.dumps({'wrong_fixed':n,'coverage':analyzed['coverage']}), flush=True)
    calibrated = velocity.VelocityModel()
    p = calibrated.probability_and_gradient(np.array([0.0, 0.0, 0.0]))[0]
    rng = np.random.default_rng(previous['chosen_parameters']['profiled_seed'])
    for old in previous['profiled_cases']:
        n, repeats = old['fixed_count_per_angle'], old['repeats']
        counts = np.stack([rng.multinomial(n, probability, repeats) for probability in p], axis=1)
        measured = rng.normal(0, velocity.BETA_TAG_SIGMA/velocity.BETA_COORDINATE_SCALE, repeats)
        assert hashlib.sha256(counts.astype('<i8').tobytes()).hexdigest()==old['count_identity']['sha256']
        assert hashlib.sha256(measured.astype('<f8').tobytes()).hexdigest()==old['independent_beta_measurement_identity']['sha256']
        analyzed = analyze(counts, calibrated, measured, args.deadline)
        for row, original in zip(analyzed['coverage'], old['coverage']):
            assert abs(row['joint_pair']['observed_fraction']-original['observed_joint_truth_coverage']) <= 1/repeats+1e-12
        analyzed.update(count_per_angle=n, repeats=repeats,
                        counts_sha256=old['count_identity']['sha256'],
                        beta_observation_sha256=old['independent_beta_measurement_identity']['sha256'])
        result['calibrated_cases'].append(analyzed)
        save()
        print(json.dumps({'calibrated':n,'coverage':analyzed['coverage']}), flush=True)
    result['status']='complete-dependent-statistic-audit'
    result['verification']={'previous_joint_result_reproduced':True,
                            'calibrated_counts_and_measurement_hashes_match':True,
                            'profile_q_never_exceeds_joint_truth_q':True,
                            'all_passed':True}
    result['dependencies']={'analysis_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    save()


if __name__=='__main__':
    main()
