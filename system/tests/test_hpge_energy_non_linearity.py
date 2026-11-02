#!/usr/bin/env python3
"""
Unit tests for hpge_energy_non_linearity_inl_dnl_calibrator.py
"""

import sys
import unittest
import numpy as np
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from hpge_energy_non_linearity_inl_dnl_calibrator import (
    PRESETS,
    fit_energy_polynomial,
    evaluate_calibrated_energy,
    run_non_linearity_analysis
)


class TestHPGeEnergyNonLinearity(unittest.TestCase):

    def test_polynomial_fitting_residuals(self):
        p = PRESETS["16_point_standard_multisource_benchmark"]
        chs = [l["channel"] for l in p["calibration_lines"]]
        es = [l["energy_lit_keV"] for l in p["calibration_lines"]]
        sigs = [l["sigma_E_keV"] for l in p["calibration_lines"]]

        fit_poly = fit_energy_polynomial(chs, es, sigs, degree=3, ch_center=4000.0)
        self.assertEqual(len(fit_poly["parameters"]), 4)
        self.assertEqual(len(fit_poly["residuals_keV"]), 16)
        # RMS polynomial residual should be small (< 0.2 keV)
        rms_res = float(np.sqrt(np.mean(np.array(fit_poly["residuals_keV"])**2)))
        self.assertLess(rms_res, 0.20)

    def test_16_point_benchmark_pipeline(self):
        p = PRESETS["16_point_standard_multisource_benchmark"]
        res = run_non_linearity_analysis(
            detector=p["detector"],
            lines=p["calibration_lines"],
            query_channels=p["query_channels"],
            poly_degree=p["poly_degree"],
            ch_center=p["channel_center"]
        )
        cm = res["comparison_metrics"]
        # Polynomial fit should drastically improve over linear fit
        self.assertLess(cm["polynomial_fit_reduced_chi2"], cm["linear_fit_reduced_chi2"])
        self.assertGreater(cm["max_linear_calibration_bias_keV"], 0.20)
        self.assertEqual(len(res["query_evaluations"]), len(p["query_channels"]))

    def test_spline_exact_interpolation_at_nodes(self):
        p = PRESETS["16_point_standard_multisource_benchmark"]
        res = run_non_linearity_analysis(
            detector=p["detector"],
            lines=p["calibration_lines"][:6],
            query_channels=[186.2, 381.1],
            poly_degree=2,
            ch_center=1000.0
        )
        # At calibration nodes, final spline residual should be very close to zero (< 0.005 keV)
        for line in res["calibration_lines"]:
            self.assertAlmostEqual(line["final_residual_keV"], 0.0, places=3)


if __name__ == "__main__":
    unittest.main()
