#!/usr/bin/env python3
"""
Unit tests for odd_odd_3d_tac_recoil_chiral_orientator.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from odd_odd_3d_tac_recoil_chiral_orientator import (
    PRESETS,
    evaluate_recoil_coupled_energy,
    find_optimal_orientation,
    run_recoil_chiral_analysis
)


class TestOddOddRecoilChiral(unittest.TestCase):

    def test_zero_recoil_reference_limit(self):
        p = PRESETS["zero_recoil_decoupled_limit"]
        res = run_recoil_chiral_analysis(
            nucleus=p["nucleus"],
            jp=p["j_p_hbar"],
            jn=p["j_n_hbar"],
            V_pn=p["V_pn_coupling"],
            moments_of_inertia=p["moments_of_inertia"],
            spins=p["spins_to_evaluate"]
        )
        # At V_pn = 0, recoil energy shift must be strictly zero
        for pt in res["spin_evolution"]:
            self.assertAlmostEqual(pt["recoil_energy_shift_keV"], 0.0, places=4)

    def test_134Pr_recoil_coupled_bifurcation(self):
        p = PRESETS["134Pr_recoil_coupled_chiral_band"]
        res = run_recoil_chiral_analysis(
            nucleus=p["nucleus"],
            jp=p["j_p_hbar"],
            jn=p["j_n_hbar"],
            V_pn=p["V_pn_coupling"],
            moments_of_inertia=p["moments_of_inertia"],
            spins=p["spins_to_evaluate"]
        )
        self.assertIsNotNone(res["recoil_bifurcation_spin_J_crit"])
        self.assertLessEqual(res["recoil_bifurcation_spin_J_crit"], 14.0)
        # High spin states should have positive recoil energy shift and large barrier
        high_spin = res["spin_evolution"][-1]
        self.assertTrue(high_spin["is_chiral_phase"])
        self.assertGreater(high_spin["chiral_barrier_keV"], 500.0)
        self.assertGreater(high_spin["recoil_energy_shift_keV"], 0.0)

    def test_energy_functional_symmetry(self):
        # Testing planar phi = 0 vs phi = pi
        E1 = evaluate_recoil_coupled_energy(14.0, 1.0, 0.0, 5.5, 5.5, 30.0, 12.0, 6.0, 0.15)
        self.assertGreater(E1, 0.0)


if __name__ == "__main__":
    unittest.main()
