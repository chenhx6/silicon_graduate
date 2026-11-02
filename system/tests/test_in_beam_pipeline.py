"""
Unit tests for In-Beam Experimental Nuclear Spectroscopy Master Pipeline Workbench.

Benchmarked against:
  - 135Pr wobbling controversy dataset (Matta 2015 / Sensharma 2019 / Nomura 2025).
  - 134Pr chiral doublet candidate dataset (Petrache 1996 / Tonev 2006 / Meng 2025).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from in_beam_experiment_analysis_pipeline import run_full_in_beam_pipeline


class InBeamPipelineTests(unittest.TestCase):

    def test_135Pr_wobbling_audit_pipeline(self):
        """Pipeline must execute full chain and detect dual roots for 135Pr linking transition."""
        res = run_full_in_beam_pipeline(
            Z_p=7, A_p=14, Z_t=50, A_t=124, E_lab_MeV=65.0,
            E_gamma_keV=726.5, detector_angle_deg=90.0, opening_angle_deg=8.0,
            a2_exp=-0.18, I_initial=8.5, I_final=7.5,
            F_tau_exp=0.55, F_tau_err=0.04, alpha_stop_ps=0.85,
            candidate_mode="wobbling",
            E_2plus_core_keV=409.2, B_E2_core_e2_b2=0.78
        )
        self.assertEqual(res["pipeline_version"], "1.0-Production")
        # Stage 1: Entrance reaction
        self.assertAlmostEqual(res["stage1_entrance_reaction"]["Wong_cross_section_mb"], 840.8, places=0)
        # Stage 2: Doppler broadening
        self.assertAlmostEqual(res["stage2_doppler_broadening"]["total_observed_fwhm_keV"], 2.39, places=1)
        # Stage 3: Dual roots for delta
        s3 = res["stage3_angular_distribution_delta"]
        self.assertAlmostEqual(s3["root1_small_magnitude"], 0.253, places=2)
        self.assertAlmostEqual(s3["root2_large_magnitude"], 7.036, places=2)
        # Stage 4: Lifetime inversion
        self.assertAlmostEqual(res["stage4_lifetime_dsam"]["tau_ps"], 0.6767, places=2)
        # Stage 6: Mode diagnostic
        diag = res["stage6_mode_diagnostic"]
        self.assertIn("delta_root1", diag)
        self.assertIn("delta_root2", diag)

    def test_134Pr_chiral_audit_pipeline(self):
        """Pipeline executes chiral audit on 134Pr candidate partner band."""
        res = run_full_in_beam_pipeline(
            Z_p=5, A_p=11, Z_t=52, A_t=128, E_lab_MeV=60.0,
            E_gamma_keV=450.0, a2_exp=0.32, I_initial=11.0, I_final=10.0,
            candidate_mode="chiral"
        )
        self.assertEqual(res["candidate_mode"], "chiral")
        self.assertIn("chiral_criteria", res["stage6_mode_diagnostic"])

    def test_low_count_feldman_cousins_integration(self):
        """When counts <= 15, pipeline automatically executes Feldman-Cousins interval."""
        res = run_full_in_beam_pipeline(
            Z_p=7, A_p=14, Z_t=50, A_t=124, E_lab_MeV=65.0,
            E_gamma_keV=726.5, n_counts=2, background_counts=3.0
        )
        self.assertIsNotNone(res["stage7_low_count_feldman_cousins"])
        fc = res["stage7_low_count_feldman_cousins"]
        self.assertEqual(fc["fc_interval_lower"], 0.0)
        self.assertTrue(fc["is_upper_limit"])

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = run_full_in_beam_pipeline(
            Z_p=7, A_p=14, Z_t=50, A_t=124, E_lab_MeV=65.0,
            E_gamma_keV=726.5, a2_exp=-0.18, F_tau_exp=0.55
        )
        s = json.dumps(res, allow_nan=False)
        self.assertIn("pipeline_version", s)


if __name__ == "__main__":
    unittest.main()
