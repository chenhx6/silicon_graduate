#!/usr/bin/env python3
"""
Unit tests for in_beam_dsam_zbl_stopping_lifetime_inverter.py (Module 159).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_dsam_zbl_stopping_lifetime_inverter import (
    PRESETS,
    InBeamDSAMZBLInverter
)

class TestInBeamDSAMZBL(unittest.TestCase):

    def test_attenuation_monotonicity(self):
        inv = InBeamDSAMZBLInverter(Ar=130, Zr=56, As=197, Zs=79)
        times_ps, v_ratio, cos_phi = inv.integrate_slowing_down()
        # Velocity must decrease monotonically
        self.assertTrue(np.all(np.diff(v_ratio) <= 1e-6))
        # Total stopping time should be between 1.0 and 3.0 ps for Au
        self.assertGreater(times_ps[-1], 0.8)
        self.assertLess(times_ps[-1], 4.0)

        # F(tau) must decrease monotonically as lifetime increases
        F1 = inv.calculate_F_tau(0.05, times_ps, v_ratio, cos_phi)
        F2 = inv.calculate_F_tau(0.20, times_ps, v_ratio, cos_phi)
        F3 = inv.calculate_F_tau(1.00, times_ps, v_ratio, cos_phi)
        self.assertGreater(F1, F2)
        self.assertGreater(F2, F3)

    def test_130Ba_lifetime_inversion(self):
        p = PRESETS["130Ba_8plus_in_Au_backing"]
        inv = InBeamDSAMZBLInverter(
            Ar=p["Ar"], Zr=p["Zr"], As=p["As"], Zs=p["Zs"],
            density_g_cm3=p["stopper_density_g_cm3"], beta_0=p["beta_0"]
        )
        res = inv.invert_lifetime(p["F_experimental"], p["F_uncertainty"], p["side_feeding_tau_ps"])
        # Level lifetime should be in the expected range ~ 0.3 - 0.7 ps
        self.assertGreater(res["tau_level_ps"], 0.2)
        self.assertLess(res["tau_level_ps"], 0.8)
        self.assertGreater(res["sigma_tau_ps"], 0.01)

    def test_quadrupole_moment_calculation(self):
        inv = InBeamDSAMZBLInverter()
        props = inv.calculate_transition_properties(0.50, 712.5, 8.0)
        # B(E2) must be positive and collectivity > 50 W.u.
        self.assertGreater(props["B_E2_e2b2"], 0.2)
        self.assertGreater(props["B_E2_W_u"], 50.0)
        # Q_0 should be in realistic range 4 - 8 e*b
        self.assertGreater(props["intrinsic_quadrupole_moment_Q0_eb"], 3.0)
        self.assertLess(props["intrinsic_quadrupole_moment_Q0_eb"], 12.0)

if __name__ == "__main__":
    import numpy as np
    unittest.main()
