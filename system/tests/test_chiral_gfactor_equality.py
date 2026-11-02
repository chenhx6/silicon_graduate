#!/usr/bin/env python3
"""
Unit tests for Chiral Doublet g-Factor Equality Theorem & Arbitrator (Module 128).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from chiral_doublet_g_factor_equality_calculator import (
    calculate_theoretical_chiral_gfactor,
    arbitrate_chiral_gfactor_equality,
    run_chiral_gfactor_analysis,
    PRESETS
)


class TestChiralGFactorEquality(unittest.TestCase):

    def test_theoretical_gfactor_calculation(self):
        theo = calculate_theoretical_chiral_gfactor(A_mass=128, Z_charge=55, spin_I=11.0, j_p=5.5, j_n=5.5)
        self.assertAlmostEqual(theo["g_R_core"], 55.0/128.0, places=3)
        self.assertGreater(theo["g_proton_term"], 0.0)
        self.assertLess(theo["g_neutron_term"], 0.0)
        self.assertGreater(theo["g_chiral_theoretical"], 0.40)
        self.assertLess(theo["g_chiral_theoretical"], 0.60)

    def test_equality_confirmation(self):
        arb = arbitrate_chiral_gfactor_equality(g1=0.58, sigma1=0.04, g2=0.56, sigma2=0.05)
        self.assertEqual(arb["status"], "chiral_equality_confirmed")
        self.assertLess(arb["chi2_g"], 1.0)
        self.assertGreater(arb["p_value"], 0.30)

    def test_rejection_of_spurious_doublet(self):
        arb = arbitrate_chiral_gfactor_equality(g1=0.85, sigma1=0.04, g2=0.32, sigma2=0.05)
        self.assertEqual(arb["status"], "chiral_equality_definitively_rejected")
        self.assertGreater(arb["chi2_g"], 9.0)
        self.assertLess(arb["p_value"], 0.003)

    def test_run_chiral_gfactor_preset(self):
        p = PRESETS["128Cs_chiral_doublet_benchmark"]
        res = run_chiral_gfactor_analysis(
            p["nucleus"], p["A_mass"], p["Z_charge"], p["spin_I"],
            p["j_proton"], p["j_neutron"],
            p["g1_measured"], p["sigma_g1"], p["g2_measured"], p["sigma_g2"]
        )
        self.assertEqual(res["arbitration"]["status"], "chiral_equality_confirmed")


if __name__ == "__main__":
    unittest.main()
