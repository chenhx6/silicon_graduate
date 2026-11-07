#!/usr/bin/env python3
"""Plot the conditional Table I reduction and a two-error covariance scenario."""
import argparse
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    root = Path(__file__).resolve().parents[2]
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--directory", type=Path, default=root / "outputs/l4/20261107-isomer-cross-region-round2/ru100")
    args = p.parse_args()
    data = json.loads((args.directory / "results.json").read_text())
    points = [v for v in data["conditional_rotor_results"] if v["assumed_K"] == 0]
    plt.rcParams.update({"font.size": 10, "svg.fonttype": "none", "pdf.fonttype": 42})
    fig, axes = plt.subplots(1, 2, figsize=(11.3, 4.3), constrained_layout=True)
    ax = axes[0]
    for parity, color, marker, band in [("+", "#2166ac", "o", 2), ("-", "#b35806", "s", 3)]:
        rows = sorted((r for r in points if r["parity"] == parity), key=lambda r: r["spin"])
        low = [r["d0_efm"] - r["d0_mapped_B_minus_error_efm"] for r in rows]
        high = [r["d0_mapped_B_plus_error_efm"] - r["d0_efm"] for r in rows]
        ax.errorbar([r["spin"] for r in rows], [r["d0_efm"] for r in rows],
                    yerr=[low, high], fmt=marker, color=color, capsize=3,
                    label=f"Band {band} ({parity})")
    ax.fill_between([12.5, 16.5], [.03, .03], [.05, .05], color="#777777", alpha=.12,
                    label="Author group values +/- quoted error")
    ax.fill_between([16.5, 18.5], [.05, .05], [.09, .09], color="#777777", alpha=.12)
    ax.plot([12.5, 16.5], [.04, .04], color="#777777", ls="--")
    ax.plot([16.5, 18.5], [.07, .07], color="#777777", ls="--")
    ax.set(xlabel=r"Spin $I$ ($\hbar$)", ylabel=r"Conditional $|D_0|$ ($e$ fm)",
           title="(a) Axial K=0 reduction of six finite entries", xlim=(12.5, 18.5))
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(alpha=.2)
    ax.text(.02, .02, "Error bars map reported B(E1) +/- error.\n"
            "No measured K or full covariance is supplied.", transform=ax.transAxes, fontsize=8)
    ax = axes[1]
    rho = [-1 + 2*k/300 for k in range(301)]
    standardized = [.03/math.sqrt(.01**2+.02**2-2*r*.01*.02) for r in rho]
    ax.plot(rho, standardized, color="#762a83", lw=2)
    ax.axvline(0, color="grey", ls=":")
    ax.scatter([0], [3/math.sqrt(5)], color="#762a83", zorder=3)
    ax.annotate("1.34 at rho=0", xy=(0, 3/math.sqrt(5)), xytext=(.15, 1.14),
                arrowprops={"arrowstyle": "-", "color": "grey"}, fontsize=9)
    ax.set(xlabel=r"Assumed correlation $\rho$ between quoted group errors",
           ylabel="Standardized difference (not an assigned significance)",
           title="(b) Sensitivity of the quoted 0.04 / 0.07 contrast", xlim=(-1, 1), ylim=(.9, 3.1))
    ax.grid(alpha=.2)
    ax.text(.03, .94, "Marginal group errors: 0.01 and 0.02 e fm\n"
            "Correlation is unknown; curve is a scenario calculation.",
            transform=ax.transAxes, va="top", fontsize=8)
    for ext in ("png", "pdf", "svg"):
        target = args.directory / f"ru100-moments-covariance.{ext}"
        fig.savefig(target, dpi=170)
        if ext == "svg":
            target.write_text("\n".join(line.rstrip() for line in target.read_text().splitlines()) + "\n")
    plt.close(fig)


if __name__ == "__main__":
    main()
