#!/usr/bin/env python3
"""Leave-one-row-out influence checks for the profiled discrepancy.

This is a descriptive sensitivity control.  It uses the same finite
common-rho grid as the main analysis but does not assign a calibrated
family-wise probability to the leave-one-row-out values.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from coverage_check import fit_shared_chi2, max_d2
from profile_alignment_models import read_rows, row_vector


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def profile_statistic(rows: list[dict], observations: list[np.ndarray], rhos: np.ndarray) -> tuple[float, float]:
    values = []
    for rho in rhos:
        r_hat, _ = fit_shared_chi2(rows, observations, float(rho), 6.5)
        values.append(max_d2(rows, observations, r_hat, float(rho), 6.5))
    index = int(np.argmin(values))
    return float(rhos[index]), float(values[index])


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
        / "influence-checks.json",
    )
    args = parser.parse_args()

    rows = read_rows(args.input)
    observations = [row_vector(row) for row in rows]
    rhos = np.round(np.linspace(-0.8, 0.8, 81), 12)
    full_rho, full_t = profile_statistic(rows, observations, rhos)
    leave_one_out = []
    for index, row in enumerate(rows):
        subset_rows = rows[:index] + rows[index + 1 :]
        subset_observations = observations[:index] + observations[index + 1 :]
        rho, statistic = profile_statistic(subset_rows, subset_observations, rhos)
        leave_one_out.append(
            {
                "dropped_index": index,
                "beam": row["beam"],
                "energy_MeV": row["beam_energy_lab_MeV"],
                "profile_rho": rho,
                "profiled_max_d2": statistic,
            }
        )

    values = [entry["profiled_max_d2"] for entry in leave_one_out]
    payload = {
        "schema_version": 1,
        "input": str(args.input),
        "input_sha256": sha256_file(args.input.resolve()),
        "analysis_script": str(Path(__file__)),
        "analysis_script_sha256": sha256_file(Path(__file__)),
        "profile_rho_grid": rhos.tolist(),
        "full_table": {
            "profile_rho": full_rho,
            "profiled_max_d2": full_t,
        },
        "leave_one_row_out": leave_one_out,
        "range_leave_one_out_profiled_max_d2": [float(min(values)), float(max(values))],
        "interpretation_boundary": [
            "The leave-one-row-out values are descriptive influence diagnostics.",
            "Their null distribution changes with the number of rows and is not assigned an experimental p-value.",
            "The check does not resolve the unavailable source covariance or cross-row dependence.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "full_profiled_max_d2": full_t,
                "leave_one_out_range": payload["range_leave_one_out_profiled_max_d2"],
                "output": str(args.output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
