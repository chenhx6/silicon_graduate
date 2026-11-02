#!/usr/bin/env python3
"""
Unit tests for In-Beam Fast-Timing Generalized Centroid Difference (GCD) Method (Module 127).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from in_beam_fast_timing_gcd_lifetime_calculator import (
    calculate_prf_walk,
    calculate_gcd_lifetime,
    invert_transition_strengths,
    run_fast_timing_gcd_analysis,
    PRESETS
)


class TestFastTimingGCD(unittest.TestCase):

    def test_prf_walk_monotonicity(self):
        w_low = calculate_prf_walk(E_gamma_keV=300.0)
        w_high = calculate_prf_walk(E_gamma_keV=1200.0)
        # Low energy has larger walk (slower trigger)
        self.assertGreater(w_low, w_high)

    def test_gcd_lifetime_inversion(self):
        # True lifetime 50 ps, E_feed=600 keV, E_decay=400 keV
        w_feed = calculate_prf_walk(600.0)
        w_decay = calculate_prf_walk(400.0)
        delta_w = w_feed - w_decay
        # C1 = delta_w + tau, C2 = -delta_w - tau
        c1 = delta_w + 50.0
        c2 = -delta_w - 50.0
        res = calculate_gcd_lifetime(C1_ps=c1, C2_ps=c2, sigma_C1_ps=1.0, sigma_C2_ps=1.0,
                                     E_feed_keV=600.0, E_decay_keV=400.0)
        self.assertAlmostEqual(res["tau_extracted_ps"], 50.0, places=3)
        self.assertAlmostEqual(res["sigma_tau_ps"], np.sqrt(2.0)/2.0, places=3)

    def test_strength_inversion(self):
        st = invert_transition_strengths(tau_ps=100.0, sigma_tau_ps=2.0, E_decay_keV=500.0, A_mass=134)
        self.assertIsNotNone(st)
        self.assertGreater(st["T_total_s"], 1e9)
        self.assertGreater(st["B_M1_Wu"], 0.0)

    def test_run_gcd_preset(self):
        p = PRESETS["134Ce_fast_timing_2plus"]
        res = run_fast_timing_gcd_analysis(
            nucleus=p["nucleus"],
            A_mass=p["A_mass"],
            E_feed_keV=p["E_feed_keV"],
            E_decay_keV=p["E_decay_keV"],
            C1_ps=p["C1_ps"],
            sigma_C1_ps=p["sigma_C1_ps"],
            C2_ps=p["C2_ps"],
            sigma_C2_ps=p["sigma_C2_ps"],
            a0_walk=p["a0_walk"],
            c0_walk=p["c0_walk"]
        )
        self.assertGreater(res["gcd_analysis"]["tau_extracted_ps"], 50.0)
        self.assertLess(res["gcd_analysis"]["tau_extracted_ps"], 120.0)


if __name__ == "__main__":
    unittest.main()
