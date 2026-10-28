#!/usr/bin/env python3
"""Reproducible shears-closure and endpoint-response toy calculations.

This is a transparent classical-angle model.  It is not an EDF/TAC
calculation and does not infer absolute transition strengths for a real
nucleus.  The AMR sin^4 law is the symmetric double-shears model used by Roy
et al.; it is deliberately not assigned to a generic one-blade MR band.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent


def clamp(x: float, lo: float = -1.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, x))


def mr_angle_from_I(I: float, j1: float, j2: float) -> float:
    c = clamp((I * I - j1 * j1 - j2 * j2) / (2.0 * j1 * j2))
    return math.acos(c)


def mr_bm1(I: float, j1: float, j2: float, g1: float, g2: float) -> float:
    """B(M1) in mu_N^2 for the fixed two-blade semiclassical formula."""
    if I == 0:
        return 0.0
    theta = mr_angle_from_I(I, j1, j2)
    mu_perp = (g1 - g2) * j1 * j2 / I * math.sin(theta)
    return 3.0 / (8.0 * math.pi) * mu_perp * mu_perp


def endpoint_power(theta_deg, values):
    """Least-squares slope of log(value) against log(theta) near zero."""
    pts = [(math.log(math.radians(t)), math.log(v))
           for t, v in zip(theta_deg, values) if t > 0 and v > 0]
    xm = sum(x for x, _ in pts) / len(pts)
    ym = sum(y for _, y in pts) / len(pts)
    num = sum((x - xm) * (y - ym) for x, y in pts)
    den = sum((x - xm) ** 2 for x, _ in pts)
    return num / den


def derivative(xs, ys):
    out = []
    for i in range(len(xs)):
        if i == 0:
            out.append((ys[1] - ys[0]) / (xs[1] - xs[0]))
        elif i == len(xs) - 1:
            out.append((ys[-1] - ys[-2]) / (xs[-1] - xs[-2]))
        else:
            out.append((ys[i + 1] - ys[i - 1]) / (xs[i + 1] - xs[i - 1]))
    return out


def closure_cos(omega, omega0=0.20, scale=0.16):
    """Bounded closure trajectory: cos(theta)=1-exp[-(omega-omega0)/scale]."""
    if omega <= omega0:
        return 0.0
    return 1.0 - math.exp(-(omega - omega0) / scale)


def mr_I_from_cos(c, j1=5.5, j2=10.0):
    return math.sqrt(j1 * j1 + j2 * j2 + 2.0 * j1 * j2 * c)


def amr_I_from_cos(c, jp1=4.5, jp2=4.5, jn1=5.5, jn2=5.5):
    # Two equal proton blades are mirror symmetric; the two neutron blades
    # are taken as the axial aligned component.  I(theta) then reaches the
    # four-blade vector-sum maximum at c=1.
    return jn1 + jn2 + (jp1 + jp2) * c


def main():
    # Fixed configuration examples.  Values are deliberately explicit toy
    # inputs, while the endpoint algebra is general.
    mr = dict(j1=5.5, j2=10.0, g1=1.20, g2=-0.20)
    amr = dict(jp1=4.5, jp2=4.5, jn1=5.5, jn2=5.5, qeff=1.10)

    theta_grid = [90.0, 75.0, 60.0, 45.0, 30.0, 15.0, 5.0, 2.0, 1.0, 0.5, 0.0]
    angular_rows = []
    mr_m1 = []
    amr_e2 = []
    for theta in theta_grid:
        t = math.radians(theta)
        c = math.cos(t)
        I_mr = mr_I_from_cos(c, mr["j1"], mr["j2"])
        m1 = mr_bm1(I_mr, **mr)
        # Roy et al. Eq. (1), printed p. 323: symmetric AMR B(E2).
        e2 = 15.0 / (32.0 * math.pi) * amr["qeff"] ** 2 * math.sin(t) ** 4
        mr_m1.append(m1)
        amr_e2.append(e2)
        angular_rows.append({
            "theta_deg": theta,
            "mr_I_hbar": I_mr,
            "mr_BM1_muN2": m1,
            "amr_I_hbar": amr_I_from_cos(c, amr["jp1"], amr["jp2"], amr["jn1"], amr["jn2"]),
            "amr_BE2_e2b2": e2,
            "amr_symmetric_BM1_proxy": 0.0,
            "amr_5pct_blade_asymmetry_M1_proxy": (0.05 * (amr["jp1"] + amr["jp2"]) * math.sin(t)) ** 2,
        })

    # Use small nonzero angles to estimate the endpoint powers.
    small_theta = [4.0, 3.0, 2.0, 1.0, 0.5]
    small_m1 = []
    small_e2 = []
    for theta in small_theta:
        t = math.radians(theta)
        c = math.cos(t)
        I_mr = mr_I_from_cos(c, mr["j1"], mr["j2"])
        small_m1.append(mr_bm1(I_mr, **mr))
        small_e2.append(15.0 / (32.0 * math.pi) * amr["qeff"] ** 2 * math.sin(t) ** 4)

    # Frequency trajectories: stable fixed-configuration closure, a smooth
    # configuration-reopening blend, and an explicitly pathological turnover
    # used only to demonstrate why a negative finite-difference J^(2) is not a
    # generic termination signature.
    omegas = [0.20 + 1.20 * i / 240.0 for i in range(241)]
    I_mr_path = [mr_I_from_cos(closure_cos(w), mr["j1"], mr["j2"]) for w in omegas]
    I_amr_path = [amr_I_from_cos(closure_cos(w), amr["jp1"], amr["jp2"], amr["jn1"], amr["jn2"]) for w in omegas]
    j2_mr = derivative(omegas, I_mr_path)
    j2_amr = derivative(omegas, I_amr_path)

    # Reopening: at omega_c, a new longer proton blade becomes available.
    # This is a mechanism proxy, not a fit to any one nucleus.
    omega_c, width = 0.82, 0.035
    old_jp, new_jp, jn = 5.5, 11.5, 10.0
    reopen_I = []
    turnover_I = []
    for w, base in zip(omegas, I_mr_path):
        blend = 1.0 / (1.0 + math.exp(-(w - omega_c) / width))
        new_c = closure_cos(w, omega0=0.64, scale=0.22)
        new_branch = mr_I_from_cos(new_c, new_jp, jn)
        reopen_I.append((1.0 - blend) * base + blend * new_branch)
        turnover_I.append(base - 0.90 * math.exp(-((w - omega_c) / 0.040) ** 2))
    j2_reopen = derivative(omegas, reopen_I)
    j2_turnover = derivative(omegas, turnover_I)

    trajectory_rows = []
    for i, w in enumerate(omegas):
        trajectory_rows.append({
            "hbar_omega_MeV": w,
            "mr_I_hbar": I_mr_path[i],
            "mr_J2_hbar2_per_MeV": j2_mr[i],
            "amr_I_hbar": I_amr_path[i],
            "amr_J2_hbar2_per_MeV": j2_amr[i],
            "reopening_I_proxy_hbar": reopen_I[i],
            "reopening_J2_proxy_hbar2_per_MeV": j2_reopen[i],
            "turnover_I_reverse_test_hbar": turnover_I[i],
            "turnover_J2_reverse_test_hbar2_per_MeV": j2_turnover[i],
        })

    def extrema(values):
        imin, imax = min(range(len(values)), key=values.__getitem__), max(range(len(values)), key=values.__getitem__)
        return {"min": {"value": values[imin], "hbar_omega_MeV": omegas[imin]},
                "max": {"value": values[imax], "hbar_omega_MeV": omegas[imax]}}

    source_files = [
        "knowledge/sources/clark-2000-shears-mechanism.md",
        "knowledge/sources/afanasjev-1999-termination-rotational-bands.md",
        "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md",
    ]
    hashes = {}
    for rel in source_files:
        p = Path(__file__).resolve().parents[5] / rel
        if p.exists():
            hashes[rel] = hashlib.sha256(p.read_bytes()).hexdigest()

    results = {
        "scope": "classical fixed-configuration angle model plus finite-difference response audit",
        "not_a_claim": ["not an EDF/TAC calculation", "not absolute strengths for a real nucleus", "negative J2 branch is a reverse-test pathology"],
        "literature_locators": {
            "Clark_Macchiavelli_2000": "Annual Review Nucl. Part. Sci. 50, 1-36, PDF pp. 11-18 (shears geometry and B(M1)); pp. 30-34 (core/crossing limits)",
            "Afanasjev_1999": "Phys. Rep. 322, 1-124, PDF pp. 4-7 (fixed-configuration alignment endpoint); pp. 37-40 (J^(2), smooth/unsmooth termination); pp. 43-53 (109Sb benchmark)",
            "Roy_2011": "Phys. Lett. B 694, 322-326, printed pp. 323-326; Eq. (1) on p. 323 gives symmetric-AMR B(E2) proportional to sin^4(theta), Table 1 p. 324 gives 110Cd lifetimes/B(E2), pp. 325-326 discuss core-plus-AMR",
        },
        "classical_endpoints": {
            "MR_Imax_hbar": mr["j1"] + mr["j2"],
            "AMR_Imax_hbar": amr["jp1"] + amr["jp2"] + amr["jn1"] + amr["jn2"],
            "quantum_example": "pi(g9/2)^-2 Jp=8 coupled to nu(h11/2)^2 Jn=10 gives Imax=18 hbar for the frozen finite-j sector; antisymmetry and core coupling matter",
        },
        "endpoint_power_fits": {"MR_BM1_theta_power": endpoint_power(small_theta, small_m1), "AMR_BE2_theta_power": endpoint_power(small_theta, small_e2)},
        "J2_extrema": {"fixed_MR": extrema(j2_mr), "fixed_AMR": extrema(j2_amr), "reopening_proxy": extrema(j2_reopen), "turnover_reverse_test": extrema(j2_turnover)},
        "source_page_hashes": hashes,
    }

    with (OUT / "shears_termination_angular.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=angular_rows[0].keys())
        writer.writeheader(); writer.writerows(angular_rows)
    with (OUT / "shears_termination_trajectory.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=trajectory_rows[0].keys())
        writer.writeheader(); writer.writerows(trajectory_rows)
    (OUT / "shears_termination_results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
