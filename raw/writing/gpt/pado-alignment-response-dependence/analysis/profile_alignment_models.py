#!/usr/bin/env python3
"""Profile reaction-dependent alignment models for the Zobel 1983 benchmark.

The input is a normalized public table of fitted (alpha_2, alpha_4) values.
The source does not provide row-internal covariance, so rho is profiled as a
declared sensitivity parameter. The script keeps this table-level analysis
separate from an event-level likelihood or detector-response calibration.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Callable

import numpy as np
from scipy.optimize import minimize

Q95_2D = 5.991464547107979


def read_rows(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        for key in ("beam_energy_lab_MeV", "alpha2", "sigma_alpha2", "alpha4", "sigma_alpha4"):
            row[key] = float(row[key])
    return rows


def tensor_polynomials(j: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    m = np.arange(j, -j - 1.0, -1.0)
    s = j * (j + 1.0)
    p2 = 3.0 * m * m - s
    p4 = 35.0 * m**4 - (30.0 * s - 25.0) * m * m + 3.0 * s * s - 6.0 * s
    idx = int(np.argmin(np.abs(m)))
    return m, p2 / p2[idx], p4 / p4[idx]


def alpha_prediction(j: float, r: float) -> tuple[float, float]:
    """Gaussian magnetic-substate population prediction."""
    if r <= 1e-8:
        return 1.0, 1.0
    m, t2, t4 = tensor_polynomials(j)
    x = -(m * m - np.min(m * m)) / (2.0 * (j * r) ** 2)
    w = np.exp(x - np.max(x))
    w /= np.sum(w)
    return float(np.dot(w, t2)), float(np.dot(w, t4))


def covariance(row: dict, rho: float) -> np.ndarray:
    s2, s4 = row["sigma_alpha2"], row["sigma_alpha4"]
    return np.array([[s2 * s2, rho * s2 * s4], [rho * s2 * s4, s4 * s4]])


def row_vector(row: dict) -> np.ndarray:
    return np.array([row["alpha2"], row["alpha4"]])


def model_r(params: np.ndarray, row: dict, model: str, ebar: float) -> float:
    if model == "shared":
        return float(params[0])
    if model == "family":
        return float(params[0] if row["beam"] == "alpha" else params[1])
    if model == "energy":
        return float(params[0] + params[1] * (row["beam_energy_lab_MeV"] - ebar) / 10.0)
    raise ValueError(f"unknown model: {model}")


def model_prediction(params: np.ndarray, row: dict, model: str, ebar: float, j: float) -> np.ndarray:
    if model == "mixture":
        r_direct, r_cascade, weight_direct = params
        direct = np.array(alpha_prediction(j, r_direct))
        cascade = np.array(alpha_prediction(j, r_cascade))
        return weight_direct * direct + (1.0 - weight_direct) * cascade
    return np.array(alpha_prediction(j, model_r(params, row, model, ebar)))


def objective(
    params: np.ndarray,
    rows: list[dict],
    model: str,
    rho: float,
    j: float,
    ebar: float,
) -> float:
    total = 0.0
    for row in rows:
        if model == "mixture":
            if not (0.02 <= params[0] <= 1.0 and 0.02 <= params[1] <= 1.0 and 0.0 <= params[2] <= 1.0):
                return 1e12
            mu = model_prediction(params, row, model, ebar, j)
        else:
            r = model_r(params, row, model, ebar)
            if not 0.02 <= r <= 1.0:
                return 1e12 + 1e9 * min(abs(r - 0.02), abs(r - 1.0))
            mu = model_prediction(params, row, model, ebar, j)
        dy = row_vector(row) - mu
        cov = covariance(row, rho)
        sign, logdet = np.linalg.slogdet(cov)
        if sign <= 0:
            return 1e12
        total += float(dy @ np.linalg.solve(cov, dy) + logdet + 2.0 * math.log(2.0 * math.pi))
    return 0.5 * total


def fit_model(rows: list[dict], model: str, rho: float, j: float = 6.5) -> dict:
    ebar = float(np.mean([r["beam_energy_lab_MeV"] for r in rows]))
    if model == "shared":
        x0 = np.array([0.27])
        bounds = [(0.02, 1.0)]
    elif model == "family":
        x0 = np.array([0.27, 0.28])
        bounds = [(0.02, 1.0), (0.02, 1.0)]
    elif model == "energy":
        x0 = np.array([0.27, 0.0])
        bounds = [(0.02, 1.0), (-0.5, 0.5)]
    elif model == "mixture":
        x0 = np.array([0.15, 0.45, 0.5])
        bounds = [(0.02, 1.0), (0.02, 1.0), (0.0, 1.0)]
    else:
        raise ValueError(model)
    starts = [x0]
    rng = np.random.default_rng(20261105)
    for _ in range(2):
        starts.append(np.array([rng.uniform(lo, hi) for lo, hi in bounds]))
    best = None
    for start in starts:
        result = minimize(
            objective,
            start,
            args=(rows, model, rho, j, ebar),
            method="L-BFGS-B",
            bounds=bounds,
            options={"maxiter": 600, "ftol": 1e-12, "gtol": 1e-8},
        )
        candidate = result
        if best is None or candidate.fun < best.fun:
            best = candidate
    assert best is not None
    params = np.asarray(best.x, dtype=float)
    predictions = []
    chi2 = 0.0
    for row in rows:
        mu = model_prediction(params, row, model, ebar, j)
        dy = row_vector(row) - mu
        d2 = float(dy @ np.linalg.solve(covariance(row, rho), dy))
        chi2 += d2
        prediction = {
            "beam": row["beam"],
            "energy_MeV": row["beam_energy_lab_MeV"],
            "alpha2_pred": float(mu[0]),
            "alpha4_pred": float(mu[1]),
            "mahalanobis_d2": d2,
        }
        if model == "mixture":
            prediction.update({
                "r_direct": float(params[0]),
                "r_cascade": float(params[1]),
                "weight_direct": float(params[2]),
            })
        else:
            prediction["r"] = model_r(params, row, model, ebar)
        predictions.append(prediction)
    k = len(params)
    # The ten rows are the independent observational units in this
    # table-level contract. Each row contributes a two-component vector, but
    # the row-internal covariance is already represented by Sigma_i.
    n = len(rows)
    return {
        "model": model,
        "rho": rho,
        "j": j,
        "params": params.tolist(),
        "nll": float(best.fun),
        "chi2": chi2,
        "aic": float(2 * best.fun + 2 * k),
        "bic": float(2 * best.fun + k * math.log(n)),
        "bic_sample_size": n,
        "max_mahalanobis_d2": max(p["mahalanobis_d2"] for p in predictions),
        "tau_max_d2": float(math.sqrt(max(p["mahalanobis_d2"] for p in predictions) / Q95_2D)),
        "predictions": predictions,
    }


def rho_profile(rows: list[dict], j: float) -> list[dict]:
    out = []
    # 0.02 spacing resolves the covariance profile minimum used in the paper.
    for rho in np.linspace(-0.8, 0.8, 81):
        for model in ("shared", "family", "energy", "mixture"):
            fit = fit_model(rows, model, float(rho), j)
            out.append(
                {
                    "rho": float(rho),
                    "model": model,
                    "nll": fit["nll"],
                    "chi2": fit["chi2"],
                    "aic": fit["aic"],
                    "bic": fit["bic"],
                    "max_mahalanobis_d2": fit["max_mahalanobis_d2"],
                    "tau_max_d2": fit["tau_max_d2"],
                    "params": fit["params"],
                }
            )
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=Path(__file__).parents[1] / "data" / "zobel83_958_table1.csv")
    parser.add_argument("--output", type=Path, default=Path(__file__).parents[1] / "analysis" / "results" / "alignment-profile.json")
    parser.add_argument("--rho", type=float, default=0.0)
    parser.add_argument("--spin", type=float, default=6.5)
    args = parser.parse_args()

    rows = read_rows(args.input)
    fits = {}
    for model in ("shared", "family", "energy", "mixture"):
        fits[model] = fit_model(rows, model, args.rho, args.spin)
    for model_fit in fits.values():
        model_fit["delta_aic_vs_shared"] = float(
            model_fit["aic"] - fits["shared"]["aic"]
        )
        model_fit["delta_bic_vs_shared"] = float(
            model_fit["bic"] - fits["shared"]["bic"]
        )
    profiles = rho_profile(rows, args.spin)
    payload = {
        "schema_version": 1,
        "input": str(args.input),
        "input_kind": "public normalized Table 1 benchmark; not raw spectra",
        "rho_contract": {
            "rho_center": args.rho,
            "profile_range": [-0.8, 0.8],
            "common_row_rho": True,
            "rows_assumed_independent": True,
            "covariance_source": "not supplied by source",
        },
        "response_map_contract": {
            "spin_j": args.spin,
            "alignment_proxy": "Gaussian magnetic-substate width r=sigma/J",
            "r_bounds": [0.02, 1.0],
            "alpha_map": "finite-J tensor-polynomial average implemented in alpha_prediction",
        },
        "spin": args.spin,
        "fits_at_rho_center": fits,
        "rho_profile": profiles,
        "interpretation_boundary": [
            "This is a table-level Gaussian profile, not an event-level Poisson likelihood.",
            "The source does not provide row-internal covariance, so rho is a sensitivity parameter.",
            "No experimental significance or coverage-calibrated p-value is claimed.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: {"aic": v["aic"], "bic": v["bic"], "chi2": v["chi2"], "params": v["params"]} for k, v in fits.items()}, indent=2))


if __name__ == "__main__":
    main()
