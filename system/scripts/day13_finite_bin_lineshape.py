#!/usr/bin/env python3
"""Synthetic DAY13 Doppler line shape: exact bin integrals versus midpoints.

Uses the previously declared entry-gate kernel, not experimental data or a
production sorter. Fits are expected multinomial KL projections with fixed
counts per angle/ROI; they are neither data fits nor confidence intervals.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.optimize import minimize
from scipy.special import ndtr, rel_entr

import day13_entry_gate_feeding_design as history


TRUE_TAU_PS = 0.070
TRUE_E_KEV = history.E0_KEV
KNOWN_ENTRY_FEED_FRACTION = 0.2
SIGMA_KEV = history.SIGMA_KEV
ANGLES = history.ANGLES_DEG
ROI_LOW_OFFSET_KEV = -140.0
ROI_HIGH_OFFSET_KEV = 20.0


def gaussian_interval(low, high):
    """Stable normal probability for arrays of standardized interval edges."""
    return np.where(low > 0, ndtr(-low) - ndtr(-high),
                    ndtr(high) - ndtr(low))


def raw_bin_probabilities(edges, e0, tau, angle, method="integral", order=128):
    ratios, weights, _ = history.kernel(tau, KNOWN_ENTRY_FEED_FRACTION,
                                        angle, order=order)
    centers = e0 * ratios
    if method == "integral":
        low = (edges[:-1, None] - centers) / SIGMA_KEV
        high = (edges[1:, None] - centers) / SIGMA_KEV
        return gaussian_interval(low, high) @ weights
    if method == "midpoint":
        midpoint = (edges[:-1] + edges[1:]) / 2
        normal = np.exp(-0.5 * ((midpoint[:, None] - centers)
                                / SIGMA_KEV)**2)
        return (normal @ weights) * np.diff(edges) / (
            math.sqrt(2 * math.pi) * SIGMA_KEV)
    raise ValueError(method)


def conditional(probabilities):
    mass = float(probabilities.sum())
    assert mass > 0 and np.min(probabilities) >= 0
    return probabilities / mass, mass


def make_edges(width, phase=0.0):
    span = ROI_HIGH_OFFSET_KEV - ROI_LOW_OFFSET_KEV
    count = int(round(span / width))
    assert abs(count * width - span) < 1e-10
    return TRUE_E_KEV + ROI_LOW_OFFSET_KEV + phase * width + (
        np.arange(count + 1) * width)


def fit_expected_histogram(edges, truth, method):
    """Scaled parameters are log(tau/true_tau) and E-true_E in keV."""
    def objective(x):
        tau, e0 = TRUE_TAU_PS * math.exp(x[0]), TRUE_E_KEV + x[1]
        total = 0.0
        for angle, p in zip(ANGLES, truth):
            q, _ = conditional(raw_bin_probabilities(edges, e0, tau,
                                                      angle, method))
            total += float(np.sum(rel_entr(p, np.maximum(q, 1e-300))))
        return total / len(ANGLES)

    starts = ((0.0, 0.0), (-0.4, -0.3), (0.4, 0.3))
    results = [minimize(objective, start, method="L-BFGS-B",
                        bounds=[(math.log(0.020 / TRUE_TAU_PS),
                                 math.log(0.25 / TRUE_TAU_PS)), (-8.0, 8.0)],
                        options={"ftol": 1e-14, "gtol": 2e-9,
                                 "maxiter": 250}) for start in starts]
    successes = [r for r in results if r.success]
    assert successes, [(r.message, r.fun) for r in results]
    best = min(successes, key=lambda r: r.fun)
    return dict(method=method,
                pseudo_true_tau_fs=1000 * TRUE_TAU_PS * math.exp(best.x[0]),
                pseudo_true_energy_keV=TRUE_E_KEV + float(best.x[1]),
                mean_KL_per_selected_photon=float(best.fun),
                multistart=[dict(start=list(s), success=bool(r.success),
                                 message=str(r.message),
                                 tau_fs=1000 * TRUE_TAU_PS * math.exp(r.x[0]),
                                 energy_keV=TRUE_E_KEV + float(r.x[1]),
                                 mean_KL=float(r.fun))
                            for s, r in zip(starts, results)])


def local_information(edges, step=1e-4):
    """Per-angle summed Fisher matrix in (log(tau/true_tau), E shift/keV)."""
    matrix = np.zeros((2, 2))
    for a in ANGLES:
        p, _ = conditional(raw_bin_probabilities(edges, TRUE_E_KEV,
                                                 TRUE_TAU_PS, a))
        derivatives = []
        for coordinate in (0, 1):
            shifted = []
            for sign in (-1, 1):
                tau = TRUE_TAU_PS * math.exp(sign * step) if coordinate == 0 else TRUE_TAU_PS
                e0 = TRUE_E_KEV + sign * step if coordinate == 1 else TRUE_E_KEV
                q, _ = conditional(raw_bin_probabilities(edges, e0, tau, a))
                shifted.append(q)
            derivatives.append((shifted[1]-shifted[0])/(2*step))
        d = np.column_stack(derivatives)
        keep = p > 1e-15
        matrix += d[keep].T @ (d[keep]/p[keep, None])
    return matrix


def calculate():
    cases = []
    additivity_error = quadrature_error = integral_order_error = 0.0
    recovery_error_fs = 0.0
    for width, phase in ((0.5, 0.0), (2.0, 0.0), (5.0, 0.0),
                         (10.0, 0.0), (20.0, 0.0), (20.0, 0.5)):
        edges = make_edges(width, phase)
        truth = [conditional(raw_bin_probabilities(edges, TRUE_E_KEV,
                                                   TRUE_TAU_PS, a))[0]
                 for a in ANGLES]
        normalizer = []
        mismatch = []
        for a, p in zip(ANGLES, truth):
            integral, mass = conditional(raw_bin_probabilities(
                edges, TRUE_E_KEV, TRUE_TAU_PS, a))
            midpoint, midpoint_mass = conditional(raw_bin_probabilities(
                edges, TRUE_E_KEV, TRUE_TAU_PS, a, "midpoint"))
            normalizer.append(dict(angle_deg=a, integral_ROI_mass=mass,
                                   midpoint_ROI_mass=midpoint_mass))
            mismatch.append(dict(angle_deg=a,
                                  total_variation_at_truth=float(
                                      np.abs(integral - midpoint).sum() / 2)))
        exact_fit = fit_expected_histogram(edges, truth, "integral")
        midpoint_fit = fit_expected_histogram(edges, truth, "midpoint")
        recovery_error_fs = max(recovery_error_fs, abs(
            exact_fit["pseudo_true_tau_fs"] - 1000 * TRUE_TAU_PS))
        assert abs(exact_fit["pseudo_true_energy_keV"] - TRUE_E_KEV) < 1e-4
        assert abs(exact_fit["mean_KL_per_selected_photon"]) < 1e-10
        cases.append(dict(bin_width_keV=width, phase_fraction=phase,
                          ROI_edges_keV=[float(edges[0]), float(edges[-1])],
                          number_of_bins=len(edges)-1,
                          normalizers=normalizer, truth_shape_mismatch=mismatch,
                          exact_integral_fit=exact_fit, midpoint_fit=midpoint_fit))
    assert recovery_error_fs < 0.001

    information_cases = []
    fine_info = local_information(make_edges(0.5))
    information_step_error = 0.0
    for width in (0.5, 2.0, 5.0, 10.0, 20.0):
        matrix = local_information(make_edges(width))
        alternate = local_information(make_edges(width), step=5e-5)
        information_step_error = max(information_step_error, float(
            np.max(np.abs(matrix-alternate))/np.max(np.abs(matrix))))
        lost = fine_info-matrix
        lost_eigenvalues = np.linalg.eigvalsh(lost)
        assert lost_eigenvalues.min() > -1e-7
        # Chosen N=10000 selected photons per point-angle group.
        covariance = np.linalg.inv(10000*matrix)
        information_cases.append(dict(bin_width_keV=width,
                                      Fisher_coordinates=["log_tau", "energy_shift_keV"],
                                      Fisher_sum_per_photon_per_angle=matrix.tolist(),
                                      lost_information_eigenvalues=lost_eigenvalues.tolist(),
                                      chosen_N_per_angle=10000,
                                      local_tau_SE_fs=1000*TRUE_TAU_PS*math.sqrt(covariance[0, 0]),
                                      local_energy_SE_keV=math.sqrt(covariance[1, 1]),
                                      tau_energy_correlation=float(covariance[0, 1]/math.sqrt(
                                          covariance[0, 0]*covariance[1, 1]))))
    assert information_step_error < 1e-5

    # Independent event generator checks bin probabilities beyond quadrature.
    rng = np.random.default_rng(131425)
    count = 600000
    feed = rng.random(count) < KNOWN_ENTRY_FEED_FRACTION
    times = rng.exponential(TRUE_TAU_PS, count) + feed*rng.exponential(history.TAU3_PS, count)
    beta = history.BETA_IN + (history.BETA_EXIT-history.BETA_IN)*np.minimum(
        times/history.T_EXIT_PS, 1.0)
    cosine = math.cos(math.radians(150.0))
    d_em = (1-beta*cosine)/np.sqrt(1-beta**2)
    d_exit = (1-history.BETA_EXIT*cosine)/math.sqrt(1-history.BETA_EXIT**2)
    energy = TRUE_E_KEV*d_exit/d_em + rng.normal(0, SIGMA_KEV, count)
    photon_weight = 1/d_em**2
    edges = make_edges(5.0)
    selected = (energy >= edges[0]) & (energy < edges[-1])
    w = photon_weight[selected]
    weighted_count = np.histogram(energy[selected], edges, weights=w)[0]
    weighted_square_count = np.histogram(energy[selected], edges, weights=w*w)[0]
    mc = weighted_count/w.sum()
    analytic, _ = conditional(raw_bin_probabilities(edges, TRUE_E_KEV, TRUE_TAU_PS, 150.0))
    se = np.sqrt(((1-mc)**2*weighted_square_count
                  + mc**2*(np.sum(w*w)-weighted_square_count)))/w.sum()
    assert np.max(np.abs(mc-analytic)-5*se) < 2e-6
    valid = se > 1e-6
    mc_check = dict(seed=131425, generated_count=count,
                    selected_count=int(selected.sum()), angle_deg=150,
                    bin_width_keV=5.0, analytic=analytic.tolist(),
                    weighted_MC=mc.tolist(), MC_SE=se.tolist(),
                    maximum_abs_bin_difference=float(np.max(np.abs(mc-analytic))),
                    maximum_standardized_difference=float(np.max(np.abs(
                        mc[valid]-analytic[valid])/se[valid])))

    # Rebinning conserves integrated probabilities, including nonuniform bins.
    fine_edges = make_edges(0.5)
    for stride in (4, 10, 20, 40):
        coarse = fine_edges[::stride]
        for a in ANGLES:
            fine = raw_bin_probabilities(fine_edges, TRUE_E_KEV, TRUE_TAU_PS, a)
            large = raw_bin_probabilities(coarse, TRUE_E_KEV, TRUE_TAU_PS, a)
            error = np.max(np.abs(fine.reshape(-1, stride).sum(axis=1) - large))
            additivity_error = max(additivity_error, float(error))
    nonuniform = np.array([TRUE_E_KEV-140, TRUE_E_KEV-90, TRUE_E_KEV-50,
                          TRUE_E_KEV-15, TRUE_E_KEV-6, TRUE_E_KEV-1,
                          TRUE_E_KEV+2, TRUE_E_KEV+20])
    for a in ANGLES:
        bins = raw_bin_probabilities(nonuniform, TRUE_E_KEV, TRUE_TAU_PS, a)
        for lo, hi, expected in zip(nonuniform[:-1], nonuniform[1:], bins):
            numeric = quad(lambda x: float(history.density(
                np.array([x]), TRUE_E_KEV, TRUE_TAU_PS,
                KNOWN_ENTRY_FEED_FRACTION, a)[0]), lo, hi,
                epsabs=2e-10, points=[float(np.clip(TRUE_E_KEV, lo, hi))])[0]
            quadrature_error = max(quadrature_error, abs(expected - numeric))
        check = raw_bin_probabilities(nonuniform, TRUE_E_KEV,
                                       TRUE_TAU_PS, a, order=256)
        integral_order_error = max(integral_order_error,
                                    float(np.max(np.abs(bins-check))))
    assert additivity_error < 1e-12 and quadrature_error < 1e-8
    assert integral_order_error < 1e-10

    # Gaussian/no-slowing limit gives an independent closed form.
    static_edges = TRUE_E_KEV + np.array([-10.0, -2.0, 0.0, 3.0, 10.0])
    ratios, weights, _ = history.kernel(TRUE_TAU_PS,
                                        KNOWN_ENTRY_FEED_FRACTION, 150.0,
                                        beta_in=history.BETA_EXIT)
    assert np.max(np.abs(ratios - 1)) < 1e-12
    static = gaussian_interval((static_edges[:-1]-TRUE_E_KEV)/SIGMA_KEV,
                               (static_edges[1:]-TRUE_E_KEV)/SIGMA_KEV)
    mixed_static = gaussian_interval(
        (static_edges[:-1, None]-TRUE_E_KEV*ratios)/SIGMA_KEV,
        (static_edges[1:, None]-TRUE_E_KEV*ratios)/SIGMA_KEV) @ weights
    static_error = float(np.max(np.abs(static-mixed_static)))
    assert static_error < 1e-12
    # Stable interval evaluation retains positive far-tail bin probabilities.
    assert gaussian_interval(np.array([8.0]), np.array([9.0]))[0] > 0

    refinement = []
    for width in (1.0, 0.5, 0.25):
        edges = make_edges(width)
        p, _ = conditional(raw_bin_probabilities(edges, TRUE_E_KEV,
                                                 TRUE_TAU_PS, 150.0))
        q, _ = conditional(raw_bin_probabilities(edges, TRUE_E_KEV,
                                                 TRUE_TAU_PS, 150.0, "midpoint"))
        refinement.append(dict(bin_width_keV=width,
                               total_variation=float(np.abs(p-q).sum()/2)))
    assert refinement[2]["total_variation"] < refinement[1]["total_variation"]
    assert refinement[1]["total_variation"] < refinement[0]["total_variation"]

    # ROI changes carry their own conditional denominator, not an extra datum.
    roi_checks = []
    for offsets in ((-140.0, 20.0), (-80.0, 5.0), (-25.0, 3.0)):
        edges = TRUE_E_KEV + np.linspace(*offsets, 81)
        raw = raw_bin_probabilities(edges, TRUE_E_KEV, TRUE_TAU_PS, 150.0)
        p, mass = conditional(raw)
        direct = raw_bin_probabilities(edges[[0, -1]], TRUE_E_KEV,
                                       TRUE_TAU_PS, 150.0)[0]
        assert abs(mass-direct) < 1e-12 and abs(float(p.sum())-1) < 1e-12
        roi_checks.append(dict(offset_edges_keV=list(offsets),
                               selected_probability=mass,
                               normalized_probability_sum=float(p.sum())))

    return dict(schema_version=1, kind="synthetic finite-bin conditional lineshape",
                source_inspiration="BC84-2; not experimental rebinning or lifetime analysis",
                chosen_parameters=dict(rest_energy_keV=TRUE_E_KEV,
                                       proper_tau_ps=TRUE_TAU_PS,
                                       known_entry_feed_fraction=KNOWN_ENTRY_FEED_FRACTION,
                                       corrected_gaussian_sigma_keV=SIGMA_KEV,
                                       angles_deg=list(ANGLES),
                                       beta_in=history.BETA_IN,
                                       beta_exit=history.BETA_EXIT,
                                       proper_slowing_time_ps=history.T_EXIT_PS,
                                       upper_tau_ps=history.TAU3_PS),
                cases=cases, refinement=refinement, ROI_checks=roi_checks,
                local_information=information_cases, independent_event_MC=mc_check,
                verification=dict(bin_additivity_max_abs_error=additivity_error,
                                  independent_quad_max_abs_error=quadrature_error,
                                  order128_256_max_bin_difference=integral_order_error,
                                  Gaussian_limit_max_abs_error=static_error,
                                  exact_fit_max_tau_error_fs=recovery_error_fs,
                                  far_tail_interval_positive=True,
                                  midpoint_small_bin_convergence_passed=True,
                                  ROI_conditional_normalization_passed=True,
                                  independent_event_MC_passed=True,
                                  Fisher_derivative_step_relative_error=information_step_error,
                                  aligned_rebin_information_loss_PSD_passed=True,
                                  all_passed=True),
                dependencies=dict(kernel_file=history.__file__,
                                  kernel_sha256=hashlib.sha256(
                                      Path(history.__file__).read_bytes()).hexdigest(),
                                  numpy=np.__version__, scipy=scipy.__version__),
                boundaries=["Transport, entry feeding, point angles and response are fixed chosen inputs.",
                            "Fits use expected multinomial histograms with equal angle weights and free tau/E.",
                            "Coarse bins discard information; additivity is implementation consistency, not independence.",
                            "Fisher errors are local expected-model design values, not finite-sample coverage or reported source uncertainties.",
                            "All fit-start success flags are retained; no proof of a globally unique optimum.",
                            "No source rebin rule, sample count, background, data fit or interval is reproduced."])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output),
                      "verification": result["verification"],
                      "fits": [{"width_keV": c["bin_width_keV"],
                                "phase": c["phase_fraction"],
                                "tau_fs": c["midpoint_fit"]["pseudo_true_tau_fs"],
                                "energy_keV": c["midpoint_fit"]["pseudo_true_energy_keV"],
                                "KL": c["midpoint_fit"]["mean_KL_per_selected_photon"]}
                               for c in result["cases"]]}))


if __name__ == "__main__":
    main()
