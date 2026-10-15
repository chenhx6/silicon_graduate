#!/usr/bin/env python3
"""Draw conditional feeding geometry, with no fitted fraction or confidence set."""
from pathlib import Path
import json
import os
import sys

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02"
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "tmp/day14-20261014/mplconfig"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.transforms import ScaledTranslation
import numpy as np

from day14_feeding_fraction_moment_bound import geometry, normalized_point, slack
from decimal import Decimal as D, localcontext

sys.path.insert(0, "/root/.codex/skills/nature-figure/scripts")
from audit_panel_alignment import require_matplotlib_panel_alignment


def main():
    data = json.loads((RUN / "tm167-feeding-fraction-input.json").read_text())
    audit = json.loads((RUN / "tm167-feeding-fraction-audit.json").read_text())
    assert audit["passed"] and audit["precision_80_vs_110_agreement_to_60digits"]
    bound = float(audit["center_bound"])
    target = np.array([float(data["target"][k]) for k in ["rho2", "rho4"]])
    feed = np.array([float(v) for v in audit["known_feeding_component_rho"]])
    rest = (target-bound*feed)/(1-bound)
    with localcontext() as ctx:
        ctx.prec = 80
        geo = geometry(data["target"]["spin_twice"])
        scales = [float(c)**0.5 for c in geo["constants"]]
        vertices = np.array([[float(p[0])*scales[0], float(p[1])*scales[1]] for p in geo["hull"]])
        active = next(f for f in geo["faces"] if f["m_twice"] == audit["active_remainder_m_twice"])
        witness = audit["quoted_marginal_box_w1"]["child_rho"]
        d_witness = slack(active, normalized_point([D(x) for x in witness], geo))
        d_center = slack(active, normalized_point([D(str(x)) for x in feed], geo))
        witness_factor = float(d_witness/d_center)
    w = np.linspace(0, 1, 201)
    center_margin = bound-w
    witness_margin = witness_factor*(1-w)
    source = dict(weight_definition=data["weight_definition"], vertices_rho=vertices.tolist(),
                  F=feed.tolist(), T=target.tolist(), R=rest.tolist(), w=w.tolist(),
                  center_facet_margin_scaled=center_margin.tolist(),
                  marginal_bounds_point_margin_scaled=witness_margin.tolist(),
                  w_center_bound=bound, marginal_bounds_point=audit["quoted_marginal_box_w1"],
                  uncertainty="No confidence region or fitted branching fraction; a constructed point within quoted marginal bounds.")
    (RUN / "tm167-feeding-fraction-figure-source.json").write_text(json.dumps(source, indent=2)+"\n")
    plt.rcParams.update({"font.family":"sans-serif", "font.sans-serif":["DejaVu Sans"],
                         "font.size":8, "axes.labelsize":8.5, "xtick.labelsize":7.2,
                         "ytick.labelsize":7.2, "svg.fonttype":"none", "pdf.fonttype":42,
                         "axes.spines.top":False, "axes.spines.right":False,
                         "axes.linewidth":0.7, "legend.frameon":False})
    fig, axes = plt.subplots(1, 2, figsize=(7.20472440945, 3.46456692913))
    fig.subplots_adjust(left=0.095, right=0.975, bottom=0.24, top=0.84, wspace=0.48)
    blue, orange, black = "#0072B2", "#D55E00", "#222222"
    ax = axes[0]
    ax.fill(vertices[:,0], vertices[:,1], color="#EAEAEA", zorder=0)
    closed = np.vstack([vertices, vertices[0]])
    ax.plot(closed[:,0], closed[:,1], color="#737373", linewidth=0.8)
    ax.scatter(vertices[:,0], vertices[:,1], color="#737373", s=8)
    ax.plot([rest[0], feed[0]], [rest[1], feed[1]], color=black, linewidth=1.1)
    for point, label, color in [(feed,"F",blue),(target,"T (D)",black),(rest,"R*",orange)]:
        ax.scatter(*point, s=24, color=color, zorder=4)
        ax.annotate(label, xy=point, xytext=(7,2), textcoords="offset points", fontsize=8, color=color)
    ax.set(xlabel=r"$\rho_2$", ylabel=r"$\rho_4$", xlim=(-1.3,2.05), ylim=(-1.6,1.65))
    ax.set_title("Fixed printed centers", loc="left", fontsize=8.5, pad=8)
    ax = axes[1]
    ax.axhspan(-0.46, 0, color="#F3F3F3", zorder=0)
    ax.axhline(0, color="#777777", linewidth=0.7)
    ax.plot(w, center_margin, color=black, linewidth=1.2, label="Fixed centers")
    ax.plot(w, witness_margin, color=blue, linestyle="--", linewidth=1.2,
            label="Point within marginal bounds")
    ax.scatter([bound], [0], s=22, color=orange, zorder=4)
    ax.set(xlim=(0,1), ylim=(-0.46,1.03), xlabel="w (fraction of target population)", ylabel="Scaled facet margin")
    ax.set_xticks([0,bound,1], ["0","0.597","1"])
    ax.set_title("One necessary facet", loc="left", fontsize=8.5, pad=8)
    ax.legend(loc="upper right", fontsize=7, handlelength=1.6, borderaxespad=0.3)
    for ax, label in zip(axes, ["a","b"]):
        transform = ax.transAxes + ScaledTranslation(-18/72, 12/72, fig.dpi_scale_trans)
        ax.text(0,1,label,transform=transform,fontsize=9,fontweight="bold",ha="left",va="top")
    fig.text(0.095,0.095,"Gray: positive populations. F: propagated component; T: target (D); R*: boundary remainder.",fontsize=6.7)
    fig.text(0.095,0.043,"Selected-tensor relaxation only; marginal bounds are not a confidence region.",fontsize=6.7)
    prefix = RUN / "tm167-feeding-fraction"
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig, axes=axes, panel_ids=["a","b"],
                                      row_groups=[["a","b"]], require_panel_labels=True,
                                      json_out=str(prefix)+".alignment.json", tolerance_pt=1.5,
                                      gutter_tolerance_pt=1.5, strict=True)
    fig.savefig(str(prefix)+".svg")
    svg = Path(str(prefix)+".svg")
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines())+"\n")
    fig.savefig(str(prefix)+".pdf")
    fig.savefig(str(prefix)+".png", dpi=300)
    plt.close(fig)
    print(json.dumps(dict(figure=str(prefix), center_bound=bound, alignment="pass", backend="python")))


if __name__ == "__main__":
    main()
