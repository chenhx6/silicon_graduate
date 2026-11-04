#!/usr/bin/env python3
"""Finite-spin asymmetric-rotor diagonalizer based on BM-II Sec. 4-5.

This is a pure collective rotor benchmark.  It deliberately excludes
quasiparticles, particle-rotor coupling, feeding and detector response.
The complete |I,K> representation is used, so D2-related degeneracies and
finite-spin corrections are retained by the matrix diagonalization itself.
"""

from __future__ import annotations

import math
from typing import Any, Dict

import numpy as np


def _angular_momentum_matrices(I: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if not math.isfinite(I) or I <= 0.0:
        raise ValueError("I must be finite and positive.")
    doubled = round(2.0 * I)
    if abs(2.0 * I - doubled) > 1.0e-10:
        raise ValueError("I must be integer or half-integer.")
    basis = np.arange(-I, I + 1.0, 1.0, dtype=float)
    dimension = basis.size
    raising = np.zeros((dimension, dimension), dtype=complex)
    for column, m in enumerate(basis[:-1]):
        raising[column + 1, column] = math.sqrt(
            max(0.0, I * (I + 1.0) - m * (m + 1.0))
        )
    lowering = raising.conj().T
    ix = 0.5 * (raising + lowering)
    iy = (raising - lowering) / (2.0j)
    iz = np.diag(basis)
    return basis, ix, iy, iz


def diagonalize_bm_asymmetric_rotor(
    I: float,
    A1: float,
    A2: float,
    A3: float,
) -> Dict[str, Any]:
    """Diagonalize ``H = A1 I1^2 + A2 I2^2 + A3 I3^2``.

    ``A1 < A2 < A3`` follows the BM-II convention used by the high-spin
    expansion, so the corresponding moments satisfy ``J1 > J2 > J3``.
    """
    A1, A2, A3 = float(A1), float(A2), float(A3)
    if not all(math.isfinite(value) for value in (A1, A2, A3)):
        raise ValueError("A1, A2 and A3 must be finite.")
    if not (A1 < A2 < A3):
        raise ValueError("BM-II axis convention requires A1 < A2 < A3.")

    k_basis, ix, iy, iz = _angular_momentum_matrices(float(I))
    hamiltonian = A1 * (ix @ ix) + A2 * (iy @ iy) + A3 * (iz @ iz)
    hamiltonian = 0.5 * (hamiltonian + hamiltonian.conj().T)
    energies, vectors = np.linalg.eigh(hamiltonian)
    dimension = int(k_basis.size)
    trace_expected = dimension * I * (I + 1.0) * (A1 + A2 + A3) / 3.0
    trace_actual = float(np.trace(hamiltonian).real)

    return {
        "I": float(I),
        "dimension": dimension,
        "K_basis": k_basis.tolist(),
        "A1": A1,
        "A2": A2,
        "A3": A3,
        "axis_convention": "A1 < A2 < A3; J1 > J2 > J3",
        "energies": energies.tolist(),
        "eigenvectors_real": vectors.real.tolist(),
        "eigenvectors_imag": vectors.imag.tolist(),
        "trace_expected": float(trace_expected),
        "trace_actual": trace_actual,
        "trace_residual": trace_actual - trace_expected,
        "boundary": (
            "Finite-spin collective asymmetric rotor only; no quasiparticle, "
            "particle-rotor, feeding or detector-response inference."
        ),
    }


def compare_bm_high_spin_with_finite_spin(
    I: float,
    A1: float,
    A2: float,
    A3: float,
    n_max: int = 2,
) -> Dict[str, Any]:
    """Compare BM-II's harmonic high-spin energies with finite-spin levels.

    The full ``|I,K>`` rotor spectrum approaches two nearly degenerate levels
    for each harmonic transverse quantum number.  Pair centroids are therefore
    used as a diagnostic mapping, not as a claim about experimentally assigned
    bands or D2 symmetry labels.
    """
    if not isinstance(n_max, int) or n_max < 0:
        raise ValueError("n_max must be a nonnegative integer.")

    diagonalized = diagonalize_bm_asymmetric_rotor(I, A1, A2, A3)
    omega = 2.0 * float(I) * math.sqrt((A2 - A1) * (A3 - A1))
    harmonic = [
        float(A1) * float(I) * (float(I) + 1.0) + (n + 0.5) * omega
        for n in range(n_max + 1)
    ]

    required_levels = 2 * (n_max + 1)
    exact_levels = np.asarray(diagonalized["energies"], dtype=float)
    if exact_levels.size < required_levels:
        raise ValueError(
            "n_max is too large for the available finite-spin spectrum."
        )

    trajectories = []
    for n, start in enumerate(range(0, required_levels, 2)):
        pair = exact_levels[start:start + 2]
        centroid = float(np.mean(pair))
        splitting = float(abs(pair[1] - pair[0]))
        residual = centroid - harmonic[n]
        trajectories.append(
            {
                "n": n,
                "exact_pair_indices": [start, start + 1],
                "exact_pair_energies": pair.tolist(),
                "exact_pair_centroid": centroid,
                "exact_pair_splitting": splitting,
                "harmonic_energy": harmonic[n],
                "centroid_minus_harmonic": residual,
                "relative_to_hbar_omega": (
                    residual / omega if omega != 0.0 else None
                ),
            }
        )

    return {
        "I": float(I),
        "A1": float(A1),
        "A2": float(A2),
        "A3": float(A3),
        "n_max": n_max,
        "hbar_omega": omega,
        "axis_convention": "A1 < A2 < A3; J1 > J2 > J3",
        "harmonic_energy_formula": "A1*I*(I+1) + (n+1/2)*hbar_omega",
        "mapping": (
            "Sorted finite-spin levels are grouped in pairs as a high-spin "
            "trajectory-centroid diagnostic; pair index is not an experimental "
            "band label."
        ),
        "trajectories": trajectories,
        "boundary": (
            "Pure finite-spin asymmetric rotor versus BM-II harmonic benchmark; "
            "no quasiparticle, particle-rotor, feeding, detector response, or "
            "experimental mode inference."
        ),
    }
