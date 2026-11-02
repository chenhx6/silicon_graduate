#!/usr/bin/env python3
"""
Unit tests for In-Beam Gamma Cascade Deorientation Coefficients U_k(I1, I2, L)
& Attenuated Angular Distribution Engine (Module 121).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from cascade_deorientation_coefficient_uk_calculator import (
    calculate_single_step_uk,
    calculate_mixed_step_uk,
    evaluate_cascade_deorientation,
    PRESETS
)


class TestCascadeDeorientationUK(unittest.TestCase):

    def test_u0_probability_conservation(self):
        # U_0 must be identically 1.0
        u0_64 = calculate_single_step_uk(6.0, 4.0, L=2.0, k=0)
        u0_42 = calculate_single_step_uk(4.0, 2.0, L=2.0, k=0)
        u0_dipole = calculate_single_step_uk(5.5, 4.5, L=1.0, k=0)
        self.assertAlmostEqual(u0_64, 1.0, places=5)
        self.assertAlmostEqual(u0_42, 1.0, places=5)
        self.assertAlmostEqual(u0_dipole, 1.0, places=5)

    def test_u2_u4_attenuation_e2(self):
        u2_64 = calculate_single_step_uk(6.0, 4.0, L=2.0, k=2)
        u4_64 = calculate_single_step_uk(6.0, 4.0, L=2.0, k=4)
        self.assertAlmostEqual(u2_64, 0.9000, places=3)
        self.assertAlmostEqual(u4_64, 0.6861, places=3)
        self.assertGreater(u2_64, u4_64)

    def test_mixed_transition(self):
        u2_pure_m1 = calculate_single_step_uk(13.0, 12.0, L=1.0, k=2)
        u2_mixed = calculate_mixed_step_uk(13.0, 12.0, L=1.0, delta=-0.15, k=2)
        self.assertNotEqual(u2_pure_m1, u2_mixed)
        self.assertGreater(u2_mixed, 0.90)

    def test_cascade_attenuation_preset(self):
        p = PRESETS["yrast_stretched_e2_cascade"]
        res = evaluate_cascade_deorientation(p["steps"], a2_init=p["a2_initial"], a4_init=p["a4_initial"])
        self.assertAlmostEqual(res["total_U2"], 0.6742, places=3)
        self.assertAlmostEqual(res["total_U4"], 0.1953, places=3)
        self.assertLess(abs(res["a2_attenuated"]), abs(res["a2_initial"]))
        self.assertLess(abs(res["a4_attenuated"]), abs(res["a4_initial"]))


if __name__ == "__main__":
    unittest.main()
