#!/usr/bin/env python3
"""Finite-density Coulomb correction to a two-species AMR shears Routhian.

This is a transparent phenomenological diagnostic, not a self-consistent
Hartree-Fock-Bogoliubov calculation.  Proton holes are represented by two
mirror blades at +/- theta_p and neutrons by two mirror blades at +/- theta_n.
The point-charge term e^2/(2 r sin(theta_p)) is regularised by a Gaussian-like
width a: V_C = kappa e^2/sqrt(a^2 + (2 r sin(theta_p))^2).  The a -> 0 limit
recovers the point-particle divergence, whereas any finite orbital density has
a finite direct matrix element.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import numpy as np


E2 = 1.4399764  # MeV fm


def p2(x: np.ndarray) -> np.ndarray:
    return 0.5 * (3.0 * x * x - 1.0)


def solve(omega: float, include_coulomb: bool, pars: dict[str, float]) -> dict[str, float]:
    """Minimise the two-angle Routhian on a 0.25 degree mesh."""
    step = math.radians(pars["grid_step_deg"])
    tp = np.arange(0.0, math.pi / 2.0 + 0.5 * step, step)
    tn = np.arange(0.0, math.pi / 2.0 + 0.5 * step, step)
    pp, nn = np.meshgrid(tp, tn, indexing="ij")
    vpn = pars["V_pn_MeV"] * (p2(np.cos(pp - nn)) + p2(np.cos(pp + nn)))
    vnn = pars["V_nn_MeV"] * p2(np.cos(2.0 * nn))
    distance = 2.0 * pars["radius_fm"] * np.sin(pp)
    vc = 0.0
    if include_coulomb:
        vc = pars["coulomb_scale"] * E2 / np.sqrt(pars["width_fm"] ** 2 + distance**2)
    ip = 2.0 * pars["j_p"] * np.cos(pp)
    inn = 2.0 * pars["j_n"] * np.cos(nn)
    ic = pars["inertia_MeV_inv"] * omega
    angular_momentum = ip + inn + ic
    routhian = vpn + vnn + vc - omega * angular_momentum
    i, j = np.unravel_index(np.argmin(routhian), routhian.shape)
    theta_p = float(pp[i, j])
    theta_n = float(nn[i, j])
    q_p = pars["q_p_eb"] * math.sin(theta_p) ** 2
    q_n = pars["q_n_eb"] * math.sin(theta_n) ** 2
    q_core = math.sqrt(pars["B_core_e2b2"])
    t22 = q_core + q_p + q_n
    mean = 0.5 * (theta_p + theta_n)
    t22_symmetric = q_core + (pars["q_p_eb"] + pars["q_n_eb"]) * math.sin(mean) ** 2
    return {
        "omega_MeV": omega,
        "theta_p_deg": math.degrees(theta_p),
        "theta_n_deg": math.degrees(theta_n),
        "delta_theta_p_minus_n_deg": math.degrees(theta_p - theta_n),
        "mean_theta_deg": math.degrees(mean),
        "I_shears_hbar": ip[i, j] + inn[i, j],
        "I_core_hbar": ic,
        "I_total_hbar": angular_momentum[i, j],
        "V_pn_MeV": float(vpn[i, j]),
        "V_nn_MeV": float(vnn[i, j]),
        "V_coulomb_MeV": float(vc[i, j]) if np.ndim(vc) else float(vc),
        "routhian_MeV": float(routhian[i, j]),
        "T22_eb": t22,
        "T22_symmetric_eb": t22_symmetric,
        "delta_T22_from_asymmetry_eb": t22 - t22_symmetric,
        "B_E2_e2b2": t22**2,
        "B_E2_symmetric_e2b2": t22_symmetric**2,
        "delta_B_E2_from_asymmetry_e2b2": t22**2 - t22_symmetric**2,
    }


def run(pars: dict[str, float]) -> dict[str, object]:
    omegas = np.linspace(pars["omega_min_MeV"], pars["omega_max_MeV"], int(pars["n_omega"]))
    rows: list[dict[str, float]] = []
    for include in (False, True):
        label = "with_coulomb" if include else "no_coulomb"
        for omega in omegas:
            row = solve(float(omega), include, pars)
            row["scenario"] = label
            rows.append(row)
    return {
        "model": "finite-density two-angle AMR shears Routhian",
        "status": "provisional phenomenological diagnostic",
        "equations": {
            "V_coulomb": "kappa*e^2/sqrt(width^2 + (2*r*sin(theta_p))^2)",
            "R": "V_pn + V_nn + V_coulomb - omega*(I_shears + I_core)",
            "I_shears": "2*j_p*cos(theta_p) + 2*j_n*cos(theta_n)",
            "T22": "sqrt(B_core) + q_p*sin(theta_p)^2 + q_n*sin(theta_n)^2",
        },
        "parameters": pars,
        "rows": rows,
        "interpretation": {
            "point_limit": "width -> 0 gives the point-particle divergence at theta_p=0",
            "finite_density": "finite width makes the direct Coulomb matrix element finite",
            "residual_angle": "10-15 deg is a calibrated model output in the chosen omega window, not an established universal constant",
            "B_E2_floor": "the imposed core term is a phenomenological proxy; Coulomb alone is not proven to generate the measured 0.06 e2 b2 floor",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", type=Path, default=Path(__file__).parent)
    args = parser.parse_args()
    pars = {
        "j_p": 4.5,
        "j_n": 5.5,
        "V_pn_MeV": 0.55,
        "V_nn_MeV": 0.50,
        "inertia_MeV_inv": 19.5,
        "radius_fm": 4.6,
        "width_fm": 2.0,
        "coulomb_scale": 1.0,
        "q_p_eb": 0.40,
        "q_n_eb": 0.10,
        "B_core_e2b2": 0.06,
        "omega_min_MeV": 0.20,
        "omega_max_MeV": 1.00,
        "n_omega": 17,
        "grid_step_deg": 0.25,
    }
    args.outdir.mkdir(parents=True, exist_ok=True)
    result = run(pars)
    json_path = args.outdir / "amr_coulomb_blades_results.json"
    csv_path = args.outdir / "amr_coulomb_blades_results.csv"
    json_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    rows = result["rows"]
    fields = list(rows[0].keys())
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(json_path)
    print(csv_path)
    for scenario in ("no_coulomb", "with_coulomb"):
        selected = [r for r in rows if r["scenario"] == scenario]
        print(scenario, "endpoint", selected[-1]["theta_p_deg"], selected[-1]["theta_n_deg"], selected[-1]["B_E2_e2b2"])


if __name__ == "__main__":
    main()
