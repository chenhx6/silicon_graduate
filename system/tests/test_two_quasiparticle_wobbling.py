#!/usr/bin/env python3
"""
Unit tests for two_quasiparticle_even_even_wobbling_analyzer.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from two_quasiparticle_even_even_wobbling_analyzer import (
    PRESETS,
    calculate_two_quasiparticle_wobbling_energies,
    evaluate_wobbling_slope_and_criteria,
    run_two_qp_wobbling_analysis
)


class TestTwoQuasiparticleWobbling(unittest.TestCase):

    def test_wobbling_energy_calculation(self):
        p = PRESETS["130Ba_two_quasiparticle_wobbler"]
        wobs = calculate_two_quasiparticle_wobbling_energies(p["yrast_levels"], p["wobbling_levels"])
        self.assertEqual(len(wobs), 4)
        self.assertAlmostEqual(wobs[0]["E_wob_keV"], 505.0, places=1)
        self.assertAlmostEqual(wobs[-1]["E_wob_keV"], 325.0, places=1)

    def test_130Ba_transverse_wobbling_confirmed(self):
        p = PRESETS["130Ba_two_quasiparticle_wobbler"]
        res = run_two_qp_wobbling_analysis(
            nucleus=p["nucleus"],
            quasiparticle_config=p["quasiparticle_config"],
            j_aligned=p["j_aligned"],
            gamma_deg=p["gamma_deg"],
            J_m=p["J_m_hbar2_per_MeV"],
            J_s=p["J_s_hbar2_per_MeV"],
            J_l=p["J_l_hbar2_per_MeV"],
            yrast_levels=p["yrast_levels"],
            wobbling_levels=p["wobbling_levels"]
        )
        wv = res["wobbling_verdict"]
        self.assertTrue(wv["is_transverse_trend"])
        self.assertLess(wv["slope_dE_wob_dI_keV_per_hbar"], -15.0)
        self.assertGreater(wv["confidence_score_pct"], 80.0)
        self.assertEqual(wv["wobbling_verdict"], "CONFIRMED_TWO_QUASIPARTICLE_TRANSVERSE_WOBBLING")

    def test_136Nd_predicted_wobbler(self):
        p = PRESETS["136Nd_two_quasiparticle_wobbler"]
        res = run_two_qp_wobbling_analysis(
            nucleus=p["nucleus"],
            quasiparticle_config=p["quasiparticle_config"],
            j_aligned=p["j_aligned"],
            gamma_deg=p["gamma_deg"],
            J_m=p["J_m_hbar2_per_MeV"],
            J_s=p["J_s_hbar2_per_MeV"],
            J_l=p["J_l_hbar2_per_MeV"],
            yrast_levels=p["yrast_levels"],
            wobbling_levels=p["wobbling_levels"]
        )
        wv = res["wobbling_verdict"]
        self.assertTrue(wv["is_transverse_trend"])
        self.assertEqual(wv["wobbling_verdict"], "CONFIRMED_TWO_QUASIPARTICLE_TRANSVERSE_WOBBLING")

    def test_spurious_counterexample_rejected(self):
        p = PRESETS["spurious_quasiparticle_counterexample"]
        res = run_two_qp_wobbling_analysis(
            nucleus=p["nucleus"],
            quasiparticle_config=p["quasiparticle_config"],
            j_aligned=p["j_aligned"],
            gamma_deg=p["gamma_deg"],
            J_m=p["J_m_hbar2_per_MeV"],
            J_s=p["J_s_hbar2_per_MeV"],
            J_l=p["J_l_hbar2_per_MeV"],
            yrast_levels=p["yrast_levels"],
            wobbling_levels=p["wobbling_levels"]
        )
        wv = res["wobbling_verdict"]
        self.assertFalse(wv["is_transverse_trend"])
        self.assertEqual(wv["wobbling_verdict"], "REJECTED_SPURIOUS_OR_SINGLE_PARTICLE_BAND")


if __name__ == "__main__":
    unittest.main()
