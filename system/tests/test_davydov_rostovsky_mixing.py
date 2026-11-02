#!/usr/bin/env python3
"""
Unit tests for davydov_rostovsky_triaxial_band_mixing_solver.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from davydov_rostovsky_triaxial_band_mixing_solver import (
    PRESETS,
    invert_gamma_mixing_parameter,
    calculate_davydov_rostovsky_parameters,
    run_davydov_rostovsky_analysis
)


class TestDavydovRostovskyMixing(unittest.TestCase):

    def test_alaga_rigid_limit(self):
        p = PRESETS["rigid_rotor_zero_mixing_limit"]
        res = run_davydov_rostovsky_analysis(
            nucleus=p["nucleus"],
            E_2g=p["E_2g_keV"],
            E_4g=p["E_4g_keV"],
            E_2gamma=p["E_2gamma_keV"],
            E_0beta=p["E_0beta_keV"],
            exp_ratio=p["exp_be2_gamma_ratio"]
        )
        m = res["mixing_results"]
        self.assertAlmostEqual(m["z_gamma_mixing_parameter"], 0.0, places=4)
        self.assertAlmostEqual(m["coupling_matrix_element_h2_keV"], 0.0, places=4)
        self.assertAlmostEqual(m["alaga_suppression_pct"], 0.0, places=3)

    def test_152Sm_classic_transitional(self):
        p = PRESETS["152Sm_classic_transitional_nucleus"]
        res = run_davydov_rostovsky_analysis(
            nucleus=p["nucleus"],
            E_2g=p["E_2g_keV"],
            E_4g=p["E_4g_keV"],
            E_2gamma=p["E_2gamma_keV"],
            E_0beta=p["E_0beta_keV"],
            exp_ratio=p["exp_be2_gamma_ratio"]
        )
        m = res["mixing_results"]
        # z_gamma should be around +0.042
        self.assertAlmostEqual(m["z_gamma_mixing_parameter"], 0.0423, places=3)
        self.assertGreater(m["coupling_matrix_element_h2_keV"], 10.0)
        self.assertGreater(m["alaga_suppression_pct"], 20.0)

    def test_inversion_monotonicity(self):
        z_low = invert_gamma_mixing_parameter(0.65)
        z_high = invert_gamma_mixing_parameter(0.45)
        # Lower branching ratio corresponds to larger mixing z_gamma
        self.assertGreater(z_high, z_low)
        self.assertGreater(z_low, 0.0)


if __name__ == "__main__":
    unittest.main()
