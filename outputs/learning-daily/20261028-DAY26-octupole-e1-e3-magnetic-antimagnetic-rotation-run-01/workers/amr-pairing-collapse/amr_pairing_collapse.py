#!/usr/bin/env python3
"""Conditional cranked-BCS control model for an AMR J^(2) anomaly.

This is a transparent mechanism model, not a 110Cd/104Pd mass-fit or a
projected PNC-CSM calculation.  Two proton-hole and two neutron-particle
quasiparticles are treated as blocked; the remaining active pair levels are
solved with a finite-temperature cranked-BCS gap equation.  A smooth response
kernel maps the loss of pair stiffness into a core inertia, so that the
resulting J^(2) peak can be compared with the direct/derived experimental
ledger without pretending that the mapping is a microscopic prediction.

Only the Python standard library is required.
"""

from __future__ import annotations

import csv
import json
import math
from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Species:
    name: str
    xi_mev: tuple[float, ...]
    jx_hbar: tuple[float, ...]
    pair_strength_mev: float
    blocked_configuration: str


PROTON = Species(
    "proton",
    (0.18, 0.28, 0.40, 0.58),
    (0.45, 0.65, 0.85, 1.00),
    0.24,
    "two pi-g9/2 holes blocked outside the residual pair reservoir",
)
NEUTRON = Species(
    "neutron",
    (0.22, 0.32, 0.42, 0.62),
    (0.50, 0.70, 0.90, 1.10),
    0.25,
    "two nu-h11/2 particles blocked outside the residual pair reservoir",
)

TEMPERATURE_MEV = 0.030
LAMBDA_MEV = 0.0
J_CORE_SUPERFLUID = 19.5
J_CORE_RIGID = 45.0
OMEGA_TRANSITION = 0.50
# The gap equation identifies the mean-field collapse centre.  The core
# susceptibility softens earlier and spreads over a finite interval, so its
# response centre is a separate phenomenological control parameter.
CORE_RESPONSE_CENTER = 0.40
TRANSITION_WIDTH = 0.120
J_PI = 4.5
OMEGA_SHEARS = 0.82


def fermi(argument_mev: float, temperature_mev: float) -> float:
    """Stable Fermi function f(E/T), with the sign convention f(x)=1/(1+e^x)."""
    scaled = max(-700.0, min(700.0, argument_mev / temperature_mev))
    return 1.0 / (1.0 + math.exp(scaled))


def solve_gap(species: Species, omega: float, tolerance: float = 1.0e-11) -> dict:
    """Solve Delta = G Delta sum_k F_k/(2 E_k) at fixed lambda.

    F_k=1-f(E_k-hbar*omega*j_x)-f(E_k+hbar*omega*j_x) is the cranked
    pair-survival factor.  The active levels are the residual levels after the
    explicitly listed blocked four-quasiparticle configuration.  Lambda is
    held fixed so this small control model isolates the gap response; a full
    particle-number-conserving calculation would solve lambda and the blocked
    occupations self-consistently in the same truncated space.
    """
    delta = 0.20
    converged = False
    iterations = 0
    for iterations in range(1, 2001):
        susceptibility = 0.0
        pair_factor_sum = 0.0
        quasiparticles = []
        for xi, jx in zip(species.xi_mev, species.jx_hbar):
            shifted = xi - LAMBDA_MEV
            energy = max(1.0e-12, math.sqrt(shifted * shifted + delta * delta))
            f_plus = fermi(energy - omega * jx, TEMPERATURE_MEV)
            f_minus = fermi(energy + omega * jx, TEMPERATURE_MEV)
            pair_factor = 1.0 - f_plus - f_minus
            susceptibility += pair_factor / (2.0 * energy)
            pair_factor_sum += pair_factor
            quasiparticles.append(
                {
                    "xi_MeV": xi,
                    "jx_hbar": jx,
                    "E_MeV": energy,
                    "pair_survival_factor": pair_factor,
                    "f_plus": f_plus,
                    "f_minus": f_minus,
                }
            )
        delta_new = max(0.0, species.pair_strength_mev * delta * susceptibility)
        delta_next = 0.5 * (delta + delta_new)
        if abs(delta_next - delta) < tolerance:
            delta = delta_next
            converged = True
            break
        delta = delta_next

    return {
        "species": species.name,
        "omega_MeV_per_hbar": omega,
        "Delta_MeV": delta,
        "gap_equation_residual_MeV": delta - delta_new,
        "pair_susceptibility_per_MeV": susceptibility,
        "sum_pair_survival": pair_factor_sum,
        "iterations": iterations,
        "converged": converged,
        "blocked_configuration": species.blocked_configuration,
        "active_level_count": len(species.xi_mev),
        "quasiparticles": quasiparticles,
    }


