#!/usr/bin/env python3
"""Finite-j AMR cutoff and core-polarization response model.

This is a deterministic, standard-library-only calculation.  It does not
solve a TAC/HFB or projected shell-model Hamiltonian.  The purpose is to make
the angular-momentum bookkeeping and the fixed-I core response explicit:

    E(I, theta) = V_shears(theta)
                  + (I - 2*j_blade*cos(theta/2))**2/(2*J_core)

The four identical fermions are first reduced to the exact single-j pair
limits J_p,max=8 and J_n,max=10.  The effective coordinate then uses
2*j_blade = J_val,max = 18, so that x=cos(theta/2) gives
J_val(theta)=18*x.  The two E2 amplitudes below are effective amplitudes in
eb; their square is an observable proxy in e^2 b^2.  A nonzero core
amplitude is deliberately kept separate from the shears sin^4(theta/2)
factor because a finite J_core by itself cannot create a B(E2) floor at
theta=0.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Any


OUTDIR = Path(__file__).resolve().parent
JVAL_MAX = 18.0
J_BLADE_EFFECTIVE = JVAL_MAX / 2.0


CASES: dict[str, dict[str, Any]] = {
    # Roy et al. use J_m=19.5 hbar^2/MeV for their 110Cd core-plus-shears
    # interpretation.  The a,b,Q parameters are a transparent illustrative
    # response set chosen to expose the endpoint and ratio mechanism.
    "110Cd": {
        "J_core_hbar2_per_MeV": 19.5,
        "a_shears_MeV": 0.80,
        "b_shears_MeV": 1.45,
        "Q_shears_eb": 0.18,
        "Q_core_eb": 0.30,
        "E2_phase": 1.0,
        "data_status": "110Cd-like conditional model; Roy Table 1 comparison",
    },
    # The Pd case is a geometry/control variant.  Its amplitude is not a new
    # extraction from the incomplete local Rather 2014 page.
    "104Pd": {
        "J_core_hbar2_per_MeV": 17.0,
        "a_shears_MeV": 0.80,
        "b_shears_MeV": 1.45,
        "Q_shears_eb": 0.27,
        "Q_core_eb": 0.14,
        "E2_phase": 1.0,
        "data_status": "104Pd-like conditional geometry/control; amplitude not source-fitted",
    },
}


ROY_110CD_TABLE1 = [
    {"I": 16, "Egamma_keV": 1075, "tau_ps": 0.36, "d_tau_ps": 0.03, "B_E2_e2b2": 0.14, "d_B_E2_e2b2": 0.01},
    {"I": 18, "Egamma_keV": 1224, "tau_ps": 0.23, "d_tau_ps": 0.03, "B_E2_e2b2": 0.12, "d_B_E2_e2b2": 0.02},
    {"I": 20, "Egamma_keV": 1323, "tau_ps": 0.17, "d_tau_ps": 0.03, "B_E2_e2b2": 0.11, "d_B_E2_e2b2": 0.02},
    {"I": 22, "Egamma_keV": 1314, "tau_ps": 0.21, "d_tau_ps": 0.07, "B_E2_e2b2": 0.09, "d_B_E2_e2b2": 0.03},
    {"I": 24, "Egamma_keV": 1358, "tau_ps": 0.27, "d_tau_ps": 0.07, "B_E2_e2b2": 0.06, "d_B_E2_e2b2": 0.02},
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def potential(x: float, params: dict[str, Any]) -> float:
    """V_shears(x) in MeV, with x=cos(theta/2)."""
    a = float(params["a_shears_MeV"])
    b = float(params["b_shears_MeV"])
    return a * x * x + b * x**4


def potential_prime(x: float, params: dict[str, Any]) -> float:
    a = float(params["a_shears_MeV"])
    b = float(params["b_shears_MeV"])
    return 2.0 * a * x + 4.0 * b * x**3


def potential_second(x: float, params: dict[str, Any]) -> float:
    a = float(params["a_shears_MeV"])
    b = float(params["b_shears_MeV"])
    return 2.0 * a + 12.0 * b * x * x


def spin_from_x(x: float, params: dict[str, Any]) -> float:
    """Stationarity map I(x)=J_val*x+J_core*V'(x)/J_val."""
    j_core = float(params["J_core_hbar2_per_MeV"])
    return JVAL_MAX * x + j_core * potential_prime(x, params) / JVAL_MAX


