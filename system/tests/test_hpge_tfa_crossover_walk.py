#!/usr/bin/env python3
"""
Unit tests for in_beam_hpge_tfa_crossover_walk_jitter_optimizer.py (Module 156).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_hpge_tfa_crossover_walk_jitter_optimizer import (
    PRESETS,
    HPGeTFACrossoverOptimizer
)

class TestHPGeTFACrossover(unittest.TestCase):

    def test_coaxial_hpge_optimization(self):
        p = PRESETS["coaxial_hpge_in_beam_70pct"]
        opt = HPGeTFACrossoverOptimizer(
            t_rise_mean_ns=p["t_rise_mean_ns"],
            t_rise_sigma_ns=p["t_rise_sigma_ns"],
            preamp_decay_us=p["preamp_decay_us"],
            capacitance_pF=p["capacitance_pF"],
            noise_series_e_n=p["noise_series_e_n"],
            noise_parallel_i_n=p["noise_parallel_i_n"]
        )
        res = opt.optimize_shaping_constants(511.0)
        # Optimal FWHM must be better than Wu Zhihua long shaping baseline
        self.assertLess(res["optimal"]["total_fwhm_ns"], res["wu_zhihua_comparison"]["total_fwhm_ns"])
        # Improvement percentage must be positive
        self.assertGreater(res["optimization_improvement_pct"], 0.0)
        # Check crossover t0 physical validity (> 2 * tau_diff)
        self.assertGreater(res["optimal"]["t0_crossover_ns"], 2.0 * res["optimal"]["tau_diff_ns"])

    def test_planar_fast_timing_regime(self):
        p = PRESETS["planar_hpge_low_energy"]
        opt = HPGeTFACrossoverOptimizer(
            t_rise_mean_ns=p["t_rise_mean_ns"],
            t_rise_sigma_ns=p["t_rise_sigma_ns"],
            capacitance_pF=p["capacitance_pF"]
        )
        res = opt.optimize_shaping_constants(122.0)
        # Planar detector with fast rise time (45 ns) should achieve sub-5 ns FWHM
        self.assertLess(res["optimal"]["total_fwhm_ns"], 5.0)

    def test_energy_scaling_monotonicity(self):
        p = PRESETS["clover_hpge_leaf_segment"]
        opt = HPGeTFACrossoverOptimizer(
            t_rise_mean_ns=p["t_rise_mean_ns"],
            t_rise_sigma_ns=p["t_rise_sigma_ns"]
        )
        energies = [100.0, 300.0, 1000.0]
        curve = opt.generate_energy_walk_curve(50.0, 150.0, energies)
        # Higher energy should have lower or equal timing jitter
        self.assertGreater(curve[0]["jitter_sigma_ns"], curve[1]["jitter_sigma_ns"])
        self.assertGreater(curve[1]["jitter_sigma_ns"], curve[2]["jitter_sigma_ns"])

if __name__ == "__main__":
    unittest.main()
