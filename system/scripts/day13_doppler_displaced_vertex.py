#!/usr/bin/env python3
"""Synthetic decay-vertex displacement and feeding checks for Day13.

Constant lab beta, collinear motion, exponential proper lifetimes, infinitesimal
planar detector with fixed normal, and isotropic rest emission are declared.
Stopping, photon recoil, particle gates and time response are absent.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.laguerre import laggauss


C_MM_PER_PS = .299792458


def decay_pdf_cdf(time_ps, level_tau_ps, feeder_tau_ps=0.):
    if feeder_tau_ps == 0:
        return 1 - math.exp(-time_ps / level_tau_ps)
    if abs(feeder_tau_ps / level_tau_ps - 1) < 1e-10:
        x = time_ps / level_tau_ps
        return 1 - math.exp(-x) * (1 + x)
    survival = (feeder_tau_ps * math.exp(-time_ps / feeder_tau_ps) -
                level_tau_ps * math.exp(-time_ps / level_tau_ps)) / (feeder_tau_ps - level_tau_ps)
    return 1 - survival


def moments(beta, radius_mm, theta_deg, level_tau_ps, feeder_tau_ps=0., order=64):
    nodes, weights = laggauss(order)
    if feeder_tau_ps:
        times = level_tau_ps * nodes[:, None] + feeder_tau_ps * nodes[None, :]
        integration_weights = weights[:, None] * weights[None, :]
    else:
        times = level_tau_ps * nodes
        integration_weights = weights
    gamma = 1 / math.sqrt(1 - beta**2)
    theta = math.radians(theta_deg)
    c0 = math.cos(theta)
    d = beta * gamma * C_MM_PER_PS * times
    distance = np.sqrt(radius_mm**2 + d**2 - 2 * radius_mm * d * c0)
    cosine = (radius_mm * c0 - d) / distance
    # Correct all events with the original target direction instead of the
    # physical emission-vertex direction. E0 is chosen as 1000keV.
    residual = 1000 * ((1 - beta * c0) / (1 - beta * cosine) - 1)
    # Detection weight: lab angular bunching * projected area / R(t)^2.
    projection = np.maximum(0., (radius_mm - d * c0) / distance)
    weight_detect = ((1 - beta**2) / (1 - beta * cosine)**2 *
                     projection * radius_mm**2 / distance**2)
    weighted = integration_weights * weight_detect
    norm = float(np.sum(weighted))
    mean = float(np.sum(weighted * residual) / norm)
    variance = float(np.sum(weighted * (residual - mean)**2) / norm)
    unweighted_mean = float(np.sum(integration_weights * residual))
    mean_flight = beta * gamma * C_MM_PER_PS * (level_tau_ps + feeder_tau_ps)
    leading_mean = -1000 * beta * mean_flight / radius_mm * math.sin(theta)**2 / (1 - beta * c0)
    leading_sigma = (1000 * beta**2 * gamma * C_MM_PER_PS / radius_mm * math.sin(theta)**2 /
                     (1 - beta * c0) * math.sqrt(level_tau_ps**2 + feeder_tau_ps**2))
    return {"mean_residual_detected_keV": mean, "sigma_detected_keV": math.sqrt(variance),
            "unweighted_mean_residual_keV": unweighted_mean,
            "relative_detection_weight_integral": norm,
            "mean_flight_mm_unconditional": mean_flight,
            "leading_small_displacement_mean_keV": leading_mean,
            "leading_small_displacement_sigma_keV": leading_sigma}


def calculate(seed=1317, samples=500_000):
    rows = []
    worst_mean_diff, worst_sigma_diff = 0., 0.
    for beta, radius, tau, feeder in ((.07, 235., 5., 0.), (.07, 235., 50., 0.),
                                     (.3, 150., 2., 0.), (.3, 150., 2., 20.),
                                     (.5, 150., 10., 0.)):
        for theta in (35, 90, 145):
            a = moments(beta, radius, theta, tau, feeder, order=48)
            b = moments(beta, radius, theta, tau, feeder, order=96)
            dm = abs(a["mean_residual_detected_keV"] - b["mean_residual_detected_keV"])
            ds = abs(a["sigma_detected_keV"] - b["sigma_detected_keV"])
            worst_mean_diff, worst_sigma_diff = max(worst_mean_diff, dm), max(worst_sigma_diff, ds)
            rows.append({"beta": beta, "radius_mm": radius, "theta_nominal_deg": theta,
                         "proper_level_tau_ps": tau, "proper_feeder_tau_ps": feeder, **b})
    rng = np.random.default_rng(seed)
    direct = rng.exponential(2., samples)
    feed = direct + rng.exponential(20., samples)
    gate = 10.
    direct_p = decay_pdf_cdf(gate, 2.)
    feeding_p = decay_pdf_cdf(gate, 2., 20.)
    direct_mc, feeding_mc = float(np.mean(direct <= gate)), float(np.mean(feed <= gate))
    assert abs(direct_mc - direct_p) < .003 and abs(feeding_mc - feeding_p) < .003
    static = moments(0., 150., 90., 50.)
    assert abs(static["mean_residual_detected_keV"]) < 1e-12 and static["sigma_detected_keV"] < 1e-12
    assert worst_mean_diff < 1e-6 and worst_sigma_diff < 1e-6
    assert all(r["mean_residual_detected_keV"] < 0 for r in rows)
    assert abs(decay_pdf_cdf(10., 2., 2.) - (1 - 6 * math.exp(-5))) < 1e-12
    return {"schema_version": 1, "kind": "displaced-vertex/feeding method toy; no lifetime or real spectrum refit",
            "rows": rows, "toy_time_gate_ps": gate,
            "time_gate": {"level_tau_ps": 2., "feeder_tau_ps": 20.,
                          "direct_probability": direct_p, "feeding_probability": feeding_p,
                          "direct_MC": direct_mc, "feeding_MC": feeding_mc,
                          "boundary": "ideal proper-time gate; actual gamma-particle timestamps need flight paths and response"},
            "assumptions": {"E0_keV": 1000., "constant_beta": True, "proper_time_dilation": True,
                            "emission": "isotropic rest photons per decay", "detector": "small planar area facing nominal vertex",
                            "missing": "stopping, photon recoil, finite detector size, angular alignment, event cuts, response/covariance"},
            "seed": seed, "samples": samples,
            "verification": {"max_mean_quad48_96_difference_keV": worst_mean_diff,
                             "max_sigma_quad48_96_difference_keV": worst_sigma_diff,
                             "static_limit_passed": True, "feeding_CDF_MC_passed": True,
                             "equal_lifetime_Erlang_limit_passed": True, "passed": True},
            "numpy_version": np.__version__}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", required=True, type=Path)
    p.add_argument("--seed", type=int, default=1317)
    p.add_argument("--samples", type=int, default=500_000)
    a = p.parse_args()
    if a.samples < 1000:
        p.error("--samples must be at least 1000")
    r = calculate(a.seed, a.samples)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(r, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(a.output), "verification": r["verification"]}))


if __name__ == "__main__":
    main()
