#!/usr/bin/env python3
"""
plot_phase_boundaries.py
Generates publication-quality plots (PNG/SVG) for the 4 inapplicability criteria
and the multimodal phase boundary topology.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import json
from pathlib import Path

WORKER_DIR = Path(__file__).resolve().parent

def plot_all():
    # 1. Plot Core Masking Ratio
    with open(WORKER_DIR / "core_quadrupole_masking.json", "r", encoding="utf-8") as f:
        data_masking = json.load(f)["summary_by_beta"]

    beta_vals = [d["beta2"] for d in data_masking]
    r_30 = [d["R_E2_theta_30"] for d in data_masking]
    r_60 = [d["R_E2_theta_60"] for d in data_masking]
    r_90 = [d["R_E2_theta_90"] for d in data_masking]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(beta_vals, r_30, label=r'$\theta = 30^\circ$ (Closing / Band termination)', color='crimson', lw=2)
    ax.plot(beta_vals, r_60, label=r'$\theta = 60^\circ$ (Intermediate shears)', color='darkorange', lw=2)
    ax.plot(beta_vals, r_90, label=r'$\theta = 90^\circ$ (Open shears)', color='navy', lw=2)
    ax.axhline(15.0, color='gray', linestyle='--', label='Masking onset threshold (R=15)')
    ax.axhline(50.0, color='black', linestyle=':', label='Complete core masking (R=50)')
    ax.axvline(0.25, color='darkgreen', linestyle='-.', label=r'Rare-earth boundary ($\beta_2 = 0.25$)')
    ax.set_yscale('log')
    ax.set_xlabel(r'Quadrupole Deformation $\beta_2$', fontsize=12)
    ax.set_ylabel(r'$R_{E2} = B(E2)_{\rm core} / B(E2)_{\rm shears}$', fontsize=12)
    ax.set_title('Criterion 1: Core Quadrupole Collective Masking of Shears Dynamics', fontsize=13)
    ax.grid(True, which="both", ls="--", alpha=0.5)
    ax.legend(loc='upper left', fontsize=9)
    plt.tight_layout()
    plt.savefig(WORKER_DIR / "core_quadrupole_masking.png", dpi=150)
    plt.close()
    print("  -> Saved core_quadrupole_masking.png")

    # 2. Plot Anharmonic Wobbling Damping
    with open(WORKER_DIR / "anharmonic_wobbling_damping.json", "r", encoding="utf-8") as f:
        data_wob = json.load(f)

    sg_vals = [d["sigma_gamma_deg"] for d in data_wob]
    damp_vals = [d["damping_ratio_Gamma_over_omega"] for d in data_wob]
    anharm_vals = [abs(d["anharmonicity_alpha"]) for d in data_wob]

    fig, ax1 = plt.subplots(figsize=(8, 5))
    color = 'tab:red'
    ax1.set_xlabel(r'Dynamic $\gamma$-Softness Width $\sigma_\gamma$ (deg)', fontsize=12)
    ax1.set_ylabel(r'Damping Ratio $\Gamma_{\rm wob} / \hbar\omega_{\rm wob}$', color=color, fontsize=12)
    line1 = ax1.plot(sg_vals, damp_vals, color=color, lw=2.5, label=r'Damping Ratio $\Gamma/\omega$')
    ax1.axhline(0.50, color='red', linestyle='--', label='Overdamped Boundary (0.50)')
    ax1.axvline(17.32, color='purple', linestyle=':', label=r'Wilets-Jean Flat Softness ($17.3^\circ$)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, ls="--", alpha=0.5)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel(r'Anharmonicity $|\alpha| = |(E_2 - 2E_1)/E_1|$', color=color, fontsize=12)
    line2 = ax2.plot(sg_vals, anharm_vals, color=color, lw=2, linestyle='--', label='Anharmonicity $|\alpha|$')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title(r'Criterion 3: Anharmonic Damping of Wobbling Phonons vs $\gamma$-Softness', fontsize=13)
    plt.tight_layout()
    plt.savefig(WORKER_DIR / "anharmonic_wobbling_damping.png", dpi=150)
    plt.close()
    print("  -> Saved anharmonic_wobbling_damping.png")

    # 3. Plot Phase Boundary Topology in (beta2, gamma)
    with open(WORKER_DIR / "phase_boundary_topology.json", "r", encoding="utf-8") as f:
        data_topo = json.load(f)["grid_points"]

    fig, ax = plt.subplots(figsize=(9, 6))

    # Group coordinates by classification
    categories = {}
    for pt in data_topo:
        cat = pt["classification"]
        if cat not in categories:
            categories[cat] = {"beta2": [], "gamma": []}
        categories[cat]["beta2"].append(pt["beta2"])
        categories[cat]["gamma"].append(pt["gamma_deg"])

    color_map = {
        "MR_exclusive": "navy",
        "AMR_exclusive": "cyan",
        "Chiral_exclusive": "magenta",
        "Wobbling_exclusive": "darkorange",
        "Chiral_Wobbling_coexistence": "purple",
        "MR_AMR_coexistence": "teal",
        "Conventional_Core_Rotation": "gray",
        "Spherical_Vibrator": "lightgreen"
    }

    for cat, coords in categories.items():
        c = color_map.get(cat, "black")
        label = cat.replace("_", " ")
        ax.scatter(coords["gamma"], coords["beta2"], label=label, color=c, s=18, alpha=0.7)

    ax.set_xlabel(r'Triaxiality $\gamma$ (degrees)', fontsize=12)
    ax.set_ylabel(r'Quadrupole Deformation $\beta_2$', fontsize=12)
    ax.set_title(r'Phase Boundary Topology of Collective Modes in $(\beta_2, \gamma)$ Space', fontsize=13)
    ax.set_xlim(-2, 62)
    ax.set_ylim(0.03, 0.42)
    ax.grid(True, ls="--", alpha=0.4)
    ax.legend(bbox_to_anchor=(1.04, 1), loc="upper left", fontsize=9)
    plt.tight_layout()
    plt.savefig(WORKER_DIR / "phase_boundary_topology.png", dpi=150)
    plt.close()
    print("  -> Saved phase_boundary_topology.png")

if __name__ == "__main__":
    plot_all()
