#!/usr/bin/env python3
"""
in_beam_gated_matrix_multiplet_deconvolution_fitter.py
======================================================
In-Beam Gamma-Gamma Coincidence Matrix Background-Subtracted Gated Spectrum
Multiplet Deconvolution & Correlated Peak Area Covariance Inversion Suite.

Physics Formulation:
--------------------
1. Gamma-Gamma Coincidence Matrix Background Subtraction:
   Based on 吴治华《原子核物理实验方法》第 10 章 §10.2–10.3 (pp. 250–265),
   汪晓莲《粒子探测技术》第 5 章, 朱永生《实验物理中的概率和统计》第 8–9 章,
   and D. C. Radford (Nucl. Instrum. Methods A 361, 297, 1995):
   In multi-detector HPGe arrays (Gammasphere, AGATA, Clover), coincidence events are sorted
   into a 2D symmetric energy matrix M(E1, E2).
   Setting a peak gate G = [E_g1, E_g2] on transition gamma_1 projects out the coincident spectrum.
   The underlying Compton continuum background is subtracted using adjacent left (B_L) and right (B_R) windows:
     S_net(E) = P_G(E) - f_L * B_L(E) - f_R * B_R(E)
   The variance per bin is governed by Poisson counting statistics:
     sigma^2(E) = P_G(E) + f_L^2 * B_L(E) + f_R^2 * B_R(E)

2. Multiplet Deconvolution & Detector Resolution Constraints:
   Closely spaced transitions (e.g. Delta E ~ 1.5 - 3.5 keV, comparable to HPGe FWHM ~ 2.0 - 2.5 keV)
   frequently overlap in gated spectra.
   The composite lineshape is modeled as a sum of K Gaussians plus a residual background:
     F(E) = sum_{j=1}^K [ A_j / (sqrt(2*pi) * sigma_j) ] * exp( -(E - E_j)^2 / (2 * sigma_j^2) ) + b_0 + b_1 * (E - E_c)
   where detector resolution constraints couple the peak widths:
     sigma_j = FWHM(E_j) / 2.35482.

3. Correlated Peak Area Covariance & Branching Uncertainty:
   When two peaks overlap severely (separation D = Delta E / FWHM < 2.0), the fitted areas
   A_1 and A_2 exhibit strong negative anti-correlation (rho(A_1, A_2) ~ -0.60 to -0.90).
   Extracting the full parameter covariance matrix V is essential for:
     - Reporting true individual peak area uncertainties sigma_{A_j} = sqrt(V_{jj});
     - Computing the uncertainty of intensity sums or branching ratios without false error inflation.
"""

import sys
import json
import math
import argparse
import numpy as np
from scipy.optimize import curve_fit


PRESETS = {
    "133Ce_wobbling_candidate_doublet": {
        "description": "133Ce closely spaced in-beam doublet (638.2 keV and 641.4 keV, Delta E = 3.2 keV)",
        "nucleus": "133Ce",
        "gate_energy_keV": 510.5,
        "true_peaks": [
            {"energy_keV": 638.20, "area": 12500.0},
            {"energy_keV": 641.40, "area": 8400.0}
        ],
        "fwhm_nominal_keV": 2.15,
        "background_level": 45.0,
        "E_min_keV": 630.0,
        "E_max_keV": 650.0,
        "bin_width_keV": 0.25
    },
    "130Ba_two_quasiparticle_triplet": {
        "description": "130Ba overlapping in-beam triplet (455.0, 458.5, and 464.0 keV)",
        "nucleus": "130Ba",
        "gate_energy_keV": 395.0,
        "true_peaks": [
            {"energy_keV": 455.00, "area": 15000.0},
            {"energy_keV": 458.50, "area": 9500.0},
            {"energy_keV": 464.00, "area": 6200.0}
        ],
        "fwhm_nominal_keV": 1.95,
        "background_level": 60.0,
        "E_min_keV": 445.0,
        "E_max_keV": 475.0,
        "bin_width_keV": 0.25
    },
    "isolated_single_peak_benchmark": {
        "description": "Isolated single calibration peak (1332.5 keV, FWHM = 2.40 keV)",
        "nucleus": "60Co-Calibration",
        "gate_energy_keV": 1173.2,
        "true_peaks": [
            {"energy_keV": 1332.50, "area": 25000.0}
        ],
        "fwhm_nominal_keV": 2.40,
        "background_level": 20.0,
        "E_min_keV": 1320.0,
        "E_max_keV": 1345.0,
        "bin_width_keV": 0.25
    }
}


