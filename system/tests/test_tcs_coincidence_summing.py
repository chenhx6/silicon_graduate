#!/usr/bin/env python3
"""
Unit tests for In-Beam True Coincidence Summing (TCS) Correction Suite (Module 129).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from in_beam_true_coincidence_summing_tcs_calculator import (
    calculate_total_efficiency,
    calculate_tcs_corrections,
    run_tcs_analysis,
    PRESETS
)


class TestTCSCoincidenceSumming(unittest.TestCase):

    def test_total_efficiency_scaling(self):
        eps_t = calculate_total_efficiency(peak_eff=0.025, pt_ratio=0.25)
        self.assertAlmostEqual(eps_t, 0.10, places=4)
        self.assertGreater(eps_t, 0.025)

    def test_summing_out_factor(self):
        pairs = [{"E_target_keV": 1000.0, "E_coincident_keV": 500.0, "branching": 1.0}]
        p_eff = {1000.0: 0.03, 500.0: 0.04}
        pt = {1000.0: 0.25, 500.0: 0.20}
        res = calculate_tcs_corrections(pairs, p_eff, pt, W0=1.0, total_decays=1e5)
        corr = res["summing_out_corrections"][0]
        self.assertAlmostEqual(corr["coincident_total_efficiency"], 0.20, places=3)
        self.assertAlmostEqual(corr["correction_factor_C_out"], 1.25, places=3)
        self.assertAlmostEqual(corr["summing_out_loss_percent"], 20.0, places=2)

    def test_summing_in_peak(self):
        pairs = [
            {"E_target_keV": 1173.2, "E_coincident_keV": 1332.5, "branching": 1.0},
            {"E_target_keV": 1332.5, "E_coincident_keV": 1173.2, "branching": 1.0}
        ]
        p_eff = {1173.2: 0.025, 1332.5: 0.022}
        pt = {1173.2: 0.22, 1332.5: 0.20}
        res = calculate_tcs_corrections(pairs, p_eff, pt, W0=1.0, total_decays=1e6)
        self.assertEqual(len(res["summing_in_peaks"]), 1)
        sum_pk = res["summing_in_peaks"][0]
        self.assertAlmostEqual(sum_pk["E_sum_peak_keV"], 2505.7, places=1)
        self.assertAlmostEqual(sum_pk["sum_in_yield_counts"], 550.0, places=1)

    def test_run_tcs_preset(self):
        p = PRESETS["60Co_close_geometry_clover"]
        res = run_tcs_analysis(
            p["nucleus"], p["cascade_pairs"], p["peak_efficiencies"],
            p["pt_ratios"], p["W0_correlation"], p["total_decays"]
        )
        self.assertEqual(len(res["summing_out_corrections"]), 2)
        for c in res["summing_out_corrections"]:
            self.assertGreater(c["correction_factor_C_out"], 1.10)


if __name__ == "__main__":
    unittest.main()
