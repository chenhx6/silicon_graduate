"""Joint intensities and their exact quadratic dependence on target mixing."""

import numpy as np

from multipolepdm.physics.amplitudes import (
    analyzer_amplitudes,
    emission_amplitudes,
    emit,
)
from multipolepdm.physics.detectors import (
    coincidence_azimuth_selection,
    resolve_detector_groups,
    uses_detector_groups,
)
from multipolepdm.physics.populations import initial_population
from multipolepdm.physics.propagation import propagate_path, propagate_unobserved


AZIMUTH_NODES = np.arange(9) * (2 * np.pi / 9)


def azimuth_mean_channels(job, xi_rad, rho, target_direction, gate_theta):
    """Average intensities at fixed gate polar angle, not polarization ratios.

    Nine equispaced nodes integrate every azimuth harmonic of the supported
    dipole/quadrupole photons exactly up to floating-point roundoff.
    """
    return np.mean(
        [
            joint_channels(job, xi_rad, rho, target_direction, (gate_theta, phi))
            for phi in AZIMUTH_NODES
        ],
        axis=0,
    )


def source_basis(job):
    d = round(2 * job.reference_spin + 1)
    basis = np.zeros((d, d, d), dtype=complex)
    basis[np.arange(d), np.arange(d), np.arange(d)] = 1
    return basis


def joint_channels(job, xi_rad, rho, target_direction, gate_direction):
    """Return parallel/perp target intensities, summing gate polarization.

    Directions are (theta_rad, phi_rad). rho may be unnormalized and batched.
    No branch normalization is performed, including at intermediate levels.
    """
    target = emission_amplitudes(job.target, *target_direction, xi_rad=xi_rad)
    gate = emission_amplitudes(job.gate, *gate_direction)
    result = []
    for analyzer in analyzer_amplitudes(target):
        if job.target_first:
            state = emit(rho, analyzer)
            state = propagate_path(state, job.intermediates)
            state = emit(state, gate)
        else:
            state = emit(rho, gate)
            state = propagate_path(state, job.intermediates)
            state = emit(state, analyzer)
        result.append(np.trace(state, axis1=-2, axis2=-1).real)
    return np.asarray(result)


def single_channels(job, xi_rad, rho, direction):
    if job.mode != "P_ADO" and not job.target_first:
        rho = propagate_unobserved(rho, job.gate)
        rho = propagate_path(rho, job.intermediates)
    a = emission_amplitudes(job.target, *direction, xi_rad=xi_rad)
    return np.asarray(
        [
            np.trace(emit(rho, t), axis1=-2, axis2=-1).real
            for t in analyzer_amplitudes(a)
        ]
    )


def grouped_single_channels(job, xi_rad, rho, group, select_azimuth):
    result = 0.0
    for weight, (theta, phi) in group.weighted_radians():
        if select_azimuth:
            channels = single_channels(job, xi_rad, rho, (theta, phi))
        else:
            channels = np.mean(
                [
                    single_channels(job, xi_rad, rho, (theta, node))
                    for node in AZIMUTH_NODES
                ],
                axis=0,
            )
        result = result + weight * channels
    return result


def grouped_joint_channels(job, xi_rad, rho, target_group, gate_group, select_azimuth):
    """Sum weighted coincidence channels for an axial source density."""
    result = 0.0
    gate_rows = tuple(gate_group.weighted_radians())
    for target_weight, target in target_group.weighted_radians():
        for gate_weight, gate in gate_rows:
            if select_azimuth:
                channels = joint_channels(job, xi_rad, rho, target, gate)
            else:
                channels = azimuth_mean_channels(
                    job, xi_rad, rho, (target[0], 0.0), gate[0]
                )
            result = result + target_weight * gate_weight * channels
    return result


def quadratic_coefficients(evaluator):
    mm = evaluator(0.0)
    ee = evaluator(np.pi / 2)
    me = evaluator(np.pi / 4) - (mm + ee) / 2
    return np.stack((mm, me, ee))


def evaluate_quadratic(coefficients, populations, xi_rad):
    # coefficients: [MM, ME, EE] x channels x source-m; output: channels x sigma x xi
    strengths = np.einsum("kcm,sm->kcs", coefficients, populations, optimize=True)
    c, s = np.cos(xi_rad), np.sin(xi_rad)
    return (
        strengths[0, ..., None] * c**2
        + 2 * strengths[1, ..., None] * c * s
        + strengths[2, ..., None] * s**2
    )


def grouped_evaluators(job, source, conditional):
    geometry = job.geometry
    groups = resolve_detector_groups(geometry, conditional)
    group_a, group_b = groups["ratio_group_a"], groups["ratio_group_b"]
    polarization_group = groups["polarization_group"]
    ratio_points, polarization_points = coincidence_azimuth_selection(geometry)

    def singles(xi, group):
        return grouped_single_channels(job, xi, source, group, geometry.select_azimuth)

    def polar(xi):
        if conditional:
            return grouped_joint_channels(
                job,
                xi,
                source,
                polarization_group,
                groups["polarization_gate_group"],
                polarization_points,
            )
        return singles(xi, polarization_group)

    def ratio(xi):
        if job.mode == "P_ADO":
            channels = (singles(xi, group_a), singles(xi, group_b))
        else:
            channels = (
                grouped_joint_channels(job, xi, source, group_a, group_b, ratio_points),
                grouped_joint_channels(job, xi, source, group_b, group_a, ratio_points),
            )
        return np.stack(channels).sum(axis=1)

    return polar, ratio


def scalar_evaluators(job, source, conditional):
    g = job.geometry
    rad = np.deg2rad
    pdir = (rad(g.theta_p_deg), rad(g.phi_p_deg))
    if conditional:
        pgate = (rad(g.theta_gate_p_deg), rad(g.phi_gate_p_deg))
        if g.polarization_gate_azimuth_average:
            polar = lambda xi: azimuth_mean_channels(job, xi, source, pdir, pgate[0])
        else:
            polar = lambda xi: joint_channels(job, xi, source, pdir, pgate)
    else:
        polar = lambda xi: single_channels(job, xi, source, pdir)
    a = (rad(g.theta_a_deg), 0.0)
    b = (rad(g.theta_b_deg), rad(g.relative_phi_deg))
    if job.mode == "P_ADO":
        ratio = lambda xi: np.stack(
            (
                single_channels(job, xi, source, a).sum(axis=0),
                single_channels(job, xi, source, b).sum(axis=0),
            )
        )
    elif g.ratio_azimuth_average:
        ratio = lambda xi: np.stack(
            (
                azimuth_mean_channels(job, xi, source, a, b[0]).sum(axis=0),
                azimuth_mean_channels(job, xi, source, (b[0], 0.0), a[0]).sum(axis=0),
            )
        )
    else:
        ratio = lambda xi: np.stack(
            (
                joint_channels(job, xi, source, a, b).sum(axis=0),
                joint_channels(job, xi, source, (b[0], 0.0), (a[0], b[1])).sum(axis=0),
            )
        )
    return polar, ratio


def response_channels(job, xi_rad, sigma, conditional=False):
    source = source_basis(job)
    pop = initial_population(job.reference_spin, sigma)
    if uses_detector_groups(job.geometry):
        polar, ratio = grouped_evaluators(job, source, conditional)
    else:
        polar, ratio = scalar_evaluators(job, source, conditional)
    cp = quadratic_coefficients(polar)
    cr = quadratic_coefficients(ratio)
    return evaluate_quadratic(cp, pop, xi_rad), evaluate_quadratic(cr, pop, xi_rad)
