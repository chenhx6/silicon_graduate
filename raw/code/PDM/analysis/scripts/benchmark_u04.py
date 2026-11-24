"""Frozen 0.1.1 injection, repeat coverage, and pure-boundary evidence."""

from dataclasses import asdict, dataclass, replace
from hashlib import sha256
from importlib.metadata import version
from itertools import product
import csv
import json
import logging
from math import atan, fsum, pi, radians
from pathlib import Path
import shlex
import sys
from time import perf_counter

import numpy as np
from scipy.integrate import trapezoid
from scipy.stats import binomtest

from multipolepdm import __version__
from multipolepdm.contracts import Geometry, GridSpec, JobRequest, Measurement, Transition
from multipolepdm.models.registry import evaluate_response
from multipolepdm.pdm.mapping import map_density
from multipolepdm.pdm.statistics import summarize_density
from multipolepdm.physics.detectors import DetectorDirection, DetectorGroup
from reference import angular_correlation as ref


MODES = ("P_ADO", "P_DCO", "PDCO")
GENERATORS = ("independent_9j", "same_kernel")
REPEATS = {"P_ADO": -0.1, "P_DCO": 1.0, "PDCO": -10.0}
DELTAS = (-10, -5, -1, -0.5, -0.1, 0.1, 0.5, 1, 5, 10)
SEED = 20261120
DRAWS = 100
MASS = 0.68
TRUTH_ALIGNMENT = 0.3
ANGLE_STEP = radians(0.1)
ALIGNMENT_STEP = 0.005
P_ERROR_FLOOR = 0.1075
P_ERROR_FRACTION = 0.8
R_ERROR_FRACTION = 0.1
AZIMUTH_NODES = 16
NOMINAL_SCAN_DEG = (-89.9, 89.9)
EXPANDED_SCAN_DEG = (-89.99, 89.99)
SOURCE = Path("raw/writing/pado/20261029_review_v1/PDM/main.tex")
PLAN = Path("outputs/plans/20261120-pdm-three-mode-rewrite/plan.md")
POLICY = Path("tmp/pdm-upgrade-011/frozen-policy.json")
EVIDENCE_DIR = "sigma03_relP80_relR10"
LOG = logging.getLogger(__name__)


@dataclass(frozen=True)
class Case:
    mode: str
    delta: float | None

    @property
    def key(self):
        mixing = "pure_E2" if self.delta is None else f"{self.delta:+g}"
        return f"{self.mode}_{mixing}"

    @property
    def xi(self):
        return None if self.delta is None else atan(self.delta)


def detector_group(theta):
    return DetectorGroup((DetectorDirection(theta),), normalization="mean")


def make_job(mode, grid, *, pure=False):
    return JobRequest(
        mode=mode,
        target=Transition(5, 4, ("E2",) if pure else ("M1", "E2")),
        gate=None if mode == "P_ADO" else Transition(4, 2, ("E2",)),
        target_first=True,
        polarization=Measurement(0.0, P_ERROR_FLOOR, P_ERROR_FLOOR),
        angular_ratio=Measurement(1.0, R_ERROR_FRACTION, R_ERROR_FRACTION),
        geometry=Geometry(
            theta_a_deg=125,
            theta_b_deg=90,
            theta_p_deg=90,
            theta_gate_p_deg=125,
            ratio_group_a=detector_group(125),
            ratio_group_b=detector_group(90),
            polarization_group=detector_group(90),
            polarization_gate_group=detector_group(125) if mode == "PDCO" else None,
            select_azimuth=False,
        ),
        grid=grid,
    )


def grid_spec(refinement=1, *, expanded=False):
    bounds = EXPANDED_SCAN_DEG if expanded else NOMINAL_SCAN_DEG
    lower, upper = map(float, np.deg2rad(bounds))
    return GridSpec(
        xi_min_rad=lower,
        xi_max_rad=upper,
        xi_step_rad=ANGLE_STEP / refinement,
        xi_input_unit="deg",
        sigma_min=0.15,
        sigma_max=5.0,
        sigma_step=5 * ALIGNMENT_STEP / refinement,
        sigma_input_unit="sigma/I",
    )


