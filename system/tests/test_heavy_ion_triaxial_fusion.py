#!/usr/bin/env python3
"""
Unit tests for heavy_ion_triaxial_fusion_barrier_distribution_inverter.py (Module 157).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from heavy_ion_triaxial_fusion_barrier_distribution_inverter import (
    PRESETS,
    TriaxialFusionBarrierInverter
)

class TestHeavyIonTriaxialFusion(unittest.TestCase):

    def test_prolate_axial_barrier_splitting(self):
        p = PRESETS["16O_154Sm_prolate_baseline"]
        inverter = TriaxialFusionBarrierInverter(
            V_B0_MeV=p["V_B0_MeV"],
            R_B0_fm=p["R_B0_fm"],
            hbar_omega_B_MeV=p["hbar_omega_B_MeV"],
            beta2=p["beta2"],
            gamma_deg=p["gamma_deg"],
            Ap=p["Ap"],
            At=p["At"]
        )
        res = inverter.evaluate_barrier_distribution(np.linspace(54.0, 68.0, 15))
        cb = res["characteristic_barriers"]
        # In prolate case (gamma=0), short and intermediate axes must have identical barriers
        self.assertAlmostEqual(cb["V_side_short_axis_MeV"], cb["V_side_interm_axis_MeV"], places=4)
        self.assertAlmostEqual(cb["triaxial_belly_splitting_MeV"], 0.0, places=4)
        # Pole barrier must be significantly lower than side barrier (prolate stretching)
        self.assertLess(cb["V_pole_MeV"], cb["V_side_short_axis_MeV"])
        self.assertFalse(res["is_triaxial_fingerprint"])

    def test_triaxial_belly_splitting_signature(self):
        p = PRESETS["16O_186W_triaxial_candidate"]
        inverter = TriaxialFusionBarrierInverter(
            V_B0_MeV=p["V_B0_MeV"],
            R_B0_fm=p["R_B0_fm"],
            hbar_omega_B_MeV=p["hbar_omega_B_MeV"],
            beta2=p["beta2"],
            gamma_deg=p["gamma_deg"],
            Ap=p["Ap"],
            At=p["At"]
        )
        res = inverter.evaluate_barrier_distribution(np.linspace(66.0, 82.0, 15))
        cb = res["characteristic_barriers"]
        # In triaxial case (gamma=22), side barriers must split significantly (> 3 MeV)
        self.assertGreater(cb["triaxial_belly_splitting_MeV"], 3.0)
        self.assertTrue(res["is_triaxial_fingerprint"])

    def test_cross_section_monotonicity(self):
        inverter = TriaxialFusionBarrierInverter(V_B0_MeV=65.0)
        sig1 = inverter.calculate_cross_section(60.0)
        sig2 = inverter.calculate_cross_section(65.0)
        sig3 = inverter.calculate_cross_section(75.0)
        self.assertGreater(sig2, sig1)
        self.assertGreater(sig3, sig2)

if __name__ == "__main__":
    import numpy as np
    unittest.main()
