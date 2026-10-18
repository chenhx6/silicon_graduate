#!/usr/bin/env python3
"""Replay Zheng2013 printed DCO/calibration data, not its missing producer.

Day16's uncredited Day17 preview: input decimals retain their printed precision.
Uncertainty-envelope tests are conditional, first-order delta-method diagnostics;
they neither infer the unpublished covariance nor correct the source's errors.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
import re

import numpy as np


def quoted(value: str) -> tuple[float, float, float]:
    """Return central value, parenthetical uncertainty, last decimal unit."""
    match = re.fullmatch(r"([+-]?\d+(?:\.\d+)?)\((\d+)\)", value)
    if match is None:
        raise ValueError(value)
    decimal, digits = match.groups()
    n_decimals = len(decimal.split(".")[1]) if "." in decimal else 0
    unit = 10.0 ** -n_decimals
    return float(decimal), int(digits) * unit, unit


def p90(a2: float, a4: float) -> float:
    denominator = 8.0 - 4.0 * a2 + 3.0 * a4
    if denominator <= 0:
        raise ValueError("Nonpositive angular-distribution denominator")
    return (12.0 * a2 + 5.0 * a4) / denominator


def p_gradient(a2: float, a4: float) -> np.ndarray:
    denominator = 8.0 - 4.0 * a2 + 3.0 * a4
    return np.array([(96.0 + 56.0 * a4) / denominator**2,
                     (40.0 - 56.0 * a2) / denominator**2])


def qpoint(energy: np.ndarray | float, electron_mass_keV: float) -> np.ndarray:
    x = np.asarray(energy) / electron_mass_keV
    return (1.0 + x) / (1.0 + x + x**2)


def interval_gap(first: tuple[float, float], second: tuple[float, float]) -> float:
    return max(0.0, first[0] - second[1], second[0] - first[1])


def overlaps(first: tuple[float, float], second: tuple[float, float]) -> bool:
    return max(first[0], second[0]) <= min(first[1], second[1])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    assert cfg["identity"] == "DAY16-PARTIAL17-Z13-PRINTED-CALIBRATION-01"
    assert len(cfg["TableI"]) == 11
    rows = []
    derivative_errors = []
    for row in cfg["TableI"]:
        aa, sa, ua = quoted(row["A"])
        pp, sp, up = quoted(row["P"])
        qq, sq, uq = quoted(row["Q"])
        a2, s2, u2 = quoted(row["A2"])
        a4, s4, u4 = quoted(row["A4"])
        assert min(aa, pp, qq, sa, sp, sq) > 0
        nominal_p = p90(a2, a4)
        g = p_gradient(a2, a4)
        for idx, central in enumerate([a2, a4]):
            step = 1e-6
            point = [a2, a4]
            point[idx] = central + step
            plus = p90(*point)
            point[idx] = central - step
            minus = p90(*point)
            derivative_errors.append(abs((plus - minus) / (2 * step) - g[idx]))
        p_corners = [p90(a2 + x * u2 / 2, a4 + y * u4 / 2)
                     for x, y in itertools.product([-1, 1], repeat=2)]
        p_box = (min(p_corners), max(p_corners))
        p_print_box = (pp - up / 2, pp + up / 2)
        q_box = ((aa - ua / 2) / (pp + up / 2),
                 (aa + ua / 2) / (pp - up / 2))
        q_print_box = (qq - uq / 2, qq + uq / 2)
        u = sa / pp
        v = aa * sp / pp**2
        sigma_q_range = (abs(u - v), u + v)
        rho_required = (u*u + v*v - sq*sq) / (2*u*v)
        # Liberal independent interval relaxation also permits rounding of each
        # quoted standard deviation by half its last digit. Dependency relaxation
        # can only lower the true minimum; a surviving exclusion is conservative.
        a_lo, a_hi = aa - ua / 2, aa + ua / 2
        p_lo, p_hi = pp - up / 2, pp + up / 2
        u_box = ((sa - ua / 2) / p_hi, (sa + ua / 2) / p_lo)
        v_box = (a_lo * (sp - up / 2) / p_hi**2,
                 a_hi * (sp + up / 2) / p_lo**2)
        relaxed_minimum = interval_gap(u_box, v_box)
        sigma_q_rounding_upper = sq + uq / 2
        pg2, pg4 = abs(g[0] * s2), abs(g[1] * s4)
        rho_ad = (sp*sp - pg2*pg2 - pg4*pg4) / (2*pg2*pg4)
        rows.append({
            **row,
            "P90_from_printed_coefficients": nominal_p,
            "P90_printing_box": p_box,
            "P90_printing_boxes_overlap": overlaps(p_box, p_print_box),
            "P90_error_local_covariance_envelope": [abs(pg2-pg4), pg2+pg4],
            "rho_A2_A4_required_if_quoted_errors_same_marginals": rho_ad,
            "A_over_P": aa / pp,
            "Q_printing_box_from_A_P": q_box,
            "Q_printing_boxes_overlap": overlaps(q_box, q_print_box),
            "sigma_Q_if_A_P_independent": math.hypot(u, v),
            "sigma_Q_any_local_covariance_envelope": sigma_q_range,
            "rho_A_P_required_if_quoted_errors_same_marginals": rho_required,
            "sigma_Q_nominal_outside_local_envelope": not -1 <= rho_required <= 1,
            "sigma_Q_relaxed_rounding_lower_bound": relaxed_minimum,
            "sigma_Q_printed_rounding_upper": sigma_q_rounding_upper,
            "sigma_Q_exclusion_survives_liberal_rounding": relaxed_minimum > sigma_q_rounding_upper,
        })
    assert max(derivative_errors) < 1e-8

    energies = np.array([row["E_keV"] for row in cfg["TableI"]], float)
    qs = np.array([quoted(row["Q"])[0] for row in cfg["TableI"]])
    sigmas = np.array([quoted(row["Q"])[1] for row in cfg["TableI"]])
    point = qpoint(energies, cfg["calibration"]["mec2_keV"])
    design = np.column_stack([point, point * energies])
    whitened = design / sigmas[:, None]
    params, _, rank, _ = np.linalg.lstsq(whitened, qs / sigmas, rcond=None)
    assert rank == 2
    covariance = np.linalg.inv(whitened.T @ whitened)
    residual = qs - design @ params
    chi2 = float(np.sum((residual / sigmas)**2))
    p_reported = np.array([quoted(cfg["calibration"]["p0"])[0],
                           quoted(cfg["calibration"]["p1_keV_inv"])[0]])
    chi2_reported_params = float(np.sum(((qs - design @ p_reported) / sigmas)**2))
    # Independent centered-coordinate algebra controls numerical parameter scaling.
    pivot = 800.0
    centered_design = np.column_stack([point, point * (energies - pivot)])
    centered, *_ = np.linalg.lstsq(centered_design / sigmas[:, None], qs / sigmas, rcond=None)
    assert np.max(np.abs(params - [centered[0] - pivot * centered[1], centered[1]])) < 1e-12
    # Same-data residual response, essential when discussing calibration roundtrips.
    hat = whitened @ covariance @ whitened.T
    assert np.max(np.abs(hat @ hat - hat)) < 1e-12
    assert abs(float(np.trace(hat)) - 2) < 1e-12

    dco = []
    for row in cfg["Fig2"]["rows"]:
        numerator, sn = row["target_135"]
        denominator, sd = row["target_90"]
        ratio = numerator / denominator
        err = ratio * math.hypot(sn/numerator, sd/denominator)
        u, v = sn/denominator, numerator*sd/denominator**2
        dco.append({**row, "gate_keV": cfg["Fig2"]["gate_E_keV"],
                    "R_from_areas": ratio,
                    "sigma_R_independent_area_diagnostic": err,
                    "sigma_R_any_local_area_covariance_envelope": [abs(u-v), u+v],
                    "spurious_extra_Reff_factor_result": ratio * quoted(cfg["calibration"]["R_eff"])[0]})
    # Constant efficiency-ratio cancellation for two actual photon energies.
    # eps90(E)=c*eps135(E) gives eps135(E1)eps90(E2)/
    # eps90(E1)eps135(E2)=1; c is not an extra DCO correction.
    c = quoted(cfg["calibration"]["R_eff"])[0]
    efficiency_product_control = (1.0 * c) / (c * 1.0)
    assert efficiency_product_control == 1

    result = {
        "identity": cfg["identity"],
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "TableI_replay": rows,
        "central_P_printing_nonclosures_keV": [r["E_keV"] for r in rows if not r["P90_printing_boxes_overlap"]],
        "central_Q_printing_nonclosures_keV": [r["E_keV"] for r in rows if not r["Q_printing_boxes_overlap"]],
        "nominal_local_Q_error_exclusions_keV": [r["E_keV"] for r in rows if r["sigma_Q_nominal_outside_local_envelope"]],
        "rounding_robust_local_Q_error_exclusions_keV": [r["E_keV"] for r in rows if r["sigma_Q_exclusion_survives_liberal_rounding"]],
        "diagonal_quoted_Q_fit": {
            "p0_p1": params.tolist(), "unscaled_conditional_covariance": covariance.tolist(),
            "parameter_error_if_independent_Q_rows": np.sqrt(np.diag(covariance)).tolist(),
            "parameter_correlation": float(covariance[0, 1] / np.sqrt(covariance[0, 0] * covariance[1, 1])),
            "chi2": chi2, "n_rows": len(qs), "n_params": 2,
            "chi2_at_printed_params": chi2_reported_params,
            "hat_diagonal": np.diag(hat).tolist(),
            "reuse_boundary": "Q_i=A_i/P_i calibrated from these same transitions; A_i/Qfit(E_i) is an in-sample residual, not an independent P validation.",
            "missing": ["full Q_i covariance", "A_i-Qfit covariance", "original least-squares/error recipe"],
        },
        "Fig2_area_replay": dco,
        "efficiency_product_control": efficiency_product_control,
        "TableII_identity_controls": cfg["TableII_selected"],
        "gradient_max_abs_error": max(derivative_errors),
        "status": "conditional-printed-data-audit; source uncertainty semantics remain unresolved",
        "all_internal_checks_passed": True,
        "day_index": 16, "partial_day_indices": [17], "formal_day17_credit": False,
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"output": str(args.output),
                      "P_nonclosures": result["central_P_printing_nonclosures_keV"],
                      "Q_nonclosures": result["central_Q_printing_nonclosures_keV"],
                      "nominal_error_exclusions": result["nominal_local_Q_error_exclusions_keV"],
                      "rounding_robust_error_exclusions": result["rounding_robust_local_Q_error_exclusions_keV"],
                      "diagonal_Q_fit": result["diagonal_quoted_Q_fit"],
                      "DCO_replay": dco,
                      "all_internal_checks_passed": True}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
