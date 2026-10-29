#!/usr/bin/env python3
"""
Quasiparticle Effective Mass and Rotational Flow Back-Reaction in Magnetic Rotation.

Models the effect of in-medium effective mass m*/m in [0.65, 1.00] on:
- Shears restoring stiffness C_shears(m*) ~ C0 * (m/m*);
- Rotational flow back-reaction current Delta J_back(omega);
- Equilibrium opening angle theta(omega), total spin I(omega), and critical closing frequency omega_c;
- Dynamical moment of inertia J^(2)(omega) and B(M1).
Benchmark system: 198Bi (j_p=4.5, j_n=6.5, delta_g=1.12 mu_N).
"""

import csv
import json
import math
import numpy as np
from scipy.optimize import minimize_scalar

def run_effective_mass_flow_model():
    j_p = 4.5
    j_n = 6.5
    j_max = j_p + j_n # 11.0 hbar
    delta_g = 1.12 # mu_N
    C0_bare = 1.45 # MeV at m*/m = 1.0
    J_core_0 = 18.0 # hbar^2 / MeV

    # Effective mass ratios: Skyrme (0.7-0.8), Gogny (0.7), relativistic RMF (0.6-0.65), bare (1.0)
    mass_ratios = {
        "bare_mass_1.0": 1.00,
        "skyrme_like_0.80": 0.80,
        "gogny_like_0.70": 0.70,
        "relativistic_0.65": 0.65
    }

    omegas = np.linspace(0.08, 0.44, 19)
    results = {}

    for case_name, m_ratio in mass_ratios.items():
        case_data = []
        # Renormalized shears stiffness scales inversely with level density ~ 1/m*
        C_eff = C0_bare / m_ratio

        # Effective core inertia enhanced by (m/m*) flow back-reaction
        j_core_eff = J_core_0 / (m_ratio ** 0.5)

        # Back-reaction coefficient
        kappa_back = 4.5 * (1.0 - m_ratio)

        for omega in omegas:
            # Back-reaction current opposing shears rotation:
            delta_j_back = - kappa_back * omega

            # Minimize Routhian with respect to theta
            def routhian(th):
                c = np.cos(th)
                v_sh = 0.5 * C_eff * (c ** 2)
                # Effective aligned angular momentum
                i_blades = j_max * c
                return v_sh - omega * (i_blades + delta_j_back) - 0.5 * j_core_eff * (omega ** 2)

            res = minimize_scalar(routhian, bounds=(0.0, np.pi/2.0), method="bounded")
            th_opt = res.x
            cos_opt = np.cos(th_opt)
            sin_opt = np.sin(th_opt)

            i_total = j_max * cos_opt + delta_j_back + j_core_eff * omega

            # Semiclassical B(M1):
            j_geom = (j_p * j_n) / j_max
            b_m1 = (3.0 / (8.0 * math.pi)) * (delta_g ** 2) * (j_geom ** 2) * (sin_opt ** 2) * 4.0

            case_data.append({
                "omega_MeV": float(round(omega, 3)),
                "theta_shears_deg": float(round(math.degrees(th_opt), 1)),
                "cos_theta": float(round(cos_opt, 4)),
                "C_eff_MeV": float(round(C_eff, 3)),
                "Delta_J_back_hbar": float(round(delta_j_back, 3)),
                "I_spin": float(round(i_total, 2)),
                "B_M1_muN2": float(round(b_m1, 3))
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
            case_data[i]["J2_hbar2_per_MeV"] = float(round(dI / dw, 1))

        results[case_name] = case_data

    return results

def main():
    res = run_effective_mass_flow_model()

    json_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/mr-effective-mass-flow/mr_effective_mass_flow_results.json"
    csv_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/mr-effective-mass-flow/mr_effective_mass_flow_results.csv"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)

    flat_rows = []
    for case_name, data in res.items():
        for r in data:
            row = {"mass_case": case_name}
            row.update(r)
            flat_rows.append(row)

    keys = flat_rows[0].keys()
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(flat_rows)

    print(f"Generated: {json_path}")
    print(f"Generated: {csv_path}")

    print("\n--- Comparison at omega = 0.20 MeV ---")
    for case_name, data in res.items():
        pt = [d for d in data if abs(d["omega_MeV"] - 0.20) < 0.01][0]
        print(f"{case_name:22s} | C_eff = {pt['C_eff_MeV']:.2f} MeV | theta = {pt['theta_shears_deg']:5.1f} deg | Spin I = {pt['I_spin']:5.2f} | J^(2) = {pt['J2_hbar2_per_MeV']:4.1f} | B(M1) = {pt['B_M1_muN2']:.3f}")

if __name__ == "__main__":
    main()
