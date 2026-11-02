#!/usr/bin/env python3
"""
Unit tests for Heavy-Ion Deep Inelastic Collisions (DIC), TKEL,
Spin Dissipation & Wilczynski Trajectory Simulator (Module 117).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from heavy_ion_dic_wilczynski_energy_loss_calculator import (
    calculate_dic_kinematics,
    simulate_wilczynski_trajectory,
    run_dic_analysis,
    PRESETS
)


class TestHeavyIonDICWilczynski(unittest.TestCase):

    def test_dic_kinematics(self):
        kin = calculate_dic_kinematics(Ap=86, Zp=36, At=166, Zt=68, Elab_MeV=703.0)
        self.assertAlmostEqual(kin["E_cm_MeV"], 463.1, delta=0.5)
        self.assertGreater(kin["L_grazing_hbar"], 300.0)
        self.assertGreater(kin["L_crit_hbar"], 200.0)
        self.assertGreater(kin["TKEL_max_MeV"], 190.0)

    def test_sticking_fraction(self):
        kin = calculate_dic_kinematics(Ap=86, Zp=36, At=166, Zt=68, Elab_MeV=703.0)
        self.assertGreater(kin["f_stick_fraction"], 0.25)
        self.assertLess(kin["f_stick_fraction"], 0.35)

    def test_trajectory_energy_loss_and_orbiting(self):
        kin = calculate_dic_kinematics(Ap=40, Zp=18, At=232, Zt=90, Elab_MeV=388.0)
        traj = simulate_wilczynski_trajectory(kin, n_steps=20)
        self.assertGreater(len(traj), 10)
        # Grazing point: zero TKEL
        self.assertAlmostEqual(traj[0]["TKEL_MeV"], 0.0, delta=1.0)
        # Final point near fusion: significant TKEL
        self.assertGreater(traj[-1]["TKEL_MeV"], 100.0)
        # Verify presence of negative orbiting branch
        branches = [pt["branch"] for pt in traj]
        self.assertIn("negative_orbiting", branches)

    def test_run_dic_analysis_preset(self):
        p = PRESETS["86Kr_166Er_703MeV"]
        res = run_dic_analysis(p["Ap"], p["Zp"], p["At"], p["Zt"], p["Elab_MeV"])
        self.assertGreater(res["max_spin_transfer_hbar"], 50.0)
        self.assertGreater(res["negative_orbiting_fraction_percent"], 10.0)


if __name__ == "__main__":
    unittest.main()
