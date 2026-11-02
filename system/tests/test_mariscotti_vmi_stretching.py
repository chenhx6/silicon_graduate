"""
Unit tests for Mariscotti Variable Moment of Inertia (VMI) Model & Centrifugal Stretching.

Benchmarked against:
  - M. A. J. Mariscotti, G. Scharff-Goldhaber, and B. Kirk, Phys. Rev. 178, 1864 (1969).
  - 卢希庭, 《原子核物理（修订版）》, 原子能出版社 (2000), 第8章 §8.5 (VMI模型, 印刷 pp. 212–215).
  - S. Frauendorf, in Chirality and Wobbling in Atomic Nuclei (CRC 2025), Ch. 2, p. 50 (VMI in 112Ru).
"""

import unittest
import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from mariscotti_vmi_rotational_stretching_calculator import (
    solve_vmi_cubic_moi,
    calculate_vmi_spectrum,
    invert_vmi_parameters
)


class MariscottiVMITests(unittest.TestCase):

    def test_rigid_rotor_limit_high_stiffness(self):
        """When restoring constant C is very large, VMI must recover rigid rotor R_4/2 = 3.3333."""
        spec = calculate_vmi_spectrum(J0=35.0, C=2500.0, spins=[2.0, 4.0, 6.0, 8.0])
        self.assertAlmostEqual(spec["R_4_2_ratio"], 3.3333, places=3)
        self.assertEqual(spec["structural_classification"], "Rigid / Well-Deformed Rotor (SU(3) limit)")
        # In rigid limit, dynamic MOI J(I) equals J0
        for lv in spec["levels"]:
            self.assertAlmostEqual(lv["moment_of_inertia_J_hbar2_MeV"], 35.0, places=1)
            self.assertLess(lv["stretching_fraction_pct"], 0.05)

    def test_transitional_centrifugal_stretching(self):
        """In transitional nuclei (moderate C), J(I) must expand dynamically with spin."""
        spec = calculate_vmi_spectrum(J0=7.0, C=0.05, spins=[2.0, 4.0, 6.0, 8.0, 10.0])
        self.assertAlmostEqual(spec["R_4_2_ratio"], 3.0194, places=2)
        self.assertEqual(spec["structural_classification"], "Centrifugally Stretched / VMI Deformed Rotor")
        # J(I) grows monotonically with spin
        j_vals = [lv["moment_of_inertia_J_hbar2_MeV"] for lv in spec["levels"]]
        for i in range(len(j_vals) - 1):
            self.assertLess(j_vals[i], j_vals[i+1])

    def test_168Er_rotor_inversion_benchmark(self):
        """Inversion of 168Er ground band must yield J0 ~ 35.8 hbar^2/MeV and RMS < 5 keV."""
        spins = [2.0, 4.0, 6.0, 8.0, 10.0, 12.0]
        e_exp = [79.8, 264.1, 548.7, 912.0, 1344.0, 1830.0]
        inv = invert_vmi_parameters(spins, e_exp)
        self.assertAlmostEqual(inv["J0_fitted_hbar2_MeV"], 35.805, places=1)
        self.assertLess(inv["rms_residual_keV"], 5.0)

    def test_112Ru_triaxial_wobbler_core_benchmark(self):
        """Inversion of 112Ru wobbler core ground band matches Frauendorf (2025) Ch. 2 notes."""
        spins = [2.0, 4.0, 6.0, 8.0, 10.0]
        e_exp = [237.2, 678.8, 1279.0, 1999.0, 2780.0]
        inv = invert_vmi_parameters(spins, e_exp)
        self.assertAlmostEqual(inv["J0_fitted_hbar2_MeV"], 11.516, places=1)
        self.assertLess(inv["rms_residual_keV"], 8.0)

    def test_invalid_parameters_raised(self):
        """C <= 0 or negative spins must raise ValueError."""
        with self.assertRaises(ValueError):
            solve_vmi_cubic_moi(J0=10.0, C=-1.0, spin_I=2.0)
        with self.assertRaises(ValueError):
            solve_vmi_cubic_moi(J0=10.0, C=1.0, spin_I=-2.0)

    def test_strict_json_serialization(self):
        """Verify strict RFC JSON serialization without NaN or Inf."""
        spec = calculate_vmi_spectrum(J0=20.0, C=10.0, spins=[2.0, 4.0, 6.0])
        s = json.dumps(spec, allow_nan=False)
        self.assertIn("R_4_2_ratio", s)


if __name__ == "__main__":
    unittest.main()
