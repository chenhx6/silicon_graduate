#!/usr/bin/env python3
"""KS70 published-coefficient inversion and explicit operator/unit bridges.

Published errors are literal marginal ranges here, not a joint confidence model.
No event data, detector-response replay, Gaussian likelihood, or delta refit to
the full 25-correlation network is claimed. This is an uncredited Day16 preview.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from decimal import Decimal
from pathlib import Path

import numpy as np

import day16_pdco_ambiguity_preview as quantum


def angular_coefficients(parts: tuple) -> np.ndarray:
    # KS70 TableII 818->658 is 2->2->0, from an unoriented source.
    rho = np.eye(5)/5
    angles = np.array([90., 135., 180.])
    x = np.cos(np.deg2rad(angles))
    design = np.array([[1., np.polynomial.legendre.legval(t, [0, 0, 1]),
                        np.polynomial.legendre.legval(t, [0, 0, 0, 0, 1])] for t in x])
    values = []
    for theta in angles:
        values.append(sum(np.trace((second@first)@rho@(second@first).conj().T).real
                          for first in quantum.operators(2, 2, parts, 0., 0.)
                          for second in quantum.operators(2, 0, (("E", 2, 1.),), float(theta), 0.)))
    beta = np.linalg.solve(design, values)
    return beta/beta[0]


def coefficient_matrices() -> tuple[dict[int, np.ndarray], float]:
    m = angular_coefficients((("M", 1, 1.),))
    e = angular_coefficients((("E", 2, 1.),))
    mix = angular_coefficients(quantum.source_parts(math.pi/4))
    linear = 2*mix-m-e
    matrices, error = {}, 0.
    for index, rank in enumerate((0, 2, 4)):
        direct = np.array([[m[index], linear[index]/2], [linear[index]/2, e[index]]])
        final = quantum.source_f(rank, 0, rank, 2, 2, 2, 0)
        reference = final*np.array([[quantum.source_f(rank, rank, 0, ell, ellp, 2, 2)
                                     for ellp in (1, 2)] for ell in (1, 2)])
        error = max(error, float(np.max(abs(direct-reference))))
        assert np.max(abs(direct-reference))<2e-12
        assert np.max(abs(reference-reference.T))<2e-12
        reference = (reference+reference.T)/2
        reference[abs(reference)<1e-14] = 0.  # Exact angular-momentum selection zeros, not observed-data clipping.
        matrices[rank] = reference
    assert np.allclose(matrices[0], np.eye(2), atol=1e-12)
    return matrices, error


def value(matrix: np.ndarray, angle_deg: float) -> float:
    vector = np.array([math.cos(math.radians(angle_deg)), math.sin(math.radians(angle_deg))])
    return float(vector@matrix@vector)


def level_roots(matrix: np.ndarray, level: float) -> list[float]:
    allowed = np.linalg.eigvalsh(matrix)
    if level<allowed[0]-1e-12 or level>allowed[-1]+1e-12:
        return []
    a, b, c = matrix[1, 1]-level, 2*matrix[0, 1], matrix[0, 0]-level
    if abs(a)<1e-13:
        roots = [-c/b] if abs(b)>1e-13 else []
        angles = [math.degrees(math.atan(r)) for r in roots]+[-90., 90.]
    else:
        discriminant = b*b-4*a*c
        assert discriminant>=-1e-12
        root = math.sqrt(max(discriminant, 0.))
        angles = [math.degrees(math.atan((-b-root)/(2*a))), math.degrees(math.atan((-b+root)/(2*a)))]
    unique = []
    for angle in sorted(angles):
        if not unique or abs(angle-unique[-1])>1e-9:
            unique.append(angle)
    return unique


def range_preimage(matrix: np.ndarray, lower: float, upper: float) -> list[list[float]]:
    points = sorted(set([-90., 90.]+level_roots(matrix, lower)+level_roots(matrix, upper)))
    active = []
    for left, right in zip(points[:-1], points[1:]):
        middle = value(matrix, (left+right)/2)
        if lower-1e-12<=middle<=upper+1e-12:
            active.append([left, right])
    # Include any isolated extrema or exact endpoint solutions.
    for point in points:
        if lower-1e-12<=value(matrix, point)<=upper+1e-12 and not any(a-1e-9<=point<=b+1e-9 for a, b in active):
            active.append([point, point])
    merged = []
    for left, right in sorted(active):
        if merged and left<=merged[-1][1]+1e-9:
            merged[-1][1] = max(merged[-1][1], right)
        else:
            merged.append([left, right])
    return merged


def intersection(first: list, second: list) -> list[list[float]]:
    result = []
    for a, b in first:
        for c, d in second:
            if max(a, c)<=min(b, d)+1e-10:
                result.append([max(a, c), min(b, d)])
    return result


def half_last_digit(text: str) -> float:
    return float(Decimal(5).scaleb(Decimal(text).as_tuple().exponent-1))


def interval_ratio(numerator: str, energy: str, factor: float) -> list[float]:
    n, hn, e, he = float(numerator), half_last_digit(numerator), float(energy), half_last_digit(energy)
    candidates = [factor*x/y for x in (n-hn, n+hn) for y in (e-he, e+he)]
    return [min(candidates), max(candidates)]


def rounding_overlap(predicted: list[float], printed: str) -> bool:
    value_, half = float(printed), half_last_digit(printed)
    return max(predicted[0], value_-half)<=min(predicted[1], value_+half)+1e-12


def unit_checks(cfg: dict) -> dict:
    units = cfg["units_inputs"]
    me, mp, hc = units["electron_rest_energy_MeV"], units["proton_rest_energy_MeV"], units["hbar_c_MeV_fm"]
    natural_per_eb_mu = 2*units["barn_fm2"]*mp*me/hc**2
    delta_per_E_MeV_eb_mu = math.sqrt(3)/10/me*natural_per_eb_mu
    rows, precision_boundaries = [], []
    for row in cfg["rows"]:
        delta, energy = float(row["delta"]), float(row["E_keV"])
        nat_factor = 10*me*1000/math.sqrt(3)
        eb_factor = nat_factor/natural_per_eb_mu
        nat, eb = nat_factor*delta/energy, eb_factor*delta/energy
        fields = [("delta", "Delta_natural"), ("delta_error_lower", "Delta_error_lower"), ("delta_error_upper", "Delta_error_upper")]
        nat_ok = all(rounding_overlap(interval_ratio(row[a], row["E_keV"], nat_factor), row[b]) for a, b in fields)
        fields_eb = [("delta", "Delta_eb_per_muN"), ("delta_error_lower", "Delta_eb_error_lower"), ("delta_error_upper", "Delta_eb_error_upper")]
        eb_ok = all(rounding_overlap(interval_ratio(row[a], row["E_keV"], eb_factor), row[b]) for a, b in fields_eb)
        central_ok = (rounding_overlap(interval_ratio(row["delta"], row["E_keV"], nat_factor), row["Delta_natural"])
                      and rounding_overlap(interval_ratio(row["delta"], row["E_keV"], eb_factor), row["Delta_eb_per_muN"]))
        assert central_ok
        for factor, pairs in ((nat_factor, fields), (eb_factor, fields_eb)):
            for source_field, target_field in pairs:
                interval = interval_ratio(row[source_field], row["E_keV"], factor)
                if not rounding_overlap(interval, row[target_field]):
                    precision_boundaries.append({"E_keV": row["E_keV"], "input_field": source_field,
                                                  "input_printed": row[source_field], "output_field": target_field,
                                                  "output_printed": row[target_field], "strict_last_digit_interval": interval,
                                                  "scope": "Strict trailing-zero significance assumption did not close; source error-rounding recipe unknown. Data and tolerance unchanged."})
        # Figure percentages are dependent decompositions of the same fitted delta.
        m1 = 100/(1+delta*delta)
        assert abs(m1-row["Fig5_M1_percent"])<=.5
        rows.append({"E_keV_TableIII": row["E_keV"], "delta_KS": delta,
                     "Delta_natural_calculated": nat, "Delta_natural_printed": row["Delta_natural"],
                     "Delta_eb_per_muN_calculated": eb, "Delta_eb_per_muN_printed": row["Delta_eb_per_muN"],
                     "M1_percent_from_delta": m1, "M1_percent_Fig5": row["Fig5_M1_percent"],
                     "central_last_digit_rounding_overlap": central_ok,
                     "all_displayed_fields_strict_rounding_overlap": nat_ok and eb_ok,
                     "new_independent_observations": 0})
    # Component-level operator bridge, keeping the explicit magnetic minus in KS70 Eq4b.
    k, ji = .818/me, 2
    common = math.sqrt(8*math.pi*k/(2*ji+1))
    bridge_errors = []
    for kind, ell, moment in (("M", 1, 1.), ("E", 2, -4.3)):
        double_factorial = math.prod(range(1, 2*ell+2, 2))
        scalar = k**ell/double_factorial*math.sqrt((ell+1)/ell)
        ks = scalar*((1j)**ell if kind == "E" else -(1j)**(ell-1))*moment
        d96 = scalar*common*(1j)**(ell+(kind == "M"))*moment
        bridge_errors.append(abs(d96-common*ks))
    assert max(bridge_errors)<1e-12
    return {"declared_unit_inputs": units, "natural_per_eb_per_muN": natural_per_eb_mu,
            "delta_per_Egamma_MeV_Delta_eb_muN": delta_per_E_MeV_eb_mu,
            "rows": rows, "rows_used": len(rows), "pure_E2_limits_retained": cfg["pure_E2_rows_keV"],
            "strict_uncertainty_rounding_boundaries": precision_boundaries,
            "operator_bridge": "a_D96=sqrt(8*pi*k/(2Ii+1))*t_KS for same BM definitions/units/state phases; mixing ratios equal for that transition",
            "operator_bridge_component_max_error": max(bridge_errors),
            "frozen_alias_note": "Frozen input used U_KS as an engineering alias for emission RME; current text uses t_KS to avoid collision with source U_lambda deorientation. Frozen input is unchanged.",
            "precision_scope": "Central values overlap under declared rounding inputs. Printed error fields are diagnostic only: trailing zeros may be typographic, source rounding recipe is not specified. No error value or tolerance was changed; no uncertainty/confidence or historical-constants fit."}


def plot_result(out: Path, matrix: dict, cfg: dict, roots: list, audit_dir: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    sys.path.insert(0, str(audit_dir))
    from audit_panel_alignment import require_matplotlib_panel_alignment
    plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["DejaVu Sans"],
                         "font.size": 8, "axes.labelsize": 8, "axes.titlesize": 8,
                         "xtick.labelsize": 7.5, "ytick.labelsize": 7.5, "legend.fontsize": 7,
                         "svg.fonttype": "none", "pdf.fonttype": 42,
                         "axes.spines.top": False, "axes.spines.right": False})
    angles = np.linspace(-90, 90, 721)
    fig, axes = plt.subplots(1, 2, figsize=(7.204724409, 3.543307087))
    fig.subplots_adjust(left=.09, right=.98, bottom=.28, top=.79, wspace=.30)
    blue, orange = "#4C78A8", "#B57A45"
    for index, (ax, rank) in enumerate(zip(axes, (2, 4))):
        key, err = ("A22", "quoted_error_A22") if rank == 2 else ("A44", "quoted_error_A44")
        model = np.array([value(matrix[rank], t) for t in angles])
        for name, color in (("direct_TableII", blue), ("indirect_TableI_658gate", orange)):
            center, half = cfg[name][key], cfg[name][err]
            ax.axhspan(center-half, center+half, color=color, alpha=.13, lw=0, zorder=0)
            ax.axhline(center, color=color, lw=.8, ls="-" if name == "direct_TableII" else "--", zorder=1)
        ax.plot(angles, model, color="#333333", lw=1.35, zorder=3)
        for root, marker in zip(roots, ("o", "s")):
            angle = root["atan_delta_degrees"]
            ax.scatter([angle], [value(matrix[rank], angle)], marker=marker, s=25,
                       facecolor="#333333" if marker == "o" else "white", edgecolor="#333333", zorder=5)
        ax.set(xlabel="atan(delta_KS), degree", ylabel=key, xlim=(-90, 90))
        low = min(model.min(), *(cfg[n][key]-cfg[n][err] for n in ("direct_TableII", "indirect_TableI_658gate")))
        high = max(model.max(), *(cfg[n][key]+cfg[n][err] for n in ("direct_TableII", "indirect_TableI_658gate")))
        ax.set_ylim(low-.06*(high-low), high+.08*(high-low))
        ax.set_xticks([-90, -45, 0, 45, 90])
        ax.text(-.14, 1.14, chr(97+index), transform=ax.transAxes, fontweight="bold", fontsize=9)
        ax.set_title("A22: central-value double root" if rank == 2 else "A44: additional shape information", loc="left", pad=14)
    handles = [Line2D([], [], color="#333333", label="Fixed-spin point model"),
               Patch(facecolor=blue, alpha=.25, label="Table II: quoted marginal range"),
               Patch(facecolor=orange, alpha=.25, label="Table I: quoted marginal range"),
               Line2D([], [], color="#333333", marker="o", ls="", label="Larger-magnitude delta root"),
               Line2D([], [], color="#333333", marker="s", markerfacecolor="white", ls="", label="Smaller-magnitude delta root")]
    fig.legend(handles=handles, loc="lower center", bbox_to_anchor=(.5, .012), ncol=3, frameon=False, fontsize=7)
    fig.text(.5, .96, "KS70 818-658 keV: corrected coefficients and quoted errors; no joint confidence fit", ha="center", va="top", fontsize=8)
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig, json_out=out/"day16-ks70-inverse.alignment.json",
                                       require_panel_labels=True, strict=True)
    fig.savefig(out/"day16-ks70-inverse.svg")
    fig.savefig(out/"day16-ks70-inverse.pdf")
    fig.savefig(out/"day16-ks70-inverse.png", dpi=300)
    svg = out/"day16-ks70-inverse.svg"
    svg.write_text("\n".join(s.rstrip(" \t") for s in svg.read_text(encoding="utf-8").splitlines())+"\n", encoding="utf-8")
    plt.close(fig)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--units-input", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--plot-audit-dir", type=Path)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text(encoding="utf-8"))
    unit_input = json.loads(args.units_input.read_text(encoding="utf-8"))
    matrix, cross_error = coefficient_matrices()
    assert cross_error<2e-12
    roots = []
    direct, indirect = cfg["direct_TableII"], cfg["indirect_TableI_658gate"]
    for angle in level_roots(matrix[2], direct["A22"]):
        delta = math.tan(math.radians(angle))
        predicted = angular_coefficients(quantum.source_parts(math.atan(delta)))
        assert abs(predicted[1]-direct["A22"])<2e-12
        roots.append({"delta_KS": delta, "atan_delta_degrees": angle,
                      "A22_model": float(predicted[1]), "A44_model": float(predicted[2]),
                      "A44_minus_direct": float(predicted[2]-direct["A44"]),
                      "M1_fraction_model": 1/(1+delta*delta),
                      "within_literal_A44_quoted_range": bool(abs(predicted[2]-direct["A44"])<=direct["quoted_error_A44"])})
    assert len(roots) == 2
    boxes = {}
    for name in ("direct_TableII", "indirect_TableI_658gate"):
        observation = cfg[name]
        intervals = {key: range_preimage(matrix[rank], observation[key]-observation[err], observation[key]+observation[err])
                     for key, err, rank in (("A22", "quoted_error_A22", 2), ("A44", "quoted_error_A44", 4))}
        boxes[name] = {"preimages_atan_degrees": intervals,
                       "intersection_atan_degrees": intersection(intervals["A22"], intervals["A44"]),
                       "confidence_level": None, "scope": "preimage of a rectangular product of quoted marginal +/- ranges only"}
    moments = unit_checks(unit_input)
    final_delta = cfg["final_network_TableIII"]["delta_KS"]
    final_predict = angular_coefficients(quantum.source_parts(math.atan(final_delta)))
    result = {"data_identity": cfg["data_identity"], "data_kind": cfg["kind"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "unit_input_sha256": hashlib.sha256(args.units_input.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "kernel_script_sha256": hashlib.sha256(Path(quantum.__file__).read_bytes()).hexdigest(),
              "physical_matrices": {str(k): h.tolist() for k, h in matrix.items()},
              "independent_F_vs_kernel_max_error": cross_error,
              "A22_physical_range": np.linalg.eigvalsh(matrix[2]).tolist(),
              "A44_physical_range": np.linalg.eigvalsh(matrix[4]).tolist(),
              "direct_A22_central_roots": roots,
              "indirect_A22_central_roots": [math.tan(math.radians(a)) for a in level_roots(matrix[2], indirect["A22"])],
              "quoted_marginal_boxes_not_confidence_regions": boxes,
              "common_literal_box_intersection": intersection(boxes["direct_TableII"]["intersection_atan_degrees"], boxes["indirect_TableI_658gate"]["intersection_atan_degrees"]),
              "network_result_context_only": {"delta": final_delta, "predicted_A22_A44": final_predict[1:].tolist(),
                                             "added_independent_constraints": 0},
              "phase_bridge_and_units": moments,
              "interpretation_boundaries": cfg["missing"]+cfg["no_claims"]+["Unoriented opening-angle correlation, not an oriented DCO swapped detector-cell ratio",
                  "A44 is additional functional information from the same fit, not statistically independent data",
                  "Biedenharn–Rose gamma-role conversion and Rose–Brink reversed-state operator normalization are different mappings"]}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/"day16-ks70-convention-inversion.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    with (args.output_dir/"day16-ks70-root-companion.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(roots[0]), lineterminator="\n")
        writer.writeheader(); writer.writerows(roots)
    if args.plot_audit_dir:
        plot_result(args.output_dir, matrix, cfg, roots, args.plot_audit_dir)
    print(json.dumps({"roots": roots, "A22_physical_range": result["A22_physical_range"],
                      "source_F_kernel_max_error": cross_error, "box_preimages_not_CI": boxes,
                      "unit_rows": moments["rows_used"], "unit_coefficient_approx": moments["delta_per_Egamma_MeV_Delta_eb_muN"],
                      "strict_error_rounding_affected_rows": sorted({r["E_keV"] for r in moments["strict_uncertainty_rounding_boundaries"]}),
                      "scope": "uncredited Day16 preview, no joint-confidence fit or raw-data replay"}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
