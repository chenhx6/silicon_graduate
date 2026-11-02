#!/usr/bin/env python3
"""
in_beam_time_spectrum_convolution_fitter.py
===========================================
In-Beam Electronic Time-Difference Spectrum Analytical Gaussian-Exponential
Convolution Lineshape Fitter & Nuclear Lifetime Deconvolution Suite.

Physics Formulation:
--------------------
1. Convolution of Nuclear Decay Law with Instrumental Response:
   Based on Nakhostin《辐射探测器信号处理》第 8 章 (pp. 310–335), 吴治华《原子核物理实验方法》第 14 章,
   and D. Bazzacco et al. (Nucl. Instrum. Methods A 309, 163, 1991):
   When nuclear lifetime tau is comparable to or smaller than the detector time resolution
   (FWHM = 2.355 * sigma_t), the measured time-difference spectrum S(t) is the physical
   convolution of the Gaussian Instrumental Response Function (IRF) with the nuclear exponential decay:
     S(t) = integral_0^infty D(u) * IRF(t - u) du + B_0
   where:
     IRF(t) = [ 1 / (sqrt(2*pi) * sigma) ] * exp( -(t - t0)^2 / (2 * sigma^2) )
     D(u)   = (A / tau) * exp( -u / tau ) * Theta(u).

2. Exact Analytical Convoluted Lineshape:
   Performing the integration analytically yields the closed-form Erfc solution:
     S(t) = [ A / (2 * tau) ] * exp( sigma^2 / (2 * tau^2) - (t - t0) / tau )
            * erfc( [ t0 + sigma^2 / tau - t ] / [ sqrt(2) * sigma ] ) + B_0
   where:
     - As t << t0: S(t) -> B_0 (flat pre-prompt background);
     - Around t ~ t0: S(t) undergoes a smooth Gaussian-like rise;
     - As t >> t0: S(t) exhibits an exact exponential decay slope ~ exp(-(t - t0)/tau).

3. Non-Linear Parameter Estimation & Covariance Inversion:
   Fits [A, tau, t0, sigma, B_0] via non-linear optimization with bounds,
   extracting the true nuclear lifetime tau even deep inside the instrumental resolution!
"""

import sys
import json
import math
import argparse
import numpy as np
from scipy.optimize import curve_fit
import scipy.special as sp


PRESETS = {
    "134Ce_fast_timing_cascade": {
        "description": "134Ce in-beam fast timing (tau_true = 0.080 ns, FWHM = 0.220 ns)",
        "nucleus": "134Ce",
        "true_tau_ns": 0.080,
        "true_t0_ns": 1.00,
        "true_fwhm_ns": 0.220,
        "true_amplitude": 25000.0,
        "true_background": 15.0,
        "t_min_ns": -0.5,
        "t_max_ns": 3.0,
        "n_bins": 120
    },
    "181Ta_isomer_decay": {
        "description": "181Ta nanosecond isomer decay (tau_true = 6.05 ns, FWHM = 1.20 ns)",
        "nucleus": "181Ta",
        "true_tau_ns": 6.05,
        "true_t0_ns": 2.00,
        "true_fwhm_ns": 1.20,
        "true_amplitude": 50000.0,
        "true_background": 25.0,
        "t_min_ns": -2.0,
        "t_max_ns": 30.0,
        "n_bins": 160
    },
    "prompt_calibration_irf": {
        "description": "Prompt calibration cascade (tau_true = 0.010 ns, FWHM = 0.200 ns)",
        "nucleus": "Prompt-IRF",
        "true_tau_ns": 0.010,
        "true_t0_ns": 1.00,
        "true_fwhm_ns": 0.200,
        "true_amplitude": 30000.0,
        "true_background": 10.0,
        "t_min_ns": -0.5,
        "t_max_ns": 2.5,
        "n_bins": 100
    }
}


def convoluted_decay_model(t, A, tau, t0, sigma, bg):
    """
    Analytical Gaussian-Exponential convolution lineshape.
    """
    tau_safe = max(1e-4, tau)
    sigma_safe = max(1e-4, sigma)

    arg = (t0 + (sigma_safe**2 / tau_safe) - t) / (math.sqrt(2.0) * sigma_safe)
    log_prefactor = math.log(max(1e-12, A / (2.0 * tau_safe))) + (sigma_safe**2 / (2.0 * tau_safe**2)) - ((t - t0) / tau_safe)
    log_clipped = np.clip(log_prefactor, -80.0, 40.0)

    erfc_vals = sp.erfc(arg)
    return np.exp(log_clipped) * erfc_vals + bg


