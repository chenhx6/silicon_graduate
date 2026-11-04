#!/usr/bin/env python3
"""Deterministic probability/count checks for the conditional BGO veto model."""

import json
import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_bgo_compton_suppression_pt_ratio_optimizer import (
    PRESETS,
    BGOComptonSuppressionOptimizer,
    format_text_report,
    run_compton_suppression_analysis,
)


class TestInBeamBGOComptonSuppression(unittest.TestCase):

    def test_zero_gate_is_exact_unsuppressed_baseline(self):
        model = BGOComptonSuppressionOptimizer(correlated_peak_rejection=0.1)
        result = model.evaluate_performance(0.0)
        for key in ("prompt_time_acceptance", "correlated_continuum_rejection",
                    "correlated_peak_rejection", "accidental_peak_loss_pct"):
            with self.subTest(key=key):
                self.assertEqual(result[key], 0.0)
        for key in ("random_survival", "peak_acceptance", "continuum_acceptance",
                    "total_acceptance", "suppression_factor_SF",
                    "singles_pt_gain_factor", "significance_gain",
                    "matrix_fom_enhancement", "matrix_peak_peak_count_acceptance"):
            with self.subTest(key=key):
                self.assertEqual(result[key], 1.0)
        self.assertEqual(result["pt_suppressed"], model.pt_unsupp)
        self.assertEqual(result["signal_counts"], 1000.0)
        self.assertEqual(result["background_counts"], 4000.0)
        self.assertEqual(result["significance_proxy"], 1000.0 / math.sqrt(5000.0))

    def test_gaussian_acceptance_uses_full_centered_gate_and_sigma(self):
        model = BGOComptonSuppressionOptimizer(prompt_sigma_ns=10.0)
        self.assertAlmostEqual(model.prompt_time_acceptance(20.0), 0.6826894921370859)
        self.assertAlmostEqual(model.prompt_time_acceptance(40.0), 0.9544997361036416)
        self.assertEqual(model.prompt_time_acceptance(1000.0), 1.0)

    def test_decay_energy_and_threshold_are_metadata_not_response_laws(self):
        baseline = BGOComptonSuppressionOptimizer().evaluate_performance(40.0)
        changed = BGOComptonSuppressionOptimizer(
            E_gamma_keV=511.0, bgo_scintillation_decay_ns=1000.0,
            bgo_energy_threshold_keV=400.0,
        ).evaluate_performance(40.0)
        self.assertEqual(baseline, changed)
        narrower = BGOComptonSuppressionOptimizer(prompt_sigma_ns=5.0)
        wider = BGOComptonSuppressionOptimizer(prompt_sigma_ns=50.0)
        self.assertGreater(narrower.prompt_time_acceptance(40.0),
                           wider.prompt_time_acceptance(40.0))

    def test_zero_random_rate_preserves_peaks_and_only_rejects_correlated_continuum(self):
        model = BGOComptonSuppressionOptimizer(bgo_singles_rate_kHz=0.0)
        result = model.evaluate_performance(1000.0)
        self.assertEqual(result["random_survival"], 1.0)
        self.assertEqual(result["accidental_peak_loss_pct"], 0.0)
        self.assertEqual(result["peak_acceptance"], 1.0)
        self.assertAlmostEqual(result["continuum_acceptance"], 0.2)
        self.assertAlmostEqual(result["suppression_factor_SF"], 5.0)
        self.assertAlmostEqual(result["pt_suppressed"], 0.23 / (0.23 + 0.77 * 0.2))

    def test_poisson_random_survival_applies_to_both_event_classes(self):
        common = dict(correlated_escape_rejection=0.7, correlated_peak_rejection=0.1)
        no_random = BGOComptonSuppressionOptimizer(
            bgo_singles_rate_kHz=0.0, **common).evaluate_performance(80.0)
        random = BGOComptonSuppressionOptimizer(
            bgo_singles_rate_kHz=1000.0, **common).evaluate_performance(80.0)
        q = math.exp(-0.08)
        for key in ("peak_acceptance", "continuum_acceptance", "signal_counts",
                    "background_counts", "normalized_peak_counts",
                    "normalized_continuum_counts", "total_acceptance"):
            with self.subTest(key=key):
                self.assertAlmostEqual(random[key], no_random[key] * q)
        self.assertEqual(random["pt_suppressed"], no_random["pt_suppressed"])
        self.assertEqual(random["suppression_factor_SF"], no_random["suppression_factor_SF"])
        self.assertAlmostEqual(random["significance_proxy"],
                               no_random["significance_proxy"] * math.sqrt(q))
        self.assertAlmostEqual(random["matrix_fom_enhancement"],
                               no_random["matrix_fom_enhancement"] * q**2)

    def test_rejection_and_survival_are_distinct_probabilities(self):
        model = BGOComptonSuppressionOptimizer(
            prompt_sigma_ns=10.0, bgo_singles_rate_kHz=1000.0,
            correlated_escape_rejection=0.6, correlated_peak_rejection=0.2,
        )
        result = model.evaluate_performance(20.0)
        timing = 0.6826894921370859
        q = math.exp(-0.02)
        self.assertAlmostEqual(result["correlated_continuum_rejection"], 0.6 * timing)
        self.assertAlmostEqual(result["correlated_peak_rejection"], 0.2 * timing)
        self.assertAlmostEqual(result["continuum_acceptance"], (1 - 0.6 * timing) * q)
        self.assertAlmostEqual(result["peak_acceptance"], (1 - 0.2 * timing) * q)
        self.assertAlmostEqual(result["normalized_peak_counts"]
                               + result["normalized_continuum_counts"],
                               result["total_acceptance"])
        self.assertAlmostEqual(result["pt_suppressed"],
                               result["normalized_peak_counts"] / result["total_acceptance"])

    def test_no_correlated_tags_cannot_improve_purity_or_counting_precision(self):
        model = BGOComptonSuppressionOptimizer(
            correlated_escape_rejection=0.0, correlated_peak_rejection=0.0)
        result = model.evaluate_performance(200.0)
        self.assertEqual(result["pt_suppressed"], model.pt_unsupp)
        self.assertEqual(result["suppression_factor_SF"], 1.0)
        self.assertLess(result["signal_counts"], model.signal_counts)
        self.assertLess(result["significance_gain"], 1.0)
        self.assertLess(result["matrix_fom_enhancement"], 1.0)

    def test_large_gate_has_no_artificial_survival_or_rejection_floor(self):
        model = BGOComptonSuppressionOptimizer(
            bgo_singles_rate_kHz=1000.0, correlated_escape_rejection=0.99)
        result = model.evaluate_performance(10000.0)
        self.assertEqual(result["prompt_time_acceptance"], 1.0)
        self.assertAlmostEqual(result["correlated_continuum_rejection"], 0.99)
        self.assertAlmostEqual(result["random_survival"], math.exp(-10.0))
        self.assertGreater(result["accidental_peak_loss_pct"], 99.99)
        self.assertLess(result["peak_acceptance"], 0.0001)

    def test_large_gate_random_underflow_keeps_limiting_pt_and_zero_counts(self):
        model = BGOComptonSuppressionOptimizer(bgo_singles_rate_kHz=1000.0)
        result = model.evaluate_performance(1e9)
        for key in ("random_survival", "signal_counts", "background_counts",
                    "significance_proxy", "matrix_fom_enhancement"):
            with self.subTest(key=key):
                self.assertEqual(result[key], 0.0)
        self.assertAlmostEqual(result["pt_suppressed"], 0.23 / (0.23 + 0.77 * 0.2))
        json.dumps(result, allow_nan=False)

    def test_perfect_correlated_rejection_has_explicit_undefined_ratios(self):
        continuum_only = BGOComptonSuppressionOptimizer(
            correlated_escape_rejection=1.0, bgo_singles_rate_kHz=0.0,
        ).evaluate_performance(1000.0)
        self.assertEqual(continuum_only["pt_suppressed"], 1.0)
        self.assertEqual(continuum_only["background_counts"], 0.0)
        self.assertIsNone(continuum_only["suppression_factor_SF"])
        self.assertIsNone(continuum_only["signal_to_background"])
        all_rejected = BGOComptonSuppressionOptimizer(
            correlated_escape_rejection=1.0, correlated_peak_rejection=1.0,
        ).evaluate_performance(1000.0)
        self.assertEqual(all_rejected["total_acceptance"], 0.0)
        self.assertEqual(all_rejected["significance_proxy"], 0.0)
        self.assertIsNone(all_rejected["pt_suppressed"])
        self.assertIsNone(all_rejected["singles_pt_gain_factor"])
        self.assertIsNone(all_rejected["matrix_peak_peak_fraction"])
        json.dumps(all_rejected, allow_nan=False)

    def test_roi_counting_objective_uses_supplied_signal_and_background(self):
        model = BGOComptonSuppressionOptimizer(
            signal_counts=40.0, background_counts=360.0, correlated_peak_rejection=0.1)
        result = model.evaluate_performance(80.0)
        signal = 40.0 * result["peak_acceptance"]
        background = 360.0 * result["continuum_acceptance"]
        expected = signal / math.sqrt(signal + background)
        self.assertAlmostEqual(result["signal_counts"], signal)
        self.assertAlmostEqual(result["background_counts"], background)
        self.assertAlmostEqual(result["significance_proxy"], expected)
        self.assertAlmostEqual(result["significance_gain"], expected / 2.0)
        self.assertEqual(result["objective_name"], "significance")
        self.assertEqual(result["objective_value"], result["significance_proxy"])
        self.assertAlmostEqual(result["signal_to_background"], signal / background)
        self.assertNotAlmostEqual(result["pt_suppressed"], signal / (signal + background))

    def test_roi_sb_is_independent_of_full_spectrum_pt(self):
        first = BGOComptonSuppressionOptimizer(pt_unsuppressed=0.1)
        second = BGOComptonSuppressionOptimizer(pt_unsuppressed=0.8)
        a, b = first.evaluate_performance(80.0), second.evaluate_performance(80.0)
        self.assertNotEqual(a["pt_suppressed"], b["pt_suppressed"])
        self.assertEqual(a["signal_counts"], b["signal_counts"])
        self.assertEqual(a["background_counts"], b["background_counts"])
        self.assertEqual(a["objective_value"], b["objective_value"])
        self.assertEqual(first.optimize_veto_window()[0], second.optimize_veto_window()[0])

    def test_background_free_roi_counts_and_precision_decrease_with_random_veto(self):
        model = BGOComptonSuppressionOptimizer(signal_counts=100.0, background_counts=0.0)
        result = model.evaluate_performance(100.0)
        self.assertIsNone(result["signal_to_background"])
        self.assertAlmostEqual(result["significance_proxy"], math.sqrt(result["signal_counts"]))
        self.assertLess(result["significance_proxy"], 10.0)
        self.assertEqual(model.optimize_veto_window()[0], 0.0)

    def test_matrix_compatibility_diagnostic_is_derived_from_independent_arm_counts(self):
        model = BGOComptonSuppressionOptimizer(
            pt_unsuppressed=0.25, correlated_peak_rejection=0.15)
        result = model.evaluate_performance(60.0)
        f = 0.25
        a = result["peak_acceptance"]
        c = result["continuum_acceptance"]
        pair_signal = (f * a)**2
        pair_background = 2 * f * (1-f) * a * c + ((1-f) * c)**2
        baseline_pair_signal = f**2
        baseline_pair_z_squared = baseline_pair_signal**2  # baseline total = 1
        pair_z_squared = pair_signal**2 / (pair_signal + pair_background)
        self.assertAlmostEqual(result["matrix_signal_counts_normalized"], pair_signal)
        self.assertAlmostEqual(result["matrix_background_counts_normalized"], pair_background)
        self.assertAlmostEqual(result["matrix_peak_peak_count_acceptance"], a**2)
        self.assertAlmostEqual(result["matrix_peak_peak_fraction"],
                               pair_signal / (pair_signal + pair_background))
        self.assertAlmostEqual(result["matrix_significance_gain_squared"],
                               pair_z_squared / baseline_pair_z_squared)
        self.assertEqual(result["matrix_fom_enhancement"],
                         result["matrix_significance_gain_squared"])
        # Squared P/T is pair purity under this assumption, not pair S/B.
        self.assertNotAlmostEqual(result["matrix_peak_peak_fraction"],
                                  pair_signal / pair_background)

    def test_signal_count_objective_finds_exact_lower_boundary(self):
        model = BGOComptonSuppressionOptimizer(objective="signal_counts")
        gate, result = model.optimize_veto_window(0.0, 250.0)
        self.assertEqual(gate, 0.0)
        self.assertEqual(result["objective_value"], 1000.0)
        self.assertEqual(model.optimize_veto_window(15.0, 250.0)[0], 15.0)

    def test_zero_random_rate_finds_exact_upper_boundary_before_prompt_saturation(self):
        model = BGOComptonSuppressionOptimizer(bgo_singles_rate_kHz=0.0)
        gate, result = model.optimize_veto_window(0.0, 40.0)
        self.assertEqual(gate, 40.0)
        self.assertGreater(result["objective_value"], model.evaluate_performance(0)["objective_value"])

    def test_flat_objective_and_equal_bounds_return_exact_smallest_allowed_gate(self):
        model = BGOComptonSuppressionOptimizer(
            bgo_singles_rate_kHz=0.0, correlated_escape_rejection=0.0)
        self.assertEqual(model.optimize_veto_window(15.0, 250.0)[0], 15.0)
        gate, result = model.optimize_veto_window(33.0, 33.0)
        self.assertEqual(gate, 33.0)
        self.assertEqual(result, model.evaluate_performance(33.0))

    def test_interior_optimum_matches_dense_independent_grid(self):
        model = BGOComptonSuppressionOptimizer(bgo_singles_rate_kHz=350.0)
        gate, result = model.optimize_veto_window()
        grid = [model.evaluate_performance(i / 4.0)["objective_value"] for i in range(1001)]
        self.assertGreater(gate, 0.0)
        self.assertLess(gate, 250.0)
        self.assertGreaterEqual(result["objective_value"] + 1e-12, max(grid))
        self.assertEqual(result["tau_veto_ns"], gate)

    def test_wide_search_interval_still_resolves_prompt_region(self):
        model = BGOComptonSuppressionOptimizer(bgo_singles_rate_kHz=350.0)
        narrow_gate, narrow_result = model.optimize_veto_window(0.0, 250.0)
        wide_gate, wide_result = model.optimize_veto_window(0.0, 1e10)
        self.assertAlmostEqual(wide_gate, narrow_gate, delta=0.001)
        self.assertAlmostEqual(wide_result["objective_value"], narrow_result["objective_value"])
        self.assertGreater(wide_result["objective_value"],
                           model.evaluate_performance(0.0)["objective_value"])

    def test_invalid_constructor_parameters_are_rejected(self):
        bad_parameters = {
            "E_gamma_keV": (0, -1, math.nan, math.inf, "bad", None),
            "pt_unsuppressed": (0, -0.1, 1.01, math.nan),
            "bgo_singles_rate_kHz": (-1, math.inf, math.nan, 1e308),
            "bgo_scintillation_decay_ns": (0, -1, math.nan),
            "bgo_energy_threshold_keV": (-1, math.inf, None),
            "prompt_sigma_ns": (0, -1, math.nan, math.inf),
            "correlated_escape_rejection": (-0.01, 1.01, math.nan),
            "correlated_peak_rejection": (-0.01, 1.01, math.inf),
            "signal_counts": (0, -1, math.nan),
            "background_counts": (-1, math.inf),
            "objective": ("matrix_fom", None),
            "response_provenance": ("", " ", None),
        }
        for name, values in bad_parameters.items():
            for value in values:
                with self.subTest(name=name, value=value):
                    with self.assertRaises(ValueError):
                        BGOComptonSuppressionOptimizer(**{name: value})
        with self.assertRaises(ValueError):
            BGOComptonSuppressionOptimizer(signal_counts=1e308, background_counts=1e308)

    def test_invalid_gate_widths_and_search_bounds_are_rejected(self):
        model = BGOComptonSuppressionOptimizer()
        for width in (-1, math.nan, math.inf, None, "bad"):
            for method in (model.evaluate_performance, model.prompt_time_acceptance,
                           model.random_survival, model.accidental_photopeak_loss,
                           model.compton_escape_rejection_efficiency):
                with self.subTest(method=method.__name__, width=width):
                    with self.assertRaises(ValueError):
                        method(width)
        for bounds in ((-1, 10), (10, 9), (0, math.inf), (math.nan, 10)):
            with self.subTest(bounds=bounds):
                with self.assertRaises(ValueError):
                    model.optimize_veto_window(*bounds)
        with self.assertRaises(ValueError):
            run_compton_suppression_analysis(eval_veto_windows_ns=[-1])

    def test_legacy_positional_analysis_api_and_explicit_metadata(self):
        output = run_compton_suppression_analysis(
            "Test setup", 850.0, 0.25, 350.0, 300.0, 70.0, [0.0, 40.0])
        self.assertEqual(output["spectrometer"], "Test setup")
        self.assertEqual(len(output["veto_window_evolution"]), 2)
        self.assertEqual(output["response_provenance"], "synthetic")
        self.assertEqual(output["objective_name"], "significance")
        self.assertIn("numerical meaning has changed", output["migration_note"])
        self.assertIn("SYNTHETIC", format_text_report(output))
        json.dumps(output, allow_nan=False)

    def test_caller_response_and_count_objective_are_forwarded(self):
        output = run_compton_suppression_analysis(
            prompt_sigma_ns=12.0, correlated_escape_rejection=0.55,
            correlated_peak_rejection=0.05, signal_counts=50.0, background_counts=25.0,
            objective="signal_counts", response_provenance="caller fixture, not calibrated",
            optimize_min_ns=10.0, optimize_max_ns=30.0, eval_veto_windows_ns=[24.0],
        )
        self.assertEqual(output["optimal_veto_window_ns"], 10.0)
        self.assertEqual(output["response_parameters"]["prompt_sigma_ns"], 12.0)
        self.assertEqual(output["response_parameters"]["correlated_escape_rejection"], 0.55)
        self.assertEqual(output["response_parameters"]["correlated_peak_rejection"], 0.05)
        self.assertEqual(output["response_provenance"], "caller fixture, not calibrated")
        self.assertEqual(output["baseline_signal_counts"], 50.0)
        self.assertEqual(output["baseline_background_counts"], 25.0)
        self.assertEqual(output["optimization_bounds_ns"], [10.0, 30.0])
        result = output["optimal_performance"]
        self.assertEqual(result["objective_value"], result["signal_counts"])
        self.assertAlmostEqual(output["veto_window_evolution"][0]["prompt_time_acceptance"],
                               0.6826894921370859)

    def test_legacy_presets_are_explicitly_synthetic(self):
        self.assertIn("gammasphere_bgo_standard_1332keV", PRESETS)
        for name, preset in PRESETS.items():
            with self.subTest(name=name):
                self.assertIn("synthetic", preset["description"].lower())
                self.assertIn("synthetic", preset["spectrometer"].lower())

    def test_report_handles_complete_correlated_rejection(self):
        output = run_compton_suppression_analysis(
            correlated_escape_rejection=1.0, correlated_peak_rejection=1.0,
            optimize_min_ns=1000.0, optimize_max_ns=1000.0,
            eval_veto_windows_ns=[1000.0],
        )
        self.assertIn("undefined", format_text_report(output))
        json.dumps(output, allow_nan=False)


if __name__ == "__main__":
    unittest.main()
