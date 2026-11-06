"""A single-j paired rotor with an explicitly defined, custom convention.

The dimensionless spin-quadrupole operator is

    Q_j(gamma) = [cos(gamma) (3 j_3**2 - j(j+1) 1)
                  + sqrt(3) sin(gamma) (j_1**2 - j_2**2)] / [4 j(j+1)],

and h_sp = C_MeV Q_j(gamma). C_MeV includes the sign and the entire strength.
It is NOT silently identified with a coefficient multiplying printed Y_2mu.
For example, conventional unit-normalized spherical harmonics projected into
the h_11/2 spinor give -sqrt(5/(4*pi)) Q_j for the corresponding real Y_2
combination. The tests check that normalization with an angular integral.
No beta/mass prescription, original-paper normalization, or Gizon calculation
is certified by this module.

All spins are half-integer, specified by positive odd integers two_j/two_I.
Angular momenta are in hbar units, energies in MeV, angles in degrees, and
the three strictly positive principal inertias in hbar**2/MeV. Axes (1,2,3)
are kept in their supplied order: inertias are never sorted. Body-fixed total
I has anomalous commutators; the single-particle j has ordinary commutators.

Only a strictly positive fixed Delta_MeV is supported. lambda_F_MeV and Delta
are inputs, not solutions of number/gap equations. With positive square roots
u, v, E = hypot(epsilon-lambda_F, Delta), the retained Hamiltonian is

    H_plus = U H_rot U + V H_rot V + E,
    H_rot  = sum_k (I_k - j_k)**2 / (2 J_k).

Here U,V,E act on the single-particle factor. The off-diagonal Nambu coupling
(often denoted h*eta) is explicitly discarded. This is a projection
approximation, not diagonalization of the full coupled Nambu Hamiltonian.
Delta=0 is rejected even away from a crossing; at a Fermi degeneracy a
separate occupation/limiting prescription would be needed.

The product basis is |K> x |Omega>, K and Omega ascending, Omega varying
fastest. Eigenvector columns returned by solve are coefficients in the D2
basis. product_embedding maps these coefficients into the product basis;
positive_energy_embedding additionally includes U,V and maps into the
particle block followed by the time-reversed-hole block. An EM operator
requires its own explicit particle/hole and core conventions: the bare
product embedding alone is not a BCS transformation of that operator.
Phases and bases inside degenerate eigenspaces are arbitrary.

There is no mode assignment, physical calibration, energy-zero adjustment,
file I/O, or import-time computation. Numerical residuals and passing tests
do not establish physical applicability or validate an EM prediction.
"""

from dataclasses import dataclass
import math
from numbers import Integral, Real

import numpy as np

__all__ = [
    "PairedRotorParameters",
    "SingleParticleSpectrum",
    "RotorSolution",
    "quadrupole_operator",
    "d2_embedding",
    "single_particle_spectrum",
    "lambda_from_top_pair",
    "tilde_lambda_from_top_pair",
    "irrotational_moments",
    "solve",
]


def _half_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, Integral) or value <= 0 or value % 2 != 1:
        raise ValueError(f"{name} must be a positive odd integer (twice a half-integer spin)")
    return int(value)


def _finite_real(value, name):
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a finite real number")
    try:
        result = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name} must be representable as a finite float") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def _inertias(values):
    try:
        result = tuple(values)
    except TypeError as exc:
        raise ValueError("inertias must contain exactly three strictly positive finite values") from exc
    if len(result) != 3:
        raise ValueError("inertias must contain exactly three values, in axis order (1,2,3)")
    result = tuple(_finite_real(x, "inertia") for x in result)
    if any(x <= 0 for x in result):
        raise ValueError("all three inertias must be strictly positive")
    return result


def _readonly(array):
    array.setflags(write=False)
    return array


def _require_finite(array, name):
    if not np.all(np.isfinite(array)):
        raise ValueError(f"inputs produce non-finite {name}; numerical scale is unsupported")


def _angle(gamma_deg):
    # Preserve the supplied axis convention; reduce only full 360-degree turns.
    return math.radians(math.remainder(_finite_real(gamma_deg, "gamma_deg"), 360.0))


