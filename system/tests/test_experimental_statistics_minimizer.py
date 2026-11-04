"""Focused tests for Zhu Ch. 13 minimization and profile errors."""

import math
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from experimental_statistics_minimizer import (
    golden_section_minimize,
    profile_threshold_interval,
)


class ExperimentalStatisticsMinimizerTests(unittest.TestCase):
    def test_golden_section_finds_bounded_quadratic_minimum(self):
        result = golden_section_minimize(lambda x: (x - 1.75) ** 2 + 2.0, -3.0, 5.0)
        self.assertAlmostEqual(result["x"], 1.75, places=6)
        self.assertAlmostEqual(result["objective"], 2.0, places=10)
        self.assertTrue(result["converged"])

    def test_profile_threshold_returns_asymmetric_endpoints(self):
        def objective(x):
            return (x - 1.0) ** 2 if x <= 1.0 else 2.0 * (x - 1.0) ** 2

        result = profile_threshold_interval(objective, 1.0, 4.0, -5.0, 5.0)
        self.assertAlmostEqual(result["lower"], -1.0, places=6)
        self.assertAlmostEqual(result["upper"], 1.0 + math.sqrt(2.0), places=6)
        self.assertAlmostEqual(result["lower_error"], 2.0, places=6)
        self.assertAlmostEqual(result["upper_error"], math.sqrt(2.0), places=6)

    def test_profile_reports_open_side_without_fabricating_error(self):
        result = profile_threshold_interval(lambda x: math.exp(-x), 0.0, 1.0, -2.0, 2.0)
        self.assertEqual(result["lower_status"], "crossed")
        self.assertEqual(result["upper_status"], "open")
        self.assertIsNone(result["upper"])


if __name__ == "__main__":
    unittest.main()
