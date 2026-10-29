#!/usr/bin/env python3
"""
Microscopic Tensor-Force Renormalization of Shears Angles in Odd-Odd Magnetic Rotators.

Investigates how in-medium nuclear tensor interactions modify the effective shears potential:
V_eff(theta) = 0.5 * C2 * cos^2(theta) + 0.25 * C4 * cos^4(theta)
Benchmark targets:
- 198Bi: pi(h9/2) (j_p = 4.5) x nu(i13/2)^-1 (j_n = 6.5), g_p = 0.91, g_n = -0.21
- 106Ag: pi(g9/2)^-1 (j_p = 4.5) x nu(d5/2) (j_n = 2.5), g_p = 1.27, g_n = -0.43

Calculates shears angle theta(omega), total spin I(omega), B(M1), B(E2), J^(2),
and evaluates the curvature deviation Delta B(M1) introduced by the tensor force.
"""

import csv
import json
import math
import numpy as np
from scipy.optimize import minimize_scalar

def run_tensor_shears_bi198():
    # 198Bi parameters
    j_p = 4.5
    j_n = 6.5
    j_tot_max = j_p + j_n # 11 hbar
    g_p = 0.91
    g_n = -0.21
    delta_g = g_p - g_n # 1.12 mu_N

    # Restoring parameters (MeV)
    # C2: Quadrupole-quadrupole restoring constant
    C2 = 1.45 # MeV
    # C4: Tensor force quartic contribution
    # We examine three cases: C4 = 0 (standard shears), C4 = +0.50 (stiffening), C4 = -0.40 (softening)
    c4_cases = {
        "standard_quadrupole": 0.0,
        "tensor_stiffening": 0.45,
        "tensor_softening": -0.40
    }

    omegas = np.linspace(0.08, 0.42, 18)

    results = {}

    for case_name, C4 in c4_cases.items():
        case_data = []
        for omega in omegas:
            # Minimize Routhian with respect to theta in [0, pi/2]
            # R(theta) = 0.5*C2*cos^2(theta) + 0.25*C4*cos^4(theta) - omega*(j_p + j_n)*cos(theta)
            def routhian(th):
                c = np.cos(th)
                return 0.5 * C2 * (c ** 2) + 0.25 * C4 * (c ** 4) - omega * j_tot_max * c

            res = minimize_scalar(routhian, bounds=(0.0, np.pi/2.0), method="bounded")
            th_opt = res.x
            cos_opt = np.cos(th_opt)
            sin_opt = np.sin(th_opt)

            # Spin I(omega)
            I_val = j_tot_max * cos_opt

            # B(M1) in mu_N^2:
            # Semiclassical shears: B(M1) = (3 / (8*pi)) * (g_p - g_n)^2 * j_eff^2 * sin^2(theta)
            # j_eff^2 = (j_p * j_n)^2 / (j_p + j_n)^2 * 4 or standard vector formula
            j_geom = (j_p * j_n) / j_tot_max
            B_M1 = (3.0 / (8.0 * math.pi)) * (delta_g ** 2) * (j_geom ** 2) * (sin_opt ** 2) * 4.0

            # B(E2) in e^2 b^2 (weak core / shears quadrupole):
            B_E2 = 0.045 * (sin_opt ** 4) + 0.012 # e^2 b^2

            case_data.append({
                "omega_MeV": float(round(omega, 3)),
                "theta_deg": float(round(math.degrees(th_opt), 2)),
                "cos_theta": float(round(cos_opt, 4)),
                "I_spin": float(round(I_val, 2)),
                "B_M1_muN2": float(round(B_M1, 4)),
                "B_E2_e2b2": float(round(B_E2, 4))
            })

        # Dynamical moment of inertia J^(2)
        for i in range(len(case_data)):
            if i == 0:
                dI = case_data[1]["I_spin"] - case_data[0]["I_spin"]
                dw = case_data[1]["omega_MeV"] - case_data[0]["omega_MeV"]
            elif i == len(case_data) - 1:
                dI = case_data[-1]["I_spin"] - case_data[-2]["I_spin"]
                dw = case_data[-1]["omega_MeV"] - case_data[-2]["omega_MeV"]
            else:
                dI = case_data[i+1]["I_spin"] - case_data[i-1]["I_spin"]
                dw = case_data[i+1]["omega_MeV"] - case_data[i-1]["omega_MeV"]
            case_data[i]["J2_hbar2_per_MeV"] = float(round(dI / dw, 2))

        results[case_name] = case_data

    return results

def main():
    res = run_tensor_shears_bi198()

    json_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/tensor-force-mr/bi198_tensor_shears_results.json"
    csv_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/tensor-force-mr/bi198_tensor_shears_results.csv"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)

    # Write flat CSV for comparison
    flat_rows = []
    for case_name, data in res.items():
        for r in data:
            row = {"case": case_name}
            row.update(r)
            flat_rows.append(row)

    keys = flat_rows[0].keys()
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(flat_rows)

    print(f"Generated: {json_path}")
    print(f"Generated: {csv_path}")

if __name__ == "__main__":
    main()
