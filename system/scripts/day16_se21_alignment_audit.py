#!/usr/bin/env python3
"""Conditional nuclear-tensor audit of a newly frozen SE21 calibration row.

Uses generic finite-J helpers; it does not rerun the old Day14 worksheets.
The source table's interpretation as rho/B is a condition, not a certification
of detector response or the author's production analysis.
"""
from __future__ import annotations

import argparse
import csv
from fractions import Fraction as F
import hashlib
import io
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import brentq, linprog

from day14_alignment_formula_contract import polynomial_weights
from day14_unobserved_feeding_transfer import cg_squared, tensor


def gaussian(tj: int, ratio: float, weights: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    m = np.arange(-tj, tj + 1, 2, dtype=float) / 2
    if ratio <= 0:
        p = np.array([float(abs(x) == .5) / 2 for x in m])
    else:
        sigma = ratio * tj / 2
        p = np.exp(-(m * m - np.min(m * m)) / (2 * sigma * sigma))
        p /= p.sum()
    return weights @ p, p


def make_figure(tj: int, vertices: np.ndarray, weights: np.ndarray, row: dict,
                output: Path, audit_scripts: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon

    sys.path.insert(0, str(audit_scripts))
    from audit_panel_alignment import require_matplotlib_panel_alignment

    matplotlib.rcParams.update({
        "font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"],
        "font.size": 7.5, "axes.labelsize": 10, "xtick.labelsize": 7.5,
        "ytick.labelsize": 7.5, "legend.fontsize": 7.4,
        "axes.linewidth": .7, "axes.spines.top": False,
        "axes.spines.right": False, "svg.fonttype": "none", "pdf.fonttype": 42,
    })
    fig = plt.figure(figsize=(89 / 25.4, 88 / 25.4))
    ax = fig.add_axes([.18, .22, .77, .54])
    # Consecutive |M| values form the convex lower chain; closure is the upper chord.
    # Clip displayed geometry explicitly: the PDF collision auditor does not
    # interpret the axes clip mask on far-away polygon strokes. All original
    # vertices remain in the numerical audit and CSV; this only sets the viewport.
    visible = [np.array(p) for p in vertices]
    for axis, edge, lower in [(0, .70, True), (0, 1.04, False),
                              (1, .15, True), (1, 1.12, False)]:
        clipped = []
        for a, b in zip(visible, visible[1:] + visible[:1]):
            inside_a = a[axis] >= edge if lower else a[axis] <= edge
            inside_b = b[axis] >= edge if lower else b[axis] <= edge
            if inside_a != inside_b:
                clipped.append(a + (b - a) * (edge - a[axis]) / (b[axis] - a[axis]))
            if inside_b:
                clipped.append(b)
        visible = clipped
    hull = Polygon(visible, facecolor="#117733", alpha=.15,
                   edgecolor="#117733", linewidth=.8, label="Any positive P(M)")
    ax.add_patch(hull)
    ratios = np.linspace(.005, .5, 500)
    curve = np.array([gaussian(tj, r, weights)[0] for r in ratios])
    line, = ax.plot(curve[:, 0], curve[:, 1], color="#0072B2", lw=1.2,
                    label="Gaussian width model")
    adopted, _ = gaussian(tj, float(row["sigma_over_J_adopted"]), weights)
    ax.plot(*adopted, "s", ms=3.5, color="#0072B2")
    ax.annotate("0.2", adopted, xytext=(-23, -3), textcoords="offset points",
                fontsize=7.5, color="#0072B2")
    a2, a4 = float(row["alpha2"]), float(row["alpha4"])
    source = ax.errorbar(a2, a4, xerr=float(row["alpha2_error"]),
                        yerr=float(row["alpha4_error"]), color="#D55E00",
                        fmt="o", ms=4, lw=.9, capsize=2.5,
                        label="Table 4.1 quoted margins")
    ax.set_xlim(.70, 1.04)
    ax.set_ylim(.15, 1.12)
    ax.set_xticks([.7, .8, .9, 1.0])
    ax.set_yticks([.2, .4, .6, .8, 1.0])
    ax.set_xlabel(r"$\alpha_2$", labelpad=3)
    ax.set_ylabel(r"$\alpha_4$", labelpad=3)
    fig.suptitle("Conditional nuclear tensors, J = 23/2", y=.985, fontsize=8.3)
    fig.legend([hull, line, source], ["Any positive P(M)", "Gaussian width model",
                                    "Table 4.1 quoted margins"],
               loc="upper center", bbox_to_anchor=(.55, .94), frameon=False)
    fig.text(.18, .085, "Margins have no assigned confidence level.", fontsize=7)
    fig.text(.18, .043, "Gate/response interpretation remains unresolved.", fontsize=7)
    fig.canvas.draw()
    require_matplotlib_panel_alignment(
        fig, json_out=str(output) + ".alignment.json", tolerance_pt=1.5,
        gutter_tolerance_pt=1.5, strict=True,
    )
    fig.savefig(str(output) + ".svg")
    fig.savefig(str(output) + ".pdf")
    fig.savefig(str(output) + ".png", dpi=600)
    # Matplotlib XML can contain line-ending whitespace; preserve editable text.
    svg = Path(str(output) + ".svg")
    svg.write_text("\n".join(x.rstrip() for x in svg.read_text().splitlines()) + "\n")
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--plot", action="store_true")
    parser.add_argument("--audit-scripts", type=Path)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    row = cfg["reference"]
    tj = int(row["Ji_twice"])
    assert tj == 23 and tj % 2 == 1
    root = Path(__file__).resolve().parents[2]
    assert hashlib.sha256((root / cfg["raw_path"]).read_bytes()).hexdigest() == cfg["raw_sha256"]
    spec = polynomial_weights(tj)
    exact = spec["exact"]
    for rank in (2, 4):
        values, _ = tensor(tj, rank)
        ref = values[tj // 2]
        assert exact[rank] == [x / ref for x in values]
        assert sum(exact[rank]) == 0
    paired = [(m, exact[2][i], exact[4][i]) for i, m in enumerate(spec["m"]) if m > 0]
    dual = [F(7) - 10 * a2 + 3 * a4 for _, a2, a4 in paired]
    assert min(dual) == 0 and all(x >= 0 for x in dual)
    s = spec["S"]
    denominator = 3 * (s - F(3, 4)) * (s - F(15, 4))
    # Independent factorization of the dual on each discrete M, with no fit.
    for m, a2, a4 in paired:
        assert F(7) - 10 * a2 + 3 * a4 == (
            105 * (m * m - F(1, 4)) * (m * m - F(9, 4)) / denominator)
    a2, a4 = F(row["alpha2"]), F(row["alpha4"])
    e2, e4 = F(row["alpha2_error"]), F(row["alpha4_error"])
    mean_dual = 7 - 10 * a2 + 3 * a4
    box_maximum = 7 - 10 * (a2 - e2) + 3 * (a4 + e4)
    assert mean_dual == -F(13, 10) and box_maximum == -F(77, 100)
    vertices = np.array([[float(a), float(b)] for _, a, b in paired])
    target = np.array([float(a2), float(a4)])
    eq = np.vstack([np.ones(len(vertices)), vertices.T])
    point_lp = linprog(np.zeros(len(vertices)), A_eq=eq, b_eq=np.r_[1., target],
                       bounds=[(0, None)] * len(vertices), method="highs")
    upper = np.vstack([vertices[:, 0], -vertices[:, 0], vertices[:, 1], -vertices[:, 1]])
    bounds = np.array([float(a2 + e2), -float(a2 - e2), float(a4 + e4), -float(a4 - e4)])
    box_lp = linprog(np.zeros(len(vertices)), A_eq=np.ones((1, len(vertices))),
                     b_eq=[1.], A_ub=upper, b_ub=bounds,
                     bounds=[(0, None)] * len(vertices), method="highs")
    assert point_lp.status == box_lp.status == 2
    weights = np.array([[float(x) for x in exact[k]] for k in (2, 4)])
    adopted = float(row["sigma_over_J_adopted"])
    predicted, pop = gaussian(tj, adopted, weights)
    complete, _ = gaussian(tj, 0., weights)
    assert np.allclose(complete, [1, 1], atol=1e-14)
    assert np.allclose(weights @ np.ones(tj + 1) / (tj + 1), 0, atol=1e-14)
    inverses = [brentq(lambda r: gaussian(tj, r, weights)[0][k] - float(target[k]),
                      1e-4, 10.) for k in (0, 1)]
    for k, ratio in enumerate(inverses):
        assert abs(gaussian(tj, ratio, weights)[0][k] - target[k]) < 1e-10
    m = np.array([float(x) for x in spec["m"]])
    # A separate pure-E2 point-response check of the reference line. Nuclear
    # spins/projections are doubled integers, so this is not the integer-only
    # mixed-photon kernel used in the earlier D96 demonstration.
    tf = int(row["Jf_twice"])
    photon_a2 = {0: F(5, 7), 1: F(5, 14), 2: -F(5, 7)}
    photon_a4 = {0: -F(12, 7), 1: F(8, 7), 2: -F(2, 7)}
    reference_photon_mass = {
        mu: sum((F(1, 2) * cg_squared(tf, 4, tj, mi - 2 * mu, 2 * mu, mi)
                 for mi in (-1, 1)), F(0)) for mu in range(-2, 3)}
    assert sum(reference_photon_mass.values()) == 1
    reference_a = [sum((w * coeff[abs(mu)] for mu, w in reference_photon_mass.items()), F(0))
                   for coeff in (photon_a2, photon_a4)]
    arbitrary_gaussian_a = []
    for coeff in (photon_a2, photon_a4):
        arbitrary_gaussian_a.append(sum(
            pop[i] * float(cg_squared(tf, 4, tj, mi - 2 * mu, 2 * mu, mi))
            * float(coeff[abs(mu)])
            for i, mi in enumerate(range(-tj, tj + 1, 2)) for mu in range(-2, 3)))
    assert np.allclose(arbitrary_gaussian_a, predicted * np.array(reference_a, dtype=float),
                       atol=1e-13, rtol=1e-13)
    implied = [F(row["same_table_A2fit"]) / reference_a[0],
               F(row["same_table_A4fit"]) / reference_a[1]]
    result = {
        "data_identity": cfg["data_identity"], "data_kind": cfg["data_kind"],
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "helper_hashes": {name: hashlib.sha256((Path(__file__).parent / name).read_bytes()).hexdigest()
                          for name in ["day14_alignment_formula_contract.py",
                                       "day14_unobserved_feeding_transfer.py"]},
        "actual_spin_twice": tj, "reference_abs_M": ".5",
        "exact_positive_population_certificate": {
            "necessary": "7 - 10 alpha2 + 3 alpha4 >= 0",
            "at_table_mean": str(mean_dual), "maximum_on_literal_quoted_box": str(box_maximum),
            "minimum_vertex_value": str(min(dual)),
            "alpha4_min_at_source_alpha2": str((10 * a2 - 7) / 3),
            "alpha2_max_at_source_alpha4": str((7 + 3 * a4) / 10),
            "point_LP_status": int(point_lp.status), "literal_box_LP_status": int(box_lp.status),
            "no_confidence_level_assigned": True,
        },
        "paired_vertices": [{"abs_M": str(m), "alpha2": str(x), "alpha4": str(y),
                             "dual": str(v)} for (m, x, y), v in zip(paired, dual)],
        "Gaussian": {"sigma_over_J_adopted": adopted, "width_parameter": adopted * tj / 2,
                     "predicted_alpha2_alpha4": predicted.tolist(),
                     "actual_discrete_population_RMS": float(np.sqrt(pop @ (m * m))),
                     "width_from_alpha2_only": float(inverses[0]),
                     "alpha2_only_width_pair": gaussian(tj, inverses[0], weights)[0].tolist(),
                     "width_from_alpha4_only": float(inverses[1]),
                     "alpha4_only_width_pair": gaussian(tj, inverses[1], weights)[0].tolist()},
        "reference_pure_E2_point_model": {
            "scope": "Conditional pure-E2 single-photon calculation, not experimental response or E2/M3 refit",
            "complete_alignment_A2max_A4max": [str(x) for x in reference_a],
            "reference_photon_mu_mass": {str(k): str(v) for k, v in reference_photon_mass.items()},
            "Gaussian_direct_CG_A2_A4": arbitrary_gaussian_a,
            "Table4p3_fit_coefficients": [row["same_table_A2fit"], row["same_table_A4fit"]],
            "implied_alpha_if_literal_pure_point_convention": [str(x) for x in implied],
            "implied_alpha_float": [float(x) for x in implied],
            "source_Table4p1_alpha": [row["alpha2"], row["alpha4"]],
            "not_resolved": "Small E2/M3 reference interference, geometry/gate correction, coefficient convention and production normalization"
        },
        "conditions": cfg["analysis_contract"],
        "not_claimed": ["unphysical experimental data", "author implementation error",
                        "new delta or sigma measurement", "mode verdict", "formal Day16 credit"],
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "day16-se21-alignment-audit.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    csv_data = io.StringIO(newline="")
    writer = csv.writer(csv_data, lineterminator="\n")
    writer.writerow(["abs_M", "alpha2_vertex", "alpha4_vertex", "positive_dual"])
    for (m, a, b), v in zip(paired, dual):
        writer.writerow([str(m), str(a), str(b), str(v)])
    (args.output_dir / "day16-se21-positive-vertices.csv").write_text(csv_data.getvalue())
    if args.plot:
        if args.audit_scripts is None:
            raise ValueError("Plot export requires the explicitly supplied audit scripts directory")
        make_figure(tj, vertices, weights, row,
                    args.output_dir / "day16-se21-alignment-region", args.audit_scripts)
    print(json.dumps({"identity": result["data_identity"],
                      "certificate": result["exact_positive_population_certificate"],
                      "Gaussian": result["Gaussian"],
                      "reference_pure_E2_point_model": result["reference_pure_E2_point_model"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
