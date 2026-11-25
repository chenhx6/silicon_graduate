from math import sqrt

import numpy as np
import pytest
from scipy.integrate import trapezoid
from scipy.stats import norm

from multipolepdm.contracts import (
    JobRequest,
    MappingResult,
    Measurement,
    ResponseGrid,
    Transition,
)
from multipolepdm.pdm.mapping import map_density
from multipolepdm.pdm.statistics import summarize_density


def _result(xi, sigma, xi_density, sigma_density):
    job = JobRequest(
        "P_ADO", Transition(2, 1), Measurement(0, 0.2, 0.2), Measurement(1, 0.2, 0.2)
    )
    polar, ratio = np.meshgrid(xi, sigma)
    valid = np.ones(polar.shape, dtype=bool)
    response = ResponseGrid(
        xi, sigma, polar, ratio, valid, job.reference_spin, job.ratio_name
    )
    density = np.outer(sigma_density, xi_density)
    integral = trapezoid(trapezoid(density, xi, axis=1), sigma)
    return MappingResult(
        job,
        response,
        np.ones_like(density),
        np.ones_like(density),
        density / integral,
        integral,
    )


def _integrate_interval(marginal, left, right):
    coordinate, density = marginal.coordinate, marginal.density
    interior = coordinate[(coordinate > left) & (coordinate < right)]
    points = np.concatenate(([left], interior, [right]))
    return trapezoid(np.interp(points, coordinate, density), points)


def test_coordinate_scaling_preserves_probability_mass_on_coarse_grid_near_poles():
    xi = np.array([-1.56, -0.43, 0.29, 1.56])
    sigma = np.array([0.2, 0.7, 1.8, 2.1])
    xi_density = 1 + xi / 2
    sigma_density = np.array([1, 3, 4, 2])
    result = _result(xi, sigma, xi_density, sigma_density)
    summary = summarize_density(result)

    expected_s = sigma / result.response.reference_spin
    expected_s_density = (
        result.response.reference_spin * sigma_density / trapezoid(sigma_density, sigma)
    )
    np.testing.assert_allclose(summary.sigma_over_i.coordinate, expected_s)
    np.testing.assert_allclose(summary.sigma_over_i.density, expected_s_density)
    for marginal in (summary.sigma_over_i, summary.delta):
        assert trapezoid(marginal.density, marginal.coordinate) == pytest.approx(
            1, abs=1e-12
        )

    np.testing.assert_allclose(summary.delta.coordinate[[0, -1]], np.tan(xi[[0, -1]]))
    delta = summary.delta.coordinate
    expected_delta_density = (1 + np.arctan(delta) / 2) / (
        (1 + delta**2) * trapezoid(xi_density, xi)
    )
    np.testing.assert_allclose(summary.delta.density, expected_delta_density, rtol=2e-7)
    intervals = [(-1.56, -1.40), (-0.25, 0.51), (1.52, 1.56)]
    for left, right in intervals:
        exact_mass = ((right - left) + (right**2 - left**2) / 4) / trapezoid(
            xi_density, xi
        )
        assert _integrate_interval(
            summary.delta, np.tan(left), np.tan(right)
        ) == pytest.approx(exact_mass, abs=2e-7)


def test_delta_eti_and_hdi_for_uniform_xi():
    half_span = 1.5
    xi = np.array([-half_span, 0, half_span])
    sigma = np.array([1, 2, 3])
    result = _result(xi, sigma, np.ones(3), np.ones(3))
    delta = summarize_density(result).delta

    assert delta.median == pytest.approx(0, abs=5e-7)
    assert delta.mode == pytest.approx(np.tan(-half_span))
    assert delta.evaluation_coordinate == "arctan_delta"
    assert len(delta.intervals) == 1
    for interval in delta.intervals:
        endpoint = np.tan(half_span * interval.mass)
        assert interval.eti == pytest.approx((-endpoint, endpoint), abs=4e-6)
        assert len(interval.hdi) == 1
        assert interval.hdi[0] == pytest.approx(
            np.tan([-half_span, -half_span + 2 * half_span * interval.mass])
        )
        np.testing.assert_array_equal(interval.hdi_segments[0].mode_ranges, interval.hdi)
        assert interval.hdi_threshold == pytest.approx(1 / (2 * half_span))


