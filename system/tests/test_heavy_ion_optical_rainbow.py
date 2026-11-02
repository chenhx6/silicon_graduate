#!/usr/bin/env python3
"""
Unit tests for Heavy-Ion Optical Model Nuclear Rainbow Scattering & Airy Minima Inverter (Module 131).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from heavy_ion_optical_rainbow_scattering_analyzer import (
    calculate_kinematics_and_sommerfeld,
    evaluate_deflection_function,
    find_rainbow_singularity_and_airy_minima,
    run_rainbow_analysis,
    PRESETS
)


class TestHeavyIonOpticalRainbow(unittest.TestCase):

    def test_kinematics_and_sommerfeld(self):
        kin = calculate_kinematics_and_sommerfeld(Ap=16, Zp=8, At=16, Zt=8, Elab_MeV=350.0)
        self.assertAlmostEqual(kin["E_cm_MeV"], 175.0, places=1)
        self.assertAlmostEqual(kin["mu_u"], 8.0, places=1)
        self.assertGreater(kin["sommerfeld_eta"], 2.0)
        self.assertLess(kin["sommerfeld_eta"], 2.5)

    def test_deflection_minimum_rainbow(self):
        eta = 2.155
        l_vals = np.linspace(10.0, 50.0, 41)
        _, th_C, th_N, th_tot = evaluate_deflection_function(eta, l_vals, l_R=25.0, Delta_theta_deg=70.0, sigma_l=12.0)
        min_idx = np.argmin(th_tot)
        self.assertLess(th_tot[min_idx], 0.0)
        self.assertAlmostEqual(l_vals[min_idx], 25.0, delta=2.0)

    def test_airy_minima_ordering(self):
        res = find_rainbow_singularity_and_airy_minima(
            eta=2.155, k_fm=8.18, l_R=25.0, Delta_theta_deg=70.0, sigma_l=12.0
        )
        th_R = res["observed_rainbow_angle_deg"]
        th_A1 = res["airy_minimum_1_deg"]
        th_A2 = res["airy_minimum_2_deg"]
        self.assertLess(th_A1, th_R)
        self.assertLess(th_A2, th_A1)
        self.assertGreater(res["inverted_V0_optical_depth_MeV"], 100.0)

    def test_run_rainbow_preset(self):
        p = PRESETS["16O_16O_350MeV"]
        out = run_rainbow_analysis(
            p["Ap"], p["Zp"], p["At"], p["Zt"], p["Elab_MeV"],
            p["l_R"], p["Delta_theta_deg"], p["sigma_l"], p["V0_nominal_MeV"]
        )
        self.assertGreater(out["rainbow_analysis"]["observed_rainbow_angle_deg"], 50.0)
        self.assertLess(out["rainbow_analysis"]["observed_rainbow_angle_deg"], 70.0)


if __name__ == "__main__":
    unittest.main()
