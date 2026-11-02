#!/usr/bin/env python3
"""
heavy_ion_dic_wilczynski_energy_loss_calculator.py
==================================================
Heavy-Ion Deep Inelastic Collisions (DIC), Total Kinetic Energy Loss (TKEL),
Angular Momentum Dissipation & Wilczynski Energy-Angle Correlation Simulator.

Physics & Engineering Formulation:
----------------------------------
1. Reaction Kinematics & Interaction Potential:
   Based on 林承键《重离子核反应》第 5 章, 吴治华《原子核物理实验方法》第 11 章,
   J. Wilczynski (Phys. Lett. B 47, 484, 1973), and W. U. Schröder & J. R. Huizenga (1977):
   For projectile (Ap, Zp) colliding with target (At, Zt) at laboratory energy Elab:
     Center-of-mass energy: E_cm = Elab * [At / (Ap + At)]
     Reduced mass: mu = [Ap * At / (Ap + At)] * m_u
     Interaction contact radius: R_int = r0 * (Ap^(1/3) + At^(1/3)) + d0  (r0 ~ 1.16 fm, d0 ~ 2.0 fm)
     Contact Coulomb barrier: V_C = 1.44 * Zp * Zt / R_int  (MeV)

2. Critical Angular Momenta & Reaction Windows:
   The grazing angular momentum for touching interaction:
     L_grazing = R_int * sqrt( 2 * mu * (E_cm - V_C) / hbar^2 )
   The critical angular momentum for complete fusion:
     L_crit = L_grazing * sqrt( max(0.0, 1.0 - V_B / E_cm) )
   Deep Inelastic Collisions (DIC) occur within the intermediate angular momentum window:
     L_crit < l <= L_grazing

3. Total Kinetic Energy Loss (TKEL) & Relaxation Model:
   The maximum energy loss corresponds to fully relaxed kinetic energy down to Coulomb barrier:
     TKEL_max = E_cm - V_C
   The energy loss as a function of impact angular momentum l is parameterized via relaxation:
     TKEL(l) = TKEL_max * [ 1.0 - exp( -k_diss * (L_grazing - l) / (L_grazing - L_crit) ) ]
   Final kinetic energy: E_final(l) = E_cm - TKEL(l).

4. Angular Momentum Transfer & The Sticking Limit:
   As the dinuclear system rotates, tangential friction transfers relative orbital
   angular momentum into intrinsic spins of both fragments:
     Rigid-body moments of inertia: J_i = (2/5) * A_i * R_i^2
     Relative moment of inertia: J_rel = mu * R_int^2
   Sticking limit fraction (maximal spin transfer):
     f_stick = (J_1 + J_2) / (J_rel + J_1 + J_2)
   Intrinsic spin transferred: Delta L(l) = l * f_stick * [ TKEL(l) / TKEL_max ]
   Fragment spins: J_p = Delta L * [Ap / (Ap + At)], J_t = Delta L * [At / (Ap + At)].

5. Wilczynski Plot Deflection Dynamics (Positive & Negative Angles):
   Near grazing (l ~ L_grazing), Coulomb repulsion dominates, producing positive scattering angles:
     theta_pos(l) = 2 * arctan( eta / l )   (where eta = Zp*Zt*e^2 / (hbar*v))
   Near fusion threshold (l -> L_crit), nuclear attractive forces pull the dinuclear complex
   across the beam axis to negative angles (nuclear orbiting):
     theta_neg(l) = theta_pos(l) - Delta theta_orbit(l)
   The observed angle is folded: theta_obs = |theta(l)|.
   Plotting (theta_obs, TKEL) creates the iconic Wilczynski "bird's beak" contour ridge!
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "86Kr_166Er_703MeV": {
        "description": "86Kr + 166Er at Elab = 703 MeV (Schröder & Huizenga 1977 benchmark)",
        "Ap": 86,
        "Zp": 36,
        "At": 166,
        "Zt": 68,
        "Elab_MeV": 703.0,
        "r0": 1.16,
        "d0": 2.0,
        "k_diss": 2.8
    },
    "40Ar_232Th_388MeV": {
        "description": "40Ar + 232Th at Elab = 388 MeV (Wilczynski 1973 discovery reaction)",
        "Ap": 40,
        "Zp": 18,
        "At": 232,
        "Zt": 90,
        "Elab_MeV": 388.0,
        "r0": 1.16,
        "d0": 2.0,
        "k_diss": 2.5
    },
    "136Xe_208Pb_860MeV": {
        "description": "136Xe + 208Pb at Elab = 860 MeV (Zagrebaev & Greiner multinucleon transfer)",
        "Ap": 136,
        "Zp": 54,
        "At": 208,
        "Zt": 82,
        "Elab_MeV": 860.0,
        "r0": 1.16,
        "d0": 2.2,
        "k_diss": 3.0
    }
}


def calculate_dic_kinematics(Ap, Zp, At, Zt, Elab_MeV, r0=1.16, d0=2.0):
    """
    Calculates center-of-mass energy, interaction contact radius, Coulomb barrier,
    and grazing/fusion angular momentum bounds.
    """
    A_tot = Ap + At
    E_cm = Elab_MeV * (At / A_tot)
    mu_u = (Ap * At) / A_tot
    hbar2_2mu = 20.7355 / mu_u  # MeV * fm^2

    R_p = 1.20 * (Ap**(1.0 / 3.0))
    R_t = 1.20 * (At**(1.0 / 3.0))
    R_int = r0 * (Ap**(1.0 / 3.0) + At**(1.0 / 3.0)) + d0
    V_C = 1.44 * Zp * Zt / R_int  # MeV

    V_B = V_C * 0.96

    if E_cm > V_C:
        L_grazing = R_int * math.sqrt((E_cm - V_C) / hbar2_2mu)
    else:
        L_grazing = 0.0

    if E_cm > V_B:
        L_crit = L_grazing * math.sqrt(max(0.0, 1.0 - V_B / E_cm))
    else:
        L_crit = 0.0

    J1 = 0.40 * Ap * (R_p**2)
    J2 = 0.40 * At * (R_t**2)
    J_rel = mu_u * (R_int**2)
    f_stick = (J1 + J2) / (J_rel + J1 + J2)

    v_rel_c = math.sqrt(2.0 * E_cm / (mu_u * 931.494))
    alpha_em = 1.0 / 137.036
    eta = (Zp * Zt * alpha_em) / max(1e-6, v_rel_c)

    theta_grazing_deg = 2.0 * math.degrees(math.atan(eta / max(1.0, L_grazing)))

    return {
        "Ap": Ap,
        "Zp": Zp,
        "At": At,
        "Zt": Zt,
        "Elab_MeV": float(Elab_MeV),
        "E_cm_MeV": float(E_cm),
        "mu_u": float(mu_u),
        "R_int_fm": float(R_int),
        "V_C_MeV": float(V_C),
        "V_B_MeV": float(V_B),
        "TKEL_max_MeV": float(max(0.0, E_cm - V_C)),
        "L_grazing_hbar": float(L_grazing),
        "L_crit_hbar": float(L_crit),
        "f_stick_fraction": float(f_stick),
        "sommerfeld_eta": float(eta),
        "theta_grazing_deg": float(theta_grazing_deg)
    }


def simulate_wilczynski_trajectory(kin, n_steps=30, k_diss=2.5):
    """
    Generates the discrete Wilczynski dynamics grid: angular momentum l,
    energy loss TKEL(l), final kinetic energy, transferred spins, and deflection angle.
    """
    L_crit = kin["L_crit_hbar"]
    L_graz = kin["L_grazing_hbar"]
    E_cm = kin["E_cm_MeV"]
    tkel_max = kin["TKEL_max_MeV"]
    f_stick = kin["f_stick_fraction"]
    eta = kin["sommerfeld_eta"]
    Ap = kin["Ap"]
    At = kin["At"]

    if L_graz <= L_crit:
        return []

    l_vals = np.linspace(L_graz, L_crit + 1.0, n_steps)
    trajectory = []

    for l in l_vals:
        frac_in = (L_graz - l) / (L_graz - L_crit)

        tkel = tkel_max * (1.0 - math.exp(-k_diss * frac_in))
        e_final = E_cm - tkel

        delta_L = l * f_stick * (tkel / max(1e-6, tkel_max))
        spin_p = delta_L * (Ap / (Ap + At))
        spin_t = delta_L * (At / (Ap + At))

        theta_coul_rad = 2.0 * math.atan(eta / l)
        theta_coul_deg = math.degrees(theta_coul_rad)

        delta_theta_orbit_deg = 85.0 * (frac_in**1.5)
        theta_deflect_deg = theta_coul_deg - delta_theta_orbit_deg
        theta_obs_deg = abs(theta_deflect_deg)

        branch = "positive_quasielastic" if theta_deflect_deg >= 0 else "negative_orbiting"

        trajectory.append({
            "angular_momentum_l": float(l),
            "penetration_fraction": float(frac_in),
            "TKEL_MeV": float(tkel),
            "E_final_MeV": float(e_final),
            "spin_transferred_hbar": float(delta_L),
            "spin_projectile_hbar": float(spin_p),
            "spin_target_hbar": float(spin_t),
            "deflection_angle_deg": float(theta_deflect_deg),
            "observed_angle_deg": float(theta_obs_deg),
            "branch": branch
        })

    return trajectory


def run_dic_analysis(Ap, Zp, At, Zt, Elab_MeV, r0=1.16, d0=2.0, k_diss=2.5, n_steps=25):
    """
    Complete DIC execution pipeline.
    """
    kin = calculate_dic_kinematics(Ap, Zp, At, Zt, Elab_MeV, r0, d0)
    traj = simulate_wilczynski_trajectory(kin, n_steps=n_steps, k_diss=k_diss)

    max_spin_trans = max([pt["spin_transferred_hbar"] for pt in traj]) if traj else 0.0
    orbiting_points = [pt for pt in traj if pt["branch"] == "negative_orbiting"]
    orbiting_fraction = (len(orbiting_points) / len(traj) * 100.0) if traj else 0.0

    return {
        "kinematics": kin,
        "max_spin_transfer_hbar": float(max_spin_trans),
        "negative_orbiting_fraction_percent": float(orbiting_fraction),
        "trajectory": traj
    }


def format_text_report(res, title="Heavy-Ion DIC Wilczynski Simulation"):
    kin = res["kinematics"]
    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Reaction: {kin['Ap']}Z({kin['Zp']}) + {kin['At']}Y({kin['Zt']}) at Elab = {kin['Elab_MeV']:.1f} MeV")
    lines.append("=" * 76)
    lines.append(f"  Center-of-Mass Energy (E_cm)    : {kin['E_cm_MeV']:.1f} MeV")
    lines.append(f"  Interaction Contact Radius (R_int): {kin['R_int_fm']:.2f} fm")
    lines.append(f"  Contact Coulomb Barrier (V_C)   : {kin['V_C_MeV']:.1f} MeV")
    lines.append(f"  Maximum Kinetic Energy Loss     : {kin['TKEL_max_MeV']:.1f} MeV (Fully Relaxed Limit)")
    lines.append(f"  Grazing Angular Momentum (L_graz): {kin['L_grazing_hbar']:.1f} hbar (Theta_graz = {kin['theta_grazing_deg']:.1f} deg)")
    lines.append(f"  Critical Fusion Momentum (L_crit): {kin['L_crit_hbar']:.1f} hbar")
    lines.append(f"  Sticking Limit Spin Fraction    : {kin['f_stick_fraction']*100.0:.1f}%")
    lines.append(f"  Maximum Spin Transferred to Core: {res['max_spin_transfer_hbar']:.1f} hbar")
    lines.append(f"  Nuclear Orbiting Branch Share   : {res['negative_orbiting_fraction_percent']:.1f}%")
    lines.append("-" * 76)
    lines.append("Wilczynski Trajectory Samples:")
    lines.append("   l (hbar)   TKEL (MeV)   E_final (MeV)   Delta_L (hbar)   Theta_obs (deg)   Branch")
    for idx, pt in enumerate(res["trajectory"]):
        if idx % max(1, len(res["trajectory"]) // 8) == 0 or idx == len(res["trajectory"]) - 1:
            lines.append(
                f"   {pt['angular_momentum_l']:6.1f}     {pt['TKEL_MeV']:8.1f}     {pt['E_final_MeV']:11.1f}     {pt['spin_transferred_hbar']:10.1f}       {pt['observed_angle_deg']:8.1f}       {pt['branch']}"
            )
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Heavy-Ion Deep Inelastic Collisions (DIC) Wilczynski Energy-Angle Correlation Simulator."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--Ap", type=int, help="Projectile mass number")
    parser.add_argument("--Zp", type=int, help="Projectile atomic number")
    parser.add_argument("--At", type=int, help="Target mass number")
    parser.add_argument("--Zt", type=int, help="Target atomic number")
    parser.add_argument("--Elab", type=float, help="Laboratory beam energy in MeV")
    parser.add_argument("--kdiss", type=float, default=2.5, help="Dissipation rate constant")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        Ap, Zp, At, Zt = p["Ap"], p["Zp"], p["At"], p["Zt"]
        Elab = p["Elab_MeV"]
        kdiss = p.get("k_diss", 2.5)
        r0 = p.get("r0", 1.16)
        d0 = p.get("d0", 2.0)
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.Ap and args.Zp and args.At and args.Zt and args.Elab:
        Ap, Zp, At, Zt = args.Ap, args.Zp, args.At, args.Zt
        Elab = args.Elab
        kdiss = args.kdiss
        r0 = 1.16
        d0 = 2.0
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_dic_analysis(Ap, Zp, At, Zt, Elab, r0=r0, d0=d0, k_diss=kdiss)

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
