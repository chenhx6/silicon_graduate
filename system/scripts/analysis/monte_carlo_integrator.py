#!/usr/bin/env python3
"""Bounded Monte Carlo integration tools based on Zhu Ch. 14.

The module implements:
  - uniform Monte Carlo integration over a rectangular domain;
  - importance sampling through an explicit proposal sampler/density;
  - one-dimensional adaptive stratified sampling with variance-aware allocation.

The outputs are numerical estimators and standard errors.  They do not replace
an experiment-specific detector response, likelihood, or coverage calibration.
"""

from __future__ import annotations

import math
from typing import Any, Callable, Dict, Iterable, Optional, Sequence, Tuple

import numpy as np


def _validate_bounds(bounds: Sequence[Tuple[float, float]]) -> tuple[np.ndarray, np.ndarray]:
    if not bounds:
        raise ValueError("bounds must contain at least one interval.")
    lower = np.asarray([item[0] for item in bounds], dtype=float)
    upper = np.asarray([item[1] for item in bounds], dtype=float)
    if lower.ndim != 1 or upper.ndim != 1 or lower.size != upper.size:
        raise ValueError("bounds must be a sequence of (lower, upper) pairs.")
    if not np.all(np.isfinite(lower)) or not np.all(np.isfinite(upper)):
        raise ValueError("bounds must be finite.")
    if np.any(upper <= lower):
        raise ValueError("Each upper bound must be greater than its lower bound.")
    return lower, upper


def monte_carlo_integrate(
    function: Callable[[np.ndarray], float],
    bounds: Sequence[Tuple[float, float]],
    n_samples: int,
    *,
    seed: Optional[int] = None,
    proposal_sampler: Optional[Callable[[np.random.Generator, int], np.ndarray]] = None,
    proposal_density: Optional[Callable[[np.ndarray], np.ndarray]] = None,
) -> Dict[str, Any]:
    r"""Estimate a finite-dimensional integral and its Monte Carlo error.

    With no proposal functions, samples are uniform in the rectangular domain:
    \(I \approx V \bar g\).  With a proposal, the sampler must return samples
    in the domain and the density must be evaluated in the same coordinate
    convention; the estimator is \(g(x)/q(x)\).
    """
    if not isinstance(n_samples, int) or n_samples < 2:
        raise ValueError("n_samples must be an integer >= 2.")
    lower, upper = _validate_bounds(bounds)
    dimension = lower.size
    volume = float(np.prod(upper - lower))
    rng = np.random.default_rng(seed)

    if proposal_sampler is None:
        samples = rng.uniform(lower, upper, size=(n_samples, dimension))
        weights = np.full(n_samples, volume, dtype=float)
        sampling_mode = "uniform-rectangular"
    else:
        if proposal_density is None:
            raise ValueError("proposal_density is required with proposal_sampler.")
        samples = np.asarray(proposal_sampler(rng, n_samples), dtype=float)
        if samples.shape != (n_samples, dimension):
            raise ValueError("proposal_sampler must return shape (n_samples, dimension).")
        weights = 1.0 / np.asarray(proposal_density(samples), dtype=float)
        sampling_mode = "importance-sampling"

    if not np.all(np.isfinite(samples)) or np.any(samples < lower) or np.any(samples > upper):
        raise ValueError("All proposal samples must be finite and inside bounds.")
    if not np.all(np.isfinite(weights)) or np.any(weights <= 0.0):
        raise ValueError("All importance weights must be finite and positive.")

    values = np.asarray([function(sample) for sample in samples], dtype=float)
    if values.shape != (n_samples,) or not np.all(np.isfinite(values)):
        raise ValueError("function must return one finite scalar for each sample.")
    contributions = values * weights
    estimate = float(np.mean(contributions))
    sample_variance = float(np.var(contributions, ddof=1))
    standard_error = math.sqrt(sample_variance / n_samples)
    return {
        "estimate": estimate,
        "sample_variance": sample_variance,
        "standard_error": standard_error,
        "n_samples": n_samples,
        "dimension": int(dimension),
        "sampling_mode": sampling_mode,
        "seed": seed,
        "bounds": [(float(a), float(b)) for a, b in zip(lower, upper)],
        "boundary": (
            "Estimator uncertainty is Monte Carlo sampling error only; "
            "no model, detector-response or coverage uncertainty is included."
        ),
    }


