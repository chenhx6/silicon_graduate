#!/usr/bin/env python3
"""Reproduce the ASYM PDF and fixed-response sensitivity study from the Wiki."""

import argparse
import csv
from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys
from unittest.mock import patch

sys.dont_write_bytecode = True

import numpy as np
import scipy
from scipy.integrate import quad, trapezoid
from scipy.optimize import minimize
from scipy.stats import norm, skewnorm

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PDM = ROOT / "raw/code/PDM"
ARCHIVE = ROOT / "raw/writing/pado/Upload"
CASES = PDM / "analysis/cases"
SOURCE = ROOT / "raw/papers/2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf"
sys.path[:0] = [str(PDM / "GUI/src"), str(ARCHIVE)]

from multipolepdm.contracts import Measurement
from multipolepdm.io.input import job_from_dict
from multipolepdm.models.registry import evaluate_response
from multipolepdm.pdm.mapping import map_density
from multipolepdm.pdm.observations import _log_measurement_density
from multipolepdm.pdm.statistics import _summarize
from p_ado.config import PdfConfig
from p_ado.pdf import fitters
from p_ado.pdf.evaluators import build_pdf_evaluator

CONFIG = PdfConfig()
EXACT = np.array([0.16, 0.50, 0.84])
ONE_SIGMA = norm.cdf([-1.0, 0.0, 1.0])
PROBS = {"exact_16_50_84": EXACT, "normal_one_sigma": ONE_SIGMA}
STARTS = [0, -1, 1, -5, 5, -12, 12, -30, 30]
ACCEPTANCE_AWARE_LIMIT = 14.5
ACCEPTANCE_AWARE_NAME = "legacy_acceptance_aware"


@dataclass
class Density:
    pdf: object
    cdf: object
    ppf: object
    support: tuple
    semantics: str


def two_scales(center, left, right, median_centered):
    left_mass = 0.5 if median_centered else left / (left + right)

    def cdf(x):
        offset = np.asarray(x) - center
        return np.where(
            offset < 0,
            2 * left_mass * norm.cdf(offset / left),
            left_mass + (1 - left_mass) * (2 * norm.cdf(offset / right) - 1),
        )

    def ppf(p):
        p = np.asarray(p)
        return center + np.where(
            p < left_mass,
            left * norm.ppf(np.clip(p / (2 * left_mass), 0, 0.5)),
            right * norm.ppf(np.clip(0.5 + (p - left_mass) / (2 * (1 - left_mass)), 0.5, 1)),
        )

    if median_centered:
        measurement = Measurement(center, left, right)

        def pdf(x):
            return np.exp(_log_measurement_density(np.asarray(x), measurement))

        semantics = "reported center is median; half mass per side"
    else:
        pdf = build_pdf_evaluator(
            {"kind": "split_normal", "mu": center, "sigma_l": left, "sigma_r": right}
        )
        semantics = "reported center is mode; widths are Gaussian scales"
    return Density(pdf, cdf, ppf, (-np.inf, np.inf), semantics)


def legacy_density(model):
    pdf = build_pdf_evaluator(model)
    if model["kind"] == "split_normal":
        return two_scales(model["mu"], model["sigma_l"], model["sigma_r"], False)
    if model["kind"] == "gaussian":
        frozen = norm(loc=model["mu"], scale=model["sigma"])
        semantics = "Gaussian center is median and mode"
    else:
        frozen = skewnorm(model["alpha"], loc=model["xi"], scale=model["omega"])
        semantics = "reported center is a median target; xi is a location parameter"
    return Density(pdf, frozen.cdf, frozen.ppf, (-np.inf, np.inf), semantics)


