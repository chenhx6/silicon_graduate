#!/usr/bin/env python3
"""Parametric coverage check for the table-level shared-alignment statistic."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

from profile_alignment_models import (
    Q95_2D,
    alpha_prediction,
    covariance,
    read_rows,
    row_vector,
)


def fit_shared_chi2(rows: list[dict], observations: list[np.ndarray], rho: float, j: float, r0: float | None = None) -> tuple[float, float]:
    def chi2(r: float) -> float:
        mu = np.array(alpha_prediction(j, r))
        total = 0.0
        for row, obs in zip(rows, observations):
            d = obs - mu
            total += float(d @ np.linalg.solve(covariance(row, rho), d))
        return total

    result = minimize_scalar(chi2, bounds=(0.02, 1.0), method="bounded", options={"xatol": 1e-7})
    return float(result.x), float(result.fun)


def max_d2(rows: list[dict], observations: list[np.ndarray], r: float, rho: float, j: float) -> float:
    mu = np.array(alpha_prediction(j, r))
    return max(
        float((obs - mu) @ np.linalg.solve(covariance(row, rho), obs - mu))
        for row, obs in zip(rows, observations)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).parents[1] / "data" / "zobel83_958_table1.csv")
    parser.add_argument("--output", type=Path, default=Path(__file__).parents[1] / "analysis" / "results" / "coverage.json")
    parser.add_argument("--n-toys", type=int, default=1000)
    parser.add_argument("--rho", type=float, default=0.0)
    parser.add_argument("--true-r", type=float, default=0.28)
    parser.add_argument("--seed", type=int, default=20261105)
    args = parser.parse_args()

    rows = read_rows(args.input)
    rng = np.random.default_rng(args.seed)
    true_mu = np.array(alpha_prediction(6.5, args.true_r))
    max_values = []
    fitted_r = []
    for _ in range(args.n_toys):
        observations = [
            rng.multivariate_normal(true_mu, covariance(row, args.rho))
            for row in rows
        ]
        r_hat, _ = fit_shared_chi2(rows, observations, args.rho, 6.5)
        fitted_r.append(r_hat)
        max_values.append(max_d2(rows, observations, r_hat, args.rho, 6.5))

    max_values = np.asarray(max_values)
    fitted_r = np.asarray(fitted_r)
    acceptance = float(np.mean(max_values <= Q95_2D))
    mc_se = float(np.sqrt(acceptance * (1.0 - acceptance) / args.n_toys))
    result = {
        "schema_version": 1,
        "input": str(args.input),
        "n_toys": args.n_toys,
        "seed": args.seed,
        "rho": args.rho,
        "true_r": args.true_r,
        "true_mu": true_mu.tolist(),
        "threshold_q95_2d": Q95_2D,
        "empirical_fraction_max_d2_leq_q95": acceptance,
        "empirical_fraction_mc_se": mc_se,
        "max_d2_quantiles": {str(q): float(np.quantile(max_values, q)) for q in (0.5, 0.9, 0.95, 0.99)},
        "fitted_r_quantiles": {str(q): float(np.quantile(fitted_r, q)) for q in (0.05, 0.5, 0.95)},
        "interpretation_boundary": [
            "This checks the coverage of the chosen max-row statistic under a declared table-level Gaussian toy model.",
            "It is not a source covariance reconstruction and is not an experimental p-value.",
            "The 2D single-row q95 threshold is not automatically a 10-row family-wise 95% threshold.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
