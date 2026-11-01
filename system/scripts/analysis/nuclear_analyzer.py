#!/usr/bin/env python3
"""
Nuclear Physics Experimental Data Analysis Suite (CLI & Library).

A unified, zero-external-dependency (NumPy + SciPy only) nuclear spectroscopy toolkit.
Designed to run seamlessly across all lab devices, clusters, and offline computers.

Commands:
  kinematics  : Heavy-ion fusion kinematics, Coulomb barrier, recoil velocity, Doppler shift.
  angdist     : In-beam gamma-ray angular distribution fit (A0, a2, a4).
  dualroots   : Solve quadratic dual roots for multipole mixing ratio delta(E2/M1).
  trapezoid   : Digital pulse processing with Jordanov recursive trapezoidal filter.
  peakfit     : High-precision photopeak fit (Gaussian + Erfc Step + Linear Baseline).
  selftest    : Run complete suite of unit tests.
"""

import sys
import os
import argparse
import numpy as np

from heavy_ion_kinematics import calculate_kinematics, doppler_shift, doppler_broadening
from angular_distribution_solver import angular_distribution_model, fit_angular_distribution, solve_delta_dual_roots
from digital_trapezoidal_filter import synthesize_preamp_pulse, apply_trapezoidal_filter, extract_trapezoid_amplitude
from gamma_peak_fitting import single_peak_model, fit_single_gamma_peak
from dco_polarization_analyzer import joint_dco_polarization_fit, calculate_dco_ratio, calculate_linear_polarization
from lifetime_lineshape_calculator import calculate_stopping_time_alpha, dsam_invert_lifetime, calculate_absolute_transition_strengths
from routhian_alignment_analyzer import calculate_alignment_and_routhians, fit_harris_reference
from ensdf_crosswalk_parser import parse_ensdf_records, crosswalk_match


def cmd_kinematics(args):
    res = calculate_kinematics(args.Ap, args.Zp, args.At, args.Zt, args.Elab, args.dE)
    print("\n=======================================================")
    print(f" Heavy-Ion Fusion Kinematics: {args.Ap}X({args.Zp}) + {args.At}Y({args.Zt})")
    print("=======================================================")
    print(f"  Beam Energy (Lab)       : {res['Elab_MeV']:.2f} MeV")
    print(f"  Center-of-Mass Energy   : {res['E_cm_MeV']:.2f} MeV")
    print(f"  Bass Interaction Radius : {res['R_B_fm']:.3f} fm")
    print(f"  Coulomb Barrier (V_B)   : {res['V_B_MeV']:.2f} MeV")
    print(f"  E_cm / V_B Ratio        : {res['E_cm_over_VB']:.3f}")
    print(f"  Grazing Ang. Momentum   : {res['l_max_hbar']:.1f} hbar")
    print(f"  Total Fusion Cross Sec  : {res['sigma_fus_mb']:.1f} mb")
    print(f"  Recoil Velocity (beta)  : {res['beta_v_over_c']:.4f} ({res['recoil_velocity_percent_c']:.2f}% of c)")
    print("=======================================================")
    if args.Egamma:
        print(f"\nDoppler Shift for E_gamma = {args.Egamma:.1f} keV:")
        for th in [30, 45, 90, 135, 150]:
            shifted = doppler_shift(args.Egamma, res['beta_v_over_c'], th)
            dE = doppler_broadening(args.Egamma, res['beta_v_over_c'], th, args.opening_angle)
            print(f"  Theta = {th:3d} deg : E_shift = {shifted:8.2f} keV ({shifted-args.Egamma:+6.2f} keV), Broadening = {dE:5.2f} keV")


