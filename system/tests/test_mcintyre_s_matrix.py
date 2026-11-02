#!/usr/bin/env python3
"""
Unit tests for heavy_ion_mcintyre_s_matrix_reaction_cross_section_analyzer.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from heavy_ion_mcintyre_s_matrix_reaction_cross_section_analyzer import (
    PRESETS,
    calculate_kinematics,
    evaluate_mcintyre_s_matrix,
    calculate_reaction_cross_sections,
    invert_strong_absorption_radius,
    run_mcintyre_analysis
)


class TestMcIntyreSMatrix(unittest.TestCase):

    def test_s_matrix_transmission_boundary(self):
        l_vals = [0, 20, 50, 55, 60, 80]
        _, eta_l, _, T_l = evaluate_mcintyre_s_matrix(l_vals, l_grazing=55.0, Delta_l=3.0)
        # Low l (deep inside): completely absorbed (eta ~ 0, T ~ 1)
        self.assertLess(eta_l[0], 0.01)
        self.assertGreater(T_l[0], 0.99)
        # At l_grazing: eta = 0.5, T = 1 - 0.25 = 0.75
        self.assertAlmostEqual(eta_l[3], 0.50, places=2)
        self.assertAlmostEqual(T_l[3], 0.75, places=2)
        # High l (far outside): unabsorbed (eta ~ 1, T ~ 0)
        self.assertGreater(eta_l[-1], 0.99)
        self.assertLess(T_l[-1], 0.01)

    def test_16O_208Pb_benchmark(self):
        p = PRESETS["16O_208Pb_129.5MeV"]
        res = run_mcintyre_analysis(
            Ap=p["Ap"], Zp=p["Zp"], At=p["At"], Zt=p["Zt"],
            Elab_MeV=p["Elab_MeV"],
            l_grazing=p["l_grazing"],
            Delta_l=p["Delta_l"],
            delta_0_rad=p["delta_0_rad"],
            l_max=p["l_max"]
        )
        xs = res["cross_sections"]
        rad = res["semiclassical_radii"]
        # Total reaction cross section should be ~ 1295 mb
        self.assertGreater(xs["sigma_reaction_mb"], 1100.0)
        self.assertLess(xs["sigma_reaction_mb"], 1500.0)
        # Strong absorption radius should be ~ 11.1 fm with r0 ~ 1.31 fm
        self.assertAlmostEqual(rad["strong_absorption_radius_R_int_fm"], 11.09, delta=0.5)
        self.assertAlmostEqual(rad["interaction_radius_parameter_r0_fm"], 1.31, delta=0.1)

    def test_12C_12C_benchmark(self):
        p = PRESETS["12C_12C_120MeV"]
        res = run_mcintyre_analysis(
            Ap=p["Ap"], Zp=p["Zp"], At=p["At"], Zt=p["Zt"],
            Elab_MeV=p["Elab_MeV"],
            l_grazing=p["l_grazing"],
            Delta_l=p["Delta_l"],
            delta_0_rad=p["delta_0_rad"],
            l_max=p["l_max"]
        )
        xs = res["cross_sections"]
        self.assertGreater(xs["sigma_reaction_mb"], 1200.0)
        self.assertLess(xs["sigma_reaction_mb"], 1600.0)

    def test_alpha_40Ca_benchmark(self):
        p = PRESETS["alpha_40Ca_104MeV"]
        res = run_mcintyre_analysis(
            Ap=p["Ap"], Zp=p["Zp"], At=p["At"], Zt=p["Zt"],
            Elab_MeV=p["Elab_MeV"],
            l_grazing=p["l_grazing"],
            Delta_l=p["Delta_l"],
            delta_0_rad=p["delta_0_rad"],
            l_max=p["l_max"]
        )
        rad = res["semiclassical_radii"]
        self.assertGreater(rad["strong_absorption_radius_R_int_fm"], 5.0)
        self.assertLess(rad["strong_absorption_radius_R_int_fm"], 8.0)


if __name__ == "__main__":
    unittest.main()
