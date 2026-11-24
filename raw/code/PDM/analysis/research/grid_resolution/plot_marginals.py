"""Render marginal and component diagnostics from the saved NPZ and JSON."""

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.lines import Line2D
from matplotlib.ticker import MaxNLocator
import numpy as np

from study import HERE, MODES, TARGETS, frozen, load


STYLES = {
    "a0.2_s0.02": ("0.20 deg / 0.02021", "#b74c05", (0, (1, 2)), 1.7),
    "a0.1_s0.01": ("0.10 deg / 0.010", "#00748b", (0, (4, 2)), 1.4),
    "a0.1_s0.005": ("0.10 deg / 0.005", "#8f3c76", (0, (3, 3, 1, 3)), 1.1),
    "a0.05_s0.005": ("0.05 deg / 0.005", "#258047", (0, (6, 3)), 1.1),
    "a0.05_s0.001": ("0.05 deg / 0.001", "#26313a", "-", 1.15),
}


def pages(axis_name, config, results, arrays, path):
    grids = list(STYLES)
    ref_grid = config["reference"]
    reference_style = STYLES[ref_grid]
    by_key = {(row["case_id"], row["grid"]): row for row in results["rows"]}
    comparison = {(row["case_id"], row["grid"]): row for row in results["comparisons"]}
    axis_key = "angle_deg" if axis_name == "angle" else "s"
    label = "Mixing angle arctan(delta) (degrees)" if axis_name == "angle" else "Alignment s = sigma / I"
    limits = config["angle_limits_deg"] if axis_name == "angle" else config["s_limits"]
    figure = plt.figure(figsize=(11.6, 9.1))
    outer = figure.add_gridspec(3, 3, left=0.075, right=0.975, bottom=0.09, top=0.86,
                                wspace=0.25, hspace=0.38)
    for row_index, truth_delta in enumerate(TARGETS):
        for col_index, mode in enumerate(MODES):
            inner = outer[row_index, col_index].subgridspec(2, 1, height_ratios=(3.8, 1.2), hspace=0.05)
            ax = figure.add_subplot(inner[0])
            bands = figure.add_subplot(inner[1], sharex=ax)
            case = next(row for row in config["cases"] if row["mode"] == mode and row["truth_delta"] == truth_delta)
            case_id = case["id"]
            truth = case["truth_angle_deg"] if axis_name == "angle" else case["truth_s"]
            ax.axvline(truth, color="#8b9296", linewidth=0.8, zorder=0)
            bands.axvline(truth, color="#8b9296", linewidth=0.8, zorder=0)
            for grid in reversed(grids):
                row = by_key[case_id, grid]
                prefix = f"{grid}__{mode}__"
                coordinates = arrays[prefix + axis_key]
                pdf = arrays[f"{prefix}{axis_name}_pdf_{row['array_index']}"]
                _, color, line, width = STYLES[grid]
                ax.plot(coordinates, pdf, color=color, linestyle=line, linewidth=width)
                y_position = len(grids) - grids.index(grid)
                for component in row[axis_name]["hdi_components"]:
                    bands.hlines(y_position, component["lower"], component["upper"], color=color, linewidth=1.2)
                    bands.scatter(component["mode"], y_position, s=8, color=color,
                                  zorder=3, clip_on=False)
            proposed = comparison[case_id, config["recommendation_candidate"]]
            cdf_gap = proposed[f"{axis_name}_cdf"]
            ax.text(0.99, 1.04, f"CDF gap {cdf_gap:.2g}", transform=ax.transAxes,
                    ha="right", va="bottom", fontsize=7, color=STYLES[config["recommendation_candidate"]][1])
            ax.set_title(f"{mode.replace('_', '-')}  |  delta = {truth_delta:+g}", fontsize=10, loc="left")
            ax.set_ylim(bottom=0)
            ax.set_xlim(*limits)
            ax.yaxis.set_major_locator(MaxNLocator(4))
            ax.tick_params(axis="x", bottom=False, labelbottom=False)
            ax.tick_params(axis="y", labelsize=8)
            bands.set(ylim=(0.5, len(grids) + 0.5), yticks=[])
            bands.xaxis.set_major_locator(MaxNLocator(7))
            bands.tick_params(axis="x", labelsize=8)
            for panel in (ax, bands):
                for spine in ("top", "right"):
                    panel.spines[spine].set_visible(False)
                panel.spines["left"].set_color("#a7afb4")
                panel.spines["bottom"].set_color("#a7afb4")
    figure.suptitle(f"{label.split(' (')[0]} marginal and 68% highest-density intervals",
                    x=0.078, y=0.978, ha="left", fontsize=16)
    handles = [Line2D([0], [0], color=color, linestyle=line, linewidth=width, label=label)
               for label, color, line, width in STYLES.values()]
    handles.append(Line2D([0], [0], color="#8b9296", linewidth=0.8, label="Synthetic truth"))
    figure.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.07, 0.944),
                  ncols=len(handles), frameon=False, fontsize=9)
    figure.text(0.079, 0.892, f"HDI rows follow the legend order. Dots mark component modes. "
                f"CDF gap compares the proposed grid with {reference_style[0]}.", fontsize=8)
    figure.supxlabel(label, y=0.034, fontsize=11)
    figure.supylabel("Normalized density", x=0.018, fontsize=11)
    path.savefig(figure)
    plt.close(figure)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "marginals.pdf")
    args = parser.parse_args()
    config = frozen(HERE / "frozen_inputs.json")
    results = load(HERE / "results.json")
    matplotlib.rcParams.update({"font.family": "DejaVu Sans", "pdf.fonttype": 42})
    with np.load(HERE / "marginals.npz") as arrays, PdfPages(args.output) as pdf:
        for axis in ("angle", "s"):
            pages(axis, config, results, arrays, pdf)


if __name__ == "__main__":
    main()
