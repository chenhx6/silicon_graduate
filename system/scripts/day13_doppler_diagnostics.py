#!/usr/bin/env python3
"""Reproduce the Day 13 synthetic Doppler exercises; no experimental fit.

Energies are keV, beta is dimensionless, internal angles are radians.
Source equation: Mavela 2019 Eqs. (4.5), (4.6); stopping is an explicitly
invented exponential toy, not a replay of Klemme 1999 or Mavela data.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def correction(energy, beta, theta):
    return energy * (1 - beta * np.cos(theta)) / np.sqrt(1 - beta**2)


def laboratory(energy, beta, theta):
    return energy * np.sqrt(1 - beta**2) / (1 - beta * np.cos(theta))


def jacobian(energy: float, beta: float, theta: float) -> np.ndarray:
    gamma = 1 / math.sqrt(1 - beta**2)
    c = math.cos(theta)
    return np.array([
        gamma * (1 - beta * c),
        energy * (gamma**3 * beta * (1 - beta * c) - gamma * c),
        energy * gamma * beta * math.sin(theta),
    ])


def calculate(samples: int = 200_000, seed: int = 1313) -> dict:
    if samples < 1000:
        raise ValueError("at least 1000 draws are required for this MC comparison")
    rng = np.random.default_rng(seed)
    e0, beta, se, sb, st = 1000.0, 0.07, 1.0, 0.002, math.radians(2)
    rows, worst_fd, worst_mc = [], 0.0, 0.0
    for degrees in (35, 90, 145):
        theta = math.radians(degrees)
        elab = float(laboratory(e0, beta, theta))
        values = np.array([elab, beta, theta])
        j = jacobian(elab, beta, theta)
        finite = []
        for axis, step in enumerate((1e-3, 1e-6, 1e-6)):
            delta = np.zeros(3)
            delta[axis] = step
            finite.append(float((correction(*(values + delta)) -
                                 correction(*(values - delta))) / (2 * step)))
        fd_error = float(np.max(np.abs(np.array(finite) - j) / np.maximum(1, np.abs(j))))
        worst_fd = max(worst_fd, fd_error)
        terms = j * np.array([se, sb, st])
        sigma = float(np.linalg.norm(terms))
        covariance_rows = []
        for rho in (-0.8, 0.0, 0.8):
            cov = np.diag([se**2, sb**2, st**2])
            cov[1, 2] = cov[2, 1] = rho * sb * st
            assert np.min(np.linalg.eigvalsh(cov)) > 0
            predicted = float(math.sqrt(j @ cov @ j))
            draws = rng.multivariate_normal(values, cov, size=samples)
            assert np.all((draws[:, 1] >= 0) & (draws[:, 1] < 1))
            corrected = correction(draws[:, 0], draws[:, 1], draws[:, 2])
            observed = float(np.std(corrected, ddof=1))
            relative = abs(observed / predicted - 1)
            worst_mc = max(worst_mc, relative)
            covariance_rows.append({"rho_beta_theta": rho, "sigma_linear_keV": predicted,
                                    "sigma_MC_keV": observed, "relative_difference": relative,
                                    "mean_bias_MC_keV": float(np.mean(corrected) - e0)})
        rows.append({"theta_deg": degrees, "E_lab_keV": elab,
                     "E_corrected_keV": float(correction(elab, beta, theta)),
                     "signed_terms_energy_beta_theta_keV": terms.tolist(),
                     "sigma_independent_keV": sigma,
                     "sigma_independent_FWHM_keV": 2.354820045 * sigma,
                     "jacobian": j.tolist(), "finite_difference_relative_error": fd_error,
                     "covariance_examples": covariance_rows})
    # Low-beta variance ambiguity: V(theta) = A + B cos^2(theta) + C sin^2(theta).
    theta_grid = np.radians([0, 35, 60, 90, 120, 145, 180])
    design = np.column_stack([np.ones(len(theta_grid)), np.cos(theta_grid)**2,
                              np.sin(theta_grid)**2])
    original = np.array([1.0, (e0 * sb)**2, (e0 * beta * st)**2])
    equivalent = original + np.array([1.0, -1.0, -1.0])
    ambiguity = {"model": "low-beta; independent constant response/velocity/angular variances",
                 "columns": ["1", "cos(theta)^2", "sin(theta)^2"],
                 "rank": int(np.linalg.matrix_rank(design)),
                 "singular_values": np.linalg.svd(design, compute_uv=False).tolist(),
                 "original_ABC_keV2": original.tolist(),
                 "equivalent_ABC_keV2": equivalent.tolist(),
                 "equivalent_sigma_response_keV": float(math.sqrt(equivalent[0])),
                 "equivalent_sigma_beta": float(math.sqrt(equivalent[1]) / e0),
                 "equivalent_sigma_theta_deg": math.degrees(math.sqrt(equivalent[2]) / (e0 * beta)),
                 "max_variance_difference_keV2": float(np.max(np.abs(design @ original - design @ equivalent)))}
    # No feeding, fixed direction, exponential emission and slowing; chosen tau=ts.
    ts, tau, initial_beta = 1.1, 1.1, 0.016
    times = rng.exponential(tau, samples)
    speeds = initial_beta * np.exp(-times / ts)
    mean_beta = initial_beta / (1 + tau / ts)
    var_beta = initial_beta**2 / (1 + 2 * tau / ts) - mean_beta**2
    stopping_rows = []
    for degrees in (35, 90, 145):
        theta = math.radians(degrees)
        photons = laboratory(e0, speeds, theta)
        errors = correction(photons, initial_beta, theta) - e0
        stopping_rows.append({"theta_deg": degrees, "exact_MC_mean_residual_keV": float(np.mean(errors)),
                              "exact_MC_sigma_keV": float(np.std(errors, ddof=1)),
                              "first_order_mean_residual_keV": e0 * (mean_beta - initial_beta) * math.cos(theta),
                              "first_order_sigma_keV": e0 * abs(math.cos(theta)) * math.sqrt(var_beta)})
    invariant_error = max(abs(correction(laboratory(e0, b, t), b, t) - e0)
                          for b in (0, 0.016, 0.07, 0.4) for t in (0, math.pi / 2, math.pi))
    assert worst_fd < 1e-7, worst_fd
    assert worst_mc < 0.015, worst_mc
    assert invariant_error < 1e-10, invariant_error
    assert ambiguity["rank"] == 2
    assert ambiguity["max_variance_difference_keV2"] < 1e-12
    return {"schema_version": 1, "kind": "synthetic-method-exercise; not measured data or experimental refit",
            "seed": seed, "samples_per_covariance": samples,
            "inputs": {"E0_keV": e0, "beta": beta, "sigma_Elab_keV": se, "sigma_beta": sb, "sigma_theta_deg": 2},
            "energy_and_uncertainty": rows, "width_identifiability": ambiguity,
            "stopping_toy": {"tau_ps": tau, "slowing_scale_ps": ts, "beta_initial": initial_beta,
                             "mean_beta": mean_beta, "variance_beta": var_beta, "rows": stopping_rows,
                             "boundary": "Klemme reports a ~1.1 ps Au stopping time, not this exponential law or toy tau"},
            "verification": {"max_fd_relative_error": worst_fd, "max_MC_relative_difference": worst_mc,
                             "max_forward_inverse_error_keV": float(invariant_error), "passed": True},
            "numpy_version": np.__version__}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=200_000)
    parser.add_argument("--seed", type=int, default=1313)
    args = parser.parse_args()
    result = calculate(args.samples, args.seed)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "verification": result["verification"],
                      "width_design_rank": result["width_identifiability"]["rank"]}))


if __name__ == "__main__":
    main()
