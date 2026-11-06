"""Full two-sector Nambu matrices for controlled paired-rotor diagnostics.

This module uses the frozen paired_single_j_rotor parameter and coordinate
conventions, including h_sp=C_MeV Q_j(gamma), half-integer I,j, positive gap,
and three positive inertias. It does not alter that module or its fits.

In the ORIGINAL particle/time-reversed-hole product coordinates, define

    H = [[H_R + xi, Delta 1], [Delta 1, H_R - xi]],
    xi = 1_I tensor (h_sp - lambda_F 1_j),
    H_R = sum_k (I_k-j_k)**2 / (2 J_k).

The product basis has ascending K,Omega, Omega fastest. With the rotor's
D2 embedding P and positive square-root BCS matrices U,V,E, the two column
embeddings into original Nambu coordinates are

    X_plus  = [UP; VP],   X_minus = [-VP; UP],   X = [X_plus, X_minus].

X is an isometry in the full product space, not a square unitary matrix.
Y=diag(P,P) is the original D2 embedding; W=Y^dagger X is square and unitary.
The complete transformed Hamiltonian, ordered (plus,minus), is

    H_t = [[A+E_D2, t K], [t K^dagger, A-E_D2]],
    A = (UP)^dagger H_R UP + (VP)^dagger H_R VP,
    E_D2 = P^dagger E P,
    K = X_plus^dagger H X_minus
      = -(UP)^dagger H_R VP + (VP)^dagger H_R UP.

Thus K is explicitly the UPPER-RIGHT block, with the sign requested above.
The lower-left block is its adjoint. The real t in [0,1] scales only these
two coupling blocks. It does not scale Delta, the field, or either diagonal
block. t=0 is the two decoupled BCS sectors; t=1 is the stated full H.
For t<1, W H_t W^dagger specifies an artificial interpolation in the
original D2 coordinates, not a new prescription for a physical pair gap.

All energies are MeV and all eigenpairs are returned, including negative
energies. "Plus/minus" labels the BCS coordinate sectors, not the signs of
the total energies; H_R removes any generic +/- energy-pair symmetry.
There is no energy-sign cut, state assignment, overlap matcher, continuation
certification, fit, EM calculation, or file I/O.

Sector weights and neighboring energy spacings are mathematical diagnostics.
Eigenvectors can rotate arbitrarily inside degenerate eigenspaces, and
energy-ordered indices can exchange character at crossings. None of these
outputs identifies physical branches. A NambuSolution is deliberately not
a RotorSolution and is not automatically compatible with its EM/transfer
operators. The physical meaning of branch following requires external work.
"""

from dataclasses import dataclass
import math
from numbers import Real

import numpy as np

if __package__:
    from .paired_single_j_rotor import PairedRotorParameters, RotorSolution, solve as solve_positive
else:
    from paired_single_j_rotor import PairedRotorParameters, RotorSolution, solve as solve_positive

__all__ = [
    "NambuSystem",
    "NambuSolution",
    "build_nambu",
    "hamiltonian_at",
    "original_d2_hamiltonian_at",
    "solve_nambu",
]


def _readonly(array):
    array.setflags(write=False)
    return array


def _finite(array, name):
    if not np.all(np.isfinite(array)):
        raise ValueError(f"non-finite {name}; numerical input scale is unsupported")


def _coupling_parameter(t):
    if isinstance(t, bool) or not isinstance(t, Real):
        raise ValueError("t must be a finite real number in [0,1]")
    try:
        value = float(t)
    except (OverflowError, ValueError) as exc:
        raise ValueError("t must be a finite real number in [0,1]") from exc
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("t must be in [0,1]")
    return value


def _require_system(system):
    if not isinstance(system, NambuSystem):
        raise TypeError("system must be returned by build_nambu")


def _spin(two_j):
    j = two_j / 2
    m = np.arange(-two_j, two_j + 1, 2) / 2
    raising = np.diag(np.sqrt((j - m[:-1]) * (j + m[:-1] + 1)), -1).astype(complex)
    return (
        (raising + raising.conj().T) / 2,
        (raising - raising.conj().T) / (2j),
        np.diag(m).astype(complex),
    )


def _rotor_product(reference):
    two_I, two_j = reference.two_I, reference.parameters.two_j
    body = list(_spin(two_I))
    body[1] *= -1
    particle = _spin(two_j)
    eye_I, eye_j = np.eye(two_I + 1), np.eye(two_j + 1)
    dimension = (two_I + 1) * (two_j + 1)
    h = np.zeros((dimension, dimension), complex)
    for ik, jk, inertia in zip(body, particle, reference.parameters.inertias_hbar2_per_MeV):
        coefficient = 0.5 / inertia
        _finite(coefficient, "rotational coefficient")
        h += coefficient * (
            np.kron(ik @ ik, eye_j) + np.kron(eye_I, jk @ jk)
            - 2 * np.kron(ik, jk)
        )
    return h


