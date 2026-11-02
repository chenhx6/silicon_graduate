"""
Unit tests for Cranked Shell Model (CSM) Two-Band Crossing & |V_12| Inverter.

Benchmarked against:
  - R. Bengtsson and S. Frauendorf, Nucl. Phys. A 327, 139 (1979).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, §4-3.
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from cranked_shell_model_band_crossing_v12_inverter import (
    calculate_two_band_crossing_csm,
    invert_v12_from_experimental_routhians
)


class CrankedShellModelCrossingTests(unittest.TestCase):

    def test_avoided_crossing_minimum_splitting(self):
        """Minimum avoided crossing splitting must equal exactly 2 * |V12| at omega = omega_c."""
        csm = calculate_two_band_crossing_csm(
            omega_c_MeV=0.280,
            V12_keV=90.0,
            i_align_hbar=10.0,
            J0_hbar2_MeV=30.0,
            J1_hbar4_MeV3=90.0
        )
        self.assertAlmostEqual(csm["minimum_splitting_Delta_e_keV"], 180.0, places=1)
        self.assertEqual(csm["crossing_frequency_omega_c_MeV"], 0.280)
        self.assertIn("Smooth Upbending", csm["crossing_classification"])

        # 50/50 configuration mixing at crossing
        pt_cross = [pt for pt in csm["profile"] if abs(pt["omega_MeV"] - 0.280) < 1e-4][0]
        self.assertAlmostEqual(pt_cross["g_band_percentage"], 50.0, places=1)
        self.assertAlmostEqual(pt_cross["s_band_percentage"], 50.0, places=1)
        self.assertAlmostEqual(pt_cross["splitting_keV"], 180.0, places=1)

    def test_sharp_backbending_vs_smooth_upbending(self):
        """Small V12 (< 35 keV) gives sharp backbend; large V12 (> 65 keV) gives smooth upbend."""
        csm_sharp = calculate_two_band_crossing_csm(omega_c_MeV=0.290, V12_keV=20.0, i_align_hbar=10.5)
        self.assertIn("Sharp Backbending", csm_sharp["crossing_classification"])

        csm_smooth = calculate_two_band_crossing_csm(omega_c_MeV=0.280, V12_keV=90.0, i_align_hbar=10.0)
        self.assertIn("Smooth Upbending", csm_smooth["crossing_classification"])

    def test_v12_inversion_roundtrip(self):
        """Forward calculate two crossing bands, then invert: V12 must be recovered exactly."""
        csm = calculate_two_band_crossing_csm(omega_c_MeV=0.320, V12_keV=45.0, i_align_hbar=7.5)
        w_list = [pt["omega_MeV"] for pt in csm["profile"]]
        e_yr = [pt["e_yrast_keV"] for pt in csm["profile"]]
        e_yrar = [pt["e_yrare_keV"] for pt in csm["profile"]]

        inv = invert_v12_from_experimental_routhians(w_list, e_yr, e_yrar)
        self.assertAlmostEqual(inv["inverted_V12_keV"], 45.0, places=1)
        self.assertAlmostEqual(inv["inverted_crossing_frequency_omega_c_MeV"], 0.320, places=2)

    def test_invalid_parameters_raised(self):
        """Negative crossing frequencies or V12 <= 0 must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_two_band_crossing_csm(omega_c_MeV=-0.28, V12_keV=90.0)
        with self.assertRaises(ValueError):
            calculate_two_band_crossing_csm(omega_c_MeV=0.28, V12_keV=-10.0)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        csm = calculate_two_band_crossing_csm(omega_c_MeV=0.280, V12_keV=90.0)
        s = json.dumps(csm, allow_nan=False)
        self.assertIn("minimum_splitting_Delta_e_keV", s)


if __name__ == "__main__":
    unittest.main()
