"""Recoupled reference for axial, reflection-symmetric gamma cascades.

Angles are radians, spins can be integer or half-integer, and transition
weights are signed Droste emission amplitudes with a common phase removed.
Single and joint intensities are scaled by 4*pi and (4*pi)**2 respectively.
"""

from dataclasses import dataclass
from functools import lru_cache
from itertools import product
from math import cos, exp, factorial, fsum, hypot, isfinite, prod, sin, sqrt

from sympy import Rational
from sympy.physics.wigner import clebsch_gordan, wigner_6j, wigner_9j


@dataclass(frozen=True)
class Multipole:
    kind: str
    order: int
    weight: float = 1.0

    def __post_init__(self):
        if (
            self.kind not in ("E", "M")
            or not isinstance(self.order, int)
            or self.order < 1
            or not isfinite(self.weight)
        ):
            raise ValueError(
                "expected an electric or magnetic multipole with finite weight"
            )


@dataclass(frozen=True)
class Transition:
    initial: float
    final: float
    components: tuple[Multipole, ...]

    def __post_init__(self):
        initial, final = _twice(self.initial), _twice(self.final)
        active = tuple(component for component in self.components if component.weight)
        if not active or len({component.order for component in active}) != len(active):
            raise ValueError(
                "expected at least one active component and distinct orders"
            )
        if (initial - final) % 2 or any(
            not abs(initial - final) <= 2 * component.order <= initial + final
            for component in active
        ):
            raise ValueError("multipolarity violates the spin triangle")
        if (
            len(
                {
                    (component.order + (component.kind == "M")) % 2
                    for component in active
                }
            )
            != 1
        ):
            raise ValueError(
                "multipoles in one transition must have the same parity change"
            )
        scale = max(abs(component.weight) for component in active)
        norm = hypot(*(component.weight / scale for component in active))
        object.__setattr__(
            self,
            "components",
            tuple(
                Multipole(
                    component.kind, component.order, (component.weight / scale) / norm
                )
                for component in active
            ),
        )

    @classmethod
    def pure(cls, initial, final, kind, order):
        return cls(initial, final, (Multipole(kind, order),))

    @classmethod
    def mixed(cls, initial, final, delta):
        """M1/E2 with delta = a(E2)/a(M1) in the Droste emission basis."""
        return cls(initial, final, (Multipole("M", 1), Multipole("E", 2, delta)))

    @property
    def max_rank(self):
        return 2 * max(component.order for component in self.components)


@dataclass(frozen=True)
class LinearIntensity:
    parallel: float
    perpendicular: float

    @property
    def total(self):
        return self.parallel + self.perpendicular

    @property
    def polarization(self):
        return (self.parallel - self.perpendicular) / self.total


def _twice(spin):
    doubled = 2 * spin
    if not isfinite(doubled) or doubled < 0 or doubled != int(doubled):
        raise ValueError("spin must be a nonnegative integer or half-integer")
    return int(doubled)


def gaussian(spin, sigma):
    """Probabilities in ascending m, with sigma in spin units."""
    if not isfinite(sigma) or sigma <= 0:
        raise ValueError("sigma must be positive and finite")
    doubled = _twice(spin)
    weights = [
        exp(-((projection**2 - (doubled % 2) ** 2) / 8 / sigma) / sigma)
        for projection in range(-doubled, doubled + 1, 2)
    ]
    norm = fsum(weights)
    return tuple(weight / norm for weight in weights)


@lru_cache(maxsize=None)
def _cg(first, second, coupled, projection_first, projection_second, projection):
    return float(
        clebsch_gordan(
            first, second, coupled, projection_first, projection_second, projection
        )
    )


def alignment(spin, populations):
    """Droste Eq. (2), including B_0=1 for normalized populations."""
    doubled = _twice(spin)
    populations = tuple(populations)
    if (
        len(populations) != doubled + 1
        or any(not isfinite(weight) or weight < 0 for weight in populations)
        or abs(fsum(populations) - 1) > 1e-12
        or any(
            abs(left - right) > 1e-12
            for left, right in zip(populations, populations[::-1])
        )
    ):
        raise ValueError(
            "populations must be normalized, nonnegative and symmetric in m"
        )
    exact_spin = Rational(doubled, 2)
    return {
        rank: sqrt(doubled + 1)
        * fsum(
            (-1) ** index
            * _cg(exact_spin, exact_spin, rank, -projection, projection, 0)
            * weight
            for index, weight in enumerate(populations)
            for projection in (Rational(2 * index - doubled, 2),)
        )
        for rank in range(0, doubled + 1, 2)
    }


