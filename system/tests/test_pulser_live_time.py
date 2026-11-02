#!/usr/bin/env python3
"""
Unit tests for in_beam_pulser_injection_live_time_corrector.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_pulser_injection_live_time_corrector import (
    PRESETS,
    calculate_pulser_live_time,
    correct_peaks,
    diagnose_hardware_clock_bias,
    run_pulser_live_time_analysis
)


class TestPulserLiveTime(unittest.TestCase):

    def test_pulser_live_time_calculation(self):
        lt_info = calculate_pulser_live_time(real_time_s=1000.0, pulser_freq_Hz=100.0, recorded_counts=80000)
        self.assertEqual(lt_info["pulses_injected"], 100000.0)
        self.assertEqual(lt_info["pulses_recorded"], 80000.0)
        self.assertAlmostEqual(lt_info["live_time_fraction"], 0.80, places=3)
        self.assertAlmostEqual(lt_info["dead_time_pct"], 20.0, places=2)
        self.assertGreater(lt_info["sigma_live_time"], 0.0)

    def test_in_beam_high_rate_clover_run(self):
        p = PRESETS["in_beam_high_rate_clover_130Ba"]
        res = run_pulser_live_time_analysis(
            experiment=p["experiment"],
            real_time_s=p["real_time_s"],
            pulser_freq_Hz=p["pulser_frequency_Hz"],
            recorded_counts=p["pulser_recorded_counts"],
            hardware_lt=p["hardware_clock_live_time"],
            physical_peaks=p["physical_peaks"]
        )
        lt = res["live_time_metrics"]
        hw = res["hardware_clock_comparison"]
        self.assertAlmostEqual(lt["live_time_fraction"], 0.774, places=2)
        # Unmonitored pileup loss should be ~ 8.1%
        self.assertAlmostEqual(hw["unmonitored_pileup_loss_pct"], 8.08, places=1)
        self.assertEqual(hw["hardware_clock_bias_severity"], "HIGH_ANALOG_PILEUP_LOSS (LTC invalid)")
        # Corrected area should be greater than measured area
        pk = res["corrected_peaks"][0]
        self.assertGreater(pk["true_area"], pk["measured_area"])
        self.assertAlmostEqual(pk["correction_multiplier"], 1.0 / 0.774, places=1)

    def test_low_rate_calibration(self):
        p = PRESETS["pure_low_rate_calibration"]
        res = run_pulser_live_time_analysis(
            experiment=p["experiment"],
            real_time_s=p["real_time_s"],
            pulser_freq_Hz=p["pulser_frequency_Hz"],
            recorded_counts=p["pulser_recorded_counts"],
            hardware_lt=p["hardware_clock_live_time"],
            physical_peaks=p["physical_peaks"]
        )
        lt = res["live_time_metrics"]
        self.assertGreater(lt["live_time_fraction"], 0.98)
        self.assertLess(lt["dead_time_pct"], 2.0)


if __name__ == "__main__":
    unittest.main()
