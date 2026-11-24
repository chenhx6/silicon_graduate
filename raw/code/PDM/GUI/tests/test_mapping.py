from math import sqrt

import numpy as np
import pytest
from scipy.integrate import quad, trapezoid
from scipy.special import ndtr
from scipy.stats import norm

from multipolepdm.contracts import JobRequest, Measurement, ResponseGrid, Transition
from multipolepdm.models.registry import evaluate_response
from multipolepdm.pdm.mapping import map_density
from multipolepdm.pdm.observations import measurement_density, observation_density


def _job(mode="P_ADO", **changes):
    inputs = {
        "target": Transition(4, 3),
        "polarization": Measurement(0, 0.2, 0.2),
        "angular_ratio": Measurement(1.2, 0.2, 0.2),
    }
    if mode != "P_ADO":
        inputs["gate"] = Transition(3, 2, ("E2",))
    return JobRequest(mode, **(inputs | changes))


def _response(job, xi, sigma, polar, ratio, valid=None):
    if valid is None:
        valid = np.ones(polar.shape, dtype=bool)
    return ResponseGrid(
        xi, sigma, polar, ratio, valid, job.reference_spin, job.ratio_name
    )


@pytest.mark.parametrize("mode", ["P_ADO", "P_DCO", "PDCO"])
def test_identity_mapping_has_unit_jacobian_and_expected_finite_mass(mode):
    job = _job(mode)
    xi, sigma = np.linspace(-0.8, 0.8, 401), np.linspace(0.4, 2.0, 401)
    polar, ratio = np.meshgrid(xi, sigma)
    mapped = map_density(job, _response(job, xi, sigma, polar, ratio))

    np.testing.assert_allclose(mapped.jacobian, 1, atol=1e-14)
    expected_density = norm.pdf(polar, 0, 0.2) * norm.pdf(ratio, 1.2, 0.2)
    np.testing.assert_allclose(mapped.observation_density, expected_density)
    np.testing.assert_allclose(
        mapped.parameter_density, expected_density / mapped.normalization
    )
    expected_mass = (ndtr(4) - ndtr(-4)) ** 2
    assert mapped.normalization == pytest.approx(expected_mass, abs=1e-7)
    assert trapezoid(
        trapezoid(mapped.parameter_density, xi, axis=1), sigma
    ) == pytest.approx(1)


def test_absolute_jacobian_with_nonuniform_quadratic_response_including_edges():
    job = _job()
    xi = np.array([-0.8, -0.45, -0.1, 0.2, 0.7])
    sigma = np.array([0.2, 0.5, 0.6, 1.1, 1.7, 2.3])
    angle, width = np.meshgrid(xi, sigma)
    polar = -angle + angle**2 / 4 + width / 2
    ratio = angle / 3 + width**2
    mapped = map_density(job, _response(job, xi, sigma, polar, ratio))
    np.testing.assert_allclose(
        mapped.jacobian, (1 - angle / 2) * 2 * width + 1 / 6, atol=1e-14
    )


@pytest.mark.parametrize("invalid_source", ["mask", "nonfinite_value"])
def test_invalid_response_breaks_full_stencil_without_bridging_gap(invalid_source):
    job = _job()
    xi, sigma = np.linspace(-0.8, 0.8, 11), np.linspace(0.4, 2, 7)
    polar, ratio = np.meshgrid(xi, sigma)
    valid = np.ones(polar.shape, dtype=bool)
    if invalid_source == "mask":
        valid[3, 5] = False
    else:
        ratio[3, 5] = np.inf
    mapped = map_density(job, _response(job, xi, sigma, polar, ratio, valid))

    undefined = np.zeros_like(valid)
    undefined[2:5, 5] = True
    undefined[3, 4:7] = True
    np.testing.assert_array_equal(np.isnan(mapped.jacobian), undefined)
    np.testing.assert_allclose(mapped.jacobian[~undefined], 1)
    assert mapped.observation_density[3, 5] == 0
    assert mapped.observation_density[3, 4] > 0
    assert not mapped.parameter_density[undefined].any()
    assert any("undefined at 5 grid points" in message for message in mapped.warnings)


def test_no_defined_stencils_reports_mask():
    job = _job()
    xi, sigma = np.linspace(-0.8, 0.8, 5), np.linspace(0.4, 2, 5)
    polar, ratio = np.meshgrid(xi, sigma)
    valid = np.eye(5, dtype=bool)
    with pytest.raises(ValueError, match="No finite Jacobian.*mask"):
        map_density(job, _response(job, xi, sigma, polar, ratio, valid))


def test_all_zero_jacobian_rejects_degenerate_response():
    job = _job()
    xi, sigma = np.linspace(-0.8, 0.8, 9), np.linspace(0.4, 2, 7)
    polar, ratio = np.meshgrid(xi, sigma)
    ratio[:] = polar
    with pytest.raises(
        ValueError, match="Jacobian is zero at every defined grid point"
    ):
        map_density(job, _response(job, xi, sigma, polar, ratio))


def test_small_positive_jacobian_is_retained_and_reported():
    job = _job()
    xi, sigma = np.linspace(-0.8, 0.8, 9), np.linspace(0.4, 2, 7)
    polar, ratio = np.meshgrid(xi, sigma)
    mapped = map_density(job, _response(job, xi, sigma, 1e-13 * polar, ratio))
    np.testing.assert_allclose(mapped.jacobian, 1e-13, rtol=1e-13, atol=0)
    assert (mapped.parameter_density > 0).all()
    assert any("Near-singular Jacobian" in message for message in mapped.warnings)


