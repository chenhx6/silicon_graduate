#!/usr/bin/env python3
"""Replay frozen literature cases through multipolepdm."""

import argparse
import csv
from dataclasses import asdict, replace
from hashlib import sha256
from importlib.metadata import version
import json
import math
import os
from pathlib import Path
import platform
import sys
from time import perf_counter


JOB_FILES = ("point_angle_ado_jobs.json", "point_angle_dco_scenarios.json")
INPUT_FILES = (*JOB_FILES, "modeling_readiness.json", "candidates.json")
FIGURES = {
    ("80Se 783.5 keV", None): "even-even transition with precise observations",
    ("135Pr 747.3 keV", None): "asymmetric polarization error",
    ("185Au 554.9 keV", 1): "first declared geometry, for illustration",
}
REFINEMENTS = {
    ("80Se 1678.7 keV", None): "upper sigma edge with large endpoint density",
    ("135Pr 747.3 keV", None): "asymmetric polarization error",
    ("185Au 554.9 keV", 4): "first declared reversed order, with two substantial xi tails",
}
GROUPED_FOLLOWUP_REFINEMENTS = {
    "odd_odd_dco_followup_jobs_01",
    "au185-518-point-angle-jobs_01",
    "starosta-cd-extreme-target-jobs_01",
    "starosta-cd-central-target-jobs_01",
    "pal190tl-point-angle-jobs_01",
}
ASSUMPTIONS = {
    "comparison": "Point-angle models of reported observations. Exact array replay is unverified.",
    "source_alignment": "Axially symmetric magnetic-substate Gaussian, free sigma at the reference state.",
    "reference_state": "Target initial state for P_ADO; first cascade step's initial state for P_DCO.",
    "mapping": "Normalize observation density times absolute response Jacobian over the finite (xi, sigma) grid.",
    "observations": "Reported central values and lower/upper widths, independent-error approximation. Asymmetric sides each carry probability 1/2 in the production observation density.",
    "nominal_weight": "Unit additional weight in (xi, sigma).",
    "acceptance": "Point angles with no finite-ring acceptance or detector-efficiency corrections.",
    "P_ADO": "Single-line P and ratio W(theta_a)/W(theta_b), using the source worker's nominal angles and ratio order.",
    "80Se_comparison": "Published deltas were extracted from P plus R_DCO at sigma/j=0.35 (publisher supplement Sec II, Eqs1-3). These P plus R_ADO calculations scan sigma and are not replays of that extraction.",
    "P_DCO": "Gate-direction-marginalized target P; directional two-photon R_DCO for the specified order and relative azimuth.",
    "185Au": "Illustrative 90/125 degree order and relative azimuth hypotheses. All six use the same reported P and R_DCO from one line. Each is reported individually without geometry weighting.",
    "overlap": "Closed intersections with each reported delta range, using the supplied signs and quoted widths without confidence-level harmonization. Intersections are descriptive and the reported deltas can share input evidence.",
}


def digest(data):
    return sha256(data).hexdigest()


def json_text(value):
    return json.dumps(value, indent=2, allow_nan=False, ensure_ascii=True) + "\n"


def write_json(path, value):
    path.write_text(json_text(value), encoding="utf-8")


def select_package(project_root):
    if project_root is not None:
        root = project_root.resolve()
        for source in (root, root / "src", root / "GUI" / "src", root / "raw/code/PDM/GUI/src"):
            if (source / "multipolepdm/__init__.py").is_file():
                sys.path.insert(0, str(source))
                break
        else:
            raise ValueError(f"Cannot locate multipolepdm sources under {root}")
    import multipolepdm

    return multipolepdm


def code_provenance(package, *, grouped=False):
    root = Path(package.__file__).resolve().parent
    files = {str(path.relative_to(root).as_posix()): digest(path.read_bytes())
             for path in sorted(root.rglob("*.py"))
             if not grouped or path.relative_to(root).parts[0] not in ("gui", "plotting")}
    return {
        "package": package.__name__,
        "version": package.__version__,
        "root": str(root),
        "sha256_manifest": digest(json_text(files).encode()),
        "files_sha256": files,
        "runner_sha256": digest(Path(__file__).read_bytes()),
    }


