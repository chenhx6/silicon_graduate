#!/usr/bin/env python3
"""Declared DSAM clock design and published-center contrasts, never a paper fit.

Inputs: exercise-contract-001.json in the Day18 run directory.  The quadrature
models a homogeneous exponential stopper, a direct/Erlang-feeding mixture,
finite angular acceptance, exact Doppler energies and Gaussian bin integrals.
It supplies no measured counts, experimental covariance or lifetime interval.
"""

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import gammainc, ndtr


def emission_density(t, tau, tau_feed, steps=3, direct_fraction=0.35):
    """Normalized density of Exp(tau) plus zero or steps feed waiting times."""
    r = 1 / tau_feed - 1 / tau
    if r <= 0:
        raise ValueError("This closed expression requires tau_feed < tau")
    direct = np.exp(-t / tau) / tau
    fed = np.exp(-t / tau) * gammainc(steps, r * t)
    fed /= tau * (tau_feed * r) ** steps
    return direct_fraction * direct + (1 - direct_fraction) * fed


def spectrum(s=1.0, tau=0.55, tau_feed=0.18, nodes=512, fixed_cut=None,
             spatial_length_um=None, distortion=0.0, window=False):
    # t is proper time in ps; E in keV, x in micrometres.  An autonomous
    # beta(proper-time) stopper is a declared effective homogeneous force.
    beta0, stop_ps, sigma_keV = 0.025, 0.45, 0.9
    z, w = leggauss(nodes)
    tmax = 40 * max(tau, tau_feed)
    if fixed_cut is not None:
        # Exact laboratory-clock cut for this exponential proper-time stopper:
        # t_lab=(stop_ps/s)*log[q(beta0)/q(beta)], q=tan(asin(beta)/2).
        q0 = beta0 / (1 + math.sqrt(1 - beta0 ** 2))
        qcut = q0 * math.exp(-s * fixed_cut / stop_ps)
        beta_cut = 2 * qcut / (1 + qcut ** 2)
        proper_cut = stop_ps / s * math.log(beta0 / beta_cut)
        tmax = min(tmax, proper_cut)
    t = (z + 1) * tmax / 2
    wt = w * tmax / 2 * emission_density(t, tau, tau_feed)
    u = s * t / stop_ps
    beta = beta0 * np.exp(-u - distortion * u * u / (1 + u))
    if spatial_length_um is not None:
        if distortion:
            raise ValueError("Spatial control uses only the exponential stopper")
        # dx/dt_proper=c*gamma*beta, integrated analytically.
        x_um = 299.792458 * stop_ps / s * (np.arcsin(beta0) - np.arcsin(beta))
        wt *= np.exp(-x_um / spatial_length_um)
    angular_x, angular_w = leggauss(8)
    edges = np.linspace(570.0, 630.0, 121)
    all_rings = []
    for angle_deg in (37.0, 79.0, 143.0):
        lo, hi = np.cos(np.radians([angle_deg + 5, angle_deg - 5]))
        mu = (lo + hi) / 2 + (hi - lo) / 2 * angular_x
        # Uniform solid-angle acceptance within this cone/ring segment.
        angular_probability = angular_w / 2
        doppler = 600 * np.sqrt(1 - beta[:, None] ** 2)
        doppler = doppler / (1 - beta[:, None] * mu[None, :])
        cdf = ndtr((edges[None, None, :] - doppler[:, :, None]) / sigma_keV)
        bins = np.diff(cdf, axis=2)
        all_rings.append(np.einsum("t,a,tab->b", wt, angular_probability, bins))
    bins = np.asarray(all_rings)
    if window:
        # A declared energy-only selection, not a reconstructed paper gate.
        bins *= (edges[:-1] >= 600.5)[None, :]
    return bins, float(wt.sum())


