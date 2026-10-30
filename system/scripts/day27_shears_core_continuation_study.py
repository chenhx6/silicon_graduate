#!/usr/bin/env python3
"""Conditional classical shears/core study; no fitted nuclear parameters."""

import argparse
import csv
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, minimize_scalar


def blade_sum(cos_angle, asymmetry):
    proton = (1.0 + asymmetry) / 2.0
    neutron = (1.0 - asymmetry) / 2.0
    return math.sqrt(proton**2 + neutron**2 + 2 * proton * neutron * cos_angle)


def energy(cos_angle, total_spin, asymmetry, core_parameter):
    """E/V, with spin divided by jp+jn and kappa=Jcore*V/(jp+jn)^2."""
    valence = blade_sum(cos_angle, asymmetry)
    return (total_spin - valence) ** 2 / (2 * core_parameter) + (
        3 * cos_angle**2 - 1
    ) / 2


def shifted_energy(cos_angle, total_spin, asymmetry, core_parameter):
    """E(c)/V-E(0)/V, avoiding a large angle-independent core energy."""
    product = (1 - asymmetry**2) / 4
    valence = blade_sum(cos_angle, asymmetry)
    reference = blade_sum(0, asymmetry)
    difference = 2 * product * cos_angle / (valence + reference)
    return (
        -difference * (2 * total_spin - valence - reference) / (2 * core_parameter)
        + 1.5 * cos_angle**2
    )


def equilibrium(cos_angle, asymmetry, core_parameter):
    product = (1 - asymmetry**2) / 4
    valence = blade_sum(cos_angle, asymmetry)
    valence_first = product / valence
    valence_second = -(product**2) / valence**3
    coefficient = 3 * core_parameter / product
    total_spin = valence * (1 + coefficient * cos_angle)
    spin_first = valence_first * (1 + coefficient * cos_angle) + (
        coefficient * valence
    )
    curvature = (
        valence_first**2 - (total_spin - valence) * valence_second
    ) / core_parameter + 3
    return {
        "asymmetry": asymmetry,
        "core_parameter": core_parameter,
        "cos_angle": cos_angle,
        "angle_deg": math.degrees(math.acos(cos_angle)),
        "valence_spin_over_blade_max": valence,
        "total_spin_over_blade_max": total_spin,
        "core_spin_over_blade_max": total_spin - valence,
        "incremental_valence_fraction": valence_first / spin_first,
        "energy_curvature_in_cos_angle": curvature,
        "remaining_valence_capacity_over_blade_max": 1 - valence,
    }


