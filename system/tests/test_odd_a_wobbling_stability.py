#!/usr/bin/env python3
"""
Unit tests for odd_a_transverse_longitudinal_wobbling_stability_solver.py (Module 158).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from odd_a_transverse_longitudinal_wobbling_stability_solver import (
    PRESETS,
    OddAWobblingStabilitySolver
)

class TestOddAWobblingStability(unittest.TestCase):

    def test_transverse_wobbling_decreasing_frequency(self):
        p = PRESETS["135Pr_transverse_rigid_stable"]
        solver = OddAWobblingStabilitySolver(
            wobbling_mode=p["wobbling_mode"],
            inertia_model=p["inertia_model"],
            j_qp=p["j_quasiparticle"],
            k_att=p["k_coriolis_attenuation"],
            gamma_deg=p["gamma_deg"],
            moi_i=p["moi_i"]
        )
        res = solver.evaluate_spin_series([8.5, 10.5, 12.5])
        # TW frequency must decrease with spin (negative slope)
        self.assertLess(res["frequency_slope_dOmega_dI"], 0.0)
        self.assertTrue(res["mode_confirmed"])
        # B(E2) ratio must be non-zero and reasonable (< 0.5)
        self.assertGreater(res["spin_trajectory"][0]["BE2_out_in_ratio"], 0.01)
        self.assertLess(res["spin_trajectory"][0]["BE2_out_in_ratio"], 0.5)

    def test_longitudinal_wobbling_increasing_frequency(self):
        p = PRESETS["187Au_longitudinal_wobbling"]
        solver = OddAWobblingStabilitySolver(
            wobbling_mode=p["wobbling_mode"],
            inertia_model=p["inertia_model"],
            j_qp=p["j_quasiparticle"],
            k_att=p["k_coriolis_attenuation"],
            gamma_deg=p["gamma_deg"],
            moi_i=p["moi_i"]
        )
        res = solver.evaluate_spin_series([11.5, 13.5, 15.5, 17.5])
        # LW frequency must increase with spin (positive slope)
        self.assertGreater(res["frequency_slope_dOmega_dI"], 0.0)
        self.assertTrue(res["mode_confirmed"])

    def test_hydrodynamic_premature_instability(self):
        p = PRESETS["135Pr_transverse_hydro_unstable"]
        solver = OddAWobblingStabilitySolver(
            wobbling_mode=p["wobbling_mode"],
            inertia_model=p["inertia_model"],
            j_qp=p["j_quasiparticle"],
            k_att=p["k_coriolis_attenuation"],
            gamma_deg=p["gamma_deg"],
            moi_i=p["moi_i"]
        )
        res = solver.evaluate_spin_series([8.5, 12.5, 16.5])
        # At high spin (16.5h), hydrodynamic TW must be unstable
        self.assertFalse(res["spin_trajectory"][2]["is_stable"])

if __name__ == "__main__":
    unittest.main()
