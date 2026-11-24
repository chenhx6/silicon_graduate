"""Exact full-direction, polarization-summed unobserved transition channel."""

import numpy as np

from multipolepdm.physics.amplitudes import coupling_matrices, emit
from multipolepdm.physics.populations import orientation_tensor, tensor_weights


def propagate_unobserved(rho, transition):
    angle = np.arctan(transition.delta)
    weights = (
        (1.0,)
        if len(transition.multipoles) == 1
        else (np.cos(angle) ** 2, np.sin(angle) ** 2)
    )
    value = 0
    for multipole, weight in zip(transition.multipoles, weights):
        value = value + weight * emit(
            rho,
            coupling_matrices(
                transition.spin_initial, transition.spin_final, int(multipole[1:])
            ),
        )
    return value


def propagate_path(rho, path):
    for transition in path:
        rho = propagate_unobserved(rho, transition)
    return rho


def deorientation_coefficient(transition, rank):
    """Transfer eigenvalue for normalized B_k, computed from the exact channel."""
    if rank > 2 * min(transition.spin_initial, transition.spin_final):
        return 0.0
    before = tensor_weights(transition.spin_initial, rank)
    rho = np.diag(before)
    after = propagate_unobserved(rho, transition).diagonal().real
    return float(
        orientation_tensor(transition.spin_final, after, rank)
        / orientation_tensor(transition.spin_initial, before, rank)
    )