def independent_point(job, case, *, azimuth_nodes=AZIMUTH_NODES):
    """Evaluate the separate 9j expansion with azimuth sums before division."""
    first = (
        ref.Transition.pure(5, 4, "E", 2)
        if case.delta is None
        else ref.Transition.mixed(5, 4, case.delta)
    )
    population = ref.gaussian(5, TRUTH_ALIGNMENT * 5)
    geometry = job.geometry
    theta_a, theta_b, theta_p = map(
        radians, (geometry.theta_a_deg, geometry.theta_b_deg, geometry.theta_p_deg)
    )

    def singles(theta):
        return ref.singles(population, first, theta)

    if job.mode == "P_ADO":
        return singles(theta_p).polarization, singles(theta_a).total / singles(theta_b).total

    gate = ref.Transition.pure(4, 2, "E", 2)
    azimuths = np.arange(azimuth_nodes) * (2 * pi / azimuth_nodes)

    def joint(target_theta, gate_theta, analyzer=None):
        return [
            ref.joint(
                population, first, gate, (target_theta, 0), (gate_theta, phi),
                target=analyzer,
            )
            for phi in azimuths
        ]

    ratio = fsum(joint(theta_a, theta_b)) / fsum(joint(theta_b, theta_a))
    if job.mode == "P_DCO":
        return singles(theta_p).polarization, ratio

    channels = joint(theta_p, radians(geometry.theta_gate_p_deg), analyzer=1)
    intensity = ref.LinearIntensity(
        fsum(row.parallel for row in channels),
        fsum(row.perpendicular for row in channels),
    )
    return intensity.polarization, ratio


def production_point(job, case):
    if case.delta is None:
        job = replace(job, target=Transition(5, 4, ("E2",)))
    xi = 0.0 if case.xi is None else case.xi
    response = evaluate_response(
        job, np.array([xi]), np.array([job.reference_spin * TRUTH_ALIGNMENT])
    )
    if not response.valid[0, 0]:
        raise ValueError(f"Undefined production response for {case.key}.")
    return float(response.polarization[0, 0]), float(response.angular_ratio[0, 0])


def errors_at(center):
    return max(P_ERROR_FLOOR, P_ERROR_FRACTION * abs(center[0])), R_ERROR_FRACTION * abs(center[1])


def interval_mass(marginal, lower, upper):
    if lower == upper:
        return 0.0
    axis, density = marginal.coordinate, marginal.density
    interior = axis[(axis > lower) & (axis < upper)]
    sample = np.concatenate(([lower], interior, [upper]))
    return float(trapezoid(np.interp(sample, axis, density), sample))


def marginal_record(marginal, truth, *, derived=False):
    (interval,) = marginal.intervals
    if interval.mass != MASS:
        raise ValueError(f"Expected only the exact {MASS} interval.")
    low, high = interval.eti
    record = {
        "coordinate": marginal.coordinate_name,
        "evaluation_coordinate": marginal.evaluation_coordinate,
        "q16": low,
        "q50": marginal.median,
        "q84": high,
        "mode": marginal.mode,
        "mean": marginal.mean,
        "std": marginal.std,
        "mean_bounds": marginal.mean_bounds,
        "mean_bound_flags": marginal.mean_bound_flags,
        "hdi_segments": [asdict(segment) for segment in interval.hdi_segments],
        "hdi_component_count": len(interval.hdi_segments),
        "hdi_mass": fsum(segment.mass for segment in interval.hdi_segments),
        "hdi_threshold_evaluation_coordinate": interval.hdi_threshold,
        "density_area": float(trapezoid(marginal.density, marginal.coordinate)),
    }
    if truth is not None:
        record.update(
            q50_minus_truth=marginal.median - truth,
            eti_contains_truth=bool(low <= truth <= high),
            hdi_contains_truth=any(left <= truth <= right for left, right in interval.hdi),
        )
    if not derived:
        left = float(marginal.coordinate[0])
        record["cdf_at_reported_quantiles"] = [
            interval_mass(marginal, left, point) for point in (low, marginal.median, high)
        ]
        record["hdi_integrated_mass"] = fsum(
            interval_mass(marginal, left, right) for left, right in interval.hdi
        )
    return record


def grid_record(response, spec):
    return {
        **asdict(spec),
        "shape_sigma_by_xi": list(response.valid.shape),
        "xi_bounds_rad": [float(response.xi_rad[0]), float(response.xi_rad[-1])],
        "xi_bounds_deg": [float(value) for value in np.rad2deg(response.xi_rad[[0, -1]])],
        "sigma_bounds": [float(response.sigma[0]), float(response.sigma[-1])],
        "sigma_over_i_bounds": [
            float(response.sigma[0] / response.reference_spin),
            float(response.sigma[-1] / response.reference_spin),
        ],
        "invalid_response_points": int(np.count_nonzero(~response.valid)),
    }


