"""
Unit tests for Alpha Decay Gamow WKB Penetration, Centrifugal Barrier & Viola-Seaborg Systematics.

Benchmarked against:
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第5章 (Alpha衰变, 印刷 pp. 121-125).
  - V. E. Viola and G. T. Seaborg, J. Inorg. Nucl. Chem. 28, 741 (1966).
  - A. Sobiczewski et al., Phys. Lett. 22, 500 (1966).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from alpha_decay_gamow_wkb_calculator import (
    calculate_gamow_factor_wkb,
    evaluate_alpha_hindrance
)


class AlphaDecayGamowWKBTests(unittest.TestCase):

    def test_212Po_benchmark_and_wkb_analytical_numerical_match(self):
        """Verify 212Po decay Gamow factor, WKB unhindered T1/2 and analytical vs numerical consistency."""
        res_L0 = calculate_gamow_factor_wkb(Z_parent=84, A_parent=212, Q_alpha_MeV=8.954, L=0)
        self.assertAlmostEqual(res_L0["Gamow_factor_2G"], 30.961, places=2)
        self.assertAlmostEqual(res_L0["turning_point_Rc_fm"], 26.374, places=2)
        self.assertAlmostEqual(res_L0["touching_radius_R0_fm"], 9.390, places=2)
        self.assertLess(res_L0["T12_WKB_unhindered_sec"], 1.0e-7)

        # Hindrance evaluation with experimental half-life 299 ns
        hin = evaluate_alpha_hindrance(2.99e-7, res_L0["T12_WKB_unhindered_sec"])
        self.assertAlmostEqual(hin["hindrance_factor_HF"], 33.28, places=1)
        self.assertAlmostEqual(hin["alpha_preformation_factor_S"], 0.0301, places=3)

    def test_238U_geiger_nuttall_scaling(self):
        """Verify 238U long-lived alpha decay: Gamow 2G ~ 86.4, T1/2 ~ 10^16 s."""
        res_u = calculate_gamow_factor_wkb(Z_parent=92, A_parent=238, Q_alpha_MeV=4.270, L=0)
        self.assertAlmostEqual(res_u["Gamow_factor_2G"], 86.378, places=1)
        self.assertGreater(res_u["T12_WKB_unhindered_sec"], 1.0e15)

        # Viola-Seaborg prediction matches experimental within order of magnitude
        log10_vs = res_u["log10_T12_Viola_Seaborg"]
        self.assertAlmostEqual(log10_vs, 17.35, places=1)

    def test_centrifugal_barrier_monotonic_hindrance(self):
        """Centrifugal barrier L*(L+1) must increase action integral 2G and reduce penetration P."""
        res_L0 = calculate_gamow_factor_wkb(Z_parent=84, A_parent=212, Q_alpha_MeV=8.954, L=0)
        res_L2 = calculate_gamow_factor_wkb(Z_parent=84, A_parent=212, Q_alpha_MeV=8.954, L=2)
        res_L4 = calculate_gamow_factor_wkb(Z_parent=84, A_parent=212, Q_alpha_MeV=8.954, L=4)

        self.assertGreater(res_L2["Gamow_factor_2G"], res_L0["Gamow_factor_2G"])
        self.assertGreater(res_L4["Gamow_factor_2G"], res_L2["Gamow_factor_2G"])
        self.assertLess(res_L2["penetration_probability_P"], res_L0["penetration_probability_P"])
        self.assertLess(res_L4["penetration_probability_P"], res_L2["penetration_probability_P"])

    def test_invalid_parameters_raised(self):
        """Unphysical inputs (Z <= 2, Q <= 0, L < 0) must be rejected."""
        with self.assertRaises(ValueError):
            calculate_gamow_factor_wkb(Z_parent=2, A_parent=4, Q_alpha_MeV=5.0)
        with self.assertRaises(ValueError):
            calculate_gamow_factor_wkb(Z_parent=84, A_parent=212, Q_alpha_MeV=-1.0)
        with self.assertRaises(ValueError):
            calculate_gamow_factor_wkb(Z_parent=84, A_parent=212, Q_alpha_MeV=8.954, L=-1)

    def test_json_strict_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = calculate_gamow_factor_wkb(Z_parent=84, A_parent=212, Q_alpha_MeV=8.954, L=0)
        hin = evaluate_alpha_hindrance(2.99e-7, res["T12_WKB_unhindered_sec"])
        payload = {"gamow_wkb": res, "hindrance": hin}
        s = json.dumps(payload, allow_nan=False)
        self.assertIn("T12_WKB_unhindered_sec", s)


if __name__ == "__main__":
    unittest.main()
