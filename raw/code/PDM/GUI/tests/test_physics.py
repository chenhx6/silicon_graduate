import numpy as np
import pytest
from numpy.polynomial.legendre import leggauss

from multipolepdm.contracts import Transition
from multipolepdm.physics.amplitudes import (
    analyzer_amplitudes,
    emission_amplitudes,
    emit,
)
from multipolepdm.physics.populations import initial_population, orientation_tensor
from multipolepdm.physics.propagation import (
    deorientation_coefficient,
    propagate_unobserved,
)


@pytest.mark.parametrize("j", [0, 0.5, 4, 4.5])
def test_gaussian_and_tensor(j):
    p = initial_population(j, [0.0001, 0.3, 2])
    np.testing.assert_allclose(p.sum(axis=-1), 1, atol=1e-14)
    np.testing.assert_allclose(orientation_tensor(j, p, 0), 1, atol=1e-14)
    np.testing.assert_allclose(p, p[:, ::-1])


@pytest.mark.parametrize(
    "transition",
    [
        Transition(5, 4),
        Transition(4.5, 3.5),
        Transition(4, 2, ("E2",)),
        Transition(0, 1, ("E1",)),
    ],
)
def test_total_radiation_probability(transition):
    rho = np.eye(round(2 * transition.spin_initial + 1))
    xs, ws = leggauss(8)
    integral = 0
    for x, w in zip(xs, ws):
        for phi in np.arange(12) * 2 * np.pi / 12:
            a = emission_amplitudes(transition, np.arccos(x), phi, -0.7)
            integral += w * 2 * np.pi / 12 * np.einsum("afi,afj->ij", a.conj(), a)
    np.testing.assert_allclose(integral, rho, atol=3e-14)


def test_transfer_preserves_unnormalized_coherence_and_trace():
    tr = Transition(3, 2, delta=-0.7)
    rng = np.random.default_rng(3)
    a = rng.normal(size=(7, 7)) + 1j * rng.normal(size=(7, 7))
    rho = a @ a.conj().T
    result = propagate_unobserved(rho, tr)
    np.testing.assert_allclose(np.trace(result), np.trace(rho))
    assert np.linalg.eigvalsh(result).min() >= -1e-12
    assert np.max(abs(result - np.diag(result.diagonal()))) > 1e-4
    assert deorientation_coefficient(tr, 0) == pytest.approx(1)


def test_electric_and_magnetic_dipole_analyzers():
    rho = np.diag([0.0, 1.0, 0.0])
    for multipole, expected in [("E1", 1), ("M1", -1)]:
        par, perp = analyzer_amplitudes(
            emission_amplitudes(Transition(1, 0, (multipole,)), np.pi / 2)
        )
        a, b = np.trace(emit(rho, par)).real, np.trace(emit(rho, perp)).real
        assert (a - b) / (a + b) == pytest.approx(expected)


def test_signed_mixing_matches_droste_directional_f_matrix():
    # D96 Eqs.3/7 for 5->4: F2(M1,E2)=-sqrt(13/15), F2(E2,E2)=0.
    from scipy.special import eval_legendre

    tr = Transition(5, 4)
    pop = initial_population(5, 1.5)
    rho = np.diag(pop)
    xs, ws = leggauss(12)
    xi = 0.4
    angular = np.array(
        [
            4
            * np.pi
            * np.trace(emit(rho, emission_amplitudes(tr, np.arccos(x), xi_rad=xi))).real
            for x in xs
        ]
    )
    actual = 2.5 * np.sum(ws * angular * eval_legendre(2, xs))
    f11 = 0.2943920288775949
    f12 = -0.9309493362512627
    expected = orientation_tensor(5, pop, 2) * (
        f11 * np.cos(xi) ** 2 + 2 * f12 * np.cos(xi) * np.sin(xi)
    )
    assert actual == pytest.approx(expected, abs=2e-13)


def test_large_known_mixing_ratio_has_finite_pure_limit():
    rho = np.diag(initial_population(3, 1))
    mixed = propagate_unobserved(rho, Transition(3, 2, delta=1e200))
    pure = propagate_unobserved(rho, Transition(3, 2, ("E2",)))
    np.testing.assert_allclose(mixed, pure, atol=1e-15)


@pytest.mark.parametrize("j", [0, 0.5, 4])
def test_positive_sigma_below_square_underflow_has_exact_aligned_limit(j):
    population = initial_population(j, 1e-300)
    assert np.isfinite(population).all()
    assert population.sum() == pytest.approx(1)
    assert np.count_nonzero(population) == (1 if j % 1 == 0 else 2)
