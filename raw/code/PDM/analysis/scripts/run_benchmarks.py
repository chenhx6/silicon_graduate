"""Run the frozen U04 synthetic matrix or reproduce the legacy T12 suite."""

import argparse
from collections import Counter
import csv
from dataclasses import asdict, dataclass, replace
from hashlib import sha256
import json
from math import atan, floor, pi, radians, sqrt, tan
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


MODES = ("P_ADO", "P_DCO", "PDCO")
GENERATORS = ("same_kernel", "independent_9j")
ERROR_P = 0.035
ERROR_RATIO_REL = 0.05
ERROR_RATIO_FLOOR = 0.025


@dataclass(frozen=True)
class Truth:
    mode: str
    delta: float
    sigma_over_i: float

    @property
    def name(self):
        return f"{self.mode}/delta={self.delta:+g}/sigma_over_i={self.sigma_over_i:g}"

    @property
    def xi(self):
        return atan(self.delta)


def configure_imports(project_root):
    gui = project_root / "GUI"
    reference_path = gui / "tests" / "reference" / "angular_correlation.py"
    if not reference_path.is_file() or not (gui / "src" / "multipolepdm").is_dir():
        raise ValueError(
            "Expected GUI/src/multipolepdm and GUI/tests/reference under the project root."
        )
    sys.path[:0] = [str(gui / "src"), str(gui / "tests")]
    return reference_path


def make_job(truth, grid, pure=None):
    """Build fixed scan inputs. The injected truth enters via the point generator."""
    from multipolepdm.contracts import Geometry, JobRequest, Measurement, Transition

    return JobRequest(
        mode=truth.mode,
        target=Transition(3, 2, (pure,) if pure else ("M1", "E2")),
        gate=None if truth.mode == "P_ADO" else Transition(2, 0, ("E2",)),
        polarization=Measurement(0.0, ERROR_P, ERROR_P),
        angular_ratio=Measurement(1.0, ERROR_RATIO_REL, ERROR_RATIO_REL),
        label=truth.name,
        geometry=Geometry(
            theta_a_deg=90,
            theta_b_deg=38,
            relative_phi_deg=18,
            theta_p_deg=81,
            phi_p_deg=13,
            theta_gate_p_deg=47,
            phi_gate_p_deg=61,
        ),
        grid=grid,
    )


def production_point(job, xi, sigma):
    from multipolepdm.models.registry import evaluate_response

    grid = evaluate_response(job, np.asarray([xi]), np.asarray([sigma]))
    if not grid.valid[0, 0]:
        raise ValueError(
            f"Invalid production response for {job.label}, xi={xi}, sigma={sigma}."
        )
    return float(grid.polarization[0, 0]), float(grid.angular_ratio[0, 0])


def independent_point(job, truth):
    from reference import angular_correlation as ref

    target = job.target
    if len(target.multipoles) == 1:
        kind, order = target.multipoles[0]
        first = ref.Transition.pure(
            target.spin_initial, target.spin_final, kind, int(order)
        )
    else:
        first = ref.Transition.mixed(
            target.spin_initial, target.spin_final, truth.delta
        )
    population = ref.gaussian(
        job.reference_spin, truth.sigma_over_i * job.reference_spin
    )
    geom = job.geometry
    polar = radians(geom.theta_p_deg), radians(geom.phi_p_deg)
    detector_a = radians(geom.theta_a_deg), 0.0
    detector_b = radians(geom.theta_b_deg), radians(geom.relative_phi_deg)
    if job.mode == "P_ADO":
        return (
            ref.singles(population, first, polar[0]).polarization,
            ref.singles(population, first, detector_a[0]).total
            / ref.singles(population, first, detector_b[0]).total,
        )
    gate = ref.Transition.pure(job.gate.spin_initial, job.gate.spin_final, "E", 2)
    ratio = ref.dco_ratio(population, first, gate, 1, detector_a, detector_b)
    if job.mode == "P_DCO":
        return ref.singles(population, first, polar[0]).polarization, ratio
    direction_gate = radians(geom.theta_gate_p_deg), radians(geom.phi_gate_p_deg)
    return ref.joint(
        population, first, gate, polar, direction_gate, target=1
    ).polarization, ratio