def fit(case, generator, job, response, center, *, noise=(0.0, 0.0)):
    errors = errors_at(center)
    measurements = [
        Measurement(value + error * float(deviate), error, error)
        for value, error, deviate in zip(center, errors, noise)
    ]
    record = {
        "case_id": case.key,
        "mode": case.mode,
        "generator": generator,
        "target_spin_initial": job.target.spin_initial,
        "target_spin_final": job.target.spin_final,
        "target_fit_multipoles": job.target.multipoles,
        "gate": None if job.gate is None else asdict(job.gate),
        "target_first": job.target_first,
        "geometry": asdict(job.geometry),
        "ratio_name": job.ratio_name,
        "I_reference": job.reference_spin,
        "delta0": case.delta,
        "arctan_delta0": case.xi,
        "equivalent_pure_E2_endpoint_angles_rad": [-pi / 2, pi / 2] if case.delta is None else None,
        "sigma_over_i_truth": TRUTH_ALIGNMENT,
        "sigma_truth": job.reference_spin * TRUTH_ALIGNMENT,
        "P0": center[0],
        "R0": center[1],
        "P_observation": asdict(measurements[0]),
        "R_observation": asdict(measurements[1]),
        "standard_normal_noise_P_R": tuple(map(float, noise)),
        "interval_mass": MASS,
        "grid": grid_record(response, job.grid),
        "observation_outside_P_R_physical_response_domain": (
            abs(measurements[0].value) > 1 or measurements[1].value < 0
        ),
        "warnings": [],
    }
    try:
        result = map_density(
            replace(job, polarization=measurements[0], angular_ratio=measurements[1]),
            response,
        )
        record["warnings"] = list(result.warnings)
        summary = summarize_density(result, masses=(MASS,))
        angle = marginal_record(summary.arctan_delta, case.xi)
        alignment = marginal_record(summary.sigma_over_i, TRUTH_ALIGNMENT)
        delta_report = marginal_record(summary.delta, case.delta, derived=True)
        joint_area = float(trapezoid(
            trapezoid(result.parameter_density, response.xi_rad, axis=1), response.sigma
        ))
        numerical_checks = {
            "joint_area": joint_area,
            "area_pass": all(
                abs(area - 1) <= 1e-6
                for area in (joint_area, angle["density_area"], alignment["density_area"], delta_report["density_area"])
            ),
            "HDI_mass_pass": all(
                abs(row[key] - MASS) <= 1e-6
                for row in (angle, alignment)
                for key in ("hdi_mass", "hdi_integrated_mass")
            ),
            "CDF_quantiles_pass": all(
                abs(actual - expected) <= 1e-6
                for row in (angle, alignment)
                for actual, expected in zip(row["cdf_at_reported_quantiles"], (0.16, 0.5, 0.84))
            ),
        }
        passed = all(value for key, value in numerical_checks.items() if key.endswith("_pass"))
        record.update(
            status="ok" if passed else "numerical_check_failed",
            normalizing_integral=result.normalization,
            numerical_checks=numerical_checks,
            arctan_delta=angle,
            delta=delta_report,
            sigma_over_i=alignment,
        )
        if case.delta is None:
            marginal = summary.arctan_delta
            left, right = marginal.coordinate[[0, -1]]
            lower_limit = -pi / 2 + radians(5)
            upper_limit = pi / 2 - radians(5)
            record["pure_endpoint_mass"] = {
                "window_from_each_physical_endpoint_deg": 5.0,
                "negative_edge": interval_mass(marginal, left, lower_limit),
                "positive_edge": interval_mass(marginal, upper_limit, right),
            }
        return record, summary
    except (ValueError, ArithmeticError) as error:
        record.update(status="failed", error=f"{type(error).__name__}: {error}")
        return record, None