def exp_quantiles(center, left, right, probs):
    if left == right:
        frozen = norm(loc=center, scale=left / norm.ppf(probs[-1]))
        return Density(frozen.pdf, frozen.cdf, frozen.ppf, (-np.inf, np.inf), "Gaussian limit")
    shape = np.log(right / left) / norm.ppf(probs[-1])
    slope = right / np.expm1(shape * norm.ppf(probs[-1]))
    endpoint = center - slope

    def normal_coordinate(x):
        with np.errstate(divide="ignore", invalid="ignore"):
            return np.log1p((np.asarray(x) - center) / slope) / shape

    def cdf(x):
        return np.where(
            (np.asarray(x) - endpoint) / slope > 0, norm.cdf(normal_coordinate(x)), float(shape < 0)
        )

    def pdf(x):
        distance = (np.asarray(x) - endpoint) * shape
        with np.errstate(divide="ignore", invalid="ignore"):
            return np.where(distance > 0, norm.pdf(normal_coordinate(x)) / distance, 0.0)

    def ppf(p):
        return center + slope * np.expm1(shape * norm.ppf(p))

    support = (endpoint, np.inf) if shape > 0 else (-np.inf, endpoint)
    return Density(pdf, cdf, ppf, support, "reported center is exact median; one finite support endpoint")


def signed_trials(center, left, right, *, accepted_shape_limit=None):
    if left == right:
        return fitters.fit_pdf_model(center, left, right, CONFIG), {}
    width = (left + right) / 2
    targets = np.array([-left, 0, right]) / width

    def optimize(objective, x0, bounds, method):
        standardized = skewnorm.ppf(EXACT, alpha)
        scale, location = np.polyfit(standardized, targets, 1)
        shifts = np.array([center, 0, 0])
        units = np.array([width, width, 1])
        lower, upper = (np.array(bounds).T - shifts) / units
        if accepted_shape_limit is not None:
            lower[-1] = max(lower[-1], -accepted_shape_limit)
            upper[-1] = min(upper[-1], accepted_shape_limit)
        guess = np.clip([location, scale, alpha], lower, upper)
        result = minimize(
            lambda candidate: objective(candidate * units + shifts) / width**2,
            guess,
            bounds=list(zip(lower, upper)),
            method=method,
            options={"ftol": 1e-14, "gtol": 1e-9, "maxiter": 250},
        )
        result.x = result.x * units + shifts
        result.fun = objective(result.x)
        return result

    trials = {}
    starts = STARTS if accepted_shape_limit is None else [
        np.clip(start, -accepted_shape_limit, accepted_shape_limit) for start in STARTS
    ]
    for alpha in starts:
        with patch.object(fitters, "minimize", optimize):
            trials[f"{alpha:g}"] = fitters.fit_pdf_model(center, left, right, CONFIG)
    eligible = [
        trial for trial in trials.values() if accepted_shape_limit is None or trial["accepted"]
    ]
    best = min(eligible, key=lambda trial: trial["fit_err"], default=None)
    return best, trials


def quantile_shape_scan():
    shapes = np.r_[0, np.geomspace(1e-3, 1e4, 401), np.inf]
    output = {}
    for name, probs in PROBS.items():
        quantiles = skewnorm.ppf(probs[:, None], shapes[None, :-1])
        half_normal = norm.ppf((1 + probs) / 2)
        quantiles = np.column_stack((quantiles, half_normal))
        ratios = (quantiles[2] - quantiles[1]) / (quantiles[1] - quantiles[0])
        assert np.min(np.diff(ratios)) > -1e-9
        output[name] = {
            "shape": shapes,
            "right_over_left": ratios,
            "max_to_min_ratio_at_alpha_15": float(
                np.diff(skewnorm.ppf(probs, -15))[0] / np.diff(skewnorm.ppf(probs, -15))[1]
            ),
            "half_normal_limit": float(ratios[-1]),
        }
    return output


