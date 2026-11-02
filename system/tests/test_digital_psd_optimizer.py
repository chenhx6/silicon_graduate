#!/usr/bin/env python3
"""
Unit tests for Digital Pulse Shape Discrimination (PSD), CCM Gate Optimization
& Neutron/Gamma FOM Engine (Module 119).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from digital_psd_charge_comparison_optimizer import (
    synthesize_scintillation_pulse,
    compute_ccm_psd,
    optimize_gate_widths,
    evaluate_fom_energy_dependence,
    run_psd_analysis,
    PRESETS
)


class TestDigitalPSDOptimizer(unittest.TestCase):

    def test_pulse_synthesis(self):
        t = np.arange(0.0, 100.0, 0.5)
        p = synthesize_scintillation_pulse(t, tau_rise=1.5, tau_fast=3.2, tau_slow=270.0, f_slow=0.20)
        self.assertEqual(len(p), len(t))
        self.assertAlmostEqual(p[0], 0.0, places=4)
        self.assertGreater(np.max(p), 0.0)

    def test_ccm_psd(self):
        t = np.arange(0.0, 300.0, 0.5)
        p = synthesize_scintillation_pulse(t, tau_rise=1.5, tau_fast=3.2, tau_slow=270.0, f_slow=0.20)
        res = compute_ccm_psd(p, dt_ns=0.5, t_short_ns=20.0, t_long_ns=250.0)
        self.assertGreater(res["Q_long"], res["Q_short"])
        self.assertGreater(res["PSD"], 0.0)
        self.assertLess(res["PSD"], 1.0)

    def test_gate_optimization(self):
        opt = optimize_gate_widths(
            tau_rise_ns=1.5, tau_fast_ns=3.2, tau_slow_ns=270.0,
            f_slow_g=0.12, f_slow_n=0.32, dt_ns=0.5, t_long_ns=300.0
        )
        self.assertGreater(opt["optimal_T_short_ns"], 5.0)
        self.assertLess(opt["optimal_T_short_ns"], 40.0)
        self.assertGreater(opt["max_delta_PSD"], 0.03)
        self.assertGreater(opt["optimal_PSD_neutron"], opt["optimal_PSD_gamma"])

    def test_fom_energy_dependence(self):
        energies = [100.0, 300.0, 500.0, 1000.0]
        fom_list = evaluate_fom_energy_dependence(base_energy_keVee=500.0, base_fom=1.45, energy_list_keVee=energies)
        self.assertEqual(len(fom_list), 4)
        # Higher energy should have higher FOM
        self.assertGreater(fom_list[-1]["FOM"], fom_list[0]["FOM"])
        self.assertEqual(fom_list[2]["FOM"], 1.45)

    def test_run_psd_analysis_preset(self):
        p = PRESETS["Stilbene_crystal_psd"]
        res = run_psd_analysis(
            scintillator=p["scintillator"],
            tau_rise_ns=p["tau_rise_ns"],
            tau_fast_ns=p["tau_fast_ns"],
            tau_slow_ns=p["tau_slow_ns"],
            f_slow_g=p["f_slow_gamma"],
            f_slow_n=p["f_slow_neutron"],
            T_long_ns=p["T_long_ns"],
            base_fom=p["base_fom"]
        )
        self.assertGreater(res["optimal_psd_separation"]["max_delta_PSD"], 0.10)


if __name__ == "__main__":
    unittest.main()