def load_batch(input_bytes, input_info, readiness):
    by_label = {case["display"]: case for case in readiness["cases"]}
    if len(by_label) != len(readiness["cases"]):
        raise ValueError("Duplicate readiness labels")
    for filename in JOB_FILES:
        jobs = json.loads(input_bytes[filename])["jobs"]
        declaration = readiness["job_file_provenance"][filename]
        if declaration != {"sha256": input_info[filename]["sha256"], "jobs": len(jobs)}:
            raise ValueError(f"Job snapshot does not match modeling_readiness.json: {filename}")
        for number, document in enumerate(jobs, 1):
            label = document["label"]
            mode = document["mode"]
            declared_case = by_label[label]
            declared_model = declared_case["point_angle"][mode]
            is_scenario = mode == "P_DCO"
            if is_scenario:
                declared_geometry = next(scenario for scenario in declared_model["scenarios"]
                                         if scenario["job_number"] == number)
                declared_geometry = {key: value for key, value in declared_geometry.items()
                                     if key != "job_number"}
                for key in ("gate", "target_first", "intermediates"):
                    if document[key] != declared_model[key]:
                        raise ValueError(f"{label} job {number}: inconsistent {key}")
            else:
                if declared_model["job_number"] != number:
                    raise ValueError(f"{label}: inconsistent job number")
                declared_geometry = declared_model["geometry"]
            if (declared_model["job_file"] != filename
                    or declared_geometry != document["geometry"]):
                raise ValueError(f"{label} job {number}: inconsistent geometry declaration")
            if set(document["target"]) != {"spin_initial", "spin_final", "multipoles"}:
                raise ValueError(f"{label}: target must specify only spins and multipoles")
            source = declared_case["observation_source"]
            yield {
                "case_id": f"{mode.lower()}_{number:02d}",
                "label": label,
                "mode": mode,
                "job_number": number,
                "scenario_number": number if is_scenario else None,
                "geometry": document["geometry"],
                "observations": document["observations"],
                "job_file": filename,
                "job_file_sha256": input_info[filename]["sha256"],
                "job_sha256_canonical": digest(json_text(document).encode()),
                "source_observations": {
                    **source,
                    "provenance": readiness["sources"][source["reference"]],
                },
                "source_model_declaration": {
                    key: value for key, value in declared_model.items() if key != "scenarios"
                },
                "geometry_method_source": readiness["sources"].get(
                    declared_model.get("geometry_method_reference")
                ),
            }, document


def integral2(density, xi, sigma, trapezoid):
    return float(trapezoid(trapezoid(density, xi, axis=1), sigma))


def edge_diagnostics(axis, density, np, trapezoid):
    low, high = axis[[0, -1]]
    width = 0.05 * (high - low)
    total = trapezoid(density, axis)
    result = {}
    for name, start, end, endpoint in (
        ("lower", low, low + width, density[0]),
        ("upper", high - width, high, density[-1]),
    ):
        edge = np.r_[start, axis[(axis > start) & (axis < end)], end]
        mass = float(trapezoid(np.interp(edge, axis, density), edge) / total)
        peak_fraction = float(endpoint / density.max())
        result[name] = {
            "outer_5pct_span_mass": mass,
            "endpoint_over_peak": peak_fraction,
            "possible_truncation": mass >= 0.05 or peak_fraction >= 0.10,
        }
    return result


def marginal_summary(marginal, np, trapezoid, evaluated=None):
    axis, density = marginal.coordinate, marginal.density
    intervals = []
    evaluation = evaluated if evaluated is not None else marginal
    for interval, evaluated_interval in zip(marginal.intervals, evaluation.intervals):
        mass = 0.0
        for component, reference in zip(interval.hdi_segments, evaluated_interval.hdi_segments):
            low, high = reference.bounds
            eval_axis, eval_density = evaluation.coordinate, evaluation.density
            nodes = np.r_[low, eval_axis[(eval_axis > low) & (eval_axis < high)], high]
            integrated = trapezoid(np.interp(nodes, eval_axis, eval_density), nodes)
            if not component.mode_ranges or any(
                not component.bounds[0] <= left <= right <= component.bounds[1]
                for left, right in component.mode_ranges
            ) or abs(integrated - component.mass) > 1e-6:
                raise ValueError("Missing or inconsistent HDI component mode or mass")
            mass += integrated
        intervals.append({**asdict(interval), "hdi": interval.hdi,
                          "integrated_hdi_mass": float(mass)})
    return {
        "median": marginal.median,
        "mode": marginal.mode,
        "area": float(trapezoid(density, axis)),
        "coordinate": marginal.coordinate_name,
        "evaluation_coordinate": marginal.evaluation_coordinate,
        "intervals": intervals,
    }


def observation_compatibility(response, job, np):
    valid = response.valid
    polarization = response.polarization[valid]
    ratio = response.angular_ratio[valid]

    def error_units(predicted, measurement):
        difference = predicted - measurement.value
        return np.abs(difference) / np.where(
            difference < 0, measurement.err_minus, measurement.err_plus
        )

    distances = np.maximum(
        error_units(polarization, job.polarization),
        error_units(ratio, job.angular_ratio),
    )
    return {
        "response_P_range": [float(polarization.min()), float(polarization.max())],
        "response_ratio_range": [float(ratio.min()), float(ratio.max())],
        "grid_points_inside_joint_quoted_error_box": int((distances <= 1).sum()),
        "minimum_joint_error_box_scale": float(distances.min()),
    }


