#!/usr/bin/env python3
"""
Unit tests for in_beam_rdds_ddcm_lifetime_inverter.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_rdds_ddcm_lifetime_inverter import (
    PRESETS,
    evaluate_ddcm_curve,
    extract_plateau_lifetime_and_be2,
    run_rdds_ddcm_analysis
)


class TestRDDSLinearLifetime(unittest.TestCase):

    def test_recoil_velocity_calculation(self):
        pts, v_um = evaluate_ddcm_curve(PRESETS["134Ce_2plus_rdds_plunger"]["measurements"], beta_recoil=0.0210)
        # v = 0.0210 * 299.792 ~ 6.296 um/ps
        self.assertAlmostEqual(v_um, 6.296, places=2)
        self.assertEqual(len(pts), 8)

    def test_134Ce_ddcm_plateau_lifetime(self):
        p = PRESETS["134Ce_2plus_rdds_plunger"]
        res = run_rdds_ddcm_analysis(
            nucleus=p["nucleus"],
            E_gamma_keV=p["E_gamma_keV"],
            beta_recoil=p["beta_recoil"],
            spin_I=p["spin_initial"],
            K_val=p["K_quantum"],
            measurements=p["measurements"]
        )
        pl = res["plateau_results"]
        # Lifetime should be extracted around 14 - 16 ps
        self.assertAlmostEqual(pl["mean_lifetime_tau_ps"], 14.9, places=0)
        self.assertGreater(pl["plateau_points_count"], 3)
        # Collectivity B(E2) should be > 50 W.u.
        self.assertGreater(pl["B_E2_W_u"], 50.0)
        self.assertGreater(pl["intrinsic_quadrupole_moment_Q0_eb"], 3.0)

    def test_short_lifetime_limit(self):
        p = PRESETS["rapid_decay_short_lifetime_limit"]
        res = run_rdds_ddcm_analysis(
            nucleus=p["nucleus"],
            E_gamma_keV=p["E_gamma_keV"],
            beta_recoil=p["beta_recoil"],
            spin_I=p["spin_initial"],
            K_val=p["K_quantum"],
            measurements=p["measurements"]
        )
        pl = res["plateau_results"]
        self.assertLess(pl["mean_lifetime_tau_ps"], 10.0)
        self.assertGreater(pl["mean_lifetime_tau_ps"], 0.5)


if __name__ == "__main__":
    unittest.main()
