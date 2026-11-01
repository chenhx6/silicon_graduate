#!/usr/bin/env python3
"""
heavy_ion_fusion_evaporation_channel_calculator.py
=================================================
Heavy-Ion Fusion-Evaporation Cross Section, Optical Barrier Distribution &
Reaction Channel Design Suite for In-Beam Nuclear Spectroscopy (A ~ 130 Region).

Physics & Formulation:
----------------------
1. Entrance Channel Kinematics & Coulomb Barrier:
   - Center-of-mass energy: E_cm = E_lab * [ A_t / (A_p + A_t) ]
   - Reduced mass: mu = m_u * [ A_p * A_t / (A_p + A_t) ]
   - Bass / Christensen-Winther Coulomb Barrier:
       R_B = 1.07 * (A_p^(1/3) + A_t^(1/3)) + 2.72 fm
       V_B = [ 1.44 * Z_p * Z_t / R_B ] * [ 1 - 0.63 / R_B ] MeV
       Barrier curvature: hbar_omega_B ~ 3.5 - 4.5 MeV

2. Wong's Analytical Fusion Cross Section:
   sigma_fus(E_cm) = [ hbar_omega_B * R_B^2 / (2 * E_cm) ] *
                     ln[ 1 + exp( 2 * pi * (E_cm - V_B) / hbar_omega_B ) ]  (in fm^2 -> mb)

3. Angular Momentum & High-Spin Fission Survival:
   - Maximum orbital angular momentum:
       L_max = sqrt( 2 * mu * R_B^2 * max(0, E_cm - V_B) ) / hbar
   - Compound nucleus survival against fission:
       B_f(J) = B_f(0) - [ hbar^2 * J*(J+1) / (2 * J_eff) ]
     For A ~ 130, compound nucleus survives fission up to J_surv ~ 50 hbar.

4. Statistical Evaporation Cascade (Hauser-Feshbach / PACE Approximation):
   - Compound nucleus excitation energy: E_ex = E_cm + Q_fusion
   - Nuclear temperature: T = sqrt( E_ex / a ), where a = A_CN / 8.5 MeV^-1
   - Energy removed per evaporated neutron: Delta_E_n = S_n + 2 * T  (~ 10.5 - 12.0 MeV)
   - Gaussian statistical distribution of xn residue yields peaked at E_peak(xn) ~ x * Delta_E_n.

5. In-Beam Recoil Kinematics & Doppler Broadening:
   - Recoil velocity: beta = v/c = sqrt( 2 * E_lab / (931.5 * A_p) ) * [ A_p / A_CN ]
   - Doppler shift: Delta_E / E_0 = beta * cos(theta_det)
   - Doppler broadening: Delta_E_FWHM = E_0 * beta * sin(theta_det) * Delta_theta_det

References:
  - 林承键, 《重离子核反应》, 原子能出版社 (2023), 第2章、第6章与第7章.
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions (2004), Ch 11.
  - 卢希庭, 《原子核物理（修订版）》, 第9章 (重离子核反应).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_liquid_drop_mass(Z: int, A: int) -> float:
    """
    Bethe-Weizsacker semi-empirical mass formula for nuclear mass in MeV.
    """
    N = A - Z
    a_v = 15.67
    a_s = 17.23
    a_c = 0.714
    a_sym = 23.285

    # Pairing term
    if A % 2 != 0:
        delta = 0.0
    elif Z % 2 == 0:
        delta = 12.0 / math.sqrt(A)
    else:
        delta = -12.0 / math.sqrt(A)

    binding = (a_v * A - a_s * (A**(2.0/3.0)) -
               a_c * (Z * (Z - 1)) / (A**(1.0/3.0)) -
               a_sym * ((N - Z)**2) / A + delta)
    m_p = 938.272
    m_n = 939.565
    return Z * m_p + N * m_n - binding


def analyze_heavy_ion_fusion(
    Z_p: int, A_p: int,
    Z_t: int, A_t: int,
    E_lab_MeV: float,
    target_thickness_mg_cm2: float = 0.5,
    detector_angle_deg: float = 90.0,
    detector_dtheta_deg: float = 8.0,
    E_gamma_keV: float = 1000.0
) -> Dict[str, Any]:
    """
    Comprehensive calculation of heavy-ion fusion kinematics, cross sections,
    xn residue yields, and in-beam Doppler broadening.
    """
    # Compound nucleus
    Z_cn = Z_p + Z_t
    A_cn = A_p + A_t

    # Masses & Q-value
    m_p = calculate_liquid_drop_mass(Z_p, A_p)
    m_t = calculate_liquid_drop_mass(Z_t, A_t)
    m_cn = calculate_liquid_drop_mass(Z_cn, A_cn)
    Q_fus = m_p + m_t - m_cn

    # Kinematics
    m_u = 931.494
    E_cm = E_lab_MeV * (float(A_t) / (A_p + A_t))
    mu_amu = (float(A_p) * A_t) / (A_p + A_t)
    mu_MeV = mu_amu * m_u

    # Coulomb Barrier (Christensen-Winther / Bass)
    R_B = 1.07 * (A_p**(1.0/3.0) + A_t**(1.0/3.0)) + 2.72 # fm
    V_B = (1.439965 * Z_p * Z_t / R_B) * (1.0 - 0.63 / R_B) # MeV
    hbar_omega = 4.0 # MeV

    # Wong Fusion Cross Section
    # sigma = [ hbar_omega * R_B^2 / (2 * E_cm) ] * ln[ 1 + exp( 2*pi*(E_cm - V_B)/hbar_omega ) ]
    # 1 fm^2 = 10 mb
    x_arg = 2.0 * math.pi * (E_cm - V_B) / hbar_omega
    if x_arg > 50.0:
        ln_term = x_arg
    elif x_arg < -50.0:
        ln_term = math.exp(x_arg)
    else:
        ln_term = math.log(1.0 + math.exp(x_arg))

    sigma_fus_mb = (hbar_omega * (R_B**2) / (2.0 * max(1e-3, E_cm))) * ln_term * 10.0

    # Maximum & Critical Angular Momentum
    # L_max = R_B * sqrt(2 * mu * max(0, E_cm - V_B)) / hbar
    # hbar * c = 197.327 MeV*fm
    hbar_c = 197.327
    if E_cm > V_B:
        L_max = (R_B / hbar_c) * math.sqrt(2.0 * mu_MeV * (E_cm - V_B))
    else:
        L_max = 0.0

    # Rotating liquid drop fission limit for A ~ 130
    L_fission_limit = 52.0 # hbar
    L_fus_eff = min(L_max, L_fission_limit)

    # Compound Nucleus Excitation Energy
    E_ex = E_cm + Q_fus

    # Statistical Evaporation Channels (xn)
    # a = A / 8.5 MeV^-1
    a_param = A_cn / 8.5
    T_nucl = math.sqrt(max(0.1, E_ex) / a_param)
    delta_E_per_neutron = 8.0 + 2.0 * T_nucl # ~ 8 MeV binding + 2T kinetic

    xn_channels = {}
    total_xn_weight = 0.0
    for x in [3, 4, 5, 6]:
        E_opt = x * delta_E_per_neutron + 5.0 # plus yrast offset
        sigma_E = 6.0 # width of evaporation window
        weight = math.exp(-0.5 * ((E_ex - E_opt) / sigma_E)**2)
        res_A = A_cn - x
        res_Z = Z_cn
        xn_channels[f"{x}n"] = {
            "residue": f"Z={res_Z}, A={res_A}",
            "E_opt_MeV": E_opt,
            "relative_weight": weight
        }
        total_xn_weight += weight

    # Normalize channel cross sections
    f_fiss_survival = min(1.0, max(0.05, 1.0 - (L_max / 70.0)**2)) if L_max > 0 else 1.0
    sigma_evap_total = sigma_fus_mb * f_fiss_survival
    for x_key in xn_channels:
        prob = (xn_channels[x_key]["relative_weight"] / max(1e-6, total_xn_weight))
        xn_channels[x_key]["cross_section_mb"] = sigma_evap_total * prob
        xn_channels[x_key]["branching_ratio_pct"] = prob * 100.0

    # Recoil Kinematics & In-Beam Doppler Broadening
    # beta = sqrt(2 * E_lab / (m_u * A_p)) * (A_p / A_cn)
    v_p_over_c = math.sqrt(2.0 * E_lab_MeV / (m_u * A_p))
    beta_recoil = v_p_over_c * (float(A_p) / A_cn)

    theta_rad = math.radians(detector_angle_deg)
    dtheta_rad = math.radians(detector_dtheta_deg)

    doppler_shift_keV = E_gamma_keV * beta_recoil * math.cos(theta_rad)
    doppler_broadening_fwhm_keV = E_gamma_keV * beta_recoil * math.sin(theta_rad) * dtheta_rad

    return {
        "entrance_channel": {
            "projectile": f"Z={Z_p}, A={A_p}",
            "target": f"Z={Z_t}, A={A_t}",
            "compound_nucleus": f"Z={Z_cn}, A={A_cn}",
            "E_lab_MeV": E_lab_MeV,
            "E_cm_MeV": E_cm,
            "Q_fusion_MeV": Q_fus,
            "E_excitation_MeV": E_ex
        },
        "barrier_and_fusion": {
            "R_barrier_fm": R_B,
            "V_barrier_MeV": V_B,
            "sigma_fusion_mb": sigma_fus_mb,
            "L_max_hbar": L_max,
            "L_fission_limit_hbar": L_fission_limit,
            "fission_survival_fraction": f_fiss_survival,
            "sigma_evaporation_total_mb": sigma_evap_total
        },
        "evaporation_channels": xn_channels,
        "in_beam_spectroscopy": {
            "recoil_velocity_beta": beta_recoil,
            "recoil_velocity_pct_c": beta_recoil * 100.0,
            "detector_angle_deg": detector_angle_deg,
            "detector_opening_dtheta_deg": detector_dtheta_deg,
            "gamma_energy_keV": E_gamma_keV,
            "doppler_shift_keV": doppler_shift_keV,
            "doppler_broadening_fwhm_keV": doppler_broadening_fwhm_keV,
            "target_thickness_mg_cm2": target_thickness_mg_cm2
        }
    }


def format_text_report(res: Dict[str, Any]) -> str:
    ent = res["entrance_channel"]
    bar = res["barrier_and_fusion"]
    evap = res["evaporation_channels"]
    spec = res["in_beam_spectroscopy"]

    lines = [
        "=" * 74,
        "   HEAVY-ION FUSION-EVAPORATION REACTION & IN-BEAM SPECTROSCOPY SUITE",
        "   Based on Lin Chengjian (Heavy-Ion Reactions) & Bertulani",
        "=" * 74,
        f" REACTION ENTRANCE CHANNEL & KINEMATICS:",
        f"   Reaction System      : {ent['projectile']} + {ent['target']} -> {ent['compound_nucleus']}*",
        f"   Lab Beam Energy      : {ent['E_lab_MeV']:.1f} MeV (E_cm = {ent['E_cm_MeV']:.2f} MeV)",
        f"   Fusion Q-Value       : {ent['Q_fusion_MeV']:+.2f} MeV",
        f"   CN Excitation Energy : E* = {ent['E_excitation_MeV']:.2f} MeV",
        "-" * 74,
        f" COULOMB BARRIER & FUSION CROSS SECTION (Wong Model):",
        f"   Barrier Height V_B   : {bar['V_barrier_MeV']:.2f} MeV (Radius R_B = {bar['R_barrier_fm']:.2f} fm)",
        f"   Energy above Barrier : Delta_E = {ent['E_cm_MeV'] - bar['V_barrier_MeV']:+.2f} MeV",
        f"   Total Fusion Cross S.: sigma_fus = {bar['sigma_fusion_mb']:.1f} mb",
        f"   Angular Momentum     : L_max = {bar['L_max_hbar']:.1f} hbar (Fission cutoff: {bar['L_fission_limit_hbar']:.0f} hbar)",
        f"   Fission Survival     : {bar['fission_survival_fraction']*100:.1f}% (Residue Cross Sec: {bar['sigma_evaporation_total_mb']:.1f} mb)",
        "-" * 74,
        f" STATISTICAL EVAPORATION CHANNELS (xn Residues):"
    ]

    for chan, data in evap.items():
        lines.append(
            f"   Channel {chan:<4} ({data['residue']}) : sigma = {data['cross_section_mb']:>6.1f} mb "
            f"({data['branching_ratio_pct']:>5.1f}%) [Peak E* ~ {data['E_opt_MeV']:.1f} MeV]"
        )

    lines.extend([
        "-" * 74,
        f" IN-BEAM GAMMA SPECTROSCOPY & DOPPLER BROADENING (E_gamma = {spec['gamma_energy_keV']:.0f} keV):",
        f"   Recoil Velocity beta : {spec['recoil_velocity_pct_c']:.2f}% c (v/c = {spec['recoil_velocity_beta']:.4f})",
        f"   Detector Angle theta : {spec['detector_angle_deg']:.1f} deg (Opening Delta_theta = {spec['detector_opening_dtheta_deg']:.1f} deg)",
        f"   Doppler Shift        : Delta_E = {spec['doppler_shift_keV']:+.2f} keV",
        f"   Doppler Broadening   : FWHM = {spec['doppler_broadening_fwhm_keV']:.2f} keV (Geometric kinematic limit)",
        f"   Target Specification : Thin self-supporting foil {spec['target_thickness_mg_cm2']:.2f} mg/cm^2",
        "=" * 74
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Heavy-Ion Fusion-Evaporation Cross Section & Spectroscopy Designer"
    )
    parser.add_argument("--Zp", type=int, default=16, help="Projectile charge (default: 16, 36S)")
    parser.add_argument("--Ap", type=int, default=36, help="Projectile mass (default: 36)")
    parser.add_argument("--Zt", type=int, default=42, help="Target charge (default: 42, 100Mo)")
    parser.add_argument("--At", type=int, default=100, help="Target mass (default: 100)")
    parser.add_argument("--Elab", type=float, default=155.0, help="Lab beam energy in MeV (default: 155.0 MeV)")
    parser.add_argument("--target-thick", type=float, default=0.5, help="Target thickness in mg/cm^2")
    parser.add_argument("--th-det", type=float, default=90.0, help="Detector angle in degrees")
    parser.add_argument("--dth-det", type=float, default=8.0, help="Detector opening angle in degrees")
    parser.add_argument("--egamma", type=float, default=1000.0, help="Gamma energy in keV")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    res = analyze_heavy_ion_fusion(
        Z_p=args.Zp, A_p=args.Ap,
        Z_t=args.Zt, A_t=args.At,
        E_lab_MeV=args.Elab,
        target_thickness_mg_cm2=args.target_thick,
        detector_angle_deg=args.th_det,
        detector_dtheta_deg=args.dth_det,
        E_gamma_keV=args.egamma
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res))


if __name__ == "__main__":
    main()
