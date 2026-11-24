"""Separate the analytic pure line and a boundary of a mixed inverse model."""

from dataclasses import replace
from math import acos, pi, radians

import numpy as np
import pytest
from numpy.polynomial.legendre import leggauss

from multipolepdm.contracts import Geometry, GridSpec, JobRequest, Measurement, Transition
from multipolepdm.models.registry import evaluate_response
from multipolepdm.pdm.mapping import map_density
from multipolepdm.pdm.statistics import summarize_density
from multipolepdm.physics.amplitudes import analyzer_amplitudes, emission_amplitudes, emit
from reference import angular_correlation as ref


def analyzer_channels(transition, density, theta):
    analyzers = analyzer_amplitudes(emission_amplitudes(transition, theta))
    return np.array([np.trace(emit(density, analyzer)).real for analyzer in analyzers])


def test_e2_analytic_test_aligned_intensity_and_polarization():
    """Secretary main.tex, eq:e2-analytic-test, uses W averaged to unity."""
    transition = Transition(2, 0, ("E2",))
    independent = ref.Transition.pure(2, 0, "E", 2)
    population = (0, 0, 1, 0, 0)
    density = np.diag(population)
    parallel, perpendicular = analyzer_channels(transition, density, pi / 4)
    channels = ref.singles(population, independent, pi / 4)
    assert 4 * pi * (parallel + perpendicular) == pytest.approx(15 / 8, abs=1e-13)
    assert (parallel - perpendicular) / (parallel + perpendicular) == pytest.approx(1, abs=1e-13)
    assert channels.total == pytest.approx(15 / 8, abs=1e-13)
    assert channels.polarization == pytest.approx(1, abs=1e-13)

    cosines, weights = leggauss(5)
    actual = np.array([
        4 * pi * analyzer_channels(transition, density, acos(cosine)).sum()
        for cosine in cosines
    ])
    np.testing.assert_allclose(actual, (15 / 2) * (1 - cosines**2) * cosines**2, atol=1e-13)
    assert weights @ actual / 2 == pytest.approx(1, abs=1e-13)
    assert analyzer_channels(transition, density, pi / 2).sum() == pytest.approx(0, abs=1e-28)


def test_forbidden_m1_pure_forward_has_no_mixing_pdf():
    with pytest.raises(ValueError):
        Transition(2, 0, ("M1", "E2"))

    transition = Transition(2, 0, ("E2",))
    independent = ref.Transition.pure(2, 0, "E", 2)
    for theta in (0.0, pi / 4, pi / 2, pi):
        parallel, perpendicular = analyzer_channels(transition, np.eye(5) / 5, theta)
        channels = ref.singles((0.2,) * 5, independent, theta)
        assert 4 * pi * (parallel + perpendicular) == pytest.approx(1, abs=1e-13)
        assert (parallel - perpendicular) / (parallel + perpendicular) == pytest.approx(0, abs=1e-13)
        assert channels.total == pytest.approx(1, abs=1e-13)
        assert channels.polarization == pytest.approx(0, abs=1e-13)

    job = JobRequest(
        mode="P_ADO", target=transition,
        geometry=Geometry(theta_a_deg=125, theta_b_deg=90, theta_p_deg=0),
        polarization=Measurement(0, 0.1075, 0.1075),
        angular_ratio=Measurement(1, 0.1, 0.1),
    )
    node_response = evaluate_response(job, np.array([0.0]), np.array([1e-100]))
    assert not node_response.valid[0, 0]
    assert np.isnan(node_response.polarization[0, 0])
    with pytest.raises(ValueError, match="pure one-component"):
        map_density(job, node_response)


@pytest.mark.parametrize("mode", ("P_ADO", "P_DCO", "PDCO"))
def test_exact_pure_e2_observation_can_invert_as_mix_allowed(mode):
    grid = GridSpec(
        xi_min_rad=radians(-89.9), xi_max_rad=radians(89.9), xi_points=157, sigma_points=51
    )
    pure = JobRequest(
        mode=mode,
        target=Transition(5, 4, ("E2",)),
        gate=None if mode == "P_ADO" else Transition(4, 2, ("E2",)),
        geometry=Geometry(
            theta_a_deg=125, theta_b_deg=90, theta_p_deg=90,
            theta_gate_p_deg=125,
            ratio_azimuth_average=mode != "P_ADO",
            polarization_gate_azimuth_average=mode == "PDCO",
        ),
        polarization=Measurement(0, 0.1075, 0.1075),
        angular_ratio=Measurement(1, 0.1, 0.1),
        grid=grid,
    )
    point = evaluate_response(pure, np.array([0.0]), np.array([1.5]))
    assert point.valid[0, 0]
    observed_p, observed_r = point.polarization.item(), point.angular_ratio.item()
    p_error, r_error = max(0.1075, 0.8 * abs(observed_p)), 0.1 * abs(observed_r)
    mixed = replace(
        pure, target=Transition(5, 4, ("M1", "E2")),
        polarization=Measurement(observed_p, p_error, p_error),
        angular_ratio=Measurement(observed_r, r_error, r_error),
    )
    endpoints = evaluate_response(mixed, np.array([-pi / 2, pi / 2]), np.array([1.5]))
    np.testing.assert_allclose(endpoints.polarization, observed_p, atol=1e-13)
    np.testing.assert_allclose(endpoints.angular_ratio, observed_r, atol=1e-13)

    response = evaluate_response(mixed)
    summary = summarize_density(map_density(mixed, response), masses=(0.68,))
    assert np.all(np.isfinite(summary.delta.coordinate))
    assert np.all(np.abs(summary.arctan_delta.coordinate) < pi / 2)
    assert np.all(summary.arctan_delta.density[np.abs(response.xi_rad) >= radians(85)] > 0)
    (hdi,) = summary.arctan_delta.intervals
    assert sum(segment.mass for segment in hdi.hdi_segments) == pytest.approx(0.68, abs=1e-6)
