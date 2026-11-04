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
            moi_m=p["moi_m"],
            moi_s=p["moi_s"],
            moi_l=p["moi_l"]
        )
        res = solver.evaluate_spin_series([8.5, 10.5, 12.5])
        # TW frequency must decrease with spin (negative slope)
        self.assertLess(res["frequency_slope_dOmega_dI"], 0.0)
        self.assertTrue(res["is_harmonic_stable"])
        # Mode confirmation is unassessed (None), adhering to scientific evidence boundary
        self.assertIsNone(res["mode_confirmed"])
        # Check critical spin matches Frauendorf 2025 formula: I_c = 5.5 / (1 - 13/21) = 14.44 hbar
        self.assertAlmostEqual(res["critical_spin_I_crit"], 14.4375, places=3)
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
            moi_m=p["moi_m"],
            moi_s=p["moi_s"],
            moi_l=p["moi_l"]
        )
        res = solver.evaluate_spin_series([11.5, 13.5, 15.5, 17.5])
        # LW frequency must increase with spin (positive slope)
        self.assertGreater(res["frequency_slope_dOmega_dI"], 0.0)
        self.assertTrue(res["is_harmonic_stable"])
        self.assertIsNone(res["mode_confirmed"])

    def test_hydrodynamic_premature_instability(self):
        p = PRESETS["135Pr_transverse_hydro_unstable"]
        solver = OddAWobblingStabilitySolver(
            wobbling_mode=p["wobbling_mode"],
            inertia_model=p["inertia_model"],
            j_qp=p["j_quasiparticle"],
            k_att=p["k_coriolis_attenuation"],
            gamma_deg=p["gamma_deg"],
            moi_m=p["moi_m"]
        )
        # Hydrodynamic critical spin is low (~ 8.0 hbar)
        self.assertLess(solver.I_crit, 9.0)
        res = solver.evaluate_spin_series([8.5, 10.5, 12.5])
        # At spins >= 8.5, harmonic TW is already unstable in pure hydrodynamic model
        self.assertFalse(res["spin_trajectory"][0]["is_stable"])

    def test_synthetic_provenance_labels(self):
        for name, p in PRESETS.items():
            self.assertEqual(p.get("data_kind"), "synthetic_model_benchmark")

if __name__ == "__main__":
    unittest.main()
