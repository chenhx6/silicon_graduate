#!/usr/bin/env python3
"""Fixed-template Poisson peak inference and a single simulated comparison.

Counts must be independent, unweighted, unsubtracted Poisson observations.
Only A >= 0 is fitted; centroid, width and background are treated as known.
The area is the full Gaussian integral, including tails outside the fit window.
Likelihood-ratio intervals and local significances have asymptotic calibration;
neither finite-sample unbiasedness nor a new nuclear level is guaranteed.

Source locators and limits: knowledge/concepts/
poisson-maximum-likelihood-and-gamma-peak-fitting-bias.md.
Simulation uses NumPy's local Generator, not the global random state.
"""

import argparse
import json
import math
from typing import Any, Dict, List, Tuple


def _finite(value: float, name: str, minimum: float = None) -> float:
    try:
        value = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(value) or (minimum is not None and value < minimum):
        raise ValueError(f"{name} must be finite and >= {minimum}")
    return value


def _vector(values, name, counts=False) -> List[float]:
    result = [_finite(x, name, 0 if counts else None) for x in values]
    if not result:
        raise ValueError(f"{name} must not be empty")
    if counts and any(not x.is_integer() for x in result):
        raise ValueError("Poisson observations must be nonnegative integer raw counts")
    return result


def _paired(n_obs, y_model):
    counts = _vector(n_obs, "n_obs", counts=True)
    means = [_finite(y, "model mean", 0) for y in y_model]
    if len(counts) != len(means):
        raise ValueError("observations and model must have identical lengths")
    return counts, means


def gaussian_peak_model(
    channels: List[float], area: float, centroid: float, sigma: float, bg: float
) -> List[float]:
    """Integrate a Gaussian over equally spaced channel bins.

    Channel values are bin centres, with edges halfway between them. A single
    channel has width one. bg is known expected counts per bin, not a density.
    Nonuniform binning needs an explicit different forward model.
    """
    channels = _vector(channels, "channels")
    area = _finite(area, "area", 0)
    centroid = _finite(centroid, "centroid")
    sigma = _finite(sigma, "sigma", 0)
    bg = _finite(bg, "bg", 0)
    if sigma == 0:
        raise ValueError("sigma must be positive")
    width = channels[1] - channels[0] if len(channels) > 1 else 1.0
    if width <= 0 or any(
        not math.isclose(b - a, width, rel_tol=1e-10, abs_tol=1e-12)
        for a, b in zip(channels, channels[1:])
    ):
        raise ValueError("channel centres must be increasing and equally spaced")
    result = []
    for x in channels:
        lo = ((x - centroid) - width / 2) / sigma / math.sqrt(2)
        hi = ((x - centroid) + width / 2) / sigma / math.sqrt(2)
        # Use survival probabilities in either tail to avoid CDF cancellation.
        if lo >= 0:
            mass = 0.5 * (math.erfc(lo) - math.erfc(hi))
        elif hi <= 0:
            mass = 0.5 * (math.erfc(-hi) - math.erfc(-lo))
        else:
            mass = 0.5 * (math.erf(hi) - math.erf(lo))
        result.append(_finite(area * mass + bg, "model mean", 0))
    return result


def compute_neyman_chisq(n_obs: List[float], y_model: List[float]) -> float:
    """Data-weighted comparison loss with the explicit max(1,n) convention."""
    counts, means = _paired(n_obs, y_model)
    return math.fsum((n - y) ** 2 / max(1.0, n)
                     for n, y in zip(counts, means))


def _deviance(counts, means):
    terms = []
    for n, y in zip(counts, means):
        if n == 0:
            terms.append(2 * y)
        elif y == 0:
            return math.inf
        else:
            d = y - n
            if abs(d) < 0.1 * n:
                term = d - n * math.log1p(d / n)
            else:
                term = d + n * (math.log(n) - math.log(y))
            terms.append(2 * max(0.0, term))
    return math.fsum(terms)


def compute_baker_cousins_poisson_deviance(
    n_obs: List[float], y_model: List[float]
) -> float:
    """2 sum(mu-n+n log(n/mu)); (0,0) contributes 0, (n>0,0) infinity.

    Validation rejects fractional or negative observations, but cannot establish
    their provenance: integer background subtraction is still not Poisson data.
    """
    counts, means = _paired(n_obs, y_model)
    return _deviance(counts, means)


def _bisect_increasing(func, lo, hi):
    """Root of an increasing function bracketed by nonpositive/nonnegative ends."""
    for _ in range(120):
        mid = lo + (hi - lo) / 2
        if func(mid) > 0:
            hi = mid
        else:
            lo = mid
        if hi - lo <= 2e-12 * max(1.0, abs(mid)):
            break
    return lo + (hi - lo) / 2


