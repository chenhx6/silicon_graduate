#!/usr/bin/env python3
"""Reproducible surrogate model for alpha clustering versus octupole mean field.

This program is deliberately a *calibration model*, not an antisymmetrized
Gogny/Skyrme HFB or GCM calculation.  It evaluates the point-cluster and
liquid-drop-inspired formulae used in the accompanying research note and a
Gaussian collective-coordinate overlap surrogate.  The output is therefore
useful for dimensional checks, limiting cases, and plotting, but it is not a
microscopic alpha preformation probability.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List


HERE = Path(__file__).resolve().parent
R0 = 1.20  # fm
E2 = 1.439964  # MeV fm
HBAR_C = 197.3269804  # MeV fm
M_N = 938.918  # MeV/c^2
RHO0 = 0.16  # fm^-3
K_F = (3.0 * math.pi**2 * RHO0 / 2.0) ** (1.0 / 3.0)  # symmetric matter
E_F = HBAR_C**2 * K_F**2 / (2.0 * M_N)
C_MF = 9.0 * R0 / (4.0 * math.pi)  # e fm in D0=C Z A^(1/3) beta2 beta3


SYSTEMS: List[Dict[str, float | int | str]] = [
    {
        "label": "16O=12C+alpha",
        "A": 16,
        "Z": 8,
        "A_core": 12,
        "Z_core": 6,
        "R_extra": 1.15,
        "beta2": 0.15,
        "beta3": 0.12,
        "sigma_R": 0.80,
        "sigma_beta": 0.080,
        "G_wildermuth": 4,
        "note": "illustrative 12C+alpha relative-motion channel",
    },
    {
        "label": "20Ne=16O+alpha",
        "A": 20,
        "Z": 10,
        "A_core": 16,
        "Z_core": 8,
        "R_extra": 1.15,
        "beta2": 0.45,
        "beta3": 0.18,
        "sigma_R": 0.90,
        "sigma_beta": 0.090,
        "G_wildermuth": 8,
        "note": "illustrative 16O+alpha relative-motion channel",
    },
    {
        "label": "212Po=208Pb+alpha",
        "A": 212,
        "Z": 84,
        "A_core": 208,
        "Z_core": 82,
        "R_extra": 0.75,
        "beta2": 0.08,
        "beta3": 0.05,
        "sigma_R": 1.30,
        "sigma_beta": 0.125,
        "G_wildermuth": 18,
        "note": "illustrative alpha-decay channel; not a measured preformation factor",
    },
    {
        "label": "224Ra=220Rn+alpha",
        "A": 224,
        "Z": 88,
        "A_core": 220,
        "Z_core": 86,
        "R_extra": 0.65,
        "beta2": 0.18,
        "beta3": 0.14,
        "sigma_R": 1.50,
        "sigma_beta": 0.145,
        "G_wildermuth": 18,
        "note": "illustrative pear-shaped region; alpha channel is not the low-energy octupole coordinate",
    },
]


def clip(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def contact_radius(a_core: float) -> float:
    return R0 * (a_core ** (1.0 / 3.0) + 4.0 ** (1.0 / 3.0))


def point_cluster_coefficients(system: Dict[str, float | int | str]) -> Dict[str, float]:
    """Return c1 and c3 for a core+alpha point partition.

    c1 follows the sign convention requested in the task,
    D0=e*(A_core*Z_alpha-4*Z_core)/A*R.  Reversing the intrinsic axis changes
    the sign but not B(E1).  c3 is the corresponding axial point-charge
    coefficient in Q3=2 e c3 R^3.
    """

    a = float(system["A"])
    ac = float(system["A_core"])
    z = float(system["Z"])
    zc = float(system["Z_core"])
    za = 2.0
    aa = 4.0
    c1 = (ac * za - aa * zc) / a
    c3 = zc * (aa / a) ** 3 - za * (ac / a) ** 3
    return {"c1": c1, "c3": c3}


def alpha_localization(system: Dict[str, float | int | str], radius: float) -> Dict[str, float]:
    """Phenomenological locality diagnostic, with explicit ingredients.

    alpha_loc is not a standard observable.  It combines a finite-width
    wave-packet factor, a Pauli-overlap penalty, and a Coulomb-energy penalty.
    Its purpose is to expose the expected trend and its assumptions.
    """

    sigma = float(system["sigma_R"])
    a = float(system["A"])
    zc = float(system["Z_core"])
    rc = contact_radius(float(system["A_core"]))
    width_factor = math.exp(-0.5 * (K_F * sigma) ** 2)
    pauli_penalty = math.exp(-0.75 * (rc / radius) ** 8 * (a / 224.0) ** (1.0 / 3.0))
    coulomb_energy = E2 * zc * 2.0 / radius
    coulomb_penalty = math.exp(-coulomb_energy / E_F)
    alpha_loc = width_factor * pauli_penalty * coulomb_penalty
    return {
        "kF_fm^-1": K_F,
        "EF_MeV": E_F,
        "wavepacket_factor": width_factor,
        "pauli_penalty": pauli_penalty,
        "coulomb_energy_MeV": coulomb_energy,
        "coulomb_penalty": coulomb_penalty,
        "alpha_loc": alpha_loc,
    }


def mf_dipole(system: Dict[str, float | int | str]) -> float:
    """Liquid-drop-inspired mean-field D0 in e fm (raw isovector coefficient)."""

    a = float(system["A"])
    z = float(system["Z"])
    return C_MF * z * a ** (1.0 / 3.0) * float(system["beta2"]) * float(system["beta3"])


def cluster_multipoles(system: Dict[str, float | int | str], radius: float) -> Dict[str, float]:
    coeff = point_cluster_coefficients(system)
    d0 = coeff["c1"] * radius
    q3 = 2.0 * coeff["c3"] * radius**3
    # K=0 rotor proxies for the 0+ -> 1-/3- upward strengths.
    b_e1 = 3.0 / (4.0 * math.pi) * d0**2
    b_e3 = 7.0 / (16.0 * math.pi) * q3**2
    return {
        "D0_cluster_e_fm": d0,
        "Q3_cluster_e_fm3": q3,
        "B_E1_cluster_e2fm2": b_e1,
        "B_E3_cluster_e2fm6": b_e3,
    }


def mf_multipoles(system: Dict[str, float | int | str]) -> Dict[str, float]:
    a = float(system["A"])
    z = float(system["Z"])
    beta3 = float(system["beta3"])
    # Q3 convention Q3=(3/sqrt(7pi)) Z R0^3 beta3.
    q3 = 3.0 / math.sqrt(7.0 * math.pi) * z * (R0 * a ** (1.0 / 3.0)) ** 3 * beta3
    d0 = mf_dipole(system)
    b_e1 = 3.0 / (4.0 * math.pi) * d0**2
    b_e3 = 7.0 / (16.0 * math.pi) * q3**2
    return {
        "D0_mf_raw_e_fm": d0,
        "Q3_mf_e_fm3": q3,
        "B_E1_mf_raw_e2fm2": b_e1,
        "B_E3_mf_e2fm6": b_e3,
    }


def projected_overlap_squared(
    system: Dict[str, float | int | str],
    radius: float,
    beta3_mf: float,
    parity: int,
    j: int,
    radius_mf: float | None = None,
) -> float:
    """Gaussian norm-kernel surrogate for |<C|Ppi PJ|MF>|^2.

    The parity factor is the two-lobe norm-kernel approximation.  A true
    projected HFB/GCM value requires antisymmetrized norm and Hamiltonian
    kernels with particle-number, parity, and angular-momentum projection.
    """

    beta_c = float(system["beta3"])
    sr = float(system["sigma_R"])
    sb = float(system["sigma_beta"])
    if radius_mf is None:
        radius_mf = contact_radius(float(system["A_core"]))
    sr2 = sr**2 + 1.5**2
    sb2 = sb**2 + 0.14**2
    gaussian = math.exp(-0.5 * ((radius - radius_mf) ** 2 / sr2 + (beta_c - beta3_mf) ** 2 / sb2))
    reflected_kernel = math.exp(-2.0 * (beta_c + beta3_mf) ** 2 / sb2)
    parity_projector = 0.5 * (1.0 + float(parity) * reflected_kernel)
    j_projector = math.exp(-j * (j + 1.0) / (2.0 * 4.0**2))
    return clip(gaussian * parity_projector * j_projector, 0.0, 1.0)


def system_row(system: Dict[str, float | int | str]) -> Dict[str, float | int | str]:
    a = float(system["A"])
    radius = contact_radius(float(system["A_core"])) + float(system["R_extra"])
    loc = alpha_localization(system, radius)
    cluster = cluster_multipoles(system, radius)
    mf = mf_multipoles(system)
    coeff = point_cluster_coefficients(system)
    overlap_pos = projected_overlap_squared(system, radius, float(system["beta3"]), +1, 0)
    overlap_neg = projected_overlap_squared(system, radius, float(system["beta3"]), -1, 3)
    alpha_channel = clip(loc["alpha_loc"] * 1.5, 0.0, 1.0)
    row: Dict[str, float | int | str] = {
        "label": system["label"],
        "A": int(system["A"]),
        "Z": int(system["Z"]),
        "A_core": int(system["A_core"]),
        "Z_core": int(system["Z_core"]),
        "R_contact_fm": contact_radius(float(system["A_core"])),
        "R_cluster_fm": radius,
        "beta2": float(system["beta2"]),
        "beta3": float(system["beta3"]),
        "G_wildermuth": int(system["G_wildermuth"]),
        "c1": coeff["c1"],
        "c3": coeff["c3"],
        **loc,
        **cluster,
        **mf,
        "alpha_channel_weight_surrogate": alpha_channel,
        "projected_overlap_squared_0plus": overlap_pos,
        "projected_overlap_squared_3minus": overlap_neg,
        "B_E1_cluster_weighted_surrogate": alpha_channel**2 * cluster["B_E1_cluster_e2fm2"],
        "B_E3_cluster_weighted_surrogate": alpha_channel**2 * cluster["B_E3_cluster_e2fm6"],
        "note": system["note"],
    }
    return row


def overlap_scan(system: Dict[str, float | int | str]) -> Iterable[Dict[str, float | int | str]]:
    a = float(system["A"])
    contact = contact_radius(float(system["A_core"]))
    r0 = contact + float(system["R_extra"])
    for parity, j, label in ((+1, 0, "0+"), (-1, 3, "3-")):
        for radius_index in range(31):
            radius = r0 - 1.5 + 3.0 * radius_index / 30.0
            for beta_index in range(31):
                beta3 = -0.30 + 0.60 * beta_index / 30.0
                yield {
                    "label": system["label"],
                    "A": int(a),
                    "Jpi": label,
                    "R_fm": radius,
                    "beta3_mf": beta3,
                    "overlap_squared": projected_overlap_squared(system, radius, beta3, parity, j),
                }


def write_csv(path: Path, rows: Iterable[Dict[str, object]]) -> None:
    rows = list(rows)
    if not rows:
        return
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    rows = [system_row(system) for system in SYSTEMS]
    scans: List[Dict[str, object]] = []
    for system in SYSTEMS:
        scans.extend(overlap_scan(system))
    write_csv(HERE / "systematics.csv", rows)
    write_csv(HERE / "overlap_scan.csv", scans)
    chart_data = {
        "schema_version": 1,
        "description": "plot-ready values generated from the surrogate model",
        "x": "A",
        "series": {
            "alpha_loc": [{"label": r["label"], "A": r["A"], "value": r["alpha_loc"]} for r in rows],
            "D0_cluster": [{"label": r["label"], "A": r["A"], "value": r["D0_cluster_e_fm"]} for r in rows],
            "D0_mf_raw": [{"label": r["label"], "A": r["A"], "value": r["D0_mf_raw_e_fm"]} for r in rows],
            "B_E1_cluster": [{"label": r["label"], "A": r["A"], "value": r["B_E1_cluster_e2fm2"]} for r in rows],
            "B_E1_mf_raw": [{"label": r["label"], "A": r["A"], "value": r["B_E1_mf_raw_e2fm2"]} for r in rows],
            "B_E3_cluster": [{"label": r["label"], "A": r["A"], "value": r["B_E3_cluster_e2fm6"]} for r in rows],
            "B_E3_mf": [{"label": r["label"], "A": r["A"], "value": r["B_E3_mf_e2fm6"]} for r in rows],
            "overlap_0plus": [{"label": r["label"], "A": r["A"], "value": r["projected_overlap_squared_0plus"]} for r in rows],
            "overlap_3minus": [{"label": r["label"], "A": r["A"], "value": r["projected_overlap_squared_3minus"]} for r in rows],
        },
    }
    (HERE / "chart_data.json").write_text(json.dumps(chart_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    payload = {
        "schema_version": 1,
        "model": "point-cluster + liquid-drop-inspired mean-field + Gaussian projection surrogate",
        "units": {"D0": "e fm", "Q3": "e fm^3", "B_E1": "e^2 fm^2", "B_E3": "e^2 fm^6", "R": "fm"},
        "constants": {"R0_fm": R0, "rho0_fm-3": RHO0, "kF_fm-1": K_F, "EF_MeV": E_F, "C_MF_e_fm": C_MF},
        "assumptions": [
            "Two point clusters have fixed A/Z and an axial relative coordinate.",
            "Q3_cluster=2 e c3 R^3 and B(E3;3->0)=7 Q3^2/(16 pi).",
            "D0_mf=C_MF Z A^(1/3) beta2 beta3 is a raw isoscalar/liquid-drop-inspired scale.",
            "The overlap is a Gaussian norm-kernel surrogate and is not a microscopic P_alpha or HFB/GCM result.",
            "Wildermuth G values are conventional illustrative shell-occupancy inputs; an exact calculation must fix the oscillator basis and daughter configuration.",
        ],
        "rows": rows,
        "overlap_scan_points": len(scans),
    }
    (HERE / "results.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"systems": len(rows), "overlap_scan_points": len(scans), "output_dir": str(HERE)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
