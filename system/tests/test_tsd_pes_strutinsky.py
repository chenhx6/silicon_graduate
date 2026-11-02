#!/usr/bin/env python3
"""
Unit tests for triaxial_superdeformed_pes_strutinsky_engine.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from triaxial_superdeformed_pes_strutinsky_engine import (
    PRESETS,
    calculate_ldm_energy_surface,
    calculate_rotational_energy_surface,
    calculate_shell_correction_surface,
    find_pes_minima_and_saddle,
    run_pes_strutinsky_analysis
)


class TestTSDPESStrutinsky(unittest.TestCase):

    def test_163Lu_tsd_well_formation_at_high_spin(self):
        p = PRESETS["163Lu_TSD_potential_energy_surface"]
        res = run_pes_strutinsky_analysis(
            Z=p["Z"], A=p["A"], spin_I=p["spin_I"], beta4=p["beta4"],
            shell_amp=p["shell_amp_MeV"], tsd_shell_amp=p["tsd_shell_amp_MeV"],
            beta2_grid_params=p["beta2_grid"], gamma_grid_params=p["gamma_grid"],
            nucleus=p["nucleus"]
        )
        self.assertTrue(res["has_secondary_tsd_well"])
        tsd = res["superdeformed_min"]
        nd = res["normal_deformed_min"]
        self.assertGreater(tsd["beta2"], 0.35)
        self.assertLess(tsd["beta2"], 0.45)
        self.assertGreater(res["tsd_barrier_height_MeV"], 1.0)
        self.assertLess(nd["beta2"], 0.25)

    def test_208Pb_spherical_doubly_magic(self):
        p = PRESETS["208Pb_spherical_doubly_magic"]
        res = run_pes_strutinsky_analysis(
            Z=p["Z"], A=p["A"], spin_I=p["spin_I"], beta4=p["beta4"],
            shell_amp=p["shell_amp_MeV"], tsd_shell_amp=p["tsd_shell_amp_MeV"],
            beta2_grid_params=p["beta2_grid"], gamma_grid_params=p["gamma_grid"],
            nucleus=p["nucleus"]
        )
        self.assertFalse(res["has_secondary_tsd_well"])
        nd = res["normal_deformed_min"]
        self.assertLessEqual(nd["beta2"], 0.10)

    def test_rotational_energy_scaling(self):
        import numpy as np
        b_arr = np.array([0.15, 0.40])
        g_arr = np.array([20.0])
        rot_zero = calculate_rotational_energy_surface(163, 0.0, b_arr, g_arr)
        self.assertEqual(rot_zero[0, 0], 0.0)
        rot_high = calculate_rotational_energy_surface(163, 35.5, b_arr, g_arr)
        # Rotational energy at large deformation (beta2=0.40) must be lower than at beta2=0.15
        self.assertLess(rot_high[1, 0], rot_high[0, 0])


if __name__ == "__main__":
    unittest.main()