def observations(job, center, errors, standardized_noise=(0.0, 0.0)):
    from multipolepdm.contracts import Measurement

    measures = [
        Measurement(value + error * float(noise), error, error)
        for value, error, noise in zip(center, errors, standardized_noise)
    ]
    return replace(job, polarization=measures[0], angular_ratio=measures[1])


class GridCache:
    def __init__(self):
        self.responses = {}
        self.builds = []

    def infer(self, job):
        from multipolepdm.jobs.workers import compute_job
        from multipolepdm.pdm.mapping import map_density
        from multipolepdm.pdm.statistics import summarize_density

        key = (
            job.mode,
            job.target,
            job.gate,
            job.target_first,
            job.intermediates,
            job.geometry,
            job.grid,
        )
        if key in self.responses:
            result = map_density(job, self.responses[key])
            return result, summarize_density(result)

        start = perf_counter()
        result, summary = compute_job(job)
        self.responses[key] = result.response
        self.builds.append(
            {
                "mode": job.mode,
                "grid": asdict(job.grid),
                "compute_job_seconds": perf_counter() - start,
            }
        )
        return result, summary


def summary_rows(summary, truth):
    for parameter, marginal, expected in (
        ("delta", summary.delta, truth.delta),
        ("sigma_over_i", summary.sigma_over_i, truth.sigma_over_i),
    ):
        for interval in marginal.intervals:
            for method, components in (("ETI", (interval.eti,)), ("HDI", interval.hdi)):
                yield {
                    "parameter": parameter,
                    "mass": interval.mass,
                    "method": method,
                    "truth": expected,
                    "median": marginal.median,
                    "mode_estimate": marginal.mode,
                    "median_bias": marginal.median - expected,
                    "intervals": components,
                    "truth_included": any(
                        lo <= expected <= hi for lo, hi in components
                    ),
                    "total_width": sum(hi - lo for lo, hi in components),
                    "components": len(components),
                }


def point_record(truth, generator, center, errors, fit):
    result, summary = fit
    return {
        "case": truth.name,
        "mode": truth.mode,
        "generator": generator,
        "delta_truth": truth.delta,
        "xi_truth_rad": truth.xi,
        "sigma_over_i_truth": truth.sigma_over_i,
        "observation": {"P": center[0], result.job.ratio_name: center[1]},
        "standard_errors": {"P": errors[0], result.job.ratio_name: errors[1]},
        "normalization_before_rescaling": result.normalization,
        "warnings": result.warnings,
        "intervals": list(summary_rows(summary, truth)),
    }


def deterministic_suite(grid, cache):
    fit_inputs, records, controls = {}, [], []
    signed = (-10.0, -3.0, -1.0, -0.2, 0.2, 1.0, 3.0, 10.0)
    for mode in MODES:
        cases = [
            Truth(mode, delta, 0.2 if abs(delta) in (0.2, 3.0) else 0.5)
            for delta in signed
        ]
        cases.extend((Truth(mode, 0.0, 0.2), Truth(mode, 0.0, 0.5)))
        for truth in cases:
            job = make_job(truth, grid)
            sigma = truth.sigma_over_i * job.reference_spin
            centers = (
                production_point(job, truth.xi, sigma),
                independent_point(job, truth),
            )
            controls.append(
                {
                    "case": truth.name,
                    "abs_point_differences": list(
                        map(float, np.abs(np.subtract(*centers)))
                    ),
                    "agrees": bool(np.allclose(*centers, atol=1e-10, rtol=1e-8)),
                }
            )
            for generator, center in zip(GENERATORS, centers):
                errors = (
                    ERROR_P,
                    max(ERROR_RATIO_FLOOR, ERROR_RATIO_REL * abs(center[1])),
                )
                fit_job = observations(job, center, errors)
                records.append(
                    point_record(truth, generator, center, errors, cache.infer(fit_job))
                )
                fit_inputs[(truth.name, generator)] = truth, fit_job, center, errors
        print(f"{mode}: {len(cases)} deterministic cases per generator", flush=True)
    return records, fit_inputs, controls