def test_explicit_delta_pdf_and_tan_statistics_do_not_conflate_density_and_estimates():
    xi = np.array([-1.5, 0, 1.5])
    sigma = np.array([1, 2, 3])
    summary = summarize_density(_result(xi, sigma, np.ones(3), np.ones(3)))
    curve = summary.delta_pdf
    statistics = summary.tan_angle_statistics

    np.testing.assert_array_equal(curve.coordinate, summary.delta.coordinate)
    np.testing.assert_array_equal(curve.density, summary.delta.density)
    assert curve.coordinate_name == "delta"
    assert not any(hasattr(curve, name) for name in ("mean", "mode", "intervals"))
    assert not any(hasattr(statistics, name) for name in ("coordinate", "density", "mean", "std"))
    assert statistics.tan_mode == summary.delta.mode == pytest.approx(np.tan(-1.5))
    assert abs(curve.coordinate[np.argmax(curve.density)]) < 0.01
    assert statistics.tan_mean == summary.delta.mean
    assert statistics.tan_median == summary.delta.median
    assert statistics.tan_mean_std_endpoints == summary.delta.mean_bounds
    assert statistics.mean_bound_flags == summary.delta.mean_bound_flags
    assert statistics.evaluation_coordinate == "arctan_delta"
    assert statistics.transformation == "tan"
    for transformed, legacy in zip(statistics.intervals, summary.delta.intervals):
        assert transformed.tan_eti == legacy.eti
        assert transformed.tan_hdi_segments == legacy.hdi_segments
        assert transformed.angle_hdi_threshold == legacy.hdi_threshold
        assert sum(segment.mass for segment in transformed.tan_hdi_segments) == pytest.approx(0.68)


def test_bimodal_hdi_leaves_gap_and_reports_exact_threshold_and_mass():
    xi = np.array([-0.5, 0, 0.5])
    sigma = np.arange(1, 8)
    result = _result(xi, sigma, np.ones(3), [0, 1, 0, 0, 0, 1, 0])
    marginal = summarize_density(result).sigma_over_i

    assert marginal.median == pytest.approx(1.5)
    assert marginal.mode == pytest.approx(1)
    for interval in marginal.intervals:
        tail = (1 - interval.mass) / 2
        assert interval.eti == pytest.approx((0.5 + sqrt(tail), 3.5 - sqrt(tail)))
        assert interval.hdi_threshold == pytest.approx(sqrt(1 - interval.mass))
        half_width = (1 - interval.hdi_threshold) / 2
        np.testing.assert_allclose(
            interval.hdi,
            [(1 - half_width, 1 + half_width), (3 - half_width, 3 + half_width)],
        )
        masses = [_integrate_interval(marginal, *segment) for segment in interval.hdi]
        assert masses == pytest.approx([interval.mass / 2] * 2)
        assert _integrate_interval(marginal, *interval.eti) == pytest.approx(
            interval.mass
        )


def test_delta_hdi_preserves_angle_components_modes_masses_and_threshold():
    xi = np.linspace(-1.2, 1.2, 7)
    sigma = np.array([1, 2, 3])
    result = _result(xi, sigma, [0, 1, 0, 0, 0, 1, 0], np.ones(3))
    summary = summarize_density(result)
    delta = summary.delta
    angle = summary.arctan_delta

    for interval, angle_interval in zip(delta.intervals, angle.intervals):
        left, right = interval.hdi
        assert left[1] <= np.tan(xi[2]) < np.tan(xi[4]) <= right[0]
        np.testing.assert_allclose(
            np.interp(np.arctan([*left, *right]), angle.coordinate, angle.density),
            interval.hdi_threshold,
            rtol=1e-10,
        )
        for segment, source, peak in zip(
            interval.hdi_segments, angle_interval.hdi_segments, np.tan(xi[[1, 5]])
        ):
            assert segment.bounds == pytest.approx(np.tan(source.bounds))
            np.testing.assert_allclose(segment.mode_ranges, [(peak, peak)])
            assert segment.mass == pytest.approx(interval.mass / 2)
            assert _integrate_interval(angle, *source.bounds) == pytest.approx(segment.mass)
        assert interval.eti == pytest.approx(np.tan(angle_interval.eti))


def test_nonuniform_grid_moments_are_exact_for_linear_density():
    xi = np.array([0.0, 0.01, 0.73, 1.0])
    sigma = np.array([1.0, 1.2, 3.0])
    summary = summarize_density(_result(xi, sigma, 2 * xi, np.ones(3)))
    angle = summary.arctan_delta
    assert angle.mean == pytest.approx(2 / 3)
    assert angle.std == pytest.approx(sqrt(1 / 18))
    assert summary.delta.mean == pytest.approx(np.tan(angle.mean))
    assert summary.delta.std is None
    assert summary.delta.mean_bounds == pytest.approx(np.tan(angle.mean_bounds))
    width = summary.sigma_over_i
    assert width.mean == pytest.approx((width.coordinate[0] + width.coordinate[-1]) / 2)
    assert width.std == pytest.approx(np.ptp(width.coordinate) / sqrt(12))