def solve_x(I: float, params: dict[str, Any]) -> tuple[float, bool]:
    """Solve the fixed-I stationary equation on 0<=x<=1.

    For nonnegative a,b the map I(x) is monotone.  Once I exceeds I(1), the
    finite-j valence sector is pinned at x=1 and all additional spin is core
    rotation.  The returned boolean identifies that endpoint branch.
    """
    if I <= 0.0:
        return 0.0, False
    endpoint_spin = spin_from_x(1.0, params)
    if I >= endpoint_spin:
        return 1.0, True
    lo, hi = 0.0, 1.0
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        if spin_from_x(mid, params) < I:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi), False


def energy(I: float, x: float, params: dict[str, Any]) -> float:
    j_core = float(params["J_core_hbar2_per_MeV"])
    residual = I - JVAL_MAX * x
    return potential(x, params) + residual * residual / (2.0 * j_core)


def row_for(I: float, params: dict[str, Any], case: str) -> dict[str, Any]:
    x, endpoint = solve_x(I, params)
    j_core = float(params["J_core_hbar2_per_MeV"])
    residual = I - JVAL_MAX * x
    omega = residual / j_core
    vpp = potential_second(x, params)
    dI_dx = JVAL_MAX + j_core * vpp / JVAL_MAX
    dx_dI = 0.0 if endpoint else 1.0 / dI_dx
    theta = 2.0 * math.acos(max(0.0, min(1.0, x)))
    if endpoint:
        dtheta_dI = 0.0
    else:
        dtheta_dI = -2.0 * dx_dI / math.sqrt(max(1.0e-30, 1.0 - x * x))
    # s = sin^2(theta/2) = 1-x^2.  This is the nonsingular closure
    # coordinate at x=1, whereas d(theta)/dI has an endpoint coordinate
    # singularity if one approaches theta=0 from the interior.
    s = 1.0 - x * x
    ds_dI = -2.0 * x * dx_dI
    q_s = float(params["Q_shears_eb"])
    q_c = float(params["Q_core_eb"])
    phase = float(params["E2_phase"])
    a_shears = q_s * s
    a_core = q_c
    b_shears = a_shears * a_shears
    b_core = a_core * a_core
    b_interference = 2.0 * phase * a_shears * a_core
    b_total = b_shears + b_core + b_interference
    j2_tangent = j_core if endpoint else j_core + JVAL_MAX**2 / vpp
    return {
        "case": case,
        "I_hbar": I,
        "x_cos_theta_over_2": x,
        "theta_deg": math.degrees(theta),
        "J_val_hbar": JVAL_MAX * x,
        "R_core_hbar": residual,
        "omega_MeV": omega,
        "V_shears_MeV": potential(x, params),
        "E_min_MeV": energy(I, x, params),
        "V_second_MeV": vpp,
        "dI_dx_hbar": dI_dx,
        "dx_dI_per_hbar": dx_dI,
        "dtheta_dI_rad_per_hbar": dtheta_dI,
        "dtheta_dI_deg_per_hbar": math.degrees(dtheta_dI),
        "d_sin2_dI_per_hbar": ds_dI,
        "B_shears_only_e2b2": b_shears,
        "B_core_only_e2b2": b_core,
        "B_interference_e2b2": b_interference,
        "B_E2_total_e2b2": b_total,
        "J2_tangent_hbar2_per_MeV": j2_tangent,
        "J2_over_B_tangent": j2_tangent / b_total if b_total > 0.0 else None,
        "endpoint_valence_pinned": endpoint,
    }


