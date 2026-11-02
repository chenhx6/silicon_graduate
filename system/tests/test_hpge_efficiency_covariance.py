#!/usr/bin/env python3
"""
Unit tests for hpge_efficiency_curve_covariance_fitter.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from hpge_efficiency_curve_covariance_fitter import (
    PRESETS,
    fit_efficiency_curve_wls,
    evaluate_efficiency_with_covariance,
    run_efficiency_analysis
)


class TestHPGeEfficiencyCovariance(unittest.TestCase):

    def test_clover_152Eu_wls_fit(self):
        p = PRESETS["clover_detector_152Eu_calibration"]
        fit_res = fit_efficiency_curve_wls(p["calibration_points"], poly_order=3, E0_keV=1000.0)
        self.assertEqual(len(fit_res["parameters"]), 4)
        self.assertLess(fit_res["reduced_chi2"], 1.5)
        self.assertAlmostEqual(fit_res["parameters"][0], -5.215, places=2)

    def test_efficiency_evaluation_and_covariance_propagation(self):
        p = PRESETS["clover_detector_152Eu_calibration"]
        fit_res = fit_efficiency_curve_wls(p["calibration_points"], poly_order=3, E0_keV=1000.0)
        eval_pt = evaluate_efficiency_with_covariance(344.28, fit_res)
        # Interpolated value near 344 keV should match experimental point ~ 0.0135
        self.assertAlmostEqual(eval_pt["efficiency"], 0.0135, places=3)
        self.assertGreater(eval_pt["sigma_efficiency"], 0.0)
        self.assertLess(eval_pt["relative_error_pct"], 3.0)
        # Naive error should be substantially larger due to ignoring negative covariance
        self.assertGreater(eval_pt["covariance_overestimate_ratio"], 1.5)

    def test_broadband_coaxial_run_pipeline(self):
        p = PRESETS["broadband_coaxial_hpge_mixed_source"]
        res = run_efficiency_analysis(
            points=p["calibration_points"],
            query_energies=[121.8, 511.0, 1173.2],
            poly_order=4,
            E0_keV=1000.0,
            detector=p["detector"]
        )
        it = res["interpolated_transitions"]
        self.assertEqual(len(it), 3)
        self.assertGreater(it[0]["efficiency"], it[2]["efficiency"])
        self.assertLess(res["fit_results"]["reduced_chi2"], 1.0)

    def test_extreme_high_energy_extrapolation_uncertainty(self):
        p = PRESETS["clover_detector_152Eu_calibration"]
        fit_res = fit_efficiency_curve_wls(p["calibration_points"], poly_order=3, E0_keV=1000.0)
        # Extrapolating to 3000 keV should yield positive efficiency and expanding uncertainty
        eval_high = evaluate_efficiency_with_covariance(3000.0, fit_res)
        eval_mid = evaluate_efficiency_with_covariance(600.0, fit_res)
        self.assertLess(eval_high["efficiency"], eval_mid["efficiency"])
        self.assertGreater(eval_high["relative_error_pct"], eval_mid["relative_error_pct"])


if __name__ == "__main__":
    unittest.main()
