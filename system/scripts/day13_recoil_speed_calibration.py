#!/usr/bin/env python3
"""Source-anchored speed-stage and synthetic centroid-calibration exercises.

Mass-number masses and a few declared toy measurements are used. No detector
run is re-fitted and no stopping/TOF response is inferred from reported widths.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


U_MEV = 931.49410242
C_MM_PER_NS = 299.792458


def beta_from_kinetic(energy_mev, mass_mev):
    gamma = 1 + energy_mev / mass_mev
    return np.sqrt(1 - gamma**-2)


def doppler_factor(beta, cosine):
    return np.sqrt(1 - beta**2) / (1 - beta * cosine)


def calculate():
    stage_rows = []
    mass = 32 * U_MEV
    for energy in (50., 75., 120.3):
        gamma = 1 + energy / mass
        beta = float(beta_from_kinetic(energy, mass))
        derivative = 1 / (mass * gamma**3 * beta)
        step = 1e-3
        finite = float((beta_from_kinetic(energy + step, mass) -
                        beta_from_kinetic(energy - step, mass)) / (2 * step))
        assert abs(derivative / finite - 1) < 1e-7
        stage_rows.append({"kinetic_MeV": energy, "mass_approx_MeV": mass, "beta": beta,
                           "d_beta_d_T_per_MeV": derivative,
                           "sigma_beta_if_sigma_T_is_0_5_MeV": .5 * derivative})
    flight_rows = []
    for length in (105., 6000.):
        beta, st, sl = .07, .130, 1.0
        time = length / (C_MM_PER_NS * beta)
        covariance = np.diag([sl**2, st**2])
        j = np.array([1 / (C_MM_PER_NS * time), -length / (C_MM_PER_NS * time**2)])
        for rho in (-.8, 0., .8):
            covariance[0, 1] = covariance[1, 0] = rho * sl * st
            sigma = float(math.sqrt(j @ covariance @ j))
            flight_rows.append({"path_length_mm": length, "TOF_ns": time,
                                "beta": beta, "sigma_length_mm": sl, "sigma_time_ns": st,
                                "path_time_rho": rho, "sigma_beta_linear": sigma,
                                "boundary": "130ps scale inspired by source test; this path/uncertainty pair is invented"})
    # This is the nominal compound boost before emission/stopping, not the
    # Klemme measured mean residual speed. Ignore mass defects/Q/excitation.
    beam_mass, target_mass, kinetic = 28 * U_MEV, 110 * U_MEV, 125.
    momentum = math.sqrt(kinetic * (kinetic + 2 * beam_mass))
    beam_beta = momentum / (beam_mass + kinetic)
    total_beta = momentum / (beam_mass + target_mass + kinetic)
    compound = {"beam_mass_number": 28, "target_mass_number": 110, "T_beam_nominal_MeV": kinetic,
                "incident_beam_beta_mass_number_model": beam_beta,
                "center_of_mass_boost_before_target_loss": total_beta,
                "Klemme_reported_residue_mean_beta": .016,
                "boundary": "nominal boost versus reported emission-speed; discrepancy does not identify target loss/evaporation or a source error"}
    # Fitting velocity from the same moving-line centroids cannot replace
    # independent calibration; first-order offset/gain/beta Jacobian has rank2.
    e0, beta, alternate = 1000., .07, .0701
    theta = np.radians([35, 60, 90, 120, 145])
    cosine = np.cos(theta)
    exact = e0 * doppler_factor(beta, cosine)
    alternate_values = e0 * doppler_factor(alternate, cosine)
    design = np.column_stack([alternate_values, np.ones(len(theta))])
    gain, offset = np.linalg.lstsq(design, exact, rcond=None)[0]
    residuals = gain * alternate_values + offset - exact
    jbeta = exact * (-beta / (1 - beta**2) + cosine / (1 - beta * cosine))
    jacobian = np.column_stack([jbeta, e0 * doppler_factor(beta, cosine), np.ones(len(theta))])
    linear_jacobian = np.column_stack([e0 * cosine, e0 * (1 + beta * cosine), np.ones(len(theta))])
    units = np.diag([.001, .001, 1.])
    singular = np.linalg.svd(jacobian @ units, compute_uv=False)
    linear_singular = np.linalg.svd(linear_jacobian @ units, compute_uv=False)
    rank_linear = int(np.linalg.matrix_rank(linear_jacobian))
    rank_exact = int(np.linalg.matrix_rank(jacobian))
    assert rank_linear == 2 and rank_exact == 3
    assert max(abs(residuals)) < .003
    assert singular[-1] > 0 and linear_singular[-1] < 1e-12
    calibration = {"E0_keV": e0, "true_beta": beta, "alternative_beta": alternate,
                   "true_gain": 1., "true_offset_keV": 0., "alternative_gain": float(gain),
                   "alternative_offset_keV": float(offset), "theta_deg": np.degrees(theta).tolist(),
                   "centroid_residuals_keV": residuals.tolist(),
                   "max_centroid_residual_keV": float(max(abs(residuals))),
                   "linear_rank": rank_linear, "exact_rank": rank_exact,
                   "column_scales_beta_gain_offset": [.001, .001, 1.],
                   "exact_scaled_singular_values_keV": singular.tolist(),
                   "linear_scaled_singular_values_keV": linear_singular.tolist(),
                   "boundary": "illustrative unconstrained gain/offset alternative; a real independent source calibration may exclude it"}
    return {"schema_version": 1, "kind": "method-exercise; no experimental speed reconstruction or fit",
            "kinetic_speed_rows": stage_rows, "TOF_rows": flight_rows, "compound_boost_example": compound,
            "centroid_calibration_example": calibration,
            "verification": {"kinetic_derivative_finite_difference": True, "rank_counterexample": True,
                             "alternative_centroid_residual_under_0_003keV": True, "passed": True},
            "numpy_version": np.__version__}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args()
    r = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(r, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "verification": r["verification"]}))


if __name__ == "__main__":
    main()
