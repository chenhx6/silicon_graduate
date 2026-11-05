#!/usr/bin/env python3
"""
Unit tests for chiral_doublet_selection_rules_m1_staggering_arbitrator.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from chiral_doublet_selection_rules_m1_staggering_arbitrator import (
    PRESETS,
    calculate_m1_staggering,
    arbitrate_chiral_selection_rules,
    run_chiral_selection_analysis
)


class TestChiralSelectionRules(unittest.TestCase):

    def test_m1_staggering_calculation(self):
        p = PRESETS["128Cs_chiral_doublet_benchmark"]
        stag1 = calculate_m1_staggering(p["band1"])
        self.assertIn(13, stag1)
        self.assertIn(14, stag1)
        self.assertGreater(stag1[13], 1.0)
        self.assertLess(stag1[14], 1.0)

    def test_128Cs_chiral_rules_screening(self):
        p = PRESETS["128Cs_chiral_doublet_benchmark"]
        res = run_chiral_selection_analysis(
            nucleus=p["nucleus"],
            band1=p["band1"],
            band2=p["band2"],
            interband=p["interband_transitions"]
        )
        self.assertEqual(res["phase_match_fraction"], 1.0)
        self.assertLess(res["mean_be2_discrepancy_pct"], 10.0)
        self.assertLess(res["min_interband_bm1_muN2"], 0.05)
        self.assertEqual(res["selection_rule_verdict"], "selection-rule-screening-pass")
        self.assertIsNone(res["confidence_score_pct"])

    def test_134Pr_chiral_rules_screening(self):
        p = PRESETS["134Pr_chiral_doublet_benchmark"]
        res = run_chiral_selection_analysis(
            nucleus=p["nucleus"],
            band1=p["band1"],
            band2=p["band2"],
            interband=p["interband_transitions"]
        )
        self.assertGreaterEqual(res["heuristic_score_pct"], 80.0)
        self.assertIsNone(res["confidence_score_pct"])
        self.assertEqual(res["selection_rule_verdict"], "selection-rule-screening-pass")

    def test_135Nd_chiral_rules_screening(self):
        p = PRESETS["135Nd_chiral_doublet_benchmark"]
        res = run_chiral_selection_analysis(
            nucleus=p["nucleus"],
            band1=p["band1"],
            band2=p["band2"],
            interband=p["interband_transitions"]
        )
        self.assertEqual(res["phase_match_fraction"], 1.0)
        self.assertLess(res["mean_be2_discrepancy_pct"], 15.0)
        self.assertLess(res["min_interband_bm1_muN2"], 0.05)
        self.assertEqual(res["selection_rule_verdict"], "selection-rule-screening-pass")
        self.assertIsNone(res["confidence_score_pct"])

    def test_spurious_counterexample_rejected(self):
        p = PRESETS["spurious_out_of_phase_counterexample"]
        res = run_chiral_selection_analysis(
            nucleus=p["nucleus"],
            band1=p["band1"],
            band2=p["band2"],
            interband=p["interband_transitions"]
        )
        self.assertEqual(res["phase_match_fraction"], 0.0)
        self.assertEqual(res["selection_rule_verdict"], "selection-rule-screening-fail")


if __name__ == "__main__":
    unittest.main()
