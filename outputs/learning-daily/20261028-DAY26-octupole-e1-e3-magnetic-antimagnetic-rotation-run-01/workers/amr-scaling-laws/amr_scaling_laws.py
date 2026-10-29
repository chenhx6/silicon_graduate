#!/usr/bin/env python3
"""Reproducible AMR critical-frequency scaling and shell-modulation scan.

The script deliberately separates the phenomenological model from experiment.
The isotope table is a candidate pool; an experimental field is populated only
when the local evidence ledger gives a traceable band value.  No external
packages are required.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


OUT = Path(__file__).resolve().parent
DATE = "2026-10-29"


def isotope(z: int, a: int, band: str, configuration: str, j_pi: float,
            j_nu: float, core_inertia: float, n_blades: int,
            evidence_status: str = "candidate-no-direct-AMR-ledger",
            source: str = "none") -> dict:
    return {
        "nucleus": f"{a}{element(z)}",
        "A": a,
        "Z": z,
        "N": a - z,
        "band": band,
        "configuration": configuration,
        "j_pi_hbar": j_pi,
        "j_nu_hbar": j_nu,
        "core_inertia_hbar2_per_MeV": core_inertia,
        "proton_blade_count": n_blades,
        "evidence_status": evidence_status,
        "evidence_source": source,
        "observed_bandhead_I0_hbar": None,
        "observed_termination_Iterm_hbar": None,
        "observed_Egamma_max_keV": None,
        "observed_omega_proxy_MeV": None,
    }


ELEMENTS = {
    46: "Pd", 48: "Cd", 49: "In", 64: "Gd", 44: "Ru",
}


def element(z: int) -> str:
    return ELEMENTS[z]


def candidate_pool() -> list[dict]:
    rows: list[dict] = []
    # Pd: odd-A entries use an effective four-hole proton blade; even-A
    # entries use the two-hole particle-plus-rotor reference configuration.
    for a in range(101, 111):
        n = a - 46
        odd = n % 2
        rows.append(isotope(
            46, a,
            "Pd AMR candidate" if a in (101, 103, 104, 105) else "Pd high-spin candidate",
            ("pi(g9/2)^-4 x nu(h11/2)(gd)^2" if odd else
             "pi(g9/2)^-2 x nu[h11/2^2(g7/2,d5/2)^2]"),
            8.5 if odd else 4.5,
            5.5 if odd else (16.0 if a == 104 else 10.0),
            5.0 if n >= 58 else 2.5,
            4 if odd else 2,
            "direct-AMR" if a == 104 else
            ("review-candidate" if a in (101, 102, 103, 105) else
             "review-scope-no-AMR-closure"),
            "rather-2014-104pd-antimagnetic-arxiv-full" if a == 104 else
            "kumar-2023-amr-review" if a <= 105 else
            "kumar-2023-amr-review",
        ))

    # Cd: Roy et al. provide the calibrated even-even chain; odd-A entries
    # retain an explicit blocking label and no invented observables.
    for a in range(106, 111):
        n = a - 48
        odd = n % 2
        if a == 106:
            j_nu, inertia = 18.0, 0.0
        elif a == 108:
            j_nu, inertia = 16.0, 0.0
        elif a == 110:
            j_nu, inertia = 10.0, 19.5
        else:
            j_nu, inertia = 12.0, 9.75
        rows.append(isotope(
            48, a, "Cd AMR candidate",
            "pi(g9/2)^-2 x nu[h11/2^2(g7/2,d5/2)^2]" if not odd else
            "pi(g9/2)^-2 x nu[h11/2(g7/2,d5/2)^2] (blocked)",
            4.5, j_nu, inertia, 2,
            "direct-AMR" if a in (106, 108, 110) else "review-candidate",
            "roy-2011-cd110-systematics-antimagnetic" if a in (106, 108, 110)
            else "roy-2013-105cd-amr-comment-metadata",
        ))

    # In: Chiara et al. report shears-band lifetime work for 108,110In;
    # the other nearby nuclei are retained as candidates with null observables.
    for a in range(108, 112):
        n = a - 49
        rows.append(isotope(
            49, a, "In shears/AMR candidate",
            "pi(g9/2)^-1 x nu(h11/2)^2(g7/2,d5/2)^n",
            4.5, 10.0 if n % 2 == 0 else 5.5, 5.0, 2,
            "lifetime-source-candidate" if a in (108, 110) else
            "candidate-no-direct-AMR-ledger",
            "chiara-2001-108-110in-shears-band-lifetimes" if a in (108, 110)
            else "kumar-2023-amr-review",
        ))

    # Gd entries are a control/candidate pool.  No local source in this run
    # establishes the requested AMR band systematics, so model outputs remain
    # explicitly unvalidated probes.
    for a in range(142, 147):
        rows.append(isotope(
            64, a, "Gd cross-mass probe (unassigned AMR)",
            "not assigned; high-j particle-hole probe only",
            6.5, 10.0, 25.0, 2,
            "cross-mass-probe-no-AMR-closure",
            "kumar-2023-amr-review",
        ))

    # A Ru control pair makes the phase-map boundary explicit without using it
    # as evidence for AMR.
    for a in (100, 101):
        rows.append(isotope(
            44, a, "Ru control candidate", "control; no assigned AMR blade",
            4.5, 5.5, 12.0, 2, "control-no-AMR-closure", "none",
        ))
    return rows


def model_constants() -> dict:
    # Calibrate the volume scale to the Roy/Rather effective value at 110Cd.
    a_ref, z_ref, v_ref, kappa = 110, 48, 1.2, 1.0
    delta_ref = (a_ref - 2 * z_ref) / a_ref
    v0 = v_ref * a_ref ** (1.0 / 3.0) / (1.0 - kappa * delta_ref ** 2)
    return {
        "V0_MeV": v0,
        "kappa_isospin": kappa,
        "reference": "110Cd, V_pinu=1.2 MeV from Roy 2011 model input",
        "shell_amplitude": 0.12,
        "shell_window_N_min": 56,
        "shell_window_N_max": 66,
    }


def h11_2_occupancy(n: int) -> float:
    return max(0.0, min(1.0, (n - 56.0) / 10.0))


def calculate(row: dict, constants: dict) -> dict:
    a, z, n = row["A"], row["Z"], row["N"]
    asym = (n - z) / a
    v_baseline = constants["V0_MeV"] * a ** (-1.0 / 3.0) * (
        1.0 - constants["kappa_isospin"] * asym ** 2
    )
    occ = h11_2_occupancy(n)
    # This is a separately reported phenomenological shell proxy, not part of
    # the prescribed volume/isospin law. It peaks at mid filling (N=61).
    shell_factor = 1.0 + constants["shell_amplitude"] * math.sin(math.pi * occ)
    v_shell = v_baseline * shell_factor
    omega_baseline = 3.0 * v_baseline / (2.0 * row["j_pi_hbar"])
    omega_shell = 3.0 * v_shell / (2.0 * row["j_pi_hbar"])
    i_close_baseline = row["j_nu_hbar"] + 2.0 * row["j_pi_hbar"] + row[
        "core_inertia_hbar2_per_MeV"
    ] * omega_baseline
    i_close_shell = row["j_nu_hbar"] + 2.0 * row["j_pi_hbar"] + row[
        "core_inertia_hbar2_per_MeV"
    ] * omega_shell
    result = dict(row)
    result.update({
        "asymmetry_delta": asym,
        "h11_2_occupancy_proxy": occ,
        "shell_factor_proxy": shell_factor,
        "V_pinu_baseline_MeV": v_baseline,
        "V_pinu_shell_MeV": v_shell,
        "hbar_omega_c_baseline_MeV": omega_baseline,
        "hbar_omega_c_shell_MeV": omega_shell,
        "I_close_baseline_hbar": i_close_baseline,
        "I_close_shell_hbar": i_close_shell,
        "theory_minus_observed_Iterm_baseline": (
            i_close_baseline - row["observed_termination_Iterm_hbar"]
            if row["observed_termination_Iterm_hbar"] is not None else None
        ),
        "theory_minus_observed_Iterm_shell": (
            i_close_shell - row["observed_termination_Iterm_hbar"]
            if row["observed_termination_Iterm_hbar"] is not None else None
        ),
    })
    if row["observed_Egamma_max_keV"] is not None:
        result["observed_omega_proxy_MeV"] = row["observed_Egamma_max_keV"] / 2000.0
        result["omega_proxy_minus_theory_shell_MeV"] = (
            result["observed_omega_proxy_MeV"] - omega_shell
        )
    else:
        result["omega_proxy_minus_theory_shell_MeV"] = None
    return result


def add_experimental_ledger(rows: list[dict]) -> None:
    values = {
        "104Pd": (16.0, 26.0, None,
                  "Rather 2014, Table 1: I=16-26; E_gamma maximum not "
                  "re-digitized in this run"),
        "106Cd": (18.0, 24.0, 1675.5,
                  "Roy 2011, p.324 Table 1 and 106Cd comparison"),
        "108Cd": (16.0, 24.0, 1469.0,
                  "Roy 2011, p.324 Table 1 and 108Cd comparison"),
        "110Cd": (16.0, 24.0, 1358.0,
                  "Roy 2011, p.324 Table 1; 26+/28+ top is effective"),
    }
    for row in rows:
        if row["nucleus"] in values:
            i0, iterm, egamma, locator = values[row["nucleus"]]
            row["observed_bandhead_I0_hbar"] = i0
            row["observed_termination_Iterm_hbar"] = iterm
            row["observed_Egamma_max_keV"] = egamma
            row["experimental_locator"] = locator
        else:
            row["experimental_locator"] = "No direct bandhead/termination/E_gamma ledger in this run"


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = list(rows[0])
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def phase_map(constants: dict) -> list[dict]:
    points = []
    for a in range(80, 221, 2):
        for n in range(40, 121, 2):
            z = a - n
            if z < 20 or z > 100:
                continue
            delta = (n - z) / a
            v = constants["V0_MeV"] * a ** (-1.0 / 3.0) * (
                1.0 - constants["kappa_isospin"] * delta ** 2
            )
            occ = h11_2_occupancy(n)
            shell = 1.0 + constants["shell_amplitude"] * math.sin(math.pi * occ)
            points.append({
                "A": a, "N": n, "Z": z, "delta": delta,
                "V_pinu_baseline_MeV": v,
                "V_pinu_shell_MeV": v * shell,
                "omega_c_baseline_MeV_for_jpi4p5": 3.0 * v / 9.0,
                "omega_c_shell_MeV_for_jpi4p5": 3.0 * v * shell / 9.0,
                "h11_2_occupancy_proxy": occ,
                "shell_factor_proxy": shell,
            })
    return points


def write_svg(path: Path, points: list[dict]) -> None:
    width, height = 900, 430
    margin = 55
    # Plot only the smooth N=constant midline as a compact chart-data view.
    line = [p for p in points if p["Z"] == p["A"] - 60 and 80 <= p["A"] <= 220]
    line.sort(key=lambda p: p["A"])
    x_min, x_max = 80, 220
    y_values = [p["omega_c_shell_MeV_for_jpi4p5"] for p in line]
    y_min, y_max = min(y_values), max(y_values)
    def xy(a: float, y: float) -> tuple[float, float]:
        x = margin + (a - x_min) / (x_max - x_min) * (width - 2 * margin)
        yy = height - margin - (y - y_min) / (y_max - y_min) * (height - 2 * margin)
        return x, yy
    path_data = " ".join(
        ("M" if i == 0 else "L") + f" {xy(p['A'], p['omega_c_shell_MeV_for_jpi4p5'])[0]:.2f},"
        f"{xy(p['A'], p['omega_c_shell_MeV_for_jpi4p5'])[1]:.2f}"
        for i, p in enumerate(line)
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<title>AMR shell-modulated critical frequency proxy at N=60</title>
<rect width="100%" height="100%" fill="white"/>
<line x1="{margin}" y1="{height-margin}" x2="{width-margin}" y2="{height-margin}" stroke="black"/>
<line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height-margin}" stroke="black"/>
<path d="{path_data}" fill="none" stroke="#174a7e" stroke-width="2"/>
<text x="{width/2-150}" y="25" font-family="sans-serif" font-size="16">AMR ωc proxy, jπ=4.5ℏ, N=60</text>
<text x="{width/2-40}" y="{height-8}" font-family="sans-serif" font-size="13">A</text>
<text x="8" y="{height/2}" transform="rotate(-90 8,{height/2})" font-family="sans-serif" font-size="13">ℏωc (MeV)</text>
</svg>
'''
    path.write_text(svg.rstrip() + "\n", encoding="utf-8")


def main() -> None:
    constants = model_constants()
    rows = candidate_pool()
    add_experimental_ledger(rows)
    calculated = [calculate(row, constants) for row in rows]
    phase = phase_map(constants)
    write_csv(OUT / "amr_isotope_systematics.csv", calculated)
    write_csv(OUT / "amr_scaling_phase_map.csv", phase)
    write_svg(OUT / "amr_scaling_phase_map.svg", phase)
    payload = {
        "schema_version": "amr-scaling-laws/v1",
        "generated": DATE,
        "model": {
            "equations": {
                "shears_closing": "cos(theta)=omega/omega_c",
                "critical_frequency": "hbar*omega_c=3*V_pinu/(2*j_pi)",
                "volume_isospin_scaling": "V_pinu=V0*A^(-1/3)*(1-kappa*((N-Z)/A)^2)",
                "closure_spin": "I_c=j_nu+2*j_pi+J_core*omega_c",
            },
            "constants": constants,
            "caveat": "Shell factor is a separate phenomenological proxy; it is not fitted to an AMR dataset.",
        },
        "candidate_count": len(calculated),
        "direct_experimental_rows": sum(r["evidence_status"] == "direct-AMR" for r in calculated),
        "candidate_rows": calculated,
        "phase_map_points": len(phase),
        "outputs": [
            "amr_isotope_systematics.csv",
            "amr_scaling_phase_map.csv",
            "amr_scaling_phase_map.svg",
        ],
    }
    (OUT / "amr_scaling_laws_results.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(json.dumps({"candidate_count": len(calculated), "phase_map_points": len(phase)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
