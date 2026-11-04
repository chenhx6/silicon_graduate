"""Tests for the BM-II Sec. 4-5e asymmetric-rotor benchmark."""

import math
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from davydov_wobbling_rotor_calculator import calculate_bm_high_spin_asymmetric_rotor


class BM2HighSpinAsymmetricRotorTests(unittest.TestCase):
    def test_energy_frequency_and_axis_convention(self):
        result = calculate_bm_high_spin_asymmetric_rotor(
            I=20.0, A1=8.0, A2=12.0, A3=30.0, n=0
        )
        self.assertAlmostEqual(
            result["hbar_omega_keV"],
            40.0 * math.sqrt(4.0 * 22.0),
            places=10,
        )
        self.assertEqual(result["axis_convention"], "A1 < A2 < A3; J1 > J2 > J3")
        self.assertIsNone(result["mode_inference"])

    def test_harmonicity_and_e2_proxies(self):
        result = calculate_bm_high_spin_asymmetric_rotor(
            I=24.0,
            A1=7.0,
            A2=11.0,
            A3=28.0,
            n=1,
            Q0_eb=3.0,
            Q2_eb=0.8,
        )
        self.assertLess(result["harmonicity_indicator_epsilon"], 0.3)
        self.assertGreater(result["B_E2_delta_n_0_proxy_eb2"], 0.0)
        self.assertGreaterEqual(result["B_E2_delta_n_minus_1_proxy_eb2"], 0.0)
        self.assertGreaterEqual(result["B_E2_delta_n_plus_1_proxy_eb2"], 0.0)

    def test_invalid_axis_order_is_rejected(self):
        with self.assertRaises(ValueError):
            calculate_bm_high_spin_asymmetric_rotor(
                I=20.0, A1=12.0, A2=8.0, A3=30.0
            )


if __name__ == "__main__":
    unittest.main()