def normalized_shape_distance(a, b):
    a, b = a / a.sum(axis=1, keepdims=True), b / b.sum(axis=1, keepdims=True)
    return float(np.max(np.abs(a - b)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    contract = json.loads(args.contract.read_text())
    checks = []

    def check(name, ok, **evidence):
        checks.append({"name": name, "passed": bool(ok), **evidence})

    base, integral = spectrum()
    check("probability_normalization", abs(integral - 1) < 2e-12,
          integrated_emission_probability=integral)
    variants = []
    for a in (0.4, 0.75, 1.25, 2.0):
        scaled, _ = spectrum(s=a, tau=0.55 / a, tau_feed=0.18 / a)
        delta = float(np.max(np.abs(scaled - base)))
        check(f"full_shape_clock_symmetry_{a}", delta < 3e-13, max_bin_delta=delta)
        gated_base, _ = spectrum(window=True)
        gated_scaled, _ = spectrum(s=a, tau=0.55 / a, tau_feed=0.18 / a, window=True)
        gated_delta = float(np.max(np.abs(gated_scaled - gated_base)))
        check(f"energy_gate_preserves_clock_symmetry_{a}", gated_delta < 3e-13,
              max_bin_delta=gated_delta)
        variants.append({"a": a, "tau_ps": 0.55 / a,
                         "feed_step_tau_ps": 0.18 / a,
                         "strength_multiplier": a, "Qt_multiplier": math.sqrt(a),
                         "max_bin_delta": delta})
    refined, _ = spectrum(nodes=768)
    coarser, _ = spectrum(nodes=384)
    check("quadrature_512_to_768", np.max(np.abs(base - refined)) < 3e-11,
          max_bin_delta=float(np.max(np.abs(base - refined))))
    check("quadrature_384_to_768", np.max(np.abs(coarser - refined)) < 3e-10,
          max_bin_delta=float(np.max(np.abs(coarser - refined))))
    # Analytic velocity moments: product of Laplace transforms of independent
    # direct/fed waiting times. This is independent of the Gaussian bin integral.
    z, w = leggauss(768)
    t = (z + 1) * 40 * 0.55 / 2
    wt = w * 40 * 0.55 / 2 * emission_density(t, 0.55, 0.18)
    for power in (0, 1, 2, 5):
        k = power / 0.45
        analytic = (0.35 + 0.65 / (1 + k * 0.18) ** 3) / (1 + k * 0.55)
        numeric = float(np.sum(wt * np.exp(-k * t)))
        check(f"Laplace_velocity_moment_{power}", abs(numeric - analytic) < 2e-12,
              analytic=analytic, quadrature=numeric)
    controls = {}
    controls["stopping_only"] = (base, spectrum(s=1.25)[0])
    controls["fixed_feeding_clock"] = (
        base, spectrum(s=1.25, tau=0.55 / 1.25, tau_feed=0.18)[0])
    controls["fixed_time_window_0.4ps"] = (
        spectrum(fixed_cut=0.4)[0],
        spectrum(s=1.25, tau=0.55 / 1.25, tau_feed=0.18 / 1.25,
                 fixed_cut=0.4)[0])
    controls["fixed_spatial_response_2um"] = (
        spectrum(spatial_length_um=2.0)[0],
        spectrum(s=1.25, tau=0.55 / 1.25, tau_feed=0.18 / 1.25,
                 spatial_length_um=2.0)[0])
    controls["stopping_shape_distortion"] = (
        base, spectrum(s=1.25, tau=0.55 / 1.25, tau_feed=0.18 / 1.25,
                       distortion=0.2)[0])
    control_results = {}
    for name, (a, b) in controls.items():
        distance = normalized_shape_distance(a, b)
        check(f"counterinput_{name}", distance > 1e-5,
              max_normalized_bin_delta=distance)
        control_results[name] = {"max_normalized_bin_delta": distance,
                                 "acceptance_ratio_per_ring": (b.sum(axis=1) / a.sum(axis=1)).tolist()}
    # The ideal centroid at 90deg is NOT a division by cos(theta) observable.
    # This design tests speed moments and complete shapes, not centroid F(90).
    source = contract["published_input"]
    b1 = list(map(Fraction, source["B1_e2b2"]))
    b2 = list(map(Fraction, source["B2_e2b2"]))
    ratios = [y / x for x, y in zip(b1, b2)]
    i_max, i_min = int(np.argmax(ratios)), int(np.argmin(ratios))
    double_ratio = max(ratios) / min(ratios)
    check("fresh_table_double_ratio_exact", double_ratio == Fraction(77, 4),
          exact=str(double_ratio), numerator_spin=source["spin"][i_max],
          denominator_spin=source["spin"][i_min])
    for a1, a2 in ((1.0, 1.25), (0.4, 2.0), (2.0, 0.4)):
        changed = [float(r) * a2 / a1 for r in ratios]
        got = max(changed) / min(changed)
        check(f"two_band_constant_scales_{a1}_{a2}", abs(got - float(double_ratio)) < 2e-13,
              double_ratio=got)
    central_range = float(double_ratio)
    threshold = (math.sqrt(central_range) - 1) / (math.sqrt(central_range) + 1)
    boxes = [{"self_chosen_fraction": d,
              "double_ratio_lower_bound": central_range * ((1 - d) / (1 + d)) ** 2,
              "not_experimental_CI": True} for d in (0.10, 0.20)]
    check("fractional_box_threshold_algebra",
          abs(central_range * ((1 - threshold) / (1 + threshold)) ** 2 - 1) < 1e-12,
          self_chosen_box_halfwidth_needed_for_extreme_central_closure=threshold)
    # Jensen quoted mean Qt are used only for a conditional differential-clock
    # sensitivity. Its already-added 5percent does not define a probability box.
    jensen_ratio = Fraction(83, 74)
    result = {
        "contract_sha256": hashlib.sha256(args.contract.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "new Day18 analytic/numerical design; published centers only; no experimental refit, profile, covariance or CI",
        "clock_transform": "s -> a*s, all lifetime/feeding means -> mean/a; same shape under homogeneous fixed-position-response assumptions",
        "clock_variants": variants,
        "counterinputs": control_results,
        "mu08_published_central_contrasts": {
            "spins": source["spin"], "B2_over_B1_exact": [str(r) for r in ratios],
            "B2_over_B1": list(map(float, ratios)),
            "double_ratio_R17_over_R18_exact": str(double_ratio),
            "double_ratio_R17_over_R18": central_range,
            "best_possible_worst_multiplicative_residual_under_free_relative_band_scale": math.sqrt(central_range),
            "per_strength_symmetric_log_box_threshold": math.log(central_range) / 4,
            "per_strength_multiplicative_threshold": central_range ** 0.25,
            "per_strength_symmetric_fractional_box_threshold": threshold,
            "illustrative_boxes": boxes,
            "probability_interpretation": "none; no use of printed marginal errors as joint confidence region",
            "literal_prose_boundary": "PDF5 says factors2to3; printedI17 central ratio5.5 andI18 inverse3.5; preserve both, no inferrederratum",
        },
        "jensen_mean_Qt_sensitivity": {
            "Qt541_over_Qt411": float(jensen_ratio),
            "a541_over_a411_for_equal_corrected_Qt": float(1 / jensen_ratio ** 2),
            "not_estimated_stopping_bias_or_error_probability": True,
        },
        "checks": checks,
        "checks_passed": sum(c["passed"] for c in checks),
        "checks_total": len(checks),
        "all_passed": all(c["passed"] for c in checks),
    }
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"output": str(args.output), "all_passed": result["all_passed"],
                      "checks": f"{result['checks_passed']}/{result['checks_total']}",
                      "mu08_double_ratio": central_range, "box_threshold": threshold}))
    if not result["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
