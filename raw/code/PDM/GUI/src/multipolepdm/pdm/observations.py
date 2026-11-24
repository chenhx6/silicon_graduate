"""Independent polarization and angular-ratio measurement densities."""

from math import log, pi

import numpy as np

from multipolepdm.contracts import Measurement


def _log_measurement_density(
    values: np.ndarray, measurement: Measurement
) -> np.ndarray:
    values = np.asarray(values, dtype=float)
    scale = np.where(
        values < measurement.value, measurement.err_minus, measurement.err_plus
    )
    with np.errstate(over="ignore"):
        standardized = (values - measurement.value) / scale
        return -0.5 * standardized**2 - np.log(scale) - 0.5 * log(2 * pi)


def measurement_density(values: np.ndarray, measurement: Measurement) -> np.ndarray:
    """Evaluate the density of a standard normal scaled separately on each side.

    Each side carries probability 1/2. The center is the median, and the
    lower and upper error endpoints are the Phi(-1) and Phi(1) quantiles.
    Unequal scales cause a jump at the median. The value there is the
    right-hand limit.
    """
    return np.exp(_log_measurement_density(values, measurement))


def observation_density(
    polarization: np.ndarray,
    angular_ratio: np.ndarray,
    polarization_measurement: Measurement,
    ratio_measurement: Measurement,
) -> np.ndarray:
    """Evaluate the product density under the independent-error approximation."""
    return np.exp(
        _log_measurement_density(polarization, polarization_measurement)
        + _log_measurement_density(angular_ratio, ratio_measurement)
    )


def observation_mesh(polarization_measurement, ratio_measurement, points=257):
    """Regular observed-space coordinates; distinct from response-grid samples."""

    def axis(measurement):
        return np.linspace(
            measurement.value - 5 * measurement.err_minus,
            measurement.value + 5 * measurement.err_plus,
            points,
        )

    polar, ratio = axis(polarization_measurement), axis(ratio_measurement)
    return (
        polar,
        ratio,
        observation_density(
            polar[:, None], ratio[None, :], polarization_measurement, ratio_measurement
        ),
    )
