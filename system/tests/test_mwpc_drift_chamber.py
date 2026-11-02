#!/usr/bin/env python3
"""
Unit tests for MWPC & Drift Chamber Field, Townsend Avalanche
& Drift Time Calibration Simulator (Module 122).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from mwpc_drift_chamber_field_avalanche_simulator import (
    calculate_electrostatic_field,
    calculate_townsend_gas_gain,
    calculate_drift_space_time_relation,
    run_mwpc_simulation,
    PRESETS
)


class TestMWPCDriftChamber(unittest.TestCase):

    def test_electrostatic_fields(self):
        fld = calculate_electrostatic_field(pitch_s_mm=2.0, gap_L_mm=5.0, wire_r0_um=10.0, voltage_V0=2600.0)
        self.assertGreater(fld["E_surface_V_cm"], 1e5)
        self.assertGreater(fld["E_drift_V_cm"], 1e3)
        self.assertLess(fld["E_drift_V_cm"], fld["E_surface_V_cm"])

    def test_townsend_gas_gain(self):
        fld = calculate_electrostatic_field(pitch_s_mm=2.0, gap_L_mm=5.0, wire_r0_um=10.0, voltage_V0=2600.0)
        ava = calculate_townsend_gas_gain(fld["q_factor_V"], wire_r0_um=10.0, pressure_Torr=760.0,
                                          townsend_A=14.0, townsend_B=180.0)
        self.assertGreater(ava["gas_gain_M"], 1e3)
        self.assertLess(ava["gas_gain_M"], 1e7)
        self.assertGreater(ava["avalanche_radius_rcrit_um"], 10.0)

    def test_drift_space_time(self):
        traj = calculate_drift_space_time_relation(gap_L_mm=10.0, drift_velocity_cm_us=5.0, diffusion_D_um2_ns=120.0, n_steps=10)
        self.assertEqual(len(traj), 10)
        # Drift time must increase monotonically
        t_vals = [pt["drift_time_ns"] for pt in traj]
        self.assertTrue(all(t_vals[i] < t_vals[i+1] for i in range(len(t_vals)-1)))

    def test_run_mwpc_preset(self):
        p = PRESETS["standard_mwpc_p10"]
        res = run_mwpc_simulation(
            pitch_s_mm=p["pitch_s_mm"],
            gap_L_mm=p["gap_L_mm"],
            wire_r0_um=p["wire_r0_um"],
            voltage_V0=p["voltage_V0"]
        )
        self.assertGreater(res["avalanche_gain"]["gas_gain_M"], 1e4)
        self.assertEqual(len(res["drift_trajectory"]), 20)


if __name__ == "__main__":
    unittest.main()
