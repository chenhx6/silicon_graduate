"""Numerical change of variables on a supplied response grid."""

import numpy as np
from scipy.integrate import trapezoid

from multipolepdm.contracts import JobRequest, MappingResult, ResponseGrid

from .observations import observation_density


_NEAR_SINGULAR = 1e-12
_SIGMA_EPS_MULTIPLIER = 64
_EDGE_WIDTH_FRACTION = 0.05
_EDGE_MASS_WARNING = 0.10
_EDGE_DENSITY_WARNING = 0.10


def _grid_axis(values: np.ndarray, name: str) -> np.ndarray:
    axis = np.asarray(values, dtype=float)
    if axis.ndim != 1 or axis.size < 3 or not np.isfinite(axis).all():
        raise ValueError(
            f"{name} must be a finite one-dimensional axis with at least three points."
        )
    widths = np.diff(axis)
    if not np.isfinite(widths).all() or not np.all(widths > 0):
        raise ValueError(f"{name} must be strictly increasing with finite spacings.")
    return axis


def _differentiate(
    values: np.ndarray, coordinates: np.ndarray, axis: int
) -> np.ndarray:
    """Use three-point stencils. NaN propagates through any incomplete stencil."""
    samples = np.moveaxis(values, axis, -1)
    widths = np.diff(coordinates)
    slopes = np.diff(samples, axis=-1) / widths
    stencil_widths = widths[:-1] + widths[1:]
    left_fraction = widths[:-1] / stencil_widths
    right_fraction = widths[1:] / stencil_widths

    derivative = np.empty_like(samples)
    derivative[..., 1:-1] = (
        right_fraction * slopes[..., :-1] + left_fraction * slopes[..., 1:]
    )
    derivative[..., 0] = slopes[..., 0] + left_fraction[0] * (
        slopes[..., 0] - slopes[..., 1]
    )
    derivative[..., -1] = slopes[..., -1] + right_fraction[-1] * (
        slopes[..., -1] - slopes[..., -2]
    )
    return np.moveaxis(derivative, -1, axis)


def _has_resolved_sigma_variation(values: np.ndarray, valid: np.ndarray) -> bool:
    """Compare each xi column's sigma range with the scale of the whole response field."""
    lower = np.min(values, axis=0, where=valid, initial=np.inf)
    upper = np.max(values, axis=0, where=valid, initial=-np.inf)
    scale = max(upper.max(), -lower.min())
    if scale <= 0:
        return False
    relative_span = upper / scale - lower / scale
    return bool(np.any(relative_span > _SIGMA_EPS_MULTIPLIER * np.finfo(float).eps))


def _edge_warnings(
    coordinates: np.ndarray, density: np.ndarray, name: str
) -> list[str]:
    lower, upper = coordinates[0], coordinates[-1]
    width = (upper - lower) * _EDGE_WIDTH_FRACTION
    peak = density.max()
    warnings = []
    for side, start, stop, endpoint in (
        ("lower", lower, lower + width, density[0]),
        ("upper", upper - width, upper, density[-1]),
    ):
        interior = coordinates[(coordinates > start) & (coordinates < stop)]
        edge = np.concatenate(([start], interior, [stop]))
        mass = trapezoid(np.interp(edge, coordinates, density), edge)
        endpoint_fraction = endpoint / peak
        if mass >= _EDGE_MASS_WARNING or endpoint_fraction >= _EDGE_DENSITY_WARNING:
            warnings.append(
                f"{name} {side} grid edge indicates possible sensitivity to the finite scan bounds. "
                f"The endpoint density is {endpoint_fraction:.1%} of the marginal peak and the outer 5% "
                f"of the span contains {mass:.1%} of the in-grid mass."
            )
    return warnings


