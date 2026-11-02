"""
Unit tests for Constant Fraction Discriminator (CFD) Walk Elimination & Fast Timing.

Benchmarked against:
  - 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第9章 §9.3 (时间测量与定时方法).
  - 汪晓莲等, 《粒子探测技术》, 中国科学技术大学出版社 (2009), 第8章 (电子学定时与脉冲成形).
  - D. A. Gedcke and W. J. McDonald, Nucl. Instrum. Methods 58, 253 (1968).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from constant_fraction_discriminator_fast_timing_calculator import (
    simulate_cfd_walk_elimination,
    calculate_fast_timing_resolution
)


class ConstantFractionDiscriminatorTests(unittest.TestCase):

    def test_cfd_zero_walk_elimination_across_dynamic_range(self):
        """CFD zero-crossing time must be strictly amplitude-independent (walk < 0.01 ps across 10:1 range)."""
        # Fast pulse: tr = 2.0 ns, f = 0.20, amplitudes from 0.5 V to 5.0 V
        res = simulate_cfd_walk_elimination(
            amplitudes_V=[0.5, 1.0, 2.0, 3.5, 5.0],
            rise_time_ns=2.0,
            fraction=0.20
        )
        self.assertAlmostEqual(res["delay_ns"], 1.60, places=2)
        self.assertLess(res["cfd_walk_ps"], 0.01)
        self.assertGreater(res["led_walk_ps"], 250.0) # LED has > 250 ps walk
        self.assertGreater(res["walk_reduction_factor"], 10000.0)

    def test_labr3_scintillator_fast_timing_resolution(self):
        """Verify sub-nanosecond timing resolution budget for LaBr3(Ce) detector."""
        # LaBr3 with 2500 photoelectrons, tau_decay = 16 ns, PMT TTS = 0.35 ns
        timing = calculate_fast_timing_resolution(
            scint_decay_time_ns=16.0,
            pmt_tts_fwhm_ns=0.35,
            N_photoelectrons=2500.0,
            noise_rms_mV=2.0,
            zero_crossing_slope_V_per_ns=1.2
        )
        self.assertAlmostEqual(timing["sigma_scint_ps"], 320.0, places=1)
        self.assertLess(timing["sigma_pmt_tts_ps"], 10.0)
        self.assertLess(timing["sigma_electronic_noise_ps"], 5.0)
        self.assertLess(timing["total_timing_resolution_FWHM_ps"], 800.0)

    def test_baf2_ultrafast_sub_200ps_resolution(self):
        """Verify BaF2 fast component achieves sub-200 ps resolution."""
        timing_baf2 = calculate_fast_timing_resolution(
            scint_decay_time_ns=0.8,
            pmt_tts_fwhm_ns=0.25,
            N_photoelectrons=1500.0,
            noise_rms_mV=1.5,
            zero_crossing_slope_V_per_ns=2.5
        )
        self.assertLess(timing_baf2["total_timing_resolution_FWHM_ps"], 100.0)

    def test_invalid_parameters_raised(self):
        """Non-positive rise time or invalid fraction must raise ValueError."""
        with self.assertRaises(ValueError):
            simulate_cfd_walk_elimination([1.0], rise_time_ns=-1.0)
        with self.assertRaises(ValueError):
            simulate_cfd_walk_elimination([1.0], fraction=1.5)
        with self.assertRaises(ValueError):
            calculate_fast_timing_resolution(10.0, 0.5, N_photoelectrons=-10.0)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = simulate_cfd_walk_elimination([0.5, 1.0, 2.0], rise_time_ns=2.0, fraction=0.20)
        timing = calculate_fast_timing_resolution(16.0, 0.35, 2500.0)
        payload = {"walk": res, "timing": timing}
        s = json.dumps(payload, allow_nan=False)
        self.assertIn("cfd_walk_ps", s)


if __name__ == "__main__":
    unittest.main()
