"""Axial Gaussian source populations; no gated-state Gaussian replacement."""

from functools import lru_cache

import numpy as np
from sympy import Rational
from sympy.physics.wigner import clebsch_gordan

from multipolepdm.contracts import spin


def substates(j):
    return np.arange(-spin(j), spin(j) + 1)


def initial_population(j, sigma):
    sigma = np.asarray(sigma, dtype=float)
    if np.any(~np.isfinite(sigma)) or np.any(sigma <= 0):
        raise ValueError("sigma must be finite and positive.")
    m = substates(j)
    # Subtract the least m^2 before exponentiation, including half-integer spins.
    offset = m * m - np.min(m * m)
    # Minimal-|m| states retain unit relative weight if sigma squared underflows.
    with np.errstate(over="ignore", under="ignore", divide="ignore", invalid="ignore"):
        exponent = np.where(offset == 0, 0.0, -offset / (2 * sigma[..., None] ** 2))
        weights = np.exp(exponent)
    return weights / weights.sum(axis=-1, keepdims=True)


@lru_cache(maxsize=256)
def tensor_weights(j, rank):
    jj = Rational(round(2 * spin(j)), 2)
    return np.array(
        [
            float(
                (-1) ** round(j - m)
                * clebsch_gordan(
                    jj,
                    jj,
                    rank,
                    Rational(round(2 * m), 2),
                    Rational(round(-2 * m), 2),
                    0,
                )
            )
            for m in substates(j)
        ]
    ) * np.sqrt(2 * j + 1)


def orientation_tensor(j, populations, rank):
    return np.asarray(populations) @ tensor_weights(j, rank)
