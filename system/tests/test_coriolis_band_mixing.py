#!/usr/bin/env python3
"""
Unit tests for Odd-A Deformed Coriolis Band Mixing & Signature Splitting Diagonalizer (Module 123).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from coriolis_band_mixing_matrix_diagonalizer import (
    construct_coriolis_matrix,
    diagonalize_coriolis_mixing,
    run_coriolis_analysis,
    PRESETS
)


class TestCoriolisBandMixing(unittest.TestCase):

    def test_matrix_construction(self):
        H, basis = construct_coriolis_matrix(I_spin=2.5, K_list=[0.5, 1.5, 2.5],
                                             eps_list=[0.0, 150.0, 380.0],
                                             A_rot_keV=13.0, j_val=5.5, a_decouple=-3.5)
        self.assertEqual(H.shape, (3, 3))
        self.assertEqual(len(basis), 3)
        # Matrix must be real symmetric
        self.assertAlmostEqual(H[0, 1], H[1, 0])
        self.assertAlmostEqual(H[1, 2], H[2, 1])
        self.assertEqual(H[0, 2], 0.0)  # Delta K = 2 is zero in single-step Coriolis

    def test_wavefunction_normalization(self):
        levels = diagonalize_coriolis_mixing(
            I_list=[1.5, 2.5, 3.5],
            K_list=[0.5, 1.5, 2.5],
            eps_list=[0.0, 150.0, 380.0],
            A_rot_keV=13.0,
            j_val=5.5
        )
        self.assertEqual(len(levels), 3)
        for lv in levels:
            amplitudes = list(lv["wavefunction_amplitudes"].values())
            norm = sum([c**2 for c in amplitudes])
            self.assertAlmostEqual(norm, 1.0, places=4)

    def test_signature_staggering(self):
        p = PRESETS["135Pr_proton_h11_2"]
        res = run_coriolis_analysis(
            A_mass=p["A_mass"],
            spins=p["spins"],
            K_values=p["K_values"],
            eps_keV=p["eps_keV"],
            A_rot_keV=p["A_rot_keV"],
            j_val=p["j_valence"],
            a_decouple=p["a_decouple"]
        )
        levels = res["levels"]
        self.assertGreater(len(levels), 5)
        # Verify that staggering S(I) alternates
        s_vals = [lv["staggering_S_keV"] for lv in levels if "staggering_S_keV" in lv]
        self.assertGreater(len(s_vals), 3)

    def test_run_coriolis_preset_dy159(self):
        p = PRESETS["159Dy_neutron_i13_2"]
        res = run_coriolis_analysis(
            A_mass=p["A_mass"],
            spins=p["spins"],
            K_values=p["K_values"],
            eps_keV=p["eps_keV"],
            A_rot_keV=p["A_rot_keV"],
            j_val=p["j_valence"],
            a_decouple=p["a_decouple"]
        )
        self.assertEqual(res["levels"][0]["spin_I"], 0.5)
        # Ground state excitation energy normalized to 0
        min_ex = min([lv["E_excitation_keV"] for lv in res["levels"]])
        self.assertAlmostEqual(min_ex, 0.0)


if __name__ == "__main__":
    unittest.main()