def summarize_arrays(result, summary, np, trapezoid):
    response = result.response
    xi, sigma = response.xi_rad, response.sigma
    density = result.parameter_density
    angle = marginal_summary(summary.arctan_delta, np, trapezoid)
    delta = marginal_summary(summary.delta, np, trapezoid, evaluated=summary.arctan_delta)
    sigma_over_i = marginal_summary(summary.sigma_over_i, np, trapezoid)
    area = integral2(density, xi, sigma, trapezoid)
    mass_errors = [abs(interval["integrated_hdi_mass"] - interval["mass"])
                   for curve in (delta, sigma_over_i) for interval in curve["intervals"]]
    if max(abs(area - 1), abs(angle["area"] - 1), abs(sigma_over_i["area"] - 1),
           *mass_errors) > 1e-6:
        raise ValueError("Density or interval normalization exceeds 1e-6 tolerance")
    return {
        "domain": {
            "xi_rad": [float(xi[0]), float(xi[-1])],
            "delta": [float(np.tan(xi[0])), float(np.tan(xi[-1]))],
            "sigma": [float(sigma[0]), float(sigma[-1])],
            "sigma_over_i": [float(sigma[0] / response.reference_spin),
                             float(sigma[-1] / response.reference_spin)],
            "xi_points": xi.size,
            "sigma_points": sigma.size,
            "xi_step_rad": float(xi[1] - xi[0]),
            "sigma_step": float(sigma[1] - sigma[0]),
            "xi_last_step_rad": float(xi[-1] - xi[-2]),
            "sigma_last_step": float(sigma[-1] - sigma[-2]),
            "sigma_over_i_step": float((sigma[1] - sigma[0]) / response.reference_spin),
            "sigma_over_i_last_step": float((sigma[-1] - sigma[-2]) / response.reference_spin),
            "reference_spin": response.reference_spin,
        },
        "response_metadata": response.metadata,
        "arctan_delta": angle,
        "delta": delta,
        "sigma_over_i": sigma_over_i,
        "edge_diagnostics": {
            "xi_rad": edge_diagnostics(xi, trapezoid(density, sigma, axis=0), np, trapezoid),
            "sigma": edge_diagnostics(sigma, trapezoid(density, xi, axis=1), np, trapezoid),
        },
        "joint_area": area,
        "mapped_normalization_before_unit_scaling": result.normalization,
        "invalid_response_points": int((~response.valid).sum()),
        "undefined_jacobian_points": int((~np.isfinite(result.jacobian)).sum()),
        "warnings": result.warnings,
        "observation_compatibility": observation_compatibility(response, result.job, np),
    }


def compare_resolution(nominal, fine):
    delta_nominal, delta_fine = nominal["delta"], fine["delta"]
    median_shift = abs(math.atan(delta_fine["median"]) - math.atan(delta_nominal["median"]))
    endpoints = []
    for direct, refined in zip(delta_nominal["intervals"], delta_fine["intervals"]):
        shifts = {"eti_max_endpoint_shift_xi_rad": max(
            abs(math.atan(first) - math.atan(second))
            for first, second in zip(direct["eti"], refined["eti"])
        )}
        shifts["hdi_component_counts"] = [len(direct["hdi"]), len(refined["hdi"])]
        shifts["hdi_max_endpoint_shift_xi_rad"] = (
            max(abs(math.atan(a) - math.atan(b))
                for pair, other in zip(direct["hdi"], refined["hdi"])
                for a, b in zip(pair, other))
            if len(direct["hdi"]) == len(refined["hdi"]) else None
        )
        endpoints.append({"mass": direct["mass"], **shifts})
    return {
        "xi_median_shift_rad": median_shift,
        "delta_intervals_endpoints_compared_in_xi": endpoints,
        "xi_median_target_met": median_shift <= 0.0035,
        "eti_endpoint_target_met": all(row["eti_max_endpoint_shift_xi_rad"] <= 0.0088
                                       for row in endpoints),
        "hdi_endpoint_target_met": all(
            row["hdi_max_endpoint_shift_xi_rad"] is not None
            and row["hdi_max_endpoint_shift_xi_rad"] <= 0.0088 for row in endpoints
        ),
    }


def refined_grid(grid):
    return replace(
        grid,
        xi_step_rad=grid.xi_step_rad / 2 if grid.xi_step_rad is not None else None,
        sigma_step=grid.sigma_step / 2 if grid.sigma_step is not None else None,
        xi_points=2 * grid.xi_points - 1,
        sigma_points=2 * grid.sigma_points - 1,
    )


