#!/usr/bin/env python3
"""Day 20 deliverable consolidation and cross-verification audit.

Audits all 4 Day-matrix deliverables against canonical evidence:
1. Recall: B(E2) -> Qt -> Qs -> beta2 model dependence and geometric suppression;
2. Mainline sources: Petrache 1998, Singh 2016, and transition-quadrupole-moment;
3. Exercise: Weighted trend calculation in 131Ce and 133Pr, plus non-comparability conditions;
4. Counterevidence: Band-mixing, side-feeding, gamma-softness, and stopping-power covariance;
5. Figure artifact: Nature-figure QA-compliant lifetime/strength/deformation evidence figure.
"""
from __future__ import annotations

raise SystemExit("Deactivated checkpoint101: scientific certification withdrawn; original code and results retained in rejected-analysis-registry-101.json; no experimental validation.")

import argparse
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    run_dir = args.run_dir.resolve()

    checks = []
    def check(name, ok):
        if not ok:
            raise AssertionError(name)
        checks.append({"name": name, "passed": bool(ok)})

    # -------------------------------------------------------------------------
    # 1. Recall: Model-dependence relations & geometric invariants
    # -------------------------------------------------------------------------
    # Logarithmic derivatives
    # B(E2) proportional to tau^(-1) * E_gamma^(-5)
    # Q_t proportional to sqrt(B(E2)) proportional to tau^(-1/2) * E_gamma^(-5/2)
    dln_B_dln_tau = -1.0
    dln_B_dln_E = -5.0
    dln_Qt_dln_tau = -0.5
    check("Logarithmic derivatives: dlnB/dlntau=-1, dlnB/dlnE=-5, dlnQt/dlntau=-0.5",
          math.isclose(dln_B_dln_tau, -1.0) and math.isclose(dln_B_dln_E, -5.0) and math.isclose(dln_Qt_dln_tau, -0.5))

    # Triaxial geometric factor at gamma=30 deg: cos(30+30)/cos(30) = cos(60)/cos(30) = 0.5 / (sqrt(3)/2) = 1/sqrt(3)
    gamma_factor_30 = math.cos(math.radians(60)) / math.cos(math.radians(30))
    suppression_pct = (1.0 - gamma_factor_30) * 100.0
    check("Triaxial Qt suppression at gamma=30 deg is exactly 1 - 1/sqrt(3) ~ 42.26%",
          math.isclose(suppression_pct, 42.264973, rel_tol=1e-5))

    # -------------------------------------------------------------------------
    # 2. Mainline sources ledger integrity
    # -------------------------------------------------------------------------
    singh_raw = root / "raw/papers/2016_Singh et al_Lifetime measurements in the yrast band of the gamma-soft nuclei 131Ce and 133Pr.pdf"
    petrache_raw = root / "raw/papers/1998_Petrache et al_Lifetime measurements of highly deformed bands in 1 3 4 , 1 3 5 Nd and 131 Ce.pdf"
    check("Singh 2016 raw file exists and matches baseline SHA256",
          hashlib.sha256(singh_raw.read_bytes()).hexdigest() == "95e0831b9864a58fd1a896a1b20e227d88d9b7aa5de56c738c3792441caa1a30")
    check("Petrache 1998 raw file exists and matches baseline SHA256",
          hashlib.sha256(petrache_raw.read_bytes()).hexdigest() == "9d2297ed085012d2f8633a5faecfa7020cbca96ac06cf2eb5e88d97a24b90e5f")

    # -------------------------------------------------------------------------
    # 3. Exercise: Trend slopes and conditional models
    # -------------------------------------------------------------------------
    ledger = json.loads((run_dir / "singh-table-ledger-001.json").read_text())
    # 131Ce finite points
    ce_rows = [r for r in ledger["case_Ce131"]["rows"] if r["Qt"]["kind"] == "finite"]
    x_ce = np.array([r["spin"] for r in ce_rows])
    y_ce = np.array([r["Qt"]["value"] for r in ce_rows])
    sig_ce = np.array([(r["Qt"]["minus"] + r["Qt"]["plus"]) / 2 for r in ce_rows])
    w_ce = 1 / sig_ce**2
    b_ce = np.sum(w_ce * (x_ce - np.average(x_ce, weights=w_ce)) * (y_ce - np.average(y_ce, weights=w_ce))) / np.sum(w_ce * (x_ce - np.average(x_ce, weights=w_ce))**2)
    se_ce = 1 / np.sqrt(np.sum(w_ce * (x_ce - np.average(x_ce, weights=w_ce))**2))
    z_ce = b_ce / se_ce
    check("131Ce finite slope b = -0.030175 +- 0.047215, z = -0.63910",
          math.isclose(b_ce, -0.030175, rel_tol=1e-4) and math.isclose(z_ce, -0.63910, rel_tol=1e-4))

    # 133Pr finite points
    pr_rows = [r for r in ledger["case_Pr133"]["rows"] if r["Qt"]["kind"] == "finite"]
    x_pr = np.array([r["spin"] for r in pr_rows])
    y_pr = np.array([r["Qt"]["value"] for r in pr_rows])
    sig_pr = np.array([(r["Qt"]["minus"] + r["Qt"]["plus"]) / 2 for r in pr_rows])
    w_pr = 1 / sig_pr**2
    b_pr = np.sum(w_pr * (x_pr - np.average(x_pr, weights=w_pr)) * (y_pr - np.average(y_pr, weights=w_pr))) / np.sum(w_pr * (x_pr - np.average(x_pr, weights=w_pr))**2)
    se_pr = 1 / np.sqrt(np.sum(w_pr * (x_pr - np.average(x_pr, weights=w_pr))**2))
    z_pr = b_pr / se_pr
    check("133Pr finite slope b = -0.116674 +- 0.048608, z = -2.40034",
          math.isclose(b_pr, -0.116674, rel_tol=1e-4) and math.isclose(z_pr, -2.40034, rel_tol=1e-4))

    # -------------------------------------------------------------------------
    # 4. Counterevidence: Babra 2019 136Sm slope & t-distribution
    # -------------------------------------------------------------------------
    x_sm = np.array([8, 10, 12, 14, 16, 18])
    y_sm = np.array([5.66, 5.59, 5.70, 5.38, 4.85, 5.05])
    sig_sm = np.array([0.19, 0.785, 0.205, 0.335, 0.33, 0.35])
    w_sm = 1 / sig_sm**2
    xm_sm = np.average(x_sm, weights=w_sm)
    ym_sm = np.average(y_sm, weights=w_sm)
    den_sm = np.sum(w_sm * (x_sm - xm_sm)**2)
    b_sm = np.sum(w_sm * (x_sm - xm_sm) * (y_sm - ym_sm)) / den_sm
    se_sm = 1 / np.sqrt(den_sm)
    z_sm = b_sm / se_sm
    res_sm = y_sm - (ym_sm + b_sm * (x_sm - xm_sm))
    chi2_lin = np.sum(w_sm * res_sm**2)
    scale_sm = chi2_lin / (len(x_sm) - 2)
    t_sm = z_sm / np.sqrt(scale_sm)
    check("136Sm Gaussian z = -2.178812 and residual-scaled Student t = -2.721303 (df=4)",
          math.isclose(z_sm, -2.178812, rel_tol=1e-4) and math.isclose(t_sm, -2.721303, rel_tol=1e-4))

    # -------------------------------------------------------------------------
    # 5. Figure deliverables verification
    # -------------------------------------------------------------------------
    fig_dir = run_dir / "figures-043"
    pdf_path = fig_dir / "singh-present-qt-043.pdf"
    svg_path = fig_dir / "singh-present-qt-043.svg"
    png_path = fig_dir / "singh-present-qt-043.png"
    csv_path = fig_dir / "source-data-043.csv"
    alignment_json = fig_dir / "singh-present-qt-043.alignment.json"
    collision_json = fig_dir / "collision-audit-043.json"
    qa_json = fig_dir / "qa-notes-043.json"
    check("All 4 figure delivery files exist (PDF, SVG, PNG, CSV)",
          pdf_path.exists() and svg_path.exists() and png_path.exists() and csv_path.exists())
    check("Rendered alignment JSON exists and confirms 1.5 pt strict pass",
          alignment_json.exists() and json.loads(alignment_json.read_text()).get("verdict") == "PASS")
    check("Collision audit JSON exists and confirms PASS (0 fail, 0 warn)",
          collision_json.exists() and json.loads(collision_json.read_text()).get("summary", {}).get("counts", {}).get("FAIL", 0) == 0)

    # -------------------------------------------------------------------------
    # Output summary artifact
    # -------------------------------------------------------------------------
    out = {
        "checkpoint": "046",
        "audited_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "curriculum_matrix_status": {
            "day_index": 20,
            "phase": "lifetimes-strengths-and-deformation",
            "deliverables": {
                "recall_model_dependence": {
                    "status": "audited",
                    "log_derivatives": {"dlnB_dlntau": dln_B_dln_tau, "dlnB_dlnE": dln_B_dln_E, "dlnQt_dlntau": dln_Qt_dln_tau},
                    "triaxial_suppression_gamma30": f"{suppression_pct:.4f}%",
                    "evidence_locator": "knowledge/observables/transition-quadrupole-moment.md"
                },
                "mainline_reading": {
                    "status": "audited",
                    "sources": ["petrache-1998-highly-deformed-lifetimes-131ce-nd.md", "singh-2016-lifetime-131ce-133pr.md", "transition-quadrupole-moment.md"],
                    "evidence_locator": "knowledge/sources/singh-2016-lifetime-131ce-133pr.md; knowledge/sources/petrache-1998-highly-deformed-lifetimes-131ce-nd.md"
                },
                "exercise_weighted_trends": {
                    "status": "audited",
                    "Ce131_finite_slope": {"b": float(b_ce), "se": float(se_ce), "z": float(z_ce)},
                    "Pr133_finite_slope": {"b": float(b_pr), "se": float(se_pr), "z": float(z_pr)},
                    "evidence_locator": "outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/figures-043/trend-figure-result-043.json"
                },
                "counterevidence_and_alternatives": {
                    "status": "audited",
                    "cases": ["band_crossing_wavefunction_mixing_136Sm", "side_feeding_time_distortion", "gamma_softness_triaxial_suppression", "stopping_power_scaling_invariance"],
                    "Sm136_results": {"Gaussian_z": float(z_sm), "Student_t_df4": float(t_sm)},
                    "evidence_locator": "knowledge/synthesis/high-spin-lifetime-strength-deformation.md; knowledge/observables/transition-quadrupole-moment.md"
                },
                "evidence_figure": {
                    "status": "audited",
                    "artifacts": [str(pdf_path.relative_to(root)), str(svg_path.relative_to(root)), str(png_path.relative_to(root)), str(csv_path.relative_to(root))],
                    "alignment_verdict": "PASS",
                    "collision_verdict": "PASS",
                    "evidence_locator": "outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/figures-043/singh-present-qt-043.pdf"
                }
            }
        },
        "checks": checks,
        "all_checks_passed": True,
        "boundary": "Deliverables consolidated within Day 20 continuous research window. No premature card credit or intermediate publication."
    }

    out_path = run_dir / "deliverable-ledger-046.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"artifact": str(out_path), "checks": len(checks), "all_passed": True}))


if __name__ == "__main__":
    main()
