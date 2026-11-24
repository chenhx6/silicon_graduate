"""Freeze and run the bounded multipolePDM grid study from the Wiki root."""

import argparse
import csv
from dataclasses import asdict, replace
from hashlib import file_digest
import json
import math
import os
from pathlib import Path
import platform
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np
import scipy
from scipy.integrate import cumulative_trapezoid, trapezoid

from multipolepdm.contracts import (
    Geometry, GridSpec, JobRequest, Measurement, ResponseGrid, Transition,
)
from multipolepdm.models.registry import evaluate_response
from multipolepdm.pdm import mapping
from multipolepdm.pdm.statistics import _summarize


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
SCRATCH = ROOT / "tmp/pdm-current-research/grid"
CASE_DIR = ROOT / "raw/code/PDM/analysis/cases"
PACKAGE = Path(mapping.__file__).resolve().parents[1]
MODES = ("P_ADO", "P_DCO", "PDCO")
TARGETS = (-0.1, 1.0, -10.0)
ANGLE_LIMIT = 89.9
SIGMA_LIMITS = (0.15, 5.0)
STEPS = (
    (0.2, 0.02), (0.2, 0.01), (0.1, 0.02), (0.1, 0.01),
    (0.05, 0.01), (0.1, 0.005), (0.05, 0.005), (0.1, 0.001),
    (0.05, 0.001),
)
TOLERANCES = {
    "angle_endpoint_deg": 0.15,
    "angle_component_mode_deg": 0.15,
    "angle_quantile_deg": 0.10,
    "angle_mean_or_std_deg": 0.10,
    "angle_cdf": 0.002,
    "s_endpoint": 0.005,
    "s_component_mode": 0.005,
    "s_quantile": 0.002,
    "s_mean_or_std": 0.002,
    "s_cdf": 0.002,
}
AUDIT = {
    "near_singular": [1e-14, 1e-12, 1e-10],
    "sigma_eps_multiplier": [32, 64, 128],
    "sigma_relative_span_nominal_eps": [0, 16, 48, 96, 192],
    "near_warning_toy_jacobian_min": 2e-15,
    "near_warning_toy_jacobian_max": 2e-10,
    "near_warning_toy_nodes": [9, 31],
}
PUBLICATIONS = {
    "B26": (
        "gpt/query/20261119-pdm-delta-broad/10.1016_j.physletb.2026.140929.pdf",
        "PDF p. 4, Table 1",
    ),
    "L22": (
        "2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf",
        "PDF p. 3, Table 1",
    ),
    "R033": (
        "gpt/query/20261119-polarization-delta-collection/10.1016_j.nuclphysa.2025.123019.pdf",
        "PDF p. 8, Table 1",
    ),
    "R034": (
        "gpt/query/20261119-polarization-delta-collection/10.1016_j.physletb.2026.140454.pdf",
        "PDF p. 4, Table 1",
    ),
    "R037": (
        "gpt/query/20261119-polarization-delta-collection/10.1016_S0375-9474_97_00058-4.pdf",
        "PDF p. 4 (printed p. 180), Table 2",
    ),
}


def load(path):
    return json.loads(path.read_text())


def dump(path, value, exclusive=False):
    with path.open("x" if exclusive else "w", encoding="ascii") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def inventory(paths, base):
    return {str(path.relative_to(base)): digest(path) for path in sorted(paths)}


def csv_rows(path, rows):
    with path.open("w", newline="", encoding="ascii") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def grid_record(angle_step, s_step):
    angle_intervals = round(2 * ANGLE_LIMIT / angle_step)
    s_intervals = round(((SIGMA_LIMITS[1] - SIGMA_LIMITS[0]) / 5) / s_step)
    return {
        "id": f"a{angle_step:g}_s{s_step:g}",
        "nominal_angle_deg": angle_step,
        "nominal_s": s_step,
        "actual_angle_deg": 2 * ANGLE_LIMIT / angle_intervals,
        "actual_angle_rad": math.radians(2 * ANGLE_LIMIT) / angle_intervals,
        "actual_s": ((SIGMA_LIMITS[1] - SIGMA_LIMITS[0]) / 5) / s_intervals,
        "angle_points": angle_intervals + 1,
        "s_points": s_intervals + 1,
        "nodes": (angle_intervals + 1) * (s_intervals + 1),
    }