def pure_forward_suite(grid):
    from multipolepdm.jobs.workers import compute_job

    rows = []
    for mode in MODES:
        truth = Truth(mode, 0.0, 0.2)
        mixed = make_job(truth, grid)
        for multipole, angles in (("M1", (0.0,)), ("E2", (-pi / 2, pi / 2))):
            job = make_job(truth, grid, pure=multipole)
            sigma = truth.sigma_over_i * job.reference_spin
            direct = production_point(job, 0.0, sigma)
            independent = independent_point(job, truth)
            endpoints = [production_point(mixed, angle, sigma) for angle in angles]
            try:
                compute_job(job)
            except ValueError as exc:
                if "pure one-component" not in str(exc):
                    raise
                rejection = str(exc)
            else:
                rejection = None
            rows.append(
                {
                    "mode": mode,
                    "multipole": multipole,
                    "sigma_over_i": truth.sigma_over_i,
                    "observables": ["P", job.ratio_name],
                    "production_forward": direct,
                    "independent_forward": independent,
                    "mixed_endpoints": [
                        {"xi_rad": angle, "response": response}
                        for angle, response in zip(angles, endpoints)
                    ],
                    "agrees": all(
                        np.allclose(direct, endpoint, atol=1e-10, rtol=1e-8)
                        for endpoint in (independent, *endpoints)
                    ),
                    "pdf_rejection": rejection,
                }
            )
    return rows


@dataclass
class Accumulator:
    completed: int = 0
    included: int = 0
    signed_bias_sum: float = 0.0
    squared_bias_sum: float = 0.0
    width_sum: float = 0.0
    multicomponent_count: int = 0

    def add(self, row):
        self.completed += 1
        self.included += row["truth_included"]
        self.signed_bias_sum += row["median_bias"]
        self.squared_bias_sum += row["median_bias"] ** 2
        self.width_sum += row["total_width"]
        self.multicomponent_count += row["components"] > 1

    def record(self, parameter, mass, method):
        count = self.completed
        coverage = self.included / count
        return {
            "parameter": parameter,
            "mass": mass,
            "method": method,
            "completed": count,
            "included": self.included,
            "coverage": coverage,
            "coverage_binomial_se": sqrt(coverage * (1 - coverage) / count),
            "mean_median_bias": self.signed_bias_sum / count,
            "median_rmse": sqrt(self.squared_bias_sum / count),
            "mean_total_width": self.width_sum / count,
            "multicomponent_fraction": self.multicomponent_count / count,
        }


def repeated_suite(fit_inputs, cache, draws, seed):
    truths = (
        Truth("P_ADO", -0.2, 0.2),
        Truth("P_DCO", 1.0, 0.5),
        Truth("PDCO", -3.0, 0.2),
    )
    rows = []
    for truth, stream in zip(truths, np.random.SeedSequence(seed).spawn(len(truths))):
        standard_noise = np.random.default_rng(stream).standard_normal((draws, 2))
        for generator in GENERATORS:
            start = perf_counter()
            _, job, center, errors = fit_inputs[(truth.name, generator)]
            statistics, failures = {}, Counter()
            for noise in standard_noise:
                noisy_job = observations(job, center, errors, noise)
                try:
                    _, summary = cache.infer(noisy_job)
                except ValueError as exc:
                    failures[str(exc)] += 1
                    continue
                for row in summary_rows(summary, truth):
                    key = row["parameter"], row["mass"], row["method"]
                    statistics.setdefault(key, Accumulator()).add(row)
            rows.append(
                {
                    "case": truth.name,
                    "mode": truth.mode,
                    "generator": generator,
                    "delta_truth": truth.delta,
                    "xi_truth_rad": truth.xi,
                    "sigma_over_i_truth": truth.sigma_over_i,
                    "observation_center": {"P": center[0], job.ratio_name: center[1]},
                    "standard_errors": {"P": errors[0], job.ratio_name: errors[1]},
                    "seed": seed,
                    "spawn_key": stream.spawn_key,
                    "requested_draws": draws,
                    "completed_draws": draws - sum(failures.values()),
                    "failed_draws": dict(failures),
                    "seconds": perf_counter() - start,
                    "intervals": [
                        value.record(*key) for key, value in statistics.items()
                    ],
                }
            )
            print(
                f"{truth.name} {generator}: {rows[-1]['completed_draws']}/{draws} draws",
                flush=True,
            )
    return rows


