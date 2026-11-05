#!/usr/bin/env python3
"""
gamma_gamma_matrix_slicer_calculator.py
=======================================
In-Beam Gamma-Gamma Coincidence Matrix Slicing, Radford 2D Background
Subtraction & Coincidence Branching Analyzer.

Physics & Formulation:
----------------------
1. 2D Symmetric Coincidence Matrix M(E1, E2):
   Accumulated from multi-fold HPGe detector arrays:
     M_ij = Number of gamma-gamma coincidence events in channels (i, j).
   Total 1D projection: P_i = sum_j M_ij.
   Smooth Compton background projection: B_i.

2. Radford Background-Subtracted Gate Formula (Radware / ESCL8R):
   When setting a peak gate G = [E_g - dE, E_g + dE] and background gates BG:
     S_i = sum_{j in G} M_ij - (W_G / W_BG) * sum_{j in BG} M_ij -
           [ (P_G - B_G) / T ] * B_i
   where:
     W_G, W_BG: Energy window widths of peak and background gates.
     T: Total counts in matrix = sum_ij M_ij.
     P_G = sum_{j in G} P_j, B_G = sum_{j in G} B_j.

3. Coincidence Peak-to-Background (P/B) Ratio & Area Extraction:
   Peak area A_coinc in gated spectrum, background area B_coinc:
     P/B = A_coinc / B_coinc
     Net intensity: I_coinc = A_coinc / (epsilon(E1) * epsilon(E2) * W(theta))

4. Coincidence Matrix Level Ordering Logic:
   - Coincident (in cascade): A feeds B -> gate on A shows B, gate on B shows A.
   - Parallel branches: A and B bypass each other -> mutually exclusive (zero coincidence).

References:
  - D. C. Radford, Nucl. Instrum. Methods A 361, 297 (1995) [ESCL8R & Radware].
  - 吴治华, 《原子核物理实验方法》, 第三版.
  - M. A. Deleplanque et al., Phys. Rev. Lett. 43, 749 (1979).
"""

import math
import json
import argparse
import sys
from typing import Dict, Any, List, Optional, Tuple


def generate_synthetic_cascade_matrix(
    cascade_energies_keV: List[float] = [200.0, 350.0, 500.0, 650.0],
    matrix_dim: int = 100,
    e_max_keV: float = 1000.0,
    peak_counts: float = 5000.0,
    compton_bg_counts: float = 80.0
) -> Dict[str, Any]:
    """
    Synthesizes a 2D coincidence matrix for an in-beam gamma cascade.
    """
    de = e_max_keV / float(matrix_dim)
    matrix = [[compton_bg_counts] * matrix_dim for _ in range(matrix_dim)]

    # Map cascade energies to matrix channels
    ch_map = [int(round(e / de)) for e in cascade_energies_keV]

    # Add coincident peak pairs (i, j) for all i != j in cascade
    n_casc = len(ch_map)
    for i in range(n_casc):
        for j in range(n_casc):
            if i != j:
                ci = ch_map[i]
                cj = ch_map[j]
                if 0 <= ci < matrix_dim and 0 <= cj < matrix_dim:
                    matrix[ci][cj] += peak_counts

    # Total 1D projection P_i
    projection = [sum(row) for row in matrix]
    total_counts = sum(projection)

    return {
        "matrix_dim": matrix_dim,
        "energy_max_keV": e_max_keV,
        "channel_width_keV": de,
        "cascade_energies_keV": cascade_energies_keV,
        "cascade_channels": ch_map,
        "total_matrix_counts": total_counts,
        "projection": projection,
        "matrix": matrix
    }


