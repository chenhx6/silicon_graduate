"""BM-II conditional strength contract: independent geometry and all roots."""
import json
import math
from pathlib import Path
import sys
import unittest
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts' / 'analysis'))
from gamma_band_mixing_z_gamma_alaga_inverter import (
    calculate_alaga_cg_coefficient, invert_z_gamma_from_branching,
    format_text_report,
)


class GammaBandMixingZGammaTests(unittest.TestCase):
    def test_independent_cg_from_total_angular_momentum(self):
        # Diagonalize J^2 in M=0 product basis, independently of factorial CG.
        for j in (2, 3, 4, 7):
            ms = list(range(-2, 3))
            h = np.diag([j*(j+1)+6-2*m*m for m in ms]).astype(float)
            for k, m in enumerate(ms[:-1]):
                h[k,k+1] = h[k+1,k] = math.sqrt((j*(j+1)-m*(m+1))*(6-m*(m+1)))
            vals, vecs = np.linalg.eigh(h)
            for J in range(abs(j-2), j+3):
                if J % 2 == 0:
                    idx = int(np.argmin(abs(vals-J*(J+1))))
                    self.assertAlmostEqual(vals[idx], J*(J+1), places=11)
                    self.assertAlmostEqual(calculate_alaga_cg_coefficient(j,J)**2,
                                           vecs[4,idx]**2, places=12)
        self.assertEqual(calculate_alaga_cg_coefficient(5,3), 0)
        with self.assertRaises(ValueError):
            calculate_alaga_cg_coefficient(1,0)

    def test_alaga_zero_mixing_and_sign_ambiguity(self):
        r = invert_z_gamma_from_branching(.7)
        self.assertEqual(r['inverted_z_gamma'], 0)
        self.assertAlmostEqual(r['predicted_B_E2_4g_to_2g_ratio'], .05)
        self.assertEqual(len(r['branches']), 2)
        self.assertAlmostEqual(r['branches'][1]['a2'], 1/3)
        self.assertIsNone(r['rotational_vibrational_h2_keV'])

    def test_two_branch_round_trips_and_cross_predictions(self):
        for R in (0, .175, .32, .54, .7, 2.8, 6.3):
            r = invert_z_gamma_from_branching(R)
            self.assertEqual(len(r['branches']), 1 if R == 0 else 2)
            for b in r['branches']:
                a, t, z = b['a2'], b['legacy_rostovsky_z_gamma'], b['bm_z2']
                self.assertAlmostEqual(.7*(1-6*a)**2, R, places=12)
                if t is not None:
                    self.assertAlmostEqual(t/(2*(1+t)), a)
                    self.assertAlmostEqual(.7*((1-2*t)/(1+t))**2, R)
                    self.assertAlmostEqual(.05*((1+8*t)/(1+t))**2,
                                           b['predicted_B_E2_4g_to_2g_ratio'])
                if z is not None:
                    self.assertAlmostEqual(z/(2*(1+2*z)), a)
                    self.assertAlmostEqual(.7*((1-z)/(1+2*z))**2, R)
                self.assertIsNone(b['h2_keV'])
                self.assertIsNone(b['epsilon2'])
        # Real solutions must survive coordinate poles.
        self.assertIsNone(invert_z_gamma_from_branching(.175)['branches'][1]['bm_z2'])
        self.assertIsNone(invert_z_gamma_from_branching(2.8)['branches'][1]['legacy_rostovsky_z_gamma'])

    def test_fixture_does_not_infer_coupling_or_shape(self):
        r = invert_z_gamma_from_branching(.540,821.1,79.8)
        self.assertAlmostEqual(r['inverted_z_gamma'], (1-math.sqrt(.540/.7))/6)
        self.assertIsNone(r['rotational_vibrational_h2_keV'])
        self.assertIn('Undetermined',r['structural_classification'])
        self.assertIn('undetermined',format_text_report(r))
        json.dumps(r,allow_nan=False)

    def test_invalid_parameters_raised(self):
        for ratio in (-.5, float('nan'), float('inf')):
            with self.assertRaises(ValueError):
                invert_z_gamma_from_branching(ratio)
        for kwargs in ({'I_gamma':3}, {'E_2g_keV':-1}, {'E_2gamma_keV':float('nan')}):
            with self.assertRaises(ValueError):
                invert_z_gamma_from_branching(.54,**kwargs)


if __name__ == '__main__':
    unittest.main()
