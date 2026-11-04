#!/usr/bin/env python3
"""
in_beam_rdds_ddcm_lifetime_inverter.py
======================================
Synthetic RDDS/DDCM Differential Decay Curve Demonstration,
Plateau Screening & Derived Transition-Quantity Calculator.

Physics Formulation:
--------------------
1. Recoil Distance Doppler-Shift (RDDS) & Plunger Technique:
   Based on 吴治华《原子核物理实验方法》第 15 章 §15.2 (pp. 430–445), 汪晓莲《粒子探测技术》第 5 章,
   A. Dewald et al. (Z. Phys. A 334, 163, 1989), and A. Dewald et al. (Prog. Part. Nucl. Phys. 67, 786, 2012):
   In in-beam plunger experiments, excited compound nuclei recoil from a thin target at speed v = beta * c
   and travel a variable mechanical distance d towards a stopper foil.
   The detected gamma-ray line splits into:
     - Shifted peak I_s(d): emitted in flight before reaching the stopper (Doppler shifted);
     - Stopped peak I_u(d): emitted after stopping inside the backing (unshifted).

2. Dewald Differential Decay Curve Method (DDCM):
   Unlike traditional centroid-shift or integral fits that suffer severely from unknown side-feeding
   delays, the DDCM solves Bateman's differential rate equation directly:
     d I_u(d) / dd = [ 1 / (v * tau) ] * [ I_s(d) - sum_k b_k * I_s,k_feed(d) ].
   When gating on higher transitions or in isolated decay:
     tau(d) = [ 1 / v ] * [ (1.0 - R(d)) / (dR / dd) ]
   where R(d) = I_u(d) / [ I_u(d) + I_s(d) ] is the normalized stopped-peak intensity ratio.

3. Plateau Region Arbitration & B(E2) Inversion:
   In the sensitive flight domain (0.15 <= R(d) <= 0.85), tau(d) forms a flat horizontal plateau
   strictly independent of feeding delays.
   For a valid input plateau, the weighted mean lifetime can be transformed into
   conditional derived quantities:
     - Transition rate: T(E2) = 1.0 / tau_mean  [s^-1];
     - Derived reduced transition probability:
         B(E2; I -> I-2) = [ 1 / (1.225e9 * E_gamma^5 * tau_mean_s) ]  [e^2 * b^2];
     - Derived intrinsic quadrupole moment Q_0:
         Q_0 = sqrt[ (16*pi / 5) * B(E2) / <I 2 K 0 | I-2, K>^2 ].
"""

import sys
import json
import math
import argparse
import numpy as np
from scipy.interpolate import UnivariateSpline


