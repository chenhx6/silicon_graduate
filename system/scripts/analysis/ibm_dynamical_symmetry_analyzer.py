#!/usr/bin/env python3
"""
Interacting Boson Model (IBM/IBFM) Dynamical Symmetry & Casten Triangle Phase Classifier.

Based on:
  - F. Iachello & A. Arima, "The Interacting Boson Model", Cambridge University Press (1987)
  - R. F. Casten, "Nuclear Structure from a Simple Perspective", Oxford University Press (2000)
  - K. Nomura et al., in "Chirality and Wobbling in Atomic Nuclei", CRC Press (2024), Chapter 11

Features:
  1. Calculates experimental energy ratios R4/2 = E(4_1)/E(2_1), R22 = E(2_2)/E(2_1), and R02 = E(0_2)/E(2_1).
  2. Classifies position within the Casten Triangle (U(5) Vibrator, SU(3) Rotor, O(6) gamma-soft).
  3. Diagnoses E(5) and X(5) critical point symmetries and O(6) gamma-unstable degeneracies.
"""

import numpy as np


def calculate_ibm_energy_ratios(E_2_1_keV, E_4_1_keV, E_0_2_keV=None, E_2_2_keV=None, E_3_1_keV=None):
    """
    Calculate key experimental diagnostic ratios for IBM dynamical symmetries.
    """
    if E_2_1_keV <= 0:
        raise ValueError("E(2_1+) energy must be strictly positive.")
        
    R42 = E_4_1_keV / E_2_1_keV
    R22 = (E_2_2_keV / E_2_1_keV) if E_2_2_keV is not None else None
    R02 = (E_0_2_keV / E_2_1_keV) if E_0_2_keV is not None else None
    
    # O(6) quasi-degeneracy between 4_1+ and 2_2+
    o6_deg_diff = abs(E_4_1_keV - E_2_2_keV) / E_2_1_keV if E_2_2_keV is not None else None
    
    return {
        "E_2_1_keV": E_2_1_keV,
        "E_4_1_keV": E_4_1_keV,
        "R42": R42,
        "R22": R22,
        "R02": R02,
        "O6_degeneracy_diff": o6_deg_diff
    }


def classify_casten_triangle_phase(R42, R22=None):
    """
    Classify collective phase within the Casten Triangle:
      - U(5) spherical harmonic vibrator : R42 approx 2.00, R22 approx 2.00
      - O(6) gamma-unstable soft rotor   : R42 approx 2.50, R22 approx 2.50
      - SU(3) axially-deformed rotor     : R42 approx 3.33, R22 >> 3.33 (gamma band pushed high)
      - E(5) critical point (U(5) - O(6)): R42 approx 2.20
      - X(5) critical point (U(5) - SU(3)): R42 approx 2.90
    """
    if R42 < 2.15:
        phase = "U(5) Spherical Harmonic Vibrator Limit"
        desc = "Equidistant phonon multiplet spectrum. R4/2 approx 2.0."
    elif 2.15 <= R42 < 2.30:
        phase = "E(5) Critical Point / U(5)-O(6) Transition"
        desc = "Second-order shape phase transition between spherical and gamma-soft."
    elif 2.30 <= R42 <= 2.65:
        if R22 is not None and abs(R22 - R42) < 0.25:
            phase = "O(6) gamma-Unstable Soft Rotor Limit"
            desc = "Flat potential in gamma. E(4_1) approx E(2_2). Typical of A approx 130 region!"
        else:
            phase = "Transitional gamma-Soft Nucleus"
            desc = "Moderately deformed nucleus with substantial gamma softness."
    elif 2.65 < R42 < 3.10:
        phase = "X(5) Critical Point / Transition to Deformed Rotor"
        desc = "First-order shape phase transition between spherical and prolate deformed."
    elif 3.10 <= R42 <= 3.35:
        phase = "SU(3) Axially-Symmetric Prolate Deformed Rotor"
        desc = "Well-developed rigid rotational band E propto I*(I+1). R4/2 approx 3.33."
    else:
        phase = "Superdeformed or Anomalous Non-collective Regime"
        desc = f"R4/2 = {R42:.2f} lies outside standard ground-band IBM limits."
        
    return {
        "phase_name": phase,
        "description": desc,
        "R42_value": R42
    }


if __name__ == "__main__":
    print("=== Benchmark: IBM Dynamical Symmetry & Casten Triangle Analyzer ===")
    # Test 130Ba: typical A approx 130 gamma-soft nucleus
    # 2_1+ = 357.2 keV, 4_1+ = 908.1 keV, 2_2+ = 901.7 keV (near degenerate with 4_1!)
    ba130_ratios = calculate_ibm_energy_ratios(E_2_1_keV=357.2, E_4_1_keV=908.1, E_2_2_keV=901.7)
    classification = classify_casten_triangle_phase(ba130_ratios["R42"], ba130_ratios["R22"])
    
    print("  130Ba Energy Ratio Diagnostics:")
    print(f"    R4/2 = E(4_1)/E(2_1) : {ba130_ratios['R42']:.3f} (O(6) limit is 2.50)")
    print(f"    R22  = E(2_2)/E(2_1) : {ba130_ratios['R22']:.3f}")
    print(f"    |E(4_1) - E(2_2)|   : {abs(908.1 - 901.7):.1f} keV (Remarkable O(6) degeneracy!)")
    print(f"    Classified Phase     : {classification['phase_name']}")
    print(f"    Interpretation       : {classification['description']}")
    print("  Outcome: Firmly establishes 130Ba core as an O(6) gamma-soft nucleus, providing micro-foundation for IBFM phonon-coupling!")
