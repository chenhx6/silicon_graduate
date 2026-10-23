#!/usr/bin/env python3
"""Plot literal Present Qt values and limits; conditional fits are not original CIs.

Input ledger contains all 12 negative-parity Present rows and two positive-parity
feeding rows. Reused literature cells are not independent observations. All
feeding rows are exported with an exclusion reason. No simulated observations.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

from day20_literal_trend_audit import fit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    parser.add_argument("--figure-skill-scripts", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.figure_skill_scripts))
    from audit_panel_alignment import require_matplotlib_panel_alignment

    root = Path(__file__).resolve().parents[2]
    ledger = json.loads(args.ledger.read_text())
    source = root / ledger["source"]
    raw = root / re.search(r'^raw_file: "(.*)"', source.read_text(), re.M).group(1)
    assert hashlib.sha256(raw.read_bytes()).hexdigest() == ledger["raw_sha256"]
    args.out_dir.mkdir(parents=True, exist_ok=True)
    stem = args.out_dir / "singh-present-qt-043"
    plt.rcParams.update({
        "font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"],
        "font.size": 8, "axes.labelsize": 9, "axes.titlesize": 10,
        "xtick.labelsize": 8, "ytick.labelsize": 8,
        "pdf.fonttype": 42, "svg.fonttype": "none", "axes.linewidth": .7,
        "axes.spines.top": False, "axes.spines.right": False,
        "legend.frameon": False,
    })
    # 180 mm by 100 mm, expressed in inches for Matplotlib and source auditing.
    fig, axes = plt.subplots(1, 2, figsize=(7.0866141732, 3.9370078740), sharey=True)
    fig.subplots_adjust(left=.10, right=.97, top=.85, bottom=.25, wspace=.16)
    table, results = [], {}
    colors = ["#3F6F8E", "#A36D42"]
    for ax, key, title, color, label in zip(
        axes, ["case_Ce131", "case_Pr133"],
        [r"$^{131}$Ce", r"$^{133}$Pr"], colors, ["a", "b"],
    ):
        data = ledger[key]
        finite = [r for r in data["rows"] if r["Qt"]["kind"] == "finite"]
        x = np.array([r["spin"] for r in finite])
        y = np.array([r["Qt"]["value"] for r in finite])
        minus = np.array([r["Qt"]["minus"] for r in finite])
        plus = np.array([r["Qt"]["plus"] for r in finite])
        sigma = (minus + plus) / 2
        result = fit(x, y, np.diag(sigma**2))
        result["normalized_weights"] = ((1 / sigma**2) / np.sum(1 / sigma**2)).tolist()
        result["fit_spin_range"] = [float(x.min()), float(x.max())]
        results[key] = result
        ax.errorbar(x, y, yerr=np.stack([minus, plus]), fmt="o", ms=4,
                    color=color, ecolor=color, elinewidth=.9, capsize=2,
                    zorder=3)
        xx = np.linspace(x.min(), x.max(), 100)
        yy = result["intercept_at_pivot"] + result["slope_eb_per_hbar"] * (xx - result["pivot_spin"])
        ax.plot(xx, yy, color=color, lw=1, ls="--", zorder=2)
        for r in data["rows"]:
            q = r["Qt"]
            if q["kind"] != "finite":
                direction = 1 if q["kind"] == "lower" else -1
                ax.plot(r["spin"], q["value"], marker="^" if direction > 0 else "v",
                        color=color, markerfacecolor="white", markersize=5,
                        markeredgewidth=.9, zorder=4)
                ax.annotate("", xy=(r["spin"], q["value"] + direction * .23),
                            xytext=(r["spin"], q["value"] + direction * .035),
                            arrowprops={"arrowstyle": "->", "color": color, "lw": .8})
            table.append({"case": key, "spin_hbar": r["spin"], "parity": r["parity"],
                          "Qt_eb": q["value"], "kind": q["kind"],
                          "minus_eb": q.get("minus", ""), "plus_eb": q.get("plus", ""),
                          "method": r.get("method", ""), "locator": data["locator"],
                          "plotted": True, "fit": q["kind"] == "finite",
                          "reason": "finite fit" if q["kind"] == "finite" else "CL unspecified; no likelihood"})
        for r in data.get("positive_feeding_rows", []):
            q = r["Qt"] or {}
            table.append({"case": key, "spin_hbar": r["spin"], "parity": r["parity"],
                          "Qt_eb": q.get("value", ""), "kind": q.get("kind", "not supplied"),
                          "minus_eb": "", "plus_eb": "", "method": "", "locator": data["locator"],
                          "plotted": False, "fit": False, "reason": "positive-parity feeding; distinct band"})
        ax.set(xlim=(6.8, 20.2), ylim=(1.55, 4.05), xticks=[7.5, 11.5, 15.5, 19.5],
               xticklabels=["15/2", "23/2", "31/2", "39/2"], xlabel=r"Initial spin $I$ ($\hbar$)")
        ax.set_yticks([2, 2.5, 3, 3.5, 4])
        ax.set_title(title, loc="left", pad=21)
        ax.text(-.12, 1.17, label, transform=ax.transAxes, weight="bold", fontsize=10)
        ax.text(0, 1.035, f"Finite points: n = {len(finite)}; b = {result['slope_eb_per_hbar']:.3f} ± {result['slope_se']:.3f}",
                fontsize=8, transform=ax.transAxes)
    axes[0].set_ylabel(r"Transition moment $Q_t$ (eb)")
    handles = [Line2D([], [], color=".25", marker="o", ls="none", ms=4, label="Finite value"),
               Line2D([], [], color=".25", marker="^", markerfacecolor="white", ls="none", ms=5, label="Lower bound"),
               Line2D([], [], color=".25", marker="v", markerfacecolor="white", ls="none", ms=5, label="Upper bound"),
               Line2D([], [], color=".25", ls="--", lw=1, label="Conditional fit")]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(.52, .055), ncol=4,
               handletextpad=.5, columnspacing=1.5, fontsize=8)
    fig.text(.10, .025, "Fit slopes b and conditional SE in eb/ℏ; original asymmetric errors shown.", fontsize=8)
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig, json_out=str(stem) + ".alignment.json",
                                       tolerance_pt=1.5, gutter_tolerance_pt=1.5, strict=True)
    fig.savefig(str(stem) + ".pdf")
    fig.savefig(str(stem) + ".svg")
    fig.savefig(str(stem) + ".png", dpi=600)
    plt.close(fig)
    assert len(table) == 14 and sum(r["plotted"] for r in table) == 12
    assert sum(r["fit"] for r in table) == 7
    with (args.out_dir / "source-data-043.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(table[0])); w.writeheader(); w.writerows(table)
    output = {"ledger_sha256": hashlib.sha256(args.ledger.read_bytes()).hexdigest(),
              "raw_sha256": ledger["raw_sha256"], "cases": results,
              "counts": {"ledger_rows_including_feeding": 14, "plotted_negative_parity": 12,
                         "finite_fitted": 7, "bounds_not_fitted": 5, "feeding_excluded": 2},
              "boundary": "Known independent symmetrized Gaussian diagnostic only. Bounds have unspecified CL; no original Cov/CI/producer recovered."}
    (args.out_dir / "trend-figure-result-043.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output["counts"]))


if __name__ == "__main__":
    main()