def compare_resolutions(coarse, fine):
    for baseline, refined in zip(coarse["intervals"], fine["intervals"]):
        to_grid_units = atan if baseline["parameter"] == "delta" else float
        median_move = abs(
            to_grid_units(baseline["median"]) - to_grid_units(refined["median"])
        )
        same_count = baseline["components"] == refined["components"]
        endpoint_move = (
            max(
                abs(to_grid_units(left) - to_grid_units(right))
                for pair_a, pair_b in zip(baseline["intervals"], refined["intervals"])
                for left, right in zip(pair_a, pair_b)
            )
            if same_count
            else None
        )
        yield {
            "parameter": baseline["parameter"],
            "mass": baseline["mass"],
            "method": baseline["method"],
            "units": "xi_rad" if baseline["parameter"] == "delta" else "sigma/I",
            "median_shift": median_move,
            "max_endpoint_shift": endpoint_move,
            "coarse_components": baseline["components"],
            "fine_components": refined["components"],
            "coarse_intervals": baseline["intervals"],
            "fine_intervals": refined["intervals"],
            "coarse_truth_included": baseline["truth_included"],
            "fine_truth_included": refined["truth_included"],
            "meets_plan_xi_thresholds": (
                same_count and median_move <= 0.0035 and endpoint_move <= 0.0088
                if baseline["parameter"] == "delta"
                else None
            ),
        }


def extended_scan(grid):
    spacing = (grid.xi_max_rad - grid.xi_min_rad) / (grid.xi_points - 1)
    added = floor((pi / 2 - grid.xi_max_rad - 1e-6) / spacing)
    if added <= 0:
        raise ValueError(
            "The refined grid is too coarse for an equal-spacing xi-bound extension."
        )
    return replace(
        grid,
        xi_min_rad=grid.xi_min_rad - added * spacing,
        xi_max_rad=grid.xi_max_rad + added * spacing,
        xi_points=grid.xi_points + 2 * added,
    )


def edge_mass(result, old_grid):
    from scipy.integrate import trapezoid

    xi = result.response.xi_rad
    marginal = trapezoid(result.parameter_density, result.response.sigma, axis=0)
    masses = {}
    for side, start, stop in (
        ("lower", xi[0], old_grid.xi_min_rad),
        ("upper", old_grid.xi_max_rad, xi[-1]),
    ):
        nodes = np.concatenate(([start], xi[(xi > start) & (xi < stop)], [stop]))
        masses[side] = float(trapezoid(np.interp(nodes, xi, marginal), nodes))
    return masses


def compare_bounds(truth, job, center, errors, fine, fine_grid, wider_grid, cache):
    fit = cache.infer(replace(job, grid=wider_grid))
    wider = point_record(truth, fine["generator"], center, errors, fit)
    intervals = []
    for row in compare_resolutions(fine, wider):
        if row["parameter"] != "delta":
            continue
        row.pop("meets_plan_xi_thresholds")
        row["baseline_intervals_xi_rad"] = [
            [atan(lo), atan(hi)] for lo, hi in row["coarse_intervals"]
        ]
        row["expanded_intervals_xi_rad"] = [
            [atan(lo), atan(hi)] for lo, hi in row["fine_intervals"]
        ]
        intervals.append(row)
    return {
        "case": truth.name,
        "mode": truth.mode,
        "generator": fine["generator"],
        "delta_truth": truth.delta,
        "sigma_over_i_truth": truth.sigma_over_i,
        "xi_truth_rad": truth.xi,
        "xi_bounds_rad": [wider_grid.xi_min_rad, wider_grid.xi_max_rad],
        "delta_bounds": [tan(wider_grid.xi_min_rad), tan(wider_grid.xi_max_rad)],
        "mass_outside_baseline_scan": edge_mass(fit[0], fine_grid),
        "expanded_warnings": wider["warnings"],
        "intervals": intervals,
    }


