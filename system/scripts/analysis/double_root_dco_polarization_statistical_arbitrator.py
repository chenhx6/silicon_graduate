#!/usr/bin/env python3
"""
double_root_dco_polarization_statistical_arbitrator.py
======================================================
In-Beam Gamma-Ray Spectroscopy DCO / Angular Distribution Multipole Mixing Ratio delta(E2/M1)
Double-Root Profile Likelihood, Linear Polarization Arbitration & Statistical Exclusion Suite.

Physics & Statistical Principles:
---------------------------------
1. DCO Quadratic Equation & Double-Root Origin:
   In directional correlations from oriented states (DCO) or angular distribution measurements,
   the observed directional correlation ratio for an unknown mixed transition (I_i -> I_f)
   gated on a known stretched E2 cascade is given by:
     R_DCO(delta) = W(theta1, theta2; delta) / W(theta2, theta1; delta)
                  = (A0 + A1 * delta + A2 * delta^2) / (B0 + B1 * delta + B2 * delta^2)
   Equating R_DCO(delta) = R_exp yields a quadratic equation:
     c2 * delta^2 + c1 * delta + c0 = 0
   where:
     c2 = A2 - R_exp * B2
     c1 = A1 - R_exp * B1
     c0 = A0 - R_exp * B0
   If discriminant Delta = c1^2 - 4 * c2 * c0 >= 0, mathematics inevitably yields TWO real roots:
     delta_1 = (-c1 - sqrt(Delta)) / (2 * c2)
     delta_2 = (-c1 + sqrt(Delta)) / (2 * c2)
   One root typically corresponds to small |delta| (predominantly M1), while the other
   corresponds to large |delta| (predominantly E2).

2. Statistical Profile Likelihood chi^2(delta) & Bounded Parameterization:
   Following 朱永生《实验物理中的概率和统计》第 6, 8, 9 章 and Hamilton (1975) Ch. 14:
   To avoid infinities as delta -> +-infinity (pure E2), the parameter is mapped to a compact angle:
     theta_delta = arctan(delta) in (-pi/2, +pi/2)  [-90 deg, +90 deg]
   The profile chi^2 is constructed as:
     chi^2_DCO(delta) = [ (R_DCO(delta) - R_exp) / sigma_R ]^2
   The 1-sigma confidence intervals around each root correspond to Delta chi^2 <= 1.0 (Neyman interval).

3. Multi-Physical Arbitration Engine (Resolving Spurious Mathematical Roots):
   a. Linear Polarization P(theta=90 deg):
      P(delta) = (p0 + p1 * delta + p2 * delta^2) / (q0 + q1 * delta + q2 * delta^2)
      For M1+E2 transitions, P is typically negative for small delta (magnetic character)
      and positive for large delta (electric character). Measuring P_exp breaks the degeneracy.
   b. Internal Conversion Coefficient alpha_K:
      alpha_K(delta) = [ alpha_K(M1) + delta^2 * alpha_K(E2) ] / [ 1 + delta^2 ]
      Comparison with BrIcc theory and experimental alpha_exp eliminates inconsistent roots.
   c. Weisskopf Single-Particle Rate Ceiling:
      Given state lifetime tau (or width Gamma) and gamma branching ratio:
        T(M1) = [ b_gamma / (tau * (1 + alpha_tot)) ] * [ 1 / (1 + delta^2) ]
        T(E2) = [ b_gamma / (tau * (1 + alpha_tot)) ] * [ delta^2 / (1 + delta^2) ]
      B(M1) [W.u.] and B(E2) [W.u.] are calculated. If B(M1) > 5.0 - 10.0 W.u.,
      it violates the single-particle Moszkowski/Weisskopf upper limit and is ruled unphysical.
   d. Likelihood Ratio Hypothesis Testing:
      Delta chi^2 = chi^2_joint(delta_2) - chi^2_joint(delta_1).
      The exclusion confidence level is:
        CL = erf( sqrt(Delta chi^2 / 2) ) * 100%
      If Delta chi^2 > 9.0, the spurious root is excluded at > 99.73% (3-sigma) confidence level.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "135Pr_wobbling_candidate": {
        "description": "135Pr transverse wobbling candidate transition (17/2+ -> 15/2+, 728 keV)",
        "nucleus": "135Pr",
        "E_gamma_keV": 728.0,
        "A_mass": 135,
        "tau_ps": 1.20,
        "A_coeffs": [1.0, 0.45, 0.90],
        "B_coeffs": [1.4, -0.70, 1.80],
        "R_exp": 0.45,
        "sigma_R": 0.04,
        "P_coeffs": [-0.15, 0.10, 0.55],
        "Q_coeffs": [1.0, 0.45, 0.90],
        "P_exp": 0.22,
        "sigma_P": 0.05,
        "alpha_K_M1": 0.0058,
        "alpha_K_E2": 0.0042,
        "alpha_exp": 0.0044,
        "sigma_alpha": 0.0004
    },
    "134Pr_chiral_intraband": {
        "description": "134Pr chiral doublet intraband M1+E2 transition (13+ -> 12+, 422 keV)",
        "nucleus": "134Pr",
        "E_gamma_keV": 422.0,
        "A_mass": 134,
        "tau_ps": 3.50,
        "A_coeffs": [1.10, 0.35, 0.75],
        "B_coeffs": [1.15, -0.40, 1.25],
        "R_exp": 0.95,
        "sigma_R": 0.05,
        "P_coeffs": [-0.25, 0.05, 0.48],
        "Q_coeffs": [1.10, 0.35, 0.75],
        "P_exp": -0.18,
        "sigma_P": 0.06,
        "alpha_K_M1": 0.0380,
        "alpha_K_E2": 0.0210,
        "alpha_exp": 0.0365,
        "sigma_alpha": 0.0030
    },
    "136Nd_triaxial_crossover": {
        "description": "136Nd gamma-band to ground-band Delta I=0 transition (2_2+ -> 2_1+, 552 keV)",
        "nucleus": "136Nd",
        "E_gamma_keV": 552.0,
        "A_mass": 136,
        "tau_ps": 2.10,
        "A_coeffs": [1.05, -0.25, 0.85],
        "B_coeffs": [1.20, 0.30, 1.40],
        "R_exp": 0.82,
        "sigma_R": 0.06,
        "P_coeffs": [-0.18, 0.12, 0.52],
        "Q_coeffs": [1.05, -0.25, 0.85],
        "P_exp": 0.15,
        "sigma_P": 0.07,
        "alpha_K_M1": 0.0160,
        "alpha_K_E2": 0.0095,
        "alpha_exp": 0.0110,
        "sigma_alpha": 0.0015
    }
}


def solve_dco_quadratic(A_coeffs, B_coeffs, R_exp):
    """
    Solves (A2 - R_exp * B2)*delta^2 + (A1 - R_exp * B1)*delta + (A0 - R_exp * B0) = 0.
    Returns roots, discriminant, and status.
    """
    A0, A1, A2 = A_coeffs
    B0, B1, B2 = B_coeffs
    c2 = A2 - R_exp * B2
    c1 = A1 - R_exp * B1
    c0 = A0 - R_exp * B0

    if abs(c2) < 1e-12:
        if abs(c1) < 1e-12:
            return {"roots": [], "status": "degenerate_no_solution", "discriminant": 0.0}
        root = -c0 / c1
        return {"roots": [float(root)], "status": "single_linear_root", "discriminant": 0.0}

    disc = c1**2 - 4.0 * c2 * c0
    if disc < 0:
        tangent_root = -c1 / (2.0 * c2)
        return {"roots": [float(tangent_root)], "status": "negative_discriminant_tangent", "discriminant": float(disc)}

    d1 = (-c1 - math.sqrt(disc)) / (2.0 * c2)
    d2 = (-c1 + math.sqrt(disc)) / (2.0 * c2)
    roots = sorted([float(d1), float(d2)])
    return {"roots": roots, "status": "two_real_roots", "discriminant": float(disc)}


def evaluate_r_dco(delta, A_coeffs, B_coeffs):
    A0, A1, A2 = A_coeffs
    B0, B1, B2 = B_coeffs
    num = A0 + A1 * delta + A2 * delta**2
    den = B0 + B1 * delta + B2 * delta**2
    if abs(den) < 1e-15:
        return 1e12
    return num / den


def evaluate_polarization(delta, P_coeffs, Q_coeffs):
    p0, p1, p2 = P_coeffs
    q0, q1, q2 = Q_coeffs
    num = p0 + p1 * delta + p2 * delta**2
    den = q0 + q1 * delta + q2 * delta**2
    if abs(den) < 1e-15:
        return 0.0
    return num / den


def evaluate_alpha_k(delta, alpha_M1, alpha_E2):
    return (alpha_M1 + delta**2 * alpha_E2) / (1.0 + delta**2)


def calculate_weisskopf_estimates(A_mass, E_gamma_keV, tau_ps, delta):
    """
    Computes B(M1) [W.u.] and B(E2) [W.u.] from state lifetime and delta.
    """
    if tau_ps is None or tau_ps <= 0:
        return None
    E_MeV = E_gamma_keV / 1000.0
    tau_s = tau_ps * 1e-12
    T_gamma = 1.0 / tau_s

    T_W_M1 = 3.15e13 * (E_MeV**3)
    T_W_E2 = 1.22e9 * (A_mass**(4.0 / 3.0)) * (E_MeV**5)

    T_M1 = T_gamma / (1.0 + delta**2)
    T_E2 = T_gamma * (delta**2) / (1.0 + delta**2)

    B_M1_Wu = T_M1 / T_W_M1 if T_W_M1 > 0 else 0.0
    B_E2_Wu = T_E2 / T_W_E2 if T_W_E2 > 0 else 0.0

    return {
        "B_M1_Wu": float(B_M1_Wu),
        "B_E2_Wu": float(B_E2_Wu),
        "T_M1_s": float(T_M1),
        "T_E2_s": float(T_E2)
    }


def analyze_double_roots(
    A_coeffs,
    B_coeffs,
    R_exp,
    sigma_R,
    P_coeffs=None,
    Q_coeffs=None,
    P_exp=None,
    sigma_P=None,
    alpha_K_M1=None,
    alpha_K_E2=None,
    alpha_exp=None,
    sigma_alpha=None,
    tau_ps=None,
    E_gamma_keV=None,
    A_mass=None
):
    """
    Complete analysis of double roots, profile chi^2 scan, and physical arbitration.
    """
    sol = solve_dco_quadratic(A_coeffs, B_coeffs, R_exp)
    roots = sol["roots"]

    theta_deg = np.linspace(-89.0, 89.0, 179)
    theta_rad = np.radians(theta_deg)
    delta_scan = np.tan(theta_rad)

    chi2_dco_scan = []
    chi2_pol_scan = []
    chi2_alpha_scan = []
    chi2_tot_scan = []

    for d in delta_scan:
        R_calc = evaluate_r_dco(d, A_coeffs, B_coeffs)
        c2_r = ((R_calc - R_exp) / sigma_R)**2
        chi2_dco_scan.append(float(c2_r))

        c2_p = 0.0
        if P_coeffs is not None and Q_coeffs is not None and P_exp is not None and sigma_P is not None:
            P_calc = evaluate_polarization(d, P_coeffs, Q_coeffs)
            c2_p = ((P_calc - P_exp) / sigma_P)**2
        chi2_pol_scan.append(float(c2_p))

        c2_a = 0.0
        if alpha_K_M1 is not None and alpha_K_E2 is not None and alpha_exp is not None and sigma_alpha is not None:
            a_calc = evaluate_alpha_k(d, alpha_K_M1, alpha_K_E2)
            c2_a = ((a_calc - alpha_exp) / sigma_alpha)**2
        chi2_alpha_scan.append(float(c2_a))

        chi2_tot_scan.append(float(c2_r + c2_p + c2_a))

    evaluated_roots = []
    for idx, d in enumerate(roots):
        R_calc = evaluate_r_dco(d, A_coeffs, B_coeffs)
        c2_r = ((R_calc - R_exp) / sigma_R)**2

        f_E2 = (d**2) / (1.0 + d**2) * 100.0
        f_M1 = 100.0 - f_E2

        root_info = {
            "root_index": idx + 1,
            "delta": float(d),
            "arctan_delta_deg": float(math.degrees(math.atan(d))),
            "f_E2_percent": float(f_E2),
            "f_M1_percent": float(f_M1),
            "R_calc": float(R_calc),
            "chi2_DCO": float(c2_r)
        }

        chi2_joint = c2_r

        if P_coeffs is not None and Q_coeffs is not None and P_exp is not None and sigma_P is not None:
            P_calc = evaluate_polarization(d, P_coeffs, Q_coeffs)
            c2_p = ((P_calc - P_exp) / sigma_P)**2
            root_info["P_calc"] = float(P_calc)
            root_info["chi2_pol"] = float(c2_p)
            chi2_joint += c2_p

        if alpha_K_M1 is not None and alpha_K_E2 is not None and alpha_exp is not None and sigma_alpha is not None:
            a_calc = evaluate_alpha_k(d, alpha_K_M1, alpha_K_E2)
            c2_a = ((a_calc - alpha_exp) / sigma_alpha)**2
            root_info["alpha_calc"] = float(a_calc)
            root_info["chi2_alpha"] = float(c2_a)
            chi2_joint += c2_a

        root_info["chi2_joint"] = float(chi2_joint)

        if tau_ps is not None and E_gamma_keV is not None and A_mass is not None:
            wk = calculate_weisskopf_estimates(A_mass, E_gamma_keV, tau_ps, d)
            root_info["weisskopf"] = wk
            if wk and wk["B_M1_Wu"] > 5.0:
                root_info["weisskopf_violation"] = "B(M1) exceeds single-particle ceiling (> 5 W.u.)"

        evaluated_roots.append(root_info)

    arbitration = {
        "status": "undetermined",
        "favored_root": None,
        "excluded_root": None,
        "delta_chi2": 0.0,
        "exclusion_confidence_percent": 0.0,
        "summary": ""
    }

    if len(evaluated_roots) == 2:
        r1 = evaluated_roots[0]
        r2 = evaluated_roots[1]
        c1 = r1["chi2_joint"]
        c2 = r2["chi2_joint"]
        d_chi2 = abs(c2 - c1)
        arbitration["delta_chi2"] = float(d_chi2)

        cl = math.erf(math.sqrt(d_chi2 / 2.0)) * 100.0
        arbitration["exclusion_confidence_percent"] = float(cl)

        v1 = "weisskopf_violation" in r1
        v2 = "weisskopf_violation" in r2

        if v1 and not v2:
            arbitration["status"] = "resolved_by_weisskopf_ceiling"
            arbitration["favored_root"] = 2
            arbitration["excluded_root"] = 1
            arbitration["summary"] = f"Root 1 excluded by anomalous M1 strength ({r1['weisskopf']['B_M1_Wu']:.2f} W.u. > 5 W.u.); Root 2 favored."
        elif v2 and not v1:
            arbitration["status"] = "resolved_by_weisskopf_ceiling"
            arbitration["favored_root"] = 1
            arbitration["excluded_root"] = 2
            arbitration["summary"] = f"Root 2 excluded by anomalous M1 strength ({r2['weisskopf']['B_M1_Wu']:.2f} W.u. > 5 W.u.); Root 1 favored."
        elif d_chi2 >= 9.0:
            fav = 1 if c1 < c2 else 2
            excl = 2 if c1 < c2 else 1
            arbitration["status"] = "resolved_by_3sigma_statistical_exclusion"
            arbitration["favored_root"] = fav
            arbitration["excluded_root"] = excl
            arbitration["summary"] = f"Root {excl} rejected at {cl:.2f}% CL (Delta chi^2 = {d_chi2:.2f} >= 9.0, >3-sigma); Root {fav} favored."
        elif d_chi2 >= 4.0:
            fav = 1 if c1 < c2 else 2
            excl = 2 if c1 < c2 else 1
            arbitration["status"] = "strongly_favored_2sigma"
            arbitration["favored_root"] = fav
            arbitration["excluded_root"] = excl
            arbitration["summary"] = f"Root {fav} favored over Root {excl} at {cl:.2f}% CL (Delta chi^2 = {d_chi2:.2f} >= 4.0, ~2-sigma)."
        else:
            arbitration["status"] = "unresolved_ambiguity"
            arbitration["summary"] = f"Ambiguity persists (Delta chi^2 = {d_chi2:.2f} < 4.0, CL = {cl:.1f}%). Additional linear polarization or conversion measurement required."

    return {
        "status": sol["status"],
        "discriminant": sol["discriminant"],
        "evaluated_roots": evaluated_roots,
        "arbitration": arbitration,
        "profile_scan_summary": {
            "min_chi2_tot": float(min(chi2_tot_scan)),
            "theta_min_deg": float(theta_deg[np.argmin(chi2_tot_scan)])
        }
    }


def main():
    parser = argparse.ArgumentParser(
        description="DCO Multipole Mixing Ratio Double-Root Profile Likelihood & Polarization Statistical Arbitrator."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--r-exp", type=float, help="Experimental DCO ratio R_exp")
    parser.add_argument("--sigma-r", type=float, default=0.05, help="Uncertainty on R_exp")
    parser.add_argument("--p-exp", type=float, help="Experimental linear polarization P_exp")
    parser.add_argument("--sigma-p", type=float, default=0.05, help="Uncertainty on P_exp")
    parser.add_argument("--alpha-exp", type=float, help="Experimental conversion coefficient alpha_exp")
    parser.add_argument("--sigma-alpha", type=float, default=0.002, help="Uncertainty on alpha_exp")
    parser.add_argument("--tau-ps", type=float, help="State lifetime in picoseconds")
    parser.add_argument("--energy-kev", type=float, help="Gamma-ray energy in keV")
    parser.add_argument("--mass-a", type=int, help="Mass number A")
    parser.add_argument("--json", action="store_true", help="Output JSON format")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        A_coeffs = p["A_coeffs"]
        B_coeffs = p["B_coeffs"]
        R_exp = p["R_exp"]
        sigma_R = p["sigma_R"]
        P_coeffs = p.get("P_coeffs")
        Q_coeffs = p.get("Q_coeffs")
        P_exp = p.get("P_exp")
        sigma_P = p.get("sigma_P")
        alpha_K_M1 = p.get("alpha_K_M1")
        alpha_K_E2 = p.get("alpha_K_E2")
        alpha_exp = p.get("alpha_exp")
        sigma_alpha = p.get("sigma_alpha")
        tau_ps = p.get("tau_ps")
        E_gamma_keV = p.get("E_gamma_keV")
        A_mass = p.get("A_mass")
        title = f"Preset: {args.preset} ({p['description']})"
    elif args.r_exp is not None:
        A_coeffs = [1.0, 0.45, 0.90]
        B_coeffs = [1.4, -0.70, 1.80]
        R_exp = args.r_exp
        sigma_R = args.sigma_r
        P_coeffs = [-0.15, 0.10, 0.55] if args.p_exp is not None else None
        Q_coeffs = [1.0, 0.45, 0.90] if args.p_exp is not None else None
        P_exp = args.p_exp
        sigma_P = args.sigma_p
        alpha_K_M1 = 0.0058 if args.alpha_exp is not None else None
        alpha_K_E2 = 0.0042 if args.alpha_exp is not None else None
        alpha_exp = args.alpha_exp
        sigma_alpha = args.sigma_alpha
        tau_ps = args.tau_ps
        E_gamma_keV = args.energy_kev
        A_mass = args.mass_a
        title = "Custom User Input"
    else:
        return parser.print_help()

    res = analyze_double_roots(
        A_coeffs=A_coeffs,
        B_coeffs=B_coeffs,
        R_exp=R_exp,
        sigma_R=sigma_R,
        P_coeffs=P_coeffs,
        Q_coeffs=Q_coeffs,
        P_exp=P_exp,
        sigma_P=sigma_P,
        alpha_K_M1=alpha_K_M1,
        alpha_K_E2=alpha_K_E2,
        alpha_exp=alpha_exp,
        sigma_alpha=sigma_alpha,
        tau_ps=tau_ps,
        E_gamma_keV=E_gamma_keV,
        A_mass=A_mass
    )

    if args.json:
        print(json.dumps(res, indent=2))
        return

    print("=" * 76)
    print("DCO Mixing Ratio Double-Root Profile Likelihood & Polarization Arbitrator")
    print(f"{title}")
    print("=" * 76)
    print(f"Discriminant Delta: {res['discriminant']:.5f} -> Status: {res['status']}")
    print("-" * 76)
    for r in res["evaluated_roots"]:
        print(f"Root {r['root_index']}: delta = {r['delta']:+.4f} (arctan delta = {r['arctan_delta_deg']:+.1f} deg)")
        print(f"  Multipole Fractions : E2 = {r['f_E2_percent']:.1f}%, M1 = {r['f_M1_percent']:.1f}%")
        print(f"  DCO Ratio           : R_calc = {r['R_calc']:.4f} (chi^2 = {r['chi2_DCO']:.3f})")
        if "P_calc" in r:
            print(f"  Linear Polarization : P_calc = {r['P_calc']:+.4f} (chi^2 = {r['chi2_pol']:.3f})")
        if "alpha_calc" in r:
            print(f"  Conversion Coeff    : alpha_calc = {r['alpha_calc']:.5f} (chi^2 = {r['chi2_alpha']:.3f})")
        print(f"  Joint Chi^2         : {r['chi2_joint']:.3f}")
        if "weisskopf" in r and r["weisskopf"]:
            wk = r["weisskopf"]
            print(f"  Weisskopf Strengths : B(M1) = {wk['B_M1_Wu']:.3f} W.u., B(E2) = {wk['B_E2_Wu']:.2f} W.u.")
        if "weisskopf_violation" in r:
            print(f"  [!] VIOLATION       : {r['weisskopf_violation']}")
        print("-" * 76)

    arb = res["arbitration"]
    print(f"Arbitration Result: {arb['status']}")
    print(f"  Delta Chi^2       : {arb['delta_chi2']:.3f}")
    print(f"  Exclusion CL      : {arb['exclusion_confidence_percent']:.2f}%")
    print(f"  Verdict           : {arb['summary']}")
    print("=" * 76)


if __name__ == "__main__":
    main()
