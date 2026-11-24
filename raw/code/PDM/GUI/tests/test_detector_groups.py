from dataclasses import replace
from itertools import product

import numpy as np
import pytest

from multipolepdm.contracts import Geometry, GridSpec, JobRequest, Measurement, Transition
from multipolepdm.models.registry import evaluate_response
from multipolepdm.pdm.mapping import map_density
from multipolepdm.physics.detectors import DetectorDirection, DetectorGroup
from multipolepdm.physics.joint import joint_channels, response_channels, single_channels
from multipolepdm.physics.populations import initial_population


def group(*rows, normalization="mean"):
    return DetectorGroup(
        tuple(DetectorDirection(*row) for row in rows), normalization=normalization
    )


def make_job(mode, geometry, *, target_first=True, separated=False):
    measurement = Measurement(0.2, 0.1, 0.1)
    if mode == "P_ADO":
        return JobRequest(
            mode, Transition(8.5, 7.5), measurement, measurement, geometry=geometry
        )
    if target_first:
        target = Transition(5, 4)
        gate = Transition(3, 1, ("E2",)) if separated else Transition(4, 2, ("E2",))
    else:
        target = Transition(3, 2) if separated else Transition(4, 3)
        gate = Transition(6, 4, ("E2",))
    return JobRequest(
        mode,
        target,
        measurement,
        measurement,
        gate=gate,
        target_first=target_first,
        intermediates=(Transition(4, 3, ("M1",)),) if separated else (),
        geometry=geometry,
    )


def density(job, sigma):
    return np.diag(initial_population(job.reference_spin, np.array([sigma]))[0])


def polarization(channels):
    return (channels[0] - channels[1]) / channels.sum()


@pytest.mark.parametrize(
    "row",
    [(-1,), (181,), (np.nan,), (90, np.inf), (90, 0, -1), (90, 0, np.nan)],
)
def test_group_direction_validation(row):
    with pytest.raises(ValueError):
        DetectorDirection(*row)


def test_group_weights_validation_and_normalization():
    rows = (DetectorDirection(80, 20, 2), DetectorDirection(70, 0, 0))
    assert DetectorGroup(rows).effective_weights == (1, 0)
    assert DetectorGroup(rows, "sum").effective_weights == (2, 0)
    for invalid in ((), rows[1:], ((90, 0, 1),)):
        with pytest.raises(ValueError):
            DetectorGroup(invalid)
    with pytest.raises(ValueError):
        DetectorGroup(rows, "automatic")


@pytest.mark.parametrize(
    "normalization,denominator_weight,expected_factor",
    [("mean", 1, 1), ("sum", 3, 1), ("sum", 1, 3)],
)
def test_135pr_legacy_ado_and_polarimeter(normalization, denominator_weight, expected_factor):
    geometry = Geometry(
        theta_a_deg=100,
        theta_b_deg=80,
        theta_p_deg=0,
        ratio_group_a=group(
            (157.6, 0, 2), (133.6, 0, 1), (25, 80, 0), normalization=normalization
        ),
        ratio_group_b=group((75.5, 0, denominator_weight), normalization=normalization),
        polarization_group=group((75.5,)),
    )
    job = make_job("P_ADO", geometry)
    xi_axis = np.array([-0.72, -0.1, 0.31, 1.15])
    sigma_axis = np.array([1.35, 3.0])
    response = evaluate_response(job, xi_axis, sigma_axis)
    for sigma_index, sigma in enumerate(sigma_axis):
        rho = density(job, sigma)
        for xi_index, xi in enumerate(xi_axis):
            far, near, polar = [
                single_channels(job, xi, rho, (np.deg2rad(theta), 0))
                for theta in (157.6, 133.6, 75.5)
            ]
            expected = (2 * far.sum() + near.sum()) / (3 * polar.sum())
            assert response.angular_ratio[sigma_index, xi_index] == pytest.approx(
                expected_factor * expected, abs=2e-13
            )
            assert response.polarization[sigma_index, xi_index] == pytest.approx(
                polarization(polar), abs=2e-13
            )
    info = response.metadata["detector_groups"]["ratio_group_a"]
    assert info["normalization"] == normalization
    expected_weights = [2 / 3, 1 / 3, 0] if normalization == "mean" else [2, 1, 0]
    assert [row["effective_weight"] for row in info["directions"]] == expected_weights
    assert response.metadata["exact_observable_identities"] == {
        "unit_ratio": False,
        "zero_linear_polarization": False,
    }
    assert np.max(np.abs(response.polarization)) > 1e-3


