"""Build the PDM overview and its individual panels from the same data."""

from dataclasses import dataclass

from matplotlib import rc_context
from matplotlib.axes import Axes
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.collections import PathCollection, QuadMesh
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator, ScalarFormatter
import numpy as np

from multipolepdm.contracts import MappingResult, Summary
from multipolepdm.pdm.statistics import DEFAULT_INTERVAL_MASS

from .intervals import draw_marginal, format_marginal, format_tan_statistics
from .style import (
    ANGLE_LABEL,
    DENSITY_CMAP,
    MATPLOTLIB_LOCK,
    MATPLOTLIB_STYLE,
    MM_PER_INCH,
    OVERVIEW_BOUNDS,
    OVERVIEW_TITLE,
    REPORT_STYLE,
    SIGMA_LABEL,
    SINGLE_PANEL_BOUNDS,
    PlotStyle,
    angle_ticks,
    panel_letter,
    style_axes,
)

PANELS = ("a", "b", "c", "d")


@dataclass(frozen=True)
class PreviewData:
    figure: Figure
    axes: tuple[Axes, Axes, Axes, Axes]


def _new_figure(size_mm: tuple[float, float]) -> Figure:
    figure = Figure(figsize=tuple(size / MM_PER_INCH for size in size_mm))
    FigureCanvasAgg(figure)
    return figure


def _draw_observation(axes: Axes, result: MappingResult, style: PlotStyle) -> PathCollection:
    ratio = result.job.angular_ratio
    polarization = result.job.polarization
    response = result.response
    valid = (
        response.valid & np.isfinite(response.angular_ratio)
        & np.isfinite(response.polarization) & np.isfinite(result.observation_density)
    )
    points = axes.scatter(
        response.angular_ratio[valid],
        response.polarization[valid],
        c=result.observation_density[valid],
        s=2,
        linewidths=0,
        cmap=DENSITY_CMAP,
        vmin=0,
        rasterized=True,
    )
    axes.errorbar(
        ratio.value,
        polarization.value,
        xerr=[[ratio.err_minus], [ratio.err_plus]],
        yerr=[[polarization.err_minus], [polarization.err_plus]],
        fmt="o",
        color="#202020",
        markerfacecolor="#FFFFFF",
        markeredgecolor="#202020",
        markersize=3.5,
        elinewidth=1.1,
        capsize=2,
        zorder=3,
    )
    ratio_subscript = {"R_ADO": "ADO", "R_DCO": "DCO"}[result.response.ratio_name]
    style_axes(
        axes,
        style,
        rf"$R_{{\mathrm{{{ratio_subscript}}}}}$",
        r"$P$",
    )
    axes.margins(0.04)
    return points


def _draw_parameters(axes: Axes, result: MappingResult, style: PlotStyle) -> QuadMesh:
    response = result.response
    reference_spin = response.reference_spin
    if reference_spin <= 0:
        raise ValueError("Plotting sigma/I requires a positive reference spin.")
    xi = np.asarray(response.xi_rad)
    scaled_sigma = np.asarray(response.sigma) / reference_spin
    density = np.asarray(result.parameter_density) * reference_spin
    mesh = axes.pcolormesh(
        xi,
        scaled_sigma,
        density,
        shading="nearest",
        cmap=DENSITY_CMAP,
        vmin=0,
        rasterized=True,
    )
    style_axes(axes, style, ANGLE_LABEL, SIGMA_LABEL)
    axes.set_xlim(xi[0], xi[-1])
    axes.set_ylim(scaled_sigma[0], scaled_sigma[-1])
    angle_ticks(axes, style)
    return mesh