@dataclass(frozen=True)
class PairedRotorParameters:
    """Inputs for the declared Q_j convention; no implicit nuclear parameters.

    C_MeV may be positive, negative, or zero; lambda_F_MeV is unrestricted
    apart from finiteness. gamma_deg may cover any domain. Inertias are copied
    to an immutable tuple, so later mutation of an input list has no effect.
    Invalid numerical inputs raise ValueError. Finite inputs that overflow
    derived matrices are also rejected when the calculation is attempted.
    """

    two_j: int
    C_MeV: float
    gamma_deg: float
    inertias_hbar2_per_MeV: tuple[float, float, float]
    lambda_F_MeV: float
    Delta_MeV: float

    def __post_init__(self):
        object.__setattr__(self, "two_j", _half_integer(self.two_j, "two_j"))
        for name in ("C_MeV", "gamma_deg", "lambda_F_MeV", "Delta_MeV"):
            object.__setattr__(self, name, _finite_real(getattr(self, name), name))
        object.__setattr__(self, "inertias_hbar2_per_MeV", _inertias(self.inertias_hbar2_per_MeV))
        if self.Delta_MeV <= 0:
            raise ValueError(
                "Delta_MeV must be strictly positive; zero gap and Fermi degeneracy "
                "need a separate occupation/limiting prescription"
            )


@dataclass(frozen=True)
class SingleParticleSpectrum:
    """Sorted eigenpairs in ascending-Omega coordinates, without pairing.

    eigenvalues_MeV contains all 2j+1 states, including Kramers multiplicity.
    kramers_pair_energies_MeV averages adjacent partners and contains j+1/2
    entries. These entries may themselves coincide, e.g. for C=0; the last
    two entries then cannot define a top-pair Fermi coordinate.
    Arrays are read-only; copy them before editing.
    """

    two_j: int
    C_MeV: float
    gamma_deg: float
    hamiltonian_MeV: np.ndarray
    eigenvalues_MeV: np.ndarray
    eigenvectors: np.ndarray
    kramers_pair_energies_MeV: np.ndarray


@dataclass(frozen=True)
class RotorSolution:
    """Eigenpairs of the retained positive-energy D2 block, with no zero shift.

    Let D=(two_I+1)(two_j+1), d=D/4. eigenvectors is (d,d), with eigenvectors
    in columns; product_embedding P is (D,d), positive_energy_embedding X is
    (2D,d). d2_basis_twice_K_Omega specifies each column of P in order.

    P @ eigenvectors are product-coordinate quasiparticle amplitudes.
    X @ eigenvectors include particle/hole amplitudes, but need not be
    eigenvectors of the full Nambu Hamiltonian because eta was discarded.
    hamiltonian_product_MeV is H_plus before the D2 reduction.
    u, v and quasiparticle_energies_MeV are in single_particle's eigenbasis.
    All array outputs are read-only. Residual fields are absolute MeV errors,
    not physical error estimates or pass/fail evidence.
    """

    two_I: int
    parameters: PairedRotorParameters
    single_particle: SingleParticleSpectrum
    eigenvalues_MeV: np.ndarray
    eigenvectors: np.ndarray
    product_embedding: np.ndarray
    positive_energy_embedding: np.ndarray
    d2_basis_twice_K_Omega: tuple[tuple[int, int], ...]
    hamiltonian_MeV: np.ndarray
    hamiltonian_product_MeV: np.ndarray
    quasiparticle_energies_MeV: np.ndarray
    u: np.ndarray
    v: np.ndarray
    hermiticity_error_MeV: float
    d2_leakage_MeV: float


def _spin_matrices(two_j):
    j = two_j / 2
    m = np.arange(-two_j, two_j + 1, 2, dtype=float) / 2
    raising = np.zeros((two_j + 1, two_j + 1), dtype=complex)
    for index, projection in enumerate(m[:-1]):
        raising[index + 1, index] = math.sqrt((j - projection) * (j + projection + 1))
    return (
        (raising + raising.conj().T) / 2,
        (raising - raising.conj().T) / (2j),
        np.diag(m).astype(complex),
    )


def quadrupole_operator(two_j, gamma_deg):
    """Return the explicitly defined dimensionless Q_j, not a printed Y_2 field."""
    two_j = _half_integer(two_j, "two_j")
    gamma = _angle(gamma_deg)
    j = two_j / 2
    x, y, z = _spin_matrices(two_j)
    result = (
        math.cos(gamma) * (3 * z @ z - j * (j + 1) * np.eye(two_j + 1))
        + math.sqrt(3) * math.sin(gamma) * (x @ x - y @ y)
    ) / (4 * j * (j + 1))
    return _readonly(result)


