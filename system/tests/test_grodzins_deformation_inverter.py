"""
Unit tests for Grodzins Product Rule & Quadrupole Deformation beta_2 Inverter.

Benchmarked against:
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 §8.4 (形变核转动能谱与形变参量).
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, §4-2.
  - S. Raman, C. W. Nestor, Jr., and P. Tikkanen, At. Data Nucl. Data Tables 78, 1 (2001).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from grodzins_deformation_beta2_quadrupole_inverter import (
    invert_beta2_and_quadrupole
)


class GrodzinsDeformationInverterTests(unittest.TestCase):

    def test_154Sm_well_deformed_prolate_rotor_benchmark(self):
        """Verify 154Sm: beta2 ~ 0.341, Grodzins ratio ~ 1.04, pairing reduction ~ 0.54."""
        # Raman 2001: 154Sm: E(2+) = 82.0 keV, B(E2) = 4.35 e^2 b^2, beta2 = 0.341
        sm = invert_beta2_and_quadrupole(Z=62, A=154, B_E2_e2_b2=4.35, E_2plus_keV=82.0)
        self.assertAlmostEqual(sm["quadrupole_deformation_beta2"], 0.3406, places=3)
        self.assertAlmostEqual(sm["intrinsic_quadrupole_moment_Q0_eb"], 6.613, places=2)
        self.assertAlmostEqual(sm["spectroscopic_quadrupole_moment_Qs_eb"], -1.889, places=2)
        self.assertAlmostEqual(sm["grodzins_ratio"], 1.037, places=2)
        self.assertAlmostEqual(sm["superfluid_pairing_reduction_ratio"], 0.543, places=2)
        self.assertIn("Highly Deformed", sm["deformation_classification"])

    def test_132Sn_doubly_magic_spherical_benchmark(self):
        """Verify 132Sn: near-spherical beta2 < 0.05, Grodzins ratio << 1.0, J_exp << J_rig."""
        sn = invert_beta2_and_quadrupole(Z=50, A=132, B_E2_e2_b2=0.011, E_2plus_keV=4041.0)
        self.assertLess(sn["quadrupole_deformation_beta2"], 0.05)
        self.assertLess(sn["grodzins_ratio"], 0.25)
        self.assertLess(sn["superfluid_pairing_reduction_ratio"], 0.05)
        self.assertIn("Near-Spherical", sn["deformation_classification"])

    def test_134Ce_triaxial_core_benchmark(self):
        """Verify 134Ce (A~130 wobbler core): moderate deformation beta2 ~ 0.17."""
        ce = invert_beta2_and_quadrupole(Z=58, A=134, B_E2_e2_b2=0.78, E_2plus_keV=409.2)
        self.assertAlmostEqual(ce["quadrupole_deformation_beta2"], 0.174, places=2)
        self.assertIn("Transitional", ce["deformation_classification"])

    def test_invalid_parameters_raised(self):
        """Z <= 0, A <= 0, or B(E2) <= 0 must raise ValueError."""
        with self.assertRaises(ValueError):
            invert_beta2_and_quadrupole(Z=0, A=154, B_E2_e2_b2=4.35)
        with self.assertRaises(ValueError):
            invert_beta2_and_quadrupole(Z=62, A=154, B_E2_e2_b2=-1.0)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        res = invert_beta2_and_quadrupole(Z=62, A=154, B_E2_e2_b2=4.35, E_2plus_keV=82.0)
        s = json.dumps(res, allow_nan=False)
        self.assertIn("quadrupole_deformation_beta2", s)


if __name__ == "__main__":
    unittest.main()
