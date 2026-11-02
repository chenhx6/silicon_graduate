"""
Unit tests for In-Beam Relativistic Doppler Broadening & Array Resolution Calculator.

Benchmarked against:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第15章 §15.2.
  - 汪晓莲等, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第5章.
  - P. J. Nolan and J. F. Sharpey-Schafer, Rep. Prog. Phys. 42, 1 (1979).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from in_beam_doppler_broadening_array_correction_calculator import (
    calculate_doppler_broadening_budget,
    compare_detector_rings
)


class InBeamDopplerBroadeningTests(unittest.TestCase):

    def test_90deg_opening_angle_broadening_dominance(self):
        """At 90 deg, sin(theta) = 1 maximizes opening angle broadening dE_theta."""
        res_90 = calculate_doppler_broadening_budget(
            E0_keV=1000.0, beta_recoil=0.020, theta_deg=90.0, opening_angle_deg=8.0
        )
        self.assertAlmostEqual(res_90["broadening_detector_angle_dE_theta_keV"], 2.79, places=1)
        self.assertAlmostEqual(res_90["E_lab_shifted_keV"], 999.8, places=1)
        self.assertGreater(res_90["total_observed_fwhm_keV"], 3.5)

    def test_forward_backward_velocity_spread_dominance(self):
        """At forward and backward angles, opening angle broadening is small, velocity spread dominates."""
        res_30 = calculate_doppler_broadening_budget(
            E0_keV=1000.0, beta_recoil=0.020, theta_deg=30.0, opening_angle_deg=8.0
        )
        res_150 = calculate_doppler_broadening_budget(
            E0_keV=1000.0, beta_recoil=0.020, theta_deg=150.0, opening_angle_deg=8.0
        )
        # Shift is large at forward/backward
        self.assertGreater(res_30["Doppler_shift_keV"], 15.0)
        self.assertLess(res_150["Doppler_shift_keV"], -15.0)
        # Angle broadening is smaller than at 90 deg (2.79 keV)
        self.assertLess(res_30["broadening_detector_angle_dE_theta_keV"], 1.6)
        self.assertLess(res_150["broadening_detector_angle_dE_theta_keV"], 1.6)

    def test_agata_tracking_sub_1deg_resolution_recovery(self):
        """Tracking arrays with Delta_theta ~ 1.2 deg suppress angle broadening below 0.6 keV."""
        res_agata = calculate_doppler_broadening_budget(
            E0_keV=1000.0, beta_recoil=0.025, theta_deg=90.0, opening_angle_deg=1.2
        )
        self.assertLess(res_agata["broadening_detector_angle_dE_theta_keV"], 0.6)
        self.assertLess(res_agata["total_observed_fwhm_keV"], 2.5) # Approaching intrinsic 2.0 keV

    def test_rings_comparison_table(self):
        """Ring comparison must cover all requested angles."""
        rings = compare_detector_rings(1000.0, beta_recoil=0.020, opening_angle_deg=8.0)
        self.assertEqual(len(rings), 5)
        # Forward ring has positive shift, backward has negative shift
        self.assertGreater(rings[0]["shift_keV"], 0.0)
        self.assertLess(rings[-1]["shift_keV"], 0.0)

    def test_invalid_parameters_raised(self):
        """E0 <= 0 or beta >= 1 must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_doppler_broadening_budget(E0_keV=-100.0)
        with self.assertRaises(ValueError):
            calculate_doppler_broadening_budget(E0_keV=1000.0, beta_recoil=1.2)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = calculate_doppler_broadening_budget(E0_keV=1000.0, beta_recoil=0.020)
        s = json.dumps(res, allow_nan=False)
        self.assertIn("total_observed_fwhm_keV", s)


if __name__ == "__main__":
    unittest.main()
