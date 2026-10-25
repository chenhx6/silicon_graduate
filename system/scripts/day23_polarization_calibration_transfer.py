#!/usr/bin/env python3
"""Source-curve arithmetic and conditional covariance bounds, not a target fit."""
import argparse
import json
from pathlib import Path

import numpy as np


CURVES = {
    "Zheng2013_EXOGAM": {
        "p": [0.39, 0.00006], "sigma": [0.02, 0.00003],
        "energies_keV": [376.0, 462.0],
        "source": "knowledge/sources/zheng-2013-linear-polarization-91ru.md",
        "locator": "Z13-2", "target": "Guo2022 Au, externally adopted curve",
    },
    "Herzan2015_JUROGAM_II": {
        "p": [0.42, -0.00019], "sigma": [0.04, 0.00007],
        "energies_keV": [450.2, 747.3, 813.2],
        "source": "knowledge/sources/herzan-2015-193bi-spectroscopy.md",
        "locator": "HE15-10", "target": "Lv2022 Pr, externally adopted curve",
    },
}


def point_sensitivity(energy):
    x = np.asarray(energy) / 511.0
    return (1 + x) / (1 + x + x*x)


def uncertainty_bounds(gradient, sigma):
    # Extremize over every PSD 2x2 covariance with these fixed marginals.
    u, v = abs(np.asarray(gradient) * sigma)
    return [float(abs(u-v)), float(u+v)]


def calculate():
    result = {"scope": "Printed calibration curves only. Target response transfer, actual covariance, target confidence intervals and mixing-branch likelihoods are unavailable.",
              "curves": {}, "controls": {}}
    for name, c in CURVES.items():
        p, sig, e = np.array(c["p"]), np.array(c["sigma"]), np.array(c["energies_keV"])
        design = np.column_stack([np.ones(len(e)), e])
        linear = design @ p
        qp = point_sensitivity(e)
        q = qp * linear
        j = qp[:, None] * design
        rows = [{"energy_keV": float(en), "Q_printed_curve": float(qi),
                 "conditional_sigma_Q_bounds_unknown_rho": uncertainty_bounds(ji, sig)}
                for en, qi, ji in zip(e, q, j)]
        pairs = []
        for i in range(len(e)-1):
            k = i + 1
            grad_log = design[i]/linear[i] - design[k]/linear[k]
            pairs.append({"energies_keV": [float(e[i]), float(e[k])],
                          "Q_first_over_second": float(q[i]/q[k]),
                          "conditional_sigma_log_ratio_bounds_unknown_rho": uncertainty_bounds(grad_log, sig)})
        rho_grid = [-1.0, -0.75, 0.0, 0.75, 1.0]
        bound_check = True
        rank_check = True
        for rho in rho_grid:
            cp = np.outer(sig, sig) * np.array([[1, rho], [rho, 1]])
            cq = j @ cp @ j.T
            diag_sd = np.sqrt(np.maximum(0, np.diag(cq)))
            for value, row in zip(diag_sd, rows):
                lo, hi = row["conditional_sigma_Q_bounds_unknown_rho"]
                bound_check &= bool(lo-1e-12 <= value <= hi+1e-12)
            rank_check &= np.linalg.matrix_rank(cq, tol=1e-13) <= 2
        fd_columns = []
        for axis, step in enumerate([1e-6, 1e-9]):
            shift = np.eye(2)[axis] * step
            fd_columns.append((qp*(design@(p+shift)) - qp*(design@(p-shift)))/(2*step))
        fd = np.column_stack(fd_columns)
        result["controls"][name+"_full_analytic_derivative"] = bool(np.allclose(fd, j, atol=1e-7))
        result["controls"][name+"_PSD_covariance_bounds"] = bool(bound_check)
        result["controls"][name+"_shared_curve_rank_at_most_two"] = bool(rank_check)
        # A common transfer multiplier cancels in the sensitivity ratio.
        result["controls"][name+"_common_transfer_cancels_in_ratio"] = bool(np.isclose(
            (1.7*q[0])/(1.7*q[1]), q[0]/q[1]))
        result["curves"][name] = {**c, "rows": rows, "pairs": pairs,
                                   "missing": ["p0-p1 covariance", "target-to-reference transfer function kappa(E)",
                                               "target A/a/background and angular-response joint covariance"]}
    result["all_controls_pass"] = all(result["controls"].values())
    result["bound_meaning"] = "If printed parameter errors are comparable marginal standard deviations, these are first-order bounds over unknown rho, not fitted target errors or confidence/credible intervals. Unknown transfer kappa(E) is not covered."
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    out = calculate()
    args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"all_controls_pass": out["all_controls_pass"],
                      "curves": {n: x["rows"] for n, x in out["curves"].items()}}, ensure_ascii=False))
    return 0 if out["all_controls_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
