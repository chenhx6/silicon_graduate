#!/usr/bin/env python3
"""
Unit tests for in_beam_prompt_delayed_time_gating_random_subtractor.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_prompt_delayed_time_gating_random_subtractor import (
    PRESETS,
    calculate_window_width,
    perform_random_subtraction,
    perform_delayed_isomer_analysis,
    run_prompt_delayed_analysis
)


class TestPromptDelayedTimeGating(unittest.TestCase):

    def test_window_width_and_normalization(self):
        w1 = {"t_start": -4.0, "t_stop": 8.0}
        w2 = {"t_start": 25.0, "t_stop": 75.0}
        self.assertEqual(calculate_window_width(w1), 12.0)
        self.assertEqual(calculate_window_width(w2), 50.0)

    def test_134Ce_prompt_random_subtraction(self):
        p = PRESETS["in_beam_134Ce_prompt_random_subtraction"]
        res = run_prompt_delayed_analysis(
            peaks=p["peaks"],
            prompt_win=p["prompt_window_ns"],
            rand_win=p["random_window_ns"],
            nucleus=p["nucleus"]
        )
        pr = res["prompt_analysis"]
        peaks = pr["subtracted_peaks"]
        self.assertEqual(len(peaks), 3)
        # Peak 409 keV: 14200 - 0.24 * 6400 = 12664.0
        self.assertAlmostEqual(peaks[0]["net_true_counts"], 12664.0, places=1)
        self.assertGreater(peaks[0]["signal_to_random_ratio"], 5.0)
        self.assertGreater(peaks[0]["significance_Z"], 50.0)

    def test_181Ta_isomer_delayed_gating(self):
        p = PRESETS["181Ta_nanosecond_isomer_delayed_gating"]
        res = run_prompt_delayed_analysis(
            peaks=p["peaks"],
            prompt_win=p["prompt_window_ns"],
            rand_win=p["random_window_ns"],
            delayed_win=p["delayed_window_ns"],
            nucleus=p["nucleus"]
        )
        da = res["delayed_analysis"]
        dpeaks = da["delayed_peaks"]
        self.assertEqual(len(dpeaks), 3)
        # Peaks 133 keV and 482 keV should be identified as isomeric transitions
        self.assertTrue(dpeaks[0]["is_isomeric_transition"])
        self.assertTrue(dpeaks[1]["is_isomeric_transition"])
        # Prompt peak 346 keV should NOT be identified as isomeric
        self.assertFalse(dpeaks[2]["is_isomeric_transition"])

    def test_high_rate_random_dominated(self):
        p = PRESETS["high_rate_random_dominated_benchmark"]
        res = run_prompt_delayed_analysis(
            peaks=p["peaks"],
            prompt_win=p["prompt_window_ns"],
            rand_win=p["random_window_ns"],
            nucleus=p["nucleus"]
        )
        pr = res["prompt_analysis"]
        peaks = pr["subtracted_peaks"]
        # f_norm = 10 / 40 = 0.25
        # 511 keV: 25000 - 0.25 * 78000 = 5500.0
        self.assertAlmostEqual(peaks[0]["net_true_counts"], 5500.0, places=1)


if __name__ == "__main__":
    unittest.main()
