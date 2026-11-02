#!/usr/bin/env python3
"""
optical_model_potential_reaction_cross_section_calculator.py
============================================================
Nuclear Optical Model Potential (OMP), S-Matrix Transmission Functions T_l / T(b) &
Total Reaction Cross Section sigma_R Calculator.

Physics & Formulation:
----------------------
1. The Complex Optical Model Potential (OMP):
   To describe simultaneously elastic scattering and flux absorption into non-elastic channels,
   the nuclear potential is complex (Feshbach 1958; Bertulani Ch. 3; Lu Xiting Ch. 9 §9.3):
     U(r) = - V_0 * f_v(r) - i * W_0 * f_w(r) - i * 4 * a_s * W_s * [ - d/dr f_s(r) ] + V_Coul(r)
   where the Woods-Saxon form factor is:
     f_i(r) = 1.0 / [ 1.0 + exp( (r - R_i) / a_i ) ]
     R_i = r_0i * A_target^(1/3)
   - Real potential V_0: Refracts the incoming wave (nuclear potential well ~ 40 - 55 MeV).
   - Imaginary volume potential W_0: Models uniform absorption into compound nucleus states.
   - Imaginary surface derivative W_s: Models absorption at the nuclear surface into direct channels.

2. Semiclassical Eikonal / WKB S-Matrix Formulation:
   Along a straight-line trajectory with impact parameter b:
     r(z) = sqrt(b^2 + z^2)
   The eikonal phase shift is:
     chi(b) = - [ 1 / (hbar * v) ] * integral_{-infinity}^{infinity} U(r(z)) dz
   The imaginary part governs flux absorption:
     Im[chi(b)] = [ 1 / (hbar * v) ] * integral_{-infinity}^{infinity} W(r(z)) dz
   The S-matrix transmission probability (absorption coefficient):
     T(b) = 1.0 - |eta(b)|^2 = 1.0 - exp( - 2.0 * Im[chi(b)] )

3. Total Reaction Cross Section:
   Integrating over impact parameters b (or summing over partial waves l = k * b):
     sigma_R = 2 * pi * integral_0^infinity b * T(b) db  (in mb: 1 fm^2 = 10 mb)
   In the black-disc limit (T(b) = 1 for b <= R, 0 for b > R):
     sigma_R -> pi * R^2.

4. Elastic and Total Cross Sections via Optical Theorem:
   The total cross section relates to forward scattering amplitude:
     sigma_total = sigma_elastic + sigma_reaction = [ 4 * pi / k ] * Im[ f(0) ]

References:
  - C. A. Bertulani & P. Danielewicz, *Introduction to Nuclear Reactions*, CRC Press (2021), Ch. 3.
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第9章 §9.3 (光学模型, 印刷 pp. 248–254).
  - 林承键, 《重离子核反应》, 科学出版社 (2017), 第2章.
  - H. Feshbach, C. E. Porter, and V. F. Weisskopf, Phys. Rev. 96, 448 (1954).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def _woods_saxon(r: float, R: float, a: float) -> float:
    """Computes Woods-Saxon form factor f(r, R, a)."""
    arg = (r - R) / a
    if arg > 60.0:
        return 0.0
    if arg < -60.0:
        return 1.0
    return 1.0 / (1.0 + math.exp(arg))


def calculate_optical_model_reaction_cross_section(
    Z_p: int,
    A_p: int,
    Z_t: int,
    A_t: int,
    E_lab_MeV: float,
    V0_MeV: float = 45.0,
    W0_volume_MeV: float = 10.0,
    Ws_surface_MeV: float = 0.0,
    r0_fm: float = 1.25,
    a0_fm: float = 0.65,
    b_max_fm: float = 14.0,
    db_fm: float = 0.05
) -> Dict[str, Any]:
    """
    Computes S-matrix transmission T(b) and total reaction cross section sigma_R
    using eikonal WKB optical model integration.
    """
    if A_p <= 0 or A_t <= 0:
        raise ValueError("Mass numbers must be strictly positive.")
    if E_lab_MeV <= 0.0:
        raise ValueError("Beam energy E_lab must be positive.")

    m_u_MeV = 931.494
    hbar_c_MeV_fm = 197.327

    # Center-of-mass energy and projectile velocity
    A_tot = float(A_p + A_t)
    E_cm_MeV = E_lab_MeV * float(A_t) / A_tot
    m_proj_MeV = float(A_p) * m_u_MeV
    v_over_c = math.sqrt(2.0 * E_lab_MeV / m_proj_MeV)
    v_hbar_inv_fm_MeV = 1.0 / (hbar_c_MeV_fm * v_over_c)

    # Nuclear radii
    R_t_fm = r0_fm * (float(A_t) ** (1.0 / 3.0))
    R_p_fm = r0_fm * (float(A_p) ** (1.0 / 3.0))
    R_int_fm = R_t_fm + R_p_fm

    # Function to calculate imaginary potential W(r)
    def calc_W(r_val):
        w_vol = W0_volume_MeV * _woods_saxon(r_val, R_t_fm, a0_fm)
        if Ws_surface_MeV > 0.0:
            # Surface derivative: - 4 * a * d/dr [ 1 / (1 + e^x) ] = 4 * e^x / (1 + e^x)^2
            arg = (r_val - R_t_fm) / a0_fm
            if abs(arg) < 30.0:
                e_x = math.exp(arg)
                w_surf = 4.0 * Ws_surface_MeV * (e_x / ((1.0 + e_x) ** 2))
            else:
                w_surf = 0.0
        else:
            w_surf = 0.0
        return w_vol + w_surf

    # Numerical eikonal integration along straight line r = sqrt(b^2 + z^2)
    dz = 0.05
    z_max = 25.0
    steps_z = int(z_max / dz)

    b_profile = []
    sigma_R_fm2 = 0.0
    steps_b = int(b_max_fm / db_fm)

    for i in range(steps_b):
        b = (i + 0.5) * db_fm

        # integrate W(r) dz from z = 0 to z_max (factor of 2 for symmetry)
        integ_W = 0.0
        for j in range(steps_z):
            z = (j + 0.5) * dz
            r = math.sqrt(b ** 2 + z ** 2)
            integ_W += calc_W(r) * dz

        # Im[chi(b)] = [ 2 / (hbar * v) ] * integral_0^inf W dz
        im_chi = 2.0 * integ_W * v_hbar_inv_fm_MeV

        # Transmission probability T(b) = 1 - exp(-2 * Im[chi])
        arg_exp = 2.0 * im_chi
        t_b = (1.0 - math.exp(-arg_exp)) if arg_exp < 50.0 else 1.0

        # Annular cross section element: dsigma = 2 * pi * b * T(b) * db
        sigma_R_fm2 += 2.0 * math.pi * b * t_b * db_fm

        if i % 8 == 0:
            b_profile.append({
                "impact_parameter_b_fm": round(b, 2),
                "optical_thickness_2ImChi": round(arg_exp, 3),
                "transmission_T_b": round(t_b, 4)
            })

    sigma_R_mb = sigma_R_fm2 * 10.0 # 1 fm^2 = 10 mb

    # Geometric scale: pi * (R_t + a)^2 in mb
    geom_scale_mb = 10.0 * math.pi * ((R_t_fm + a0_fm) ** 2)

    return {
        "reaction": f"{A_p}X({Z_p}) + {A_t}Y({Z_t})",
        "E_lab_MeV": E_lab_MeV,
        "E_cm_MeV": round(E_cm_MeV, 2),
        "projectile_velocity_v_over_c": round(v_over_c, 4),
        "target_radius_R_fm": round(R_t_fm, 2),
        "diffuseness_a_fm": a0_fm,
        "optical_potential_V0_MeV": V0_MeV,
        "optical_potential_W0_MeV": W0_volume_MeV,
        "optical_potential_Ws_MeV": Ws_surface_MeV,
        "total_reaction_cross_section_sigma_R_mb": round(sigma_R_mb, 1),
        "geometric_scale_mb": round(geom_scale_mb, 1),
        "nuclear_opacity_ratio": round(sigma_R_mb / max(geom_scale_mb, 1.0), 3),
        "transmission_profile": b_profile
    }


def format_text_report(omp_res: Dict[str, Any]) -> str:
    lines = [
        "=" * 76,
        "   NUCLEAR OPTICAL MODEL POTENTIAL (OMP) & REACTION CROSS SECTION SUITE",
        "   Based on Bertulani Ch. 3 (2021), Lu Xiting §9.3 & Lin Chengjian Ch. 2",
        "=" * 76,
        f" REACTION SYSTEM: {omp_res['reaction']} at E_lab = {omp_res['E_lab_MeV']:.1f} MeV",
        f"   Center-of-Mass Energy E_cm  : {omp_res['E_cm_MeV']:.2f} MeV (v/c = {omp_res['projectile_velocity_v_over_c']:.4f})",
        f"   Target Radius R & Diffuseness: R = {omp_res['target_radius_R_fm']:.2f} fm, a = {omp_res['diffuseness_a_fm']:.2f} fm",
        f"   Optical Potential Well      : Real V_0 = {omp_res['optical_potential_V0_MeV']:.1f} MeV, Imag Volume W_0 = {omp_res['optical_potential_W0_MeV']:.1f} MeV, Surface W_s = {omp_res['optical_potential_Ws_MeV']:.1f} MeV",
        "-" * 76,
        " REACTION CROSS SECTION & NUCLEAR OPACITY:",
        f"   Total Reaction Cross Section: sigma_R = {omp_res['total_reaction_cross_section_sigma_R_mb']:.1f} mb",
        f"   Geometric Scale pi*(R+a)^2  : {omp_res['geometric_scale_mb']:.1f} mb",
        f"   Nuclear Opacity Ratio       : {omp_res['nuclear_opacity_ratio']:.3f} (Black disc limit = 1.0)",
        "-" * 76,
        " IMPACT PARAMETER S-MATRIX TRANSMISSION PROFILE T(b):",
        "   Impact b (fm)      Optical Depth 2*Im(chi)      Transmission T(b)",
    ]

    for pt in omp_res["transmission_profile"]:
        lines.append(f"     {pt['impact_parameter_b_fm']:6.2f} fm             {pt['optical_thickness_2ImChi']:10.3f}                {pt['transmission_T_b']:6.4f}")

    lines.extend([
        "-" * 76,
        " Methodological Guidelines for Optical Model Analysis:",
        "   - W_0 (volume) accounts for compound nucleus absorption in central collisions (b < R).",
        "   - W_s (surface) accounts for direct transfer and inelastic scattering in peripheral collisions.",
        "   - T(b) -> 1 marks strong absorption (black core); T(b) -> 0 outside nuclear surface.",
        "=" * 76
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Nuclear Optical Model Potential (OMP) Reaction Cross Section Calculator"
    )
    parser.add_argument("--Zp", type=int, default=1, help="Projectile Z (default: 1 for proton)")
    parser.add_argument("--Ap", type=int, default=1, help="Projectile A (default: 1)")
    parser.add_argument("--Zt", type=int, default=28, help="Target Z (default: 28 for Ni)")
    parser.add_argument("--At", type=int, default=58, help="Target A (default: 58)")
    parser.add_argument("--Elab", type=float, default=40.0, help="Beam energy E_lab in MeV (default: 40.0)")
    parser.add_argument("--V0", type=float, default=45.0, help="Real potential well V0 in MeV (default: 45.0)")
    parser.add_argument("--W0", type=float, default=10.0, help="Imaginary volume potential W0 in MeV (default: 10.0)")
    parser.add_argument("--Ws", type=float, default=0.0, help="Imaginary surface potential Ws in MeV (default: 0.0)")
    parser.add_argument("--preset", type=str, default="40MeV_p_58Ni",
                        choices=["40MeV_p_58Ni", "100MeV_alpha_58Ni", "16O_208Pb_fusion_om"],
                        help="Benchmark preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    zp, ap = args.Zp, args.Ap
    zt, at = args.Zt, args.At
    elab = args.Elab
    v0, w0, ws = args.V0, args.W0, args.Ws

    if args.preset == "40MeV_p_58Ni":
        zp, ap, zt, at, elab = 1, 1, 28, 58, 40.0
        v0, w0, ws = 45.0, 10.0, 3.0
    elif args.preset == "100MeV_alpha_58Ni":
        zp, ap, zt, at, elab = 2, 4, 28, 58, 100.0
        v0, w0, ws = 100.0, 20.0, 5.0
    elif args.preset == "16O_208Pb_fusion_om":
        zp, ap, zt, at, elab = 8, 16, 82, 208, 90.0
        v0, w0, ws = 50.0, 15.0, 0.0

    res = calculate_optical_model_reaction_cross_section(
        zp, ap, zt, at, elab, V0_MeV=v0, W0_volume_MeV=w0, Ws_surface_MeV=ws
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res))


if __name__ == "__main__":
    main()
