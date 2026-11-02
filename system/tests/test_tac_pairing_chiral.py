#!/usr/bin/env python3
"""
Unit tests for Self-Consistent 3D TAC with Pairing Gap Equation
& Chiral Restoration Phase Transition Simulator (Module 120).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from tac_pairing_self_consistent_chiral_engine import (
    calculate_self_consistent_pairing_gap,
    calculate_dynamic_moi,
    find_tac_pairing_chiral_barrier,
    scan_spin_evolution_with_pairing,
    PRESETS
)


class TestTACPairingChiral(unittest.TestCase):

    def test_pairing_cap_quenching(self):
        pair_low = calculate_self_consistent_pairing_gap(A_mass=134, J_spin=4.0, J_m=30.0)
        pair_high = calculate_self_consistent_pairing_gap(A_mass=134, J_spin=7.0, J_m=30.0)
        self.assertGreater(pair_low["Delta_J_MeV"], pair_high["Delta_J_MeV"])
        self.assertGreater(pair_high["rotational_frequency_omega_MeV"], pair_low["rotational_frequency_omega_MeV"])

    def test_dynamic_moi_increase(self):
        moi_paired = calculate_dynamic_moi(J_m_rig=30.0, J_s_rig=18.0, J_l_rig=8.0, Delta_J=0.8, Delta_0=1.0)
        moi_unpaired = calculate_dynamic_moi(J_m_rig=30.0, J_s_rig=18.0, J_l_rig=8.0, Delta_J=0.0, Delta_0=1.0)
        self.assertLess(moi_paired["J_m"], moi_unpaired["J_m"])
        self.assertAlmostEqual(moi_unpaired["J_m"], 30.0)

    def test_chiral_equilibrium_and_barrier(self):
        # Low spin: planar
        res_low = find_tac_pairing_chiral_barrier(J_spin=10.0, j_pi=5.5, j_nu=5.5, J_s=15.0, J_m=25.0, J_l=6.0)
        self.assertEqual(res_low["phase"], "planar_rotation")
        self.assertAlmostEqual(res_low["barrier_keV"], 0.0, delta=1.0)

        # High spin: aplanar chiral
        res_high = find_tac_pairing_chiral_barrier(J_spin=18.0, j_pi=5.5, j_nu=5.5, J_s=15.0, J_m=25.0, J_l=6.0)
        self.assertEqual(res_high["phase"], "aplanar_chiral_rotation")
        self.assertGreater(res_high["barrier_keV"], 10.0)
        self.assertGreater(res_high["aplanarity_volume_metric"], 0.30)

    def test_scan_spin_evolution_134pr(self):
        p = PRESETS["134Pr_chiral_tripod_pairing"]
        res = scan_spin_evolution_with_pairing(
            A_mass=p["A_mass"],
            spins=p["spins"],
            j_pi=p["j_pi"],
            j_nu=p["j_nu"],
            J_m_rig=p["J_m_rig"],
            J_s_rig=p["J_s_rig"],
            J_l_rig=p["J_l_rig"],
            f_block=p["f_block"],
            omega_c_MeV=p["omega_c_MeV"]
        )
        self.assertIsNotNone(res["critical_bifurcation_spin_Jcrit"])
        self.assertEqual(res["critical_bifurcation_spin_Jcrit"], 16.0)
        self.assertEqual(len(res["spin_trajectory"]), len(p["spins"]))


if __name__ == "__main__":
    unittest.main()