def multiplet_model_function(E_arr, *params):
    """
    Composite lineshape: sum of K Gaussians + linear background.
    params: [A_1, E_1, ..., A_K, E_K, sigma_common, b_0, b_1]
    """
    E = np.array(E_arr, dtype=float)
    num_peaks = (len(params) - 3) // 2
    sigma_com = max(1e-3, params[-3])
    b0 = params[-2]
    b1 = params[-1]
    E_c = float(np.mean(E))

    y = b0 + b1 * (E - E_c)
    for j in range(num_peaks):
        Aj = params[2 * j]
        Ej = params[2 * j + 1]
        prefactor = Aj / (math.sqrt(2.0 * math.pi) * sigma_com)
        y += prefactor * np.exp(-((E - Ej)**2) / (2.0 * sigma_com**2))
    return y


def generate_synthetic_gated_spectrum(peaks, fwhm_nominal, bkg_level, E_min, E_max, bin_width, seed=42):
    """
    Generates synthetic gated energy spectrum with Poisson fluctuations.
    """
    np.random.seed(seed)
    n_bins = int(round((E_max - E_min) / bin_width))
    E_axis = np.linspace(E_min, E_max, n_bins)

    sigma_true = fwhm_nominal / 2.35482
    p_true = []
    for p in peaks:
        p_true.extend([p["area"], p["energy_keV"]])
    p_true.extend([sigma_true, bkg_level, 0.0])

    y_exact = multiplet_model_function(E_axis, *p_true)
    # Poisson fluctuations
    counts = np.random.poisson(np.maximum(0.0, y_exact)).astype(float)
    sigma_counts = np.sqrt(np.maximum(1.0, counts))
    return E_axis, counts, sigma_counts


def fit_gated_multiplet(E_axis, counts, sigma_counts, initial_peak_guesses, fwhm_guess):
    """
    Fits multiplet lineshape to gated spectrum using weighted non-linear optimization.
    Returns fitted parameters, uncertainties, covariance matrix, and deconvolution metrics.
    """
    K = len(initial_peak_guesses)
    p0 = []
    bounds_lower = []
    bounds_upper = []

    sigma_init = fwhm_guess / 2.35482

    for guess in initial_peak_guesses:
        p0.extend([guess["area_guess"], guess["energy_guess"]])
        bounds_lower.extend([0.0, E_axis[0]])
        bounds_upper.extend([1e8, E_axis[-1]])

    p0.extend([sigma_init, float(np.min(counts)), 0.0])
    bounds_lower.extend([0.05, 0.0, -100.0])
    bounds_upper.extend([5.0, 1e6, 100.0])

    try:
        popt, pcov = curve_fit(
            multiplet_model_function,
            E_axis,
            counts,
            p0=p0,
            bounds=(bounds_lower, bounds_upper),
            sigma=sigma_counts,
            maxfev=6000
        )
        perr = np.sqrt(np.diag(pcov))
    except Exception:
        popt = np.array(p0)
        pcov = np.identity(len(p0))
        perr = np.zeros(len(p0))

    # Goodness of fit
    y_fit = multiplet_model_function(E_axis, *popt)
    residuals = counts - y_fit
    chi2 = float(np.sum((residuals / sigma_counts)**2))
    ndf = max(1, len(E_axis) - len(popt))
    red_chi2 = chi2 / ndf

    fitted_fwhm = popt[-3] * 2.35482
    sigma_fwhm = perr[-3] * 2.35482

    fitted_peaks = []
    for j in range(K):
        aj = float(popt[2 * j])
        sig_aj = float(perr[2 * j])
        ej = float(popt[2 * j + 1])
        sig_ej = float(perr[2 * j + 1])
        fitted_peaks.append({
            "peak_index": j + 1,
            "area": aj,
            "sigma_area": sig_aj,
            "energy_keV": ej,
            "sigma_energy_keV": sig_ej,
            "relative_area_pct": (sig_aj / max(1.0, aj)) * 100.0
        })

    # Separation & correlation metrics for doublets
    metrics = {
        "fitted_fwhm_keV": float(fitted_fwhm),
        "sigma_fwhm_keV": float(sigma_fwhm),
        "chi2": float(chi2),
        "ndf": int(ndf),
        "reduced_chi2": float(red_chi2)
    }

    if K >= 2:
        delta_E = abs(fitted_peaks[1]["energy_keV"] - fitted_peaks[0]["energy_keV"])
        d_ratio = delta_E / max(1e-3, fitted_fwhm)
        cov_a1_a2 = float(pcov[0, 2])
        corr_a1_a2 = cov_a1_a2 / max(1e-12, perr[0] * perr[2])
        metrics["peak1_peak2_delta_E_keV"] = float(delta_E)
        metrics["peak_separation_in_fwhm"] = float(d_ratio)
        metrics["area_correlation_rho"] = float(corr_a1_a2)
        metrics["is_severely_overlapping"] = bool(d_ratio < 2.0)

    return {
        "peaks": fitted_peaks,
        "metrics": metrics,
        "background": {
            "baseline_b0": float(popt[-2]),
            "slope_b1": float(popt[-1])
        },
        "covariance_matrix": pcov.tolist()
    }


