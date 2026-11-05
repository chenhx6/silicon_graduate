#!/usr/bin/env python3
"""Render model checks, with central data and explicitly non-statistical boxes."""
import csv
import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "observables-v1/observable-predictions.json"
payload = json.loads(SOURCE.read_text())
selected = [
    next(row for row in payload["predictions"] if not row["dual_partner"]
         and row["is_recorded_best_start"]
         and "/model-fit-C60/" in row["energy_fit"]),
    next(row for row in payload["predictions"] if not row["dual_partner"]
         and row["energy_start"] == 0
         and "/model-fit-free-inertias-C120/" in row["energy_fit"]),
    next(row for row in payload["predictions"] if not row["dual_partner"]
         and row["energy_start"] == 1
         and "/model-fit-free-inertias-C120/" in row["energy_fit"]),
]
labels = ["Irrotational; energy RMS 71.97 keV",
          "Independent inertias; RMS 39.93 keV",
          "Independent inertias; RMS 43.26 keV"]
colors, markers = ["#0072B2", "#D55E00", "#009E73"], ["o", "s", "^"]
order = sorted(range(6), key=lambda n: selected[0]["photon"]["pairs"][n]["target_energy_MeV"])
out = BASE / "figures"
data_dir = out / "made/data"
data_dir.mkdir(parents=True, exist_ok=True)
exported = []

with plt.rc_context({"font.size": 10, "pdf.fonttype": 42, "axes.spines.top": False,
                     "axes.spines.right": False}):
    fig, axes = plt.subplots(2, 1, figsize=(9.0, 8.5), layout="constrained")
    ax = axes[0]
    for n, k in enumerate(order):
        row = selected[0]["photon"]["pairs"][k]
        t, r = row["target_RI"], row["reference_RI"]
        dt, dr = row["target_RI_margin"], row["reference_RI_margin"]
        center = row["reported_photon_ratio"]
        low, high = (t - dt) / (r + dr) / center, (t + dt) / (r - dr) / center
        ax.fill_between([n - .34, n + .34], low, high, color=".85", linewidth=0)
    ax.axhline(1, color=".25", ls=":", lw=1)
    for j, (model, label, color, marker) in enumerate(zip(selected, labels, colors, markers)):
        values = [model["photon"]["pairs"][k]["prediction_over_reported_ratio"] for k in order]
        ax.scatter(np.arange(6) + (j - 1) * .17, values, c=color, marker=marker,
                   s=42, label=label, zorder=3)
        for k in order:
            row = model["photon"]["pairs"][k]
            exported.append({"model": label, "target_keV": 1000 * row["target_energy_MeV"],
                             "reference_keV": 1000 * row["reference_energy_MeV"],
                             "role": row["role"], "reported_ratio": row["reported_photon_ratio"],
                             "predicted_ratio": row["predicted_photon_ratio"],
                             "prediction_over_reported_ratio": row["prediction_over_reported_ratio"]})
    names = []
    for k in order:
        row = selected[0]["photon"]["pairs"][k]
        suffix = "\nscale anchor" if row["role"] == "scale-calibration" else "\nwithheld"
        names.append(f'{1000*row["target_energy_MeV"]:.1f}/{1000*row["reference_energy_MeV"]:.1f}' + suffix)
    ax.set_xticks(range(6), names, fontsize=9)
    ax.set(yscale="log", ylabel="Predicted / reported photon ratio",
           title="(a) One scale anchor does not close all five withheld branches",
           ylim=(.002, 35))
    ax.legend(loc="upper left", bbox_to_anchor=(0, .92), fontsize=8)
    ax.text(.01, .98, "Grey boxes: rectangular ±1 quoted RI margins; not confidence intervals",
            transform=ax.transAxes, va="top", fontsize=8)
    ax.grid(axis="y", which="major", alpha=.18)

    original = selected[1]
    dual = next(row for row in payload["predictions"] if row["dual_partner"]
                and row["energy_start"] == 0
                and row["energy_fit"] == original["energy_fit"])
    ax = axes[1]
    transfer_rows = []
    for model, color, marker, offset in ((original, colors[1], "s", -4), (dual, colors[0], "o", 4)):
        states = [s for s in model["transfer"]["states"] if s["model_excitation_keV"] < 2000]
        xx = [s["model_excitation_keV"] for s in states]
        yy = [s["relative_removal_to_first"] for s in states]
        gamma = model["parameters"]["gamma_deg"]
        ax.vlines(np.array(xx) + offset, 0, yy, color=color, lw=1.3)
        ax.scatter(np.array(xx) + offset, yy, color=color, marker=marker,
                   label=fr"Model $\gamma={gamma:.2f}^\circ$; same energies", zorder=3)
        transfer_rows.extend({"dual": model["dual_partner"], **s} for s in states)
    ax.set(xlim=(150, 2000), ylim=(0, 3.8), xlabel="Model excitation energy (keV)",
           ylabel=r"Bare removal strength / first $11/2$ strength",
           title="(b) Fixed removal operator distinguishes the energy-equivalent pair")
    ax.legend(loc="upper right", fontsize=9)
    ax.text(.98, .69, "Model prediction only\nNo experimental state matching\n"
            "Markers displaced ±4 keV for visibility",
            transform=ax.transAxes, ha="right", va="top", fontsize=9)
    ax.grid(axis="y", alpha=.18)
    fig.savefig(out / "energy_vs_observables.pdf")
    fig.savefig(out / "energy_vs_observables.png", dpi=180)

for name, rows in (("photon_predictions.csv", exported), ("transfer_predictions.csv", transfer_rows)):
    with (data_dir / name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
record = {
    "input": str(SOURCE.relative_to(BASE)), "input_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "selection": "Three distinct energy minima without active bounds. Plot subset chosen after prediction by this energy-bound criterion; all 14 parameter sets remain in input.",
    "display_boundary": "Model/data central comparison; grey boxes are Cartesian single-margin RI envelopes, not confidence intervals. Transfer panel has model energies only and no experimental matching.",
    "files": [{"path": str(p.relative_to(BASE)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
              for p in (out / "energy_vs_observables.pdf", out / "energy_vs_observables.png",
                        data_dir / "photon_predictions.csv", data_dir / "transfer_predictions.csv")],
}
(out / "figure-record.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"figure": str(out / "energy_vs_observables.pdf"), "rows": len(exported)}))
