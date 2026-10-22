#!/usr/bin/env python3
"""Quantitative audit of Radeck 2012 distance-offset bridge and kinematic scaling.

Audits the coordinate relation between relative distance d and contact offset d0 in
Radeck 2012 Eq. (5) vs Eq. (9), evaluates in-flight decay probabilities across measured
distances, and quantifies the mechanical zero uncertainty compression in inverse kinematics.
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # Radeck 2012 parameters for 98Ru 2_1+ state (p. 7)
    v_radeck = 13.49  # um/ps (beta = 4.5%)
    tau_2_1 = 8.36    # ps
    v_tau = v_radeck * tau_2_1  # 112.7764 um decay length
    d0_nominal = 8.0  # um offset at electrical contact
    delta_d0 = 1.0    # um uncertainty on d0

    # Measured distances in Radeck 2012 (Figs. 3, 8, 10)
    distances = [3.0, 10.0, 20.0, 50.0, 100.0, 200.0, 300.0, 450.0]

    # Evaluate in-flight decay probability under both conventions
    # Convention A: Physical addition d_phys = d + d0, matching Eq. (9) printed exponent -(d + d0)/(v*tau)
    # Convention B: Literal subtraction d - d0 from Eq. (5)
    curve_comparison = []
    for d in distances:
        p_eq9 = 1.0 - math.exp(-(d + d0_nominal) / v_tau)
        p_eq5 = 1.0 - math.exp(-(d - d0_nominal) / v_tau)
        curve_comparison.append({
            "relative_distance_um": d,
            "P_convention_A_eq9": p_eq9,
            "P_convention_B_eq5": p_eq5,
            "t_flight_A_ps": (d + d0_nominal) / v_radeck,
            "t_flight_B_ps": (d - d0_nominal) / v_radeck,
        })

    # Assertions on Convention A vs B:
    # 1. At shortest distance d = 3 um:
    p3_A = curve_comparison[0]["P_convention_A_eq9"]
    p3_B = curve_comparison[0]["P_convention_B_eq5"]
    check("Convention A gives positive in-flight decay at d=3um (~9.3%)", 0.08 < p3_A < 0.10)
    check("Convention B gives unphysical negative decay probability at d=3um", p3_B < 0.0)

    # 2. Convention A matches visual Fig. 3 shifted peak observation (~8-10% shifted component)
    check("Convention A at d=3um matches ~9.3% in-flight decay", math.isclose(p3_A, 0.092932, rel_tol=1e-3))

    # 3. Both conventions converge at large distances (d = 450 um)
    p450_A = curve_comparison[-1]["P_convention_A_eq9"]
    p450_B = curve_comparison[-1]["P_convention_B_eq5"]
    check("At d=450um, Convention A exceeds 98%", p450_A > 0.98)
    check("At d=450um, difference between conventions is under 0.3%", abs(p450_A - p450_B) < 0.003)

    # 4. Kinematic compression of contact offset uncertainty Delta d0 = 1 um
    # In Radeck inverse kinematics: Delta_tau = Delta_d0 / v
    delta_tau_radeck = delta_d0 / v_radeck  # = 0.0741 ps
    v_klemme = 4.796  # um/ps (beta = 1.6%, normal kinematics)
    delta_tau_klemme = delta_d0 / v_klemme  # = 0.2085 ps
    compression_ratio = delta_tau_klemme / delta_tau_radeck  # = 2.8128

    check("Radeck offset sensitivity is ~0.074 ps (under 1% of tau=8.36 ps)",
          math.isclose(delta_tau_radeck, 0.074129, rel_tol=1e-4))
    check("Klemme offset sensitivity is ~0.209 ps",
          math.isclose(delta_tau_klemme, 0.208507, rel_tol=1e-4))
    check("Inverse kinematics compresses offset uncertainty by factor 2.81",
          math.isclose(compression_ratio, 2.81276, rel_tol=1e-4))

    # 5. Decay length comparison
    decay_length_radeck = v_tau  # 112.78 um
    decay_length_klemme = v_klemme * tau_2_1  # 40.09 um
    spatial_stretch = decay_length_radeck / decay_length_klemme
    check("Spatial decay length is stretched by factor 2.81 in inverse kinematics",
          math.isclose(spatial_stretch, compression_ratio, rel_tol=1e-12))

    # 6. Contact offset fraction of decay length
    offset_fraction_radeck = d0_nominal / decay_length_radeck
    offset_fraction_klemme = d0_nominal / decay_length_klemme
    check("d0 is only ~7.1% of decay length in Radeck", math.isclose(offset_fraction_radeck, 0.070937, rel_tol=1e-4))
    check("d0 is ~20.0% of decay length in conventional kinematics", math.isclose(offset_fraction_klemme, 0.199528, rel_tol=1e-4))

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Radeck 2012 distance-offset bridge (Eq. 5 vs Eq. 9) and kinematic scaling audit",
        "radeck_parameters": {
            "v_um_per_ps": v_radeck,
            "beta": 0.045,
            "tau_2_1_ps": tau_2_1,
            "decay_length_um": v_tau,
            "d0_nominal_um": d0_nominal,
            "delta_d0_um": delta_d0,
        },
        "coordinate_conventions": {
            "convention_A_eq9_physical": {
                "formula": "P(d) = a * [1 - exp((-d - d0)/(v*tau))]",
                "physical_meaning": "d0 is the residual foil separation at electrical contact; physical distance is d_phys = d + d0",
                "d_3um_in_flight_probability": p3_A,
                "validity": "Physically consistent with Fig. 3 observation of ~9% shifted component at d=3um",
            },
            "convention_B_eq5_literal": {
                "formula": "Gk(d) = alpha_k + (1 - alpha_k) * exp(-Gamma_k * (d - d0) / v)",
                "literal_meaning": "d - d0 subtraction",
                "d_3um_in_flight_probability": p3_B,
                "validity": "Yields unphysical negative probability (-4.5%) if d is interpreted as relative distance",
            },
            "reconciliation_rule": "Preserve literal text of both Eq. (5) and Eq. (9) without claiming an erratum; physical decay in Eq. (9) uses d_phys = d + d0",
        },
        "distance_curve_comparison": curve_comparison,
        "kinematic_compression_of_d0": {
            "radeck_delta_tau_ps": delta_tau_radeck,
            "klemme_delta_tau_ps": delta_tau_klemme,
            "compression_factor": compression_ratio,
            "insight": "High recoil velocity compresses absolute mechanical offset uncertainty Delta_d0 linearly: Delta_tau = Delta_d0 / v",
        },
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Radeck coordinate bridge audit completed: {len(checks)} checks passed.")
    print(f"Convention A P(d=3um): {p3_A*100:.2f}% (Convention B: {p3_B*100:.2f}%)")
    print(f"Kinematic compression of Delta_d0: {compression_ratio:.2f}x (Delta_tau: {delta_tau_radeck:.3f} ps vs {delta_tau_klemme:.3f} ps)")


if __name__ == "__main__":
    main()
