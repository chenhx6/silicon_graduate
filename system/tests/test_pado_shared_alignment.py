#!/usr/bin/env python3
"""Deterministic tests for P-ADO Shared Alignment Null & Projectile Family Profile."""

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from pado_shared_alignment_projectile_family_analyzer import (
    Q_95_2D,
    ZOBEL83_ROWS,
    analyze_projectile_families,
    compute_alpha,
    find_optimal_shared_r,
    mahalanobis_squared,
    tensor_polynomials,
)


class TestPADOSharedAlignment(unittest.TestCase):
    def test_tensor_polynomials_normalization(self):
        """Verify that Yamazaki tensor polynomials are normalized to 1.0 at min |m|."""
        m_vals, t2, t4 = tensor_polynomials(6.5)
        self.assertEqual(len(m_vals), 14)
        self.assertEqual(m_vals[0], 6.5)
        self.assertEqual(m_vals[-1], -6.5)
        min_idx = [abs(mv) for mv in m_vals].index(0.5)
        self.assertAlmostEqual(t2[min_idx], 1.0, places=7)
        self.assertAlmostEqual(t4[min_idx], 1.0, places=7)

    def test_alpha_limits(self):
        """Test asymptotic limits of alpha_k: r -> 0 gives full alignment (1.0)."""
        a2_0, a4_0 = compute_alpha(6.5, 0.0)
        self.assertAlmostEqual(a2_0, 1.0, places=5)
        self.assertAlmostEqual(a4_0, 1.0, places=5)

        # High r -> random orientation gives vanishing alignment
        a2_inf, a4_inf = compute_alpha(6.5, 10.0)
        self.assertAlmostEqual(a2_inf, 0.0, delta=0.01)
        self.assertAlmostEqual(a4_inf, 0.0, delta=0.01)

    def test_mahalanobis_zero_distance(self):
        """Mahalanobis distance of identical vectors is 0."""
        d2 = mahalanobis_squared((0.8, 0.5), (0.8, 0.5), 0.03, 0.08, rho=0.2)
        self.assertAlmostEqual(d2, 0.0, places=7)

    def test_zobel83_all10_rows_rejected(self):
        """Cross-projectile null must be rejected (tau_req > 1.0) on Zobel 1983 Table 1."""
        res = find_optimal_shared_r(ZOBEL83_ROWS, j=6.5, rho=0.0)
        self.assertFalse(res["passes_shared_null_at_tau1"])
        self.assertGreater(res["tau_required"], 2.0)
        self.assertGreater(res["min_max_mahalanobis_d2"], Q_95_2D)

    def test_zobel83_12c_family_accepted(self):
        """12C heavy-ion family must pass the shared null (tau_req < 1.0) at rho=0."""
        c12_rows = [r for r in ZOBEL83_ROWS if r["beam"] == "12C"]
        res = find_optimal_shared_r(c12_rows, j=6.5, rho=0.0)
        self.assertTrue(res["passes_shared_null_at_tau1"])
        self.assertLess(res["tau_required"], 1.0)
        self.assertLess(res["min_max_mahalanobis_d2"], Q_95_2D)
        self.assertAlmostEqual(res["optimal_r_sigma_over_j"], 0.2824, delta=0.005)

    def test_zobel83_alpha_family_rejected(self):
        """Alpha light-ion family must fail the shared null (tau_req > 1.0) at rho=0."""
        alpha_rows = [r for r in ZOBEL83_ROWS if r["beam"] == "alpha"]
        res = find_optimal_shared_r(alpha_rows, j=6.5, rho=0.0)
        self.assertFalse(res["passes_shared_null_at_tau1"])
        self.assertGreater(res["tau_required"], 2.0)

    def test_projectile_family_report_structure(self):
        """Check comprehensive structure and conclusions."""
        report = analyze_projectile_families(ZOBEL83_ROWS, j=6.5, rho=0.0)
        self.assertEqual(report["conclusion"]["cross_projectile_null"], "REJECTED")
        self.assertEqual(report["conclusion"]["alpha_family_null"], "REJECTED")
        self.assertEqual(report["conclusion"]["12C_family_null"], "ACCEPTED")


if __name__ == "__main__":
    unittest.main()