@pytest.mark.parametrize("mode", ["P_ADO", "P_DCO", "PDCO"])
@pytest.mark.parametrize("select_azimuth", [True, False])
def test_single_row_group_matches_scalar_geometry(mode, select_azimuth):
    scalar = Geometry(
        theta_a_deg=66,
        theta_b_deg=141,
        relative_phi_deg=42,
        theta_p_deg=83,
        phi_p_deg=29,
        theta_gate_p_deg=52,
        phi_gate_p_deg=151,
        ratio_azimuth_average=not select_azimuth,
        polarization_gate_azimuth_average=not select_azimuth,
    )
    grouped = replace(
        scalar,
        ratio_group_a=group((66, 0, 9)),
        ratio_group_b=group((141, 42)),
        polarization_group=group((83, 29)),
        polarization_gate_group=group((52, 151)),
        select_azimuth=select_azimuth,
    )
    axes = (np.array([-0.3, 0.63]), np.array([0.8, 1.7]))
    baseline = evaluate_response(make_job(mode, scalar), *axes)
    actual = evaluate_response(make_job(mode, grouped), *axes)
    np.testing.assert_allclose(actual.polarization, baseline.polarization, atol=2e-13, rtol=0)
    np.testing.assert_allclose(actual.angular_ratio, baseline.angular_ratio, atol=2e-13, rtol=0)
    np.testing.assert_array_equal(actual.valid, baseline.valid)


def point_channels(job, xi, rho, target, gate):
    return joint_channels(job, xi, rho, np.deg2rad(target[:2]), np.deg2rad(gate[:2]))


@pytest.mark.parametrize("target_first", [True, False])
def test_weighted_pairs_and_analyzers_follow_cascade_order(target_first):
    rows_a = ((67, 37, 2.0), (119, -21, 1.0))
    rows_b = ((36, 93, 1.0), (154, 201, 4.0))
    rows_p = ((90, 19, 2.0), (29, 124, 1.0))
    rows_gate_p = ((52, 17, 1.0), (141, 88, 5.0))
    geometry = Geometry(
        ratio_group_a=group(*rows_a, normalization="sum"),
        ratio_group_b=group(*rows_b),
        polarization_group=group(*rows_p),
        polarization_gate_group=group(*rows_gate_p, normalization="sum"),
        select_azimuth=True,
    )
    job = make_job("PDCO", geometry, target_first=target_first, separated=True)
    xi, sigma = 0.37, 1.21
    rho = density(job, sigma)
    ratio_channels = [
        np.array(
            [
                point_channels(job, xi, rho, target, gate).sum(),
                point_channels(job, xi, rho, gate, target).sum(),
            ]
        )
        for target, gate in product(rows_a, rows_b)
    ]
    ratio_weights = np.array(
        [target[2] * gate[2] / 5 for target, gate in product(rows_a, rows_b)]
    )
    ratio_sums = ratio_weights @ ratio_channels
    expected_ratio = ratio_sums[0] / ratio_sums[1]
    ratio_average = np.average(
        [channels[0] / channels[1] for channels in ratio_channels], weights=ratio_weights
    )
    analyzer_channels = [
        point_channels(job, xi, rho, target, gate)
        for target, gate in product(rows_p, rows_gate_p)
    ]
    analyzer_weights = np.array(
        [target[2] / 3 * gate[2] for target, gate in product(rows_p, rows_gate_p)]
    )
    expected_p = polarization(analyzer_weights @ analyzer_channels)
    analyzer_average = np.average(
        [polarization(channels) for channels in analyzer_channels],
        weights=analyzer_weights,
    )
    pdco = evaluate_response(job, [xi], [sigma])
    p_dco = evaluate_response(replace(job, mode="P_DCO"), [xi], [sigma])
    expected_singles = polarization(
        sum(
            weight / 3 * single_channels(job, xi, rho, np.deg2rad((theta, phi)))
            for theta, phi, weight in rows_p
        )
    )
    assert pdco.angular_ratio[0, 0] == pytest.approx(expected_ratio, abs=2e-13)
    assert p_dco.angular_ratio[0, 0] == pytest.approx(expected_ratio, abs=2e-13)
    assert pdco.polarization[0, 0] == pytest.approx(expected_p, abs=2e-13)
    assert p_dco.polarization[0, 0] == pytest.approx(expected_singles, abs=2e-13)
    assert abs(expected_ratio - ratio_average) > 1e-4
    assert abs(expected_p - analyzer_average) > 1e-4
    assert abs(expected_p - expected_singles) > 1e-4


def test_ring_average_integrates_channels_and_ignores_declared_phi():
    geometry = Geometry(
        ratio_group_a=group((70, 27)),
        ratio_group_b=group((140, 152)),
        polarization_group=group((77, 24)),
        polarization_gate_group=group((52, 98)),
    )
    ring_job = make_job("PDCO", geometry)
    xi, sigma = 0.31, 1.8
    rho = density(ring_job, sigma)
    nodes = np.linspace(0, 360, 37, endpoint=False)

    def average(target_theta, gate_theta):
        return np.mean(
            [
                point_channels(
                    ring_job, xi, rho, (target_theta, 13), (gate_theta, node)
                )
                for node in nodes
            ],
            axis=0,
        )

    ring = evaluate_response(ring_job, [xi], [sigma])
    expected_p = polarization(average(77, 52))
    expected_ratio = average(70, 140).sum() / average(140, 70).sum()
    assert ring.polarization[0, 0] == pytest.approx(expected_p, abs=2e-13)
    assert ring.angular_ratio[0, 0] == pytest.approx(expected_ratio, abs=2e-13)
    at_zero = replace(geometry, polarization_gate_group=group((52, 24)))
    for point_geometry in (geometry, at_zero):
        point = evaluate_response(
            replace(ring_job, geometry=replace(point_geometry, select_azimuth=True)),
            [xi],
            [sigma],
        )
        assert abs(point.polarization[0, 0] - expected_p) > 1e-4
        assert abs(point.angular_ratio[0, 0] - expected_ratio) > 1e-4
    assert ring.metadata["ratio_azimuth_average"]
    assert ring.metadata["polarization_gate_azimuth_average"]
    assert not ring.metadata["select_azimuth"]