def old_masking(beta, effective_moment=0.25, angle_deg=90):
    radius = 1.2 * 160 ** (1 / 3)
    moment = 3 / math.sqrt(5 * math.pi) * 66 * radius**2
    moment *= beta * (1 + 0.36 * beta) / 100
    return (moment / effective_moment) ** 2 / math.sin(
        math.radians(angle_deg) / 2
    ) ** 4


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    # This is an independently minimized conditional Hamiltonian, not a replay
    # of the old classifier or a fit to 143Sm/60Ni experimental data.
    rows = []
    deviations = []
    force_residuals = []
    steps = (1e-3, 3e-4, 1e-4)
    for asymmetry in (0.0, 0.35, 0.6, 0.85, 0.95):
        for core_parameter in (0.001, 0.02, 0.1, 0.5):
            for cos_angle in np.linspace(0.05, 0.95, 19):
                row = equilibrium(float(cos_angle), asymmetry, core_parameter)
                target_spin = row["total_spin_over_blade_max"]
                solution = minimize_scalar(
                    shifted_energy,
                    bounds=(0, 1),
                    args=(target_spin, asymmetry, core_parameter),
                    method="bounded",
                    options={"xatol": 1e-12},
                )
                if not solution.success:
                    raise RuntimeError(solution.message)
                deviations.append(abs(solution.x - cos_angle))
                derivative_errors = []
                for step in steps:
                    derivative = (
                        shifted_energy(cos_angle + step, target_spin, asymmetry, core_parameter)
                        - shifted_energy(cos_angle - step, target_spin, asymmetry, core_parameter)
                    ) / (2 * step)
                    derivative_errors.append(abs(derivative))
                force_residuals.append(derivative_errors)
                row["numerically_minimized_cos_angle"] = solution.x
                rows.append(row)
    maximum_deviation = max(deviations)
    if maximum_deviation > 2e-7:
        raise AssertionError(f"Analytic/numeric minimum mismatch: {maximum_deviation}")
    if any(row["energy_curvature_in_cos_angle"] <= 0 for row in rows):
        raise AssertionError("Unstable interior equilibrium")
    if any(not 0 < row["incremental_valence_fraction"] < 1 for row in rows):
        raise AssertionError("Invalid differential spin decomposition")

    capacity = [
        {
            "asymmetry": value,
            "perpendicular_to_closed_capacity_fraction": 1
            - math.sqrt((1 + value**2) / 2),
        }
        for value in (0, 0.34, 0.35, 0.36, 0.6, 0.85, 0.95, 0.9999)
    ]
    if capacity[-1]["perpendicular_to_closed_capacity_fraction"] >= 1e-4:
        raise AssertionError("Extreme-asymmetry limit failed")
    # Zero interaction removes the P2 restoring term; its minimum then satisfies
    # j(c)=I whenever I lies inside the allowed valence interval.
    zero_interaction_checks = []
    for asymmetry in (0, 0.35, 0.6, 0.95):
        target_c = 0.4
        target = blade_sum(target_c, asymmetry)
        solution = minimize_scalar(
            lambda c: (target - blade_sum(c, asymmetry)) ** 2,
            bounds=(0, 1),
            method="bounded",
            options={"xatol": 1e-12},
        )
        zero_interaction_checks.append(abs(solution.x - target_c))
    if max(zero_interaction_checks) > 2e-7:
        raise AssertionError("Zero-interaction minimum failed")

    aggregate_strength = 0.4
    pair_count = 5
    gap = 1.0
    interaction_samples = np.array([0.2, -0.1, 0.5, 0.3, -0.4])
    individual_strength = aggregate_strength / pair_count
    per_pair_energy = individual_strength * interaction_samples.sum()
    aggregate_energy = aggregate_strength * interaction_samples.mean()
    if not math.isclose(per_pair_energy, aggregate_energy, abs_tol=1e-14):
        raise AssertionError("Equivalent interaction normalization failed")

    critical_beta = brentq(lambda beta: old_masking(beta) - 50, 1e-5, 0.4)
    csv_path = args.output_dir / "conditional-shears-core-scan.csv"
    with csv_path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    result = {
        "schema_version": 1,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "status": "conditional-model-verified",
        "data_kind": "specified illustrative Hamiltonian; not experimental",
        "hamiltonian": "E/V=(Ibar-jbar(c))^2/(2*kappa)+(3*c^2-1)/2",
        "assumptions": [
            "classical fixed nonzero blades",
            "core parallel to valence resultant",
            "repulsive quadrupole interaction V>0, Jcore>0",
            "closing sector 0<=cos(theta)<=1",
            "no pairing, crossing, triaxial core response, or quantum termination",
        ],
        "scan_rows": len(rows),
        "analytic_numeric_max_cos_angle_error": maximum_deviation,
        "finite_difference_steps": steps,
        "finite_difference_max_force_residuals": np.max(
            np.array(force_residuals), axis=0
        ).tolist(),
        "zero_interaction_max_error": max(zero_interaction_checks),
        "valence_capacity": capacity,
        "old_classifier_internal_check": {
            "beta_at_ratio50_with_its_fixed_inputs": critical_beta,
            "at_beta_005": old_masking(0.05),
            "at_beta_018": old_masking(0.18),
            "at_beta_025": old_masking(0.25),
            "meaning": "algebraic replay of assumptions; not a physical beta threshold",
        },
        "normalization_counterexample": {
            "same_interaction_energy": aggregate_energy,
            "gap_over_aggregate_strength": gap / aggregate_strength,
            "gap_over_per_pair_strength": gap / individual_strength,
            "old_threshold_3_5_changes_classification": True,
            "meaning": "same Hamiltonian written with Fbar or sum(F); no empirical pairing bound",
        },
        "artifact": {
            "path": csv_path.name,
            "sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        },
    }
    output = args.output_dir / "conditional-shears-core-result.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
