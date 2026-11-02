#!/usr/bin/env python3
"""
in_beam_array_fold_multiplicity_entry_state_unfolder.py
=======================================================
In-Beam Multi-Detector Array Coincidence Fold-to-Multiplicity Response Inversion,
Compound Nucleus Entry-State Spin (J_entry) and Excitation Energy Unfolding Suite.

Physics Formulation:
--------------------
1. Gamma-Ray Multiplicity & Fold Measurement in Fusion-Evaporation Reactions:
   Based on 吴治华《原子核物理实验方法》第 10 章 §10.6 (pp. 290–305) 与第 15 章,
   汪晓莲《粒子探测技术》第 8 章, C. A. Bertulani "Introduction to Nuclear Reactions" Ch. 6,
   and M. Jaaskelainen et al. (Nucl. Instrum. Methods 204, 385, 1983):
   In heavy-ion fusion-evaporation reactions, high-spin compound states de-excite via cascades of
   gamma-rays. A 4pi calorimeter or multi-detector array (e.g. BGO ball or Clover array with N_det
   elements and individual efficiency eps_det) detects a coincidence Fold k (number of triggered crystals)
   and total Sum Energy H.

2. Analytical Fold-to-Multiplicity Response Matrix P(k | M):
   The probability of observing fold k given a true gamma multiplicity M is given by combinatorial
   inclusion-exclusion:
     P(k | M) = (N_det choose k) * sum_{j=0}^k (-1)^(k - j) * (k choose j) * [ 1 - (N_det - j) / N_det * eps_det ]^M
   This form correctly accounts for multiple photon hits in the same detector (pileup/summing).

3. Iterative Bayesian Deconvolution of Multiplicity Distribution P(M):
   Given experimental fold histogram F(k), the true multiplicity distribution P(M) is unfolded via
   Richardson-Lucy iterative deconvolution:
     P^(n+1)(M) = P^(n)(M) * sum_k [ P(k | M) * F_meas(k) / ( sum_M' P(k | M') * P^(n)(M') ) ]
   yielding the mean multiplicity <M>, variance sigma_M^2, and FWHM.

4. Entry State Spin <J_entry> and Excitation Energy Mapping:
   The gamma cascade consists of N_stat statistical E1 dipole transitions (Delta J ~ 0.5 hbar) followed
   by stretched E2 quadrupole rotational transitions (Delta J = 2 hbar):
     <J_entry> = 2 * ( <M> - N_stat ) + N_stat * Delta J_stat + J_bandhead
     sigma_J = 2 * sigma_M
   The average entry excitation energy above the yrast line is:
     <E*_entry> = <H> / eps_sum + E_thresh
   providing essential input for calculating side-feeding and spin population in high-spin wobbling/chiral bands.
"""

import sys
import json
import math
import argparse
import numpy as np


PRESETS = {
    "4pi_bgo_ball_fusion_evaporation": {
        "description": "4pi 30-detector BGO ball for 36Ar + 100Mo -> 132Ce + 4n (Jaaskelainen 1983)",
        "reaction": "36Ar + 100Mo -> 132Ce + 4n at Elab = 160 MeV",
        "N_det": 30,
        "eps_det": 0.85,
        "eps_sum": 0.78,
        "N_stat": 3.5,
        "J_bandhead": 0.0,
        "measured_fold_histogram": {
            "8": 450, "9": 980, "10": 2100, "11": 4200, "12": 6800,
            "13": 9200, "14": 11500, "15": 12800, "16": 11900, "17": 9800,
            "18": 7100, "19": 4400, "20": 2300, "21": 1050, "22": 420
        },
        "mean_sum_energy_MeV": 26.5
    },
    "clover_array_multiplicity_filter": {
        "description": "12-Clover array with BGO suppression shields (48 channels, eps = 0.70)",
        "reaction": "Heavy-ion fusion at Elab = 145 MeV",
        "N_det": 48,
        "eps_det": 0.70,
        "eps_sum": 0.65,
        "N_stat": 4.0,
        "J_bandhead": 0.0,
        "measured_fold_histogram": {
            "6": 600, "8": 1500, "10": 3400, "12": 6200, "14": 8900,
            "16": 10500, "18": 9800, "20": 7400, "22": 4600, "24": 2200, "26": 850
        },
        "mean_sum_energy_MeV": 22.0
    },
    "low_multiplicity_transfer_reaction": {
        "description": "Peripheral transfer reaction measuring low fold (k = 2 to 6)",
        "reaction": "Few-nucleon transfer reaction",
        "N_det": 24,
        "eps_det": 0.80,
        "eps_sum": 0.70,
        "N_stat": 2.0,
        "J_bandhead": 2.0,
        "measured_fold_histogram": {
            "1": 3500, "2": 8200, "3": 11500, "4": 9400, "5": 5100, "6": 1800, "7": 450
        },
        "mean_sum_energy_MeV": 6.8
    }
}


