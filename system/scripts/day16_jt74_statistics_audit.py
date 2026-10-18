#!/usr/bin/env python3
"""Audit the actual JT74 F table against exact probabilities and DELTA's F unit.

No experimental confidence interval is refitted. The paper's literal table,
modern F quantiles and a separately identified legacy Fortran table remain
different objects. Source variance and linearity assumptions are not supplied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess

from scipy.integrate import quad
from scipy.stats import f as f_distribution


def f_tail_by_density(value: float, nu: int) -> float:
    """Independent Student-t density quadrature for F(1,nu)'s upper tail."""
    normalization = math.exp(math.lgamma((nu + 1) / 2) - math.lgamma(nu / 2)) / math.sqrt(nu * math.pi)
    integral, _ = quad(lambda t: normalization * (1 + t*t/nu) ** (-(nu + 1)/2),
                       0, math.sqrt(value), epsabs=1e-13, epsrel=1e-13)
    return 1 - 2 * integral


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--delta-input", type=Path, required=True)
    parser.add_argument("--workdir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    delta = json.loads(args.delta_input.read_text())
    assert cfg["identity"] == "JT74-ACTUAL-TABLE3-F-AND-RANK-01"
    assert delta["identity"] == "JT74-DELTA-F-SOURCE-COMPARISON-01"
    root = Path(__file__).resolve().parents[2]
    workdir = args.workdir.resolve()
    assert workdir.is_relative_to(root / "tmp")
    workdir.mkdir(parents=True, exist_ok=True)
    source = Path(delta["source_path"])
    assert hashlib.sha256(source.read_bytes()).hexdigest() == delta["source_sha256"]
    lines = source.read_bytes().splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if b"Real FUNCTION F(N)" in line)
    stop = next(i for i in range(start, len(lines)) if lines[i][:72].strip() == b"END") + 1
    unit = b"".join(lines[start:stop])
    (workdir / "original_F_unit.f").write_bytes(unit)
    # Parse the original fixed-column DATA table independently of the input copy.
    body = "\n".join(line[:72].decode()[6:] for line in lines[start:stop])
    match = re.search(r"DATA\s+FF\s*/(.*?)/", body, re.S | re.I)
    assert match is not None
    ff_values = [float(x) for x in re.findall(r"\d+\.\d+", match[1])]
    assert ff_values == delta["actual_FF_1_to_16"]
    cases = delta["nu_cases_from_source"] + [0, -1]
    driver = ("      PROGRAM FPROBE\n      INTEGER I,NVAL(%d)\n      REAL F\n      EXTERNAL F\n" % len(cases)
              + "      DATA NVAL/" + ",".join(str(x) for x in cases) + "/\n"
              + "      DO 10 I=1,%d\n" % len(cases)
              + "      WRITE(*,'(I4,1X,F16.10)') NVAL(I),F(NVAL(I))\n"
              + "   10 CONTINUE\n      END\n")
    assert all(len(line) <= 72 for line in driver.splitlines())
    (workdir / "fprobe.f").write_text(driver)
    command = ["gfortran", "-std=legacy", "-O0", "-ffixed-form", str(workdir / "original_F_unit.f"),
               str(workdir / "fprobe.f"), "-o", str(workdir / "fprobe")]
    build = subprocess.run(command, capture_output=True, text=True)
    (workdir / "build.log").write_text(build.stdout + build.stderr)
    assert build.returncode == 0, build.stderr
    run = subprocess.run([str(workdir / "fprobe")], capture_output=True, text=True)
    (workdir / "fprobe-output.txt").write_text(run.stdout + run.stderr)
    assert run.returncode == 0, run.stderr
    actual = {int(line.split()[0]): float(line.split()[1]) for line in run.stdout.splitlines()}
    assert set(actual) == set(cases)
    for nu in cases:
        expected = ff_values[nu - 1] if 1 <= nu <= 16 else 1.0
        assert abs(actual[nu] - expected) < 3e-7

    original_rows = []
    quadrature_errors = []
    for nu, table_value in cfg["Table3_nu_F_printed"]:
        exact = float(f_distribution.isf(cfg["source_tail_probability"], 1, nu))
        tail = float(f_distribution.sf(table_value, 1, nu))
        direct = f_tail_by_density(table_value, nu)
        quadrature_errors.append(abs(tail - direct))
        if nu == 1:
            analytic = 1 - 2 / math.pi * math.atan(math.sqrt(table_value))
            assert abs(analytic - tail) < 1e-13
        if nu == 2:
            analytic = 1 - math.sqrt(table_value / (table_value + 2))
            assert abs(analytic - tail) < 1e-13
        tail_box = [float(f_distribution.sf(table_value + .005, 1, nu)),
                    float(f_distribution.sf(table_value - .005, 1, nu))]
        original_rows.append({"nu": nu, "JT74_printed_F": table_value,
                              "F_exact_upper_tail_32percent": exact,
                              "JT74_actual_upper_tail": tail,
                              "tail_with_printed_half_last_digit": tail_box,
                              "nominal_32percent_inside_rounding_box": tail_box[0] <= .32 <= tail_box[1],
                              "source_recipe_takeover_R_over_nu": 1 / table_value,
                              "exact32_recipe_takeover_R_over_nu": 1 / exact})
    assert max(quadrature_errors) < 2e-13
    delta_rows = []
    for nu in delta["nu_cases_from_source"]:
        value = actual[nu]
        delta_rows.append({"nu": nu, "DELTA_actual_F": value,
                           "DELTA_actual_upper_tail": float(f_distribution.sf(value, 1, nu)),
                           "F_exact_CDF_0_683": float(f_distribution.ppf(.683, 1, nu)),
                           "F_exact_upper_tail_32percent": float(f_distribution.isf(.32, 1, nu)),
                           "beyond_16_default": nu > 16})
    # Algebraic identity in R/nu, not a fabricated experimental chi-square sample.
    # Scrit=R+max(1,R*F/nu)=max(R+1,R*(1+F/nu)).
    result = {"identity": cfg["identity"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "delta_input_sha256": hashlib.sha256(args.delta_input.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "original_F_unit_sha256": hashlib.sha256(unit).hexdigest(),
              "F_unit_compiled_unmodified": True, "compile_exit": build.returncode, "run_exit": run.returncode,
              "JT74_Table3_exact_probability_audit": original_rows,
              "DELTA_F_unit_actual_runs": delta_rows,
              "independent_quadrature_max_abs_difference": max(quadrature_errors),
              "invalid_nu_F_unit_returns": {str(nu): actual[nu] for nu in [0, -1]},
              "invalid_nu_boundary": "The isolated F unit defaults to1; this is not a meaningful statistical threshold for nu<=0. Full DELTA's separate degree-of-freedom warning remains necessary.",
              "threshold_identity": "Scrit=R+max(1,R*F/nu)=max(R+1,R*(1+F/nu)); SIGMA is an absolute S threshold, not the increment or parameter sigma.",
              "rank_cases_from_source": cfg["rank_cases"],
              "scope": "Source-table and code-function audit. No original experiment, coverage calibration, nuisance covariance or EL18 producer is reconstructed.",
              "day_index": 16, "partial_day_indices": [17], "formal_day17_credit": False,
              "all_internal_checks_passed": True}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({"output": str(args.output), "compile_exit": build.returncode, "run_exit": run.returncode,
                      "JT74_rows": original_rows, "DELTA_rows": delta_rows,
                      "quadrature_max_abs_error": max(quadrature_errors), "all_internal_checks_passed": True}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