def metrics(density, center, left, right):
    lower, upper = density.support
    mass_left, error_left = quad(density.pdf, lower, center, epsabs=1e-10)
    mass_right, error_right = quad(density.pdf, center, upper, epsabs=1e-10)
    assert abs(mass_left + mass_right - 1) < 2e-8
    assert abs(mass_left - density.cdf(center)) < 2e-8
    center_left = float(density.pdf(np.nextafter(center, -np.inf)))
    center_right = float(density.pdf(np.nextafter(center, np.inf)))
    targets = np.array([center - left, center, center + right])
    scales = np.array([left, (left + right) / 2, right])
    quantiles = {}
    for name, probs in PROBS.items():
        fitted = density.ppf(probs)
        assert np.allclose(density.cdf(fitted), probs, atol=1e-10, rtol=0)
        quantiles[name] = {
            "value": fitted,
            "signed_error_in_supplied_width": (fitted - targets) / scales,
            "coverage_between_supplied_endpoints": float(
                density.cdf(targets[-1]) - density.cdf(targets[0])
            ),
        }
    return {
        "center_semantics": density.semantics,
        "support": density.support,
        "integrated_mass": mass_left + mass_right,
        "quad_error_estimate": error_left + error_right,
        "left_mass": mass_left,
        "pdf_center_left": center_left,
        "pdf_center_right": center_right,
        "pdf_jump_right_minus_left": center_right - center_left,
        "continuous_at_center": bool(np.isclose(center_left, center_right, atol=1e-12, rtol=1e-12)),
        "mass_outside_unit_bounds": float(density.cdf(-1) + 1 - density.cdf(1)),
        "quantiles": quantiles,
    }


def summarize_axis(axis, density):
    summary = _summarize(axis, density, (0.68,))
    interval = summary.intervals[0]
    components = []
    for lower, upper in interval.hdi:
        interior = (axis > lower) & (axis < upper)
        nodes = np.r_[lower, axis[interior], upper]
        values = np.r_[np.interp(lower, axis, summary.density),
                       summary.density[interior], np.interp(upper, axis, summary.density)]
        mode = int(np.argmax(values))
        components.append({"bounds": [lower, upper], "mode": float(nodes[mode]),
                           "density_at_mode": float(values[mode])})
    return {
        "eti": interval.eti,
        "hdi_components": components,
        "median": summary.median,
        "global_mode": summary.mode,
    }, summary.density


def fixed_mapping(models, out, prefix=""):
    source = json.loads((CASES / "point_angle_ado_jobs.json").read_text())
    label = "135Pr 747.3 keV"
    job_data = next(job for job in source["jobs"] if job["label"] == label)
    job = job_from_dict(job_data)
    response = evaluate_response(job)
    baseline = map_density(job, response)
    xi = response.xi_rad
    sigma = response.sigma
    spin = response.reference_spin
    defined = np.isfinite(baseline.jacobian) & (baseline.jacobian > 0)
    fixed = baseline.jacobian[defined] * norm.pdf(
        response.angular_ratio[defined], loc=job.angular_ratio.value, scale=job.angular_ratio.err_minus
    )
    polar_grid = np.linspace(-1, 1, 241)
    ratio_grid = np.linspace(0.12, 0.62, 181)
    ratio_pdf = norm.pdf(ratio_grid, loc=job.angular_ratio.value, scale=job.angular_ratio.err_minus)
    grids = {"P": polar_grid, "R_ADO": ratio_grid}
    summaries, curves = {}, {}
    for name, density in models.items():
        mapped = np.zeros_like(baseline.parameter_density)
        mapped[defined] = fixed * density.pdf(response.polarization[defined])
        area = float(trapezoid(trapezoid(mapped, xi, axis=1), sigma))
        assert np.isfinite(area) and area > 0
        mapped /= area
        if name == "current":
            assert np.allclose(mapped, baseline.parameter_density, atol=1e-12, rtol=1e-12)
            assert np.isclose(area, baseline.normalization)
        angle_density = trapezoid(mapped, sigma, axis=0)
        sigma_density = spin * trapezoid(mapped, xi, axis=1)
        angle, angle_curve = summarize_axis(np.degrees(xi), np.radians(1) * angle_density)
        alignment, alignment_curve = summarize_axis(sigma / spin, sigma_density)
        negative = xi <= 0
        summaries[name] = {
            "angle_deg": angle, "sigma_over_I": alignment, "mapping_normalization": area,
            "angle_negative_mass": float(trapezoid(angle_density[negative], xi[negative])),
        }
        curves[f"angle_density_per_deg_{name}"] = angle_curve
        curves[f"sigma_over_I_density_{name}"] = alignment_curve
        grids[name] = density.pdf(polar_grid)[:, None] * ratio_pdf[None, :]
    write_csv(out / f"{prefix}angle_marginals.csv", {"angle_deg": np.degrees(xi), **{
        key: value for key, value in curves.items() if key.startswith("angle_")
    }})
    write_csv(out / f"{prefix}sigma_marginals.csv", {"sigma_over_I": sigma / spin, **{
        key: value for key, value in curves.items() if key.startswith("sigma_")
    }})
    rows = []
    for name, axes in summaries.items():
        for axis in ("angle_deg", "sigma_over_I"):
            summary = axes[axis]
            for component, interval in enumerate(summary["hdi_components"], start=1):
                rows.append((name, axis, component, *interval["bounds"], interval["mode"],
                             *summary["eti"], summary["global_mode"], summary["median"]))
    write_csv(out / f"{prefix}inference_summary.csv", dict(zip(
        ("model", "axis", "hdi_component", "hdi_lower", "hdi_upper", "hdi_component_mode",
         "eti_lower", "eti_upper", "global_mode", "median"), zip(*rows)
    )))
    np.savez_compressed(out / f"{prefix}observable_grids.npz", **grids)
    return {
        "job": job_data, "grid": asdict(job.grid), "reference_spin": spin,
        "baseline_warnings": baseline.warnings,
        "sigma_over_I_range": [float(sigma[0] / spin), float(sigma[-1] / spin)],
        "study": summaries,
    }