def calculate_binomial_response_matrix(N_det, eps_det, max_fold, max_mult):
    """
    Calculates analytical Fold-to-Multiplicity response matrix P(k | M).
    Matrix dimensions: [max_fold + 1, max_mult + 1].
    """
    resp = np.zeros((max_fold + 1, max_mult + 1), dtype=float)

    for k in range(min(N_det + 1, max_fold + 1)):
        binom_N_k = math.comb(N_det, k)
        for M in range(max_mult + 1):
            sum_term = 0.0
            for j in range(k + 1):
                binom_k_j = math.comb(k, j)
                sign = (-1.0)**(k - j)
                frac = (N_det - j) / float(N_det)
                base = max(0.0, 1.0 - frac * eps_det)
                sum_term += sign * binom_k_j * (base**M)
            resp[k, M] = max(0.0, binom_N_k * sum_term)

    # Normalize columns so sum_k P(k | M) = 1.0 (or total efficiency)
    col_sums = np.sum(resp, axis=0)
    for M in range(max_mult + 1):
        if col_sums[M] > 0:
            resp[:, M] /= col_sums[M]

    return resp


def unfold_multiplicity_distribution(fold_hist, resp_matrix, n_iterations=35):
    """
    Performs Richardson-Lucy iterative deconvolution of fold distribution to extract P(M).
    """
    max_fold, max_mult = resp_matrix.shape[0] - 1, resp_matrix.shape[1] - 1
    f_meas = np.zeros(max_fold + 1, dtype=float)
    for k_str, val in fold_hist.items():
        k = int(k_str)
        if k <= max_fold:
            f_meas[k] = float(val)

    total_counts = np.sum(f_meas)
    if total_counts > 0:
        f_meas /= total_counts

    # Initial guess: flat prior
    p_M = np.ones(max_mult + 1, dtype=float) / (max_mult + 1)

    for _ in range(n_iterations):
        f_pred = np.dot(resp_matrix, p_M)
        f_pred = np.maximum(1e-15, f_pred)
        ratio = f_meas / f_pred
        correction = np.dot(resp_matrix.T, ratio)
        p_M = p_M * correction
        p_M /= np.sum(p_M)

    mult_axis = np.arange(max_mult + 1)
    mean_M = float(np.sum(mult_axis * p_M))
    var_M = float(np.sum(((mult_axis - mean_M)**2) * p_M))
    sigma_M = math.sqrt(max(0.0, var_M))

    return mult_axis, p_M, mean_M, sigma_M


def map_to_entry_spin_and_energy(mean_M, sigma_M, mean_H_MeV, N_stat=3.5, delta_I_stat=0.5,
                                  J_bandhead=0.0, eps_sum=0.75):
    """
    Maps multiplicity to compound nucleus entry-state spin <J_entry> and excitation energy <E*_entry>.
    """
    rot_multiplicity = max(0.0, mean_M - N_stat)
    mean_J = 2.0 * rot_multiplicity + N_stat * delta_I_stat + J_bandhead
    sigma_J = 2.0 * sigma_M

    entry_E_star_MeV = mean_H_MeV / max(1e-3, eps_sum)

    return {
        "mean_multiplicity_M": float(mean_M),
        "sigma_multiplicity_M": float(sigma_M),
        "mean_entry_spin_hbar": float(mean_J),
        "sigma_entry_spin_hbar": float(sigma_J),
        "mean_entry_excitation_energy_MeV": float(entry_E_star_MeV),
        "rotational_gamma_count": float(rot_multiplicity),
        "statistical_gamma_count": float(N_stat)
    }


