#!/usr/bin/env python3
"""
Unit tests for DCO Multipole Mixing Ratio Double-Root Profile Likelihood
& Polarization Statistical Arbitrator (Module 115).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from double_root_dco_polarization_statistical_arbitrator import (
    solve_dco_quadratic,
    evaluate_r_dco,
    evaluate_polarization,
    evaluate_alpha_k,
    calculate_weisskopf_estimates,
    analyze_double_roots,
    PRESETS
)


class TestDoubleRootArbitrator(unittest.TestCase):

    def test_solve_dco_quadratic(self):
        A = [1.0, 0.45, 0.90]
        B = [1.4, -0.70, 1.80]
        R_exp = 0.45
        sol = solve_dco_quadratic(A, B, R_exp)
        self.assertEqual(sol["status"], "two_real_roots")
        self.assertEqual(len(sol["roots"]), 2)
        # Verify both roots satisfy R_DCO(delta) == R_exp
        for r in sol["roots"]:
            r_calc = evaluate_r_dco(r, A, B)
            self.assertAlmostEqual(r_calc, R_exp, places=4)

    def test_polarization_arbitration(self):
        p = PRESETS["134Pr_chiral_intraband"]
        res = analyze_double_roots(
            A_coeffs=p["A_coeffs"],
            B_coeffs=p["B_coeffs"],
            R_exp=p["R_exp"],
            sigma_R=p["sigma_R"],
            P_coeffs=p["P_coeffs"],
            Q_coeffs=p["Q_coeffs"],
            P_exp=p["P_exp"],
            sigma_P=p["sigma_P"],
            alpha_K_M1=p["alpha_K_M1"],
            alpha_K_E2=p["alpha_K_E2"],
            alpha_exp=p["alpha_exp"],
            sigma_alpha=p["sigma_alpha"],
            tau_ps=p["tau_ps"],
            E_gamma_keV=p["E_gamma_keV"],
            A_mass=p["A_mass"]
        )
        arb = res["arbitration"]
        self.assertEqual(arb["status"], "resolved_by_3sigma_statistical_exclusion")
        self.assertEqual(arb["favored_root"], 1)
        self.assertGreater(arb["delta_chi2"], 9.0)
        self.assertGreater(arb["exclusion_confidence_percent"], 99.7)

    def test_weisskopf_rate_ceiling(self):
        # Lifetime tau = 0.01 ps for 300 keV transition in A=130
        # Small delta=0.05 will have huge T(M1), violating single-particle limit
        wk = calculate_weisskopf_estimates(A_mass=130, E_gamma_keV=300.0, tau_ps=0.01, delta=0.05)
        self.assertIsNotNone(wk)
        self.assertGreater(wk["B_M1_Wu"], 5.0)

    def test_profile_chi2_scan(self):
        p = PRESETS["136Nd_triaxial_crossover"]
        res = analyze_double_roots(
            A_coeffs=p["A_coeffs"],
            B_coeffs=p["B_coeffs"],
            R_exp=p["R_exp"],
            sigma_R=p["sigma_R"],
            P_coeffs=p["P_coeffs"],
            Q_coeffs=p["Q_coeffs"],
            P_exp=p["P_exp"],
            sigma_P=p["sigma_P"]
        )
        summary = res["profile_scan_summary"]
        self.assertIn("min_chi2_tot", summary)
        self.assertIn("theta_min_deg", summary)
        self.assertEqual(len(summary["local_profile_intervals"]), 2)
        for interval in summary["local_profile_intervals"]:
            self.assertIn("delta_min", interval)
            self.assertIn("delta_lower", interval)
            self.assertIn("delta_upper", interval)
        self.assertGreaterEqual(summary["theta_min_deg"], -90.0)
        self.assertLessEqual(summary["theta_min_deg"], 90.0)


if __name__ == "__main__":
    unittest.main()
