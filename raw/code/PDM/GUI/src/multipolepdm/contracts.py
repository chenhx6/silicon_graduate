"""Immutable inputs and explicitly named scientific output containers."""

from dataclasses import dataclass, field
from math import isfinite, pi
from typing import Any

import numpy as np

from multipolepdm.physics.detectors import DetectorGroup


def spin(value: float) -> float:
    value = float(value)
    if not isfinite(value) or value < 0 or abs(2 * value - round(2 * value)) > 1e-10:
        raise ValueError("Spin must be a nonnegative integer or half-integer.")
    return round(2 * value) / 2


@dataclass(frozen=True)
class Transition:
    spin_initial: float
    spin_final: float
    multipoles: tuple[str, ...] = ("M1", "E2")
    delta: float = 0.0

    def __post_init__(self):
        object.__setattr__(self, "spin_initial", spin(self.spin_initial))
        object.__setattr__(self, "spin_final", spin(self.spin_final))
        object.__setattr__(self, "multipoles", tuple(self.multipoles))
        if self.multipoles not in (("M1",), ("E1",), ("E2",), ("M2",), ("M1", "E2")):
            raise ValueError("Supported multipoles: M1, E1, E2, M2, or M1/E2.")
        for component in self.multipoles:
            rank = int(component[1:])
            if not (
                abs(self.spin_initial - self.spin_final)
                <= rank
                <= self.spin_initial + self.spin_final
            ):
                raise ValueError(f"{component} is forbidden by the spin triangle rule.")
            if (self.spin_initial - self.spin_final) % 1:
                raise ValueError(
                    "A photon transition cannot change integer to half-integer spin."
                )
        if not isfinite(self.delta):
            raise ValueError(
                "Known mixing ratio must be finite; select a pure multipole for pure limits."
            )


@dataclass(frozen=True)
class Measurement:
    value: float
    err_minus: float
    err_plus: float

    def __post_init__(self):
        if not all(isfinite(x) for x in (self.value, self.err_minus, self.err_plus)):
            raise ValueError("Measurement and errors must be finite.")
        if min(self.err_minus, self.err_plus) <= 0:
            raise ValueError("Both errors must be positive magnitudes.")


@dataclass(frozen=True)
class Geometry:
    theta_a_deg: float = 90.0
    theta_b_deg: float = 30.0
    theta_p_deg: float = 90.0
    relative_phi_deg: float = 0.0
    phi_p_deg: float = 0.0
    theta_gate_p_deg: float = 90.0
    phi_gate_p_deg: float = 0.0
    ratio_azimuth_average: bool = False
    polarization_gate_azimuth_average: bool = False
    ratio_group_a: DetectorGroup | None = None
    ratio_group_b: DetectorGroup | None = None
    polarization_group: DetectorGroup | None = None
    polarization_gate_group: DetectorGroup | None = None
    select_azimuth: bool = False

    def __post_init__(self):
        for key, value in vars(self).items():
            if key in ("ratio_group_a", "ratio_group_b", "polarization_group",
                       "polarization_gate_group"):
                if value is not None and not isinstance(value, DetectorGroup):
                    raise ValueError(f"{key} must be a DetectorGroup.")
                continue
            if key.endswith("_azimuth_average") or key == "select_azimuth":
                if not isinstance(value, bool):
                    raise ValueError(f"{key} must be a boolean.")
                continue
            if not isfinite(value) or (
                key.startswith("theta") and not 0 <= value <= 180
            ):
                raise ValueError(f"Invalid detector angle: {key} (degrees).")


