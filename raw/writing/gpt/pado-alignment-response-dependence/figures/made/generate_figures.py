#!/usr/bin/env python3
"""Generate figures for the P-ADO alignment-response paper."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).parents[2]
RESULTS = ROOT / "analysis" / "results"
OUT = ROOT / "figures"
MADE = ROOT / "figures" / "made" / "data"
OUT.mkdir(parents=True, exist_ok=True)
MADE.mkdir(parents=True, exist_ok=True)


def save(fig, name: str) -> None:
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    profile = json.loads((RESULTS / "alignment-profile.json").read_text())
    coverage = json.loads((RESULTS / "coverage.json").read_text())
    center = profile["fits_at_rho_center"]

    colors = {"alpha": "#1b6ca8", "12C": "#c24e00"}
    fig, axes = plt.subplots(1, 3, figsize=(13.0, 4.0))

    # Panel A: alpha2
    ax = axes[0]
    for beam in ("alpha", "12C"):
        rows = [r for r in profile["fits_at_rho_center"]["shared"]["predictions"] if r["beam"] == beam]
        source = [r for r in profile["rho_profile"] if r["model"] == "shared" and abs(r["rho"]) < 1e-12]
        ax.errorbar(
            [r["energy_MeV"] for r in rows],
            [r["alpha2_pred"] for r in rows],
            fmt="none",
        )
    # Read the CSV directly without adding a pandas dependency.
    import csv
    with (ROOT / "data" / "zobel83_958_table1.csv").open(newline="", encoding="utf-8") as handle:
        table = list(csv.DictReader(handle))
    for beam in ("alpha", "12C"):
        subset = [r for r in table if r["beam"] == beam]
        ax.errorbar(
            [float(r["beam_energy_lab_MeV"]) for r in subset],
            [float(r["alpha2"]) for r in subset],
            yerr=[float(r["sigma_alpha2"]) for r in subset],
            fmt="o",
            color=colors[beam],
            label=beam,
        )
    for model, ls in (("shared", "--"), ("family", "-"), ("energy", ":"), ("mixture", "-.")):
        fit = center[model]
        for beam in ("alpha", "12C"):
            pred = [p for p in fit["predictions"] if p["beam"] == beam]
            ax.plot(
                [p["energy_MeV"] for p in pred],
                [p["alpha2_pred"] for p in pred],
                ls=ls,
                color=colors[beam],
                alpha=0.8,
            )
    ax.set_xlabel(r"$E_{\rm lab}$ (MeV)")
    ax.set_ylabel(r"$\alpha_2$")
    ax.set_title("(a) Rank-2 alignment")
    ax.legend(frameon=False, fontsize=8)

    # Panel B: tau profile
    ax = axes[1]
    for model, label, ls in (
        ("shared", "shared", "--"),
        ("family", "family", "-"),
        ("energy", "energy", ":"),
        ("mixture", "mixture", "-."),
    ):
        rows = [r for r in profile["rho_profile"] if r["model"] == model]
        ax.plot([r["rho"] for r in rows], [r["tau_max_d2"] for r in rows], ls=ls, label=label)
    ax.axhline(1.0, color="black", lw=1, alpha=0.6)
    ax.set_xlabel(r"Assumed common $\rho$")
    ax.set_ylabel(r"$\tau_{\rm max}$")
    ax.set_title("(b) Covariance sensitivity")
    ax.legend(frameon=False, fontsize=8)

    # Panel C: toy coverage
    ax = axes[2]
    q = coverage["max_d2_quantiles"]
    vals = [q["0.5"], q["0.9"], q["0.95"], q["0.99"]]
    labels = ["50%", "90%", "95%", "99%"]
    ax.bar(labels, vals, color="#5a9367")
    ax.axhline(coverage["threshold_q95_2d"], color="black", ls="--", label=r"$q_{0.95}^{2D}$")
    ax.set_ylabel(r"max-row $D^2$")
    ax.set_title(f"(c) Toy coverage = {coverage['empirical_fraction_max_d2_leq_q95']:.3f}")
    ax.legend(frameon=False, fontsize=8)

    fig.suptitle("Reaction-dependent alignment response in the $^{67}$Ga P-ADO benchmark")
    save(fig, "alignment_response_profile")


if __name__ == "__main__":
    main()
