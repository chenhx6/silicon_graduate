#!/usr/bin/env python3
"""Berry geometry of a four-state chiral--octupole rotating-nucleus toy model.

The code is an auditable phenomenological calculation.  It uses the localized
basis |L,+>, |R,+>, |L,->, |R,-> (two Pauli spaces) and a complex Hermitian
Hamiltonian whose parameters are (hbar*omega, beta2, beta3).  The occupied
two-state subspace is followed with a polar-decomposition Wilson link, so the
reported loop phase is gauge invariant modulo 2*pi.  Projector derivatives
also give the trace Berry curvature and the quantum metric.

Nothing in this file is fitted to a nucleus.  In particular, nonzero smooth
curvature is not by itself a quantized Chern number or evidence for a nuclear
topological phase.  A genuine topological invariant requires a closed surface,
an everywhere-open gap, and a specified microscopic Hamiltonian.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent
PI = math.pi


def paulis() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    i2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return i2, sx, sy, sz


I2, SX, SY, SZ = paulis()
TAU = [np.kron(x, I2) for x in (SX, SY, SZ)]
XI = [np.kron(I2, x) for x in (SX, SY, SZ)]
TAU_Z_XI_Z = np.kron(SZ, SZ)
IDENTITY = np.eye(4, dtype=complex)


def hamiltonian(omega: float, beta2: float, beta3: float) -> np.ndarray:
    """Return a 4x4 conditional Routhian in keV.

    The x components are tunnelling between localized L/R or +/- octupole
    wells.  The y components are the minimal time-reversal-breaking cranking
    terms.  beta3 controls reflection-asymmetric mixing and omega controls the
    rotational field.  The weak tau_z xi_z term is the lowest local
    chirality--octupole coupling that differentiates the four corners.
    """
    # All coefficients are declared synthetic scales (keV or keV per unit
    # deformation).  beta2 enters the tunnelling amplitudes to retain a
    # quadrupole--octupole coordinate dependence.
    t_chi = 72.0 * math.exp(-0.55 * omega) * (1.0 + 0.35 * beta2)
    t_par = 54.0 * (1.0 + 0.25 * beta2 * beta2)
    rot_chi = 26.0 * omega
    rot_par = 18.0 * omega
    oct_chi = 95.0 * beta3
    oct_par = 82.0 * beta3
    local_bias = 11.0 * (beta2 - 0.20) + 7.0 * beta3 * beta3
    coupling = 9.0 * beta3 + 2.5 * omega * beta2

    h = 480.0 * IDENTITY
    h = h - t_chi * TAU[0] + rot_chi * TAU[1] + local_bias * TAU[2]
    h = h - t_par * XI[0] + rot_par * XI[1] + oct_par * XI[2]
    h = h + oct_chi * TAU[2] + coupling * TAU_Z_XI_Z
    return (h + h.conj().T) / 2.0


def eigensystem(omega: float, beta2: float, beta3: float) -> tuple[np.ndarray, np.ndarray]:
    vals, vecs = np.linalg.eigh(hamiltonian(omega, beta2, beta3))
    return vals.real, vecs


def projector(omega: float, beta2: float, beta3: float, rank: int = 2) -> np.ndarray:
    _, vecs = eigensystem(omega, beta2, beta3)
    occ = vecs[:, :rank]
    return occ @ occ.conj().T


def projector_derivatives(omega: float, beta2: float, beta3: float, step: float = 1e-5):
    base = np.array([omega, beta2, beta3], dtype=float)
    derivs = []
    for axis in range(3):
        plus = base.copy()
        minus = base.copy()
        plus[axis] += step
        minus[axis] -= step
        derivs.append((projector(*plus) - projector(*minus)) / (2.0 * step))
    return derivs


def geometry(omega: float, beta2: float, beta3: float) -> dict[str, float]:
    """Trace curvature and quantum metric of the lowest rank-two subspace."""
    p = projector(omega, beta2, beta3)
    ds = projector_derivatives(omega, beta2, beta3)
    curvature = {}
    metric = {}
    names = ("omega", "beta2", "beta3")
    for a in range(3):
        for b in range(a + 1, 3):
            comm = ds[a] @ ds[b] - ds[b] @ ds[a]
            # A=i<U|dU>; F_ab=i Tr P[d_aP,d_bP].
            f = 1j * np.trace(p @ comm)
            g = 0.5 * np.trace(ds[a] @ ds[b])
            curvature[f"F_{names[a]}_{names[b]}"] = float(np.real(f))
            metric[f"g_{names[a]}_{names[b]}"] = float(np.real(g))
    gaps = np.diff(eigensystem(omega, beta2, beta3)[0])
    return {**curvature, **metric, "gap_1_2_keV": float(gaps[1]), "gap_2_3_keV": float(gaps[2])}


def polar_unitary(overlap: np.ndarray) -> np.ndarray:
    """Unitary factor of overlap by SVD; stable under arbitrary eigenvector phases."""
    u, _, vh = np.linalg.svd(overlap)
    return u @ vh


def loop_points(n: int = 240, beta2: float = 0.20, omega_c: float = 0.42,
                radius_omega: float = 0.18, radius_beta3: float = 0.075):
    points = []
    for k in range(n + 1):
        phi = 2.0 * PI * k / n
        points.append((omega_c + radius_omega * math.cos(phi), beta2,
                       radius_beta3 * math.sin(phi), phi))
    return points


def wilson_loop(points: list[tuple[float, float, float, float]], rank: int = 2):
    """Return non-Abelian Wilson phase and per-link data for a closed path."""
    states = []
    energies = []
    for omega, beta2, beta3, _ in points:
        vals, vecs = eigensystem(omega, beta2, beta3)
        states.append(vecs[:, :rank])
        energies.append(vals)
    holonomy = np.eye(rank, dtype=complex)
    rows = []
    cumulative = 0.0
    for j in range(len(points) - 1):
        link = polar_unitary(states[j].conj().T @ states[j + 1])
        step_phase = -float(np.angle(np.linalg.det(link)))
        cumulative += step_phase
        holonomy = holonomy @ link
        rows.append({
            "step": j,
            "phi": points[j][3],
            "omega": points[j][0],
            "beta2": points[j][1],
            "beta3": points[j][2],
            "E0_keV": float(energies[j][0]),
            "E1_keV": float(energies[j][1]),
            "link_phase_rad": step_phase,
            "geometric_phase_unwrapped_rad": cumulative,
            "gap_0_1_keV": float(energies[j][1] - energies[j][0]),
        })
    gamma = -float(np.angle(np.linalg.det(holonomy)))
    return gamma, rows, holonomy


def single_state_phase(points):
    """Abelian lowest-state phase, used for the dynamical-phase comparison."""
    vecs = []
    vals = []
    for omega, beta2, beta3, _ in points:
        e, v = eigensystem(omega, beta2, beta3)
        vals.append(float(e[0]))
        vecs.append(v[:, 0])
    phase = 0.0
    cumulative = []
    for j in range(len(points) - 1):
        phase += -float(np.angle(np.vdot(vecs[j], vecs[j + 1])))
        cumulative.append(phase)
    return float(phase), vals, cumulative


def dynamical_phase_rows(points, energies, periods=(0.005, 0.010, 0.020)):
    """Integrate -E(t)dt/hbar for several traversal periods.

    ``period`` is T/hbar in keV^-1 and the path parameter runs from 0 to 1.
    The constant energy zero is removed before integration because it is a
    gauge convention; the geometric phase is unaffected by this choice.
    """
    e = np.asarray(energies, dtype=float)
    e_relative = e - e[0]
    s = np.linspace(0.0, 1.0, len(e_relative))
    integral = float(np.trapezoid(e_relative, s))
    rows = []
    for period in periods:
        rows.append({
            "period_T_over_hbar_keV_inv": float(period),
            "relative_energy_integral_keV": integral,
            "dynamical_phase_rad": -float(period) * integral,
            "geometric_phase_rad": None,
            "phase_dependence": "changes with traversal period; independent geometric phase is stored separately",
        })
    return rows


def effective_gap_rows(gamma: float, n: int = 21):
    """Two-path tunnelling interference proxy for Berry-phase gap modulation."""
    rows = []
    for i in range(n):
        spin = 8 + i * 0.5
        t1 = 38.0 * math.exp(-0.045 * (spin - 8.0))
        t2 = 31.0 * math.exp(-0.035 * (spin - 8.0))
        dynamic = 0.31 * (spin - 8.0)
        phase = gamma + dynamic
        gap = 2.0 * abs(t1 + t2 * complex(math.cos(phase), math.sin(phase)))
        gap_classical = 2.0 * (t1 + t2)
        rows.append({
            "I": spin,
            "t_path1_keV": t1,
            "t_path2_keV": t2,
            "geometric_phase_rad": gamma,
            "dynamical_phase_rad": dynamic,
            "total_interference_phase_rad": phase,
            "gap_with_berry_proxy_keV": gap,
            "gap_zero_phase_keV": gap_classical,
            "gap_shift_keV": gap - gap_classical,
            "S_proxy_keV": (gap - gap_classical) / max(2.0 * spin, 1.0),
        })
    return rows


def transition_branch_rows(gamma: float):
    """Synthetic E1/M1 branch ratio proxy, not a nuclear transition fit."""
    rows = []
    for i in range(13):
        spin = 8 + i * 0.5
        e1_amp = 0.32 * (1.0 + 0.35 * math.cos(gamma + 0.12 * i))
        m1_amp = 1.00 * (1.0 - 0.22 * math.cos(gamma + 0.12 * i))
        e1_energy = 0.68 + 0.012 * i
        m1_energy = 0.52 + 0.010 * i
        rate_e1 = e1_energy ** 3 * e1_amp ** 2
        rate_m1 = m1_energy ** 3 * m1_amp ** 2
        rows.append({
            "I": spin,
            "E1_amplitude_proxy": e1_amp,
            "M1_amplitude_proxy": m1_amp,
            "E1_energy_MeV": e1_energy,
            "M1_energy_MeV": m1_energy,
            "Gamma_E1_proxy": rate_e1,
            "Gamma_M1_proxy": rate_m1,
            "E1_over_M1_branch_ratio_proxy": rate_e1 / rate_m1,
            "selection_rule": "E1 changes parity; M1 preserves parity",
        })
    return rows


def write_csv(path: Path, rows: list[dict]):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def svg_path(path: Path, rows: list[dict], x_key: str, y_key: str,
             title: str, x_label: str, y_label: str):
    width, height, margin = 720, 420, 58
    xs = [float(r[x_key]) for r in rows]
    ys = [float(r[y_key]) for r in rows]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    if xmax == xmin:
        xmax += 1.0
    if ymax == ymin:
        ymax += 1.0
    def xy(x, y):
        px = margin + (x - xmin) / (xmax - xmin) * (width - 2 * margin)
        py = height - margin - (y - ymin) / (ymax - ymin) * (height - 2 * margin)
        return px, py
    points = " ".join(f"{xy(x, y)[0]:.2f},{xy(x, y)[1]:.2f}" for x, y in zip(xs, ys))
    text = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="100%" height="100%" fill="white"/><text x="{width/2}" y="25" text-anchor="middle" font-family="sans-serif" font-size="16">{title}</text>
<line x1="{margin}" y1="{height-margin}" x2="{width-margin}" y2="{height-margin}" stroke="black"/><line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height-margin}" stroke="black"/>
<polyline points="{points}" fill="none" stroke="#1f5a9d" stroke-width="2"/>
<text x="{width/2}" y="{height-12}" text-anchor="middle" font-family="sans-serif" font-size="13">{x_label}</text>
<text x="15" y="{height/2}" transform="rotate(-90 15 {height/2})" text-anchor="middle" font-family="sans-serif" font-size="13">{y_label}</text>
</svg>
'''
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def main():
    beta2_values = np.linspace(0.12, 0.28, 9)
    beta3_values = np.linspace(-0.12, 0.12, 13)
    omega_values = np.linspace(0.18, 0.66, 9)
    grid_rows = []
    for omega in omega_values:
        for beta2 in beta2_values:
            for beta3 in beta3_values:
                row = {"omega": float(omega), "beta2": float(beta2), "beta3": float(beta3)}
                row.update(geometry(float(omega), float(beta2), float(beta3)))
                grid_rows.append(row)
    points = loop_points()
    gamma_nonabelian, wilson_rows, holonomy = wilson_loop(points)
    gamma_abelian, energies, phase_curve = single_state_phase(points)
    dynamic_rows = dynamical_phase_rows(points, energies)
    for row in dynamic_rows:
        row["geometric_phase_rad"] = gamma_nonabelian
    for row, phase in zip(wilson_rows, phase_curve):
        row["abelian_ground_phase_unwrapped_rad"] = phase
    gap_rows = effective_gap_rows(gamma_nonabelian)
    branch_rows = transition_branch_rows(gamma_nonabelian)
    metadata = {
        "model": "four-state chiral-octupole rotating-nucleus Berry geometry toy",
        "basis": ["|L,+>", "|R,+>", "|L,->", "|R,->"],
        "coordinates": ["hbar*omega [MeV]", "beta2", "beta3"],
        "occupied_subspace": "lowest two eigenstates; non-Abelian Wilson loop",
        "connection": "A_mu = i U^dagger partial_mu U",
        "curvature": "F_mn = i Tr[P (partial_m P partial_n P - partial_n P partial_m P)]",
        "quantum_metric": "g_mn = 1/2 Re Tr[(partial_m P)(partial_n P)]",
        "loop": {"omega_c": 0.42, "radius_omega": 0.18, "beta2": 0.20, "radius_beta3": 0.075,
                 "points": len(points) - 1},
        "gamma_nonabelian_rad": gamma_nonabelian,
        "gamma_ground_state_rad": gamma_abelian,
        "dynamical_phase_scan": dynamic_rows,
        "wilson_holonomy_real": holonomy.real.tolist(),
        "wilson_holonomy_imag": holonomy.imag.tolist(),
        "evidence_boundary": [
            "Synthetic coefficients are not fitted to 78Br, 130Cs, 133Ce, or 135Nd.",
            "A smooth nonzero Berry curvature is not a quantized topological invariant.",
            "Effective gap and E1/M1 branch rows are interference proxies, not measured observables.",
            "The four local minima require a declared double-well potential; the Hamiltonian describes tunnelling around them.",
        ],
    }
    write_csv(OUT / "berry_curvature_metric_grid.csv", grid_rows)
    write_csv(OUT / "berry_loop_accumulation.csv", wilson_rows)
    write_csv(OUT / "dynamical_vs_geometric_phase.csv", dynamic_rows)
    write_csv(OUT / "spectrum_topological_perturbation.csv", gap_rows)
    write_csv(OUT / "e1_m1_branch_ratio_proxy.csv", branch_rows)
    svg_path(OUT / "berry_phase_accumulation.svg", wilson_rows, "phi", "geometric_phase_unwrapped_rad",
             "Non-Abelian geometric phase along C", "loop parameter phi [rad]", "phase [rad]")
    svg_path(OUT / "topological_gap_proxy.svg", gap_rows, "I", "gap_shift_keV",
             "Berry-phase tunnelling-gap proxy", "spin I", "gap shift [keV]")
    (OUT / "results.json").write_text(json.dumps({"metadata": metadata, "grid_rows": len(grid_rows),
                                                     "loop_rows": wilson_rows, "gap_rows": gap_rows,
                                                     "branch_rows": branch_rows}, indent=2) + "\n", encoding="utf-8")
    (OUT / "chart_data.json").write_text(json.dumps({"phase_curve": wilson_rows,
                                                       "gap_proxy": gap_rows,
                                                       "branch_ratio_proxy": branch_rows}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"gamma_nonabelian_rad": gamma_nonabelian,
                      "gamma_ground_state_rad": gamma_abelian,
                      "grid_rows": len(grid_rows), "loop_rows": len(wilson_rows)}, indent=2))


if __name__ == "__main__":
    main()
