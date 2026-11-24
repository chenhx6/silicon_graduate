"""Exact observable identities for the declared axial source and photon model."""

from fractions import Fraction
from math import isfinite

from multipolepdm.physics.detectors import (
    coincidence_azimuth_selection,
    resolve_detector_groups,
    uses_detector_groups,
)


def _axial_distribution(group, *, fold_theta, point):
    """Return the total effective weight and exact relative weights by direction."""
    counts = {}
    for row in group.directions:
        weight = Fraction(str(row.weight))
        if weight == 0:
            continue
        theta = Fraction(str(row.theta_deg))
        if fold_theta:
            theta = min(theta, 180 - theta)
        phi = Fraction(str(row.phi_deg)) % 360 if point and theta not in (0, 180) else 0
        key = (theta, phi)
        counts[key] = counts.get(key, 0) + weight
    total = sum(counts.values())
    distribution = {direction: weight / total for direction, weight in counts.items()}
    return (total if group.normalization == "sum" else Fraction(1)), distribution


def _grouped_constants(job):
    conditional = job.mode == "PDCO"
    geometry = job.geometry
    groups = resolve_detector_groups(geometry, conditional)
    ratio_points, polarization_points = coincidence_azimuth_selection(geometry)
    ado = job.mode == "P_ADO"
    total_a, distribution_a = _axial_distribution(
        groups["ratio_group_a"],
        fold_theta=ado or not ratio_points,
        point=not ado and ratio_points,
    )
    total_b, distribution_b = _axial_distribution(
        groups["ratio_group_b"],
        fold_theta=ado or not ratio_points,
        point=not ado and ratio_points,
    )
    constant_ratio = None
    if distribution_a == distribution_b:
        if ado:
            try:
                value = float(total_a / total_b)
            except OverflowError:
                value = float("inf")
            if isfinite(value) and value > 0:
                constant_ratio = value
        else:
            constant_ratio = 1.0
    if not ado and constant_ratio is None:
        folded_angles = {
            min(Fraction(str(row.theta_deg)), 180 - Fraction(str(row.theta_deg)))
            for group in (groups["ratio_group_a"], groups["ratio_group_b"])
            for row in group.directions
            if row.weight > 0
        }
        # On one polar cone and its mirror, exchanging the photon roles
        # preserves every even-rank term, including point-selected azimuths.
        if len(folded_angles) == 1:
            constant_ratio = 1.0

    def all_at_poles(group):
        return all(
            row.theta_deg in (0, 180) for row in group.directions if row.weight > 0
        )

    zero_polarization = all_at_poles(groups["polarization_group"]) and (
        not conditional
        or not polarization_points
        or all_at_poles(groups["polarization_gate_group"])
    )
    return constant_ratio, zero_polarization


def observable_constants(job):
    """Return the exact constant angular ratio, if any, and whether P is zero."""
    g = job.geometry
    if uses_detector_groups(g):
        return _grouped_constants(job)
    # Compare declared decimal angles exactly, without an angular tolerance.
    angle = lambda value: Fraction(str(value))
    a, b = angle(g.theta_a_deg), angle(g.theta_b_deg)
    unit_ratio = a == b or a + b == 180
    p, gate_p = angle(g.theta_p_deg), angle(g.theta_gate_p_deg)
    pole = lambda theta: theta == 0 or theta == 180
    if job.mode != "PDCO":
        zero_polarization = pole(p)
    else:
        zero_polarization = pole(p) and (
            pole(gate_p) or g.polarization_gate_azimuth_average
        )
        delta_phi = (angle(g.phi_p_deg) - angle(g.phi_gate_p_deg)) % 360
        collinear = (p == gate_p and delta_phi == 0) or (
            p + gate_p == 180 and abs(delta_phi) == 180
        )
        final_spin = job.gate.spin_final if job.target_first else job.target.spin_final
        # Collinear photons have total projection 0 or +/-2. If only 0 is
        # allowed, tracing the gate helicity removes all linear polarization.
        if (
            not g.polarization_gate_azimuth_average
            and not job.intermediates
            and job.reference_spin + final_spin < 2
            and collinear
        ):
            zero_polarization = True
    return 1.0 if unit_ratio else None, zero_polarization