@dataclass(frozen=True)
class NambuSystem:
    """Fixed matrices and embeddings, with read-only arrays.

    If P has shape (D,d), original_d2_embedding Y and embedding X both
    have shape (2D,2d). d2_transform W is (2d,2d). Hplus, Hminus and K
    are (d,d). endpoint_product_MeV is the explicitly constructed original
    (2D,2D) H; endpoint_original_d2_MeV is Y^dagger H Y.

    reference_plus retains the frozen rotor solver's complete Hplus
    eigensystem for explicitly chosen mathematical seeds, without matching
    them to any full-Nambu state. Diagnostic errors are absolute numerical
    residuals, not physical error estimates or validity certificates.
    """

    reference_plus: RotorSolution
    rotor_product_MeV: np.ndarray
    endpoint_product_MeV: np.ndarray
    endpoint_original_d2_MeV: np.ndarray
    original_d2_embedding: np.ndarray
    embedding: np.ndarray
    d2_transform: np.ndarray
    Hplus_MeV: np.ndarray
    Hminus_MeV: np.ndarray
    K_MeV: np.ndarray
    unitarity_error: float
    direct_transform_error_MeV: float
    D2_leakage_MeV: float
    positive_reference_error_MeV: float
    hermiticity_error_MeV: float

    @property
    def two_I(self):
        return self.reference_plus.two_I

    @property
    def parameters(self):
        return self.reference_plus.parameters

    @property
    def sector_dimension(self):
        return self.Hplus_MeV.shape[0]

    @property
    def positive_embedding(self):
        return self.embedding[:, :self.sector_dimension]

    @property
    def negative_embedding(self):
        return self.embedding[:, self.sector_dimension:]


@dataclass(frozen=True)
class NambuSolution:
    """All eigenpairs at one t, without physical-state selection.

    eigenvectors are columns in the (+,-) D2 coordinates. embedding maps
    those coordinates to the original particle/hole product basis.
    eigenvectors_original_d2=W@eigenvectors and eigenvectors_product=
    X@eigenvectors expose both coordinate representations.

    plus/minus_sector_weights refer to BCS coordinate sectors, not particle
    number, transfer strength or a branch label. Degenerate eigenvectors,
    and hence their individual weights, can depend on the chosen basis.
    adjacent_spacings_MeV reports sorted spectral gaps without declaring
    unique matches or continuations.

    full_endpoint_residual_norms_MeV uses the ORIGINAL full H at t=1.
    At t<1 this is generally nonzero even for exact eigenvectors of H_t.
    interpolated_residual_norms_MeV and original_d2_residual_norms_MeV
    instead test the interpolated problem in its two square representations.
    """

    system: NambuSystem
    t: float
    hamiltonian_MeV: np.ndarray
    original_d2_hamiltonian_MeV: np.ndarray
    eigenvalues_MeV: np.ndarray
    eigenvectors: np.ndarray
    eigenvectors_original_d2: np.ndarray
    eigenvectors_product: np.ndarray
    plus_sector_weights: np.ndarray
    minus_sector_weights: np.ndarray
    adjacent_spacings_MeV: np.ndarray
    interpolated_residual_norms_MeV: np.ndarray
    original_d2_residual_norms_MeV: np.ndarray
    full_endpoint_residual_norms_MeV: np.ndarray
    hermiticity_error_MeV: float

    @property
    def embedding(self):
        return self.system.embedding