def _draw_panel(
    figure: Figure,
    panel: str,
    bounds: tuple[float, float, float, float],
    result: MappingResult,
    summary: Summary,
    style: PlotStyle,
    mass: float,
    overview: bool,
) -> Axes:
    axes = figure.add_axes(bounds, label=panel)
    panel_letter(axes, panel, style)
    if panel in ("a", "b"):
        left, bottom, width, height = bounds
        gap, bar_width = (0.014, 0.014) if overview else (0.028, 0.028)
        color_axes = figure.add_axes(
            (left + width + gap, bottom, bar_width, height), label=f"{panel}-colorbar"
        )
        if panel == "a":
            mesh = _draw_observation(axes, result, style)
            label = r"PDF per $R$, $P$"
        else:
            mesh = _draw_parameters(axes, result, style)
            label = r"PDF (rad$^{-1}$)"
        formatter = ScalarFormatter(useOffset=False, useMathText=False)
        formatter.set_powerlimits((-2, 3))
        figure.colorbar(
            mesh, cax=color_axes, ticks=MaxNLocator(nbins=5), format=formatter
        )
        color_axes.set_title(label, fontsize=style.axis_pt, pad=1.5 * style.axis_pt)
        color_axes.tick_params(labelsize=style.tick_pt, width=0.8, length=3)
        color_axes.yaxis.get_offset_text().set_fontsize(style.tick_pt)
    elif panel == "c":
        draw_marginal(
            axes,
            summary.arctan_delta,
            ANGLE_LABEL,
            style,
            mass,
        )
        angle_ticks(axes, style)
    else:
        draw_marginal(axes, summary.sigma_over_i, SIGMA_LABEL, style, mass)
    return axes


def _report_text(summary: Summary, mass: float) -> dict[str, str]:
    return {
        "c": format_tan_statistics(summary.tan_angle_statistics, summary.arctan_delta, mass),
        "d": format_marginal(summary.sigma_over_i, mass),
    }


def _with_footer(size, text_blocks, style):
    width, base_height = size
    line_count = max((text.count("\n") + 1 for text in text_blocks), default=0)
    footer = (line_count * 1.3 + 1.0) * style.tick_pt * MM_PER_INCH / 72 if line_count else 0
    height = base_height + footer
    figure = _new_figure((width, height))

    def bounds_with_footer(bounds):
        left, bottom, panel_width, panel_height = bounds
        return left, (bottom * base_height + footer) / height, panel_width, panel_height * base_height / height

    return figure, bounds_with_footer


def _draw_report_text(figure, axes, text, style):
    position = axes.get_position()
    offset = 34 / (72 * figure.get_figheight())
    figure.text(
        position.x0, position.y0 - offset, text,
        ha="left", va="top", fontsize=style.tick_pt, linespacing=1.23,
    )


def make_preview(
    result: MappingResult,
    summary: Summary,
    *,
    style: PlotStyle = REPORT_STYLE,
    mass: float | None = None,
    focus_delta: bool = False,
) -> PreviewData:
    """Return axes a to d at full scan extent, independent of legacy focus_delta."""
    mass = DEFAULT_INTERVAL_MASS if mass is None else mass
    with MATPLOTLIB_LOCK, rc_context(MATPLOTLIB_STYLE):
        text_blocks = _report_text(summary, mass)
        figure, adjust = _with_footer(style.overview_mm, text_blocks.values(), style)
        figure.suptitle(OVERVIEW_TITLE, y=0.98, fontsize=style.axis_pt + 1)
        axes = tuple(
            _draw_panel(
                figure,
                panel,
                adjust(bounds),
                result,
                summary,
                style,
                mass,
                overview=True,
            )
            for panel, bounds in zip(PANELS, OVERVIEW_BOUNDS)
        )
        for panel, axis in zip(PANELS, axes):
            if panel in text_blocks:
                _draw_report_text(figure, axis, text_blocks[panel], style)
    return PreviewData(figure, axes)


def make_panel(
    result: MappingResult,
    summary: Summary,
    panel: str,
    *,
    style: PlotStyle = REPORT_STYLE,
    mass: float | None = None,
    focus_delta: bool = False,
) -> Figure:
    """Redraw a panel at full extent, independent of legacy focus_delta."""
    if panel not in PANELS:
        raise ValueError("Panel must be one of a, b, c or d.")
    mass = DEFAULT_INTERVAL_MASS if mass is None else mass
    with MATPLOTLIB_LOCK, rc_context(MATPLOTLIB_STYLE):
        kind = "density" if panel in ("a", "b") else "marginal"
        text = _report_text(summary, mass)[panel] if kind == "marginal" else ""
        figure, adjust = _with_footer(style.panel_mm, (text,) if text else (), style)
        axes = _draw_panel(
            figure,
            panel,
            adjust(SINGLE_PANEL_BOUNDS[kind]),
            result,
            summary,
            style,
            mass,
            overview=False,
        )
        if text:
            _draw_report_text(figure, axes, text, style)
    return figure
