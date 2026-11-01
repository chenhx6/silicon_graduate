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