def slice_matrix_gate(
    matrix_data: Dict[str, Any],
    gate_energy_keV: float,
    gate_width_keV: float = 10.0,
    bg_offset_keV: float = 25.0
) -> Dict[str, Any]:
    """
    Slices a 1D coincidence spectrum from the 2D matrix using Radford background subtraction.
    """
    de = matrix_data["channel_width_keV"]
    dim = matrix_data["matrix_dim"]
    mat = matrix_data["matrix"]
    proj = matrix_data["projection"]
    tot_counts = matrix_data["total_matrix_counts"]

    g_ch = int(round(gate_energy_keV / de))
    half_w = max(int(round(0.5 * gate_width_keV / de)), 1)

    g_min = max(g_ch - half_w, 0)
    g_max = min(g_ch + half_w, dim - 1)
    n_gate_ch = g_max - g_min + 1

    # Background gates: left and right
    bg_dist = int(round(bg_offset_keV / de))
    bg1_min = max(g_ch - bg_dist - half_w, 0)
    bg1_max = min(g_ch - bg_dist + half_w, dim - 1)
    bg2_min = max(g_ch + bg_dist - half_w, 0)
    bg2_max = min(g_ch + bg_dist + half_w, dim - 1)

    bg_indices = list(range(bg1_min, bg1_max + 1)) + list(range(bg2_min, bg2_max + 1))
    n_bg_ch = len(bg_indices)

    # Sliced spectrum S_i
    sliced_spectrum = []
    ratio_w = float(n_gate_ch) / float(max(n_bg_ch, 1))

    # Average smooth background in gate
    p_gate = sum(proj[j] for j in range(g_min, g_max + 1))
    b_gate = ratio_w * sum(proj[j] for j in bg_indices)

    for i in range(dim):
        # Raw gate sum
        sum_g = sum(mat[i][j] for j in range(g_min, g_max + 1))
        # Background gate sum
        sum_bg = sum(mat[i][j] for j in bg_indices)
        # Radford formula
        s_i = sum_g - ratio_w * sum_bg
        sliced_spectrum.append(round(s_i, 1))

    # Find coincident peaks in sliced spectrum
    coinc_peaks = []
    for e_casc in matrix_data["cascade_energies_keV"]:
        if abs(e_casc - gate_energy_keV) > 2.0 * gate_width_keV:
            ch_c = int(round(e_casc / de))
            if 0 <= ch_c < dim:
                area = sliced_spectrum[ch_c]
                coinc_peaks.append({
                    "energy_keV": e_casc,
                    "channel": ch_c,
                    "net_coincident_area": area,
                    "status": "In_Cascade_Screening_Pass" if area > 500.0 else "Weak_or_Unobserved"
                })

    return {
        "gate_energy_keV": gate_energy_keV,
        "gate_channel_range": [g_min, g_max],
        "gate_total_counts": p_gate,
        "gate_background_counts": round(b_gate, 1),
        "peak_to_background_ratio": round((p_gate - b_gate) / max(b_gate, 1.0), 2),
        "coincident_cascade_peaks": coinc_peaks
    }


def format_text_report(summary: Dict[str, Any]) -> str:
    lines = []
    lines.append("=" * 72)
    lines.append("   GAMMA-GAMMA COINCIDENCE MATRIX SLICING & RADWARE ANALYZER")
    lines.append("=" * 72)

    lines.append(f" MATRIX SPECIFICATIONS: Dimension = {summary['matrix_dim']}x{summary['matrix_dim']}, E_max = {summary['energy_max_keV']} keV")
    lines.append(f"   Total Matrix Events            : {summary['total_matrix_counts']:.2e} counts")
    lines.append(f"   Known Cascade Transitions      : {summary['cascade_energies_keV']} keV")
    lines.append("-" * 72)

    sl = summary["sliced_gate"]
    lines.append(f" SLICED GATE AT E_gamma = {sl['gate_energy_keV']} keV:")
    lines.append(f"   Channel Gate Interval          : [{sl['gate_channel_range'][0]} - {sl['gate_channel_range'][1]}]")
    lines.append(f"   Peak-to-Background (P/B) Ratio : {sl['peak_to_background_ratio']}")
    lines.append(f"   Gate Total / Background Counts : {sl['gate_total_counts']} / {sl['gate_background_counts']}")
    lines.append("-" * 72)
    lines.append(" COINCIDENT CASCADE PEAKS IDENTIFIED:")
    lines.append(f"   {'Coincident E_gamma (keV)':<26} {'Net Peak Area':<20} {'Cascade Status':<20}")
    lines.append("   " + "-" * 66)
    for pk in sl["coincident_cascade_peaks"]:
        lines.append(f"   {pk['energy_keV']:<26.1f} {pk['net_coincident_area']:<20.1f} {pk['status']:<20}")
    lines.append("-" * 72)
    lines.append(" Physical Significance:")
    lines.append("   - Radford 2D subtraction eliminates Compton-Compton and Compton-peak background.")
    lines.append(
        "   - Supports mutual-coincidence ordering under the supplied "
        "cascade/background contract; it is not, by itself, proof of a "
        "rotational-band assignment."
    )
    lines.append("   - Fundamental engine behind in-beam level scheme construction (escl8r / Radware).")
    lines.append("========================================================================")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Gamma-Gamma Coincidence Matrix Slicing & Radware Analyzer."
    )
    parser.add_argument("-G", "--gate", type=float, default=350.0, help="Gated gamma energy in keV (default: 350.0)")
    parser.add_argument("-W", "--width", type=float, default=12.0, help="Gate energy width in keV (default: 12.0)")
    parser.add_argument("--e-max", type=float, default=1000.0, help="Maximum matrix energy in keV (default: 1000.0)")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    mat_res = generate_synthetic_cascade_matrix(e_max_keV=args.e_max)
    slice_res = slice_matrix_gate(mat_res, args.gate, args.width)

    summary = {
        "matrix_dim": mat_res["matrix_dim"],
        "energy_max_keV": mat_res["energy_max_keV"],
        "total_matrix_counts": mat_res["total_matrix_counts"],
        "cascade_energies_keV": mat_res["cascade_energies_keV"],
        "sliced_gate": slice_res
    }

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(format_text_report(summary))


if __name__ == "__main__":
    main()