def compare(coarse, fine):
    if any(row["status"] == "failed" for row in (coarse, fine)):
        return {"status": "fit_failed"}
    before, after = (row["arctan_delta"] for row in (coarse, fine))
    center = abs(before["q50"] - after["q50"])
    eti = [abs(before[key] - after[key]) for key in ("q16", "q84")]
    old_segments, new_segments = (row["hdi_segments"] for row in (before, after))
    hdi = None
    if len(old_segments) == len(new_segments):
        hdi = [
            [abs(old - new) for old, new in zip(left["bounds"], right["bounds"])]
            for left, right in zip(old_segments, new_segments)
        ]
    return {
        "angle_q50_change_rad": center,
        "angle_ETI_endpoint_changes_rad": eti,
        "angle_HDI_endpoint_changes_rad": hdi,
        "old_new_HDI_component_counts": [len(old_segments), len(new_segments)],
        "meets_plan_xi_thresholds": (
            center <= 0.0035 and max(eti) <= 0.0088 and hdi is not None
            and all(max(offsets) <= 0.0088 for offsets in hdi)
        ),
    }


def coverage(rows):
    successful = [row for row in rows if row["status"] == "ok"]
    scores = {}
    for parameter, interval in product(("arctan_delta", "sigma_over_i"), ("eti", "hdi")):
        count = sum(row[parameter][f"{interval}_contains_truth"] for row in successful)
        valid = len(successful)
        confidence = binomtest(count, valid).proportion_ci(MASS) if valid else None
        scores[f"{parameter}_{interval}"] = {
            "covered": count,
            "valid_fits": valid,
            "attempts": len(rows),
            "fraction_of_valid_fits": count / valid if valid else None,
            "binomial_interval": None if confidence is None else [confidence.low, confidence.high],
            "binomial_confidence_level": MASS,
            "binomial_method": "exact Clopper-Pearson",
        }
    return scores


def save_json(path, payload):
    path.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def save_csv(path, rows):
    rows = list(rows)
    fields = list(dict.fromkeys(key for row in rows for key in row))
    with path.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({
                key: json.dumps(value, allow_nan=False) if isinstance(value, (dict, list, tuple)) else value
                for key, value in row.items()
            })


def flat_record(record):
    flat = {key: val for key, val in record.items() if key not in ("arctan_delta", "delta", "sigma_over_i")}
    for name in ("P_observation", "R_observation", "numerical_checks", "pure_endpoint_mass"):
        for key, value in flat.pop(name, {}).items():
            flat[f"{name}_{key}"] = value
    for parameter in ("arctan_delta", "delta", "sigma_over_i"):
        for key, value in record.get(parameter, {}).items():
            flat[f"{parameter}_{key}"] = value
    return flat


def file_hashes(repo, paths):
    return {path.relative_to(repo).as_posix(): sha256(path.read_bytes()).hexdigest() for path in paths}


def freeze(project, output, check_bounds):
    repo = project.parents[2]
    source_path = repo / POLICY
    archive_path = project / "analysis" / "benchmarks" / EVIDENCE_DIR / "frozen-policy.json"
    if not source_path.is_file():
        source_path = archive_path
    policy_bytes = source_path.read_bytes()
    policy = json.loads(policy_bytes)
    expected = {
        "delta": list(DELTAS), "sigma_over_i": TRUTH_ALIGNMENT, "scan_sigma": True,
        "p_error": "max(0.1075,0.8*abs(P))", "r_error": "0.1*abs(R)",
        "geometry": {
            "target": "5->4 M1/E2", "gate": "4->2 E2", "ratio_theta_deg": [125, 90],
            "P_theta_deg": 90, "P_gate_theta_deg": 125, "select_azimuth": False,
        },
    }
    if any(policy["injection"].get(key) != value for key, value in expected.items()):
        raise ValueError("U04 constants differ from the frozen injection policy.")
    if (
        policy["conventions"]["HDI_ETI_mass"] != MASS
        or policy["grid"]["angle_step_deg"] != 0.1
        or policy["grid"]["sigma_over_i_step"] != ALIGNMENT_STEP
        or (policy["grid"]["angle_min_deg"], policy["grid"]["angle_max_deg"]) != NOMINAL_SCAN_DEG
    ):
        raise ValueError("U04 constants differ from the frozen grid or interval policy.")

    primary = grid_spec()
    frozen = {
        "policy_sha256": sha256(policy_bytes).hexdigest(),
        "source_locator": f"{SOURCE.as_posix()}#eq:e2-analytic-test",
        "plan_locator": f"{PLAN.as_posix()}#section-6-and-U04",
        "response_jobs_by_mode": {mode: asdict(make_job(mode, primary)) for mode in MODES},
        "job_measurements": "Response-only placeholders are replaced by each case's generated observations before inversion.",
        "injection": expected,
        "generator_identity": {
            "independent_9j": "Independent Droste angular-momentum expansion; production inversion.",
            "same_kernel": "Production response for generation and inversion; self-consistency.",
        },
        "generator_independent_azimuth_nodes": AZIMUTH_NODES,
        "angle_bounds_deg": NOMINAL_SCAN_DEG,
        "angle_expansion_bounds_deg": EXPANDED_SCAN_DEG if check_bounds else None,
        "sigma_over_i_bounds": [primary.sigma_min / 5, primary.sigma_max / 5],
        "grid_refinement": asdict(grid_spec(2)),
        "grid_expansion": asdict(grid_spec(2, expanded=True)) if check_bounds else None,
        "repeat_noise": {
            "cases": REPEATS, "draws_per_case": DRAWS, "seed": SEED,
            "generator": "numpy.default_rng (PCG64), independent standard-normal P and R",
            "shared_between_input_generators": True,
        },
        "interval_mass": MASS,
        "observation_errors": policy["observation_density"]["input_errors"],
    }
    output.mkdir(parents=True, exist_ok=True)
    for name, data in (
        ("frozen-policy.json", policy_bytes),
        ("frozen-job.json", (json.dumps(frozen, indent=2) + "\n").encode()),
    ):
        destination = output / name
        if destination.exists() and destination.read_bytes() != data:
            raise ValueError(f"Frozen artifact differs at {destination}. Use a new output directory.")
        destination.write_bytes(data)
    return repo


