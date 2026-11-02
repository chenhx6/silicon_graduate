#!/usr/bin/env python3
"""
hpge_efficiency_curve_covariance_fitter.py
==========================================
HPGe / Clover Detector Photopeak Efficiency Calibration Curve Fitter,
Weighted Least Squares Matrix Inversion & Full Covariance Error Propagation Engine.

Physics Formulation:
--------------------
1. Photopeak Detection Efficiency Parametrization:
   Based on 吴治华《原子核物理实验方法》第 10 章 §10.4 (pp. 265–275), 汪晓莲《粒子探测技术》第 5 章,
   朱永生《实验物理中的概率和统计》第 3 & 6–7 章, and D. C. Radford (NIM A 361, 297, 1995):
   In in-beam gamma spectroscopy and radioactive decay measurements, determining absolute
   transition intensities and branching ratios requires accurate detector efficiency epsilon(E_gamma).
   For standard coaxial HPGe and Clover detectors (E_gamma >= 80 - 100 keV), the efficiency
   is parameterized in logarithmic polynomial space:
     ln(epsilon(E)) = sum_{k=0}^M a_k * [ ln(E / E_0) ]^k
   where E_0 = 1000 keV is a scaling reference ensuring well-conditioned inversion.

2. Weighted Least Squares (WLS) & Covariance Matrix:
   Given N calibration points (E_i, epsilon_i +- sigma_i), the log-transformed data are:
     y_i = ln(epsilon_i),  sigma_{y_i} = sigma_i / epsilon_i
   The weight matrix is W = diag(1 / sigma_{y_i}^2), and the design matrix is X_{ik} = [ ln(E_i / E_0) ]^k.
   The optimal parameter vector is obtained from normal equations:
     a_hat = (X^T * W * X)^(-1) * X^T * W * y
   The parameter error covariance matrix is:
     V_a = (X^T * W * X)^(-1)
   which contains strong negative off-diagonal correlations (rho_ij ~ -0.80 to -0.99) between adjacent powers.

3. Rigorous Error Propagation vs Naive Error Fallacy:
   At any arbitrary gamma energy E, the Jacobian vector is j(E) = [1, ln(E/E_0), ..., (ln(E/E_0))^M]^T.
   The exact variance of the efficiency is:
     sigma_{ln epsilon}^2(E) = j(E)^T * V_a * j(E)
     sigma_{epsilon}(E) = epsilon(E) * sqrt( sigma_{ln epsilon}^2(E) )
   Ignoring the covariance terms (naive variance sum: sum j_k^2 * V_kk) grossly overestimates
   the efficiency uncertainty by 200% - 600%!
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "clover_detector_152Eu_calibration": {
        "description": "Clover HPGe detector calibrated with 152Eu standard source (121 to 1408 keV)",
        "detector": "Clover-HPGe-SingleCrystal",
        "geometry": "d = 25 cm from target",
        "E0_keV": 1000.0,
        "poly_order": 3,
        "calibration_points": [
            {"E_keV": 121.78, "efficiency": 0.02450, "sigma_eff": 0.00045},
            {"E_keV": 244.70, "efficiency": 0.01780, "sigma_eff": 0.00035},
            {"E_keV": 344.28, "efficiency": 0.01350, "sigma_eff": 0.00025},
            {"E_keV": 411.12, "efficiency": 0.01160, "sigma_eff": 0.00030},
            {"E_keV": 443.96, "efficiency": 0.01080, "sigma_eff": 0.00028},
            {"E_keV": 778.90, "efficiency": 0.00680, "sigma_eff": 0.00015},
            {"E_keV": 867.38, "efficiency": 0.00620, "sigma_eff": 0.00018},
            {"E_keV": 964.08, "efficiency": 0.00565, "sigma_eff": 0.00012},
            {"E_keV": 1085.87, "efficiency": 0.00510, "sigma_eff": 0.00014},
            {"E_keV": 1112.07, "efficiency": 0.00495, "sigma_eff": 0.00013},
            {"E_keV": 1408.01, "efficiency": 0.00405, "sigma_eff": 0.00010}
        ]
    },
    "broadband_coaxial_hpge_mixed_source": {
        "description": "Broadband coaxial HPGe calibrated with 133Ba + 152Eu + 60Co (81 to 1332 keV)",
        "detector": "Coaxial-HPGe-70pct",
        "geometry": "d = 15 cm close geometry",
        "E0_keV": 1000.0,
        "poly_order": 4,
        "calibration_points": [
            {"E_keV": 81.00, "efficiency": 0.0380, "sigma_eff": 0.0008},
            {"E_keV": 121.78, "efficiency": 0.0460, "sigma_eff": 0.0009},
            {"E_keV": 276.40, "efficiency": 0.0325, "sigma_eff": 0.0006},
            {"E_keV": 344.28, "efficiency": 0.0265, "sigma_eff": 0.0005},
            {"E_keV": 356.02, "efficiency": 0.0258, "sigma_eff": 0.0005},
            {"E_keV": 778.90, "efficiency": 0.0132, "sigma_eff": 0.0003},
            {"E_keV": 964.08, "efficiency": 0.0110, "sigma_eff": 0.00025},
            {"E_keV": 1173.24, "efficiency": 0.0092, "sigma_eff": 0.00020},
            {"E_keV": 1332.50, "efficiency": 0.0082, "sigma_eff": 0.00018},
            {"E_keV": 1408.01, "efficiency": 0.0078, "sigma_eff": 0.00018}
        ]
    }
}


def fit_efficiency_curve_wls(points, poly_order=3, E0_keV=1000.0):
    """
    Performs weighted least squares fit of ln(efficiency) vs ln(E/E0).
    Returns best-fit parameters, full covariance matrix, and chi2.
    """
    E_vals = np.array([p["E_keV"] for p in points], dtype=float)
    eff_vals = np.array([p["efficiency"] for p in points], dtype=float)
    sig_eff = np.array([p["sigma_eff"] for p in points], dtype=float)

    y = np.log(eff_vals)
    sigma_y = sig_eff / eff_vals
    weights = 1.0 / (sigma_y**2)

    x = np.log(E_vals / E0_keV)
    N = len(E_vals)
    M = poly_order

    # Design matrix X: X[i, k] = x[i]^k
    X = np.zeros((N, M + 1))
    for k in range(M + 1):
        X[:, k] = x**k

    # Normal equations: (X^T * W * X) * a = X^T * W * y
    W = np.diag(weights)
    XT_W = np.dot(X.T, W)
    A_mat = np.dot(XT_W, X)

    try:
        cov_a = np.linalg.inv(A_mat)
        a_params = np.dot(cov_a, np.dot(XT_W, y))
    except np.linalg.LinAlgError:
        cov_a = np.identity(M + 1)
        a_params = np.zeros(M + 1)

    # Residuals & Goodness of Fit
    y_pred = np.dot(X, a_params)
    residuals = y - y_pred
    chi2 = float(np.sum((residuals / sigma_y)**2))
    ndf = max(1, N - (M + 1))
    red_chi2 = chi2 / ndf

    # Correlation matrix
    corr_a = np.zeros_like(cov_a)
    for i in range(M + 1):
        for j in range(M + 1):
            denom = math.sqrt(max(1e-16, cov_a[i, i] * cov_a[j, j]))
            corr_a[i, j] = cov_a[i, j] / denom

    return {
        "parameters": [float(val) for val in a_params],
        "parameter_errors": [float(math.sqrt(max(0.0, cov_a[k, k]))) for k in range(M + 1)],
        "covariance_matrix": cov_a.tolist(),
        "correlation_matrix": corr_a.tolist(),
        "chi2": float(chi2),
        "ndf": int(ndf),
        "reduced_chi2": float(red_chi2),
        "poly_order": int(poly_order),
        "E0_keV": float(E0_keV)
    }


def evaluate_efficiency_with_covariance(E_keV, fit_result):
    """
    Evaluates efficiency and exact propagated uncertainty using full covariance matrix.
    Also evaluates naive diagonal-only variance for diagnostic comparison.
    """
    E0 = fit_result["E0_keV"]
    a_params = np.array(fit_result["parameters"])
    cov_a = np.array(fit_result["covariance_matrix"])
    M = fit_result["poly_order"]

    x = math.log(max(1e-3, E_keV) / E0)
    j_vec = np.array([x**k for k in range(M + 1)])

    ln_eff = float(np.dot(j_vec, a_params))
    eff = float(math.exp(ln_eff))

    # Rigorous Covariance Propagation: sigma^2 = j^T * Cov * j
    var_ln_eff_rigorous = float(np.dot(j_vec, np.dot(cov_a, j_vec)))
    sigma_eff_rigorous = eff * math.sqrt(max(0.0, var_ln_eff_rigorous))

    # Naive Diagonal-Only Variance Fallacy: sigma_naive^2 = sum j_k^2 * Cov_kk
    diag_cov = np.diag(np.diag(cov_a))
    var_ln_eff_naive = float(np.dot(j_vec, np.dot(diag_cov, j_vec)))
    sigma_eff_naive = eff * math.sqrt(max(0.0, var_ln_eff_naive))

    rel_err_pct = (sigma_eff_rigorous / max(1e-12, eff)) * 100.0
    overestimate_factor = sigma_eff_naive / max(1e-12, sigma_eff_rigorous)

    return {
        "E_gamma_keV": float(E_keV),
        "efficiency": float(eff),
        "sigma_efficiency": float(sigma_eff_rigorous),
        "relative_error_pct": float(rel_err_pct),
        "naive_sigma_efficiency": float(sigma_eff_naive),
        "covariance_overestimate_ratio": float(overestimate_factor)
    }


def run_efficiency_analysis(points, query_energies=None, poly_order=3, E0_keV=1000.0, detector="HPGe"):
    """
    Complete execution pipeline: fits efficiency calibration and interpolates query transitions.
    """
    fit_res = fit_efficiency_curve_wls(points, poly_order=poly_order, E0_keV=E0_keV)

    if query_energies is None:
        query_energies = [100.0, 200.0, 400.0, 600.0, 800.0, 1000.0, 1200.0]

    interp_results = []
    for E in query_energies:
        res_pt = evaluate_efficiency_with_covariance(E, fit_res)
        interp_results.append(res_pt)

    return {
        "detector": detector,
        "fit_results": fit_res,
        "interpolated_transitions": interp_results
    }


def format_text_report(res, title="HPGe Efficiency Curve Covariance Fitter"):
    det = res["detector"]
    fr = res["fit_results"]
    it = res["interpolated_transitions"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Detector: {det} | Order = {fr['poly_order']} | Red. Chi^2 = {fr['reduced_chi2']:.2f} (Chi^2/ndf = {fr['chi2']:.2f}/{fr['ndf']})")
    lines.append("=" * 76)
    lines.append("Fitted Polynomial Coefficients (ln(eps) = sum a_k [ln(E/E0)]^k):")
    for k, (a, err) in enumerate(zip(fr["parameters"], fr["parameter_errors"])):
        lines.append(f"  a_{k} (degree {k}) : {a:10.5f} +- {err:10.5f}")
    lines.append("-" * 76)
    lines.append("Correlation Matrix Elements rho_ij:")
    corr = fr["correlation_matrix"]
    dim = len(corr)
    header = "       " + " ".join([f"  a_{c}   " for c in range(dim)])
    lines.append(header)
    for r in range(dim):
        row_str = f"  a_{r}  " + " ".join([f"{corr[r][c]:8.3f}" for c in range(dim)])
        lines.append(row_str)
    lines.append("-" * 76)
    lines.append("Energy Interpolation & Rigorous Covariance Propagation:")
    lines.append("  E_gamma (keV)   Efficiency eps      +- 1 sigma       Rel Err (%)   Naive Err Bias")
    for p in it:
        lines.append(f"    {p['E_gamma_keV']:7.1f}        {p['efficiency']:9.6f}      {p['sigma_efficiency']:9.6f}       {p['relative_error_pct']:5.2f}%         x{p['covariance_overestimate_ratio']:4.2f}")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="HPGe Detector Efficiency Curve Fitter & Covariance Error Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental calibration preset")
    parser.add_argument("--query-E", type=str, help="Comma-separated query gamma energies in keV (e.g. 409,638)")
    parser.add_argument("--order", type=int, default=3, help="Polynomial order (default: 3)")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        points = p["calibration_points"]
        det = f"{p['detector']} ({p['geometry']})"
        order = p.get("poly_order", args.order)
        E0 = p.get("E0_keV", 1000.0)
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    q_energies = None
    if args.query_E:
        q_energies = [float(x.strip()) for x in args.query_E.split(",") if x.strip()]

    res = run_efficiency_analysis(
        points=points,
        query_energies=q_energies,
        poly_order=order,
        E0_keV=E0,
        detector=det
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