def sensitivity_definitions(key, grid):
    if key in REFINEMENTS:
        yield "grid_refinement", refined_grid(grid), None, REFINEMENTS[key]
    if key == ("80Se 783.5 keV", None):
        yield "sigma_lower_extension", replace(grid, sigma_min=0.075, sigma_points=209), None, "precise even-even control"
    if key == ("80Se 1678.7 keV", None):
        yield "sigma_upper_extension", replace(grid, sigma_max=3.0, sigma_points=309), None, REFINEMENTS[key]
    if key == ("185Au 554.9 keV", 4):
        yield "xi_extension", replace(
            grid, xi_min_rad=-1.569, xi_max_rad=1.569, xi_points=3139
        ), None, REFINEMENTS[key]
    if key == ("185Au 554.9 keV", 1):
        yield "sigma_upper_extension", replace(grid, sigma_max=12.75, sigma_points=303), None, "upper sigma edge in first geometry"
    if key in REFINEMENTS or key == ("185Au 554.9 keV", 1):
        yield "sigma_weight", grid, "exp(-sigma/I_ref)", "exploratory downweighting of large sigma"


def annotate_figure(figure, case):
    old_height = figure.get_figheight()
    figure.set_figheight(old_height + 0.45)
    scale = old_height / figure.get_figheight()
    for axes in figure.axes:
        left, bottom, width, height = axes.get_position().bounds
        axes.set_position((left, bottom * scale, width, height * scale))
    geometry = case["geometry"]
    angles = (f"theta_a/theta_b = {geometry['theta_a_deg']:g}/{geometry['theta_b_deg']:g} deg, "
              f"theta_P = {geometry['theta_p_deg']:g} deg")
    if case["scenario_number"] is not None:
        angles = (f"scenario {case['scenario_number']} (illustrative), {angles}, "
                  f"relative phi = {geometry['relative_phi_deg']:g} deg")
    figure.text(0.5, 0.976, f"{case['label']}  |  {case['mode']} point-angle model",
                ha="center", va="top", fontsize=8)
    figure.text(0.5, 0.952, angles, ha="center", va="top", fontsize=6.5)


def run_case(case, document, output, save_grids, png, np, trapezoid, *, grouped=False):
    from multipolepdm.io.input import job_from_dict, job_to_dict
    from multipolepdm.models.registry import evaluate_response
    from multipolepdm.pdm.mapping import map_density
    from multipolepdm.pdm.statistics import summarize_density

    def evaluate(study, request, weight=None, base=None, figure_reason=None):
        elapsed = {}
        row = {
            "study": study,
            "additional_weight": weight or "unit",
            "job": job_to_dict(request),
            "timing_seconds": elapsed,
        }
        name = f"{case['case_id']}_{study}"
        started = perf_counter()
        result = None
        try:
            if weight is None:
                stamp = perf_counter()
                response = evaluate_response(request)
                elapsed["response"] = perf_counter() - stamp
                stamp = perf_counter()
                result = map_density(request, response)
                elapsed["mapping"] = perf_counter() - stamp
            else:
                stamp = perf_counter()
                response = base.response
                density = base.parameter_density * np.exp(
                    -response.sigma[:, None] / response.reference_spin
                )
                mass = integral2(density, response.xi_rad, response.sigma, trapezoid)
                result = replace(base, parameter_density=density / mass,
                                 normalization=base.normalization * mass, warnings=())
                elapsed["reweight_mapping"] = perf_counter() - stamp
            stamp = perf_counter()
            summary = summarize_density(result, masses=(0.68,))
            row.update(summarize_arrays(result, summary, np, trapezoid))
            elapsed["summary_and_diagnostics"] = perf_counter() - stamp
            row["status"] = "success"
        except Exception as error:
            row.update(status="failed", error=f"{type(error).__name__}: {error}")
        elapsed["inference"] = perf_counter() - started
        if row["status"] == "success":
            try:
                if figure_reason:
                    from matplotlib import rc_context
                    from matplotlib.backends.backend_agg import FigureCanvasAgg
                    from multipolepdm.plotting.overview import make_preview
                    from multipolepdm.plotting.style import MATPLOTLIB_STYLE

                    row["figure_selection_reason"] = figure_reason
                    stamp = perf_counter()
                    figure = make_preview(result, summary, mass=0.68).figure
                    annotate_figure(figure, case)
                    elapsed["preview_build"] = perf_counter() - stamp
                    row["figures"] = []
                    for extension in ("pdf", "png") if png else ("pdf",):
                        stamp = perf_counter()
                        path = output / f"{name}.{extension}"
                        with rc_context(MATPLOTLIB_STYLE):
                            FigureCanvasAgg(figure).print_figure(path, dpi=200)
                        elapsed[f"{extension}_render_and_write"] = perf_counter() - stamp
                        row["figures"].append({"file": path.name, "bytes": path.stat().st_size})
                    figure.clear()
                if save_grids:
                    stamp = perf_counter()
                    path = output / f"{name}.npz"
                    np.savez_compressed(
                        path, xi_rad=response.xi_rad, sigma=response.sigma,
                        polarization=response.polarization, angular_ratio=response.angular_ratio,
                        valid=response.valid, observation_density=result.observation_density,
                        jacobian=result.jacobian, parameter_density=result.parameter_density,
                    )
                    row["grid_file"] = {"file": path.name, "bytes": path.stat().st_size}
                    elapsed["grid_save"] = perf_counter() - stamp
            except Exception as error:
                row["artifact_error"] = f"{type(error).__name__}: {error}"
        print(f"{case['label']} {case['case_id']} {study} {row['status']} "
              f"{perf_counter() - started:.3f}s", flush=True)
        return row, result if row["status"] == "success" else None

    request = job_from_dict(document)
    key = (case["label"], case["scenario_number"])
    nominal, base = evaluate("nominal", request, figure_reason=None if grouped else FIGURES.get(key))
    runs = [nominal]
    studies = sensitivity_definitions(key, request.grid) if not grouped else ()
    if grouped and (key in REFINEMENTS or case["case_id"] in GROUPED_FOLLOWUP_REFINEMENTS):
        studies = [("grid_refinement", refined_grid(request.grid), None,
                    "Halve both requested steps on the same domain.")]
    for name, grid, weight, reason in studies:
        if weight and base is None:
            runs.append({"study": name, "status": "skipped", "error": "No nominal density"})
            continue
        run = evaluate(name, replace(request, grid=grid), weight, base)[0]
        run["sensitivity_selection_reason"] = reason
        if run["status"] == nominal["status"] == "success":
            if name == "grid_refinement":
                run["resolution_comparison"] = compare_resolution(nominal, run)
            run["shift_relative_to_nominal"] = {
                coordinate: {
                    stat: run[coordinate][stat] - nominal[coordinate][stat]
                    for stat in ("median", "mode")
                }
                for coordinate in ("delta", "sigma_over_i")
            }
        runs.append(run)
    return {**case, "runs": runs}