PRESETS = {
    "134Ce_2plus_rdds_plunger": {
        "description": "synthetic_ddcm_demo: 134Ce-like 2+_1 -> 0+ fixture; counts are hand-constructed, not measured",
        "data_kind": "synthetic_ddcm_demo",
        "nucleus": "134Ce",
        "E_gamma_keV": 409.0,
        "beta_recoil": 0.0210,
        "spin_initial": 2.0,
        "K_quantum": 0.0,
        "measurements": [
            {"d_um": 12.0, "stopped_counts": 2100.0, "shifted_counts": 18200.0},
            {"d_um": 25.0, "stopped_counts": 4350.0, "shifted_counts": 16100.0},
            {"d_um": 50.0, "stopped_counts": 7900.0, "shifted_counts": 12400.0},
            {"d_um": 80.0, "stopped_counts": 11500.0, "shifted_counts": 8800.0},
            {"d_um": 120.0, "stopped_counts": 14900.0, "shifted_counts": 5400.0},
            {"d_um": 180.0, "stopped_counts": 17800.0, "shifted_counts": 2600.0},
            {"d_um": 250.0, "stopped_counts": 19400.0, "shifted_counts": 1050.0},
            {"d_um": 350.0, "stopped_counts": 20100.0, "shifted_counts": 350.0}
        ]
    },
    "128Cs_chiral_bandhead_lifetime": {
        "description": "synthetic_ddcm_demo: 128Cs-like 9+ fixture; counts are hand-constructed, not measured",
        "data_kind": "synthetic_ddcm_demo",
        "nucleus": "128Cs",
        "E_gamma_keV": 280.0,
        "beta_recoil": 0.0185,
        "spin_initial": 9.0,
        "K_quantum": 0.0,
        "measurements": [
            {"d_um": 5.0, "stopped_counts": 3100.0, "shifted_counts": 16500.0},
            {"d_um": 15.0, "stopped_counts": 7800.0, "shifted_counts": 11800.0},
            {"d_um": 30.0, "stopped_counts": 13200.0, "shifted_counts": 6500.0},
            {"d_um": 50.0, "stopped_counts": 16900.0, "shifted_counts": 2800.0},
            {"d_um": 80.0, "stopped_counts": 18900.0, "shifted_counts": 800.0},
            {"d_um": 120.0, "stopped_counts": 19500.0, "shifted_counts": 200.0}
        ]
    },
    "rapid_decay_short_lifetime_limit": {
        "description": "synthetic_ddcm_demo: short-lived-state fixture; counts are hand-constructed, not measured",
        "data_kind": "synthetic_ddcm_demo",
        "nucleus": "Fast-Decay-Nuclide",
        "E_gamma_keV": 850.0,
        "beta_recoil": 0.0250,
        "spin_initial": 4.0,
        "K_quantum": 0.0,
        "measurements": [
            {"d_um": 4.0, "stopped_counts": 4500.0, "shifted_counts": 15000.0},
            {"d_um": 10.0, "stopped_counts": 9800.0, "shifted_counts": 9800.0},
            {"d_um": 20.0, "stopped_counts": 15500.0, "shifted_counts": 4100.0},
            {"d_um": 35.0, "stopped_counts": 18400.0, "shifted_counts": 1200.0},
            {"d_um": 60.0, "stopped_counts": 19400.0, "shifted_counts": 250.0}
        ]
    }
}


def evaluate_ddcm_curve(measurements, beta_recoil):
    """
    Calculates normalized stopped ratios R(d), numerical derivative dR/dd,
    and pointwise lifetime tau(d).
    """
    # Recoil speed: v = beta * c = beta * 299.792 um/ps
    v_um_per_ps = beta_recoil * 299.792458

    d_arr = np.array([m["d_um"] for m in measurements], dtype=float)
    u_arr = np.array([m["stopped_counts"] for m in measurements], dtype=float)
    s_arr = np.array([m["shifted_counts"] for m in measurements], dtype=float)

    tot_arr = u_arr + s_arr
    R_arr = u_arr / np.maximum(1.0, tot_arr)

    # Statistical uncertainty on R: sigma_R = sqrt( u*s^2 + s*u^2 ) / tot^2
    sig_u = np.sqrt(np.maximum(1.0, u_arr))
    sig_s = np.sqrt(np.maximum(1.0, s_arr))
    sig_R = np.sqrt((s_arr**2) * (sig_u**2) + (u_arr**2) * (sig_s**2)) / np.maximum(1.0, tot_arr**2)

    # Smooth spline interpolation for derivative dR / dd
    # Adaptive degree spline (deg = min(3, m - 1))
    deg = min(3, len(d_arr) - 1)
    if deg >= 1:
        spline = UnivariateSpline(d_arr, R_arr, w=1.0/np.maximum(1e-4, sig_R), k=deg, s=len(d_arr))
        dR_dd = spline.derivative()(d_arr)
    else:
        dR_dd = np.gradient(R_arr, d_arr)
    dR_dd = np.maximum(1e-6, dR_dd)

    # Pointwise lifetime: tau(d) = [ (1 - R(d)) / (dR/dd) ] / v
    tau_d_ps = ((1.0 - R_arr) / dR_dd) / v_um_per_ps
    sig_tau_ps = (sig_R / (dR_dd * v_um_per_ps))

    points_res = []
    for i in range(len(d_arr)):
        in_plateau = bool(0.12 <= R_arr[i] <= 0.88)
        points_res.append({
            "d_um": float(d_arr[i]),
            "stopped_counts": float(u_arr[i]),
            "shifted_counts": float(s_arr[i]),
            "R_ratio": float(R_arr[i]),
            "sigma_R": float(sig_R[i]),
            "dR_dd_per_um": float(dR_dd[i]),
            "tau_ps": float(tau_d_ps[i]),
            "sigma_tau_ps": float(sig_tau_ps[i]),
            "is_in_plateau": in_plateau
        })

    return points_res, v_um_per_ps


