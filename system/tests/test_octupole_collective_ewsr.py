#!/usr/bin/env python3
"""
Unit tests for Microscopic Octupole Modes, Isoscalar Energy-Weighted
Sum Rules (IS-EWSR) & Alternating-Parity Pear-Shaped Dynamics (Module 118).
"""

import sys
from pathlib import Path
import unittest
import numpy as np

MODULES_DIR = Path(__file__).resolve().parent.parent / "scripts" / "analysis"
sys.path.insert(0, str(MODULES_DIR))

from octupole_collective_ewsr_parity_doublet_analyzer import (
    calculate_octupole_ewsr,
    calculate_parity_splitting_ewsr,
    invert_intrinsic_dipole_moment,
    run_octupole_analysis,
    PRESETS
)


class TestOctupoleCollectiveEWSR(unittest.TestCase):

    def test_octupole_ewsr_208pb(self):
        ewsr = calculate_octupole_ewsr(A_mass=208, Z_charge=82, E_3minus_keV=2614.5, B_E3_down_Wu=34.0)
        self.assertAlmostEqual(ewsr["R0_fm"], 7.11, places=1)
        self.assertGreater(ewsr["B_Wu_e2_fm6"], 2500.0)
        self.assertGreater(ewsr["S_IS_EWSR_MeV_e2_fm6"], 1e7)
        self.assertGreater(ewsr["EWSR_exhaustion_percent"], 5.0)
        self.assertLess(ewsr["EWSR_exhaustion_percent"], 12.0)

    def test_parity_splitting_collapse(self):
        p = PRESETS["224Ra_pear_shaped"]
        ps = calculate_parity_splitting_ewsr(p["pos_spins"], p["pos_energies_keV"], p["neg_spins"], p["neg_energies_keV"])
        self.assertEqual(len(ps["splittings"]), 5)
        # High spin parity splitting delta_E should be smaller than low spin
        dE_low = ps["splittings"][0]["delta_E_keV"]
        dE_high = ps["splittings"][-1]["delta_E_keV"]
        self.assertLess(dE_high, dE_low)

    def test_dipole_moment_inversion(self):
        res = invert_intrinsic_dipole_moment(
            A_mass=224, Z_charge=88, beta2=0.19, spin_I=5.0,
            E_E1_keV=179.0, E_E2_keV=143.0, I_E1=35.0, I_E2=100.0
        )
        self.assertGreater(res["D0_intrinsic_dipole_e_fm"], 0.0)
        self.assertGreater(res["beta3_octupole_deformation"], 0.0)

    def test_run_octupole_analysis_preset(self):
        p = PRESETS["144Ba_octupole_deformed"]
        res = run_octupole_analysis(
            A_mass=p["A_mass"],
            Z_charge=p["Z_charge"],
            beta2=p["beta2"],
            E_3minus_keV=p["E_3minus_keV"],
            B_E3_down_Wu=p["B_E3_down_Wu"],
            pos_spins=p["pos_spins"],
            pos_energies_keV=p["pos_energies_keV"],
            neg_spins=p["neg_spins"],
            neg_energies_keV=p["neg_energies_keV"],
            branching_test=p["branching_test"]
        )
        self.assertIsNotNone(res["ewsr_analysis"])
        self.assertIsNotNone(res["parity_splitting_analysis"])
        self.assertIsNotNone(res["dipole_moment_inversion"])


if __name__ == "__main__":
    unittest.main()
