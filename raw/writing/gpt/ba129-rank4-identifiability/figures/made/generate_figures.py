#!/usr/bin/env python3
"""Generate the rank-4 companion-line diagnostic figure."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def load_points(path: Path) -> dict[str, dict[str, float]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    return {
        row["label"]: {key: float(row[key]) for key in ("A4", "A4_sigma")}
        for row in rows
    }


def write_plot(results_path: Path, output: Path) -> None:
    results = json.loads(results_path.read_text(encoding="utf-8"))
    points = load_points(
        results_path.parents[2] / "data" / "ba129_same_parent_A4.csv"
    )
    target = points["target_365"]
    reference = points["reference_462"]
    ratio = float(results["algebra"]["F4_ratio"])

    plt.rcParams.update(
        {
            "font.size": 9,
            "axes.labelsize": 10,
            "axes.titlesize": 10,
            "legend.fontsize": 8,
            "figure.dpi": 160,
        }
    )
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.1))
    fig.subplots_adjust(left=0.09, right=0.99, bottom=0.22, top=0.78, wspace=0.34)

    ax = axes[0]
    names = ["365-keV target", "461.6-keV reference"]
    values = [target["A4"], reference["A4"]]
    errors = [target["A4_sigma"], reference["A4_sigma"]]
    x = np.arange(2)
    ax.errorbar(
        x,
        values,
        yerr=errors,
        fmt="o",
        ms=5,
        capsize=3,
        color="#173f5f",
        lw=1.2,
    )
    ax.axhline(0, color="0.35", lw=0.8)
    ax.set_xticks(x, names, rotation=20, ha="right")
    ax.set_ylabel(r"Published $A_4$")
    ax.set_title("(a) Same-parent summary coefficients")
    ax.set_ylim(-0.08, 0.29)
    ax.grid(axis="y", alpha=0.25)

    ax = axes[1]
    ref_grid = np.linspace(-0.12, 0.22, 600)
    f_grid = np.linspace(0, 1, 200)
    for f in (0.0, 0.25, 0.5, 0.75, 1.0):
        ax.plot(
            ref_grid,
            ratio * f * ref_grid,
            color="#2a9d8f",
            alpha=0.22 if f not in (0.0, 1.0) else 0.7,
            lw=1.0 if f not in (0.0, 1.0) else 1.4,
        )
    envelope_lo = np.minimum(ratio * ref_grid, 0)
    envelope_hi = np.maximum(ratio * ref_grid, 0)
    ax.fill_between(
        ref_grid,
        envelope_lo,
        envelope_hi,
        color="#2a9d8f",
        alpha=0.08,
        label=r"$0\leq f_{E2}\leq1$, $s_4=1$",
    )
    ax.errorbar(
        [reference["A4"]],
        [target["A4"]],
        xerr=[reference["A4_sigma"]],
        yerr=[target["A4_sigma"]],
        fmt="o",
        ms=5,
        capsize=3,
        color="#d1495b",
        label="public summary point",
    )
    ax.axhline(0, color="0.35", lw=0.8)
    ax.axvline(0, color="0.35", lw=0.8)
    ax.set_xlabel(r"Reference $A_4^{(r)}$")
    ax.set_ylabel(r"Target $A_4^{(t)}$")
    ax.set_title(r"(b) Conditional rank-4 gate")
    ax.set_xlim(-0.12, 0.22)
    ax.set_ylim(-0.30, 0.34)
    ax.grid(alpha=0.2)
    ax.legend(loc="upper left", frameon=False)
    ax.text(
        0.02,
        0.04,
        r"$A_4^{(t)}=-\frac{8}{3}f_{E2}s_4A_4^{(r)}$",
        transform=ax.transAxes,
        color="#1d6f66",
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches="tight")
    fig.savefig(output.with_suffix(".png"), dpi=300, bbox_inches="tight")
    plt.close(fig)

    data_dir = output.parent / "made" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    with (data_dir / "rank4_relation_curve.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["A4_reference", "A4_target_f0", "A4_target_f1"])
        for ref, f0, f1 in zip(ref_grid, np.zeros_like(ref_grid), ratio * ref_grid):
            writer.writerow([f"{ref:.8g}", f"{f0:.8g}", f"{f1:.8g}"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    write_plot(args.results, args.output)
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
