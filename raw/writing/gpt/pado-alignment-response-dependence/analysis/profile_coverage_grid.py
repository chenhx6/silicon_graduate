#!/usr/bin/env python3
"""Least-favorable nuisance-grid calibration for the profiled P-ADO statistic.

Every toy repeats the observed statistic's complete profile over common rho and
the row maximum.  The grid is deliberately kept separate from the primary
three-point calibration so that a conservative nuisance envelope can be
reported without pretending that the source covariance is known.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import platform
import sys
from pathlib import Path

import numpy as np
import scipy

from coverage_check import max_d2
from profile_alignment_models import alpha_prediction, covariance, read_rows
from profile_coverage import profiled_statistic


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


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
        / "profile-coverage-grid.json",
    )
    parser.add_argument("--n-toys", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20261108)
    parser.add_argument("--spin", type=float, default=6.5)
    parser.add_argument("--rho-min", type=float, default=-0.8)
    parser.add_argument("--rho-max", type=float, default=0.8)
    parser.add_argument("--rho-step", type=float, default=0.02)
    args = parser.parse_args()

    rows = read_rows(args.input)
    n_grid = int(round((args.rho_max - args.rho_min) / args.rho_step))
    profile_rhos = np.round(
        np.linspace(args.rho_min, args.rho_max, n_grid + 1), 12
    )
    true_rs = [0.10, 0.20, 0.28, 0.40, 0.60]
    true_rhos = [-0.80, -0.60, -0.30, 0.00, 0.30, 0.60, 0.80]
    rng = np.random.default_rng(args.seed)
    cells = []
    raw_rows = []

    for true_rho in true_rhos:
        for true_r in true_rs:
            true_mu = np.asarray(alpha_prediction(args.spin, true_r))
            values = []
            for toy_index in range(args.n_toys):
                observations = [
                    rng.multivariate_normal(true_mu, covariance(row, true_rho))
                    for row in rows
                ]
                value = profiled_statistic(rows, observations, profile_rhos, args.spin)
                values.append(value)
                raw_rows.append(
                    {
                        "true_r": true_r,
                        "true_rho": true_rho,
                        "toy_index": toy_index,
                        "profiled_max_d2": value,
                    }
                )
            arr = np.asarray(values)
            cells.append(
                {
                    "true_r": true_r,
                    "true_rho": true_rho,
                    "n_toys": args.n_toys,
                    "q50": float(np.quantile(arr, 0.50)),
                    "q95": float(np.quantile(arr, 0.95)),
                    "q99": float(np.quantile(arr, 0.99)),
                    "single_row_q95_acceptance": float(
                        np.mean(arr <= 5.991464547107979)
                    ),
                }
            )

    observations = [
        np.asarray([row["alpha2"], row["alpha4"]]) for row in rows
    ]
    # Reuse the exact fixed-rho fit helper for the observed table, avoiding a
    # second implementation of the profile rule.
    from coverage_check import fit_shared_chi2

    observed_profile_values = []
    for rho in profile_rhos:
        r_hat, _ = fit_shared_chi2(rows, observations, float(rho), args.spin)
        observed_profile_values.append(max_d2(rows, observations, r_hat, float(rho), args.spin))
    observed_t = float(min(observed_profile_values))
    observed_rho = float(profile_rhos[int(np.argmin(observed_profile_values))])
    worst = max(cells, key=lambda cell: cell["q95"])

    raw_path = args.output.with_name("profile-coverage-grid-toys.csv")
    with raw_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=("true_r", "true_rho", "toy_index", "profiled_max_d2")
        )
        writer.writeheader()
        writer.writerows(raw_rows)

    payload = {
        "schema_version": 1,
        "input": str(args.input),
        "input_sha256": sha256_file(args.input.resolve()),
        "analysis_script": str(Path(__file__)),
        "analysis_script_sha256": sha256_file(Path(__file__)),
        "seed": args.seed,
        "n_toys_per_cell": args.n_toys,
        "true_r_values": true_rs,
        "true_rho_values": true_rhos,
        "profile_rho_grid": profile_rhos.tolist(),
        "observed_profiled_max_d2": observed_t,
        "observed_profile_rho": observed_rho,
        "worst_case_q95": worst["q95"],
        "worst_case_q95_cell": {
            "true_r": worst["true_r"],
            "true_rho": worst["true_rho"],
        },
        "cells": cells,
        "raw_toy_values_file": raw_path.name,
        "raw_toy_value_count": len(raw_rows),
        "environment": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "interpretation_boundary": [
            "Every toy repeats the same common-rho profile and maximum-row operation used for the observed statistic.",
            "The worst-case q95 is conservative only within the declared independent-row Gaussian nuisance grid.",
            "It does not model unknown cross-row covariance, detector response or feeding and is not an experimental p-value.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "cells": len(cells),
                "n_toys_per_cell": args.n_toys,
                "observed_profiled_max_d2": observed_t,
                "worst_case_q95": worst["q95"],
                "worst_case_q95_cell": {
                    "true_r": worst["true_r"],
                    "true_rho": worst["true_rho"],
                },
                "output": str(args.output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
