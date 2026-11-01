"""Regression against using a model preference as independent spectroscopy."""

import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from wobbling_branching_ratio_phase_calculator import (
    calculate_theoretical_wobbling_delta,
    compare_wobbling_with_experimental_roots,
    mixing_from_matrix_elements,
)


class MixingBoundaryTests(unittest.TestCase):
    def test_intrinsic_inputs_do_not_supply_transition_elements(self):
        for mode in ("TW", "LW"):
            result = calculate_theoretical_wobbling_delta(
                15.5, 5.5, 26.0, 720.0, 5.0, 1.25, 0.40, mode
            )
            self.assertIsNone(result["theoretical_delta_E2_M1"])
            self.assertEqual(result["amplitude_status"], "insufficient-model-input")

    def test_theory_equal_to_one_root_does_not_select_it(self):
        result = compare_wobbling_with_experimental_roots(3.10, -0.15, 3.10)
        self.assertIsNone(result["selected_matching_root"])
        self.assertFalse(result["is_wobbling_confirmed"])
        self.assertEqual(len(result["candidates"]), 2)

    def test_signed_amplitude_conversion_and_fraction(self):
        result = mixing_from_matrix_elements(1000.0, -2.0, 0.835)
        self.assertAlmostEqual(result["theoretical_delta_E2_M1"], -2.0)
        self.assertAlmostEqual(result["E2_multipolarity_fraction_percent"], 80.0)
        self.assertIn("negative", result["phase_sign"])

    def test_zero_amplitudes_and_invalid_values(self):
        self.assertEqual(mixing_from_matrix_elements(1000, 0, 1)[
            "E2_multipolarity_fraction_percent"], 0.0)
        pure = mixing_from_matrix_elements(1000, 1, 0)
        self.assertIsNone(pure["theoretical_delta_E2_M1"])
        self.assertEqual(pure["E2_multipolarity_fraction_percent"], 100.0)
        json.dumps(pure, allow_nan=False)
        for args in [(1000, 0, 0), (0, 1, 1), (float("nan"), 1, 1)]:
            with self.assertRaises(ValueError):
                mixing_from_matrix_elements(*args)

    def test_large_roots_and_order_preserve_both_candidates(self):
        result = compare_wobbling_with_experimental_roots(None, 1e250, -1e250)
        self.assertEqual(len(result["candidates"]), 2)
        self.assertFalse(result["is_wobbling_confirmed"])
        json.dumps(result, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