def join_literature(cases, candidates):
    by_label = {case["display"]: case for case in candidates["candidates"]}
    if len(by_label) != len(candidates["candidates"]):
        raise ValueError("Ambiguous candidate labels in literature comparison")
    for case in cases:
        candidate = by_label[case["label"]]
        case["nuclide"] = candidate["nuclide"]
        case["energy_keV"] = candidate["energy_keV"]
        case["nuclear_class"] = candidate["nuclear_class"]
        for run in case["runs"]:
            if run["status"] != "success":
                continue
            branches = []
            for branch in candidate["selection_only"]:
                center, minus, plus = (branch[key] for key in ("center", "minus", "plus"))
                if any(value is None for value in (center, minus, plus)):
                    branches.append({"reported_delta": branch["reported_delta"],
                                     "range": None, "overlap": None})
                    continue
                low, high = center - minus, center + plus
                overlaps = []
                for interval in run["delta"]["intervals"]:
                    eti_low, eti_high = interval["eti"]
                    overlaps.append({
                        "mass": interval["mass"],
                        "eti": max(low, eti_low) <= min(high, eti_high),
                        "hdi_union": any(max(low, start) <= min(high, stop)
                                         for start, stop in interval["hdi"]),
                    })
                branches.append({"reported_delta": branch["reported_delta"],
                                 "center": center, "range": [low, high], "overlap": overlaps})
            run["literature_comparison"] = branches


def write_csv(path, cases, code_hash):
    fields = [
        "case_id", "label", "mode", "scenario_number", "geometry", "study", "status",
        "observations", "job_file_sha256", "code_sha256", "reference_spin", "xi_points",
        "sigma_points", "delta_median", "delta_mode", "sigma_over_i_median",
        "sigma_over_i_mode", "delta_intervals", "sigma_over_i_intervals",
        "joint_error_box_scale", "edge_diagnostics", "literature_comparison", "error",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fields)
        writer.writeheader()
        for case in cases:
            for run in case["runs"]:
                row = {key: case[key] for key in fields if key in case}
                row.update({key: run[key] for key in fields if key in run})
                row["code_sha256"] = code_hash
                if run["status"] == "success":
                    for key in ("reference_spin", "xi_points", "sigma_points"):
                        row[key] = run["domain"][key]
                    for key in ("delta", "sigma_over_i"):
                        for stat in ("median", "mode", "intervals"):
                            row[f"{key}_{stat}"] = run[key][stat]
                    row["joint_error_box_scale"] = run["observation_compatibility"][
                        "minimum_joint_error_box_scale"
                    ]
                writer.writerow({
                    key: json.dumps(value, separators=(",", ":"))
                    if isinstance(value, (dict, list, tuple)) else value
                    for key, value in row.items()
                })


def peak_rss_bytes():
    try:
        import resource
    except ImportError:
        return None
    maximum = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return maximum if sys.platform == "darwin" else maximum * 1024


