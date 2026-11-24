import xml.etree.ElementTree as ET

import numpy as np
import pytest
from matplotlib.collections import PathCollection, QuadMesh
from matplotlib.container import ErrorbarContainer
from PIL import Image
from scipy.integrate import trapezoid

from multipolepdm.contracts import (
    JobRequest, MappingResult, Measurement, ResponseGrid, Transition,
)
from multipolepdm.pdm.statistics import summarize_density
from multipolepdm.plotting import make_panel, make_preview, save_overview, save_panel, supported_formats
from multipolepdm.plotting.intervals import format_marginal
from multipolepdm.plotting.style import ANGLE_LABEL, ETI_COLOR, MEAN_COLOR, OVERVIEW_TITLE, SIGMA_LABEL


@pytest.fixture
def case():
    xi = np.array([-1.5, -1.2, -0.8, -0.5, 0, 0.4, 0.85, 1.2, 1.5])
    sigma = np.array([0.8, 1.0, 2.5, 4.2, 5.5, 6.4])
    job = JobRequest(
        "P_ADO", Transition(8, 7), Measurement(-0.08, 0.03, 0.06),
        Measurement(1.21, 0.05, 0.08), label="Synthetic",
    )
    angle, width = np.meshgrid(xi, sigma)
    polar = np.sin(angle) + width
    ratio = np.cos(angle) * width
    polar[0, 1], ratio[0, 1] = polar[0, 0], ratio[0, 0]
    polar[-1, -1], ratio[-1, -1] = -20, 40
    polar[-2, -1], ratio[-2, -1] = -1e6, 1e6
    valid = np.ones_like(angle, dtype=bool)
    valid[-2, -1] = False
    response = ResponseGrid(xi, sigma, polar, ratio, valid, job.reference_spin, job.ratio_name)
    observations = np.arange(xi.size * sigma.size, dtype=float).reshape(angle.shape)
    observations[0, 1] = observations[0, 0]
    density = np.outer([0, 0.3, 1, 0.7, 0.2, 0], [0, 3, 0, 0, 0, 0, 1.8, 0, 0])
    normalization = trapezoid(trapezoid(density, xi, axis=1), sigma)
    result = MappingResult(
        job, response, observations, np.ones_like(density), density / normalization, normalization,
    )
    return result, summarize_density(result)


def test_observation_keeps_full_response_domain_folds_and_asymmetric_errors(case):
    result, summary = case
    observation = make_preview(result, summary).axes[0]
    points, = (item for item in observation.collections if isinstance(item, PathCollection))
    assert points.get_cmap().name == "viridis"
    assert points.get_rasterized()
    assert not any(isinstance(item, QuadMesh) for item in observation.collections)
    response = result.response
    valid = response.valid
    plotted = points.get_offsets()
    np.testing.assert_array_equal(
        plotted, np.column_stack((response.angular_ratio[valid], response.polarization[valid]))
    )
    np.testing.assert_array_equal(points.get_array(), result.observation_density[valid])
    assert np.count_nonzero(np.all(plotted == plotted[0], axis=1)) == 2
    assert observation.get_xlim()[1] > 40
    assert observation.get_ylim()[0] < -20
    assert observation.get_xlim()[1] < 1e6

    error, = (item for item in observation.containers if isinstance(item, ErrorbarContainer))
    ratio, polar = result.job.angular_ratio, result.job.polarization
    horizontal, vertical = error.lines[2]
    np.testing.assert_allclose(
        horizontal.get_segments()[0],
        [[ratio.value - ratio.err_minus, polar.value], [ratio.value + ratio.err_plus, polar.value]],
    )
    np.testing.assert_allclose(
        vertical.get_segments()[0],
        [[ratio.value, polar.value - polar.err_minus], [ratio.value, polar.value + polar.err_plus]],
    )
    left, right = observation.get_xlim()
    bottom, top = observation.get_ylim()
    assert left < ratio.value - ratio.err_minus < ratio.value + ratio.err_plus < right
    assert bottom < polar.value - polar.err_minus < polar.value + polar.err_plus < top


def test_parameter_measure_colorbars_ticks_and_layout(case):
    result, summary = case
    preview = make_preview(result, summary)
    observation, parameter, angle, width = preview.axes
    assert preview.figure._suptitle.get_text() == OVERVIEW_TITLE
    mesh, = (item for item in parameter.collections if isinstance(item, QuadMesh))
    assert mesh.get_cmap().name == "viridis"
    np.testing.assert_array_equal(
        mesh.get_array().reshape(result.parameter_density.shape),
        result.parameter_density * result.response.reference_spin,
    )
    assert mesh.colorbar is not observation.collections[0].colorbar
    assert parameter.get_ylabel() == width.get_xlabel() == SIGMA_LABEL
    for axes in (parameter, angle):
        assert axes.get_xlabel() == ANGLE_LABEL
        np.testing.assert_allclose(axes.get_xticks(), np.arange(-3, 4) * np.pi / 8)
        assert axes.get_xticklabels()[1].get_text() == r"$-\pi/4$"
        assert axes.get_xlim() == (result.response.xi_rad[0], result.response.xi_rad[-1])
    assert parameter.get_ylim() == tuple(summary.sigma_over_i.coordinate[[0, -1]])
    np.testing.assert_allclose(
        [axes.get_position().bounds[2:] for axes in (observation, parameter)],
        [observation.get_position().bounds[2:]] * 2,
    )
    preview.figure.canvas.draw()
    renderer = preview.figure.canvas.get_renderer()
    for axes in (parameter, angle):
        ticks = [tick.get_window_extent(renderer) for tick in axes.get_xticklabels()]
        assert all(left.x1 < right.x0 for left, right in zip(ticks, ticks[1:]))
    for density_panel, marginal_panel in ((observation, angle), (parameter, width)):
        xlabel = density_panel.xaxis.label.get_window_extent(renderer)
        legend_labels = marginal_panel.get_legend().get_texts()
        assert xlabel.y0 > max(text.get_window_extent(renderer).y1 for text in legend_labels)


