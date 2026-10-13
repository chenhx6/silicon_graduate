#!/usr/bin/env python3
"""Synthetic Day13 geometry, finite-bin and peak-gate checks, not a data refit.

Source-inspired plane separations/noise scale are from Vandebrouck 2016.
Photon directions, beta, response, gates, and independence are explicit exercise
choices. Published FWHM or timing figures are not fitted here.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def correction(energy, beta, theta):
    return energy * (1 - beta * np.cos(theta)) / np.sqrt(1 - beta**2)


def laboratory(e0, beta, theta):
    return e0 * np.sqrt(1 - beta**2) / (1 - beta * np.cos(theta))


def gate_fraction(half_width, mean_shift, sigma):
    if sigma == 0:
        return float(abs(mean_shift) <= half_width)
    return 0.5 * (math.erf((half_width - mean_shift) / (math.sqrt(2) * sigma)) -
                  math.erf((-half_width - mean_shift) / (math.sqrt(2) * sigma)))


def finite_bin(theta0, half_width, beta=0.07, e0=1000, order=128):
    # Uniform polar-angle bin: this is neither a uniform solid-angle nor a
    # nuclear angular distribution. Its measure is a stated toy input.
    points, weights = leggauss(order)
    theta = theta0 + half_width * points
    energy = laboratory(e0, beta, theta)
    center_corrected = correction(energy, beta, theta0)
    mean = float(np.dot(weights, center_corrected) / 2)
    variance = float(np.dot(weights, (center_corrected - mean)**2) / 2)
    point_corrected = correction(energy, beta, theta)
    c = math.cos(theta0)
    denom = 1 - beta * c
    # d^2 E_lab/dtheta^2 divided by E_lab, holding beta fixed.
    curvature = -beta * c / denom + 2 * beta**2 * math.sin(theta0)**2 / denom**2
    approximation_bias = 0.5 * e0 * curvature * half_width**2 / 3
    return {"mean_bias_keV": mean - e0, "sigma_keV": math.sqrt(variance),
            "second_order_mean_bias_keV": approximation_bias,
            "max_eventwise_residual_keV": float(np.max(np.abs(point_corrected - e0)))}


def calculate(seed=1314, samples=300_000):
    rng = np.random.default_rng(seed)
    l1, separation, s1, s2 = 174., 105., .073, .084
    l2, radius, e0, beta = l1 + separation, 235., 1000., .07
    # x_target=(L2*x1-L1*x2)/D ; alpha=atan((x2-x1)/D).
    transform = np.array([[l2 / separation, -l1 / separation],
                          [-1 / separation, 1 / separation]])
    covariance = transform @ np.diag([s1**2, s2**2]) @ transform.T
    errors = rng.normal(size=(samples, 2)) * [s1, s2]
    xt = errors @ transform[0]
    alpha = np.arctan((errors[:, 1] - errors[:, 0]) / separation)
    geometry_rows = []
    max_sigma_difference = 0.
    for degrees in (35, 60, 90, 120, 145):
        theta = math.radians(degrees)
        elab = laboratory(e0, beta, theta)
        # Gamma hit is fixed in space; changing reconstructed target changes
        # its direction and changing alpha changes recoil direction.
        gamma_theta = np.arctan2(radius * math.sin(theta) - xt, radius * math.cos(theta))
        relative_theta = gamma_theta - alpha
        corrected = correction(elab, beta, relative_theta)
        jtheta = e0 * beta * math.sin(theta) / (1 - beta * math.cos(theta))
        j = jtheta * np.array([-math.cos(theta) / radius, -1.])
        full = float(math.sqrt(j @ covariance @ j))
        diagonal = float(math.sqrt(np.dot(j**2, np.diag(covariance))))
        observed = float(np.std(corrected, ddof=1))
        max_sigma_difference = max(max_sigma_difference, abs(observed / full - 1))
        # Numerical derivative from the primitive independent plane coordinates.
        def from_planes(x1, x2):
            target = (l2 * x1 - l1 * x2) / separation
            a = math.atan((x2 - x1) / separation)
            ng = math.atan2(radius * math.sin(theta) - target, radius * math.cos(theta))
            return float(correction(elab, beta, ng - a))
        finite = np.array([(from_planes(1e-4, 0) - from_planes(-1e-4, 0)) / 2e-4,
                           (from_planes(0, 1e-4) - from_planes(0, -1e-4)) / 2e-4])
        primitive = j @ transform
        assert np.max(np.abs(finite - primitive)) < 1e-6
        geometry_rows.append({"theta_deg": degrees, "full_covariance_sigma_keV": full,
                              "diagonal_only_sigma_keV": diagonal, "MC_sigma_keV": observed,
                              "diagonal_over_full_ratio": diagonal / full,
                              "mean_bias_MC_keV": float(np.mean(corrected) - e0),
                              "primitive_plane_derivatives_keV_per_mm": primitive.tolist(),
                              "finite_difference_derivatives": finite.tolist()})
    bin_rows = []
    for degrees in (35, 90, 145):
        for half_width_deg in (1, 5, 10):
            a = finite_bin(math.radians(degrees), math.radians(half_width_deg), order=64)
            b = finite_bin(math.radians(degrees), math.radians(half_width_deg), order=128)
            assert abs(a["mean_bias_keV"] - b["mean_bias_keV"]) < 1e-9
            bin_rows.append({"theta_deg": degrees, "half_bin_deg": half_width_deg, **b})
    # A fixed +/-3-keV rest-energy gate around a synthetic line. Response and
    # line widths are invented Gaussian examples, not AGATA measured values.
    gate_rows = []
    sigmas = {35: 2.3779657635, 90: 2.6448476435, 145: 2.3952111749}
    true_ratio = 1.30
    for sbias in (0., .001, .002):
        for degrees in (35, 90, 145):
            theta = math.radians(degrees)
            mean = float(correction(laboratory(e0, beta, theta), beta + sbias, theta) - e0)
            fraction = gate_fraction(3., mean, sigmas[degrees])
            gate_rows.append({"beta_bias": sbias, "theta_deg": degrees,
                              "mean_residual_keV": mean, "assumed_sigma_keV": sigmas[degrees],
                              "gate_acceptance": fraction})
    gates_by_key = {(r["beta_bias"], r["theta_deg"]): r["gate_acceptance"] for r in gate_rows}
    observed_ratio = true_ratio * gates_by_key[(.002, 145)] / gates_by_key[(.002, 90)]
    equal_width_baseline = gate_fraction(3., 0., 2.5)
    ratio_rows = [{"beta_bias": b, "true_N145_over_N90": true_ratio,
                   "gated_N145_over_N90": true_ratio * gates_by_key[(b, 145)] / gates_by_key[(b, 90)]}
                  for b in (0., .001, .002)]
    zeros = finite_bin(math.pi / 3, math.radians(10), beta=0.)
    assert abs(zeros["mean_bias_keV"]) < 1e-10 and zeros["sigma_keV"] < 1e-10
    assert max(r["max_eventwise_residual_keV"] for r in bin_rows) < 1e-10
    assert max_sigma_difference < .012
    assert gate_fraction(1000., 0., 2.5) == 1.
    assert abs(gate_fraction(3., 0., 2.5) - gate_fraction(3., -0., 2.5)) < 1e-14
    assert observed_ratio < true_ratio
    return {"schema_version": 1, "kind": "source-inspired synthetic method checks; no experimental refit",
            "seed": seed, "samples": samples,
            "geometry_inputs": {"L1_mm": l1, "L2_mm": l2, "sigma_x1_mm": s1,
                                "sigma_x2_mm": s2, "photon_radius_mm": radius, "E0_keV": e0, "beta": beta},
            "target_angle_covariance_mm_rad": covariance.tolist(),
            "target_angle_correlation": float(covariance[0, 1] / math.sqrt(covariance[0, 0] * covariance[1, 1])),
            "geometry_rows": geometry_rows, "finite_polar_bin_rows": bin_rows,
            "gate_half_width_keV": 3., "gate_rows": gate_rows, "gate_ratio_rows": ratio_rows,
            "equal_width_zero_bias_reference_gate": equal_width_baseline,
            "verification": {"max_geometry_MC_relative_difference": max_sigma_difference,
                             "finite_bin_64_128_convergence": True, "static_limit_passed": True,
                             "eventwise_exact_inversion_passed": True, "plane_jacobian_passed": True,
                             "passed": True}, "numpy_version": np.__version__}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--seed", type=int, default=1314)
    p.add_argument("--samples", type=int, default=300_000)
    args = p.parse_args()
    if args.samples < 1000:
        p.error("--samples must be at least 1000")
    result = calculate(args.seed, args.samples)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "verification": result["verification"]}))


if __name__ == "__main__":
    main()
