"""Deterministic 26/90 degree ring-average benchmark, independent of old recoveries.

Run from any directory with ``python3 /path/to/benchmark_geometry_26.py run``.
The default output is analysis/benchmarks/geometry26_20261125. Existing files
are never overwritten by run. Use ``verify`` or ``summary`` to consume a run.

Python API: load_case('N10') -> (MappingResult, Summary, record), load_records(),
summarize_results(records). N01..N10 are P_ADO, N11..N20 P_DCO, N21..N30 PDCO;
within each mode delta increases through DELTAS. N10/N20/N30 have delta=+10.

Nxx.npz parameter_density is per radian per sigma/I (I_ref times the native
MappingResult density). parameter_density_per_rad_sigma preserves the native
array exactly. jacobian is the native |d(P,R)/d(angle,sigma)|. Formal v3
export_result snapshots live in snapshots/Nxx and retain all native arrays.

HDI mass is probability under the full marginal; mass_fraction is the branch's
share of the complete 68% HDI union. True delta-PDF statistics are evaluated
on its Jacobian-transformed curve with the existing statistics implementation;
they are separate from tan-transformed angle statistics. No kernel is changed.
"""

from __future__ import annotations

import argparse
import json
import shlex
import sys
from collections import Counter
from dataclasses import asdict, replace
from datetime import datetime, timezone
from hashlib import sha256
from importlib.metadata import version
from math import atan, fsum, radians
from pathlib import Path
from time import perf_counter

sys.dont_write_bytecode = True

import numpy as np
from scipy.integrate import trapezoid

PROJECT = Path(__file__).resolve().parents[2]
ROOT = PROJECT.parents[2]
PACKAGE = PROJECT / "GUI/src/multipolepdm"
sys.path.insert(0, str(PACKAGE.parent))

from multipolepdm import __version__
from multipolepdm.contracts import (
    Geometry,
    GridSpec,
    JobRequest,
    Measurement,
    OutputSpec,
    Transition,
)
from multipolepdm.io.export import export_result, load_snapshot
from multipolepdm.io.input import job_to_dict
from multipolepdm.models.registry import evaluate_response
from multipolepdm.pdm.mapping import map_density
from multipolepdm.pdm.statistics import (
    _summarize,
    density_segment,
    summarize_density,
)
from multipolepdm.physics.detectors import DetectorDirection, DetectorGroup

MODES = ("P_ADO", "P_DCO", "PDCO")
DELTAS = (-10., -5., -1., -.5, -.1, .1, .5, 1., 5., 10.)
MASS = .68
TRUTH_SIGMA = 1.5
TRUTH_ALIGNMENT = .3
P_ERROR_FLOOR = .1075
DEFAULT_OUTPUT = PROJECT / "analysis/benchmarks/geometry26_20261125"
FROZEN_INPUT = PROJECT / "analysis/research/grid_resolution/frozen_inputs.json"
OLD_EVIDENCE = PROJECT / "analysis/benchmarks/sigma03_relP80_relR10"
SCHEMA = "multipolepdm-geometry26-v1"


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def save_json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, ensure_ascii=False,
                                    allow_nan=False) + "\n", encoding="utf-8")


def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()


def file_record(path, *, source):
    path = Path(path).resolve()
    return {"path": path.relative_to(ROOT).as_posix(), "size": path.stat().st_size,
            "sha256": digest(path), "source": source}


def tree_hashes(path):
    return {p.relative_to(path).as_posix(): digest(p)
            for p in sorted(Path(path).rglob("*")) if p.is_file()}


def grid_spec():
    return GridSpec(xi_min_rad=radians(-89), xi_max_rad=radians(89),
                    xi_step_rad=radians(.1), xi_input_unit="rad",
                    sigma_min=.15, sigma_max=5., sigma_step=.025,
                    sigma_input_unit="sigma")


def detector_group(theta):
    return DetectorGroup((DetectorDirection(theta, phi_deg=0.),), normalization="mean")