def logistic(argument: float) -> float:
    clipped = max(-700.0, min(700.0, argument))
    return 1.0 / (1.0 + math.exp(-clipped))


def pairing_stiffness(omega: float) -> float:
    """Finite-response bridge: one at low frequency, zero after pair collapse."""
    return 1.0 - logistic((omega - CORE_RESPONSE_CENTER) / TRANSITION_WIDTH)


def core_inertia_with_pairing(omega: float) -> float:
    stiffness = pairing_stiffness(omega)
    return J_CORE_RIGID - (J_CORE_RIGID - J_CORE_SUPERFLUID) * stiffness


def total_spin(omega: float, with_pairing: bool) -> float:
    """Minimal AMR spin: two shears plus a frequency-dependent core response."""
    shear_spin = 12.0 + 2.0 * J_PI * omega / OMEGA_SHEARS
    core = core_inertia_with_pairing(omega) if with_pairing else J_CORE_RIGID
    return shear_spin + core * omega


def finite_difference(values: list[float], grid: list[float]) -> list[float]:
    result: list[float] = []
    for index in range(len(values)):
        if index == 0:
            result.append((values[1] - values[0]) / (grid[1] - grid[0]))
        elif index == len(values) - 1:
            result.append((values[-1] - values[-2]) / (grid[-1] - grid[-2]))
        else:
            result.append((values[index + 1] - values[index - 1]) /
                          (grid[index + 1] - grid[index - 1]))
    return result


