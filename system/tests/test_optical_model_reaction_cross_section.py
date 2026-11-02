"""
Unit tests for Nuclear Optical Model Potential (OMP) Reaction Cross Section Calculator.

Benchmarked against:
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions (2021), Ch. 3.
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第9章 §9.3 (光学模型).
  - 林承键, 《重离子核反应》, 科学出版社 (2017), 第2章.
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from optical_model_potential_reaction_cross_section_calculator import (
    calculate_optical_model_reaction_cross_section
)


class OpticalModelReactionCrossSectionTests(unittest.TestCase):

    def test_40MeV_p_58Ni_benchmark(self):
        """Verify 40 MeV p + 58Ni reaction cross section ~ 1090 mb."""
        omp = calculate_optical_model_reaction_cross_section(
            Z_p=1, A_p=1, Z_t=28, A_t=58, E_lab_MeV=40.0,
            V0_MeV=45.0, W0_volume_MeV=10.0, Ws_surface_MeV=3.0
        )
        self.assertAlmostEqual(omp["total_reaction_cross_section_sigma_R_mb"], 1093.9, places=0)
        self.assertAlmostEqual(omp["geometric_scale_mb"], 946.4, places=0)
        self.assertGreater(omp["nuclear_opacity_ratio"], 1.0)
        self.assertEqual(len(omp["transmission_profile"]), 35)

    def test_transmission_t_b_monotonic_decrease(self):
        """Transmission probability T(b) must decrease monotonically from b=0 out to b > R."""
        omp = calculate_optical_model_reaction_cross_section(
            Z_p=1, A_p=1, Z_t=28, A_t=58, E_lab_MeV=40.0
        )
        prof = omp["transmission_profile"]
        # Central collisions have high absorption (T ~ 0.98)
        self.assertGreater(prof[0]["transmission_T_b"], 0.95)
        # Peripheral collisions outside R have low absorption
        self.assertLess(prof[-1]["transmission_T_b"], 0.01)

    def test_heavy_ion_optical_model_scale(self):
        """Heavy ion 16O + 208Pb at 90 MeV produces reaction cross section."""
        omp_hi = calculate_optical_model_reaction_cross_section(
            Z_p=8, A_p=16, Z_t=82, A_t=208, E_lab_MeV=90.0,
            V0_MeV=50.0, W0_volume_MeV=15.0, Ws_surface_MeV=0.0, b_max_fm=18.0
        )
        self.assertGreater(omp_hi["total_reaction_cross_section_sigma_R_mb"], 500.0)
        self.assertGreater(omp_hi["target_radius_R_fm"], 7.0)

    def test_invalid_parameters_raised(self):
        """Negative beam energies or non-positive mass numbers must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_optical_model_reaction_cross_section(1, 1, 28, 58, E_lab_MeV=-10.0)
        with self.assertRaises(ValueError):
            calculate_optical_model_reaction_cross_section(1, 0, 28, 58, E_lab_MeV=40.0)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        omp = calculate_optical_model_reaction_cross_section(1, 1, 28, 58, 40.0)
        s = json.dumps(omp, allow_nan=False)
        self.assertIn("total_reaction_cross_section_sigma_R_mb", s)


if __name__ == "__main__":
    unittest.main()
