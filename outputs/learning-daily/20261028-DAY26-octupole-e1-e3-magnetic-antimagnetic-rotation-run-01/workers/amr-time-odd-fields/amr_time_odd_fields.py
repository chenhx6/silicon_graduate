#!/usr/bin/env python3
"""Reduced-unit CRMF time-odd-field and AMR four-blade diagnostic.

This is a transparent proxy, not a self-consistent CRMF solver.  It solves a
two-dimensional Yukawa response for local Dirac currents, evaluates the
reduced interaction -alpha dot V, and compares time-odd-off/on diagnostics.
All field, energy and inertia scales are explicitly model units unless a
source locator is attached in the generated manifest.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent
N = 81
EXTENT = 8.0
X = np.linspace(-EXTENT, EXTENT, N)
Z = np.linspace(-EXTENT, EXTENT, N)
XX, ZZ = np.meshgrid(X, Z, indexing="ij")
DX = float(X[1] - X[0])
DA = DX * DX

# Reduced couplings and inverse ranges.  These are deliberately visible
# parameters, not a named CDFT parameter set.
COUPLINGS = {"g_omega": 1.10, "g_rho": 0.25, "e": 0.30}
MESON_MASSES = {"omega": 1.15, "rho": 1.35, "photon": 0.25}
V2 = 1.20
SHEAR_A = 9.0
ALPHA_SCALE = 0.42
TIME_ODD_TARGETS = (0.15, 0.20, 0.25)


def gaussian(cx: float, cz: float, sigma: float = 0.85) -> np.ndarray:
    return np.exp(-((XX - cx) ** 2 + (ZZ - cz) ** 2) / (2.0 * sigma**2))


def stream_current(cx: float, cz: float, sign: float, sigma: float = 0.85):
    """Divergence-free x-z current from a localized stream function."""
    psi = sign * gaussian(cx, cz, sigma)
    dz_psi = np.gradient(psi, DX, axis=1)
    dx_psi = np.gradient(psi, DX, axis=0)
    # j=(d_z psi, 0, -d_x psi), so div j is zero to finite-difference error.
    return dz_psi, -dx_psi


def blade_pair(theta: float, amplitude: float, sign_order=(1.0, -1.0)):
    """Return a mirrored pair whose integrated magnetic moments cancel."""
    separation = 2.25 * math.sin(theta)
    jx_plus, jz_plus = stream_current(+separation, 0.0, sign_order[0])
    jx_minus, jz_minus = stream_current(-separation, 0.0, sign_order[1])
    return amplitude * (jx_plus + jx_minus), amplitude * (jz_plus + jz_minus), (
        (amplitude * jx_plus, amplitude * jz_plus),
        (amplitude * jx_minus, amplitude * jz_minus),
    )


def curl_y(jx: np.ndarray, jz: np.ndarray) -> np.ndarray:
    return np.gradient(jx, DX, axis=1) - np.gradient(jz, DX, axis=0)


def magnetic_moment_y(jx: np.ndarray, jz: np.ndarray) -> float:
    return float(np.sum(XX * jz - ZZ * jx) * DA)


def yukawa_response(source: np.ndarray, mass: float) -> np.ndarray:
    """Periodic-box reduced Green-function response in Fourier space."""
    kx = 2.0 * np.pi * np.fft.fftfreq(N, d=DX)
    kz = 2.0 * np.pi * np.fft.fftfreq(N, d=DX)
    KX, KZ = np.meshgrid(kx, kz, indexing="ij")
    kernel = 1.0 / (KX * KX + KZ * KZ + mass * mass)
    response = np.fft.ifft2(np.fft.fft2(source) * kernel).real
    return response


def fields_from_currents(jp, jn):
    jbx, jbz = jp[0] + jn[0], jp[1] + jn[1]
    jix, jiz = jp[0] - jn[0], jp[1] - jn[1]
    omega = tuple(yukawa_response(c, MESON_MASSES["omega"]) for c in (jbx, jbz))
    rho = tuple(yukawa_response(c, MESON_MASSES["rho"]) for c in (jix, jiz))
    photon = tuple(yukawa_response(c, MESON_MASSES["photon"]) for c in (jp[0], jp[1]))
    vx = COUPLINGS["g_omega"] * omega[0] + COUPLINGS["g_rho"] * rho[0] + COUPLINGS["e"] * photon[0]
    vz = COUPLINGS["g_omega"] * omega[1] + COUPLINGS["g_rho"] * rho[1] + COUPLINGS["e"] * photon[1]
    return {"omega": omega, "rho": rho, "photon": photon, "total": (vx, vz)}


def field_energy(jp, jn, fields) -> float:
    jbx, jbz = jp[0] + jn[0], jp[1] + jn[1]
    jix, jiz = jp[0] - jn[0], jp[1] - jn[1]
    omega, rho, photon = fields["omega"], fields["rho"], fields["photon"]
    integrand = (
        COUPLINGS["g_omega"] * (jbx * omega[0] + jbz * omega[1])
        + COUPLINGS["g_rho"] * (jix * rho[0] + jiz * rho[1])
        + COUPLINGS["e"] * (jp[0] * photon[0] + jp[1] * photon[1])
    )
    return float(-0.5 * np.sum(integrand) * DA)


def state_at(theta: float):
    # p and n pairs are the four local blades.  Each pair has zero integrated
    # transverse magnetic moment but a nonzero local current for theta>0.
    jp = blade_pair(theta, 1.00, (1.0, -1.0))
    jn = blade_pair(theta, 0.86, (-1.0, 1.0))
    currents = {"p": (jp[0], jp[1]), "n": (jn[0], jn[1]), "baryon": (jp[0] + jn[0], jp[1] + jn[1])}
    fields = fields_from_currents(jp, jn)
    moment_p = magnetic_moment_y(*jp[:2])
    moment_n = magnetic_moment_y(*jn[:2])
    moment_total = magnetic_moment_y(currents["baryon"][0], currents["baryon"][1])
    local_norm = float(np.sqrt(np.mean(fields["total"][0] ** 2 + fields["total"][1] ** 2)))
    return {
        "theta": theta,
        "jp": jp,
        "jn": jn,
        "currents": currents,
        "fields": fields,
        "field_energy": field_energy(jp, jn, fields),
        "moment_p": moment_p,
        "moment_n": moment_n,
        "moment_total": moment_total,
        "local_current_rms": float(np.sqrt(np.mean(currents["baryon"][0] ** 2 + currents["baryon"][1] ** 2))),
        "local_field_rms": local_norm,
    }


def orbital_shift(state, species: str, side: float, direction: float) -> float:
    """Reduced expectation of Delta h_odd=-alpha dot V for a blade orbital."""
    current_pair = state["jp"] if species == "p" else state["jn"]
    separation = 2.25 * math.sin(state["theta"])
    cx = side * separation
    # Localized orbital density; use its own blade current as a velocity proxy.
    jx, jz = stream_current(cx, 0.0, direction)
    rho = gaussian(cx, 0.0, 0.85)
    speed = np.sqrt(jx * jx + jz * jz) + 1.0e-12
    ux, uz = jx / speed, jz / speed
    vx, vz = state["fields"]["total"]
    return float(-ALPHA_SCALE * np.sum(rho * (ux * vx + uz * vz)) * DA / np.sum(rho * DA))


def level_table(state_on):
    descriptors = [
        ("p_g9/2_hole", "p", +1.0, +1.0, -3.20),
        ("p_g7/2_comparator", "p", +1.0, -1.0, -1.10),
        ("n_h11/2_particle", "n", -1.0, +1.0, 0.80),
        ("n_h9/2_comparator", "n", -1.0, -1.0, 2.10),
    ]
    rows = []
    for name, species, side, direction, baseline in descriptors:
        on_shift = orbital_shift(state_on, species, side, direction)
        rows.append({
            "level": name,
            "species": species,
            "baseline_energy_MeV": baseline,
            "time_odd_off_shift_MeV": 0.0,
            "time_odd_on_shift_MeV": on_shift,
            "energy_off_MeV": baseline,
            "energy_on_MeV": baseline + on_shift,
        })
    by_name = {r["level"]: r for r in rows}
    p_so_off = by_name["p_g7/2_comparator"]["energy_off_MeV"] - by_name["p_g9/2_hole"]["energy_off_MeV"]
    p_so_on = by_name["p_g7/2_comparator"]["energy_on_MeV"] - by_name["p_g9/2_hole"]["energy_on_MeV"]
    n_so_off = by_name["n_h11/2_particle"]["energy_off_MeV"] - by_name["n_h9/2_comparator"]["energy_off_MeV"]
    n_so_on = by_name["n_h11/2_particle"]["energy_on_MeV"] - by_name["n_h9/2_comparator"]["energy_on_MeV"]
    rows.extend([
        {"level": "proton_spin_orbit_proxy", "species": "p", "baseline_energy_MeV": p_so_off, "time_odd_off_shift_MeV": 0.0, "time_odd_on_shift_MeV": p_so_on - p_so_off, "energy_off_MeV": p_so_off, "energy_on_MeV": p_so_on},
        {"level": "neutron_spin_orbit_proxy", "species": "n", "baseline_energy_MeV": n_so_off, "time_odd_off_shift_MeV": 0.0, "time_odd_on_shift_MeV": n_so_on - n_so_off, "energy_off_MeV": n_so_off, "energy_on_MeV": n_so_on},
    ])
    return rows


def experimental_j2():
    # Direct E_gamma centers transcribed from Roy 2011 p.324 Table 1 and the
    # associated Cd sequences in the local audit.  Values remain source data;
    # no smoothing is applied to the 110Cd 1323/1314-keV near coincidence.
    data = {
        "106Cd": [980.8, 1150.6, 1310.6, 1487.6, 1675.5],
        "108Cd": [956.0, 1105.0, 1260.0, 1469.0],
        "110Cd": [1075.0, 1224.0, 1323.0, 1314.0, 1358.0],
    }
    rows = []
    for nucleus, energies in data.items():
        for i in range(1, len(energies) - 1):
            delta_mev = (energies[i + 1] - energies[i]) / 1000.0
            rows.append({
                "nucleus": nucleus,
                "center_index": i,
                "e_gamma_prev_keV": energies[i],
                "e_gamma_next_keV": energies[i + 1],
                "j2_hbar2_per_MeV": 4.0 / delta_mev if delta_mev else None,
                "boundary": "110Cd near-coincident lines" if nucleus == "110Cd" and i == 2 else "finite-difference source diagnostic",
            })
    return rows


def write_csv(path: Path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def plot_svg(path: Path, potential_rows):
    width, height = 900, 520
    xvals = [r["theta_deg"] for r in potential_rows]
    xmin, xmax = min(xvals), max(xvals)
    ymin = min(r["u_off"] for r in potential_rows)
    ymax = max(r["u_on"] for r in potential_rows)
    def px(x): return 70 + (x - xmin) / (xmax - xmin) * 780
    def py(y): return 450 - (y - ymin) / (ymax - ymin) * 370
    off = " ".join(f"{px(r['theta_deg']):.1f},{py(r['u_off']):.1f}" for r in potential_rows)
    on = " ".join(f"{px(r['theta_deg']):.1f},{py(r['u_on']):.1f}" for r in potential_rows)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="white"/><line x1="70" y1="450" x2="850" y2="450" stroke="#333"/><line x1="70" y1="80" x2="70" y2="450" stroke="#333"/>
<polyline fill="none" stroke="#3465a4" stroke-width="3" points="{off}"/><polyline fill="none" stroke="#cc4c4c" stroke-width="3" points="{on}"/>
<text x="80" y="45" font-family="sans-serif" font-size="18">AMR four-blade stiffness proxy (reduced units)</text>
<text x="375" y="500" font-family="sans-serif" font-size="14">theta (degree)</text><text x="10" y="260" transform="rotate(-90 10 260)" font-family="sans-serif" font-size="14">U_scissors</text>
<line x1="620" y1="35" x2="660" y2="35" stroke="#3465a4" stroke-width="3"/><text x="670" y="40" font-family="sans-serif" font-size="13">time-odd off</text>
<line x1="620" y1="60" x2="660" y2="60" stroke="#cc4c4c" stroke-width="3"/><text x="670" y="65" font-family="sans-serif" font-size="13">time-odd on (proxy)</text>
</svg>'''
    path.write_text(svg, encoding="utf-8")


def main():
    theta_ref = math.radians(45.0)
    state = state_at(theta_ref)
    zero = state_at(math.radians(1.0))
    levels = level_table(state)
    potential_rows = []
    ref_norm = state["local_field_rms"]
    for degree in np.linspace(10.0, 90.0, 81):
        sample = state_at(math.radians(float(degree)))
        u_off = V2 * math.sin(math.radians(float(degree))) ** 2
        ratio = sample["local_field_rms"] / ref_norm if ref_norm else 0.0
        eta = 0.20 * (0.75 + 0.25 * ratio)
        potential_rows.append({
            "theta_deg": round(float(degree), 3),
            "u_off": u_off,
            "u_on": u_off * (1.0 + eta),
            "field_rms": sample["local_field_rms"],
            "enhancement_percent": 100.0 * eta,
            "field_energy": sample["field_energy"],
        })
    enhancement = [r["enhancement_percent"] for r in potential_rows]
    target_scan = [{"target_percent": 100.0 * t, "u_on_over_u_off_percent": 100.0 * (1.0 + t)} for t in TIME_ODD_TARGETS]

    exp_rows = experimental_j2()
    median_j2 = {}
    for nucleus in ("106Cd", "108Cd", "110Cd"):
        vals = [r["j2_hbar2_per_MeV"] for r in exp_rows if r["nucleus"] == nucleus and r["j2_hbar2_per_MeV"] is not None and r["j2_hbar2_per_MeV"] > 0]
        median_j2[nucleus] = float(np.median(vals)) if vals else None
    # The gain is a response ansatz tied to the calculated local field metric;
    # it is not a decomposition of the experimental J(2).
    field_factor = state["local_field_rms"] / (state["local_field_rms"] + abs(zero["local_field_rms"]) + 1.0e-12)
    core_off = {"106Cd": 22.5, "108Cd": 22.5, "110Cd": 42.0}
    j2_rows = []
    for nucleus, off in core_off.items():
        gain = 0.06 + 0.06 * field_factor + {"106Cd": 0.00, "108Cd": 0.01, "110Cd": 0.02}[nucleus]
        j2_rows.append({
            "nucleus": nucleus,
            "time_odd_off_model_j2": off,
            "time_odd_on_model_j2": off * (1.0 + gain),
            "time_odd_contribution_percent": 100.0 * gain,
            "experimental_positive_median_j2": median_j2[nucleus],
            "interpretation": "proxy response; not an experimental subtraction",
        })

    field_rows = []
    vorticity = curl_y(state["currents"]["baryon"][0], state["currents"]["baryon"][1])
    for i in range(N):
        for k in range(N):
            field_rows.append({
                "x": round(float(XX[i, k]), 5), "z": round(float(ZZ[i, k]), 5),
                "j_baryon_x": float(state["currents"]["baryon"][0][i, k]), "j_baryon_z": float(state["currents"]["baryon"][1][i, k]),
                "V_x": float(state["fields"]["total"][0][i, k]), "V_z": float(state["fields"]["total"][1][i, k]),
                "vorticity_y": float(vorticity[i, k]),
            })

    write_csv(ROOT / "local_fields.csv", field_rows)
    write_csv(ROOT / "level_shifts.csv", levels)
    write_csv(ROOT / "scissors_potential.csv", potential_rows)
    write_csv(ROOT / "j2_cd_systematics.csv", exp_rows)
    write_csv(ROOT / "j2_time_odd_proxy.csv", j2_rows)
    plot_svg(ROOT / "time_odd_fields.svg", potential_rows)

    manifest = {
        "schema_version": 1,
        "artifact_id": "amr-relativistic-time-odd-fields-20261029",
        "status": "proxy-model-self-audit",
        "model_boundary": "not a self-consistent 3-D CRMF calculation; reduced units and response ansatz are explicit",
        "equations": {
            "dirac_cranking": "h' = alpha dot[-i grad - V(r)] + beta(m+S) + V0 - omega dot J",
            "time_odd_vector": "V = g_omega omega + g_rho tau_3 rho + e(1-tau_3)/2 A",
            "field_response": "(-nabla^2 + m_a^2) a_i(r) = g_a j_i(r)",
            "time_odd_shift": "Delta h_odd = - alpha dot V(r)",
            "shears_proxy": "U_off = V2 sin^2(theta); U_on = U_off[1+eta(theta)]",
            "j2": "J^(2) = 4 / [E_gamma(I+2->I)-E_gamma(I->I-2)]",
        },
        "symmetry_diagnostic": {
            "theta_deg": 45.0,
            "local_current_rms": state["local_current_rms"],
            "local_field_rms": state["local_field_rms"],
            "mu_p_transverse_proxy": state["moment_p"],
            "mu_n_transverse_proxy": state["moment_n"],
            "mu_total_transverse_proxy": state["moment_total"],
            "near_closure_local_current_rms": zero["local_current_rms"],
            "interpretation": "paired blade moments cancel globally while the local current and vector field are nonzero away from closure",
        },
        "level_summary": levels,
        "scissors_summary": {
            "enhancement_min_percent": min(enhancement),
            "enhancement_max_percent": max(enhancement),
            "target_scan": target_scan,
            "warning": "15-25 percent is a prescribed sensitivity band, not a published CRMF result",
        },
        "j2_summary": j2_rows,
        "source_locators": [
            "knowledge/sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md, PDF pp.467, 487-490",
            "knowledge/sources/roy-2011-cd110-systematics-antimagnetic.md, PDF p.324 Table 1 and pp.325-326",
            "knowledge/sources/rather-2014-104pd-antimagnetic-first-page.md, printed 061303-1 Eqs.1-2",
        ],
    }
    (ROOT / "results.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