def run(project, output, check_bounds):
    legacy_dirs = {project / "analysis" / "benchmarks", project / "analysis"}
    if output in legacy_dirs or (output / "synthetic_benchmarks.json").exists():
        raise ValueError(f"Use a dedicated U04 output directory such as benchmarks/{EVIDENCE_DIR}.")
    repo = freeze(project, output, check_bounds)
    package = project / "GUI" / "src" / "multipolepdm"
    inputs = sorted(
        list(package.glob("*.py"))
        + [
            path for module in ("config", "models", "pdm", "physics")
            for path in (package / module).rglob("*.py")
        ]
        + list((project / "GUI" / "tests" / "reference").glob("*.py"))
        + [project / "GUI" / "tests" / "test_pure_calibration_v011.py"]
        + [Path(__file__).with_name(name).resolve() for name in (
            "benchmark_u04.py", "plot_benchmark_u04.py", "run_benchmarks.py"
        )]
    )
    start_hashes = file_hashes(repo, inputs)
    reference_documents = [path for path in (repo / SOURCE, repo / PLAN) if path.is_file()]
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.FileHandler(output / "run.log", mode="w", encoding="utf-8"), logging.StreamHandler()],
    )
    command = shlex.join([sys.executable, *sys.argv])
    LOG.info("Command from %s: %s", Path.cwd(), command)
    LOG.info("Frozen job SHA-256 %s", sha256((output / "frozen-job.json").read_bytes()).hexdigest())
    provenance = {
        "command": command, "working_directory": str(Path.cwd()),
        "source_version": __version__,
        "python": sys.version, "dependencies": {name: version(name) for name in ("numpy", "scipy", "sympy")},
        "source_sha256": start_hashes, "source_stable_during_run": None,
        "reference_documents_sha256_at_start": file_hashes(repo, reference_documents),
    }
    save_json(output / "provenance.json", provenance)

    started = perf_counter()
    main, repeats, repeated_summary, sensitivity, controls = [], [], [], [], []
    curves = {}
    random = np.random.default_rng(SEED)
    for mode in MODES:
        job = make_job(mode, grid_spec())
        base_response = evaluate_response(job)
        cases = [Case(mode, delta) for delta in DELTAS]
        pure = Case(mode, None)
        centers = {}
        base_rows = {}
        for case in (*cases, pure):
            center_ref = independent_point(job, case)
            center_prod = production_point(job, case)
            controls.append({
                "case_id": case.key, "independent_9j": center_ref, "same_kernel": center_prod,
                "abs_difference_P_R": [abs(left - right) for left, right in zip(center_ref, center_prod)],
                "agrees": bool(np.allclose(center_ref, center_prod, rtol=5e-11, atol=5e-12)),
            })
            for generator, center in zip(GENERATORS, (center_ref, center_prod)):
                key = case.key, generator
                centers[key] = center
                row, summary = fit(case, generator, job, base_response, center)
                base_rows[key] = row
                if case.delta is not None:
                    main.append(row)
                if summary is not None:
                    curves[f"{case.key}__{generator}"] = np.stack(
                        (summary.arctan_delta.coordinate, summary.arctan_delta.density)
                    )
        LOG.info("%s deterministic fits complete", mode)
        repeat_case = Case(mode, REPEATS[mode])
        noise = random.standard_normal((DRAWS, 2))
        for generator in GENERATORS:
            center = centers[(repeat_case.key, generator)]
            matched_rows = []
            for index, vector in enumerate(noise):
                row, _ = fit(repeat_case, generator, job, base_response, center, noise=vector)
                row["draw_index"] = index
                matched_rows.append(row)
            repeats.extend(matched_rows)
            repeated_summary.append({
                "case_id": repeat_case.key, "generator": generator,
                "failed_or_numerical_check_failed": sum(row["status"] != "ok" for row in matched_rows),
                "observation_outside_P_R_physical_response_domain": sum(
                    row["observation_outside_P_R_physical_response_domain"]
                    for row in matched_rows
                ),
                "coverage": coverage(matched_rows),
            })
        LOG.info("%s repeated fits complete (%d draws x %d generators)", mode, DRAWS, len(GENERATORS))

        del base_response
        edge_cases = (cases[0], cases[-1], pure)
        fine_job = replace(job, grid=grid_spec(2))
        fine_response = evaluate_response(fine_job)
        fine = {
            (case.key, generator): fit(
                case, generator, fine_job, fine_response, centers[(case.key, generator)]
            )[0]
            for case, generator in product(edge_cases, GENERATORS)
        }
        del fine_response
        wider = {}
        if check_bounds:
            wide_job = replace(job, grid=grid_spec(2, expanded=True))
            wide_response = evaluate_response(wide_job)
            wider = {
                (case.key, generator): fit(
                    case, generator, wide_job, wide_response, centers[(case.key, generator)]
                )[0]
                for case, generator in product(edge_cases, GENERATORS)
            }
            del wide_response
        for key, row in fine.items():
            comparison = {
                "base": base_rows[key], "refined": row,
                "refinement": compare(base_rows[key], row),
            }
            if key in wider:
                comparison.update(expanded=wider[key], expansion=compare(row, wider[key]))
            sensitivity.append(comparison)
        LOG.info("%s refined and finite-domain fits complete", mode)

    provenance["source_stable_during_run"] = file_hashes(repo, inputs) == start_hashes
    provenance["reference_documents_sha256_at_finish"] = file_hashes(repo, reference_documents)
    provenance["elapsed_seconds"] = perf_counter() - started
    save_json(output / "provenance.json", provenance)
    save_json(output / "deterministic.json", main)
    save_csv(output / "deterministic.csv", map(flat_record, main))
    save_json(output / "generator_agreement.json", controls)
    save_csv(output / "repeated_draws.csv", map(flat_record, repeats))
    save_json(output / "repeated_coverage.json", repeated_summary)
    save_json(output / "grid_and_endpoint_sensitivity.json", sensitivity)
    save_csv(
        output / "grid_and_endpoint_sensitivity.csv",
        (
            {"resolution": resolution, **flat_record(item[resolution])}
            for item in sensitivity for resolution in ("base", "refined", "expanded")
            if resolution in item
        ),
    )
    np.savez_compressed(output / "angle_marginals.npz", **curves)
    from plot_benchmark_u04 import save_figures

    save_figures(output, main, repeated_summary, curves)
    fitted = main + repeats + [
        item[key] for item in sensitivity for key in ("base", "refined", "expanded") if key in item
    ]
    failures = sum(row["status"] != "ok" for row in fitted)
    refinement_flags = sum(not item["refinement"].get("meets_plan_xi_thresholds", False) for item in sensitivity)
    LOG.info(
        "Saved %d deterministic fits, %d repeated fits, %d sensitivity comparisons; "
        "%d unsuccessful fit records, %d refinement threshold flags, %.1f seconds",
        len(main), len(repeats), len(sensitivity), failures, refinement_flags, provenance["elapsed_seconds"],
    )
    if not provenance["source_stable_during_run"]:
        LOG.error("Source hashes changed between start and finish.")
    if failures or not all(row["agrees"] for row in controls) or not provenance["source_stable_during_run"]:
        return 1
    return 2 if refinement_flags else 0
