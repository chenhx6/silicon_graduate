#!/usr/bin/env python3
"""Conditional reduction of the archived 100Ru Table I; no nuclear fit.

The axial rotor K is an explicit assumption. Reported marginal B errors do
not supply a covariance matrix. Fits below assume independent Gaussian B
errors and are diagnostics, not a complete significance calculation.
"""

import argparse
import hashlib
import json
import math
from pathlib import Path


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cg1_squared(spin, kval=0):
    """|<I K 1 0 | I-1 K>|^2, same K at both endpoints."""
    if spin < 1 or abs(kval) > spin - 1:
        raise ValueError("Invalid I->I-1 rotor state")
    return (spin * spin - kval * kval) / (spin * (2 * spin + 1))


def cg2_squared(spin, kval=0):
    """|<I K 2 0 | I-2 K>|^2, same K at both endpoints."""
    if spin < 2 or abs(kval) > spin - 2:
        raise ValueError("Invalid I->I-2 rotor state")
    numerator = (
        3 * (spin + kval) * (spin + kval - 1)
        * (spin - kval) * (spin - kval - 1)
    )
    return numerator / (2 * spin * (spin - 1) * (2 * spin - 1) * (2 * spin + 1))


def moment(bval, prefactor):
    return math.sqrt(bval / prefactor)


def reduce_row(row, kval):
    spin = row["spin"]
    c1 = 3 / (4 * math.pi) * cg1_squared(spin, kval)
    c2 = 5 / (16 * math.pi) * cg2_squared(spin, kval)
    b1, s1 = row["b_e1_e2fm2"], row["db_e1_e2fm2"]
    b2, s2 = row["b_e2_e2fm4"], row["db_e2_e2fm4"]
    d0, q0 = moment(b1, c1), moment(b2, c2)
    # Exact map of the quoted B +/- dB endpoints, not a new coverage claim.
    d0_lo = moment(max(0, b1 - s1), c1)
    d0_hi = moment(b1 + s1, c1)
    sd, sq = d0 * s1 / (2 * b1), q0 * s2 / (2 * b2)
    ratio = d0 / q0
    direct_ratio = math.sqrt(5 / 12 * b1 / b2
                             * cg2_squared(spin, kval) / cg1_squared(spin, kval))
    assert math.isclose(ratio, direct_ratio, rel_tol=2e-14)
    # Length-unit check: 1 b = 100 fm^2.
    assert math.isclose(moment(b2 * 1e-4, c2) * 100, q0, rel_tol=2e-14)
    assert math.isclose(moment(b1 / 100, c1) * 10, d0, rel_tol=2e-14)
    # Shared lifetime scaling of B1 and B2 cancels in D0/Q0.
    for scale in (0.2, 3.7):
        scaled_ratio = moment(scale * b1, c1) / moment(scale * b2, c2)
        assert math.isclose(scaled_ratio, ratio, rel_tol=2e-14)
    rel1, rel2 = s1 / b1, s2 / b2
    return {
        "spin": spin, "parity": row["parity"], "assumed_K": kval,
        "d0_efm": d0, "d0_linear_error_efm": sd,
        "d0_mapped_B_minus_error_efm": d0_lo,
        "d0_mapped_B_plus_error_efm": d0_hi,
        "q0_efm2": q0, "q0_linear_error_efm2": sq,
        "abs_d0_over_q0_fm_inverse": ratio,
        "ratio_linear_relative_error_bounds_unknown_rho": [
            abs(rel1 - rel2) / 2, (rel1 + rel2) / 2
        ],
        "uncertainty_scope": "reported marginal B errors; delta method for ratios; covariance unknown",
    }


def fit_moment_squared(rows, multipole, kval=0):
    """B_i = c_i * x, x=D0^2 or Q0^2; conditional independent-error GLS."""
    if multipole == 1:
        bkey, skey = "b_e1_e2fm2", "db_e1_e2fm2"
        factor = lambda spin: 3 / (4 * math.pi) * cg1_squared(spin, kval)
    elif multipole == 2:
        bkey, skey = "b_e2_e2fm4", "db_e2_e2fm4"
        factor = lambda spin: 5 / (16 * math.pi) * cg2_squared(spin, kval)
    else:
        raise ValueError(multipole)
    den = sum(factor(r["spin"]) ** 2 / r[skey] ** 2 for r in rows)
    estimate = sum(factor(r["spin"]) * r[bkey] / r[skey] ** 2 for r in rows) / den
    chi2 = sum(((r[bkey] - factor(r["spin"]) * estimate) / r[skey]) ** 2
               for r in rows)
    return {
        "multipole": multipole, "assumed_K": kval, "n": len(rows),
        "moment_squared": estimate, "moment_squared_conditional_error": 1 / math.sqrt(den),
        "moment": math.sqrt(estimate), "chi2": chi2, "dof": len(rows) - 1,
        "scope": "independent Gaussian B errors; no raw-spectrum refit; no p-value assigned",
    }


