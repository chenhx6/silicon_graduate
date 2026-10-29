#!/usr/bin/env python3
"""
Finite-Range Shears Interaction and Rotational Frequency Quenching in Magnetic Rotation.

Models the effect of nuclear finite force range (mu = 0.8, 1.2, 1.6 fm) vs zero-range contact limit
on the shears restoring potential V_eff(theta) and rotational dynamics.
Benchmark system: 198Bi (j_p = 4.5, j_n = 6.5, delta_g = 1.12 mu_N).

Calculates:
- Non-linear restoring potential V(theta) and its derivatives;
- Equilibrium shears angle theta(omega) and total spin I(omega);
- Rotational frequency quenching curve omega(I);
- Dynamical moment of inertia J^(2)(omega);
- Reduced magnetic dipole transition rates B(M1; I -> I-1).
"""

import csv
import json
import math
import numpy as np
from scipy.optimize import minimize_scalar

def run_finite_range_model():
    j_p = 4.5
    j_n = 6.5
    j_tot_max = j_p + j_n # 11 hbar
    delta_g = 1.12 # mu_N
    R0 = 1.2 * (198.0 ** (1.0 / 3.0)) # ~ 6.99 fm

    # Ranges of nuclear forces to test (in fm):
    # Contact limit is approximated by a small range or pure quadratic in cos(theta)
    force_ranges = {
        "contact_zero_range": 0.0,
        "finite_range_0.8fm": 0.8,
        "finite_range_1.2fm_Gogny": 1.2,
        "finite_range_1.6fm": 1.6
    }

    # Reference potential depth V0 such that low-spin curvature matches experimental spacing
    V0 = 2.40 # MeV

    # Frequencies hbar*omega from 0.05 to 0.45 MeV
    omegas = np.linspace(0.06, 0.42, 19)
    results = {}

    for case_name, mu in force_ranges.items():
        case_data = []
        for omega in omegas:
            def routhian(th):
                # theta in [0, pi/2]
                cos_th = np.cos(th)
                if mu == 0.0:
                    # Contact limit: pure (1/2)*C*cos^2(th)
                    v_pot = 0.5 * V0 * (cos_th ** 2)
                else:
                    # Finite-range Gaussian overlap of two angular wavepackets on sphere of radius R0
                    # Distance d^2 = 2*R0^2 * (1 - cos(theta))
                    # Overlap ~ exp(- d^2 / (2*mu^2))
                    # Potential energy increases as blades close against repulsive core/overlap:
                    # V(theta) = V0 * [ 1.0 - exp( - (R0**2 / (mu**2)) * (1.0 - cos_th)) ]
                    # Normalizing to 0 at theta = pi/2:
                    arg_open = (R0**2 / (mu**2)) * 1.0 # 1 - cos(pi/2)
                    arg_th = (R0**2 / (mu**2)) * (1.0 - cos_th)
                    # Smooth saturation potential:
                    scale = 0.5 * V0 / (1.0 - np.exp(- (R0**2 / (mu**2))))
                    v_pot = scale * (np.exp(- arg_th) - np.exp(- arg_open))

                # Routhian: R = V_pot - omega * j_tot_max * cos(theta)
                return v_pot - omega * j_tot_max * cos_th

            res = minimize_scalar(routhian, bounds=(0.0, np.pi/2.0), method="bounded")
            th_opt = res.x
            cos_opt = np.cos(th_opt)
            sin_opt = np.sin(th_opt)
            i_spin = j_tot_max * cos_opt

            # Semiclassical B(M1):
            j_geom = (j_p * j_n) / j_tot_max
            b_m1 = (3.0 / (8.0 * math.pi)) * (delta_g ** 2) * (j_geom ** 2) * (sin_opt ** 2) * 4.0

            case_data.append({
                "omega_MeV": float(round(omega, 3)),
                "theta_shears_deg": float(round(math.degrees(th_opt), 2)),
                "cos_theta": float(round(cos_opt, 4)),
                "I_spin": float(round(i_spin, 2)),
                "B_M1_muN2": float(round(b_m1, 4))
            })

        # Dynamical moment of inertia J^(2) = dI / domega
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
    res = run_finite_range_model()

    json_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/finite-range-shears/finite_range_shears_results.json"
    csv_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/finite-range-shears/finite_range_shears_results.csv"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)

    flat_rows = []
    for case_name, data in res.items():
        for r in data:
            row = {"force_case": case_name}
            row.update(r)
            flat_rows.append(row)

    keys = flat_rows[0].keys()
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(flat_rows)

    print(f"Generated: {json_path}")
    print(f"Generated: {csv_path}")

    print("\n--- Comparison at omega = 0.26 MeV ---")
    for case_name, data in res.items():
        pt = [d for d in data if abs(d["omega_MeV"] - 0.26) < 0.01][0]
        print(f"{case_name:25s} | theta = {pt['theta_shears_deg']:5.1f} deg | Spin I = {pt['I_spin']:5.2f} | J^(2) = {pt['J2_hbar2_per_MeV']:5.1f} | B(M1) = {pt['B_M1_muN2']:.3f}")

if __name__ == "__main__":
    main()
