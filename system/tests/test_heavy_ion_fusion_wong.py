"""
Unit tests for Heavy-Ion Fusion Wong Barrier Penetration & Spin Distribution.

Benchmarked against:
  - 林承键, 《重离子核反应》, 科学出版社 (2017), 第6章 (近垒重离子熔合反应, 印刷 pp. 134–153).
  - C. Y. Wong, Phys. Rev. Lett. 31, 766 (1973).
  - C. A. Bertulani & P. Danielewicz, Introduction to Nuclear Reactions (2021), Ch. 5.
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from heavy_ion_fusion_spin_distribution_wong_calculator import (
    calculate_heavy_ion_fusion_wong
)


class HeavyIonFusionWongTests(unittest.TestCase):

    def test_wong_analytical_partial_wave_sum_convergence(self):
        """Wong analytical closed formula must agree with discrete partial wave sum within 0.1%."""
        # 16O + 122Sn at Elab = 80 MeV (Ecm = 70.72 MeV, VB0 ~ 50.56 MeV)
        res = calculate_heavy_ion_fusion_wong(Z_p=8, A_p=16, Z_t=50, A_t=122, E_lab_MeV=80.0)
        self.assertAlmostEqual(res["Wong_cross_section_mb"], 1030.0, places=0)
        self.assertAlmostEqual(res["partial_wave_sum_cross_section_mb"], 1030.2, places=0)
        self.assertGreater(res["wong_sum_agreement_pct"], 99.9)

    def test_sub_barrier_fusion_enhancement(self):
        """At Ecm < VB0, transmission T_l falls exponentially but remains non-zero."""
        # 16O + 122Sn barrier is ~ 50.56 MeV. Test at Elab = 55 MeV (Ecm ~ 48.6 MeV < VB0)
        res_sub = calculate_heavy_ion_fusion_wong(Z_p=8, A_p=16, Z_t=50, A_t=122, E_lab_MeV=55.0)
        self.assertLess(res_sub["E_cm_MeV"], res_sub["barrier_height_VB0_MeV"])
        self.assertGreater(res_sub["Wong_cross_section_mb"], 0.0)
        self.assertLess(res_sub["Wong_cross_section_mb"], 100.0) # Sub-barrier tunneling regime

    def test_rldm_fission_limit_evaporation_residue_division(self):
        """Partial waves above l_fiss must be partitioned into fusion-fission cross section."""
        # High energy: Elab = 130 MeV produces spins up to l ~ 65 hbar
        res_high = calculate_heavy_ion_fusion_wong(Z_p=8, A_p=16, Z_t=50, A_t=122, E_lab_MeV=130.0, l_fiss_hbar=50)
        self.assertGreater(res_high["fusion_fission_cross_section_mb"], 0.0)
        self.assertAlmostEqual(
            res_high["evaporation_residue_cross_section_mb"] + res_high["fusion_fission_cross_section_mb"],
            res_high["partial_wave_sum_cross_section_mb"],
            places=1
        )

    def test_xn_evaporation_planning_recommendations(self):
        """Higher neutron evaporation channels must require higher recommended beam energies."""
        res = calculate_heavy_ion_fusion_wong(Z_p=8, A_p=16, Z_t=50, A_t=122, E_lab_MeV=80.0)
        channels = res["xn_evaporation_planning"]
        self.assertEqual(len(channels), 5) # 2n, 3n, 4n, 5n, 6n
        for i in range(len(channels) - 1):
            self.assertLess(channels[i]["recommended_E_lab_MeV"], channels[i+1]["recommended_E_lab_MeV"])

    def test_invalid_parameters_raised(self):
        """Negative beam energies or zero nucleon numbers must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_heavy_ion_fusion_wong(Z_p=0, A_p=16, Z_t=50, A_t=122, E_lab_MeV=80.0)
        with self.assertRaises(ValueError):
            calculate_heavy_ion_fusion_wong(Z_p=8, A_p=16, Z_t=50, A_t=122, E_lab_MeV=-10.0)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = calculate_heavy_ion_fusion_wong(Z_p=8, A_p=16, Z_t=50, A_t=122, E_lab_MeV=80.0)
        s = json.dumps(res, allow_nan=False)
        self.assertIn("Wong_cross_section_mb", s)


if __name__ == "__main__":
    unittest.main()
