"""Analytic sum-rule and symmetry tests; no experimental certification."""
from dataclasses import replace
from pathlib import Path
import sys
import unittest

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts/analysis"))
from paired_single_j_rotor import PairedRotorParameters, solve
from paired_single_j_transfer import strengths


class BareTransferTests(unittest.TestCase):
    def test_free_rotor_only_R0_is_reached(self):
        for tj in (1, 3, 11):
            for lam in (-2.0, 0.0, 2.0):
                delta = 1.0
                s = solve(tj, PairedRotorParameters(tj, 0., 23., (10., 10., 10.), lam, delta))
                t = strengths(s)
                occupation = (1 + lam / np.hypot(lam, delta)) / 2
                self.assertAlmostEqual(t.removal_strengths[0], (tj+1)*occupation, places=11)
                self.assertAlmostEqual(t.addition_strengths[0], (tj+1)*(1-occupation), places=11)
                np.testing.assert_allclose(t.removal_strengths[1:], 0., atol=1e-24)
                np.testing.assert_allclose(t.addition_strengths[1:], 0., atol=1e-24)

    def test_complete_sum_rules_with_deformed_field(self):
        s = solve(11, PairedRotorParameters(11, 9.75, 21., (15., 6., 2.), .75, 1.))
        t = strengths(s)
        self.assertLess(t.sum_rule_error, 1e-11)
        self.assertGreater(np.count_nonzero(t.removal_strengths > 1e-6), 1)
        self.assertLess(t.removal_strengths[:2].sum(), t.removal_sum)
        self.assertFalse(t.removal_strengths.flags.writeable)

    def test_parameter_duality_exchanges_addition_and_removal(self):
        p = PairedRotorParameters(11, 9.75, 21., (15., 6., 2.), .75, 1.)
        pd = PairedRotorParameters(11, 9.75, 39., (15., 2., 6.), -.75, 1.)
        s, sd = solve(11, p), solve(11, pd)
        np.testing.assert_allclose(s.eigenvalues_MeV, sd.eigenvalues_MeV, atol=1e-11)
        a, b = strengths(s), strengths(sd)
        np.testing.assert_allclose(a.removal_strengths, b.addition_strengths, atol=1e-10)
        np.testing.assert_allclose(a.addition_strengths, b.removal_strengths, atol=1e-10)
        self.assertGreater(np.max(abs(a.removal_strengths-b.removal_strengths)), .01)

    def test_eigenstate_rephasing_does_not_change_strength(self):
        s = solve(11, PairedRotorParameters(11, 9.75, 21., (15., 6., 2.), .75, 1.))
        phase = np.exp(1j*np.linspace(0., 6., len(s.eigenvalues_MeV)))
        alternate = replace(s, eigenvectors=s.eigenvectors*phase)
        a, b = strengths(s), strengths(alternate)
        np.testing.assert_allclose(a.removal_strengths, b.removal_strengths, atol=1e-13)
        np.testing.assert_allclose(a.addition_strengths, b.addition_strengths, atol=1e-13)

    def test_wrong_final_spin_is_outside_operator_scope(self):
        s = solve(9, PairedRotorParameters(11, 9.75, 21., (15., 6., 2.), .75, 1.))
        with self.assertRaises(ValueError):
            strengths(s)


if __name__ == "__main__":
    unittest.main()
