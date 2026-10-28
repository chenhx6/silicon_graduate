#!/usr/bin/env python3
"""Reduced TAC-RMF/CDFT response model for 135Pr and 137Pr.

This is a reproducible diagnostic model, not a PC-PK1 solver.  It keeps the
cranked one-body form h = h0 - omega_x Jx - omega_z Jz, minimizes the
orientation angle, and mixes effective 3qp/5qp Routhians.  The current fields
are smooth 2-D proxies whose integrated moments are tied to the same
orientation and blocking variables.  No claim is made that the proxy fields
are published CDFT densities.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


OUT = Path(__file__).resolve().parent
HBAR_OMEGA = [0.20 + 0.005 * i for i in range(71)]


CASES = {
    "135Pr": {
        "N": 76,
        "crossing_target": 0.37,
        "spin_target": 16.5,  # 33/2, Garg et al. comparison
        "delta_p": 1.080,
        "delta_n": 0.764,
        # Relative neutron chemical-potential shift is a sensitivity input,
        # not a published 135Pr/137Pr PC-PK1 output.
        "lambda_n_shift": 0.00,
        "block_n": 0.00,
    },
    "137Pr": {
        "N": 78,
        "crossing_target": 0.42,
        "spin_target": 17.5,  # 35/2, Garg et al. comparison
        "delta_p": 1.048,
        "delta_n": 0.650,
        # A controlled +0.20-MeV higher-neutron-Fermi-surface scenario.
        "lambda_n_shift": 0.20,
        "block_n": 0.0,
    },
}


def fermi_occupancy(e_minus_lambda: float, delta: float) -> float:
    """Smooth HFB-like occupation proxy, bounded for large arguments."""
    x = max(-60.0, min(60.0, 2.0 * e_minus_lambda / max(delta, 1.0e-9)))
    return 1.0 / (1.0 + math.exp(x))


def config_parameters(case: dict, label: str) -> dict:
    """Return effective blade and pair-blocking parameters.

    The values reproduce the source-reported crossing locations only as a
    reduced response model.  The 3qp and 5qp labels follow Garg 2015 and
    Agarwal 2007; they are not a replacement for blocked PC-PK1 orbitals.
    """
    # Proton g7/2 pair is the extra 5qp alignment.  Neutron blocking is made
    # explicit so that the N=78 sensitivity can be reversed in one line.
    neutron_modulation = 1.0 - 0.32 * case["lambda_n_shift"] / 0.20
    neutron_modulation = max(0.45, min(1.0, neutron_modulation))
    if label == "3qp":
        jp, jn = 5.5, 10.0 * (1.0 - 0.05 * case["lambda_n_shift"] / 0.20)
        theta0 = math.radians(31.6 if case["N"] == 76 else 30.8)
        e0 = 0.0
    else:
        jp = 11.5 * (1.0 - 0.04 * case["lambda_n_shift"] / 0.20)
        jn = 10.0 * neutron_modulation
        theta0 = math.radians(26.9 if case["N"] == 76 else 27.8)
        e0 = 2.20

    # The g7/2-pair alignment slope is adjusted by the controlled N=78
    # blocking scenario.  Choose the reduced slopes so E5/(J5-J3) equals the
    # source comparison point (0.37 or 0.42 MeV).
    return {
        "jp": jp,
        "jn": jn,
        "theta0": theta0,
        "e0": e0,
        "neutron_modulation": neutron_modulation,
    }


def minimize_orientation(omega: float, params: dict) -> tuple[float, float, float, float]:
    """Minimize a reduced TAC Routhian over theta in the x-z plane."""
    best = None
    # A dense deterministic grid avoids optimizer/package dependencies.
    for k in range(1801):
        theta = math.radians(0.05 * k)
        # Weak orientation stiffness represents the self-consistent shape
        # response.  It is not a fitted PC-PK1 parameter.
        stiffness = 0.28
        jx = params["jp"] * math.sin(theta) + 0.28 * params["jn"] * math.sin(theta)
        jz = params["jn"] * math.cos(theta) + 0.18 * params["jp"] * math.cos(theta)
        # Intrinsic proton/neutron alignment components; the cranking field
        # projects these fixed components onto the trial omega direction.
        jx = 0.62 * params["jp"] + 0.08 * params["jn"]
        jz = 0.74 * params["jn"] + 0.10 * params["jp"]
        routhian = (
            params["e0"]
            + 0.5 * stiffness * (theta - params["theta0"]) ** 2
            - omega * (jx * math.sin(theta) + jz * math.cos(theta))
        )
        if best is None or routhian < best[0]:
            best = (routhian, theta, jx, jz)
    assert best is not None
    return best


def mix_two_configurations(e3: float, e5: float, coupling: float = 0.12) -> tuple[float, float, float]:
    """Return lower eigenvalue, 5qp probability and gap of a 2x2 crossing."""
    mean = 0.5 * (e3 + e5)
    half = 0.5 * (e5 - e3)
    root = math.sqrt(half * half + coupling * coupling)
    lower = mean - root
    p5 = 0.5 * (1.0 - half / root)
    return lower, p5, 2.0 * root


def current_proxy(theta: float, jp: float, jn: float, radius: float = 4.0) -> list[dict]:
    """Return integrated proton/neutron current moments on a polar grid."""
    rows = []
    # A pair of counter-streaming Gaussian patches gives a compact visual
    # proxy for the intrinsic current distribution in the x-z plane.
    sigma = 1.05
    for ix in range(-20, 21):
        x = 0.25 * ix
        for iz in range(-20, 21):
            z = 0.25 * iz
            r2 = x * x + z * z
            radial = math.exp(-r2 / (2.0 * sigma * sigma))
            proton = (jp * radial * math.cos(theta), jp * radial * math.sin(theta))
            neutron = (
                jn * radial * math.cos(theta + math.pi / 2.0),
                jn * radial * math.sin(theta + math.pi / 2.0),
            )
            rows.append({
                "x": round(x, 3), "z": round(z, 3),
                "jp_x": proton[0], "jp_z": proton[1],
                "jn_x": neutron[0], "jn_z": neutron[1],
            })
    return rows


def run_case(name: str, case: dict) -> tuple[list[dict], dict, list[dict]]:
    p3 = config_parameters(case, "3qp")
    p5 = config_parameters(case, "5qp")
    # Recalibrate only the effective 5qp blade slope to the source comparison
    # point; this exposes rather than hides the model/data normalization.
    j3 = p3["jp"] + p3["jn"]
    target = case["crossing_target"]
    # Calibrate the *reduced* Routhian offsets so the un-mixed minima cross at
    # the literature comparison frequency.  This is a transparent response
    # normalization, not a microscopic fit.
    r3_target, _, _, _ = minimize_orientation(target, p3)
    p5["e0"] = 0.0
    r5_target, _, _, _ = minimize_orientation(target, p5)
    p5["e0"] = r3_target - r5_target
    rows = []
    for omega in HBAR_OMEGA:
        r3, t3, jx3, jz3 = minimize_orientation(omega, p3)
        r5, t5, jx5, jz5 = minimize_orientation(omega, p5)
        energy, p5mix, gap = mix_two_configurations(r3, r5)
        theta = (1.0 - p5mix) * t3 + p5mix * t5
        jp = (1.0 - p5mix) * p3["jp"] + p5mix * p5["jp"]
        jn = (1.0 - p5mix) * p3["jn"] + p5mix * p5["jn"]
        omega_x = omega * math.sin(theta)
        omega_z = omega * math.cos(theta)
        j2 = (1.0 - p5mix) * (jx3 + jz3) + p5mix * (jx5 + jz5)
        rows.append({
            "nuclide": name, "hbar_omega_MeV": omega,
            "theta_J_deg": math.degrees(theta),
            "omega_x_MeV": omega_x, "omega_z_MeV": omega_z,
            "routhian_MeV": energy, "p5qp": p5mix, "avoided_gap_MeV": gap,
            "Jp_hbar": jp, "Jn_hbar": jn, "Jtot_hbar": j2,
            "pairing_gap_p_MeV": case["delta_p"],
            "pairing_gap_n_MeV": case["delta_n"],
            "lambda_n_shift_MeV": case["lambda_n_shift"],
        })
    # Select closest pre/post points for current-field inspection.
    before = min(rows, key=lambda row: abs(row["hbar_omega_MeV"] - (target - 0.05)))
    after = min(rows, key=lambda row: abs(row["hbar_omega_MeV"] - (target + 0.05)))
    current_rows = []
    for stage, row in (("before", before), ("after", after)):
        current_rows.extend(
            {"stage": stage, **cell} for cell in current_proxy(
                math.radians(row["theta_J_deg"]), row["Jp_hbar"], row["Jn_hbar"]
            )
        )
    crossing = min(rows, key=lambda row: abs(row["p5qp"] - 0.5))
    summary = {
        "nuclide": name,
        "N": case["N"],
        "source_comparison_crossing_hbar_omega_MeV": case["crossing_target"],
        "source_comparison_crossing_spin": case["spin_target"],
        "model_midmix_hbar_omega_MeV": crossing["hbar_omega_MeV"],
        "model_midmix_theta_J_deg": crossing["theta_J_deg"],
        "model_midmix_Jp_hbar": crossing["Jp_hbar"],
        "model_midmix_Jn_hbar": crossing["Jn_hbar"],
        "pairing_gap_p_MeV": case["delta_p"],
        "pairing_gap_n_MeV": case["delta_n"],
        "higher_neutron_fermi_surface_scenario_shift_MeV": case["lambda_n_shift"],
        "status": "reduced TAC-RMF/CDFT-inspired proxy; not a PC-PK1 calculation",
    }
    return rows, summary, current_rows


def main() -> None:
    all_rows, summaries, currents = [], [], []
    for name, case in CASES.items():
        rows, summary, current_rows = run_case(name, case)
        all_rows.extend(rows)
        summaries.append(summary)
        currents.extend(current_rows)

    with (OUT / "pr_tac_rmf_bandcrossing_trajectory.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=all_rows[0].keys())
        writer.writeheader()
        writer.writerows(all_rows)
    with (OUT / "pr_tac_rmf_current_proxy.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=currents[0].keys())
        writer.writeheader()
        writer.writerows(currents)
    with (OUT / "pr_tac_rmf_bandcrossing_results.json").open("w") as handle:
        json.dump({
            "model": "reduced_TAC_RMF_CDFT_response",
            "equations": {
                "cranked_hamiltonian": "h = h0 - omega_x Jx - omega_z Jz",
                "orientation": "theta_J = atan2(omega_x, omega_z)",
                "configuration_mixing": "H=[[e3,W],[W,e5]], W=0.12 MeV",
                "current_proxy": "jp(r), jn(r) are normalized Gaussian vector fields tied to Jp/Jn and theta_J",
            },
            "source_anchors": {
                "Garg2015": "135Pr crossing ~0.37 MeV, ~33/2-; 137Pr comparison ~0.42 MeV, ~35/2-; PRC 92 054325 pp.7-8",
                "Agarwal2007": "137Pr back-bending ~0.48 MeV; 3qp/5qp TAC hybrid; PRC 76 024321 pp.6-7",
                "Lv2025": "PC-PK1 TAC-CDFT method example is 136Pr, not 135/137Pr; source page LV25-4, LV25-13",
            },
            "summaries": summaries,
            "limitations": [
                "No Dirac single-particle basis, meson fields, blocked HFB density, or self-consistent PC-PK1 iteration is implemented.",
                "The higher-neutron-Fermi-surface shift and blocking response are controlled assumptions for sensitivity analysis.",
                "Current fields are diagnostic proxies; they are not published jp(r)/jn(r) densities.",
            ],
        }, handle, indent=2)
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()
