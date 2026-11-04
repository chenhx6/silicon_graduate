#!/usr/bin/env python3
"""Calibrate the same rho-profiled max-row statistic used on the table."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from coverage_check import fit_shared_chi2, max_d2
from profile_alignment_models import Q95_2D, alpha_prediction, covariance, read_rows


def profiled_statistic(rows, observations, profile_rhos, j):
    values = []
    for rho in profile_rhos:
        r_hat, _ = fit_shared_chi2(rows, observations, float(rho), j)
        values.append(max_d2(rows, observations, r_hat, float(rho), j))
    return float(min(values))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).parents[1] / "data" / "zobel83_958_table1.csv",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parents[1]
        / "analysis"
        / "results"
        / "profile-coverage.json",
    )
    parser.add_argument("--n-toys", type=int, default=300)
    parser.add_argument("--seed", type=int, default=20261107)
    parser.add_argument("--spin", type=float, default=6.5)
    args = parser.parse_args()

    rows = read_rows(args.input)
    profile_rhos = np.linspace(-0.8, 0.8, 81)
    true_rhos = [-0.6, 0.0, 0.6]
    rng = np.random.default_rng(args.seed)
    true_r = 0.28
    true_mu = np.asarray(alpha_prediction(args.spin, true_r))
    quantiles = {}
    acceptance = {}
    toy_values = {}
    for true_rho in true_rhos:
        values = []
        for _ in range(args.n_toys):
            observations = [
                rng.multivariate_normal(true_mu, covariance(row, true_rho))
                for row in rows
            ]
            values.append(profiled_statistic(rows, observations, profile_rhos, args.spin))
        arr = np.asarray(values)
        key = str(true_rho)
        toy_values[key] = values
        quantiles[key] = {
            str(q): float(np.quantile(arr, q)) for q in (0.5, 0.9, 0.95, 0.99)
        }
        acceptance[key] = {
            "at_single_row_q95_2d": float(np.mean(arr <= Q95_2D)),
            "mc_se": float(
                np.sqrt(
                    np.mean(arr <= Q95_2D)
                    * (1.0 - np.mean(arr <= Q95_2D))
                    / args.n_toys
                )
            ),
        }

    observed_values = []
    for rho in profile_rhos:
        r_hat, _ = fit_shared_chi2(rows, [np.asarray([row["alpha2"], row["alpha4"]]) for row in rows], float(rho), args.spin)
        observed_values.append(max_d2(rows, [np.asarray([row["alpha2"], row["alpha4"]]) for row in rows], r_hat, float(rho), args.spin))
    observed_t = float(min(observed_values))
    payload = {
        "schema_version": 1,
        "input": str(args.input),
        "n_toys_per_true_rho": args.n_toys,
        "seed": args.seed,
        "true_r": true_r,
        "true_rho_values": true_rhos,
        "profile_rho_grid": profile_rhos.tolist(),
        "observed_profiled_max_d2": observed_t,
        "single_row_q95_2d": Q95_2D,
        "profiled_max_d2_quantiles": quantiles,
        "single_row_threshold_acceptance": acceptance,
        "interpretation_boundary": [
            "Each toy repeats the same rho-profile and max-row operation used for the observed statistic.",
            "This is a table-level Gaussian toy calibration, not an experimental p-value.",
            "The source covariance and cross-row dependence remain unavailable.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "observed_profiled_max_d2": observed_t,
                "profiled_q95": {
                    key: value["0.95"] for key, value in quantiles.items()
                },
                "output": str(args.output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
