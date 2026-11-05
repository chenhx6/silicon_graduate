#!/usr/bin/env python3
"""Uncalibrated row-specific-correlation envelope for the P-ADO table.

Each row is allowed its own within-row rho on the declared finite grid while
the response proxy r remains shared.  This is a sensitivity envelope, not a
likelihood model or a calibrated p-value, because cross-row covariance remains
unknown.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar

from profile_alignment_models import alpha_prediction, covariance, read_rows, row_vector


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def rowwise_envelope(rows: list[dict], r: float, rhos: np.ndarray) -> tuple[float, list[dict]]:
    mu = np.asarray(alpha_prediction(6.5, r))
    values = []
    for index, row in enumerate(rows):
        residual = row_vector(row) - mu
        d2_by_rho = [
            float(residual @ np.linalg.solve(covariance(row, float(rho)), residual))
            for rho in rhos
        ]
        best_index = int(np.argmin(d2_by_rho))
        values.append(
            {
                "row_index": index,
                "beam": row["beam"],
                "energy_MeV": row["beam_energy_lab_MeV"],
                "profile_rho_i": float(rhos[best_index]),
                "mahalanobis_d2": float(d2_by_rho[best_index]),
            }
        )
    return max(item["mahalanobis_d2"] for item in values), values


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
        / "row-covariance-envelope.json",
    )
    args = parser.parse_args()
    rows = read_rows(args.input)
    rhos = np.round(np.linspace(-0.8, 0.8, 81), 12)

    result = minimize_scalar(
        lambda r: rowwise_envelope(rows, float(r), rhos)[0],
        bounds=(0.02, 1.0),
        method="bounded",
        options={"xatol": 1e-7},
    )
    best_r = float(result.x)
    best_t, rows_out = rowwise_envelope(rows, best_r, rhos)
    payload = {
        "schema_version": 1,
        "input": str(args.input),
        "input_sha256": sha256_file(args.input.resolve()),
        "analysis_script": str(Path(__file__)),
        "analysis_script_sha256": sha256_file(Path(__file__)),
        "shared_response_r": best_r,
        "profiled_rowwise_max_d2": float(best_t),
        "rho_i_grid": rhos.tolist(),
        "rows": rows_out,
        "interpretation_boundary": [
            "This is an uncalibrated row-specific within-row-correlation sensitivity envelope.",
            "It does not model cross-row covariance or source nuisance parameters.",
            "It is not an experimental p-value, likelihood-ratio statistic or coverage result.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "shared_response_r": best_r,
                "profiled_rowwise_max_d2": best_t,
                "output": str(args.output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