def write_csv(path, columns):
    with path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(columns)
        writer.writerows(zip(*columns.values()))


def json_safe(value):
    if isinstance(value, np.ndarray):
        return json_safe(value.tolist())
    if isinstance(value, np.generic):
        return json_safe(value.item())
    if isinstance(value, float) and not np.isfinite(value):
        return "Infinity" if value == np.inf else "-Infinity" if value == -np.inf else None
    if isinstance(value, (tuple, list)):
        return [json_safe(item) for item in value]
    if isinstance(value, dict):
        return {key: json_safe(item) for key, item in value.items()}
    return value


def observation_cases():
    candidates = json.loads((CASES / "candidates.json").read_text())["candidates"]
    observations = []
    for ratio in (1, 1.5, 2, 5):
        observations.append((f"control_{ratio:g}_wide_right", 0, 0.1, 0.1 * ratio))
        if ratio > 1:
            observations.append((f"control_{ratio:g}_wide_left", 0, 0.1 * ratio, 0.1))
    for energy in ("747.3", "813.2", "450.2"):
        candidate = next(row for row in candidates if row["display"] == f"135Pr {energy} keV")
        obs = candidate["observations"]["P"]
        key = f"135Pr_{energy.replace('.', 'p')}_P"
        observations.extend([(key, obs["value"], obs["minus"], obs["plus"]),
                             (key + "_reflected", -obs["value"], obs["plus"], obs["minus"])])
    return observations


def sample_points(center, left, right):
    return np.unique(np.r_[np.linspace(center - 5 * left, center + 5 * right, 501),
                           center, np.nextafter(center, -np.inf)])