def build_nambu(two_I, params):
    """Construct both sectors from PairedRotorParameters, with positive gap.

    Reuses only public frozen-rotor outputs; its Hplus is independently
    reconstructed from the original H_R before agreement is reported.
    Input spin/gap/inertia checks are inherited from solve_positive.
    """
    reference = solve_positive(two_I, params)
    p = reference.product_embedding
    dimension, d = p.shape
    xp = reference.positive_energy_embedding
    up, vp = xp[:dimension], xp[dimension:]
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            hrot = _rotor_product(reference)
            xi = np.kron(
                np.eye(reference.two_I + 1),
                reference.single_particle.hamiltonian_MeV
                - reference.parameters.lambda_F_MeV * np.eye(reference.parameters.two_j + 1),
            )
            gap = reference.parameters.Delta_MeV * np.eye(dimension)
            original = np.block([[hrot + xi, gap], [gap, hrot - xi]])
            hup, hvp = hrot @ up, hrot @ vp
            a = up.conj().T @ hup + vp.conj().T @ hvp
            s = reference.single_particle.eigenvectors
            e = (s * reference.quasiparticle_energies_MeV) @ s.conj().T
            e_d2 = p.conj().T @ np.kron(np.eye(reference.two_I + 1), e) @ p
            hplus, hminus = a + e_d2, a - e_d2
            k = -up.conj().T @ hvp + vp.conj().T @ hup
            xm = np.vstack((-vp, up))
            x = np.hstack((xp, xm))
            zero_p = np.zeros_like(p)
            y = np.block([[p, zero_p], [zero_p, p]])
            w = y.conj().T @ x
            original_d2 = y.conj().T @ original @ y
            block = np.block([[hplus, k], [k.conj().T, hminus]])
            for array, name in ((original, "original Nambu Hamiltonian"), (block, "Nambu blocks"),
                                (w, "D2 Bogoliubov transform")):
                _finite(array, name)
            unitary_error = max(
                float(np.max(abs(w.conj().T @ w - np.eye(2 * d)))),
                float(np.max(abs(w @ w.conj().T - np.eye(2 * d)))),
            )
            transform_error = float(np.max(abs(x.conj().T @ original @ x - block)))
            leakage = float(np.max(abs(original @ x - x @ block)))
            plus_error = float(np.max(abs(hplus - reference.hamiltonian_MeV)))
            hermitian_error = max(float(np.max(abs(original - original.conj().T))),
                                  float(np.max(abs(block - block.conj().T))))
    except FloatingPointError as exc:
        raise ValueError("inputs overflow the supported Nambu numerical scale") from exc
    return NambuSystem(
        reference_plus=reference, rotor_product_MeV=_readonly(hrot),
        endpoint_product_MeV=_readonly(original),
        endpoint_original_d2_MeV=_readonly(original_d2),
        original_d2_embedding=_readonly(y), embedding=_readonly(x),
        d2_transform=_readonly(w), Hplus_MeV=_readonly(hplus),
        Hminus_MeV=_readonly(hminus), K_MeV=_readonly(k),
        unitarity_error=unitary_error, direct_transform_error_MeV=transform_error,
        D2_leakage_MeV=leakage, positive_reference_error_MeV=plus_error,
        hermiticity_error_MeV=hermitian_error,
    )


def hamiltonian_at(system, t):
    """Return [[Hplus,t*K],[t*K^dagger,Hminus]], retaining every state."""
    _require_system(system)
    t = _coupling_parameter(t)
    return _readonly(np.block([
        [system.Hplus_MeV, t * system.K_MeV],
        [t * system.K_MeV.conj().T, system.Hminus_MeV],
    ]))


def original_d2_hamiltonian_at(system, t):
    """Return W H_t W^dagger in the original particle/hole D2 coordinates."""
    h = hamiltonian_at(system, t)
    w = system.d2_transform
    result = w @ h @ w.conj().T
    _finite(result, "interpolated original D2 Hamiltonian")
    return _readonly(result)


def solve_nambu(system, t=1.0):
    """Diagonalize the entire interpolated matrix; no branch tracking or cuts."""
    _require_system(system)
    t = _coupling_parameter(t)
    h = hamiltonian_at(system, t)
    try:
        with np.errstate(over="raise", invalid="raise"):
            energies, vectors = np.linalg.eigh(h)
            _finite(energies, "Nambu eigenvalues")
            original_h = system.d2_transform @ h @ system.d2_transform.conj().T
            original_vectors = system.d2_transform @ vectors
            product_vectors = system.embedding @ vectors
            interpolation_residual = np.linalg.norm(h @ vectors - vectors * energies, axis=0)
            original_residual = np.linalg.norm(
                original_h @ original_vectors - original_vectors * energies, axis=0)
            endpoint_residual = np.linalg.norm(
                system.endpoint_product_MeV @ product_vectors - product_vectors * energies, axis=0)
            d = system.sector_dimension
            plus_weight = np.sum(abs(vectors[:d]) ** 2, axis=0)
            minus_weight = np.sum(abs(vectors[d:]) ** 2, axis=0)
            for array, name in ((vectors, "Nambu eigenvectors"), (product_vectors, "embedded eigenvectors"),
                                (interpolation_residual, "interpolation residual"),
                                (original_residual, "original D2 residual"),
                                (endpoint_residual, "full-endpoint residual")):
                _finite(array, name)
    except FloatingPointError as exc:
        raise ValueError("inputs overflow the supported Nambu solution scale") from exc
    return NambuSolution(
        system=system, t=t, hamiltonian_MeV=h,
        original_d2_hamiltonian_MeV=_readonly(original_h),
        eigenvalues_MeV=_readonly(energies), eigenvectors=_readonly(vectors),
        eigenvectors_original_d2=_readonly(original_vectors),
        eigenvectors_product=_readonly(product_vectors),
        plus_sector_weights=_readonly(plus_weight), minus_sector_weights=_readonly(minus_weight),
        adjacent_spacings_MeV=_readonly(np.diff(energies)),
        interpolated_residual_norms_MeV=_readonly(interpolation_residual),
        original_d2_residual_norms_MeV=_readonly(original_residual),
        full_endpoint_residual_norms_MeV=_readonly(endpoint_residual),
        hermiticity_error_MeV=float(np.max(abs(h - h.conj().T))),
    )
