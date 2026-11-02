"""
Unit tests for In-Beam Level Scheme Loop Residuals & Level Intensity Balancer.

Benchmarked against:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第10章 §10.6.
  - D. C. Radford, Nucl. Instrum. Methods Phys. Res. A 361, 297 (1995) [Radware].
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from level_scheme_loop_residual_intensity_balancer import (
    evaluate_ritz_combination_loop,
    calculate_level_intensity_balance
)


class LevelSchemeLoopBalancerTests(unittest.TestCase):

    def test_consistent_ritz_energy_loop(self):
        """Consistent closed loops must yield residual ~ 0 and Z-score < 1.0."""
        # 134Ce Loop: 2_g+ -> 2+ (556.0 keV) + 2+ -> 0+ (409.2 keV) = 965.2 keV vs 2_g+ -> 0+ (965.2 keV)
        l_fwd = [("2_g+ -> 2+", 556.0, 0.2), ("2+ -> 0+", 409.2, 0.2)]
        l_bwd = [("2_g+ -> 0+", 965.2, 0.3)]
        res = evaluate_ritz_combination_loop("Loop 1 (2_g+ cross)", l_fwd, l_bwd)
        self.assertAlmostEqual(res["delta_E_residual_keV"], 0.0, places=2)
        self.assertLess(res["normalized_z_score"], 0.1)
        self.assertIn("Excellent", res["verdict"])

    def test_conflict_energy_loop_detection(self):
        """Inconsistent loops with delta_E > 3*sigma must be flagged as discrepant."""
        l_fwd = [("4+ -> 2+", 700.0, 0.5), ("2+ -> 0+", 500.0, 0.5)]
        l_bwd = [("4+ -> 0+ (wrong)", 1208.0, 0.8)]
        res = evaluate_ritz_combination_loop("Conflict Loop", l_fwd, l_bwd)
        self.assertAlmostEqual(res["delta_E_residual_keV"], -8.0, places=1)
        self.assertGreater(res["normalized_z_score"], 7.0)
        self.assertIn("Discrepant", res["verdict"])

    def test_level_intensity_balance_and_side_feeding(self):
        """Intensity balancer correctly extracts prompt reaction side-feeding I_side = I_out - I_in."""
        levels = [
            {"level_id": "0+", "energy_keV": 0.0},
            {"level_id": "2+", "energy_keV": 409.2},
            {"level_id": "4+", "energy_keV": 1048.9},
            {"level_id": "6+", "energy_keV": 1819.3}
        ]
        transitions = [
            {"from": "6+", "to": "4+", "I_gamma": 42.0, "alpha_tot": 0.005},
            {"from": "4+", "to": "2+", "I_gamma": 78.0, "alpha_tot": 0.012},
            {"from": "2+", "to": "0+", "I_gamma": 100.0, "alpha_tot": 0.035}
        ]
        balances = calculate_level_intensity_balance(levels, transitions)
        self.assertEqual(len(balances), 4)

        # 6+ top state has no incoming feeder => 100% side-feeding
        b6 = [b for b in balances if b["level_id"] == "6+"][0]
        self.assertEqual(b6["side_feeding_fraction_pct"], 100.0)

        # 4+ intermediate state has side-feeding I_out - I_in = 78.94 - 42.21 = 36.73
        b4 = [b for b in balances if b["level_id"] == "4+"][0]
        self.assertAlmostEqual(b4["extracted_side_feeding_I_side"], 36.73, places=2)
        self.assertAlmostEqual(b4["side_feeding_fraction_pct"], 46.5, places=1)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        l_fwd = [("A", 100.0, 0.1)]
        l_bwd = [("B", 100.0, 0.1)]
        res = evaluate_ritz_combination_loop("Loop", l_fwd, l_bwd)
        s = json.dumps(res, allow_nan=False)
        self.assertIn("delta_E_residual_keV", s)


if __name__ == "__main__":
    unittest.main()