@lru_cache(maxsize=None)
def _pure_transfer(initial, final, order, rank):
    if rank > min(initial, final):
        return 0.0
    spin_i, spin_f = Rational(initial, 2), Rational(final, 2)
    phase = (-1) ** ((initial + final) // 2 + rank + order)
    return (
        phase
        * sqrt((initial + 1) * (final + 1))
        * float(wigner_6j(spin_i, spin_i, rank, spin_f, spin_f, order))
    )


def transfer(transition, rank):
    """Steffen–Alder Eq. (12.209–210), acting on trace-normalized tensors."""
    return fsum(
        component.weight**2
        * _pure_transfer(
            _twice(transition.initial), _twice(transition.final), component.order, rank
        )
        for component in transition.components
    )


def _path_product(path, rank):
    return prod(transfer(transition, rank) for transition in path)


def _path_check(path, exit_spin):
    for left, right in zip(path, path[1:]):
        if left.final != right.initial:
            raise ValueError("transitions must form an emission-ordered cascade")
    if path and path[-1].final != exit_spin:
        raise ValueError("path does not reach the required spin")


def _initial_alignment(populations, first, before):
    _path_check(before, first.initial)
    spin = before[0].initial if before else first.initial
    return alignment(spin, populations)


@lru_cache(maxsize=None)
def _f_prefactor(initial, final, order, order_prime, rank, outgoing, incoming):
    """Factor in Droste Eq. (7) excluding its helicity CG coefficient."""
    if (
        not abs(outgoing - incoming) <= rank <= outgoing + incoming
        or not abs(order - order_prime) <= rank <= order + order_prime
        or outgoing > final
        or incoming > initial
    ):
        return 0.0
    spin_i, spin_f = Rational(initial, 2), Rational(final, 2)
    nine_j = wigner_9j(
        spin_i, spin_i, incoming, order, order_prime, rank, spin_f, spin_f, outgoing
    )
    dimension = (initial + 1) * (final + 1) * (2 * order + 1) * (2 * order_prime + 1)
    dimension *= (2 * outgoing + 1) * (2 * incoming + 1)
    return (-1) ** (order - 1) * sqrt(dimension) * float(nine_j)


@lru_cache(maxsize=None)
def radiation(transition, rank, outgoing=0, incoming=0, *, polarized=False):
    """Generalized A in Droste Eqs. (3–4), with Starosta's corrected primed phase."""
    if polarized and rank < 2:
        return 0.0
    projection_prime = -1 if polarized else 1
    return fsum(
        left.weight
        * right.weight
        * (-1 if polarized and right.kind == "M" else 1)
        * _cg(left.order, right.order, rank, -1, projection_prime, projection_prime - 1)
        * _f_prefactor(
            _twice(transition.initial),
            _twice(transition.final),
            left.order,
            right.order,
            rank,
            outgoing,
            incoming,
        )
        for left, right in product(transition.components, repeat=2)
    )


@lru_cache(maxsize=None)
def small_d(rank, row, column, theta):
    """Real matrix element <rank,row|exp(-i theta J_y)|rank,column>."""
    if max(abs(row), abs(column)) > rank:
        return 0.0
    cosine, sine = cos(theta / 2), sin(theta / 2)
    prefactor = sqrt(
        prod(
            factorial(rank + value) * factorial(rank - value) for value in (row, column)
        )
    )
    return prefactor * fsum(
        (-1) ** (row - column + index)
        * cosine ** (2 * rank + column - row - 2 * index)
        * sine ** (row - column + 2 * index)
        / (
            factorial(rank + column - index)
            * factorial(index)
            * factorial(row - column + index)
            * factorial(rank - row - index)
        )
        for index in range(max(0, column - row), min(rank + column, rank - row) + 1)
    )


def singles(populations, transition, theta, *, before=()):
    """Scaled parallel and perpendicular intensity from Droste Eqs. (12–15)."""
    tensors = _initial_alignment(populations, transition, before)
    direction, stokes = [], []
    for rank, initial_alignment in tensors.items():
        if rank > min(_twice(transition.initial), transition.max_rank):
            continue
        weight = initial_alignment * _path_product(before, rank)
        direction.append(
            weight
            * radiation(transition, rank, incoming=rank)
            * small_d(rank, 0, 0, theta)
        )
        stokes.append(
            -weight
            * radiation(transition, rank, incoming=rank, polarized=True)
            * small_d(rank, 0, 2, theta)
        )
    total, difference = fsum(direction), fsum(stokes)
    return LinearIntensity((total + difference) / 2, (total - difference) / 2)


def joint(
    populations,
    first,
    second,
    direction_first,
    direction_second,
    *,
    before=(),
    between=(),
    target=None,
):
    """Droste Eqs. (1,16), with analyzer for emission index 1 or 2, or neither.

    Directions are (theta, phi) in a common lab frame. The analyzer axes are
    e_theta and e_phi for the target direction, with supplied phi fixing the
    reference meridian even at a pole.
    """
    if target not in (None, 1, 2):
        raise ValueError("target must be emission index 1, 2, or None")
    _path_check((first, *between), second.initial)
    tensors = _initial_alignment(populations, first, before)
    theta_first, phi_first = direction_first
    theta_second, phi_second = direction_second
    azimuth = phi_second - phi_first
    direction, stokes = [], []
    for incoming, initial_alignment in tensors.items():
        if incoming > _twice(first.initial) or initial_alignment == 0:
            continue
        entrance = initial_alignment * _path_product(before, incoming)
        max_intermediate = min(
            _twice(first.final), _twice(second.initial), second.max_rank
        )
        for middle in range(0, max_intermediate + 1, 2):
            propagation = entrance * _path_product(between, middle)
            second_directional = radiation(second, middle, incoming=middle)
            second_polarized = radiation(
                second, middle, incoming=middle, polarized=True
            )
            for coupled in range(
                abs(incoming - middle), min(incoming + middle, first.max_rank) + 1
            ):
                first_directional = radiation(first, coupled, middle, incoming)
                first_polarized = radiation(
                    first, coupled, middle, incoming, polarized=True
                )
                for projection in range(min(middle, coupled) + 1):
                    weight = (
                        propagation
                        * (1 if projection == 0 else 2)
                        * cos(projection * azimuth)
                        * _cg(incoming, middle, coupled, 0, projection, projection)
                    )
                    directional_first = small_d(coupled, projection, 0, theta_first)
                    directional_second = small_d(middle, projection, 0, theta_second)
                    direction.append(
                        weight
                        * first_directional
                        * second_directional
                        * directional_first
                        * directional_second
                    )
                    if target == 1:
                        analyzer = small_d(coupled, projection, 2, theta_first) + (
                            -1
                        ) ** coupled * small_d(coupled, projection, -2, theta_first)
                        stokes.append(
                            -weight
                            * first_polarized
                            * second_directional
                            * analyzer
                            * directional_second
                            / 2
                        )
                    if target == 2:
                        analyzer = small_d(
                            middle, projection, 2, theta_second
                        ) + small_d(middle, projection, -2, theta_second)
                        stokes.append(
                            -weight
                            * first_directional
                            * second_polarized
                            * directional_first
                            * analyzer
                            / 2
                        )
    total = fsum(direction)
    if target is None:
        return total
    difference = fsum(stokes)
    return LinearIntensity((total + difference) / 2, (total - difference) / 2)


def dco_ratio(
    populations,
    first,
    second,
    target,
    direction_a,
    direction_b,
    *,
    before=(),
    between=(),
):
    """W(target at a, gate at b)/W(target at b, gate at a)."""
    if target not in (1, 2):
        raise ValueError("target must be emission index 1 or 2")
    numerator_directions = (
        (direction_a, direction_b) if target == 1 else (direction_b, direction_a)
    )
    numerator = joint(
        populations,
        first,
        second,
        *numerator_directions,
        before=before,
        between=between,
    )
    denominator = joint(
        populations,
        first,
        second,
        *numerator_directions[::-1],
        before=before,
        between=between,
    )
    return numerator / denominator
