#!/usr/bin/env python3
"""Replay ST99 printed calibration and Eq.7; never refit or infer actual Cov."""
from __future__ import annotations

import argparse
from datetime import datetime
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re

import numpy as np


def quoted(value: str) -> tuple[float, float | None]:
    match = re.fullmatch(r"([+-]?(?:\d*\.\d+|\d+))(?:\((\d+)\))?", value)
    if not match:
        raise ValueError(f"Unsupported printed number: {value}")
    center = Decimal(match[1])
    error = None
    if match[2] is not None:
        error = float(Decimal(match[2]) * Decimal(10) ** center.as_tuple().exponent)
    return float(center), error


def q_curve(energy: float, slope: float) -> float:
    x = energy / 511.0
    return (1 + x) / (1 + x + x * x) * (0.31 + slope * energy)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inp = json.loads(args.input.read_text())
    root = Path(__file__).resolve().parents[2]
    raw = root / inp["raw_file"]
    assert hashlib.sha256(raw.read_bytes()).hexdigest() == inp["raw_sha256"]
    assert inp["identity"].endswith("-02"), "Use corrected, frozen input-v2"
    assert "integrated_647_A" not in inp["calibration"]
    assert quoted("0.092(9)") == (0.092, 0.009)
    assert quoted("0.100(8)") == (0.1, 0.008)
    calibration = []
    for energy, reaction, av, pv, qv in inp["calibration"]["rows"]:
        a, sa = quoted(av)
        p, _ = quoted(pv)
        q, sq = quoted(qv)
        calibration.append({
            "E_keV": float(energy), "reaction": reaction,
            "A_over_P": a / p, "sigma_from_A_only_P_fixed": sa / p,
            "printed_Q": q, "printed_sigma_Q": sq,
            "correct_printed_central_curve": q_curve(float(energy), 7e-5),
            "legacy_wrong_exponent_control": q_curve(float(energy), 7e-4),
            "budget_boundary": "P/model/calibration errors and covariance not supplied",
        })
    curve490 = q_curve(490, 7e-5)
    integrated = {
        "source_approx_Q": 0.24, "P_using_source_approx_Q": 0.120 / 0.24,
        "sigma_from_A_only_using_source_approx_Q": 0.012 / 0.24,
        "printed_central_curve_Q": curve490, "P_using_central_curve": 0.120 / curve490,
        "sigma_from_A_only_using_central_curve": 0.012 / curve490,
        "legacy_wrong_exponent_Q": q_curve(490, 7e-4),
        "legacy_wrong_exponent_P": 0.120 / q_curve(490, 7e-4),
        "boundary": "Approximate source Q and fitted central curve are different inputs; no extra Q error invented.",
    }
    h = inp["rounding_diagnostic"]["mean_theory_error_last_decimal_halfwidth"]
    hs = inp["rounding_diagnostic"]["score_halfwidth"]
    results = []
    for table in inp["tables"]:
        observation = [quoted(x) for x in inp["observations"][table["energy"]]["values"]]
        obs = np.array([x[0] for x in observation])
        sig = np.array([x[1] for x in observation])
        assert obs.shape == sig.shape == (5,) and np.all(sig > h)
        for row in table["rows"]:
            theory = np.array([float(x) for x in row["theory"]])
            residual = obs - theory
            standardized = residual / sig
            ndf = row["ndf"]
            central = float(standardized @ standardized / ndf)
            distances = np.abs(residual)
            lower = float(np.sum((np.maximum(distances - 2*h, 0)/(sig+h))**2)/ndf)
            upper = float(np.sum(((distances + 2*h)/(sig-h))**2)/ndf)
            # Independent scalar interval extrema sum exactly for a rowwise box.
            assert 0 <= lower <= central <= upper
            published = float(row["reported_reduced_chi2"])
            overlap = max(lower, published-hs) <= min(upper, published+hs)
            sensitivity = []
            for rho in inp["chosen_correlation_sensitivity"]["rho_polarization_grid"]:
                cor = np.eye(5)
                cor[:4, :4] = (1-rho)*np.eye(4) + rho*np.ones((4,4))
                eigenvalues = np.linalg.eigvalsh(cor)
                assert np.min(eigenvalues) > 0
                value = float(standardized @ np.linalg.solve(cor, standardized)/ndf)
                # Independent decomposition into common and contrast components.
                zp = standardized[:4]
                common = np.sum(zp)**2/4
                analytic = ((zp@zp-common)/(1-rho) + common/(1+3*rho)
                            + standardized[4]**2)/ndf
                assert abs(value-analytic) < 2e-10
                if rho == 0:
                    assert abs(value-central) < 1e-12
                sensitivity.append({"chosen_rho": rho, "reduced_quadratic_score": value,
                                    "smallest_correlation_eigenvalue": float(eigenvalues[0])})
            results.append({
                "table": table["name"], "locator": table["locator"], "energy_keV": int(table["energy"]),
                "spin": row["spin"], "kind": row["kind"], "ndf": ndf,
                "arctan_delta_degrees_or_pure_label": row["arctan_delta"], "sigma_over_I": float(row["sigma_I"]),
                "standardized_residuals": standardized.tolist(), "chi2_contributions": (standardized**2).tolist(),
                "literal_printed_diagonal_reduced_score": central,
                "source_reported_reduced_score": published,
                "conservative_rowwise_rounding_enclosure": [lower,upper],
                "reported_rounding_interval_overlaps_enclosure": overlap,
                "chosen_covariance_sensitivity": sensitivity,
            })
    out = {
        "at_UTC": datetime.now().astimezone().isoformat(), "identity": inp["identity"],
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "raw_sha256_verified": inp["raw_sha256"],
        "calibration_table": calibration, "integrated_490": integrated, "table_replay": results,
        "controls": {"printed_number_parser": True, "raw_hash": True,
                     "rounding_encloses_central": True, "all_chosen_covariances_PD": True,
                     "covariance_inverse_and_analytic_decomposition_agree": True,
                     "rho0_recovers_diagonal": True, "optimized_source_parameters": False,
                     "actual_event_covariance_obtained": False},
        "boundary": "Rounding enclosures are conditional decimal boxes, not confidence intervals. A mismatch remains a reproduction boundary, not an author-error verdict. No p-values, model probabilities or independent sixth integrated-P datum.",
    }
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"calibration490": integrated,
                      "rows": [{k:x[k] for k in ["table", "spin", "ndf", "literal_printed_diagonal_reduced_score", "source_reported_reduced_score", "conservative_rowwise_rounding_enclosure", "reported_rounding_interval_overlaps_enclosure"]} for x in results]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