def experimental_ledger() -> list[dict]:
    """Source-ledger values; J2 proxy is 4/delta-E_gamma and is conditional."""
    rows: list[dict] = []
    roy = [
        (16, 1075.0, 0.36, 0.14),
        (18, 1224.0, 0.23, 0.12),
        (20, 1323.0, 0.17, 0.11),
        (22, 1314.0, 0.21, 0.09),
        (24, 1358.0, 0.27, 0.06),
    ]
    for spin, energy, lifetime, be2 in roy:
        rows.append(
            {
                "nucleus": "110Cd",
                "source": "Roy2011 Table 1, p.324",
                "spin_hbar": spin,
                "Egamma_keV": energy,
                "omega_MeV_per_hbar": energy / 2000.0,
                "lifetime_ps": lifetime,
                "B_E2_e2b2": be2,
                "J2_proxy_hbar2_per_MeV": None,
                "status": "direct lifetime and B(E2); no direct J2 table",
            }
        )
    for index in range(len(roy) - 1):
        spin0, eg0, _, be20 = roy[index]
        spin1, eg1, _, be21 = roy[index + 1]
        delta_e = eg1 - eg0
        rows.append(
            {
                "nucleus": "110Cd",
                "source": "derived from Roy2011 Table 1 E_gamma",
                "spin_hbar": f"{spin0}-{spin1}",
                "Egamma_keV": f"{eg0}->{eg1}",
                "omega_MeV_per_hbar": (eg0 + eg1) / 4000.0,
                "lifetime_ps": None,
                "B_E2_e2b2": (be20 + be21) / 2.0,
                "J2_proxy_hbar2_per_MeV": 4.0 / delta_e if delta_e else None,
                "status": "conditional finite difference; negative value is retained",
            }
        )
    pd_points = [
        (16, 0.26, 112.3),
        (18, 0.22, 140.9),
        (20, 0.19, 334.2),
        (22, 0.13, 282.3),
        (24, 0.07, 554.3),
    ]
    for spin, be2, ratio in pd_points:
        rows.append(
            {
                "nucleus": "104Pd",
                "source": "Rather2014 Table 1, p.10",
                "spin_hbar": spin,
                "Egamma_keV": None,
                "omega_MeV_per_hbar": None,
                "lifetime_ps": None,
                "B_E2_e2b2": be2,
                "J2_proxy_hbar2_per_MeV": be2 * ratio,
                "status": "derived from reported J2/B(E2), not an independent J2 measurement",
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_svg(output_path: Path, rows: list[dict]) -> None:
    """Write a dependency-free SVG showing gap and J2 control curves."""
    width, height = 960, 520
    left, right, top, bottom = 70, 30, 30, 70
    x0, x1 = 0.0, 0.8
    y0, y1 = 0.0, 100.0

    def sx(value: float) -> float:
        return left + (value - x0) / (x1 - x0) * (width - left - right)

    def sy(value: float) -> float:
        return height - bottom - (value - y0) / (y1 - y0) * (height - top - bottom)

    def path(points: list[tuple[float, float]], colour: str, width_px: float = 2.5) -> str:
        commands = " ".join(("M" if i == 0 else "L") + f" {sx(x):.2f},{sy(y):.2f}"
                             for i, (x, y) in enumerate(points))
        return f'<path d="{commands}" fill="none" stroke="{colour}" stroke-width="{width_px}"/>'

    gap_p = [(row["omega_MeV_per_hbar"], row["Delta_p_MeV"]) for row in rows]
    gap_n = [(row["omega_MeV_per_hbar"], row["Delta_n_MeV"]) for row in rows]
    j_pair = [(row["omega_MeV_per_hbar"], min(y1, row["J2_pairing_hbar2_per_MeV"])) for row in rows]
    j_none = [(row["omega_MeV_per_hbar"], min(y1, row["J2_no_pairing_hbar2_per_MeV"])) for row in rows]
    body = [
        f'<rect width="{width}" height="{height}" fill="white"/>',
        f'<line x1="{left}" y1="{height-bottom}" x2="{width-right}" y2="{height-bottom}" stroke="black"/>',
        f'<line x1="{left}" y1="{top}" x2="{left}" y2="{height-bottom}" stroke="black"/>',
        path(gap_p, "#1f77b4"), path(gap_n, "#2ca02c"),
        path(j_pair, "#d62728"), path(j_none, "#7f7f7f", 2.0),
        f'<line x1="{sx(OMEGA_TRANSITION):.2f}" y1="{top}" x2="{sx(OMEGA_TRANSITION):.2f}" y2="{height-bottom}" stroke="#aa0000" stroke-dasharray="5,5"/>',
        '<text x="70" y="20" font-family="sans-serif" font-size="16">AMR pairing control model</text>',
        f'<text x="{width/2-70:.0f}" y="{height-20}" font-family="sans-serif" font-size="13">hbar omega (MeV)</text>',
        '<text x="78" y="45" font-family="sans-serif" font-size="12" fill="#1f77b4">Delta_p</text>',
        '<text x="140" y="45" font-family="sans-serif" font-size="12" fill="#2ca02c">Delta_n</text>',
        '<text x="205" y="45" font-family="sans-serif" font-size="12" fill="#d62728">J2 paired</text>',
        '<text x="285" y="45" font-family="sans-serif" font-size="12" fill="#7f7f7f">J2 no-pair</text>',
        '<text x="540" y="45" font-family="sans-serif" font-size="12" fill="#aa0000">transition center</text>',
    ]
    path_data = "\n".join(body)
    output_path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">\n{path_data}\n</svg>\n', encoding="utf-8")


def main() -> None:
    grid = [round(0.01 * index, 4) for index in range(81)]
    gap_rows: list[dict] = []
    for omega in grid:
        proton = solve_gap(PROTON, omega)
        neutron = solve_gap(NEUTRON, omega)
        gap_rows.append(
            {
                "omega_MeV_per_hbar": omega,
                "Delta_p_MeV": proton["Delta_MeV"],
                "Delta_n_MeV": neutron["Delta_MeV"],
                "pair_stiffness_response": pairing_stiffness(omega),
                "J_core_pairing_hbar2_per_MeV": core_inertia_with_pairing(omega),
                "J_core_no_pairing_hbar2_per_MeV": J_CORE_RIGID,
                "blocked_proton_count": 2,
                "blocked_neutron_count": 2,
                "gap_converged_p": proton["converged"],
                "gap_converged_n": neutron["converged"],
            }
        )

    spins_pair = [total_spin(omega, True) for omega in grid]
    spins_none = [total_spin(omega, False) for omega in grid]
    j2_pair = finite_difference(spins_pair, grid)
    j2_none = finite_difference(spins_none, grid)
    curve_rows: list[dict] = []
    for row, ip, inn, jp, jn in zip(gap_rows, spins_pair, spins_none, j2_pair, j2_none):
        curve_rows.append(
            {
                **row,
                "I_pairing_hbar": ip,
                "I_no_pairing_hbar": inn,
                "J2_pairing_hbar2_per_MeV": jp,
                "J2_no_pairing_hbar2_per_MeV": jn,
            }
        )

    ledger = experimental_ledger()
    write_csv(OUT / "pairing_gap_scan.csv", gap_rows)
    write_csv(OUT / "j2_curve.csv", curve_rows)
    write_csv(OUT / "experimental_ledger.csv", ledger)
    write_svg(OUT / "pairing_j2_control.svg", curve_rows)

    peak = max(curve_rows, key=lambda row: row["J2_pairing_hbar2_per_MeV"])
    roy_direct = [row for row in ledger if row["nucleus"] == "110Cd" and row["J2_proxy_hbar2_per_MeV"] is not None]
    pd_peak = max(row["J2_proxy_hbar2_per_MeV"] for row in ledger if row["nucleus"] == "104Pd")
    results = {
        "status": "conditional-mechanism-model-with-evidence-ledger",
        "units": {"omega": "MeV/hbar", "gap": "MeV", "spin": "hbar", "inertia": "hbar^2/MeV"},
        "equations": {
            "cranked_quasiparticle": "E_k=sqrt((xi_k-lambda)^2+Delta^2)",
            "pair_survival": "F_k=1-f(E_k-omega*jx_k)-f(E_k+omega*jx_k)",
            "self_consistent_gap": "Delta=G*Delta*sum_k[F_k/(2*E_k)]",
            "spin": "I(omega)=I_shears(omega)+J_core(omega)*omega",
            "dynamic_inertia": "J2=dI/domega",
            "core_response": "J_core=45-(45-19.5)*S_pair(omega), S_pair=1/(1+exp((omega-0.40)/0.12))",
        },
        "blocked_configuration": {
            "protons": PROTON.blocked_configuration,
            "neutrons": NEUTRON.blocked_configuration,
            "interpretation": "The active levels are a residual pair reservoir; this is not a full blocked HFB/PNC wave function.",
        },
        "parameters": {
            "G_p_MeV": PROTON.pair_strength_mev,
            "G_n_MeV": NEUTRON.pair_strength_mev,
            "lambda_MeV": LAMBDA_MEV,
            "temperature_smearing_MeV": TEMPERATURE_MEV,
            "J_core_superfluid_hbar2_per_MeV": J_CORE_SUPERFLUID,
            "J_core_rigid_hbar2_per_MeV": J_CORE_RIGID,
            "transition_center_MeV_per_hbar": OMEGA_TRANSITION,
            "core_response_center_MeV_per_hbar": CORE_RESPONSE_CENTER,
            "transition_width_MeV_per_hbar": TRANSITION_WIDTH,
        },
        "model_outputs": {
            "pairing_curve_peak_J2_hbar2_per_MeV": peak["J2_pairing_hbar2_per_MeV"],
            "pairing_curve_peak_omega_MeV_per_hbar": peak["omega_MeV_per_hbar"],
            "no_pairing_J2_range_hbar2_per_MeV": [min(j2_none), max(j2_none)],
            "fully_collapsed_core_limit_hbar2_per_MeV": J_CORE_RIGID,
            "Roy_core_fit_hbar2_per_MeV": J_CORE_SUPERFLUID,
            "Rather_104Pd_derived_J2_peak_hbar2_per_MeV": pd_peak,
        },
        "evidence_boundaries": {
            "110Cd": "Roy2011 Table 1 directly gives tau and B(E2), not a J2 table. Its E_gamma finite differences contain a negative 20-22 proxy and do not independently establish a 60-70 peak.",
            "104Pd": "Rather2014 Table 1 reports J2/B(E2); multiplying by B(E2) gives a derived maximum about 63.5 hbar^2/MeV at I=20.",
            "pairing": "Zhang2013/2019 support frequency-dependent PNC pairing, blocking and occupation rearrangement, but neither measures a Delta(omega) collapse in 110Cd.",
            "causality": "The J2 peak follows here only after an explicit finite-response mapping from pair stiffness to J_core; it is a falsifiable mechanism control, not source-reported attribution.",
        },
        "roy_110cd_derived_rows": roy_direct,
    }
    (OUT / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
