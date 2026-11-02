"""
Unit tests for Nuclear Seniority Scheme & Half-Filled Shell Isomer Engine.

Benchmarked against:
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. I, §3-4 (pp. 314–332).
  - A. K. Jain et al., Nuclear Isomers: A Primer, Springer (2021), Ch. 3 & Ch. 5.
  - K. L. G. Heyde, Basic Ideas and Concepts in Nuclear Physics, Ch. 8.
"""

import unittest
import sys
import json
import math
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from seniority_scheme_half_filled_isomer_calculator import (
    calculate_seniority_fractional_factor,
    calculate_seniority_v2_multiplet_spins,
    evaluate_seniority_isomer_properties
)


class SenioritySchemeIsomerTests(unittest.TestCase):

    def test_half_filled_shell_exact_cancellation(self):
        """At mid-shell n = j + 1/2, fractional parentage factor F and B(E2) scaling must be exactly 0."""
        # For h11/2 (j = 5.5, capacity = 12): n = 6 is half-filled
        res_h11 = calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=6, v_seniority=2)
        self.assertEqual(res_h11["fractional_parentage_factor"], 0.0)
        self.assertEqual(res_h11["b_e2_scaling_factor"], 0.0)
        self.assertTrue(res_h11["is_half_filled"])
        self.assertTrue(res_h11["is_seniority_cancellation"])

        # For g9/2 (j = 4.5, capacity = 10): n = 5 is half-filled
        res_g9 = calculate_seniority_fractional_factor(j_orbital=4.5, n_particles=5, v_seniority=2)
        self.assertEqual(res_g9["fractional_parentage_factor"], 0.0)
        self.assertEqual(res_g9["b_e2_scaling_factor"], 0.0)
        self.assertTrue(res_g9["is_half_filled"])

        # For i13/2 (j = 6.5, capacity = 14): n = 7 is half-filled
        res_i13 = calculate_seniority_fractional_factor(j_orbital=6.5, n_particles=7, v_seniority=2)
        self.assertEqual(res_i13["fractional_parentage_factor"], 0.0)
        self.assertEqual(res_i13["b_e2_scaling_factor"], 0.0)

    def test_particle_hole_symmetry_parabolic_scaling(self):
        """Particle-hole conjugate states (n and 2j+1-n) must have identical B(E2) scaling factors."""
        # In h11/2: n = 2 (2 particles) and n = 10 (2 holes) must match
        res_2 = calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=2, v_seniority=2)
        res_10 = calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=10, v_seniority=2)
        self.assertAlmostEqual(res_2["b_e2_scaling_factor"], res_10["b_e2_scaling_factor"], places=6)
        self.assertEqual(res_2["fractional_parentage_factor"], - res_10["fractional_parentage_factor"])

        # n = 4 and n = 8 must match
        res_4 = calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=4, v_seniority=2)
        res_8 = calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=8, v_seniority=2)
        self.assertAlmostEqual(res_4["b_e2_scaling_factor"], res_8["b_e2_scaling_factor"], places=6)
        self.assertAlmostEqual(res_4["b_e2_scaling_factor"], 0.2500, places=4)

    def test_seniority_v2_multiplet_spins(self):
        """Allowed spins for v=2 in j-shell are J = 2, 4, ..., 2j-1."""
        spins_h11 = calculate_seniority_v2_multiplet_spins(5.5)
        self.assertEqual(spins_h11, [2, 4, 6, 8, 10])

        spins_g9 = calculate_seniority_v2_multiplet_spins(4.5)
        self.assertEqual(spins_g9, [2, 4, 6, 8])

    def test_isomer_half_life_cancellation_and_finite_decay(self):
        """At mid-shell T1/2 is infinite (in pure single-j model); away from mid-shell T1/2 is finite."""
        # Half-filled shell
        iso_mid = evaluate_seniority_isomer_properties(j_orbital=5.5, n_particles=6, E_gamma_keV=100.0)
        self.assertTrue(math.isinf(iso_mid["T12_actual_sec"]))
        self.assertIn("Seniority Isomer", iso_mid["isomer_status"])

        # Away from mid-shell (n = 2)
        iso_2 = evaluate_seniority_isomer_properties(j_orbital=5.5, n_particles=2, E_gamma_keV=297.0)
        self.assertFalse(math.isinf(iso_2["T12_actual_sec"]))
        self.assertGreater(iso_2["T12_actual_sec"], 0.0)
        self.assertIn("Normal Seniority Decay", iso_2["isomer_status"])

    def test_invalid_parameters_raised(self):
        """Integer spins or occupancy exceeding shell capacity must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_seniority_fractional_factor(j_orbital=2.0, n_particles=2) # integer j
        with self.assertRaises(ValueError):
            calculate_seniority_fractional_factor(j_orbital=5.5, n_particles=15) # n > 12

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        # Away from mid-shell gives finite floats
        iso = evaluate_seniority_isomer_properties(j_orbital=5.5, n_particles=2, E_gamma_keV=100.0)
        s = json.dumps(iso, allow_nan=False)
        self.assertIn("b_e2_scaling_factor", s)


if __name__ == "__main__":
    unittest.main()
