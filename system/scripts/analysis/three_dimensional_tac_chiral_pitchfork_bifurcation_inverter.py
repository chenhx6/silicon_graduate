#!/usr/bin/env python3
"""
three_dimensional_tac_chiral_pitchfork_bifurcation_inverter.py
==============================================================
Three-Dimensional Tilted Axis Cranking (3D-TAC) Chiral Pitchfork Bifurcation
Phase Transition Inverter & Out-of-Plane Orientation Energy Engine.

Physics Formulation:
--------------------
1. 3D-TAC Orientation Energy Surface:
   Based on "Chirality and Wobbling in Atomic Nuclei" (CRC Press 2025) Chapter 2 (J. Meng & P. W. Zhao),
   Chapter 9 (PDF pp. 204–221), P. W. Zhao et al. (Phys. Lett. B 699, 181, 2011),
   and S. Frauendorf & J. Meng (Nucl. Phys. A 617, 131, 1997):
   In triaxial odd-odd nuclei with high-j valence particles (proton particle j_p along short s-axis,
   neutron hole j_n along long l-axis, and collective core rotation R along intermediate m-axis),
   the total angular momentum J = (J_s, J_m, J_l) tilts in three dimensions:
     J_s = J * sin(theta) * cos(phi)
     J_m = J * sin(theta) * sin(phi)
     J_l = J * cos(theta)
   where:
     - theta in [0, pi] is the polar angle;
     - phi in [0, pi/2] is the out-of-plane azimuth (phi = 0 is the planar (s, l) frame).

2. Quasiclassical Energy Functional:
   E(J, theta, phi) = [ (J * sin(theta) * cos(phi) - j_p)^2 / (2 * J_s) ]
                    + [ (J * sin(theta) * sin(phi))^2 / (2 * J_m) ]
                    + [ (J * cos(theta) - j_n)^2 / (2 * J_l) ]
   where J_m > J_s, J_l is the hydrodynamical moment-of-inertia ordering.

3. Supercritical Pitchfork Bifurcation Mechanism:
   - Low Spin (J < J_crit):
     The core angular momentum is small. The minimum of E is locked in the planar boundary:
       phi_min = 0 deg (Planar Rotation, no chirality).
   - Bifurcation Critical Point J_crit:
     At the critical spin J_crit, the planar minimum becomes an unstable saddle point:
       J_crit = sqrt( [ j_p * (J_m / J_s) ]^2 + [ j_n * (J_m / J_l) ]^2 ) * factor
     The energy surface undergoes a supercritical pitchfork bifurcation, splitting into two
     time-reversal degenerate aplanar minima at:
       phi_min(J) = +- arccos( J_crit / J ) > 0 deg.
     All three components (J_s, J_m, J_l) are simultaneously non-zero!

4. Chiral Barrier Height & Quantum Tunneling:
   The potential energy barrier separating left-handed and right-handed states is:
     Delta_E_barrier(J) = E(J, theta_saddle, phi=0) - E(J, theta_min, phi_min).
   This barrier height governs the energy splitting Delta E(I) = E_chiral(Band 2) - E_chiral(Band 1)
   observed in experimental chiral doublet bands.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "134Pr_chiral_bifurcation": {
        "description": "134Pr landmark chiral nucleus (Frauendorf & Meng 1997, Petrache 1996)",
        "nucleus": "134Pr",
        "quasiparticles": {"j_p_hbar": 5.5, "j_n_hbar": 5.5},
        "moments_of_inertia": {"J_m": 30.0, "J_s": 12.0, "J_l": 6.0},
        "spins_to_evaluate": [10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0]
    },
    "128Cs_chiral_bifurcation": {
        "description": "128Cs chiral doublet benchmark (Grodner 2006, Grodner 2018)",
        "nucleus": "128Cs",
        "quasiparticles": {"j_p_hbar": 5.5, "j_n_hbar": 5.5},
        "moments_of_inertia": {"J_m": 34.0, "J_s": 14.0, "J_l": 8.0},
        "spins_to_evaluate": [10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 22.0]
    },
    "axial_symmetric_no_bifurcation": {
        "description": "Axially symmetric rotor (J_s = J_m) where pitchfork bifurcation cannot occur",
        "nucleus": "Axial-Rotor",
        "quasiparticles": {"j_p_hbar": 5.5, "j_n_hbar": 5.5},
        "moments_of_inertia": {"J_m": 25.0, "J_s": 25.0, "J_l": 10.0},
        "spins_to_evaluate": [10.0, 12.0, 14.0, 16.0, 18.0, 20.0]
    }
}


def evaluate_tac_energy(J, theta_rad, phi_rad, j_p, j_n, J_m, J_s, J_l):
    """
    Evaluates quasiclassical 3D-TAC orientation energy E(J, theta, phi) in MeV.
    """
    Js = J * math.sin(theta_rad) * math.cos(phi_rad)
    Jm = J * math.sin(theta_rad) * math.sin(phi_rad)
    Jl = J * math.cos(theta_rad)

    E_s = ((Js - j_p)**2) / (2.0 * max(1e-3, J_s))
    E_m = (Jm**2) / (2.0 * max(1e-3, J_m))
    E_l = ((Jl - j_n)**2) / (2.0 * max(1e-3, J_l))

    return E_s + E_m + E_l


def calculate_pitchfork_bifurcation(J_val, j_p, j_n, J_m, J_s, J_l):
    """
    Finds optimal (theta, phi) orientation and computes planar vs aplanar barrier.
    """
    # Grid search for global minimum on (theta, phi) surface
    thetas = np.linspace(0.1, math.pi / 2.0 - 0.05, 90)
    phis = np.linspace(0.0, math.pi / 2.0, 90)

    best_E = float("inf")
    best_theta = 0.0
    best_phi = 0.0

    # Also evaluate optimal planar energy at phi = 0
    planar_E = float("inf")
    planar_theta = 0.0

    for th in thetas:
        E_planar = evaluate_tac_energy(J_val, th, 0.0, j_p, j_n, J_m, J_s, J_l)
        if E_planar < planar_E:
            planar_E = E_planar
            planar_theta = th

        for ph in phis:
            E_curr = evaluate_tac_energy(J_val, th, ph, j_p, j_n, J_m, J_s, J_l)
            if E_curr < best_E:
                best_E = E_curr
                best_theta = th
                best_phi = ph

    # Barrier height: E(planar saddle) - E(aplanar minimum) in keV
    barrier_keV = max(0.0, (planar_E - best_E) * 1000.0)
    is_chiral = bool(best_phi > math.radians(5.0) and barrier_keV > 5.0)

    # Normalized chiral volume: V_chiral = sin(theta) * cos(theta) * sin(phi)
    v_chiral = math.sin(best_theta) * math.cos(best_theta) * math.sin(best_phi)

    return {
        "J_hbar": float(J_val),
        "optimal_theta_deg": float(math.degrees(best_theta)),
        "optimal_phi_deg": float(math.degrees(best_phi)),
        "is_chiral_phase": is_chiral,
        "planar_energy_MeV": float(planar_E),
        "min_energy_MeV": float(best_E),
        "chiral_barrier_keV": float(barrier_keV),
        "chiral_volume_metric": float(v_chiral)
    }


def run_chiral_pitchfork_analysis(nucleus, quasiparticles, moments_of_inertia, spins_to_evaluate):
    """
    Complete execution pipeline for 3D-TAC chiral pitchfork bifurcation analysis.
    """
    jp = quasiparticles["j_p_hbar"]
    jn = quasiparticles["j_n_hbar"]
    Jm = moments_of_inertia["J_m"]
    Js = moments_of_inertia["J_s"]
    Jl = moments_of_inertia["J_l"]

    # Approximate analytical critical spin J_crit
    if Jm > Js and Jm > Jl:
        J_crit_est = math.sqrt(jp**2 + jn**2) * (1.0 + (Js / Jm))
    else:
        J_crit_est = float("inf")

    spin_results = []
    for J in spins_to_evaluate:
        pt = calculate_pitchfork_bifurcation(J, jp, jn, Jm, Js, Jl)
        spin_results.append(pt)

    # Locate actual bifurcation point J_bifurcate where phi > 5 deg
    J_bif = None
    for pt in spin_results:
        if pt["is_chiral_phase"]:
            J_bif = pt["J_hbar"]
            break

    return {
        "nucleus": nucleus,
        "parameters": {
            "j_p_hbar": float(jp),
            "j_n_hbar": float(jn),
            "J_m": float(Jm),
            "J_s": float(Js),
            "J_l": float(Jl),
            "analytical_J_crit_est": float(J_crit_est)
        },
        "bifurcation_spin_J_crit": J_bif,
        "spin_evolution": spin_results
    }


def format_text_report(res, title="3D-TAC Chiral Pitchfork Bifurcation Inverter"):
    nuc = res["nucleus"]
    p = res["parameters"]
    evol = res["spin_evolution"]
    J_bif = res["bifurcation_spin_J_crit"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Quasiparticles: j_p = {p['j_p_hbar']:.1f}, j_n = {p['j_n_hbar']:.1f} hbar | MOI: [J_m={p['J_m']:.1f}, J_s={p['J_s']:.1f}, J_l={p['J_l']:.1f}]")
    lines.append("=" * 76)
    lines.append(f"  Pitchfork Bifurcation Critical Spin J_crit : {f'{J_bif:.1f} hbar' if J_bif is not None else 'NONE (No Chiral Phase)'}")
    lines.append("-" * 76)
    lines.append("Spin Evolution of 3D Orientation & Chiral Tunneling Barrier:")
    lines.append("  Spin J (hbar)   Theta (deg)   Phi (deg)    Phase       Barrier Delta_E (keV)   Chiral Vol")
    for pt in evol:
        phase_str = "CHIRAL (Aplanar)" if pt["is_chiral_phase"] else "PLANAR (phi=0)"
        lines.append(f"    {pt['J_hbar']:4.1f}          {pt['optimal_theta_deg']:5.1f}        {pt['optimal_phi_deg']:5.1f}     {phase_str:16}     {pt['chiral_barrier_keV']:8.1f}             {pt['chiral_volume_metric']:6.3f}")
    lines.append("-" * 76)
    max_barr = max([pt["chiral_barrier_keV"] for pt in evol])
    lines.append(f"  Maximum Chiral Barrier Height   : {max_barr:.1f} keV (Defines left-right tunneling splitting)")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="3D-TAC Chiral Pitchfork Bifurcation Inverter & Orientation Energy Engine."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        qp = p["quasiparticles"]
        moi = p["moments_of_inertia"]
        spins = p["spins_to_evaluate"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_chiral_pitchfork_analysis(
        nucleus=nucleus,
        quasiparticles=qp,
        moments_of_inertia=moi,
        spins_to_evaluate=spins
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