def run_fold_unfolding_analysis(fold_hist, N_det, eps_det, eps_sum, mean_H_MeV,
                                N_stat=3.5, J_bandhead=0.0, max_mult=40):
    """
    Complete execution pipeline for fold unfolding and entry-state analysis.
    """
    max_fold = N_det
    resp = calculate_binomial_response_matrix(N_det, eps_det, max_fold, max_mult)
    mult_axis, p_M, mean_M, sigma_M = unfold_multiplicity_distribution(fold_hist, resp)
    entry_info = map_to_entry_spin_and_energy(
        mean_M=mean_M,
        sigma_M=sigma_M,
        mean_H_MeV=mean_H_MeV,
        N_stat=N_stat,
        J_bandhead=J_bandhead,
        eps_sum=eps_sum
    )

    return {
        "array_parameters": {
            "N_det": int(N_det),
            "detector_efficiency": float(eps_det),
            "sum_efficiency": float(eps_sum)
        },
        "entry_state": entry_info,
        "unfolded_distribution": {
            "multiplicities": mult_axis.tolist(),
            "probabilities": [float(p) for p in p_M]
        }
    }


def format_text_report(res, title="In-Beam Array Fold Unfolding & Entry-State Analyzer"):
    arr = res["array_parameters"]
    ent = res["entry_state"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Detector Array: N_det = {arr['N_det']} modules | Efficiency eps_det = {arr['detector_efficiency']*100.0:.1f}% (Sum eps = {arr['sum_efficiency']*100.0:.1f}%)")
    lines.append("=" * 76)
    lines.append("Unfolded Gamma-Ray Multiplicity Distribution:")
    lines.append(f"  Mean Multiplicity <M>           : {ent['mean_multiplicity_M']:.2f} +- {ent['sigma_multiplicity_M']:.2f} photons")
    lines.append(f"  Rotational Quadrupole Photons   : {ent['rotational_gamma_count']:.2f} (carrying Delta J = 2 hbar each)")
    lines.append(f"  Statistical Dipole Photons      : {ent['statistical_gamma_count']:.2f} (cooling without major spin loss)")
    lines.append("-" * 76)
    lines.append("Compound Nucleus Entry-State Spin & Energy Mapping:")
    lines.append(f"  Mean Entry Spin <J_entry>       : {ent['mean_entry_spin_hbar']:.1f} +- {ent['sigma_entry_spin_hbar']:.1f} hbar")
    lines.append(f"  Mean Entry Excitation Energy E* : {ent['mean_entry_excitation_energy_MeV']:.2f} MeV (above ground state)")
    lines.append("-" * 76)
    lines.append("High-Spin Feeding Potential:")
    if ent['mean_entry_spin_hbar'] >= 30.0:
        feed_str = "EXCELLENT - Feeds ultra-high spin wobbling/superdeformed states"
    elif ent['mean_entry_spin_hbar'] >= 20.0:
        feed_str = "OPTIMAL - Strongly populates chiral doublet & transverse wobbling bands"
    else:
        feed_str = "LOW SPIN - Suitable for low-lying vibrational/octupole collective states"
    lines.append(f"  Feeding Assessment              : {feed_str}")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Array Fold Unfolding & Entry-State Analyzer."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        N_det = p["N_det"]
        eps_det = p["eps_det"]
        eps_sum = p["eps_sum"]
        N_stat = p.get("N_stat", 3.5)
        J_0 = p.get("J_bandhead", 0.0)
        hist = p["measured_fold_histogram"]
        H_mean = p["mean_sum_energy_MeV"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_fold_unfolding_analysis(
        fold_hist=hist,
        N_det=N_det,
        eps_det=eps_det,
        eps_sum=eps_sum,
        mean_H_MeV=H_mean,
        N_stat=N_stat,
        J_bandhead=J_0
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