@pytest.mark.parametrize("sigma_field", ["polarization", "angular_ratio"])
def test_tiny_but_relatively_resolved_sigma_response_is_retained(sigma_field):
    job = _job()
    xi, sigma = np.linspace(-0.8, 0.8, 9), np.linspace(0.4, 2, 7)
    angle, width = np.meshgrid(xi, sigma)
    tiny_width = 1e-16 * width
    polar, ratio = (
        (tiny_width, angle) if sigma_field == "polarization" else (angle, tiny_width)
    )
    mapped = map_density(job, _response(job, xi, sigma, polar, ratio))
    np.testing.assert_allclose(mapped.jacobian, 1e-16, rtol=1e-13, atol=0)
    assert (mapped.parameter_density > 0).all()


def test_production_near_aligned_scan_has_no_resolved_sigma_variation():
    job = _job(
        polarization=Measurement(0, 0.3, 0.3), angular_ratio=Measurement(1, 0.3, 0.3)
    )
    xi, sigma = np.linspace(-0.7, 0.7, 141), np.linspace(0.112, 0.120, 9)
    response = evaluate_response(job, xi, sigma)
    with pytest.raises(
        ValueError, match="No resolved sigma variation in either response field"
    ):
        map_density(job, response)

    wider = evaluate_response(job, xi, np.linspace(0.112, 0.15, 9))
    assert map_density(job, wider).normalization > 0


def test_masked_response_outlier_does_not_make_sigma_variation_resolved():
    job = _job()
    xi, sigma = np.linspace(-0.8, 0.8, 9), np.linspace(0.4, 2, 7)
    polar, width = np.meshgrid(xi, sigma)
    ratio = 1 + 8 * np.finfo(float).eps * width
    valid = np.ones(polar.shape, dtype=bool)
    valid[3, 4] = False
    ratio[3, 4] = 10
    with pytest.raises(
        ValueError, match="No resolved sigma variation in either response field"
    ):
        map_density(job, _response(job, xi, sigma, polar, ratio, valid))


def test_edge_mass_warning_includes_axis_and_side():
    job = _job(polarization=Measurement(-0.75, 0.012, 0.012))
    xi, sigma = np.linspace(-0.8, 0.8, 201), np.linspace(0.4, 2.0, 201)
    polar, ratio = np.meshgrid(xi, sigma)
    mapped = map_density(job, _response(job, xi, sigma, polar, ratio))
    marginal = trapezoid(mapped.parameter_density, sigma, axis=0)
    assert marginal[0] < 0.1 * marginal.max()
    assert any("xi_rad lower grid edge" in message for message in mapped.warnings)
    assert not any("upper grid edge" in message for message in mapped.warnings)


def test_narrow_flat_scan_warns_even_when_each_edge_strip_contains_little_mass():
    job = _job(
        polarization=Measurement(0, 0.3, 0.3), angular_ratio=Measurement(1, 0.3, 0.3)
    )
    xi, sigma = np.linspace(-0.1, 0.1, 401), np.linspace(0.9, 1.1, 401)
    polar, ratio = np.meshgrid(xi, sigma)
    mapped = map_density(job, _response(job, xi, sigma, polar, ratio))

    assert mapped.normalization == pytest.approx(0.0681822, abs=1e-7)
    edge_warnings = [message for message in mapped.warnings if "grid edge" in message]
    assert len(edge_warnings) == 4
    for axis_name in ("xi_rad", "sigma"):
        for side in ("lower", "upper"):
            warning = next(
                message for message in edge_warnings if f"{axis_name} {side}" in message
            )
            assert "finite scan bounds" in warning
            assert "of the marginal peak" in warning


def test_pure_target_requires_forward_only_path():
    job = _job(target=Transition(4, 3, ("E2",)))
    xi, sigma = np.linspace(-0.8, 0.8, 9), np.linspace(0.4, 2, 7)
    polar, ratio = np.meshgrid(xi, sigma)
    with pytest.raises(
        ValueError, match="pure one-component.*forward-only.*PDM PDF is undefined"
    ):
        map_density(job, _response(job, xi, sigma, polar, ratio))


@pytest.mark.parametrize("errors", [(0.3, 0.3), (0.12, 0.65)])
def test_measurement_density_matches_declared_normal_quantiles(errors):
    center = 0.2
    err_minus, err_plus = errors
    measurement = Measurement(center, err_minus, err_plus)

    below_error = quad(
        measurement_density, -np.inf, center - err_minus, args=(measurement,)
    )[0]
    below_center = quad(measurement_density, -np.inf, center, args=(measurement,))[0]
    upper_error_tail = quad(
        measurement_density, center + err_plus, np.inf, args=(measurement,)
    )[0]
    upper_half = quad(measurement_density, center, np.inf, args=(measurement,))[0]
    assert below_error == pytest.approx(ndtr(-1))
    assert below_center == pytest.approx(0.5)
    assert upper_half == pytest.approx(0.5)
    assert 1 - upper_error_tail == pytest.approx(ndtr(1))
    assert measurement_density(center, measurement) == pytest.approx(
        1 / (sqrt(2 * np.pi) * err_plus)
    )


def test_observation_density_combines_asymmetric_errors_independently():
    job = _job(
        polarization=Measurement(0, 0.1, 0.4), angular_ratio=Measurement(1, 0.2, 0.6)
    )
    polar, ratio = np.array([-0.1, 0.4]), np.array([1.6, 0.8])
    actual = observation_density(polar, ratio, job.polarization, job.angular_ratio)
    np.testing.assert_allclose(
        actual, norm.pdf(1) ** 2 / np.array([0.1 * 0.6, 0.4 * 0.2])
    )
