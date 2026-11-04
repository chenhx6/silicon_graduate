#!/usr/bin/env python3
"""Small bounded minimization tools based on Zhu Ch. 13.

These routines are deliberately narrower than a full MINUIT implementation:
they provide a reproducible one-dimensional bracketed minimizer and a
profile-threshold scan for asymmetric parameter errors.  They do not infer
coverage or replace a multidimensional likelihood fit.
"""

from __future__ import annotations

import math
from typing import Any, Callable, Dict, Optional


def _finite_value(function: Callable[[float], float], x: float) -> float:
    value = float(function(float(x)))
    if not math.isfinite(value):
        raise ValueError("objective must return a finite scalar.")
    return value


def golden_section_minimize(
    function: Callable[[float], float],
    lower: float,
    upper: float,
    *,
    tolerance: float = 1.0e-8,
    max_iterations: int = 256,
) -> Dict[str, Any]:
    """Minimize a presumed unimodal scalar objective on a closed interval.

    The method follows the 0.618/golden-section contraction discussed in
    Zhu Ch. 13.2.  A multimodal objective may return only a local minimum
    within the supplied bracket.
    """
    lower = float(lower)
    upper = float(upper)
    tolerance = float(tolerance)
    if not math.isfinite(lower) or not math.isfinite(upper) or upper <= lower:
        raise ValueError("lower and upper must be finite with upper > lower.")
    if not math.isfinite(tolerance) or tolerance <= 0.0:
        raise ValueError("tolerance must be positive and finite.")
    if not isinstance(max_iterations, int) or max_iterations < 1:
        raise ValueError("max_iterations must be a positive integer.")

    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    x_left = upper - ratio * (upper - lower)
    x_right = lower + ratio * (upper - lower)
    f_left = _finite_value(function, x_left)
    f_right = _finite_value(function, x_right)
    calls = 2

    for iteration in range(1, max_iterations + 1):
        if abs(upper - lower) <= tolerance:
            break
        if f_left <= f_right:
            upper = x_right
            x_right, f_right = x_left, f_left
            x_left = upper - ratio * (upper - lower)
            f_left = _finite_value(function, x_left)
        else:
            lower = x_left
            x_left, f_left = x_right, f_right
            x_right = lower + ratio * (upper - lower)
            f_right = _finite_value(function, x_right)
        calls += 1
    else:
        iteration = max_iterations

    candidate = x_left if f_left <= f_right else x_right
    candidate_value = f_left if f_left <= f_right else f_right
    return {
        "x": float(candidate),
        "objective": float(candidate_value),
        "bracket": [float(lower), float(upper)],
        "iterations": int(iteration),
        "function_calls": int(calls),
        "converged": bool(abs(upper - lower) <= tolerance),
        "boundary": (
            "Assumes a useful unimodal bracket; a bounded local minimum is "
            "not evidence of a global minimum or statistical coverage."
        ),
    }


def _profile_root(
    function: Callable[[float], float],
    x_hat: float,
    target: float,
    bound: float,
    direction: int,
    initial_step: float,
    tolerance: float,
    max_iterations: int,
) -> Dict[str, Any]:
    """Find one threshold crossing while moving away from x_hat."""
    near = float(x_hat)
    far = near + direction * float(initial_step)
    far = max(bound, far) if direction < 0 else min(bound, far)
    f_near = _finite_value(function, near) - target
    f_far = _finite_value(function, far) - target
    if f_near > tolerance:
        raise ValueError("objective(x_hat) must be at or below the threshold.")

    step = abs(far - near)
    for _ in range(max_iterations):
        if f_far >= 0.0:
            break
        if far == bound:
            return {
                "root": None,
                "status": "open",
                "bracket": [min(near, far), max(near, far)],
            }
        step *= 2.0
        next_far = near + direction * step
        next_far = max(bound, next_far) if direction < 0 else min(bound, next_far)
        near, f_near = far, f_far
        far = next_far
        f_far = _finite_value(function, far) - target
    else:
        return {
            "root": None,
            "status": "bracket-failed",
            "bracket": [min(near, far), max(near, far)],
        }

    lo, hi = (far, near) if direction < 0 else (near, far)
    f_lo = f_far if direction < 0 else f_near
    f_hi = f_near if direction < 0 else f_far
    for _ in range(max_iterations):
        if hi - lo <= tolerance:
            break
        mid = 0.5 * (lo + hi)
        f_mid = _finite_value(function, mid) - target
        if f_mid >= 0.0:
            if direction < 0:
                lo, f_lo = mid, f_mid
            else:
                hi, f_hi = mid, f_mid
        else:
            if direction < 0:
                hi, f_hi = mid, f_mid
            else:
                lo, f_lo = mid, f_mid
    root = 0.5 * (lo + hi)
    return {
        "root": float(root),
        "status": "crossed",
        "bracket": [float(lo), float(hi)],
    }


