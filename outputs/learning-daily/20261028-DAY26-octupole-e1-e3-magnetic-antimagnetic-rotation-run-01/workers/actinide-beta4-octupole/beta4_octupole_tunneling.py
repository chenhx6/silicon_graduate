#!/usr/bin/env python3
"""Reduced beta2-beta3-beta4 and orbital-mixing model for light actinides.

The code is deliberately a transparent response model.  It is not a
self-consistent Woods-Saxon, Nilsson, HFB, GCM, or EDF calculation.  It keeps
the symmetry-allowed beta2*beta3**2*beta4 term explicit, follows its minimum
energy path (MEP), and solves a one-dimensional Schrodinger equation in beta3
for the parity splitting.  A separate two-level single-particle surrogate
tracks how beta4 changes the Delta-l=Delta-j=3 proton and neutron pairs.

All beta coordinates are dimensionless.  Energies and matrix elements in the
surrogate are in MeV.  The numerical values are model inputs chosen for
sensitivity diagnostics; they are not fitted values for 224,226Ra or 226,228Th.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import eigh_tridiagonal

try:  # Plotting is optional; tabular outputs remain the primary result.
    import matplotlib.pyplot as plt
except Exception:  # pragma: no cover - optional dependency
    plt = None


OUT = Path(__file__).resolve().parent

# Fixed quadrupole window requested by the task.
BETA2_VALUES = np.array([0.150, 0.175, 0.200])
BETA3_GRID = np.linspace(-0.32, 0.32, 321)
BETA4_GRID = np.linspace(-0.08, 0.08, 161)
BETA4_SCAN = np.linspace(-0.06, 0.06, 25)

# beta3 collective kinetic coefficient hbar^2/(2 B_33), in MeV.  Because beta3
# is dimensionless this is an effective collective scale, not a SI mass.
# Chosen so the reduced-model splitting remains numerically resolvable on the
# finite grid while the well zero-point energy stays below the central barrier.
H2_OVER_2B33 = 5.0e-5
SCHROD_GRID = np.linspace(-0.32, 0.32, 641)

# Landau coefficients for the transparent PES.  The sign convention is such
# that positive beta4 lowers the beta3^2 coefficient when G234 > 0.
LANDau = {
    "a3_at_beta2_0175_MeV": -13.5,
    "a3_beta2_curvature_MeV": 220.0,
    "b3_MeV": 260.0,
    "c3_MeV": 1200.0,
    "k4_MeV": 45.0,
    "u4_MeV": 4000.0,
    "G234_MeV": 70.0,
}

# The labels are a basis convention.  Actual ordering can change with the
# nucleus and deformation; delta is defined as epsilon_upper-epsilon_lower in
# this two-level diagnostic basis.
ORBITAL_PAIRS = [
    {
        "species": "proton",
        "lower_orbit": "pi f7/2",
        "upper_orbit": "pi i13/2",
        "delta0_MeV": 0.260,
        "delta_beta2_MeV": 3.2,
        "delta_beta4_MeV": -2.6,
        "kappa3_MeV": 2.70,
        "overlap0": 0.92,
        "overlap_beta2": -0.60,
        "overlap_beta4": 1.80,
    },
    {
        "species": "neutron",
        "lower_orbit": "nu g9/2",
        "upper_orbit": "nu j15/2",
        "delta0_MeV": 0.180,
        "delta_beta2_MeV": -2.2,
        "delta_beta4_MeV": -1.7,
        "kappa3_MeV": 3.00,
        "overlap0": 0.97,
        "overlap_beta2": -0.40,
        "overlap_beta4": 1.30,
    },
]


def a3(beta2: float) -> float:
    """Bare beta3 quadratic coefficient at fixed beta2."""
    return LANDau["a3_at_beta2_0175_MeV"] + LANDau["a3_beta2_curvature_MeV"] * (
        beta2 - 0.175
    ) ** 2


def pes(beta3, beta4, beta2: float, coupling_scale: float = 1.0):
    """Return the symmetry-even Landau PES in MeV.

    V(beta3,beta4)=1/2*a3*beta3^2+1/4*b3*beta3^4+1/6*c3*beta3^6
                    +1/2*k4*beta4^2+1/4*u4*beta4^4
                    -G234*beta2*beta3^2*beta4.

    The last term is invariant under beta3 -> -beta3.  Its sign is a model
    convention, not a symmetry prediction.  Positive beta4 therefore
    stabilizes a finite beta3 in this chosen convention.
    """
    b3 = np.asarray(beta3)
    b4 = np.asarray(beta4)
    return (
        0.5 * a3(beta2) * b3**2
        + 0.25 * LANDau["b3_MeV"] * b3**4
        + (LANDau["c3_MeV"] / 6.0) * b3**6
        + 0.5 * LANDau["k4_MeV"] * b4**2
        + 0.25 * LANDau["u4_MeV"] * b4**4
        - coupling_scale * LANDau["G234_MeV"] * beta2 * b3**2 * b4
    )


def beta4_mep(beta3: float, beta2: float, coupling_scale: float = 1.0) -> float:
    """Minimize V with respect to beta4 using Newton iterations.

    For positive k4 and u4 the derivative is monotone.  The root is therefore
    unique and the iteration is clipped to the saved beta4 grid for auditability.
    """
    rhs = coupling_scale * LANDau["G234_MeV"] * beta2 * beta3**2
    x = rhs / LANDau["k4_MeV"]
    for _ in range(30):
        f = LANDau["k4_MeV"] * x + LANDau["u4_MeV"] * x**3 - rhs
        df = LANDau["k4_MeV"] + 3.0 * LANDau["u4_MeV"] * x**2
        step = f / df
        x -= step
        if abs(step) < 1.0e-14:
            break
    return float(np.clip(x, BETA4_GRID[0], BETA4_GRID[-1]))


def parabolic_minimum(x: np.ndarray, y: np.ndarray, index: int) -> tuple[float, float]:
    """Refine a grid minimum with a local parabolic interpolation."""
    if index <= 0 or index >= len(x) - 1:
        return float(x[index]), float(y[index])
    x0, xm, xp = x[index - 1 : index + 2]
    y0, ym, yp = y[index - 1 : index + 2]
    denom = y0 - 2.0 * ym + yp
    if abs(denom) < 1.0e-14:
        return float(xm), float(ym)
    dx = 0.5 * (x0 - xp) * (y0 - yp) / denom
    xv = float(xm + dx)
    yv = float(ym - (y0 - yp) ** 2 / (8.0 * denom))
    return xv, yv


def positive_minimum(beta2: float, beta4: float) -> tuple[float, float, float]:
    """Return beta3_min>0, well depth, and central barrier at fixed beta4."""
    x = BETA3_GRID[BETA3_GRID >= 0.0]
    y = pes(x, beta4, beta2)
    # Exclude beta3=0 when searching for a broken-reflection minimum.
    i = int(np.argmin(y[1:])) + 1
    q, vmin = parabolic_minimum(x, y, i)
    v_center = float(pes(0.0, beta4, beta2))
    return q, vmin, v_center - vmin


def mep_curve(beta2: float, beta3_values: np.ndarray | None = None):
    """Return beta4*(beta3), V_MEP(beta3), and the shifted MEP."""
    x = BETA3_GRID if beta3_values is None else np.asarray(beta3_values)
    b4 = np.array([beta4_mep(float(q), beta2) for q in x])
    v = pes(x, b4, beta2)
    v_shift = v - float(np.min(v))
    return x, b4, v, v_shift


def mep_summary(beta2: float) -> dict:
    x, b4, v, v_shift = mep_curve(beta2)
    mask = x >= 0.0
    i = int(np.argmin(v[mask]))
    x_pos = x[mask]
    v_pos = v[mask]
    b4_pos = b4[mask]
    q, vmin = parabolic_minimum(x_pos, v_pos, i)
    b4_at_min = float(np.interp(q, x_pos, b4_pos))
    center = float(pes(0.0, beta4_mep(0.0, beta2), beta2))
    return {
        "beta2": float(beta2),
        "beta3_min": q,
        "beta4_at_beta3_min": b4_at_min,
        "V_min_MeV": vmin,
        "V_barrier_MeV": center - vmin,
        "beta4_at_center": beta4_mep(0.0, beta2),
        "mep_symmetry_max_abs_MeV": float(np.max(np.abs(v - v[::-1]))),
    }


def curvature_at_minimum(beta2: float, beta4: float, q: float) -> float:
    """Numerical d2V/dbeta3^2 at a finite positive minimum."""
    h = 2.0e-4
    return float(
        (pes(q + h, beta4, beta2) - 2.0 * pes(q, beta4, beta2) + pes(q - h, beta4, beta2))
        / h**2
    )


def wkb_from_curve(x: np.ndarray, v_shift: np.ndarray, beta2: float, q_min: float) -> dict:
    """Estimate the lowest parity splitting from the central forbidden region."""
    dx = float(x[1] - x[0])
    # A finite-difference curvature gives the well harmonic scale.  This is
    # only a prefactor; the exponential is the diagnostic of interest.
    b4_min = beta4_mep(q_min, beta2)
    curv = curvature_at_minimum(beta2, b4_min, q_min)
    hbar_omega = math.sqrt(max(2.0 * H2_OVER_2B33 * curv, 0.0))

    # Use the exact even ground state energy from the same grid for the WKB
    # turning-point search.  This keeps the comparison with diagonalization
    # explicit while marking cases where WKB is not applicable.
    eig = schrodinger(beta2, beta4_mode="mep")
    e0 = eig["E_even_MeV"]
    central = (x >= 0.0) & (x <= q_min)
    forbidden = central & (v_shift > e0)
    if not np.any(forbidden):
        return {
            "WKB_applicable": False,
            "E0_MeV": e0,
            "S_over_hbar": None,
            "DeltaE_WKB_MeV": None,
            "hbar_omega_MeV": hbar_omega,
        }
    q_forbid = x[forbidden]
    v_forbid = v_shift[forbidden]
    # Double the positive-half integral to cross the complete central barrier.
    action_half = float(np.trapezoid(np.sqrt(np.maximum((v_forbid - e0) / H2_OVER_2B33, 0.0)), q_forbid))
    action = 2.0 * action_half
    delta = hbar_omega / math.pi * math.exp(-action) if hbar_omega > 0 else 0.0
    return {
        "WKB_applicable": True,
        "E0_MeV": e0,
        "S_over_hbar": action,
        "DeltaE_WKB_MeV": delta,
        "hbar_omega_MeV": hbar_omega,
    }


def schrodinger(beta2: float, beta4_mode: float | str = "mep", grid: np.ndarray | None = None) -> dict:
    """Diagonalize H=-h2*d2/dbeta3^2+V(beta3) and classify parity."""
    x = SCHROD_GRID if grid is None else np.asarray(grid, dtype=float)
    if beta4_mode == "mep":
        b4 = np.array([beta4_mep(float(q), beta2) for q in x])
        v = pes(x, b4, beta2)
        mode_label = "mep"
    else:
        b4 = np.full_like(x, float(beta4_mode))
        v = pes(x, b4, beta2)
        mode_label = float(beta4_mode)
    v -= float(np.min(v))
    dx = float(x[1] - x[0])
    t = H2_OVER_2B33 / dx**2
    diag = 2.0 * t + v
    off = np.full(len(x) - 1, -t)
    evals, evecs = eigh_tridiagonal(diag, off, select="i", select_range=(0, 3))
    # Eigenvectors are normalized in the Euclidean convention.  Parity is
    # diagnosed by the discrete overlap under x -> -x.
    parity = np.array([np.dot(evecs[:, i], evecs[::-1, i]) for i in range(4)])
    # For a symmetric one-dimensional potential the ground state is even and
    # the first excited state is odd.  Do not use argmax/argmin here: near a
    # degenerate doublet tiny LAPACK roundoff can make the second even state
    # have a parity overlap infinitesimally closer to +1 than the ground state.
    even, odd = 0, 1
    return {
        "beta2": float(beta2),
        "beta4_mode": mode_label,
        "E_even_MeV": float(evals[even]),
        "E_odd_MeV": float(evals[odd]),
        "DeltaE_odd_minus_even_MeV": float(evals[odd] - evals[even]),
        "even_parity_expectation": float(parity[even]),
        "odd_parity_expectation": float(parity[odd]),
        "grid_points": len(x),
        "grid_step": dx,
    }


def orbital_row(pair: dict, beta2: float, beta4: float, beta3: float) -> dict:
    """Evaluate the beta4-dependent two-level octupole mixing surrogate."""
    delta = pair["delta0_MeV"] + pair["delta_beta2_MeV"] * (beta2 - 0.175) + pair["delta_beta4_MeV"] * beta4
    overlap = pair["overlap0"] * (
        1.0 + pair["overlap_beta2"] * (beta2 - 0.175) + pair["overlap_beta4"] * beta4
    )
    overlap = max(overlap, 0.05)
    v3 = pair["kappa3_MeV"] * beta3 * overlap
    spectral_gap = math.sqrt(delta**2 + 4.0 * v3**2)
    mixing = 0.5 * (1.0 - abs(delta) / spectral_gap) if spectral_gap else 0.0
    chi_proxy = 2.0 * (pair["kappa3_MeV"] * overlap) ** 2 / max(abs(delta), 1.0e-9)
    return {
        "species": pair["species"],
        "lower_orbit": pair["lower_orbit"],
        "upper_orbit": pair["upper_orbit"],
        "beta2": float(beta2),
        "beta4": float(beta4),
        "beta3_reference": float(beta3),
        "delta_epsilon_MeV": float(delta),
        "octupole_overlap_proxy": float(overlap),
        "octupole_matrix_element_MeV": float(v3),
        "adiabatic_pair_gap_MeV": float(spectral_gap),
        "mixing_probability": float(mixing),
        "chi3_proxy_MeV": float(chi_proxy),
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def make_plots(surface_rows, fixed_rows, orbital_rows, mep_rows) -> None:
    if plt is None:
        return
    # Contour and MEP at the middle beta2 slice.
    b2_ref = 0.175
    grid = [r for r in surface_rows if abs(r["beta2"] - b2_ref) < 1e-12]
    b3 = np.array(sorted({r["beta3"] for r in grid}))
    b4 = np.array(sorted({r["beta4"] for r in grid}))
    z = np.array([r["V_MeV"] for r in grid]).reshape(len(b4), len(b3))
    mep = [r for r in mep_rows if abs(r["beta2"] - b2_ref) < 1e-12]
    fig, ax = plt.subplots(figsize=(6.5, 4.6))
    levels = np.linspace(float(z.min()), float(z.min() + 0.5), 18)
    cs = ax.contourf(b3, b4, z, levels=levels, cmap="viridis", extend="max")
    ax.plot([r["beta3"] for r in mep], [r["beta4_mep"] for r in mep], "w-", lw=2, label="MEP")
    ax.set(xlabel=r"$\beta_3$", ylabel=r"$\beta_4$", title=r"$V(\beta_3,\beta_4)$ at $\beta_2=0.175$")
    fig.colorbar(cs, ax=ax, label="V (MeV)")
    ax.legend(); fig.tight_layout(); fig.savefig(OUT / "pes_beta3_beta4_beta2_0175.png", dpi=180); plt.close(fig)

    # Fixed-beta4 response and parity splitting.
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for b2 in BETA2_VALUES:
        rows = [r for r in fixed_rows if abs(r["beta2"] - b2) < 1e-12]
        axes[0].plot([r["beta4"] for r in rows], [r["V_barrier_MeV"] for r in rows], label=fr"$\beta_2={b2:.3f}$")
        axes[1].semilogy([r["beta4"] for r in rows], [max(r["DeltaE_exact_MeV"], 1e-12) * 1e3 for r in rows], label=fr"$\beta_2={b2:.3f}$")
    axes[0].set(xlabel=r"fixed $\beta_4$", ylabel=r"$V_{barrier}$ (MeV)")
    axes[1].set(xlabel=r"fixed $\beta_4$", ylabel=r"$\Delta E$ (keV)")
    for axis in axes: axis.grid(alpha=0.25); axis.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(OUT / "beta4_barrier_and_parity_splitting.png", dpi=180); plt.close(fig)

    # Orbital gap and mixing at the central beta2 slice.
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for species in sorted({r["species"] for r in orbital_rows}):
        rows = [r for r in orbital_rows if r["species"] == species and abs(r["beta2"] - 0.175) < 1e-12]
        label = species + " pair"
        axes[0].plot([r["beta4"] for r in rows], [r["delta_epsilon_MeV"] for r in rows], label=label)
        axes[1].plot([r["beta4"] for r in rows], [r["mixing_probability"] for r in rows], label=label)
    axes[0].set(xlabel=r"$\beta_4$", ylabel=r"$|\epsilon_b-\epsilon_a|$ (MeV)")
    axes[1].set(xlabel=r"$\beta_4$", ylabel="octupole mixing probability")
    for axis in axes: axis.grid(alpha=0.25); axis.legend(fontsize=8)
    fig.tight_layout(); fig.savefig(OUT / "orbital_beta4_response.png", dpi=180); plt.close(fig)


def main() -> None:
    surface_rows = []
    for b2 in BETA2_VALUES:
        for b4 in BETA4_GRID:
            vals = pes(BETA3_GRID, b4, float(b2))
            for q, value in zip(BETA3_GRID, vals):
                surface_rows.append({"beta2": float(b2), "beta3": float(q), "beta4": float(b4), "V_MeV": float(value)})

    mep_rows = []
    mep_summaries = []
    for b2 in BETA2_VALUES:
        x, b4, v, v_shift = mep_curve(float(b2))
        for q, b4q, value, shifted in zip(x, b4, v, v_shift):
            mep_rows.append({"beta2": float(b2), "beta3": float(q), "beta4_mep": float(b4q), "V_MeV": float(value), "V_shifted_MeV": float(shifted)})
        mep_summaries.append(mep_summary(float(b2)))

    fixed_rows = []
    for b2 in BETA2_VALUES:
        for b4 in BETA4_SCAN:
            q, vmin, barrier = positive_minimum(float(b2), float(b4))
            exact = schrodinger(float(b2), float(b4))
            # A WKB comparison using the fixed-beta4 potential and the exact
            # ground-state energy from that same one-dimensional Hamiltonian.
            x = SCHROD_GRID
            v = pes(x, float(b4), float(b2)); v_shift = v - float(v.min())
            # Temporarily use a local fixed-mode calculation for E0.
            e0 = exact["E_even_MeV"]
            forbidden = (x >= 0.0) & (x <= q) & (v_shift > e0)
            if np.any(forbidden):
                action = 2.0 * float(np.trapezoid(np.sqrt(np.maximum((v_shift[forbidden] - e0) / H2_OVER_2B33, 0.0)), x[forbidden]))
                curv = curvature_at_minimum(float(b2), float(b4), q)
                omega = math.sqrt(max(2.0 * H2_OVER_2B33 * curv, 0.0))
                wkb_delta = omega / math.pi * math.exp(-action)
                wkb_ok = True
            else:
                action, wkb_delta, wkb_ok = None, None, False
            fixed_rows.append({
                "beta2": float(b2),
                "beta4": float(b4),
                "beta3_min": q,
                "V_barrier_MeV": float(barrier),
                "V_min_MeV": float(vmin),
                "DeltaE_exact_MeV": exact["DeltaE_odd_minus_even_MeV"],
                "DeltaE_WKB_MeV": wkb_delta,
                "WKB_action_S_over_hbar": action,
                "WKB_applicable": wkb_ok,
                "even_parity_expectation": exact["even_parity_expectation"],
                "odd_parity_expectation": exact["odd_parity_expectation"],
            })

    # Add the fully minimized MEP parity result as a separate, clearly labeled
    # table row rather than pretending that beta4 is a measured constant.
    mep_parity_rows = []
    for summary in mep_summaries:
        exact = schrodinger(summary["beta2"], "mep")
        x, b4, v, v_shift = mep_curve(summary["beta2"], SCHROD_GRID)
        wkb = wkb_from_curve(x, v_shift, summary["beta2"], summary["beta3_min"])
        mep_parity_rows.append({**summary, **exact, **wkb, "mode": "MEP_beta4_minimized"})

    orbital_rows = []
    for b2 in BETA2_VALUES:
        for b4 in BETA4_SCAN:
            fixed = next(r for r in fixed_rows if abs(r["beta2"] - b2) < 1e-12 and abs(r["beta4"] - b4) < 1e-12)
            for pair in ORBITAL_PAIRS:
                orbital_rows.append(orbital_row(pair, float(b2), float(b4), fixed["beta3_min"]))

    # Aggregate sensitivity slopes over beta4>=0, keeping the parameter
    # dependence visible instead of reducing it to one universal coefficient.
    sensitivity = []
    for b2 in BETA2_VALUES:
        rows = [r for r in fixed_rows if abs(r["beta2"] - b2) < 1e-12 and r["beta4"] >= 0.0]
        x = np.array([r["beta4"] for r in rows])
        barrier = np.array([r["V_barrier_MeV"] for r in rows])
        qmin = np.array([r["beta3_min"] for r in rows])
        split = np.array([r["DeltaE_exact_MeV"] for r in rows])
        sensitivity.append({
            "beta2": float(b2),
            "dV_barrier_d_beta4_MeV": float(np.polyfit(x, barrier, 1)[0]),
            "dbeta3_min_d_beta4": float(np.polyfit(x, qmin, 1)[0]),
            "dlog10_DeltaE_d_beta4": float(np.polyfit(x, np.log10(split), 1)[0]),
            "barrier_at_beta4_0_MeV": float(barrier[0]),
            "barrier_at_beta4_0p04_MeV": float(np.interp(0.04, x, barrier)),
            "beta3_min_at_beta4_0": float(qmin[0]),
            "beta3_min_at_beta4_0p04": float(np.interp(0.04, x, qmin)),
        })

    write_csv(OUT / "pes_grid.csv", surface_rows)
    write_csv(OUT / "mep_path.csv", mep_rows)
    write_csv(OUT / "fixed_beta4_scan.csv", fixed_rows)
    write_csv(OUT / "mep_parity_splitting.csv", mep_parity_rows)
    write_csv(OUT / "orbital_beta4_scan.csv", orbital_rows)
    write_csv(OUT / "sensitivity_summary.csv", sensitivity)

    convergence_rows = []
    for n_grid in (321, 641, 1281):
        grid = np.linspace(-0.32, 0.32, n_grid)
        diag_result = schrodinger(0.175, "mep", grid=grid)
        convergence_rows.append({
            "beta2": 0.175,
            "grid_points": n_grid,
            "grid_step": float(grid[1] - grid[0]),
            "DeltaE_exact_MeV": diag_result["DeltaE_odd_minus_even_MeV"],
            "even_parity_expectation": diag_result["even_parity_expectation"],
            "odd_parity_expectation": diag_result["odd_parity_expectation"],
        })
    write_csv(OUT / "schrodinger_grid_convergence.csv", convergence_rows)

    # Explicit checks requested by the model contract.
    symmetry_errors = []
    for b2 in BETA2_VALUES:
        for b4 in BETA4_SCAN:
            symmetry_errors.append(
                float(np.max(np.abs(pes(BETA3_GRID, b4, float(b2)) - pes(-BETA3_GRID, b4, float(b2)))))
            )
    positive_mep = all(r["beta4_at_beta3_min"] >= -1e-12 for r in mep_summaries)
    coupling_off_max = max(abs(beta4_mep(float(q), float(b2), coupling_scale=0.0)) for b2 in BETA2_VALUES for q in BETA3_GRID)
    coupling_sign_flip_max = max(
        abs(beta4_mep(float(q), float(b2), coupling_scale=1.0) + beta4_mep(float(q), float(b2), coupling_scale=-1.0))
        for b2 in BETA2_VALUES for q in BETA3_GRID
    )
    reference = {
        "beta2": 0.175,
        "fixed_beta4_rows": [r for r in fixed_rows if abs(r["beta2"] - 0.175) < 1e-12 and abs(r["beta4"] - 0.04) < 1e-12],
        "mep_row": next(r for r in mep_parity_rows if abs(r["beta2"] - 0.175) < 1e-12),
    }
    result = {
        "model": "beta2-beta3-beta4 Landau PES + one-dimensional beta3 Schrodinger + two-level orbital surrogate",
        "status": "model-result; not a calibrated Woods-Saxon/Nilsson/HFB/EDF prediction",
        "nuclei_context": ["224Ra", "226Ra", "226Th", "228Th"],
        "units": {"beta": "dimensionless", "energy": "MeV", "parity_splitting": "MeV", "orbital_overlap": "dimensionless"},
        "formulas": {
            "PES": "V=1/2*a3*b3^2+1/4*b3c*b3^4+1/6*c3*b3^6+1/2*k4*b4^2+1/4*u4*b4^4-G234*b2*b3^2*b4",
            "MEP": "beta4*(beta3) solves k4*beta4+u4*beta4^3=G234*beta2*beta3^2",
            "single_particle": "E+-=(eps_a+eps_b)/2 +/- sqrt((delta/2)^2+(v3*beta3)^2)",
            "WKB": "S/hbar=int d beta3 sqrt((V-E0)/(hbar^2/(2B33))); DeltaE=(hbar omega/pi)*exp(-S/hbar)",
        },
        "parameters": {"landau": LANDau, "hbar2_over_2B33_MeV": H2_OVER_2B33, "beta2_values": BETA2_VALUES.tolist(), "beta4_scan": BETA4_SCAN.tolist(), "orbital_pairs": ORBITAL_PAIRS},
        "mep_summaries": mep_summaries,
        "sensitivity_summary": sensitivity,
        "reference": reference,
        "checks": {
            "max_PES_reflection_symmetry_error_MeV": max(symmetry_errors),
            "MEP_beta4_nonnegative_at_finite_beta3": positive_mep,
            "coupling_off_MEP_beta4_max_abs": coupling_off_max,
            "coupling_sign_reversal_MEP_beta4_error": coupling_sign_flip_max,
            "WKB_exact_splitting_same_units": True,
        },
        "evidence_boundary": {
            "direct_experiment": "Existing local source pages constrain strong E3/Q3, parity-band systematics and model context; they do not provide a beta4-resolved PES for all four target nuclei.",
            "author_model": "Gogny/mean-field source pages identify 224Ra and 226Th as strong-octupole candidates but retain softness and model dependence.",
            "task_inference": "The beta4 stabilization, orbital response, WKB and exact diagonalization values here are reduced-model diagnostics.",
        },
    }
    parameter_manifest = {
        "model": result["model"],
        "status": result["status"],
        "landau": LANDau,
        "hbar2_over_2B33_MeV": H2_OVER_2B33,
        "beta2_values": BETA2_VALUES.tolist(),
        "beta3_grid": [float(BETA3_GRID[0]), float(BETA3_GRID[-1]), len(BETA3_GRID)],
        "beta4_grid": [float(BETA4_GRID[0]), float(BETA4_GRID[-1]), len(BETA4_GRID)],
        "beta4_scan": BETA4_SCAN.tolist(),
        "schrodinger_grid": [float(SCHROD_GRID[0]), float(SCHROD_GRID[-1]), len(SCHROD_GRID)],
        "orbital_pairs": ORBITAL_PAIRS,
    }
    (OUT / "parameters.json").write_text(json.dumps(parameter_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "results.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    make_plots(surface_rows, fixed_rows, orbital_rows, mep_rows)


if __name__ == "__main__":
    main()
