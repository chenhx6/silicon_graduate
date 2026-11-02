#!/usr/bin/env python3
"""
Unit tests for chiral_vibrational_quartic_schrodinger_diagonalizer.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from chiral_vibrational_quartic_schrodinger_diagonalizer import (
    PRESETS,
    diagonalize_chiral_schrodinger,
    run_chiral_schrodinger_analysis
)


class TestChiralQuarticSchrodinger(unittest.TestCase):

    def test_harmonic_limit_energy_ladder(self):
        p = PRESETS["harmonic_vibrator_limit"]
        res = diagonalize_chiral_schrodinger(p["c2_MeV"], p["c4_MeV"], p["B_phi_hbar2_per_MeV"])
        evals = res["eigenvalues_rel_keV"]
        # In harmonic limit, E1 - E0 ~ hbar*omega and E2 - E0 ~ 2*hbar*omega
        hw = evals[1]
        self.assertAlmostEqual(evals[2] / hw, 2.06, delta=0.1)
        self.assertEqual(res["barrier_height_keV"], 0.0)
        self.assertFalse(res["is_double_well"])

    def test_135Nd_chiral_vibration(self):
        p = PRESETS["135Nd_chiral_vibration"]
        res = run_chiral_schrodinger_analysis(
            nucleus=p["nucleus"],
            c2_MeV=p["c2_MeV"],
            c4_MeV=p["c4_MeV"],
            B_phi=p["B_phi_hbar2_per_MeV"]
        )
        sr = res["schrodinger_results"]
        self.assertTrue(sr["is_double_well"])
        self.assertGreater(sr["barrier_height_keV"], 100.0)
        self.assertLess(sr["barrier_height_keV"], 250.0)
        # Chiral splitting should be > 200 keV (chiral vibration regime)
        self.assertGreater(sr["chiral_splitting_keV"], 200.0)

    def test_134Pr_deep_double_well_tunneling(self):
        p = PRESETS["134Pr_static_chiral_rotation"]
        res = run_chiral_schrodinger_analysis(
            nucleus=p["nucleus"],
            c2_MeV=p["c2_MeV"],
            c4_MeV=p["c4_MeV"],
            B_phi=p["B_phi_hbar2_per_MeV"]
        )
        sr = res["schrodinger_results"]
        self.assertGreater(sr["barrier_height_keV"], 500.0)
        # Splitting should collapse compared to 135Nd due to deep tunneling barrier
        self.assertLess(sr["chiral_splitting_keV"], 150.0)
        self.assertGreater(sr["anharmonic_ratio_R21"], 4.0)

    def test_dipole_matrix_element_parity_selection(self):
        p = PRESETS["135Nd_chiral_vibration"]
        res = diagonalize_chiral_schrodinger(p["c2_MeV"], p["c4_MeV"], p["B_phi_hbar2_per_MeV"])
        # Dipole matrix element <0|sin(phi)|1> between even and odd states must be non-zero
        self.assertGreater(res["dipole_matrix_element_M01"], 0.10)


if __name__ == "__main__":
    unittest.main()
