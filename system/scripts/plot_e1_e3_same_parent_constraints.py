#!/usr/bin/env python3
"""Plot central published-branch reconstructions, with conditional labels."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    args.output.mkdir(parents=True, exist_ok=True)
    with plt.rc_context({"font.size": 10, "svg.fonttype": "none"}):
        fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.7), constrained_layout=True)
        for nucleus, color, marker in [("98Mo", "#0072B2", "o"), ("100Ru", "#D55E00", "s")]:
            rows = sorted((r for r in data["rows"] if r["nucleus"] == nucleus), key=lambda r: r["initial_spin"])
            x = [r["initial_spin"] for r in rows]
            for ax, key in zip(axes, [
                "B_E1_over_B_E3_fm_minus4",
                "conditional_K0_intrinsic_amplitude_ratio_squared_fm_minus4",
            ]):
                ax.plot(x, [r[key]*1e9 for r in rows], color=color,
                        marker=marker, label=nucleus, linewidth=1.3, markersize=6)
                ax.set_xticks([5, 7], [r"$5^-$", r"$7^-$"])
                ax.set_xlabel("Initial spin")
                ax.grid(axis="y", alpha=.22)
        axes[0].set_title("Same-parent photon branches")
        axes[0].set_ylabel(r"$B(E1)/B(E3)$  [$10^{-9}$ fm$^{-4}$]")
        axes[1].set_title(r"Conditional axial $K=0$ mapping")
        axes[1].set_ylabel(r"$|t_1/t_3|^2$ proxy  [$10^{-9}$ fm$^{-4}$]")
        axes[0].legend(frameon=False)
        fig.suptitle("Central reconstructions; joint covariance unavailable", fontsize=11)
        for suffix in ["pdf", "svg", "png"]:
            artifact = args.output/f"e1-e3-central-constraints.{suffix}"
            fig.savefig(artifact, dpi=220,
                        metadata={"Creator": "same-parent E1/E3 published-branch analysis"}
                        if suffix == "pdf" else None)
            if suffix == "svg":
                artifact.write_text("\n".join(line.rstrip() for line in artifact.read_text().splitlines()) + "\n")
        plt.close(fig)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