def make_job(mode, grid=None):
    return JobRequest(
        mode=mode, target=Transition(5, 4, ("M1", "E2")),
        gate=None if mode == "P_ADO" else Transition(4, 2, ("E2",)),
        target_first=True, intermediates=(),
        polarization=Measurement(0., P_ERROR_FLOOR, P_ERROR_FLOOR),
        angular_ratio=Measurement(1., .1, .1),
        geometry=Geometry(
            theta_a_deg=26., theta_b_deg=90., theta_p_deg=90.,
            theta_gate_p_deg=90., relative_phi_deg=0., phi_p_deg=0., phi_gate_p_deg=0.,
            ratio_azimuth_average=False, polarization_gate_azimuth_average=False,
            ratio_group_a=detector_group(26.), ratio_group_b=detector_group(90.),
            polarization_group=detector_group(90.),
            polarization_gate_group=detector_group(90.) if mode == "PDCO" else None,
            select_azimuth=False,
        ), grid=grid if grid is not None else grid_spec(),
    )


def response_key(job):
    """Cache only the response inputs; observations never enter the shared cache."""
    return sha256(json.dumps({
        "mode": job.mode, "target": asdict(job.target),
        "gate": asdict(job.gate) if job.gate else None,
        "target_first": job.target_first,
        "intermediates": [asdict(t) for t in job.intermediates],
        "geometry": asdict(job.geometry), "grid": asdict(job.grid),
    }, sort_keys=True).encode()).hexdigest()


class ResponseCache:
    def __init__(self):
        self.responses = {}
        self.evaluations = 0
        self.hits = 0

    def get(self, job):
        key = response_key(job)
        if key not in self.responses:
            self.responses[key] = evaluate_response(job)
            self.evaluations += 1
        else:
            self.hits += 1
        return self.responses[key]


def production_truth(job, delta):
    response = evaluate_response(job, np.array([atan(delta)]), np.array([TRUTH_SIGMA]))
    if not response.valid[0, 0]:
        raise ValueError(f"Invalid generated truth for {job.mode}, delta={delta}.")
    return float(response.polarization[0, 0]), float(response.angular_ratio[0, 0])


def observed_job(template, case_id, p, ratio):
    err_p, err_r = max(P_ERROR_FLOOR, .8 * abs(p)), .1 * abs(ratio)
    return replace(template, label=case_id,
                   polarization=Measurement(p, err_p, err_p),
                   angular_ratio=Measurement(ratio, err_r, err_r),
                   output=OutputSpec(directory="snapshots", full_csv=False))


def marginal_statistics(marginal, truth):
    interval, = marginal.intervals
    total = fsum(s.mass for s in interval.hdi_segments)
    return {
        "coordinate": marginal.coordinate_name,
        "evaluation_coordinate": marginal.evaluation_coordinate,
        "q16": interval.eti[0], "q50": marginal.median, "q84": interval.eti[1],
        "eti": list(interval.eti), "mode": marginal.mode,
        "mean": marginal.mean, "std": marginal.std,
        "mean_bounds": list(marginal.mean_bounds),
        "mean_bound_flags": marginal.mean_bound_flags,
        "hdi_mass": total, "interval_mass": interval.mass,
        "hdi_threshold": interval.hdi_threshold,
        "hdi_component_count": len(interval.hdi_segments),
        "hdi_segments": [
            {**asdict(s), "mass_fraction": s.mass / total,
             "contains_truth": bool(s.bounds[0] <= truth <= s.bounds[1])}
            for s in interval.hdi_segments
        ],
        "hdi_contains_truth": any(s.bounds[0] <= truth <= s.bounds[1]
                                  for s in interval.hdi_segments),
        "eti_contains_truth": bool(interval.eti[0] <= truth <= interval.eti[1]),
        "q50_minus_truth": marginal.median - truth,
    }