def extract_plateau_lifetime_and_be2(
    points_res,
    v_um_per_ps,
    E_gamma_keV,
    spin_I,
    K_val,
    data_kind="synthetic_ddcm_demo",
):
    """
    Extracts a derived lifetime and conditional B(E2)/Q0 quantities.
    """
    plateau_pts = [p for p in points_res if p["is_in_plateau"] and p["tau_ps"] > 0]
    if not plateau_pts:
        return {
            "status": "not-ready",
            "data_kind": data_kind,
            "reason": "No valid DDCM plateau points were found; derived lifetime and transition quantities are withheld.",
            "plateau_points_count": 0,
            "mean_lifetime_tau_ps": None,
            "sigma_tau_ps": None,
            "transition_rate_per_s": None,
            "B_E2_e2b2": None,
            "B_E2_W_u": None,
            "intrinsic_quadrupole_moment_Q0_eb": None,
        }

    taus = np.array([p["tau_ps"] for p in plateau_pts])
    weights = 1.0 / np.maximum(1e-3, np.array([p["sigma_tau_ps"] for p in plateau_pts]))**2

    tau_mean_ps = float(np.sum(taus * weights) / np.sum(weights))
    sigma_tau_mean = float(math.sqrt(1.0 / np.sum(weights)))

    # Transition rate: T(E2) = 1.0 / tau (s^-1)
    tau_mean_s = tau_mean_ps * 1e-12
    trans_rate_s_minus1 = 1.0 / max(1e-18, tau_mean_s)

    # B(E2) calculation: T(E2) = 1.225e13 * E_MeV^5 * B(E2)_e2b2 (1 b^2 = 10^4 fm^4)
    E_MeV = max(0.01, E_gamma_keV / 1000.0)
    denom_e2 = 1.225e13 * (E_MeV**5) * tau_mean_s
    B_E2_e2b2 = (1.0 / max(1e-12, denom_e2)) if denom_e2 > 0 else 0.0

    # Weisskopf single-particle unit: B(E2)_sp ~ 0.00386 e^2 b^2 for A ~ 130
    b_e2_wu = B_E2_e2b2 / 0.00386

    # Intrinsic quadrupole moment Q0: B(E2; I -> I-2) = (5/16pi) * e^2 * Q0^2 * <I 2 K 0 | I-2, K>^2
    # Clebsch-Gordan coefficient for 2+ -> 0+: <2 2 0 0 | 0 0> = 1.0 / sqrt(5)
    # So for 2 -> 0: B(E2) = (1/16pi) * e^2 * Q0^2 => Q0 = sqrt( 16pi * B(E2) )
    cg_sq = 0.20 if spin_I <= 2.0 else 0.35
    q0_val = math.sqrt(max(0.0, (16.0 * math.pi / 5.0) * (B_E2_e2b2 / max(1e-4, cg_sq))))

    return {
        "status": "derived-from-synthetic-counts" if data_kind == "synthetic_ddcm_demo" else "derived-from-input",
        "data_kind": data_kind,
        "plateau_points_count": len(plateau_pts),
        "mean_lifetime_tau_ps": tau_mean_ps,
        "sigma_tau_ps": sigma_tau_mean,
        "recoil_velocity_v_um_per_ps": float(v_um_per_ps),
        "transition_rate_per_s": float(trans_rate_s_minus1),
        "B_E2_e2b2": float(B_E2_e2b2),
        "B_E2_W_u": float(b_e2_wu),
        "intrinsic_quadrupole_moment_Q0_eb": float(q0_val)
    }


