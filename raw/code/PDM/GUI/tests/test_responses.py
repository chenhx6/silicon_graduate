from dataclasses import replace

import numpy as np
import pytest
from numpy.polynomial.legendre import leggauss

from multipolepdm.contracts import Geometry, JobRequest, Measurement, Transition
from multipolepdm.models.registry import evaluate_response
from multipolepdm.physics.joint import joint_channels, single_channels
from multipolepdm.physics.populations import initial_population


def make_job(mode="P_DCO", target_first=True, intermediates=()):
    obs = Measurement(0.3, 0.05, 0.05)
    if target_first:
        target, gate = (
            Transition(5, 4),
            Transition(
                4 if not intermediates else 3, 2 if not intermediates else 1, ("E2",)
            ),
        )
    else:
        target, gate = Transition(4, 3), Transition(6, 4, ("E2",))
    return JobRequest(
        mode,
        target,
        obs,
        obs,
        gate=gate,
        target_first=target_first,
        intermediates=intermediates,
    )


@pytest.mark.parametrize("target_first", [True, False])
def test_p_dco_single_p_gate_angle_invariant(target_first):
    job = make_job(target_first=target_first)
    a = evaluate_response(job, np.array([-0.5, 0.5]), np.array([0.8, 1.5]))
    b = evaluate_response(
        replace(job, geometry=Geometry(theta_a_deg=70, theta_b_deg=20)),
        np.array([-0.5, 0.5]),
        np.array([0.8, 1.5]),
    )
    np.testing.assert_allclose(a.polarization, b.polarization, atol=2e-14)
    assert np.max(abs(a.angular_ratio - b.angular_ratio)) > 1e-3


@pytest.mark.parametrize("first", [True, False])
def test_target_second_singles_matches_transfer(first):
    job = make_job(target_first=first)
    rho = np.diag(initial_population(job.reference_spin, 1.1))
    direction = (1.2, 0.3)
    total = np.zeros(2)
    xs, ws = leggauss(7)
    for x, w in zip(xs, ws):
        for phi in np.arange(10) * 2 * np.pi / 10:
            total += (
                w
                * 2
                * np.pi
                / 10
                * joint_channels(job, -0.4, rho, direction, (np.arccos(x), phi))
            )
    np.testing.assert_allclose(
        total, single_channels(job, -0.4, rho, direction), atol=3e-14
    )


def test_dco_joint_gate_weight_preserved():
    job = make_job()
    rho = np.diag(initial_population(5, 1.2))
    a = joint_channels(job, 0.4, rho, (0.5, 0), (1.5, 0.3))
    np.testing.assert_allclose(
        joint_channels(job, 0.4, 17 * rho, (0.5, 0), (1.5, 0.3)), 17 * a
    )
    original = evaluate_response(job, np.array([-0.4, 0.4]), np.array([1.0]))
    swapped = evaluate_response(
        replace(job, geometry=replace(job.geometry, theta_a_deg=30, theta_b_deg=90)),
        np.array([-0.4, 0.4]),
        np.array([1.0]),
    )
    np.testing.assert_allclose(
        original.angular_ratio * swapped.angular_ratio, 1, atol=2e-14
    )


def test_pdco_fixed_gate_polarization():
    job = make_job("PDCO")
    a = evaluate_response(job, np.array([-0.5, 0.5]), np.array([1.0]))
    b = evaluate_response(
        replace(job, geometry=replace(job.geometry, theta_gate_p_deg=35)),
        np.array([-0.5, 0.5]),
        np.array([1.0]),
    )
    np.testing.assert_allclose(a.angular_ratio, b.angular_ratio)
    assert np.max(abs(a.polarization - b.polarization)) > 1e-3


def test_nonadjacent_relative_azimuth():
    job = make_job(intermediates=(Transition(4, 3, ("M1",)),))
    a = evaluate_response(job, np.array([-0.4, 0.4]), np.array([1.0]))
    b = evaluate_response(
        replace(job, geometry=replace(job.geometry, relative_phi_deg=70)),
        np.array([-0.4, 0.4]),
        np.array([1.0]),
    )
    np.testing.assert_allclose(a.polarization, b.polarization)
    assert np.max(abs(a.angular_ratio - b.angular_ratio)) > 1e-3


def test_quadratic_grid_agrees_direct_trace():
    job = make_job("PDCO")
    xi, sig = np.array([-0.7, 0.23, 0.8]), np.array([0.8, 1.3])
    result = evaluate_response(job, xi, sig)
    for s, sigma in enumerate(sig):
        for i, x in enumerate(xi):
            rho = np.diag(initial_population(job.reference_spin, sigma))
            p = joint_channels(job, x, rho, (np.pi / 2, 0), (np.pi / 2, 0))
            assert result.polarization[s, i] == pytest.approx(
                (p[0] - p[1]) / p.sum(), abs=1e-13
            )


@pytest.mark.parametrize("mode", ["P_ADO", "P_DCO", "PDCO"])
@pytest.mark.parametrize("angles", [(0, 180), (35, 145), (85, 95), (35.1, 144.9)])
def test_equivalent_angle_pairs_do_not_map_roundoff_into_a_pdf(mode, angles):
    from multipolepdm.io.input import example_data, job_from_dict
    from multipolepdm.pdm.mapping import map_density

    job = replace(
        job_from_dict(example_data(mode)),
        geometry=Geometry(
            theta_a_deg=angles[0], theta_b_deg=angles[1], relative_phi_deg=73
        ),
    )
    response = evaluate_response(
        job, np.linspace(-1.5, 1.5, 121), np.linspace(0.2, 5, 51)
    )
    np.testing.assert_array_equal(response.angular_ratio[response.valid], 1.0)
    with pytest.raises(ValueError, match="Jacobian is zero"):
        map_density(job, response)


def test_beam_polarization_keeps_the_conditional_gate_distinction():
    job = replace(make_job(), geometry=Geometry(theta_p_deg=0, theta_gate_p_deg=90))
    xi, sigma = np.array([-0.4, 0.4]), np.array([0.8, 1.5])
    single = evaluate_response(job, xi, sigma)
    conditional = evaluate_response(replace(job, mode="PDCO"), xi, sigma)
    np.testing.assert_array_equal(single.polarization, 0)
    assert np.max(abs(conditional.polarization)) > 0.01


def test_collinear_low_spin_helicity_rule_does_not_apply_across_a_gap():
    from multipolepdm.pdm.mapping import map_density

    obs = Measurement(0, 0.1, 0.1)
    job = JobRequest("PDCO", Transition(1, 1), obs, obs, gate=Transition(1, 0, ("M1",)))
    xi, sigma = np.linspace(-1.5, 1.5, 101), np.linspace(0.2, 1, 31)
    response = evaluate_response(job, xi, sigma)
    np.testing.assert_array_equal(response.polarization[response.valid], 0)
    with pytest.raises(ValueError, match="Jacobian is zero"):
        map_density(job, response)
    gap_job = replace(job, intermediates=(Transition(1, 1, ("M1",)),))
    assert np.max(abs(evaluate_response(gap_job, xi, sigma).polarization)) > 0.1


def test_nonzero_small_angle_is_not_rounded_to_a_beam_pole():
    from multipolepdm.io.input import example_data, job_from_dict

    job = replace(
        job_from_dict(example_data()),
        target=Transition(1, 0, ("E1",)),
        geometry=Geometry(theta_p_deg=1e-20),
    )
    response = evaluate_response(job, np.array([0.0]), np.array([1e-300]))
    assert response.polarization[0, 0] == pytest.approx(1)
