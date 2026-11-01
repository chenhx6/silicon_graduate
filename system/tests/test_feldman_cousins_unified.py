"""
Unit tests for Feldman-Cousins Unified Confidence Intervals with Physical Boundaries.

Benchmarked against:
  - G. J. Feldman and R. D. Cousins, Phys. Rev. D 57, 3873 (1998), Tables IV and X.
  - 朱永生, 《实验物理中的概率和统计（第二版）》, 科学出版社 (2006), 第11章 (小信号测量的区间估计, 印刷 pp. 370–383).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from feldman_cousins_unified_confidence_interval_calculator import (
    calculate_poisson_fc_interval,
    calculate_gaussian_fc_interval
)


class FeldmanCousinsUnifiedTests(unittest.TestCase):

    def test_poisson_zero_background_table_iv(self):
        """Verify Poisson 90% CL intervals for b = 0 match Feldman-Cousins (1998) Table IV."""
        # Table IV: b = 0.0: n=0 [0.00, 2.44], n=1 [0.11, 4.36], n=2 [0.53, 5.91], n=3 [1.10, 7.42]
        res0 = calculate_poisson_fc_interval(n_obs=0, background=0.0, cl=0.90)
        self.assertEqual(res0["fc_interval_lower"], 0.0)
        self.assertAlmostEqual(res0["fc_interval_upper"], 2.435, places=1)
        self.assertTrue(res0["is_upper_limit"])

        res1 = calculate_poisson_fc_interval(n_obs=1, background=0.0, cl=0.90)
        self.assertAlmostEqual(res1["fc_interval_lower"], 0.105, places=1)
        self.assertAlmostEqual(res1["fc_interval_upper"], 4.355, places=1)

        res2 = calculate_poisson_fc_interval(n_obs=2, background=0.0, cl=0.90)
        self.assertAlmostEqual(res2["fc_interval_lower"], 0.535, places=1)
        self.assertAlmostEqual(res2["fc_interval_upper"], 5.905, places=1)

    def test_poisson_finite_background_transition(self):
        """Verify automatic transition from Upper Limit (n <= b) to Two-Sided Interval (n > b)."""
        # Background b = 3.0, 90% CL
        # When n = 0 <= b: upper limit
        res_0 = calculate_poisson_fc_interval(n_obs=0, background=3.0, cl=0.90)
        self.assertEqual(res_0["fc_interval_lower"], 0.0)
        self.assertLess(res_0["fc_interval_upper"], 1.15)
        self.assertTrue(res_0["is_upper_limit"])
        self.assertIn("Upper Limit", res_0["interval_classification"])

        # When n = 6 > b: two-sided interval
        res_6 = calculate_poisson_fc_interval(n_obs=6, background=3.0, cl=0.90)
        self.assertGreater(res_6["fc_interval_lower"], 0.0)
        self.assertFalse(res_6["is_upper_limit"])
        self.assertIn("Two-Sided", res_6["interval_classification"])

    def test_gaussian_physical_boundary_table_x(self):
        """Verify Gaussian 90% CL intervals with mu >= 0 match Feldman-Cousins Table X."""
        # Table X: x = -2.0 [0.00, 0.40], x = -1.5 [0.00, 0.55], x = 0.0 [0.00, 1.64], x = 2.0 [0.58, 3.64]
        g_m20 = calculate_gaussian_fc_interval(x_obs=-2.0, sigma=1.0, cl=0.90)
        self.assertEqual(g_m20["mu_fc_lower"], 0.0)
        self.assertAlmostEqual(g_m20["mu_fc_upper"], 0.402, places=2)

        g_m15 = calculate_gaussian_fc_interval(x_obs=-1.5, sigma=1.0, cl=0.90)
        self.assertEqual(g_m15["mu_fc_lower"], 0.0)
        self.assertAlmostEqual(g_m15["mu_fc_upper"], 0.555, places=2)

        g_00 = calculate_gaussian_fc_interval(x_obs=0.0, sigma=1.0, cl=0.90)
        self.assertEqual(g_00["mu_fc_lower"], 0.0)
        self.assertAlmostEqual(g_00["mu_fc_upper"], 1.645, places=2)

        g_20 = calculate_gaussian_fc_interval(x_obs=2.0, sigma=1.0, cl=0.90)
        self.assertAlmostEqual(g_20["mu_fc_lower"], 0.582, places=2)
        self.assertAlmostEqual(g_20["mu_fc_upper"], 3.645, places=2)

    def test_invalid_parameters_raised(self):
        """Invalid inputs must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_poisson_fc_interval(n_obs=-1, background=3.0)
        with self.assertRaises(ValueError):
            calculate_poisson_fc_interval(n_obs=5, background=-1.0)
        with self.assertRaises(ValueError):
            calculate_gaussian_fc_interval(x_obs=1.0, sigma=-1.0)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        p_res = calculate_poisson_fc_interval(n_obs=0, background=3.0, cl=0.90)
        g_res = calculate_gaussian_fc_interval(x_obs=-1.5, sigma=1.0, cl=0.90)
        payload = {"poisson": p_res, "gaussian": g_res}
        s = json.dumps(payload, allow_nan=False)
        self.assertIn("fc_interval_upper", s)


if __name__ == "__main__":
    unittest.main()
