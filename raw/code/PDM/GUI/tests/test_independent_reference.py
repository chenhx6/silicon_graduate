from math import acos, cos, pi, radians, sin, sqrt, tan

import numpy as np
import pytest

from reference.angular_correlation import (
    Transition,
    alignment,
    dco_ratio,
    gaussian,
    joint,
    singles,
    transfer,
)


ATOL = 2e-12


def mean_over_sphere(function):
    nodes, weights = np.polynomial.legendre.leggauss(6)
    return (
        sum(
            weight * function((acos(node), 2 * pi * azimuth / 12))
            for node, weight in zip(nodes, weights)
            for azimuth in range(12)
        )
        / 24
    )


def frame(direction):
    theta, phi = direction
    return (
        np.array([sin(theta) * cos(phi), sin(theta) * sin(phi), cos(theta)]),
        np.array([cos(theta) * cos(phi), cos(theta) * sin(phi), -sin(theta)]),
        np.array([-sin(phi), cos(phi), 0]),
    )


@pytest.mark.parametrize("order", [1, 2])
@pytest.mark.parametrize("kind", ["E", "M"])
def test_zero_spin_cascade_closed_form_and_stokes_rotation(order, kind):
    first = Transition.pure(0, order, kind, order)
    last = Transition.pure(order, 0, kind, order)
    for a, b in [
        ((0.0, 0.0), (pi / 2, 0.0)),
        ((0.63, 0.3), (1.81, 1.2)),
        ((pi / 2, 1.2), (pi / 2, 1.2)),
        ((pi, 0.8), (0.6, 2.1)),
    ]:
        x = float(frame(a)[0] @ frame(b)[0])
        if order == 1:
            relative_x, relative_y = 3 * x**2 / 4, 3 / 4
        else:
            relative_x, relative_y = 5 * (2 * x**2 - 1) ** 2 / 4, 5 * x**2 / 4
        if kind == "M":
            relative_x, relative_y = relative_y, relative_x
        total = relative_x + relative_y
        assert joint((1,), first, last, a, b) == pytest.approx(total, abs=ATOL)
        for target, direction, gate in [(1, a, b), (2, b, a)]:
            _, parallel, perpendicular = frame(direction)
            gate_vector = frame(gate)[0]
            projections = np.square(
                [gate_vector @ parallel, gate_vector @ perpendicular]
            )
            rotation = (
                (projections[0] - projections[1]) / sum(projections)
                if abs(x) < 1 - ATOL
                else 0
            )
            expected_difference = rotation * (relative_x - relative_y)
            analyzed = joint((1,), first, last, a, b, target=target)
            assert analyzed.parallel == pytest.approx(
                (total + expected_difference) / 2, abs=ATOL
            )
            assert analyzed.perpendicular == pytest.approx(
                (total - expected_difference) / 2, abs=ATOL
            )


def test_electric_and_magnetic_analyzers_and_pole_reference():
    electric = Transition.pure(2, 0, "E", 2)
    magnetic = Transition.pure(1, 0, "M", 1)
    assert singles((0, 0.5, 0, 0.5, 0), electric, pi / 2).polarization == pytest.approx(
        1
    )
    assert singles((0, 1, 0), magnetic, pi / 2).polarization == pytest.approx(-1)
    assert singles((0, 0.5, 0, 0.5, 0), electric, 0).polarization == pytest.approx(0)
    assert singles((0, 1, 0), magnetic, 0).total == pytest.approx(0, abs=ATOL)
    assert singles((0.5, 0, 0, 0, 0.5), electric, pi / 2).polarization == pytest.approx(
        -1
    )


