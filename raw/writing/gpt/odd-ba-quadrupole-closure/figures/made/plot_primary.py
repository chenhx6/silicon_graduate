#!/usr/bin/env python3
"""Plot the frozen model results; no smoothing, fit, or angle clipping.

The main source data are data/results/calibrated-chain.json. CSV files under
figures/made/data are disposable plot views of those data, not independent
observations. All points are model predictions; no confidence band is inferred.
"""
import csv
import argparse
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "data/results/calibrated-chain.json"
FIGURES = ROOT / "figures"
CACHE = Path(__file__).resolve().parent / "data/v4"
DATA = json.loads(SOURCE.read_text())
CASES = DATA["cases"]
A = np.array([c["case"]["odd_A"] for c in CASES])
STYLE = {
    "font.size": 10, "axes.labelsize": 11, "legend.fontsize": 9.5,
    "xtick.labelsize": 10, "ytick.labelsize": 10,
    "font.family": "DejaVu Sans", "pdf.fonttype": 42,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.linewidth": .7, "lines.linewidth": 1.3,
    "savefig.facecolor": "white",
}


def save(fig, name):
    for ext in ("pdf", "png"):
        path = FIGURES / f"{name}.{ext}"
        if path.exists():
            raise FileExistsError(f"Version the figure instead of overwriting: {path}")
        fig.savefig(path, dpi=220)
    plt.close(fig)


def primary():
    q2 = [c["primary"]["full"]["q2_e2b2"] for c in CASES]
    r = [c["primary"]["full"]["signed_ratio"] for c in CASES]
    z5 = [c["primary"]["restricted"][1]["raw_proxy_ratio"] for c in CASES]
    za = [c["primary"]["restricted"][-1]["raw_proxy_ratio"] for c in CASES]
    with plt.rc_context(STYLE):
        fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.85), layout="constrained")
        ax = axes[0]
        ax.plot(A, q2, "o-", color="#0072B2", markersize=5)
        ax.set(xlabel="Odd Ba mass number A", ylabel=r"$q_2$ ($e^2\,b^2$)",
               xticks=A, ylim=(0, 1.75))
        ax.set_title("(a)", loc="left", fontsize=10)
        ax = axes[1]
        ax.axhspan(1., 1.17, color="#BDBDBD", alpha=.35)
        ax.axhline(1., color=".4", lw=.7, ls=":")
        ax.axhline(0., color=".65", lw=.5)
        ax.plot(A, r, "o-", color="#0072B2", label=r"Complete $r$")
        ax.plot(A, z5, "s--", color="#D55E00", markersize=4, label=r"$J+2$: $n=5$")
        ax.plot(A, za, "^:", color="#333333", mfc="white", markersize=5,
                label=r"$J+2$: all")
        ax.set(xlabel="Odd Ba mass number A", ylabel="Cubic ratio",
               xticks=A, ylim=(-.24, 1.17))
        ax.set_title("(b)", loc="left", fontsize=10)
        ax.text(128.7, 1.075, r"$z>1$: no real angle", fontsize=9.5)
        ax.legend(loc="center left", frameon=False)
        save(fig, "charge_and_ratios-v4")
    with (CACHE / "primary-view.csv").open("x", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["A", "q2_e2b2", "signed_full_ratio", "proxy_n5_ratio", "proxy_all_ratio"])
        writer.writerows(zip(A, q2, r, z5, za))


