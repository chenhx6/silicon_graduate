"""Dimensionless lab-tensor matrix elements for paired_single_j_rotor.

CONVENTIONS
The normalized unsymmetrized rotational basis is
sqrt((2I+1)/(8*pi**2)) D^{I*}_{MK}(Euler) |j,Omega>. Product coordinates
match RotorSolution: K and Omega ascend, with Omega varying fastest.
Use the Condon--Shortley CG convention and Wigner--Eckart normalization

 <If Mf|T_{L mu}|Ii Mi> =
   CG(Ii Mi,L mu|If Mf) <If||T_L||Ii> / sqrt(2If+1).

For T_{L mu}=sum_nu D^{L*}_{mu nu} t_{L nu}, the product-space RME is

 T_product[(Kf,Of),(Ki,Oi)] =
   sqrt(2Ii+1) sum_nu CG(Ii Ki,L nu|If Kf) t_nu[Of,Oi].

The two operators supplied here are:
* collective_quadrupole: rank 2, intrinsic identity, q20=cos(gamma),
  q2,+/-2=sin(gamma)/sqrt(2), q2,+/-1=0. Thus sum_nu |q2nu|**2=1.
  This collective tensor is distinct from the single-j Q_j potential.
* particle_j: rank 1, j0=jz, j+1=-(jx+i*jy)/sqrt(2),
  j-1=(jx-i*jy)/sqrt(2), with angular momentum measured in hbar units.

Both have identical particle and time-reversed-hole blocks in the
RotorSolution Nambu convention. The collective operator acts on the core;
particle j is time-odd. Consequently the positive-energy projection uses
U_f T U_i + V_f T V_i for BOTH operators. It does not use the minus
coherence factor of a time-even single-particle electric tensor.

With P the D2/product embedding, X the positive-energy embedding and V the
rotor eigenvectors, the explicitly retained operations are
  bare_D2 = P_f^dagger T_product P_i,
  paired_D2 = X_f^dagger diag(T_product,T_product) X_i,
  RME = V_f^dagger paired_D2 V_i,
  unit_B = |RME|**2 / (2Ii+1).
The two solutions MUST have equal parameter values, including shape,
inertias, C, lambda and gap. Even separately equivalent axis conventions
are not silently joined. Eigenvectors may be rephased consistently.

LIMITS
These are dimensionless unit tensors. There is no Q0, effective charge,
g factor, mu_N, E2/M1 prefactor, photon-energy weighting, internal
conversion, branching normalization, or mixing-ratio sign assignment.
particle_j is NOT the complete magnetic moment or a complete M1 operator.
For a convention such as g_R I + (g_j-g_R) j, the diagonal Delta I=0
g_R I contribution is still REQUIRED externally; its reduced matrix
element is g_R sqrt(I(I+1)(2I+1)) delta_alpha_f,alpha_i.

Upward, downward and diagonal matrix elements are all returned. Unit B
is not a photon branch probability. The rotor's eta-discarding
approximation is inherited; this module supplies no physical validation,
source-model replay, or mode labels. It performs no file I/O.

CG implementation: the Racah factorial sum is evaluated as an exact
Fraction, including cancellations. Only the final signed square root is
converted to float. No legacy analyzer or optional symbolic package is
imported. Tests independently construct coupled angular-momentum states
by highest-weight diagonalization and lowering.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import math
from numbers import Integral

import numpy as np

if __package__:
    from .paired_single_j_rotor import RotorSolution
else:
    from paired_single_j_rotor import RotorSolution

__all__ = [
    "ReducedTensorResult",
    "UnitEMResult",
    "clebsch_gordan",
    "collective_quadrupole",
    "particle_j",
    "unit_em",
]


@lru_cache(maxsize=512)
def _factorial(n):
    return math.factorial(n)


@lru_cache(maxsize=4096)
def _cg_racah(j1, m1, j2, m2, total, projection):
    """All arguments are validated doubled integers."""
    if (
        m1 + m2 != projection
        or abs(m1) > j1 or abs(m2) > j2 or abs(projection) > total
        or (j1 - m1) % 2 or (j2 - m2) % 2 or (total - projection) % 2
        or total < abs(j1 - j2) or total > j1 + j2
        or (j1 + j2 - total) % 2
    ):
        return 0.0
    a = (total + j1 - j2) // 2
    b = (total - j1 + j2) // 2
    c = (j1 + j2 - total) // 2
    d = (j1 + j2 + total) // 2 + 1
    j1_minus_m1 = (j1 - m1) // 2
    j2_plus_m2 = (j2 + m2) // 2
    total_minus_j2_plus_m1 = (total - j2 + m1) // 2
    total_minus_j1_minus_m2 = (total - j1 - m2) // 2
    low = max(0, -total_minus_j2_plus_m1, -total_minus_j1_minus_m2)
    high = min(c, j1_minus_m1, j2_plus_m2)
    summed = Fraction(0)
    for z in range(low, high + 1):
        denominator = math.prod(_factorial(n) for n in (
            z, c - z, j1_minus_m1 - z, j2_plus_m2 - z,
            total_minus_j2_plus_m1 + z, total_minus_j1_minus_m2 + z,
        ))
        summed += Fraction((-1) ** z, denominator)
    if not summed:
        return 0.0
    numerator = (total + 1) * math.prod(_factorial(n) for n in (
        a, b, c, (total + projection) // 2, (total - projection) // 2,
        (j1 + m1) // 2, j1_minus_m1, j2_plus_m2, (j2 - m2) // 2,
    ))
    squared = Fraction(numerator, _factorial(d)) * summed * summed
    return math.copysign(math.sqrt(float(squared)), 1 if summed > 0 else -1)


def clebsch_gordan(two_j1, two_m1, two_j2, two_m2, two_J, two_M):
    """Condon--Shortley CG(j1 m1,j2 m2|J M), using six doubled integers.

    Non-integer inputs, booleans and negative j1/j2/J raise ValueError.
    Forbidden triangle/projection/parity combinations return exactly zero.
    Integer and half-integer angular momenta are both supported.
    """
    args = (two_j1, two_m1, two_j2, two_m2, two_J, two_M)
    if any(isinstance(x, bool) or not isinstance(x, Integral) for x in args):
        raise ValueError("CG arguments must be doubled integers, not floats or booleans")
    values = tuple(int(x) for x in args)
    if any(values[index] < 0 for index in (0, 2, 4)):
        raise ValueError("CG angular momenta j1, j2 and J must be nonnegative")
    return _cg_racah(*values)


@dataclass(frozen=True)
class ReducedTensorResult:
    """A final-state-by-initial-state unit-tensor matrix, with read-only arrays.

    product_rme is in the unsymmetrized product coordinates.
    bare_d2_rme uses only P; d2_rme additionally uses the positive-energy
    Nambu projection. rme and unit_B refer to the supplied eigenstate
    columns. There are no physical electromagnetic units or decay cuts.
    """

    operator: str
    rank: int
    two_I_initial: int
    two_I_final: int
    product_rme: np.ndarray
    bare_d2_rme: np.ndarray
    d2_rme: np.ndarray
    rme: np.ndarray
    unit_B: np.ndarray


@dataclass(frozen=True)
class UnitEMResult:
    """The two unit operators, without combining their physical scales."""

    collective_quadrupole: ReducedTensorResult
    particle_j: ReducedTensorResult


def _readonly(array):
    array.setflags(write=False)
    return array


def _matrix(value, shape, name):
    try:
        array = np.asarray(value, dtype=complex)
    except (ValueError, TypeError) as exc:
        raise ValueError(f"{name} must be a finite numeric matrix") from exc
    if array.shape != shape or not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must have shape {shape} with finite entries")
    return array


def _solution_coordinates(solution):
    if not isinstance(solution, RotorSolution):
        raise TypeError("initial and final must be RotorSolution objects")
    two_I = solution.two_I
    if isinstance(two_I, bool) or not isinstance(two_I, Integral) or two_I <= 0 or two_I % 2 != 1:
        raise ValueError("RotorSolution.two_I must be a positive odd integer")
    dim = (two_I + 1) * (solution.parameters.two_j + 1)
    reduced_dim = dim // 4
    p = _matrix(solution.product_embedding, (dim, reduced_dim), "product_embedding")
    x = _matrix(solution.positive_energy_embedding, (2 * dim, reduced_dim), "positive_energy_embedding")
    v = _matrix(solution.eigenvectors, (reduced_dim, reduced_dim), "eigenvectors")
    for array, name in ((p, "product_embedding"), (x, "positive_energy_embedding"), (v, "eigenvectors")):
        if not np.allclose(array.conj().T @ array, np.eye(reduced_dim), atol=2e-10, rtol=0):
            raise ValueError(f"{name} must have orthonormal columns")
    return p, x, v


def _pair_coordinates(initial, final):
    if not isinstance(initial, RotorSolution) or not isinstance(final, RotorSolution):
        raise TypeError("initial and final must be RotorSolution objects")
    if initial.parameters != final.parameters:
        raise ValueError("initial and final must have identical rotor parameter values and axis conventions")
    return _solution_coordinates(initial), _solution_coordinates(final)


def _collective_components(parameters):
    gamma = math.radians(math.remainder(parameters.gamma_deg, 360.0))
    identity = np.eye(parameters.two_j + 1)
    return {
        0: math.cos(gamma) * identity,
        -2: math.sin(gamma) / math.sqrt(2) * identity,
        2: math.sin(gamma) / math.sqrt(2) * identity,
    }


def _particle_components(two_j):
    j = two_j / 2
    projections = np.arange(-two_j, two_j + 1, 2) / 2
    raising = np.zeros((two_j + 1, two_j + 1), complex)
    for index, m in enumerate(projections[:-1]):
        raising[index + 1, index] = math.sqrt((j - m) * (j + m + 1))
    return {
        0: np.diag(projections).astype(complex),
        1: -raising / math.sqrt(2),
        -1: raising.conj().T / math.sqrt(2),
    }


def _product_rme(two_Ii, two_If, two_j, rank, components):
    n = two_j + 1
    result = np.zeros(((two_If + 1) * n, (two_Ii + 1) * n), complex)
    if abs(two_If - two_Ii) > 2 * rank or two_If + two_Ii < 2 * rank:
        return result
    factor = math.sqrt(two_Ii + 1)
    for col, ki in enumerate(range(-two_Ii, two_Ii + 1, 2)):
        for nu, intrinsic in components.items():
            kf = ki + 2 * nu
            if abs(kf) > two_If:
                continue
            row = (kf + two_If) // 2
            cg = clebsch_gordan(two_Ii, ki, 2 * rank, 2 * nu, two_If, kf)
            result[row * n:(row + 1) * n, col * n:(col + 1) * n] += factor * cg * intrinsic
    return result


def _evaluate(initial, final, coordinates, rank, components, name):
    (pi, xi, vi), (pf, xf, vf) = coordinates
    product = _product_rme(initial.two_I, final.two_I, initial.parameters.two_j, rank, components)
    bare_d2 = pf.conj().T @ product @ pi
    di, df = pi.shape[0], pf.shape[0]
    # X already contains the D2 embedding: do not apply P a second time.
    paired_d2 = (xf[:df].conj().T @ product @ xi[:di]
                 + xf[df:].conj().T @ product @ xi[di:])
    rme = vf.conj().T @ paired_d2 @ vi
    unit_B = np.abs(rme) ** 2 / (initial.two_I + 1)
    if not np.all(np.isfinite(rme)) or not np.all(np.isfinite(unit_B)):
        raise ValueError("non-finite reduced matrix elements or unit strengths")
    return ReducedTensorResult(
        name, rank, initial.two_I, final.two_I, _readonly(product),
        _readonly(bare_d2), _readonly(paired_d2), _readonly(rme), _readonly(unit_B),
    )


def collective_quadrupole(initial, final):
    """Dimensionless collective quadrupole RMEs and unit B; no Q0 or E2 prefactor."""
    coordinates = _pair_coordinates(initial, final)
    return _evaluate(initial, final, coordinates, 2, _collective_components(initial.parameters),
                     "collective_quadrupole")


def particle_j(initial, final):
    """Particle-j RMEs and unit B; NOT complete M1, including on a diagonal."""
    coordinates = _pair_coordinates(initial, final)
    return _evaluate(initial, final, coordinates, 1, _particle_components(initial.parameters.two_j),
                     "particle_j")


def unit_em(initial, final):
    """Return both unit tensors for equal-parameter solutions, without physical scales."""
    coordinates = _pair_coordinates(initial, final)
    core = _evaluate(initial, final, coordinates, 2, _collective_components(initial.parameters),
                     "collective_quadrupole")
    angular = _evaluate(initial, final, coordinates, 1, _particle_components(initial.parameters.two_j),
                        "particle_j")
    return UnitEMResult(core, angular)