def case_statistics(result, summary, delta):
    angle = summary.arctan_delta
    # The existing routine evaluates the supplied true delta curve, rather than
    # interpreting Summary.delta's legacy transformed estimates as PDF stats.
    curve = summary.delta_pdf
    delta_stats = _summarize(curve.coordinate, curve.density, (MASS,), "delta")
    transformed = marginal_statistics(summary.delta, delta)
    transformed.update(
        interpretation="Direct tan endpoints/estimates of angle statistics; not delta-PDF HDI or mean.",
        hdi_threshold_applies_to="arctan_delta PDF only",
    )
    nodes, heights = density_segment(angle.coordinate, angle.density,
                                    (-abs(atan(delta)), abs(atan(delta))))
    spin = result.response.reference_spin
    raw = result.parameter_density
    i, j = np.unravel_index(np.argmax(raw), raw.shape)
    return {
        "arctan_delta": marginal_statistics(angle, atan(delta)),
        "tan_angle_statistics": transformed,
        "delta_pdf": {**marginal_statistics(delta_stats, delta),
                      "density_definition": "p_delta = p_angle(arctan(delta))/(1+delta**2)",
                      "evaluation": "Existing _summarize on the exported refined delta PDF",
                      "curve_area": float(trapezoid(curve.density, curve.coordinate))},
        "sigma_over_i": marginal_statistics(summary.sigma_over_i, TRUTH_ALIGNMENT),
        "probability_smaller_absolute_delta": float(trapezoid(heights, nodes)),
        "joint_mode": {"angle_rad": float(result.response.xi_rad[j]),
                       "sigma_over_i": float(result.response.sigma[i] / spin)},
    }


def export_slide_npz(path, result, summary):
    r = result.response
    np.savez_compressed(
        path, angle=r.xi_rad, sigma_over_i=r.sigma / r.reference_spin,
        parameter_density=r.reference_spin * result.parameter_density,
        parameter_density_per_rad_sigma=result.parameter_density,
        response_P=r.polarization, response_R=r.angular_ratio,
        observation_density=result.observation_density, valid=r.valid,
        jacobian=result.jacobian, sigma=r.sigma,
        delta_pdf_coordinate=summary.delta_pdf.coordinate,
        delta_pdf_density=summary.delta_pdf.density,
        angle_pdf=summary.arctan_delta.density,
        sigma_over_i_pdf=summary.sigma_over_i.density,
        reference_spin=np.array(r.reference_spin),
        normalization=np.array(result.normalization),
    )


def check_result(result, summary):
    r = result.response
    native_area = trapezoid(trapezoid(result.parameter_density, r.xi_rad, axis=1), r.sigma)
    np.testing.assert_allclose(native_area, 1., atol=5e-12, rtol=0)
    checks = {"native_density_area": float(native_area)}
    for name in ("arctan_delta", "sigma_over_i"):
        m = getattr(summary, name)
        area = trapezoid(m.density, m.coordinate)
        np.testing.assert_allclose(area, 1., atol=5e-12, rtol=0)
        interval, = m.intervals
        mass = fsum(s.mass for s in interval.hdi_segments)
        np.testing.assert_allclose(mass, MASS, atol=5e-12, rtol=0)
        quantile_mass = []
        for quantile in (*interval.eti[:1], m.median, interval.eti[1]):
            x, y = density_segment(m.coordinate, m.density, (m.coordinate[0], quantile))
            quantile_mass.append(float(trapezoid(y, x)))
        np.testing.assert_allclose(quantile_mass, [.16, .5, .84], atol=5e-12, rtol=0)
        checks[name] = {"area": float(area), "hdi_integrated_mass": mass,
                        "cdf_at_q16_q50_q84": quantile_mass}
    curve = summary.delta_pdf
    expected = np.interp(np.arctan(curve.coordinate), summary.arctan_delta.coordinate,
                         summary.arctan_delta.density) / (1 + curve.coordinate**2)
    # _delta_report normalizes its adaptively refined trapezoidal curve.
    expected /= trapezoid(expected, curve.coordinate)
    np.testing.assert_allclose(curve.density, expected, atol=5e-12, rtol=5e-12)
    checks["delta_pdf_jacobian_max_abs_error"] = float(np.max(np.abs(curve.density - expected)))
    np.testing.assert_allclose(
        [summary.delta.intervals[0].eti[0], summary.delta.median, summary.delta.intervals[0].eti[1]],
        np.tan([summary.arctan_delta.intervals[0].eti[0], summary.arctan_delta.median,
                summary.arctan_delta.intervals[0].eti[1]]), atol=5e-12, rtol=5e-12)
    expected_ratio_average = result.job.mode != "P_ADO"
    expected_p_average = result.job.mode == "PDCO"
    if (r.metadata["select_azimuth"] is not False
            or r.metadata["ratio_azimuth_average"] != expected_ratio_average
            or r.metadata["polarization_gate_azimuth_average"] != expected_p_average
            or not r.metadata["azimuth_integration"].startswith("Uniform nine-node")):
        raise ValueError("Benchmark response must use the unselected-phi ring-average path.")
    return checks


