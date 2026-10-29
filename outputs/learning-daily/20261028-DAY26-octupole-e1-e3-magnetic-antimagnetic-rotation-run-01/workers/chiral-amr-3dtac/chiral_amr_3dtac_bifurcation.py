#!/usr/bin/env python3
"""Minimal four-blade 3D-TAC/Routhian bifurcation diagnostic.

The proton-hole and neutron-particle pairs are represented by their net
shears vectors jp=(jp,0,0), jn=(0,0,jn).  The two members of each pair are
mirror blades, so the ideal AMR transverse magnetic moment cancels.  A
symmetry-preserving *magnitude* of the intermediate-axis cranking component
omega_m enters as -kappa_m omega_m**2 I_m**2/(2 I**2).  This is deliberately
even in I_m: it permits a pitchfork.  A signed external field linear in I_m
would bias one handedness and produce a tilted crossover instead.

This is a classical constrained diagnostic, not a TAC self-consistent
Hartree-Fock calculation and not a fit to 106Ag or 106Cd.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np

OUT = Path(__file__).resolve().parent


def routhian(theta, phi, spin, p):
    Is = spin * np.sin(theta) * np.cos(phi)
    Im = spin * np.sin(theta) * np.sin(phi)
    Il = spin * np.cos(theta)
    base = ((Is - p["jp"]) ** 2 / (2 * p["Js"])
            + Im ** 2 / (2 * p["Jm"])
            + (Il - p["jn"]) ** 2 / (2 * p["Jl"]))
    # omega_m is a symmetric TAC drive magnitude.  The square preserves C.
    drive = -0.5 * p["kappa_drive"] * p["omega_m"] ** 2 * Im ** 2 / spin ** 2
    return base + drive


def observables(theta, phi, spin, p, egrid):
    Is = spin * math.sin(theta) * math.cos(phi)
    Im = spin * math.sin(theta) * math.sin(phi)
    Il = spin * math.cos(theta)
    R = np.array([Is - p["jp"], Im, Il - p["jn"]])
    chi = float(np.dot(np.array([p["jp"], 0.0, 0.0]),
                       np.cross(np.array([0.0, 0.0, p["jn"]]), R)))
    # A geometry-only M1 proxy: it vanishes in the ideal four-blade AMR
    # limit and grows with the out-of-plane order parameter.  Units are not
    # assigned; it is not an experimental B(M1).
    q = abs(Im) / max(spin, 1e-12)
    m1_proxy = p["m1_scale"] * q * q
    # E2 proxy retains a nonzero core contribution after blade closure.
    e2_proxy = p["e2_core"] + p["e2_blade"] * (1.0 - q * q) ** 2
    # Landau barrier and a two-state tunnelling splitting proxy.
    e0 = float(np.min(egrid))
    ep = float(np.min(egrid[:, np.argmin(np.abs(p["phi_grid"]))]))
    barrier = max(ep - e0, 0.0)
    splitting = p["split_prefactor"] * math.exp(-barrier / p["split_scale"])
    return {
        "theta_deg": math.degrees(theta), "phi_deg_signed": math.degrees(phi),
        "phi_deg_abs": abs(math.degrees(phi)), "I_s": Is, "I_m": Im,
        "I_l": Il, "R_m": Im, "chi_g_signed": chi,
        "chi_g_abs": abs(chi), "order_parameter_q": q,
        "B_M1_proxy": m1_proxy, "B_E2_proxy": e2_proxy,
        "partner_splitting_proxy_MeV": splitting,
        "barrier_proxy_MeV": barrier,
    }


def scan_one(spin, omega, p, theta_grid, phi_grid):
    p = dict(p, omega_m=omega, phi_grid=phi_grid)
    th, ph = np.meshgrid(theta_grid, phi_grid, indexing="ij")
    eg = routhian(th, ph, spin, p)
    # Find both signs separately to expose the mirror pair.
    rows = []
    for sign in (-1, 1):
        mask = ph * sign >= -1e-12
        masked = np.where(mask, eg, np.inf)
        i, k = np.unravel_index(np.argmin(masked), masked.shape)
        rows.append(observables(float(th[i, k]), float(ph[i, k]), spin, p, eg))
    planar_k = int(np.argmin(np.abs(phi_grid)))
    ephi = np.min(eg, axis=0)
    dphi = float(phi_grid[1] - phi_grid[0])
    curvature = (ephi[planar_k + 1] - 2 * ephi[planar_k]
                 + ephi[planar_k - 1]) / dphi ** 2
    for row in rows:
        row.update({"I": spin, "omega_m": omega,
                    "planar_phi_curvature_MeV": float(curvature),
                    "mode": "aplanar_chiral_candidate"
                    if row["phi_deg_abs"] > p["phi_tol_deg"]
                    else "planar_AMR_candidate"})
    return rows


def main():
    p = {"jp": 8.0, "jn": 10.0, "Js": 10.0, "Jm": 18.0, "Jl": 14.0,
         "kappa_drive": 44.0, "m1_scale": 1.0, "e2_core": 0.06,
         "e2_blade": 0.22, "split_prefactor": 0.08, "split_scale": 0.08,
         "phi_tol_deg": 1.0}
    theta_grid = np.linspace(0.0, math.pi, 721)
    phi_grid = np.linspace(-math.pi / 2, math.pi / 2, 721)
    spins = [18, 22, 26, 30]
    omegas = np.linspace(0.0, 0.80, 81)
    rows = []
    for spin in spins:
        for omega in omegas:
            rows.extend(scan_one(spin, float(omega), p, theta_grid, phi_grid))
    csv_path = OUT / "bifurcation_scan.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    # One representative branch summary, retaining both mirrors.
    reps = [r for r in rows if r["I"] == 22]
    first = next((r for r in reps if r["mode"] == "aplanar_chiral_candidate"), None)
    mirror = {}
    for r in reps:
        mirror.setdefault(round(r["omega_m"], 5), []).append(r)
    max_mirror_dchi = max(abs(a["chi_g_abs"] - b["chi_g_abs"])
                          for pair in mirror.values() if len(pair) == 2
                          for a, b in [pair])
    result = {"schema": "chiral-amr-3dtac-four-blade/v1",
              "model_role": "symmetry-preserving Routhian diagnostic; not a fit",
              "equations": {
                  "Routhian": "sum_k (I_k-j_k)^2/(2 J_k) - kappa_m omega_m^2 I_m^2/(2 I^2)",
                  "vectors": "j_p=(j_p,0,0), j_n=(0,0,j_n), R=I-j_p-j_n",
                  "chirality": "chi_g=j_p.(j_n x R)=-j_p*j_n*I_m",
                  "pitchfork": "even R(I_m), planar curvature changes sign; +/- I_m degenerate",
                  "M1": "B(M1)_proxy proportional to (I_m/I)^2, geometry only",
              },
              "parameters": {k: v for k, v in p.items() if k != "phi_grid"},
              "scan": {"spins": spins, "omega_m_range": [0.0, 0.80],
                       "theta_points": len(theta_grid), "phi_points": len(phi_grid),
                       "representative_spin": 22,
                       "first_aplanar_row_at_I22": first,
                       "max_mirror_abs_chi_difference": max_mirror_dchi},
              "interpretation": [
                  "At low omega_m the four blades and core vector are planar and the ideal AMR M1 proxy is zero.",
                  "Increasing the symmetric intermediate-axis drive softens the planar curvature and creates equal +/- handed minima.",
                  "The partner splitting and B(M1)/B(E2) values are model proxies; no laboratory transition rate is predicted.",
                  "A signed linear omega_m I_m term would explicitly select one handedness and remove the pitchfork.",
              ],
              "source_premises": [
                  "Frauendorf and Meng 1997; Frauendorf 2001, planar/aplanar TAC geometry.",
                  "Frauendorf 2001, AMR double-shears and transverse magnetic cancellation.",
                  "mr-amr-to-chiral-topological-transition-mechanisms.md, 106Ag candidate/alternative explanation boundary.",
                  "cd110-amr-double-shears-criteria.md, 106Cd-like ideal AMR diagnostics.",
              ]}
    (OUT / "bifurcation_scan.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        import matplotlib.pyplot as plt
        r = [x for x in rows if x["I"] == 22 and x["phi_deg_signed"] >= -1e-8]
        x = [z["omega_m"] for z in r]; y = [z["phi_deg_abs"] for z in r]
        plt.plot(x, y, color="#173f5f", lw=2); plt.xlabel(r"$|\omega_m|$ (MeV/$\hbar$)")
        plt.ylabel(r"$|\phi|$ (deg)"); plt.title("Four-blade 3D-TAC pitchfork diagnostic")
        plt.tight_layout(); plt.savefig(OUT / "bifurcation_diagram.svg"); plt.close()
    except Exception as exc:
        result["plot_warning"] = str(exc)
    print(json.dumps({"csv": str(csv_path), "json": str(OUT / "bifurcation_scan.json"),
                      "first_aplanar_I22": first}, ensure_ascii=False))


if __name__ == "__main__":
    main()
