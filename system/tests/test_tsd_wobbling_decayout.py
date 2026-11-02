#!/usr/bin/env python3
"""
Unit tests for triaxial_superdeformed_wobbling_decayout_analyzer.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from triaxial_superdeformed_wobbling_decayout_analyzer import (
    PRESETS,
    calculate_transition_widths_and_tunneling,
    evaluate_decayout_threshold,
    run_tsd_decayout_analysis
)


class TestTSDWobblingDecayout(unittest.TestCase):

    def test_transition_widths_high_spin_retention(self):
        p = PRESETS["163Lu_TSD2_wobbling_decayout"]
        res = calculate_transition_widths_and_tunneling(p["transitions"], p["barrier_params"])
        self.assertEqual(len(res), len(p["transitions"]))
        # At highest spin (39.5 hbar), in-TSD branching should dominate
        top = res[0]
        self.assertGreater(top["branching_in"] + top["branching_wob"], 0.70)
        self.assertLess(top["branching_decayout"], 0.30)

    def test_transition_widths_low_spin_decayout(self):
        p = PRESETS["163Lu_TSD2_wobbling_decayout"]
        res = calculate_transition_widths_and_tunneling(p["transitions"], p["barrier_params"])
        # At lowest spin (15.5 hbar), decayout should dominate completely (> 99%)
        bottom = res[-1]
        self.assertGreater(bottom["branching_decayout"], 0.99)

    def test_163Lu_decayout_threshold(self):
        p = PRESETS["163Lu_TSD2_wobbling_decayout"]
        res = run_tsd_decayout_analysis(
            nucleus=p["nucleus"],
            deformation_params=p["deformation_params"],
            barrier_params=p["barrier_params"],
            transitions=p["transitions"]
        )
        th = res["decayout_threshold"]
        self.assertGreater(th["critical_decayout_spin_I50"], 30.0)
        self.assertLess(th["critical_decayout_spin_I50"], 39.0)
        self.assertGreater(th["max_wobbling_branching"], 0.03)

    def test_165Lu_delayed_decayout(self):
        p = PRESETS["165Lu_TSD2_wobbling_decayout"]
        res = run_tsd_decayout_analysis(
            nucleus=p["nucleus"],
            deformation_params=p["deformation_params"],
            barrier_params=p["barrier_params"],
            transitions=p["transitions"]
        )
        th = res["decayout_threshold"]
        self.assertGreater(th["critical_decayout_spin_I50"], 20.0)


if __name__ == "__main__":
    unittest.main()