def quoted_difference(dlow, slow, dhigh, shigh, rho):
    variance = slow * slow + shigh * shigh - 2 * rho * slow * shigh
    if variance <= 0:
        raise ValueError("Nonpositive difference variance")
    return (dhigh - dlow) / math.sqrt(variance)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    data = json.loads(args.input.read_text())
    source = root / data["source_pdf"]
    assert sha256(source) == data["source_sha256"], "Source changed"
    finite = [r for r in data["rows"] if r["b_e1_e2fm2"] is not None]
    censored = [r for r in data["rows"] if r["b_e1_e2fm2"] is None]
    assert len(finite) == 6 and len(censored) == 2
    for row in finite:
        assert row["tau_ps"] > 0
        for key in ("b_e1_e2fm2", "db_e1_e2fm2", "b_e2_e2fm4", "db_e2_e2fm4"):
            assert row[key] > 0
    # Known low-spin rotor CG values independent of the data.
    assert math.isclose(cg1_squared(1), 1 / 3)
    assert math.isclose(cg2_squared(2), 1 / 5)
    for spin in range(3, 22):
        for kval in range(min(2, spin - 2) + 1):
            assert math.isclose(cg1_squared(spin, kval), cg1_squared(spin, -kval))
            assert math.isclose(cg2_squared(spin, kval), cg2_squared(spin, -kval))
    reduced = [reduce_row(r, kval) for kval in (0, 1, 2) for r in finite]
    all_fit = fit_moment_squared(finite, 1)
    low_fit = fit_moment_squared([r for r in finite if r["spin"] <= 16], 1)
    high_fit = fit_moment_squared([r for r in finite if r["spin"] > 16], 1)
    delta = all_fit["chi2"] - low_fit["chi2"] - high_fit["chi2"]
    assert delta >= -1e-12
    qfit = fit_moment_squared(finite, 2)
    low, slow = data["author_quoted_d0_low"]
    high, shigh = data["author_quoted_d0_high"]
    sensitivity = [
        {"rho": rho, "standardized_difference": quoted_difference(low, slow, high, shigh, rho)}
        for rho in (-1, -0.75, -0.5, 0, 0.5, 0.75, 1)
    ]
    for rho in (-1, 0, 1):
        a = quoted_difference(low, slow, high, shigh, rho)
        b = quoted_difference(high, shigh, low, slow, rho)
        assert math.isclose(a, -b)
    # A common scale on all B values leaves the conditional shape chi-square invariant.
    scaled = [{**r, "b_e1_e2fm2": 2.3 * r["b_e1_e2fm2"],
               "db_e1_e2fm2": 2.3 * r["db_e1_e2fm2"]} for r in finite]
    assert math.isclose(fit_moment_squared(scaled, 1)["chi2"], all_fit["chi2"], rel_tol=2e-14)
    result = {
        "analysis": "100Ru Table I conditional axial-rotor moment reduction",
        "source_pdf": data["source_pdf"], "source_sha256": data["source_sha256"],
        "input_sha256": sha256(args.input), "script_sha256": sha256(Path(__file__)),
        "source_locator": data["source_locator"],
        "units": {"B1": "e2 fm2", "B2": "e2 fm4", "D0": "e fm", "Q0": "e fm2"},
        "finite_rows_used": len(finite), "upper_limit_rows_not_treated_as_zero": censored,
        "conditional_rotor_results": reduced,
        "K0_independent_B_error_fits": {
            "one_dipole": all_fit, "spin_le16": low_fit, "spin_gt16": high_fit,
            "delta_chi2": delta, "one_quadrupole": qfit,
        },
        "author_quoted_group_moment_covariance_sensitivity": sensitivity,
        "scope": [
            "rotor K scans are assumptions, not measured K assignments",
            "no complete covariance, p-value, static octupole inference or raw DSAM refit",
            "D0 from absolute B(E1) does not require Q0",
            "D0/Q0 from same-parent strengths cancels common lifetime but not unknown branch covariance",
            "group moments quoted by authors and fits here have different uncertainty constructions",
        ],
        "checks": [
            "archived source hash", "missing/upper-limit rows excluded from finite estimates",
            "low-spin CG references", "K-sign symmetry", "fm/barn unit conversion",
            "direct and ratio moment formulas agree", "common lifetime scale cancels in ratio",
            "nested fit does not increase residual", "quoted contrast changes sign on group swap",
            "common B/error scale does not alter conditional shape chi-square",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "finite_rows": 6, "upper_limit_rows": 2, "conditional_delta_chi2": delta,
        "conditional_low_D0": low_fit["moment"], "conditional_high_D0": high_fit["moment"],
        "author_group_contrast_rho0": quoted_difference(low, slow, high, shigh, 0),
        "p_value_assigned": False,
    }, indent=2))


if __name__ == "__main__":
    main()
