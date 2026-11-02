#!/usr/bin/env python3
"""
Unit tests for Spontaneous Fission Double-Humped Barrier Action
& Half-Life Simulator (Module 124).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from spontaneous_fission_wkb_action_calculator import (
    calculate_sf_hill_wheeler_transmission,
    calculate_double_hump_sf_half_life,
    calculate_fissility_and_swiatecki,
    run_spontaneous_fission_analysis,
    PRESETS
)


class TestSpontaneousFissionAction(unittest.TestCase):

    def test_hill_wheeler_penetration(self):
        # Sub-barrier
        P_sub, arg_sub = calculate_sf_hill_wheeler_transmission(barrier_height_MeV=6.0, barrier_hw_MeV=1.0, energy_MeV=1.0)
        self.assertLess(P_sub, 1e-10)
        self.assertGreater(arg_sub, 25.0)

        # Above-barrier
        P_above, arg_above = calculate_sf_hill_wheeler_transmission(barrier_height_MeV=4.0, barrier_hw_MeV=1.0, energy_MeV=6.0)
        self.assertGreaterEqual(P_above, 0.99)

    def test_double_hump_barrier_scaling(self):
        res_high = calculate_double_hump_sf_half_life(E_A_MeV=6.5, hw_A_MeV=1.0, E_B_MeV=6.0, hw_B_MeV=0.5)
        res_low = calculate_double_hump_sf_half_life(E_A_MeV=5.0, hw_A_MeV=1.0, E_B_MeV=4.5, hw_B_MeV=0.5)
        self.assertGreater(res_high["effective_action_S_eff"], res_low["effective_action_S_eff"])
        self.assertGreater(res_high["T_half_years"], res_low["T_half_years"])

    def test_fissility_systematics(self):
        fiss = calculate_fissility_and_swiatecki(Z_charge=92, A_mass=238, delta_U_MeV=2.2)
        self.assertAlmostEqual(fiss["Z2_over_A"], 35.56, places=1)
        self.assertGreater(fiss["fissility_parameter_x"], 0.70)
        self.assertLess(fiss["fissility_parameter_x"], 0.85)

    def test_presets_238u_and_252cf(self):
        p_u = PRESETS["238U_spontaneous_fission"]
        res_u = run_spontaneous_fission_analysis(
            p_u["nucleus"], p_u["Z_charge"], p_u["A_mass"],
            p_u["E_A_MeV"], p_u["hw_A_MeV"], p_u["E_B_MeV"], p_u["hw_B_MeV"],
            p_u["E_0_MeV"], p_u["delta_U_MeV"]
        )
        self.assertGreater(res_u["quantum_penetration"]["log10_T_half_years"], 10.0)

        p_cf = PRESETS["252Cf_spontaneous_fission"]
        res_cf = run_spontaneous_fission_analysis(
            p_cf["nucleus"], p_cf["Z_charge"], p_cf["A_mass"],
            p_cf["E_A_MeV"], p_cf["hw_A_MeV"], p_cf["E_B_MeV"], p_cf["hw_B_MeV"],
            p_cf["E_0_MeV"], p_cf["delta_U_MeV"]
        )
        self.assertLess(res_cf["quantum_penetration"]["log10_T_half_years"], 5.0)


if __name__ == "__main__":
    unittest.main()
