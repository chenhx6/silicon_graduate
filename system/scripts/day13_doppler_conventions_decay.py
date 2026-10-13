#!/usr/bin/env python3
"""Explicit convention and decay-geometry toys for Day13, not source re-fits."""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


C_UM_PER_PS = 299.792458


def lab_exact(e0, beta, theta):
    return e0 * np.sqrt(1 - beta**2) / (1 - beta * np.cos(theta))


def inverse_exact(energy, beta, theta):
    return energy * (1 - beta * np.cos(theta)) / np.sqrt(1 - beta**2)


def lab_linear(e0, beta, theta):
    return e0 * (1 + beta * np.cos(theta))


def inverse_linear(energy, beta, theta):
    # Exact inverse of the stated approximate forward law. This is not the
    # first-order truncation E*(1-beta*cos(theta)), which is a third convention.
    return energy / (1 + beta * np.cos(theta))


def inside_uniform_target(depth_um, flight_length_um):
    if depth_um == 0:
        return 0.0
    a = depth_um / flight_length_um
    return 1 + math.expm1(-a) / a


def calculate(seed=1315, samples=500_000):
    rng = np.random.default_rng(seed)
    convention_rows = []
    exact_error = 0.
    linear_error = 0.
    for e0, beta in ((1434., .0548), (2168., .0589), (1000., .07)):
        for degrees in (0, 70, 90, 110, 180):
            theta = math.radians(degrees)
            le = float(lab_exact(e0, beta, theta))
            ll = float(lab_linear(e0, beta, theta))
            exact_error = max(exact_error, abs(inverse_exact(le, beta, theta) - e0))
            linear_error = max(linear_error, abs(inverse_linear(ll, beta, theta) - e0))
            mixed = float(inverse_exact(ll, beta, theta) - e0)
            opposite = float(inverse_linear(le, beta, theta) - e0)
            convention_rows.append({"E0_keV": e0, "beta": beta, "theta_deg": degrees,
                                    "exact_lab_keV": le, "linear_lab_keV": ll,
                                    "linear_forward_exact_inverse_residual_keV": mixed,
                                    "exact_forward_linear_inverse_residual_keV": opposite,
                                    "mixed_second_order_residual_keV": e0 * beta**2 * (0.5 - math.cos(theta)**2)})
    decay_rows = []
    max_mc_relative = 0.
    points, weights = leggauss(128)
    for nucleus, tau, beta in (("52Cr", 1.0099, .0548), ("38Ar", .578, .0589)):
        thickness = .5
        gamma = 1 / math.sqrt(1 - beta**2)
        length = beta * gamma * C_UM_PER_PS * tau
        exit_distance = rng.uniform(0., thickness, samples)
        emission_distance = rng.exponential(length, samples)
        mc = float(np.mean(emission_distance < exit_distance))
        analytical = inside_uniform_target(thickness, length)
        quadrature = float(np.dot(weights, -np.expm1(-(points + 1) * thickness / (2 * length))) / 2)
        assert abs(quadrature - analytical) < 1e-13
        relative = abs(mc / analytical - 1)
        max_mc_relative = max(max_mc_relative, relative)
        decay_rows.append({"nucleus_input_label": nucleus, "proper_lifetime_ps": tau, "beta": beta,
                           "mean_flight_um_lab_dilated": length,
                           "mean_flight_um_without_dilation": beta * C_UM_PER_PS * tau,
                           "target_depth_um": thickness,
                           "inside_probability_uniform_depth": analytical,
                           "inside_probability_start_of_target": -math.expm1(-thickness / length),
                           "inside_probability_MC": mc, "inside_probability_quadrature": quadrature,
                           "probability_after_1mm_without_feeding": math.exp(-1000 / length),
                           "MC_relative_difference": relative})
    # A shared incoming photon direction must be applied to the sum of all
    # deposits belonging to that one fully absorbed photon.
    e0, beta, theta1 = 1000., .07, math.radians(60)
    radius = 235.
    r1 = np.array([radius * math.sin(theta1), 0., radius * math.cos(theta1)])
    direction_of_scattered_photon = np.array([1., 0., 0.])
    r2 = r1 + 50 * direction_of_scattered_photon
    theta2 = math.acos(r2[2] / np.linalg.norm(r2))
    elab = float(lab_exact(e0, beta, theta1))
    scattering_angle = math.acos(float(np.dot(r1 / np.linalg.norm(r1), direction_of_scattered_photon)))
    e_scattered = elab / (1 + elab / 510.99895 * (1 - math.cos(scattering_angle)))
    e_deposit_1 = elab - e_scattered
    e_deposit_2 = e_scattered
    correct = float(inverse_exact(e_deposit_1 + e_deposit_2, beta, theta1))
    separately = float(inverse_exact(e_deposit_1, beta, theta1) +
                       inverse_exact(e_deposit_2, beta, theta2))
    wrong_first = float(inverse_exact(e_deposit_1 + e_deposit_2, beta, theta2))
    common_factor = float(inverse_exact(e_deposit_1, beta, theta1) +
                          inverse_exact(e_deposit_2, beta, theta1))
    assert abs(correct - e0) < 1e-10 and abs(common_factor - e0) < 1e-10
    assert e_deposit_2 > e_deposit_1  # Highest deposit would choose the second hit.
    assert exact_error < 1e-10 and linear_error < 1e-10
    assert max_mc_relative < .03
    assert inside_uniform_target(0., 10.) == 0.
    assert 0 < inside_uniform_target(.5, 10.) < inside_uniform_target(1., 10.) < 1.
    assert abs(inside_uniform_target(1., 1e6) - 5e-7) < 1e-12
    return {"schema_version": 1, "kind": "synthetic convention/decay/Compton-ordering checks",
            "seed": seed, "samples": samples, "convention_rows": convention_rows, "decay_rows": decay_rows,
            "Compton_two_hit_example": {"E0_keV": e0, "beta": beta, "first_emission_angle_deg": 60,
                                        "second_radial_angle_deg": math.degrees(theta2),
                                        "scatter_angle_deg": math.degrees(scattering_angle),
                                        "hit1_mm": r1.tolist(), "hit2_mm": r2.tolist(),
                                        "deposits_keV": [e_deposit_1, e_deposit_2],
                                        "corrected_sum_using_first_point_keV": correct,
                                        "wrong_separate_radial_corrections_keV": separately,
                                        "highest_deposit_wrong_first_point_keV": wrong_first,
                                        "sum_with_common_incoming_direction_keV": common_factor,
                                        "boundary": "assume second-hit photoelectric absorption; positions/energies are invented consistent Compton kinematics"},
            "verification": {"max_exact_roundtrip_error_keV": float(exact_error),
                             "max_linear_roundtrip_error_keV": float(linear_error),
                             "max_decay_MC_relative_difference": max_mc_relative,
                             "analytic_quadrature_match": True, "static_and_thin_target_limits": True,
                             "common_direction_energy_sum": True, "passed": True},
            "numpy_version": np.__version__}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--seed", type=int, default=1315)
    p.add_argument("--samples", type=int, default=500_000)
    a = p.parse_args()
    if a.samples < 1000:
        p.error("--samples must be at least 1000")
    result = calculate(a.seed, a.samples)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(a.output), "verification": result["verification"]}))


if __name__ == "__main__":
    main()
