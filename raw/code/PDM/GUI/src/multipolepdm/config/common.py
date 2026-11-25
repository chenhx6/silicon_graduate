"""Shared labels and defaults, kept independent of GUI widgets."""

from multipolepdm.contracts import Geometry
from multipolepdm.grid import recommend_grid

COMMON_FIELDS = ("target", "observations", "geometry", "grid", "output")
DEFAULT_GEOMETRY = Geometry()
DEFAULT_GRID = recommend_grid(5.0)
