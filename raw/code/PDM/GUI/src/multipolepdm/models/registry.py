"""Three observation definitions feeding one PDM core."""

import numpy as np

from multipolepdm.config import p_ado, p_dco, pdco
from multipolepdm.contracts import ResponseGrid
from multipolepdm.grid import axis_metadata
from multipolepdm.physics.detectors import (
    coincidence_azimuth_selection,
    resolve_detector_groups,
    uses_detector_groups,
)

MODE_CONFIGS = {c.MODE: c for c in (p_ado, p_dco, pdco)}
RESPONSE_ROUNDOFF_TOLERANCE = 1e-12


def detector_response_metadata(job, conditional):
    geometry = job.geometry
    grouped = uses_detector_groups(geometry)
    group_metadata = {}
    if grouped:
        ratio_points, polarization_points = coincidence_azimuth_selection(geometry)
        ratio_average = job.mode != "P_ADO" and not ratio_points
        polarization_average = conditional and not polarization_points
        average_azimuth = (
            not geometry.select_azimuth or ratio_average or polarization_average
        )
        groups = resolve_detector_groups(geometry, conditional)
        group_metadata = {
            "select_azimuth": geometry.select_azimuth,
            "detector_groups": {
                name: {
                    "normalization": group.normalization,
                    "directions": [
                        {
                            "theta_deg": direction.theta_deg,
                            "phi_deg": direction.phi_deg,
                            "weight": direction.weight,
                            "effective_weight": weight,
                        }
                        for direction, weight in zip(
                            group.directions, group.effective_weights
                        )
                    ],
                }
                for name, group in groups.items()
            },
        }
    else:
        ratio_average = job.mode != "P_ADO" and geometry.ratio_azimuth_average
        polarization_average = conditional and geometry.polarization_gate_azimuth_average
        average_azimuth = ratio_average or polarization_average
    return {
        "ratio_azimuth_average": ratio_average,
        "polarization_gate_azimuth_average": polarization_average,
        "azimuth_integration": (
            "Uniform nine-node intensity mean; polar angles remain fixed."
            if average_azimuth
            else "Point directions; no azimuthal averaging."
        ),
        **group_metadata,
    }


def build_response(job, xi_rad, sigma, conditional=False):
    from multipolepdm.physics.joint import response_channels

    xi_rad, sigma = np.asarray(xi_rad, dtype=float), np.asarray(sigma, dtype=float)
    if xi_rad.ndim != 1 or sigma.ndim != 1 or not np.all(np.isfinite(xi_rad)):
        raise ValueError("Response coordinates must be finite one-dimensional arrays.")
    pc, rc = response_channels(job, xi_rad, sigma, conditional)
    den = pc.sum(axis=0)
    valid = (den > 0) & (rc[1] > 0)
    polarization = np.full(den.shape, np.nan)
    angular_ratio = np.full(den.shape, np.nan)
    np.divide(pc[0] - pc[1], den, out=polarization, where=valid)
    np.divide(rc[0], rc[1], out=angular_ratio, where=valid)
    valid &= np.isfinite(polarization) & np.isfinite(angular_ratio)
    from multipolepdm.physics.symmetries import observable_constants

    constant_ratio, zero_polarization = observable_constants(job)
    # Preserve analytic identities instead of turning roundoff into a PDF.
    if constant_ratio is not None:
        angular_ratio[valid] = constant_ratio
    if zero_polarization:
        polarization[valid] = 0.0
    roundoff = RESPONSE_ROUNDOFF_TOLERANCE
    valid &= (np.abs(polarization) <= 1 + roundoff) & (angular_ratio >= -roundoff)
    polarization[valid] = np.clip(polarization[valid], -1, 1)
    angular_ratio[valid] = np.maximum(angular_ratio[valid], 0)
    polarization[~valid] = np.nan
    angular_ratio[~valid] = np.nan
    return ResponseGrid(
        xi_rad,
        sigma,
        polarization,
        angular_ratio,
        valid,
        job.reference_spin,
        job.ratio_name,
        {
            "polarization_definition": "direction-gated"
            if conditional
            else "single-line",
            "target_first": job.target_first,
            "reference_spin": job.reference_spin,
            "xi_unit": "rad",
            "core_alignment": "sigma",
            "grid": {
                name: axis_metadata(axis, requested_step)
                for name, axis, requested_step in (
                    ("arctan_delta_rad", xi_rad, job.grid.xi_step_rad),
                    ("sigma", sigma, job.grid.sigma_step),
                )
                if axis.size > 1
            },
            **detector_response_metadata(job, conditional),
            "undefined_response_points": int(np.count_nonzero(~valid)),
            "exact_observable_identities": {
                "unit_ratio": constant_ratio == 1.0,
                "zero_linear_polarization": zero_polarization,
            },
            "amplitude_convention": "KS/Droste: (-1)^L CG(Jf mf L q | Ji mi) D*; electric helicity factor lambda; e_theta parallel",
        },
    )


def evaluate_response(job, xi_rad=None, sigma=None):
    from multipolepdm.models import (
        p_ado as ado_model,
        p_dco as dco_model,
        pdco as pdco_model,
    )

    if xi_rad is None and sigma is None:
        xi_rad, sigma = job.grid.axes(job.reference_spin)
    elif xi_rad is None or sigma is None:
        raise ValueError("Provide both xi_rad and sigma axes, or neither.")
    return {"P_ADO": ado_model, "P_DCO": dco_model, "PDCO": pdco_model}[
        job.mode
    ].evaluate(job, xi_rad, sigma)
