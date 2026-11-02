#!/usr/bin/env python3
"""
Unit tests for in_beam_spin_alignment_sigma_mixing_ratio_extractor.py (Module 161).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_spin_alignment_sigma_mixing_ratio_extractor import (
    PRESETS,
    SpinAlignmentMixingExtractor,
    calculate_alpha_k,
    calculate_A_k_theoretical
)

class TestInBeamSpinAlignment(unittest.TestCase):

    def test_alignment_attenuation_limits(self):
        # When sigma -> 0 (full alignment), alpha_k -> 1.0
        a2_full = calculate_alpha_k(4.0, 0.001, 2)
        self.assertAlmostEqual(a2_full, 1.0, places=3)

        # When sigma is large, alpha_k must decrease towards 0
        a2_mid = calculate_alpha_k(4.0, 2.0, 2)
        a2_wide = calculate_alpha_k(4.0, 10.0, 2)
        self.assertGreater(a2_full, a2_mid)
        self.assertGreater(a2_mid, a2_wide)
        self.assertLess(a2_wide, 0.1)

    def test_pure_E2_reference_calibration(self):
        p = PRESETS["130Ba_wobbling_candidate_delta"]
        ext = SpinAlignmentMixingExtractor(
            I_ref_i=p["reference_E2"]["I_initial"],
            I_ref_f=p["reference_E2"]["I_final"],
            a2_ref=p["reference_E2"]["a2_exp"],
            sigma_a2_ref=p["reference_E2"]["sigma_a2"],
            a4_ref=p["reference_E2"]["a4_exp"],
            sigma_a4_ref=p["reference_E2"]["sigma_a4"]
        )
        cal = ext.extract_sigma_over_I()
        # Calibrated sigma/I must be in realistic heavy-ion range ~ 0.3 - 0.55
        self.assertGreater(cal["sigma_over_I"], 0.25)
        self.assertLess(cal["sigma_over_I"], 0.60)
        self.assertGreater(cal["alpha2_measured"], 0.40)
        self.assertLess(cal["alpha2_measured"], 0.95)

    def test_mixing_ratio_inversion(self):
        p = PRESETS["128Cs_chiral_partner_dipole"]
        ext = SpinAlignmentMixingExtractor(
            I_ref_i=p["reference_E2"]["I_initial"],
            I_ref_f=p["reference_E2"]["I_final"],
            a2_ref=p["reference_E2"]["a2_exp"],
            sigma_a2_ref=p["reference_E2"]["sigma_a2"],
            a4_ref=p["reference_E2"]["a4_exp"],
            sigma_a4_ref=p["reference_E2"]["sigma_a4"]
        )
        res = ext.invert_mixing_ratio(
            I_tgt_i=p["target_transition"]["I_initial"],
            I_tgt_f=p["target_transition"]["I_final"],
            a2_tgt=p["target_transition"]["a2_exp"],
            sig_a2_tgt=p["target_transition"]["sigma_a2"],
            a4_tgt=p["target_transition"]["a4_exp"],
            sig_a4_tgt=p["target_transition"]["sigma_a4"]
        )
        # Chiral partner dipole transition should be predominantly M1 (|delta| < 0.2)
        self.assertLess(abs(res["best_fit_delta"]), 0.2)
        self.assertTrue(res["is_pure_dipole"])

if __name__ == "__main__":
    unittest.main()