def test_connected_hdi_retains_tied_point_and_plateau_modes():
    xi = np.array([-1.0, -0.8, -0.4, -0.25, -0.1, 0.05, 0.2, 0.4, 0.8, 1.0])
    result = _result(xi, [1, 2], [0, 1.3, 1.55, 2, 2, 1.8, 2, 1.54, 1.29, 0], [1, 1])
    interval = summarize_density(result).arctan_delta.intervals[0]
    segment, = interval.hdi_segments
    assert segment.mode_ranges == ((-0.25, -0.1), (0.2, 0.2))
    assert segment.mass == pytest.approx(0.68)


@pytest.mark.parametrize("scale, singular", [(0.5, False), (1.0, True)])
def test_delta_mean_guide_flags_report_invalid_upper_angle(scale, singular):
    xi = scale * np.array([0.0, 0.1, 0.2, 1.45, 1.54, 1.56])
    result = _result(xi, [1, 2], [0, 0.16, 0, 0, 1, 1], [1, 1])
    summary = summarize_density(result)
    angle, delta = summary.arctan_delta, summary.delta
    assert angle.mean_bounds[1] > xi[-1]
    assert delta.mean_bounds[1] is None
    assert "outside_scan" in delta.mean_bound_flags[1]
    assert ("tan_singularity" in delta.mean_bound_flags[1]) is singular
    assert delta.mean_bounds[0] == pytest.approx(np.tan(angle.mean_bounds[0]))


def test_mapped_identity_summary_matches_gaussian_quantiles_in_both_coordinates():
    job = JobRequest(
        "P_ADO",
        Transition(2, 1),
        Measurement(0, 0.15, 0.15),
        Measurement(1, 0.15, 0.15),
    )
    xi, sigma = np.linspace(-0.8, 0.8, 401), np.linspace(0.2, 1.8, 401)
    polar, ratio = np.meshgrid(xi, sigma)
    response = ResponseGrid(
        xi, sigma, polar, ratio, np.ones(polar.shape, dtype=bool), 2, "R_ADO"
    )
    summary = summarize_density(map_density(job, response))

    assert summary.delta.median == pytest.approx(0, abs=1e-10)
    assert summary.sigma_over_i.median == pytest.approx(0.5)
    for delta_int, sigma_int in zip(
        summary.delta.intervals, summary.sigma_over_i.intervals
    ):
        half_width = norm.ppf((1 + delta_int.mass) / 2) * 0.15
        assert delta_int.eti == pytest.approx(
            (-np.tan(half_width), np.tan(half_width)), abs=3e-5
        )
        assert sigma_int.eti == pytest.approx(
            ((1 - half_width) / 2, (1 + half_width) / 2), abs=1.5e-5
        )


def test_hdi_at_nonmaximal_plateau_clips_tied_mass_from_left():
    xi = np.array([-0.5, 0, 0.5])
    sigma = np.arange(1, 8)
    mass = 0.5
    result = _result(xi, sigma, np.ones(3), [0, 1, 1, 0, 0, 2, 0])
    marginal = summarize_density(result, (mass,)).sigma_over_i
    (interval,) = marginal.intervals
    assert interval.hdi_threshold == pytest.approx(0.5)
    np.testing.assert_allclose(interval.hdi, [(1, 1.25), (2.75, 3.25)])
    assert sum(
        _integrate_interval(marginal, *segment) for segment in interval.hdi
    ) == pytest.approx(mass)


def test_uniform_marginal_hdi_clips_plateau_to_requested_mass():
    xi = np.array([-0.5, 0, 0.5])
    sigma = np.array([1, 2, 3])
    result = _result(xi, sigma, np.ones(3), np.ones(3))
    (interval,) = summarize_density(result, (0.68,)).sigma_over_i.intervals
    assert interval.eti == pytest.approx((0.66, 1.34))
    assert interval.hdi_threshold == pytest.approx(1)
    assert interval.hdi[0] == pytest.approx((0.5, 1.18))


@pytest.mark.parametrize("mass", [0, 1, np.nan, np.inf])
def test_invalid_interval_mass(mass):
    xi = np.array([-0.5, 0, 0.5])
    sigma = np.array([1, 2, 3])
    result = _result(xi, sigma, np.ones(3), np.ones(3))
    with pytest.raises(ValueError, match="strictly between zero and one"):
        summarize_density(result, (mass,))
