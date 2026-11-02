"""
Unit tests for Davydov-Chaban Non-Adiabatic Triaxial Rotor & Beta-Stretching Calculator.

Benchmarked against:
  - A. S. Davydov and A. A. Chaban, Nucl. Phys. 20, 499 (1960).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, §4-2.
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from davydov_chaban_beta_stretching_triaxial_calculator import (
    solve_chaban_stretching_parameter_p,
    calculate_davydov_filippov_epsilon,
    calculate_davydov_chaban_spectrum
)


class DavydovChabanStretchingTests(unittest.TestCase):

    def test_stretching_parameter_p_monotonicity(self):
        """Dynamic beta-stretching ratio p = beta / beta_0 must be >= 1.0 and increase with mu and eps."""
        p_rigid = solve_chaban_stretching_parameter_p(mu=0.0, eps=2.0)
        self.assertEqual(p_rigid, 1.0)

        p_soft1 = solve_chaban_stretching_parameter_p(mu=0.20, eps=2.0)
        p_soft2 = solve_chaban_stretching_parameter_p(mu=0.35, eps=2.0)
        self.assertGreater(p_soft1, 1.0)
        self.assertGreater(p_soft2, p_soft1)

    def test_112Ru_triaxial_wobbler_benchmark(self):
        """Verify 112Ru benchmark reproduces Davydov-Chaban spectrum with beta-stretching."""
        res = calculate_davydov_chaban_spectrum(E_2plus_keV=237.2, gamma_deg=22.0, mu_nonadiabatic=0.28)
        self.assertEqual(len(res["levels"]), 5)
        # Check 2_1+ matches reference
        lv21 = [lv for lv in res["levels"] if lv["state"] == "2_1+"][0]
        self.assertAlmostEqual(lv21["energy_keV"], 237.2, places=1)
        self.assertAlmostEqual(lv21["stretching_factor_p"], 1.0080, places=3)

        # Gamma-bandhead 2_2+
        lv22 = [lv for lv in res["levels"] if lv["state"] == "2_2+"][0]
        self.assertAlmostEqual(lv22["energy_keV"], 706.0, places=1)

    def test_invalid_parameters_raised(self):
        """Negative E2 or negative mu must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_davydov_chaban_spectrum(E_2plus_keV=-100.0)
        with self.assertRaises(ValueError):
            calculate_davydov_chaban_spectrum(E_2plus_keV=200.0, mu_nonadiabatic=-0.5)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = calculate_davydov_chaban_spectrum(E_2plus_keV=237.2)
        s = json.dumps(res, allow_nan=False)
        self.assertIn("R_4_2_ratio", s)


if __name__ == "__main__":
    unittest.main()