def cmd_dualroots(args):
    roots = solve_delta_dual_roots(args.a2, args.F11, args.F12, args.F22, alpha2=args.alpha2)
    print("\n=======================================================")
    print(f" Multipole Mixing Ratio delta Dual-Root Solution")
    print("=======================================================")
    print(f"  Experimental a2         : {args.a2:+.4f}")
    print(f"  Orientation alpha2      : {args.alpha2:.4f}")
    print(f"  F-coefficients (11,12,22): {args.F11:.4f}, {args.F12:.4f}, {args.F22:.4f}")
    if roots is None:
        print("  Status: No real roots exist for this a2 (unphysical or bad calibration).")
    else:
        d1 = roots["delta_small_root (M1 dominated)"]
        d2 = roots["delta_large_root (E2 dominated)"]
        e2_pct1 = 100.0 * (d1**2) / (1.0 + d1**2)
        e2_pct2 = 100.0 * (d2**2) / (1.0 + d2**2)
        print(f"  Root 1 (M1 dominated)   : delta = {d1:+.4f} (E2 fraction: {e2_pct1:.1f}%, M1 fraction: {100-e2_pct1:.1f}%)")
        print(f"  Root 2 (E2 dominated)   : delta = {d2:+.4f} (E2 fraction: {e2_pct2:.1f}%, M1 fraction: {100-e2_pct2:.1f}%)")
        print("\n  [EXPERT NOTICE]")
        print("  Both roots yield the EXACT SAME a2 value!")
        print("  Do NOT select Root 2 (wobbling) without independent Linear Polarization (P) measurement!")
    print("=======================================================")


def cmd_dco(args):
    res = joint_dco_polarization_fit(
        R_dco_exp=args.Rdco, R_dco_err=args.Rdco_err,
        P_exp=args.P, P_err=args.P_err,
        theta1_deg=args.th1, theta2_deg=args.th2, theta_pol_deg=args.th_pol,
        F2_11=args.F11, F2_12=args.F12, F2_22=args.F22, F4_22=args.F44,
        alpha2=args.alpha2
    )
    print("\n=======================================================")
    print(" Joint DCO Ratio & Linear Polarization Fit")
    print("=======================================================")
    print(f"  Input Exp R_DCO         : {args.Rdco:.3f} +/- {args.Rdco_err:.3f} (angles: {args.th1:.0f}/{args.th2:.0f} deg)")
    print(f"  Input Exp Polarization  : {args.P:+.3f} +/- {args.P_err:.3f} (at {args.th_pol:.0f} deg)")
    print(f"  Best-fit delta          : {res['best_delta']:+.4f} (+{res['delta_err_high']:.4f} / -{res['delta_err_low']:.4f})")
    print(f"  Model R_DCO at best-fit : {res['r_dco_theo']:.3f}")
    print(f"  Model Pol P at best-fit : {res['p_theo']:+.3f}")
    print(f"  Minimum Chi2            : {res['min_chi2']:.2f}")
    print("=======================================================")


def cmd_lifetime(args):
    alpha = calculate_stopping_time_alpha(args.A, args.Z, args.beta, args.stopper)
    print("\n=======================================================")
    print(f" Nuclear Excited-State Lifetime & DSAM Analysis")
    print("=======================================================")
    print(f"  Recoil Nucleus          : A={args.A}, Z={args.Z} (beta={args.beta:.4f})")
    print(f"  Stopper Material        : {args.stopper} (slowing-down time alpha = {alpha:.3f} ps)")
    if args.F is not None:
        tau = dsam_invert_lifetime(args.F, alpha)
        print(f"  Measured Attenuation F  : {args.F:.3f}")
        print(f"  Inverted Lifetime tau   : {tau:.3f} ps ({tau*1000.0:.1f} fs, T_1/2 = {tau*0.693147*1000.0:.1f} fs)")
    else:
        tau = args.tau
        print(f"  Input Lifetime tau      : {tau:.3f} ps")

    if args.Egamma:
        strengths = calculate_absolute_transition_strengths(
            tau_ps=tau, E_gamma_keV=args.Egamma, delta=args.delta,
            I_initial=args.I, branching_ratio=args.br
        )
        print("-------------------------------------------------------")
        print(f"  Gamma Transition Energy : {args.Egamma:.1f} keV (br = {args.br:.2f}, delta = {args.delta:+.2f})")
        print(f"  Absolute B(E2)          : {strengths['B_E2_e2b2']:.4f} e^2 b^2 ({strengths['B_E2_W_u']:.1f} W.u.)")
        print(f"  Absolute B(M1)          : {strengths['B_M1_muN2']:.4f} mu_N^2 ({strengths['B_M1_W_u']:.3f} W.u.)")
        print(f"  Intrinsic Quadrupole Qt : {strengths['Qt_eb']:.2f} e b")
    print("=======================================================")


