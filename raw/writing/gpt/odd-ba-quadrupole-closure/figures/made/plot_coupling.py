#!/usr/bin/env python3
"""Plot the five-point quadrupole-coupling intervention, without interpolation."""
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
SOURCE = ROOT / "data/results/quadrupole-path.csv"
with SOURCE.open() as stream:
    rows = list(csv.DictReader(stream))


def column(name):
    return np.array([float(row[name]) for row in rows])


def main(output=None):
    destination = ROOT / "figures" if output is None else output.resolve()
    if output is not None:
        destination.mkdir(parents=True, exist_ok=False)
    s = column("s")
    with plt.rc_context({
        "font.size": 10, "axes.labelsize": 11, "legend.fontsize": 9.5,
        "font.family": "DejaVu Sans", "pdf.fonttype": 42,
        "axes.spines.top": False, "axes.spines.right": False,
        "lines.linewidth": 1.3, "savefig.facecolor": "white",
    }):
        fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.8), layout="constrained")
        ax = axes[0]
        ax.plot(s, 100 * column("q2_static_fraction"), "s-", color="#009E73",
                label="Static")
        ax.plot(s, 100 * column("q2_other_same_J_fraction"), "o--", color="#0072B2",
                label="Other 11/2 states")
        ax.set(xlabel=r"Quadrupole coupling fraction $s$",
               ylabel=r"Fraction of complete $q_2$ (%)", xticks=s, ylim=(0, 38))
        ax.set_title("(a)", loc="left", fontsize=10)
        ax.legend(frameon=False, loc="upper left")
        ax = axes[1]
        ax.axhspan(1, 1.14, color="#BDBDBD", alpha=.35)
        ax.axhline(1, color=".4", lw=.7, ls=":")
        ax.axhline(0, color=".65", lw=.5)
        ax.plot(s, column("full_signed_ratio"), "o-", color="#0072B2",
                label=r"Complete $r$")
        ax.plot(s, column("proxy_all_raw_ratio"), "^--", color="#D55E00",
                label=r"$J+2$: all")
        ax.set(xlabel=r"Quadrupole coupling fraction $s$",
               ylabel="Cubic ratio", xticks=s, ylim=(-.22, 1.14))
        ax.set_title("(b)", loc="left", fontsize=10)
        ax.text(.02, 1.04, r"$z>1$: no real angle", fontsize=9.5)
        ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0., .84))
        for suffix in ("pdf", "png"):
            path = destination / f"quadrupole_path-v2.{suffix}"
            if path.exists():
                raise FileExistsError(path)
            fig.savefig(path, dpi=220)
        plt.close(fig)
    out = (ROOT / "figures/made/data/quadrupole-path-v2-plot-record.json"
           if output is None else destination / "quadrupole-path-plot-record.json")
    with out.open("x") as stream:
        json.dump({
            "source": str(SOURCE.relative_to(ROOT)),
            "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
            "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "transformations": ["fractions multiplied by 100", "raw cubic ratios retained"],
            "points": 5,
            "lines": "visual connections, not additional calculations or interpolation claims",
            "uncertainty": "deterministic interventions; no confidence interval",
        }, stream, indent=2)
        stream.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, help="New directory for regenerated figures")
    args = parser.parse_args()
    main(args.output_dir)
