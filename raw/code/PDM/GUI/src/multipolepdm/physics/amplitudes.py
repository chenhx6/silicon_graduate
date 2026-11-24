"""Unit-total-radiation photon amplitudes in a declared helicity basis.

Rows are daughter m, columns are parent m; helicity order is (+1, -1).
The analyzer uses electric-field axes e_theta (parallel) and e_phi (perp).
All angles accepted here are radians. The (-1)^L basis phase makes the input
E2/M1 ratio the KS/Droste radiation amplitude ratio (D96 Eqs.3/5/7), not the
opposite-signed bare CG/D basis ratio.
"""

from functools import lru_cache

import numpy as np
from scipy.linalg import expm
from sympy import Rational
from sympy.physics.wigner import clebsch_gordan

from multipolepdm.physics.populations import substates


@lru_cache(maxsize=256)
def coupling_matrices(ji, jf, rank):
    mi, mf = substates(ji), substates(jf)
    result = np.zeros((2 * rank + 1, len(mf), len(mi)))
    a, b = Rational(round(2 * jf), 2), Rational(round(2 * ji), 2)
    for f, m_f in enumerate(mf):
        for i, m_i in enumerate(mi):
            q = m_i - m_f
            if abs(q) <= rank and q == round(q):
                result[int(q + rank), f, i] = float(
                    clebsch_gordan(
                        a,
                        rank,
                        b,
                        Rational(round(2 * m_f), 2),
                        int(q),
                        Rational(round(2 * m_i), 2),
                    )
                )
    result.setflags(write=False)
    return result


@lru_cache(maxsize=512)
def small_d(rank, theta):
    m = np.arange(-rank, rank + 1)
    raising = np.diag(np.sqrt((rank - m[:-1]) * (rank + m[:-1] + 1)), -1)
    value = expm((raising.T - raising) * (theta / 2))
    value.setflags(write=False)
    return value


@lru_cache(maxsize=1024)
def pure_amplitudes(ji, jf, multipole, theta, phi):
    rank = int(multipole[1:])
    couplings = coupling_matrices(ji, jf, rank)
    q = np.arange(-rank, rank + 1)
    d = small_d(rank, float(theta))
    amplitudes = []
    for helicity in (1, -1):
        angular = np.exp(1j * q * phi) * d[:, helicity + rank]
        electric = helicity if multipole.startswith("E") else 1
        source_phase = (-1) ** rank
        amplitudes.append(
            source_phase
            * electric
            * np.sqrt((2 * rank + 1) / (8 * np.pi))
            * np.einsum("q,qfi->fi", angular, couplings)
        )
    value = np.asarray(amplitudes)
    value.setflags(write=False)
    return value


def emission_amplitudes(transition, theta, phi=0.0, xi_rad=None):
    parts = [
        pure_amplitudes(
            transition.spin_initial, transition.spin_final, p, float(theta), float(phi)
        )
        for p in transition.multipoles
    ]
    if len(parts) == 1:
        return parts[0]
    xi = np.arctan(transition.delta) if xi_rad is None else xi_rad
    return np.cos(xi) * parts[0] + np.sin(xi) * parts[1]


def analyzer_amplitudes(helicity):
    plus, minus = helicity
    return (plus + minus) / np.sqrt(2), (plus - minus) / (1j * np.sqrt(2))


def emit(rho, amplitudes):
    """Sum specified polarization channels without renormalizing gate weights."""
    amplitudes = np.asarray(amplitudes)
    if amplitudes.ndim == 2:
        amplitudes = amplitudes[None, ...]
    return np.einsum(
        "afi,...ij,agj->...fg", amplitudes, rho, amplitudes.conj(), optimize=True
    )
