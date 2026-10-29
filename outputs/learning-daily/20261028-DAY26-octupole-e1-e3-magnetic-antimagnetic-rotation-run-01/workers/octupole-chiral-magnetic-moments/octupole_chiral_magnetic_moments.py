#!/usr/bin/env python3
"""Minimal four-state octupole--chiral magnetic-moment model.

The calculation is deliberately phenomenological.  It keeps the two local
labels chi=+/-1 (left/right) and p=+/-1 (intrinsic parity well), diagonalises
a 4 by 4 tunnelling Hamiltonian at fixed I, and evaluates a magnetic-moment
operator in units of mu_N.  No number in the output is an experimental value.

The script is self contained apart from NumPy and Matplotlib (the latter is
optional).  It writes a flat CSV, a JSON record, and an SVG plot.
"""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent


def basis_labels():
    # The order is chosen to make the requested relation transparent:
    # 1=(chi=+,p=+), 2=(chi=-,p=+), 3=(chi=-,p=-), 4=(chi=+,p=-).
    return [(1, 1), (-1, 1), (-1, -1), (1, -1)]


def four_state_matrices(t_chi, t_parity, t_mix, diagonal, offdiag_scale=0.0):
    labels = basis_labels()
    H = np.zeros((4, 4), dtype=float)
    M = np.diag(np.asarray(diagonal, dtype=float))
    for a, (chi_a, p_a) in enumerate(labels):
        for b, (chi_b, p_b) in enumerate(labels):
            if a >= b:
                continue
            if chi_a == -chi_b and p_a == p_b:
                H[a, b] = H[b, a] = -t_chi
            elif chi_a == chi_b and p_a == -p_b:
                H[a, b] = H[b, a] = -t_parity
            elif chi_a == -chi_b and p_a == -p_b:
                H[a, b] = H[b, a] = -t_mix
    # A small off-diagonal magnetic kernel is retained to expose coherent
    # interference; setting it to zero gives the purely diagonal limit.
    if offdiag_scale:
        for a, (chi_a, p_a) in enumerate(labels):
            for b, (chi_b, p_b) in enumerate(labels):
                if a < b and chi_a == -chi_b and p_a == -p_b:
                    M[a, b] = M[b, a] = offdiag_scale * chi_a * p_a
    return H, M


def decoupling(I, beta3, parity, cfg):
    """Return b0^p and its magnetic-moment correction.

    The sign convention is the standard K=1/2 phenomenology
    E_dec=A*b0*(-1)^(I+1/2)*(I+1/2).  The magnetic correction below is a
    declared proxy for the K=1/2 wave-function admixture, not a universal
    identity: delta_mu_dec = c_mu*b0*(-1)^(I+1/2)/(I+1).
    """
    theta = 0.5 * math.atan2(2.0 * beta3 * cfg["v_oct"], cfg["delta_eps"])
    b0 = cfg["b0_base"] + parity * cfg["b0_mix"] * math.sin(2.0 * theta)
    phase = (-1.0) ** int(round(I + 0.5))
    energy = cfg["A_rot"] * b0 * phase * (I + 0.5)
    mu_corr = cfg["c_mu"] * b0 * phase / (I + 1.0)
    return b0, energy, mu_corr, theta


def local_moment(I, beta3, barrier, chi, parity, cfg):
    g_r = cfg["g_R"]
    K = 0.5
    theta = 0.5 * math.atan2(2.0 * beta3 * cfg["v_oct"], cfg["delta_eps"])
    g_k = cfg["g_K0"] + parity * cfg["g_K_split"] * math.sin(2.0 * theta)
    core = g_r * I
    intrinsic = (g_k - g_r) * K * K / (I + 1.0)
    b0, dec_energy, dec_mu, _ = decoupling(I, beta3, parity, cfg)
    chiral = chi * cfg["m_chi"] * math.tanh(barrier)
    parity_term = parity * cfg["m_parity"] * beta3
    interference = chi * parity * cfg["m_chip"] * beta3 * math.tanh(barrier)
    return {
        "mu_core": core,
        "mu_intrinsic": intrinsic,
        "mu_decoupling": dec_mu,
        "mu_chiral": chiral,
        "mu_parity": parity_term,
        "mu_interference": interference,
        "mu_local": core + intrinsic + dec_mu + chiral + parity_term + interference,
        "g_K": g_k,
        "b0": b0,
        "decoupling_energy": dec_energy,
        "mixing_angle": theta,
    }


