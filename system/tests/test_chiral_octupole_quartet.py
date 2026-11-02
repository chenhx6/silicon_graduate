#!/usr/bin/env python3
"""
Unit tests for Chiral-Octupole Dual Symmetry-Breaking Quartet Bands Analyzer (Module 130).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from chiral_octupole_quartet_bands_analyzer import (
    evaluate_quartet_properties,
    run_chiral_octupole_analysis,
    PRESETS
)


class TestChiralOctupoleQuartet(unittest.TestCase):

    def test_quartet_properties_calculation(self):
        spins = [8.0, 9.0, 10.0]
        p1 = [1850.0, 2260.0, 2730.0]
        p2 = [1920.0, 2330.0, 2795.0]
        n1 = [2050.0, 2440.0, 2890.0]
        n2 = [2115.0, 2500.0, 2945.0]
        res = evaluate_quartet_properties(spins, p1, p2, n1, n2)
        self.assertAlmostEqual(res["mean_chiral_splitting_pos_keV"], 68.33, places=1)
        self.assertAlmostEqual(res["mean_chiral_splitting_neg_keV"], 60.0, places=1)
        self.assertGreater(res["quartet_confidence_percent"], 50.0)

    def test_confirmation_78br(self):
        p = PRESETS["78Br_chiral_octupole_quartet"]
        res = evaluate_quartet_properties(p["spins"], p["E_pos1_keV"], p["E_pos2_keV"],
                                          p["E_neg1_keV"], p["E_neg2_keV"])
        self.assertTrue(res["is_chiral_octupole_confirmed"])
        self.assertGreaterEqual(res["quartet_confidence_percent"], 65.0)

    def test_rejection_counterexample(self):
        p = PRESETS["pseudo_quartet_counterexample"]
        res = evaluate_quartet_properties(p["spins"], p["E_pos1_keV"], p["E_pos2_keV"],
                                          p["E_neg1_keV"], p["E_neg2_keV"])
        self.assertFalse(res["is_chiral_octupole_confirmed"])
        self.assertLess(res["quartet_confidence_percent"], 50.0)

    def test_run_quartet_analysis(self):
        p = PRESETS["78Br_chiral_octupole_quartet"]
        out = run_chiral_octupole_analysis(
            p["nucleus"], p["A_mass"], p["Z_charge"], p["spins"],
            p["E_pos1_keV"], p["E_pos2_keV"], p["E_neg1_keV"], p["E_neg2_keV"]
        )
        self.assertTrue(out["quartet_evaluation"]["is_chiral_octupole_confirmed"])
        self.assertEqual(len(out["quartet_evaluation"]["levels"]), 5)


if __name__ == "__main__":
    unittest.main()