@dataclass(frozen=True)
class GridSpec:
    xi_min_rad: float = -1.56
    xi_max_rad: float = 1.56
    xi_points: int = 3121
    sigma_min: float | None = None
    sigma_max: float | None = None
    sigma_points: int = 201
    xi_step_rad: float | None = None
    sigma_step: float | None = None
    xi_input_unit: str = "rad"
    sigma_input_unit: str = "sigma"

    def axes(self, reference_spin: float) -> tuple[np.ndarray, np.ndarray]:
        from multipolepdm.grid import MAX_GRID_POINTS, stepped_axis

        if self.xi_input_unit not in ("rad", "deg"):
            raise ValueError("Angle input unit must be 'rad' or 'deg'.")
        if self.sigma_input_unit not in ("sigma", "sigma/I"):
            raise ValueError("Width input unit must be 'sigma' or 'sigma/I'.")
        if reference_spin <= 0:
            raise ValueError(
                "I_ref=0 is a forward-response case, not a two-parameter sigma scan."
            )
        lo = (
            self.sigma_min
            if self.sigma_min is not None
            else (0.15 if reference_spin % 1 == 0 else 0.20)
        )
        hi = self.sigma_max if self.sigma_max is not None else reference_spin
        if not (isfinite(lo) and isfinite(hi) and 0 < lo < hi):
            raise ValueError("Require 0 < sigma_min < sigma_max.")
        if not (-pi / 2 < self.xi_min_rad < self.xi_max_rad < pi / 2):
            raise ValueError("xi grid must lie strictly inside (-pi/2, pi/2) radians.")
        for n, step in ((self.xi_points, self.xi_step_rad),
                        (self.sigma_points, self.sigma_step)):
            if step is not None:
                continue
            if isinstance(n, bool) or not isinstance(n, int) or n < 3:
                raise ValueError("Each grid axis requires at least three points.")
        # Reject excessive counts before allocating either axis.
        counts = []
        for low, high, step, points in (
            (self.xi_min_rad, self.xi_max_rad, self.xi_step_rad, self.xi_points),
            (lo, hi, self.sigma_step, self.sigma_points),
        ):
            if step is not None:
                if not isfinite(step) or step <= 0:
                    raise ValueError("Grid step must be finite and positive.")
                counts.append((high-low)/step + 2)
            else:
                counts.append(points)
        if counts[0] * counts[1] > MAX_GRID_POINTS:
            raise ValueError(
                "Grid exceeds 20 million points; reduce resolution or split the study."
            )
        xi = (stepped_axis(self.xi_min_rad, self.xi_max_rad, self.xi_step_rad)
              if self.xi_step_rad is not None else
              np.linspace(self.xi_min_rad, self.xi_max_rad, self.xi_points))
        sigma = (stepped_axis(lo, hi, self.sigma_step) if self.sigma_step is not None
                 else np.linspace(lo, hi, self.sigma_points))
        return xi, sigma


@dataclass(frozen=True)
class OutputSpec:
    directory: str = "pdm-results"
    full_csv: bool = False


@dataclass(frozen=True)
class JobRequest:
    mode: str
    target: Transition
    polarization: Measurement
    angular_ratio: Measurement
    label: str = "Transition"
    gate: Transition | None = None
    target_first: bool = True
    intermediates: tuple[Transition, ...] = ()
    geometry: Geometry = field(default_factory=Geometry)
    grid: GridSpec = field(default_factory=GridSpec)
    output: OutputSpec = field(default_factory=OutputSpec)

    def __post_init__(self):
        if self.mode not in ("P_ADO", "P_DCO", "PDCO"):
            raise ValueError("Unknown mode; choose P_ADO, P_DCO, or PDCO.")
        object.__setattr__(self, "intermediates", tuple(self.intermediates))
        if not isinstance(self.target_first, bool):
            raise ValueError("target_first must be a boolean.")
        if self.mode == "P_ADO":
            if self.gate is not None or self.intermediates:
                raise ValueError(
                    "P_ADO has no directional gate or intermediate path inputs."
                )
        else:
            if self.gate is None:
                raise ValueError("DCO modes require a gate transition.")
            first, last = (
                (self.target, self.gate)
                if self.target_first
                else (self.gate, self.target)
            )
            path = (first, *self.intermediates, last)
            if any(a.spin_final != b.spin_initial for a, b in zip(path, path[1:])):
                raise ValueError(
                    "Path endpoint spins do not match; supply intermediate transitions."
                )

    @property
    def reference_spin(self) -> float:
        return (
            self.target.spin_initial
            if self.mode == "P_ADO" or self.target_first
            else self.gate.spin_initial
        )

    @property
    def ratio_name(self) -> str:
        return "R_ADO" if self.mode == "P_ADO" else "R_DCO"


