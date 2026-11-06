"""Quadratic and signed cubic rotational scalars of a Hermitian rank-2 tensor.

The caller supplies ALL five lab components in one declared full representation,
with Q_m^dagger = (-1)^m Q_-m and a normalized state. Dense and scipy sparse
matrices are accepted. No normalization of the operator or state is performed.
Units are retained: q2 has Q units squared and q3 has Q units cubed.

    q2 = <Q . Q> = sum_m ||Q_m psi||^2
    q3 = -sqrt(7/2) <[Q x Q]^2 . Q>.

Operator ordering and complex phases are preserved. The reality check precedes
conversion to real scalars; the complex totals remain available. Optional lab
Jz,Jplus generators check SU(2) and rank-2 covariance. Without generators,
rank-2 transformation and completeness are CALLER DECLARATIONS. A component
dictionary alone cannot establish the physical completeness of a Hilbert space.
Full within the declared model space does not mean full within a nucleus.

Reduced convention, R[f,i] = <Jf,alpha_f || Q || Ji,alpha_i>:
    <Jf Mf|Q_m|Ji Mi> = CG(Ji Mi,2 m|Jf Mf) R[f,i]/sqrt(2Jf+1).
For initial i with spin J, complete closure gives
    q2 = sum_a |R[a,i]|^2/(2J+1),
    q3 = -sqrt(35/2) (-1)^(2J)/(2J+1)
         * sum_ab {2 2 2; J Ja Jb} R[i,a] R[a,b] R[b,i].
The half-integer phase is essential. For J=0 the 6j is 1/5, recovering
    q3 = -sqrt(7/10) sum_ab R[0,2a] R[2a,2b] R[2b,0].
Hermitian reciprocity is R[f,i] = (-1)^(Jf-Ji) conjugate(R[i,f]).
NaNs in a reduced table mean UNKNOWN, not zero. Missing required elements or
undeclared state completeness suppress the complete-moment result and are reported.

q3/q2^(3/2) is returned WITHOUT clipping. Quantum operators and magnitude
fluctuations can put it outside [-1,1]. A signed rigid-equivalent angle
acos(ratio)/3 is conditional, and undefined outside that interval except for
explicitly reported tiny boundary rounding. Full model-space moments do not
automatically determine physical intrinsic shape: fluctuations and projection
of the charge operator into the model space affect that interpretation.

j_plus_two_proxy implements rotationally invariant restricted RME contractions
in caller registry order (default at most five J+2 states). Projectors onto
complete chosen magnetic multiplets commute with rotations. These quantities
differ from the complete charge-polynomial moments q2/q3; their shape conversion
has limited regimes. Rotational invariance does not imply complete closure or
a valid intrinsic-shape conversion.

Only the frozen pure Condon--Shortley CG helper is reused. The 6j uses its own
exact-Fraction Racah sum. There is no I/O, fitting, source replay, band/mode
classification, experimental input, or import of a legacy analyzer.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
import math
from numbers import Integral, Real
from types import MappingProxyType

import numpy as np
from scipy import sparse

if __package__:
    from .paired_single_j_em import clebsch_gordan
else:
    from paired_single_j_em import clebsch_gordan

__all__ = [
    "FullRepresentation", "Multiplet", "ReducedQuadrupole", "ScalarInvariants",
    "ClosureResult", "RestrictedProxy", "direct_invariants", "reduced_invariants",
    "j_plus_two_proxy", "direct_from_spectrum", "reduced_table_from_spectrum",
    "wigner_6j",
]


def _integer(value, name, minimum=0):
    if isinstance(value, bool) or not isinstance(value, Integral) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return int(value)


def _tolerance(value, name):
    if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite, real, and nonnegative")
    return float(value)


def _max_abs(value):
    data = value.data if sparse.issparse(value) else np.asarray(value)
    return float(np.max(np.abs(data))) if data.size else 0.


def _matrix(value, dimension, name):
    matrix = sparse.csr_matrix(value, dtype=complex) if sparse.issparse(value) else np.asarray(value, dtype=complex)
    if matrix.shape != (dimension, dimension):
        raise ValueError(f"{name} must have full representation shape {(dimension, dimension)}")
    data = matrix.data if sparse.issparse(matrix) else matrix
    if not np.all(np.isfinite(data)):
        raise ValueError(f"{name} contains nonfinite entries")
    return matrix


def _check_residual(residual, scale, name, rtol, atol):
    if not math.isfinite(residual) or residual > atol + rtol * scale:
        raise ValueError(f"{name} residual {residual:.6g} exceeds {atol + rtol * scale:.6g}")


@dataclass(frozen=True)
class FullRepresentation:
    """Caller declaration of a full finite model representation, not a nucleus."""

    label: str
    dimension: int

    def __post_init__(self):
        if not isinstance(self.label, str) or not self.label.strip():
            raise ValueError("representation label must be nonempty")
        _integer(self.dimension, "dimension", 1)


@dataclass(frozen=True)
class Multiplet:
    label: str
    two_J: int

    def __post_init__(self):
        if not isinstance(self.label, str) or not self.label.strip():
            raise ValueError("multiplet label must be nonempty")
        _integer(self.two_J, "two_J")


@dataclass(frozen=True)
class ReducedQuadrupole:
    """One row/column per whole angular multiplet; rows final, columns initial.

    complete must explicitly declare that the registry exhausts the model.
    Its sum(2J+1) must then equal representation.dimension. NaNs denote unknown
    RMEs. Forbidden triangle/parity channels can be certified as zero by angular
    momentum alone; an allowed channel with zero component CG remains unknown.
    """

    representation: FullRepresentation
    multiplets: tuple
    rme: np.ndarray
    complete: bool
    unresolved: tuple = ()

    def __post_init__(self):
        if not isinstance(self.representation, FullRepresentation):
            raise TypeError("representation must be FullRepresentation")
        states = tuple(self.multiplets)
        if not states or any(not isinstance(s, Multiplet) for s in states):
            raise ValueError("multiplets must be a nonempty sequence of Multiplet")
        if len({s.label for s in states}) != len(states):
            raise ValueError("multiplet labels must be unique")
        if type(self.complete) is not bool:
            raise ValueError("complete must be an explicit boolean")
        dimension = sum(s.two_J + 1 for s in states)
        if dimension > self.representation.dimension or (
            self.complete and dimension != self.representation.dimension
        ):
            raise ValueError("multiplet dimensions do not match the declared completeness")
        matrix = np.array(self.rme, dtype=complex, copy=True)
        if matrix.shape != (len(states), len(states)) or np.any(np.isinf(matrix)):
            raise ValueError("RME table must be square, with finite entries or unknown NaNs")
        matrix.setflags(write=False)
        object.__setattr__(self, "multiplets", states)
        object.__setattr__(self, "rme", matrix)
        object.__setattr__(self, "unresolved", tuple(self.unresolved))


@dataclass(frozen=True)
class ScalarInvariants:
    q2: float
    q3: float
    raw_ratio: object
    rigid_equivalent_angle_deg: object
    angle_status: str
    q2_complex: complex
    q3_complex: complex
    representation: FullRepresentation
    diagnostics: object


@dataclass(frozen=True)
class ClosureResult:
    """ScalarInvariants is reserved for complete charge-polynomial closure.

    Restricted sums over whole multiplets can also be rotationally invariant.

    quadratic_by_state maps labels to a nonnegative value or None.
    cubic_by_state_pair maps ordered (a,b) labels to a complex value or None.
    Spin-group sums include KNOWN contributions only; consult missing_entries
    and complete before interpreting them. Complex terms are not discarded.
    """

    invariants: object
    complete: bool
    quadratic_partial: float
    cubic_partial: complex
    quadratic_by_state: object
    cubic_by_state_pair: object
    quadratic_by_two_J: object
    cubic_by_two_J_pair: object
    missing_entries: tuple
    declared_complete_registry: bool
    unrepresented_dimension: int
    reciprocity_residual: float


@dataclass(frozen=True)
class RestrictedProxy:
    """Rotationally invariant restricted RME/projector contractions.

    These differ from the complete charge-polynomial moments. The flag
    complete_scalar_closure refers to that polynomial closure, not to rotational
    invariance. Shape conversion requires additional regime assumptions.
    """

    selected_labels: tuple
    quadratic_strength_sum: float
    quadratic_closure_contribution: float
    cubic_chain: complex
    scaled_absolute_chain: float
    raw_proxy_ratio: object
    proxy_angle_deg: object
    angle_status: str
    ordering: str = "caller multiplet registry order"
    complete_scalar_closure: bool = False


def _angle(ratio, tolerance):
    if ratio is None:
        return None, "undefined_zero_quadratic"
    if not math.isfinite(ratio):
        raise ValueError("nonfinite invariant ratio")
    if abs(ratio) > 1:
        if abs(ratio) - 1 > tolerance:
            return None, "outside_rigid_domain"
        return (0. if ratio > 0 else 60.), "rounded_numerical_boundary"
    return math.degrees(math.acos(ratio)) / 3, "within_rigid_domain"


def _summarize(q2, q3, q2_scale, q3_scale, representation, diagnostics, rtol, atol, angle_tolerance):
    q2, q3 = complex(q2), complex(q3)
    if not all(math.isfinite(z) for z in (q2.real, q2.imag, q3.real, q3.imag)):
        raise ValueError("nonfinite scalar: check operator scale")
    _check_residual(abs(q2.imag), q2_scale, "quadratic imaginary", rtol, atol)
    _check_residual(abs(q3.imag), q3_scale, "cubic imaginary", rtol, atol)
    if q2.real < 0:
        raise ValueError("negative quadratic invariant")
    if q2.real == 0 and q3 != 0:
        raise ValueError("nonzero cubic with zero quadratic invariant")
    ratio = q3.real / q2.real / math.sqrt(q2.real) if q2.real else None
    angle, status = _angle(ratio, angle_tolerance)
    return ScalarInvariants(
        q2.real, q3.real, ratio, angle, status, q2, q3, representation,
        MappingProxyType(dict(diagnostics)),
    )


def _tensor(components, representation, rtol, atol, angular_generators=None):
    if not isinstance(representation, FullRepresentation):
        raise TypeError("an explicit FullRepresentation is required")
    if (not hasattr(components, "keys") or set(components) != set(range(-2, 3))
            or any(isinstance(m, bool) or not isinstance(m, Integral) for m in components)):
        raise ValueError("exactly the five integer components -2,-1,0,1,2 are required")
    q = {m: _matrix(components[m], representation.dimension, f"Q[{m}]") for m in range(-2, 3)}
    scale = max(_max_abs(t) for t in q.values())
    residual = max(_max_abs(q[m].conj().T - (-1)**m * q[-m]) for m in q)
    _check_residual(residual, scale, "spherical Hermiticity", rtol, atol)
    diagnostics = {"spherical_hermiticity_residual": residual,
                   "rank2_covariance": "caller_declared"}
    if angular_generators is not None:
        if len(angular_generators) != 2:
            raise ValueError("angular_generators must be (Jz,Jplus)")
        jz, jp = (_matrix(a, representation.dimension, name)
                  for a, name in zip(angular_generators, ("Jz", "Jplus")))
        _check_residual(_max_abs(jz - jz.conj().T), _max_abs(jz), "Jz Hermiticity", rtol, atol)
        jm = jp.conj().T
        checks = [(jz @ jp - jp @ jz - jp, (_max_abs(jz @ jp), _max_abs(jp @ jz), _max_abs(jp))),
                  (jp @ jm - jm @ jp - 2*jz, (_max_abs(jp @ jm), _max_abs(jm @ jp), 2*_max_abs(jz)))]
        for error, scales in checks:
            _check_residual(_max_abs(error), max(scales), "SU(2)", rtol, atol)
        worst = 0.
        for m in q:
            for left, right, target in [
                (jz @ q[m], q[m] @ jz, m*q[m]),
                (jp @ q[m], q[m] @ jp,
                 math.sqrt((2-m)*(3+m))*q[m+1] if m < 2 else 0*q[m]),
            ]:
                err = _max_abs(left - right - target)
                _check_residual(err, max(_max_abs(left), _max_abs(right), _max_abs(target)),
                                "rank-2 covariance", rtol, atol)
                worst = max(worst, err)
        diagnostics.update(rank2_covariance="checked", rank2_covariance_residual=worst)
    return q, diagnostics


def direct_invariants(components, state, *, representation, angular_generators=None,
                      rtol=1e-10, atol=0., norm_tolerance=1e-10, angle_tolerance=1e-12):
    """Direct operator contractions in the full supplied representation.

    angular_generators, when provided, are lab (Jz,Jplus), in hbar units.
    No missing components, automatic state normalization, tensor symmetrization,
    reality projection before checking, or unconditional angle clipping.
    """
    rtol, atol, norm_tolerance, angle_tolerance = (
        _tolerance(v, n) for v, n in [(rtol, "rtol"), (atol, "atol"),
                                     (norm_tolerance, "norm_tolerance"), (angle_tolerance, "angle_tolerance")]
    )
    q, diagnostics = _tensor(components, representation, rtol, atol, angular_generators)
    psi = np.asarray(state, dtype=complex)
    if psi.shape != (representation.dimension,) or not np.all(np.isfinite(psi)):
        raise ValueError("state must be a finite full-representation vector")
    norm_error = abs(np.vdot(psi, psi) - 1)
    if norm_error > norm_tolerance:
        raise ValueError(f"state is not normalized: residual {norm_error:.6g}")
    vectors = {m: q[m] @ psi for m in q}
    q2 = sum(complex(np.vdot(v, v)) for v in vectors.values())
    cubic, scale = 0j, 0.
    for m in q:
        for n in q:
            p = -m-n
            if abs(p) > 2:
                continue
            # The bra Q_m becomes (-1)^m (Q_-m psi)^dagger, combining
            # with the dot-product phase (-1)^(m+n) into (-1)^n.
            coefficient = (-1)**n * clebsch_gordan(4, 2*m, 4, 2*n, 4, 2*(m+n))
            term = coefficient * np.vdot(vectors[-m], q[n] @ vectors[p])
            cubic += term
            scale += abs(term)
    diagnostics["state_norm_residual"] = float(norm_error)
    return _summarize(q2, -math.sqrt(3.5)*cubic, abs(q2), math.sqrt(3.5)*scale,
                      representation, diagnostics, rtol, atol, angle_tolerance)


def _triangle(a, b, c):
    return abs(a-b) <= c <= a+b and (a+b+c) % 2 == 0


@lru_cache(maxsize=8192)
def _sixj(a, b, c, d, e, f):
    triangles = [(a, b, c), (a, e, f), (d, b, f), (d, e, c)]
    if any(not _triangle(*t) for t in triangles):
        return 0.
    prefactor = Fraction(1)
    for x, y, z in triangles:
        prefactor *= Fraction(
            math.prod(math.factorial(v) for v in ((x+y-z)//2, (x-y+z)//2, (-x+y+z)//2)),
            math.factorial((x+y+z)//2 + 1),
        )
    lows = [(a+b+c)//2, (a+e+f)//2, (d+b+f)//2, (d+e+c)//2]
    highs = [(a+b+d+e)//2, (a+c+d+f)//2, (b+c+e+f)//2]
    total = Fraction(0)
    for z in range(max(lows), min(highs) + 1):
        denominator = math.prod(math.factorial(v) for v in
                                [*(z-x for x in lows), *(x-z for x in highs)])
        total += Fraction((-1)**z * math.factorial(z+1), denominator)
    if not total:
        return 0.
    return math.copysign(math.sqrt(float(prefactor * total * total)), 1 if total > 0 else -1)


def wigner_6j(two_a, two_b, two_c, two_d, two_e, two_f):
    """Real Wigner {a b c;d e f}, using doubled nonnegative integer arguments.

    Exact rational cancellation is retained until the final signed square root.
    Invalid triangles return zero; invalid argument types raise ValueError.
    """
    args = tuple(_integer(v, "6j argument") for v in (two_a, two_b, two_c, two_d, two_e, two_f))
    return _sixj(*args)


def _allowed(a, b):
    return _triangle(a, 4, b)


def _prepare_reduced(table, rtol, atol):
    if not isinstance(table, ReducedQuadrupole):
        raise TypeError("table must be ReducedQuadrupole")
    matrix = table.rme.copy()
    known = np.isfinite(matrix)
    scale = float(np.max(np.abs(matrix[known]))) if np.any(known) else 0.
    worst = 0.
    for f, sf in enumerate(table.multiplets):
        for i, si in enumerate(table.multiplets):
            if not _allowed(si.two_J, sf.two_J):
                if known[f, i]:
                    _check_residual(abs(matrix[f, i]), scale, "forbidden RME", rtol, atol)
                matrix[f, i], known[f, i] = 0., True
            elif known[f, i] and known[i, f]:
                error = abs(matrix[f, i] - (-1)**((sf.two_J-si.two_J)//2)*matrix[i, f].conjugate())
                _check_residual(error, scale, "RME Hermitian reciprocity", rtol, atol)
                worst = max(worst, error)
    return matrix, known, worst


def reduced_invariants(table, initial_index, *, rtol=1e-10, atol=0., angle_tolerance=1e-12):
    """General-spin complete 6j closure, with explicit state/spin decomposition.

    On missing required matrix elements or an incomplete declared registry,
    return ClosureResult(invariants=None, complete=False), listing missing
    entries and only labelled partial sums. No missing channel is fitted,
    inferred from a zero CG, or silently assigned zero.
    """
    rtol, atol, angle_tolerance = (_tolerance(v, n) for v, n in
                                  [(rtol, "rtol"), (atol, "atol"), (angle_tolerance, "angle_tolerance")])
    matrix, known, reciprocity = _prepare_reduced(table, rtol, atol)
    initial = _integer(initial_index, "initial_index")
    if initial >= len(table.multiplets):
        raise IndexError("initial_index out of range")
    states = table.multiplets
    tj = states[initial].two_J
    outer = [a for a, state in enumerate(states) if _allowed(tj, state.two_J)]
    missing, quadratic, cubic, by_spin, by_pair = set(), {}, {}, {}, {}
    q2, q3, cubic_scale = 0., 0j, 0.
    for a in outer:
        for row, col in [(a, initial), (initial, a)]:
            if not known[row, col]:
                missing.add((states[row].label, states[col].label))
        value = float(abs(matrix[a, initial])**2 / (tj+1)) if known[a, initial] else None
        quadratic[states[a].label] = value
        if value is not None:
            q2 += value
            by_spin[states[a].two_J] = by_spin.get(states[a].two_J, 0.) + value
    for a in outer:
        for b in outer:
            coefficient = -math.sqrt(17.5) * (-1)**tj / (tj+1) * wigner_6j(
                4, 4, 4, tj, states[a].two_J, states[b].two_J)
            key = (states[a].label, states[b].label)
            entries = [(initial, a), (a, b), (b, initial)]
            if coefficient == 0:
                cubic[key] = 0j
                continue
            absent = [(r, c) for r, c in entries if not known[r, c]]
            if absent:
                missing.update((states[r].label, states[c].label) for r, c in absent)
                cubic[key] = None
                continue
            value = complex(coefficient * matrix[initial, a] * matrix[a, b] * matrix[b, initial])
            cubic[key] = value
            q3 += value
            cubic_scale += abs(value)
            spin_pair = (states[a].two_J, states[b].two_J)
            by_pair[spin_pair] = by_pair.get(spin_pair, 0j) + value
    complete = table.complete and not missing
    invariants = _summarize(
        q2, q3, q2, cubic_scale, table.representation,
        {"reciprocity_residual": reciprocity, "closure": "complete_declared_model_space"},
        rtol, atol, angle_tolerance,
    ) if complete else None
    return ClosureResult(
        invariants, complete, q2, q3, MappingProxyType(quadratic), MappingProxyType(cubic),
        MappingProxyType(by_spin), MappingProxyType(by_pair), tuple(sorted(missing)), table.complete,
        table.representation.dimension - sum(s.two_J+1 for s in states), reciprocity,
    )


def j_plus_two_proxy(table, initial_index, *, max_states=5, rtol=1e-10, atol=0., angle_tolerance=1e-12):
    """Rotationally invariant restricted contractions, with conditional shape conversion.

    S=sum_a |R[a,i]|^2, C=sum_ab R[a,i]* R[a,b] R[b,i], all a,b at J+2.
    Proxy ratio=sqrt(7/10)*|C|/S^(3/2); max_states=None retains that entire
    spin sector. It still omits other spin sectors from the complete polynomial
    closure. The selected projectors contain whole magnetic multiplets, so the
    restriction preserves rotational invariance. Unknown needed RMEs raise.
    Caller registry order is NOT silently interpreted as energy order.
    """
    rtol, atol, angle_tolerance = (_tolerance(v, n) for v, n in
                                  [(rtol, "rtol"), (atol, "atol"), (angle_tolerance, "angle_tolerance")])
    matrix, known, _ = _prepare_reduced(table, rtol, atol)
    i = _integer(initial_index, "initial_index")
    if i >= len(table.multiplets):
        raise IndexError("initial_index out of range")
    if max_states is not None:
        _integer(max_states, "max_states", 1)
    tj = table.multiplets[i].two_J
    selected = [a for a, s in enumerate(table.multiplets) if s.two_J == tj+4]
    if max_states is not None:
        selected = selected[:max_states]
    if not selected:
        raise ValueError("no J+2 states available in the registry")
    required = {(a, i) for a in selected} | {(i, a) for a in selected}
    required |= {(a, b) for a in selected for b in selected}
    missing = [(table.multiplets[a].label, table.multiplets[b].label)
               for a, b in sorted(required) if not known[a, b]]
    if missing:
        raise ValueError(f"proxy has unknown required RMEs: {missing}")
    u = matrix[selected, i]
    middle = matrix[np.ix_(selected, selected)]
    strength = float(np.sum(abs(u)**2))
    chain = complex(np.vdot(u, middle @ u))
    if not all(math.isfinite(v) for v in (strength, chain.real, chain.imag)):
        raise ValueError("nonfinite proxy contraction: check operator scale")
    scale = float(np.sum(abs(u[:, None].conj() * middle * u[None, :])))
    _check_residual(abs(chain.imag), scale, "proxy chain imaginary", rtol, atol)
    cubic = math.sqrt(.7)*abs(chain)
    ratio = cubic/strength/math.sqrt(strength) if strength else None
    angle, status = _angle(ratio, angle_tolerance)
    return RestrictedProxy(tuple(table.multiplets[a].label for a in selected),
                           strength, strength/(tj+1), chain, cubic, ratio, angle, status)


def _spectrum_coordinates(solution, operator, label, rtol, atol):
    """Duck-typed read-only adapter; never import or mutate an IBFM kernel."""
    if operator.rank != 2 or solution.model_key != operator.model_key:
        raise ValueError("matching model identity and rank-2 operator required")
    basis = solution.basis
    representation = FullRepresentation(label, basis.full_dimension)
    indices = np.asarray(basis.full_indices)
    if (indices.ndim != 1 or indices.dtype.kind not in "iu"
            or len(set(indices.tolist())) != len(indices)
            or np.any(indices < 0) or np.any(indices >= representation.dimension)):
        raise ValueError("invalid full_indices embedding")
    vectors = np.asarray(solution.vectors, dtype=complex)
    if (vectors.ndim != 2 or vectors.shape[0] != len(indices)
            or not 0 < vectors.shape[1] <= len(indices) or not np.all(np.isfinite(vectors))):
        raise ValueError("invalid spectrum eigenvector matrix")
    _check_residual(_max_abs(vectors.conj().T @ vectors - np.eye(vectors.shape[1])),
                    1., "spectrum orthonormality", rtol, atol)
    return representation, indices, vectors


def direct_from_spectrum(solution, operator, state_index, *, representation_label, **options):
    """Lift a fixed-M Spectrum vector through full_indices before contracting."""
    rtol = _tolerance(options.get("rtol", 1e-10), "rtol")
    atol = _tolerance(options.get("atol", 0.), "atol")
    representation, indices, vectors = _spectrum_coordinates(
        solution, operator, representation_label, rtol, atol)
    state = _integer(state_index, "state_index")
    if state >= vectors.shape[1]:
        raise IndexError("state_index out of range")
    psi = np.zeros(representation.dimension, dtype=complex)
    psi[indices] = vectors[:, state]
    return direct_invariants(operator.components, psi, representation=representation, **options)


def reduced_table_from_spectrum(solution, operator, *, representation_label,
                                rtol=1e-10, atol=0., cg_tolerance=0.):
    """Same-M,q=0 adapter with unknown masks for allowed zero-CG channels.

    Whole-registry completeness is inferred ONLY when the complete M block and
    sum(2J+1) account for the full representation. Higher-|M| omissions or
    truncated eigenvector sets remain incomplete. This does not join independent
    M-block phases or recover invisible channels by assuming they vanish.
    """
    rtol, atol, cg_tolerance = (_tolerance(v, n) for v, n in
                               [(rtol, "rtol"), (atol, "atol"), (cg_tolerance, "cg_tolerance")])
    representation, indices, vectors = _spectrum_coordinates(
        solution, operator, representation_label, rtol, atol)
    q, _ = _tensor(operator.components, representation, rtol, atol)
    tm = solution.basis.two_M
    if isinstance(tm, bool) or not isinstance(tm, Integral):
        raise ValueError("RME adapter requires a declared fixed doubled M")
    spins = tuple(_integer(j, "two_J") for j in solution.two_J)
    if len(spins) != vectors.shape[1] or any(j < abs(tm) or (j-tm) % 2 for j in spins):
        raise ValueError("invalid J labels for this fixed-M block")
    component = vectors.conj().T @ (q[0][indices][:, indices] @ vectors
                                    if sparse.issparse(q[0]) else q[0][np.ix_(indices, indices)] @ vectors)
    scale = max(_max_abs(component), _max_abs(q[0]))
    matrix = np.empty(component.shape, dtype=complex)
    unresolved = []
    for f, jf in enumerate(spins):
        for i, ji in enumerate(spins):
            cg = clebsch_gordan(ji, int(tm), 4, 0, jf, int(tm))
            allowed = _allowed(ji, jf)
            if not allowed or abs(cg) <= cg_tolerance:
                _check_residual(abs(component[f, i]), scale, "component selection", rtol, atol)
                matrix[f, i] = complex(np.nan, np.nan) if allowed else 0.
                if allowed:
                    unresolved.append(f"allowed R[{f},{i}] has unresolved q=0 CG")
            else:
                matrix[f, i] = component[f, i] * math.sqrt(jf+1) / cg
    complete = vectors.shape[0] == vectors.shape[1] and sum(j+1 for j in spins) == representation.dimension
    return ReducedQuadrupole(representation, tuple(Multiplet(f"state_{i}", j) for i, j in enumerate(spins)),
                             matrix, bool(complete), tuple(unresolved))
