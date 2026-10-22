#!/usr/bin/env python3
"""Quantitative audit of MSCD fast timing: background response and PRD calibration.

Models the analytical background correction procedure from Régis 2011 PhD thesis
(Appendix A, pp. 96-98), branch asymmetry sensitivity, and Fit 1 PRD curve parameters (p. 44).
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def calculate_mscd_background_correction(delta_c_total_ps, delta_c_compton_ps, alpha_bkg):
    """
    Régis 2011 Appendix A Eq. (A.1)-(A.2):
    Delta_CT = (Delta_CD + alpha * Delta_CC) / (1 + alpha)
    tc = Delta_CT - Delta_CD = -alpha * (Delta_CT - Delta_CC) = -alpha * ts
    Delta_CD = Delta_CT + alpha * ts
    """
    ts = delta_c_total_ps - delta_c_compton_ps
    tc = -alpha_bkg * ts
    delta_c_delayed = delta_c_total_ps + alpha_bkg * ts
    tau_shift = (delta_c_delayed - delta_c_total_ps) / 2.0
    return {
        "ts_ps": ts,
        "tc_ps": tc,
        "delta_c_delayed_ps": delta_c_delayed,
        "tau_shift_ps": tau_shift,
    }


def calculate_asymmetric_branch_centroids(c_d1, c_d2, c_c1, c_c2, alpha1, alpha2):
    """Calculate measured total centroids and compare symmetric vs independent reconstruction."""
    c_t1 = (c_d1 + alpha1 * c_c1) / (1.0 + alpha1)
    c_t2 = (c_d2 + alpha2 * c_c2) / (1.0 + alpha2)
    delta_c_total = c_t2 - c_t1
    delta_c_compton = c_c2 - c_c1
    true_delta_c_delayed = c_d2 - c_d1

    alpha_mean = (alpha1 + alpha2) / 2.0
    ts = delta_c_total - delta_c_compton
    delta_c_recon_mean = delta_c_total + alpha_mean * ts

    c_d1_indep = (1.0 + alpha1) * c_t1 - alpha1 * c_c1
    c_d2_indep = (1.0 + alpha2) * c_t2 - alpha2 * c_c2
    delta_c_recon_indep = c_d2_indep - c_d1_indep

    error_mean = delta_c_recon_mean - true_delta_c_delayed
    error_indep = delta_c_recon_indep - true_delta_c_delayed

    return {
        "true_delta_c_ps": true_delta_c_delayed,
        "delta_c_total_measured_ps": delta_c_total,
        "delta_c_compton_ps": delta_c_compton,
        "alpha1": alpha1,
        "alpha2": alpha2,
        "alpha_mean": alpha_mean,
        "recon_with_mean_alpha_ps": delta_c_recon_mean,
        "error_mean_ps": error_mean,
        "tau_error_mean_ps": error_mean / 2.0,
        "recon_independent_ps": delta_c_recon_indep,
        "error_indep_ps": error_indep,
    }


def prd_fit1(e_gamma, a=-826391.0, b=3316.85, c=-1.28444, d=14104.7):
    """Régis 2011 p. 44 Fit 1 calibration parameters."""
    return a / math.sqrt(b + e_gamma) + c * e_gamma + d


def prd_relative(e_gamma, e_ref):
    """Relative PRD shifted to cross zero at E_ref."""
    return prd_fit1(e_gamma) - prd_fit1(e_ref)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # 1. Benchmark reproduction: 214Po 768 -> 609 keV transition (Régis 2011 p. 98)
    bkg_bench = calculate_mscd_background_correction(
        delta_c_total_ps=150.0,
        delta_c_compton_ps=189.0,
        alpha_bkg=0.3
    )

    check("214Po benchmark ts is -39 ps", math.isclose(bkg_bench["ts_ps"], -39.0, abs_tol=1e-12))
    check("214Po benchmark tc is +11.7 ps", math.isclose(bkg_bench["tc_ps"], 11.7, abs_tol=1e-12))
    check("214Po Delta_CD correction is -11.7 ps",
          math.isclose(bkg_bench["delta_c_delayed_ps"] - 150.0, -11.7, abs_tol=1e-12))
    check("214Po lifetime shift is -5.85 ps", math.isclose(bkg_bench["tau_shift_ps"], -5.85, abs_tol=1e-12))

    # 2. Peak-to-background ratio sensitivity (P/B > 10 rule, Régis p. 98)
    bkg_clean = calculate_mscd_background_correction(150.0, 165.0, alpha_bkg=0.08)
    check("For alpha=0.08 and small ts, tau shift is under 1 ps", abs(bkg_clean["tau_shift_ps"]) < 1.0)

    # 3. Branch asymmetry audit
    c_d1, c_d2 = 995.0, 1055.0
    c_c1, c_c2 = 980.0, 1080.0

    asym_sym = calculate_asymmetric_branch_centroids(c_d1, c_d2, c_c1, c_c2, 0.30, 0.30)
    check("Symmetric branch background reconstruction is exact (error < 1e-12 ps)",
          abs(asym_sym["error_mean_ps"]) < 1e-12)

    asym_mild = calculate_asymmetric_branch_centroids(c_d1, c_d2, c_c1, c_c2, 0.25, 0.35)
    check("Mild asymmetry (0.25, 0.35) produces non-zero error with mean alpha",
          abs(asym_mild["error_mean_ps"]) > 0.1)
    check("Independent subtraction eliminates mild asymmetry error completely",
          abs(asym_mild["error_indep_ps"]) < 1e-12)

    asym_strong = calculate_asymmetric_branch_centroids(c_d1, c_d2, c_c1, c_c2, 0.10, 0.50)
    check("Strong asymmetry (0.10, 0.50) produces > 0.5 ps centroid difference error",
          abs(asym_strong["error_mean_ps"]) > 0.5)
    check("Strong asymmetry lifetime error exceeds 0.25 ps",
          abs(asym_strong["tau_error_mean_ps"]) > 0.25)
    check("Independent subtraction eliminates strong asymmetry error completely",
          abs(asym_strong["error_indep_ps"]) < 1e-12)

    # 4. Régis Fit 1 PRD curve reproduction (p. 44, p. 48)
    e_ref = 609.0
    prd_at_ref = prd_relative(e_ref, e_ref)
    check("PRD at Delta E = 0 is strictly zero", math.isclose(prd_at_ref, 0.0, abs_tol=1e-12))

    prd_344_minus_609 = prd_relative(344.0, 609.0)
    check("PRD(344 - 609) matches -129(8) ps (p. 48)", math.isclose(prd_344_minus_609, -128.65, abs_tol=0.5))

    prd_1120_minus_609 = prd_relative(1120.0, 609.0)
    check("PRD(1120 - 609) matches +126(8) ps (p. 48 Eq. 4.15)", math.isclose(prd_1120_minus_609, 126.39, abs_tol=0.5))

    # 5. 214Po 2+ state lifetime extraction (p. 48 Eq. 4.16-4.17)
    delta_c_meas = 124.0  # ps
    tau_214po = (delta_c_meas - prd_1120_minus_609) / 2.0
    check("214Po 2+ lifetime extraction gives ~ -1.2 ps, confirming <= 4 ps limit", tau_214po < 0.0 and abs(tau_214po) < 2.0)

    # 6. Propagation of PRD calibration uncertainty (2-sigma = 8 ps)
    prd_unc = 8.0
    tau_unc = prd_unc / 2.0
    check("Factor of 2 in MSCD reduces PRD uncertainty on tau to 4 ps", math.isclose(tau_unc, 4.0, abs_tol=1e-12))

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Régis 2011 PhD thesis: Fit 1 PRD calibration (p. 44), 214Po benchmark (p. 48), and Appendix A background correction",
        "regis_fit1_parameters": {
            "a_ps_sqrt_keV": -826391.0,
            "b_keV": 3316.85,
            "c_ps_per_keV": -1.28444,
            "d_ps": 14104.7,
            "source": "Régis 2011 PhD thesis, Chapter 4, p. 44, Eq. (4.13)",
        },
        "benchmark_214po_609_reference": {
            "PRD_344_minus_609_ps": prd_344_minus_609,
            "PRD_1120_minus_609_ps": prd_1120_minus_609,
            "measured_Delta_C_ps": delta_c_meas,
            "extracted_tau_ps": tau_214po,
            "adopted_limit_ps": "<= 4 ps",
            "source": "Régis 2011 PhD thesis, Chapter 4, p. 48, Eqs. (4.15)-(4.17)",
        },
        "background_correction_benchmark_768_609": {
            "ts_ps": bkg_bench["ts_ps"],
            "tc_ps": bkg_bench["tc_ps"],
            "alpha_bkg": 0.3,
            "delta_c_delayed_correction_ps": bkg_bench["delta_c_delayed_ps"] - 150.0,
            "tau_shift_ps": bkg_bench["tau_shift_ps"],
            "source": "Régis 2011 PhD thesis, Appendix A, p. 98, Eq. (A.2)",
        },
        "branch_asymmetry_analysis": {
            "case_symmetric_030_030": asym_sym,
            "case_mild_asymmetry_025_035": asym_mild,
            "case_strong_asymmetry_010_050": asym_strong,
            "insight": "Equal branch background enables linear correction; asymmetric background requires independent branch-by-branch subtraction",
        },
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"MSCD audit completed: {len(checks)} checks passed.")
    print(f"PRD(1120 - 609): {prd_1120_minus_609:.2f} ps (Régis reports 126(8) ps)")
    print(f"214Po extracted tau: {tau_214po:.2f} ps (confirming tau <= 4 ps)")
    print(f"214Po 768-609 background correction: tc = +{bkg_bench['tc_ps']:.1f} ps, tau shift = {bkg_bench['tau_shift_ps']:.2f} ps")


if __name__ == "__main__":
    main()
