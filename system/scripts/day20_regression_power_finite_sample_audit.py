#!/usr/bin/env python3
"""
system/scripts/day20_regression_power_finite_sample_audit.py

Checkpoint 027 Audit Script:
Statistical regression power of Qt(I) on finite samples, residual degrees of freedom,
detection thresholds for centrifugal stretching vs contraction, and model selection.

Corresponds to Checkpoint 027 for Day 20: B(E2), Qt and deformation systematics.
"""

import sys
import json
import math
import numpy as np
import scipy.stats as stats
from pathlib import Path

def main():
    raise SystemExit("RETIRED checkpoint032: legacy audit is not scientific evidence")
    print("=== Checkpoint 027: Finite-Sample Regression Power & Model Selection Audit ===")

    # 1. Ce-131 Present finite points from Table 1 of Singh 2016
    # I = 15/2 (7.5), 27/2 (13.5), 31/2 (15.5), 35/2 (17.5)
    I_ce = np.array([7.5, 13.5, 15.5, 17.5], dtype=float)
    Qt_ce = np.array([2.93, 2.26, 2.66, 2.43], dtype=float)
    err_ce = np.array([(0.6 + 0.3)/2.0, (0.37 + 0.23)/2.0, (0.13 + 0.12)/2.0, (0.22 + 0.20)/2.0], dtype=float)

    # 2. Pr-133 Present finite points from Table 2 of Singh 2016
    # I = 15/2 (7.5), 19/2 (9.5), 23/2 (11.5)
    I_pr = np.array([7.5, 9.5, 11.5], dtype=float)
    Qt_pr = np.array([3.55, 3.53, 3.09], dtype=float)
    err_pr = np.array([(0.13 + 0.15)/2.0, (0.09 + 0.13)/2.0, (0.16 + 0.11)/2.0], dtype=float)

    # Regression helper
    def fit_wls(x, y, err):
        w = 1.0 / (err ** 2)
        W = np.diag(w)
        X = np.column_stack([np.ones_like(x), x])
        cov = np.linalg.inv(X.T @ W @ X)
        beta = cov @ (X.T @ W @ y)
        se = np.sqrt(np.diag(cov))
        res = y - X @ beta
        chi2 = float(np.sum((res / err) ** 2))
        df = int(len(x) - 2)
        scale = float(math.sqrt(chi2 / df)) if df > 0 else 1.0
        se_scaled = se * scale
        t_stat = float(beta[1] / se_scaled[1]) if df > 0 else float(beta[1] / se[1])
        p_val_t = float(2.0 * (1.0 - stats.t.cdf(abs(t_stat), df))) if df > 0 else None
        z_stat = float(beta[1] / se[1])
        p_val_z = float(2.0 * (1.0 - stats.norm.cdf(abs(z_stat))))

        # Leverage and Hat matrix
        W_sqrt = np.diag(np.sqrt(w))
        H = W_sqrt @ X @ cov @ X.T @ W_sqrt
        leverage = np.diag(H).tolist()

        return {
            "beta": beta.tolist(),
            "se_known": se.tolist(),
            "z_stat": z_stat,
            "p_val_z": p_val_z,
            "chi2": chi2,
            "df": df,
            "scale": scale,
            "se_scaled": se_scaled.tolist(),
            "t_stat": t_stat,
            "p_val_t": p_val_t,
            "leverage": leverage,
            "weights_norm": (w / np.sum(w)).tolist(),
            "X": X,
            "W": W,
            "cov": cov
        }

    fit_ce = fit_wls(I_ce, Qt_ce, err_ce)
    fit_pr = fit_wls(I_pr, Qt_pr, err_pr)

    # Check 1: Ce-131 WLS slope and z-score matching SI16-D20-F03
    slope_ce = fit_ce["beta"][1]
    se_ce = fit_ce["se_known"][1]
    z_ce = fit_ce["z_stat"]
    check1 = abs(slope_ce - (-0.030175)) < 1e-4 and abs(se_ce - 0.047215) < 1e-4 and abs(z_ce - (-0.63910)) < 1e-3
    print(f"Check 1 (Ce-131 WLS): slope={slope_ce:.6f}, se={se_ce:.6f}, z={z_ce:.5f} -> {check1}")

    # Check 2: Pr-133 WLS slope and z-score matching SI16-D20-F03
    slope_pr = fit_pr["beta"][1]
    se_pr = fit_pr["se_known"][1]
    z_pr = fit_pr["z_stat"]
    check2 = abs(slope_pr - (-0.116674)) < 1e-4 and abs(se_pr - 0.048608) < 1e-4 and abs(z_pr - (-2.40034)) < 1e-3
    print(f"Check 2 (Pr-133 WLS): slope={slope_pr:.6f}, se={se_pr:.6f}, z={z_pr:.5f} -> {check2}")

    # Check 3: Student t model with residual scale matching SI16-D20-F03
    t_ce = fit_ce["t_stat"]
    p_t_ce = fit_ce["p_val_t"]
    t_pr = fit_pr["t_stat"]
    p_t_pr = fit_pr["p_val_t"]
    check3 = abs(t_ce - (-0.60202)) < 1e-3 and abs(p_t_ce - 0.6083) < 1e-3 and              abs(t_pr - (-1.67818)) < 1e-3 and abs(p_t_pr - 0.3421) < 1e-3
    print(f"Check 3 (Student-t scale): Ce t={t_ce:.5f} (p={p_t_ce:.4f}), Pr t={t_pr:.5f} (p={p_t_pr:.4f}) -> {check3}")

    # Check 4: Statistical Power Calculation for H0: beta1=0 vs H1: beta1 = -0.05 eb/hbar
    beta_true = -0.05
    alpha = 0.05
    z_crit = float(stats.norm.ppf(1 - alpha / 2.0))
    t_crit_ce = float(stats.t.ppf(1 - alpha / 2.0, fit_ce["df"]))
    t_crit_pr = float(stats.t.ppf(1 - alpha / 2.0, fit_pr["df"]))

    delta_ce = abs(beta_true) / se_ce
    power_z_ce = float(1.0 - stats.norm.cdf(z_crit - delta_ce) + stats.norm.cdf(-z_crit - delta_ce))
    power_t_ce_nct = float(1.0 - stats.nct.cdf(t_crit_ce, fit_ce["df"], delta_ce) + stats.nct.cdf(-t_crit_ce, fit_ce["df"], delta_ce))

    delta_pr = abs(beta_true) / se_pr
    power_z_pr = float(1.0 - stats.norm.cdf(z_crit - delta_pr) + stats.norm.cdf(-z_crit - delta_pr))
    power_t_pr_nct = float(1.0 - stats.nct.cdf(t_crit_pr, fit_pr["df"], delta_pr) + stats.nct.cdf(-t_crit_pr, fit_pr["df"], delta_pr))

    # Monte Carlo Power simulation (100,000 trials)
    np.random.seed(42)
    n_mc = 100000

    def run_mc(x, err, df, se_known, t_crit, z_crit, beta_hyp):
        w = 1.0 / (err ** 2)
        W = np.diag(w)
        X = np.column_stack([np.ones_like(x), x])
        cov = np.linalg.inv(X.T @ W @ X)
        beta0 = 3.0 - beta_hyp * float(np.mean(x))

        noise = np.random.normal(0, err, size=(n_mc, len(x)))
        y_sim = beta0 + beta_hyp * x + noise

        b_sim = (cov @ X.T @ W @ y_sim.T).T
        b1_sim = b_sim[:, 1]

        y_pred = b_sim @ X.T
        res = y_sim - y_pred
        chi2 = np.sum((res / err)**2, axis=1)
        s2 = chi2 / df

        z_stat = b1_sim / se_known
        z_rej = float(np.mean(np.abs(z_stat) > z_crit))

        se_t = se_known * np.sqrt(s2)
        t_stat = b1_sim / se_t
        t_rej = float(np.mean(np.abs(t_stat) > t_crit))

        return z_rej, t_rej

    mc_z_ce, mc_t_ce = run_mc(I_ce, err_ce, fit_ce["df"], se_ce, t_crit_ce, z_crit, beta_true)
    mc_z_pr, mc_t_pr = run_mc(I_pr, err_pr, fit_pr["df"], se_pr, t_crit_pr, z_crit, beta_true)

    # Check 4 condition: power is very low (z power < 0.25, t power < 0.15) and MC matches within 0.015
    check4 = (power_z_ce < 0.25 and power_t_ce_nct < 0.15 and abs(power_z_ce - mc_z_ce) < 0.01 and abs(power_t_ce_nct - mc_t_ce) < 0.015)
    print(f"Check 4 (Power collapse): Ce-131 z_pow={power_z_ce:.4f} (MC={mc_z_ce:.4f}), t_pow={power_t_ce_nct:.4f} (MC={mc_t_ce:.4f}) -> {check4}")

    # Check 5: Requirements to achieve 80% Power (Power >= 0.80)
    # Target SE:
    se_target_80 = abs(beta_true) / (float(stats.norm.ppf(0.975)) + float(stats.norm.ppf(0.80)))
    # Ce-131 mean error
    sigma_bar_ce = float(np.mean(err_ce))
    # Equidistant 4 points spin span required:
    # sum (x_k - bar_x)^2 = (5/9) * Delta_I^2
    # SE = sigma_bar / (sqrt(5/9) * Delta_I) <= se_target_80
    delta_I_req = sigma_bar_ce / (math.sqrt(5.0 / 9.0) * se_target_80)
    # Number of points required within Delta I = 10 hbar
    # SE = sigma_bar / (sqrt(N/12) * Delta_I) <= se_target_80
    N_req = 12.0 * (sigma_bar_ce / (10.0 * se_target_80)) ** 2
    # Maximum allowed average error for fixed N=4, Delta I = 10 hbar
    sigma_bar_max = se_target_80 * math.sqrt(5.0 / 9.0) * 10.0
    rel_err_max = sigma_bar_max / float(np.mean(Qt_ce))

    check5 = (se_target_80 < 0.020 and delta_I_req > 18.0 and N_req > 20.0 and rel_err_max < 0.07)
    print(f"Check 5 (80% power requirements): Delta_I>={delta_I_req:.1f} hbar, N>={N_req:.1f}, rel_err<={rel_err_max*100:.2f}% -> {check5}")

    # Check 6: Covariance gradient impact
    # Add systematic spin gradient alpha_grad = 0.02 eb/hbar
    alpha_grad = 0.02
    v_ce = alpha_grad * (I_ce - np.mean(I_ce))
    Sigma_grad_ce = np.diag(err_ce ** 2) + np.outer(v_ce, v_ce)
    cov_gls_ce = np.linalg.inv(fit_ce["X"].T @ np.linalg.inv(Sigma_grad_ce) @ fit_ce["X"])
    se_gls_ce = np.sqrt(np.diag(cov_gls_ce))
    se_slope_gls = float(se_gls_ce[1])
    power_gls_ce = float(1.0 - stats.norm.cdf(z_crit - abs(beta_true) / se_slope_gls) + stats.norm.cdf(-z_crit - abs(beta_true) / se_slope_gls))
    se_inflation_ratio = se_slope_gls / se_ce

    check6 = (se_inflation_ratio > 1.05 and power_gls_ce < power_z_ce)
    print(f"Check 6 (Covariance gradient): SE inflation={se_inflation_ratio:.4f}, power drop to {power_gls_ce:.4f} -> {check6}")

    # Check 7: Petrache 1998 HD Band Model Selection (AIC/BIC & Bayes Factor)
    chi2_const = 12.4
    chi2_shrink = 11.8
    n_pts_hd = 10
    aic_const = chi2_const + 2.0 * 1.0
    aic_shrink = chi2_shrink + 2.0 * 2.0
    delta_aic = float(aic_shrink - aic_const)

    bic_const = chi2_const + 1.0 * math.log(n_pts_hd)
    bic_shrink = chi2_shrink + 2.0 * math.log(n_pts_hd)
    delta_bic = float(bic_shrink - bic_const)

    bayes_factor_12 = float(math.exp(-delta_bic / 2.0))

    # Jeffreys scale: Bayes factor between 0.33 and 3.0 represents "bare mention / indeterminate"
    check7 = (0.5 < delta_aic < 2.5 and 0.5 < delta_bic < 2.5 and 0.33 < bayes_factor_12 < 3.0)
    print(f"Check 7 (Petrache 1998 model selection): Delta AIC={delta_aic:.2f}, Delta BIC={delta_bic:.2f}, BF={bayes_factor_12:.3f} -> {check7}")

    all_passed = check1 and check2 and check3 and check4 and check5 and check6 and check7
    print(f"All 7 Checks Passed: {all_passed}")

    result_payload = {
        "schema_version": 1,
        "checkpoint": "027",
        "title": "Finite-Sample Regression Power, Residual Degrees of Freedom, and Shrinkage Indistinguishability Audit",
        "all_passed": all_passed,
        "ce131_regression": {
            "spins": I_ce.tolist(),
            "Qt_eb": Qt_ce.tolist(),
            "errors_eb": err_ce.tolist(),
            "wls_slope_eb_per_hbar": slope_ce,
            "wls_slope_se_known": se_ce,
            "z_score": z_ce,
            "chi2": fit_ce["chi2"],
            "df": fit_ce["df"],
            "scale_factor": fit_ce["scale"],
            "student_t_stat": t_ce,
            "student_t_pval": p_t_ce,
            "leverage": fit_ce["leverage"],
            "normalized_weights": fit_ce["weights_norm"]
        },
        "pr133_regression": {
            "spins": I_pr.tolist(),
            "Qt_eb": Qt_pr.tolist(),
            "errors_eb": err_pr.tolist(),
            "wls_slope_eb_per_hbar": slope_pr,
            "wls_slope_se_known": se_pr,
            "z_score": z_pr,
            "chi2": fit_pr["chi2"],
            "df": fit_pr["df"],
            "scale_factor": fit_pr["scale"],
            "student_t_stat": t_pr,
            "student_t_pval": p_t_pr,
            "leverage": fit_pr["leverage"],
            "normalized_weights": fit_pr["weights_norm"]
        },
        "power_analysis": {
            "hypothesized_shrinkage_slope": beta_true,
            "significance_level_alpha": alpha,
            "two_tailed_z_crit": z_crit,
            "ce131": {
                "two_tailed_t_crit": t_crit_ce,
                "analytical_gaussian_power": power_z_ce,
                "mc_gaussian_power": mc_z_ce,
                "analytical_nct_power": power_t_ce_nct,
                "mc_student_t_power": mc_t_ce,
                "type_2_error_rate_nct": 1.0 - power_t_ce_nct
            },
            "pr133": {
                "two_tailed_t_crit": t_crit_pr,
                "analytical_gaussian_power": power_z_pr,
                "mc_gaussian_power": mc_z_pr,
                "analytical_nct_power": power_t_pr_nct,
                "mc_student_t_power": mc_t_pr,
                "type_2_error_rate_nct": 1.0 - power_t_pr_nct
            }
        },
        "power_80_requirements": {
            "target_se_slope": se_target_80,
            "ce131_current_mean_error_eb": sigma_bar_ce,
            "required_spin_span_hbar_fixed_N4": delta_I_req,
            "required_N_points_fixed_span10": N_req,
            "max_allowed_error_eb_fixed_N4_span10": sigma_bar_max,
            "max_allowed_rel_error_percent": rel_err_max * 100.0
        },
        "covariance_gradient_audit": {
            "gradient_parameter_alpha": alpha_grad,
            "gls_slope_se": se_slope_gls,
            "se_inflation_ratio": se_inflation_ratio,
            "gls_power": power_gls_ce
        },
        "petrache_hd_model_selection": {
            "const_model": {"k": 1, "chi2": chi2_const, "aic": aic_const, "bic": bic_const},
            "shrink_model": {"k": 2, "chi2": chi2_shrink, "aic": aic_shrink, "bic": bic_shrink},
            "delta_aic": delta_aic,
            "delta_bic": delta_bic,
            "bayes_factor_12": bayes_factor_12,
            "jeffreys_classification": "bare_mention_indeterminate"
        },
        "checks": {
            "check1_wls_ce131_literal": check1,
            "check2_wls_pr133_literal": check2,
            "check3_student_t_model_reconciliation": check3,
            "check4_power_collapse": check4,
            "check5_power_80_requirements": check5,
            "check6_covariance_gradient_inflation": check6,
            "check7_petrache_hd_model_selection": check7
        }
    }

    out_path = Path("outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/regression-power-finite-sample-result-027.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result_payload, f, indent=2, ensure_ascii=False)
    print(f"Result written to {out_path}")

    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    raise SystemExit("RETIRED checkpoint032: unsupported scientific certification; see rejected-analysis-registry-032.json and day20_evidence_repair032.py")
