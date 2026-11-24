"""Plot the frozen U04 evidence from its recorded summaries and angle curves."""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np


MODES = ("P_ADO", "P_DCO", "PDCO")
GENERATORS = ("independent_9j", "same_kernel")
GENERATOR_NAMES = {"independent_9j": "Independent 9j", "same_kernel": "Same kernel"}
ETI = "#405c73"
HDI = "#b34a38"
TRUTH = "#35302c"


def save(figure, output, name):
    figure.savefig(output / f"{name}.pdf", bbox_inches="tight")
    plt.close(figure)


def plot_recovery(output, rows, parameter):
    fig, axes = plt.subplots(3, 2, figsize=(10, 9), layout="constrained")
    if parameter == "delta":
        bounds = [
            bound
            for row in rows if row["status"] != "failed"
            for bounds in (
                (row[parameter]["q16"], row[parameter]["q84"]),
                *(segment["bounds"] for segment in row[parameter]["hdi_segments"]),
            )
            for bound in bounds
        ]
        delta_limit = max(12.0, max(map(abs, bounds), default=0.0) * 1.1)
    for row, mode in enumerate(MODES):
        for col, generator in enumerate(GENERATORS):
            ax = axes[row, col]
            section = [item for item in rows if item["mode"] == mode and item["generator"] == generator]
            for index, item in enumerate(section):
                x = item["delta0"] if parameter == "delta" else index
                offset = 0.08 * abs(x) if parameter == "delta" else 0.11
                if item["status"] == "failed":
                    ax.text(x, 0.95, "Failed", transform=ax.get_xaxis_transform(), ha="center")
                    continue
                stats = item[parameter]
                ax.vlines(x - offset, stats["q16"], stats["q84"], color=ETI, lw=1.6)
                ax.plot(x - offset, stats["q50"], ".", color=ETI)
                for segment in stats["hdi_segments"]:
                    ax.vlines(x + offset, *segment["bounds"], color=HDI, lw=1.6)
                    for low, high in segment["mode_ranges"]:
                        ax.vlines(x + offset, low, high, color=HDI, lw=4)
                        if low == high:
                            ax.plot(x + offset, low, ".", color=HDI)
            deltas = [item["delta0"] for item in section]
            if parameter == "delta":
                ax.set_xscale("symlog", linthresh=0.1)
                ax.set_yscale("symlog", linthresh=0.1)
                ax.plot([-12, 12], [-12, 12], color=TRUTH, lw=0.8, ls="--")
                ax.set_xlim(-12, 12)
                ax.set_ylim(-delta_limit, delta_limit)
            else:
                ax.axhline(0.3, color=TRUTH, lw=0.8, ls="--")
                ax.set_ylim(0, 1.03)
                ax.set_xticks(range(len(section)), [f"{value:g}" for value in deltas])
            ax.set_title(f"{mode} | {GENERATOR_NAMES[generator]}")
            ax.grid(axis="y", alpha=0.22)
    fig.supxlabel("Injected mixing ratio, δ₀")
    fig.supylabel("Recovered δ" if parameter == "delta" else "Recovered σ/I")
    fig.legend(
        handles=[
            Line2D([0], [0], color=TRUTH, ls="--", label="Truth"),
            Line2D([0], [0], color=ETI, marker=".", label="68% ETI and median"),
            Line2D([0], [0], color=HDI, marker=".", label="68% HDI segments and peaks"),
        ],
        loc="outside upper center", ncol=3, frameon=False,
    )
    save(fig, output, f"recovery_{parameter}")


def plot_marginals(output, rows, curves):
    selections = {"P_ADO": (-0.1, 0.5), "P_DCO": (-1, 1), "PDCO": (-10, 10)}
    fig, axes = plt.subplots(3, 2, figsize=(10, 7.5), layout="constrained", sharex=True)
    for mode, panels in zip(MODES, axes):
        for delta, ax in zip(selections[mode], panels):
            for generator, style in zip(GENERATORS, ("-", "--")):
                row = next(item for item in rows if (
                    item["mode"], item["delta0"], item["generator"]
                ) == (mode, delta, generator))
                key = f"{row['case_id']}__{generator}"
                if key not in curves:
                    continue
                angle, density = curves[key]
                ax.plot(angle, density, ls=style, color=ETI, lw=1.5, label=GENERATOR_NAMES[generator])
                if generator == "independent_9j":
                    stats = row["arctan_delta"]
                    ax.axvspan(stats["q16"], stats["q84"], alpha=0.09, color=ETI)
                    for segment in stats["hdi_segments"]:
                        left, right = segment["bounds"]
                        ax.axvspan(left, right, alpha=0.18, color=HDI)
                    ax.axvline(row["arctan_delta0"], color=TRUTH, ls=":", lw=1)
            ax.set_title(f"{mode} | δ₀ = {delta:g}")
            ax.grid(alpha=0.15)
    fig.supxlabel("Mixing angle, arctan(δ) [rad]")
    fig.supylabel("Angle marginal density")
    handles, _ = axes[0, 0].get_legend_handles_labels()
    handles.extend([
        Line2D([0], [0], color=TRUTH, ls=":", label="Truth"),
        Patch(color=ETI, alpha=0.09, label="68% ETI"),
        Patch(color=HDI, alpha=0.18, label="68% HDI"),
    ])
    fig.legend(handles=handles, loc="outside upper center", ncol=5, frameon=False)
    save(fig, output, "representative_angle_marginals")


def plot_coverage(output, summaries):
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.8), layout="constrained", sharey=True)
    labels = ("Angle ETI", "Angle HDI", "σ/I ETI", "σ/I HDI")
    for mode, ax in zip(MODES, axes):
        data = [row for row in summaries if row["case_id"].startswith(f"{mode}_")]
        for offset, color, row in zip((-0.08, 0.08), (ETI, HDI), data):
            for index, score in enumerate(row["coverage"].values()):
                fraction = score["fraction_of_valid_fits"]
                if fraction is None:
                    continue
                low, high = score["binomial_interval"]
                ax.errorbar(
                    index + offset, fraction, yerr=[[fraction - low], [high - fraction]],
                    fmt="o", color=color, ms=4,
                )
        ax.set_title(data[0]["case_id"].replace(f"{mode}_", f"{mode} | δ₀ = "))
        ax.set_xticks(range(len(labels)), labels, rotation=25, ha="right")
        ax.axhline(0.68, color=TRUTH, ls="--", lw=0.8)
        ax.set_ylim(0, 1)
        ax.grid(axis="y", alpha=0.22)
    fig.supylabel("Truth inclusion frequency with 68% binomial interval")
    fig.legend(
        handles=[
            Line2D([0], [0], color=color, marker="o", label=GENERATOR_NAMES[generator])
            for generator, color in zip(GENERATORS, (ETI, HDI))
        ],
        loc="outside upper center", ncol=2, frameon=False,
    )
    save(fig, output, "repeated_observation_coverage")


def save_figures(output, main, coverage, curves):
    plot_recovery(output, main, "delta")
    plot_recovery(output, main, "sigma_over_i")
    plot_marginals(output, main, curves)
    plot_coverage(output, coverage)
