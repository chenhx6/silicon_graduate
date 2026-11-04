#!/usr/bin/env python3
"""Calibrate the same rho-profiled max-row statistic used on the table."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
from pathlib import Path
import sys

import numpy as np
import scipy

from coverage_check import fit_shared_chi2, max_d2
from profile_alignment_models import Q95_2D, alpha_prediction, covariance, read_rows


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


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
    parser.add_argument("--n-toys", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20261107)
    parser.add_argument("--spin", type=float, default=6.5)
    parser.add_argument("--rho-min", type=float, default=-0.8)
    parser.add_argument("--rho-max", type=float, default=0.8)
    parser.add_argument("--rho-step", type=float, default=0.02)
    parser.add_argument("--bootstrap-toys", type=int, default=1000)
    args = parser.parse_args()

    rows = read_rows(args.input)
    n_grid = int(round((args.rho_max - args.rho_min) / args.rho_step))
    profile_rhos = np.round(
        np.linspace(args.rho_min, args.rho_max, n_grid + 1), 12
    )
    true_rhos = [-0.6, 0.0, 0.6]
    rng = np.random.default_rng(args.seed)
    bootstrap_rng = np.random.default_rng(args.seed + 1_000_000)
    true_r = 0.28
    true_mu = np.asarray(alpha_prediction(args.spin, true_r))
    quantiles = {}
    acceptance = {}
    toy_rows = []
    for true_rho in true_rhos:
        values = []
        for toy_index in range(args.n_toys):
            observations = [
                rng.multivariate_normal(true_mu, covariance(row, true_rho))
                for row in rows
            ]
            value = profiled_statistic(rows, observations, profile_rhos, args.spin)
            values.append(value)
            toy_rows.append(
                {
                    "true_rho": true_rho,
                    "toy_index": toy_index,
                    "profiled_max_d2": value,
                }
            )
        arr = np.asarray(values)
        key = str(true_rho)
        bootstrap_indices = bootstrap_rng.integers(
            0, len(arr), size=(args.bootstrap_toys, len(arr))
        )
        bootstrap_q95 = np.quantile(arr[bootstrap_indices], 0.95, axis=1)
        quantiles[key] = {
            str(q): float(np.quantile(arr, q)) for q in (0.5, 0.9, 0.95, 0.99)
        }
        quantiles[key]["0.95_bootstrap_ci95"] = [
            float(np.quantile(bootstrap_q95, 0.025)),
            float(np.quantile(bootstrap_q95, 0.975)),
        ]
        quantiles[key]["0.95_bootstrap_sd"] = float(np.std(bootstrap_q95, ddof=1))
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
        observations = [
            np.asarray([row["alpha2"], row["alpha4"]]) for row in rows
        ]
        r_hat, _ = fit_shared_chi2(
            rows, observations, float(rho), args.spin
        )
        observed_values.append(
            max_d2(rows, observations, r_hat, float(rho), args.spin)
        )
    observed_t = float(min(observed_values))
    observed_profile_rho = float(profile_rhos[int(np.argmin(observed_values))])
    toy_path = args.output.with_name("profile-coverage-toys.csv")
    with toy_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=("true_rho", "toy_index", "profiled_max_d2")
        )
        writer.writeheader()
        writer.writerows(toy_rows)
    payload = {
        "schema_version": 2,
        "input": str(args.input),
        "input_sha256": sha256_file(args.input),
        "analysis_script": str(Path(__file__)),
        "analysis_script_sha256": sha256_file(Path(__file__)),
        "n_toys_per_true_rho": args.n_toys,
        "seed": args.seed,
        "bootstrap_toys": args.bootstrap_toys,
        "bootstrap_seed": args.seed + 1_000_000,
        "true_r": true_r,
        "true_rho_values": true_rhos,
        "profile_rho_grid": profile_rhos.tolist(),
        "observed_profiled_max_d2": observed_t,
        "observed_profile_rho": observed_profile_rho,
        "toy_values_file": toy_path.name,
        "toy_value_count": len(toy_rows),
        "single_row_q95_2d": Q95_2D,
        "profiled_max_d2_quantiles": quantiles,
        "single_row_threshold_acceptance": acceptance,
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
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