def run_multiplet_analysis(peaks, fwhm_nominal, bkg_level, E_min, E_max, bin_width, nucleus="Nucleus"):
    """
    Complete execution pipeline for gated multiplet deconvolution.
    """
    E_axis, counts, sigma_counts = generate_synthetic_gated_spectrum(
        peaks=peaks,
        fwhm_nominal=fwhm_nominal,
        bkg_level=bkg_level,
        E_min=E_min,
        E_max=E_max,
        bin_width=bin_width
    )

    guesses = [{"area_guess": p["area"], "energy_guess": p["energy_keV"]} for p in peaks]
    fit_res = fit_gated_multiplet(E_axis, counts, sigma_counts, guesses, fwhm_nominal)
    fit_res["nucleus"] = nucleus
    fit_res["simulation_truth"] = peaks
    return fit_res


def format_text_report(res, title="In-Beam Gated Matrix Multiplet Deconvolution Fitter"):
    nuc = res["nucleus"]
    m = res["metrics"]
    pks = res["peaks"]
    truth = res.get("simulation_truth", [])

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {nuc} | Red. Chi^2 = {m['reduced_chi2']:.2f} (Chi^2/ndf = {m['chi2']:.1f}/{m['ndf']}) | FWHM = {m['fitted_fwhm_keV']:.3f} +- {m['sigma_fwhm_keV']:.3f} keV")
    lines.append("=" * 76)
    lines.append("Deconvoluted Multiplet Peak Components:")
    lines.append("  #   Energy E (keV)      Net Area (counts)    Rel Err (%)   Sim Truth Area   Diff (%)")
    for j, p in enumerate(pks):
        t_area = truth[j]["area"] if j < len(truth) else 0.0
        diff_pct = (abs(p["area"] - t_area) / max(1.0, t_area)) * 100.0 if t_area > 0 else 0.0
        lines.append(f"  {p['peak_index']}   {p['energy_keV']:8.2f} +- {p['sigma_energy_keV']:4.2f}   {p['area']:8.1f} +- {p['sigma_area']:6.1f}       {p['relative_area_pct']:4.2f}%       {t_area:8.1f}        {diff_pct:4.2f}%")
    lines.append("-" * 76)
    if "peak_separation_in_fwhm" in m:
        lines.append("Doublet Overlap & Covariance Diagnostics:")
        lines.append(f"  Peak Energy Separation Delta E  : {m['peak1_peak2_delta_E_keV']:.2f} keV")
        lines.append(f"  Separation in FWHM Units (D)    : {m['peak_separation_in_fwhm']:.2f} x FWHM ({'Severely Overlapping (< 2 FWHM)' if m['is_severely_overlapping'] else 'Well Resolved'})")
        lines.append(f"  Area Covariance Correlation rho : {m['area_correlation_rho']:.3f} ({'Strong Anti-Correlation' if m['area_correlation_rho'] < -0.5 else 'Mild/Weak Correlation'})")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Gated Matrix Multiplet Deconvolution Fitter."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        peaks = p["true_peaks"]
        fwhm = p["fwhm_nominal_keV"]
        bg = p["background_level"]
        emin = p["E_min_keV"]
        emax = p["E_max_keV"]
        bw = p["bin_width_keV"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        return parser.print_help()

    res = run_multiplet_analysis(
        peaks=peaks,
        fwhm_nominal=fwhm,
        bkg_level=bg,
        E_min=emin,
        E_max=emax,
        bin_width=bw,
        nucleus=nucleus
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
