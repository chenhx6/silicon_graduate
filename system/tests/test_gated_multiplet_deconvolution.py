#!/usr/bin/env python3
"""
Unit tests for in_beam_gated_matrix_multiplet_deconvolution_fitter.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_gated_matrix_multiplet_deconvolution_fitter import (
    PRESETS,
    multiplet_model_function,
    generate_synthetic_gated_spectrum,
    fit_gated_multiplet,
    run_multiplet_analysis
)


class TestGatedMultipletDeconvolution(unittest.TestCase):

    def test_multiplet_model_evaluation(self):
        E = [638.0, 640.0, 642.0]
        # 2 peaks: A1=1000, E1=638, A2=800, E2=641, sigma=0.9, b0=10, b1=0
        params = [1000.0, 638.0, 800.0, 641.0, 0.9, 10.0, 0.0]
        y = multiplet_model_function(E, *params)
        self.assertEqual(len(y), 3)
        self.assertGreater(y[0], 100.0)
        self.assertGreater(y[2], 100.0)

    def test_133Ce_doublet_deconvolution(self):
        p = PRESETS["133Ce_wobbling_candidate_doublet"]
        res = run_multiplet_analysis(
            peaks=p["true_peaks"],
            fwhm_nominal=p["fwhm_nominal_keV"],
            bkg_level=p["background_level"],
            E_min=p["E_min_keV"],
            E_max=p["E_max_keV"],
            bin_width=p["bin_width_keV"],
            nucleus=p["nucleus"]
        )
        self.assertEqual(len(res["peaks"]), 2)
        p1 = res["peaks"][0]
        p2 = res["peaks"][1]
        self.assertAlmostEqual(p1["energy_keV"], 638.2, places=1)
        self.assertAlmostEqual(p2["energy_keV"], 641.4, places=1)
        self.assertLess(abs(p1["area"] - 12500.0) / 12500.0, 0.05)
        self.assertLess(abs(p2["area"] - 8400.0) / 8400.0, 0.05)
        self.assertLess(res["metrics"]["reduced_chi2"], 1.5)

    def test_triplet_deconvolution(self):
        p = PRESETS["130Ba_two_quasiparticle_triplet"]
        res = run_multiplet_analysis(
            peaks=p["true_peaks"],
            fwhm_nominal=p["fwhm_nominal_keV"],
            bkg_level=p["background_level"],
            E_min=p["E_min_keV"],
            E_max=p["E_max_keV"],
            bin_width=p["bin_width_keV"],
            nucleus=p["nucleus"]
        )
        self.assertEqual(len(res["peaks"]), 3)
        self.assertLess(res["metrics"]["reduced_chi2"], 1.5)

    def test_single_peak_calibration(self):
        p = PRESETS["isolated_single_peak_benchmark"]
        res = run_multiplet_analysis(
            peaks=p["true_peaks"],
            fwhm_nominal=p["fwhm_nominal_keV"],
            bkg_level=p["background_level"],
            E_min=p["E_min_keV"],
            E_max=p["E_max_keV"],
            bin_width=p["bin_width_keV"],
            nucleus=p["nucleus"]
        )
        self.assertEqual(len(res["peaks"]), 1)
        self.assertAlmostEqual(res["peaks"][0]["energy_keV"], 1332.5, places=1)


if __name__ == "__main__":
    unittest.main()