def _d2_keys(two_I, two_j):
    return tuple(
        (k, omega)
        for k in range(-two_I, two_I + 1, 2)
        for omega in range(-two_j, two_j + 1, 2)
        if (two_j + k) % 4 == 0 and (two_j + omega) % 4 == 0
    )


def d2_embedding(two_I, two_j):
    """Orthonormal D2 embedding for half-integer I,j; column phase (-1)^(I-j).

    Each column is (|K,Omega> + (-1)^(I-j)|-K,-Omega>)/sqrt(2).
    The representatives have j+K and j+Omega even; K then Omega ascend.
    Rows are the full product basis, Omega fastest. No restriction I>=j
    is imposed. Integer I or j is outside this interface.
    """
    two_I = _half_integer(two_I, "two_I")
    two_j = _half_integer(two_j, "two_j")
    keys = _d2_keys(two_I, two_j)
    p = np.zeros(((two_I + 1) * (two_j + 1), len(keys)), dtype=float)
    phase = 1 if ((two_I - two_j) // 2) % 2 == 0 else -1
    for column, (k, omega) in enumerate(keys):
        row = ((k + two_I) // 2) * (two_j + 1) + (omega + two_j) // 2
        opposite = ((-k + two_I) // 2) * (two_j + 1) + (-omega + two_j) // 2
        p[row, column] = 1 / math.sqrt(2)
        p[opposite, column] = phase / math.sqrt(2)
    return _readonly(p)


def single_particle_spectrum(two_j, C_MeV, gamma_deg):
    """Diagonalize C_MeV Q_j(gamma); return all states and sorted Kramers pairs."""
    two_j = _half_integer(two_j, "two_j")
    strength = _finite_real(C_MeV, "C_MeV")
    angle = _finite_real(gamma_deg, "gamma_deg")
    try:
        with np.errstate(over="raise", invalid="raise"):
            h = strength * quadrupole_operator(two_j, angle)
            _require_finite(h, "single-particle Hamiltonian")
            energies, vectors = np.linalg.eigh(h)
            _require_finite(energies, "single-particle energies")
            pairs = 0.5 * energies[::2] + 0.5 * energies[1::2]
    except FloatingPointError as exc:
        raise ValueError("single-particle numerical scale is unsupported") from exc
    return SingleParticleSpectrum(
        two_j, strength, angle, _readonly(h), _readonly(energies),
        _readonly(vectors), _readonly(pairs),
    )


def _top_pair(spectrum):
    if not isinstance(spectrum, SingleParticleSpectrum):
        raise TypeError("spectrum must be returned by single_particle_spectrum")
    pairs = spectrum.kramers_pair_energies_MeV
    if pairs.ndim != 1 or pairs.size < 2 or not np.all(np.isfinite(pairs)):
        raise ValueError("top-pair conversion requires at least two finite Kramers-pair energies")
    if np.any(np.diff(pairs) < 0):
        raise ValueError("Kramers-pair energies must be in ascending order")
    upper, lower = float(pairs[-1]), float(pairs[-2])
    interval = lower - upper
    resolution = 64 * np.finfo(float).eps * max(abs(upper), abs(lower))
    if not math.isfinite(interval) or -interval <= resolution:
        raise ValueError("top two Kramers pairs are degenerate or numerically unresolved")
    return upper, interval


def lambda_from_top_pair(spectrum, tilde_lambda):
    """lambda_F = epsilon_top + tilde_lambda*(epsilon_next - epsilon_top), MeV.

    The denominator is negative. The pair labels refer to sorted
    single-particle energies, not magnetic projections or BCS energies.
    No clipping to the interval [0,1] is performed.
    """
    tilde = _finite_real(tilde_lambda, "tilde_lambda")
    upper, interval = _top_pair(spectrum)
    return _finite_real(upper + tilde * interval, "derived lambda_F_MeV")


def tilde_lambda_from_top_pair(spectrum, lambda_F_MeV):
    """Inverse of lambda_from_top_pair; undefined for a collapsed top interval."""
    lam = _finite_real(lambda_F_MeV, "lambda_F_MeV")
    upper, interval = _top_pair(spectrum)
    return _finite_real((lam - upper) / interval, "derived tilde_lambda")


def irrotational_moments(J0_hbar2_per_MeV, gamma_deg):
    """Return (4/3) J0 sin²(gamma-2*pi*k/3), k=1,2,3, without axis sorting.

    J0 must be positive. Exact axial angles (multiples of 60 degrees) are
    rejected because one moment is mathematically zero; round-off sin(pi)
    must not disguise a singular rotor as strictly positive. Nearby angles
    are supported if all computed moments remain finite and positive.
    """
    j0 = _finite_real(J0_hbar2_per_MeV, "J0_hbar2_per_MeV")
    degrees = _finite_real(gamma_deg, "gamma_deg")
    if j0 <= 0:
        raise ValueError("J0_hbar2_per_MeV must be strictly positive")
    if math.remainder(degrees, 60.0) == 0:
        raise ValueError("axial irrotational limit has a zero inertia; strictly positive inertias are required")
    gamma = _angle(degrees)
    return _inertias(tuple((4 / 3) * j0 * math.sin(gamma - 2 * math.pi * k / 3) ** 2
                           for k in (1, 2, 3)))


def solve(two_I, params):
    """Solve the positive-energy paired rotor in its D2-invariant subspace.

    Return RotorSolution, without energy shifts, fitting, or physical labels.
    Delta must be positive. Large/near-singular numerical scales that produce
    non-finite matrices raise ValueError; a failed eigensolver is not hidden.
    """
    two_I = _half_integer(two_I, "two_I")
    if not isinstance(params, PairedRotorParameters):
        raise TypeError("params must be PairedRotorParameters")
    sp = single_particle_spectrum(params.two_j, params.C_MeV, params.gamma_deg)
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            xi = sp.eigenvalues_MeV - params.lambda_F_MeV
            qp_energy = np.hypot(xi, params.Delta_MeV)
            _require_finite(qp_energy, "quasiparticle energies")
            u = np.sqrt(np.clip((1 + xi / qp_energy) / 2, 0, 1))
            v = np.sqrt(np.clip((1 - xi / qp_energy) / 2, 0, 1))
            s = sp.eigenvectors
            umat = (s * u) @ s.conj().T
            vmat = (s * v) @ s.conj().T
            emat = (s * qp_energy) @ s.conj().T
            norm = umat @ umat + vmat @ vmat
            body = list(_spin_matrices(two_I))
            body[1] *= -1
            particle = _spin_matrices(params.two_j)
            identity_I = np.eye(two_I + 1)
            h = np.kron(identity_I, emat)
            # Factorized evaluation of U Hrot U + V Hrot V. In particular,
            # transform j_k**2 itself; squaring the transformed j_k is wrong.
            for ik, jk, inertia in zip(body, particle, params.inertias_hbar2_per_MeV):
                coefficient = _finite_real(0.5 / inertia, "derived rotational coefficient")
                paired_j = umat @ jk @ umat + vmat @ jk @ vmat
                jj = jk @ jk
                paired_jj = umat @ jj @ umat + vmat @ jj @ vmat
                h += coefficient * (
                    np.kron(ik @ ik, norm)
                    + np.kron(identity_I, paired_jj)
                    - 2 * np.kron(ik, paired_j)
                )
            _require_finite(h, "positive-energy Hamiltonian")
            p = d2_embedding(two_I, params.two_j)
            reduced = p.conj().T @ h @ p
            hermiticity = float(np.max(abs(h - h.conj().T)))
            leakage = float(np.max(abs(h @ p - p @ reduced)))
            energies, vectors = np.linalg.eigh(reduced)
            _require_finite(energies, "rotor eigenvalues")
            x = np.vstack((np.kron(identity_I, umat) @ p,
                           np.kron(identity_I, vmat) @ p))
    except FloatingPointError as exc:
        raise ValueError("inputs overflow the supported paired-rotor numerical scale") from exc
    return RotorSolution(
        two_I=two_I, parameters=params, single_particle=sp,
        eigenvalues_MeV=_readonly(energies), eigenvectors=_readonly(vectors),
        product_embedding=p, positive_energy_embedding=_readonly(x),
        d2_basis_twice_K_Omega=_d2_keys(two_I, params.two_j),
        hamiltonian_MeV=_readonly(reduced), hamiltonian_product_MeV=_readonly(h),
        quasiparticle_energies_MeV=_readonly(qp_energy), u=_readonly(u), v=_readonly(v),
        hermiticity_error_MeV=hermiticity, d2_leakage_MeV=leakage,
    )
