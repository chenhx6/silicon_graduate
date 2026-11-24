"""Marginalize and evaluate the piecewise-linear PDFs in angle and sigma/I."""

from collections.abc import Iterable
from dataclasses import replace
from math import pi, tan

import numpy as np
from scipy.integrate import trapezoid

from multipolepdm.contracts import HDISegment, Interval, MappingResult, MarginalSummary, Summary

DEFAULT_INTERVAL_MASS = 0.68


_DELTA_AREA_TOLERANCE = 2e-7


def _delta_curve(xi: np.ndarray, density: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Interpolate in xi and refine the transformed piecewise-linear PDF.

    Compare the trapezoid in delta against the exact xi mass on each half
    segment, with an error budget apportioned by xi width.
    """
    area_budget = _DELTA_AREA_TOLERANCE * trapezoid(density, xi) / (xi[-1] - xi[0])
    delta = np.tan(xi)
    if not np.all(np.diff(delta) > 0):
        raise ValueError(
            "xi_rad must transform to strictly increasing delta coordinates."
        )
    transformed = density * np.cos(xi) ** 2
    while True:
        widths = np.diff(xi)
        midpoint = xi[:-1] + widths / 2
        left_xi_width = midpoint - xi[:-1]
        right_xi_width = xi[1:] - midpoint
        mid_density = density[:-1] + (density[1:] - density[:-1]) * (
            left_xi_width / widths
        )
        mid_delta = np.tan(midpoint)
        left_width = mid_delta - delta[:-1]
        right_width = delta[1:] - mid_delta
        linear_mid = transformed[:-1] + (transformed[1:] - transformed[:-1]) * (
            left_width / (left_width + right_width)
        )
        left_error = np.abs(
            (
                left_width * (transformed[:-1] + linear_mid)
                - left_xi_width * (density[:-1] + mid_density)
            )
            / 2
        )
        right_error = np.abs(
            (
                right_width * (linear_mid + transformed[1:])
                - right_xi_width * (mid_density + density[1:])
            )
            / 2
        )
        split = np.flatnonzero(
            (left_error + right_error > area_budget * widths)
            & (left_xi_width > 0)
            & (right_xi_width > 0)
            & (left_width > 0)
            & (right_width > 0)
        )
        if split.size == 0:
            return delta, transformed
        xi = np.insert(xi, split + 1, midpoint[split])
        density = np.insert(density, split + 1, mid_density[split])
        delta = np.insert(delta, split + 1, mid_delta[split])
        transformed = np.insert(
            transformed, split + 1, mid_density[split] * np.cos(midpoint[split]) ** 2
        )


def _quantile(
    coordinate: np.ndarray,
    density: np.ndarray,
    cumulative: np.ndarray,
    probability: float,
) -> float:
    target = probability * cumulative[-1]
    upper = int(np.searchsorted(cumulative, target))
    if upper == 0 or target == cumulative[upper]:
        return float(coordinate[upper])
    lower = upper - 1
    mass_fraction = (target - cumulative[lower]) / (
        cumulative[upper] - cumulative[lower]
    )
    left, right = density[lower : upper + 1] / max(density[lower], density[upper])
    root = np.sqrt((1 - mass_fraction) * left**2 + mass_fraction * right**2)
    position = mass_fraction * (left + right) / (left + root)
    return float(coordinate[lower] + position * (coordinate[upper] - coordinate[lower]))


def density_segment(
    coordinate: np.ndarray, density: np.ndarray, bounds: tuple[float, float]
) -> tuple[np.ndarray, np.ndarray]:
    """Return a piecewise-linear density restricted to the given bounds."""
    start, stop = bounds
    first = np.searchsorted(coordinate, start, side="right")
    last = np.searchsorted(coordinate, stop, side="left")
    nodes = np.concatenate(([start], coordinate[first:last], [stop]))
    heights = np.concatenate(
        (
            [np.interp(start, coordinate, density)],
            density[first:last],
            [np.interp(stop, coordinate, density)],
        )
    )
    return nodes, heights


def _hdi_segment(
    coordinate: np.ndarray, density: np.ndarray, bounds: tuple[float, float]
) -> HDISegment:
    nodes, heights = density_segment(coordinate, density, bounds)
    highest = heights == heights.max()
    edges = np.flatnonzero(np.diff(highest, prepend=False, append=False))
    mode_ranges = tuple(
        (float(nodes[left]), float(nodes[right - 1]))
        for left, right in edges.reshape(-1, 2)
    )
    return HDISegment(bounds, float(trapezoid(heights, nodes)), mode_ranges)


def _hdi(
    coordinate: np.ndarray, density: np.ndarray, mass: float
) -> tuple[tuple[HDISegment, ...], float]:
    """Find the density threshold and integrate the clipped linear segments."""
    widths = np.diff(coordinate)
    left, right = density[:-1], density[1:]
    low, high = np.minimum(left, right), np.maximum(left, right)
    cell_mass = widths * (left + right) / 2
    target = mass * cell_mass.sum()
    flat_heights = np.unique(low[(low == high) & (low > 0)])

    def mass_at_or_above(height: float) -> float:
        partial = (low < height) & (high > height)
        fraction = (high[partial] - height) / (high[partial] - low[partial])
        return float(
            cell_mass[low >= height].sum()
            + np.sum(widths[partial] * fraction * (high[partial] + height) / 2)
        )

    lower, upper = 0.0, float(density.max())
    while True:
        threshold = lower + (upper - lower) / 2
        if threshold == lower or threshold == upper:
            break
        if mass_at_or_above(threshold) >= target:
            lower = threshold
        else:
            upper = threshold

    threshold = lower
    plateau = np.searchsorted(flat_heights, lower)
    if plateau < flat_heights.size and flat_heights[plateau] <= upper:
        threshold = float(flat_heights[plateau])

    above = high > threshold
    starts, stops = coordinate[:-1].copy(), coordinate[1:].copy()
    rising = above & (left < threshold)
    falling = above & (right < threshold)
    starts[rising] += (
        widths[rising] * (threshold - left[rising]) / (right[rising] - left[rising])
    )
    stops[falling] -= (
        widths[falling]
        * (threshold - right[falling])
        / (left[falling] - right[falling])
    )

    tied = (low == threshold) & (high == threshold) & (threshold > 0)
    if tied.any():
        remaining = target - (mass_at_or_above(threshold) - cell_mass[tied].sum())
        for index in np.flatnonzero(tied):
            if remaining <= 0:
                break
            if remaining < cell_mass[index]:
                stops[index] = starts[index] + remaining / threshold
            above[index] = True
            remaining -= cell_mass[index]

    intervals = []
    for start, stop in zip(starts[above], stops[above]):
        if stop <= start:
            continue
        if intervals and start <= intervals[-1][1]:
            intervals[-1] = (intervals[-1][0], float(stop))
        else:
            intervals.append((float(start), float(stop)))
    return tuple(
        _hdi_segment(coordinate, density, bounds) for bounds in intervals
    ), threshold


def _moments(coordinate: np.ndarray, density: np.ndarray) -> tuple[float, float]:
    """Integrate the first moment and centered second moment exactly per cell."""
    left, right = coordinate[:-1], coordinate[1:]
    lower, upper = density[:-1], density[1:]
    midpoint = (left + right) / 2
    widths = right - left
    mean = float(np.sum(widths * (
        left * lower + 2 * midpoint * (lower + upper) + right * upper
    )) / 6)
    variance = np.sum(widths * (
        (left - mean) ** 2 * lower
        + 2 * (midpoint - mean) ** 2 * (lower + upper)
        + (right - mean) ** 2 * upper
    )) / 6
    return mean, float(np.sqrt(variance))


def _summarize(
    coordinate: np.ndarray, density: np.ndarray, masses: tuple[float, ...],
    coordinate_name: str,
) -> MarginalSummary:
    widths = np.diff(coordinate)
    if not np.all(widths > 0):
        raise ValueError("Marginal coordinates must be strictly increasing.")
    area = float(trapezoid(density, coordinate))
    if not np.isfinite(area) or area <= 0:
        raise ValueError("A marginal must have positive finite mass.")
    density = density / area
    cumulative = np.concatenate(
        ([0.0], np.cumsum(widths * (density[:-1] + density[1:]) / 2))
    )

    intervals = []
    for mass in masses:
        tail = (1 - mass) / 2
        eti = (
            _quantile(coordinate, density, cumulative, tail),
            _quantile(coordinate, density, cumulative, 1 - tail),
        )
        segments, threshold = _hdi(coordinate, density, mass)
        intervals.append(Interval(mass, eti, segments, threshold))
    mean, std = _moments(coordinate, density)
    mean_bounds = (mean - std, mean + std)
    mean_flags = tuple(
        () if coordinate[0] <= bound <= coordinate[-1] else ("outside_scan",)
        for bound in mean_bounds
    )
    return MarginalSummary(
        coordinate=coordinate,
        density=density,
        median=_quantile(coordinate, density, cumulative, 0.5),
        mode=float(coordinate[np.argmax(density)]),
        intervals=tuple(intervals),
        coordinate_name=coordinate_name,
        evaluation_coordinate=coordinate_name,
        mean=mean,
        std=std,
        mean_bounds=mean_bounds,
        mean_bound_flags=mean_flags,
    )


def _delta_report(angle: MarginalSummary) -> MarginalSummary:
    """Map angle estimates to delta while retaining the angle threshold measure."""
    coordinate, density = _delta_curve(angle.coordinate, angle.density)
    density /= trapezoid(density, coordinate)
    intervals = tuple(
        replace(
            interval,
            eti=tuple(map(tan, interval.eti)),
            hdi_segments=tuple(
                HDISegment(
                    tuple(map(tan, segment.bounds)),
                    segment.mass,
                    tuple(tuple(map(tan, band)) for band in segment.mode_ranges),
                )
                for segment in interval.hdi_segments
            ),
        )
        for interval in angle.intervals
    )
    flags = tuple(
        existing + (("tan_singularity",) if abs(bound) >= pi / 2 else ())
        for bound, existing in zip(angle.mean_bounds, angle.mean_bound_flags)
    )
    return MarginalSummary(
        coordinate=coordinate,
        density=density,
        median=tan(angle.median),
        mode=tan(angle.mode),
        intervals=intervals,
        coordinate_name="delta",
        evaluation_coordinate=angle.evaluation_coordinate,
        mean=tan(angle.mean),
        std=None,
        mean_bounds=tuple(
            None if flag else tan(bound)
            for bound, flag in zip(angle.mean_bounds, flags)
        ),
        mean_bound_flags=flags,
    )


def summarize_density(
    result: MappingResult, masses: Iterable[float] = (DEFAULT_INTERVAL_MASS,)
) -> Summary:
    """Evaluate angles and sigma/I and report angle estimates through tan.

    ETI and HDI use their piecewise-linear evaluation curves. At an HDI threshold
    plateau, ties are taken from left to right to attain the requested mass.
    """
    masses = tuple(float(mass) for mass in masses)
    if any(not 0 < mass < 1 for mass in masses):
        raise ValueError("Interval masses must lie strictly between zero and one.")
    response = result.response
    spin = response.reference_spin
    if not np.isfinite(spin) or spin <= 0:
        raise ValueError(
            "A finite positive I_ref is required to summarize sigma/I_ref."
        )
    xi, sigma = (
        np.asarray(response.xi_rad, dtype=float),
        np.asarray(response.sigma, dtype=float),
    )
    if (
        xi.ndim != 1 or sigma.ndim != 1 or xi.size < 2 or sigma.size < 2
        or not np.all(np.diff(xi) > 0) or not np.all(np.diff(sigma) > 0)
        or not np.isfinite(sigma).all() or not (-pi / 2 < xi[0] < xi[-1] < pi / 2)
    ):
        raise ValueError(
            "Marginal axes must be finite and increasing, with angles inside tan's principal domain."
        )
    density = np.asarray(result.parameter_density, dtype=float)
    if (
        density.shape != (sigma.size, xi.size)
        or not np.isfinite(density).all()
        or np.any(density < 0)
    ):
        raise ValueError(
            "Parameter density must be finite and nonnegative with shape (n_sigma, n_xi)."
        )
    xi_density = trapezoid(density, sigma, axis=0)
    sigma_density = trapezoid(density, xi, axis=1)
    angle = _summarize(xi, xi_density, masses, "arctan_delta")
    return Summary(
        delta=_delta_report(angle),
        sigma_over_i=_summarize(sigma / spin, spin * sigma_density, masses, "sigma_over_i"),
        arctan_delta=angle,
    )
