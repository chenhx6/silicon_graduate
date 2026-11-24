"""Step-defined axes with explicit final cells (never silently rescale a step)."""

from math import ceil, isfinite

import numpy as np

MAX_GRID_POINTS = 20_000_000


def stepped_axis(lower: float, upper: float, step: float) -> np.ndarray:
    if not all(isfinite(v) for v in (lower, upper, step)):
        raise ValueError("Grid bounds and step must be finite.")
    if not lower < upper or step <= 0:
        raise ValueError("Require minimum < maximum and a positive grid step.")
    count = (upper - lower) / step
    if not isfinite(count) or count > MAX_GRID_POINTS - 1:
        raise ValueError("Grid axis exceeds the supported point limit.")
    # Roundoff at an exact multiple must not create a near-zero last cell.
    nearest = round(count)
    if abs(count - nearest) <= 32 * np.finfo(float).eps * max(1, abs(count)):
        intervals = nearest
    else:
        intervals = ceil(count)
    if intervals < 2:
        raise ValueError("Each grid axis requires at least three points; reduce step.")
    result = lower + np.arange(intervals + 1, dtype=float) * step
    result[-1] = upper
    if not np.all(np.diff(result) > 0):
        raise ValueError("Grid step is too small to resolve at these coordinates.")
    return result


def axis_metadata(axis: np.ndarray, requested_step: float | None) -> dict:
    steps = np.diff(axis)
    return {
        "minimum": float(axis[0]),
        "maximum": float(axis[-1]),
        "points": int(axis.size),
        "requested_step": requested_step,
        "actual_step_min": float(steps.min()),
        "actual_step_max": float(steps.max()),
        "last_step": float(steps[-1]),
    }
