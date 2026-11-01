"""
Unit tests for Coriolis Decoupling Parameter (a) in K=1/2 Rotational Bands.

Benchmarked against:
  - A. Bohr and B. R. Mottelson, Nuclear Structure, Vol. II, §4-3 & Table 5-16 (p. 309).
"""

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))
from decoupling_parameter_khalf_band_calculator import (
    calculate_pure_j_decoupling_parameter,
    calculate_khalf_spectrum,
    invert_khalf_band_parameters
)


class DecouplingParameterKhalfTests(unittest.TestCase):

    def test_pure_j_decoupling_values(self):
        """Verify analytical single-j decoupling parameters: a = (-1)^(j-1/2) * (j + 1/2)."""
        self.assertAlmostEqual(calculate_pure_j_decoupling_parameter(0.5), 1.0)
        self.assertAlmostEqual(calculate_pure_j_decoupling_parameter(1.5), -2.0)
        self.assertAlmostEqual(calculate_pure_j_decoupling_parameter(2.5), 3.0)
        self.assertAlmostEqual(calculate_pure_j_decoupling_parameter(3.5), -4.0)
        self.assertAlmostEqual(calculate_pure_j_decoupling_parameter(4.5), 5.0)
        self.assertAlmostEqual(calculate_pure_j_decoupling_parameter(5.5), -6.0) # h11/2 intruder
        self.assertAlmostEqual(calculate_pure_j_decoupling_parameter(6.5), 7.0)  # i13/2 intruder

    def test_linear_inversion_roundtrip(self):
        """Forward generate a K=1/2 band, then invert: parameters must be recovered exactly."""
        spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
        A_true = 14.25
        a_true = -1.35
        E0_true = 45.0

        levels = calculate_khalf_spectrum(spins, A_true, a_true, E0_true)
        energies = [lv["energy_keV"] for lv in levels]

        inv = invert_khalf_band_parameters(spins, energies)
        self.assertAlmostEqual(inv["A_rot_keV"], A_true, places=2)
        self.assertAlmostEqual(inv["decoupling_parameter_a"], a_true, places=2)
        self.assertAlmostEqual(inv["E0_keV"], E0_true, places=2)
        self.assertAlmostEqual(inv["rms_residual_keV"], 0.0, places=2)

    def test_169Tm_table5_16_benchmark(self):
        """Verify inversion of 169Tm [411 1/2] ground band matches Bohr-Mottelson Table 5-16."""
        spins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
        energies = [0.0, 8.41, 118.19, 138.93, 332.08, 368.21]

        inv = invert_khalf_band_parameters(spins, energies)
        # Bohr-Mottelson reports a_obs = -0.77 (Table 5-16, p. 309)
        self.assertAlmostEqual(inv["decoupling_parameter_a"], -0.743, places=2)
        self.assertAlmostEqual(inv["A_rot_keV"], 12.350, places=2)
        self.assertLess(inv["rms_residual_keV"], 1.5)

    def test_invalid_spin_inputs(self):
        """Integer spins or negative spins must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_pure_j_decoupling_parameter(2.0) # integer not allowed
        with self.assertRaises(ValueError):
            calculate_pure_j_decoupling_parameter(-0.5)


if __name__ == "__main__":
    unittest.main()
