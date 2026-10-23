#!/usr/bin/env python3
"""Conditional diagnostics of visually checked Singh tables; never a paper fit/CI.

The input is a typed audit ledger. Limits and reused literature rows are not
Gaussian observations. Covariance additions below are declared mathematical
controls, not estimated experimental systematics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.stats import chi2, norm, t


def fit(x, y, covariance):
    x, y, covariance = map(np.asarray, (x, y, covariance))
    design = np.column_stack([np.ones(len(x)), x - x.mean()])
    whiten = np.linalg.cholesky(covariance)
    a = np.linalg.solve(whiten, design)
    b = np.linalg.solve(whiten, y)
    coeff, _, _, _ = np.linalg.lstsq(a, b, rcond=None)
    vc = np.linalg.inv(a.T @ a)
    residual = b - a @ coeff
    one = np.linalg.solve(whiten, np.ones(len(x)))
    constant = float(one @ b / (one @ one))
    chi0 = float(np.sum((b - one * constant) ** 2))
    chi1 = float(residual @ residual)
    z = float(coeff[1] / np.sqrt(vc[1, 1]))
    df = len(x) - 2
    estimated_scale = chi1 / df
    student = z / np.sqrt(estimated_scale)
    return {
        "pivot_spin": float(x.mean()), "intercept_at_pivot": float(coeff[0]),
        "slope_eb_per_hbar": float(coeff[1]),
        "slope_se": float(np.sqrt(vc[1, 1])), "Gaussian_z": z,
        "Gaussian_two_sided_tail": float(2 * norm.sf(abs(z))),
        "constant_eb": constant, "constant_se": float(1 / np.sqrt(one @ one)),
        "constant_chi2": chi0, "constant_dof": len(x) - 1,
        "linear_chi2": chi1, "linear_dof": len(x) - 2,
        "constant_tail": float(chi2.sf(chi0, len(x) - 1)),
        "delta_chi2": chi0 - chi1,
        "estimated_common_error_scale_control": {
            "scale_variance": estimated_scale,
            "slope_se": float(np.sqrt(vc[1, 1] * estimated_scale)),
            "Student_t": float(student), "dof": df,
            "Student_two_sided_tail": float(2 * t.sf(abs(student), df)),
            "boundary": "Additional common unknown error scale estimated from residuals; this is not the known-error Gaussian model.",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    ledger = json.loads(args.input.read_text())
    root = Path(__file__).resolve().parents[2]
    source = root / ledger["source"]
    import re
    raw = root / re.search(r'^raw_file: "(.*)"', source.read_text(), re.M).group(1)
    if hashlib.sha256(raw.read_bytes()).hexdigest() != ledger["raw_sha256"]:
        raise ValueError("literal-ledger/raw identity mismatch")
    checks, cases = [], {}

    def check(name, value):
        checks.append({"name": name, "passed": bool(value)})
        if not value:
            raise AssertionError(name)

    for name in ("case_Ce131", "case_Pr133"):
        rows = ledger[name]["rows"]
        finite = [r for r in rows if r["Qt"]["kind"] == "finite"]
        x = np.array([r["spin"] for r in finite])
        y = np.array([r["Qt"]["value"] for r in finite])
        lower = np.array([r["Qt"]["minus"] for r in finite])
        upper = np.array([r["Qt"]["plus"] for r in finite])
        sigma = (lower + upper) / 2
        diag = np.diag(sigma ** 2)
        base = fit(x, y, diag)
        # Separate centered scalar solution independently checks whitening/GLS.
        weights = 1 / sigma ** 2
        xm = np.average(x, weights=weights)
        ym = np.average(y, weights=weights)
        den = np.sum(weights * (x - xm) ** 2)
        slope = np.sum(weights * (x - xm) * (y - ym)) / den
        check(name + " scalar/whitened agreement", np.isclose(base["slope_eb_per_hbar"], slope))
        check(name + " nested-model delta chi2 equals z2", np.isclose(base["delta_chi2"], base["Gaussian_z"] ** 2))
        perm = np.arange(len(x))[::-1]
        changed = fit(x[perm], y[perm], diag[np.ix_(perm, perm)])
        check(name + " observation order invariant", np.isclose(changed["Gaussian_z"], base["Gaussian_z"]))
        scaled = fit(x, y * 1.1, diag * 1.1 ** 2)
        check(name + " full value/Cov scaling invariant", np.isclose(scaled["Gaussian_z"], base["Gaussian_z"]))
        # Add independent synthetic calibration uncertainty along nuisance vectors.
        # A shared additive offset lies in the intercept space; a method step or
        # spin trend does not. All nuisance amplitudes have units eb.
        offset = np.ones(len(x)) * .30
        trend = (x - np.mean(x)) * .05
        method = np.array([.20 if r["method"] == "DSAM" else 0 for r in finite])
        covariance_controls = {
            "common_additive_0p30eb": fit(x, y, diag + np.outer(offset, offset)),
            "spin_slope_nuisance_0p05eb_per_hbar": fit(x, y, diag + np.outer(trend, trend)),
        }
        if np.any(method):
            covariance_controls["DSAM_group_offset_0p20eb"] = fit(x, y, diag + np.outer(method, method))
        check(name + " additive intercept nuisance preserves slope precision", np.isclose(covariance_controls["common_additive_0p30eb"]["slope_se"], base["slope_se"]))
        check(name + " trend nuisance increases slope variance", np.isclose(covariance_controls["spin_slope_nuisance_0p05eb_per_hbar"]["slope_se"] ** 2, base["slope_se"] ** 2 + .05 ** 2))
        cases[name] = {
            "finite_rows": finite, "excluded_censored_rows": [r for r in rows if r not in finite],
            "mean_asymmetric_errors": base,
            "all_lower_errors_control": fit(x, y, np.diag(lower ** 2)),
            "all_upper_errors_control": fit(x, y, np.diag(upper ** 2)),
            "declared_covariance_controls": covariance_controls,
        }
    ce27 = ledger["case_Ce131"]["rows"][3]
    prfeed = [r["sidefeeding"]["tau_ps"]["value"] for r in ledger["case_Pr133"]["rows"][:3]]
    check("visually verified Ce27 lifetime is 1.25ps", ce27["tau"]["value"] == 1.25)
    check("visually verified Pr sidefeeding is1100/1.9/14ps", prfeed == [1100, 1.9, 14])
    result = {
        "kind": "conditional printed-table diagnostics and declared covariance controls",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "source_sha256": ledger["raw_sha256"], "cases": cases,
        "literal_corrections": {"Ce27_tau_ps": ce27["tau"], "Pr133_sidefeeding_ps": prfeed,
            "Pr133_1100_over_14": 1100 / 14, "Pr133_nonmonotonic": True},
        "checks": checks, "all_controls_passed": all(c["passed"] for c in checks),
        "boundary": "No original counts, MINOS profile, joint covariance, limit likelihood or original producer. Symmetrized Gaussian tails and invented nuisance priors are conditional diagnostics, not experimental confidence intervals or causal feeding attribution.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"output": str(args.output), "controls": len(checks), "conditional_Gaussian_z": {k: v["mean_asymmetric_errors"]["Gaussian_z"] for k, v in cases.items()}}))


if __name__ == "__main__":
    main()