def cmd_align(args):
    spins = [float(x.strip()) for x in args.spins.split(",")]
    energies = [float(x.strip()) for x in args.energies.split(",")]
    if len(spins) != len(energies):
        raise ValueError("Number of spins must equal number of energies.")

    res = calculate_alignment_and_routhians(spins, energies, J0=args.J0, J1=args.J1, K=args.K)
    print("\n=======================================================")
    print(" Nuclear Rotational Alignment & Routhian Analysis")
    print("=======================================================")
    print(f"  Harris Reference Core   : J0 = {args.J0:.1f} hbar^2/MeV, J1 = {args.J1:.1f} hbar^4/MeV^3, K = {args.K:.1f}")
    print("  Spin (hbar) | hbar*omega (MeV) | Alignment i_x (hbar) | e' (MeV)")
    print("  --------------------------------------------------------------")
    for sp, w, ix, ep in zip(res["spin_mid"], res["omega_MeV"], res["ix_hbar"], res["eprime_MeV"]):
        print(f"    {sp:5.1f}     |     {w:.4f}     |      {ix:+6.2f}        |  {ep:+.3f}")
    if res["critical_omega_crossing"]:
        print(f"\n  [BAND CROSSING DETECTED]")
        print(f"  Critical Frequency omega_c approx {res['critical_omega_crossing']:.3f} MeV/hbar")
        print(f"  Alignment Gain Delta(i_x) approx {res['alignment_gain']:.1f} hbar")
    print("=======================================================")


def cmd_ensdf(args):
    with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    levels = parse_ensdf_records(content)
    print("\n=======================================================")
    print(f" NNDC ENSDF Dataset Parser: {args.file}")
    print("=======================================================")
    print(f"  Successfully parsed {len(levels)} levels.")
    total_gammas = sum(len(l["gammas"]) for l in levels)
    print(f"  Total gamma transitions : {total_gammas}")

    if args.peaks:
        meas_peaks = [float(x.strip()) for x in args.peaks.split(",")]
        cw = crosswalk_match(meas_peaks, levels, tolerance_keV=args.tol)
        print(f"\n  Crosswalk Matched Known Transitions ({len(cw['matched'])}):")
        for m in cw["matched"]:
            print(f"    Exp {m['exp_energy_keV']:6.1f} keV <-> ENSDF {m['ensdf_energy_keV']:6.1f} keV (diff: {m['diff_keV']:+4.1f} keV), J_pi = {m['parent_jpi']}, Mult = {m['mult']}")
        print(f"\n  Unmatched New Transitions ({len(cw['unmatched_new_candidates'])}):")
        for u in cw["unmatched_new_candidates"]:
            print(f"    Candidate new peak: {u:6.1f} keV")
    print("=======================================================")


