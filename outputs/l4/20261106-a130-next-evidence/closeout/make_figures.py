#!/usr/bin/env python3
"""Plot only frozen results for the 2026-11-06 closeout; never solve/refit a model."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "knowledge").is_dir())
DATA = ROOT / "raw/writing/gpt/odd-ba-quadrupole-closure/data/results"
RUN = HERE.parent
OUT = HERE / "figures"
OUT.mkdir(exist_ok=True)
inputs = {}
plotted = {}


def read(path):
    inputs[str(path.relative_to(ROOT))] = {
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bytes": path.stat().st_size,
    }
    if path.suffix == ".json":
        return json.loads(path.read_text())
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream))


plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 20,
    "axes.labelsize": 20,
    "axes.titlesize": 22,
    "xtick.labelsize": 20,
    "ytick.labelsize": 20,
    "legend.fontsize": 20,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.grid": True,
    "grid.alpha": 0.17,
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
})
BLUE, ORANGE, GREEN = "#1F77B4", "#C55A11", "#1E8449"


def save(fig, stem):
    fig.savefig(OUT / f"{stem}.pdf", bbox_inches="tight")
    fig.savefig(OUT / f"{stem}.png", bbox_inches="tight", dpi=150)
    plt.close(fig)


chain = read(DATA / "calibrated-chain.json")
rows = []
for case in chain["cases"]:
    r = next(x for x in case["primary"]["restricted"] if x["max_states"] == 5)
    rows.append({
        "A": case["case"]["odd_A"],
        "within_selected_percent": 100 * r["fraction_of_Jplus2_q2"],
        "within_full_percent": 100 * r["fraction_of_full_q2"],
        "q2": case["primary"]["full"]["q2_e2b2"],
    })
plotted["coverage"] = rows
fig, ax = plt.subplots(figsize=(10.4, 3.2), layout="constrained")
x = np.arange(5)
ax.bar(x - .19, [r["within_selected_percent"] for r in rows], .36,
       color=BLUE, label=r"Five states / all $15/2$ states")
ax.bar(x + .19, [r["within_full_percent"] for r in rows], .36,
       color=ORANGE, label=r"Five states / full $q_2$")
for i, row in enumerate(rows):
    ax.text(i + .19, row["within_full_percent"] + 2.5,
            f'{row["within_full_percent"]:.1f}', ha="center", fontsize=20)
ax.set(xticks=x, xticklabels=[str(r["A"]) for r in rows],
       xlabel="Ba mass number A", ylabel="Strength fraction (%)", ylim=(0, 132))
ax.legend(loc="upper center", frameon=False, ncols=2, fontsize=20)
save(fig, "coverage")

path = read(DATA / "quadrupole-path.json")["points"]
plotted["coupling"] = path
fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.4), layout="constrained")
s = [r["s"] for r in path]
axes[0].plot(s, [r["q2_e2b2"] for r in path], "o-", color=BLUE, lw=2.3)
axes[0].set(xlabel=r"$s=\Gamma_0/(0.6\,{\rm MeV})$",
            ylabel=r"$q_2$ ($e^2$b$^2$)", ylim=(0, .8), title="Total strength")
axes[1].plot(s, [100 * r["q2_static_fraction"] for r in path], "s-",
             color=ORANGE, lw=2.3)
axes[1].set(xlabel=r"$s=\Gamma_0/(0.6\,{\rm MeV})$",
            ylabel="Static fraction (%)", ylim=(0, 40), title="Static redistribution")
save(fig, "coupling")

rigid = read(RUN / "rigid-core-control/summary.csv")
all_rigid = [r for r in rigid if r["proxy_n"] == "all"]
plotted["rigid"] = all_rigid
C = [float(r["C_MeV"]) for r in all_rigid]
fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.4), layout="constrained")
axes[0].plot(C, [float(r["full_ratio"]) for r in all_rigid], "o-",
             color=BLUE, label=r"Full $q_3/q_2^{3/2}$")
axes[0].plot(C, [float(r["proxy_raw_ratio"]) for r in all_rigid], "s-",
             color=ORANGE, label=r"All $15/2$: $z$")
axes[0].axhline(1, color="#555555", ls="--", lw=1.5)
axes[0].set(xlabel="Field strength C (MeV)", ylabel="Raw ratio", ylim=(0, 1.2))
axes[0].legend(frameon=False, loc="lower right", fontsize=20)
axes[1].plot(C, [float(r["full_angle_deg"]) for r in all_rigid], "o-",
             color=BLUE, label="Full angle")
angles = [float(r["proxy_angle_deg"]) if r["proxy_angle_deg"] else np.nan
          for r in all_rigid]
axes[1].plot(C, angles, "s-", color=ORANGE, label="Restricted angle")
axes[1].text(7.8, 8, "undefined\nat C=8", ha="right", color=ORANGE, fontsize=20)
axes[1].set(xlabel="Field strength C (MeV)", ylabel="Angle (deg)", ylim=(0, 40))
axes[1].legend(loc="upper right", frameon=False, fontsize=20)
save(fig, "rigid")

replay = read(RUN / "source-chain-replay/comparison.csv")
plotted["replay"] = replay
fig, ax = plt.subplots(figsize=(10.4, 3.2), layout="constrained")
spins = [7, 9, 13, 15, 17]
for A, marker, color in [(135, "o", BLUE), (137, "s", ORANGE)]:
    selected = [r for r in replay if int(r["odd_A"]) == A and int(r["two_J"]) != 11]
    assert [int(r["two_J"]) for r in selected] == spins
    ax.plot(np.arange(5), [float(r["kernel_minus_source_plot_keV"]) for r in selected],
            marker + "-", label=rf"$^{{{A}}}$Ba", color=color, lw=2)
ax.axhline(0, color="#555555", ls="--", lw=1)
ax.set(xticks=np.arange(5), xticklabels=[f"{J}/2" for J in spins],
       ylabel="Kernel - source (keV)", xlabel="Lowest state of each negative-parity spin",
       ylim=(-.6, 3.8))
ax.legend(frameon=False, ncols=2, loc="upper right")
save(fig, "replay")

widths = read(RUN / "isomer-benchmark/decay-width-results.json")
primary = next(r for r in widths["rows"]
               if r["operator"] == "primary" and r["initial_ordinal"] == 0)
maximum = max(r["model_scheme_half_life_upper_bound_ns"] for r in widths["rows"])
plotted["lifetimes"] = {
    "primary_upper_ns": primary["model_scheme_half_life_upper_bound_ns"],
    "max_all14_upper_ns": maximum, "observed_ns": 589, "quoted_margin_ns": 20,
    "experimental_identity": "Vogt2017 Table III; 19/2 tentative parent",
}
fig, ax = plt.subplots(figsize=(10.4, 3.0), layout="constrained")
values = [primary["model_scheme_half_life_upper_bound_ns"], maximum, 589]
for y, val in enumerate(values):
    if y < 2:
        ax.scatter(val, y, marker="<", s=150, color=ORANGE, zorder=5)
        ax.annotate("", (val / 2.5, y), (val, y),
                    arrowprops={"arrowstyle": "->", "color": ORANGE, "lw": 1.5})
    else:
        ax.errorbar(val, y, xerr=20, fmt="o", color=BLUE, capsize=4, ms=8)
    label = f"{val:.4g} ns"
    ax.text(val * (1.6 if y < 2 else .55), y + .17, label,
            ha="left" if y < 2 else "right", fontsize=20)
ax.set(xscale="log", xlim=(5e-5, 5000), ylim=(-.55, 2.65),
       yticks=[0, 1, 2],
       yticklabels=["Primary model bound", "Largest of 14 bounds", "Vogt2017 observation"],
       xlabel=r"$T_{1/2}$ (ns; logarithmic scale)")
save(fig, "lifetimes")

(HERE / "figure-inputs.json").write_text(json.dumps({
    "created_at_utc": datetime.now(timezone.utc).isoformat(),
    "purpose": "Visualization of frozen results only; no new physical calculation.",
    "inputs": inputs, "plotted": plotted,
    "observed_values_are_linked_to_E05": True,
    "minimum_source_plot_font_pt": 20,
}, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"figures": 5, "inputs": len(inputs), "output": str(OUT)}))
