#!/usr/bin/env python3
"""Offline audit of actual unmodified DELTA1.01 execution receipts.

Checks native angle coordinates and printed coefficient precision, preserves
all minima/sentinel limits and the known pure-control interpolation failure.
No interpretation as the EL18 experimental producer or covariance is made.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re

import numpy as np

from day16_d96_eq4_erratum_audit import coefficient


def theoretical(spins: tuple, ell: int, delta: float) -> list[float]:
    ji, jm, jf = spins
    first = (("M", 1, 1.0), ("E", 2, delta)) if ell == 1 else (
        ("E", 2, 1.0), ("M", 3, delta))
    pure = (("E", 2, 1.0),)
    return [coefficient(ji, jm, first, k, 0, k, False)
            * coefficient(jm, jf, pure, 0, k, k, False) for k in [2, 4]]


def capture(text: str) -> tuple[list, list]:
    lines = text.splitlines()
    grid, minima = [], []
    in_grid = False
    for i, line in enumerate(lines):
        if "STEPPING IN ATAN(DELTA1)" in line:
            in_grid = True
        if "DELTA(1) MINIMUM" in line:
            in_grid = False
        values = line.split()
        if len(values) == 5:
            try:
                numeric = [float(x) for x in values]
            except ValueError:
                continue
            if in_grid:
                grid.append({"output_line": i+1, "chi2": numeric[0], "A2": numeric[1],
                             "A4": numeric[2], "atan_delta1_deg": numeric[3],
                             "atan_delta2_deg": numeric[4]})
        if "DELTA(1)=" in line:
            match = re.search(r"DELTA\(1\)=\s*(\S+)\s*\+\s*(\S+)\s*-\s*(\S+)\s*SIGMA=\s*(\S+)\s*SIGMA/DEGREE OF FREEDOM=\s*(\S+)", line)
            assert match, line
            numbers = [float(x) for x in match.groups()]
            previous = next(row for row in reversed(lines[:i]) if len(row.split()) == 5
                            and all(re.fullmatch(r"[-+0-9.Ee]+", x) for x in row.split()))
            fitted = [float(x) for x in previous.split()]
            minima.append({"output_line": i+1, "delta_printed": numbers[0],
                           "right_error_printed": numbers[1], "left_error_printed": numbers[2],
                           "right_boundary_not_found_sentinel": numbers[1] == 1000.0,
                           "left_boundary_not_found_sentinel": numbers[2] == 1000.0,
                           "absolute_chi2_threshold_SIGMA": numbers[3],
                           "SIGMA_over_internal_NFREE": numbers[4],
                           "chi2_at_interpolated_minimum": fitted[0],
                           "A2_A4_at_interpolated_minimum_printed": fitted[1:3],
                           "atan_delta1_deg_printed": fitted[3],
                           "SIGMA_is_delta_standard_deviation": False})
    return grid, minima


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--executions", type=Path, required=True)
    parser.add_argument("--followup", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    receipt = json.loads(args.executions.read_text())
    extra = json.loads(args.followup.read_text())
    assert receipt["input_sha256"] == hashlib.sha256(args.input.read_bytes()).hexdigest()
    assert cfg["source_sha256"] == hashlib.sha256(args.source.read_bytes()).hexdigest()
    cases = receipt["cases"] + extra["cases"]
    outputs, global_error = [], 0.0
    for case in cases:
        assert case["exit_code"] == 0
        output = case["output_text"]
        assert "END OF ANALYSIS FOR THIS SPIN COMBINATION" in output
        assert hashlib.sha256(output.encode()).hexdigest() == case["output_sha256"]
        grid, minima = capture(output)
        assert grid and minima
        pure = case["id"].startswith("pure")
        spins, ell = ((4, 2, 0), 2) if pure else ((3, 2, 0), 1)
        errors = []
        for row in grid:
            # The original literal RADS constant is intentionally carried.
            native_delta = math.tan(row["atan_delta1_deg"] * 0.0174532)
            expected = theoretical(spins, ell, native_delta)
            errors += [abs(row[key] - x) for key, x in zip(["A2", "A4"], expected)]
        global_error = max(global_error, max(errors))
        assert max(errors) <= 0.00051  # F9.3 output rounding plus single precision.
        zero_grid = [r for r in grid if abs(r["atan_delta1_deg"]) < 1e-8]
        outputs.append({"id": case["id"], "grid_rows": len(grid),
                        "grid_printed_max_kernel_difference": max(errors),
                        "all_reported_minima": minima, "zero_angle_grid_rows": zero_grid,
                        "source_changed": False,
                        "scope": "Actual public-program output with declared source inputs; printed grid precision only, no original experiment replay."})
    pure2 = next(x for x in outputs if x["id"] == "pure_4_2_0")
    pure1 = next(x for x in outputs if x["id"] == "pure_4_2_0_1deg")
    purepoint1 = next(x for x in outputs if x["id"] == "pure_4_2_0_0p1deg_local")
    pure_minima = [r["all_reported_minima"][0]["chi2_at_interpolated_minimum"]
                   for r in [pure2, pure1, purepoint1]]
    assert pure_minima[0] > pure_minima[1] > pure_minima[2]
    assert pure2["zero_angle_grid_rows"][0]["chi2"] == 0.0
    result = {"identity": "DAY16-DELTA101-OUTPUT-AUDIT-01",
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "execution_receipt_sha256": hashlib.sha256(args.executions.read_bytes()).hexdigest(),
              "followup_receipt_sha256": hashlib.sha256(args.followup.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "source_sha256": cfg["source_sha256"], "cases": outputs,
              "global_max_printed_grid_coefficient_difference": global_error,
              "pure_interpolation_failure_and_refinement": {
                  "known_exact_grid_chi2": 0.0,
                  "interpolated_chi2_at_steps_2_1_0p1_local": pure_minima,
                  "initial_default_step_passed_exact_pure_minimum_test": False,
                  "source_code_modified_to_improve_it": False,
                  "meaning": "Three-point local parabolic approximation moved away from the exact grid minimum. Refinement is necessary for this deliberately precise benchmark; not an experimental data correction."},
              "source_error_rule": "DIPS uses absolute SIGMA=max(SQmin+1,SQmin*(1+F(NFREE)/NFREE)); F is the table labelled F(1,N,0.683). It is neither a delta-axis standard deviation nor universally DeltaChi2=1.",
              "internal_NFREE_rule": "SETUP starts1, adds each DATAtrue item, subtracts each varied mixing coordinate (special fixed-case starts0). This literal counter is not silently replaced with usual Ndata-Nparameters.",
              "sentinel_rule": "ERRL/ERRR initialized1000; retained when no crossing found in the angular scan. Do not parse the printed1000 as a finite measured error or complete wrapped confidence set.",
              "independence_rule": "SQRES is a sum of squared standardized residuals, with no cross-covariance or pure-theory uncertainty input.",
              "generic_code_evidence_only": True,
              "EL18_2018_exact_source_input_response_covariance_recovered": False,
              "all_offline_integrity_and_declared_kernel_checks_passed": True}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({k: result[k] for k in result if k != "cases"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
