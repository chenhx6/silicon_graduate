#!/usr/bin/env python3
"""
Unit tests for in_beam_array_coincidence_efficiency_angular_matrix_inverter.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_array_coincidence_efficiency_angular_matrix_inverter import (
    PRESETS,
    calculate_mutual_pair_angle,
    evaluate_directional_correlation_weight,
    calculate_array_coincidence_efficiency,
    run_coincidence_matrix_analysis
)


class TestArrayCoincidenceEfficiency(unittest.TestCase):

    def test_pair_angle_geometry(self):
        d1 = {"theta_deg": 90.0, "phi_deg": 0.0}
        d2 = {"theta_deg": 90.0, "phi_deg": 180.0}
        th_rad, cos_th = calculate_mutual_pair_angle(d1, d2)
        self.assertAlmostEqual(cos_th, -1.0, places=4)
        self.assertAlmostEqual(th_rad, 3.14159, places=3)

        d3 = {"theta_deg": 90.0, "phi_deg": 90.0}
        th_rad2, cos_th2 = calculate_mutual_pair_angle(d1, d3)
        self.assertAlmostEqual(cos_th2, 0.0, places=4)

    def test_isotropic_reference_baseline(self):
        p = PRESETS["isotropic_unpolarized_reference"]
        res = run_coincidence_matrix_analysis(
            array_name=p["array_name"],
            E1=p["E1_keV"], E2=p["E2_keV"],
            A2=p["A2_coef"], A4=p["A4_coef"],
            Q2=p["Q2_factor"], Q4=p["Q4_factor"],
            detectors=p["detector_rings"]
        )
        cr = res["coincidence_results"]
        # In isotropic case, F_geom must be exactly 1.0000
        self.assertAlmostEqual(cr["geometric_modulation_factor_F"], 1.0000, places=4)
        self.assertAlmostEqual(cr["angular_correlation_bias_pct"], 0.0, places=3)

    def test_12_clover_60Co_cascade(self):
        p = PRESETS["12_clover_array_60Co_cascade"]
        res = run_coincidence_matrix_analysis(
            array_name=p["array_name"],
            E1=p["E1_keV"], E2=p["E2_keV"],
            A2=p["A2_coef"], A4=p["A4_coef"],
            Q2=p["Q2_factor"], Q4=p["Q4_factor"],
            detectors=p["detector_rings"]
        )
        cr = res["coincidence_results"]
        self.assertEqual(cr["num_detectors"], 12)
        self.assertEqual(cr["num_detector_pairs"], 132)
        self.assertGreater(cr["true_coincidence_efficiency"], 1e-4)
        self.assertNotEqual(cr["geometric_modulation_factor_F"], 1.000)


if __name__ == "__main__":
    unittest.main()