def request(mode, geometry, target, gate, polar, ratio, label=""):
    return JobRequest(
        mode=mode, target=Transition(**target), label=label,
        gate=Transition(**gate) if gate else None,
        geometry=Geometry(**geometry), polarization=Measurement(**polar),
        angular_ratio=Measurement(**ratio),
    )


def observation(center, width):
    return dict(value=center, err_minus=width, err_plus=width)


def freeze(path):
    candidate_file = CASE_DIR / "candidates.json"
    evidence_file = CASE_DIR / "source_evidence.json"
    manifest_file = CASE_DIR / "empirical_manifest.json"
    manifest = {entry["path"]: entry["sha256"] for entry in load(manifest_file)["files"]}
    evidence = load(evidence_file)
    for file in (candidate_file, evidence_file):
        assert digest(file) == manifest[str(file.relative_to(ROOT))]
    published = {
        (row["nuclide"], row["energy_keV"], row["source"]): row["observations"]["P"]
        for row in evidence["cases"] if row["tier"] == "main"
    }
    empirical_rows = []
    for row in load(candidate_file)["candidates"]:
        if row["tier"] != "main":
            continue
        source = row["provenance"]["reference"]
        polar = row["observations"]["P"]
        assert polar["as_reported"] == published[row["nuclide"], row["energy_keV"], source]
        pdf, locator = PUBLICATIONS[source]
        empirical_rows.append({
            "line": row["display"], "source": source, "p_as_reported": polar["as_reported"],
            "minus": polar["minus"], "plus": polar["plus"],
            "width": (polar["minus"] + polar["plus"]) / 2,
            "pdf": f"raw/papers/{pdf}", "locator": locator,
        })
    assert len(empirical_rows) == len(published) == 10
    scientific_paths = [ROOT / row["pdf"] for row in empirical_rows]
    for pdf in set(scientific_paths):
        archived_hash = manifest.get(str(pdf.relative_to(ROOT)))
        if archived_hash:
            assert digest(pdf) == archived_hash
    floor = float(np.median([row["width"] for row in empirical_rows]))
    cases = []
    for mode in MODES:
        geometry = asdict(Geometry(
            theta_a_deg=125, theta_b_deg=90, theta_p_deg=90, theta_gate_p_deg=125,
            ratio_azimuth_average=(mode != "P_ADO"),
            polarization_gate_azimuth_average=(mode == "PDCO"),
        ))
        target = asdict(Transition(5, 4))
        gate = None if mode == "P_ADO" else asdict(Transition(4, 2, ("E2",)))
        dummy = observation(0.0, 1.0)
        job = request(mode, geometry, target, gate, dummy, dummy)
        xi = np.arctan(TARGETS)
        truth_response = evaluate_response(job, xi, np.array([1.5]))
        assert truth_response.valid.all()
        for index, delta in enumerate(TARGETS):
            polar = float(truth_response.polarization[0, index])
            ratio = float(truth_response.angular_ratio[0, index])
            cases.append({
                "id": f"{mode}_{delta:+g}", "mode": mode,
                "geometry": geometry, "target": target, "gate": gate, "target_first": True,
                "truth_delta": delta, "truth_angle_deg": math.degrees(xi[index]),
                "truth_s": 0.3, "truth_sigma": 1.5,
                "polarization": observation(polar, max(floor, 0.8 * abs(polar))),
                "ratio": observation(ratio, 0.10 * ratio),
            })
    grids = [grid_record(*steps) for steps in STEPS]
    dump(path, {
        "source_package_sha256": inventory(PACKAGE.rglob("*.py"), PACKAGE),
        "empirical_sha256": inventory(
            set([candidate_file, evidence_file, manifest_file, *scientific_paths]), ROOT,
        ),
        "empirical_rows": empirical_rows, "polarization_error_floor": floor,
        "polarization_error_rule": "max(floor, 0.8 * abs(P0))",
        "floor_rule": "Median over distinct main-tier lines of mean left/right P uncertainty",
        "ratio_error_rule": "0.10 * R0",
        "generation": "Exact forward centers with no random draw. Independent symmetric Gaussian errors.",
        "angle_limits_deg": [-ANGLE_LIMIT, ANGLE_LIMIT], "sigma_limits": SIGMA_LIMITS,
        "s_limits": [0.03, 1.0], "mass": 0.68, "cases": cases, "grids": grids,
        "reference": grids[-1]["id"],
        "recommendation_candidate": "a0.1_s0.01",
        "comparison_tolerances": TOLERANCES, "normalization_atol": 5e-12,
        "comparison_exact_agreements": ["both HDI branch counts", "domain edge flags"],
        "audit": AUDIT,
    }, exclusive=True)
    path.with_suffix(".sha256").write_text(f"{digest(path)}  {path.name}\n", encoding="ascii")


