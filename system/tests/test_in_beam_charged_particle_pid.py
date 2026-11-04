import numpy as np
#!/usr/bin/env python3
"""
Unit tests for in_beam_charged_particle_pid_delta_e_telescope_inverter.py (Module 163).
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts" / "analysis"))

from in_beam_charged_particle_pid_delta_e_telescope_inverter import (
    PRESETS,
    ChargedParticlePIDInverter
)

class TestInBeamChargedParticlePID(unittest.TestCase):

    def test_relative_pid_scaling(self):
        inv = ChargedParticlePIDInverter(thickness_T0_um=65.0, angle_incidence_deg=0.0)
        # Check that PI increases as expected with mass and charge
        # Proton (1.2 MeV, 14.5 MeV) vs Alpha (8.5 MeV, 18.2 MeV)
        pi_p = inv.calculate_pid_value(1.20, 14.5)
        pi_d = inv.calculate_pid_value(2.20, 12.0)
        pi_a = inv.calculate_pid_value(8.50, 18.2)
        self.assertGreater(pi_d, pi_p)
        self.assertGreater(pi_a, pi_d)
        # Alpha should have much higher PI than proton (~ 8 - 12x)
        self.assertGreater(pi_a / pi_p, 6.0)

    def test_geometric_thickness_scaling(self):
        inv_0deg = ChargedParticlePIDInverter(thickness_T0_um=65.0, angle_incidence_deg=0.0)
        inv_45deg = ChargedParticlePIDInverter(thickness_T0_um=65.0, angle_incidence_deg=45.0)
        # Effective thickness at 45 deg should be T0 / cos(45) ~ 1.414 * T0
        self.assertAlmostEqual(inv_45deg.T_eff / inv_0deg.T_eff, np.sqrt(2.0), places=2)

    def test_fom_clean_separation(self):
        inv = ChargedParticlePIDInverter()
        fom = inv.evaluate_separation_fom(proton_ref_pi=20.0, sigma_pct=7.0)
        # Proton vs Alpha must have FOM > 3.0
        self.assertGreater(fom["1H (Proton) vs 4He (Alpha)"]["FOM"], 3.0)
        self.assertTrue(fom["1H (Proton) vs 4He (Alpha)"]["is_clean_separation"])

if __name__ == "__main__":
    import numpy as np
    unittest.main()
