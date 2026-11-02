#!/usr/bin/env python3
"""
Unit tests for coriolis_anti_pairing_gap_quenching_moi_engine.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from coriolis_anti_pairing_gap_quenching_moi_engine import (
    PRESETS,
    calculate_cap_pairing_gap,
    calculate_cap_moments_of_inertia,
    solve_spin_state_cap,
    run_cap_analysis
)


class TestCoriolisAntiPairing(unittest.TestCase):

    def test_cap_gap_quenching_function(self):
        gap_zero = calculate_cap_pairing_gap(0.0, 1.0, 0.5)
        self.assertEqual(gap_zero["delta_MeV"], 1.0)
        self.assertEqual(gap_zero["quenching_fraction"], 0.0)
        self.assertTrue(gap_zero["is_superfluid"])

        gap_half = calculate_cap_pairing_gap(0.25, 1.0, 0.5)
        self.assertAlmostEqual(gap_half["delta_MeV"], 0.866, places=3)

        gap_crit = calculate_cap_pairing_gap(0.50, 1.0, 0.5)
        self.assertEqual(gap_crit["delta_MeV"], 0.0)
        self.assertFalse(gap_crit["is_superfluid"])

    def test_163Lu_tsd_cap_phase_transition(self):
        p = PRESETS["163Lu_TSD_superfluid_to_normal_phase_transition"]
        res = run_cap_analysis(
            nucleus=p["nucleus"],
            delta_0_MeV=p["delta_0_MeV"],
            omega_crit_MeV=p["omega_crit_MeV"],
            J_rig_dict=p["J_rigid_hbar2_per_MeV"],
            irr_ratio=p["J_irrotational_ratio"],
            spins=p["spins_to_evaluate"]
        )
        self.assertIsNotNone(res["critical_transition_spin_I_CAP"])
        self.assertGreaterEqual(res["critical_transition_spin_I_CAP"], 30.0)
        self.assertLessEqual(res["critical_transition_spin_I_CAP"], 40.0)
        # High spin should reach rigid limit
        top_spin = res["spin_evolution"][-1]
        self.assertEqual(top_spin["pairing_gap_MeV"], 0.0)
        self.assertAlmostEqual(top_spin["moments_of_inertia"]["J_m"], 72.0, places=2)

    def test_rigid_limit_preset(self):
        p = PRESETS["rigid_rotor_zero_pairing_limit"]
        res = run_cap_analysis(
            nucleus=p["nucleus"],
            delta_0_MeV=p["delta_0_MeV"],
            omega_crit_MeV=p["omega_crit_MeV"],
            J_rig_dict=p["J_rigid_hbar2_per_MeV"],
            irr_ratio=p["J_irrotational_ratio"],
            spins=p["spins_to_evaluate"]
        )
        for pt in res["spin_evolution"]:
            self.assertEqual(pt["pairing_gap_MeV"], 0.0)
            self.assertFalse(pt["is_superfluid"])


if __name__ == "__main__":
    unittest.main()