def cmd_selftest(args):
    print("\nExecuting comprehensive test suite...")
    ret = os.system(f"{sys.executable} system/scripts/analysis/test_analysis_suite.py")
    if ret != 0:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Nuclear Physics Spectroscopy Analysis Suite")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Kinematics
    p_kin = subparsers.add_parser("kinematics", help="Heavy-ion fusion kinematics")
    p_kin.add_argument("--Ap", type=int, required=True, help="Projectile mass number")
    p_kin.add_argument("--Zp", type=int, required=True, help="Projectile charge number")
    p_kin.add_argument("--At", type=int, required=True, help="Target mass number")
    p_kin.add_argument("--Zt", type=int, required=True, help="Target charge number")
    p_kin.add_argument("--Elab", type=float, required=True, help="Lab beam energy (MeV)")
    p_kin.add_argument("--dE", type=float, default=0.0, help="Target energy loss (MeV)")
    p_kin.add_argument("--Egamma", type=float, default=1000.0, help="Gamma energy for Doppler test (keV)")
    p_kin.add_argument("--opening_angle", type=float, default=8.0, help="Detector half-opening angle (deg)")
    p_kin.set_defaults(func=cmd_kinematics)

    # Dual roots
    p_dual = subparsers.add_parser("dualroots", help="Solve delta dual roots")
    p_dual.add_argument("--a2", type=float, required=True, help="Fitted a2 coefficient")
    p_dual.add_argument("--F11", type=float, required=True, help="F2(L=1, L=1)")
    p_dual.add_argument("--F12", type=float, required=True, help="F2(L=1, L=2)")
    p_dual.add_argument("--F22", type=float, required=True, help="F2(L=2, L=2)")
    p_dual.add_argument("--alpha2", type=float, default=1.0, help="Orientation parameter B2/B0")
    p_dual.set_defaults(func=cmd_dualroots)

    # DCO & Polarization
    p_dco = subparsers.add_parser("dco", help="Joint DCO ratio and linear polarization fit")
    p_dco.add_argument("--Rdco", type=float, required=True, help="Measured DCO ratio")
    p_dco.add_argument("--Rdco_err", type=float, default=0.05, help="DCO ratio error")
    p_dco.add_argument("--P", type=float, required=True, help="Measured linear polarization degree")
    p_dco.add_argument("--P_err", type=float, default=0.05, help="Polarization error")
    p_dco.add_argument("--th1", type=float, default=30.0, help="Detector 1 angle (deg)")
    p_dco.add_argument("--th2", type=float, default=90.0, help="Detector 2 angle (deg)")
    p_dco.add_argument("--th_pol", type=float, default=90.0, help="Polarimeter angle (deg)")
    p_dco.add_argument("--F11", type=float, required=True, help="F2(11)")
    p_dco.add_argument("--F12", type=float, required=True, help="F2(12)")
    p_dco.add_argument("--F22", type=float, required=True, help="F2(22)")
    p_dco.add_argument("--F44", type=float, default=0.0, help="F4(22)")
    p_dco.add_argument("--alpha2", type=float, default=0.85, help="Alignment parameter")
    p_dco.set_defaults(func=cmd_dco)

    # Lifetime & DSAM
    p_life = subparsers.add_parser("lifetime", help="Excited state lifetime and DSAM stopping analysis")
    p_life.add_argument("--A", type=int, default=131, help="Recoil mass number")
    p_life.add_argument("--Z", type=int, default=58, help="Recoil atomic number")
    p_life.add_argument("--beta", type=float, default=0.025, help="Initial recoil velocity v/c")
    p_life.add_argument("--stopper", type=str, default="Au", help="Stopper foil material (Au, Pb, Ta)")
    p_life.add_argument("--F", type=float, default=None, help="Measured DSAM attenuation factor F(tau)")
    p_life.add_argument("--tau", type=float, default=1.0, help="Lifetime tau in ps (if F is not provided)")
    p_life.add_argument("--Egamma", type=float, default=None, help="Gamma energy (keV)")
    p_life.add_argument("--delta", type=float, default=100.0, help="Mixing ratio delta (E2/M1)")
    p_life.add_argument("--I", type=float, default=10.0, help="Initial state spin")
    p_life.add_argument("--br", type=float, default=1.0, help="Gamma branching ratio")
    p_life.set_defaults(func=cmd_lifetime)

    # Rotational Alignment & Routhian
    p_align = subparsers.add_parser("align", help="Rotational frequency, alignment i_x, and Routhians")
    p_align.add_argument("--spins", type=str, required=True, help="Comma-separated list of spins (e.g. 5.5,7.5,9.5,11.5)")
    p_align.add_argument("--energies", type=str, required=True, help="Comma-separated list of energies in keV (e.g. 0,350,800,1350)")
    p_align.add_argument("--J0", type=float, default=15.0, help="Harris core parameter J0")
    p_align.add_argument("--J1", type=float, default=30.0, help="Harris core parameter J1")
    p_align.add_argument("--K", type=float, default=0.0, help="K quantum number")
    p_align.set_defaults(func=cmd_align)

    # ENSDF Crosswalk
    p_ensdf = subparsers.add_parser("ensdf", help="Parse ENSDF file and crosswalk match experimental gamma peaks")
    p_ensdf.add_argument("--file", type=str, required=True, help="Path to ENSDF text file")
    p_ensdf.add_argument("--peaks", type=str, default="", help="Comma-separated experimental peak energies in keV")
    p_ensdf.add_argument("--tol", type=float, default=1.0, help="Energy matching tolerance (keV)")
    p_ensdf.set_defaults(func=cmd_ensdf)

    # Selftest
    p_test = subparsers.add_parser("selftest", help="Run regression test suite")
    p_test.set_defaults(func=cmd_selftest)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
