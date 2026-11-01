"""Boundary and numerical checks for the ideal dead-time models."""

import importlib.util
import math
from pathlib import Path
import json
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "system/scripts/analysis/detector_deadtime_pileup_correction_calculator.py"
SPEC = importlib.util.spec_from_file_location("deadtime", SCRIPT)
deadtime = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(deadtime)


class DeadtimeModelsTests(unittest.TestCase):
    def forward(self, **overrides):
        values = dict(true_rate=30000.0, tau_nonpar=1e-5, tau_par=1e-5,
                      tau_hybrid_p=5e-6, tau_hybrid_n=5e-6, peaking_time=4e-6)
        values.update(overrides)
        return deadtime.calculate_deadtime_models(**values)

    def test_old_regression_contract(self):
        result = self.forward()
        self.assertAlmostEqual(result["non_paralyzable"]["observed_rate_cps"],
                               30000 / 1.3)
        self.assertAlmostEqual(result["paralyzable"]["observed_rate_cps"],
                               30000 * math.exp(-0.3))
        inv = deadtime.invert_observed_rate(22000, 1e-5, 1e-5)
        self.assertGreater(inv["paralyzable_dual_root_inversion"]
                           ["dual_root_discrepancy_ratio"], 5)

    def test_zero_input_has_unit_acceptance_and_zero_loss(self):
        for times in ({}, dict(tau_nonpar=0, tau_par=0, tau_hybrid_p=0,
                              tau_hybrid_n=0, peaking_time=0)):
            result = self.forward(true_rate=0, **times)
            for key in ("non_paralyzable", "paralyzable", "hybrid"):
                self.assertEqual(result[key]["observed_rate_cps"], 0)
                self.assertEqual(result[key]["live_time_fraction"], 1)
                self.assertEqual(result[key]["fractional_loss"], 0)
            self.assertEqual(result["pileup_diagnostics"]["pileup_loss_fraction"], 0)

    def test_no_deadtime_is_identity(self):
        for rate in (0, 1e-100, 1, 1e10, 1e308):
            result = self.forward(true_rate=rate, tau_nonpar=0, tau_par=0,
                                  tau_hybrid_p=0, tau_hybrid_n=0, peaking_time=0)
            for key in ("non_paralyzable", "paralyzable", "hybrid"):
                self.assertEqual(result[key]["observed_rate_cps"], rate)
                self.assertEqual(result[key]["fractional_loss"], 0)
            self.assertFalse(result["paralyzable"]["is_in_saturated_regime"])
            self.assertIsNone(result["paralyzable"]["max_possible_rate_cps"])
            inv = deadtime.invert_observed_rate(rate, 0, 0)
            self.assertEqual(inv["non_paralyzable_inversion"]["true_rate_cps"], rate)
            roots = inv["paralyzable_dual_root_inversion"]
            self.assertEqual(roots["root1_unsaturated_cps"], rate)
            self.assertIsNone(roots["root2_paralyzed_cps"])

    def test_invalid_inputs_are_rejected(self):
        for name in ("true_rate", "tau_nonpar", "tau_par", "tau_hybrid_p",
                     "tau_hybrid_n", "peaking_time"):
            for value in (-1, math.nan, math.inf, -math.inf):
                with self.subTest(name=name, value=value), self.assertRaises(ValueError):
                    self.forward(**{name: value})
        for index in range(3):
            for value in (-1, math.nan, math.inf, -math.inf):
                args = [1, 1e-5, 1e-5]
                args[index] = value
                with self.subTest(index=index, value=value), self.assertRaises(ValueError):
                    deadtime.invert_observed_rate(*args)

    def test_lambert_domains_and_convergence(self):
        endpoint = -1 / math.e
        self.assertEqual(deadtime.lambert_w_eval(endpoint, 0), -1)
        self.assertEqual(deadtime.lambert_w_eval(endpoint, -1), -1)
        self.assertEqual(deadtime.lambert_w_eval(0, 0), 0)
        for x, branch in ((endpoint, 2), (0, -1), (0.1, -1),
                          (math.nextafter(endpoint, -math.inf), 0),
                          (math.nan, 0), (math.inf, 0), (-math.inf, 0)):
            with self.subTest(x=x, branch=branch), self.assertRaises(ValueError):
                deadtime.lambert_w_eval(x, branch)
        for kwargs in (dict(tol=0), dict(tol=math.nan), dict(max_iter=0),
                       dict(max_iter=1.5)):
            with self.assertRaises(ValueError):
                deadtime.lambert_w_eval(0.2, **kwargs)
        with self.assertRaises(RuntimeError):
            deadtime.lambert_w_eval(0.2, max_iter=1)

    def test_lambert_small_arguments_log_residual(self):
        for x in (-1e-20, -1e-100, -1e-300, -5e-324):
            for branch in (0, -1):
                value = deadtime.lambert_w_eval(x, branch)
                self.assertAlmostEqual(math.log(-value) + value, math.log(-x),
                                       delta=3e-11)
                if branch == 0:
                    self.assertLess(abs(value / x - 1), 3e-12)
                else:
                    self.assertLessEqual(value, -1)

    def test_lambert_positive_and_near_branch_point(self):
        for x in (1e-100, 0.1, 1, 10, 1e300):
            value = deadtime.lambert_w_eval(x)
            self.assertAlmostEqual(math.log(value) + value, math.log(x), delta=3e-11)
        # High-precision values for the exact binary64 argument next to -1/e.
        x = math.nextafter(-1 / math.e, 0)
        self.assertAlmostEqual(deadtime.lambert_w_eval(x, 0),
                               -0.9999999846957459, delta=2e-14)
        self.assertAlmostEqual(deadtime.lambert_w_eval(x, -1),
                               -1.0000000153042543, delta=2e-14)
        for distance in (1e-12, 1e-8, 1e-4):
            x = -1 / math.e + distance
            lower = deadtime.lambert_w_eval(x, 0)
            upper = deadtime.lambert_w_eval(x, -1)
            self.assertGreater(lower, -1)
            self.assertLess(upper, -1)
            self.assertAlmostEqual(lower * math.exp(lower), x, delta=2e-14)
            self.assertAlmostEqual(upper * math.exp(upper), x, delta=2e-14)

    def test_inverse_zero_peak_and_out_of_range(self):
        tau = 1e-5
        roots = deadtime.invert_observed_rate(0, tau, tau)["paralyzable_dual_root_inversion"]
        self.assertEqual(roots["root1_unsaturated_cps"], 0)
        self.assertIsNone(roots["root2_paralyzed_cps"])
        maximum = (1 / math.e) / tau
        roots = deadtime.invert_observed_rate(maximum, tau, tau)["paralyzable_dual_root_inversion"]
        self.assertAlmostEqual(roots["root1_unsaturated_cps"], 1 / tau)
        self.assertEqual(roots["root1_unsaturated_cps"], roots["root2_paralyzed_cps"])
        self.assertEqual(roots["dual_root_discrepancy_ratio"], 1)
        roots = deadtime.invert_observed_rate(math.nextafter(maximum, math.inf),
                                             tau, tau)["paralyzable_dual_root_inversion"]
        self.assertFalse(roots["is_physically_admissible"])
        self.assertIsNone(roots["root1_unsaturated_cps"])
        for rate in (1 / tau, 2 / tau):
            result = deadtime.invert_observed_rate(rate, tau, tau)
            self.assertFalse(result["non_paralyzable_inversion"]["is_physically_admissible"])
            self.assertIsNone(result["non_paralyzable_inversion"]["true_rate_cps"])
            self.assertEqual(result["non_paralyzable_inversion"]["inversion_status"],
                             "asymptotic-limit-exceeded")

    def test_roundtrip_both_branches(self):
        tau = 1e-5
        for exposure in (1e-12, 0.001, 0.3, 0.999, 1, 1.001, 3, 100, 700):
            rate = exposure / tau
            result = self.forward(true_rate=rate, tau_par=tau, tau_nonpar=tau)
            p_rate = result["paralyzable"]["observed_rate_cps"]
            roots = deadtime.invert_observed_rate(p_rate, tau, tau)["paralyzable_dual_root_inversion"]
            key = "root1_unsaturated_cps" if exposure <= 1 else "root2_paralyzed_cps"
            self.assertAlmostEqual(roots[key] / rate, 1, delta=3e-10)
            for key in ("root1_unsaturated_cps", "root2_paralyzed_cps"):
                root = roots[key]
                self.assertAlmostEqual((root * math.exp(-root * tau)) / p_rate,
                                       1, delta=3e-10)
            np_rate = result["non_paralyzable"]["observed_rate_cps"]
            inverse = deadtime.invert_observed_rate(np_rate, tau, tau)
            self.assertAlmostEqual(inverse["non_paralyzable_inversion"]["true_rate_cps"]
                                   / rate, 1, delta=3e-10)

    def test_tiny_loss_and_huge_exposure(self):
        result = self.forward(true_rate=1e-20)
        self.assertGreater(result["non_paralyzable"]["fractional_loss"], 0)
        self.assertGreater(result["paralyzable"]["fractional_loss"], 0)
        self.assertGreater(result["pileup_diagnostics"]["pileup_loss_fraction"], 0)
        result = self.forward(true_rate=1e308, tau_nonpar=1e308,
                              tau_par=1e308, tau_hybrid_p=0, tau_hybrid_n=1e308)
        self.assertGreater(result["non_paralyzable"]["observed_rate_cps"], 0)
        self.assertGreater(result["hybrid"]["observed_rate_cps"], 0)
        self.assertEqual(result["paralyzable"]["observed_rate_cps"], 0)

    def test_attenuation_preserves_representable_rate_after_exp_underflow(self):
        rate, tau = 1e308, 1e-305
        result = self.forward(true_rate=rate, tau_par=tau,
                              tau_hybrid_p=tau, tau_hybrid_n=0,
                              peaking_time=tau / 2)
        expected = math.exp(math.log(rate) - rate * tau)
        self.assertGreater(expected, 0)
        for key in ("paralyzable", "hybrid"):
            self.assertAlmostEqual(result[key]["observed_rate_cps"] / expected,
                                   1, delta=1e-13)
        self.assertAlmostEqual(result["pileup_diagnostics"]["clean_peak_rate_cps"]
                               / expected, 1, delta=1e-13)

    def test_inverse_preserves_positive_rate_if_dimensionless_product_underflows(self):
        rate, tau = 1e-300, 1e-100
        roots = deadtime.invert_observed_rate(rate, 0, tau)["paralyzable_dual_root_inversion"]
        self.assertEqual(roots["root1_unsaturated_cps"], rate)
        high = roots["root2_paralyzed_cps"]
        self.assertGreater(high * tau, 1)
        self.assertAlmostEqual(math.log(high) - high * tau, math.log(rate), delta=1e-10)

    def test_hybrid_limits_and_disclosure(self):
        for p, n, expected in ((0, 1e-5, "non_paralyzable"),
                               (1e-5, 0, "paralyzable")):
            result = self.forward(tau_hybrid_p=p, tau_hybrid_n=n)
            self.assertAlmostEqual(result["hybrid"]["observed_rate_cps"],
                                   result[expected]["observed_rate_cps"])
            self.assertIn("approx", result["hybrid"]["model_status"].lower())

    def test_text_report_degenerate_roots(self):
        for rate, tau in ((0, 0), (1, 0), (0, 1e-5), (1 / math.e / 1e-5, 1e-5)):
            text = deadtime.format_text_report(
                self.forward(true_rate=rate, tau_par=tau),
                deadtime.invert_observed_rate(rate, tau, tau))
            self.assertIn("approx", text.lower())
            self.assertNotIn("Wu Zhihua", text)
            self.assertNotIn("Full-Energy", text)

    def test_standalone_cli_validation_and_all_zero(self):
        for flags in ([], ["--json"]):
            result = subprocess.run([sys.executable, str(SCRIPT), "-n", "0", "-m", "0",
                                     "--tau-np", "0", "--tau-p", "0", "--tp", "0"] + flags,
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            if "--json" in flags:
                parsed = json.loads(result.stdout)
                self.assertIsNone(parsed["forward"]["paralyzable"]["max_possible_rate_cps"])
        result = subprocess.run([sys.executable, str(SCRIPT), "-n", "nan"],
                                capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Traceback", result.stderr)

    def test_strict_json_serialization_on_all_edge_cases(self):
        cases = [
            # Zero dead time edges (previously produced math.inf)
            (100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 100.0),
            # All zero
            (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
            # Over range nonparalyzable inversion
            (1000.0, 1e-4, 1e-4, 5e-5, 5e-5, 1e-5, 10000.0),
            # Paralyzable outside model range
            (1000.0, 1e-5, 1e-5, 5e-6, 5e-6, 1e-6, 50000.0),
            # Coalesced root at peak
            (100000.0, 1e-5, 1e-5, 5e-6, 5e-6, 1e-6, (1 / math.e) / 1e-5),
        ]
        for true_n, tau_np, tau_p, tau_hp, tau_hn, tp, obs_m in cases:
            fwd = deadtime.calculate_deadtime_models(
                true_rate=true_n, tau_nonpar=tau_np, tau_par=tau_p,
                tau_hybrid_p=tau_hp, tau_hybrid_n=tau_hn, peaking_time=tp)
            inv = deadtime.invert_observed_rate(
                observed_rate=obs_m, tau_nonpar=tau_np, tau_par=tau_p)
            payload = {"forward": fwd, "inversion": inv}
            encoded = json.dumps(payload, allow_nan=False)
            self.assertNotIn("NaN", encoded)
            self.assertNotIn("Infinity", encoded)
            decoded = json.loads(encoded)
            self.assertIsInstance(decoded, dict)

if __name__ == "__main__":
    unittest.main()