def _polygon_area(path):
    vertices = path.vertices
    return abs(trapezoid(vertices[:, 1], vertices[:, 0]))


@pytest.mark.parametrize("panel", ["c", "d"])
def test_marginal_guides_fill_and_text_match_single_summary(case, panel):
    result, summary = case
    angle_panel = panel == "c"
    evaluated = summary.arctan_delta if angle_panel else summary.sigma_over_i
    reported = summary.delta if angle_panel else evaluated
    interval, = evaluated.intervals
    figure = make_panel(result, summary, panel)
    axes, = figure.axes
    curve, threshold, *guides = axes.lines
    np.testing.assert_array_equal(curve.get_xdata(), evaluated.coordinate)
    np.testing.assert_array_equal(curve.get_ydata(), evaluated.density)
    assert len(guides) == 6
    assert tuple(threshold.get_ydata()) == (interval.hdi_threshold,) * 2
    for color, lines, expected in (
        (ETI_COLOR, guides[:3], [interval.eti[0], evaluated.median, interval.eti[1]]),
        (MEAN_COLOR, guides[3:], [evaluated.mean, *evaluated.mean_bounds]),
    ):
        for line, coordinate in zip(lines, expected):
            assert line.get_color() == color
            assert tuple(line.get_xdata()) == (coordinate, coordinate)
    paths = [item.get_paths()[0] for item in axes.collections]
    assert len(paths) == len(interval.hdi_segments) == (2 if angle_panel else 1)
    for path, segment in zip(paths, interval.hdi_segments):
        np.testing.assert_allclose(
            [path.vertices[:, 0].min(), path.vertices[:, 0].max()], segment.bounds
        )
        assert path.vertices[:, 1].min() == 0
        np.testing.assert_allclose(
            path.vertices[:, 1].max(),
            np.interp(segment.mode_ranges[0][0], evaluated.coordinate, evaluated.density),
        )
        assert _polygon_area(path) == pytest.approx(segment.mass)
    assert sum(map(_polygon_area, paths)) == pytest.approx(0.68)
    labels = [text.get_text() for text in axes.get_legend().get_texts()]
    assert labels == ["68% ETI (16%, 50%, 84%)", "Mean +/- SD", "68% HDI threshold", "68% HDI"]
    figure.canvas.draw()
    renderer = figure.canvas.get_renderer()
    for text in axes.get_legend().get_texts():
        box = text.get_window_extent(renderer)
        assert figure.bbox.contains(box.x0, box.y0)
        assert figure.bbox.contains(box.x1, box.y1)
    expected_text = format_marginal(reported, angle=evaluated if angle_panel else None)
    assert figure.texts[0].get_text() == expected_text
    assert expected_text in [text.get_text() for text in make_preview(result, summary).figure.texts]


@pytest.mark.parametrize("extension", ["png", "pdf", "svg"])
def test_overview_and_single_panel_exports(case, tmp_path, extension):
    result, summary = case
    overview = save_overview(result, summary, tmp_path / f"overview.{extension}", dpi=120)
    panel = save_panel(result, summary, "c", tmp_path / f"angle.{extension}", dpi=120)
    if extension == "png":
        for path, figure in (
            (overview, make_preview(result, summary).figure),
            (panel, make_panel(result, summary, "c")),
        ):
            with Image.open(path) as image:
                assert image.format == "PNG"
                assert image.size == tuple(int(length * 120) for length in figure.get_size_inches())
    elif extension == "pdf":
        assert overview.read_bytes().startswith(b"%PDF")
        assert panel.read_bytes().startswith(b"%PDF")
    else:
        for path, count in ((overview, 3), (panel, 2)):
            tree = ET.parse(path)
            namespace = "{http://www.w3.org/2000/svg}"
            text = " ".join("".join(node.itertext()) for node in tree.iter(f"{namespace}text"))
            assert "68% HDI" in text and "68% ETI" in text
            assert "tan(mean angle)" in text
            fills = [node.get("id") for node in tree.iter() if node.get("id", "").startswith("pdm-hdi-")]
            assert len(fills) == len(set(fills)) == count


def test_extra_backend_formats_and_invalid_format(case, tmp_path):
    result, summary = case
    formats = supported_formats()
    assert {"png", "pdf", "svg"} <= formats.keys()
    assert "pgf" not in formats
    if "eps" in formats:
        path = save_panel(result, summary, "c", tmp_path / "angle.eps", dpi=120)
        assert path.read_bytes().startswith(b"%!PS-Adobe")
    if "tiff" in formats:
        path = save_panel(result, summary, "d", tmp_path / "sigma.tiff", dpi=120)
        with Image.open(path) as image:
            assert image.format == "TIFF"
    with pytest.raises(ValueError, match="Unsupported figure format"):
        save_panel(result, summary, "a", tmp_path / "panel.unknown")
    assert save_panel(result, summary, "d", tmp_path / "sigma", dpi=120).suffix == ".png"
