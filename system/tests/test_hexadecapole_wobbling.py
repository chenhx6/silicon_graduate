#!/usr/bin/env python3
"""
Unit tests for triaxial_hexadecapole_deformation_wobbling_modifier.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from triaxial_hexadecapole_deformation_wobbling_modifier import (
    PRESETS,
    calculate_hexadecapole_modified_moi,
    calculate_wobbling_frequency_with_beta4,
    run_hexadecapole_wobbling_analysis
)


class TestHexadecapoleWobbling(unittest.TestCase):

    def test_pure_quadrupole_limit(self):
        p = PRESETS["pure_quadrupole_limit"]
        res = run_hexadecapole_wobbling_analysis(
            nucleus=p["nucleus"],
            beta2=p["beta2"],
            gamma_deg=p["gamma_deg"],
            beta4=p["beta4"],
            J_base=p["J_base_hbar2_per_MeV"],
            j_aligned=p["j_aligned_hbar"],
            spin_I=p["spin_I"]
        )
        w = res["wobbling_modification"]
        # At beta4 = 0, delta frequency must be strictly 0.0
        self.assertAlmostEqual(w["delta_wobbling_freq_keV"], 0.0, places=4)
        self.assertAlmostEqual(w["wobbling_freq_unperturbed_keV"], w["wobbling_freq_modified_keV"], places=4)

    def test_163Lu_positive_beta4_shift(self):
        p = PRESETS["163Lu_TSD_positive_beta4"]
        res = run_hexadecapole_wobbling_analysis(
            nucleus=p["nucleus"],
            beta2=p["beta2"],
            gamma_deg=p["gamma_deg"],
            beta4=p["beta4"],
            J_base=p["J_base_hbar2_per_MeV"],
            j_aligned=p["j_aligned_hbar"],
            spin_I=p["spin_I"]
        )
        w = res["wobbling_modification"]
        # Frequency should be ~ 1440 keV with small positive shift
        self.assertGreater(w["wobbling_freq_modified_keV"], 1000.0)
        self.assertGreater(w["delta_wobbling_freq_keV"], 0.0)

    def test_135Pr_negative_beta4_shift(self):
        p = PRESETS["135Pr_triaxial_negative_beta4"]
        res = run_hexadecapole_wobbling_analysis(
            nucleus=p["nucleus"],
            beta2=p["beta2"],
            gamma_deg=p["gamma_deg"],
            beta4=p["beta4"],
            J_base=p["J_base_hbar2_per_MeV"],
            j_aligned=p["j_aligned_hbar"],
            spin_I=p["spin_I"]
        )
        w = res["wobbling_modification"]
        # Frequency should be ~ 1650 keV with negative shift
        self.assertGreater(w["wobbling_freq_modified_keV"], 1000.0)
        self.assertLess(w["delta_wobbling_freq_keV"], 0.0)

    def test_intermediate_axis_dominance_preserved(self):
        p = PRESETS["163Lu_TSD_positive_beta4"]
        moi = calculate_hexadecapole_modified_moi(p["beta2"], p["gamma_deg"], p["beta4"], p["J_base_hbar2_per_MeV"])
        m = moi["modified_MOI"]
        self.assertGreater(m["J_m"], m["J_s"])
        self.assertGreater(m["J_m"], m["J_l"])


if __name__ == "__main__":
    unittest.main()
