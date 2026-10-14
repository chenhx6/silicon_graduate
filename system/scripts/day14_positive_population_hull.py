#!/usr/bin/env python3
"""Kinematic positive-population feasibility of published 67Ga fit means.

All source rows retain their unknown covariance. The hull assumes J=13/2,
symmetric diagonal populations, and the same complete-alignment tensor
reference. LP witnesses and covariance controls are mathematical examples,
not fitted experimental populations or an ALY/Gaussian hypothesis test.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import os
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from day14_zobel83_alignment_worksheet import (
    tensor_polynomials, alpha, inverse_alpha2)


def rational_vertices():
    j = F(13, 2)
    s = j * (j + 1)
    m = [F(2*k+1, 2) for k in range(7)]
    t2 = [3*x*x - s for x in m]
    t4 = [35*x**4 - (30*s-25)*x*x + 3*s*s-6*s for x in m]
    return m, [(a/t2[0], b/t4[0]) for a, b in zip(t2, t4)]


def rational_edges(points):
    # All seven points lie on a strictly convex parabola. Ordered by |M|,
    # they give the six lower edges and the closing upper chord.
    rows = []
    for first, second in zip(points, points[1:]+points[:1]):
        dx, dy = second[0]-first[0], second[1]-first[1]
        n = [-dy, dx]
        offset = -(n[0]*first[0] + n[1]*first[1])
        if offset < 0:  # The isotropic point (0,0) is inside.
            n, offset = [-x for x in n], -offset
        rows.append((n, offset))
    return rows


def witness(points, mean):
    aeq = np.vstack([np.ones(7), points.T])
    beq = np.r_[1., mean]
    basic = linprog(np.zeros(7), A_eq=aeq, b_eq=beq,
                    bounds=[(0, None)]*7, method="highs")
    result = {"solver_status": int(basic.status), "solver_message": basic.message,
              "feasible_exact_fit_mean": bool(basic.success),
              "q_is_a_chosen_mathematical_witness_not_measured": True}
    if basic.success:
        # Maximize the minimum pair mass to identify an interior witness.
        objective = np.r_[np.zeros(7), -1.]
        a_ub = np.c_[-np.eye(7), np.ones(7)]
        interior = linprog(objective, A_ub=a_ub, b_ub=np.zeros(7),
                           A_eq=np.c_[aeq, np.zeros(3)], b_eq=beq,
                           bounds=[(0, None)]*8, method="highs")
        if not interior.success:
            raise AssertionError("interior witness solver failed")
        result.update({"q_basic": basic.x.tolist(),
                       "q_maximum_minimum_mass": interior.x[:7].tolist(),
                       "minimum_mass": float(interior.x[7]),
                       "constraint_residual": float(np.max(abs(
                           aeq @ interior.x[:7] - beq)))})
    return result


def closest_on_hull(points, mean, covariance):
    inv = np.linalg.inv(covariance)
    candidates = []
    for k, (a, b) in enumerate(zip(points, np.roll(points, -1, axis=0))):
        d = b-a
        t = np.clip((mean-a) @ inv @ d / (d @ inv @ d), 0., 1.)
        p = a+t*d
        residual = p-mean
        candidates.append((float(residual @ inv @ residual), k, p))
    distance, edge, point = min(candidates, key=lambda x: x[0])
    return distance, edge, point


def audit(z83, z80):
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    check("ten_Z83_rows_same_fixed_parent", len(z83["rows"]) == 10 and
          z83["transition"]["Ji"] == 6.5 and z83["transition"]["Jf"] == 4.5)
    check("all_source_covariances_remain_unknown", all(
        x["covariance_alpha2_alpha4"] is None for x in z83["rows"]) and
        z80["rho_source"] is None)
    m, vertices = rational_vertices()
    edges = rational_edges(vertices)
    check("all_exact_edges_nonnegative_on_all_vertices", all(
        n[0]*p[0]+n[1]*p[1]+offset >= 0
        for n, offset in edges for p in vertices))
    v = np.array([[float(x) for x in point] for point in vertices])
    full_m, full_t = tensor_polynomials(6.5)
    positive_indices = [np.flatnonzero(np.isclose(full_m, float(x)))[0] for x in m]
    check("exact_fraction_vertices_match_full_Stevens_reference",
          np.allclose(v.T, full_t[:, positive_indices], atol=1e-14))
    check("isotropic_population_inside_hull_with_zero_tensors",
          np.allclose(v.mean(axis=0), 0, atol=1e-14))
    aeq = np.vstack([np.ones(7), v.T])
    check("three_constraints_leave_four_linear_population_directions",
          np.linalg.matrix_rank(aeq) == 3 and aeq.shape[1] - 3 == 4)

    # An exact Farkas certificate, normalized for easy interpretation.
    dual = (F(7, 3), -F(10, 3), F(1))
    dual_at_vertices = [dual[0]+dual[1]*p[0]+dual[2]*p[1] for p in vertices]
    published = [F(973, 1000), F(803, 1000)]
    violation = dual[0]+dual[1]*published[0]+dual[2]*published[1]
    check("exact_Farkas_nonnegative_columns_and_negative_mean",
          min(dual_at_vertices) == 0 and violation == -F(107, 1000))
    rounding_worst = violation + (abs(dual[1])+abs(dual[2])) * F(1, 2000)
    check("printed_three_decimal_rounding_cannot_remove_certificate",
          rounding_worst < 0)

    rows = []
    source_rows = [{"source": "Z83-11 / printed392 Table1",
                    "beam": x["beam"], "energy_MeV": x["beam_energy_lab_MeV"],
                    "mean": [x["alpha2"], x["alpha4"]],
                    "marginal_sigmas": [x["sigma_alpha2_stat_fit"],
                                        x["sigma_alpha4_stat_fit"]]}
                   for x in z83["rows"]]
    source_rows.append({"source": "Z80-17 / printed226 Table1",
                        "beam": "12C", "energy_MeV": z80["beam_energy_MeV"],
                        "mean": [z80["alpha2"], z80["alpha4"]],
                        "marginal_sigmas": [z80["sigma_alpha2"], z80["sigma_alpha4"]]})
    for i, row in enumerate(source_rows):
        mean = np.array(row["mean"])
        values = [float(n[0])*mean[0]+float(n[1])*mean[1]+float(offset)
                  for n, offset in edges]
        inside = min(values) >= -1e-12
        w = witness(v, mean)
        check(f"row{i}_LP_matches_all_hull_halfspaces", inside == w[
            "feasible_exact_fit_mean"] and w["solver_status"] in (0, 2))
        if inside:
            q = np.array(w["q_maximum_minimum_mass"])
            check(f"row{i}_witness_positive_normalized_and_exact_moments",
                  np.min(q) > 0 and np.isclose(q.sum(), 1) and
                  np.allclose(v.T @ q, mean, atol=1e-12))
        rows.append({**row, "halfspace_values": values, **w})
    check("only_alpha11p3_mean_outside_this_conditional_hull", [
        i for i, x in enumerate(rows) if not x["feasible_exact_fit_mean"]] == [0])

    # Unknown covariance: test only declared Gaussian controls. Each closest
    # point is found over ALL seven polygon edges, then independently checked
    # against the active-plane formula, not just a Gaussian population curve.
    mean = np.array(rows[0]["mean"])
    sigma = np.array(rows[0]["marginal_sigmas"])
    normal = np.array([-10/3, 1.])
    gap = .107
    threshold = -2*math.log(.32)
    controls = []
    for rho in [-.8, 0., .8, .95]:
        cov = np.outer(sigma, sigma) * np.array([[1, rho], [rho, 1]])
        distance, edge, point = closest_on_hull(v, mean, cov)
        predicted = gap*gap / (normal @ cov @ normal)
        projection = mean + gap*(cov @ normal)/(normal @ cov @ normal)
        check(f"rho{rho}_all_edge_distance_equals_active_plane_formula",
              edge == 0 and np.isclose(distance, predicted, atol=1e-11) and
              np.allclose(point, projection))
        check(f"rho{rho}_closest_point_is_on_physical_hull",
              np.isclose(point[1], 1+(10/3)*(point[0]-1)) and
              .875 <= point[0] <= 1)
        controls.append({"rho_chosen": rho, "covariance_chosen": cov.tolist(),
                         "closest_physical_point": point.tolist(),
                         "minimum_Mahalanobis_squared": distance,
                         "joint68_ellipse_intersects_hull_chosen": distance <= threshold})
    check("unknown_rho_changes_joint68_intersection_decision", controls[0][
        "joint68_ellipse_intersects_hull_chosen"] and not controls[-1][
        "joint68_ellipse_intersects_hull_chosen"])
    constant = sigma[1]**2 + (10/3*sigma[0])**2
    multiplier = 2*(10/3)*sigma[0]*sigma[1]
    critical_rho = (constant-gap*gap/threshold)/multiplier
    critical_cov = np.outer(sigma, sigma)*np.array([[1, critical_rho],
                                                  [critical_rho, 1]])
    distance, edge, critical_point = closest_on_hull(v, mean, critical_cov)
    check("conditional_rho_critical_point_is_joint68_tangent", edge == 0 and
          np.isclose(distance, threshold) and .875 < critical_point[0] < 1)
    return {
        "kind": "L2 kinematic positive-population hull applied to printed fit means",
        "conditions": {"J": "13/2", "P_minusM_equals_P_M": True,
                       "diagonal_population": True, "reference_abs_M": "1/2",
                       "source_adopted_delta": 0,
                       "not_a_reaction_population_prior": True},
        "exact_vertices": [{"abs_M": str(mm), "alpha2": str(p[0]),
                            "alpha4": str(p[1])} for mm, p in zip(m, vertices)],
        "exact_halfspaces": [{"normal": [str(x) for x in n],
                             "offset": str(b), "inequality": "n dot alpha + offset >= 0"}
                            for n, b in edges],
        "Farkas_certificate_alpha11p3": {
            "dual_normalized_lambda": [str(x) for x in dual],
            "values_on_seven_columns": [str(x) for x in dual_at_vertices],
            "value_at_printed_mean": str(violation),
            "maximum_value_with_three_decimal_rounding": str(rounding_worst),
            "lower_hull_alpha4_at_alpha2_0p973": .91,
            "printed_alpha4": .803},
        "all_source_rows": rows,
        "chosen_covariance_controls": controls,
        "joint68_full_Q_threshold": threshold,
        "chosen_model_critical_rho": critical_rho,
        "boundaries": [
            "The central-fit-mean feasibility result is conditional on fixed J, tensor reference and the source-adopted multipolarity/response convention.",
            "A fitted mean outside the kinematic hull does not reject the measurement; actual joint covariance, nuisance/response and finite-sample likelihood are not supplied.",
            "A feasible LP witness is not a measured P(M), a fitted Gaussian width, or proof of physical realization by the reaction.",
            "ALY and Gaussian curves impose feeding/population conditions in addition to quantum positivity; they are not this complete hull.",
            "No row is silently dropped; the ten nonempty Z83 rows and the matched Z80 row are all audited, and missing alpha9 remains unfilled.",
            "The chosen Gaussian covariance controls are not experimental significance, a source confidence region, or an L4 replay.",
            "The two publications share the Zobel1979 reference; independent raw sampling is not attested.",
            "Day15 remains uncredited partial preview; formal DAY14 score remains21/24."],
        "checks": checks, "checks_passed": len(checks)}


def plot(result, prefix):
    root = Path(__file__).resolve().parents[2]
    prefix.resolve().relative_to(root)
    os.environ["MPLCONFIGDIR"] = str(root/"tmp/day14-20261014/mplconfig")
    import matplotlib as mpl
    mpl.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import Polygon
    mpl.rcParams.update({"font.family": "sans-serif",
                         "font.sans-serif": ["Arial", "Liberation Sans", "DejaVu Sans"],
                         "svg.fonttype": "none", "pdf.fonttype": 42,
                         "svg.hashsalt": "day14-positive-population-hull",
                         "font.size": 9, "axes.spines.top": False,
                         "axes.spines.right": False, "axes.linewidth": .8,
                         "legend.frameon": False})
    # Explicit inch dimensions keep static and rendered width audits aligned.
    fig, ax = plt.subplots(figsize=(5.511811023622047, 4.330708661417323))
    vertices = np.array([[float(F(p["alpha2"])), float(F(p["alpha4"]))]
                         for p in result["exact_vertices"]])
    # Geometrically crop the view, rather than exporting off-page paths that
    # only rely on a renderer's clip mask. The full seven vertices remain in
    # the calculation, canonical table and source-data file.
    left = .60
    visible = []
    for first, second in zip(np.roll(vertices, 1, axis=0), vertices):
        inside_first, inside_second = first[0] >= left, second[0] >= left
        if inside_first != inside_second:
            fraction = (left-first[0]) / (second[0]-first[0])
            visible.append(first+fraction*(second-first))
        if inside_second:
            visible.append(second)
    ax.add_patch(Polygon(visible, closed=True, fc="#e7e7e7", ec=".2",
                         lw=1.1, label="Positive P(M)"))
    curve = np.array([alpha(6.5, r) for r in np.geomspace(
        .01, inverse_alpha2(6.5, left), 501)])
    ax.plot(curve[:, 0], curve[:, 1], color="#228833", lw=1.1,
            ls="--", label="Gaussian")
    rows = result["all_source_rows"]
    for beam, marker, color, label in [
        ("alpha", "o", "#cc6677", "α beam, 1983"),
        ("12C", "s", "#4477aa", "12C beam, 1983")]:
        selected = [x for x in rows[:-1] if x["beam"] == beam]
        ax.errorbar([x["mean"][0] for x in selected],
                    [x["mean"][1] for x in selected],
                    xerr=[x["marginal_sigmas"][0] for x in selected],
                    yerr=[x["marginal_sigmas"][1] for x in selected],
                    fmt=marker, color=color, markersize=4, capsize=2,
                    lw=.8, label=label)
    last = rows[-1]
    ax.errorbar(*last["mean"], xerr=last["marginal_sigmas"][0],
                yerr=last["marginal_sigmas"][1], fmt="D", mfc="white",
                mec=".15", ecolor=".15", markersize=4, capsize=2,
                lw=.8, label="12C beam, 1980")
    ax.annotate("11.3 MeV", xy=(.973, .803), xytext=(.99, .60),
                fontsize=8, ha="center", color="#aa4466",
                arrowprops={"arrowstyle": "-", "lw": .6, "color": "#aa4466"})
    ax.set(xlabel="Nuclear alignment α₂", ylabel="Nuclear alignment α₄",
           xlim=(.60, 1.04), ylim=(-.20, 1.30),
           title="67Ga, 958.0 keV: positive populations and fit means")
    ax.legend(loc="upper left", fontsize=8, handlelength=1.5, ncol=3,
              columnspacing=1.3, handletextpad=.4)
    fig.subplots_adjust(left=.15, right=.98, top=.90, bottom=.24)
    fig.text(.15, .065,
             "Fit means ± quoted stat. errors; joint covariance unavailable.\n"
             "Hull/curve: conditional J = 13/2 model, shown over α₂ ≥ 0.60.",
             fontsize=8, color=".35")
    sys.dont_write_bytecode = True
    sys.path.insert(0, "/root/.codex/skills/nature-figure/scripts")
    from audit_panel_alignment import require_matplotlib_panel_alignment
    require_matplotlib_panel_alignment(
        fig, json_out=str(prefix)+".alignment.json",
        overlay_svg=str(prefix)+".alignment.svg", strict=True)
    svg = Path(str(prefix)+".svg")
    fig.savefig(svg, metadata={"Date": None})
    svg.write_text("\n".join(x.rstrip() for x in svg.read_text().splitlines())+"\n")
    tmp_prefix = root/"tmp/day14-20261014"/prefix.name
    fig.savefig(str(tmp_prefix)+".pdf", metadata={"CreationDate": None, "ModDate": None})
    fig.savefig(str(tmp_prefix)+".png", dpi=400)
    plt.close(fig)
    with Path(str(prefix)+".source-data.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["kind", "source", "beam", "energy_MeV",
                                              "alpha2", "alpha4", "sigma2", "sigma4"],
                                lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(dict(kind="published-fit", source=row["source"],
                                 beam=row["beam"], energy_MeV=row["energy_MeV"],
                                 alpha2=row["mean"][0], alpha4=row["mean"][1],
                                 sigma2=row["marginal_sigmas"][0],
                                 sigma4=row["marginal_sigmas"][1]))
        for p in vertices:
            writer.writerow(dict(kind="task-hull-vertex", source="declared tensor model",
                                 alpha2=p[0], alpha4=p[1]))
        for p in curve:
            writer.writerow(dict(kind="task-Gaussian", source="declared Gaussian model",
                                 alpha2=p[0], alpha4=p[1]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixture-z83", type=Path, required=True)
    parser.add_argument("--fixture-z80", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plot-prefix", type=Path)
    args = parser.parse_args()
    result = audit(json.loads(args.fixture_z83.read_text()),
                   json.loads(args.fixture_z80.read_text()))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n")
    if args.plot_prefix:
        plot(result, args.plot_prefix)
    print(json.dumps({"checks_passed": result["checks_passed"],
                      "all_checks_true": all(result["checks"].values()),
                      "output": str(args.output)}))


if __name__ == "__main__":
    main()
