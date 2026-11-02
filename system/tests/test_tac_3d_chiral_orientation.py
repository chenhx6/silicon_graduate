"""
Unit tests for 3D TAC Chiral Orientation Energy Surface & Bifurcation Calculator.

Benchmarked against:
  - S. Frauendorf and J. Meng, Nucl. Phys. A 617, 131 (1997).
  - S. Frauendorf, Rev. Mod. Phys. 73, 463 (2001), Sec. VII.B.
  - J. Meng & Y. P. Wang, in Chirality and Wobbling in Atomic Nuclei (CRC 2025), Ch. 3.
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from tac_3d_chiral_orientation_energy_surface_calculator import (
    find_chiral_equilibrium_and_barrier,
    scan_chiral_spin_evolution
)


class TAC3DChiralOrientationTests(unittest.TestCase):

    def test_low_spin_planar_phase(self):
        """At low spin J <= 12 hbar, equilibrium is planar (phi ~ 0 deg, Jm ~ 0)."""
        res = find_chiral_equilibrium_and_barrier(J_tot=10.0, J_m=25.0, J_s=15.0, J_l=5.0)
        self.assertFalse(res["is_chiral_geometry"])
        self.assertEqual(res["chiral_phase"], "Planar Rotation")
        self.assertLess(res["phi_min_deg"], 5.0)
        self.assertAlmostEqual(res["chiral_barrier_keV"], 0.0, places=1)

    def test_high_spin_chiral_bifurcation(self):
        """At high spin J >= 16 hbar, spontaneous chiral symmetry breaking creates aplanar minimum."""
        res_16 = find_chiral_equilibrium_and_barrier(J_tot=16.0, J_m=25.0, J_s=15.0, J_l=5.0)
        self.assertTrue(res_16["is_chiral_geometry"])
        self.assertGreater(res_16["chiral_barrier_keV"], 5.0)

        res_18 = find_chiral_equilibrium_and_barrier(J_tot=18.0, J_m=25.0, J_s=15.0, J_l=5.0)
        self.assertTrue(res_18["is_chiral_geometry"])
        self.assertGreater(res_18["chiral_barrier_keV"], 100.0)
        self.assertGreater(res_18["aplanarity_volume_metric"], 0.40)
        # All three components are non-zero
        comps = res_18["angular_momentum_components"]
        self.assertGreater(comps["J_s_short_hbar"], 5.0)
        self.assertGreater(comps["J_m_intermediate_hbar"], 5.0)
        self.assertGreater(comps["J_l_long_hbar"], 5.0)

    def test_spin_evolution_trajectory(self):
        """Scan correctly detects bifurcation from planar to chiral."""
        spins = [8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]
        traj = scan_chiral_spin_evolution(spins, J_m=25.0, J_s=15.0, J_l=5.0)
        self.assertEqual(len(traj), 7)
        # First 4 are planar, last 3 are chiral
        self.assertFalse(traj[0]["is_chiral_geometry"])
        self.assertFalse(traj[3]["is_chiral_geometry"])
        self.assertTrue(traj[4]["is_chiral_geometry"])
        self.assertTrue(traj[5]["is_chiral_geometry"])
        self.assertTrue(traj[6]["is_chiral_geometry"])

    def test_invalid_parameters_raised(self):
        """J <= 0 or non-positive MOIs must raise ValueError."""
        with self.assertRaises(ValueError):
            find_chiral_equilibrium_and_barrier(J_tot=-5.0)
        with self.assertRaises(ValueError):
            find_chiral_equilibrium_and_barrier(J_tot=18.0, J_m=-10.0)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = find_chiral_equilibrium_and_barrier(J_tot=18.0)
        s = json.dumps(res, allow_nan=False)
        self.assertIn("chiral_barrier_keV", s)


if __name__ == "__main__":
    unittest.main()
