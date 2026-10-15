#!/usr/bin/env python3
"""Recheck printed conditional chi-square values and arctan-delta units.

No magnetic-substate model, raw angular fit or experimental confidence interval
is reconstructed. Rounding intervals are necessary arithmetic checks only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"


def number(literal):
    match = re.fullmatch(r"([+-]?\d+\.\d+)\((\d+)\)", literal)
    places = len(match[1].split(".")[1])
    return float(match[1]), int(match[2]) * 10 ** -places, 0.5 * 10 ** -places


def round_half(literal):
    return 0.5 * 10 ** -len(literal.split(".")[1])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RUN / "ionescu1981-feeding-table-audit.json")
    args = parser.parse_args()
    data = json.loads((RUN / "ionescu1981-table-input.json").read_text())
    proof = json.loads((RUN / "ionescu1981-pdf-verification-working.json").read_text())
    checks = {}

    def check(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)

    check("original_hash_unchanged", hashlib.sha256((ROOT / proof["path"]).read_bytes()).hexdigest() == data["source_sha256"])
    check("ten_table1_transitions_not_twenty_independent_rows", len(data["table1"]) == 10)
    records = []
    for row in data["table1"]:
        chi, lower, upper = 0.0, 0.0, 0.0
        for rank in [2, 4]:
            obs, error, half = number(row[f"A{rank}_exp"])
            calc_literal = row[f"A{rank}_calculated"]
            difference = abs(obs - float(calc_literal))
            residual_half = half + round_half(calc_literal)
            chi += (difference / error) ** 2
            lower += (max(0, difference - residual_half) / (error + half)) ** 2
            upper += ((difference + residual_half) / (error - half)) ** 2
        reported = float(row["reported_chi2"])
        chalf = round_half(row["reported_chi2"])
        check("rounding_compatible_" + row["Egamma_literal_kev"], lower <= reported + chalf and upper >= max(0, reported - chalf))
        records.append(row | {"recomputed_from_displayed_centers": chi, "necessary_rounding_interval": [lower, upper], "not_full_model_refit": True})
    check("multiplet_warning_retained", data["table1"][-1]["multiplet"] == "T" and data["table1"][0]["multiplet"] == "Q")
    fits = []
    for line in data["table2"]:
        for fit in line["fits"]:
            theta = fit["arctan_delta_deg"]
            lo, hi = theta - fit["angle_error_minus"], theta + fit["angle_error_plus"]
            delta = math.tan(math.radians(theta))
            values = [math.sin(math.radians(x)) ** 2 for x in [lo, hi]]
            if lo <= 0 <= hi:
                values.append(0.0)
            fits.append(fit | {"Egamma_kev": line["Egamma_kev"], "angle_interval_deg": [lo, hi], "delta": delta, "delta_endpoint_range": [math.tan(math.radians(lo)), math.tan(math.radians(hi))], "conditional_radiative_E2_fraction": math.sin(math.radians(theta)) ** 2, "fraction_endpoint_range": [min(values), max(values)], "coverage_not_recovered": True})
            check("radiative_identity_" + str(len(fits)), math.isclose(delta * delta / (1 + delta * delta), math.sin(math.radians(theta)) ** 2))
    check("three_lines_seven_hypothesis_roots", len(data["table2"]) == 3 and len(fits) == 7)
    same = [f for f in fits if f["Egamma_kev"] == "251.03"]
    check("same_coefficients_allow_three_roots_in_source", len(same) == 3 and {f["arctan_delta_deg"] for f in same} == {76, 18, -7.5})
    small = next(f for f in same if f["arctan_delta_deg"] == -7.5)
    naive = (-7.5) ** 2 / (1 + (-7.5) ** 2)
    check("degree_value_not_dimensionless_delta", naive > 0.98 and small["conditional_radiative_E2_fraction"] < 0.02)
    check("zero_local_sidefeeding_sigma_coefficient", data["table3_zero_sidefeeding"]["sidefeeding_intensity_Is"] == 0)
    check("no_raw_covariance_or_CI_inferred", data["actual_covariance"] is data["confidence_coverage"] is data["full_model_inputs"] is None)
    output = {"kind": "printed conditional Eq7 and table-unit audit, not population-model reanalysis", "source_doi": data["source_doi"], "source_sha256": data["source_sha256"], "table1_checks": records, "table2_hypothesis_transforms": fits, "wrong_degree_as_delta_control": {"chosen_wrong_delta": -7.5, "wrong_fraction": naive, "correct_fraction_for_source_angle_minus7p5deg": small["conditional_radiative_E2_fraction"]}, "Table3_zero_sidefeeding": data["table3_zero_sidefeeding"] | {"derivative_local_rho_wrt_local_sigma": "Is/IT * d rho_sf/dsigma = 0, holding parents/U/intensities fixed", "actual_parent_tensors_or_derivative_numeric_not_inferred": True}, "actual_fit_covariance": None, "actual_coverage": None, "checks": checks, "check_count": len(checks), "passed": all(checks.values())}
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"checks": len(checks), "passed": output["passed"], "table1_rows": len(records), "Table2_roots": len(fits), "251_transforms": [{k: f[k] for k in ["arctan_delta_deg", "delta", "conditional_radiative_E2_fraction"]} for f in same], "no_model_refit": True}))


if __name__ == "__main__":
    main()
