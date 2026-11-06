"""Explicit single-j sd-IBFM kernel; not a PBOS clone or a nuclear fit.

Space and conventions
---------------------
Normalized boson occupation states have mode order (s,d_-2,d_-1,d_0,d_1,d_2),
fixed n_b and no boson truncation. One fermion has ascending m=-j,...,+j;
the full product index is boson_index*(2j+1)+fermion_index. Angular momenta
are in hbar units. n_b/core identity is entirely a caller input.

Condon--Shortley CGs, tilde b_lm=(-1)**(l-m) b_l,-m and
tilde a_jm=(-1)**(j-m) a_j,-m are used. In particular
 [a^dagger x tilde a]^0 = -n_f/sqrt(2j+1) for half-integer j.
The Wigner--Eckart convention is
 <Jf Mf|T_kq|Ji Mi> = CG(Ji Mi,k q|Jf Mf)*<Jf||T_k||Ji>/sqrt(2Jf+1).

H_B = eps_d n_d + kappa Q_chi . Q_chi is an ordinary operator product
(including its one-body contractions), with no 1/n_b scaling. H_BF uses
Nomura et al., PRC 96, 014304 (2017), Eqs. (3)-(6), restricted to j=j'=j'':
 Gamma_jj = Gamma0*(1-2*v2)*Q_jj
 Lambda_jj^j = -2*Lambda0*sqrt(5/(2j+1))*(2*u*v*Q_jj)**2
 A_j = -A0*sqrt(2j+1).
Q_jj is a caller-supplied SIGNED reduced matrix element of Y^2. There is
no guessed radial factor. u,v are real nonnegative square roots.

The bare exchange X is
 : [[d^dagger x tilde a]^j x [a^dagger x tilde d]^j]^0 : .
It is expanded directly into -d^dagger a^dagger a d, including all CG/tilde
phases. No a a^dagger contraction is retained. Hence the monopole term
is exactly A0*n_d for n_f=1. The single-j H_F common shift is dropped.

Only fixed-M Hamiltonians are made dense; all full-space operators are
sparse. solve() retains the COMPLETE chosen M block. J^2 diagonalizes
numerically degenerate ENERGY eigenspaces, followed by independent H,
J^2, integer-spin and orthonormality residual checks. Degeneracy tolerances
are declared in caller energy units. No matrix is silently symmetrized.
Multiplicity within the same E,J remains arbitrary, not a physical label.

E2 = eB Q_chi_prime - eF*(1-2*v2)*Q_jj*[a^dagger x tilde a]^2/sqrt(5).
magnetic_moment() is mu=gB L+gj j. m1() is sqrt(3/(4*pi))*mu.
These are distinct operators. Caller units are retained. RME strengths
are |<Jf||T||Ji>|^2/(2Ji+1), not photon rates, delta or band assignments.
Both EM operators use the SAME supplied eigenvectors and phases.
core_quadrupole(), fermion_unit_tensor(), core_L() and particle_j()
also expose the separate unit tensors for external scale calibration.

M=1/2,q=0 normally suffices for odd-state rank-1 and rank-2 RMEs. An allowed
transition with zero CG denominator raises, or is explicitly NaN-masked;
triangle-forbidden selection zeros are separately exposed. Independent
M-block solves have independent eigenvector phases; this API deliberately
requires same-M,q=0 solutions for RME extraction. Full tensor components
and block bases are exposed for externally phase-linked calculations.

Dependencies: numpy, scipy, and ONLY the pure clebsch_gordan helper from
the frozen paired_single_j_em module (no legacy analyzer). This module
does no file I/O, fitting, BLAS-thread reconfiguration, or source replay.
Run with OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1.
"""

from dataclasses import dataclass
from functools import cached_property, lru_cache
import math
from numbers import Integral, Real
from types import MappingProxyType

import numpy as np
from scipy import linalg, sparse

if __package__:
    from .paired_single_j_em import clebsch_gordan
else:
    from paired_single_j_em import clebsch_gordan