def load_records(directory=DEFAULT_OUTPUT):
    return read_json(Path(directory) / "results.json")["injections"]


def load_case(case_id, directory=DEFAULT_OUTPUT):
    """Read formal snapshots only; this never evaluates a response or remaps."""
    directory = Path(directory)
    row = next(r for r in load_records(directory) if r["case_id"] == case_id)
    result, summary = load_snapshot(directory / row["snapshot_path"])
    return result, summary, row


def summarize_results(records):
    def counts(rows):
        angle = [r["statistics"]["arctan_delta"] for r in rows]
        delta = [r["statistics"]["delta_pdf"] for r in rows]
        sigma = [r["statistics"]["sigma_over_i"] for r in rows]
        return {
            "cases": len(rows),
            "angle_hdi_contains_truth": sum(s["hdi_contains_truth"] for s in angle),
            "angle_eti_contains_truth": sum(s["eti_contains_truth"] for s in angle),
            "delta_pdf_hdi_contains_truth": sum(s["hdi_contains_truth"] for s in delta),
            "delta_pdf_eti_contains_truth": sum(s["eti_contains_truth"] for s in delta),
            "sigma_hdi_contains_truth": sum(s["hdi_contains_truth"] for s in sigma),
            "sigma_eti_contains_truth": sum(s["eti_contains_truth"] for s in sigma),
            "angle_hdi_branch_counts": dict(Counter(str(s["hdi_component_count"]) for s in angle)),
            "delta_pdf_hdi_branch_counts": dict(Counter(str(s["hdi_component_count"]) for s in delta)),
            "interpretation": "Deterministic truth membership counts, not repeated-sampling coverage.",
        }
    large = [r for r in records if abs(r["delta_truth"]) >= 5]
    return {
        "all": counts(records),
        "by_mode": {m: counts([r for r in records if r["mode"] == m]) for m in MODES},
        "large_absolute_delta": {
            "all": counts(large),
            "negative": counts([r for r in large if r["delta_truth"] < 0]),
            "positive": counts([r for r in large if r["delta_truth"] > 0]),
            "median_smaller_absolute_delta_count": sum(
                abs(r["statistics"]["tan_angle_statistics"]["q50"]) < abs(r["delta_truth"])
                for r in large),
            "cases": [{"case_id": r["case_id"], "mode": r["mode"],
                       "delta_truth": r["delta_truth"],
                       **{k: r["statistics"][k] for k in
                          ("arctan_delta", "tan_angle_statistics", "delta_pdf")},
                       "probability_smaller_absolute_delta":
                       r["statistics"]["probability_smaller_absolute_delta"]} for r in large],
        },
    }