def add_finite_difference_j2(rows: list[dict[str, Any]], params: dict[str, Any]) -> None:
    """Add J^(2)=4/(E_gamma(I+2)-E_gamma(I)) on an integer-spin grid."""
    integer_rows = {int(round(row["I_hbar"])): row for row in rows if abs(row["I_hbar"] - round(row["I_hbar"])) < 1e-9}
    for row in rows:
        I = int(round(row["I_hbar"]))
        if I not in integer_rows or I - 2 not in integer_rows or I + 2 not in integer_rows:
            row["Egamma_down_MeV"] = None
            row["Egamma_up_MeV"] = None
            row["J2_fd_hbar2_per_MeV"] = None
            row["J2_over_B_fd"] = None
            continue
        e_down = integer_rows[I]["E_min_MeV"] - integer_rows[I - 2]["E_min_MeV"]
        e_up = integer_rows[I + 2]["E_min_MeV"] - integer_rows[I]["E_min_MeV"]
        denominator = e_up - e_down
        j2_fd = 4.0 / denominator if denominator > 0.0 else None
        row["Egamma_down_MeV"] = e_down
        row["Egamma_up_MeV"] = e_up
        row["J2_fd_hbar2_per_MeV"] = j2_fd
        row["J2_over_B_fd"] = (j2_fd / row["B_E2_total_e2b2"] if j2_fd is not None and row["B_E2_total_e2b2"] > 0 else None)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def pure_shears_row(I: float) -> dict[str, Any]:
    """No-core reference: hard constraint I=J_val*x, valid only I<=18."""
    if I > JVAL_MAX:
        return {
            "I_hbar": I,
            "x_pure": None,
            "theta_pure_deg": None,
            "dtheta_dI_pure_deg_per_hbar": None,
            "status": "outside fixed-valence domain",
        }
    x = I / JVAL_MAX
    theta = 2.0 * math.acos(max(0.0, min(1.0, x)))
    if x >= 1.0:
        derivative = None
    else:
        derivative = math.degrees(-2.0 / (JVAL_MAX * math.sqrt(1.0 - x * x)))
    return {
        "I_hbar": I,
        "x_pure": x,
        "theta_pure_deg": math.degrees(theta),
        "dtheta_dI_pure_deg_per_hbar": derivative,
        "status": "pure-shears reference",
    }


def make_case_rows(case: str, params: dict[str, Any]) -> list[dict[str, Any]]:
    # Half-hbar mesh shows the continuous trajectory; integer rows support
    # the finite-difference J^(2) diagnostic.
    rows = [row_for(12.0 + 0.5 * n, params, case) for n in range(33)]
    add_finite_difference_j2(rows, params)
    return rows


def selected(rows: list[dict[str, Any]], spins: tuple[int, ...] = (14, 16, 18, 20, 22, 24, 26, 28)) -> list[dict[str, Any]]:
    wanted = set(spins)
    return [row for row in rows if int(round(row["I_hbar"])) in wanted and abs(row["I_hbar"] - round(row["I_hbar"])) < 1e-9]


