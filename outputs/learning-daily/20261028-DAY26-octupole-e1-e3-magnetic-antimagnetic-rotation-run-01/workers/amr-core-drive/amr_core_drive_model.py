#!/usr/bin/env python3
"""Reduced two-coordinate AMR core-polarization model.

The model is deliberately phenomenological.  It minimizes a laboratory-frame
energy at fixed total spin I and then reports the conjugate frequency
omega=(I-I_qp)/J_core(beta).  This is useful here because a beta-dependent
moment of inertia can change the shears angle at fixed I; a minimization of a
Routhian at fixed omega alone would hide that feedback.

The output is numerical evidence for the stated model only.  It is not a
self-consistent HFB/TAC calculation and it does not separate experimental
B(E2) amplitudes without an independent phase convention.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path


OUT = Path(__file__).resolve().parent


PARAMS = {
    "beta0": 0.11,
    "C_core": 700.0,       # MeV in the dimensionless beta coordinate
    "J0": 8.0,              # hbar^2 / MeV
    "dJ_dbeta": 120.0,      # hbar^2 / MeV per unit beta
    "V_shears": 5.0,        # MeV; V_s=V_shears*cos(theta)^2
    "j_h": 5.5,             # hbar, one blade magnitude
    "j_p": 8.0,             # hbar, fixed aligned contribution
    "Q_shears": 0.267,      # effective e b amplitude
    "Qcore_per_beta": 1.0,  # effective e b amplitude per beta
    "theta_min": 0.0,
    "theta_max": math.pi / 2.0,
    "beta_min": 0.05,
    "beta_max": 0.25,
}


NUCLIDES = {
    "102Pd": {"beta0": 0.10, "J0": 6.0, "dJ_dbeta": 95.0},
    "104Pd": {"beta0": 0.11, "J0": 8.0, "dJ_dbeta": 110.0},
    "106Cd": {"beta0": 0.10, "J0": 7.0, "dJ_dbeta": 100.0},
    "108Cd": {"beta0": 0.105, "J0": 8.0, "dJ_dbeta": 110.0},
    "110Cd": {"beta0": 0.11, "J0": 8.0, "dJ_dbeta": 120.0},
}


def j_core(beta: float, p: dict) -> float:
    return p["J0"] + p["dJ_dbeta"] * (beta - p["beta0"])


def i_qp(theta: float, p: dict) -> float:
    return p["j_p"] + 2.0 * p["j_h"] * math.cos(theta)


def v_shears(theta: float, p: dict) -> float:
    # Open blades (theta=pi/2) are the zero of the residual interaction;
    # rotation closes the blades through the angular-momentum constraint.
    return p["V_shears"] * math.cos(theta) ** 2


def e_core(beta: float, p: dict) -> float:
    return 0.5 * p["C_core"] * (beta - p["beta0"]) ** 2


def lab_energy(theta: float, beta: float, total_i: float, p: dict) -> float:
    j = j_core(beta, p)
    if j <= 0.0:
        return float("inf")
    residual = total_i - i_qp(theta, p)
    return v_shears(theta, p) + e_core(beta, p) + residual * residual / (2.0 * j)


def minimize_grid(total_i: float, p: dict) -> tuple[float, float, float]:
    """Coarse-to-fine deterministic minimizer; no SciPy dependency."""
    lo_t, hi_t = p["theta_min"], p["theta_max"]
    lo_b, hi_b = p["beta_min"], p["beta_max"]
    best = (float("inf"), 0.5 * (lo_t + hi_t), p["beta0"])
    for n in (161, 121, 101, 81):
        for it in range(n):
            theta = lo_t + (hi_t - lo_t) * it / (n - 1)
            for ib in range(n):
                beta = lo_b + (hi_b - lo_b) * ib / (n - 1)
                value = lab_energy(theta, beta, total_i, p)
                if value < best[0]:
                    best = (value, theta, beta)
        span_t = (hi_t - lo_t) / (n - 1) * 2.0
        span_b = (hi_b - lo_b) / (n - 1) * 2.0
        lo_t, hi_t = max(p["theta_min"], best[1] - span_t), min(p["theta_max"], best[1] + span_t)
        lo_b, hi_b = max(p["beta_min"], best[2] - span_b), min(p["beta_max"], best[2] + span_b)
    return best[1], best[2], best[0]


def observables(theta: float, beta: float, total_i: float, p: dict) -> dict:
    j = j_core(beta, p)
    iqp = i_qp(theta, p)
    omega = (total_i - iqp) / j
    # V'= -V sin(2 theta), so tau_s=-V'=+V sin(2 theta).
    tau_shears = p["V_shears"] * math.sin(2.0 * theta)
    # At fixed I the core contribution changes omega and hence the closing
    # torque.  This is the retarding term relative to beta=beta0.
    omega_ref = (total_i - iqp) / p["J0"]
    tau_close = 2.0 * p["j_h"] * omega * math.sin(theta)
    tau_close_ref = 2.0 * p["j_h"] * omega_ref * math.sin(theta)
    tau_retarding = tau_close_ref - tau_close
    f_quad = -p["C_core"] * (beta - p["beta0"])  # elastic restoring force
    f_drive = 0.5 * p["dJ_dbeta"] * omega * omega
    # The requested amplitude-level formula. Q_core is an effective coherent
    # amplitude; its phase is fixed to + for this baseline and scanned below.
    q_s = p["Q_shears"] * math.sin(theta) ** 2
    q_c = p["Qcore_per_beta"] * beta
    b_total = (q_s + q_c) ** 2
    b_shears_only = q_s * q_s
    b_core_only = q_c * q_c
    return {
        "I": total_i,
        "theta_rad": theta,
        "theta_deg": math.degrees(theta),
        "beta2": beta,
        "J_core": j,
        "I_qp": iqp,
        "I_core": j * omega,
        "omega": omega,
        "E_total": lab_energy(theta, beta, total_i, p),
        "V_shears": v_shears(theta, p),
        "E_core": e_core(beta, p),
        "tau_shears": tau_shears,
        "tau_close": tau_close,
        "tau_close_ref_beta0": tau_close_ref,
        "tau_retarding": tau_retarding,
        "F_quad_total": f_quad,
        "F_quad_drive": f_drive,
        "Q_shears_amp": q_s,
        "Q_core_amp": q_c,
        "B_E2_total": b_total,
        "B_E2_shears_only": b_shears_only,
        "B_E2_core_only": b_core_only,
    }


def trajectory(p: dict, i_values: list[float]) -> list[dict]:
    rows = []
    for total_i in i_values:
        theta, beta, _ = minimize_grid(total_i, p)
        rows.append(observables(theta, beta, total_i, p))
    rows.sort(key=lambda row: row["omega"])
    for k, row in enumerate(rows):
        if k == 0 or k == len(rows) - 1:
            row["J2"] = None
            row["J2_over_B_E2"] = None
        else:
            dw = rows[k + 1]["omega"] - rows[k - 1]["omega"]
            dI = rows[k + 1]["I"] - rows[k - 1]["I"]
            row["J2"] = dI / dw if dw else None
            row["J2_over_B_E2"] = row["J2"] / row["B_E2_total"] if row["B_E2_total"] else None
    return rows


def stiffness_scan(base: dict, i_values: list[float]) -> list[dict]:
    rows = []
    for c in (180.0, 300.0, 700.0, 1100.0, 1500.0):
        p = dict(base)
        p["C_core"] = c
        tr = trajectory(p, i_values)
        for row in tr:
            rows.append({"C_core": c, "I": row["I"], "omega": row["omega"],
                         "theta_deg": row["theta_deg"], "beta2": row["beta2"],
                         "J_core": row["J_core"], "B_E2_total": row["B_E2_total"],
                         "tau_retarding": row["tau_retarding"]})
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    i_values = [12.0 + 0.25 * n for n in range(57)]
    rows = trajectory(PARAMS, i_values)
    scan = stiffness_scan(PARAMS, i_values[::2])
    write_csv(OUT / "amr_core_drive_trajectory.csv", rows)
    write_csv(OUT / "amr_core_drive_stiffness_scan.csv", scan)

    # A compact plotting payload keeps the artifact usable without matplotlib.
    chart = {
        "trajectory": [{k: r[k] for k in ("I", "omega", "theta_deg", "beta2", "J_core", "tau_shears", "tau_retarding", "B_E2_total", "J2_over_B_E2")} for r in rows],
        "stiffness_scan": scan,
        "observed_110Cd_B_E2_e2b2": [0.14, 0.12, 0.11, 0.09, 0.06],
        "observed_110Cd_initial_spins": [16, 18, 20, 22, 24],
    }
    (OUT / "amr_core_drive_chart_data.json").write_text(json.dumps(chart, indent=2) + "\n", encoding="utf-8")

    summary = {
        "model": "fixed-I laboratory energy with beta-dependent core inertia",
        "equations": {
            "E": "V_shears(theta)+0.5*C_core*(beta-beta0)^2+(I-I_qp(theta))^2/(2*J_core(beta))",
            "V_shears": "V_shears*cos(theta)^2",
            "I_qp": "j_p+2*j_h*cos(theta)",
            "J_core": "J0+dJ_dbeta*(beta-beta0)",
            "B_E2": "(Q_shears*sin(theta)^2+Q_core(beta))^2",
            "tau_shears": "-dV/dtheta=V_shears*sin(2*theta)",
            "F_quad": "-dE_core/d beta=-C_core*(beta-beta0)",
        },
        "parameters": PARAMS,
        "nuclei_parameter_context": NUCLIDES,
        "trajectory_rows": len(rows),
        "stiffness_rows": len(scan),
        "limits": [
            "Phenomenological two-coordinate surrogate; not HFB/TAC or angular-momentum projected.",
            "Q_shears and Q_core are coherent effective amplitudes; experimental B(E2) cannot be uniquely partitioned without phase and transition-density information.",
            "Rather 2014 local source is a first-page excerpt; no 104Pd point-by-point table is asserted here.",
        ],
    }
    for name in ("amr_core_drive_trajectory.csv", "amr_core_drive_stiffness_scan.csv", "amr_core_drive_chart_data.json"):
        summary.setdefault("artifact_sha256", {})[name] = file_sha256(OUT / name)
    (OUT / "amr_core_drive_results.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"trajectory_rows": len(rows), "stiffness_rows": len(scan), "output": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