def calculate(I, beta3, barrier, cfg):
    labels = basis_labels()
    local = [local_moment(I, beta3, barrier, chi, p, cfg) for chi, p in labels]
    diagonal = [x["mu_local"] for x in local]
    t_chi = cfg["t_chi0"] * math.exp(-cfg["barrier_chi"] * barrier)
    t_parity = cfg["t_parity0"] * math.exp(-cfg["barrier_parity"] * barrier)
    t_mix = cfg["t_mix0"] * beta3 * math.exp(-cfg["barrier_mix"] * barrier)
    H, M = four_state_matrices(
        t_chi, t_parity, t_mix, diagonal, cfg["m_offdiag"] * beta3
    )
    evals, evecs = np.linalg.eigh(H)
    mu_eigen = np.einsum("ij,ji->i", evecs.T @ M, evecs)
    d12 = diagonal[0] - diagonal[1]
    d34 = diagonal[2] - diagonal[3]
    return {
        "spin": I,
        "beta3": beta3,
        "barrier_depth": barrier,
        "t_chi": t_chi,
        "t_parity": t_parity,
        "t_chi_parity": t_mix,
        "local": local,
        "mu_local": diagonal,
        "energies": evals.tolist(),
        "mu_eigen": mu_eigen.tolist(),
        "delta_mu_12": d12,
        "delta_mu_34": d34,
        "symmetry_residual": d12 + d34,
        "interference_prediction": 4.0 * local[0]["mu_interference"],
        "hermiticity_error": float(np.max(np.abs(H - H.T))),
        "moment_hermiticity_error": float(np.max(np.abs(M - M.T))),
    }


