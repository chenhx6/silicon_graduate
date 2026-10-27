#!/usr/bin/env python3
"""Conditional finite-mesh P-ADO Jacobian sign audit.

This script imports response and Jacobian helpers only.  It does not invoke the
CLI, read an input transition file, write raw data, or claim a global fold or
global invertibility.  Results are a small finite-mesh diagnostic for two
spin-transition examples.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

import numpy as np

from p_ado.compute.jacobian import transform_pdf_with_central_difference
from p_ado.physics.pado import build_pado_points, fast_pr, prepare_transition
from p_ado.physics.sigmaOverI import align_par


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().with_suffix(".json")


def response(ji: float, jf: float, delta: float, sigma_i: float) -> np.ndarray:
    pre = prepare_transition(ji, jf)
    sigma = ji * sigma_i
    return np.asarray(
        fast_pr(
            delta,
            align_par(ji, 2, sigma),
            align_par(ji, 4, sigma),
            pre,
        ),
        dtype=float,
    )


def finite_det(
    ji: float,
    jf: float,
    delta: float,
    sigma_i: float,
    h_delta: float,
    h_sigma_i: float,
) -> float:
    p_plus = response(ji, jf, delta + h_delta, sigma_i)
    p_minus = response(ji, jf, delta - h_delta, sigma_i)
    s_plus = response(ji, jf, delta, sigma_i + h_sigma_i)
    s_minus = response(ji, jf, delta, sigma_i - h_sigma_i)
    jac = np.column_stack(
        (
            (p_plus - p_minus) / (2.0 * h_delta),
            (s_plus - s_minus) / (2.0 * h_sigma_i),
        )
    )
    return float(np.linalg.det(jac))


def tiny_compute_jacobian_check(ji: float, jf: float) -> dict:
    """Exercise compute.jacobian on a tiny 5x5 grid, not a production run."""
    xi = np.array([-80.0, -40.0, 0.0, 40.0, 80.0])
    sigma_i = np.array([0.20, 0.30, 0.40, 0.50, 0.60])
    theta = np.deg2rad(xi)
    delta = np.tan(theta)
    sigma = ji * sigma_i
    points = build_pado_points(ji, jf, delta, xi, sigma, sigma_i)
    rows, report, export = transform_pdf_with_central_difference(
        points,
        lambda x: np.ones_like(x, dtype=float),
        lambda x: np.ones_like(x, dtype=float),
        return_report=True,
        return_array=True,
        return_export_data=True,
    )
    signed = np.asarray(export["detj_signed_delta_sigma"], dtype=float)
    return {
        "grid_shape": list(points.shape),
        "interior_shape": list(rows.shape),
        "signed_det_range": [float(np.nanmin(signed)), float(np.nanmax(signed))],
        "signed_positive_count": int(np.count_nonzero(signed > 0.0)),
        "signed_negative_count": int(np.count_nonzero(signed < 0.0)),
        "signed_zero_count": int(np.count_nonzero(signed == 0.0)),
        "report_status": report["delta_sigma"]["status"],
    }


def one_pair(ji: float, jf: float, xis: list[float], sigma_grid: list[float]) -> dict:
    h_delta = 1.0e-5
    h_sigma_i = 1.0e-5
    rows = []
    for xi in xis:
        delta = math.tan(math.radians(xi))
        for sigma_i in sigma_grid:
            det = finite_det(ji, jf, delta, sigma_i, h_delta, h_sigma_i)
            p, ado = response(ji, jf, delta, sigma_i)
            rows.append(
                {
                    "xi_deg": xi,
                    "delta": delta,
                    "sigma_over_i": sigma_i,
                    "P": float(p),
                    "ADO": float(ado),
                    "det_delta_sigma": det,
                }
            )

    dets = np.asarray([row["det_delta_sigma"] for row in rows], dtype=float)
    sign_changes = []
    for xi in xis:
        subset = [row for row in rows if row["xi_deg"] == xi]
        for left, right in zip(subset[:-1], subset[1:]):
            if left["det_delta_sigma"] * right["det_delta_sigma"] < 0.0:
                sign_changes.append(
                    {
                        "xi_deg": xi,
                        "sigma_left": left["sigma_over_i"],
                        "sigma_right": right["sigma_over_i"],
                        "det_left": left["det_delta_sigma"],
                        "det_right": right["det_delta_sigma"],
                    }
                )

    iso = []
    pre = prepare_transition(ji, jf)
    for sigma_i in [1.0, 2.0, 5.0, 10.0, 50.0, 100.0]:
        sigma = ji * sigma_i
        a2 = align_par(ji, 2, sigma)
        a4 = align_par(ji, 4, sigma)
        r0 = response(ji, jf, 0.0, sigma_i)
        r2 = response(ji, jf, 2.0, sigma_i)
        iso.append(
            {
                "sigma_over_i": sigma_i,
                "align2": float(a2),
                "align4": float(a4),
                "P_delta0": float(r0[0]),
                "ADO_delta0": float(r0[1]),
                "P_delta2": float(r2[0]),
                "ADO_delta2": float(r2[1]),
            }
        )

    # Coordinate scaling check at xi=-60 deg.  theta is in radians here.
    xi0 = -60.0
    d0 = math.tan(math.radians(xi0))
    h_theta = 1.0e-4
    h_sigma = 1.0e-5
    pre0 = prepare_transition(ji, jf)

    def f_delta(d: float, s: float) -> np.ndarray:
        sig = ji * s
        return np.asarray(
            fast_pr(d, align_par(ji, 2, sig), align_par(ji, 4, sig), pre0),
            dtype=float,
        )

    dcol = (f_delta(d0 + h_delta, 0.30) - f_delta(d0 - h_delta, 0.30)) / (
        2.0 * h_delta
    )
    scol = (f_delta(d0, 0.30 + h_sigma) - f_delta(d0, 0.30 - h_sigma)) / (
        2.0 * h_sigma
    )
    j_delta = float(np.linalg.det(np.column_stack((dcol, scol))))
    theta0 = math.radians(xi0)
    tcol = (
        f_delta(math.tan(theta0 + h_theta), 0.30)
        - f_delta(math.tan(theta0 - h_theta), 0.30)
    ) / (2.0 * h_theta)
    j_theta_rad = float(np.linalg.det(np.column_stack((tcol, scol))))

    return {
        "Ji": ji,
        "Jf": jf,
        "mesh_points": len(rows),
        "det_delta_sigma_range": [float(np.min(dets)), float(np.max(dets))],
        "det_delta_sigma_positive_count": int(np.count_nonzero(dets > 0.0)),
        "det_delta_sigma_negative_count": int(np.count_nonzero(dets < 0.0)),
        "det_delta_sigma_zero_count": int(np.count_nonzero(dets == 0.0)),
        "response_finite": bool(
            all(np.isfinite(row["P"]) and np.isfinite(row["ADO"]) for row in rows)
        ),
        "ADO_positive": bool(all(row["ADO"] > 0.0 for row in rows)),
        "sign_change_brackets": sign_changes,
        "isotropic_limit": iso,
        "theta_delta_scaling": {
            "xi_deg": xi0,
            "J_delta": j_delta,
            "J_theta_rad": j_theta_rad,
            "ratio": j_theta_rad / j_delta,
            "expected_1_plus_delta2": 1.0 + d0 * d0,
            "relative_error": abs(
                (j_theta_rad / j_delta) - (1.0 + d0 * d0)
            )
            / (1.0 + d0 * d0),
        },
        "compute_jacobian_tiny_grid": tiny_compute_jacobian_check(ji, jf),
    }


def main() -> int:
    root_cmd = (
        "PYTHONDONTWRITEBYTECODE=1 "
        "PYTHONPATH=raw/writing/pado/Upload:tmp/day25-pado-venv/lib/python3.12/"
        "site-packages:/opt/venv/lib/python3.12/site-packages "
        "python3 outputs/learning-daily/20261027-DAY25-chirality-"
        "counterevidence-shape-coexistence-run-01/pado-jacobian-sign-audit-011.py"
    )
    xis = [-85.0, -80.0, -60.0, -40.0, -20.0, 0.0, 20.0, 40.0, 60.0, 80.0, 85.0]
    sigma_grid = [0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
    result = {
        "schema": "pado-jacobian-sign-audit-011",
        "command": root_cmd,
        "scope": "conditional finite-mesh diagnostic; not a producer, experiment result, global invertibility proof, or global-fold proof",
        "source_scope": {
            "physics": "raw/writing/pado/Upload/p_ado/physics/pado.py",
            "alignment": "raw/writing/pado/Upload/p_ado/physics/sigmaOverI.py",
            "jacobian": "raw/writing/pado/Upload/p_ado/compute/jacobian.py",
            "old_locator": "raw/writing/pado/20260722.pdf printed p.6, Local invertibility §2, lines 433-443",
        },
        "grid": {
            "xi_deg": xis,
            "sigma_over_i": sigma_grid,
            "ADO_detector_angles_deg": [26.0, 90.0],
            "polarimeter_angle_deg": 90.0,
            "h_delta": 1.0e-5,
            "h_sigma_over_i": 1.0e-5,
            "theta_scaling_h_rad": 1.0e-4,
            "endpoint_policy": "exclude ±90° because tan(xi) is singular there",
        },
        "pairs": [
            one_pair(5.5, 4.5, xis, sigma_grid),
            one_pair(9.5, 8.5, xis, sigma_grid),
        ],
        "interpretation_boundary": [
            "A sign bracket indicates a conditional finite-mesh local-detJ diagnostic and motivates refinement.",
            "It does not establish a global fold, a second preimage, or mandatory non-injectivity.",
            "The old p.6 local-invertibility sentence is scoped to that manuscript's explored transition/domain and is not transferred to the second pair.",
            "Isotropic convergence J→0, P→0, ADO→1 is a limiting check, not an experimental measurement.",
        ],
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(OUT.relative_to(ROOT)),
        "pairs": [
            {
                "Ji": p["Ji"],
                "Jf": p["Jf"],
                "range": p["det_delta_sigma_range"],
                "positive": p["det_delta_sigma_positive_count"],
                "negative": p["det_delta_sigma_negative_count"],
                "brackets": len(p["sign_change_brackets"]),
            }
            for p in result["pairs"]
        ],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
