"""Save report-sized Matplotlib figures from PDM result data."""

from pathlib import Path
from tempfile import TemporaryDirectory

from matplotlib import rc_context
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.colors import to_rgb
from matplotlib.figure import Figure

from multipolepdm.contracts import MappingResult, Summary

from .intervals import HDI_ARTIST_PREFIX
from .overview import make_panel, make_preview
from .style import EXPORT_DPI, HDI_ALPHA, HDI_COLOR, MATPLOTLIB_LOCK, MATPLOTLIB_STYLE


def supported_formats() -> dict[str, str]:
    """Return backend formats that can be exported without a TeX toolchain."""
    return {
        extension: name
        for extension, name in FigureCanvasAgg.get_supported_filetypes().items()
        if extension != "pgf"
    }


def _flatten_hdi_alpha(figure: Figure) -> None:
    """Use the equivalent opaque color for PostScript on a white background."""
    color = tuple(1 - HDI_ALPHA * (1 - channel) for channel in to_rgb(HDI_COLOR))
    for artist in figure.findobj():
        key = artist.get_gid()
        if key and key.startswith(HDI_ARTIST_PREFIX):
            artist.set_alpha(1)
            artist.set_facecolor(color)


def _save(figure: Figure, path: str | Path, dpi: float) -> Path:
    destination = Path(path)
    if not destination.suffix:
        destination = destination.with_suffix(".png")
    extension = destination.suffix[1:].lower()
    if extension not in supported_formats():
        raise ValueError(f"Unsupported figure format: {extension!r}.")
    if extension in ("eps", "ps"):
        _flatten_hdi_alpha(figure)
    with TemporaryDirectory(dir=destination.parent, prefix=".pdm-") as directory:
        temporary = Path(directory) / destination.name
        with MATPLOTLIB_LOCK, rc_context(MATPLOTLIB_STYLE):
            figure.savefig(temporary, format=extension, dpi=dpi, facecolor="white")
        temporary.replace(destination)
    return destination


def save_overview(
    result: MappingResult,
    summary: Summary,
    path: str | Path,
    *,
    mass: float | None = None,
    dpi: float = EXPORT_DPI,
    focus_delta: bool = False,
) -> Path:
    """Save all four panels at report size, using the filename extension."""
    return _save(
        make_preview(result, summary, mass=mass, focus_delta=focus_delta).figure,
        path,
        dpi,
    )


def save_panel(
    result: MappingResult,
    summary: Summary,
    panel: str,
    path: str | Path,
    *,
    mass: float | None = None,
    dpi: float = EXPORT_DPI,
    focus_delta: bool = False,
) -> Path:
    """Save one panel at report size, using the filename extension."""
    return _save(
        make_panel(result, summary, panel, mass=mass, focus_delta=focus_delta),
        path,
        dpi,
    )