def frozen(path):
    assert digest(path) == path.with_suffix(".sha256").read_text().split()[0]
    return load(path)


def cumulative_at(axis, pdf, cumulative, queries):
    indices = np.searchsorted(axis, queries, side="right") - 1
    indices = np.clip(indices, 0, len(axis) - 2)
    offset = queries - axis[indices]
    slope = (pdf[indices + 1] - pdf[indices]) / np.diff(axis)[indices]
    return cumulative[indices] + offset * (pdf[indices] + 0.5 * slope * offset)


def summarize(axis, pdf, mass, tolerance):
    raw_area = float(trapezoid(pdf, axis))
    marginal = _summarize(axis, pdf, (mass,))
    pdf = marginal.density
    interval = marginal.intervals[0]
    cdf = cumulative_trapezoid(pdf, axis, initial=0)
    widths = np.diff(axis)
    midpoint = 0.5 * (axis[:-1] + axis[1:])
    displacement = widths / (2 * math.sqrt(3))
    nodes = np.stack([midpoint - displacement, midpoint + displacement])
    weights = 0.5 * widths * np.interp(nodes, axis, pdf)
    mean = float(np.sum(nodes * weights))
    variance = float(np.sum((nodes - mean) ** 2 * weights))
    components = []
    for lower, upper in interval.hdi:
        points = np.r_[lower, axis[(axis > lower) & (axis < upper)], upper]
        heights = np.interp(points, axis, pdf)
        peak = int(np.argmax(heights))
        component_mass = float(np.diff(cumulative_at(axis, pdf, cdf, points[[0, -1]]))[0])
        components.append({
            "lower": lower, "upper": upper, "mode": float(points[peak]),
            "mode_density": float(heights[peak]), "mass": component_mass,
        })
    hdi_mass = sum(component["mass"] for component in components)
    assert abs(hdi_mass - mass) < tolerance, (hdi_mass, mass)
    assert max(abs(raw_area - 1), abs(cdf[-1] - 1)) < tolerance
    assert (pdf >= 0).all() and (np.diff(cdf) >= 0).all()
    assert abs(float(weights.sum()) - 1) < tolerance
    width = 0.05 * (axis[-1] - axis[0])
    edge_cdf = cumulative_at(axis, pdf, cdf, np.array([axis[0] + width, axis[-1] - width]))
    return {
        "q16": interval.eti[0], "q50": marginal.median, "q84": interval.eti[1],
        "mean": mean, "std": math.sqrt(variance), "mode": marginal.mode,
        "hdi_components": components, "hdi_mass": hdi_mass,
        "hdi_threshold": interval.hdi_threshold,
        "raw_marginal_area": raw_area, "cdf_end": float(cdf[-1]),
        "edge_mass_5pct": [float(edge_cdf[0]), float(1 - edge_cdf[1])],
        "endpoint_to_peak": [float(pdf[0] / pdf.max()), float(pdf[-1] / pdf.max())],
    }, pdf, cdf


