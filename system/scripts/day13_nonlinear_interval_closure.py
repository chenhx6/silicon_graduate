#!/usr/bin/env python3
"""Synthetic DAY13 finite-count joint lifetime/energy likelihood closure.

Known no-feeding exponential proper-time model, fixed bins, point angles and
Gaussian response. Separate fixed selected counts at three angles are used.
An imposed lifetime lower bound and a no-loss limit test asymptotic-region
assumptions; these are not experimental source intervals or a refit.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from datetime import datetime
from functools import lru_cache
from pathlib import Path

import numpy as np
import scipy
from numpy.polynomial.legendre import leggauss
from scipy.optimize import minimize
from scipy.stats import chi2

import day13_finite_bin_lineshape as bins


REFERENCE_TAU_PS = 0.070
LOWER_TAU_PS = 0.020
UPPER_TAU_PS = 0.250
PARAMETER_BOUNDS = [(math.log(LOWER_TAU_PS/REFERENCE_TAU_PS),
                     math.log(UPPER_TAU_PS/REFERENCE_TAU_PS)), (-8.0, 8.0)]


class LineShape:
    def __init__(self, order=128, beta_in=bins.history.BETA_IN):
        self.order = order
        self.beta_in = beta_in
        self.edges = bins.make_edges(5.0)
        nodes, weights = leggauss(order)
        self.time = bins.history.T_EXIT_PS*(nodes+1)/2
        self.time_quadrature = weights*bins.history.T_EXIT_PS/2
        beta = beta_in+(bins.history.BETA_EXIT-beta_in)*self.time/bins.history.T_EXIT_PS
        cosine = np.cos(np.deg2rad(bins.ANGLES))[:, None]
        d = (1-beta[None, :]*cosine)/np.sqrt(1-beta[None, :]**2)
        exit_d = (1-bins.history.BETA_EXIT*cosine)/math.sqrt(1-bins.history.BETA_EXIT**2)
        self.ratio = np.column_stack((exit_d/d, np.ones(len(bins.ANGLES))))
        self.angular = np.column_stack((1/d**2, 1/exit_d[:, 0]**2))

    def waiting(self, log_tau):
        tau = REFERENCE_TAU_PS*math.exp(log_tau)
        density = np.exp(-self.time/tau)/tau
        survival = math.exp(-bins.history.T_EXIT_PS/tau)
        weight = np.r_[self.time_quadrature*density, survival]
        derivative = np.r_[self.time_quadrature*density*(self.time/tau-1),
                           survival*bins.history.T_EXIT_PS/tau]
        return weight, derivative

    @lru_cache(maxsize=256)
    def Gaussian_matrices(self, energy_shift):
        centers = (bins.TRUE_E_KEV+energy_shift)*self.ratio
        low = (self.edges[:-1][None, :, None]-centers[:, None, :])/bins.SIGMA_KEV
        high = (self.edges[1:][None, :, None]-centers[:, None, :])/bins.SIGMA_KEV
        integral = bins.gaussian_interval(low, high)*self.angular[:, None, :]
        derivative = self.ratio[:, None, :]/bins.SIGMA_KEV*(
            np.exp(-low**2/2)-np.exp(-high**2/2))/math.sqrt(2*math.pi)
        derivative *= self.angular[:, None, :]
        return integral, derivative

    def probability_and_gradient(self, x):
        weight, derivative = self.waiting(float(x[0]))
        g, de = self.Gaussian_matrices(float(x[1]))
        raw = g @ weight
        raw_dt = g @ derivative
        raw_de = de @ weight
        denominator = raw.sum(axis=1, keepdims=True)
        p = raw/denominator
        dt = (raw_dt-p*raw_dt.sum(axis=1, keepdims=True))/denominator
        denergy = (raw_de-p*raw_de.sum(axis=1, keepdims=True))/denominator
        return p, np.stack((dt, denergy), axis=-1)

    def likelihood(self, x, counts):
        p, gradient = self.probability_and_gradient(x)
        clipped = np.maximum(p, 1e-250)
        objective = -float(np.sum(counts*np.log(clipped)))
        score = -np.sum((counts/clipped)[..., None]*gradient, axis=(0, 1))
        return objective, score

    def grid_bank(self):
        tau_values = np.linspace(LOWER_TAU_PS, UPPER_TAU_PS, 116)
        energy_values = np.linspace(-3.0, 3.0, 61)
        coordinates = []
        log_probabilities = []
        for energy in energy_values:
            g, _ = self.Gaussian_matrices(float(energy))
            time_weights = np.column_stack([self.waiting(math.log(t/REFERENCE_TAU_PS))[0]
                                           for t in tau_values])
            raw = g @ time_weights
            p = raw/raw.sum(axis=1, keepdims=True)
            log_probabilities.append(np.log(np.maximum(p, 1e-250)).transpose(2, 0, 1).reshape(len(tau_values), -1))
            coordinates.extend((math.log(t/REFERENCE_TAU_PS), float(energy)) for t in tau_values)
        return np.array(coordinates), np.concatenate(log_probabilities)


def validation(model):
    probability_error = gradient_error = order_error = 0.0
    higher = LineShape(order=256)
    for tau in (0.020, 0.070, 0.250):
        for energy_shift in (-0.7, 0.0, 0.6):
            x = np.array([math.log(tau/REFERENCE_TAU_PS), energy_shift])
            p, gradient = model.probability_and_gradient(x)
            alternate, _ = higher.probability_and_gradient(x)
            order_error = max(order_error, float(np.max(np.abs(p-alternate))))
            assert np.max(np.abs(p.sum(axis=1)-1)) < 1e-12
            for g, angle in enumerate(bins.ANGLES):
                ratio, w, _ = bins.history.kernel(tau, 0.0, angle)
                low = (model.edges[:-1, None]-(bins.TRUE_E_KEV+energy_shift)*ratio)/bins.SIGMA_KEV
                high = (model.edges[1:, None]-(bins.TRUE_E_KEV+energy_shift)*ratio)/bins.SIGMA_KEV
                q, _ = bins.conditional(bins.gaussian_interval(low, high) @ w)
                probability_error = max(probability_error, float(np.max(np.abs(p[g]-q))))
            for coordinate in (0, 1):
                step = 1e-5
                before, after = x.copy(), x.copy()
                before[coordinate] -= step
                after[coordinate] += step
                finite = (model.probability_and_gradient(after)[0]
                          - model.probability_and_gradient(before)[0])/(2*step)
                gradient_error = max(gradient_error, float(np.max(np.abs(finite-gradient[..., coordinate]))))
    assert probability_error < 1e-10 and order_error < 1e-10 and gradient_error < 1e-7
    static = LineShape(beta_in=bins.history.BETA_EXIT)
    p1, grad1 = static.probability_and_gradient(np.array([0.0, 0.0]))
    p2, _ = static.probability_and_gradient(np.array([math.log(0.2/REFERENCE_TAU_PS), 0.0]))
    assert np.max(np.abs(p1-p2)) < 1e-12 and np.max(np.abs(grad1[..., 0])) < 1e-12
    return dict(probability_agreement_with_existing_no_feed_kernel_max_error=probability_error,
                analytic_gradient_finite_difference_max_error=gradient_error,
                quadrature128_256_max_probability_difference=order_error,
                no_loss_lifetime_shape_independence_passed=True)


def deadline_check(deadline):
    if deadline and datetime.now(deadline.tzinfo) >= deadline:
        raise RuntimeError("original research deadline reached; leave recoverable partial analysis")


def analyze_case(model, coordinates, log_bank, tau, count, repeats, rng, deadline, no_loss=False):
    truth = np.array([math.log(tau/REFERENCE_TAU_PS), 0.0])
    p, derivative = model.probability_and_gradient(truth)
    counts = np.stack([rng.multinomial(count, probability, repeats) for probability in p], axis=1)
    starting_points = []
    if no_loss:
        starting_points = np.tile(truth, (repeats, 1))
        grid_objective = np.full(repeats, np.inf)
    else:
        starting_points = np.zeros((repeats, 2))
        grid_objective = np.zeros(repeats)
        for start in range(0, repeats, 128):
            deadline_check(deadline)
            chunk = counts[start:start+128].reshape(-1, p.size)
            likelihood = chunk @ log_bank.T
            selected = np.argmax(likelihood, axis=1)
            starting_points[start:start+len(chunk)] = coordinates[selected]
            grid_objective[start:start+len(chunk)] = -likelihood[np.arange(len(chunk)), selected]
    estimates, delta = [], []
    first_failure = second_failure = fallback_count = 0
    max_grid_disadvantage = 0.0
    failed_details = []
    for i, observed in enumerate(counts):
        if i % 100 == 0:
            deadline_check(deadline)
        objective = lambda x: model.likelihood(x, observed)
        first = minimize(objective, starting_points[i], jac=True, method="L-BFGS-B",
                         bounds=PARAMETER_BOUNDS,
                         options={"ftol": 1e-12, "gtol": 1e-6, "maxiter": 150})
        second_start = truth if not no_loss else np.array([math.log(0.12/REFERENCE_TAU_PS), 0.7])
        second = minimize(objective, second_start, jac=True, method="L-BFGS-B",
                          bounds=PARAMETER_BOUNDS,
                          options={"ftol": 1e-12, "gtol": 1e-6, "maxiter": 150})
        first_failure += int(not first.success)
        second_failure += int(not second.success)
        successes = [fit for fit in (first, second) if fit.success]
        if not successes:
            fallback_count += 1
            fallback = minimize(lambda x: objective(x)[0], starting_points[i], method="Powell",
                                bounds=PARAMETER_BOUNDS,
                                options={"ftol": 1e-12, "xtol": 1e-9, "maxiter": 200})
            if fallback.success:
                successes.append(fallback)
        if not successes:
            failed_details.append(dict(index=i, first=str(first.message), second=str(second.message)))
            continue
        best = min(successes, key=lambda fit: fit.fun)
        at_truth = objective(truth)[0]
        assert best.fun <= at_truth+1e-6
        max_grid_disadvantage = max(max_grid_disadvantage, float(best.fun-grid_objective[i]))
        assert best.fun <= grid_objective[i]+1e-6
        estimates.append(best.x)
        delta.append(max(0.0, 2*float(at_truth-best.fun)))
    assert not failed_details, failed_details[:5]
    estimates, delta = np.array(estimates), np.array(delta)
    fitted_tau = 1000*REFERENCE_TAU_PS*np.exp(estimates[:, 0])
    boundary_fraction = float(np.mean(np.abs(estimates[:, 0]-PARAMETER_BOUNDS[0][0]) < 1e-6))
    threshold_rows = []
    for probability in (0.683, 0.95):
        threshold = float(chi2.ppf(probability, 2))
        measured = float(np.mean(delta <= threshold))
        if no_loss:
            expected_asymptotic = float(chi2.cdf(threshold, 1))
        elif tau == LOWER_TAU_PS:
            expected_asymptotic = float(0.5*chi2.cdf(threshold, 1)+0.5*chi2.cdf(threshold, 2))
        else:
            expected_asymptotic = probability
        threshold_rows.append(dict(nominal_regular_two_parameter_probability=probability,
                                   delta_deviance_threshold=threshold,
                                   observed_joint_truth_coverage=measured,
                                   binomial_MC_SE=math.sqrt(measured*(1-measured)/repeats),
                                   declared_case_asymptotic_probability=expected_asymptotic))
    return dict(no_loss=no_loss, true_tau_fs=1000*tau,
                fixed_selected_count_per_angle=count, repeats=repeats,
                fitted_tau_mean_fs=float(fitted_tau.mean()),
                fitted_energy_shift_mean_keV=float(estimates[:, 1].mean()),
                lifetime_lower_bound_fraction=boundary_fraction,
                lifetime_upper_bound_fraction=float(np.mean(
                    np.abs(estimates[:, 0]-PARAMETER_BOUNDS[0][1]) < 1e-6)),
                energy_bound_fraction=float(np.mean(np.abs(estimates[:, 1]) > 8-1e-5)),
                coverage=threshold_rows,
                delta_deviance_quantiles=np.quantile(delta, [.5, .683, .95, .99]).tolist(),
                optimization=dict(first_start_failures=first_failure,
                                  second_start_failures=second_failure,
                                  Powell_fallback_count=fallback_count,
                                  unverified_experiments=failed_details,
                                  coarse_grid_max_disadvantage=max_grid_disadvantage))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--repeats", type=int, default=2000)
    parser.add_argument("--deadline", type=datetime.fromisoformat)
    args = parser.parse_args()
    model = LineShape()
    checks = validation(model)
    deadline_check(args.deadline)
    coordinates, bank = model.grid_bank()
    rng = np.random.default_rng(131431)
    result = dict(schema_version=1, status="running", kind="synthetic nonlinear joint lifetime/energy region closure",
                  source_inspiration="BC84 point/interval/finiteN boundaries; source lifetimes/errors unchanged",
                  chosen_parameters=dict(seed=131431, point_angles_deg=list(bins.ANGLES),
                                         no_feeding=True, beta_in=bins.history.BETA_IN,
                                         beta_exit=bins.history.BETA_EXIT,
                                         proper_slowing_time_ps=bins.history.T_EXIT_PS,
                                         Gaussian_corrected_sigma_keV=bins.SIGMA_KEV,
                                         true_rest_energy_keV=bins.TRUE_E_KEV,
                                         bin_edges_keV=model.edges.tolist(),
                                         imposed_tau_bounds_ps=[LOWER_TAU_PS, UPPER_TAU_PS],
                                         energy_shift_bounds_keV=[-8.0, 8.0],
                                         repeats_per_case=args.repeats),
                  verification=checks, cases=[],
                  dependencies=dict(kernel_sha256=hashlib.sha256(
                      Path(bins.history.__file__).read_bytes()).hexdigest(),
                                    numpy=np.__version__, scipy=scipy.__version__),
                  boundaries=["The20fs minimum is an imposed model-domain control, not a physical minimum or source prior.",
                              "Known no-feeding model/response/transport/fixed bins omit real source nuisance parameters.",
                              "Coverage measures whether the true pair is inside a likelihood region; it is not a projected tau interval.",
                              "No-loss tau is unidentifiable; fitted tau values then depend on optimizer start and have no lifetime meaning.",
                              "Two starts and a coarse bank are numerical controls, not a global-optimum theorem.",
                              "No reported20O interval, actual template uncertainty or experiment likelihood is reproduced."])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    def save():
        args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    save()
    for tau, count in ((0.070, 25), (0.070, 1000), (0.020, 25), (0.020, 1000)):
        case = analyze_case(model, coordinates, bank, tau, count, args.repeats, rng, args.deadline)
        result["cases"].append(case)
        save()
        print(json.dumps({"case": len(result["cases"]), "result": case}), flush=True)
    static = LineShape(beta_in=bins.history.BETA_EXIT)
    result["cases"].append(analyze_case(static, None, None, 0.070, 1000,
                                       args.repeats, rng, args.deadline, no_loss=True))
    result["status"] = "complete-synthetic-analysis"
    result["verification"]["all_experiments_numerically_verified"] = True
    result["verification"]["all_passed"] = True
    save()
    print(json.dumps({"status": result["status"], "verification": result["verification"],
                      "case_count": len(result["cases"])}), flush=True)


if __name__ == "__main__":
    main()