def adaptive_stratified_integrate_1d(
    function: Callable[[float], float],
    lower: float,
    upper: float,
    n_samples: int,
    *,
    n_strata: int = 8,
    pilot_samples_per_stratum: int = 8,
    seed: Optional[int] = None,
) -> Dict[str, Any]:
    r"""Estimate a 1D integral using pilot variance and stratified allocation.

    Stratum allocation follows the variance-aware rule
    \(L_i \propto V_i s_i\), with a uniform fallback when all pilot standard
    deviations vanish.  The pilot observations are included in the reported
    estimator through stratum means; production samples are allocated on top of
    the pilot budget.
    """
    lower = float(lower)
    upper = float(upper)
    if not math.isfinite(lower) or not math.isfinite(upper) or upper <= lower:
        raise ValueError("upper must be greater than finite lower.")
    if not isinstance(n_samples, int) or n_samples < n_strata * pilot_samples_per_stratum:
        raise ValueError("n_samples must cover the pilot sample budget.")
    if not isinstance(n_strata, int) or n_strata < 1:
        raise ValueError("n_strata must be positive.")
    if not isinstance(pilot_samples_per_stratum, int) or pilot_samples_per_stratum < 2:
        raise ValueError("pilot_samples_per_stratum must be >= 2.")

    rng = np.random.default_rng(seed)
    edges = np.linspace(lower, upper, n_strata + 1)
    widths = np.diff(edges)
    pilot_values = []
    pilot_stds = []
    for i in range(n_strata):
        x = rng.uniform(edges[i], edges[i + 1], pilot_samples_per_stratum)
        y = np.asarray([function(float(value)) for value in x], dtype=float)
        if not np.all(np.isfinite(y)):
            raise ValueError("function must return finite values.")
        pilot_values.append(y)
        pilot_stds.append(float(np.std(y, ddof=1)))

    remaining = n_samples - n_strata * pilot_samples_per_stratum
    allocation_weights = widths * np.asarray(pilot_stds)
    if float(np.sum(allocation_weights)) <= 0.0:
        allocation_weights = widths.copy()
    raw = remaining * allocation_weights / float(np.sum(allocation_weights))
    extra = np.floor(raw).astype(int)
    for index in np.argsort(-(raw - extra))[: remaining - int(np.sum(extra))]:
        extra[index] += 1

    stratum_estimates = []
    stratum_variances = []
    allocated_counts = []
    for i in range(n_strata):
        n_i = pilot_samples_per_stratum + int(extra[i])
        if extra[i] > 0:
            x_extra = rng.uniform(edges[i], edges[i + 1], int(extra[i]))
            y_extra = np.asarray([function(float(value)) for value in x_extra], dtype=float)
            values = np.concatenate([pilot_values[i], y_extra])
        else:
            values = pilot_values[i]
        mean_i = float(np.mean(values))
        var_i = float(np.var(values, ddof=1)) if values.size > 1 else 0.0
        stratum_estimates.append(mean_i)
        stratum_variances.append(var_i)
        allocated_counts.append(int(values.size))

    estimate = float(np.sum(widths * np.asarray(stratum_estimates)))
    variance_estimate = float(
        np.sum((widths * widths) * np.asarray(stratum_variances) / np.asarray(allocated_counts))
    )
    return {
        "estimate": estimate,
        "standard_error": math.sqrt(max(0.0, variance_estimate)),
        "variance_estimate": variance_estimate,
        "n_samples": int(sum(allocated_counts)),
        "n_strata": n_strata,
        "stratum_edges": edges.tolist(),
        "stratum_sample_counts": allocated_counts,
        "pilot_standard_deviations": pilot_stds,
        "seed": seed,
        "boundary": (
            "One-dimensional adaptive stratification; allocation uses pilot variances "
            "and does not include model or numerical-discretization uncertainty."
        ),
    }
