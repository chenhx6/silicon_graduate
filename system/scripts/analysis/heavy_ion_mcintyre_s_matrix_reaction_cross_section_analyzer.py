#!/usr/bin/env python3
"""
heavy_ion_mcintyre_s_matrix_reaction_cross_section_analyzer.py
==============================================================
Heavy-Ion Strong Absorption Model (SAM) McIntyre S-Matrix Parametrization,
Partial Wave Transmission & Total Reaction Cross Section Inversion Suite.

Physics Formulation:
--------------------
1. S-Matrix Partial Wave Decomposition in Heavy-Ion Scattering:
   Based on 林承键《重离子核反应》第 3 章 §3.2 (pp. 55–75), C. A. Bertulani "Introduction to Nuclear Reactions"
   Chapter 3 & 4, J. A. McIntyre et al. (Phys. Rev. 117, 1337, 1960), and Frahn & Venter (Ann. Phys. 24, 243, 1963):
   In low-to-medium energy heavy-ion elastic scattering (e.g. 16O + 208Pb at Elab = 130 MeV),
   strong nuclear absorption depletes flux from the elastic channel.
   The scattering S-matrix is parameterized as:
     S_l = eta_l * exp( 2 * i * delta_l )
   where eta_l in [0, 1] is the reflection coefficient (modulus) and delta_l is the total phase shift.

2. McIntyre Strong Absorption Parametrization:
   The smooth absorption cutoff is parameterized as a Woods-Saxon function in angular momentum space:
     eta_l = 1 / [ 1 + exp( (l_g - l) / Delta_l ) ]
   where:
     - l_g is the grazing angular momentum (where absorption is 50%: eta_{l_g} = 0.50);
     - Delta_l is the angular momentum diffuseness parameter.
   The partial wave transmission coefficient (absorption probability) is:
     T_l = 1 - |S_l|^2 = 1 - eta_l^2.

3. Cross Section Integrals:
   - Total reaction cross section:
       sigma_R = (pi / k^2) * sum_{l=0}^{l_max} (2*l + 1) * T_l
   - Total elastic scattering cross section:
       sigma_el = (pi / k^2) * sum_{l=0}^{l_max} (2*l + 1) * |1 - S_l|^2
   - Total cross section:
       sigma_tot = sigma_R + sigma_el.

4. Semiclassical Inversion of Strong Absorption Radius:
   From the grazing angular momentum l_g, the strong absorption radius R_int is inverted from:
     E_cm = (Z_p * Z_t * e^2) / R_int + [ hbar^2 * l_g * (l_g + 1) ] / [ 2 * mu * R_int^2 ]
   This yields the interaction radius parameter r_0 = R_int / (A_p^(1/3) + A_t^(1/3))
   and the spatial surface diffuseness d = Delta_l / k.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "16O_208Pb_129.5MeV": {
        "description": "16O + 208Pb strong absorption scattering at Elab = 129.5 MeV (Ball et al. 1975)",
        "Ap": 16,
        "Zp": 8,
        "At": 208,
        "Zt": 82,
        "Elab_MeV": 129.5,
        "l_grazing": 55.4,
        "Delta_l": 3.25,
        "delta_0_rad": 0.45,
        "l_max": 90
    },
    "12C_12C_120MeV": {
        "description": "12C + 12C high-energy elastic scattering at Elab = 120 MeV (Stokstad 1980)",
        "Ap": 12,
        "Zp": 6,
        "At": 12,
        "Zt": 6,
        "Elab_MeV": 120.0,
        "l_grazing": 24.8,
        "Delta_l": 2.10,
        "delta_0_rad": 0.30,
        "l_max": 50
    },
    "alpha_40Ca_104MeV": {
        "description": "alpha + 40Ca strong absorption & reaction cross section at Elab = 104 MeV",
        "Ap": 4,
        "Zp": 2,
        "At": 40,
        "Zt": 20,
        "Elab_MeV": 104.0,
        "l_grazing": 28.5,
        "Delta_l": 2.40,
        "delta_0_rad": 0.50,
        "l_max": 60
    }
}


def calculate_kinematics(Ap, Zp, At, Zt, Elab_MeV):
    """
    Calculates center-of-mass energy E_cm, reduced mass, wavenumber k, and Sommerfeld parameter.
    """
    A_tot = Ap + At
    E_cm = Elab_MeV * (At / A_tot)
    mu_u = (Ap * At) / A_tot
    m_u_MeV = 931.494
    hbar_c = 197.327

    mu_MeV = mu_u * m_u_MeV
    k_fm = math.sqrt(2.0 * mu_MeV * E_cm) / hbar_c
    v_rel_c = math.sqrt(2.0 * E_cm / mu_MeV)
    alpha_em = 1.0 / 137.036
    eta = (Zp * Zt * alpha_em) / max(1e-6, v_rel_c)

    return {
        "E_cm_MeV": float(E_cm),
        "mu_u": float(mu_u),
        "k_fm_minus1": float(k_fm),
        "v_rel_c": float(v_rel_c),
        "sommerfeld_eta": float(eta)
    }


def evaluate_mcintyre_s_matrix(l_vals, l_grazing, Delta_l, delta_0_rad=0.0):
    """
    Evaluates the McIntyre reflection coefficient eta_l and transmission T_l for each partial wave.
    """
    l_arr = np.array(l_vals, dtype=float)
    dl = max(1e-3, Delta_l)

    # Woods-Saxon in angular momentum space
    arg = (l_grazing - l_arr) / dl
    arg_clipped = np.clip(arg, -60.0, 60.0)
    eta_l = 1.0 / (1.0 + np.exp(arg_clipped))

    # Nuclear phase shift
    delta_nucl = delta_0_rad / (1.0 + np.exp(arg_clipped))

    # Transmission coefficient T_l = 1 - eta_l^2
    T_l = 1.0 - (eta_l**2)

    return l_arr, eta_l, delta_nucl, T_l


def calculate_reaction_cross_sections(kin, l_grazing, Delta_l, delta_0_rad=0.0, l_max=100):
    """
    Integrates partial waves to evaluate total reaction, elastic, and total cross sections.
    """
    k_fm = kin["k_fm_minus1"]
    l_vals = np.arange(0, l_max + 1)

    l_arr, eta_l, delta_nucl, T_l = evaluate_mcintyre_s_matrix(
        l_vals, l_grazing, Delta_l, delta_0_rad
    )

    # Conversion factor from fm^2 to millibarns (1 fm^2 = 10 mb)
    fm2_to_mb = 10.0
    prefactor_mb = (math.pi / (k_fm**2)) * fm2_to_mb

    weights = 2.0 * l_arr + 1.0

    # Reaction cross section: sigma_R = prefactor * sum (2l+1) * T_l
    sigma_R_mb = prefactor_mb * float(np.sum(weights * T_l))

    # Elastic scattering cross section: S_l = eta_l * exp(2i delta)
    # |1 - S_l|^2 = 1 + eta_l^2 - 2 * eta_l * cos(2 * delta_nucl)
    one_minus_S_sq = 1.0 + (eta_l**2) - 2.0 * eta_l * np.cos(2.0 * delta_nucl)
    sigma_el_mb = prefactor_mb * float(np.sum(weights * one_minus_S_sq))

    sigma_tot_mb = sigma_R_mb + sigma_el_mb

    return {
        "sigma_reaction_mb": float(sigma_R_mb),
        "sigma_elastic_mb": float(sigma_el_mb),
        "sigma_total_mb": float(sigma_tot_mb),
        "l_grazing_hbar": float(l_grazing),
        "Delta_l_hbar": float(Delta_l)
    }


def invert_strong_absorption_radius(Ap, Zp, At, Zt, kin, l_grazing, Delta_l):
    """
    Inverts the strong absorption interaction radius R_int and radius parameter r_0 from l_grazing.
    """
    E_cm = kin["E_cm_MeV"]
    k_fm = kin["k_fm_minus1"]
    mu_u = kin["mu_u"]
    hbar_c = 197.327
    e2_MeV_fm = 1.43996

    # Semiclassical root for R_int: E_cm = Zp*Zt*e^2/R + (hbar*l_g)^2 / (2*mu*R^2)
    # Rearranged: E_cm * R^2 - (Zp*Zt*e^2) * R - (hbar*l_g)^2 / (2*mu) = 0
    a_quad = E_cm
    b_quad = -(Zp * Zt * e2_MeV_fm)
    c_quad = -((hbar_c * l_grazing)**2) / (2.0 * mu_u * 931.494)

    discriminant = b_quad**2 - 4.0 * a_quad * c_quad
    if discriminant >= 0.0:
        R_int_fm = (-b_quad + math.sqrt(discriminant)) / (2.0 * a_quad)
    else:
        R_int_fm = 10.0

    A_sum_cbrt = (Ap**(1.0 / 3.0)) + (At**(1.0 / 3.0))
    r0_fm = R_int_fm / max(1e-3, A_sum_cbrt)
    diffuseness_d_fm = Delta_l / max(1e-3, k_fm)

    return {
        "strong_absorption_radius_R_int_fm": float(R_int_fm),
        "interaction_radius_parameter_r0_fm": float(r0_fm),
        "spatial_diffuseness_d_fm": float(diffuseness_d_fm)
    }


def run_mcintyre_analysis(Ap, Zp, At, Zt, Elab_MeV, l_grazing, Delta_l, delta_0_rad=0.0, l_max=100):
    """
    Complete execution pipeline for McIntyre S-matrix and reaction cross section analysis.
    """
    kin = calculate_kinematics(Ap, Zp, At, Zt, Elab_MeV)
    xs = calculate_reaction_cross_sections(kin, l_grazing, Delta_l, delta_0_rad, l_max)
    rad = invert_strong_absorption_radius(Ap, Zp, At, Zt, kin, l_grazing, Delta_l)

    return {
        "kinematics": kin,
        "cross_sections": xs,
        "semiclassical_radii": rad,
        "system": {
            "Ap": Ap, "Zp": Zp, "At": At, "Zt": Zt,
            "Elab_MeV": float(Elab_MeV)
        }
    }


def format_text_report(res, title="Heavy-Ion McIntyre S-Matrix Reaction Cross Section Analyzer"):
    sys_p = res["system"]
    kin = res["kinematics"]
    xs = res["cross_sections"]
    rad = res["semiclassical_radii"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"System: {sys_p['Ap']}Z({sys_p['Zp']}) + {sys_p['At']}Y({sys_p['Zt']}) at Elab = {sys_p['Elab_MeV']:.1f} MeV")
    lines.append("=" * 76)
    lines.append(f"  Center-of-Mass Energy E_cm      : {kin['E_cm_MeV']:.2f} MeV (Wavenumber k = {kin['k_fm_minus1']:.3f} fm^-1)")
    lines.append(f"  Sommerfeld Parameter eta        : {kin['sommerfeld_eta']:.3f} (Strong Coulomb dominance)")
    lines.append("-" * 76)
    lines.append("McIntyre Strong Absorption Model (SAM) Cross Sections:")
    lines.append(f"  Grazing Angular Momentum l_g    : {xs['l_grazing_hbar']:.1f} hbar (Diffuseness Delta_l = {xs['Delta_l_hbar']:.2f} hbar)")
    lines.append(f"  Total Reaction Cross Section    : sigma_R  = {xs['sigma_reaction_mb']:8.1f} mb ({xs['sigma_reaction_mb']/1000.0:.3f} barns)")
    lines.append(f"  Total Elastic Cross Section     : sigma_el = {xs['sigma_elastic_mb']:8.1f} mb")
    lines.append(f"  Total Scattering Cross Section  : sigma_tot= {xs['sigma_total_mb']:8.1f} mb")
    lines.append("-" * 76)
    lines.append("Semiclassical Interaction Geometry Inversion:")
    lines.append(f"  Strong Absorption Radius R_int  : {rad['strong_absorption_radius_R_int_fm']:.2f} fm")
    lines.append(f"  Nuclear Radius Parameter r_0    : {rad['interaction_radius_parameter_r0_fm']:.3f} fm  [R_int = r_0 * (A_p^1/3 + A_t^1/3)]")
    lines.append(f"  Spatial Surface Diffuseness d   : {rad['spatial_diffuseness_d_fm']:.3f} fm  [d = Delta_l / k]")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Heavy-Ion McIntyre S-Matrix & Reaction Cross Section Inverter."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--Ap", type=int, help="Projectile A")
    parser.add_argument("--Zp", type=int, help="Projectile Z")
    parser.add_argument("--At", type=int, help="Target A")
    parser.add_argument("--Zt", type=int, help="Target Z")
    parser.add_argument("--Elab", type=float, help="Beam energy in MeV")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        Ap, Zp, At, Zt = p["Ap"], p["Zp"], p["At"], p["Zt"]
        Elab = p["Elab_MeV"]
        l_g = p["l_grazing"]
        dl = p["Delta_l"]
        d0 = p.get("delta_0_rad", 0.40)
        lmax = p.get("l_max", 90)
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.Ap and args.Zp and args.At and args.Zt and args.Elab:
        Ap, Zp, At, Zt = args.Ap, args.Zp, args.At, args.Zt
        Elab = args.Elab
        l_g = 50.0
        dl = 3.0
        d0 = 0.40
        lmax = 90
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = run_mcintyre_analysis(
        Ap=Ap, Zp=Zp, At=At, Zt=Zt,
        Elab_MeV=Elab,
        l_grazing=l_g,
        Delta_l=dl,
        delta_0_rad=d0,
        l_max=lmax
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
