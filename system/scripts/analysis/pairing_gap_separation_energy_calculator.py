#!/usr/bin/env python3
"""
Two-Neutron Separation Energy Systematics, Pairing Gaps & Shell Closure Analyzer.

Based on:
  - A. Bohr & B. R. Mottelson, Nuclear Structure Vol. I, Ch. 2 (Masses & Separation energies)
  - K. Heyde, Basic Ideas and Concepts in Nuclear Physics, Ch. 7 (Two-neutron separation energy & pairing)
  - M. Wang et al., Chin. Phys. C 45, 030003 (2021) (AME 2020 atomic mass evaluation)
  - M. Bender et al., Eur. Phys. J. A 8, 59 (2000) (Pairing gaps from nuclear mean-field)

Features:
  1. Computes two-neutron separation energy S_2n along isotopic chains from binding energies or mass excesses.
  2. Evaluates 3-point and 5-point odd-even staggering (OES) pairing gaps Delta_n^(3) and Delta_n^(5).
  3. Detects magic number shell closure drops delta_2n = S_2n(N_magic) - S_2n(N_magic + 2).
  4. Identifies shape phase transitions (e.g. N=88 -> 90) via anomalous S_2n slope flattening or inversion.
  5. Compares experimental pairing gaps with global empirical BCS baselines: Delta approx 12 / sqrt(A) MeV.
"""

import numpy as np

# Neutron mass excess in MeV (AME 2020)
MASS_EXCESS_NEUTRON_MEV = 8.071317


def calculate_s2n_series(N_list, binding_energies_MeV=None, mass_excesses_MeV=None):
    """
    Compute two-neutron separation energy series S_2n(N) = B(N) - B(N-2).
    Can accept either binding energies B(N) or mass excesses Delta(N).
    """
    N_arr = np.array(N_list, dtype=int)

    if binding_energies_MeV is not None:
        B_arr = np.array(binding_energies_MeV, dtype=float)
        # S_2n(N) = B(N) - B(N-2)
        s2n_res = []
        for i in range(len(N_arr)):
            n_val = N_arr[i]
            # Find N - 2
            idx_prev = np.where(N_arr == (n_val - 2))[0]
            if len(idx_prev) > 0:
                s2n = B_arr[i] - B_arr[idx_prev[0]]
                s2n_res.append({"N": int(n_val), "S_2n_MeV": float(s2n)})
        return s2n_res
    elif mass_excesses_MeV is not None:
        M_arr = np.array(mass_excesses_MeV, dtype=float)
        # S_2n(N) = M(N-2) + 2*M_n - M(N)
        s2n_res = []
        for i in range(len(N_arr)):
            n_val = N_arr[i]
            idx_prev = np.where(N_arr == (n_val - 2))[0]
            if len(idx_prev) > 0:
                s2n = M_arr[idx_prev[0]] + 2.0 * MASS_EXCESS_NEUTRON_MEV - M_arr[i]
                s2n_res.append({"N": int(n_val), "S_2n_MeV": float(s2n)})
        return s2n_res
    else:
        raise ValueError("Either binding_energies_MeV or mass_excesses_MeV must be provided.")


def calculate_pairing_gap_3point(B_minus, B_center, B_plus, is_odd_N=True):
    """
    Calculate 3-point odd-even staggering pairing gap Delta^(3):
    For odd N (center is odd A):
      Delta^(3) = 0.5 * [ B(N-1) - 2*B(N) + B(N+1) ].
    For even N (center is even A):
      Delta^(3) = 0.5 * [ 2*B(N) - B(N-1) - B(N+1) ].
    """
    bm = float(B_minus)
    b0 = float(B_center)
    bp = float(B_plus)

    if is_odd_N:
        gap = 0.5 * (bm - 2.0 * b0 + bp)
    else:
        gap = 0.5 * (2.0 * b0 - bm - bp)

    return {
        "is_odd_N": is_odd_N,
        "B_minus": bm,
        "B_center": b0,
        "B_plus": bp,
        "delta_3point_MeV": float(gap)
    }