def channels():
    spins = (7, 9, 11, 13, 15)
    # Static and excited same-spin terms are distinct, parallel pieces of q2.
    parts = []
    for tj in spins:
        if tj == 11:
            parts.append(("11/2 static", "#009E73", "//", [
                c["primary"]["same_spin"]["static_fraction_of_full_q2"] for c in CASES]))
            parts.append(("11/2 other", "#009E73", "", [
                c["primary"]["same_spin"]["other_same_spin_fraction_of_full_q2"] for c in CASES]))
        else:
            colour = {7: "#56B4E9", 9: "#E69F00", 13: "#CC79A7", 15: "#333333"}[tj]
            parts.append((f"{tj}/2", colour, "", [
                next(x["fraction_of_full"] for x in c["primary"]["quadratic_channels"]
                     if x["two_J"] == tj) for c in CASES]))
    case = next(c for c in CASES if c["case"]["odd_A"] == 135)
    matrix = np.zeros((5, 5))
    for pair in case["primary"]["signed_cubic_spin_pairs"]:
        matrix[spins.index(pair["two_Ja"]), spins.index(pair["two_Jb"])] = (
            pair["normalized_to_q2_power_3_over_2"])
    with plt.rc_context(STYLE):
        fig, axes = plt.subplots(1, 2, figsize=(7.1, 3.65), layout="constrained",
                                 gridspec_kw={"width_ratios": [1.05, 1]})
        ax = axes[0]
        bottom = np.zeros(5)
        for label, colour, hatch, values in parts:
            values = 100 * np.asarray(values)
            ax.bar(A, values, bottom=bottom, width=1.25, color=colour,
                   edgecolor="white", linewidth=.5, label=label, hatch=hatch)
            bottom += values
        ax.set(xlabel="Odd Ba mass number A", ylabel=r"Fraction of complete $q_2$ (%)",
               xticks=A, ylim=(0, 100))
        ax.set_title("(a)", loc="left", fontsize=10)
        ax.legend(ncol=3, frameon=False, loc="lower center", bbox_to_anchor=(.5, 1.12),
                  columnspacing=.7, handlelength=1.2, fontsize=9.5)
        ax = axes[1]
        image = ax.imshow(matrix, cmap="RdBu_r", vmin=-.24, vmax=.24)
        ax.set(xticks=np.arange(5), yticks=np.arange(5),
               xticklabels=[f"{s}/2" for s in spins],
               yticklabels=[f"{s}/2" for s in spins],
               xlabel=r"Intermediate spin $J_b$", ylabel=r"Intermediate spin $J_a$")
        ax.set_title("(b)", loc="left", fontsize=10)
        for i in range(5):
            for j in range(5):
                x = matrix[i, j]
                text = "0" if abs(x) < 1e-12 else f"{x:.3f}"
                ax.text(j, i, text, ha="center", va="center", fontsize=9.5,
                        color="white" if abs(x) > .15 else "black")
        fig.colorbar(image, ax=ax, shrink=.75, label=r"$q_3(J_a,J_b)/q_2^{3/2}$")
        save(fig, "angular_channels-v4")
    with (CACHE / "135Ba-cubic-view.csv").open("x", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["two_Ja", "two_Jb", "normalized_signed_cubic"])
        for i, a in enumerate(spins):
            for j, b in enumerate(spins):
                writer.writerow([a, b, matrix[i, j]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        help="New directory for figures and derived plot views")
    args = parser.parse_args()
    if args.output_dir is not None:
        FIGURES = args.output_dir.resolve()
        FIGURES.mkdir(parents=True, exist_ok=False)
        CACHE = FIGURES / "data"
    CACHE.mkdir(parents=True, exist_ok=True)
    primary()
    channels()
    report = {
        "input": str(SOURCE.relative_to(ROOT)),
        "sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "transformations": [
            "Read frozen model outputs with no fit or smoothing.",
            "Display the complete signed ratio and the restricted absolute ratios separately.",
            "Plot values >1 as measured by the computation; no clipped angle.",
            "Split same-spin strength into static and other states.",
            "Normalize signed cubic spin-pair contributions by the same full q2^(3/2).",
        ],
        "uncertainty": "No inferred error bars. Five deterministic model cases, not five experimental replicates.",
        "figure_dimensions_inches": {"charge_and_ratios-v4": [7.1, 2.85], "angular_channels-v4": [7.1, 3.65]},
    }
    with (CACHE / "plot-record.json").open("x") as stream:
        json.dump(report, stream, indent=2)
        stream.write("\n")
