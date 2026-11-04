"""Regression tests for the bounded Suhonen-style constant-pairing BCS solver."""

import sys
from pathlib import Path
import math
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts" / "analysis"))

from bcs_constant_pairing_solver import solve_constant_pairing_bcs


class BCSConstantPairingTests(unittest.TestCase):
    def test_half_filled_degenerate_shell_has_analytic_gap(self):
        result = solve_constant_pairing_bcs(
            single_particle_energies_MeV=[0.0],
            pair_degeneracies=[3.0],
            target_particles=3.0,
            pairing_strength_MeV=1.0,
        )
        self.assertTrue(result["converged"])
        self.assertAlmostEqual(result["particle_number"], 3.0, places=8)
        self.assertAlmostEqual(result["chemical_potential_MeV"], 0.0, places=8)
        self.assertAlmostEqual(result["gap_MeV"], 1.5, places=8)
        self.assertAlmostEqual(result["orbitals"][0]["v2"], 0.5, places=8)
        self.assertLess(abs(result["gap_equation_residual_MeV"]), 1.0e-8)

    def test_number_constraint_and_quasiparticle_identity(self):
        result = solve_constant_pairing_bcs(
            single_particle_energies_MeV=[0.0, 0.87, 5.08],
            pair_degeneracies=[3.0, 1.0, 2.0],
            target_particles=4.0,
            pairing_strength_MeV=1.0,
        )
        self.assertTrue(result["converged"])
        self.assertAlmostEqual(result["particle_number"], 4.0, places=8)
        self.assertLess(abs(result["particle_number_residual"]), 1.0e-8)
        for orbital in result["orbitals"]:
            u = orbital["u"]
            v = orbital["v"]
            eta = orbital["eta_MeV"]
            eqp = orbital["quasiparticle_energy_MeV"]
            self.assertAlmostEqual(u * u + v * v, 1.0, places=8)
            self.assertGreaterEqual(eqp, 0.0)
            self.assertTrue(math.isfinite(eta))

    def test_invalid_pairing_strength_is_rejected(self):
        with self.assertRaises(ValueError):
            solve_constant_pairing_bcs([0.0], [1.0], 1.0, 0.0)


if __name__ == "__main__":
    unittest.main()