def run_rdds_ddcm_analysis(
    nucleus,
    E_gamma_keV,
    beta_recoil,
    spin_I,
    K_val,
    measurements,
    data_kind="synthetic_ddcm_demo",
):
    """
    Complete execution pipeline for in-beam RDDS DDCM lifetime analysis.
    """
    pts, v_um = evaluate_ddcm_curve(measurements, beta_recoil)
    plateau_res = extract_plateau_lifetime_and_be2(
        pts,
        v_um,
        E_gamma_keV,
        spin_I,
        K_val,
        data_kind=data_kind,
    )

    return {
        "nucleus": nucleus,
        "recoil_parameters": {
            "beta_recoil": float(beta_recoil),
            "velocity_um_per_ps": float(v_um),
            "E_gamma_keV": float(E_gamma_keV),
            "spin_initial": float(spin_I)
        },
        "data_kind": data_kind,
        "evidence_boundary": [
            "Preset counts are synthetic unless an external raw-data manifest is supplied.",
            "Returned lifetime and transition quantities are derived outputs.",
            "No paper-level claim is made without peak fits, gates, response, feeding, and covariance."
        ],
        "ddcm_points": pts,
        "plateau_results": plateau_res
    }


def format_text_report(res, title="In-Beam RDDS Differential Decay Curve Method (DDCM) Inverter"):
    nuc = res["nucleus"]
    rp = res["recoil_parameters"]
    pl = res["plateau_results"]
    pts = res["ddcm_points"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | E_gamma = {rp['E_gamma_keV']:.1f} keV | Recoil beta = {rp['beta_recoil']:.4f} (v = {rp['velocity_um_per_ps']:.3f} um/ps)")
    lines.append("=" * 76)
    lines.append("Plunger Distance Grid & DDCM Differential Analysis:")
    lines.append("  d (um)   Stopped (u)   Shifted (s)   Ratio R(d)    dR/dd (1/um)   tau(d) (ps)    Plateau?")
    for p in pts:
        tag = "YES" if p["is_in_plateau"] else "No"
        lines.append(f"   {p['d_um']:5.1f}     {p['stopped_counts']:7.0f}       {p['shifted_counts']:7.0f}       {p['R_ratio']:5.3f}         {p['dR_dd_per_um']:6.4f}      {p['tau_ps']:6.2f} +- {p['sigma_tau_ps']:4.2f}    {tag}")
    lines.append("-" * 76)
    if pl.get("status") == "not-ready":
        lines.append("DDCM STATUS: not-ready")
        lines.append(f"  Reason: {pl['reason']}")
        lines.append("=" * 76)
        return "\n".join(lines)

    lines.append(f"Derived DDCM quantities ({pl.get('status', 'derived-from-input')}):")
    lines.append(f"  Nuclear Level Lifetime tau      : {pl['mean_lifetime_tau_ps']:.2f} +- {pl['sigma_tau_ps']:.2f} ps  ({pl['plateau_points_count']} plateau distances)")
    lines.append(f"  Derived Transition Rate T(E2)  : {pl['transition_rate_per_s']:10.3e} s^-1")
    lines.append(f"  Derived B(E2)                  : {pl['B_E2_e2b2']:.4f} e^2 b^2  (~ {pl['B_E2_W_u']:.1f} W.u.)")
    lines.append(f"  Derived Quadrupole Moment Q_0  : {pl['intrinsic_quadrupole_moment_Q0_eb']:.2f} e b")
    lines.append("-" * 76)
    lines.append("Evidence boundary: DDCM formalism does not remove the need for valid gates,")
    lines.append("response, feeding, stopping, distance, and covariance checks.")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Synthetic RDDS/DDCM differential decay curve demonstration."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load synthetic DDCM demonstration preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nuc = p["nucleus"]
        eg = p["E_gamma_keV"]
        beta = p["beta_recoil"]
        spin = p["spin_initial"]
        k_q = p["K_quantum"]
        meas = p["measurements"]
        data_kind = p.get("data_kind", "synthetic_ddcm_demo")
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_rdds_ddcm_analysis(
        nucleus=nuc,
        E_gamma_keV=eg,
        beta_recoil=beta,
        spin_I=spin,
        K_val=k_q,
        measurements=meas,
        data_kind=data_kind,
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
