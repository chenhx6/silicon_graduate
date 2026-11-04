"""Tests for the finite-spin BM-II asymmetric-rotor matrix."""

import math
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from bm2_asymmetric_rotor_matrix_diagonalizer import (
    compare_bm_high_spin_with_finite_spin,
    diagonalize_bm_asymmetric_rotor,
)


class BM2AsymmetricRotorMatrixTests(unittest.TestCase):
    def test_trace_and_dimension(self):
        result = diagonalize_bm_asymmetric_rotor(4.0, 8.0, 12.0, 30.0)
        self.assertEqual(result["dimension"], 9)
        self.assertAlmostEqual(result["trace_residual"], 0.0, places=10)

    def test_axial_limit_has_expected_k_degeneracy(self):
        result = diagonalize_bm_asymmetric_rotor(2.0, 10.0, 10.0 + 1.0e-8, 30.0)
        # E(K=0)=A_perp I(I+1), E(|K|=1)=A_perp[I(I+1)-1]+A3,
        # E(|K|=2)=A_perp[I(I+1)-4]+4*A3.
        expected = sorted([
            10.0 * 6.0,
            10.0 * 5.0 + 30.0,
            10.0 * 5.0 + 30.0,
            10.0 * 2.0 + 120.0,
            10.0 * 2.0 + 120.0,
        ])
        for observed, target in zip(result["energies"], expected):
            self.assertAlmostEqual(observed, target, places=5)

    def test_invalid_axis_order_is_rejected(self):
        with self.assertRaises(ValueError):
            diagonalize_bm_asymmetric_rotor(4.0, 12.0, 8.0, 30.0)

    def test_high_spin_pair_centroids_approach_harmonic_benchmark(self):
        result = compare_bm_high_spin_with_finite_spin(
            40.0, 8.0, 12.0, 30.0, n_max=1
        )
        self.assertEqual(len(result["trajectories"]), 2)
        self.assertLess(
            abs(result["trajectories"][0]["relative_to_hbar_omega"]),
            0.01,
        )
        self.assertLess(
            result["trajectories"][0]["exact_pair_splitting"],
            1.0e-6,
        )

    def test_comparison_rejects_too_many_trajectory_pairs(self):
        with self.assertRaises(ValueError):
            compare_bm_high_spin_with_finite_spin(
                1.0, 8.0, 12.0, 30.0, n_max=2
            )


if __name__ == "__main__":
    unittest.main()