def profile_threshold_interval(
    function: Callable[[float], float],
    x_hat: float,
    delta_objective: float,
    lower_bound: float,
    upper_bound: float,
    *,
    initial_step: Optional[float] = None,
    tolerance: float = 1.0e-8,
    max_iterations: int = 256,
) -> Dict[str, Any]:
    """Estimate asymmetric errors from a one-dimensional objective profile.

    The two endpoints solve ``f(x) = f(x_hat) + delta_objective``.  This is
    the MINOS-like profile idea described in Zhu Ch. 13.8, while leaving the
    choice of ``delta_objective`` to the caller (for example, a likelihood
    or least-squares convention).  Bounds that never cross the threshold are
    reported as open rather than fabricated as finite errors.
    """
    lower_bound = float(lower_bound)
    upper_bound = float(upper_bound)
    x_hat = float(x_hat)
    delta_objective = float(delta_objective)
    tolerance = float(tolerance)
    if not (
        math.isfinite(lower_bound)
        and math.isfinite(upper_bound)
        and lower_bound < upper_bound
    ):
        raise ValueError("bounds must be finite with lower_bound < upper_bound.")
    if not lower_bound <= x_hat <= upper_bound:
        raise ValueError("x_hat must lie inside the supplied bounds.")
    if not math.isfinite(delta_objective) or delta_objective <= 0.0:
        raise ValueError("delta_objective must be positive and finite.")
    if not math.isfinite(tolerance) or tolerance <= 0.0:
        raise ValueError("tolerance must be positive and finite.")
    if not isinstance(max_iterations, int) or max_iterations < 1:
        raise ValueError("max_iterations must be a positive integer.")

    f_hat = _finite_value(function, x_hat)
    target = f_hat + delta_objective
    scale = max(upper_bound - lower_bound, tolerance)
    step = float(initial_step) if initial_step is not None else scale / 100.0
    if not math.isfinite(step) or step <= 0.0:
        raise ValueError("initial_step must be positive and finite.")
    step = min(step, scale)

    left = _profile_root(
        function,
        x_hat,
        target,
        lower_bound,
        -1,
        step,
        tolerance,
        max_iterations,
    )
    right = _profile_root(
        function,
        x_hat,
        target,
        upper_bound,
        +1,
        step,
        tolerance,
        max_iterations,
    )
    left_root = left["root"]
    right_root = right["root"]
    return {
        "x_hat": x_hat,
        "objective_at_hat": f_hat,
        "threshold": target,
        "lower": left_root,
        "upper": right_root,
        "lower_error": None if left_root is None else x_hat - left_root,
        "upper_error": None if right_root is None else right_root - x_hat,
        "lower_status": left["status"],
        "upper_status": right["status"],
        "lower_bracket": left["bracket"],
        "upper_bracket": right["bracket"],
        "boundary": (
            "Profile-threshold endpoints are one-dimensional objective "
            "crossings; they are not automatically confidence intervals. "
            "Coverage and nuisance-parameter treatment remain external."
        ),
    }