def write_outputs(records, cfg, beta3_values, barrier_values, spins):
    csv_path = HERE / "magnetic_moment_network.csv"
    fields = [
        "spin", "beta3", "barrier_depth", "state", "chi", "parity",
        "mu_core", "mu_intrinsic", "mu_decoupling", "mu_chiral",
        "mu_parity", "mu_interference", "mu_local", "g_K", "b0",
        "decoupling_energy", "mixing_angle", "delta_mu_12", "delta_mu_34",
        "symmetry_residual", "interference_prediction", "t_chi", "t_parity",
        "t_chi_parity", "hermiticity_error", "moment_hermiticity_error",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for record in records:
            for idx, (chi, parity) in enumerate(basis_labels(), start=1):
                item = record["local"][idx - 1]
                row = {
                    "spin": record["spin"], "beta3": record["beta3"],
                    "barrier_depth": record["barrier_depth"], "state": idx,
                    "chi": chi, "parity": parity, **item,
                    "delta_mu_12": record["delta_mu_12"],
                    "delta_mu_34": record["delta_mu_34"],
                    "symmetry_residual": record["symmetry_residual"],
                    "interference_prediction": record["interference_prediction"],
                    "t_chi": record["t_chi"], "t_parity": record["t_parity"],
                    "t_chi_parity": record["t_chi_parity"],
                    "hermiticity_error": record["hermiticity_error"],
                    "moment_hermiticity_error": record["moment_hermiticity_error"],
                }
                writer.writerow(row)

    json_path = HERE / "magnetic_moment_network.json"
    payload = {
        "model": "four-state octupole-chiral magnetic moment and K=1/2 decoupling",
        "units": {"energy": "MeV", "magnetic_moment": "mu_N"},
        "state_order": {"1": "chi=+1,p=+1", "2": "chi=-1,p=+1",
                         "3": "chi=-1,p=-1", "4": "chi=+1,p=-1"},
        "parameters": cfg,
        "beta3_values": beta3_values,
        "barrier_values": barrier_values,
        "spins": spins,
        "records": records,
        "checks": {
            "max_hermiticity_error": max(r["hermiticity_error"] for r in records),
            "max_moment_hermiticity_error": max(r["moment_hermiticity_error"] for r in records),
            "max_interference_identity_error": max(
                abs(r["symmetry_residual"] - r["interference_prediction"])
                for r in records
            ),
        },
        "evidence_boundary": "synthetic forward model; no target-nucleus fit",
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    plot_path = HERE / "magnetic_moment_plot_data.csv"
    plot_fields = ["spin", "beta3", "barrier_depth", "mu1", "mu2", "mu3", "mu4",
                   "delta_mu_12", "delta_mu_34", "symmetry_residual"]
    with plot_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=plot_fields)
        writer.writeheader()
        for r in records:
            writer.writerow({
                "spin": r["spin"], "beta3": r["beta3"], "barrier_depth": r["barrier_depth"],
                "mu1": r["mu_local"][0], "mu2": r["mu_local"][1],
                "mu3": r["mu_local"][2], "mu4": r["mu_local"][3],
                "delta_mu_12": r["delta_mu_12"], "delta_mu_34": r["delta_mu_34"],
                "symmetry_residual": r["symmetry_residual"],
            })
    return payload


def make_plot(records):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        return False
    selected = [r for r in records if abs(r["beta3"] - 0.25) < 1e-12 and abs(r["barrier_depth"] - 0.5) < 1e-12]
    selected.sort(key=lambda x: x["spin"])
    x = [r["spin"] for r in selected]
    fig, axes = plt.subplots(2, 1, figsize=(7.6, 7.2), sharex=True)
    for idx, label in enumerate(["1", "2", "3", "4"]):
        axes[0].plot(x, [r["mu_local"][idx] for r in selected], marker="o", ms=2.5, label=f"mu{label}")
    axes[0].set_ylabel("local mu (mu_N)")
    axes[0].legend(ncol=4, fontsize=8)
    axes[0].grid(alpha=0.25)
    axes[1].plot(x, [r["delta_mu_12"] for r in selected], label="mu1-mu2")
    axes[1].plot(x, [r["delta_mu_34"] for r in selected], label="mu3-mu4")
    axes[1].plot(x, [r["symmetry_residual"] for r in selected], label="sum (interference)")
    axes[1].axhline(0.0, color="black", lw=0.7)
    axes[1].set_xlabel("I (hbar)")
    axes[1].set_ylabel("Delta mu (mu_N)")
    axes[1].legend(fontsize=8)
    axes[1].grid(alpha=0.25)
    fig.suptitle("Synthetic octupole--chiral magnetic-moment network")
    fig.tight_layout()
    fig.savefig(HERE / "magnetic_moment_network.svg")
    plt.close(fig)
    return True


def main():
    cfg = {
        "g_R": 0.40, "g_K0": 0.72, "g_K_split": 0.30,
        "A_rot": 0.020, "b0_base": 1.10, "b0_mix": 0.85,
        "v_oct": 0.40, "delta_eps": 1.20, "c_mu": 0.065,
        "m_chi": 0.060, "m_parity": 0.020, "m_chip": 0.035,
        "t_chi0": 0.090, "t_parity0": 0.120, "t_mix0": 0.045,
        "barrier_chi": 0.40, "barrier_parity": 0.80, "barrier_mix": 0.55,
        "m_offdiag": 0.018,
    }
    beta3_values = [0.00, 0.15, 0.25, 0.35]
    barrier_values = [0.20, 0.50, 1.00, 2.00]
    spins = [0.5 + i for i in range(16)]
    records = [calculate(I, beta3, barrier, cfg)
               for beta3 in beta3_values
               for barrier in barrier_values
               for I in spins]
    payload = write_outputs(records, cfg, beta3_values, barrier_values, spins)
    plotted = make_plot(records)
    summary = {
        "records": len(records),
        "csv": str(HERE / "magnetic_moment_network.csv"),
        "json": str(HERE / "magnetic_moment_network.json"),
        "plot_data": str(HERE / "magnetic_moment_plot_data.csv"),
        "svg": str(HERE / "magnetic_moment_network.svg") if plotted else None,
        "checks": payload["checks"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