def grid_axes(config, grid):
    limits = np.deg2rad(config["angle_limits_deg"])
    spec = GridSpec(*limits, grid["angle_points"], *config["sigma_limits"], grid["s_points"])
    return spec.axes(5)


def build_job(case):
    return request(
        case["mode"], case["geometry"], case["target"], case["gate"],
        case["polarization"], case["ratio"], case["id"],
    )


def edge_flags(warnings):
    return [warning.split(" grid edge")[0] for warning in warnings if " grid edge" in warning]


def run_group(config, grid_id, mode, output):
    grid = next(grid for grid in config["grids"] if grid["id"] == grid_id)
    xi, sigma = grid_axes(config, grid)
    angle = np.rad2deg(xi)
    s = sigma / 5
    arrays = {"angle_deg": angle, "s": s}
    cases = [case for case in config["cases"] if case["mode"] == mode]
    first = build_job(cases[0])
    build_start = perf_counter()
    response = evaluate_response(first, xi, sigma)
    build_seconds = perf_counter() - build_start
    rows = []
    for index, case in enumerate(cases):
        job = build_job(case)
        start = perf_counter()
        result = mapping.map_density(job, response)
        map_seconds = perf_counter() - start
        start = perf_counter()
        pdf = result.parameter_density
        area = float(trapezoid(trapezoid(pdf, xi, axis=1), sigma))
        tolerance = config["normalization_atol"]
        assert abs(area - 1) < tolerance
        angle_stats, angle_pdf, angle_cdf = summarize(
            angle, np.deg2rad(trapezoid(pdf, sigma, axis=0)), config["mass"], tolerance,
        )
        s_stats, s_pdf, s_cdf = summarize(
            s, 5 * trapezoid(pdf, xi, axis=1), config["mass"], tolerance,
        )
        for key, values in (
            ("angle_pdf", angle_pdf), ("angle_cdf", angle_cdf),
            ("s_pdf", s_pdf), ("s_cdf", s_cdf),
        ):
            arrays[f"{key}_{index}"] = values
        rows.append({
            "case_id": case["id"], "mode": mode, "grid": grid_id, "array_index": index,
            "truth_delta": case["truth_delta"], "truth_angle_deg": case["truth_angle_deg"],
            "angle": angle_stats, "s": s_stats, "normalization": result.normalization,
            "joint_pdf_area": area, "warnings": result.warnings,
            "edge_flags": edge_flags(result.warnings),
            "valid_nodes": int(np.count_nonzero(response.valid)),
            "finite_jacobian_nodes": int(np.count_nonzero(np.isfinite(result.jacobian))),
            "truth_in_angle_hdi": any(
                component["lower"] <= case["truth_angle_deg"] <= component["upper"]
                for component in angle_stats["hdi_components"]
            ),
            "map_seconds": map_seconds, "marginal_seconds": perf_counter() - start,
        })
        del result, pdf
    peak_mib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
    dump(output.parent / f"{output.name}.json", {
        "mode": mode, "grid": grid_id, "build_seconds": build_seconds,
        "peak_process_rss_mib": peak_mib, "response_metadata": response.metadata,
        "actual_angle_endpoints_deg": angle[[0, -1]].tolist(),
        "actual_s_endpoints": s[[0, -1]].tolist(), "rows": rows,
    })
    np.savez_compressed(output.parent / f"{output.name}.npz", **arrays)


def cdf_distance(axis, pdf, cdf, other_axis, other_pdf, other_cdf):
    knots = np.union1d(axis, other_axis)
    diff = np.interp(knots, axis, pdf) - np.interp(knots, other_axis, other_pdf)
    left = diff[:-1]
    right = diff[1:]
    cross = (left * right < 0)
    roots = knots[:-1][cross] - np.diff(knots)[cross] * left[cross] / (right[cross] - left[cross])
    points = np.r_[knots, roots]
    return float(np.max(np.abs(
        cumulative_at(axis, pdf, cdf, points)
        - cumulative_at(other_axis, other_pdf, other_cdf, points)
    )))


