"""
Unit tests for DSAM Doppler Attenuation F(tau) & Picosecond Lifetime Inverter.

Benchmarked against:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第15章 (核寿命的测量, 印刷 pp. 421–452).
  - P. J. Nolan and J. F. Sharpey-Schafer, Rep. Prog. Phys. 42, 1 (1979).
  - A. E. Blaugrund, Nucl. Phys. 88, 501 (1966).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from dsam_doppler_attenuation_lss_blaugrund_lifetime_calculator import (
    calculate_dsam_f_tau_value,
    invert_lifetime_from_f_tau,
    calculate_lss_stopping_constants,
    generate_f_tau_calibration_curve
)


class DSAMDopplerAttenuationLifetimeTests(unittest.TestCase):

    def test_dsam_f_tau_monotonic_decrease(self):
        """Attenuation factor F(tau) must decrease monotonically as lifetime tau increases."""
        taus = [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
        f_vals = [calculate_dsam_f_tau_value(t, alpha_stop_ps=0.85) for t in taus]
        for i in range(len(f_vals) - 1):
            self.assertGreater(f_vals[i], f_vals[i+1])
        # Asymptotic limits
        self.assertGreater(f_vals[0], 0.95) # Ultra-fast decay in flight
        self.assertLess(f_vals[-1], 0.25)  # Decays mostly at rest

    def test_lifetime_inversion_roundtrip(self):
        """Forward calculate F(tau_true), then invert: must recover tau_true exactly."""
        tau_true_ps = 0.450
        alpha_stop = 0.82
        f_true = calculate_dsam_f_tau_value(tau_true_ps, alpha_stop)

        inv = invert_lifetime_from_f_tau(F_exp=f_true, F_err=0.02, alpha_stop_ps=alpha_stop)
        self.assertAlmostEqual(inv["tau_ps"], tau_true_ps, places=3)
        self.assertAlmostEqual(inv["tau_fs"], tau_true_ps * 1000.0, places=1)
        self.assertLess(inv["tau_lower_ps"], tau_true_ps)
        self.assertGreater(inv["tau_upper_ps"], tau_true_ps)

    def test_134Ce_in_Au_benchmark(self):
        """Verify inversion of typical in-beam A~130 recoil in gold backing."""
        inv = invert_lifetime_from_f_tau(F_exp=0.52, F_err=0.03, alpha_stop_ps=0.82)
        self.assertAlmostEqual(inv["tau_ps"], 0.7487, places=2)
        self.assertAlmostEqual(inv["tau_fs"], 748.7, places=0)
        self.assertEqual(inv["lifetime_regime"], "Optimal DSAM Range (High sensitivity to stopping power)")

    def test_lss_stopping_constants(self):
        """Verify LSS reduced energy factor and electronic stopping constant ke."""
        # 134Ce (Z1=58, M1=134) in Au (Z2=79, M2=197)
        lss = calculate_lss_stopping_constants(Z_recoil=58, M_recoil=134.0, Z_backing=79, M_backing=197.0)
        self.assertAlmostEqual(lss["a_TF_Angstrom"], 0.0811, places=3)
        self.assertAlmostEqual(lss["lss_k_e"], 0.2103, places=3)

    def test_invalid_parameters_raised(self):
        """F_exp <= 0 or >= 1 must raise ValueError."""
        with self.assertRaises(ValueError):
            invert_lifetime_from_f_tau(F_exp=1.0)
        with self.assertRaises(ValueError):
            invert_lifetime_from_f_tau(F_exp=-0.1)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        inv = invert_lifetime_from_f_tau(F_exp=0.55, F_err=0.04, alpha_stop_ps=0.85)
        lss = calculate_lss_stopping_constants(Z_recoil=58, M_recoil=134.0, Z_backing=79, M_backing=197.0)
        curve = generate_f_tau_calibration_curve(alpha_stop_ps=0.85)
        payload = {"inv": inv, "lss": lss, "curve": curve}
        s = json.dumps(payload, allow_nan=False)
        self.assertIn("tau_ps", s)


if __name__ == "__main__":
    unittest.main()
