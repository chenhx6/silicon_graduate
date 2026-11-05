#!/usr/bin/env python3
"""Conditional two-rank profile in coefficient space, without ratio errors.

The Gaussian covariance, shared parent tensor and response ratios are
declared scenarios. Free real reference coefficients are profiled. This
relaxes, rather than verifies, magnetic-substate-population positivity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.optimize import minimize_scalar

from rank4_invariant import load_rows, native_f


def coefficient_ratios(theta: np.ndarray | float) -> np.ndarray:
    """Signed delta=tan(theta); cosine/sine form includes the pure-E2 limit."""
    c, s = np.cos(theta), np.sin(theta)
    rank2 = -0.7 * c * c + 1.4 * math.sqrt(11) * c * s - 0.1 * s * s
    rank4 = -(8 / 3) * s * s
    return np.stack((rank2, rank4), axis=-1)


def covariance(scales: np.ndarray, rho_within: float, rho_cross: float) -> np.ndarray:
    if not (abs(rho_within) < 1 and abs(rho_cross) < 1):
        raise ValueError("correlation scenarios must define positive-definite matrices")
    if len(scales) != 4 or np.any(scales <= 0) or not np.all(np.isfinite(scales)):
        raise ValueError("four positive finite error scales are required")
    rank = np.array([[1.0, rho_within], [rho_within, 1.0]])
    line = np.array([[1.0, rho_cross], [rho_cross, 1.0]])
    return np.outer(scales, scales) * np.kron(line, rank)


def profiled_distance(
    theta: np.ndarray | float, y: np.ndarray, cov: np.ndarray, response: np.ndarray
) -> np.ndarray:
    """Exact Gaussian nuisance minimum for each theta: (Ly)'(LVL')^-1(Ly).

    This is profiling with fixed covariance, not integration over reference
    coefficients; no log-determinant of the projected covariance is added.
    """
    g = coefficient_ratios(theta) * response
    residual = y[:2] - g * y[2:]
    c00 = cov[0, 0] - 2 * g[..., 0] * cov[0, 2] + g[..., 0] ** 2 * cov[2, 2]
    c11 = cov[1, 1] - 2 * g[..., 1] * cov[1, 3] + g[..., 1] ** 2 * cov[3, 3]
    c01 = (
        cov[0, 1]
        - g[..., 1] * cov[0, 3]
        - g[..., 0] * cov[2, 1]
        + g[..., 0] * g[..., 1] * cov[2, 3]
    )
    determinant = c00 * c11 - c01 * c01
    if np.any(determinant <= 0):
        raise ValueError("projected covariance must be positive definite")
    return (
        c11 * residual[..., 0] ** 2
        - 2 * c01 * residual[..., 0] * residual[..., 1]
        + c00 * residual[..., 1] ** 2
    ) / determinant


def direct_gls(theta: float, y: np.ndarray, cov: np.ndarray, response: np.ndarray) -> float:
    """Independent nuisance fit used to check the projected-residual formula."""
    g = coefficient_ratios(theta) * response
    design = np.vstack((np.diag(g), np.eye(2)))
    whitened_design = np.linalg.solve(np.linalg.cholesky(cov), design)
    whitened_y = np.linalg.solve(np.linalg.cholesky(cov), y)
    nuisance, *_ = np.linalg.lstsq(whitened_design, whitened_y, rcond=None)
    residual = whitened_y - whitened_design @ nuisance
    return float(residual @ residual)


def minimum_in_interval(
    y: np.ndarray, cov: np.ndarray, response: np.ndarray,
    lo: float, hi: float, grid_size: int,
) -> dict:
    grid = np.linspace(lo, hi, grid_size)
    values = profiled_distance(grid, y, cov, response)
    candidates = [(float(values[0]), lo), (float(values[-1]), hi)]
    for i in np.flatnonzero((values[1:-1] <= values[:-2]) & (values[1:-1] <= values[2:])) + 1:
        result = minimize_scalar(
            lambda angle: float(profiled_distance(angle, y, cov, response)),
            bounds=(grid[i - 1], grid[i + 1]), method="bounded",
            options={"xatol": 1e-13},
        )
        if not result.success:
            raise RuntimeError("local profile refinement failed")
        candidates.append((float(result.fun), float(result.x)))
    score, theta = min(candidates)
    return {
        "distance": score,
        "theta_radians": theta,
        "delta_at_diagnostic_minimum": None if abs(math.cos(theta)) < 1e-12 else math.tan(theta),
        "pure_E2_endpoint": abs(math.cos(theta)) < 1e-12,
        "f_E2_at_diagnostic_minimum": math.sin(theta) ** 2,
        "not_an_experimental_estimate": True,
    }


def branch_minima(y: np.ndarray, cov: np.ndarray, response: np.ndarray, grid_size: int = 1025) -> dict:
    spans = {
        "negative_large": (-math.pi / 2, -math.pi / 4),
        "small": (-math.pi / 4, math.pi / 4),
        "positive_large": (math.pi / 4, math.pi / 2),
    }
    branches = {
        name: minimum_in_interval(y, cov, response, lo, hi, grid_size)
        for name, (lo, hi) in spans.items()
    }
    # The |delta|=1 boundary is included in both adjacent closures.
    best_large = min((branches["negative_large"], branches["positive_large"]), key=lambda b: b["distance"])
    return {
        "branches": branches,
        "global": min(branches.values(), key=lambda b: b["distance"]),
        "distance_small_minus_large": branches["small"]["distance"] - best_large["distance"],
    }


def analyze(article_root: Path) -> dict:
    csv_path = article_root / "data/ba129_same_parent_A4.csv"
    contract_path = article_root / "data/input-contract.json"
    rows = load_rows(csv_path, require_reference_nonzero=False)
    contract = json.loads(contract_path.read_text())
    t, r = rows["target_365"], rows["reference_462"]
    y = np.array([t["A2"], t["A4"], r["A2"], r["A4"]], dtype=float)
    response = np.array(contract["response_ratio_s2_s4"], dtype=float)
    if response.shape != (2,) or not np.all(np.isfinite(response)) or np.any(response == 0):
        raise ValueError("two finite nonzero response ratios are required for this scenario")
    # Check analytic coefficients against the independent factorial implementation.
    fref = native_f(13, 9, 2, 2, 2)
    matrix = np.array([[native_f(13, 11, 2, a, b) / fref for b in (1, 2)] for a in (1, 2)])
    analytic = np.array([[-0.7, 0.7 * math.sqrt(11)], [0.7 * math.sqrt(11), -0.1]])
    assert np.max(np.abs(matrix - analytic)) < 1e-12

    cases = []
    direct_checks = []
    refinement_checks = []
    for scenario in contract["uncertainty_scenarios"]:
        scales = np.array(scenario["standard_error_scales"], dtype=float)
        for rho_within in contract["correlation_grid"]:
            for rho_cross in contract["correlation_grid"]:
                cov = covariance(scales, rho_within, rho_cross)
                assert np.min(np.linalg.eigvalsh(cov)) > 0
                fit = branch_minima(y, cov, response)
                cases.append({
                    "scenario": scenario["id"], "rho_within_line": rho_within,
                    "rho_cross_line": rho_cross, **fit,
                })
                if rho_within == 0 and rho_cross == 0:
                    refined = branch_minima(y, cov, response, 2049)
                    refinement_checks.append(abs(fit["global"]["distance"] - refined["global"]["distance"]))
                    for theta in [-1.4, -0.8, -0.2, 0.0, 0.7, math.pi / 2]:
                        direct_checks.append(abs(
                            direct_gls(theta, y, cov, response)
                            - float(profiled_distance(theta, y, cov, response))
                        ))
        # Non-diagonal covariance is essential for checking the projection signs.
        cov = covariance(scales, -0.4, 0.8)
        for theta in [-1.2, -0.4, 0.3, 1.4]:
            direct_checks.append(abs(
                direct_gls(theta, y, cov, response)
                - float(profiled_distance(theta, y, cov, response))
            ))

    assert max(direct_checks) < 1e-9
    assert max(refinement_checks) < 1e-8
    zero = np.zeros(4)
    isotropic_distances = profiled_distance(np.linspace(-math.pi / 2, math.pi / 2, 51), zero, np.eye(4), response)
    assert np.all(isotropic_distances == 0)
    # Generated coefficient control with a physical common m=+/-1/2 ensemble.
    for delta in [-2.0, -0.33, 0.5]:
        reference = np.array([40 / 91, -216 / 1001])
        y_control = np.r_[coefficient_ratios(math.atan(delta)) * reference, reference]
        assert float(profiled_distance(math.atan(delta), y_control, np.eye(4), np.ones(2))) < 1e-27

    minimum = -(2 + math.sqrt(137)) / 5
    result = {
        "scope": "conditional coefficient-space nuisance profiling; not an experimental refit",
        "input_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        "contract_sha256": hashlib.sha256(contract_path.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "runtime": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
        "rank2": {
            "reference_normalized_matrix": analytic.tolist(),
            "quotient": "(-7 + 14*sqrt(11)*delta - delta^2)/(10*(1+delta^2))",
            "lower_bound": minimum,
            "upper_bound": (-2 + math.sqrt(137)) / 5,
            "central_ratio": float(y[0] / y[2]),
            "positive_s2_needed_at_central_values": float(y[0] / y[2] / minimum),
            "condition": "shared rank-2 selected-parent tensor; bound on response-corrected ratio only",
        },
        "profile_definition": "min over real b2,b4 of (y-B_delta b)' V^-1 (y-B_delta b)",
        "response_ratios_s2_s4": response.tolist(),
        "cases": cases,
        "controls": {
            "maximum_projected_vs_direct_GLS_error": max(direct_checks),
            "maximum_1025_vs_2049_grid_refined_distance_change": max(refinement_checks),
            "isotropic_reference_all_delta_unidentified": True,
            "physical_same_parent_coefficient_controls_passed": True,
        },
        "boundary": [
            "covariance is a chosen finite family; no actual covariance inferred",
            "OCR error-scale scenario keeps evaluated signs and means; it is not a corrected measurement",
            "free reference coefficients relax physical population-positivity constraints",
            "branch distance contrasts have no p-value, probability or confidence interpretation",
            "same-parent state identity does not establish identical postselection or response",
        ],
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).parent / "results/companion-profile.json")
    args = parser.parse_args()
    result = analyze(Path(__file__).resolve().parents[1])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    central = [case for case in result["cases"] if case["rho_within_line"] == case["rho_cross_line"] == 0]
    print(json.dumps({"rank2": result["rank2"], "diagonal_cases": central, "controls": result["controls"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
