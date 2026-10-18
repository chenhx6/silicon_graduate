#!/usr/bin/env python3
"""Plot actual Co60 source controls and the finite-MC detector ratio.

Independent simulated histories; all complete pairs enter the declared bins.
The detector panel is a named rawcore recipe, not an experimental Q calibration.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from audit_panel_alignment import require_matplotlib_panel_alignment


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "CO60-NATIVE-CONTROL-FIGURE-01" and cfg["backend"] == "python"
    data_path, theory_path = Path(cfg["data"]), Path(cfg["theory"])
    assert sha(data_path) == cfg["data_sha256"] and sha(theory_path) == cfg["theory_sha256"]
    data, theory = json.loads(data_path.read_text()), json.loads(theory_path.read_text())
    args.out.mkdir(parents=True, exist_ok=True)
    mpl.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"],
        "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8, "legend.fontsize": 7,
        "xtick.labelsize": 7, "ytick.labelsize": 7, "axes.linewidth": .7,
        "axes.spines.top": False, "axes.spines.right": False,
        "pdf.fonttype": 42, "svg.fonttype": "none", "savefig.dpi": 600})
    fig, axes = plt.subplots(1, 2, figsize=(7.086614173228346, 3.3858267716535433))
    fig.subplots_adjust(left=.105, right=.975, bottom=.30, top=.78, wspace=.42)
    source_rows = []
    styles = {"corr": ("#31749E", "o", "Correlations on"), "iso": ("#777777", "s", "Correlations off")}
    centers = np.linspace(-.95, .95, 20)
    extremes = []
    for row in data["rows"]:
        color, marker, label = styles[row["mode"]]
        counts = np.asarray(row["emitted_100bin_histogram"]).reshape(20, 5).sum(axis=1)
        n = row["emitted_complete_unique_pairs"]
        assert int(counts.sum()) == n
        y = 20*counts/n
        se = 20/n*np.sqrt(n/(n-1)*(counts-counts*counts/n))
        axes[0].errorbar(centers, y, yerr=se, color=color, marker=marker, markersize=3,
                         linestyle="none", linewidth=.8, capsize=1.5, label=label)
        extremes += [float(np.min(y-se)), float(np.max(y+se))]
        for center, count, value, error in zip(centers, counts, y, se):
            source_rows.append(["a", row["mode"], center, int(count), n, value, error])
    x = np.linspace(-1, 1, 501)
    coefficients = theory["actual_source_mixed"]["a0_to_a4"]
    expected = np.polynomial.legendre.legval(x, coefficients)
    axes[0].plot(x, expected, color="#164866", linewidth=1.2, label="Configured point model")
    extremes += [float(expected.min()), float(expected.max())]
    axes[0].axhline(1, color="#BBBBBB", linewidth=.6, zorder=0)
    axes[0].set(xlabel="cos θ between emitted γ rays", ylabel="Yield / isotropic mean",
                xlim=(-1.05, 1.05), ylim=(min(extremes)-.025, max(extremes)+.025))
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(.52, .99), ncol=3,
               handlelength=1.7, labelspacing=.25, borderpad=0, frameon=False)
    assert not data["undefined_denominator_zero_bins"]
    ratio = np.asarray(data["detector_ratio_corr_per_history_over_iso_per_history"])
    se = np.sqrt(np.diag(data["ratio_cov_valid_bins_fixedN_independent_MC"]))
    detector_centers = np.linspace(-.9, .9, len(ratio))
    axes[1].errorbar(detector_centers, ratio, yerr=se, fmt="o", color="#31749E",
                     markersize=3.5, linewidth=.8, capsize=2)
    axes[1].axhline(1, color="#777777", linewidth=.8, linestyle="--")
    axes[1].set(xlabel="cos θ from reconstructed positions", ylabel="On / off yield per history",
                xlim=(-1.05, 1.05), ylim=(min(.4, float(np.min(ratio-se)))-.05,
                                         max(1.4, float(np.max(ratio+se)))+.05))
    for axis, letter, title in zip(axes, ["a", "b"], ["Emission control", "Detector response"]):
        axis.set_title(title, loc="left", pad=14, fontweight="normal")
        axis.text(-.18, 1.13, letter, transform=axis.transAxes, fontweight="bold", fontsize=9)
        axis.set_xticks([-1, -.5, 0, .5, 1])
    fig.text(.105, .12, "100,000 decays per mode; 99,840 / 99,845 complete pairs; 507 / 549 detector pairs.", fontsize=7)
    fig.text(.105, .065, "Error bars: 1 statistical SE. 12-quad rawcore recipe; unpolarized transport; no experimental Q.", fontsize=7)
    fig.canvas.draw()
    alignment = require_matplotlib_panel_alignment(fig,
        json_out=args.out/"co60-control.alignment.json",
        overlay_svg=args.out/"co60-control.alignment.svg",
        tolerance_pt=1.5, gutter_tolerance_pt=1.5, strict=True)
    fig.savefig(args.out/"co60-control.svg")
    fig.savefig(args.out/"co60-control.pdf")
    fig.savefig(args.out/"co60-control.png", dpi=600)
    # SVG line-end whitespace is semantically inert but fails Git's text gate.
    svg = args.out/"co60-control.svg"
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines())+"\n")
    plt.close(fig)
    with (args.out/"co60-control.source-data.csv").open("w", newline="") as stream:
        writer = csv.writer(stream, lineterminator="\n")
        writer.writerow(["panel", "mode", "cos_center", "counts", "normalization_N", "value", "stat_SE"])
        writer.writerows(source_rows)
        for center, value, error in zip(detector_centers, ratio, se):
            writer.writerow(["b", "on/off", center, "", 100000, value, error])
    result = {"script_sha256": sha(Path(__file__)), "contract_sha256": sha(args.contract),
        "data_sha256": sha(data_path), "theory_sha256": sha(theory_path),
        "alignment_verdict": alignment["verdict"], "size_mm": [180, 86],
        "source_complete_pairs_corr_iso": [99840, 99845], "detector_pairs_corr_iso": [507, 549],
        "all_source_bins_included": True, "no_journal_submission_claim": True,
        "exports": {name: sha(args.out/name) for name in ["co60-control.svg", "co60-control.pdf",
            "co60-control.png", "co60-control.source-data.csv", "co60-control.alignment.json",
            "co60-control.alignment.svg"]}}
    (args.out/"co60-control.render.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
