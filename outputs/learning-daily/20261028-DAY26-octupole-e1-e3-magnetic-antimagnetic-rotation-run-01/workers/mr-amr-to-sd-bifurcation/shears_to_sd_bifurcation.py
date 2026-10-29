#!/usr/bin/env python3
"""
Bifurcation and Phase Diagram from Magnetic/Antimagnetic Rotation to Superdeformation at High Spin.

Models the competition between:
- Route A: Shears closing and non-collective termination in Well 1 (beta2 ~ 0.12);
- Route B: High-spin crossing into Superdeformed (SD) minimum in Well 2 (beta2 ~ 0.55).
Benchmark target: 194Pb (Z=82, N=112, A=194) and 110Cd (Z=48, N=62, A=110).

Calculates:
- Energy trajectories E_ND(I), E_SD(I);
- Crossing spin I_bifurc where E_SD drops below E_ND;
- Shears opening angle theta(I);
- Observable B(M1), B(E2), and dynamical moment of inertia J^(2)(I);
- WKB barrier tunneling probability P_tunnel(I).
"""

import csv
import json
import math
import numpy as np
from scipy.optimize import minimize_scalar

def run_pb194_bifurcation():
    # 194Pb parameters:
    # Well 1: weakly oblate/prolate core beta2 ~ 0.12, shears bandhead I ~ 11, shears blades j_p = 4.5, j_n = 6.5
    # Well 2: superdeformed minimum beta2 ~ 0.58, J_SD ~ 95 hbar^2 / MeV

    # Dual-well core potential V_core(beta2) in MeV:
    # Modeled as double-well polynomial: V(beta2) = a * (beta2 - beta1)^2 * (beta2 - beta2_sd) + barrier
    def v_core(b2):
        # Local minimum 1 at b2 = 0.12 (E = 0.0)
        # Saddle point at b2 = 0.35 (E = 3.8 MeV barrier)
        # Local minimum 2 at b2 = 0.56 (E_SD_excitation = 4.5 MeV at I=0)
        # Smooth representation:
        term1 = 35.0 * (b2 - 0.12)**2
        term_barrier = 3.6 * np.exp(-((b2 - 0.35)**2) / (2.0 * (0.08**2)))
        term2 = 4.2 + 45.0 * (b2 - 0.56)**2 - 4.2 * np.exp(-((b2 - 0.12)**2) / (2.0 * (0.08**2)))
        # Simplified robust dual well:
        e1 = 38.0 * (b2 - 0.12)**2
        e2 = 4.5 + 40.0 * (b2 - 0.56)**2
        # Blended with barrier
        barrier = 2.8 * np.exp(-((b2 - 0.34)**2) / (2.0 * (0.07**2)))
        return min(e1, e2) + barrier

    # Moment of inertia function: J(beta2) = J0 + k * beta2^2 (hbar^2 / MeV)
    def inertia_core(b2):
        return 16.0 + 240.0 * (b2 ** 2)

    # Shears parameters in Well 1
    C_shears = 1.65 # MeV
    j_p = 4.5
    j_n = 6.5
    j_blades_max = j_p + j_n # 11 hbar

    # Spin grid from I = 10 to 44 hbar
    spins = np.arange(12, 45, 2)

    results = []

    for I in spins:
        # 1. State in Well 1 (Normal Deformed / Shears mode):
        # Total spin I = I_blades + I_core
        # I_blades = j_blades_max * cos(theta), limited to [0, j_blades_max]
        # Minimize total energy with respect to theta
        def e_well1(th):
            cos_th = np.cos(th)
            i_b = j_blades_max * cos_th
            i_c = max(0.0, I - i_b)
            v_sh = 0.5 * C_shears * (cos_th ** 2)
            j_c = inertia_core(0.12)
            e_rot_c = (i_c ** 2) / (2.0 * j_c)
            return v_sh + e_rot_c

        res1 = minimize_scalar(e_well1, bounds=(0.0, np.pi/2.0), method="bounded")
        th_opt = res1.x
        cos_opt = np.cos(th_opt)
        sin_opt = np.sin(th_opt)
        e_nd = res1.fun

        # Shears observable properties in Well 1:
        # B(M1) ~ sin^2(theta)
        delta_g = 1.12 # mu_N
        j_geom = (j_p * j_n) / j_blades_max
        b_m1_nd = (3.0 / (8.0 * math.pi)) * (delta_g ** 2) * (j_geom ** 2) * (sin_opt ** 2) * 4.0 if I <= 24 else 0.02
        b_e2_nd = 0.05 + 0.08 * (sin_opt ** 4) # e^2 b^2

        # 2. State in Well 2 (Superdeformed Collective Rotor):
        # beta2 ~ 0.56, pure collective rotation around x: E_SD = E_excitation + I*(I+1) / (2*J_SD)
        j_sd = inertia_core(0.56) # ~ 91 hbar^2 / MeV
        e_sd = 4.5 + (I * (I + 1.0)) / (2.0 * j_sd)

        # SD observables:
        b_m1_sd = 0.0 # pure collective E2 rotor has negligible M1
        # Q0_sd ~ 20 eb -> B(E2; I -> I-2) ~ (5/(16*pi)) * Q0^2 * <I 0 2 0 | I-2 0>^2 ~ 1.5 - 2.0 e^2 b^2
        b_e2_sd = 1.85 # e^2 b^2

        # 3. Yrast phase selection:
        favored_phase = "MR_Shears" if e_nd <= e_sd else "Superdeformed"

        # 4. Barrier tunneling action S/hbar between Well 1 and Well 2:
        # Simple WKB barrier penetration: Delta_E_barrier ~ 2.8 - (e_sd - e_nd) if e_nd < e_sd
        v_eff_barrier = max(0.05, 2.5 - 0.08 * max(0.0, I - 18))
        # Tunneling probability
        p_tunnel = math.exp(- 2.0 * math.sqrt(2.0 * 20.0 * v_eff_barrier) * 0.24)

        results.append({
            "I_spin": int(I),
            "E_ND_MeV": float(round(e_nd, 3)),
            "E_SD_MeV": float(round(e_sd, 3)),
            "Delta_E_SD_minus_ND": float(round(e_sd - e_nd, 3)),
            "favored_phase": favored_phase,
            "shears_angle_deg": float(round(math.degrees(th_opt), 1)),
            "B_M1_ND_muN2": float(round(b_m1_nd, 3)),
            "B_E2_ND_e2b2": float(round(b_e2_nd, 3)),
            "B_E2_SD_e2b2": float(round(b_e2_sd, 3)),
            "P_tunnel_WKB": float(f"{p_tunnel:.2e}")
        })

    # Calculate dynamical moments of inertia J^(2) = dI / domega
    # For ND:
    for i in range(len(results)):
        if i < len(results) - 1:
            dE_nd = results[i+1]["E_ND_MeV"] - results[i]["E_ND_MeV"]
            dE_sd = results[i+1]["E_SD_MeV"] - results[i]["E_SD_MeV"]
            dI = results[i+1]["I_spin"] - results[i]["I_spin"]
            w_nd = dE_nd / dI
            w_sd = dE_sd / dI
            results[i]["omega_ND_MeV"] = float(round(w_nd, 3))
            results[i]["omega_SD_MeV"] = float(round(w_sd, 3))
        else:
            results[i]["omega_ND_MeV"] = results[i-1]["omega_ND_MeV"]
            results[i]["omega_SD_MeV"] = results[i-1]["omega_SD_MeV"]

    for i in range(len(results) - 1):
        dI = results[i+1]["I_spin"] - results[i]["I_spin"]
        dw_nd = max(0.005, results[i+1]["omega_ND_MeV"] - results[i]["omega_ND_MeV"])
        dw_sd = max(0.005, results[i+1]["omega_SD_MeV"] - results[i]["omega_SD_MeV"])
        results[i]["J2_ND_hbar2_per_MeV"] = float(round(dI / dw_nd, 1))
        results[i]["J2_SD_hbar2_per_MeV"] = float(round(dI / dw_sd, 1))
    results[-1]["J2_ND_hbar2_per_MeV"] = results[-2]["J2_ND_hbar2_per_MeV"]
    results[-1]["J2_SD_hbar2_per_MeV"] = results[-2]["J2_SD_hbar2_per_MeV"]

    return results

def main():
    results = run_pb194_bifurcation()

    json_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/mr-amr-to-sd-bifurcation/pb194_bifurcation_results.json"
    csv_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/mr-amr-to-sd-bifurcation/pb194_bifurcation_results.csv"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    keys = results[0].keys()
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    print(f"Generated: {json_path}")
    print(f"Generated: {csv_path}")

    # Print crossing summary
    for r in results:
        if r["favored_phase"] == "Superdeformed" and r["I_spin"] <= 30:
            print(f"Found SD crossing at spin I = {r['I_spin']}: E_ND = {r['E_ND_MeV']} MeV, E_SD = {r['E_SD_MeV']} MeV")
            break

if __name__ == "__main__":
    main()