def main() -> None:
    all_rows: list[dict[str, Any]] = []
    case_summaries: dict[str, Any] = {}
    for case, params in CASES.items():
        rows = make_case_rows(case, params)
        all_rows.extend(rows)
        endpoint_spin = spin_from_x(1.0, params)
        endpoint_row = row_for(endpoint_spin, params, case)
        case_summaries[case] = {
            "parameters": params,
            "I_sat_hbar": endpoint_spin,
            "endpoint": endpoint_row,
            "selected_rows": selected(rows),
        }

    trajectory_path = OUTDIR / "amr_core_polarization_trajectory.csv"
    write_csv(trajectory_path, all_rows)

    # The no-core comparison uses the 110Cd-like potential and quantifies the
    # closure delay on the common I<=18 domain.
    cd_rows = {int(round(row["I_hbar"])): row for row in make_case_rows("110Cd", CASES["110Cd"]) if abs(row["I_hbar"] - round(row["I_hbar"])) < 1e-9}
    comparison_rows: list[dict[str, Any]] = []
    for I in (12, 14, 16, 18, 20, 24, 26):
        pure = pure_shears_row(float(I))
        finite = cd_rows[I]
        pure_d = pure["dtheta_dI_pure_deg_per_hbar"]
        finite_d = finite["dtheta_dI_deg_per_hbar"]
        comparison_rows.append({
            **pure,
            "theta_core_deg": finite["theta_deg"],
            "dtheta_dI_core_deg_per_hbar": finite_d,
            "d_sin2_dI_core_per_hbar": finite["d_sin2_dI_per_hbar"],
            "closure_delay_deg": (finite["theta_deg"] - pure["theta_pure_deg"] if pure["theta_pure_deg"] is not None else None),
            "abs_slope_ratio_core_over_pure": (abs(finite_d) / abs(pure_d) if pure_d not in (None, 0.0) else None),
        })
    comparison_path = OUTDIR / "closure_comparison.csv"
    write_csv(comparison_path, comparison_rows)

    scan_rows: list[dict[str, Any]] = []
    I_scan = 16.0
    base = CASES["110Cd"]
    for j_core in (0.1, 5.0, 10.0, 19.5, 30.0):
        params = dict(base)
        params["J_core_hbar2_per_MeV"] = j_core
        row = row_for(I_scan, params, "110Cd")
        scan_rows.append({
            "I_hbar": I_scan,
            "J_core_hbar2_per_MeV": j_core,
            "theta_deg": row["theta_deg"],
            "dtheta_dI_deg_per_hbar": row["dtheta_dI_deg_per_hbar"],
            "J2_tangent_hbar2_per_MeV": row["J2_tangent_hbar2_per_MeV"],
            "R_core_hbar": row["R_core_hbar"],
        })
    scan_path = OUTDIR / "core_inertia_scan_at_I16.csv"
    write_csv(scan_path, scan_rows)

    pair_limit_rows = [
        {"pair": "pi(g9/2)^-2", "j_single_hbar": 4.5, "allowed_J_hbar": "0,2,4,6,8", "J_max_hbar": 8, "exchange_rule": "even J"},
        {"pair": "nu(h11/2)^2", "j_single_hbar": 5.5, "allowed_J_hbar": "0,2,4,6,8,10", "J_max_hbar": 10, "exchange_rule": "even J"},
    ]
    pair_path = OUTDIR / "finite_j_pair_limits.csv"
    write_csv(pair_path, pair_limit_rows)

    params_payload = {
        "status": "provisional conditional mechanism model",
        "units": {"I": "hbar", "J_core": "hbar^2/MeV", "V": "MeV", "omega": "MeV", "Q": "eb", "B_E2": "e^2 b^2"},
        "finite_j_boundary": {
            "exchange_phase": "P12 |(jj)JM> = (-1)^(2j-J)|(jj)JM>; fermion antisymmetry requires phase=-1",
            "proton_pair": {"orbit": "g9/2", "allowed_J_hbar": [0, 2, 4, 6, 8], "J_max_hbar": 8},
            "neutron_pair": {"orbit": "h11/2", "allowed_J_hbar": [0, 2, 4, 6, 8, 10], "J_max_hbar": 10},
            "J_val_max_hbar": JVAL_MAX,
            "classical_unantisymmetrized_upper_bound_hbar": 20,
            "effective_mapping": "x=cos(theta/2), J_val=J_val,max*x=2*j_blade*x, j_blade=9; this is a coarse-grained four-blade coordinate, not one physical single-particle j.",
        },
        "equations": {
            "energy": "E(I,x)=V_shears(x)+(I-J_val,max*x)^2/(2 J_core)",
            "potential": "V_shears(x)=a*x^2+b*x^4",
            "stationarity": "I=J_val,max*x+(J_core/J_val,max)*V_shears_prime(x)",
            "core_residual": "R_core=I-J_val,max*x=J_core*omega",
            "closure_slope": "dx/dI=1/[J_val,max+(J_core/J_val,max)V_shears_second(x)]; dtheta/dI=-2 dx/dI/sqrt(1-x^2)",
            "dynamic_inertia": "J^(2)=J_core+J_val,max^2/V_shears_second(x) on the interior branch; J^(2)=J_core after x is pinned at 1",
            "E2_proxy": "B_total=[Q_core + phase*Q_shears*sin^2(theta/2)]^2; B_shears_only=Q_shears^2*sin^4(theta/2)",
        },
        "cases": CASES,
        "evidence": {
            "Roy_2011": "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md:47-52, 68",
            "Rather_2014": "knowledge/sources/rather-2014-104pd-antimagnetic-first-page.md:43-47",
            "Zhang_2019": "knowledge/sources/zhang-2019-104pd-pnc-antimagnetic-rotation.md:44-52",
        },
        "boundary": "The model is a transparent surrogate, not a microscopic TAC/HFB or angular-momentum-projected calculation; Q_core and Q_shears are effective amplitudes.",
    }
    params_path = OUTDIR / "parameters.json"
    params_path.write_text(json.dumps(params_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    result_payload: dict[str, Any] = {
        "status": "completed provisional AMR finite-j/core-polarization scan",
        "script": Path(__file__).name,
        "finite_j_pair_limits": pair_limit_rows,
        "Roy_110Cd_Table1_reference": ROY_110CD_TABLE1,
        "case_summaries": case_summaries,
        "closure_comparison_at_common_spins": comparison_rows,
        "core_inertia_scan_at_I16": scan_rows,
        "checks": {
            "J_val_max_hbar": JVAL_MAX,
            "classical_minus_quantum_upper_bound_hbar": 20.0 - JVAL_MAX,
            "110Cd_high_spin_platform_window": [0.08, 0.12],
            "110Cd_model_platform_rows_I_hbar": [22, 24, 26, 28],
            "110Cd_model_platform_values_e2b2": [row["B_E2_total_e2b2"] for row in case_summaries["110Cd"]["selected_rows"] if row["I_hbar"] in (22, 24, 26, 28)],
            "110Cd_ratio_rows_I_hbar": [16, 18, 20, 22, 24, 26],
            "110Cd_ratio_values_fd": [row["J2_over_B_fd"] for row in case_summaries["110Cd"]["selected_rows"] if row["I_hbar"] in (16, 18, 20, 22, 24, 26)],
        },
        "output_files": {},
    }
    result_path = OUTDIR / "results.json"
    result_path.write_text(json.dumps(result_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    output_paths = [trajectory_path, comparison_path, scan_path, pair_path, params_path, result_path]
    result_payload["output_files"] = {path.name: sha256(path) for path in output_paths}
    result_path.write_text(json.dumps(result_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("finite-j limits: Jp_max=8, Jn_max=10, Jval_max=18 hbar")
    for case, summary in case_summaries.items():
        endpoint = summary["endpoint"]
        print(f"{case}: I_sat={summary['I_sat_hbar']:.6f} hbar, endpoint R_core={endpoint['R_core_hbar']:.6f} hbar")
    print("110Cd selected platform:", [round(v, 6) for v in result_payload["checks"]["110Cd_model_platform_values_e2b2"]])
    print("110Cd selected J2/B(fd):", [round(v, 3) for v in result_payload["checks"]["110Cd_ratio_values_fd"] if v is not None])


if __name__ == "__main__":
    main()