def _fit(channels, n_obs, centroid, sigma, bg, loss_type, data_kind):
    if data_kind != "raw-counts":
        raise ValueError("Use a joint on/off likelihood for background-subtracted data")
    if loss_type not in ("poisson", "neyman"):
        raise ValueError("loss_type must be 'poisson' or 'neyman'")
    template = gaussian_peak_model(channels, 1, centroid, sigma, 0)
    bg = _finite(bg, "bg", 0)
    counts, _ = _paired(n_obs, template)
    mass = math.fsum(template)
    if mass <= 0:
        raise ValueError("Gaussian has no numerically resolvable mass in this window")
    if bg == 0 and any(n > 0 and p == 0 for n, p in zip(counts, template)):
        raise ValueError("Positive counts in a bin with zero model support")

    def loss(area):
        means = [area * p + bg for p in template]
        if loss_type == "poisson":
            return _deviance(counts, means)
        return math.fsum((n - y) ** 2 / max(1.0, n)
                         for n, y in zip(counts, means))

    if loss_type == "neyman":
        # Solve the weighted linear least-squares problem without a scan.
        curvature = math.fsum(p * p / max(1.0, n)
                              for n, p in zip(counts, template))
        if curvature == 0:
            raise ValueError("Neyman curvature underflow; rescale the model")
        area = max(0.0, math.fsum(p * (n - bg) / max(1.0, n)
                                  for n, p in zip(counts, template)) / curvature)
    elif bg == 0:
        area = math.fsum(counts) / mass
    else:
        # Negative score of log L is monotone; its sign at A=0 tests the boundary.
        def negative_score(area):
            return math.fsum(
                p - (n * p) / (area * p + bg) for n, p in zip(counts, template)
            )

        if negative_score(0) >= 0:
            area = 0.0
        else:
            # At this bound sum(n*p/(A*p+b)) <= sum(n)/A = mass.
            upper = _finite(math.fsum(counts) / mass, "area bracket", 0)
            area = _bisect_increasing(negative_score, 0, upper)
    return _finite(area, "fitted area", 0), loss, mass


def _loss_interval(area, loss, delta):
    minimum = loss(area)
    target = minimum + delta
    lower = 0.0
    if area > 0 and loss(0) > target:
        lower = _bisect_increasing(lambda a: target - loss(a), 0, area)
    upper = area + max(1.0, math.sqrt(area))
    while loss(upper) < target:
        upper = area + 2 * (upper - area)
        if not math.isfinite(upper):
            raise ValueError("Cannot bracket likelihood endpoint at finite precision")
    upper = _bisect_increasing(lambda a: loss(a) - target, area, upper)
    return lower, upper


def fit_peak_area_1d(
    channels: List[float], n_obs: List[float], centroid: float, sigma: float,
    bg: float, loss_type: str = "poisson"
) -> Tuple[float, float, float]:
    """Compatibility tuple (area, minimum loss, upper delta-loss=1 distance).

    The third element is not a symmetric standard error or a coverage guarantee.
    For Neyman it is only a loss contour. Use infer_peak_area for Poisson endpoints.
    """
    area, loss, _ = _fit(channels, n_obs, centroid, sigma, bg, loss_type, "raw-counts")
    _, upper = _loss_interval(area, loss, 1.0)
    return area, loss(area), upper - area


def infer_peak_area(
    channels: List[float], n_obs: List[float], centroid: float, sigma: float,
    bg: float, *, delta_deviance: float = 1.0, data_kind: str = "raw-counts"
) -> Dict[str, Any]:
    """Nonnegative MLE and conditional LR interval for fixed shape/background.

    With no nuisance parameters the profile is just the one-dimensional
    likelihood. Nominal delta=1 (about 68%) or 3.84 (about 95%, two-sided) uses
    regular asymptotics only. Low counts and A=0 require coverage calibration.
    """
    delta = _finite(delta_deviance, "delta_deviance", 0)
    if delta == 0:
        raise ValueError("delta_deviance must be positive")
    bg = _finite(bg, "bg", 0)
    area, loss, mass = _fit(channels, n_obs, centroid, sigma, bg, "poisson", data_kind)
    minimum, null = loss(area), loss(0)
    lower, upper = _loss_interval(area, loss, delta)
    q0 = max(0.0, null - minimum) if area > 0 else 0.0
    if bg == 0:
        calibration, z, p = "unavailable-zero-background-null", None, None
    else:
        calibration = "asymptotic-local-half-chi-square"
        z = math.sqrt(q0)
        # Inclusive-tail convention at the atom: no excess means p=1, Z=0.
        p = 0.5 * math.erfc(z / math.sqrt(2)) if q0 > 0 else 1.0
    return {
        "fitted_area_counts": area,
        "min_deviance_chi_lambda2": minimum,
        "null_deviance_A0": null if math.isfinite(null) else None,
        "null_has_zero_likelihood": not math.isfinite(null),
        "area_error_lower_counts": area - lower,
        "area_error_upper_counts": upper - area,
        "profile_likelihood_interval": {
            "lower_counts": lower, "upper_counts": upper, "delta_deviance": delta,
            "coverage": "not-calibrated-finite-sample",
            "nuisance_treatment": "centroid-width-background-fixed",
        },
        "window_signal_fraction": mass,
        "local_test": {
            "q0": q0 if math.isfinite(q0) else None,
            "calibration": calibration, "z_asymptotic_local": z,
            "p_asymptotic_local": p,
            "p_at_q0_zero_convention": "inclusive-tail-p=1; no-excess-Z=0",
        },
    }