@pytest.mark.parametrize("delta", [0, 0.5, -0.5, -sqrt(3), 1e12, -1e12])
def test_signed_mixed_anchor_and_pure_limit(delta):
    transition = Transition.mixed(1.5, 0.5, delta)
    populations = (0.5, 0, 0, 0.5)
    result = singles(populations, transition, pi / 2)
    assert alignment(1.5, populations)[2] == pytest.approx(1)
    assert result.parallel == pytest.approx(
        (sqrt(3) + delta) ** 2 / (4 * (1 + delta**2)), abs=ATOL
    )
    assert result.perpendicular == pytest.approx(delta**2 / (1 + delta**2), abs=ATOL)
    if abs(delta) == 1e12:
        pure = singles(populations, Transition.pure(1.5, 0.5, "E", 2), pi / 2)
        assert result.parallel == pytest.approx(pure.parallel, abs=ATOL)
        assert result.perpendicular == pytest.approx(pure.perpendicular, abs=ATOL)


def test_primed_phase_check_uses_both_signs():
    populations = (0.5, 0, 0, 0.5)
    positive = singles(populations, Transition.mixed(1.5, 0.5, 0.5), pi / 2)
    negative = singles(populations, Transition.mixed(1.5, 0.5, -0.5), pi / 2)
    difference_corrected = positive.parallel - positive.perpendicular
    difference_printed = negative.parallel - negative.perpendicular
    assert difference_corrected == pytest.approx(0.7964101615137754)
    assert difference_printed == pytest.approx(0.1035898384862246)
    assert difference_corrected - difference_printed == pytest.approx(4 * sqrt(3) / 10)


def test_nonadjacent_cascade_rank_two_closed_form():
    first = Transition.pure(0, 1, "M", 1)
    last = Transition.pure(1, 0, "M", 1)
    assert transfer(Transition.pure(1, 1, "M", 1), 2) == pytest.approx(-0.5)
    assert transfer(Transition.pure(1, 1, "E", 2), 2) == pytest.approx(0.1)
    for delta in [0.5, -0.5]:
        middle = Transition.mixed(1, 1, delta)
        assert transfer(middle, 0) == pytest.approx(1)
        assert transfer(middle, 2) == pytest.approx(-0.38)
        for theta in [0.12, 0.77, pi / 2, 2.9]:
            x = cos(theta)
            expected_total = 1 - 0.38 * (3 * (1 + x**2) / 4 - 1)
            expected_difference = -0.38 * 3 * (1 - x**2) / 4
            for target in (1, 2):
                analyzed = joint(
                    (1,),
                    first,
                    last,
                    (0, 0),
                    (theta, 0),
                    between=(middle,),
                    target=target,
                )
                assert analyzed.total == pytest.approx(expected_total, abs=ATOL)
                assert analyzed.parallel - analyzed.perpendicular == pytest.approx(
                    expected_difference, abs=ATOL
                )


def test_full_directional_integral_of_nonadjacent_joint_is_one():
    p = gaussian(3, 1.1)
    first = Transition.mixed(3, 2, -0.6)
    gap = Transition.mixed(2, 2, 0.8)
    last = Transition.mixed(2, 1, 0.4)
    nodes, weights = np.polynomial.legendre.leggauss(4)
    integral = (
        sum(
            weight_a
            * weight_b
            * joint(
                p,
                first,
                last,
                (acos(node_a), 0),
                (acos(node_b), 2 * pi * azimuth / 9),
                between=(gap,),
            )
            for node_a, weight_a in zip(nodes, weights)
            for node_b, weight_b in zip(nodes, weights)
            for azimuth in range(9)
        )
        / 36
    )
    assert integral == pytest.approx(1, abs=ATOL)


