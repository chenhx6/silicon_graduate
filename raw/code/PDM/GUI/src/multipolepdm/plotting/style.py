"""Shared Matplotlib styles and physical figure geometry for PDM."""

from dataclasses import dataclass
from math import pi
from threading import RLock

from matplotlib.axes import Axes
from matplotlib.ticker import FixedFormatter, FixedLocator, MaxNLocator, ScalarFormatter
from matplotlib.transforms import ScaledTranslation

MM_PER_INCH = 25.4
EXPORT_DPI = 600
PDF_COLOR = "#222222"
HDI_COLOR = "#0072B2"
HDI_ALPHA = 0.25
ETI_COLOR = "#D55E00"
MEAN_COLOR = "#626262"
DENSITY_CMAP = "viridis"
ANGLE_LABEL = r"$\arctan(\delta)$"
SIGMA_LABEL = r"$\sigma/I$"
OVERVIEW_TITLE = "Full Range Marginalization; Constant Weight"
MATPLOTLIB_LOCK = RLock()

MATPLOTLIB_STYLE = {
    "figure.facecolor": "white",
    "figure.autolayout": False,
    "figure.constrained_layout.use": False,
    "axes.facecolor": "white",
    "axes.edgecolor": "#222222",
    "axes.labelcolor": "#222222",
    "axes.grid": False,
    "axes.linewidth": 0.8,
    "axes.formatter.use_locale": False,
    "font.family": "sans-serif",
    "font.sans-serif": ["DejaVu Sans"],
    "text.color": "#222222",
    "text.usetex": False,
    "mathtext.fontset": "dejavusans",
    "xtick.color": "#222222",
    "ytick.color": "#222222",
    "pdf.fonttype": 42,
    "svg.fonttype": "none",
    "savefig.bbox": None,
    "savefig.facecolor": "white",
    "savefig.transparent": False,
}


@dataclass(frozen=True)
class PlotStyle:
    overview_mm: tuple[float, float]
    panel_mm: tuple[float, float]
    axis_pt: float
    tick_pt: float
    panel_letter_pt: float


REPORT_STYLE = PlotStyle((183, 150), (89, 75), 9, 8, 10)
GUI_STYLE = PlotStyle((238, 195), (116, 98), 12, 10, 13)

OVERVIEW_BOUNDS = (
    (0.103, 0.595, 0.306, 0.295),
    (0.565, 0.595, 0.306, 0.295),
    (0.103, 0.090, 0.306, 0.340),
    (0.565, 0.090, 0.306, 0.340),
)
SINGLE_PANEL_BOUNDS = {
    "density": (0.213, 0.229, 0.595, 0.644),
    "marginal": (0.213, 0.229, 0.680, 0.590),
}


def angle_ticks(axes: Axes, style: PlotStyle) -> None:
    lower, upper = axes.get_xlim()
    ticks = (
        (-3 * pi / 8, r"$-3\pi/8$"), (-pi / 4, r"$-\pi/4$"),
        (-pi / 8, r"$-\pi/8$"), (0.0, "$0$"), (pi / 8, r"$\pi/8$"),
        (pi / 4, r"$\pi/4$"), (3 * pi / 8, r"$3\pi/8$"),
    )
    visible = [(value, label) for value, label in ticks if lower <= value <= upper]
    axes.xaxis.set_major_locator(FixedLocator([value for value, _ in visible]))
    axes.xaxis.set_major_formatter(FixedFormatter([label for _, label in visible]))
    axes.tick_params(axis="x", labelsize=style.tick_pt - 1)


def style_axes(axes: Axes, style: PlotStyle, xlabel: str, ylabel: str) -> None:
    axes.set_xlabel(xlabel, fontsize=style.axis_pt)
    axes.set_ylabel(ylabel, fontsize=style.axis_pt)
    axes.tick_params(labelsize=style.tick_pt, width=0.8, length=3, direction="out")
    for axis in (axes.xaxis, axes.yaxis):
        axis.set_major_locator(MaxNLocator(nbins=5))
        axis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=False))
        axis.get_offset_text().set_fontsize(style.tick_pt)
    axes.spines[["top", "right"]].set_visible(False)


def panel_letter(axes: Axes, panel: str, style: PlotStyle) -> None:
    offset = ScaledTranslation(
        -0.9 * style.panel_letter_pt / 72,
        0.4 * style.panel_letter_pt / 72,
        axes.figure.dpi_scale_trans,
    )
    axes.text(
        0,
        1,
        panel,
        transform=axes.transAxes + offset,
        fontsize=style.panel_letter_pt,
        fontweight="bold",
        ha="left",
        va="bottom",
    )
