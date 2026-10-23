#!/usr/bin/env python3
"""Audit of Stopping Power Systematic Covariance on the A ~ 130 HD Plateau.

This script audits Open Question 1 of Day 20:
The potential stretching or compression effect of unpublicized stopping power
systematic covariance on the fine structure of the A ~ 130 highly deformed (HD) platform.

It proves:
1. Across the four HD nuclei in Petrache 1998 Table I (131Ce, 132Ce, 134Nd, 135Nd),
   a standard +/- 15% stopping power scaling uncertainty (f_sys = 7.5% on Q0 ~ tau^-1/2)
   dilates the global weighted average uncertainty from +/- 0.18 eb (stat) to +/- 0.56 eb (stat+sys),
   a 3.06-fold increase, yielding Q0 = 7.06 +/- 0.18 (stat) +/- 0.53 (sys) eb.
2. For the relative isotopic difference between the Ce (Z=58) and Nd (Z=60) chains,
   the rank-1 stopping power covariance cancels by >99%, shifting the uncertainty from
   0.3744 eb (stat) to 0.3764 eb (full), and leaving the z-score virtually unchanged (1.40 -> 1.39 sigma).
3. Therefore, relative HD platform flatness across nuclei is structurally immune to stopping power calibration,
   while absolute deformation parameters (beta2 ~ 0.36-0.38) carry the full +/- 7.5% systematic envelope.
"""

from __future__ import annotations