def test_directional_marginals_do_not_regaussianize_or_drop_gate_probability():
    before = Transition.mixed(4.5, 3.5, -0.2)
    first = Transition.mixed(3.5, 2.5, 0.7)
    gap = Transition.mixed(2.5, 2.5, -0.8)
    last = Transition.mixed(2.5, 1.5, -0.4)
    p = gaussian(4.5, 1.4)
    fixed = (1.18, 0.28)
    another_gate = (0.89, 0.13)
    for target in (1, 2):

        def response(gate):
            angles = (fixed, gate) if target == 1 else (gate, fixed)
            return joint(
                p, first, last, *angles, before=(before,), between=(gap,), target=target
            )

        want = (
            singles(p, first, fixed[0], before=(before,))
            if target == 1
            else singles(p, last, fixed[0], before=(before, first, gap))
        )
        assert mean_over_sphere(lambda gate: response(gate).parallel) == pytest.approx(
            want.parallel, abs=ATOL
        )
        assert mean_over_sphere(
            lambda gate: response(gate).perpendicular
        ) == pytest.approx(want.perpendicular, abs=ATOL)
        assert (
            abs(
                response(another_gate).polarization - response((1.83, 1.7)).polarization
            )
            > 0.01
        )
        angles = (fixed, another_gate) if target == 1 else (another_gate, fixed)
        assert response(another_gate).total == pytest.approx(
            joint(p, first, last, *angles, before=(before,), between=(gap,)), abs=ATOL
        )
    assert mean_over_sphere(
        lambda direction: singles(p, first, direction[0], before=(before,)).total
    ) == pytest.approx(1, abs=ATOL)
    final_marginal = singles(p, last, fixed[0], before=(before, first, gap))
    fresh_gaussian = singles(gaussian(last.initial, 1.4), last, fixed[0])
    assert abs(final_marginal.polarization - fresh_gaussian.polarization) > 0.01


def test_dco_detector_and_transition_roles_and_relative_azimuth():
    t = Transition.mixed(5, 4, -0.4)
    g = Transition.pure(4, 2, "E", 2)
    p = gaussian(5, 1.5)
    a, b = (0.9, 0.2), (1.4, 1.6)
    value = dco_ratio(p, t, g, 1, a, b)
    assert abs(value - 1) > 0.05
    assert dco_ratio(p, t, g, 1, b, a) == pytest.approx(1 / value)
    assert dco_ratio(p, t, g, 2, a, b) == pytest.approx(1 / value)
    assert dco_ratio(
        p, t, g, 1, (a[0], a[1] + 0.32), (b[0], b[1] + 0.32)
    ) == pytest.approx(value)
    assert abs(dco_ratio(p, t, g, 1, a, (b[0], 0.6)) - value) > 0.01


@pytest.mark.parametrize(
    "delta_degrees,expected",
    [
        (-70, (0.273255003527, 0.437181264921, 0.173582689178, 0.362034032055)),
        (70, (-0.177717134737, -0.498826923183, 0.675959927383, 1.355587916565)),
    ],
)
def test_droste_figure_7_signed_point(delta_degrees, expected):
    t = Transition.mixed(5, 4, tan(radians(delta_degrees)))
    g = Transition.pure(4, 2, "E", 2)
    p = gaussian(5, 1.5)
    equator = (pi / 2, 0)
    assert (
        singles(p, t, pi / 2).polarization,
        joint(p, t, g, equator, equator, target=1).polarization,
        joint(p, t, g, equator, equator, target=2).polarization,
        dco_ratio(p, t, g, 1, (0, 0), equator),
    ) == pytest.approx(expected, abs=ATOL)


@pytest.mark.parametrize(
    "spins,orders,published",
    [
        ((10, 8, 6), (2, 2), 1),
        ((10, 8, 7), (2, 1), 0.56),
        ((10, 8, 8), (2, 2), 0.57),
        ((9, 8, 6), (1, 2), 1.81),
        ((9, 8, 7), (1, 1), 1),
        ((9, 8, 8), (1, 1), 1.79),
    ],
)
def test_kramer_flecken_table_1_selected_printed_rows(spins, orders, published):
    initial, middle, final = spins
    first = Transition.pure(initial, middle, "E", orders[0])
    last = Transition.pure(middle, final, "E", orders[1])
    p = gaussian(initial, 0.3 * initial)
    point_a, point_b = (pi / 2, 0), (radians(38), radians(18))
    assert dco_ratio(p, first, last, 1, point_a, point_b) == pytest.approx(
        published, abs=0.005
    )
