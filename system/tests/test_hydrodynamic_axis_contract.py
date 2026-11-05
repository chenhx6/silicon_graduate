"""Regression tests for the hydrodynamic Lund-axis convention."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from davydov_wobbling_rotor_calculator import (
    calculate_hydrodynamic_inertias,
    hydrodynamic_inertia_contract,
    check_greiner_sum_rule,
    davydov_filippov_energies_and_be2,
)


class HydrodynamicAxisContractTests(unittest.TestCase):
    def test_named_order_is_monotonic_across_gamma_branches(self):
        for gamma in (0.0, 20.0, 30.0, 40.0, 60.0):
            contract = hydrodynamic_inertia_contract(gamma)
            self.assertLessEqual(contract["A_m_keV"], contract["A_s_keV"])
            self.assertLessEqual(contract["A_s_keV"], contract["A_l_keV"])

    def test_long_axis_and_short_axis_are_exchanged_above_thirty_degrees(self):
        contract = hydrodynamic_inertia_contract(40.0)
        self.assertTrue(contract["axis_permutation_applied"])
        self.assertEqual(
            contract["raw_k_axis_mapping"],
            "A_m=A1,A_s=A3,A_l=A2",
        )
        raw = contract["raw_A1_A2_A3_keV"]
        self.assertAlmostEqual(contract["A_m_keV"], raw[0])
        self.assertAlmostEqual(contract["A_s_keV"], raw[2])
        self.assertAlmostEqual(contract["A_l_keV"], raw[1])

    def test_axial_limits_are_reported_without_shape_name_inference(self):
        self.assertEqual(
            hydrodynamic_inertia_contract(0.0)["axial_limit"],
            "J_m = J_s (A_m = A_s)",
        )
        self.assertEqual(
            hydrodynamic_inertia_contract(60.0)["axial_limit"],
            "J_s = J_l (A_s = A_l)",
        )

    def test_gamma_and_physical_inputs_are_bounded(self):
        with self.assertRaises(ValueError):
            calculate_hydrodynamic_inertias(-0.1)
        with self.assertRaises(ValueError):
            calculate_hydrodynamic_inertias(60.1)
        with self.assertRaises(ValueError):
            calculate_hydrodynamic_inertias(20.0, beta2=0.0)

    def test_greiner_sum_rule_exact_satisfaction(self):
        res = check_greiner_sum_rule(357.0, 901.0, 1258.0)
        self.assertAlmostEqual(res["residual_keV"], 0.0)
        self.assertAlmostEqual(res["relative_discrepancy_pct"], 0.0)
        self.assertEqual(res["greiner_sum_rule_verdict"], "RIGID_ASYMMETRIC_ROTOR_SCREENING_PASS")

    def test_greiner_branching_ratio_at_30_degrees(self):
        res = davydov_filippov_energies_and_be2(30.0, 100.0)
        self.assertAlmostEqual(res["E2_2_over_E2_1"], 2.0, places=2)
        # B(E2; 2_2->0_1) / B(E2; 2_2->2_1) at gamma=30 deg is 7/40 = 0.1750
        self.assertAlmostEqual(res["B_E2_22_to_01_over_22_to_21"], 0.1750, places=3)


if __name__ == "__main__":
    unittest.main()
