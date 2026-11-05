#!/usr/bin/env python3
"""Plot declared coefficient-space profiles and covariance sensitivity."""
from __future__ import annotations

import csv
import json
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ARTICLE = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARTICLE / "analysis"))
from companion_profile import covariance, profiled_distance
from rank4_invariant import load_rows


def main() -> None:
    contract = json.loads((ARTICLE / "data/input-contract.json").read_text())
    result = json.loads((ARTICLE / "analysis/results/companion-profile.json").read_text())
    rows = load_rows(ARTICLE / "data/ba129_same_parent_A4.csv")
    t, r = rows["target_365"], rows["reference_462"]
    y = np.array([t["A2"], t["A4"], r["A2"], r["A4"]])
    response = np.array(contract["response_ratio_s2_s4"])
    fig, axes = plt.subplots(1, 2, figsize=(7.2, 2.9), layout="constrained")
    names = {"evaluated": "2014 evaluation", "primary1977": "1977 primary table"}
    colors = {"evaluated": "#2166ac", "primary1977": "#b35806"}
    theta = np.deg2rad(np.linspace(-85, 0, 800))
    curves = []
    for scenario in contract["uncertainty_scenarios"]:
        name = scenario["id"]
        version_rows = load_rows(ARTICLE / scenario["dataset_file"], require_reference_nonzero=False)
        vt, vr = version_rows["target_365"], version_rows["reference_462"]
        y = np.array([vt["A2"], vt["A4"], vr["A2"], vr["A4"]])
        cov = covariance(np.array(scenario["standard_error_scales"]), 0, 0)
        central = next(c for c in result["cases"]
                       if c["scenario"] == name and c["rho_within_line"] == c["rho_cross_line"] == 0)
        diff = profiled_distance(theta, y, cov, response) - central["global"]["distance"]
        axes[0].plot(np.rad2deg(theta), diff, label=names[name], color=colors[name])
        for x, d in zip(np.rad2deg(theta), diff):
            curves.append([name, float(x), float(d)])
        cross_zero = [c for c in result["cases"] if c["scenario"] == name and c["rho_cross_line"] == 0]
        axes[1].plot([c["rho_within_line"] for c in cross_zero],
                     [c["distance_small_minus_large"] for c in cross_zero],
                     marker="o", ms=3.5, label=names[name], color=colors[name])
    axes[0].axvline(-45, ls="--", color="0.45", lw=0.8)
    axes[0].set(xlabel=r"$\arctan\delta$ (degrees)", ylabel=r"$D(\delta)-D_{\min}$",
                title="(a) Fixed diagonal covariance", ylim=(0, 45), xlim=(-85, 0))
    axes[0].legend(fontsize=7, frameon=False)
    axes[1].axhline(0, color="0.45", lw=0.8)
    axes[1].set(xlabel=r"Within-line correlation $\rho_w$",
                ylabel=r"$D_{\rm small}-D_{\rm large}$",
                title=r"(b) Chosen $\rho_c=0$ slice")
    for ax in axes:
        ax.tick_params(labelsize=8)
        ax.xaxis.label.set_size(9)
        ax.yaxis.label.set_size(9)
        ax.title.set_fontsize(10)
        ax.grid(alpha=0.2)
    for suffix in ("pdf", "png"):
        fig.savefig(ARTICLE / f"figures/companion_profiles.{suffix}", dpi=300)
    plt.close(fig)
    out = ARTICLE / "figures/made/data/companion_profile_curves.csv"
    with out.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["scenario", "theta_degrees", "distance_above_minimum"])
        writer.writerows(curves)
    print("Generated conditional companion-profile figures.")


if __name__ == "__main__":
    main()