def acceptance_aware():
    prefix = "acceptance_aware_"
    feasibility = quantile_shape_scan()
    limits = {name: scan["half_normal_limit"] for name, scan in feasibility.items()}
    study, curves, rows = {}, [], []
    mapping = None
    for label, center, left, right in observation_cases():
        selected, trials = signed_trials(center, left, right, accepted_shape_limit=ACCEPTANCE_AWARE_LIMIT)
        stretch = max(left, right) / min(left, right)
        accepted_trials = {start: trial for start, trial in trials.items() if trial["accepted"]}
        entry = {
            "center": center, "minus": left, "plus": right, "wide_over_narrow": stretch,
            "exceeds_skew_normal_family_range": {name: stretch > limit for name, limit in limits.items()},
            "selected": selected, "accepted_starts": list(accepted_trials),
            "trials_by_alpha": trials, "metrics": None,
        }
        study[label] = entry
        beyond_limit = entry["exceeds_skew_normal_family_range"]["exact_16_50_84"]
        if selected is None:
            assert not accepted_trials
            rows.append((label, False, "", "", "", "", "", "", beyond_limit, 0))
            continue
        assert selected["accepted"]
        diagnostics = selected["diagnostics"]
        shape = diagnostics.get("candidate_params", {}).get("alpha")
        if trials:
            assert selected["fit_err"] == min(trial["fit_err"] for trial in accepted_trials.values())
            assert diagnostics["optimizer_success"] and abs(shape) <= ACCEPTANCE_AWARE_LIMIT
        density = legacy_density(selected)
        entry["metrics"] = metrics(density, center, left, right)
        residuals = entry["metrics"]["quantiles"]["exact_16_50_84"]["signed_error_in_supplied_width"]
        rows.append((label, True, selected["kind"], shape, diagnostics.get("optimizer_success"),
                     diagnostics.get("accepted_with_warnings"), selected.get("fit_err"),
                     max(abs(residuals)), beyond_limit, len(accepted_trials)))
        points = sample_points(center, left, right)
        curves.extend(zip([label] * len(points), points, density.pdf(points)))
        if label == "135Pr_747p3_P":
            assert beyond_limit
            assert 0.01 < max(abs(residuals)) < 0.02
            mapping = fixed_mapping({ACCEPTANCE_AWARE_NAME: density}, HERE, prefix)
    assert mapping is not None
    write_csv(HERE / f"{prefix}fits.csv", dict(zip(
        ("case", "accepted", "kind", "alpha", "optimizer_success", "accepted_with_warnings", "sse",
         "max_abs_scaled_residual_q16_q50_q84", "beyond_skew_normal_ratio_limit", "accepted_starts"),
        zip(*rows)
    )))
    write_csv(HERE / f"{prefix}pdf_curves.csv", dict(zip(
        ("case", "x", ACCEPTANCE_AWARE_NAME), zip(*curves)
    )))
    report = {
        "model": ACCEPTANCE_AWARE_NAME,
        "selection": "minimum exact-quantile SSE among candidates accepted by legacy checks",
        "shape_search_limit": ACCEPTANCE_AWARE_LIMIT, "legacy_acceptance_limit": CONFIG.skew_accept_shape_soft_limit,
        "shape_limit_rationale": "0.5 margin inside the original policy limit; a study choice",
        "legacy_config": asdict(CONFIG), "quantile_conventions": PROBS, "shape_ratio_limits": limits,
        "cases": study, "fixed_mapping": mapping,
    }
    (HERE / f"{prefix}results.json").write_text(json.dumps(json_safe(report), indent=2, allow_nan=False) + "\n")
    print(f"PASS acceptance-aware: {sum(row[1] for row in rows)}/{len(rows)} cases returned an accepted PDF")