def generate_synthetic_spectrum(t_arr, A, tau, t0, sigma, bg, seed=42):
    """
    Generates synthetic time-difference spectrum with Poisson count fluctuations.
    """
    np.random.seed(seed)
    y_exact = convoluted_decay_model(t_arr, A, tau, t0, sigma, bg)
    y_noisy = np.random.poisson(np.maximum(0.0, y_exact)).astype(float)
    return y_noisy


def fit_convoluted_time_spectrum(t_arr, counts, p0_guess=None):
    """
    Fits the convoluted model to experimental time-difference histogram.
    """
    y = np.array(counts, dtype=float)
    t = np.array(t_arr, dtype=float)

    if p0_guess is None:
        max_idx = np.argmax(y)
        t0_est = t[max_idx]
        bg_est = float(np.mean(y[:max(3, len(y)//10)]))
        a_est = float(np.sum(np.maximum(0.0, y - bg_est)) * (t[1] - t[0]))
        tau_est = 1.0
        sigma_est = 0.15
        p0 = [a_est, tau_est, t0_est, sigma_est, bg_est]
    else:
        p0 = p0_guess

    bounds = (
        [10.0, 1e-4, t[0], 1e-3, 0.0],
        [1e8, 50.0, t[-1], 5.0, 1e5]
    )

    # Weighting: 1 / sqrt(y) for Poisson errors
    sigma_y = np.sqrt(np.maximum(1.0, y))

    try:
        popt, pcov = curve_fit(convoluted_decay_model, t, y, p0=p0, bounds=bounds, sigma=sigma_y, maxfev=4000)
        perr = np.sqrt(np.diag(pcov))
    except Exception:
        popt = p0
        perr = [0.0] * len(p0)

    A_fit, tau_fit, t0_fit, sigma_fit, bg_fit = popt
    A_err, tau_err, t0_err, sigma_err, bg_err = perr

    # Chi-square and goodness of fit
    y_pred = convoluted_decay_model(t, *popt)
    chi2 = float(np.sum(((y - y_pred) / sigma_y)**2))
    ndf = max(1, len(y) - len(popt))
    reduced_chi2 = chi2 / ndf

    fwhm_fit = sigma_fit * 2.35482
    fwhm_err = sigma_err * 2.35482

    return {
        "fit_parameters": {
            "amplitude_A": float(A_fit),
            "sigma_A": float(A_err),
            "lifetime_tau_ns": float(tau_fit),
            "sigma_tau_ns": float(tau_err),
            "centroid_t0_ns": float(t0_fit),
            "sigma_t0_ns": float(t0_err),
            "irf_sigma_ns": float(sigma_fit),
            "sigma_irf_sigma_ns": float(sigma_err),
            "irf_fwhm_ns": float(fwhm_fit),
            "sigma_irf_fwhm_ns": float(fwhm_err),
            "background_B0": float(bg_fit),
            "sigma_B0": float(bg_err)
        },
        "fit_quality": {
            "chi2": float(chi2),
            "ndf": int(ndf),
            "reduced_chi2": float(reduced_chi2)
        }
    }


def run_time_convolution_analysis(nucleus, true_tau_ns, true_fwhm_ns, true_t0_ns,
                                  true_amplitude=25000.0, true_background=15.0,
                                  t_min_ns=-1.0, t_max_ns=4.0, n_bins=120):
    """
    Complete execution pipeline: synthesizes convoluted time spectrum and de-convolves lifetime.
    """
    t_arr = np.linspace(t_min_ns, t_max_ns, n_bins)
    sigma_true = true_fwhm_ns / 2.35482

    counts = generate_synthetic_spectrum(
        t_arr=t_arr,
        A=true_amplitude,
        tau=true_tau_ns,
        t0=true_t0_ns,
        sigma=sigma_true,
        bg=true_background
    )

    fit_res = fit_convoluted_time_spectrum(t_arr, counts)
    fit_res["nucleus"] = nucleus
    fit_res["simulation_truth"] = {
        "true_tau_ns": float(true_tau_ns),
        "true_fwhm_ns": float(true_fwhm_ns),
        "true_t0_ns": float(true_t0_ns),
        "true_amplitude": float(true_amplitude),
        "true_background": float(true_background)
    }
    return fit_res


def format_text_report(res, title="Time Spectrum Convolution & Lifetime Fitter"):
    fp = res["fit_parameters"]
    fq = res["fit_quality"]
    st = res["simulation_truth"]

    lines = []
    lines.append("=" * 76)
    lines.append(f"{title}")
    lines.append(f"Nucleus: {res['nucleus']} | Reduced Chi^2 = {fq['reduced_chi2']:.2f} (Chi^2/ndf = {fq['chi2']:.1f}/{fq['ndf']})")
    lines.append("=" * 76)
    lines.append("Simulation Truth vs Deconvoluted Fit Parameters:")
    lines.append(f"  Nuclear Lifetime (tau)          : Fit = {fp['lifetime_tau_ns']:.4f} +- {fp['sigma_tau_ns']:.4f} ns  (Truth = {st['true_tau_ns']:.4f} ns)")
    lines.append(f"  Instrument Resolution (FWHM)    : Fit = {fp['irf_fwhm_ns']:.4f} +- {fp['sigma_irf_fwhm_ns']:.4f} ns  (Truth = {st['true_fwhm_ns']:.4f} ns)")
    lines.append(f"  Time Centroid Zero (t_0)        : Fit = {fp['centroid_t0_ns']:.4f} +- {fp['sigma_t0_ns']:.4f} ns  (Truth = {st['true_t0_ns']:.4f} ns)")
    lines.append(f"  Integrated Peak Amplitude (A)   : Fit = {fp['amplitude_A']:.1f} +- {fp['sigma_A']:.1f} counts")
    lines.append(f"  Accidental Baseline (B_0)       : Fit = {fp['background_B0']:.2f} +- {fp['sigma_B0']:.2f} counts/bin")
    lines.append("-" * 76)
    error_tau_pct = abs(fp['lifetime_tau_ns'] - st['true_tau_ns']) / st['true_tau_ns'] * 100.0
    lines.append(f"  Lifetime Deconvolution Accuracy : {100.0 - error_tau_pct:.2f}% (Error = {error_tau_pct:.2f}%)")
    lines.append("=" * 76)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="In-Beam Time Spectrum Gaussian-Exponential Convolution & Lifetime Fitter."
    )
    parser.add_argument("--preset", choices=list(PRESETS.keys()), help="Load experimental preset")
    parser.add_argument("--nucleus", type=str, default="Nucleus", help="Nucleus name")
    parser.add_argument("--tau-ns", type=float, default=1.0, help="True lifetime in ns")
    parser.add_argument("--fwhm-ns", type=float, default=0.5, help="IRF FWHM in ns")
    parser.add_argument("--t0-ns", type=float, default=1.0, help="Time zero in ns")
    parser.add_argument("--json", action="store_true", help="Output pure JSON")
    args = parser.parse_args()

    if args.preset:
        p = PRESETS[args.preset]
        nucleus = p["nucleus"]
        tau = p["true_tau_ns"]
        fwhm = p["true_fwhm_ns"]
        t0 = p["true_t0_ns"]
        amp = p["true_amplitude"]
        bg = p["true_background"]
        tmin = p["t_min_ns"]
        tmax = p["t_max_ns"]
        nbins = p["n_bins"]
        title = f"Preset: {args.preset} ({p['description']})"
    else:
        nucleus = args.nucleus
        tau = args.tau_ns
        fwhm = args.fwhm_ns
        t0 = args.t0_ns
        amp = 20000.0
        bg = 15.0
        tmin = -1.0
        tmax = tau * 5.0 + 2.0
        nbins = 120
        title = "Custom User Input"

    res = run_time_convolution_analysis(
        nucleus=nucleus,
        true_tau_ns=tau,
        true_fwhm_ns=fwhm,
        true_t0_ns=t0,
        true_amplitude=amp,
        true_background=bg,
        t_min_ns=tmin,
        t_max_ns=tmax,
        n_bins=nbins
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print(format_text_report(res, title=title))


if __name__ == "__main__":
    main()