__all__ = [
    "IBFMParameters", "CoreParameters", "BosonSpace", "fermion_tensor",
    "spin_components", "BlockBasis", "TensorOperator", "Spectrum",
    "ReducedTensor", "CoreE2Calibration", "IBFMKernel", "BosonCore",
    "diagonalize_scalar", "reduced_matrix_elements", "transition_rme",
    "calibrate_core_e2", "ZeroClebschGordanError", "max_abs",
]

MODE_M = (0, -2, -1, 0, 1, 2)


def _integer(value, name, minimum=None):
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise ValueError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be >= {minimum}")
    return int(value)


def _real(value, name):
    if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value):
        raise ValueError(f"{name} must be finite and real")
    return float(value)


def _half_integer(two_j):
    two_j = _integer(two_j, "two_j", 1)
    if two_j % 2 != 1:
        raise ValueError("two_j must be odd (one half-integer fermion)")
    return two_j


def _readonly(value):
    value = np.asarray(value)
    value.setflags(write=False)
    return value


def max_abs(matrix):
    """Maximum absolute entry, including for an empty sparse matrix."""
    data = matrix.data if sparse.issparse(matrix) else np.asarray(matrix)
    return float(np.max(np.abs(data))) if data.size else 0.0


def _csr(matrix):
    result = sparse.csr_matrix(matrix)
    result.sum_duplicates()
    result.eliminate_zeros()
    return result


def _hermitian(matrix, name, tolerance=2e-12):
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError(f"{name} must be square")
    data = matrix.data if sparse.issparse(matrix) else np.asarray(matrix)
    if not np.all(np.isfinite(data)):
        raise ValueError(f"{name} contains non-finite entries")
    error = max_abs(matrix - matrix.conj().T)
    if error > tolerance * max(1.0, max_abs(matrix)):
        raise ValueError(f"{name} is not Hermitian: max residual {error:.6g}")
    return error


@dataclass(frozen=True)
class CoreParameters:
    n_b: int
    eps_d: float
    kappa: float
    chi: float

    def __post_init__(self):
        _integer(self.n_b, "n_b", 0)
        for name in ("eps_d", "kappa", "chi"):
            _real(getattr(self, name), name)


@dataclass(frozen=True)
class IBFMParameters:
    n_b: int
    two_j: int
    eps_d: float
    kappa: float
    chi: float
    v2: float
    Q_jj: float
    Gamma0: float = 0.0
    Lambda0: float = 0.0
    A0: float = 0.0

    def __post_init__(self):
        _integer(self.n_b, "n_b", 0)
        _half_integer(self.two_j)
        for name in ("eps_d", "kappa", "chi", "v2", "Q_jj", "Gamma0", "Lambda0", "A0"):
            _real(getattr(self, name), name)
        if not 0 <= self.v2 <= 1:
            raise ValueError("v2 must be an occupation probability in [0,1]")

    @property
    def gamma_jj(self):
        return (1 - 2 * self.v2) * self.Q_jj

    @property
    def beta_jj(self):
        return 2 * math.sqrt(self.v2 * (1 - self.v2)) * self.Q_jj

    @property
    def exchange_coefficient(self):
        return -2 * self.Lambda0 * math.sqrt(5 / (self.two_j + 1)) * self.beta_jj**2


def _compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in _compositions(total - first, slots - 1):
                yield (first,) + rest