raise SystemExit("Deactivated checkpoint101: scientific certification withdrawn; original code and results retained in rejected-analysis-registry-101.json; no experimental validation.")

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import numpy as np


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True, help="Run output directory")
    args = parser.parse_args()

    controls: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            raise AssertionError(f"Control failed: {name}")
        controls.append(name)

    # 1. Petrache 1998 Table I literal data for HD bands
    # 131Ce: Q0 = 7.3(4) eb
    # 132Ce: Q0 = 7.4(3) eb (Clark 1992)
    # 134Nd: Q0 = 6.8(3) eb (yrast HD)
    # 135Nd: Q0 = 7.3(10) eb
    nuclei = ["131Ce", "132Ce", "134Nd", "135Nd"]
    y = np.array([7.3, 7.4, 6.8, 7.3], dtype=float)
    err = np.array([0.4, 0.3, 0.3, 1.0], dtype=float)
    V_stat = np.diag(err ** 2)

    # Statistical WLS baseline
    w = 1.0 / (err ** 2)
    w_sum = float(np.sum(w))
    mean_wls = float(np.sum(w * y) / w_sum)
    se_wls = float(1.0 / math.sqrt(w_sum))

    check("WLS mean reproduces literal plateau ~ 7.15 eb", math.isclose(mean_wls, 7.1492, abs_tol=0.01))
    check("WLS standard error reproduces literal error ~ 0.18-0.19 eb", math.isclose(se_wls, 0.1842, abs_tol=0.01))

    # 2. Rank-1 stopping power covariance: 15% stopping error -> 7.5% Q0 error
    f_sys = 0.075
    V_sys = (f_sys ** 2) * np.outer(y, y)
    V_full = V_stat + V_sys

    X = np.ones((4, 1))
    inv_V = np.linalg.inv(V_full)
    cov_mu = np.linalg.inv(X.T @ inv_V @ X)
    mu_gls = float((cov_mu @ (X.T @ inv_V @ y))[0])
    se_gls = float(math.sqrt(cov_mu[0, 0]))
    se_sys = float(math.sqrt(max(0.0, se_gls ** 2 - se_wls ** 2)))

    check("GLS standard error is dilated by factor > 2.5", se_gls / se_wls > 2.5)
    check("Absolute systematic uncertainty on plateau exceeds 0.5 eb", se_sys > 0.5)

    # 3. Relative difference between Ce chain and Nd chain
    # Ce: indices 0, 1; Nd: indices 2, 3
    w_ce = w[:2] / np.sum(w[:2])
    w_nd = w[2:] / np.sum(w[2:])

    mean_ce = float(np.sum(w_ce * y[:2]))
    mean_nd = float(np.sum(w_nd * y[2:]))
    diff = mean_ce - mean_nd

    L = np.array([w_ce[0], w_ce[1], -w_nd[0], -w_nd[1]])
    var_diff_stat = float(L @ V_stat @ L)
    var_diff_full = float(L @ V_full @ L)

    se_diff_stat = float(math.sqrt(var_diff_stat))
    se_diff_full = float(math.sqrt(var_diff_full))

    z_diff_stat = diff / se_diff_stat
    z_diff_full = diff / se_diff_full

    check("Relative difference between Ce and Nd is ~ 0.52 eb", math.isclose(diff, 0.5227, abs_tol=0.01))
    check("Statistical z-score of difference is ~ 1.40 sigma (consistent with flat)", math.isclose(z_diff_stat, 1.396, abs_tol=0.05))
    check("Rank-1 stopping covariance alters difference variance by less than 1.5%", abs(se_diff_full - se_diff_stat) / se_diff_stat < 0.015)
    check("Difference z-score is virtually invariant under rank-1 stopping covariance", math.isclose(z_diff_full, z_diff_stat, rel_tol=0.01))

    # 4. Multi-scale stopping scan
    scan_scales = [0.0, 0.05, 0.075, 0.10, 0.15]
    scan_results = []
    for fs in scan_scales:
        V_s = V_stat + (fs ** 2) * np.outer(y, y)
        inv_Vs = np.linalg.inv(V_s)
        cov_m = np.linalg.inv(X.T @ inv_Vs @ X)
        m = float((cov_m @ (X.T @ inv_Vs @ y))[0])
        se = float(math.sqrt(cov_m[0, 0]))
        v_diff = float(L @ V_s @ L)
        se_d = float(math.sqrt(v_diff))
        scan_results.append({
            "stopping_q0_error_fraction": fs,
            "equivalent_stopping_power_error_percent": fs * 200.0,
            "plateau_mean_eb": m,
            "plateau_total_se_eb": se,
            "plateau_sys_se_eb": float(math.sqrt(max(0.0, se ** 2 - se_wls ** 2))),
            "ce_minus_nd_difference_eb": diff,
            "difference_se_eb": se_d,
            "difference_z_score": diff / se_d
        })

    result = {
        "schema_version": 1,
        "checkpoint": "058",
        "title": "Audit of Stopping Power Systematic Covariance on the A ~ 130 HD Plateau",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "controls_passed": controls,
        "baseline_data": [
            {"nucleus": n, "Q0_eb": float(val), "stat_err_eb": float(e)}
            for n, val, e in zip(nuclei, y, err)
        ],
        "plateau_wls_stat_only": {
            "mean_Q0_eb": mean_wls,
            "stat_uncertainty_eb": se_wls
        },
        "plateau_gls_nominal_15pct_stopping": {
            "mean_Q0_eb": mu_gls,
            "total_uncertainty_eb": se_gls,
            "stat_uncertainty_eb": se_wls,
            "sys_uncertainty_eb": se_sys,
            "uncertainty_dilation_factor": se_gls / se_wls
        },
        "relative_fine_structure_ce_vs_nd": {
            "mean_ce_hd_eb": mean_ce,
            "mean_nd_hd_eb": mean_nd,
            "difference_eb": diff,
            "difference_stat_se_eb": se_diff_stat,
            "difference_full_se_eb": se_diff_full,
            "stat_z_score": z_diff_stat,
            "full_z_score": z_diff_full,
            "relative_immunity_conclusion": "Rank-1 common stopping power uncertainty cancels by >99% in the relative difference between nuclei, proving that the flatness of the HD platform across isotopes is immune to stopping power calibration."
        },
        "stopping_power_scan": scan_results,
        "methodological_boundary": {
            "declared_model": "Rank-1 multiplicative stopping power covariance V = V_stat + f_sys^2 y y^T.",
            "experimental_ci": False,
            "conclusion": "Resolves Open Question 1: global platform height carries +/- 0.53 eb stopping uncertainty, but fine-structure flatness is structurally protected by common-mode cancellation."
        }
    }

    out_path = args.run_dir / "hd-plateau-stopping-covariance-result-058.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(f"Wrote {out_path} ({len(controls)} controls passed)")


if __name__ == "__main__":
    main()
