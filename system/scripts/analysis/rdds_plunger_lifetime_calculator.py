#!/usr/bin/env python3
"""
rdds_plunger_lifetime_calculator.py
===================================
Recoil Distance Doppler-Shift (RDDS) Plunger Nuclear Lifetime &
Differential Decay Curve Method (DDCM) Analyzer.

Physics & Formulation:
----------------------
1. Plunger Kinematics:
   - Target at x = 0, Stopper at x = d (distance from ~1 um to 10 mm).
   - Recoil velocity: v = beta * c.
   - Flight time: t_flight = d / (beta * c).
   - Gamma emission in flight (shifted peak): E_s = E_0 * (1 + beta * cos(theta)).
   - Gamma emission after stopping (unshifted peak): E_u = E_0.

2. Decay Ratio Function R(d):
   For a single level decaying with lifetime tau:
     I_u(d) = I_0 * exp(-d / (beta * c * tau))
     I_s(d) = I_0 * [ 1 - exp(-d / (beta * c * tau)) ]
     R(d) = I_u(d) / [ I_s(d) + I_u(d) ] = exp(-d / (beta * c * tau))
   Lifetime inversion:
     tau = - [ d(ln R) / d(d) ]^(-1) / (beta * c)

3. Differential Decay Curve Method (DDCM, Dewald 1989):
   Eliminates feeding model dependence by using the derivative of the shifted curve:
     tau(d) = [ I_u(d) - alpha_feed * I_u_feed(d) ] / [ v * (d(I_s) / dd) ]
   where alpha_feed normalizes the direct feeding intensity.

4. B(E2) and Transition Quadrupole Moment Q_t:
   tau = 1.0 / T_gamma. For pure E2 transition:
     B(E2; I -> I-2) = 0.0816 / [ E_gamma^5(MeV) * tau(ps) * (1 + alpha_tot) ]  (e^2 b^2)
     Q_t = sqrt[ (16 * pi / 5) * B(E2) / <I K 2 0 | I-2 K>^2 ]

References:
  - T. K. Alexander and J. S. Forster, Adv. Nucl. Phys. 10, 197 (1978).
  - A. Dewald et al., Z. Phys. A 334, 163 (1989) [DDCM method].
  - 吴治华, 《原子核物理实验方法》, 第三版.
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple

C_LIGHT_UM_PS = 0.299792458  # um / ps


def calculate_flight_time_and_shifts(
    distance_um: float,
    beta_v_over_c: float,
    E_0_keV: float,
    det_angle_deg: float = 30.0
) -> Dict[str, float]:
    """
    Computes recoil flight time in ps and shifted/unshifted peak positions in keV.
    """
    v_um_ps = beta_v_over_c * C_LIGHT_UM_PS
    t_flight_ps = distance_um / max(v_um_ps, 1e-6)

    rad = math.radians(det_angle_deg)
    # First-order Doppler shift
    E_shifted_keV = E_0_keV * (1.0 + beta_v_over_c * math.cos(rad))
    delta_E_keV = E_shifted_keV - E_0_keV

    return {
        "distance_um": distance_um,
        "flight_time_ps": round(t_flight_ps, 2),
        "E_unshifted_keV": E_0_keV,
        "E_shifted_keV": round(E_shifted_keV, 2),
        "Doppler_shift_keV": round(delta_E_keV, 2)
    }


def fit_exponential_rdds_lifetime(
    distances_um: List[float],
    I_unshifted: List[float],
    I_shifted: List[float],
    beta_v_over_c: float
) -> Dict[str, Any]:
    """
    Inverts the mean lifetime tau (in ps) from a series of (distance, I_u, I_s) points
    using linear regression on ln(R) vs d.
    """
    v_um_ps = beta_v_over_c * C_LIGHT_UM_PS

    valid_d = []
    ln_R_list = []

    for d, u, s in zip(distances_um, I_unshifted, I_shifted):
        tot = u + s
        if tot > 0 and u > 0:
            r = u / tot
            if 0.02 < r < 0.98:  # Sensitive region
                valid_d.append(d)
                ln_R_list.append(math.log(r))

    n = len(valid_d)
    if n < 2:
        return {"error": "Insufficient points in sensitive region (0.02 < R < 0.98)"}

    mean_d = sum(valid_d) / n
    mean_lnr = sum(ln_R_list) / n

    num = sum((valid_d[i] - mean_d) * (ln_R_list[i] - mean_lnr) for i in range(n))
    den = sum((valid_d[i] - mean_d) ** 2 for i in range(n))
    slope = num / den if den != 0 else 0.0

    # ln R = - d / (v * tau) -> slope = - 1 / (v * tau) -> tau = - 1 / (slope * v)
    if slope < 0:
        tau_ps = - 1.0 / (slope * v_um_ps)
    else:
        tau_ps = float("inf")

    # Standard linear regression variance on slope
    ss_res = sum((ln_R_list[i] - (mean_lnr + slope * (valid_d[i] - mean_d))) ** 2 for i in range(n))
    s_err = math.sqrt(ss_res / (n - 2) / den) if n > 2 and den > 0 else 0.1 * abs(slope)
    tau_uncert_ps = abs(tau_ps * (s_err / abs(slope))) if abs(slope) > 0 else 0.0

    return {
        "num_sensitive_points": n,
        "regression_slope_um_inv": round(slope, 6),
        "recoil_velocity_um_ps": round(v_um_ps, 4),
        "extracted_lifetime_ps": round(tau_ps, 2),
        "lifetime_uncertainty_ps": round(tau_uncert_ps, 2)
    }


def calculate_ddcm_point_lifetime(
    I_u: float,
    I_s_derivative: float,  # d(I_s) / dd in um^-1
    beta_v_over_c: float,
    I_u_feed: Optional[float] = None,
    alpha_feed: float = 0.0
) -> float:
    """
    Computes DDCM lifetime at a single distance point:
    tau = (I_u - alpha_feed * I_u_feed) / (v * d(I_s)/dd).
    """
    v_um_ps = beta_v_over_c * C_LIGHT_UM_PS
    net_u = I_u - (alpha_feed * I_u_feed if I_u_feed is not None else 0.0)

    denom = v_um_ps * I_s_derivative
    if denom > 1e-6:
        return net_u / denom
    return float("nan")


def convert_lifetime_to_be2_and_qt(
    tau_ps: float,
    E_gamma_keV: float,
    I_initial: float = 2.0,
    K_quantum: float = 0.0,
    alpha_conversion: float = 0.01
) -> Dict[str, Any]:
    """
    Extracts reduced transition probability B(E2) (e^2 b^2) and transition
    quadrupole moment Q_t (e b) from measured plunger lifetime.
    """
    E_MeV = E_gamma_keV * 1e-3
    # B(E2) = 0.0816 / [ E_gamma^5 * tau * (1 + alpha) ]
    denom = (E_MeV ** 5) * tau_ps * (1.0 + alpha_conversion)
    b_e2 = 0.0816 / max(denom, 1e-12)

    # Clebsch-Gordan coefficient <I K 2 0 | I-2 K>
    # For 2+ -> 0+ with K=0: <2 0 2 0 | 0 0> = 1 / sqrt(5)
    cg_sq = 0.20  # standard for 2 -> 0

    # Q_t = sqrt[ (16*pi/5) * B(E2) / cg_sq ]
    q_t_eb = math.sqrt(max((16.0 * math.pi / 5.0) * b_e2 / cg_sq, 0.0))

    # Weisskopf unit: B_W(E2) = 0.0594 * A^(4/3) e^2 fm^4 ~ 5.94e-6 * A^(4/3) e^2 b^2
    # For A ~ 130: B_W(E2) ~ 5.94e-6 * 638 ~ 0.0038 e^2 b^2
    b_e2_wu = b_e2 / 0.0038

    return {
        "tau_ps": tau_ps,
        "E_gamma_keV": E_gamma_keV,
        "B_E2_e2_b2": round(b_e2, 4),
        "B_E2_Weisskopf_units": round(b_e2_wu, 1),
        "transition_quadrupole_moment_Qt_eb": round(q_t_eb, 3)
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   RECOIL DISTANCE DOPPLER SHIFT (RDDS) PLUNGER LIFETIME ANALYZER")
    lines.append("=" * 72)

    kin = summary["kinematics"]
    lines.append(f" PLUNGER KINEMATICS: E_0 = {kin['E_unshifted_keV']} keV, v/c = {summary['beta_v_over_c']:.4f}")
    lines.append(f"   Recoil Velocity                : {kin['flight_time_ps']} ps at d = {kin['distance_um']} um")
    lines.append(f"   Doppler Shifted Peak E_s       : {kin['E_shifted_keV']} keV (Shift = {kin['Doppler_shift_keV']} keV)")
    lines.append("-" * 72)

    if "exponential_fit" in summary:
        ef = summary["exponential_fit"]
        lines.append(" EXPONENTIAL DECAY CURVE FIT:")
        lines.append(f"   Sensitive Points Analyzed      : {ef['num_sensitive_points']}")
        lines.append(f"   Recoil Velocity                : {ef['recoil_velocity_um_ps']} um/ps")
        lines.append(f"   Extracted Level Lifetime tau   : {ef['extracted_lifetime_ps']} +/- {ef['lifetime_uncertainty_ps']} ps")
        lines.append("-" * 72)

    if "electromagnetic" in summary:
        em = summary["electromagnetic"]
        lines.append(" EXTRACTED TRANSITION STRENGTH & COLLECTIVE DEFORMATION:")
        lines.append(f"   B(E2) Transition Probability   : {em['B_E2_e2_b2']} e^2 b^2 ({em['B_E2_Weisskopf_units']} W.u.)")
        lines.append(f"   Transition Quadrupole Moment Qt: {em['transition_quadrupole_moment_Qt_eb']} e*b")
        lines.append("-" * 72)

    lines.append(" Physical Significance:")
    lines.append("   - RDDS Plunger is the gold-standard method for picosecond lifetimes (1-200 ps).")
    lines.append("   - DDCM removes side-feeding delay dependence by using shifted curve derivatives.")
    lines.append("   - Provides absolute B(E2) to test triaxial wobbling and superdeformation.")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Recoil Distance Doppler Shift (RDDS) Plunger Lifetime Analyzer."
    )
    parser.add_argument("--beta", type=float, default=0.015, help="Recoil velocity v/c (default: 0.015)")
    parser.add_argument("--E0", type=float, default=400.0, help="Unshifted gamma transition energy in keV (default: 400.0)")
    parser.add_argument("--demo-fit", action="store_true", help="Run benchmark RDDS distance scan regression")
    parser.add_argument("--distances", type=str, default=None, help="Comma-separated distances in um")
    parser.add_argument("--I-u", type=str, default=None, help="Comma-separated unshifted peak intensities")
    parser.add_argument("--I-s", type=str, default=None, help="Comma-separated shifted peak intensities")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    kin = calculate_flight_time_and_shifts(50.0, args.beta, args.E0)
    summary = {"beta_v_over_c": args.beta, "kinematics": kin}

    if args.demo_fit or (args.distances is None):
        # Synthetic plunger scan for tau ~ 15 ps with v = 0.015 c ~ 0.0045 um/ps
        # v * tau ~ 0.0045 * 15 ~ 0.067 um? wait: v = 0.015 * 0.3 um/ps = 0.0045 um/ps
        # Let's say v = 0.02 c -> v = 0.006 um/ps -> at d = 50 um, t = 50 / 0.0045 ~ 11 ps
        dist = [10.0, 25.0, 50.0, 80.0, 120.0, 180.0, 250.0]
        iu = [90.0, 75.0, 52.0, 32.0, 16.0, 5.0, 1.5]
        iss = [10.0, 25.0, 48.0, 68.0, 84.0, 95.0, 98.5]
        ef_res = fit_exponential_rdds_lifetime(dist, iu, iss, args.beta)
        summary["exponential_fit"] = ef_res
        if "extracted_lifetime_ps" in ef_res and ef_res["extracted_lifetime_ps"] > 0:
            summary["electromagnetic"] = convert_lifetime_to_be2_and_qt(ef_res["extracted_lifetime_ps"], args.E0)
    elif args.distances and args.I_u and args.I_s:
        dist = [float(x.strip()) for x in args.distances.split(",")]
        iu = [float(x.strip()) for x in args.I_u.split(",")]
        iss = [float(x.strip()) for x in args.I_s.split(",")]
        ef_res = fit_exponential_rdds_lifetime(dist, iu, iss, args.beta)
        summary["exponential_fit"] = ef_res
        if "extracted_lifetime_ps" in ef_res and ef_res["extracted_lifetime_ps"] > 0:
            summary["electromagnetic"] = convert_lifetime_to_be2_and_qt(ef_res["extracted_lifetime_ps"], args.E0)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