class BosonSpace:
    """Full normalized fixed-N sd occupation basis, in lexicographic order.

    Returned sparse matrices are cached; callers must not mutate them.
    bilinear(a,b) is b_a^dagger b_b, not two independent projected ladders.
    """

    def __init__(self, n_b):
        self.n_b = _integer(n_b, "n_b", 0)
        self.occupations = tuple(_compositions(self.n_b, 6))
        self.index = MappingProxyType({n: i for i, n in enumerate(self.occupations)})
        self.dimension = len(self.occupations)
        self.m = _readonly(np.array(self.occupations, dtype=int) @ np.array(MODE_M))

    @lru_cache(maxsize=None)
    def bilinear(self, create, annihilate):
        create = _integer(create, "create", 0)
        annihilate = _integer(annihilate, "annihilate", 0)
        if create >= 6 or annihilate >= 6:
            raise ValueError("boson mode indices must be 0..5")
        rows, cols, values = [], [], []
        for col, occ in enumerate(self.occupations):
            if not occ[annihilate]:
                continue
            target = list(occ)
            factor = math.sqrt(target[annihilate])
            target[annihilate] -= 1
            factor *= math.sqrt(target[create] + 1)
            target[create] += 1
            rows.append(self.index[tuple(target)])
            cols.append(col)
            values.append(factor)
        return sparse.csr_matrix((values, (rows, cols)), shape=(self.dimension,) * 2)

    @cached_property
    def identity(self):
        return sparse.eye(self.dimension, format="csr")

    @cached_property
    def n_d(self):
        return sparse.diags([sum(n[1:]) for n in self.occupations], format="csr", dtype=float)

    @lru_cache(maxsize=None)
    def d_tensor(self, rank, q):
        rank, q = _integer(rank, "rank", 0), _integer(q, "q")
        if abs(q) > rank:
            raise ValueError("|q| must not exceed rank")
        result = sparse.csr_matrix((self.dimension,) * 2)
        for b in range(-2, 3):
            a = b + q
            if -2 <= a <= 2:
                weight = (-1.0)**b * clebsch_gordan(4, 2*a, 4, -2*b, 2*rank, 2*q)
                if weight:
                    result += weight * self.bilinear(a + 3, b + 3)
        return _csr(result)

    def quadrupole(self, chi):
        chi = _real(chi, "chi")
        return {
            q: _csr((-1.0)**q * self.bilinear(0, 3-q)
                    + self.bilinear(3+q, 0) + chi * self.d_tensor(2, q))
            for q in range(-2, 3)
        }

    @cached_property
    def L_plus(self):
        result = sparse.csr_matrix((self.dimension,) * 2)
        for m in range(-2, 2):
            result += math.sqrt((2-m)*(3+m)) * self.bilinear(m+4, m+3)
        return _csr(result)

    @cached_property
    def angular(self):
        return {0: sparse.diags(self.m, format="csr", dtype=float),
                1: -self.L_plus / math.sqrt(2),
                -1: self.L_plus.T / math.sqrt(2)}

    @cached_property
    def L2(self):
        return _csr(sparse.diags(self.m * (self.m + 1), format="csr", dtype=float)
                    + self.L_plus.T @ self.L_plus)

    def hamiltonian(self, eps_d, kappa, chi):
        eps_d, kappa = _real(eps_d, "eps_d"), _real(kappa, "kappa")
        q = self.quadrupole(chi)
        qq = sum(((-1.0)**m * (q[m] @ q[-m]) for m in range(-2, 3)),
                 sparse.csr_matrix((self.dimension,) * 2))
        return _csr(eps_d * self.n_d + kappa * qq)