def pure_forward(document, np):
    from multipolepdm.io.input import job_from_dict, job_to_dict
    from multipolepdm.models.registry import evaluate_response

    request = job_from_dict(document)
    row = {"study": "nominal", "job": job_to_dict(request), "no_delta_pdf": True}
    try:
        _, sigma = request.grid.axes(request.reference_spin)
        response = evaluate_response(request, np.array([0.0]), sigma)
        valid = response.valid[:, 0]
        widths = sigma / request.reference_spin
        row.update(
            status="success",
            domain={"reference_spin": request.reference_spin, "sigma_points": sigma.size,
                    "sigma_over_i_step": float(widths[1] - widths[0]),
                    "sigma_over_i_last_step": float(widths[-1] - widths[-2])},
            response_metadata=response.metadata,
            forward={
                "sigma_over_i": widths.tolist(),
                "polarization": np.where(valid, response.polarization[:, 0], None).tolist(),
                "ratio": np.where(valid, response.angular_ratio[:, 0], None).tolist(),
                "defined": valid.tolist(),
            },
            observation_compatibility=observation_compatibility(response, request, np),
        )
    except Exception as error:
        row.update(status="failed", error=f"{type(error).__name__}: {error}")
    return row


def grouped_csv(path, fields, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                key: json.dumps(value, separators=(",", ":"), allow_nan=False)
                if isinstance(value, (dict, list, tuple)) else value
                for key, value in row.items()
            })


def write_grouped_tables(output, cases):
    runs, intervals, references, forward = [], [], [], []
    for case in cases:
        literature = case["literature"]
        job = case["input"]
        source = case["source_declaration"]["observation_source"]
        observations = job["observations"]
        ratio_name = "R_ADO" if case["mode"] == "P_ADO" else "R_DCO"
        identity = {
            "case_id": case["case_id"], "label": case["label"], "mode": case["mode"],
            "role": case["role"], "kind": case["kind"],
            "nuclide": literature["nuclide"], "energy_keV": literature["energy_keV"],
            "nuclear_class": literature["nuclear_class"],
            "target_spin_initial": job["target"]["spin_initial"],
            "target_spin_final": job["target"]["spin_final"], "source_reference": source["reference"],
        }
        for branch_index, branch in enumerate(literature["delta_branches"], 1):
            references.append({
                **identity, "quantity": "delta", "branch": branch_index,
                "center": branch["center"], "minus": branch["minus"], "plus": branch["plus"],
                "reference_type": branch["error_type"], "as_reported": branch["reported_delta"],
                "locator": branch["locator"], "source_coordinate": branch.get("coordinate", "delta"),
            })
        width = literature["sigma_over_i_reference"]
        if width:
            references.append({
                **identity, "quantity": "sigma_over_i", "center": width["value"],
                "minus": width.get("err_minus"), "plus": width.get("err_plus"),
                "reference_type": width["kind"], "source_coordinate": width["source_coordinate"],
                "locator": width["locator"],
            })
        for run in case["runs"]:
            run_identity = {**identity, "study": run["study"]}
            domain = run.get("domain", {})
            runs.append({
                **run_identity, "status": run["status"], "reference_spin": domain.get("reference_spin"),
                "xi_points": domain.get("xi_points"), "sigma_points": domain.get("sigma_points"),
                "xi_step_rad": domain.get("xi_step_rad"), "xi_last_step_rad": domain.get("xi_last_step_rad"),
                "sigma_over_i_step": domain.get("sigma_over_i_step"),
                "sigma_over_i_last_step": domain.get("sigma_over_i_last_step"),
                "ratio_name": ratio_name, "p_value": observations["P"]["value"],
                "p_err_minus": observations["P"]["err_minus"], "p_err_plus": observations["P"]["err_plus"],
                "ratio_value": observations[ratio_name]["value"],
                "ratio_err_minus": observations[ratio_name]["err_minus"],
                "ratio_err_plus": observations[ratio_name]["err_plus"],
                "geometry": job["geometry"], "warnings": run.get("warnings"),
                "joint_error_box_scale": run.get("observation_compatibility", {}).get(
                    "minimum_joint_error_box_scale"
                ),
                "error": run.get("error") or run.get("artifact_error"),
            })
            for coordinate in ("arctan_delta", "delta", "sigma_over_i"):
                if coordinate not in run:
                    continue
                marginal = run[coordinate]
                interval, = marginal["intervals"]
                common = {**run_identity, "coordinate": coordinate,
                          "evaluation_coordinate": marginal["evaluation_coordinate"],
                          "interval_mass": interval["mass"]}
                intervals.append({
                    **common, "interval_type": "ETI", "low": interval["eti"][0],
                    "high": interval["eti"][1], "q50": marginal["median"],
                })
                for segment_index, segment in enumerate(interval["hdi_segments"], 1):
                    for mode_index, (mode_low, mode_high) in enumerate(segment["mode_ranges"], 1):
                        intervals.append({
                            **common, "interval_type": "HDI", "segment": segment_index,
                            "low": segment["bounds"][0], "high": segment["bounds"][1],
                            "segment_mass": segment["mass"], "mode_range": mode_index,
                            "mode_low": mode_low, "mode_high": mode_high,
                        })
            if "forward" in run:
                curve = run["forward"]
                for width, pol, ratio, valid in zip(
                    curve["sigma_over_i"], curve["polarization"], curve["ratio"], curve["defined"]
                ):
                    forward.append({**run_identity, "sigma_over_i": width, "P": pol,
                                    "ratio": ratio, "response_defined": valid})

    identity_fields = ["case_id", "label", "mode", "role", "kind", "nuclide", "energy_keV",
                       "nuclear_class", "target_spin_initial", "target_spin_final", "source_reference"]
    grouped_csv(output / "results.csv", [*identity_fields, "study", "status",
                "reference_spin", "xi_points", "sigma_points", "xi_step_rad", "xi_last_step_rad",
                "sigma_over_i_step", "sigma_over_i_last_step", "p_value", "p_err_minus", "p_err_plus",
                "ratio_name", "ratio_value", "ratio_err_minus", "ratio_err_plus", "geometry",
                "warnings", "joint_error_box_scale", "error"], runs)
    grouped_csv(output / "intervals_68.csv", [*identity_fields, "study", "coordinate",
                "evaluation_coordinate", "interval_mass", "interval_type", "segment", "segment_mass",
                "low", "high", "q50", "mode_range", "mode_low", "mode_high"], intervals)
    grouped_csv(output / "literature_references.csv", [*identity_fields, "quantity", "branch",
                "center", "minus", "plus", "reference_type", "source_coordinate", "as_reported",
                "locator"], references)
    if forward:
        grouped_csv(output / "forward_curves.csv", [*identity_fields, "study", "sigma_over_i",
                    "P", "ratio", "response_defined"], forward)


