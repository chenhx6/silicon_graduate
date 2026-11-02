"""
Unit tests for High-j Triaxial Cranking Routhians & Signature Inversion.

Benchmarked against:
  - S. Frauendorf, in Chirality and Wobbling in Atomic Nuclei (CRC Press 2025), Ch. 2, Eq. (2.13).
  - S. Frauendorf and J. Meng, Nucl. Phys. A 617, 131 (1997).
  - R. Bengtsson and I. Ragnarsson, Nucl. Phys. A 436, 14 (1985).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from triaxial_cranking_single_j_routhian_diagram_calculator import (
    diagonalize_triaxial_cranked_high_j,
    scan_routhian_frequency_trajectory
)


class TriaxialCrankingRouthianTests(unittest.TestCase):

    def test_h11_2_triaxial_chiral_dimension_and_alignment(self):
        """Verify h11/2 (j=5.5) has 12 Routhians, and lowest state aligns strongly with x-axis (<jx> ~ 5.5)."""
        diag = diagonalize_triaxial_cranked_high_j(
            j_orbital=5.5, gamma_deg=-30.0, omega_MeV=0.20, kappa_MeV=3.0
        )
        self.assertEqual(len(diag["levels"]), 12)
        lowest = diag["levels"][0]
        # At gamma = -30 deg, alignment along x-axis (short s-axis in Frauendorf convention)
        self.assertAlmostEqual(lowest["alignment_jx_hbar"], 5.47, places=1)
        self.assertEqual(lowest["signature_alpha"], "-1/2")

    def test_signature_inversion_at_low_frequency(self):
        """In triaxial intruder orbital, signature splitting Delta_e' is negative at low frequencies."""
        diag = diagonalize_triaxial_cranked_high_j(
            j_orbital=5.5, gamma_deg=-30.0, omega_MeV=0.20, kappa_MeV=3.0
        )
        self.assertTrue(diag["is_signature_inverted"])
        self.assertLess(diag["lowest_signature_splitting_keV"], 0.0)

    def test_frequency_scan_trajectory(self):
        """Trajectory scan correctly tracks lowest Routhian sloping down with frequency."""
        traj = scan_routhian_frequency_trajectory(
            j_orbital=5.5, gamma_deg=-30.0, kappa_MeV=3.0, omega_max_MeV=0.30, omega_step_MeV=0.05
        )
        self.assertGreater(len(traj), 5)
        # Routhian e'(omega) must decrease monotonically as -omega*jx pulls it down
        e_vals = [pt["lowest_routhian_MeV"] for pt in traj]
        for i in range(len(e_vals) - 1):
            self.assertGreater(e_vals[i], e_vals[i+1])

    def test_invalid_parameters_raised(self):
        """Integer j or j <= 0.5 must raise ValueError."""
        with self.assertRaises(ValueError):
            diagonalize_triaxial_cranked_high_j(j_orbital=2.0) # integer
        with self.assertRaises(ValueError):
            diagonalize_triaxial_cranked_high_j(j_orbital=0.5) # j too small

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        diag = diagonalize_triaxial_cranked_high_j(j_orbital=5.5, gamma_deg=-30.0, omega_MeV=0.20)
        s = json.dumps(diag, allow_nan=False)
        self.assertIn("Routhian_e_MeV", s)


if __name__ == "__main__":
    unittest.main()
