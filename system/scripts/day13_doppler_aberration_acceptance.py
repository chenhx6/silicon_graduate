#!/usr/bin/env python3
"""Finite-acceptance Lorentz angle/energy exercises from Longfellow Eq.(2).

Counts are per emitted photon, not a time-dependent relativistic intensity.
Full-azimuth bins, angular coefficients and energy-dependent efficiency are
explicit toys, not the GRETINA array's calibration or measured distribution.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


def rest_cosine(lab_cosine, beta):
    return (lab_cosine - beta) / (1 - beta * lab_cosine)


def lab_cosine(rest_cosine_value, beta):
    return (rest_cosine_value + beta) / (1 + beta * rest_cosine_value)


def jacobian(lab_cosine_value, beta):
    return (1 - beta**2) / (1 - beta * lab_cosine_value)**2


def wstar(cosine, a2=0., a4=0.):
    p2 = (3 * cosine**2 - 1) / 2
    p4 = (35 * cosine**4 - 30 * cosine**2 + 3) / 8
    return 1 + a2 * p2 + a4 * p4


def integrate_bin(degrees, beta, a2=0., a4=0., half=5., order=128, efficiency=False):
    low = math.cos(math.radians(degrees + half))
    high = math.cos(math.radians(degrees - half))
    points, weights = leggauss(order)
    labc = (high + low) / 2 + (high - low) * points / 2
    density = .5 * wstar(rest_cosine(labc, beta), a2, a4) * jacobian(labc, beta)
    if efficiency:
        # epsilon(E_lab)=0.5*(E_lab/E0)^(-0.8), chosen only as a toy.
        ratio = math.sqrt(1 - beta**2) / (1 - beta * labc)
        eps = np.clip(.5 * ratio**-.8, .01, .99)
        density *= eps
    return float((high - low) * np.dot(weights, density) / 2)


def calculate(seed=1316, samples=400_000):
    rng = np.random.default_rng(seed)
    points, weights = leggauss(256)
    rest_draws = rng.uniform(-1, 1, samples)
    rows, maximum_mc_error, maximum_energy_error = [], 0., 0.
    for beta in (0., .016, .07, .3, .5):
        gamma = 1 / math.sqrt(1 - beta**2)
        lab_draws = lab_cosine(rest_draws, beta)
        # E0=1000keV fixed, still the lab angles bunch forward after E correction.
        elab = 1000 * gamma * (1 + beta * rest_draws)
        corrected = elab * gamma * (1 - beta * lab_draws)
        maximum_energy_error = max(maximum_energy_error, float(np.max(np.abs(corrected - 1000))))
        for a2, a4 in ((0., 0.), (.3, .1)):
            normalization = float(.5 * np.dot(weights, wstar(rest_cosine(points, beta), a2, a4) * jacobian(points, beta)))
            assert abs(normalization - 1) < 1e-12
        bins = []
        for degrees in (35, 90, 145):
            low, high = math.cos(math.radians(degrees + 5)), math.cos(math.radians(degrees - 5))
            observed = float(np.mean((lab_draws >= low) & (lab_draws <= high)))
            exact = integrate_bin(degrees, beta)
            maximum_mc_error = max(maximum_mc_error, abs(observed / exact - 1))
            biased = integrate_bin(degrees, beta, efficiency=True)
            bins.append({"lab_bin_center_deg": degrees, "lab_half_bin_deg": 5,
                         "isotropic_probability_exact": exact, "isotropic_probability_MC": observed,
                         "toy_efficiency_weighted_probability": biased,
                         "rest_frame_edges_deg": [math.degrees(math.acos(rest_cosine(high, beta))),
                                                 math.degrees(math.acos(rest_cosine(low, beta)))],
                         "anisotropic_a2_0_3_a4_0_1_probability": integrate_bin(degrees, beta, .3, .1)})
        solid_angle_145 = math.cos(math.radians(140)) - math.cos(math.radians(150))
        solid_angle_90 = math.cos(math.radians(85)) - math.cos(math.radians(95))
        density_ratio = (bins[2]["isotropic_probability_exact"] / solid_angle_145 /
                         (bins[1]["isotropic_probability_exact"] / solid_angle_90))
        weighted_ratio = (bins[2]["toy_efficiency_weighted_probability"] / solid_angle_145 /
                          (bins[1]["toy_efficiency_weighted_probability"] / solid_angle_90))
        rows.append({"beta": beta, "J_forward": float(jacobian(1., beta)),
                     "J_90": float(jacobian(0., beta)), "J_backward": float(jacobian(-1., beta)),
                     "bins": bins, "solid_angle_normalized_lab_density_145_over_90": density_ratio,
                     "same_density_ratio_with_toy_epsilon_lab": weighted_ratio})
    step = 1e-6
    for beta in (0., .07, .5):
        for c in (-.8, 0., .8):
            derivative = (rest_cosine(c + step, beta) - rest_cosine(c - step, beta)) / (2 * step)
            assert abs(derivative / jacobian(c, beta) - 1) < 1e-8
    assert maximum_energy_error < 1e-10
    assert maximum_mc_error < .04
    assert abs(rows[0]["solid_angle_normalized_lab_density_145_over_90"] - 1.) < 1e-14
    return {"schema_version": 1, "kind": "synthetic Lorentz angle/energy/finite acceptance exercise",
            "seed": seed, "samples": samples, "rows": rows,
            "assumptions": {"source": "Longfellow2026 Eq2 and Eq18", "E0_keV": 1000.,
                            "counting_measure": "per emitted photon; full azimuth", "epsilon_toy": "clip(0.5*(Elab/E0)^(-0.8),0.01,0.99)",
                            "response_not_included": "GRETINA actual angular coverage, polarization, feeding, tails, covariance"},
            "verification": {"angle_density_normalization_passed": True,
                             "jacobian_finite_difference_passed": True, "static_limit_passed": True,
                             "max_MC_bin_relative_difference": maximum_mc_error,
                             "max_energy_inverse_error_keV": maximum_energy_error, "passed": True},
            "numpy_version": np.__version__}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--seed", type=int, default=1316)
    p.add_argument("--samples", type=int, default=400_000)
    a = p.parse_args()
    if a.samples < 1000:
        p.error("--samples must be at least 1000")
    r = calculate(a.seed, a.samples)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(r, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(a.output), "verification": r["verification"]}))


if __name__ == "__main__":
    main()
