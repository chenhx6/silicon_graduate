"""Detector directions and effective response weights."""

from dataclasses import dataclass
from math import isfinite, radians


@dataclass(frozen=True)
class DetectorDirection:
    theta_deg: float
    phi_deg: float = 0.0
    weight: float = 1.0

    def __post_init__(self):
        if not isfinite(self.theta_deg) or not 0 <= self.theta_deg <= 180:
            raise ValueError("Detector theta must be in [0, 180] degrees.")
        if not isfinite(self.phi_deg):
            raise ValueError("Detector phi must be finite.")
        if not isfinite(self.weight) or self.weight < 0:
            raise ValueError("Detector weight must be finite and nonnegative.")


@dataclass(frozen=True)
class DetectorGroup:
    directions: tuple[DetectorDirection, ...]
    normalization: str = "mean"

    def __post_init__(self):
        directions = tuple(self.directions)
        if not all(isinstance(direction, DetectorDirection) for direction in directions):
            raise ValueError("Detector groups require DetectorDirection rows.")
        if not any(direction.weight > 0 for direction in directions):
            raise ValueError("Detector groups must have positive total weight.")
        if self.normalization not in ("mean", "sum"):
            raise ValueError("Detector normalization must be 'mean' or 'sum'.")
        object.__setattr__(self, "directions", directions)

    @property
    def effective_weights(self) -> tuple[float, ...]:
        weights = tuple(direction.weight for direction in self.directions)
        if self.normalization == "sum":
            return weights
        scale = max(weights)
        scaled = tuple(weight / scale for weight in weights)
        total = sum(scaled)
        return tuple(weight / total for weight in scaled)

    def weighted_radians(self):
        """Yield positive effective weights and (theta, phi) in radians."""
        for direction, weight in zip(self.directions, self.effective_weights):
            if weight > 0:
                yield weight, (
                    radians(direction.theta_deg),
                    radians(direction.phi_deg % 360),
                )


def uses_detector_groups(geometry):
    return any(
        group is not None
        for group in (
            geometry.ratio_group_a,
            geometry.ratio_group_b,
            geometry.polarization_group,
            geometry.polarization_gate_group,
        )
    )


def coincidence_azimuth_selection(geometry):
    """Return point selection for the ratio and polarization coincidences."""
    return (
        geometry.select_azimuth and not geometry.ratio_azimuth_average,
        geometry.select_azimuth and not geometry.polarization_gate_azimuth_average,
    )


def resolve_detector_groups(geometry, conditional):
    """Resolve omitted roles with their scalar direction and unit weight."""
    groups = {
        "ratio_group_a": geometry.ratio_group_a
        or DetectorGroup((DetectorDirection(geometry.theta_a_deg),)),
        "ratio_group_b": geometry.ratio_group_b
        or DetectorGroup(
            (DetectorDirection(geometry.theta_b_deg, geometry.relative_phi_deg),)
        ),
        "polarization_group": geometry.polarization_group
        or DetectorGroup((DetectorDirection(geometry.theta_p_deg, geometry.phi_p_deg),)),
    }
    if conditional:
        groups["polarization_gate_group"] = (
            geometry.polarization_gate_group
            or DetectorGroup(
                (DetectorDirection(geometry.theta_gate_p_deg, geometry.phi_gate_p_deg),)
            )
        )
    return groups
