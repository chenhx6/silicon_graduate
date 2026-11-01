#!/usr/bin/env python3
"""
Nuclear High-Spin Rotational Band Routhian & Alignment (i_x) Analyzer.

Based on:
  - R. Bengtsson & S. Frauendorf, Nucl. Phys. A 327, 139 (1979) (Cranking model Routhian)
  - S. M. Harris, Phys. Rev. 138, B509 (1965) (Harris reference parameterization)

Features:
  1. Automatic Harris reference core parameter (J0, J1) fitting from low-spin ground band.
  2. Calculates rotational frequency hbar*omega, aligned angular momentum i_x(omega), and experimental Routhians e'(omega).
  3. Automated detection of band crossing critical frequency omega_c and alignment gain Delta_ix (e.g. proton pair alignment).
"""

import numpy as np


def fit_harris_reference(spins, energies_keV, K=0.0):
    """
    Fit Harris reference core parameters J0 and J1 from low-spin band levels.
    J^(1) = I_x / omega = J0 + J1 * omega^2
    """
    I = np.array(spins, dtype=float)
    E = np.array(energies_keV, dtype=float) / 1000.0 # Convert to MeV
    
    # Calculate omega and Ix for Delta I = 2 transitions
    omegas = []
    Ix_list = []
    for idx in range(len(I) - 1):
        dI = I[idx+1] - I[idx]
        if abs(dI - 2.0) < 0.1: # Cascade E2
            E_gamma = E[idx+1] - E[idx]
            omega = E_gamma / 2.0
            # Midpoint spin
            I_mid = (I[idx+1] + I[idx]) / 2.0
            Ix = np.sqrt(max(0.0, (I_mid + 0.5)**2 - K**2))
            omegas.append(omega)
            Ix_list.append(Ix)
            
    omegas = np.array(omegas)
    Ix_list = np.array(Ix_list)
    
    if len(omegas) < 2:
        # Default typical A approx 130 core parameters
        return {"J0": 15.0, "J1": 30.0, "fitted": False}
        
    # Linear regression of (Ix / omega) vs omega^2
    y = Ix_list / omegas
    x = omegas**2
    slope, intercept = np.polyfit(x, y, 1)
    
    J0 = max(5.0, intercept)
    J1 = max(0.0, slope * 3.0) # In Harris convention J_core = J0 + J1*w^2
    return {"J0": J0, "J1": J1, "fitted": True}


def calculate_alignment_and_routhians(spins, energies_keV, J0=15.0, J1=30.0, K=0.0):
    """
    Calculate rotational frequency, alignment i_x, and experimental Routhians e'.
    
    Returns:
        dict containing arrays of omega (MeV/hbar), i_x (hbar), e_prime (MeV), and crossing diagnostics.
    """
    I = np.array(spins, dtype=float)
    E = np.array(energies_keV, dtype=float) / 1000.0 # MeV
    
    omega_arr = []
    ix_arr = []
    eprime_arr = []
    spin_mid_arr = []
    
    for idx in range(len(I) - 1):
        dI = I[idx+1] - I[idx]
        if abs(dI - 2.0) < 0.1: # Delta I = 2 cascade
            E_gamma = E[idx+1] - E[idx]
            omega = E_gamma / 2.0
            I_mid = (I[idx+1] + I[idx]) / 2.0
            Ix = np.sqrt(max(0.0, (I_mid + 0.5)**2 - K**2))
            
            # Harris reference angular momentum and energy
            # I_ref = J0*w + J1*w^3
            # E_ref = 0.5*J0*w^2 + 0.75*J1*w^4
            I_ref = J0 * omega + (1.0 / 3.0) * J1 * (omega**3)
            E_ref = 0.5 * J0 * (omega**2) + 0.25 * J1 * (omega**4)
            
            # Alignment i_x = I_x - I_ref
            i_x = Ix - I_ref
            
            # Experimental Routhian e' = E_mid - omega*Ix - E_ref
            E_mid = (E[idx+1] + E[idx]) / 2.0
            e_prime = E_mid - omega * Ix + E_ref
            
            omega_arr.append(omega)
            ix_arr.append(i_x)
            eprime_arr.append(e_prime)
            spin_mid_arr.append(I_mid)
            
    omega_arr = np.array(omega_arr)
    ix_arr = np.array(ix_arr)
    eprime_arr = np.array(eprime_arr)
    
    # Detect band crossing (sudden gain in i_x > 4.0 hbar)
    critical_omega = None
    delta_ix_gain = 0.0
    if len(ix_arr) >= 3:
        d_ix = np.diff(ix_arr)
        max_jump_idx = np.argmax(d_ix)
        if d_ix[max_jump_idx] > 3.0:
            critical_omega = omega_arr[max_jump_idx]
            delta_ix_gain = ix_arr[-1] - ix_arr[0]
            
    return {
        "omega_MeV": omega_arr,
        "ix_hbar": ix_arr,
        "eprime_MeV": eprime_arr,
        "spin_mid": np.array(spin_mid_arr),
        "critical_omega_crossing": critical_omega,
        "alignment_gain": delta_ix_gain
    }


if __name__ == "__main__":
    print("=== Benchmark: High-Spin Rotational Routhian & Alignment Analyzer ===")
    # Simulated 131Ce ground band crossing with (pi h11/2)^2 alignment around hbar*omega = 0.31 MeV
    # Spins: 11/2-, 15/2-, 19/2-, 23/2-, 27/2-, 31/2-, 35/2-, 39/2-
    test_spins = [5.5, 7.5, 9.5, 11.5, 13.5, 15.5, 17.5, 19.5]
    # Energies in keV showing clear backbending (frequency deceleration then re-acceleration)
    test_energies = [0.0, 350.0, 800.0, 1350.0, 1920.0, 2400.0, 2900.0, 3550.0]
    
    res = calculate_alignment_and_routhians(test_spins, test_energies, J0=15.0, J1=30.0, K=3.5)
    print("  Calculated Rotational Frequency & Alignment:")
    for w, ix, sp in zip(res["omega_MeV"], res["ix_hbar"], res["spin_mid"]):
        print(f"    Spin {sp:4.1f} hbar : hbar*omega = {w:.3f} MeV, i_x = {ix:+5.2f} hbar")
        
    if res["critical_omega_crossing"]:
        print(f"\n  Detected Band Crossing: omega_c approx {res['critical_omega_crossing']:.3f} MeV/hbar")
        print(f"  Alignment Gain Delta(i_x) approx {res['alignment_gain']:.1f} hbar (Signature of pair breaking!)")
