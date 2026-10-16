#!/usr/bin/env python3
"""Audit rounded 135Pr observable identities; do not refit a nuclear transition.

The covariance grid is a declared calibration sensitivity model. Counts, event
overlap, joint response and the original calibration covariance are unavailable.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path

import numpy as np


def fraction(delta: float) -> float:
    return delta * delta / (1.0 + delta * delta)


def fraction_image(row: dict) -> dict:
    delta = float(row["delta"])
    lo = delta - float(row["err_minus"])
    hi = delta + float(row["err_plus"])
    values = [fraction(lo), fraction(hi)]
    if lo <= 0 <= hi:
        values.append(0.0)
    return {
        "line": row["line"], "E_keV": row["E_keV"],
        "delta": delta, "literal_delta_endpoints": [lo, hi],
        "radiative_E2_fraction": fraction(delta),
        "literal_fraction_image_not_CI": [min(values), max(values)],
    }


def qpoint(energy: float, mass_energy: float) -> float:
    x = energy / mass_energy
    return (1.0 + x) / (1.0 + x + x * x)


def parameters(cfg: dict) -> tuple[np.ndarray, np.ndarray]:
    a, q = cfg["lv_a"], cfg["adopted_Q"]
    return (
        np.array([float(a["intercept"]), float(a["slope_per_keV"]),
                  float(q["p0"]), float(q["p1_per_keV"])]),
        np.array([float(a["intercept_error_scale"]),
                  float(a["slope_error_scale_per_keV"]),
                  float(q["p0_error_scale"]), float(q["p1_error_scale_per_keV"])]),
    )


def conditional_p(params: np.ndarray, energy: float, ratio: float,
                  mass_energy: float) -> float:
    a = params[0] + energy * params[1]
    asymmetry = (a - ratio) / (a + ratio)
    q = qpoint(energy, mass_energy) * (params[2] + energy * params[3])
    return asymmetry / q


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text(encoding="utf-8"))
    params, scales = parameters(cfg)
    mass = float(cfg["electron_rest_energy_keV"])
    p0, p1 = params[2:]
    rows, gradients = [], []
    rounding = []
    for row in cfg["lv_rows"]:
        e = float(row["E_keV"])
        a, asym = params[0] + e * params[1], float(row["A"])
        qp = qpoint(e, mass)
        factor, q = p0 + p1 * e, qp * (p0 + p1 * e)
        assert q > 0 and abs(asym) < 1
        p = asym / q
        # This is an algebraic proxy from rounded published A, not raw counts.
        ratio_proxy = a * (1 - asym) / (1 + asym)
        assert math.isclose(conditional_p(params, e, ratio_proxy, mass), p,
                            rel_tol=1e-12, abs_tol=1e-12)
        da = (1 - asym * asym) / (2 * a * q)
        dq = -p / factor
        gradient = np.array([da, e * da, dq, e * dq])
        gradients.append(gradient)
        # Compare derivatives of the full count-ratio formula, with dimensioned
        # parameter steps scaled to the quoted marginal calibration scales.
        for j in range(4):
            step = scales[j] * 1e-3
            plus, minus = params.copy(), params.copy()
            plus[j] += step
            minus[j] -= step
            finite = (conditional_p(plus, e, ratio_proxy, mass)
                      - conditional_p(minus, e, ratio_proxy, mass)) / (2 * step)
            assert math.isclose(finite, gradient[j], rel_tol=4e-6, abs_tol=1e-7)
        transformed_errors = [float(row["A_plus"]) / q, float(row["A_minus"]) / q]
        reported = [float(row["P"]), float(row["P_plus"]), float(row["P_minus"])]
        reconstructed = [p, *transformed_errors]
        compatible = [bool(abs(x - y) <= 0.005) for x, y in zip(reconstructed, reported)]
        assert all(compatible)
        rounding.append({"line": row["line"], "reconstructed": reconstructed,
                         "reported": reported, "half_last_digit": 0.005,
                         "rounding_compatible": compatible})
        rows.append({"line": row["line"], "E_keV": e, "a_Lv": a,
                     "Qpoint": qp, "Q_adopted_Herzan": q,
                     "P_from_SI_A_and_adopted_Q": p,
                     "P_reported": reported[0],
                     "ratio_proxy_Nparallel_over_Nperp": ratio_proxy,
                     "a_for_zero_asymmetry_at_fixed_proxy": ratio_proxy,
                     "fractional_a_shift_to_zero": ratio_proxy / a - 1,
                     "dP_da0_da1_dp0_dp1": gradient.tolist()})
    g = np.array(gradients)
    covariance_grid = []
    for rho_a in cfg["sensitivity_model"]["rho_a_values"]:
        for rho_q in cfg["sensitivity_model"]["rho_Q_values"]:
            cov = np.diag(scales * scales)
            cov[0, 1] = cov[1, 0] = rho_a * scales[0] * scales[1]
            cov[2, 3] = cov[3, 2] = rho_q * scales[2] * scales[3]
            # PSD is checked in standardized coordinates to avoid mixing units.
            standardized = cov / np.outer(scales, scales)
            assert np.linalg.eigvalsh(standardized).min() >= -1e-12
            pcov = g @ cov @ g.T
            assert np.linalg.eigvalsh(pcov).min() >= -1e-12
            sigma = np.sqrt(np.maximum(0, np.diag(pcov)))
            corr = pcov / np.outer(sigma, sigma)
            covariance_grid.append({"rho_a": rho_a, "rho_Q": rho_q,
                                    "conditional_P_covariance": pcov.tolist(),
                                    "conditional_P_sigma": sigma.tolist(),
                                    "conditional_P_correlation": corr.tolist()})
    diagonal = next(x for x in covariance_grid if x["rho_a"] == x["rho_Q"] == 0)
    sigma_grid = np.array([x["conditional_P_sigma"] for x in covariance_grid])
    for i, row in enumerate(rows):
        row["conditional_calibration_sigma_diagonal_model"] = diagonal["conditional_P_sigma"][i]
        row["conditional_calibration_sigma_grid_range"] = [float(sigma_grid[:, i].min()),
                                                          float(sigma_grid[:, i].max())]
    images = {key: [fraction_image(row) for row in cfg[key]] for key in ("matta_rows", "lv_rows")}
    # A convention sign reversal is an exact invariance of the fraction.
    for key in images:
        for row in cfg[key]:
            assert fraction(float(row["delta"])) == fraction(-float(row["delta"]))
    contrast = []
    for line in ("747", "813"):
        m = next(x for x in images["matta_rows"] if x["line"] == line)
        l = next(x for x in images["lv_rows"] if x["line"] == line)
        mr, lr = m["literal_fraction_image_not_CI"], l["literal_fraction_image_not_CI"]
        contrast.append({"line": line, "Matta_literal_image": mr, "Lv_literal_image": lr,
                         "literal_images_disjoint": max(mr[0], lr[0]) > min(mr[1], lr[1]),
                         "meaning": "Reported branch-magnitude difference; not a significance or confidence test"})
    result = {"data_identity": cfg["data_identity"], "data_kind": cfg["kind"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "fraction_images": images, "published_branch_contrast": contrast,
              "Lv_calibration_identity": rows, "rounding_reproduction": rounding,
              "calibration_model": cfg["sensitivity_model"],
              "calibration_parameter_order": ["a0", "a1_per_keV", "p0", "p1_per_keV"],
              "calibration_covariance_grid": covariance_grid,
              "boundaries": cfg["boundaries"]}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "day16-pr135-branch-calibration.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    table = io.StringIO(newline="")
    writer = csv.writer(table, lineterminator="\n")
    writer.writerow(["line", "a_Lv", "Q_adopted", "P_reconstructed", "P_reported",
                     "conditional_cal_sigma_rho0", "sigma_grid_min", "sigma_grid_max"])
    for row in rows:
        writer.writerow([row["line"], row["a_Lv"], row["Q_adopted_Herzan"],
                         row["P_from_SI_A_and_adopted_Q"], row["P_reported"],
                         row["conditional_calibration_sigma_diagonal_model"],
                         *row["conditional_calibration_sigma_grid_range"]])
    (args.output_dir / "day16-pr135-calibration-crosswalk.csv").write_text(
        table.getvalue(), encoding="utf-8")
    print(json.dumps({"identity": result["data_identity"], "published_rows": len(rows),
                      "rounding_compatible": all(all(x["rounding_compatible"]) for x in rounding),
                      "calibration_rows": rows, "branch_contrast": contrast}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
