#!/usr/bin/env python3
"""
Calibrated Quantum Microscopic Cranking and Core Polarization for Antimagnetic Rotation (AMR).
Benchmark target: 110Cd Band 1 (Roy et al., Phys. Lett. B 697, 275 (2011)).
- Experimental states: I = 16+, 18+, 20+, 22+, 24+
- Experimental omega: 0.38 - 0.65 MeV
- Experimental B(E2): 0.14(1) -> 0.06(2) e^2 b^2
- J^(2)/B(E2): 245 - 414 hbar^2 / MeV / (e^2 b^2)
"""

import csv
import json
import math
import numpy as np
from scipy.optimize import minimize

def run_calibrated_amr():
    # 110Cd parameters
    # 2 proton holes in g9/2 (j_pi = 4.5), 2 neutron particles in h11/2 (j_nu = 5.5)
    # Maximum blade alignment spin = 2*4.5 + 2*5.5 = 20 hbar.
    j_pi = 4.5
    j_nu = 5.5

    C_shears = 14.2 # MeV
    C_core = 300.0  # MeV, rigid core resistant to large centrifugal deformation
    beta2_0 = 0.115
    J0_core = 6.2   # Core dynamic moment of inertia hbar^2 / MeV

    exp_data = [
        {"I": 16, "omega": 0.382, "BE2_exp": None, "BE2_err": None},
        {"I": 18, "omega": 0.453, "BE2_exp": 0.14, "BE2_err": 0.01},
        {"I": 20, "omega": 0.523, "BE2_exp": 0.12, "BE2_err": 0.01},
        {"I": 22, "omega": 0.588, "BE2_exp": 0.08, "BE2_err": 0.01},
        {"I": 24, "omega": 0.645, "BE2_exp": 0.06, "BE2_err": 0.02}
    ]

    results = []

    for i, d in enumerate(exp_data):
        omega = d["omega"]

        def routhian(x):
            th_pi, th_nu, beta2 = x
            cos_pi = np.cos(th_pi)
            cos_nu = np.cos(th_nu)
            E_shears = 0.5 * C_shears * ((j_pi * cos_pi + j_nu * cos_nu) / (j_pi + j_nu))**2
            E_core = 0.5 * C_core * (beta2 - beta2_0)**2
            J_core = J0_core * (beta2 / beta2_0)
            Ix_blades = 2.0 * j_pi * cos_pi + 2.0 * j_nu * cos_nu
            R = E_shears + E_core - omega * Ix_blades - 0.5 * J_core * (omega ** 2)
            return R

        x0 = [1.0, 1.0, 0.115]
        bnds = [(0.0, np.pi/2.0), (0.0, np.pi/2.0), (0.08, 0.16)]
        res = minimize(routhian, x0, bounds=bnds, method="L-BFGS-B")

        th_pi_opt, th_nu_opt, beta2_opt = res.x
        J_core_opt = J0_core * (beta2_opt / beta2_0)
        I_blades = 2.0 * j_pi * np.cos(th_pi_opt) + 2.0 * j_nu * np.cos(th_nu_opt)
        I_total = I_blades + J_core_opt * omega

        sin4_factor = (np.sin(th_pi_opt) * np.sin(th_nu_opt)) ** 2
        BE2_shears = 0.105 * sin4_factor
        BE2_core = 0.055 * (beta2_opt / beta2_0)**2
        BE2_total = BE2_shears + BE2_core

        results.append({
            "I_nominal": d["I"],
            "omega_MeV": float(round(omega, 3)),
            "theta_pi_deg": float(round(math.degrees(th_pi_opt), 1)),
            "theta_nu_deg": float(round(math.degrees(th_nu_opt), 1)),
            "beta2_core": float(round(beta2_opt, 4)),
            "I_blades": float(round(I_blades, 2)),
            "I_calc": float(round(I_total, 2)),
            "B_M1": 0.0,
            "B_E2_calc_e2b2": float(round(BE2_total, 3)),
            "B_E2_shears_e2b2": float(round(BE2_shears, 3)),
            "B_E2_core_e2b2": float(round(BE2_core, 3)),
            "B_E2_exp": d["BE2_exp"],
            "B_E2_err": d["BE2_err"]
        })

    for i in range(len(results)):
        if i == 0:
            dI = results[1]["I_calc"] - results[0]["I_calc"]
            dw = results[1]["omega_MeV"] - results[0]["omega_MeV"]
        elif i == len(results) - 1:
            dI = results[-1]["I_calc"] - results[-2]["I_calc"]
            dw = results[-1]["omega_MeV"] - results[-2]["omega_MeV"]
        else:
            dI = results[i+1]["I_calc"] - results[i-1]["I_calc"]
            dw = results[i+1]["omega_MeV"] - results[i-1]["omega_MeV"]
        J2 = dI / dw
        results[i]["J2_hbar2_per_MeV"] = float(round(J2, 1))
        be2 = results[i]["B_E2_calc_e2b2"]
        results[i]["J2_over_BE2_calc"] = float(round(J2 / be2, 0)) if be2 > 0 else 0.0

    return results

def main():
    results = run_calibrated_amr()

    json_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-quantum-four-blade/cd110_amr_quantum_cranking.json"
    csv_path = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/amr-quantum-four-blade/cd110_amr_quantum_cranking.csv"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    keys = results[0].keys()
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    print(f"Generated: {json_path}")
    print(f"Generated: {csv_path}")

if __name__ == "__main__":
    main()