def evaluate_peak_fitting_methods(
    true_area: float = 60.0, centroid: float = 50.0, sigma: float = 2.0,
    bg_counts: float = 2.0, seed: int = 42
) -> Dict[str, Any]:
    """Generate ONE spectrum; its errors are not estimates of ensemble bias.

    Positional API and main result sections are preserved. Deprecated
    bias_percentage means single-realization relative error, undefined at A=0.
    Legacy Z and upper-error keys alias explicitly qualified quantities.
    """
    import numpy as np

    true_area = _finite(true_area, "true_area", 0)
    channels = [float(i) for i in range(100)]
    means = gaussian_peak_model(channels, true_area, centroid, sigma, bg_counts)
    counts = np.random.default_rng(seed).poisson(means).tolist()
    poi = infer_peak_area(channels, counts, centroid, sigma, bg_counts)
    area, loss, _ = _fit(channels, counts, centroid, sigma, bg_counts,
                         "neyman", "raw-counts")
    ney = {"fitted_area_counts": area, "min_neyman_chisq": loss(area)}
    for fit in (poi, ney):
        error = fit["fitted_area_counts"] - true_area
        fit["estimation_error_counts"] = error
        fit["relative_error_percentage"] = 100 * error / true_area if true_area else None
        fit["bias_percentage"] = fit["relative_error_percentage"]
    poi["area_uncertainty_1sigma"] = poi["area_error_upper_counts"]
    poi["statistical_significance_Z_sigma"] = poi["local_test"]["z_asymptotic_local"]
    poi["delta_chi2"] = poi["local_test"]["q0"]
    return {
        "true_parameters": {
            "true_area_counts": true_area, "centroid_channel": centroid,
            "sigma_channel": sigma, "background_counts_per_channel": bg_counts,
        },
        "poisson_mle_baker_cousins": poi,
        "neyman_least_squares": ney,
        "simulation": {
            "kind": "single-realization-not-ensemble-bias",
            "seed": seed, "sampler": "numpy.random.default_rng.poisson",
            "channels": channels, "observed_counts": counts,
            "expected_counts": means,
        },
        "api_notes": {
            "bias_percentage": "deprecated alias of single-realization relative_error_percentage",
            "area_uncertainty_1sigma": "deprecated alias of upper delta-deviance=1 distance only",
            "statistical_significance_Z_sigma": "alias of asymptotic local Z; may be null",
            "removed": ["is_unbiased", "systematic_underestimation",
                        "neyman_least_squares.area_uncertainty_1sigma"],
        },
    }


def format_text_report(res: Dict[str, Any]) -> str:
    poi, ney = res["poisson_mle_baker_cousins"], res["neyman_least_squares"]
    interval, test = poi["profile_likelihood_interval"], poi["local_test"]
    z = test["z_asymptotic_local"]
    significance = f"{z:.3f}" if z is not None else "unavailable (singular null)"
    return "\n".join([
        "POISSON PEAK FIT: fixed centroid, width and known background",
        f"True simulated full Gaussian area: {res['true_parameters']['true_area_counts']:.3f}",
        f"Nonnegative Poisson MLE area: {poi['fitted_area_counts']:.3f} counts",
        f"LR interval (delta={interval['delta_deviance']:g}): "
        f"[{interval['lower_counts']:.3f}, {interval['upper_counts']:.3f}] counts",
        f"Minimum Poisson deviance: {poi['min_deviance_chi_lambda2']:.3f}",
        f"Asymptotic LOCAL excess Z: {significance}",
        f"Neyman area (max(1,n) weights): {ney['fitted_area_counts']:.3f} counts",
        f"Single-realization Poisson estimation error: {poi['estimation_error_counts']:+.3f} counts",
        f"Single-realization Neyman estimation error: {ney['estimation_error_counts']:+.3f} counts",
        "These errors do not measure ensemble bias; MLE can have finite-sample bias.",
        "Interval coverage and local p-values need calibration for sparse/boundary data.",
        "Minimum deviance has no automatic chi-square goodness-of-fit calibration.",
        "A centroid/width search requires a trials correction; background uncertainty needs profiling.",
        "A large local Z alone does not establish a new transition or nuclear level.",
        "Fit raw counts; background-subtracted spectra require a joint observation model.",
    ])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--area", "-A", type=float, default=60.0)
    parser.add_argument("--bg", type=float, default=2.0)
    parser.add_argument("--centroid", type=float, default=50.0)
    parser.add_argument("--sigma", type=float, default=2.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        res = evaluate_peak_fitting_methods(args.area, args.centroid, args.sigma,
                                            args.bg, args.seed)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(res, indent=2, allow_nan=False) if args.json else format_text_report(res))


if __name__ == "__main__":
    main()