def grouped_snapshot(input_dir, expected_batch):
    from build_grouped_geometry_snapshots import VERSION

    raw = (input_dir / "snapshot.json").read_bytes()
    manifest_raw = (input_dir / "manifest.json").read_bytes()
    snapshot, manifest = json.loads(raw), json.loads(manifest_raw)
    snapshot_hash = digest(raw)
    if (snapshot["schema"] != VERSION or snapshot["batch"] != expected_batch
            or manifest["schema"] != VERSION or manifest["snapshot_sha256"] != snapshot_hash
            or manifest["jobs"] != len(snapshot["cases"])):
        raise ValueError("Frozen grouped-geometry manifest or batch mismatch")
    return snapshot, {"snapshot.json": snapshot_hash, "manifest.json": digest(manifest_raw)}


def run_grouped(input_dir, output, package, batch, *, save_grids=False, entrypoint=None):
    import numpy as np
    from scipy.integrate import trapezoid

    started = perf_counter()
    frozen_input = input_dir.resolve()
    output = output.resolve()
    historical_output = frozen_input.parent / "results"
    if output == historical_output or output.is_relative_to(historical_output) or (
        output.is_relative_to(frozen_input) or frozen_input.is_relative_to(output)
    ):
        raise ValueError("Grouped results require a separate output directory")
    output.mkdir(parents=True, exist_ok=True)
    snapshot, hashes = grouped_snapshot(input_dir, batch)
    code = code_provenance(package, grouped=True)
    cases = []
    for entry in snapshot["cases"]:
        job = entry["job"]
        case = {key: value for key, value in entry.items() if key not in ("job", "historical_jobs")}
        case.update(
            input=job, label=job["label"], mode=job["mode"], geometry=job["geometry"],
            observations=job["observations"],
            job_numbers=[item["job_number"] for item in entry["historical_jobs"]],
            kind="pure_forward" if len(job["target"]["multipoles"]) == 1 else "mixed_inverse",
        )
        case["scenario_number"] = (case["job_numbers"][0]
                                   if batch == "literature" and job["mode"] == "P_DCO" else None)
        if case["kind"] == "pure_forward":
            run = pure_forward(job, np)
            case["runs"] = [run]
            print(f"{case['label']} {case['case_id']} pure_forward {run['status']}", flush=True)
        else:
            case = run_case(case, job, output, save_grids, False, np, trapezoid, grouped=True)
        case["status"] = case["runs"][0]["status"]
        cases.append(case)
    if grouped_snapshot(input_dir, batch)[1] != hashes or code_provenance(package, grouped=True) != code:
        raise RuntimeError("Production code or frozen input changed during the replay")
    if entrypoint:
        code["entrypoint_sha256"] = digest(entrypoint.read_bytes())
    failures = sum(run["status"] != "success" or bool(run.get("artifact_error"))
                   for case in cases for run in case["runs"])
    write_json(output / "results.json", {
        "schema": snapshot["schema"], "batch": batch, "frozen_inputs_sha256": hashes,
        "sources": snapshot["sources"], "legacy_inputs_sha256": snapshot["legacy_inputs_sha256"],
        "provenance": code, "interval_mass": 0.68, "reported_delta_used_in_inference": False,
        "geometry_scope": "Declared response models; alternatives share observations. "
                          "Ideal rings assume uniform relative azimuth acceptance.",
        "cases": cases, "failed_runs": failures, "elapsed_seconds": perf_counter() - started,
    })
    write_grouped_tables(output, cases)
    print(f"{len(cases)} grouped snapshot cases, {failures} failed runs", flush=True)
    return int(failures != 0)


