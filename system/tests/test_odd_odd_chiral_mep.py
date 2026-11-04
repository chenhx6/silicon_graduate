#!/usr/bin/env python3
"""
Unit tests for odd_odd_chiral_mep_instanton_tunneling_solver.py (Module 155).
"""

import sys
import unittest
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from odd_odd_chiral_mep_instanton_tunneling_solver import (
    PRESETS,
    OddOddChiralMEPInstantonSolver
)

class TestOddOddChiralMEP(unittest.TestCase):

    def test_134Pr_static_chiral_regime(self):
        p = PRESETS["134Pr_chiral_mep_instanton"]
        solver = OddOddChiralMEPInstantonSolver(
            spin=p["spin"],
            j_p=p["j_p"],
            j_n=p["j_n"],
            gamma_deg=p["gamma_deg"],
            moi_s=p["moi_s"],
            moi_i=p["moi_i"],
            moi_l=p["moi_l"]
        )
        res = solver.solve_instanton_action(n_nodes=15)
        # Verify symmetry of left and right chiral minima
        min_info = res["minima_info"]
        self.assertTrue(min_info["is_chiral_broken"])
        self.assertAlmostEqual(min_info["right_minimum"]["theta_deg"],
                               min_info["left_minimum"]["theta_deg"], delta=1.0)
        self.assertAlmostEqual(min_info["right_minimum"]["phi_deg"],
                               -min_info["left_minimum"]["phi_deg"], delta=1.0)
        # Chiral barrier must be positive and substantial (> 200 keV)
        self.assertGreater(res["barrier_height_MeV"], 0.2)
        # Instanton action must be positive (> 2 hbar)
        self.assertGreater(res["instanton_action_hbar"], 2.0)
        # Tunneling splitting must be suppressed (< 20 keV)
        self.assertLess(res["tunneling_splitting_keV"], 20.0)

    def test_134Pr_vibrational_regime_near_critical_spin(self):
        p = PRESETS["134Pr_chiral_vibration"]
        solver = OddOddChiralMEPInstantonSolver(
            spin=p["spin"],
            j_p=p["j_p"],
            j_n=p["j_n"],
            gamma_deg=p["gamma_deg"],
            moi_s=p["moi_s"],
            moi_i=p["moi_i"],
            moi_l=p["moi_l"]
        )
        res = solver.solve_instanton_action(n_nodes=15)
        # At lower spin I=13, barrier is very shallow (< 50 keV)
        self.assertLess(res["barrier_height_MeV"], 0.05)
        # Tunneling splitting is larger in vibrational regime
        self.assertGreater(res["tunneling_splitting_keV"], 10.0)

    def test_mep_continuity_and_boundary(self):
        solver = OddOddChiralMEPInstantonSolver(spin=16.0)
        mep = solver.compute_minimum_energy_path(n_nodes=15)
        # Verify trajectory starts at left minimum (phi < 0) and ends at right minimum (phi > 0)
        phis = mep["nodes_phi_deg"]
        self.assertLess(phis[0], 0.0)
        self.assertGreater(phis[-1], 0.0)
        # Potential relative energy must be non-negative
        v_rel = np.array(mep["V_along_mep_MeV"])
        self.assertTrue(np.all(v_rel >= -1e-6))

    def test_synthetic_provenance_labels(self):
        for name, p in PRESETS.items():
            self.assertEqual(p.get("data_kind"), "synthetic_model_benchmark")

if __name__ == "__main__":
    unittest.main()
