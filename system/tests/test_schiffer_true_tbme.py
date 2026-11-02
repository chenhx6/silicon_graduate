"""
Unit tests for Schiffer-True Universal TBME & Pandya Inversion.

Benchmarked against:
  - J. P. Schiffer and W. W. True, Rev. Mod. Phys. 48, 191 (1976).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. I, §3-4.
  - S. P. Pandya, Phys. Rev. 103, 956 (1956).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from schiffer_true_two_body_matrix_elements_calculator import (
    calculate_semiclassical_angle_theta12,
    calculate_schiffer_true_pp_spectrum,
    calculate_schiffer_true_ph_pandya_spectrum,
    evaluate_nordheim_coupling_rule
)


class SchifferTrueTBMETests(unittest.TestCase):

    def test_semiclassical_angle_limits(self):
        """theta_12 must equal 180 deg for J=0, and decrease monotonically with J."""
        angles = []
        for J in range(0, 12):
            _, th = calculate_semiclassical_angle_theta12(5.5, 5.5, J)
            angles.append(th)
        self.assertAlmostEqual(angles[0], 180.0, places=1)
        self.assertLess(angles[-1], 35.0)
        for i in range(len(angles) - 1):
            self.assertGreater(angles[i], angles[i+1])

    def test_particle_particle_ground_state_is_J0(self):
        """Particle-particle pairing interaction produces deepest attractive minimum at J=0+."""
        pp = calculate_schiffer_true_pp_spectrum(5.5, 5.5)
        self.assertEqual(pp["ground_state_spin_J"], 0)
        self.assertAlmostEqual(pp["spectrum"][0]["V_pp_MeV"], -3.70, places=1)

    def test_pandya_particle_hole_spectrum_inversion(self):
        """Pandya transformation inverts the multiplet spectrum."""
        ph = calculate_schiffer_true_ph_pandya_spectrum(5.5, 5.5)
        self.assertEqual(len(ph["spectrum"]), 12)
        # J=0 is no longer the deep pairing minimum
        v_j0 = ph["spectrum"][0]["V_ph_MeV"]
        self.assertGreater(v_j0, -1.0) # Inverted from -3.7 MeV

    def test_nordheim_odd_odd_coupling_rule(self):
        """134Pr (pi h11/2 (x) nu h11/2^-1) has N = +1, favoring aligned chiral bandhead."""
        nord = evaluate_nordheim_coupling_rule(j_p=5.5, l_p=5, j_n=5.5, l_n=5)
        self.assertEqual(nord["nordheim_number_N"], 1)
        self.assertIn("Weak Nordheim Rule", nord["rule_classification"])
        self.assertEqual(nord["predicted_favored_spin_J"], 11)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        pp = calculate_schiffer_true_pp_spectrum(5.5, 5.5)
        ph = calculate_schiffer_true_ph_pandya_spectrum(5.5, 5.5)
        nord = evaluate_nordheim_coupling_rule(5.5, 5, 5.5, 5)
        payload = {"pp": pp, "ph": ph, "nord": nord}
        s = json.dumps(payload, allow_nan=False)
        self.assertIn("ground_state_spin_J", s)


if __name__ == "__main__":
    unittest.main()
