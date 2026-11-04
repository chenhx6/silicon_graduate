#!/usr/bin/env python3
"""Plot matched and misspecified-rho coverage grids."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).parents[2]
RESULT = ROOT / "analysis" / "results" / "coverage-grid.json"
OUT = ROOT / "figures"


def matrix(cells, rhos, rs, key):
    return np.array(
        [[next(c[key] for c in cells if c["true_rho"] == rho and c["true_r"] == r) for r in rs] for rho in rhos]
    )


def main() -> None:
    data = json.loads(RESULT.read_text())
    rhos = data["true_rho_values"]
    rs = data["true_r_values"]
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 3.8), constrained_layout=True)
    for ax, group, title in (
        (axes[0], "matched_covariance", "Matched covariance"),
        (axes[1], "rho_misspecified_to_zero", r"Fit assumes $\rho=0$"),
    ):
        z = matrix(data[group], rhos, rs, "coverage_at_q95_2d")
        im = ax.imshow(
            z,
            origin="lower",
            vmin=0.45,
            vmax=0.75,
            cmap="viridis",
            aspect="auto",
            extent=[min(rs) - 0.04, max(rs) + 0.04, min(rhos) - 0.15, max(rhos) + 0.15],
        )
        for i, rho in enumerate(rhos):
            for j, r in enumerate(rs):
                ax.text(r, rho, f"{z[i,j]:.2f}", ha="center", va="center", color="white", fontsize=8)
        ax.set_xlabel(r"true $r=\sigma/J$")
        ax.set_ylabel(r"true $\rho$")
        ax.set_title(title)
    cbar = fig.colorbar(im, ax=axes, shrink=0.85)
    cbar.set_label("Empirical coverage of single-row $q_{0.95}^{(2)}$")
    fig.suptitle("Coverage of the maximum-row alignment discrepancy")
    fig.savefig(OUT / "coverage_grid.pdf", bbox_inches="tight")
    fig.savefig(OUT / "coverage_grid.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
