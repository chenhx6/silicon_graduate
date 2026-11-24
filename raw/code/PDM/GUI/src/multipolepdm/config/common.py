"""Shared labels and defaults, kept independent of GUI widgets."""

from multipolepdm.contracts import Geometry, GridSpec

COMMON_FIELDS = ("target", "observations", "geometry", "grid", "output")
DEFAULT_GEOMETRY = Geometry()
DEFAULT_GRID = GridSpec()