def floor_evidence():
    frozen = read_json(FROZEN_INPUT)
    rows = frozen["empirical_rows"]
    if len({r["line"] for r in rows}) != len(rows):
        raise ValueError("Frozen empirical error rows are not distinct.")
    widths = [(r["minus"] + r["plus"]) / 2 for r in rows]
    np.testing.assert_allclose(widths, [r["width"] for r in rows], atol=2e-16, rtol=0)
    median = float(np.median(widths))
    np.testing.assert_allclose([median, frozen["polarization_error_floor"]],
                               P_ERROR_FLOOR, atol=2e-16, rtol=0)
    originals = []
    for path in sorted({r["pdf"] for r in rows}):
        p = ROOT / path
        if digest(p) != frozen["empirical_sha256"][path]:
            raise ValueError(f"Frozen empirical original hash mismatch: {path}")
        originals.append(file_record(p, source="Original identified in frozen_inputs.json empirical_rows"))
    return {"frozen_input": file_record(FROZEN_INPUT, source="Local experimental error-floor evidence"),
            "rule": frozen["floor_rule"], "distinct_lines": len(rows), "rows": rows,
            "computed_widths": widths, "computed_median": median,
            "adopted_floor": P_ERROR_FLOOR,
            "scope": "Recomputed from frozen local extracted errors; no new PDF re-extraction.",
            "original_files": originals}


def verify(directory=DEFAULT_OUTPUT, *, check_manifest=True):
    directory = Path(directory)
    rows = load_records(directory)
    expected_ids = [f"N{i:02d}" for i in range(1, 31)]
    if [r["case_id"] for r in rows] != expected_ids:
        raise ValueError("Expected precisely N01..N30.")
    checks = []
    for row in rows:
        result, summary, _ = load_case(row["case_id"], directory)
        for a in ("observation_density", "jacobian", "parameter_density"):
            if getattr(result, a).shape != (195, 1781):
                raise ValueError(f"Unexpected shape: {row['case_id']}/{a}")
        stats = case_statistics(result, summary, row["delta_truth"])
        if json.loads(json.dumps(stats)) != row["statistics"]:
            raise ValueError(f"Snapshot statistics disagree for {row['case_id']}")
        local = check_result(result, summary)
        with np.load(directory / row["npz_path"], allow_pickle=False) as data:
            for name, expected in {
                "angle": result.response.xi_rad,
                "sigma_over_i": result.response.sigma / result.response.reference_spin,
                "parameter_density": result.parameter_density * result.response.reference_spin,
                "parameter_density_per_rad_sigma": result.parameter_density,
                "response_P": result.response.polarization,
                "response_R": result.response.angular_ratio,
                "observation_density": result.observation_density,
                "valid": result.response.valid, "jacobian": result.jacobian,
                "delta_pdf_coordinate": summary.delta_pdf.coordinate,
                "delta_pdf_density": summary.delta_pdf.density,
            }.items():
                np.testing.assert_array_equal(data[name], expected)
            area = trapezoid(trapezoid(data["parameter_density"], data["angle"], axis=1),
                             data["sigma_over_i"])
            np.testing.assert_allclose(area, 1., atol=5e-12, rtol=0)
            local["slide_density_area"] = float(area)
        checks.append({"case_id": row["case_id"], **local})
    if check_manifest:
        manifest = read_json(directory / "manifest.json")
        for entry in manifest["files"]:
            p = ROOT / entry["path"]
            if p.stat().st_size != entry["size"] or digest(p) != entry["sha256"]:
                raise ValueError(f"Archive integrity failure: {p}")
    return {"status": "passed", "cases": len(checks), "checks": checks,
            "method": "Snapshot load, exact companion-array comparison, numerical quadrature and all branch stats; no mapping rerun."}


