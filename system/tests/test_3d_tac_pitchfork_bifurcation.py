#!/usr/bin/env python3
"""
Unit tests for three_dimensional_tac_chiral_pitchfork_bifurcation_inverter.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from three_dimensional_tac_chiral_pitchfork_bifurcation_inverter import (
    PRESETS,
    evaluate_tac_energy,
    calculate_pitchfork_bifurcation,
    run_chiral_pitchfork_analysis
)


class Test3DTACPitchforkBifurcation(unittest.TestCase):

    def test_planar_energy_at_low_spin(self):
        p = PRESETS["134Pr_chiral_bifurcation"]
        pt = calculate_pitchfork_bifurcation(
            10.0,
            p["quasiparticles"]["j_p_hbar"],
            p["quasiparticles"]["j_n_hbar"],
            p["moments_of_inertia"]["J_m"],
            p["moments_of_inertia"]["J_s"],
            p["moments_of_inertia"]["J_l"]
        )
        self.assertFalse(pt["is_chiral_phase"])
        self.assertAlmostEqual(pt["optimal_phi_deg"], 0.0, delta=1.0)
        self.assertAlmostEqual(pt["chiral_barrier_keV"], 0.0, delta=1.0)

    def test_aplanar_chiral_bifurcation_at_high_spin(self):
        p = PRESETS["134Pr_chiral_bifurcation"]
        pt = calculate_pitchfork_bifurcation(
            16.0,
            p["quasiparticles"]["j_p_hbar"],
            p["quasiparticles"]["j_n_hbar"],
            p["moments_of_inertia"]["J_m"],
            p["moments_of_inertia"]["J_s"],
            p["moments_of_inertia"]["J_l"]
        )
        self.assertTrue(pt["is_chiral_phase"])
        self.assertGreater(pt["optimal_phi_deg"], 40.0)
        self.assertGreater(pt["chiral_barrier_keV"], 200.0)
        self.assertGreater(pt["chiral_volume_metric"], 0.20)

    def test_134Pr_full_spin_evolution(self):
        p = PRESETS["134Pr_chiral_bifurcation"]
        res = run_chiral_pitchfork_analysis(
            nucleus=p["nucleus"],
            quasiparticles=p["quasiparticles"],
            moments_of_inertia=p["moments_of_inertia"],
            spins_to_evaluate=p["spins_to_evaluate"]
        )
        self.assertIsNotNone(res["bifurcation_spin_J_crit"])
        self.assertLessEqual(res["bifurcation_spin_J_crit"], 14.0)
        self.assertEqual(len(res["spin_evolution"]), len(p["spins_to_evaluate"]))

    def test_axial_symmetric_no_bifurcation(self):
        p = PRESETS["axial_symmetric_no_bifurcation"]
        res = run_chiral_pitchfork_analysis(
            nucleus=p["nucleus"],
            quasiparticles=p["quasiparticles"],
            moments_of_inertia=p["moments_of_inertia"],
            spins_to_evaluate=p["spins_to_evaluate"]
        )
        self.assertIsNone(res["bifurcation_spin_J_crit"])
        for pt in res["spin_evolution"]:
            self.assertFalse(pt["is_chiral_phase"])
            self.assertEqual(pt["optimal_phi_deg"], 0.0)


if __name__ == "__main__":
    unittest.main()
