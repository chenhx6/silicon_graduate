#!/usr/bin/env python3
"""Constrained particle-rotor geometry for a planar-to-aplanar transition.

This is a deterministic diagnostic model, not a fit to 106Ag, 106Cd or 198Bi.
It minimizes

    E(I) = sum_k (I_k - j_k)^2 / (2 J_k),       |I| = I,

for j_p=(j_p,0,0), j_n=(0,0,j_n), and J_m > J_s,J_l.  The intermediate-axis
component I_m is the out-of-plane order parameter.  With the stated intrinsic
vectors, R=I-j_p-j_n has R_m=I_m and

    chi_g = j_p . (j_n x R) = -j_p*j_n*I_m.

The two signs of I_m are degenerate in this even-in-phi Hamiltonian.  A
nonzero minimum therefore demonstrates the classical aplanar bifurcation
condition; it does not by itself establish a laboratory chiral doublet.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent


def energy(theta: np.ndarray, phi: np.ndarray, spin: float, jp: float,
           jn: float, Js: float, Jm: float, Jl: float) -> np.ndarray:
    """Particle-rotor energy on the fixed-|I| sphere."""
    Is = spin * np.sin(theta) * np.cos(phi)
    Im = spin * np.sin(theta) * np.sin(phi)
    Il = spin * np.cos(theta)
    return ((Is - jp) ** 2 / (2.0 * Js) + Im ** 2 / (2.0 * Jm)
            + (Il - jn) ** 2 / (2.0 * Jl))


def one_spin(spin: int, theta_grid: np.ndarray, phi_grid: np.ndarray,
             pars: dict[str, float]) -> dict[str, object]:
    jp, jn = pars["jp"], pars["jn"]
    Js, Jm, Jl = pars["Js"], pars["Jm"], pars["Jl"]
    theta, phi = np.meshgrid(theta_grid, phi_grid, indexing="ij")
    e = energy(theta, phi, spin, jp, jn, Js, Jm, Jl)
    i, k = np.unravel_index(np.argmin(e), e.shape)
    th, ph, emin = float(theta[i, k]), float(phi[i, k]), float(e[i, k])

    # The two minima should be equal within the angular grid resolution.
    e_minus = float(e[i, np.argmin(np.abs(phi_grid + abs(ph)))])
    Is = spin * math.sin(th) * math.cos(ph)
    Im = spin * math.sin(th) * math.sin(ph)
    Il = spin * math.cos(th)
    Rm = Im  # j_p and j_n have no intermediate-axis component
    chi = -jp * jn * Rm

    # Numerical curvature at the planar stationary point after minimizing theta.
    # The sign changes at the planar-to-aplanar bifurcation.
    ip = int(np.argmin(np.abs(phi_grid)))
    ep = e[:, ip]
    iphi = min(ip + 1, len(phi_grid) - 1)
    imhi = max(ip - 1, 0)
    dphi = float(phi_grid[iphi] - phi_grid[imhi]) / 2.0
    curvature = float((np.min(e[:, iphi]) - 2.0 * np.min(ep)
                       + np.min(e[:, imhi])) / max(dphi * dphi, 1e-12))

    # Dimensionless magnetic diagnostic: project the intrinsic magnetic vector
    # transverse to I.  It is not a B(M1) value and carries no experimental unit.
    gp, gn = pars["gp"], pars["gn"]
    mu = np.array([gp * jp, 0.0, gn * jn])
    ivec = np.array([Is, Im, Il])
    mu_perp2 = float(np.dot(mu, mu) - (np.dot(mu, ivec) / spin) ** 2)

    return {
        "I": spin,
        "theta_deg": round(math.degrees(th), 6),
        "phi_deg_signed": round(math.degrees(ph), 6),
        "phi_deg_abs": round(abs(math.degrees(ph)), 6),
        "E_min": round(emin, 10),
        "mirror_energy_difference": round(emin - e_minus, 10),
        "I_s": round(Is, 8),
        "I_m": round(Im, 8),
        "I_l": round(Il, 8),
        "R_m": round(Rm, 8),
        "chi_g_signed": round(chi, 8),
        "chi_g_abs": round(abs(chi), 8),
        "planar_phi_curvature": round(curvature, 8),
        "mu_perp2_dimensionless": round(max(mu_perp2, 0.0), 8),
        "mode": "aplanar_chiral_candidate" if abs(ph) > pars["phi_tolerance_rad"]
        else "planar_shears_candidate",
    }


def run() -> None:
    pars = {
        "jp": 5.5,
        "jn": 5.5,
        # Effective moments in hbar^2/MeV.  Chosen only to satisfy Jm>Js,Jl.
        "Js": 10.0,
        "Jm": 30.0,
        "Jl": 15.0,
        "gp": 1.0,
        "gn": 0.0,
        "phi_tolerance_rad": math.radians(1.0),
    }
    spins = list(range(8, 31))
    theta_grid = np.linspace(0.0, math.pi, 721)
    phi_grid = np.linspace(-math.pi / 2.0, math.pi / 2.0, 721)
    rows = [one_spin(i, theta_grid, phi_grid, pars) for i in spins]
    first_aplanar = next((r["I"] for r in rows
                          if r["mode"] == "aplanar_chiral_candidate"), None)
    first_negative_curvature = next((r["I"] for r in rows
                                     if r["planar_phi_curvature"] < 0), None)
    max_mirror_error = max(abs(float(r["mirror_energy_difference"])) for r in rows)

    csv_path = OUT / "transition_scan.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    result = {
        "schema": "chiral-amr-transition/planar-aplanar-fixed-spin/v1",
        "model_role": "deterministic geometry diagnostic; not a fit to any nucleus",
        "equations": {
            "energy": "sum_k (I_k-j_k)^2/(2 J_k), |I|=I",
            "intrinsic_vectors": "j_p=(j_p,0,0), j_n=(0,0,j_n), R=I-j_p-j_n",
            "order_parameter": "I_m=R_m",
            "geometric_chirality": "chi_g=j_p.(j_n x R)=-j_p*j_n*I_m",
            "bifurcation": "J_m>J_s,J_l and the planar phi=0 curvature changes sign",
        },
        "parameters": pars,
        "scan": {
            "spin_range": [spins[0], spins[-1]],
            "theta_points": len(theta_grid),
            "phi_points": len(phi_grid),
            "first_aplanar_grid_spin": first_aplanar,
            "first_negative_planar_curvature_spin": first_negative_curvature,
            "max_left_right_energy_difference": max_mirror_error,
        },
        "interpretation": [
            "At low I the minimum lies at phi=0: the proton and neutron blades and R are coplanar, chi_g=0.",
            "At the grid bifurcation the minimum splits to +/-phi: I_m and chi_g become nonzero, giving two classical handed minima.",
            "The equal mirror energies are imposed by the even-in-phi Hamiltonian; quantum tunnelling, projection, partner-band strengths and experimental feeding are absent.",
            "The dimensionless mu_perp diagnostic is not B(M1), and no numerical row is an experimental value.",
        ],
        "rows": rows,
        "source_premises": [
            "Frauendorf 2001, PDF pp.475-476 and 484-485: PAC/planar/aplanar TAC and laboratory restoration.",
            "Frauendorf 2001, PDF pp.487-488: magnetic and antimagnetic rotation observables.",
            "Frauendorf and Meng 1997, model geometry: chiral aplanar rotation requires a dominant intermediate-axis inertia.",
            "Clark 2000, PDF pp.11-18 and 30-34: shears angle, B(M1) trend, core-rotation/configuration-crossing limits.",
        ],
    }
    json_path = OUT / "transition_scan.json"
    json_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"json": str(json_path), "csv": str(csv_path),
                      "first_aplanar_grid_spin": first_aplanar,
                      "first_negative_planar_curvature_spin": first_negative_curvature,
                      "max_mirror_error": max_mirror_error}, ensure_ascii=False))


if __name__ == "__main__":
    run()
