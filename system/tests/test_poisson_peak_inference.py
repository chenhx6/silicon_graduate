"""Scientific regression tests for the fixed-template Poisson peak example."""

import json
import math
from pathlib import Path
import random
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
import poisson_likelihood_peak_fitting_bias_calculator as peak


class PoissonPeakInferenceTests(unittest.TestCase):
    def test_integrated_bins_and_finite_window_area(self):
        narrow = peak.gaussian_peak_model([0.0], 100.0, 0.0, 0.01, 0.0)
        self.assertAlmostEqual(narrow[0], 100.0)
        window = peak.gaussian_peak_model([0.0], 100.0, 0.0, 1.0, 0.0)
        self.assertAlmostEqual(window[0], 100.0 * math.erf(0.5 / math.sqrt(2)))
        # Far-tail integration must not cancel to zero at only eight sigma.
        self.assertGreater(peak.gaussian_peak_model([8.5], 1, 0, 1, 0)[0], 0)

    def test_poisson_support_and_empty_bins(self):
        self.assertEqual(peak.compute_baker_cousins_poisson_deviance([0], [0]), 0)
        self.assertEqual(peak.compute_baker_cousins_poisson_deviance([0], [2]), 4)
        self.assertTrue(math.isinf(
            peak.compute_baker_cousins_poisson_deviance([1], [0])))
        self.assertAlmostEqual(
            peak.compute_baker_cousins_poisson_deviance([2], [3]),
            2 * (1 + 2 * math.log(2 / 3)))

    def test_invalid_data_are_rejected(self):
        for counts, means in [([], []), ([1, 2], [1]), ([-1], [1]),
                              ([0.5], [1]), ([math.nan], [1]),
                              ([1], [-1]), ([1], [math.inf])]:
            with self.subTest(counts=counts, means=means):
                with self.assertRaises(ValueError):
                    peak.compute_baker_cousins_poisson_deviance(counts, means)
        with self.assertRaises(ValueError):
            peak.infer_peak_area([0], [1], 0, 1, 1,
                                 data_kind="background-subtracted")

    def test_invalid_model_or_fit_is_rejected(self):
        for sigma, bg in [(0, 1), (-1, 1), (math.nan, 1), (1, -1)]:
            with self.subTest(sigma=sigma, bg=bg):
                with self.assertRaises(ValueError):
                    peak.fit_peak_area_1d([0], [1], 0, sigma, bg)
        for channels in ([], [0, 0], [0, 2, 1], [0, 1, 3], [0, math.inf]):
            with self.assertRaises(ValueError):
                peak.gaussian_peak_model(channels, 1, 0, 1, 1)
        with self.assertRaises(ValueError):
            peak.fit_peak_area_1d([0], [1], 0, 1, 1, "typo")
        with self.assertRaises(ValueError):
            peak.infer_peak_area([0], [1], 0, 1, 1, delta_deviance=0)
        with self.assertRaises(ValueError):
            peak.gaussian_peak_model([0], -1, 0, 1, 0)

    def test_boundary_has_zero_discovery_statistic(self):
        result = peak.infer_peak_area([0], [0], 0, 1, 2)
        self.assertEqual(result["fitted_area_counts"], 0)
        interval = result["profile_likelihood_interval"]
        self.assertEqual(interval["lower_counts"], 0)
        mass = math.erf(0.5 / math.sqrt(2))
        self.assertAlmostEqual(interval["upper_counts"], 0.5 / mass, places=7)
        self.assertEqual(result["local_test"]["q0"], 0)
        self.assertEqual(result["local_test"]["z_asymptotic_local"], 0)
        self.assertEqual(result["local_test"]["p_asymptotic_local"], 1)

    def test_one_bin_matches_analytic_likelihood_ratio(self):
        result = peak.infer_peak_area([0], [15], 0, 1, 5)
        mass = math.erf(0.5 / math.sqrt(2))
        self.assertAlmostEqual(result["fitted_area_counts"], 10 / mass, places=7)
        q0 = 2 * (15 * math.log(15 / 5) + 5 - 15)
        test = result["local_test"]
        self.assertAlmostEqual(test["q0"], q0, places=9)
        self.assertAlmostEqual(test["z_asymptotic_local"], math.sqrt(q0))
        self.assertAlmostEqual(
            test["p_asymptotic_local"], 0.5 * math.erfc(math.sqrt(q0 / 2)))
        # Endpoints solve delta deviance = 1 and are asymmetric.
        interval = result["profile_likelihood_interval"]
        for endpoint in (interval["lower_counts"], interval["upper_counts"]):
            means = peak.gaussian_peak_model([0], endpoint, 0, 1, 5)
            self.assertAlmostEqual(
                peak.compute_baker_cousins_poisson_deviance([15], means)
                - result["min_deviance_chi_lambda2"], 1, places=7)
        self.assertNotAlmostEqual(result["area_error_lower_counts"],
                                  result["area_error_upper_counts"], places=3)

    def test_large_area_and_uncertainty_have_no_fixed_scan_cap(self):
        result = peak.infer_peak_area([0], [1000000], 0, 1, 0)
        mass = math.erf(0.5 / math.sqrt(2))
        self.assertAlmostEqual(result["fitted_area_counts"], 1000000 / mass, places=5)
        self.assertGreater(result["area_error_upper_counts"], 200)

    def test_zero_background_is_singular_and_json_remains_valid(self):
        for area in (0, 100):
            result = peak.evaluate_peak_fitting_methods(area, 50, 2, 0, 42)
            poi = result["poisson_mle_baker_cousins"]
            self.assertIsNone(poi["local_test"]["z_asymptotic_local"])
            self.assertEqual(poi["local_test"]["calibration"],
                             "unavailable-zero-background-null")
            json.dumps(result, allow_nan=False)
            self.assertNotIn("Discovery!", peak.format_text_report(result))

    def test_zero_sampler_seed_and_single_realization_labels(self):
        random.seed(321)
        state = random.getstate()
        a = peak.evaluate_peak_fitting_methods(0, 50, 2, 0, 42)
        self.assertEqual(random.getstate(), state)
        self.assertEqual(a["simulation"]["observed_counts"], [0] * 100)
        self.assertIsNone(a["poisson_mle_baker_cousins"]["relative_error_percentage"])
        b = peak.evaluate_peak_fitting_methods(seed=123)
        self.assertEqual(b, peak.evaluate_peak_fitting_methods(seed=123))
        self.assertNotIn("is_unbiased", b["poisson_mle_baker_cousins"])
        self.assertNotIn("systematic_underestimation", b["neyman_least_squares"])
        report = peak.format_text_report(b)
        self.assertIn("Single-realization", report)
        self.assertIn("coverage", report)

    def test_zero_background_mle_is_total_counts_over_window_mass(self):
        channels, counts = [-1, 0, 1], [4, 8, 3]
        result = peak.infer_peak_area(channels, counts, 0, 1, 0)
        mass = sum(peak.gaussian_peak_model(channels, 1, 0, 1, 0))
        self.assertAlmostEqual(result["fitted_area_counts"], sum(counts) / mass)

    def test_finite_sample_boundary_bias_has_an_exact_counterexample(self):
        # At true A=0, b=1, E[max(0,N-1)] = P(N=0) = exp(-1).
        # Sum the discrete ensemble, rather than labelling a single fit "bias".
        mass = math.erf(0.5 / math.sqrt(2))
        mean_estimate = 0.0
        for n in range(30):
            fitted = peak.fit_peak_area_1d([0], [n], 0, 1, 1)[0]
            mean_estimate += fitted * math.exp(-1) / math.factorial(n)
        self.assertAlmostEqual(mean_estimate, math.exp(-1) / mass, places=9)
        self.assertGreater(mean_estimate, 0)

    def test_large_mean_sampler_does_not_underflow_or_saturate(self):
        result = peak.evaluate_peak_fitting_methods(1000000, 50, 2, 0, 42)
        self.assertGreater(sum(result["simulation"]["observed_counts"]), 900000)
        self.assertTrue(all(n >= 0 and isinstance(n, int)
                            for n in result["simulation"]["observed_counts"]))

    def test_numerically_unidentifiable_window_or_impossible_bin_is_rejected(self):
        with self.assertRaises(ValueError):
            peak.infer_peak_area([0], [0], 1e6, 1, 1)
        with self.assertRaises(ValueError):
            peak.infer_peak_area([0, 100], [1, 1], 0, 0.01, 0)

    def test_tiny_positive_background_keeps_score_numerically_defined(self):
        result = peak.infer_peak_area([0, 100], [1, 0], 0, 0.01, 1e-310)
        self.assertAlmostEqual(result["fitted_area_counts"], 1)
        self.assertTrue(math.isfinite(result["local_test"]["q0"]))

    def test_neyman_solution_matches_weighted_linear_least_squares(self):
        channels, counts = [-1, 0, 1], [0, 5, 2]
        template = peak.gaussian_peak_model(channels, 1, 0, 1, 0)
        expected = max(0, sum(p * (n - 1) / max(1, n)
                              for p, n in zip(template, counts))
                       / sum(p * p / max(1, n)
                             for p, n in zip(template, counts)))
        fitted, _, _ = peak.fit_peak_area_1d(channels, counts, 0, 1, 1, "neyman")
        self.assertAlmostEqual(fitted, expected)


if __name__ == "__main__":
    unittest.main()
