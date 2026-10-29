#!/usr/bin/env python3
"""Transparent CRMF spatial-current surrogate for magnetic rotation.

This is a two-dimensional, divergence-free linear-response proxy.  It is not a
CRMF solver: no Dirac-Hartree equations, meson propagator, pairing field, or
3-D self-consistent iteration is solved.  The purpose is to make the current
decomposition and its falsifiable diagnostics reproducible.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Nucleus:
    name: str
    jp: float
    jn: float
    g_delta_free: float
    radius: float
    core_susceptibility: float
    core_fraction_low: float
    core_fraction_high: float


NUCLEI = (
    Nucleus("199Pb", 10.0, 9.0, 1.17, 6.8, 0.78, 0.14, 0.26),
    Nucleus("135Pr", 5.5, 5.0, 1.10, 5.6, 0.62, 0.10, 0.20),
)


def gaussian(x: float, z: float, cx: float, cz: float, sigma: float) -> float:
    return math.exp(-((x - cx) ** 2 + (z - cz) ** 2) / (2.0 * sigma * sigma))


def loop_stream(x: float, z: float, cx: float, cz: float, sigma: float, amp: float) -> float:
    """A localized stream function; j=(d psi/dz, -d psi/dx) is divergence free."""
    q = gaussian(x, z, cx, cz, sigma)
    return amp * q


def cylindrical_stream(x: float, z: float, sigma: float, amp: float) -> float:
    """A regularized axisymmetric stream function for the termination limit."""
    r2 = x * x + z * z
    return amp * r2 * math.exp(-r2 / (2.0 * sigma * sigma))


def stream_and_current(
    x: float,
    z: float,
    theta: float,
    omega: float,
    nucleus: Nucleus,
    h: float,
) -> tuple[float, float, float, float, float]:
    """Return valence/core/total (jx,jz) from finite differences of streams."""
    theta_rad = math.radians(theta)
    # The two lobes close as the shears angle closes.  Their signed offsets
    # define a non-axisymmetric current topology at low and intermediate omega.
    separation = 1.18 * math.sin(theta_rad)
    sigma_val = 0.72
    amp = ((0.80 + 0.35 * omega) * math.cos(0.5 * theta_rad)
           * (nucleus.jp + nucleus.jn) / 19.0)
    # At termination, continuously mix the two-lobe field into a cylindrical
    # flow.  This is a diagnostic interpolation, not a claim about a CRMF PES.
    lam = max(0.0, min(1.0, (theta - 8.0) / 62.0))
    psi_val = lambda xx, zz: (
        lam
        * (
            loop_stream(xx, zz, separation, 0.0, sigma_val, amp)
            - loop_stream(xx, zz, -separation, 0.0, sigma_val, amp)
        )
        + (1.0 - lam) * cylindrical_stream(xx, zz, 1.10, 0.68 * amp)
    )
    # Current from the valence stream function.
    jx_v = (psi_val(x, z + h) - psi_val(x, z - h)) / (2.0 * h)
    jz_v = -(psi_val(x + h, z) - psi_val(x - h, z)) / (2.0 * h)

    f_core = nucleus.core_fraction_low + (nucleus.core_fraction_high - nucleus.core_fraction_low) * omega / 0.75
    f_core = max(nucleus.core_fraction_low, min(nucleus.core_fraction_high, f_core))
    # Core counter-flow is a broadened, opposite-sign response.  The factor
    # chi/(1+chi) is the local linear-response saturation of the vector field.
    response = f_core * nucleus.core_susceptibility / (1.0 + nucleus.core_susceptibility)
    sigma_core = 2.0 * sigma_val
    core_stream = lambda xx, zz: -response * (
        lam * (
            loop_stream(xx, zz, separation, 0.0, sigma_core, amp)
            - loop_stream(xx, zz, -separation, 0.0, sigma_core, amp)
        )
        + (1.0 - lam) * cylindrical_stream(xx, zz, 1.55, 0.68 * amp)
    )
    jx_c = (core_stream(x, z + h) - core_stream(x, z - h)) / (2.0 * h)
    jz_c = -(core_stream(x + h, z) - core_stream(x - h, z)) / (2.0 * h)
    # The no-sea approximation used by most practical CDFT calculations does
    # not provide an independently resolved Dirac-sea current.  We retain a
    # small labelled residual here solely as a sensitivity channel; it must
    # never be read as a calculated vacuum-polarization contribution.
    sea_stream = lambda xx, zz: 0.06 * core_stream(xx, zz)
    jx_s = (sea_stream(x, z + h) - sea_stream(x, z - h)) / (2.0 * h)
    jz_s = -(sea_stream(x + h, z) - sea_stream(x - h, z)) / (2.0 * h)
    return jx_v, jz_v, jx_c, jz_c, jx_s, jz_s, f_core


def integrate_fields(nucleus: Nucleus, omega: float, n: int, extent: float):
    h = 2.0 * extent / (n - 1)
    xs = [-extent + i * h for i in range(n)]
    theta = 70.0 - 62.0 * omega / 0.75
    fields = []
    totals = {key: 0.0 for key in ("jval", "jcore", "jsea", "jtotal", "jdirac", "vorticity_abs")}
    circulation_signs = []
    for z in xs:
        for x in xs:
            jx_v, jz_v, jx_c, jz_c, jx_s, jz_s, f_core = stream_and_current(x, z, theta, omega, nucleus, h)
            # The total Dirac current is decomposed into valence, core and a
            # separately labelled proxy for negative-energy anti-polarization.
            jx_t, jz_t = jx_v + jx_c + jx_s, jz_v + jz_c + jz_s
            # curl_y = d jz/dx - d jx/dz, evaluated from total current.
            def total_at(xx, zz):
                a, b, c, d, e, f, _ = stream_and_current(xx, zz, theta, omega, nucleus, h)
                return a + c + e, b + d + f
            jx_xp, jz_xp = total_at(x + h, z)
            jx_xm, jz_xm = total_at(x - h, z)
            jx_zp, jz_zp = total_at(x, z + h)
            jx_zm, jz_zm = total_at(x, z - h)
            vort = (jz_xp - jz_xm) / (2.0 * h) - (jx_zp - jx_zm) / (2.0 * h)
            area = h * h
            l_v = x * jz_v - z * jx_v
            l_c = x * jz_c - z * jx_c
            l_s = x * jz_s - z * jx_s
            l_t = x * jz_t - z * jx_t
            jnorm = math.hypot(jx_t, jz_t)
            totals["jval"] += l_v * area
            totals["jcore"] += l_c * area
            totals["jsea"] += l_s * area
            totals["jtotal"] += l_t * area
            totals["jdirac"] += jnorm * area
            totals["vorticity_abs"] += abs(vort) * area
            circulation_signs.append(1 if vort >= 0.0 else -1)
            fields.append({
                "nucleus": nucleus.name,
                "omega_MeV": round(omega, 6),
                "x_fm": round(x, 6),
                "z_fm": round(z, 6),
                "j_valence_x": jx_v,
                "j_valence_z": jz_v,
                "j_core_x": jx_c,
                "j_core_z": jz_c,
                "j_sea_x_proxy": jx_s,
                "j_sea_z_proxy": jz_s,
                "j_total_x": jx_t,
                "j_total_z": jz_t,
                "vorticity_y": vort,
            })
    # A normalized signed-vorticity index is only a topology diagnostic.
    topology = sum(circulation_signs) / len(circulation_signs)
    I = nucleus.jp + nucleus.jn + 2.0 * omega / 0.75
    theta_rad = math.radians(theta)
    mu_free = nucleus.g_delta_free * nucleus.jp * nucleus.jn / I * math.sin(theta_rad)
    q = 1.0 - (nucleus.core_fraction_low + (nucleus.core_fraction_high - nucleus.core_fraction_low) * omega / 0.75)
    q = max(0.70, min(0.90, q))
    b_free = 3.0 / (8.0 * math.pi) * mu_free * mu_free
    b_eff = b_free * q * q
    summary = {
        "nucleus": nucleus.name,
        "omega_MeV": omega,
        "shears_angle_deg": theta,
        "I_hbar": I,
        "g_delta_free": nucleus.g_delta_free,
        "g_eff_over_g_free": q,
        "quenching_fraction": 1.0 - q,
        "B_M1_free_muN2": b_free,
        "B_M1_eff_muN2": b_eff,
        "B_M1_correction_factor": q * q,
        "J_valence_hbar": totals["jval"],
        "J_core_counter_hbar": totals["jcore"],
        "J_dirac_sea_antipolarization_proxy_hbar": totals["jsea"],
        "J_total_current_hbar": totals["jtotal"],
        "J_dirac_abs_integral": totals["jdirac"],
        "vorticity_abs_integral": totals["vorticity_abs"],
        "topology_signed_vorticity_index": topology,
        "core_fraction_input": f_core,
        "grid_n": n,
        "grid_extent_fm": extent,
    }
    return fields, summary


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--grid", type=int, default=81)
    parser.add_argument("--extent", type=float, default=6.0)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    frequencies = [0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75]
    all_fields: list[dict] = []
    summaries: list[dict] = []
    for nucleus in NUCLEI:
        for omega in frequencies:
            fields, summary = integrate_fields(nucleus, omega, args.grid, args.extent)
            all_fields.extend(fields)
            summaries.append(summary)
    write_csv(args.output / "current_slices.csv", all_fields)
    write_csv(args.output / "crmf_current_summary.csv", summaries)
    manifest = {
        "model": "2D divergence-free Dirac-current linear-response surrogate",
        "generated": "2026-10-29",
        "script": "crmf_dirac_currents.py",
        "nuclei": [n.name for n in NUCLEI],
        "frequencies_MeV": frequencies,
        "grid": {"n": args.grid, "extent_fm": args.extent},
        "equations": {
            "dirac_current": "j_D^i = bar(psi) gamma^i psi",
            "vector_field_proxy": "V_vec = g_omega omega_vec + g_rho tau_3 rho_vec + e A_vec; omega_vec ∝ j_D",
            "core_response": "j_core = -f_core chi/(1+chi) * broadened(j_valence)",
            "m1": "B(M1)=3/(8 pi) [g_delta j_p j_n/I sin(theta)]^2",
            "effective_operator": "B(M1)_eff = (g_eff/g_free)^2 B(M1)_free",
        },
        "interpretation": "Proxy only; not a self-consistent CRMF calculation and not experimental extraction.",
        "files": ["crmf_current_summary.csv", "current_slices.csv", "results.json", "topology_landscape.svg"],
    }
    (args.output / "results.json").write_text(json.dumps({"manifest": manifest, "summary": summaries}, indent=2) + "\n", encoding="utf-8")
    # A dependency-free SVG keeps the plot data inspectable in a browser.
    width, height = 900, 520
    x0, y0, pw, ph = 70, 40, 790, 390
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
             '<rect width="100%" height="100%" fill="white"/>',
             '<text x="70" y="25" font-family="sans-serif" font-size="16">CRMF current proxy: effective g-factor and core counter-flow</text>',
             f'<line x1="{x0}" y1="{y0+ph}" x2="{x0+pw}" y2="{y0+ph}" stroke="black"/>',
             f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+ph}" stroke="black"/>',
             '<text x="420" y="505" font-family="sans-serif" font-size="13">hbar omega (MeV)</text>',
             '<text x="8" y="250" transform="rotate(-90 8 250)" font-family="sans-serif" font-size="13">g_eff/g_free</text>']
    colors = {"199Pb": "#b2182b", "135Pr": "#2166ac"}
    for nucleus in NUCLEI:
        rows = [row for row in summaries if row["nucleus"] == nucleus.name]
        points = []
        for row in rows:
            xx = x0 + pw * (row["omega_MeV"] - 0.15) / 0.60
            yy = y0 + ph * (0.90 - row["g_eff_over_g_free"]) / 0.20
            points.append(f"{xx:.1f},{yy:.1f}")
        lines.append(f'<polyline points="{" ".join(points)}" fill="none" stroke="{colors[nucleus.name]}" stroke-width="3"/>')
        lines.append(f'<text x="{x0+pw-90}" y="{y0+25+(0 if nucleus.name=="199Pb" else 22)}" fill="{colors[nucleus.name]}" font-family="sans-serif" font-size="13">{nucleus.name}</text>')
    lines.append('</svg>')
    (args.output / "topology_landscape.svg").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
