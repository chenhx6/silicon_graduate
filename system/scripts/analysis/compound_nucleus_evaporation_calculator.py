#!/usr/bin/env python3
"""
compound_nucleus_evaporation_calculator.py
==========================================
Statistical Fusion-Evaporation Cross Section & Particle Cascade Simulator
(Hauser-Feshbach / Weisskopf-Ewing / PACE Framework).

Physics & Formulation:
----------------------
1. Heavy-Ion Fusion Cross Section (Bass / Hill-Wheeler Model):
   - Center-of-mass energy: E_cm = E_lab * A_t / (A_p + A_t)
   - Reduced mass: mu = m_u * A_p * A_t / (A_p + A_t)
   - Coulomb / Bass interaction barrier:
     V_B = 1.44 * Z_p * Z_t / R_B - b_s * R_p * R_t / (R_p + R_t)
     where R_i = 1.12 * A_i^(1/3) - 0.94 * A_i^(-1/3)
   - Maximum fusion angular momentum:
     l_fus^2 = (2 * mu * R_B^2 / hbar^2) * max(E_cm - V_B, 0)
   - Fission limit (Cohen-Plasil-Swiatecki Rotating Liquid Drop):
     l_crit = min(l_fus, l_RLDM)
   - Fusion cross section:
     sigma_fus(E_cm) = (pi * hbar^2 / (2 * mu * E_cm)) * l_crit^2

2. Compound Nucleus Excitation Energy:
   E_ex = E_cm + Q_fusion = E_cm + [M(Z_p, A_p) + M(Z_t, A_t) - M(Z_CN, A_CN)]

3. Statistical Decay Widths (Weisskopf-Ewing / Bohr-Wheeler):
   - Neutron width Gamma_n:
     Gamma_n ~ (2*s_n + 1) * (m_n * R^2 / (pi * hbar^2)) * T_n^2 * rho_res(E_ex - S_n) / rho_CN(E_ex)
   - Charged particle width (p, alpha) with Coulomb barrier penetration:
     V_C = 1.44 * z_part * Z_res / (1.2 * (A_res^(1/3) + A_part^(1/3)))
     Gamma_p ~ (2*s_p + 1) * (m_p * R^2 / (pi * hbar^2)) * T_p^2 * rho_res(E_ex - S_p - 0.7*V_C) / rho_CN(E_ex)
   - Fission width Gamma_f (Bohr-Wheeler formula):
     Gamma_f ~ (T_f / (2 * pi * rho_CN(E_ex))) * rho_sad(E_ex - B_f(l))
   - Statistical gamma width Gamma_gamma:
     Gamma_gamma ~ 1.5 - 3.0 eV (GDR E1 cascade)

4. Multi-step Evaporation Cascade:
   Simulates consecutive particle emission steps (xn, pxn, alphaxn)
   until residual excitation energy falls below particle emission thresholds.
   Computes individual residue production cross sections in mb.

References:
  - R. Bass, Nuclear Reactions with Heavy Ions, Springer (1980).
  - V. F. Weisskopf and D. H. Ewing, Phys. Rev. 57, 472 (1940).
  - S. Cohen, F. Plasil, and W. J. Swiatecki, Ann. Phys. 82, 557 (1974).
  - 林承键, 《重离子核反应》.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

HBAR_C_MEV_FM = 197.327
U_MEV = 931.494


def myers_swiatecki_binding_energy(Z: int, A: int) -> float:
    """Computes liquid drop binding energy in MeV."""
    if A <= 0 or Z <= 0:
        return 0.0
    a_v = 15.67
    a_s = 17.23
    a_c = 0.714
    a_sym = 23.28

    vol = a_v * A
    surf = a_s * (A ** (2.0 / 3.0))
    coul = a_c * Z * (Z - 1.0) / (A ** (1.0 / 3.0))
    sym = a_sym * ((A - 2.0 * Z) ** 2) / A

    return vol - surf - coul - sym


def nuclear_mass(Z: int, A: int) -> float:
    """Rest mass in MeV: M = Z*m_p + N*m_n - B."""
    m_p = 938.272
    m_n = 939.565
    B = myers_swiatecki_binding_energy(Z, A)
    return Z * m_p + (A - Z) * m_n - B


def calculate_fusion_barrier(Z_p: int, A_p: int, Z_t: int, A_t: int) -> Dict[str, float]:
    """
    Computes Bass interaction barrier V_B (in MeV) and barrier radius R_B (in fm).
    """
    r_p = 1.12 * (A_p ** (1.0 / 3.0)) - 0.94 * (A_p ** (-1.0 / 3.0))
    r_t = 1.12 * (A_t ** (1.0 / 3.0)) - 0.94 * (A_t ** (-1.0 / 3.0))

    R_12 = r_p * r_t / (r_p + r_t)
    R_B = r_p + r_t + 2.7

    # Coulomb term at barrier
    coul_B = 1.44 * Z_p * Z_t / R_B
    # Nuclear proximity attraction
    nuc_B = 0.03 * R_12
    V_B = coul_B - nuc_B

    return {
        "V_B_MeV": round(max(V_B, 5.0), 2),
        "R_B_fm": round(R_B, 2),
        "R_12_fm": round(R_12, 2)
    }


def calculate_fusion_cross_section(
    Z_p: int,
    A_p: int,
    Z_t: int,
    A_t: int,
    E_lab_MeV: float
) -> Dict[str, Any]:
    """
    Computes center-of-mass energy, excitation energy, critical angular momentum,
    and total fusion cross section sigma_fus (in mb).
    """
    Z_cn = Z_p + Z_t
    A_cn = A_p + A_t

    E_cm = E_lab_MeV * float(A_t) / float(A_p + A_t)
    mu_amu = (A_p * A_t) / float(A_p + A_t)
    mu_MeV = mu_amu * U_MEV

    barr = calculate_fusion_barrier(Z_p, A_p, Z_t, A_t)
    V_B = barr["V_B_MeV"]
    R_B = barr["R_B_fm"]

    # Masses & Q-value
    M_p = nuclear_mass(Z_p, A_p)
    M_t = nuclear_mass(Z_t, A_t)
    M_cn = nuclear_mass(Z_cn, A_cn)
    Q_fus = M_p + M_t - M_cn
    E_ex = E_cm + Q_fus

    # Angular momentum: l_fus^2 = (2 * mu * R_B^2 / hbar^2) * (E_cm - V_B)
    hbar_factor = (HBAR_C_MEV_FM ** 2)

    if E_cm > V_B:
        l_fus_sq = (2.0 * mu_MeV * (R_B ** 2) / hbar_factor) * (E_cm - V_B)
        l_fus = math.sqrt(max(l_fus_sq, 0.0))
    else:
        # Sub-barrier tunneling approximation
        T_tunnel = math.exp(-2.0 * math.pi * (V_B - E_cm) / 2.5) if (V_B - E_cm) < 10.0 else 0.0
        l_fus = 2.0 * T_tunnel
        l_fus_sq = l_fus ** 2

    # RLDM fission limit for angular momentum: l_f ~ 0.8 * A_cn^(2/3) * (1 - x_fiss)
    fissility = (Z_cn ** 2) / (50.88 * A_cn * (1.0 - 1.78 * ((A_cn - 2.0 * Z_cn) / A_cn) ** 2))
    l_RLDM = max(80.0 * (1.0 - fissility), 10.0)

    l_crit = min(l_fus, l_RLDM)

    # Cross section in mb: sigma = pi * (hbar / p)^2 * l_crit^2
    # lambda_bar^2 = hbar^2 / (2 * mu * E_cm) in fm^2
    if E_cm > 0.5:
        lam_sq_fm2 = hbar_factor / (2.0 * mu_MeV * E_cm)
        # 1 fm^2 = 10 mb
        sigma_fus_mb = math.pi * lam_sq_fm2 * (l_crit ** 2) * 10.0
    else:
        sigma_fus_mb = 0.0

    return {
        "projectile": f"Z={Z_p}, A={A_p}",
        "target": f"Z={Z_t}, A={A_t}",
        "compound_nucleus": f"Z={Z_cn}, A={A_cn}",
        "E_lab_MeV": E_lab_MeV,
        "E_cm_MeV": round(E_cm, 2),
        "barrier_V_B_MeV": V_B,
        "barrier_R_B_fm": R_B,
        "Q_fusion_MeV": round(Q_fus, 2),
        "compound_excitation_E_ex_MeV": round(E_ex, 2),
        "l_fus_hbar": round(l_fus, 1),
        "l_RLDM_limit_hbar": round(l_RLDM, 1),
        "l_crit_hbar": round(l_crit, 1),
        "sigma_fusion_mb": round(sigma_fus_mb, 1)
    }


def estimate_partial_widths(Z_res: int, A_res: int, E_ex: float) -> Dict[str, float]:
    """
    Estimates relative decay widths for neutron (n), proton (p), alpha (a),
    and fission (f) from an intermediate compound state.
    """
    if E_ex <= 1.0:
        return {"Gamma_n": 0.0, "Gamma_p": 0.0, "Gamma_a": 0.0, "Gamma_f": 0.0, "Gamma_tot": 1e-6}

    # Separation energies (approximate from liquid drop)
    S_n = 8.0 - 0.015 * (A_res - 2.0 * Z_res)
    S_p = 6.0 + 0.03 * Z_res
    S_a = 5.0 + 0.02 * Z_res

    # Coulomb barriers
    R_coul = 1.25 * (A_res ** (1.0 / 3.0))
    V_Cp = 1.44 * (Z_res - 1) / (R_coul + 1.2)
    V_Ca = 1.44 * 2.0 * (Z_res - 2) / (R_coul + 2.0)

    # Effective level density parameter a ~ A / 8.5
    a_param = A_res / 8.5

    # Available excitation in daughters
    U_n = max(E_ex - S_n, 0.0)
    U_p = max(E_ex - S_p - 0.7 * V_Cp, 0.0)
    U_a = max(E_ex - S_a - 0.7 * V_Ca, 0.0)

    # Relative densities ~ exp(2*sqrt(a*U))
    rho_n = math.exp(2.0 * math.sqrt(a_param * U_n)) if U_n > 0 else 0.0
    rho_p = math.exp(2.0 * math.sqrt(a_param * U_p)) if U_p > 0 else 0.0
    rho_a = 2.0 * math.exp(2.0 * math.sqrt(a_param * U_a)) if U_a > 0 else 0.0

    # Fission barrier B_f ~ 40 - 0.7 * (Z^2/A)
    fissility = (Z_res ** 2) / float(A_res)
    B_f = max(40.0 - 0.75 * fissility, 2.0)
    U_f = max(E_ex - B_f, 0.0)
    rho_f = 0.5 * math.exp(2.0 * math.sqrt(a_param * U_f)) if U_f > 0 else 0.0

    tot = rho_n + rho_p + rho_a + rho_f + 1e-12

    return {
        "Gamma_n": rho_n / tot,
        "Gamma_p": rho_p / tot,
        "Gamma_a": rho_a / tot,
        "Gamma_f": rho_f / tot,
        "U_n_MeV": round(U_n, 2)
    }


def simulate_statistical_evaporation_cascade(
    Z_cn: int,
    A_cn: int,
    E_ex: float,
    sigma_fus_mb: float
) -> List[Dict[str, Any]]:
    """
    Simulates consecutive particle emission steps and calculates residue cross sections.
    Follows main channels: 1n, 2n, 3n, 4n, 5n, 6n, p, pxn, axn.
    """
    residues = {}

    # Queue of states: (Z, A, E_ex, prob, channel_name)
    queue = [(Z_cn, A_cn, E_ex, 1.0, "")]

    step_count = 0
    while queue and step_count < 1000:
        step_count += 1
        Z_curr, A_curr, E_curr, prob, path = queue.pop(0)

        if prob < 1e-4 or E_curr < 6.0:
            # Reached discrete regime (gamma cascade to ground state residue)
            ch_name = path if path != "" else "CN"
            residues[ch_name] = residues.get(ch_name, 0.0) + prob
            continue

        widths = estimate_partial_widths(Z_curr, A_curr, E_curr)

        # Mean kinetic energy of evaporated particle ~ 2 * T ~ 2 * sqrt(E/a)
        temp = math.sqrt(max(E_curr / (A_curr / 8.5), 0.1))

        # 1. Neutron emission (n)
        if widths["Gamma_n"] > 0.005:
            dE_n = 8.0 + 2.0 * temp
            p_n = prob * widths["Gamma_n"]
            queue.append((Z_curr, A_curr - 1, max(E_curr - dE_n, 0.0), p_n, path + "n"))

        # 2. Proton emission (p)
        if widths["Gamma_p"] > 0.005:
            dE_p = 6.0 + 0.03 * Z_curr + 2.0 * temp
            p_p = prob * widths["Gamma_p"]
            queue.append((Z_curr - 1, A_curr - 1, max(E_curr - dE_p, 0.0), p_p, path + "p"))

        # 3. Alpha emission (a)
        if widths["Gamma_a"] > 0.005:
            dE_a = 5.0 + 0.05 * Z_curr + 2.0 * temp
            p_a = prob * widths["Gamma_a"]
            queue.append((Z_curr - 2, A_curr - 4, max(E_curr - dE_a, 0.0), p_a, path + "a"))

        # 4. Fission
        if widths["Gamma_f"] > 0.005:
            p_f = prob * widths["Gamma_f"]
            residues["fission"] = residues.get("fission", 0.0) + p_f

    # Normalize and sort residual channels
    sorted_res = []
    total_yield = sum(residues.values()) if residues else 1.0

    for ch, p_val in sorted(residues.items(), key=lambda x: -x[1]):
        norm_p = p_val / total_yield
        sigma_ch = norm_p * sigma_fus_mb
        sorted_res.append({
            "channel": ch,
            "branching_ratio": round(norm_p, 4),
            "cross_section_mb": round(sigma_ch, 1)
        })

    return sorted_res


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   HEAVY-ION FUSION-EVAPORATION RESIDUE CROSS SECTION CALCULATOR")
    lines.append("=" * 72)

    fus = summary["fusion_kinematics"]
    lines.append(f" REACTION: {fus['projectile']} + {fus['target']} -> {fus['compound_nucleus']}*")
    lines.append(f"   Beam Energy E_lab              : {fus['E_lab_MeV']} MeV")
    lines.append(f"   Center-of-Mass Energy E_cm     : {fus['E_cm_MeV']} MeV (Barrier V_B = {fus['barrier_V_B_MeV']} MeV)")
    lines.append(f"   Compound Excitation Energy E*  : {fus['compound_excitation_E_ex_MeV']} MeV (Q_fus = {fus['Q_fusion_MeV']} MeV)")
    lines.append(f"   Fusion Spin Limit l_crit       : {fus['l_crit_hbar']} hbar (l_fus = {fus['l_fus_hbar']}, l_RLDM = {fus['l_RLDM_limit_hbar']})")
    lines.append(f"   Total Fusion Cross Section     : {fus['sigma_fusion_mb']} mb")
    lines.append("-" * 72)
    lines.append(" EVAPORATION RESIDUE POPULATION CHANNELS:")
    lines.append(f"   {'Channel':<15} {'Branching Ratio':<20} {'Cross Section (mb)':<20}")
    lines.append("   " + "-" * 55)
    for r in summary["residues"][:10]:
        lines.append(f"   {r['channel']:<15} {r['branching_ratio']:<20.4f} {r['cross_section_mb']:<20.1f}")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Essential for planning in-beam gamma-ray spectroscopy experiments.")
    lines.append("   - Predicts peak beam energy for xn channels (e.g. populating 4n vs 5n residues).")
    lines.append("   - Evaluates charged particle (p, alpha) competition and fission suppression.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Statistical Heavy-Ion Fusion-Evaporation Cross Section Calculator."
    )
    parser.add_argument("-Zp", type=int, required=True, help="Projectile atomic number Z_p")
    parser.add_argument("-Ap", type=int, required=True, help="Projectile mass number A_p")
    parser.add_argument("-Zt", type=int, required=True, help="Target atomic number Z_t")
    parser.add_argument("-At", type=int, required=True, help="Target mass number A_t")
    parser.add_argument("-E", "--elab", type=float, required=True, help="Beam energy E_lab in MeV")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    fus_res = calculate_fusion_cross_section(args.Zp, args.Ap, args.Zt, args.At, args.elab)
    Z_cn = args.Zp + args.Zt
    A_cn = args.Ap + args.At

    residues = simulate_statistical_evaporation_cascade(
        Z_cn, A_cn, fus_res["compound_excitation_E_ex_MeV"], fus_res["sigma_fusion_mb"]
    )

    summary = {
        "fusion_kinematics": fus_res,
        "residues": residues
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
