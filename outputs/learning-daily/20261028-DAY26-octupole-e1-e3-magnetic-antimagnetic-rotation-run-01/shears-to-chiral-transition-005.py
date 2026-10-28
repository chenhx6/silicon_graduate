#!/usr/bin/env python3
"""
shears-to-chiral-transition-005.py

PhD-Level Microscopic Investigation:
Critical Geometric Bifurcation from Planar Shears (Magnetic Rotation)
to 3D Aplanar Chiral Rotation in A~130 Nuclei.

Formalism:
1. Two high-j quasiparticles coupled to a triaxial rotor (PRM / Classical TAC Routhian):
   - Proton particle in h11/2 (j_pi) strongly aligned to short axis (s)
   - Neutron hole in h11/2 (j_nu) strongly aligned to long axis (l)
   - Core collective rotation with hydrodynamic moments of inertia:
     J_k = (4/3) * J_0 * sin^2(gamma - 2*pi*k/3) for k = s, m, l
2. Total Routhian E'(theta, phi; omega, gamma):
   E' = - (omega_s * j_pi_s + omega_l * j_nu_l) - 0.5 * sum_k J_k * omega_k^2 + V_int(chi)
   where omega = (omega * sin(theta)*cos(phi), omega * sin(theta)*sin(phi), omega * cos(theta))
3. Symmetry Analysis:
   - Planar shears (phi = 0): invariant under S = T * R_y(pi)
   - Chiral bifurcation (phi != 0): S is spontaneously broken when J_m > J_s, J_l
     and omega exceeds critical frequency omega_c.
"""

import json
import math
import numpy as np

def calculate_moments_of_inertia(gamma_deg, J0=30.0):
    gamma = math.radians(gamma_deg)
    # k = 1 (s - short axis): k*2pi/3 = 2pi/3
    # k = 2 (m - intermediate axis): k*2pi/3 = 4pi/3
    # k = 3 (l - long axis): k*2pi/3 = 2pi
    Js = (4.0 / 3.0) * J0 * (math.sin(gamma - 2.0 * math.pi / 3.0)) ** 2
    Jm = (4.0 / 3.0) * J0 * (math.sin(gamma - 4.0 * math.pi / 3.0)) ** 2
    Jl = (4.0 / 3.0) * J0 * (math.sin(gamma)) ** 2
    return Js, Jm, Jl

def routhian_energy(theta, phi, omega, gamma_deg, j_pi=5.5, j_nu=5.5, J0=30.0, V_pn=1.5):
    Js, Jm, Jl = calculate_moments_of_inertia(gamma_deg, J0)

    # Angular velocity components
    w_s = omega * math.sin(theta) * math.cos(phi)
    w_m = omega * math.sin(theta) * math.sin(phi)
    w_l = omega * math.cos(theta)

    # Collective rotational energy in Routhian: - 0.5 * sum J_k w_k^2
    E_coll = -0.5 * (Js * w_s**2 + Jm * w_m**2 + Jl * w_l**2)

    # Coriolis coupling to aligned quasiparticles
    # Proton particle aligned with s-axis, neutron hole aligned with l-axis
    E_coriolis = - (w_s * j_pi + w_l * j_nu)

    # Residual particle-hole interaction (shears interaction): V_pn * (j_pi . j_nu) / (j_pi * j_nu)
    # In intrinsic frame, j_pi = (j_pi, 0, 0), j_nu = (0, 0, j_nu) -> scalar product is 0 for orthogonal blades
    # If blades recline under Coriolis, small adjustment
    E_int = V_pn * 0.5 * (math.cos(theta)**2) # phenomenological shears angle dependence

    return E_coll + E_coriolis + E_int

def find_routhian_minimum(omega, gamma_deg, j_pi=5.5, j_nu=5.5, J0=30.0, V_pn=1.5):
    # Scan theta in [0, pi/2] and phi in [0, pi/2]
    thetas = np.linspace(0.1, math.pi/2 - 0.05, 90)
    phis = np.linspace(0.0, math.pi/2, 91)

    min_E = 1e9
    best_theta = 0.0
    best_phi = 0.0

    for t in thetas:
        for p in phis:
            E = routhian_energy(t, p, omega, gamma_deg, j_pi, j_nu, J0, V_pn)
            if E < min_E:
                min_E = E
                best_theta = t
                best_phi = p

    return best_theta, best_phi, min_E

def run_systematic_study():
    results = {
        "title": "Bifurcation from Planar Shears MR to 3D Chiral Rotation",
        "parameters": {
            "j_pi": 5.5,
            "j_nu": 5.5,
            "J0": 30.0,
            "V_pn": 1.5,
            "gamma_scans": [-30.0, -20.0, -10.0, 0.0]
        },
        "omega_evolution": []
    }

    omegas = np.linspace(0.1, 0.7, 13)

    for g in [-30.0, -20.0, -10.0, 0.0]:
        Js, Jm, Jl = calculate_moments_of_inertia(g, J0=30.0)
        gamma_record = {
            "gamma_deg": g,
            "moments_of_inertia": {"Js": Js, "Jm": Jm, "Jl": Jl},
            "points": []
        }
        for w in omegas:
            t, p, E = find_routhian_minimum(w, g)
            # Check if planar or aplanar
            mode = "planar_magnetic_rotation" if p < 0.05 else "aplanar_chiral_rotation"
            # Calculate angular momentum components: I_k = J_k * w_k + j_k
            w_s = w * math.sin(t) * math.cos(p)
            w_m = w * math.sin(t) * math.sin(p)
            w_l = w * math.cos(t)

            Is = Js * w_s + 5.5
            Im = Jm * w_m
            Il = Jl * w_l + 5.5
            Itot = math.sqrt(Is**2 + Im**2 + Il**2)

            gamma_record["points"].append({
                "omega_MeV": round(float(w), 3),
                "theta_deg": round(math.degrees(t), 2),
                "phi_deg": round(math.degrees(p), 2),
                "mode": mode,
                "E_routhian_MeV": round(float(E), 4),
                "angular_momentum": {
                    "Is": round(float(Is), 3),
                    "Im": round(float(Im), 3),
                    "Il": round(float(Il), 3),
                    "Itot": round(float(Itot), 3)
                }
            })
        results["omega_evolution"].append(gamma_record)

    out_json = "outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/shears-to-chiral-transition-005.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    print("SUCCESS: wrote results to", out_json)

if __name__ == "__main__":
    run_systematic_study()
