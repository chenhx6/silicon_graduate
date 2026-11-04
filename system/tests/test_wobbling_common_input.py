"""Cross-check the shared frozen-alignment wobbling convention."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from davydov_wobbling_rotor_calculator import (
    falsify_wobbling_vs_signature_partner,
    frauendorf_wobbling_frequency,
)
from triaxial_wobbling_tip_chiral_analyzer import (
    calculate_transverse_wobbling_spectrum,
)


class WobblingCommonInputTests(unittest.TestCase):
    def test_tw_frequency_matches_named_moi_implementation(self):
        # frauendorf_* takes A_m, A_s, A_l in keV. Convert the same input
        # to J_m, J_s, J_l for the independent named-MOI implementation.
        A_m, A_s, A_l = 12.0, 25.0, 45.0
        I, j = 10.5, 6.5
        J_m, J_s, J_l = (1000.0 / (2.0 * value) for value in (A_m, A_s, A_l))

        by_A = frauendorf_wobbling_frequency(I, j, A_m, A_s, A_l, mode="TW")
        by_J = calculate_transverse_wobbling_spectrum(
            J_m, J_s, J_l, j, [I]
        )["spectrum"][0]

        self.assertEqual(by_A["status"], "stable_harmonic")
        self.assertAlmostEqual(
            by_A["omega_wob_keV"],
            by_J["hbar_omega_TW_keV"],
            places=1,
        )

    def test_critical_and_supercritical_states_are_not_called_tip(self):
        result = frauendorf_wobbling_frequency(
            13.5, 6.5, 12.0, 25.0, 45.0, mode="TW"
        )
        self.assertEqual(result["status"], "HFA_unstable_requires_full_model")
        self.assertIsNone(result["mode_confirmed"])

    def test_electromagnetic_screen_is_conditional(self):
        result = falsify_wobbling_vs_signature_partner(
            be2_out_over_in=0.35,
            b_m1_out_w_u=0.04,
            delta_mixing_ratio=2.5,
        )
        self.assertEqual(
            result["verdict"],
            "MODEL_CRITERIA_SATISFIED__NOT_EXPERIMENTAL_CONFIRMATION",
        )
        self.assertIsNone(result["mode_confirmed"])


if __name__ == "__main__":
    unittest.main()
