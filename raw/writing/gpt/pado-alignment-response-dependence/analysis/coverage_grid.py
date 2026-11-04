#!/usr/bin/env python3
"""Coverage grid for the maximum-row alignment discrepancy.

The grid separates two questions:
1. matched covariance: the fitted statistic uses the true rho;
2. covariance misspecification: the data use true rho but the fit assumes rho=0.

This remains a declared table-level Gaussian toy model, not an experimental
coverage or a reconstructed source covariance.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from coverage_check import fit_shared_chi2, max_d2
from profile_alignment_models import Q95_2D, alpha_prediction, covariance, read_rows


def run_grid(rows, true_rs, true_rhos, n_toys, seed, fit_rho_mode):
    rng = np.random.default_rng(seed)
    cells = []
    for true_rho in true_rhos:
        for true_r in true_rs:
            true_mu = np.array(alpha_prediction(6.5, true_r))
            fit_rho = true_rho if fit_rho_mode == "matched" else 0.0
            values = []
            for _ in range(n_toys):
                observations = [
                    rng.multivariate_normal(true_mu, covariance(row, true_rho))
                    for row in rows
                ]
                r_hat, _ = fit_shared_chi2(rows, observations, fit_rho, 6.5)
                values.append(max_d2(rows, observations, r_hat, fit_rho, 6.5))
            values = np.asarray(values)
            cells.append(
                {
                    "true_r": true_r,
                    "true_rho": true_rho,
                    "fit_rho": fit_rho,
                    "coverage_at_q95_2d": float(np.mean(values <= Q95_2D)),
                    "q95_max_d2": float(np.quantile(values, 0.95)),
                    "q99_max_d2": float(np.quantile(values, 0.99)),
                    "median_max_d2": float(np.quantile(values, 0.5)),
                }
            )
    return cells


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
        default=Path(__file__).parents[1] / "analysis" / "results" / "coverage-grid.json",
    )
    parser.add_argument("--n-toys", type=int, default=1000)
    parser.add_argument("--seed", type=int, default=20261106)
    args = parser.parse_args()

    rows = read_rows(args.input)
    true_rs = [0.10, 0.20, 0.28, 0.40, 0.60]
    true_rhos = [-0.60, -0.30, 0.00, 0.30, 0.60]
    payload = {
        "schema_version": 1,
        "input": str(args.input),
        "n_toys_per_cell": args.n_toys,
        "seed": args.seed,
        "true_r_values": true_rs,
        "true_rho_values": true_rhos,
        "threshold_q95_2d": Q95_2D,
        "matched_covariance": run_grid(
            rows, true_rs, true_rhos, args.n_toys, args.seed, "matched"
        ),
        "rho_misspecified_to_zero": run_grid(
            rows, true_rs, true_rhos, args.n_toys, args.seed + 1, "zero"
        ),
        "interpretation_boundary": [
            "The grid calibrates a declared maximum-row statistic under a Gaussian toy model.",
            "It does not reconstruct the source covariance or establish an experimental p-value.",
            "The rho=0 fit in the misspecified grid is a sensitivity control, not a recommended covariance choice.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "cells": len(payload["matched_covariance"]),
        "n_toys_per_cell": args.n_toys,
        "output": str(args.output),
    }, indent=2))


if __name__ == "__main__":
    main()