@pytest.mark.parametrize("mode", ["P_ADO", "P_DCO", "PDCO"])
@pytest.mark.parametrize("mirror", [False, True])
def test_equivalent_full_groups_produce_zero_jacobian(mode, mirror):
    group_a = group((49, 37, 2), (72, -20, 1))
    group_b = (
        group((108, 102, 2), (131, 64, 4)) if mirror else
        group((72, 340, 2), (49, 37, 4), (90, 0, 0))
    )
    job = make_job(
        mode,
        Geometry(
            ratio_group_a=group_a,
            ratio_group_b=group_b,
            polarization_group=group((77, 24)),
            polarization_gate_group=group((52, 98)),
            select_azimuth=not mirror,
        ),
    )
    axes = (np.array([-0.73, 0.23, 0.91]), np.array([0.8, 1.7, 3]))
    _, raw = response_channels(job, *axes, conditional=(mode == "PDCO"))
    np.testing.assert_allclose(raw[0] / raw[1], 1.0, atol=2e-13, rtol=0)
    response = evaluate_response(job, *axes)
    assert response.valid.all()
    assert np.ptp(response.polarization) > 1e-3
    np.testing.assert_array_equal(response.angular_ratio, 1.0)
    assert response.metadata["exact_observable_identities"]["unit_ratio"]
    with pytest.raises(ValueError, match="Jacobian is zero"):
        map_density(job, response)


def test_proportional_ado_groups_can_have_nonunit_constant_ratio():
    job = make_job(
        "P_ADO",
        Geometry(
            ratio_group_a=group((50, 0, 6), (82, 0, 3), normalization="sum"),
            ratio_group_b=group((98, 0, 1), (130, 0, 2), normalization="sum"),
        ),
    )
    axes = (np.array([-0.73, 0.23, 0.91]), np.array([0.8, 1.7, 3]))
    response = evaluate_response(job, *axes)
    np.testing.assert_array_equal(response.angular_ratio, 3.0)
    assert not response.metadata["exact_observable_identities"]["unit_ratio"]
    with pytest.raises(ValueError, match="Jacobian is zero"):
        map_density(job, response)


@pytest.mark.parametrize("mode", ["P_ADO", "P_DCO", "PDCO"])
def test_all_polarimeter_rows_at_poles_produce_zero_jacobian(mode):
    job = make_job(
        mode,
        Geometry(
            ratio_group_a=group((61, 22)),
            ratio_group_b=group((23, 78)),
            polarization_group=group((0, 77, 2), (180, 11, 4), (99, 0, 0)),
            polarization_gate_group=group((71, 27)),
        ),
    )
    axes = (np.array([-0.73, 0.23, 0.91]), np.array([0.8, 1.7, 3]))
    response = evaluate_response(job, *axes)
    assert response.valid.all()
    assert np.ptp(response.angular_ratio) > 1e-3
    np.testing.assert_array_equal(response.polarization, 0.0)
    assert response.metadata["exact_observable_identities"]["zero_linear_polarization"]
    with pytest.raises(ValueError, match="Jacobian is zero"):
        map_density(job, response)


def test_near_mirrored_angles_do_not_trigger_an_identity():
    job = make_job(
        "P_ADO",
        Geometry(
            theta_a_deg=90,
            theta_b_deg=90,
            ratio_group_a=group((71,)),
            ratio_group_b=group((np.nextafter(109.0, 180),)),
        ),
    )
    response = evaluate_response(job, [0.17], [1.4])
    assert not response.metadata["exact_observable_identities"]["unit_ratio"]


def test_grid_metadata_describes_actual_axes_and_skips_single_points():
    job = replace(
        make_job("P_ADO", Geometry(ratio_group_a=group((71,)))),
        grid=GridSpec(xi_step_rad=0.3, sigma_step=0.5),
    )
    response = evaluate_response(job, [-0.3, 0, 0.1], [0.8, 1.3, 1.5])
    info = response.metadata["grid"]
    assert info["arctan_delta_rad"]["requested_step"] == 0.3
    assert info["arctan_delta_rad"]["last_step"] == pytest.approx(0.1)
    assert info["sigma"]["requested_step"] == 0.5
    assert info["sigma"]["last_step"] == pytest.approx(0.2)
    assert evaluate_response(job, [0], [1]).metadata["grid"] == {}
    assert set(evaluate_response(job, [0], [1, 1.5]).metadata["grid"]) == {"sigma"}
