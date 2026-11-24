"""Draw evaluated marginals and format their reported estimates."""

from math import isclose

from matplotlib.axes import Axes
from matplotlib.patches import Patch

from multipolepdm.contracts import Interval, MarginalSummary
from multipolepdm.pdm.statistics import DEFAULT_INTERVAL_MASS, density_segment

from .style import (
    ETI_COLOR, HDI_ALPHA, HDI_COLOR, MEAN_COLOR, PDF_COLOR, PlotStyle, style_axes,
)

HDI_ARTIST_PREFIX = "pdm-hdi-"
FLAG_LABELS = {
    "outside_scan": "outside scan",
    "tan_singularity": "tan singularity",
}


def select_interval(marginal: MarginalSummary, mass: float = DEFAULT_INTERVAL_MASS) -> Interval:
    for interval in marginal.intervals:
        if isclose(interval.mass, mass, rel_tol=0, abs_tol=1e-9):
            return interval
    raise ValueError(f"The marginal does not contain a {mass:.6g} probability interval.")


def _bounds_text(bounds):
    return "[" + ", ".join(f"{value:.4g}" if value is not None else "n/a" for value in bounds) + "]"


def format_marginal(
    marginal: MarginalSummary,
    mass: float = DEFAULT_INTERVAL_MASS,
    *,
    angle: MarginalSummary | None = None,
) -> str:
    interval = select_interval(marginal, mass)
    percent = f"{interval.mass:.0%}"
    label = "delta" if angle is not None else "sigma/I"
    lines = [f"HDI {percent} ({label})"]
    for index, segment in enumerate(interval.hdi_segments, start=1):
        lines.append(f"  {index}. {_bounds_text(segment.bounds)}, mass {segment.mass:.2%}")
        for lower, upper in segment.mode_ranges:
            mode = f"{lower:.4g}" if lower == upper else _bounds_text((lower, upper))
            lines.append(f"      mode {mode}")
    lines.append(f"ETI {percent}   q50 = {marginal.median:.4g}  {_bounds_text(interval.eti)}")
    if angle is None:
        lines.append(f"Mean +/- SD   {marginal.mean:.4g} +/- {marginal.std:.4g}")
    else:
        lines.extend((
            f"Mean-based   tan(mean angle) = {marginal.mean:.4g}",
            f"  tan(mean angle +/- SD)   {_bounds_text(marginal.mean_bounds)}",
            f"  Angle mean +/- SD   {angle.mean:.4g} +/- {angle.std:.4g} rad",
        ))
    for side, flags in zip(("Lower", "Upper"), marginal.mean_bound_flags):
        if flags:
            lines.append(f"  {side} guide: " + ", ".join(FLAG_LABELS[flag] for flag in flags))
    return "\n".join(lines)


def draw_marginal(
    axes: Axes, marginal: MarginalSummary, xlabel: str, style: PlotStyle, mass: float,
) -> None:
    coordinate, density = marginal.coordinate, marginal.density
    interval = select_interval(marginal, mass)
    percent = f"{interval.mass:.0%}"
    style_axes(axes, style, xlabel, "Probability density")
    for index, bounds in enumerate(interval.hdi):
        fill_x, fill_y = density_segment(coordinate, density, bounds)
        fill = axes.fill_between(
            fill_x, 0, fill_y, color=HDI_COLOR, alpha=HDI_ALPHA, linewidth=0, zorder=1
        )
        fill.set_gid(f"{HDI_ARTIST_PREFIX}{axes.get_label()}-{index}")
    axes.plot(coordinate, density, color=PDF_COLOR, linewidth=1.1, zorder=4)
    axes.set_xlim(coordinate[0], coordinate[-1])
    axes.set_ylim(bottom=0)

    threshold = axes.axhline(
        interval.hdi_threshold, color=HDI_COLOR, linestyle="--", linewidth=0.9,
        label=f"{percent} HDI threshold", zorder=2,
    )
    lower, upper = interval.eti
    axes.axvline(lower, color=ETI_COLOR, linestyle="--", linewidth=0.9, zorder=3)
    tail = (1 - interval.mass) / 2
    eti = axes.axvline(
        marginal.median, color=ETI_COLOR, linestyle="-", linewidth=1.0, zorder=3,
        label=f"{percent} ETI ({tail:.0%}, 50%, {1 - tail:.0%})",
    )
    axes.axvline(upper, color=ETI_COLOR, linestyle="--", linewidth=0.9, zorder=3)
    mean = axes.axvline(
        marginal.mean, color=MEAN_COLOR, linestyle="-", linewidth=1.0,
        label="Mean +/- SD", zorder=3,
    )
    for bound in marginal.mean_bounds:
        axes.axvline(bound, color=MEAN_COLOR, linestyle=":", linewidth=1.1, zorder=3)

    band = Patch(facecolor=HDI_COLOR, alpha=HDI_ALPHA, linewidth=0, label=f"{percent} HDI")
    axes.legend(
        handles=(eti, mean, threshold, band),
        loc="lower center", bbox_to_anchor=(0.47, 1.11), ncols=2,
        frameon=False, fontsize=style.tick_pt, borderaxespad=0,
        columnspacing=0.8, handlelength=1.5, handletextpad=0.45,
    )
