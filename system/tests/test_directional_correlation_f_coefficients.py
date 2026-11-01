"""
Unit tests for Directional Correlation F-Coefficients, Angular Distribution &
Dual-Root Mixing Ratio Inversion.

Benchmarked against:
  - W. D. Hamilton (1975), The Electromagnetic Interaction in Nuclear Spectroscopy, Appendix 2
  - 卢希庭 (2000), 《原子核物理（修订版）》, 第7章 §7.6
"""

import math
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from directional_correlation_f_coefficients_calculator import (
    calculate_f_coefficient,
    calculate_angular_distribution_coefficients,
    invert_delta_dual_roots,
    calculate_dco_and_ado_ratios
)


class DirectionalCorrelationFCoefficientsTests(unittest.TestCase):

    def test_hamilton_table_appendix2_benchmarks(self):
        """Verify exact agreement with printed tables in Hamilton (1975) Appendix 2."""
        # Hamilton p. 890 / PDF p. 901, I1 = 1:
        # L=1, L'=1, I0=0, I1=1: F2 = +0.7071
        f2_10 = calculate_f_coefficient(2, 1, 1, If=0.0, Ii=1.0)
        self.assertAlmostEqual(f2_10, 0.7071, places=3)

        # L=1, L'=1, I0=1, I1=1: F2 = -0.3536
        f2_11 = calculate_f_coefficient(2, 1, 1, If=1.0, Ii=1.0)
        self.assertAlmostEqual(f2_11, -0.3536, places=3)

        # L=1, L'=2, I0=1, I1=1: F2 = -1.0607
        f2_12 = calculate_f_coefficient(2, 1, 2, If=1.0, Ii=1.0)
        self.assertAlmostEqual(f2_12, -1.0607, places=3)

        # L=2, L'=2, I0=1, I1=1: F2 = -0.3536
        f2_22 = calculate_f_coefficient(2, 2, 2, If=1.0, Ii=1.0)
        self.assertAlmostEqual(f2_22, -0.3536, places=3)

        # L=1, L'=1, I0=2, I1=1: F2 = +0.0707
        f2_21 = calculate_f_coefficient(2, 1, 1, If=2.0, Ii=1.0)
        self.assertAlmostEqual(f2_21, 0.0707, places=3)

        # Hamilton p. 891 / PDF p. 902, I1 = 3/2:
        # L=1, L'=1, I0=3/2, I1=3/2: F2 = -0.4000
        f2_half_11 = calculate_f_coefficient(2, 1, 1, If=1.5, Ii=1.5)
        self.assertAlmostEqual(f2_half_11, -0.4000, places=3)

        # L=1, L'=2, I0=3/2, I1=3/2: F2 = -0.7746
        f2_half_12 = calculate_f_coefficient(2, 1, 2, If=1.5, Ii=1.5)
        self.assertAlmostEqual(f2_half_12, -0.7746, places=3)

        # L=2, L'=2, I0=3/2, I1=3/2: F2 = 0.0000
        f2_half_22 = calculate_f_coefficient(2, 2, 2, If=1.5, Ii=1.5)
        self.assertAlmostEqual(f2_half_22, 0.0000, places=3)

    def test_pure_e2_stretched_transition(self):
        """Verify 2+ -> 0+ stretched E2 transition coefficients."""
        f2 = calculate_f_coefficient(2, 2, 2, If=0.0, Ii=2.0)
        f4 = calculate_f_coefficient(4, 2, 2, If=0.0, Ii=2.0)
        self.assertAlmostEqual(f2, -0.5976, places=3)
        self.assertAlmostEqual(f4, -1.0690, places=3)

    def test_multipole_symmetry(self):
        """F_k(L, L', If, Ii) must be symmetric under L <-> L' interchange."""
        for Ii in [1.0, 2.0, 3.5, 7.5]:
            for If in [Ii - 1.0, Ii, Ii + 1.0]:
                if If < 0:
                    continue
                f_12 = calculate_f_coefficient(2, 1, 2, If, Ii)
                f_21 = calculate_f_coefficient(2, 2, 1, If, Ii)
                self.assertAlmostEqual(f_12, f_21, places=6)

    def test_dual_root_analytic_roundtrip(self):
        """Forward compute a2 from delta = -0.15, then invert: root1 must recover -0.15."""
        Ii, If = 7.5, 6.5 # 15/2 -> 13/2
        true_delta = -0.15
        alpha2 = 0.85

        dist = calculate_angular_distribution_coefficients(Ii, If, delta=true_delta, alpha2=alpha2)
        a2_theo = dist["attenuated_a_k"]["a2"]

        inv = invert_delta_dual_roots(a2_theo, Ii, If, alpha2=alpha2)
        self.assertTrue(inv["has_real_roots"])
        self.assertAlmostEqual(inv["root1_small_magnitude"], true_delta, places=4)
        self.assertIsNotNone(inv["root2_large_magnitude"])
        # Root 2 must give the EXACT same a2
        dist_root2 = calculate_angular_distribution_coefficients(Ii, If, delta=inv["root2_large_magnitude"], alpha2=alpha2)
        self.assertAlmostEqual(dist_root2["attenuated_a_k"]["a2"], a2_theo, places=3)

    def test_unphysical_a2_returns_no_real_roots(self):
        """An unphysically large a2 must result in negative discriminant and no real roots."""
        inv = invert_delta_dual_roots(a2_measured=2.50, Ii=7.5, If=6.5, alpha2=0.85)
        self.assertFalse(inv["has_real_roots"])
        self.assertIsNone(inv["root1_small_magnitude"])
        self.assertIsNone(inv["root2_large_magnitude"])
        self.assertIn("No real roots", inv["verdict"])

    def test_dco_and_ado_ratio_calculation(self):
        """Verify DCO ratio calculation between 30 and 90 degrees."""
        dco = calculate_dco_and_ado_ratios(Ii=7.5, If=6.5, delta=-0.15, theta1_deg=30.0, theta2_deg=90.0)
        self.assertGreater(dco["R_DCO"], 1.0)
        self.assertAlmostEqual(dco["R_DCO"], dco["W_theta1"] / dco["W_theta2"], places=4)


if __name__ == "__main__":
    unittest.main()