def run(directory=DEFAULT_OUTPUT):
    directory = Path(directory).resolve()
    if directory != DEFAULT_OUTPUT.resolve() and DEFAULT_OUTPUT.resolve() not in directory.parents:
        raise ValueError("Output must be in the exclusively owned geometry26_20261125 tree.")
    if directory.exists() and any(p.name != "trials" for p in directory.iterdir()):
        raise FileExistsError("Output is nonempty. Use verify/summary; run never overwrites evidence.")
    directory.mkdir(parents=True, exist_ok=True)
    started = perf_counter()
    old_start = tree_hashes(OLD_EVIDENCE)
    if not old_start:
        raise ValueError("Expected the read-only old evidence baseline to exist.")
    sources = [*sorted(PACKAGE.rglob("*.py")), Path(__file__).resolve()]
    test_path = PROJECT / "analysis/tests/test_geometry26.py"
    if test_path.is_file():
        sources.append(test_path)
    source_start = {str(p.relative_to(ROOT)): digest(p) for p in sources}
    inputs = directory / "inputs"
    inputs.mkdir()
    for source in sources:
        target = inputs / source.relative_to(PROJECT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())
    (inputs / "frozen_inputs.json").write_bytes(FROZEN_INPUT.read_bytes())
    floor = floor_evidence()
    save_json(directory / "floor_evidence.json", floor)
    grid = grid_spec()
    xi, sigma = grid.axes(5.)
    frozen = {
        "schema": SCHEMA, "generator": "evaluate_response production kernel",
        "truth": {"deltas": DELTAS, "source_spin": 5., "sigma": TRUTH_SIGMA,
                  "sigma_over_i": TRUTH_ALIGNMENT, "population": "single axial Gaussian at I=5"},
        "errors": {"P": "max(0.1075,0.8*abs(P))", "R": "0.1*abs(R)",
                   "sides": "Positive absolute magnitudes, equal left/right", "center_noise": "none"},
        "jobs": {m: job_to_dict(make_job(m, grid)) for m in MODES},
        "grid_actual": {"xi_bounds_rad": xi[[0, -1]].tolist(),
                        "xi_bounds_deg": np.rad2deg(xi[[0, -1]]).tolist(),
                        "xi_step_rad": radians(.1), "sigma_bounds": sigma[[0, -1]].tolist(),
                        "sigma_step": .025, "sigma_over_i_bounds": [.03, 1.],
                        "sigma_over_i_step": .005, "shape_sigma_by_angle": [len(sigma), len(xi)],
                        "nodes": len(sigma) * len(xi)},
        "interval_mass": MASS, "all_hdi_branches": True,
        "mass_fraction_definition": "branch mass / mass of complete 68% HDI union",
        "ratio": "target A gate B / target B gate A; A=26 deg, B=90 deg; unselected relative phi",
        "polarization": "P at 90 deg; PDCO downstream directional gate at 90 deg; unselected relative phi",
        "azimuth_average": True,
        "geometry_flags": {"select_azimuth": False, "ratio_azimuth_average": False,
                           "polarization_gate_azimuth_average": False},
        "flag_interpretation": "Grouped detector API: select_azimuth=False averages intensities over phi irrespective of the two legacy False averaging flags. Numerical phi=0 inputs are not selected directions.",
        "npz_density": "parameter_density per radian per sigma/I = I_ref * MappingResult.parameter_density",
        "npz_jacobian": "native abs d(P,R)/d(angle_rad,sigma)",
        "id_order": "N01..N10 P_ADO; N11..N20 P_DCO; N21..N30 PDCO; each in deltas order",
    }
    save_json(directory / "frozen_job.json", frozen)
    provenance = {
        "schema": SCHEMA, "command": shlex.join([sys.executable, *sys.argv]),
        "working_directory": str(Path.cwd()), "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "package_version": __version__, "python": sys.version,
        "dependencies": {n: version(n) for n in ("numpy", "scipy", "sympy", "matplotlib")},
        "source_sha256": source_start, "source_snapshot": "inputs/GUI/src/multipolepdm",
        "old_evidence_sha256_before": old_start,
        "old_evidence_policy": "Hash-only baseline; no old response/recovery loaded or computed",
        "counts": {"full_grid_response_evaluations": 0, "truth_point_evaluations": 0,
                   "independent_mappings": 0, "old_mappings": 0},
    }
    save_json(directory / "provenance.json", provenance)
    rows = []
    cache = ResponseCache()
    for mode in MODES:
        template = make_job(mode, grid)
        for delta in DELTAS:
            case_id = f"N{len(rows) + 1:02d}"
            p, ratio = production_truth(template, delta)
            provenance["counts"]["truth_point_evaluations"] += 1
            job = observed_job(template, case_id, p, ratio)
            response = cache.get(job)
            result = map_density(job, response)
            provenance["counts"]["independent_mappings"] += 1
            summary = summarize_density(result, (MASS,))
            checks = check_result(result, summary)
            snapshot = directory / "snapshots" / case_id
            if export_result(result, summary, snapshot) != "saved":
                raise RuntimeError(f"Snapshot not fully saved for {case_id}")
            export_slide_npz(directory / f"{case_id}.npz", result, summary)
            row = {
                "schema": SCHEMA, "id": case_id, "case_id": case_id, "mode": mode,
                "label": f"{mode}_{delta:+g}", "status": "ok", "delta_truth": delta,
                "angle_truth_rad": atan(delta), "sigma_truth": TRUTH_SIGMA,
                "sigma_over_i_truth": TRUTH_ALIGNMENT,
                "input": job_to_dict(job), "P_observation": asdict(job.polarization),
                "R_observation": asdict(job.angular_ratio), "ratio_name": job.ratio_name,
                "response_cache_key": response_key(job), "response_metadata": response.metadata,
                "statistics": case_statistics(result, summary, delta),
                "normalization_native": result.normalization, "checks": checks,
                "npz_path": f"{case_id}.npz", "snapshot_path": f"snapshots/{case_id}",
                "warnings": list(result.warnings),
            }
            rows.append(row)
            save_json(directory / "results.json", {"schema": SCHEMA, "injections": rows})
            print(f"{case_id} {mode} delta={delta:+g} P={p:.10g} R={ratio:.10g} "
                  f"branches={row['statistics']['arctan_delta']['hdi_component_count']}", flush=True)
    provenance["counts"]["full_grid_response_evaluations"] = cache.evaluations
    provenance["counts"]["response_cache_hits"] = cache.hits
    provenance["counts"]["exported_v3_snapshots"] = len(rows)
    provenance["old_evidence_sha256_after"] = tree_hashes(OLD_EVIDENCE)
    provenance["old_evidence_unchanged"] = provenance["old_evidence_sha256_after"] == old_start
    provenance["source_stable_during_run"] = all(digest(p) == source_start[str(p.relative_to(ROOT))]
                                                 for p in sources)
    if not provenance["old_evidence_unchanged"] or not provenance["source_stable_during_run"]:
        save_json(directory / "provenance.json", provenance)
        raise RuntimeError("Source or old evidence changed during run; inspect provenance.")
    if (cache.evaluations, cache.hits, len(rows)) != (3, 27, 30):
        raise RuntimeError("Unexpected response/mapping counts.")
    save_json(directory / "aggregate_summary.json", summarize_results(rows))
    validation = verify(directory, check_manifest=False)
    save_json(directory / "validation.json", validation)
    provenance["elapsed_seconds"] = perf_counter() - started
    save_json(directory / "provenance.json", provenance)
    ready = {"status": "ready", "cases": 30, "results": "results.json",
             "schema": SCHEMA, "slide_examples": ["N10.npz", "N20.npz", "N30.npz"],
             "counts": provenance["counts"], "validation": "validation.json",
             "old_evidence_unchanged": True,
             "command": provenance["command"]}
    save_json(directory / "ready.json", ready)
    files = [file_record(p, source="Generated deterministic geometry26 benchmark or exact input snapshot")
             for p in sorted(directory.rglob("*")) if p.is_file() and p != directory / "manifest.json"]
    files.extend(floor["original_files"])
    save_json(directory / "manifest.json", {
        "archive_type": "research-archive-v1", "archive_required": True,
        "retrieved_at": provenance["retrieved_at"], "schema": SCHEMA,
        "source": "Production PDM deterministic geometry26 calculation; local machine results",
        "files": files,
    })
    print(json.dumps(ready, indent=2), flush=True)
    return ready


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("action", choices=("run", "verify", "summary"))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.action == "run":
        run(args.output)
    elif args.action == "verify":
        result = verify(args.output)
        print(json.dumps({"status": result["status"], "cases": result["cases"]}))
    else:
        summary = summarize_results(load_records(args.output))
        summary["large_absolute_delta"].pop("cases")
        print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