def compare(row, ref, arrays, ref_arrays, tolerances):
    output = {
        "case_id": row["case_id"], "mode": row["mode"], "grid": row["grid"],
        "reference_grid": ref["grid"], "edge_flags_equal": row["edge_flags"] == ref["edge_flags"],
    }
    for name, axis, unit in (("angle", "angle_deg", "_deg"), ("s", "s", "")):
        sample, reference = row[name], ref[name]
        branches, ref_branches = sample["hdi_components"], reference["hdi_components"]
        same_count = len(branches) == len(ref_branches)
        output[f"{name}_branches"] = len(branches)
        output[f"{name}_reference_branches"] = len(ref_branches)
        output[f"{name}_branch_count_equal"] = same_count
        for field, fields in (("endpoint", ("lower", "upper")), ("component_mode", ("mode",))):
            output[f"{name}_{field}{unit}"] = max(
                abs(branch[key] - ref_branch[key])
                for branch, ref_branch in zip(branches, ref_branches) for key in fields
            ) if same_count else None
        output[f"{name}_quantile{unit}"] = max(
            abs(sample[key] - reference[key]) for key in ("q16", "q50", "q84")
        )
        output[f"{name}_mean_or_std{unit}"] = max(
            abs(sample[key] - reference[key]) for key in ("mean", "std")
        )
        suffix, ref_suffix = row["array_index"], ref["array_index"]
        output[f"{name}_cdf"] = cdf_distance(
            arrays[axis], arrays[f"{name}_pdf_{suffix}"], arrays[f"{name}_cdf_{suffix}"],
            ref_arrays[axis], ref_arrays[f"{name}_pdf_{ref_suffix}"], ref_arrays[f"{name}_cdf_{ref_suffix}"],
        )
    failures = [key for key in tolerances if output[key] is None or output[key] > tolerances[key]]
    failures.extend(
        key for key in ("angle_branch_count_equal", "s_branch_count_equal", "edge_flags_equal")
        if not output[key]
    )
    output["converged"] = not failures
    output["failed_checks"] = failures
    return output