def main():
    feasibility = quantile_shape_scan()
    study, curves, rows = {}, [], []
    for label, center, left, right in observation_cases():
        legacy = fitters.fit_pdf_model(center, left, right, CONFIG)
        optimized, trials = signed_trials(center, left, right)
        models = {
            "current": two_scales(center, left, right, True),
            "legacy": legacy_density(legacy),
            "split_mode": two_scales(center, left, right, False),
            "legacy_multistart": legacy_density(optimized),
            "smooth_q16": exp_quantiles(center, left, right, EXACT),
            "smooth_1sigma": exp_quantiles(center, left, right, ONE_SIGMA),
        }
        if label == "135Pr_747p3_P":
            mapping = fixed_mapping(models, HERE)
        stretch = max(left, right) / min(left, right)
        study[label] = {
            "center": center, "minus": left, "plus": right,
            "wide_over_narrow": stretch,
            "exceeds_skew_normal_family_range": {
                name: bool(stretch > item["half_normal_limit"]) for name, item in feasibility.items()
            },
            "legacy": legacy, "multistart_min_sse": optimized, "multistart_trials_by_alpha": trials,
            "models": {},
        }
        points = sample_points(center, left, right)
        densities = {}
        for name, density in models.items():
            result = metrics(density, center, left, right)
            study[label]["models"][name] = result
            densities[name] = density.pdf(points)
            for convention, quantiles in result["quantiles"].items():
                rows.append((label, name, convention, *quantiles["value"],
                             *quantiles["signed_error_in_supplied_width"],
                             result["left_mass"], result["integrated_mass"], result["pdf_jump_right_minus_left"]))
        if legacy["kind"] == "split_normal":
            assert np.array_equal(densities["legacy"], densities["split_mode"])
        assert np.allclose(study[label]["models"]["current"]["quantiles"]["normal_one_sigma"]["signed_error_in_supplied_width"], 0, atol=1e-12)
        assert np.allclose(study[label]["models"]["smooth_q16"]["quantiles"]["exact_16_50_84"]["signed_error_in_supplied_width"], 0, atol=1e-12)
        assert np.allclose(study[label]["models"]["smooth_1sigma"]["quantiles"]["normal_one_sigma"]["signed_error_in_supplied_width"], 0, atol=1e-12)
        curves.extend(zip([label] * len(points), points, *densities.values()))
    assert study["control_1_wide_right"]["legacy"]["kind"] == "gaussian"
    for name in ("control_1.5_wide_right", "control_1.5_wide_left", "135Pr_450p2_P", "135Pr_450p2_P_reflected"):
        fit = study[name]["multistart_min_sse"]
        assert fit["accepted"] and max(fit["diagnostics"]["norm_errors"].values()) < 1e-5
    for name in ("control_2_wide_right", "control_5_wide_right", "135Pr_747p3_P", "135Pr_813p2_P"):
        assert all(study[name]["exceeds_skew_normal_family_range"].values())
    for name, entry in study.items():
        if name.endswith("_reflected"):
            original = study[name.removesuffix("_reflected")]
        elif name.endswith("_wide_left"):
            original = study[name.replace("_wide_left", "_wide_right")]
        else:
            continue
        for model in ("current", "split_mode", "smooth_q16", "smooth_1sigma"):
            for convention in PROBS:
                actual = entry["models"][model]["quantiles"][convention]["value"]
                expected = original["models"][model]["quantiles"][convention]["value"]
                assert np.allclose(actual, -expected[::-1], atol=1e-12)
    write_csv(HERE / "pdf_curves.csv", dict(zip(("case", "x", *models), zip(*curves))))
    write_csv(HERE / "pdf_metrics.csv", dict(zip(
        ("case", "model", "convention", "q_low", "q_median", "q_high", "resid_low",
         "resid_median", "resid_high", "left_mass", "integrated_mass", "pdf_jump"), zip(*rows)
    )))
    inputs = [SOURCE, CASES / "candidates.json", CASES / "point_angle_ado_jobs.json",
              Path(fitters.__file__), ARCHIVE / "p_ado/config.py",
              ARCHIVE / "p_ado/pdf/evaluators.py",
              *(PDM / "GUI/src/multipolepdm/pdm" / name for name in
                ("mapping.py", "observations.py", "statistics.py"))]
    report = {
        "versions": {"python": sys.version.split()[0], "numpy": np.__version__, "scipy": scipy.__version__},
        "inputs_sha256": {str(path.relative_to(ROOT)): sha256(path.read_bytes()).hexdigest() for path in inputs},
        "legacy_config": asdict(CONFIG), "quantile_conventions": PROBS,
        "skew_normal_feasibility_scan": feasibility, "cases": study, "fixed_mapping": mapping,
    }
    (HERE / "results.json").write_text(json.dumps(json_safe(report), indent=2, allow_nan=False) + "\n")
    print(f"PASS {len(study)} cases, {len(models)} PDFs, {len(rows)} two-convention metrics; production mapping replay matched")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--acceptance-aware", action="store_true",
                        help="write separate follow-up artifacts with accepted-only selection")
    if parser.parse_args().acceptance_aware:
        acceptance_aware()
    else:
        main()
