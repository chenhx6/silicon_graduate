#!/usr/bin/env python3
"""
Unit tests for hpge_neutron_damage_hole_trapping_corrector.py (Module 165).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from hpge_neutron_damage_hole_trapping_corrector import (
    PRESETS,
    HPGeneutronDamageTrappingCorrector
)

class TestHPGeNeutronDamageTrapping(unittest.TestCase):

    def test_moderate_damage_restoration(self):
        p = PRESETS["moderate_neutron_damage_1332keV"]
        corrector = HPGeneutronDamageTrappingCorrector(
            E_true_keV=p["E_true_keV"],
            fwhm_undamaged_keV=p["fwhm_undamaged_keV"],
            hole_lifetime_us=p["hole_lifetime_us"],
            detector_depth_cm=p["detector_depth_cm"],
            t_r_min_ns=p["t_r_min_ns"]
        )
        res = corrector.execute_restoration(n_events=12000)
        # Check that FWHM resolution improved significantly (> 10%)
        self.assertGreater(res["fwhm_improvement_percent"], 10.0)
        # Restored FWHM should approach undamaged target
        self.assertLess(res["restored_metrics"]["fwhm_keV"], 2.30)
        # FWTM/FWHM ratio should improve towards 1.82
        self.assertLess(res["restored_metrics"]["fwtm_fwhm_ratio"],
                        res["raw_damaged_metrics"]["fwtm_fwhm_ratio"])
        self.assertTrue(res["is_resolution_recovered"])

    def test_centroid_recovery(self):
        p = PRESETS["severe_neutron_damage_850keV"]
        corrector = HPGeneutronDamageTrappingCorrector(
            E_true_keV=p["E_true_keV"],
            fwhm_undamaged_keV=p["fwhm_undamaged_keV"],
            hole_lifetime_us=p["hole_lifetime_us"],
            detector_depth_cm=p["detector_depth_cm"],
            t_r_min_ns=p["t_r_min_ns"]
        )
        res = corrector.execute_restoration(n_events=12000)
        # Centroid error should be less than 0.5 keV after restoration
        centroid_err = abs(res["restored_metrics"]["centroid_keV"] - p["E_true_keV"])
        self.assertLess(centroid_err, 0.50)

if __name__ == "__main__":
    unittest.main()