def threshold_audit(config):
    settings = config["audit"]
    case = config["cases"][0]
    job = build_job(case)
    grid = next(grid for grid in config["grids"] if grid["id"] == config["recommendation_candidate"])
    normal = evaluate_response(job, *grid_axes(config, grid))
    s_count, xi_count = settings["near_warning_toy_nodes"]
    xi = np.linspace(-1, 1, xi_count)
    sigma = np.linspace(*config["sigma_limits"], s_count)
    normalized_s = (sigma - sigma[0]) / np.ptp(sigma)
    unit_s = normalized_s[:, None]
    shape = (sigma.size, xi.size)
    toy_ratio = np.broadcast_to(1 + 0.1 * xi, shape)
    toy_valid = np.ones(shape, dtype=bool)
    toy_job = replace(
        job, polarization=Measurement(0.5, 0.1, 0.1), angular_ratio=Measurement(1, 0.1, 0.1),
    )

    def toy(polar):
        return ResponseGrid(
            xi, sigma, np.broadcast_to(polar, shape), toy_ratio, toy_valid,
            job.reference_spin, job.ratio_name,
        )

    jacobian_target = np.geomspace(
        settings["near_warning_toy_jacobian_min"], settings["near_warning_toy_jacobian_max"],
        xi.size,
    )
    warning_toy = toy(0.5 + (sigma - sigma[0])[:, None] * jacobian_target / 0.1)
    original_near = mapping._NEAR_SINGULAR
    original_eps = mapping._SIGMA_EPS_MULTIPLIER
    near_rows, sigma_rows = [], []
    try:
        for label, audit_job, response in (
            ("P_ADO_-0.1", job, normal), ("low_jacobian_toy", toy_job, warning_toy),
        ):
            baseline = mapping.map_density(audit_job, response)
            for cutoff in settings["near_singular"]:
                mapping._NEAR_SINGULAR = cutoff
                trial = mapping.map_density(audit_job, response)
                np.testing.assert_array_equal(trial.parameter_density, baseline.parameter_density)
                np.testing.assert_array_equal(trial.jacobian, baseline.jacobian)
                assert trial.normalization == baseline.normalization
                assert [w for w in trial.warnings if not w.startswith("Near-singular")] == [
                    w for w in baseline.warnings if not w.startswith("Near-singular")
                ]
                near_rows.append({
                    "input": label, "threshold": cutoff, "unchanged_pdf": True,
                    "unchanged_normalization": True, "unchanged_jacobian": True,
                    "flagged_nodes": int(np.count_nonzero(trial.jacobian <= cutoff)),
                    "warnings": [w for w in trial.warnings if w.startswith("Near-singular")],
                })
            mapping._NEAR_SINGULAR = original_near

        eps = np.finfo(float).eps
        response_specs = [("P_ADO_-0.1", job, normal, None)]
        response_specs.extend(
            (f"toy_{units}_eps", toy_job, toy(0.5 + 0.5 * eps * units * unit_s), units)
            for units in settings["sigma_relative_span_nominal_eps"]
        )
        for label, audit_job, response, units in response_specs:
            field = response.polarization
            scale = np.max(np.abs(field))
            span = float(np.max(field.max(axis=0) / scale - field.min(axis=0) / scale) / eps)
            for multiplier in settings["sigma_eps_multiplier"]:
                mapping._SIGMA_EPS_MULTIPLIER = multiplier
                expected = (
                    "zero_jacobian" if units == 0 else "unresolved_sigma" if span <= multiplier else "valid"
                )
                error = None
                try:
                    mapping.map_density(audit_job, response)
                    status = "valid"
                except ValueError as exc:
                    error = str(exc)
                    if "No resolved sigma variation" in error:
                        status = "unresolved_sigma"
                    elif "Jacobian is zero" in error:
                        status = "zero_jacobian"
                    else:
                        raise
                assert status == expected, (label, multiplier, span, status)
                sigma_rows.append({
                    "input": label, "nominal_span_eps": units,
                    "measured_relative_p_span_eps": span,
                    "multiplier": multiplier, "status": status, "error": error,
                })
    finally:
        mapping._NEAR_SINGULAR = original_near
        mapping._SIGMA_EPS_MULTIPLIER = original_eps
    return {
        "near_singular": near_rows, "sigma_resolvability": sigma_rows,
        "registry_roundoff": {
            "value": 1e-12, "status": "untested",
            "reason": "Local literal in build_response, with no independently callable filter helper.",
        },
    }


def flatten_result(row):
    flat = {key: value for key, value in row.items() if key not in ("angle", "s")}
    for name in ("angle", "s"):
        if name not in row:
            continue
        values = row[name]
        flat[f"{name}_branches"] = len(values["hdi_components"])
        flat.update({f"{name}_{key}": value for key, value in values.items()})
    return {
        key: json.dumps(value) if isinstance(value, (tuple, list, dict)) else value
        for key, value in flat.items()
    }


