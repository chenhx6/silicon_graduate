#!/usr/bin/env python3
"""
Unit tests for cranked_triaxial_shape_coexistence_pes_engine.py (Module 160).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from cranked_triaxial_shape_coexistence_pes_engine import (
    PRESETS,
    CrankedShapeCoexistencePESEngine
)

class TestCrankedShapeCoexistencePES(unittest.TestCase):

    def test_130Ba_shape_crossing_detection(self):
        p = PRESETS["130Ba_triaxial_oblate_coexistence"]
        engine = CrankedShapeCoexistencePESEngine(
            C2=p["C2"], C3=p["C3"], C4=p["C4"],
            J0=p["J0"], beta0=p["beta0"],
            shell_minima=p["shell_minima"]
        )
        res = engine.evaluate_frequency_evolution(p["eval_frequencies_MeV"])
        # Shape transition should be detected
        self.assertTrue(res["has_shape_transition"])
        # Crossing frequency should be in range 0.15 - 0.35 MeV/hbar
        w_cross = res["critical_crossing_frequency_omega_cross_MeV"]
        self.assertGreater(w_cross, 0.15)
        self.assertLess(w_cross, 0.35)

    def test_zero_frequency_oblate_ground_state(self):
        p = PRESETS["130Ba_triaxial_oblate_coexistence"]
        engine = CrankedShapeCoexistencePESEngine(
            C2=p["C2"], C3=p["C3"], C4=p["C4"],
            J0=p["J0"], beta0=p["beta0"],
            shell_minima=p["shell_minima"]
        )
        min_info = engine.find_coexisting_minima(0.0)
        # At zero spin, oblate shape is yrast
        self.assertEqual(min_info["yrast_shape"], "Oblate")
        self.assertLess(min_info["energy_difference_E2_minus_E1_MeV"], 0.0)
        # Both minima must have positive barriers to saddle point
        self.assertGreater(min_info["barrier_height_from_min1_MeV"], 0.1)
        self.assertGreater(min_info["barrier_height_from_min2_MeV"], 0.1)

    def test_high_spin_triaxial_stabilization(self):
        p = PRESETS["130Ba_triaxial_oblate_coexistence"]
        engine = CrankedShapeCoexistencePESEngine(
            C2=p["C2"], C3=p["C3"], C4=p["C4"],
            J0=p["J0"], beta0=p["beta0"],
            shell_minima=p["shell_minima"]
        )
        min_info = engine.find_coexisting_minima(0.35)
        # At omega = 0.35 MeV, triaxial shape becomes yrast
        self.assertEqual(min_info["yrast_shape"], "Triaxial/Prolate")
        self.assertGreater(min_info["energy_difference_E2_minus_E1_MeV"], 0.0)

    def test_synthetic_provenance_labels(self):
        for name, p in PRESETS.items():
            self.assertEqual(p.get("data_kind"), "synthetic_model_benchmark")

if __name__ == "__main__":
    unittest.main()
