#!/usr/bin/env python3
"""
Unit tests for Digital Moving Window Deconvolution (MWD) & Baseline Restorer (BLR) (Module 126).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from digital_mwd_baseline_restorer_filter import (
    synthesize_hpge_trace,
    apply_moving_window_deconvolution,
    apply_moving_average,
    apply_adaptive_baseline_restorer,
    run_mwd_blr_analysis,
    PRESETS
)


class TestMWDBaselineRestorer(unittest.TestCase):

    def test_mwd_tail_cancellation(self):
        dt = 10.0
        tau_pre = 50000.0
        t, v = synthesize_hpge_trace(
            n_samples=1000, dt_ns=dt, pulse_starts_ns=[2000.0],
            amplitudes=[1000.0], tau_rise_ns=30.0, tau_pre_ns=tau_pre,
            noise_std=0.0, baseline_shift=0.0
        )
        M_win_samples = 200
        M_decay_samples = tau_pre / dt
        v_mwd = apply_moving_window_deconvolution(v, M_win_samples, M_decay_samples)
        self.assertAlmostEqual(v_mwd[250], 1000.0, delta=15.0)
        self.assertAlmostEqual(v_mwd[500], 0.0, delta=2.0)

    def test_moving_average_smoothing(self):
        np.random.seed(42)
        noisy = np.random.normal(0.0, 5.0, 500)
        smooth = apply_moving_average(noisy, L_samples=25)
        self.assertLess(np.std(smooth), np.std(noisy))

    def test_adaptive_baseline_tracking(self):
        v_sig = np.zeros(300) + 50.0
        v_clean, bl = apply_adaptive_baseline_restorer(v_sig, threshold=15.0)
        self.assertAlmostEqual(v_clean[-1], 0.0, delta=1.0)
        self.assertAlmostEqual(bl[-1], 50.0, delta=1.0)

    def test_run_mwd_blr_presets(self):
        p = PRESETS["close_doublet_pileup"]
        res = run_mwd_blr_analysis(
            sampling_dt_ns=p["sampling_dt_ns"],
            tau_pre_us=p["tau_pre_us"],
            tau_rise_ns=p["tau_rise_ns"],
            M_win_us=p["M_win_us"],
            L_smooth_us=p["L_smooth_us"],
            pulse_starts_us=p["pulse_starts_us"],
            true_energies_keV=p["true_energies_keV"],
            noise_std_keV=p["noise_std_keV"],
            baseline_drift_keV=p["baseline_drift_keV"]
        )
        self.assertGreater(res["resolution_summary"]["resolution_improvement_factor"], 10.0)
        self.assertEqual(len(res["peaks"]), 2)


if __name__ == "__main__":
    unittest.main()