def run(path, output):
    config = frozen(path)
    source_before = inventory(PACKAGE.rglob("*.py"), PACKAGE)
    assert source_before == config["source_package_sha256"]
    assert all(digest(ROOT / name) == value for name, value in config["empirical_sha256"].items())
    start = perf_counter()
    output.mkdir(parents=True, exist_ok=True)
    output = output.resolve()
    groups, arrays = {}, {}
    marginal_arrays = {}
    for grid in config["grids"]:
        for mode in MODES:
            grid_id = grid["id"]
            prefix = output / f"{grid_id}_{mode}"
            subprocess.run([
                sys.executable, "-B", str(Path(__file__).resolve()), "worker",
                "--input", str(path.resolve()), "--grid", grid_id, "--mode", mode,
                "--output", str(prefix),
            ], check=True)
            groups[grid_id, mode] = load(output / f"{prefix.name}.json")
            with np.load(output / f"{prefix.name}.npz") as saved:
                arrays[grid_id, mode] = {key: saved[key] for key in saved.files}
            marginal_arrays.update(
                {f"{grid_id}__{mode}__{key}": value for key, value in arrays[grid_id, mode].items()}
            )
    rows, comparisons, tradeoff = [], [], []
    reference_id = config["reference"]
    for grid in config["grids"]:
        grid_id = grid["id"]
        grid_comparisons, single_job_times, group_peaks = [], [], []
        for mode in MODES:
            group = groups[grid_id, mode]
            ref_group = groups[reference_id, mode]
            group_peaks.append(group["peak_process_rss_mib"])
            for row, ref in zip(group["rows"], ref_group["rows"]):
                assert row["case_id"] == ref["case_id"]
                rows.append(row)
                grid_comparisons.append(compare(
                    row, ref, arrays[grid_id, mode], arrays[reference_id, mode],
                    config["comparison_tolerances"],
                ))
                single_job_times.append(
                    group["build_seconds"] + row["map_seconds"] + row["marginal_seconds"]
                )
        comparisons.extend(grid_comparisons)
        tradeoff.append({
            **grid, "converged_cases": sum(row["converged"] for row in grid_comparisons),
            "cases": len(grid_comparisons),
            "single_job_seconds_median": float(np.median(single_job_times)),
            "single_job_seconds_min": min(single_job_times),
            "single_job_seconds_max": max(single_job_times),
            "max_peak_process_rss_mib": max(group_peaks),
        })
    eligible = [
        grid for grid in tradeoff
        if grid["id"] != reference_id and grid["converged_cases"] == grid["cases"]
    ]
    fastest = min(eligible, key=lambda grid: grid["single_job_seconds_median"]) if eligible else None
    audit = threshold_audit(config)
    assert inventory(PACKAGE.rglob("*.py"), PACKAGE) == source_before
    csv_rows(HERE / "results.csv", [flatten_result(row) for row in rows])
    csv_rows(HERE / "comparisons.csv", [flatten_result(row) for row in comparisons])
    csv_rows(HERE / "grid_tradeoff.csv", tradeoff)
    csv_rows(HERE / "near_singular.csv", [flatten_result(row) for row in audit["near_singular"]])
    csv_rows(HERE / "sigma_resolvability.csv", audit["sigma_resolvability"])
    np.savez_compressed(HERE / "marginals.npz", **marginal_arrays)
    dump(HERE / "threshold_audit.json", audit)
    dump(HERE / "results.json", {
        "input_sha256": digest(path), "study_script_sha256": digest(Path(__file__)),
        "python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__,
        "platform": platform.platform(), "openblas_num_threads": os.environ["OPENBLAS_NUM_THREADS"],
        "package_path": str(PACKAGE), "source_hashes_verified_before_and_after": True,
        "run_wall_seconds": perf_counter() - start,
        "reference_grid": reference_id, "fastest_converged": fastest,
        "grid_tradeoff": tradeoff,
        "response_groups": [
            {key: value for key, value in group.items() if key != "rows"} for group in groups.values()
        ],
        "rows": rows, "comparisons": comparisons,
    })
    print(json.dumps({"fastest_converged": fastest, "reference": reference_id, "rows": len(rows)}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("freeze", "run", "worker"))
    parser.add_argument("--input", type=Path, default=HERE / "frozen_inputs.json")
    parser.add_argument("--output", type=Path, default=SCRATCH)
    parser.add_argument("--grid")
    parser.add_argument("--mode", choices=MODES)
    args = parser.parse_args()
    if os.environ.get("OPENBLAS_NUM_THREADS") != "1" or not sys.dont_write_bytecode:
        parser.error("Run with OPENBLAS_NUM_THREADS=1 and python -B.")
    if args.command == "freeze":
        freeze(args.input)
    elif args.command == "run":
        run(args.input, args.output)
    else:
        run_group(frozen(args.input), args.grid, args.mode, args.output)


if __name__ == "__main__":
    main()