def convergence_suite(grid, records, fit_inputs, cache, check_bounds):
    fine_grid = replace(
        grid, xi_points=2 * grid.xi_points - 1, sigma_points=2 * grid.sigma_points - 1
    )
    wider_grid = extended_scan(fine_grid) if check_bounds else None
    comparisons, bound_checks = [], []
    for mode in MODES:
        independent = [
            record
            for record in records
            if record["mode"] == mode and record["generator"] == "independent_9j"
        ]
        large_delta = [
            record for record in independent if abs(record["delta_truth"]) == 10
        ]
        interior = max(
            (record for record in independent if abs(record["delta_truth"]) < 10),
            key=lambda record: (
                max(row["components"] for row in record["intervals"]),
                abs(atan(record["intervals"][0]["median"]) - record["xi_truth_rad"]),
            ),
        )
        for coarse in (*large_delta, interior):
            truth, job, center, errors = fit_inputs[
                (coarse["case"], coarse["generator"])
            ]
            fine = point_record(
                truth,
                coarse["generator"],
                center,
                errors,
                cache.infer(replace(job, grid=fine_grid)),
            )
            comparisons.append(
                {
                    "case": truth.name,
                    "mode": mode,
                    "generator": coarse["generator"],
                    "delta_truth": truth.delta,
                    "sigma_over_i_truth": truth.sigma_over_i,
                    "fine_warnings": fine["warnings"],
                    "intervals": list(compare_resolutions(coarse, fine)),
                }
            )
            if wider_grid is not None and abs(truth.delta) == 10:
                bound_checks.append(
                    compare_bounds(
                        truth, job, center, errors, fine, fine_grid, wider_grid, cache
                    )
                )
    return fine_grid, wider_grid, comparisons, bound_checks


