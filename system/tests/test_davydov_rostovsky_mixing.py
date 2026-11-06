"""Compatibility and reparameterization, without mechanism identification."""
import json
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'/'analysis'))
from davydov_rostovsky_triaxial_band_mixing_solver import (
    PRESETS, invert_gamma_mixing_parameter, calculate_davydov_rostovsky_parameters,
    run_davydov_rostovsky_analysis, format_text_report,
)


class TestDavydovRostovskyMixing(unittest.TestCase):
    def test_alaga_rigid_limit(self):
        p = PRESETS['rigid_rotor_zero_mixing_limit']
        m = calculate_davydov_rostovsky_parameters(p['E_2g_keV'],p['E_2gamma_keV'],p['E_0beta_keV'],p['exp_be2_gamma_ratio'])
        self.assertEqual(m['z_gamma_mixing_parameter'],0)
        self.assertEqual(m['predicted_ratio_2gamma_to_4g_vs_2g'],.05)
        self.assertEqual(len(m['branches']),2)
        self.assertIsNone(m['coupling_matrix_element_h2_keV'])
        self.assertIsNone(m['non_adiabatic_softness_mu'])

    def test_legacy_fixtures_and_text_json(self):
        for p in PRESETS.values():
            r = run_davydov_rostovsky_analysis(p['nucleus'],p['E_2g_keV'],p['E_4g_keV'],p['E_2gamma_keV'],p['E_0beta_keV'],p['exp_be2_gamma_ratio'])
            m = r['mixing_results']
            q = math.sqrt(p['exp_be2_gamma_ratio']/.7)
            self.assertAlmostEqual(m['z_gamma_mixing_parameter'],(1-q)/(2+q))
            self.assertIsNone(m['coupling_matrix_element_h2_keV'])
            self.assertIn('unverified',m['preset_provenance'])
            self.assertIn('No unique',format_text_report(r))
            json.dumps(r,allow_nan=False)

    def test_both_branches_mapping_and_corrected_4g_prediction(self):
        for R in (0,.175,.54,.7,2.8,6.3):
            m = calculate_davydov_rostovsky_parameters(100,1200,1500,R)
            self.assertEqual(invert_gamma_mixing_parameter(R),m['z_gamma_mixing_parameter'])
            for b in m['branches']:
                t = b['legacy_rostovsky_z_gamma']
                if t is not None:
                    a = t/(2*(1+t))
                    self.assertAlmostEqual(.7*((1-2*t)/(1+t))**2,R)
                    self.assertAlmostEqual(.05*(1+14*a)**2,b['predicted_B_E2_4g_to_2g_ratio'])
            self.assertEqual(len(m['branches']),1 if R==0 else 2)
        b = calculate_davydov_rostovsky_parameters(100,1200,1500,2.8)['branches'][1]
        self.assertIsNone(b['legacy_rostovsky_z_gamma'])
        self.assertEqual(b['legacy_rostovsky_coordinate'],'infinite')
        self.assertAlmostEqual(b['a2'],.5)
        self.assertAlmostEqual(b['predicted_B_E2_4g_to_2g_ratio'],3.2)

    def test_inversion_monotonicity_on_declared_branch(self):
        self.assertGreater(invert_gamma_mixing_parameter(.45),invert_gamma_mixing_parameter(.65))
        self.assertLess(invert_gamma_mixing_parameter(.8),0)

    def test_invalid_inputs_are_not_clamped(self):
        for R in (-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):
                invert_gamma_mixing_parameter(R)
        for e in (0,-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):
                calculate_davydov_rostovsky_parameters(100,1200,e,.54)


if __name__ == '__main__':
    unittest.main()
