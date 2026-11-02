#!/usr/bin/env python3
"""
Unit tests for multiphonon_wobbling_anharmonic_spectrum_solver.py (Module 166).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from multiphonon_wobbling_anharmonic_spectrum_solver import (
    PRESETS,
    MultiphononWobblingSolver
)

class TestMultiphononWobblingAnharmonic(unittest.TestCase):

    def test_harmonic_limit_behavior(self):
        # When g4 = 0 and mixing_eps = 0, R_21 must equal 2.000 exactly
        solver = MultiphononWobblingSolver(
            spin=20.0,
            hbar_omega_w_keV=300.0,
            g4_anharmonicity_keV=0.0,
            mixing_epsilon=0.0,
            B_E2_in_e2b2=5.0
        )
        res = solver.solve_multiphonon_properties()
        self.assertAlmostEqual(res["energy_ratio_R21"], 2.000, places=4)
        self.assertAlmostEqual(res["electromagnetic_rates"]["branching_ratio_BE2_20_over_21"], 0.0, places=4)

    def test_163Lu_two_phonon_softening(self):
        p = PRESETS["163Lu_TSD2_two_phonon_benchmark"]
        solver = MultiphononWobblingSolver(
            spin=p["spin"],
            hbar_omega_w_keV=p["hbar_omega_w_keV"],
            g4_anharmonicity_keV=p["g4_anharmonicity_keV"],
            mixing_epsilon=p["mixing_epsilon"],
            B_E2_in_e2b2=p["B_E2_in_e2b2"]
        )
        res = solver.solve_multiphonon_properties()
        # R_21 should show softening (1.5 - 1.9)
        self.assertGreater(res["energy_ratio_R21"], 1.50)
        self.assertLess(res["energy_ratio_R21"], 1.90)
        # Direct Delta n=2 branching should be finite (> 5%)
        self.assertGreater(res["electromagnetic_rates"]["branching_ratio_BE2_20_over_21"], 0.05)
        self.assertTrue(res["is_two_phonon_confirmed"])

    def test_135Pr_two_phonon_consistency(self):
        p = PRESETS["135Pr_normal_deformed_two_phonon"]
        solver = MultiphononWobblingSolver(
            spin=p["spin"],
            hbar_omega_w_keV=p["hbar_omega_w_keV"],
            g4_anharmonicity_keV=p["g4_anharmonicity_keV"],
            mixing_epsilon=p["mixing_epsilon"],
            B_E2_in_e2b2=p["B_E2_in_e2b2"]
        )
        res = solver.solve_multiphonon_properties()
        self.assertTrue(res["is_two_phonon_confirmed"])
        self.assertGreater(res["electromagnetic_rates"]["B_E2_2_to_0_e2b2"], 0.01)

if __name__ == "__main__":
    unittest.main()
