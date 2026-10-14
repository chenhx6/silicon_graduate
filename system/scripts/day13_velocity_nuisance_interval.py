#!/usr/bin/env python3
"""Synthetic DAY13 entry-velocity nuisance and joint tau/E region closure.

Same no-feeding history kernel as the preceding interval exercise. Compare a
wrong fixed entry velocity with a fitted velocity constrained by one noisy,
independent Gaussian measurement. It is a chosen global velocity nuisance,
not event-by-event experimental reconstruction or a source uncertainty.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime
from pathlib import Path

import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy.stats import chi2

import day13_finite_bin_lineshape as bins
import day13_nonlinear_interval_closure as intervals


TRUE_BETA_IN = 0.126
WRONG_FIXED_BETA_IN = 0.125
BETA_TAG_SIGMA = 0.001
BETA_COORDINATE_SCALE = 0.001
BOUNDS = intervals.PARAMETER_BOUNDS+[(-6.0, 6.0)]


class VelocityModel:
    def __init__(self, order=128):
        self.clock = intervals.LineShape(order=order)
        self.order = order

    def probability_and_gradient(self, x):
        beta_in = TRUE_BETA_IN+BETA_COORDINATE_SCALE*x[2]
        time = self.clock.time
        beta = beta_in+(bins.history.BETA_EXIT-beta_in)*time/bins.history.T_EXIT_PS
        cosine = np.cos(np.deg2rad(bins.ANGLES))[:, None]
        d = (1-beta[None, :]*cosine)/np.sqrt(1-beta[None, :]**2)
        exit_d = (1-bins.history.BETA_EXIT*cosine)/math.sqrt(1-bins.history.BETA_EXIT**2)
        ratio = np.column_stack((exit_d/d, np.ones(len(bins.ANGLES))))
        angular = np.column_stack((1/d**2, 1/exit_d[:, 0]**2))
        d_log_d = (beta[None, :]/(1-beta[None, :]**2)
                   - cosine/(1-beta[None, :]*cosine))*(1-time/bins.history.T_EXIT_PS)
        ratio_derivative = np.column_stack((-ratio[:, :-1]*d_log_d,
                                            np.zeros(len(bins.ANGLES))))*BETA_COORDINATE_SCALE
        angular_derivative = np.column_stack((-2*angular[:, :-1]*d_log_d,
                                              np.zeros(len(bins.ANGLES))))*BETA_COORDINATE_SCALE
        e0 = bins.TRUE_E_KEV+x[1]
        centers = e0*ratio
        edges = self.clock.edges
        low = (edges[:-1][None, :, None]-centers[:, None, :])/bins.SIGMA_KEV
        high = (edges[1:][None, :, None]-centers[:, None, :])/bins.SIGMA_KEV
        integral = bins.gaussian_interval(low, high)
        derivative_mean = (np.exp(-low**2/2)-np.exp(-high**2/2))/(
            math.sqrt(2*math.pi)*bins.SIGMA_KEV)
        time_weight, time_derivative = self.clock.waiting(float(x[0]))
        raw = (integral*angular[:, None, :]) @ time_weight
        raw_dt = (integral*angular[:, None, :]) @ time_derivative
        raw_de = (derivative_mean*ratio[:, None, :]*angular[:, None, :]) @ time_weight
        raw_db = (derivative_mean*e0*ratio_derivative[:, None, :]*angular[:, None, :]
                  + integral*angular_derivative[:, None, :]) @ time_weight
        denominator = raw.sum(axis=1, keepdims=True)
        p = raw/denominator
        derivatives = [(v-p*v.sum(axis=1, keepdims=True))/denominator
                       for v in (raw_dt, raw_de, raw_db)]
        return p, np.stack(derivatives, axis=-1)

    def likelihood(self, x, counts, observed_beta_coordinate):
        p, derivative = self.probability_and_gradient(x)
        clipped = np.maximum(p, 1e-250)
        residual = (TRUE_BETA_IN+BETA_COORDINATE_SCALE*x[2]
                    -(TRUE_BETA_IN+BETA_COORDINATE_SCALE*observed_beta_coordinate))/BETA_TAG_SIGMA
        value = -float(np.sum(counts*np.log(clipped)))+0.5*residual**2
        gradient = -np.sum((counts/clipped)[..., None]*derivative, axis=(0, 1))
        gradient[2] += residual*BETA_COORDINATE_SCALE/BETA_TAG_SIGMA
        return value, gradient


class FixedVelocityComparison:
    """Explicitly separate the generator probability and fit likelihood."""
    def __init__(self, generator, fitted_model):
        self.generator = generator
        self.fitted_model = fitted_model

    def probability_and_gradient(self, x):
        return self.generator.probability_and_gradient(x)

    def likelihood(self, x, counts):
        return self.fitted_model.likelihood(x, counts)


def validate(model):
    probability_error = gradient_error = order_error = 0.0
    higher = VelocityModel(order=256)
    for tau, energy, beta_coordinate in ((0.020, -0.5, -1.0), (0.070, 0.0, 0.0),
                                        (0.150, 0.4, 1.5)):
        x = np.array([math.log(tau/intervals.REFERENCE_TAU_PS), energy, beta_coordinate])
        p, gradient = model.probability_and_gradient(x)
        simple = intervals.LineShape(beta_in=TRUE_BETA_IN+BETA_COORDINATE_SCALE*beta_coordinate)
        expected, _ = simple.probability_and_gradient(x[:2])
        probability_error = max(probability_error, float(np.max(np.abs(p-expected))))
        alternate, _ = higher.probability_and_gradient(x)
        order_error = max(order_error, float(np.max(np.abs(p-alternate))))
        for coordinate in (0, 1, 2):
            step = 1e-5
            before, after = x.copy(), x.copy()
            before[coordinate] -= step
            after[coordinate] += step
            finite = (model.probability_and_gradient(after)[0]
                      - model.probability_and_gradient(before)[0])/(2*step)
            gradient_error = max(gradient_error, float(np.max(np.abs(finite-gradient[..., coordinate]))))
    assert probability_error < 1e-10 and order_error < 1e-10 and gradient_error < 1e-7
    return dict(probability_agreement_with_fixed_velocity_model_max_error=probability_error,
                analytic_three_coordinate_gradient_max_FD_error=gradient_error,
                quadrature128_256_max_bin_difference=order_error)


def profiled_case(model, count, repeats, rng, deadline):
    truth = np.array([0.0, 0.0, 0.0])
    p, derivative = model.probability_and_gradient(truth)
    counts = np.stack([rng.multinomial(count, q, repeats) for q in p], axis=1)
    measured_coordinate = rng.normal(0, BETA_TAG_SIGMA/BETA_COORDINATE_SCALE, repeats)
    estimates, delta = [], []
    failure_attempts = []
    fallback_count = 0
    for i, observed in enumerate(counts):
        if i % 100 == 0:
            intervals.deadline_check(deadline)
        objective = lambda x: model.likelihood(x, observed, measured_coordinate[i])
        starts = ([0.0, 0.0, float(np.clip(measured_coordinate[i], -5.0, 5.0))],
                  [math.log(0.10/intervals.REFERENCE_TAU_PS), -1.0, 0.0])
        results = [minimize(objective, start, jac=True, method="L-BFGS-B", bounds=BOUNDS,
                            options={"ftol": 1e-12, "gtol": 1e-6, "maxiter": 180})
                   for start in starts]
        successes = [r for r in results if r.success]
        for start_index, r in enumerate(results):
            if not r.success:
                failure_attempts.append(dict(index=i, start_index=start_index, message=str(r.message)))
        if not successes:
            fallback_count += 1
            fallback = minimize(lambda x: objective(x)[0], starts[0], method="Powell", bounds=BOUNDS,
                                options={"ftol": 1e-12, "xtol": 1e-8, "maxiter": 250})
            if fallback.success:
                successes.append(fallback)
        assert successes, (i, failure_attempts[-2:])
        best = min(successes, key=lambda r: r.fun)
        # Profile the velocity at the true interest pair (tau,E), retaining its
        # independent Gaussian observation in both numerator and denominator.
        constrained = minimize_scalar(lambda value: objective(np.array([0.0, 0.0, value]))[0],
                                      bounds=(-6.0, 6.0), method="bounded",
                                      options={"xatol": 1e-10})
        assert constrained.success
        assert best.fun <= constrained.fun+1e-6
        estimates.append(best.x)
        delta.append(max(0.0, 2*float(constrained.fun-best.fun)))
    estimates, delta = np.array(estimates), np.array(delta)
    rows = []
    for probability in (0.683, 0.95):
        threshold = float(chi2.ppf(probability, 2))
        coverage = float(np.mean(delta <= threshold))
        rows.append(dict(nominal_interest_pair_probability=probability,
                         delta_deviance_threshold=threshold,
                         observed_joint_truth_coverage=coverage,
                         binomial_MC_SE=math.sqrt(coverage*(1-coverage)/repeats)))
    return dict(fixed_count_per_angle=count, repeats=repeats,
                fitted_tau_mean_fs=float((1000*intervals.REFERENCE_TAU_PS*np.exp(estimates[:, 0])).mean()),
                fitted_energy_shift_mean_keV=float(estimates[:, 1].mean()),
                fitted_entry_beta_mean=float((TRUE_BETA_IN+BETA_COORDINATE_SCALE*estimates[:, 2]).mean()),
                imposed_tau_lower_bound_fraction=float(np.mean(np.abs(
                    estimates[:, 0]-BOUNDS[0][0]) < 1e-6)),
                velocity_boundary_fraction=float(np.mean(np.abs(estimates[:, 2]) > 6-1e-5)),
                coverage=rows, optimization_failed_attempts=failure_attempts,
                Powell_fallback_count=fallback_count,
                count_identity=dict(shape=list(counts.shape), dtype="little-endian int64",
                                    sha256=hashlib.sha256(counts.astype('<i8').tobytes()).hexdigest()),
                independent_beta_measurement_identity=dict(sha256=hashlib.sha256(
                    measured_coordinate.astype('<f8').tobytes()).hexdigest(), count=repeats))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--repeats", type=int, default=2000)
    parser.add_argument("--deadline", type=datetime.fromisoformat)
    args = parser.parse_args()
    model = VelocityModel()
    checks = validate(model)
    generator = intervals.LineShape()
    wrong = intervals.LineShape(beta_in=WRONG_FIXED_BETA_IN)
    coordinates, bank = wrong.grid_bank()
    truth_probability = generator.probability_and_gradient(np.array([0.0, 0.0]))[0]
    expected_counts = 10000*truth_probability
    expected_fit = minimize(lambda x: wrong.likelihood(x, expected_counts), [0.0, -2.0], jac=True,
                            method="L-BFGS-B", bounds=intervals.PARAMETER_BOUNDS,
                            options={"ftol": 1e-13, "gtol": 1e-7, "maxiter": 200})
    assert expected_fit.success
    _, d = model.probability_and_gradient(np.array([0.0, 0.0, 0.0]))
    flat_d = d.reshape(-1, 3)
    flat_p = truth_probability.ravel()
    keep = flat_p > 1e-14
    gamma_fisher = 1000*(flat_d[keep].T @ (flat_d[keep]/flat_p[keep, None]))
    calibration_information = np.diag([0.0, 0.0, (BETA_COORDINATE_SCALE/BETA_TAG_SIGMA)**2])
    joint_covariance = np.linalg.inv(gamma_fisher+calibration_information)
    # Independent derivation: interest-pair profile covariance is the Schur block.
    total = gamma_fisher+calibration_information
    profile = total[:2, :2]-np.outer(total[:2, 2], total[2, :2])/total[2, 2]
    assert np.max(np.abs(np.linalg.inv(profile)-joint_covariance[:2, :2])) < 1e-10
    result = dict(schema_version=1, status="running", kind="synthetic entry-velocity nuisance interval closure",
                  chosen_parameters=dict(true_tau_fs=70.0, true_entry_beta=TRUE_BETA_IN,
                                         wrong_fixed_entry_beta=WRONG_FIXED_BETA_IN,
                                         independent_beta_tag_sigma=BETA_TAG_SIGMA,
                                         exit_beta=bins.history.BETA_EXIT,
                                         no_feeding=True, fixed_history_family=True,
                                         point_angles_deg=list(bins.ANGLES), repeats=args.repeats,
                                         wrong_fixed_seed=131432, profiled_seed=131433),
                  expected_wrong_fixed_fit=dict(pseudo_true_tau_fs=1000*intervals.REFERENCE_TAU_PS*math.exp(expected_fit.x[0]),
                                               pseudo_true_energy_shift_keV=float(expected_fit.x[1])),
                  local_profile_design_at1000_per_angle=dict(
                      tau_SE_fs=1000*intervals.REFERENCE_TAU_PS*math.sqrt(joint_covariance[0, 0]),
                      energy_SE_keV=math.sqrt(joint_covariance[1, 1]),
                      entry_beta_SE=BETA_COORDINATE_SCALE*math.sqrt(joint_covariance[2, 2])),
                  wrong_fixed_cases=[], profiled_cases=[], verification=checks,
                  dependencies=dict(interval_runner_sha256=hashlib.sha256(
                      Path(intervals.__file__).read_bytes()).hexdigest()),
                  boundaries=["Entrybeta is one global nuisance per experiment, not a reconstructed speed per photon/event.",
                              "Gaussian tag is independent and unbiased by construction; shared calibration or biased tags need another joint model.",
                              "Fixed transport/response/no-feeding and point angles are chosen; they are not actual20O settings.",
                              "Profile coverage concerns the tau/E interest pair, not the three-parameter region or projected tau interval.",
                              "Statistical closure in the correct family does not validate that family or an actual velocity-stage binding.",
                              "No reported source bias, uncertainty, independent velocity resolution or lifetime is recalculated."])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    def save():
        args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    save()
    comparison = FixedVelocityComparison(generator, wrong)
    wrong_rng = np.random.default_rng(131432)
    for count in (25, 1000):
        case = intervals.analyze_case(comparison, coordinates, bank, 0.070, count,
                                      args.repeats, wrong_rng, args.deadline)
        for row in case["coverage"]:
            row["declared_case_asymptotic_probability"] = None
            row["interpretation"] = "wrong fixed velocity; regular correct-model chi2 expectation is inapplicable"
        result["wrong_fixed_cases"].append(case)
        save()
        print(json.dumps({"wrong_fixed_count": count, "result": case}), flush=True)
    profile_rng = np.random.default_rng(131433)
    for count in (25, 1000):
        case = profiled_case(model, count, args.repeats, profile_rng, args.deadline)
        result["profiled_cases"].append(case)
        save()
        print(json.dumps({"profiled_count": count, "result": case}), flush=True)
    result["status"] = "complete-synthetic-analysis"
    result["verification"]["Schur_profile_information_check_passed"] = True
    result["verification"]["all_passed"] = True
    result["dependencies"]["analysis_script_sha256_at_execution"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    save()
    print(json.dumps({"status": result["status"], "verification": result["verification"]}), flush=True)


if __name__ == "__main__":
    main()
