#!/usr/bin/env python3
"""Plot the frozen rigid-charge control from the accompanying revision package."""
import argparse
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "data/revision-v2/rigid-control/summary.csv"
DETAILS = ROOT / "data/revision-v2/rigid-control/frozen/results.json"


def main(output=None):
    dest = ROOT / "figures" if output is None else output.resolve()
    if output is not None:
        dest.mkdir(parents=True, exist_ok=False)
    data = json.loads(DETAILS.read_text())
    with SOURCE.open(newline="") as stream:
        rows = {(float(r["C_MeV"]), r["proxy_n"]): r
                for r in csv.DictReader(stream)}
    cases = data["cases"]
    C = np.array([c["C_MeV"] for c in cases])
    assert list(C) == [0, 1, 2, 4, 8]
    for c in cases:
        assert abs(c["full_6j"]["q2"] - 1) < 1e-12
        assert abs(c["full_6j"]["q3"] - .5) < 1e-12
        for p in c["proxies"]:
            key = "all" if p["n"] is None else str(p["n"])
            assert abs(float(rows[(c["C_MeV"], key)]["proxy_raw_ratio"])
                       - p["raw_ratio"]) < 1e-12
    with plt.rc_context({
        "font.size": 10, "axes.labelsize": 11, "legend.fontsize": 9.5,
        "font.family": "DejaVu Sans", "pdf.fonttype": 42,
        "axes.spines.top": False, "axes.spines.right": False,
        "lines.linewidth": 1.3, "savefig.facecolor": "white",
    }):
        fig, axes = plt.subplots(1, 2, figsize=(7.1, 2.8), layout="constrained")
        ax = axes[0]
        ax.axhspan(1, 1.14, color="#BDBDBD", alpha=.35)
        ax.axhline(1, color=".4", lw=.7, ls=":")
        ax.plot(C, [c["full_6j"]["signed_ratio"] for c in cases], "o-",
                color="#0072B2", label=r"Complete $r$")
        for n, marker, label in [(5, "v:", r"$15/2$: five"),
                                 (None, "^--", r"$15/2$: all 48")]:
            key = "all" if n is None else str(n)
            vals = [float(rows[(value, key)]["proxy_raw_ratio"]) for value in C]
            ax.plot(C, vals, marker, color="#D55E00",
                    markerfacecolor="none" if n == 5 else "#D55E00",
                    label=label)
        ax.set(xlabel=r"Field strength $C$ (MeV)", ylabel="Cubic ratio",
               xticks=C, ylim=(0, 1.14))
        ax.set_title("(a)", loc="left", fontsize=10)
        ax.text(.15, 1.055, r"$z>1$: no real angle", fontsize=9.5)
        ax.legend(frameon=False, loc="lower right")
        ax = axes[1]
        ax.plot(C, [100*float(rows[(value, "all")]["static_q2_fraction"])
                    for value in C],
                "s-", color="#009E73", label="Static")
        ax.plot(C, [100*c["static"]["q2_other_same_I_fraction"] for c in cases],
                "o--", color="#0072B2", label="Other 11/2 states")
        ax.set(xlabel=r"Field strength $C$ (MeV)",
               ylabel=r"Fraction of complete $q_2$ (%)", xticks=C, ylim=(0, 40))
        ax.set_title("(b)", loc="left", fontsize=10)
        ax.legend(frameon=False, loc="center right")
        for ext in ["pdf", "png"]:
            path = dest / f"rigid_charge_control-v1.{ext}"
            if path.exists():
                raise FileExistsError(path)
            fig.savefig(path, dpi=220)
        plt.close(fig)
    record = {
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "additional_source": str(DETAILS.relative_to(ROOT)),
        "additional_source_sha256": hashlib.sha256(DETAILS.read_bytes()).hexdigest(),
        "producer_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "points": len(cases), "fixed_gamma_deg": 20,
        "transformations": ["fractions multiplied by 100", "raw ratios retained"],
        "boundary": "Independent rigid-charge model; C is not the IBFM Gamma0. "
                    "Lines connect computed points only. No empirical uncertainty.",
    }
    target = (ROOT / "figures/made/data/rigid-control-v1-plot-record.json"
              if output is None else dest / "rigid-control-v1-plot-record.json")
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("x") as f:
        json.dump(record, f, indent=2)
        f.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path)
    main(parser.parse_args().output_dir)
