from dataclasses import replace

import numpy as np
import pytest

from multipolepdm.contracts import Geometry, JobRequest, Measurement, Transition
from multipolepdm.io.input import example_data, job_from_dict
from multipolepdm.models.registry import evaluate_response
from multipolepdm.physics.joint import (
    azimuth_mean_channels,
    joint_channels,
    single_channels,
)
from multipolepdm.physics.populations import initial_population
from multipolepdm.physics.detectors import DetectorDirection, DetectorGroup


def test_ring_gate_is_not_an_unconditional_single_line_or_mean_polarization():
    obs = Measurement(0, 0.1, 0.1)
    job = JobRequest(
        "PDCO",
        Transition(0, 1, ("E1",)),
        obs,
        obs,
        gate=Transition(1, 0, ("E1",)),
        geometry=Geometry(polarization_gate_azimuth_average=True),
    )
    response = evaluate_response(job, np.array([0.0]), np.array([1.0]))
    assert response.polarization[0, 0] == pytest.approx(1 / 3, abs=3e-14)
    single = evaluate_response(
        replace(job, mode="P_DCO"), np.array([0.0]), np.array([1.0])
    )
    assert single.polarization[0, 0] == pytest.approx(0, abs=3e-14)
    phi = np.arange(72) * (2 * np.pi / 72)
    points = np.array(
        [
            joint_channels(job, 0.0, np.ones((1, 1)), (np.pi / 2, 0), (np.pi / 2, x))
            for x in phi
        ]
    )
    wrong = np.mean((points[:, 0] - points[:, 1]) / points.sum(axis=1))
    assert wrong == pytest.approx(np.sqrt(2) - 1, abs=1e-12)
    assert abs(wrong - response.polarization[0, 0]) > 0.05


@pytest.mark.parametrize("target_first", [True, False])
def test_both_averaged_responses_match_raw_intensity_quadrature(target_first):
    obs = Measurement(0, 0.1, 0.1)
    target, gate = (
        (Transition(5, 4), Transition(4, 2, ("E2",)))
        if target_first
        else (Transition(4, 3), Transition(6, 4, ("E2",)))
    )
    geometry = Geometry(
        theta_a_deg=42,
        theta_b_deg=90,
        theta_p_deg=77,
        phi_p_deg=23,
        theta_gate_p_deg=58,
        ratio_azimuth_average=True,
        polarization_gate_azimuth_average=True,
    )
    job = JobRequest(
        "PDCO",
        target,
        obs,
        obs,
        gate=gate,
        target_first=target_first,
        geometry=geometry,
    )
    xi, sigma = np.array([-0.7, 0.6]), np.array([0.8, 1.5])
    response = evaluate_response(job, xi, sigma)
    phi = np.arange(18) * (2 * np.pi / 18)
    for s, width in enumerate(sigma):
        rho = np.diag(initial_population(job.reference_spin, width))
        for i, angle in enumerate(xi):
            p = np.mean(
                [
                    joint_channels(
                        job,
                        angle,
                        rho,
                        tuple(np.deg2rad([77, 23])),
                        (np.deg2rad(58), x),
                    )
                    for x in phi
                ],
                axis=0,
            )
            numerator = np.mean(
                [
                    joint_channels(
                        job, angle, rho, (np.deg2rad(42), 0), (np.pi / 2, x)
                    ).sum()
                    for x in phi
                ]
            )
            denominator = np.mean(
                [
                    joint_channels(
                        job, angle, rho, (np.pi / 2, 0), (np.deg2rad(42), x)
                    ).sum()
                    for x in phi
                ]
            )
            assert response.polarization[s, i] == pytest.approx(
                (p[0] - p[1]) / p.sum(), abs=2e-13
            )
            assert response.angular_ratio[s, i] == pytest.approx(
                numerator / denominator, abs=2e-13
            )


def test_p_dco_single_p_does_not_acquire_a_gate_condition_when_ratio_is_averaged():
    job = job_from_dict(example_data("P_DCO"))
    job = replace(job, geometry=replace(job.geometry, select_azimuth=True))
    xi, sigma = np.array([-0.7, 0.6]), np.array([0.8, 1.5])
    point = evaluate_response(job, xi, sigma)
    averaged_job = replace(
        job, geometry=replace(job.geometry, ratio_azimuth_average=True)
    )
    averaged = evaluate_response(averaged_job, xi, sigma)
    np.testing.assert_array_equal(point.polarization, averaged.polarization)
    assert np.max(abs(point.angular_ratio - averaged.angular_ratio)) > 1e-3
    changed = evaluate_response(
        replace(
            averaged_job,
            geometry=replace(
                averaged_job.geometry,
                ratio_group_b=replace(
                    averaged_job.geometry.ratio_group_b,
                    directions=tuple(
                        replace(row, phi_deg=row.phi_deg + 137)
                        for row in averaged_job.geometry.ratio_group_b.directions
                    ),
                ),
            ),
        ),
        xi,
        sigma,
    )
    np.testing.assert_array_equal(averaged.angular_ratio, changed.angular_ratio)


def test_polarization_azimuth_average_does_not_modify_dco():
    job = job_from_dict(example_data("PDCO"))
    job = replace(job, geometry=replace(job.geometry, select_azimuth=True))
    axes = (np.array([-0.7, 0.6]), np.array([0.8, 1.5]))
    point = evaluate_response(job, *axes)
    averaged = evaluate_response(
        replace(
            job, geometry=replace(job.geometry, polarization_gate_azimuth_average=True)
        ),
        *axes,
    )
    np.testing.assert_array_equal(point.angular_ratio, averaged.angular_ratio)
    assert np.max(abs(point.polarization - averaged.polarization)) > 1e-3


def test_averaged_gate_restores_axial_zero_polarization_at_the_beam():
    job = job_from_dict(example_data("PDCO"))
    job = replace(
        job,
        geometry=replace(
            job.geometry,
            polarization_group=DetectorGroup((DetectorDirection(0),)),
            polarization_gate_group=DetectorGroup((DetectorDirection(90),)),
            polarization_gate_azimuth_average=True,
        ),
    )
    r = evaluate_response(job, np.array([-0.7, 0.6]), np.array([0.8, 1.5]))
    np.testing.assert_array_equal(r.polarization, 0)


def test_ring_average_agrees_with_independent_recoupled_reference():
    from reference import angular_correlation as ref

    obs = Measurement(0, 0.1, 0.1)
    job = JobRequest(
        "PDCO",
        Transition(3, 2),
        obs,
        obs,
        gate=Transition(2, 0, ("E2",)),
        geometry=Geometry(
            theta_p_deg=81,
            phi_p_deg=13,
            theta_gate_p_deg=47,
            polarization_gate_azimuth_average=True,
        ),
    )
    xi, width = 0.4, 0.9
    rho = np.diag(initial_population(3, width))
    channels = azimuth_mean_channels(
        job, xi, rho, tuple(np.deg2rad([81, 13])), np.deg2rad(47)
    )
    first, last = (
        ref.Transition.mixed(3, 2, np.tan(xi)),
        ref.Transition.pure(2, 0, "E", 2),
    )
    values = [
        ref.joint(
            ref.gaussian(3, width),
            first,
            last,
            tuple(np.deg2rad([81, 13])),
            (np.deg2rad(47), p),
            target=1,
        )
        for p in np.arange(17) * 2 * np.pi / 17
    ]
    expected = (
        np.mean([[x.parallel, x.perpendicular] for x in values], axis=0)
        / (4 * np.pi) ** 2
    )
    np.testing.assert_allclose(channels, expected, rtol=1e-12, atol=3e-14)
