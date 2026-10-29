#!/usr/bin/env python3
"""Transparent beta2-beta3 third-well and parity-tunnelling sensitivity model.

This is a reproducible reduced model, not an EDF or a fit to fission data.
It deliberately exposes the distinction between a beta3=0 constrained path,
an octupole-relaxed path, and a parity WKB calculation with an assumed mass.
All numerical outputs are labelled as model proxies in the companion README.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


HERE = Path(__file__).resolve().parent

NUCLEI = {
    "230Th": {"Z": 90, "A": 230, "oct_strength": 19.0, "q3_target": 0.30},
    "232Th": {"Z": 90, "A": 232, "oct_strength": 25.0, "q3_target": 0.36},
    "232U": {"Z": 92, "A": 232, "oct_strength": 29.0, "q3_target": 0.39},
    "234U": {"Z": 92, "A": 234, "oct_strength": 31.0, "q3_target": 0.41},
    "236U": {"Z": 92, "A": 236, "oct_strength": 32.0, "q3_target": 0.43},
}

B2_VALUES = [0.10 + 0.01 * i for i in range(121)]
B3_VALUES = [-0.50 + 0.0125 * i for i in range(81)]


def quadrupole_path(beta2: float) -> float:
    """Three-well reference path; coefficients are diagnostic controls."""
    return (
        1.35
        + 0.08 * (beta2 - 0.25)
        - 1.05 * math.exp(-((beta2 - 0.25) / 0.085) ** 2)
        - 0.74 * math.exp(-((beta2 - 0.57) / 0.105) ** 2)
        - 0.46 * math.exp(-((beta2 - 0.92) / 0.115) ** 2)
        + 0.95 * math.exp(-((beta2 - 0.92) / 0.13) ** 2)
        + 0.16 * (beta2 - 0.72) ** 2
    )


def octupole_quadratic(beta2: float, p: dict[str, float]) -> float:
    return 5.0 - p["oct_strength"] * math.exp(-((beta2 - 0.92) / 0.14) ** 2)


def energy(beta2: float, beta3: float, p: dict[str, float]) -> float:
    a3 = octupole_quadratic(beta2, p)
    return quadrupole_path(beta2) + 0.5 * a3 * beta3**2 + 35.0 * beta3**4


def relaxed_beta3(beta2: float, p: dict[str, float]) -> float:
    a3 = octupole_quadratic(beta2, p)
    return math.sqrt(max(0.0, -a3 / 140.0))


def relaxed_energy(beta2: float, p: dict[str, float]) -> float:
    q3 = relaxed_beta3(beta2, p)
    return energy(beta2, q3, p)


def local_minima(rows: list[tuple[float, float]]) -> list[tuple[float, float]]:
    result = []
    for i in range(1, len(rows) - 1):
        if rows[i][1] <= rows[i - 1][1] and rows[i][1] <= rows[i + 1][1]:
            result.append(rows[i])
    return result


def path_features(p: dict[str, float]) -> dict[str, float]:
    symmetric = [(b, quadrupole_path(b)) for b in B2_VALUES]
    relaxed = [(b, relaxed_energy(b, p)) for b in B2_VALUES]
    mins_rel = local_minima(relaxed)
    third_rel = min(mins_rel, key=lambda x: abs(x[0] - 0.92))
    # Compare both paths at the relaxed HD coordinate. The constrained path
    # need not have a local minimum there, which is the instability being
    # diagnosed rather than hidden by selecting a different beta2 point.
    third_sym = (third_rel[0], quadrupole_path(third_rel[0]))
    symmetric_local = any(abs(q - third_rel[0]) <= 0.015 for q, _ in local_minima(symmetric))
    ground_rel = min(relaxed, key=lambda x: x[1])
    hd_beta3 = relaxed_beta3(third_rel[0], p)

    def between(a: float, b: float, curve: list[tuple[float, float]]) -> float:
        lo, hi = sorted((a, b))
        return max(v for q, v in curve if lo <= q <= hi)

    # The outer barrier is truncated at beta2=1.30. This is a path diagnostic,
    # not a multidimensional least-action fission saddle.
    outer_saddle = max(v for q, v in relaxed if third_rel[0] <= q <= 1.30)
    inner_saddle = between(0.57, third_rel[0], relaxed)
    return {
        "beta2_third_symmetric": third_sym[0],
        "energy_third_symmetric_MeV": third_sym[1],
        "beta2_third_relaxed": third_rel[0],
        "symmetric_path_has_local_minimum_near_third": symmetric_local,
        "beta3_third_relaxed": hd_beta3,
        "energy_third_relaxed_MeV": third_rel[1],
        "energy_ground_relaxed_MeV": ground_rel[1],
        "third_well_octupole_gain_MeV": third_sym[1] - third_rel[1],
        "inner_path_barrier_above_third_MeV": inner_saddle - third_rel[1],
        "outer_path_barrier_above_third_MeV": outer_saddle - third_rel[1],
    }


def q3_geometry(p: dict[str, float], beta3: float, beta2: float) -> dict[str, float]:
    radius = 1.20 * p["A"] ** (1.0 / 3.0)
    q3_efm3 = (3.0 / (4.0 * math.pi)) * p["Z"] * radius**3 * beta3
    # 1 b^(3/2) = (100 fm^2)^(3/2) = 1000 fm^3.
    return {
        "R_fm": radius,
        "Q3_geometry_efm3": q3_efm3,
        "Q3_geometry_eb32": q3_efm3 / 1000.0,
        "D0_proxy_efm": 0.20 * beta3 / 0.40,
        "beta2_used_for_D0": beta2,
        "observable_status": "geometrical/proxy; not an experimental extraction",
    }


def parity_wkb(beta3: float, mass: float = 140.0) -> dict[str, float]:
    """Double-well WKB estimate, with a dimensionless collective mass input."""
    d4 = 140.0
    barrier = d4 * beta3**4 / 4.0
    curvature = 2.0 * d4 * beta3**2
    # V(q)-V_min = d4/4*(q^2-beta3^2)^2; analytic action at the well bottom.
    action = 2.0 * math.sqrt(2.0 * mass) * math.sqrt(d4) * beta3**3 / 3.0
    hbar_omega = math.sqrt(curvature / mass)
    splitting_mev = hbar_omega / math.pi * math.exp(-action)
    return {
        "beta3": beta3,
        "collective_mass_assumed": mass,
        "barrier_at_beta3_MeV": barrier,
        "action_over_hbar": action,
        "hbar_omega_MeV": hbar_omega,
        "parity_splitting_keV": 1000.0 * splitting_mev,
    }


def decay_rows(summary: dict[str, dict[str, float]]) -> list[dict[str, float | str]]:
    rows = []
    for nucleus, f in summary.items():
        for excitation in (0.0, 0.5, 1.0, 2.0):
            barrier = max(0.02, f["outer_path_barrier_above_third_MeV"] - excitation)
            width = 0.30
            mass = 12.0
            action = 2.0 * width * math.sqrt(2.0 * mass * barrier)
            transmission = math.exp(-2.0 * action)
            rows.append(
                {
                    "nucleus": nucleus,
                    "excitation_above_third_MeV": excitation,
                    "outer_barrier_remaining_MeV": barrier,
                    "fission_action_proxy": action,
                    "fission_transmission_proxy": transmission,
                    "gamma_width_needed_for_competition": "unknown_without_level_density_and_E1/E2/E3_strengths",
                    "interpretation": "fission proxy is suppressed when outer barrier remains; no absolute branching ratio",
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(rows[0])
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    pes_rows = []
    summaries = {}
    wkb_rows = []
    chart = {"pes": {}, "parity_wkb": {}, "q3": {}}
    for nucleus, p in NUCLEI.items():
        for beta2 in B2_VALUES:
            for beta3 in B3_VALUES:
                pes_rows.append({
                    "nucleus": nucleus,
                    "beta2": beta2,
                    "beta3": beta3,
                    "energy_MeV": energy(beta2, beta3, p),
                    "path": "2D_beta2_beta3",
                    "reflection_partner_included": True,
                })
        f = path_features(p)
        geom = q3_geometry(p, f["beta3_third_relaxed"], f["beta2_third_relaxed"])
        f.update(geom)
        summaries[nucleus] = f
        chart["pes"][nucleus] = {
            "beta2": B2_VALUES,
            "symmetric_energy_MeV": [quadrupole_path(b) for b in B2_VALUES],
            "relaxed_energy_MeV": [relaxed_energy(b, p) for b in B2_VALUES],
            "relaxed_beta3": [relaxed_beta3(b, p) for b in B2_VALUES],
        }
        chart["q3"][nucleus] = geom
        for beta3 in [0.05 + 0.01 * i for i in range(46)]:
            row = parity_wkb(beta3)
            row["nucleus"] = nucleus
            wkb_rows.append(row)
        chart["parity_wkb"][nucleus] = [r for r in wkb_rows if r["nucleus"] == nucleus]

    decay = decay_rows(summaries)
    write_csv(HERE / "pes_grid.csv", pes_rows)
    write_csv(HERE / "parity_wkb.csv", wkb_rows)
    write_csv(HERE / "decay_competition.csv", decay)
    (HERE / "chart_data.json").write_text(json.dumps(chart, indent=2) + "\n", encoding="utf-8")
    result = {
        "model": "reduced beta2-beta3 third-well plus one-dimensional parity-WKB sensitivity",
        "status": "illustrative_reduced_model_not_EDF_or_experimental_fit",
        "equations": {
            "energy": "V=V_quad(beta2)+0.5*a3(beta2)*beta3^2+35*beta3^4",
            "a3": "a3=5- strength*exp(-((beta2-0.92)/0.14)^2)",
            "q3": "Q3=(3/(4*pi))*Z*R^3*beta3; R=1.2*A^(1/3) fm",
            "wkb": "S/hbar=2*sqrt(2*B)*sqrt(d4)*beta3^3/3; Delta=hw/pi*exp(-S/hbar)",
        },
        "grid": {"beta2": [min(B2_VALUES), max(B2_VALUES), len(B2_VALUES)], "beta3": [min(B3_VALUES), max(B3_VALUES), len(B3_VALUES)]},
        "collective_mass_assumed_for_wkb": 140.0,
        "note": "All coefficients and masses are explicit sensitivity inputs; no row is a measured barrier, beta3, Q3, D0, or decay width.",
        "nuclei": summaries,
        "files": ["hyperdeformed_actinides.py", "pes_grid.csv", "parity_wkb.csv", "decay_competition.csv", "chart_data.json", "README.md"],
    }
    (HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
