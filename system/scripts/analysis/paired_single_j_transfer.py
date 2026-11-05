"""Bare single-j addition/removal from a declared even-core R=0 state.

This is an explicit transfer-operator model, not the induced boson-fermion
operator used in the 1998 IBFM paper. It excludes multistep reaction effects,
other j orbitals, DWBA normalization and configuration-dependent renormalization.
It can be compared to relative strengths within the same j channel only under
those additional assumptions; its strengths are not mixing probabilities.

In the product basis for I=j, the normalized R=0 vector has
v[K,Omega]=delta(K,Omega)/sqrt(2j+1). The positive-energy Nambu embeddings give
addition and removal amplitudes sqrt(2j+1) v^dagger X_particle/hole psi.
Summing over the complete retained D2 spectrum yields sum(u_nu^2) and
sum(v_nu^2); their sum is 2j+1. Spectral truncation need not saturate these sums.
"""
from dataclasses import dataclass
import numpy as np

from paired_single_j_rotor import RotorSolution


@dataclass(frozen=True)
class BareTransferResult:
    removal_strengths: np.ndarray
    addition_strengths: np.ndarray
    removal_sum: float
    addition_sum: float
    bcs_removal_sum: float
    bcs_addition_sum: float
    sum_rule_error: float


def strengths(solution):
    """Return bare strengths for I=j, without energy-window or state matching."""
    if not isinstance(solution, RotorSolution):
        raise TypeError("solution must be a RotorSolution")
    if solution.two_I != solution.parameters.two_j:
        raise ValueError("a bare rank-j operator from R=0 requires final I=j")
    n = solution.parameters.two_j + 1
    r0 = np.eye(n, dtype=float).reshape(-1) / np.sqrt(n)
    p = solution.product_embedding
    if np.linalg.norm(p @ (p.conj().T @ r0) - r0) > 1e-10:
        raise ValueError("R=0 vector is outside the supplied D2 sector")
    x = solution.positive_energy_embedding
    addition = np.abs(np.sqrt(n) * (r0 @ x[:n*n] @ solution.eigenvectors)) ** 2
    removal = np.abs(np.sqrt(n) * (r0 @ x[n*n:] @ solution.eigenvectors)) ** 2
    expected_removal = float(solution.v @ solution.v)
    expected_addition = float(solution.u @ solution.u)
    error = max(abs(float(removal.sum()) - expected_removal),
                abs(float(addition.sum()) - expected_addition),
                abs(float(removal.sum() + addition.sum()) - n))
    removal.setflags(write=False)
    addition.setflags(write=False)
    return BareTransferResult(
        removal, addition, float(removal.sum()), float(addition.sum()),
        expected_removal, expected_addition, error,
    )