def map_density(job: JobRequest, response: ResponseGrid) -> MappingResult:
    """Map independent measurement densities to a finite (xi_rad, sigma) grid.

    The Jacobian is its absolute determinant, with NaN for undefined stencils.
    Invalid observation nodes and undefined parameter-density nodes have zero
    density for quadrature.
    """
    if len(job.target.multipoles) == 1:
        raise ValueError(
            "A pure one-component target has no mixing-angle degree of freedom. "
            "Use the forward-only path for this target. A two-dimensional PDM PDF is undefined."
        )
    if job.reference_spin <= 0:
        raise ValueError(
            "I_ref=0 requires the forward-only path. A two-dimensional PDM PDF is undefined."
        )
    if (
        response.reference_spin != job.reference_spin
        or response.ratio_name != job.ratio_name
    ):
        raise ValueError(
            "Response reference spin and angular-ratio name must match the job."
        )

    xi = _grid_axis(response.xi_rad, "xi_rad")
    sigma = _grid_axis(response.sigma, "sigma")
    if xi[0] <= -np.pi / 2 or xi[-1] >= np.pi / 2:
        raise ValueError("xi_rad must lie strictly inside (-pi/2, pi/2).")
    shape = (sigma.size, xi.size)
    polar = np.asarray(response.polarization, dtype=float)
    ratio = np.asarray(response.angular_ratio, dtype=float)
    valid = np.asarray(response.valid, dtype=bool)
    if polar.shape != shape or ratio.shape != shape or valid.shape != shape:
        raise ValueError("Response arrays must have shape (n_sigma, n_xi).")
    valid = valid & np.isfinite(polar) & np.isfinite(ratio)
    polar = np.where(valid, polar, np.nan)
    ratio = np.where(valid, ratio, np.nan)
    with np.errstate(over="ignore", invalid="ignore"):
        jacobian = np.abs(
            _differentiate(polar, xi, axis=1) * _differentiate(ratio, sigma, axis=0)
            - _differentiate(polar, sigma, axis=0) * _differentiate(ratio, xi, axis=1)
        )
    defined = np.isfinite(jacobian)
    if not defined.any():
        raise ValueError(
            "No finite Jacobian on the grid. Check the response mask and derivative stencils."
        )
    jacobian[~defined] = np.nan
    if not np.any(jacobian[defined] > 0):
        raise ValueError(
            "The Jacobian is zero at every defined grid point. A two-dimensional PDM PDF is undefined."
        )
    if not (
        _has_resolved_sigma_variation(polar, valid)
        or _has_resolved_sigma_variation(ratio, valid)
    ):
        raise ValueError(
            "No resolved sigma variation in either response field on this grid "
            f"(within {_SIGMA_EPS_MULTIPLIER} machine epsilons relative to each field's scale). "
            "A two-dimensional PDM PDF is numerically unresolved."
        )

    observations = np.zeros(shape)
    observations[valid] = observation_density(
        polar[valid], ratio[valid], job.polarization, job.angular_ratio
    )
    parameter_density = np.zeros(shape)
    with np.errstate(over="ignore", invalid="ignore"):
        np.multiply(
            observations,
            jacobian,
            out=parameter_density,
            where=defined & (jacobian > 0),
        )
        normalization = float(
            trapezoid(trapezoid(parameter_density, xi, axis=1), sigma)
        )
    if not np.isfinite(normalization) or normalization <= 0:
        raise ValueError(
            "The mapped grid has no positive finite normalization. Check the scan and observation scales."
        )
    parameter_density /= normalization

    warnings = [
        "Observation density assumes independent polarization and angular-ratio errors. "
        "Asymmetric errors use a median-centered normal transform with a density jump at the median."
    ]
    if not defined.all():
        warnings.append(
            f"Jacobian undefined at {np.count_nonzero(~defined)} grid points. "
            "Invalid responses and incomplete derivative stencils contribute zero density."
        )
    near_singular = np.count_nonzero(jacobian <= _NEAR_SINGULAR)
    if near_singular:
        warnings.append(
            f"Near-singular Jacobian (<= {_NEAR_SINGULAR:g} in xi_rad, sigma) at {near_singular} grid points."
        )
    warnings.extend(
        _edge_warnings(xi, trapezoid(parameter_density, sigma, axis=0), "xi_rad")
    )
    warnings.extend(
        _edge_warnings(sigma, trapezoid(parameter_density, xi, axis=1), "sigma")
    )
    return MappingResult(
        job,
        response,
        observations,
        jacobian,
        parameter_density,
        normalization,
        tuple(warnings),
    )