def calculate_pairing_gap_5point(B_m2, B_m1, B_0, B_p1, B_p2, is_odd_N=True):
    """
    Calculate 5-point pairing gap Delta^(5) eliminating linear and quadratic curvature:
    For odd N:
      Delta^(5) = (1/8) * [ -B(N-2) + 4*B(N-1) - 6*B(N) + 4*B(N+1) - B(N+2) ].
    For even N:
      Delta^(5) = (1/8) * [ B(N-2) - 4*B(N-1) + 6*B(N) - 4*B(N+1) + B(N+2) ].
    """
    bm2 = float(B_m2)
    bm1 = float(B_m1)
    b0  = float(B_0)
    bp1 = float(B_p1)
    bp2 = float(B_p2)

    if is_odd_N:
        gap = (1.0 / 8.0) * (-bm2 + 4.0 * bm1 - 6.0 * b0 + 4.0 * bp1 - bp2)
    else:
        gap = (1.0 / 8.0) * (bm2 - 4.0 * bm1 + 6.0 * b0 - 4.0 * bp1 + bp2)

    return {
        "is_odd_N": is_odd_N,
        "delta_5point_MeV": float(gap)
    }


def detect_shell_closure_drop(s2n_series, expected_magic=[20, 28, 50, 82, 126], threshold_drop_MeV=1.8):
    """
    Detect magic number shell gap drops: delta_2n(N_magic) = S_2n(N_magic) - S_2n(N_magic + 2).
    """
    s2n_dict = {item["N"]: item["S_2n_MeV"] for item in s2n_series}
    detected_gaps = []

    for magic in expected_magic:
        if magic in s2n_dict and (magic + 2) in s2n_dict:
            s_magic = s2n_dict[magic]
            s_next  = s2n_dict[magic + 2]
            drop = s_magic - s_next
            is_closed_shell = drop >= threshold_drop_MeV
            detected_gaps.append({
                "N_magic": magic,
                "S_2n_at_magic_MeV": s_magic,
                "S_2n_at_next_MeV": s_next,
                "shell_drop_delta_2n_MeV": float(drop),
                "is_shell_closure": is_closed_shell
            })

    return detected_gaps


def detect_shape_transition_anomaly(s2n_series, max_flat_slope_MeV=0.25):
    """
    Detect shape phase transitions where S_2n slope becomes anomalously flat or positive:
      slope = [S_2n(N) - S_2n(N-2)] / 2.
    Normally slope is negative (-0.6 ~ -1.0 MeV / neutron).
    A flat slope or positive slope indicates onset of strong deformation (e.g. N=88 -> 90).
    """
    s2n_sorted = sorted(s2n_series, key=lambda x: x["N"])
    anomalies = []

    for i in range(1, len(s2n_sorted)):
        n_curr = s2n_sorted[i]["N"]
        n_prev = s2n_sorted[i-1]["N"]
        dN = n_curr - n_prev
        if dN == 2:
            s_curr = s2n_sorted[i]["S_2n_MeV"]
            s_prev = s2n_sorted[i-1]["S_2n_MeV"]
            # Normal drop per neutron: (s_prev - s_curr) / 2
            drop_per_neutron = (s_prev - s_curr) / 2.0
            # Anomaly if drop is less than threshold or negative (S_2n increases)
            if drop_per_neutron < max_flat_slope_MeV:
                anomalies.append({
                    "N_transition": n_curr,
                    "N_previous": n_prev,
                    "S2n_previous_MeV": s_prev,
                    "S2n_current_MeV": s_curr,
                    "drop_per_neutron_MeV": float(drop_per_neutron),
                    "is_shape_phase_transition": True,
                    "diagnosis": f"Anomalous S_2n flattening at N={n_prev}->{n_curr} (drop={drop_per_neutron:.2f} MeV/n): Signature of sudden onset of quadrupole deformation!"
                })

    return anomalies


def compare_empirical_bcs_gap(A):
    """
    Compute empirical BCS pairing gap baselines:
      Delta_emp1 = 12.0 / sqrt(A) MeV
      Delta_emp2 = 4.8 / (A^(1/3)) MeV
    """
    a_f = float(A)
    d1 = 12.0 / np.sqrt(a_f)
    d2 = 4.8 / (a_f ** (1.0 / 3.0))

    return {
        "A": int(A),
        "Delta_12_over_sqrt_A_MeV": float(d1),
        "Delta_4.8_over_cbrt_A_MeV": float(d2)
    }
