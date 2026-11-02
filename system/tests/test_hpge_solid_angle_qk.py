#!/usr/bin/env python3
"""
Unit tests for hpge_detector_solid_angle_attenuation_qk_integrator.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from hpge_detector_solid_angle_attenuation_qk_integrator import (
    PRESETS,
    evaluate_germanium_mu_cm,
    calculate_ray_path_length_cm,
    calculate_solid_angle_attenuation_qk,
    run_attenuation_qk_analysis
)


class TestHPGeSolidAngleQk(unittest.TestCase):

    def test_germanium_attenuation_coefficient(self):
        mu_low = evaluate_germanium_mu_cm(200.0)
        mu_high = evaluate_germanium_mu_cm(1332.0)
        self.assertGreater(mu_low, mu_high)
        self.assertGreater(mu_high, 0.10)

    def test_ray_path_geometry(self):
        R = 3.5
        L = 7.0
        d = 15.0
        # On-axis ray (alpha = 0): should equal full crystal length L
        t0 = calculate_ray_path_length_cm(0.0, R, L, d)
        self.assertAlmostEqual(t0, L, places=4)

    def test_standard_coaxial_attenuation(self):
        p = PRESETS["standard_coaxial_hpge_15cm"]
        res = run_attenuation_qk_analysis(
            R_cm=p["radius_cm"],
            L_cm=p["length_cm"],
            d_cm=p["distance_cm"],
            energy_keV=p["energy_keV"],
            detector=p["detector"]
        )
        r = res["attenuation_results"]
        # For standard geometry at 15 cm, Q2 ~ 0.97, Q4 ~ 0.90
        self.assertGreater(r["Q2_attenuation_factor"], 0.95)
        self.assertLess(r["Q2_attenuation_factor"], 0.99)
        self.assertGreater(r["Q4_attenuation_factor"], 0.85)
        self.assertLess(r["Q4_attenuation_factor"], 0.95)
        self.assertGreater(r["Q2_attenuation_factor"], r["Q4_attenuation_factor"])

    def test_far_geometry_limit(self):
        p = PRESETS["far_geometry_calibration_50cm"]
        res = run_attenuation_qk_analysis(
            R_cm=p["radius_cm"],
            L_cm=p["length_cm"],
            d_cm=p["distance_cm"],
            energy_keV=p["energy_keV"],
            detector=p["detector"]
        )
        r = res["attenuation_results"]
        # At 50 cm, both Q2 and Q4 should approach unity (> 0.99)
        self.assertGreater(r["Q2_attenuation_factor"], 0.99)
        self.assertGreater(r["Q4_attenuation_factor"], 0.98)


if __name__ == "__main__":
    unittest.main()
