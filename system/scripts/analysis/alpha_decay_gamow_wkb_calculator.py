#!/usr/bin/env python3
"""
alpha_decay_gamow_wkb_calculator.py
===================================
Alpha Decay Gamow Quantum Tunneling WKB Penetration, Centrifugal Barrier Hindrance &
Viola-Seaborg Systematics Suite.

Physics & Formulation:
----------------------
1. Gamow Quantum Tunneling Penetration Probability:
   For alpha particle (Z=2, m_alpha = 3727.38 MeV) decaying from parent (Z, A) to daughter (Z_d = Z-2, A_d = A-4):
     mu = [ m_alpha * (A_d * m_u) ] / [ m_alpha + A_d * m_u ]   (Reduced mass)
     Total effective barrier:
       V(r) = [ 2 * Z_d * e^2 / r ] + [ hbar^2 * L*(L + 1) / (2 * mu * r^2) ]
     Classical outer turning point R_c(L): V(R_c) = Q_alpha
     Nuclear touching radius R_0:
       R_0 = r_0 * [ (A - 4)^(1/3) + 4^(1/3) ]  (r_0 ~ 1.20 - 1.25 fm)

2. WKB Action Integral (Gamow Factor 2G):
   P(L) = exp( -2 * G(L) )
   where G(L) = integral_{R_0}^{R_c(L)} sqrt[ (2*mu / hbar^2) * (V(r) - Q_alpha) ] dr
   - For L = 0 (Analytical Gamow Formula):
       2*G_0 = [ 4 * Z_d * e^2 / (hbar * v) ] * [ arccos(sqrt(x_0)) - sqrt(x_0 * (1 - x_0)) ]
       where x_0 = R_0 / R_c(0) and v = sqrt(2 * Q_alpha / mu).
   - For L > 0 (Centrifugal Barrier):
       Numerically integrated using Simpson's 3/8 rule, accounting for centrifugal hindrance.

3. Decay Constant & Half-Life:
   Assault frequency: nu = v_in / (2 * R_0) ~ 10^21 - 10^22 s^-1  (v_in = sqrt(2*(Q + V_0)/m_alpha))
   Decay constant: lambda = nu * P(L) * S_alpha
   Half-life: T_12_WKB = ln(2) / lambda
   where S_alpha is the alpha preformation factor (typically 0.05 - 0.20 in heavy nuclei).

4. Hindrance Factor (HF):
   HF = T_12_exp / T_12_WKB(unhindered, L=0, S_alpha=1)
   - HF ~ 1 - 4   : Favored / unhindered transition (same Nilsson state or 0+ -> 0+).
   - HF ~ 10 - 500 : Hindered transition (change in parity, spin Delta_I = L, or configuration restructuring).

5. Viola-Seaborg Systematics (Sobiczewski Parameters):
   log10(T_12_sec) = (a * Z + b) / sqrt(Q_alpha) + (c * Z + d) + h_log
   where a = 1.66175, b = -8.5166, c = -0.20228, d = -33.9069.

References:
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第5章 (Alpha衰变).
  - G. Gamow, Z. Phys. 51, 204 (1928).
  - V. E. Viola and G. T. Seaborg, J. Inorg. Nucl. Chem. 28, 741 (1966).
  - A. Sobiczewski, F. A. Gareev, and B. N. Kalinkin, Phys. Lett. 22, 500 (1966).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def calculate_gamow_factor_wkb(
    Z_parent: int,
    A_parent: int,
    Q_alpha_MeV: float,
    L: int = 0,
    r0_fm: float = 1.25,
    V0_well_MeV: float = 25.0
) -> Dict[str, Any]:
    """
    Calculates exact WKB Gamow factor 2G, barrier penetration probability P,
    assault frequency nu, and theoretical unhindered half-life.
    """
    if Z_parent <= 2 or A_parent <= 4:
        raise ValueError("Parent nucleus must have Z > 2 and A > 4.")
    if Q_alpha_MeV <= 0.0:
        raise ValueError("Q_alpha must be positive for spontaneous alpha decay.")
    if L < 0:
        raise ValueError("Orbital angular momentum L must be nonnegative.")

    Z_d = Z_parent - 2
    A_d = A_parent - 4

    m_u = 931.494 # MeV/c^2
    m_alpha = 3727.379 # MeV/c^2
    m_d = float(A_d) * m_u
    mu_MeV = (m_alpha * m_d) / (m_alpha + m_d)

    c_m_s = 2.99792458e8 # m/s
    hbar_c = 197.327 # MeV * fm
    e2_constant = 1.439965 # MeV * fm
    alpha_em = 1.0 / 137.036

    # Nuclear touching radius R_0
    R_0 = r0_fm * (A_d ** (1.0 / 3.0) + 4.0 ** (1.0 / 3.0)) # fm

    # Classical outer turning point for L = 0
    Rc_0 = (2.0 * Z_d * e2_constant) / Q_alpha_MeV # fm

    if R_0 >= Rc_0:
        # Above barrier
        two_G = 0.0
        P_pen = 1.0
        Rc_eff = R_0
    else:
        v_over_c = math.sqrt(2.0 * Q_alpha_MeV / mu_MeV)
        x_0 = R_0 / Rc_0

        # Analytical L = 0 Gamow action:
        # 2*G_0 = [ 8 * Z_d * alpha_em / (v/c) ] * [ arccos(sqrt(x_0)) - sqrt(x_0 * (1 - x_0)) ]
        prefactor = (8.0 * Z_d * alpha_em) / v_over_c
        geom_factor = math.acos(math.sqrt(x_0)) - math.sqrt(x_0 * (1.0 - x_0))
        two_G0 = prefactor * geom_factor

        if L == 0:
            two_G = two_G0
            Rc_eff = Rc_0
        else:
            # Numerical Simpson integration for L > 0
            # V_eff(r) = [ 2 * Z_d * e^2 / r ] + [ hbar^2 * L*(L + 1) / (2 * mu * r^2) ]
            def integrand(r):
                v_coul = (2.0 * Z_d * e2_constant) / r
                v_cent = (hbar_c ** 2 * L * (L + 1.0)) / (2.0 * mu_MeV * (r ** 2))
                diff = v_coul + v_cent - Q_alpha_MeV
                return math.sqrt(max(0.0, diff))

            # Bisection search for Rc(L) where V_eff(Rc) = Q_alpha
            r_low = R_0
            r_high = Rc_0 * 2.0
            for _ in range(50):
                r_mid = 0.5 * (r_low + r_high)
                v_mid = (2.0 * Z_d * e2_constant) / r_mid + (hbar_c ** 2 * L * (L + 1.0)) / (2.0 * mu_MeV * (r_mid ** 2))
                if v_mid > Q_alpha_MeV:
                    r_low = r_mid
                else:
                    r_high = r_mid
            Rc_eff = r_mid

            # Composite Simpson rule
            N_steps = 1000
            dr = (Rc_eff - R_0) / float(N_steps)
            integ_val = 0.0
            for i in range(N_steps + 1):
                r_i = R_0 + i * dr
                weight = 1.0 if (i == 0 or i == N_steps) else (4.0 if i % 2 == 1 else 2.0)
                integ_val += weight * integrand(r_i)
            integ_val *= (dr / 3.0)

            # 2 * G(L) = 2 * sqrt(2 * mu) / hbar * integral
            two_G = 2.0 * math.sqrt(2.0 * mu_MeV) / hbar_c * integ_val

        # Penetration probability P = exp(-2G)
        P_pen = math.exp(-two_G) if two_G < 700.0 else 0.0

    # Assault frequency nu = v_in / (2 * R_0)
    R0_meters = R_0 * 1e-15
    v_in_c = math.sqrt(2.0 * (Q_alpha_MeV + V0_well_MeV) / m_alpha)
    v_in_m_s = v_in_c * c_m_s
    nu_s1 = v_in_m_s / (2.0 * R0_meters)

    # Theoretical unhindered decay constant and half-life (S_alpha = 1.0)
    lambda_unhindered = nu_s1 * P_pen
    if lambda_unhindered > 0.0:
        t12_wkb_sec = math.log(2.0) / lambda_unhindered
    else:
        t12_wkb_sec = float("inf")

    # Viola-Seaborg Systematics (Sobiczewski et al. parameters)
    a_vs = 1.66175
    b_vs = -8.5166
    c_vs = -0.20228
    d_vs = -33.9069
    # Even-odd hindrance parameter
    if Z_parent % 2 != 0 and A_parent % 2 != 0:
        h_log = 1.066 # odd-odd
    elif Z_parent % 2 != 0:
        h_log = 0.772 # odd-Z
    elif A_parent % 2 != 0:
        h_log = 0.605 # odd-N
    else:
        h_log = 0.0 # even-even

    log10_t12_vs = (a_vs * Z_parent + b_vs) / math.sqrt(Q_alpha_MeV) + (c_vs * Z_parent + d_vs) + h_log
    t12_vs_sec = 10.0 ** log10_t12_vs

    # Alpha particle kinetic energy with recoil correction: E_alpha = Q * (A-4)/A
    E_alpha_lab_MeV = Q_alpha_MeV * float(A_d) / float(A_parent)
    E_recoil_daughter_MeV = Q_alpha_MeV * 4.0 / float(A_parent)

    return {
        "parent": {"Z": Z_parent, "A": A_parent},
        "daughter": {"Z": Z_d, "A": A_d},
        "Q_alpha_MeV": Q_alpha_MeV,
        "E_alpha_lab_MeV": round(E_alpha_lab_MeV, 4),
        "E_recoil_daughter_keV": round(E_recoil_daughter_MeV * 1000.0, 2),
        "angular_momentum_L": L,
        "touching_radius_R0_fm": round(R_0, 3),
        "turning_point_Rc_fm": round(Rc_eff, 3),
        "Gamow_factor_2G": round(two_G, 3),
        "penetration_probability_P": P_pen,
        "assault_frequency_nu_s1": nu_s1,
        "T12_WKB_unhindered_sec": t12_wkb_sec,
        "T12_Viola_Seaborg_sec": t12_vs_sec,
        "log10_T12_Viola_Seaborg": round(log10_t12_vs, 3)
    }


def evaluate_alpha_hindrance(
    t12_exp_sec: float,
    t12_wkb_unhindered_sec: float
) -> Dict[str, Any]:
    """
    Calculates Hindrance Factor (HF) and effective alpha preformation factor S_alpha.
    """
    if t12_wkb_unhindered_sec <= 0.0 or t12_exp_sec <= 0.0:
        return {"hindrance_factor": None, "preformation_factor": None, "classification": "Undefined"}

    hf = t12_exp_sec / t12_wkb_unhindered_sec
    s_alpha = 1.0 / hf if hf > 0 else 0.0

    if hf < 4.0:
        classification = "Favored / Unhindered (0+ -> 0+ or identical Nilsson configuration)"
    elif hf < 50.0:
        classification = "Moderately Hindered (L > 0 angular momentum transfer or minor shape change)"
    else:
        classification = "Strongly Hindered (Major single-particle restructuring, Delta_pi change, or isomerism)"

    return {
        "T12_exp_sec": t12_exp_sec,
        "hindrance_factor_HF": round(hf, 2),
        "alpha_preformation_factor_S": round(s_alpha, 4),
        "transition_classification": classification
    }


def format_text_report(gam: Dict[str, Any], hin: Optional[Dict[str, Any]] = None) -> str:
    p = gam["parent"]
    d = gam["daughter"]
    lines = [
        "=" * 74,
        "   ALPHA DECAY GAMOW WKB TUNNELING & VIOLA-SEABORG SYSTEMATICS SUITE",
        "   Based on Lu Xiting §5.1-5.3 & Gamow Quantum Barrier Penetration Theory",
        "=" * 74,
        f" DECAY SYSTEM: ({p['Z']}, {p['A']}) -> ({d['Z']}, {d['A']}) + alpha",
        f"   Total Decay Energy Q_alpha : {gam['Q_alpha_MeV']:.4f} MeV",
        f"   Alpha Particle Lab Energy  : E_alpha = {gam['E_alpha_lab_MeV']:.4f} MeV",
        f"   Daughter Recoil Energy     : E_recoil = {gam['E_recoil_daughter_keV']:.2f} keV",
        f"   Orbital Angular Momentum L : {gam['angular_momentum_L']} hbar",
        "-" * 74,
        " WKB QUANTUM TUNNELING BARRIER CHARACTERISTICS:",
        f"   Nuclear Touching Radius R_0: {gam['touching_radius_R0_fm']:.3f} fm",
        f"   Classical Turning Point R_c: {gam['turning_point_Rc_fm']:.3f} fm (Barrier Width: {gam['turning_point_Rc_fm'] - gam['touching_radius_R0_fm']:.3f} fm)",
        f"   Gamow Action 2*G(L)        : {gam['Gamow_factor_2G']:.3f}",
        f"   Barrier Penetration P(L)   : {gam['penetration_probability_P']:.3e}",
        f"   Assault Frequency nu       : {gam['assault_frequency_nu_s1']:.3e} s^-1",
        "-" * 74,
        " THEORETICAL HALF-LIFE ESTIMATES:",
        f"   WKB Unhindered T_1/2       : {gam['T12_WKB_unhindered_sec']:.2e} s",
        f"   Viola-Seaborg Systematics  : {gam['T12_Viola_Seaborg_sec']:.2e} s (log10 T_1/2 = {gam['log10_T12_Viola_Seaborg']:.2f})",
    ]

    if hin is not None:
        lines.extend([
            "-" * 74,
            " EXPERIMENTAL HINDRANCE FACTOR (HF) & CONFIGURATION DIAGNOSTICS:",
            f"   Experimental Half-Life     : {hin['T12_exp_sec']:.2e} s",
            f"   Hindrance Factor HF        : {hin['hindrance_factor_HF']:.2f}",
            f"   Preformation Factor S_alpha: {hin['alpha_preformation_factor_S']:.4f}",
            f"   Transition Assignment      : {hin['transition_classification']}",
        ])

    lines.extend([
        "-" * 74,
        " Physical Significance & Methodological Guidelines:",
        "   - Half-life spans over 25 orders of magnitude, governed exponentially by 2G(Q).",
        "   - HF ~ 1 marks unhindered ground-to-ground or identical Nilsson state decays.",
        "   - Large HF (> 10) signals angular momentum barrier L > 0 or isomer configuration change.",
        "=" * 74
    ])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Alpha Decay Gamow WKB Penetration & Viola-Seaborg Calculator"
    )
    parser.add_argument("--Z", "-Z", type=int, default=84, help="Parent proton number Z (default: 84 for Po)")
    parser.add_argument("--A", "-A", type=int, default=212, help="Parent mass number A (default: 212)")
    parser.add_argument("--Q", "-Q", type=float, default=8.954, help="Q_alpha energy in MeV (default: 8.954 MeV)")
    parser.add_argument("--L", "-L", type=int, default=0, help="Angular momentum transfer L (default: 0)")
    parser.add_argument("--r0", type=float, default=1.25, help="Radius parameter r0 in fm (default: 1.25 fm)")
    parser.add_argument("--t12-exp", type=float, default=None, help="Experimental half-life in seconds")
    parser.add_argument("--preset", type=str, default=None,
                        choices=["212Po", "210Po", "238U", "241Am", "254No", "294Og"],
                        help="Benchmark preset: 212Po, 210Po, 238U, 241Am, 254No, 294Og")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")

    args = parser.parse_args()

    Z_val = args.Z
    A_val = args.A
    Q_val = args.Q
    L_val = args.L
    t12_exp = args.t12_exp

    if args.preset == "212Po":
        Z_val, A_val, Q_val, L_val, t12_exp = 84, 212, 8.954, 0, 2.99e-7
    elif args.preset == "210Po":
        Z_val, A_val, Q_val, L_val, t12_exp = 84, 210, 5.407, 0, 1.196e7
    elif args.preset == "238U":
        Z_val, A_val, Q_val, L_val, t12_exp = 92, 238, 4.270, 0, 1.41e17
    elif args.preset == "241Am":
        Z_val, A_val, Q_val, L_val, t12_exp = 95, 241, 5.578, 0, 1.36e10
    elif args.preset == "254No":
        Z_val, A_val, Q_val, L_val, t12_exp = 102, 254, 8.220, 0, 51.0
    elif args.preset == "294Og":
        Z_val, A_val, Q_val, L_val, t12_exp = 118, 294, 11.810, 0, 0.0007

    gam_res = calculate_gamow_factor_wkb(
        Z_parent=Z_val, A_parent=A_val, Q_alpha_MeV=Q_val, L=L_val, r0_fm=args.r0
    )

    hin_res = None
    if t12_exp is not None:
        hin_res = evaluate_alpha_hindrance(
            t12_exp_sec=t12_exp, t12_wkb_unhindered_sec=gam_res["T12_WKB_unhindered_sec"]
        )

    if args.json:
        out = {"gamow_wkb": gam_res}
        if hin_res is not None:
            out["hindrance"] = hin_res
        print(json.dumps(out, indent=2))
    else:
        print(format_text_report(gam_res, hin_res))


if __name__ == "__main__":
    main()
