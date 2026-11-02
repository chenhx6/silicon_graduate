#!/usr/bin/env python3
"""
Unit tests for In-Beam Time Spectrum Gaussian-Exponential Convolution Fitter (Module 132).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from in_beam_time_spectrum_convolution_fitter import (
    convoluted_decay_model,
    fit_convoluted_time_spectrum,
    run_time_convolution_analysis,
    PRESETS
)


class TestTimeSpectrumConvolution(unittest.TestCase):

    def test_model_shape_and_limits(self):
        t = np.linspace(-2.0, 8.0, 100)
        y = convoluted_decay_model(t, A=10000.0, tau=1.5, t0=1.0, sigma=0.3, bg=10.0)
        self.assertEqual(len(y), len(t))
        self.assertAlmostEqual(y[0], 10.0, delta=1.0)
        self.assertGreater(np.max(y), 1000.0)
        self.assertLess(y[-1], y[np.argmax(y)] * 0.1)

    def test_decay_rate_sensitivity(self):
        t_tail = 6.0
        y_fast = convoluted_decay_model(np.array([t_tail]), A=10000.0, tau=0.5, t0=1.0, sigma=0.2, bg=0.0)[0]
        y_slow = convoluted_decay_model(np.array([t_tail]), A=10000.0, tau=2.5, t0=1.0, sigma=0.2, bg=0.0)[0]
        self.assertLess(y_fast, y_slow)

    def test_fit_deconvolution(self):
        t_arr = np.linspace(-0.5, 4.0, 120)
        true_tau = 0.50
        true_sigma = 0.10
        y_ideal = convoluted_decay_model(t_arr, A=30000.0, tau=true_tau, t0=1.0, sigma=true_sigma, bg=15.0)
        res = fit_convoluted_time_spectrum(t_arr, y_ideal)
        fit_tau = res["fit_parameters"]["lifetime_tau_ns"]
        fit_sigma = res["fit_parameters"]["irf_sigma_ns"]
        self.assertAlmostEqual(fit_tau, true_tau, places=2)
        self.assertAlmostEqual(fit_sigma, true_sigma, places=2)
        self.assertLess(res["fit_quality"]["reduced_chi2"], 0.1)

    def test_run_time_convolution_preset(self):
        p = PRESETS["134Ce_fast_timing_cascade"]
        res = run_time_convolution_analysis(
            p["nucleus"], p["true_tau_ns"], p["true_fwhm_ns"], p["true_t0_ns"],
            p["true_amplitude"], p["true_background"], p["t_min_ns"], p["t_max_ns"], p["n_bins"]
        )
        fit_tau = res["fit_parameters"]["lifetime_tau_ns"]
        error_pct = abs(fit_tau - p["true_tau_ns"]) / p["true_tau_ns"] * 100.0
        self.assertLess(error_pct, 5.0)


if __name__ == "__main__":
    unittest.main()