@dataclass(frozen=True)
class ResponseGrid:
    xi_rad: np.ndarray
    sigma: np.ndarray
    polarization: np.ndarray
    angular_ratio: np.ndarray
    valid: np.ndarray
    reference_spin: float
    ratio_name: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class MappingResult:
    job: JobRequest
    response: ResponseGrid
    observation_density: np.ndarray
    jacobian: np.ndarray
    parameter_density: np.ndarray
    normalization: float
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class Interval:
    mass: float
    eti: tuple[float, float]
    hdi_segments: tuple["HDISegment", ...]
    hdi_threshold: float

    @property
    def hdi(self) -> tuple[tuple[float, float], ...]:
        return tuple(segment.bounds for segment in self.hdi_segments)


@dataclass(frozen=True)
class HDISegment:
    bounds: tuple[float, float]
    mass: float
    mode_ranges: tuple[tuple[float, float], ...]


@dataclass(frozen=True)
class MarginalSummary:
    coordinate: np.ndarray
    density: np.ndarray
    median: float
    mode: float
    intervals: tuple[Interval, ...]
    coordinate_name: str
    evaluation_coordinate: str
    mean: float
    std: float | None
    mean_bounds: tuple[float | None, float | None]
    mean_bound_flags: tuple[tuple[str, ...], tuple[str, ...]]


@dataclass(frozen=True)
class MarginalPDF:
    coordinate: np.ndarray
    density: np.ndarray
    coordinate_name: str


@dataclass(frozen=True)
class TanAngleInterval:
    mass: float
    tan_eti: tuple[float, float]
    tan_hdi_segments: tuple[HDISegment, ...]
    angle_hdi_threshold: float


@dataclass(frozen=True)
class TanAngleStatistics:
    """Transformed angle estimates, not statistics evaluated on the delta PDF."""

    tan_median: float
    tan_mode: float
    tan_mean: float
    tan_mean_std_endpoints: tuple[float | None, float | None]
    mean_bound_flags: tuple[tuple[str, ...], tuple[str, ...]]
    intervals: tuple[TanAngleInterval, ...]
    evaluation_coordinate: str = "arctan_delta"
    transformation: str = "tan"

    @classmethod
    def from_marginal(cls, marginal: MarginalSummary) -> "TanAngleStatistics":
        if marginal.coordinate_name != "delta" or marginal.evaluation_coordinate != "arctan_delta":
            raise ValueError("Expected tan-transformed arctan(delta) statistics.")
        return cls(
            marginal.median,
            marginal.mode,
            marginal.mean,
            marginal.mean_bounds,
            marginal.mean_bound_flags,
            tuple(
                TanAngleInterval(
                    interval.mass, interval.eti, interval.hdi_segments, interval.hdi_threshold
                )
                for interval in marginal.intervals
            ),
        )


@dataclass(frozen=True)
class Summary:
    """Keep delta as a legacy aggregate; use the separate PDF and statistic views."""

    delta: MarginalSummary
    sigma_over_i: MarginalSummary
    arctan_delta: MarginalSummary

    @property
    def delta_pdf(self) -> MarginalPDF:
        return MarginalPDF(self.delta.coordinate, self.delta.density, "delta")

    @property
    def tan_angle_statistics(self) -> TanAngleStatistics:
        return TanAngleStatistics.from_marginal(self.delta)
