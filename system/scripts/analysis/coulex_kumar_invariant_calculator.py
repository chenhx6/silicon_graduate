#!/usr/bin/env python3
"""
Coulomb Excitation (Coulex) Kinematics & Kumar Quadrupole Invariant Calculator.

Based on:
  - K. Alder & A. Winther, "Electromagnetic Excitation", North-Holland (1975)
  - K. Kumar, Phys. Rev. Lett. 28, 249 (1972) (Quadrupole invariant formulation)
  - D. Cline, Ann. Rev. Nucl. Part. Sci. 36, 683 (1986) (Coulex invariant analysis)

Features:
  1. Calculates Cline safe Coulomb excitation maximum beam energy E_safe (d_min >= Rp + Rt + 5 fm).
  2. Extracts static quadrupole moment Q_s(2_1^+) from diagonal E2 matrix element.
  3. Inverts model-independent Kumar quadrupole invariants Q^2, cos(3*delta), and effective triaxial angle gamma_eff.
"""

import numpy as np


def calculate_safe_coulex_energy(Ap, Zp, At, Zt, d_safe_fm=5.0):
    """
    Calculate maximum safe laboratory beam energy (MeV) for Coulomb excitation.
    Cline criterion: minimum distance of closest approach d_min >= R_p + R_t + d_safe
    where R = 1.25 * A^(1/3) fm.
    """
    Rp = 1.25 * (Ap**(1.0/3.0))
    Rt = 1.25 * (At**(1.0/3.0))
    d_min = Rp + Rt + d_safe_fm
    
    # Head-on collision distance: d_min = 1.44 * (Zp * Zt) / E_cm
    E_cm_safe = 1.439965 * (Zp * Zt) / d_min
    E_lab_safe = E_cm_safe * (Ap + At) / At
    
    return {
        "d_min_fm": d_min,
        "E_cm_safe_MeV": E_cm_safe,
        "E_lab_safe_MeV": E_lab_safe
    }


def reorientation_static_quadrupole(Z_target, A_target, M22_diagonal_eb):
    """
    Calculate static electric quadrupole moment Q_s(2_1^+) in e*b from diagonal matrix element <2||M(E2)||2>.
    Q_s(2_1^+) = sqrt(16*pi / 5) * (C_{2 2 2 0}^{2 2} / sqrt(5)) * <2||M(E2)||2>
    C_{2 2 2 0}^{2 2} = sqrt(4/7) approx 0.755929
    Q_s = sqrt(16*pi / 35) * <2||M(E2)||2> approx 0.7579 * <2||M(E2)||2>
    """
    c_factor = np.sqrt(16.0 * np.pi / 35.0)
    Q_s_eb = c_factor * M22_diagonal_eb
    
    if Q_s_eb < -0.05:
        shape_str = "Prolate (Well-deformed elongated ellipsoid)"
    elif Q_s_eb > 0.05:
        shape_str = "Oblate (Flattened disc-like ellipsoid)"
    else:
        shape_str = "Near-zero / Triaxial (gamma approx 30 deg or spherical)"
        
    return {
        "Q_s_eb": Q_s_eb,
        "M22_eb": M22_diagonal_eb,
        "shape_polarity": shape_str
    }


def calculate_kumar_invariants(M02_list_eb, M22_diag_eb, Z, A):
    """
    Calculate Kumar quadrupole invariants:
      q2 = sum_i <0||M(E2)||2_i>^2
      q3 = -sqrt(35/2) * [M(E2) x M(E2) x M(E2)]_0
      cos(3*delta) = q3 / (q2)^(3/2)
    """
    m02_arr = np.array(M02_list_eb, dtype=float)
    
    # Second-order invariant q2 = Q^2 (e^2 b^2)
    q2 = np.sum(m02_arr**2)
    
    # Third-order invariant approximation (dominated by first 2_1^+ intermediate state)
    # q3 approx -(sqrt(7/10)) * <0||M(E2)||2_1>^2 * <2_1||M(E2)||2_1>
    m02_1 = m02_arr[0] if len(m02_arr) > 0 else 0.0
    q3 = -np.sqrt(7.0 / 10.0) * (m02_1**2) * M22_diag_eb
    
    # cos(3*delta)
    denom = (max(1e-6, q2))**1.5
    cos_3delta = np.clip(q3 / denom, -1.0, 1.0)
    
    delta_rad = (1.0 / 3.0) * np.arccos(cos_3delta)
    gamma_eff_deg = np.degrees(delta_rad)
    
    # Convert Q^2 to effective beta2 rms deformation
    # Q = (3 / 4*pi) * Z * R0^2 * beta
    R0_fm = 1.2 * (A**(1.0/3.0))
    # R0^2 in b (1 fm^2 = 0.01 b)
    R02_b = (R0_fm**2) * 0.01
    charge_factor = (3.0 * Z / (4.0 * np.pi)) * R02_b
    
    beta_eff = np.sqrt(q2) / max(1e-4, charge_factor)
    
    return {
        "q2_invariant_e2b2": q2,
        "q3_invariant_e3b3": q3,
        "cos_3delta": cos_3delta,
        "gamma_eff_deg": gamma_eff_deg,
        "beta_eff_rms": beta_eff
    }


if __name__ == "__main__":
    print("=== Benchmark: Coulex Kinematics & Kumar Invariant Inversion ===")
    # Safe Coulex test: 130Ba on 208Pb target
    safe = calculate_safe_coulex_energy(Ap=130, Zp=56, At=208, Zt=82)
    print(f"  130Ba + 208Pb Safe Coulomb Energy : E_lab_safe = {safe['E_lab_safe_MeV']:.1f} MeV (E_cm = {safe['E_cm_safe_MeV']:.1f} MeV)")
    
    # Typical Coulex measurements in 130Ba:
    # <0||M(E2)||2_1> = 1.15 e*b, <0||M(E2)||2_2> = 0.35 e*b
    # Diagonal reorientation <2_1||M(E2)||2_1> = -0.55 e*b (prolate-triaxial)
    M02 = [1.15, 0.35]
    M22 = -0.55
    
    reorient = reorientation_static_quadrupole(56, 130, M22)
    print(f"\n  Reorientation Static Quadrupole Q_s : {reorient['Q_s_eb']:+.3f} e*b")
    print(f"  Polarity Classification             : {reorient['shape_polarity']}")
    
    invariants = calculate_kumar_invariants(M02, M22, Z=56, A=130)
    print("\n  Kumar Quadrupole Invariant Analysis:")
    print(f"    Second-Order Invariant Q^2   : {invariants['q2_invariant_e2b2']:.3f} e^2 b^2")
    print(f"    Third-Order Invariant q3     : {invariants['q3_invariant_e3b3']:+.3f} e^3 b^3")
    print(f"    Asymmetry Invariant cos(3*d) : {invariants['cos_3delta']:+.3f}")
    print(f"    Effective Triaxial Angle     : gamma_eff = {invariants['gamma_eff_deg']:.1f} deg")
    print(f"    Effective Quadrupole beta    : beta_eff  = {invariants['beta_eff_rms']:.3f}")
    print("  Outcome: Confirms robust non-zero triaxial deformation (gamma around 20-30 deg)!")