def main():
    started = perf_counter()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Directory of frozen inputs")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--project-root", type=Path, help="PDM, GUI, source, or containing wiki root")
    parser.add_argument("--save-grids", action="store_true", help="Save compressed full arrays for every run")
    parser.add_argument("--png", action="store_true", help="Also render the three PDF overviews as PNG")
    args = parser.parse_args()
    sys.dont_write_bytecode = True
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    os.environ["MPLCONFIGDIR"] = str(output / ".matplotlib")
    os.environ.setdefault("MPLBACKEND", "Agg")
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    package = select_package(args.project_root)
    if (args.input / "snapshot.json").is_file():
        return run_grouped(args.input, output, package, "literature", save_grids=args.save_grids)
    import numpy as np
    from scipy.integrate import trapezoid

    input_bytes = {name: (args.input / name).read_bytes() for name in INPUT_FILES}
    input_info = {name: {"sha256": digest(data), "bytes": len(data)}
                  for name, data in input_bytes.items()}
    code = code_provenance(package)
    readiness = json.loads(input_bytes["modeling_readiness.json"])
    batch = tuple(load_batch(input_bytes, input_info, readiness))
    cases = [run_case(case, doc, output, args.save_grids, args.png, np, trapezoid)
             for case, doc in batch]
    comparison_start = perf_counter()
    join_literature(cases, json.loads(input_bytes["candidates.json"]))
    comparison_seconds = perf_counter() - comparison_start
    if code_provenance(package) != code:
        raise RuntimeError("Production code or runner changed while the cases were running")
    if any(digest((args.input / name).read_bytes()) != entry["sha256"]
           for name, entry in input_info.items()):
        raise RuntimeError("Input snapshot changed while the cases were running")

    success = [case for case in cases if case["runs"][0]["status"] == "success"]
    coverage = {
        mode: {
            "successful_nominal_runs": sum(case["mode"] == mode for case in success),
            "distinct_lines": len({case["label"] for case in success if case["mode"] == mode}),
            "distinct_nuclides": sorted({case["nuclide"] for case in success if case["mode"] == mode}),
            "exact_published_array_replays": 0,
        }
        for mode in ("P_ADO", "P_DCO", "PDCO")
    }
    coverage["odd_odd_successful_lines"] = sum(
        case["nuclear_class"] == "odd-odd" for case in success
    )
    rows = [run for case in cases for run in case["runs"]]
    failure_count = sum(run["status"] != "success" or "artifact_error" in run for run in rows)
    write_started = perf_counter()
    write_csv(output / "results.csv", cases, code["sha256_manifest"])
    report = {
        "title": "Literature point-angle model comparisons",
        "argv": [sys.executable, *sys.argv],
        "working_directory": str(Path.cwd()),
        "input_directory": str(args.input.resolve()),
        "input_files": input_info,
        "code": code,
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "dependencies": {name: version(name) for name in ("numpy", "scipy", "matplotlib", "sympy")},
            "openblas_num_threads": os.environ["OPENBLAS_NUM_THREADS"],
            "peak_process_rss_bytes": peak_rss_bytes(),
        },
        "model_assumptions": ASSUMPTIONS,
        "diagnostics": {
            "edge_flag_rule": "Report each endpoint and outer 5% of in-grid span; flag >=10% of peak density or >=5% of total in-grid mass. Outside-grid mass is unknown.",
            "joint_error_box_scale": "Smallest simultaneous P and ratio error-box scale containing any valid model grid point, using each quoted directional width. Geometric diagnostic without a chi-square fit or a p-value.",
            "sensitivity_weight": "Exploratory exp(-sigma/I_ref) applied only to the mapped density after nominal inference; renormalized on the nominal domain. No experimental calibration is implied.",
            "sensitivity_bounds": "Bound changes evaluated independently from point-count refinement; nominal step sizes are held approximately fixed.",
        },
        "coverage": coverage,
        "run_counts": {"total": len(rows), "success": len(rows) - failure_count,
                       "failed_or_skipped": failure_count},
        "cases": cases,
        "timing_seconds": {
            "comparison_join": comparison_seconds,
            "csv_write": perf_counter() - write_started,
            "wall_before_json_write": perf_counter() - started,
        },
    }
    write_json(output / "results.json", report)
    print(f"{len(success)}/{len(cases)} nominal runs successful; "
          f"{failure_count} failed or skipped runs/artifacts; {perf_counter() - started:.3f}s total",
          flush=True)
    return int(failure_count != 0)


if __name__ == "__main__":
    raise SystemExit(main())