def write_evidence(output, evidence):
    output.mkdir(parents=True, exist_ok=True)
    (output / "synthetic_benchmarks.json").write_text(
        json.dumps(evidence, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    identity_fields = ("case", "mode", "generator", "delta_truth", "sigma_over_i_truth")
    fields = (
        "kind",
        *identity_fields,
        "parameter",
        "mass",
        "method",
        "median",
        "median_bias",
        "truth_included",
        "total_width",
        "components",
        "intervals",
        "completed",
        "included",
        "coverage",
        "coverage_binomial_se",
        "mean_median_bias",
        "median_rmse",
        "mean_total_width",
        "multicomponent_fraction",
        "median_shift",
        "max_endpoint_shift",
        "coarse_components",
        "fine_components",
        "coarse_truth_included",
        "fine_truth_included",
        "meets_plan_xi_thresholds",
        "baseline_intervals_xi_rad",
        "expanded_intervals_xi_rad",
        "multipole",
        "production_forward",
        "independent_forward",
        "agrees",
        "pdf_rejection",
    )
    with (output / "synthetic_benchmarks.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for kind in (
            "deterministic",
            "repeated",
            "convergence",
            "xi_bound_sensitivity",
        ):
            for record in evidence[kind]:
                identity = {field: record[field] for field in identity_fields}
                for row in record["intervals"]:
                    writer.writerow({"kind": kind, **identity, **row})
        for record in evidence["pure_forward"]:
            writer.writerow(
                {
                    "kind": "pure_forward",
                    "sigma_over_i_truth": record["sigma_over_i"],
                    **record,
                }
            )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--suite", choices=("synthetic", "legacy-synthetic"), default="synthetic"
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--project-root", type=Path, default=Path(__file__).resolve().parents[2]
    )
    parser.add_argument("--seed", type=int, default=20261120)
    parser.add_argument(
        "--draws", type=int, default=100, help="Noisy draws per case and generator."
    )
    parser.add_argument("--xi-points", type=int, default=3121)
    parser.add_argument("--sigma-points", type=int, default=201)
    parser.add_argument(
        "--check-xi-bounds",
        action="store_true",
        help="Extend the fine grid toward both pure limits for large-mixing and endpoint cases.",
    )
    args = parser.parse_args()
    if args.draws < 1 or args.seed < 0 or min(args.xi_points, args.sigma_points) < 3:
        parser.error(
            "Require draws >= 1, seed >= 0, and at least three points per axis."
        )
    reference_path = configure_imports(args.project_root.resolve())
    if args.suite == "synthetic":
        if any(
            getattr(args, name) != parser.get_default(name)
            for name in ("seed", "draws", "xi_points", "sigma_points")
        ):
            parser.error("The U04 suite is frozen. Seed, draw, and point-count overrides apply only to legacy-synthetic.")
        from benchmark_u04 import run

        return run(args.project_root.resolve(), args.output.resolve(), args.check_xi_bounds)
    from multipolepdm.contracts import GridSpec

    start = perf_counter()
    grid = GridSpec(
        xi_points=args.xi_points,
        sigma_points=args.sigma_points,
        sigma_min=0.15,
        sigma_max=3.0,
    )
    core_paths = ("pdm/mapping.py", "pdm/statistics.py", "jobs/workers.py")
    package_path = reference_path.parents[2] / "src" / "multipolepdm"
    core_hashes = {
        name: sha256((package_path / name).read_bytes()).hexdigest()
        for name in core_paths
    }
    cache = GridCache()
    deterministic, fit_inputs, point_controls = deterministic_suite(grid, cache)
    pure = pure_forward_suite(grid)
    fine_grid, wider_grid, convergence, bound_checks = convergence_suite(
        grid, deterministic, fit_inputs, cache, args.check_xi_bounds
    )
    repeated = repeated_suite(fit_inputs, cache, args.draws, args.seed)
    evidence = {
        "suite": args.suite,
        "elapsed_seconds_before_writing": perf_counter() - start,
        "settings": {
            "numpy": np.__version__,
            "python": sys.version.split()[0],
            "reference_sha256": sha256(reference_path.read_bytes()).hexdigest(),
            "core_sha256_at_start": core_hashes,
            "core_unchanged_on_disk_through_run": all(
                sha256((package_path / name).read_bytes()).hexdigest() == digest
                for name, digest in core_hashes.items()
            ),
            "grid": asdict(grid),
            "doubled_grid": asdict(fine_grid),
            "seed": args.seed,
            "production_default_grid": asdict(GridSpec()),
            "expanded_xi_grid": asdict(wider_grid) if wider_grid is not None else None,
            "draws_per_case_and_generator": args.draws,
            "target_spins": [3, 2],
            "DCO_gate_spins": [2, 0],
            "DCO_gate_multipole": "E2",
            "geometry": asdict(make_job(Truth("PDCO", 0.0, 0.2), grid).geometry),
            "error_model": {
                "distribution": "Independent untruncated normal draws, fixed symmetric errors",
                "P_sd": ERROR_P,
                "ratio_sd_relative": ERROR_RATIO_REL,
                "ratio_sd_floor": ERROR_RATIO_FLOOR,
                "streams": "SeedSequence.spawn by truth case; shared standard draws across generators",
            },
            "coverage": "Marginal truth inclusion among completed fits, with plug-in binomial SE.",
            "response_cache": "compute_job builds each mixed mode/resolution; subsequent fits map and summarize the cached ResponseGrid.",
            "convergence_selection": "Both delta=+/-10 and one interior case per mode, chosen by the most interval components then largest absolute xi median bias.",
        },
        "response_grid_builds": cache.builds,
        "point_parity": point_controls,
        "pure_forward": pure,
        "deterministic": deterministic,
        "repeated": repeated,
        "convergence": convergence,
        "xi_bound_sensitivity": bound_checks,
    }
    write_evidence(args.output, evidence)
    print(
        f"Synthetic suite finished in {perf_counter() - start:.2f} s. Evidence in {args.output}.",
        flush=True,
    )
    failed = (
        not all(row["agrees"] for row in point_controls)
        or not all(row["agrees"] and row["pdf_rejection"] for row in pure)
        or any(row["completed_draws"] != args.draws for row in repeated)
    )
    needs_refinement = any(
        interval.get("meets_plan_xi_thresholds") is False
        for case in convergence
        for interval in case["intervals"]
    )
    return 1 if failed else (2 if needs_refinement else 0)


if __name__ == "__main__":
    raise SystemExit(main())
