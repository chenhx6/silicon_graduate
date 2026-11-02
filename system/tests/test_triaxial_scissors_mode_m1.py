#!/usr/bin/env python3
"""
Unit tests for triaxial_two_rotor_scissors_mode_m1_solver.py (Module 164).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from triaxial_two_rotor_scissors_mode_m1_solver import (
    PRESETS,
    TriaxialScissorsModeM1Solver
)

class TestTriaxialScissorsModeM1(unittest.TestCase):

    def test_axial_prolate_single_mode(self):
        p = PRESETS["156Gd_axial_prolate_baseline"]
        solver = TriaxialScissorsModeM1Solver(
            A=p["A"], Z=p["Z"], beta2=p["beta2"], gamma_deg=p["gamma_deg"],
            b_sym_MeV=p["b_sym_MeV"], moi_base_MeV_inv=p["moi_base_MeV_inv"]
        )
        res = solver.solve_scissors_modes()
        # At gamma = 0, short-axis mode should be zero/inactive
        self.assertAlmostEqual(res["shear_deformations"]["delta_s"], 0.0, places=4)
        self.assertAlmostEqual(res["scissors_short_axis"]["BM1_muN2"], 0.0, places=4)
        # Long-axis mode should be active with substantial strength (B(M1) > 1.5 mu_N^2)
        self.assertGreater(res["scissors_long_axis"]["BM1_muN2"], 1.5)
        self.assertFalse(res["is_scissors_doublet_split"])

    def test_triaxial_scissors_doublet_splitting(self):
        p = PRESETS["134Ba_triaxial_scissors_doublet"]
        solver = TriaxialScissorsModeM1Solver(
            A=p["A"], Z=p["Z"], beta2=p["beta2"], gamma_deg=p["gamma_deg"],
            b_sym_MeV=p["b_sym_MeV"], moi_base_MeV_inv=p["moi_base_MeV_inv"]
        )
        res = solver.solve_scissors_modes()
        # In triaxial case (gamma=24), both short and long modes must have B(M1) > 0.4 mu_N^2
        self.assertGreater(res["scissors_short_axis"]["BM1_muN2"], 0.4)
        self.assertGreater(res["scissors_long_axis"]["BM1_muN2"], 0.4)
        # Energy splitting should be significant (> 0.5 MeV)
        self.assertGreater(res["scissors_splitting_MeV"], 0.5)
        self.assertTrue(res["is_scissors_doublet_split"])

    def test_sum_rule_positivity(self):
        solver = TriaxialScissorsModeM1Solver(A=134, Z=56, beta2=0.25, gamma_deg=20.0)
        res = solver.solve_scissors_modes()
        self.assertGreater(res["total_B_M1_muN2"], 0.5)
        self.assertGreater(res["EWSR_MeV_muN2"], 1.0)

if __name__ == "__main__":
    unittest.main()