def fermion_tensor(two_j, rank, q):
    """NF=1 matrix of [a^dagger_j x tilde a_j]^rank_q; no Q_jj/BCS factors."""
    two_j = _half_integer(two_j)
    rank, q = _integer(rank, "rank", 0), _integer(q, "q")
    if abs(q) > rank:
        raise ValueError("|q| must not exceed rank")
    rows, cols, values = [], [], []
    for col, m in enumerate(range(-two_j, two_j + 1, 2)):
        mf = m + 2*q
        if abs(mf) <= two_j:
            value = (-1)**((two_j+m)//2) * clebsch_gordan(
                two_j, mf, two_j, -m, 2*rank, 2*q)
            if value:
                rows.append((mf + two_j)//2)
                cols.append(col)
                values.append(value)
    return sparse.csr_matrix((values, (rows, cols)), shape=(two_j+1,) * 2)


def spin_components(two_j):
    """Ordinary particle angular momentum, not magnetic or BCS-attenuated."""
    two_j = _half_integer(two_j)
    j = two_j/2
    m = np.arange(-two_j, two_j+1, 2)/2
    plus = sparse.diags(np.sqrt((j-m[:-1])*(j+m[:-1]+1)), -1,
                        shape=(two_j+1,) * 2, format="csr")
    return {0: sparse.diags(m, format="csr"), 1: -plus/math.sqrt(2),
            -1: plus.T/math.sqrt(2)}


@dataclass(frozen=True)
class BlockBasis:
    n_b: int
    two_j: object                 # None for the even boson-only core
    two_M: object                 # None for the complete product basis
    full_indices: np.ndarray
    boson_occupations: np.ndarray
    two_m_fermion: np.ndarray
    full_dimension: int

    @property
    def dimension(self):
        return len(self.full_indices)

    def restrict(self, operator, final=None):
        final = self if final is None else final
        if (self.n_b, self.two_j, self.full_dimension) != (
                final.n_b, final.two_j, final.full_dimension):
            raise ValueError("incompatible product spaces")
        if operator.shape != (self.full_dimension,) * 2:
            raise ValueError("operator has wrong full-space dimensions")
        return sparse.csr_matrix(operator)[final.full_indices][:, self.full_indices].tocsr()


def _basis(bosons, two_j, two_M):
    nf = 1 if two_j is None else two_j + 1
    mf = np.zeros(1, dtype=int) if two_j is None else np.arange(-two_j, two_j+1, 2)
    total_m = (2*bosons.m[:, None] + mf[None, :]).ravel()
    if two_M is not None:
        two_M = _integer(two_M, "two_M")
        if two_M % 2 != (0 if two_j is None else 1):
            raise ValueError("two_M parity is incompatible with this space")
    indices = np.arange(len(total_m)) if two_M is None else np.flatnonzero(total_m == two_M)
    if not len(indices):
        raise ValueError("requested M block is empty")
    return BlockBasis(
        bosons.n_b, two_j, two_M, _readonly(indices),
        _readonly(np.asarray(bosons.occupations, dtype=int)[indices//nf]),
        _readonly(mf[indices % nf]), len(total_m),
    )


@dataclass(frozen=True)
class TensorOperator:
    name: str
    rank: int
    components: object
    model_key: object

    def block(self, initial, final=None, q=0):
        return initial.restrict(self.components[q], final)


@dataclass(frozen=True)
class Spectrum:
    energies: np.ndarray
    two_J: np.ndarray
    vectors: np.ndarray
    basis: BlockBasis
    hamiltonian: object
    J2: object
    model_key: object
    degeneracy_groups: tuple
    diagnostics: object

    def indices_for_J(self, two_J):
        return np.flatnonzero(self.two_J == _integer(two_J, "two_J", 0))


def diagonalize_scalar(hamiltonian, J2, basis, model_key=None, *,
                       degeneracy_atol=1e-12, degeneracy_rtol=1e-12,
                       residual_tolerance=2e-10):
    """Complete fixed-M diagonalization and J^2 resolution of energy degeneracy.

    No averaging with adjoints occurs. Tolerances are exposed: the energy
    grouping uses absolute caller energy units plus a relative term. The
    acceptance checks use matrix infinity-norm scales. Same-(E,J) vectors
    can remain arbitrary. A near-degeneracy rotation that spoils H residuals
    is rejected, not relabeled as an eigenstate.
    """
    if not isinstance(basis, BlockBasis) or basis.two_M is None:
        raise ValueError("diagonalization requires a fixed-M BlockBasis")
    for x, name in ((degeneracy_atol, "degeneracy_atol"),
                    (degeneracy_rtol, "degeneracy_rtol"),
                    (residual_tolerance, "residual_tolerance")):
        if _real(x, name) < 0:
            raise ValueError(f"{name} must be nonnegative")
    if residual_tolerance == 0:
        raise ValueError("residual_tolerance must be positive")
    h, j2 = _csr(hamiltonian), _csr(J2)
    shape = (basis.dimension,) * 2
    if h.shape != shape or j2.shape != shape:
        raise ValueError("scalar matrices must match basis dimensions")
    herm_h, herm_j = _hermitian(h, "H"), _hermitian(j2, "J2")
    h_scale = max(1.0, float(np.max(np.asarray(abs(h).sum(axis=1)))))
    j_scale = max(1.0, float(np.max(np.asarray(abs(j2).sum(axis=1)))))
    comm = max_abs(h @ j2 - j2 @ h)
    if comm > residual_tolerance * h_scale * j_scale:
        raise ValueError(f"H does not commute with J2: {comm:.6g}")
    energies, vectors = linalg.eigh(h.toarray(), driver="evd")
    groups, start = [], 0
    while start < len(energies):
        end = start + 1
        while end < len(energies):
            tol = degeneracy_atol + degeneracy_rtol * max(abs(energies[start]), abs(energies[end]))
            if energies[end] - energies[start] > tol:
                break
            end += 1
        sub = vectors[:, start:end]
        small_j2 = sub.conj().T @ (j2 @ sub)
        _hermitian(small_j2, "J2 in energy eigenspace")
        _, rotate = linalg.eigh(small_j2, driver="evd")
        vectors[:, start:end] = sub @ rotate
        groups.append(tuple(range(start, end)))
        start = end
    # Fix one phase per eigenvector ONCE; all observables reuse these columns.
    for i in range(vectors.shape[1]):
        pivot = vectors[np.argmax(np.abs(vectors[:, i])), i]
        vectors[:, i] *= np.conj(pivot) / abs(pivot)
    hv, jv = h @ vectors, j2 @ vectors
    energies = np.real(np.sum(vectors.conj() * hv, axis=0))
    j_eigen = np.real(np.sum(vectors.conj() * jv, axis=0))
    if np.min(j_eigen) < -residual_tolerance*j_scale:
        raise ValueError("J2 has negative angular eigenvalues")
    two_J = np.rint(np.sqrt(1 + 4*np.maximum(j_eigen, 0)) - 1).astype(int)
    target_j2 = two_J*(two_J+2)/4
    h_res = np.linalg.norm(hv - vectors*energies, axis=0)
    j_res = np.linalg.norm(jv - vectors*target_j2, axis=0)
    orth = max_abs(vectors.conj().T @ vectors - np.eye(len(energies)))
    parity = 0 if basis.two_j is None else 1
    if (np.any(two_J % 2 != parity) or np.any(two_J < abs(basis.two_M))
            or max_abs(j_eigen-target_j2) > residual_tolerance*j_scale
            or max_abs(j_res) > residual_tolerance*j_scale):
        raise ValueError("J2 resolution failed; cannot assign definite total J")
    if max_abs(h_res) > residual_tolerance*h_scale or orth > residual_tolerance:
        raise ValueError("eigensystem residual failed after degeneracy resolution")
    diagnostics = MappingProxyType(dict(
        hermiticity_H_max=herm_h, hermiticity_J2_max=herm_j,
        commutator_H_J2_max=comm, H_inf_scale=h_scale, J2_inf_scale=j_scale,
        energy_residual_max=max_abs(h_res), J2_residual_max=max_abs(j_res),
        orthonormality_max=orth, degeneracy_atol=degeneracy_atol,
        degeneracy_rtol=degeneracy_rtol, residual_tolerance=residual_tolerance,
    ))
    return Spectrum(_readonly(energies), _readonly(two_J), _readonly(vectors),
                    basis, h, j2, model_key, tuple(groups), diagnostics)


class BosonCore:
    """Even core; solve M=0 to retain one state of every integer-J multiplet."""

    def __init__(self, parameters):
        if not isinstance(parameters, CoreParameters):
            raise TypeError("parameters must be CoreParameters")
        self.parameters = parameters
        self.bosons = BosonSpace(parameters.n_b)
        self.model_key = ("core", parameters)

    @cached_property
    def hamiltonian(self):
        p = self.parameters
        return self.bosons.hamiltonian(p.eps_d, p.kappa, p.chi)

    @lru_cache(maxsize=None)
    def basis(self, two_M=0):
        return _basis(self.bosons, None, two_M)

    def solve(self, two_M=0, **options):
        basis = self.basis(two_M)
        return diagonalize_scalar(basis.restrict(self.hamiltonian),
                                  basis.restrict(self.bosons.L2),
                                  basis, self.model_key, **options)

    def e2(self, eB, chi_prime):
        eB = _real(eB, "eB")
        return TensorOperator("core E2", 2, MappingProxyType({
            q: eB*t for q, t in self.bosons.quadrupole(chi_prime).items()}),
            self.model_key)


class IBFMKernel:
    """New single-j kernel. Sparse full-space matrices are read-only by contract."""

    def __init__(self, parameters):
        if not isinstance(parameters, IBFMParameters):
            raise TypeError("parameters must be IBFMParameters")
        self.parameters = parameters
        self.bosons = BosonSpace(parameters.n_b)
        self.model_key = ("single-j-ibfm", parameters)
        self.fermion_identity = sparse.eye(parameters.two_j+1, format="csr")
        self.particle_angular = spin_components(parameters.two_j)

    @property
    def dimension(self):
        return self.bosons.dimension * (self.parameters.two_j+1)

    @lru_cache(maxsize=None)
    def basis(self, two_M=1):
        return _basis(self.bosons, self.parameters.two_j, two_M)

    def _kron(self, boson, fermion):
        return sparse.kron(boson, fermion, format="csr")

    @cached_property
    def angular(self):
        return {q: self._kron(self.bosons.angular[q], self.fermion_identity)
                + self._kron(self.bosons.identity, self.particle_angular[q])
                for q in (-1, 0, 1)}

    @cached_property
    def J2(self):
        z = self.angular[0]
        plus = -math.sqrt(2)*self.angular[1]
        return _csr(z @ z + z + plus.conj().T @ plus)

    @cached_property
    def bare_exchange(self):
        """Colon-ordered scalar, WITHOUT the Lambda_jj^j prefactor.

        b is the annihilated d projection; mi,mf are twice fermion
        projections. Scalar coupling enforces mf=mi+2*(b-a).
        The first minus sign below is the fermion normal-ordering sign.
        """
        tj = self.parameters.two_j
        result = sparse.csr_matrix((self.dimension,) * 2)
        for a in range(-2, 3):
            for b in range(-2, 3):
                rows, cols, values = [], [], []
                for col, mi in enumerate(range(-tj, tj+1, 2)):
                    mf, mu = mi + 2*(b-a), 2*a-mi
                    if abs(mf) > tj or abs(mu) > tj:
                        continue
                    weight = (-(-1.0)**(((tj+mi)//2)+b)
                              * clebsch_gordan(4, 2*a, tj, -mi, tj, mu)
                              * clebsch_gordan(tj, mf, 4, -2*b, tj, -mu)
                              * clebsch_gordan(tj, mu, tj, -mu, 0, 0))
                    if weight:
                        rows.append((mf+tj)//2)
                        cols.append(col)
                        values.append(weight)
                f = sparse.csr_matrix((values, (rows, cols)), shape=(tj+1,) * 2)
                result += self._kron(self.bosons.bilinear(a+3, b+3), f)
        return _csr(result)

    @cached_property
    def quadrupole_scalar(self):
        """Q_chi . [a^dagger x tilde a]^2, without Gamma_jj."""
        q = self.bosons.quadrupole(self.parameters.chi)
        return _csr(sum(((-1.0)**m * self._kron(
            q[m], fermion_tensor(self.parameters.two_j, 2, -m))
            for m in range(-2, 3)), sparse.csr_matrix((self.dimension,) * 2)))

    @cached_property
    def monopole_scalar(self):
        """-sqrt(2j+1)*n_d*[a^dagger x tilde a]^0; equals n_d at NF=1."""
        tj = self.parameters.two_j
        return -math.sqrt(tj+1)*self._kron(self.bosons.n_d, fermion_tensor(tj, 0, 0))

    @cached_property
    def components(self):
        p = self.parameters
        terms = {
            "boson": self._kron(self.bosons.hamiltonian(p.eps_d, p.kappa, p.chi),
                                self.fermion_identity),
            "quadrupole": p.Gamma0*p.gamma_jj*self.quadrupole_scalar,
            "exchange": p.exchange_coefficient*self.bare_exchange,
            "monopole": p.A0*self.monopole_scalar,
        }
        for name, term in terms.items():
            _hermitian(term, name)
        return MappingProxyType(terms)

    @cached_property
    def hamiltonian(self):
        return _csr(sum(self.components.values(), sparse.csr_matrix((self.dimension,) * 2)))

    def solve(self, two_M=1, **options):
        basis = self.basis(two_M)
        return diagonalize_scalar(basis.restrict(self.hamiltonian),
                                  basis.restrict(self.J2), basis, self.model_key, **options)

    def core_quadrupole(self, chi_prime):
        """Unit core Q_chi_prime in the product space; no eB, no fermion term."""
        return TensorOperator("unit core quadrupole", 2, MappingProxyType({
            q: self._kron(t, self.fermion_identity)
            for q, t in self.bosons.quadrupole(chi_prime).items()}), self.model_key)

    def fermion_unit_tensor(self, rank):
        """[a^dagger x tilde a]^rank in product space, no Q_jj/u/v/charge."""
        rank = _integer(rank, "rank", 0)
        return TensorOperator(f"unit fermion tensor rank {rank}", rank, MappingProxyType({
            q: self._kron(self.bosons.identity, fermion_tensor(self.parameters.two_j, rank, q))
            for q in range(-rank, rank+1)}), self.model_key)

    def particle_j(self):
        """Unit particle angular momentum; neither magnetic moment nor M1."""
        return TensorOperator("unit particle j", 1, MappingProxyType({
            q: self._kron(self.bosons.identity, t)
            for q, t in self.particle_angular.items()}), self.model_key)

    def core_L(self):
        """Unit core angular momentum in the product space; no gB."""
        return TensorOperator("unit core L", 1, MappingProxyType({
            q: self._kron(t, self.fermion_identity)
            for q, t in self.bosons.angular.items()}), self.model_key)

    def e2(self, eB, eF, chi_prime):
        eB, eF = _real(eB, "eB"), _real(eF, "eF")
        b = self.core_quadrupole(chi_prime).components
        f = self.fermion_unit_tensor(2).components
        factor = -eF*self.parameters.gamma_jj/math.sqrt(5)
        return TensorOperator("E2", 2, MappingProxyType({
            q: _csr(eB*b[q] + factor*f[q])
            for q in range(-2, 3)}), self.model_key)

    def magnetic_moment(self, gB, gj):
        """mu=gB L+gj j; NO sqrt(3/4pi), NO BCS occupation factor."""
        gB, gj = _real(gB, "gB"), _real(gj, "gj")
        b, f = self.core_L().components, self.particle_j().components
        return TensorOperator("magnetic moment", 1, MappingProxyType({
            q: _csr(gB*b[q] + gj*f[q])
            for q in (-1, 0, 1)}), self.model_key)

    def m1(self, gB, gj):
        """Standard transition M1=sqrt(3/4pi)*mu, retaining caller units."""
        mu = self.magnetic_moment(gB, gj)
        return TensorOperator("M1", 1, MappingProxyType({
            q: math.sqrt(3/(4*math.pi))*t for q, t in mu.components.items()}), self.model_key)


class ZeroClebschGordanError(ValueError):
    """The selected tensor component cannot determine an allowed RME."""


@dataclass(frozen=True)
class ReducedTensor:
    operator: str
    rank: int
    rme: np.ndarray                 # rows final, columns initial
    strength: np.ndarray            # squared caller units
    selection_zero: np.ndarray
    unobservable: np.ndarray        # allowed but zero CG: NaN, never set to zero


def _em_coordinates(initial, operator, final):
    if not isinstance(initial, Spectrum) or not isinstance(final, Spectrum):
        raise TypeError("RME extraction requires Spectrum objects")
    if initial.model_key != operator.model_key or final.model_key != operator.model_key:
        raise ValueError("operator and spectra must belong to the same declared model")
    if initial.basis.two_M != final.basis.two_M:
        raise ValueError("only same-M q=0 RMEs are supported; other M phases need explicit linking")
    return initial.basis.two_M


def _rme_factor(two_Ji, two_Jf, two_M, rank):
    if abs(two_Jf-two_Ji) > 2*rank or two_Jf+two_Ji < 2*rank:
        return 0.0, True
    cg = clebsch_gordan(int(two_Ji), int(two_M), 2*rank, 0, int(two_Jf), int(two_M))
    return cg/math.sqrt(two_Jf+1), False


def reduced_matrix_elements(initial, operator, final=None, *, zero_cg="raise"):
    """Same-M,q=0 RMEs from fixed eigenvectors; zero_cg='mask' returns NaNs.

    Tensor selection-rule violations in the actual component are rejected.
    This never interprets a zero CG denominator as a vanishing RME.
    """
    final = initial if final is None else final
    two_M = _em_coordinates(initial, operator, final)
    if zero_cg not in ("raise", "mask"):
        raise ValueError("zero_cg must be 'raise' or 'mask'")
    t = operator.block(initial.basis, final.basis)
    component = final.vectors.conj().T @ (t @ initial.vectors)
    rme = np.zeros(component.shape, dtype=complex)
    selection = np.zeros(component.shape, dtype=bool)
    unobservable = np.zeros(component.shape, dtype=bool)
    tolerance = 5e-10*max(1.0, max_abs(component))
    for f, jf in enumerate(final.two_J):
        for i, ji in enumerate(initial.two_J):
            factor, forbidden = _rme_factor(ji, jf, two_M, operator.rank)
            if forbidden or factor == 0:
                if abs(component[f, i]) > tolerance:
                    raise ValueError(f"tensor selection residual at ({f},{i}) exceeds tolerance")
                if forbidden:
                    selection[f, i] = True
                elif zero_cg == "raise":
                    raise ZeroClebschGordanError(f"allowed ({f},{i}) has zero q=0 CG; use another component")
                else:
                    unobservable[f, i] = True
                    rme[f, i] = complex(np.nan, np.nan)
            else:
                rme[f, i] = component[f, i]/factor
    strength = abs(rme)**2/(initial.two_J[None, :]+1)
    return ReducedTensor(operator.name, operator.rank, _readonly(rme),
                         _readonly(strength), _readonly(selection), _readonly(unobservable))


def transition_rme(initial, operator, initial_index, final_index, final=None):
    """One same-M RME. Triangle-forbidden transitions return exactly zero.

    A zero CG on an allowed transition always raises. Use
    reduced_matrix_elements for the complete selection/unobservable masks.
    """
    final = initial if final is None else final
    two_M = _em_coordinates(initial, operator, final)
    i = _integer(initial_index, "initial_index", 0)
    f = _integer(final_index, "final_index", 0)
    if i >= len(initial.energies) or f >= len(final.energies):
        raise IndexError("state index out of range")
    factor, forbidden = _rme_factor(initial.two_J[i], final.two_J[f], two_M, operator.rank)
    value = np.vdot(final.vectors[:, f],
                    operator.block(initial.basis, final.basis) @ initial.vectors[:, i])
    if forbidden or factor == 0:
        if abs(value) > 5e-10*max(1.0, max_abs(operator.components[0])):
            raise ValueError("tensor selection residual exceeds tolerance")
        if forbidden:
            return 0j
        raise ZeroClebschGordanError("allowed transition has zero q=0 CG; RME is undetermined")
    return complex(value/factor)


@dataclass(frozen=True)
class CoreE2Calibration:
    eB: float
    unit_B_0_to_2: float
    target_B_0_to_2: float
    initial_index: int
    final_index: int


def calibrate_core_e2(core, solution, initial_index, final_index, *,
                      chi_prime, target_B_0_to_2, sign=1):
    """Calibrate |eB| on an explicit core 0->2 transition; sign is a convention.

    target_B_0_to_2 is UPWARD. For a measured downward 2->0 strength, the
    caller must supply 5*B(2->0). No W.u./eb conversion or data lookup is
    performed. State indices are caller-selected, not physical band labels.
    """
    if not isinstance(core, BosonCore) or solution.model_key != core.model_key:
        raise ValueError("calibration requires the matching boson-only core")
    i = _integer(initial_index, "initial_index", 0)
    f = _integer(final_index, "final_index", 0)
    if i >= len(solution.energies) or f >= len(solution.energies):
        raise IndexError("state index out of range")
    if solution.two_J[i] != 0 or solution.two_J[f] != 4:
        raise ValueError("calibration transition must be J=0 -> J=2")
    target = _real(target_B_0_to_2, "target_B_0_to_2")
    if target <= 0 or isinstance(sign, bool) or sign not in (-1, 1):
        raise ValueError("target must be positive and sign must be +1 or -1")
    unit = abs(transition_rme(solution, core.e2(1, chi_prime), i, f))**2
    if unit <= np.finfo(float).eps:
        raise ValueError("chosen core 0->2 matrix element vanishes; cannot calibrate eB")
    return CoreE2Calibration(sign*math.sqrt(target/unit), unit, target, i, f)
