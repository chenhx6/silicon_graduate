"""
Unit tests for Gamma-Band Mikhailov z_gamma Mixing & Alaga Correction Inverter.

Benchmarked against:
  - G. Alaga et al., Mat. Fys. Medd. Dan. Vid. Selsk. 29, no. 9 (1955).
  - V. M. Mikhailov, Izv. Akad. Nauk SSSR, Ser. Fiz. 30, 1334 (1966).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, §4-2.
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from gamma_band_mixing_z_gamma_alaga_inverter import (
    calculate_alaga_cg_coefficient,
    invert_z_gamma_from_branching
)


class GammaBandMixingZGammaTests(unittest.TestCase):

    def test_unperturbed_alaga_coefficients(self):
        """Verify unperturbed Clebsch-Gordan coefficients for K=2 to K=0 transitions."""
        # <2 2 2 -2 | 0 0> = sqrt(1/5)
        self.assertAlmostEqual(calculate_alaga_cg_coefficient(2, 0), 0.44721, places=4)
        # <2 2 2 -2 | 2 0> = sqrt(2/7)
        self.assertAlmostEqual(calculate_alaga_cg_coefficient(2, 2), 0.53452, places=4)
        # <2 2 2 -2 | 4 0> = sqrt(1/70)
        self.assertAlmostEqual(calculate_alaga_cg_coefficient(2, 4), 0.11952, places=4)

    def test_168Er_mikhailov_inversion_benchmark(self):
        """168Er gamma band benchmark: R_exp = 0.540 -> z_gamma ~ 0.0203, h2 ~ 6.14 keV."""
        res = invert_z_gamma_from_branching(
            R_exp_B_E2=0.540, E_2gamma_keV=821.1, E_2g_keV=79.8
        )
        self.assertAlmostEqual(res["inverted_z_gamma"], 0.02028, places=4)
        self.assertAlmostEqual(res["rotational_vibrational_h2_keV"], 6.14, places=1)
        self.assertAlmostEqual(res["unperturbed_Alaga_ratio"], 0.7000, places=3)
        self.assertIn("Well-Deformed", res["structural_classification"])

    def test_gamma_soft_large_mixing_130Ba(self):
        """130Ba transitional gamma-soft nucleus exhibits large z_gamma > 0.05."""
        res_soft = invert_z_gamma_from_branching(
            R_exp_B_E2=0.320, E_2gamma_keV=908.1, E_2g_keV=357.4
        )
        self.assertGreater(res_soft["inverted_z_gamma"], 0.050)
        self.assertGreater(res_soft["rotational_vibrational_h2_keV"], 10.0)
        self.assertIn("Transitional", res_soft["structural_classification"])

    def test_invalid_parameters_raised(self):
        """Non-positive branching ratio must raise ValueError."""
        with self.assertRaises(ValueError):
            invert_z_gamma_from_branching(R_exp_B_E2=-0.5)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = invert_z_gamma_from_branching(R_exp_B_E2=0.540)
        s = json.dumps(res, allow_nan=False)
        self.assertIn("inverted_z_gamma", s)


if __name__ == "__main__":
    unittest.main()
