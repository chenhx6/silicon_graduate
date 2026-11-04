#!/usr/bin/env python3
"""Independent algebra/uncertainty tests, not a nuclear mass validation."""
import sys
import unittest
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts' / 'analysis'))
from nuclear_odd_even_pairing_gap_multichannel_solver import NuclearPairingGapSolver


class TestNuclearOddEvenPairingGap(unittest.TestCase):
    def solver(self, q=74, degree=0, amplitude=0.6, **kwargs):
        b = {q+k: 1000+8*k+0.02*k**degree+(-1)**(q+k)*amplitude for k in range(-2,3)}
        return NuclearPairingGapSolver(A=q+56, Z=56, N=q, binding_chain_MeV=b, **kwargs)

    def test_both_parities_and_constant_staggering_normalization(self):
        for q in (73,74):
            g = self.solver(q=q).extract_multipoint_gaps()
            for name in g['filter_order']:
                self.assertAlmostEqual(g[name], 1.2, places=11)

    def test_polynomial_background_cancellation(self):
        for degree in (0,1,2,3):
            g = self.solver(degree=degree, amplitude=0).extract_multipoint_gaps()
            self.assertAlmostEqual(g['Delta_5_point_MeV'], 0, places=11)
            if degree < 3:
                self.assertAlmostEqual(g['Delta_4_point_left_MeV'], 0, places=11)
            if degree < 2:
                self.assertAlmostEqual(g['Delta_3_point_MeV'], 0, places=11)
        g = self.solver(degree=4, amplitude=0).extract_multipoint_gaps()
        self.assertAlmostEqual(g['Delta_5_point_MeV'], 0.06, places=11)

    def test_mass_to_binding_conversion(self):
        b = self.solver().b_chain
        m = {q: q*931.5-val+30000 for q,val in b.items()}
        s = NuclearPairingGapSolver(binding_chain_MeV=m, quantity='mass_energy_MeV')
        a, c = self.solver().extract_multipoint_gaps(), s.extract_multipoint_gaps()
        for name in a['filter_order']:
            self.assertAlmostEqual(a[name], c[name], places=10)

    def test_stencil_average_identities(self):
        b = {q: 850+7*q+0.001*q**3+0.7*(-1)**q for q in range(70,79)}
        def at(q):
            return NuclearPairingGapSolver(A=q+56,Z=56,N=q,binding_chain_MeV=b).extract_multipoint_gaps()
        for q in (73,74):
            self.assertAlmostEqual(at(q)['Delta_4_point_left_MeV'],
                (at(q)['Delta_3_point_MeV']+at(q-1)['Delta_3_point_MeV'])/2, places=11)
            self.assertAlmostEqual(at(q)['Delta_5_point_MeV'],
                (at(q)['Delta_4_point_left_MeV']+at(q+1)['Delta_4_point_left_MeV'])/2, places=11)

    def test_covariance_and_shared_mass_dependence(self):
        g = self.solver(uncertainties_MeV=[0.01]*5).extract_multipoint_gaps()
        c = np.asarray(g['indicator_covariance_MeV2'])
        np.testing.assert_allclose(np.diag(c),0.01**2*np.array([1.5,1.25,70/64]))
        self.assertAlmostEqual(c[0,2],0.01**2*1.25)
        self.assertGreater(c[0,2],0)

    def test_common_offset_cancels(self):
        g = self.solver(covariance_MeV2=np.ones((5,5))*0.25).extract_multipoint_gaps()
        np.testing.assert_allclose(g['indicator_covariance_MeV2'],np.zeros((3,3)),atol=1e-15)

    def test_missing_masses_never_replaced(self):
        s = NuclearPairingGapSolver(binding_chain_MeV={'N-1':990,'N':1000,'N+1':1008})
        g = s.extract_multipoint_gaps()
        self.assertEqual(g['Delta_3_point_MeV'],1)
        self.assertIsNone(g['Delta_4_point_left_MeV'])
        self.assertIsNone(g['Delta_5_point_MeV'])
        self.assertIsNone(g['filters']['Delta_3_point_MeV']['sigma_MeV'])
        empty = NuclearPairingGapSolver().execute_analysis()
        self.assertIsNone(empty['multipoint_pairing_gaps']['Delta_3_point_MeV'])
        self.assertEqual(empty['quasiparticle_properties']['status'],'not-inferred')

    def test_exact_labels_and_duplicates(self):
        s = NuclearPairingGapSolver(binding_chain_MeV={
            'N-2 (128Ba)':1,'N-1 (129Ba)':2,'N (130Ba)':4,'N+1 (131Ba)':5,'N+2 (132Ba)':8})
        self.assertEqual(s.b_chain[74],4)
        with self.assertRaises(ValueError):
            NuclearPairingGapSolver(binding_chain_MeV={'N':4,'74':4})

    def test_proton_axis_and_odd_parity(self):
        b = {q:1000+8*(q-55)+(-1)**q*0.6 for q in range(53,58)}
        s = NuclearPairingGapSolver(A=130,Z=55,N=75,binding_chain_MeV=b,species='proton')
        g = s.extract_multipoint_gaps()
        self.assertAlmostEqual(g['Delta_5_point_MeV'],1.2)
        self.assertEqual(g['particle_number_order'],list(range(53,58)))

    def test_negative_not_clipped(self):
        g = self.solver(amplitude=-0.6).extract_multipoint_gaps()
        self.assertAlmostEqual(g['Delta_5_point_MeV'],-1.2)

    def test_invalid_inputs(self):
        cases = [{'A':131},{'N':74.1},{'Z':True},{'quantity':'mass_u'},
            {'species':'pair'},{'binding_chain_MeV':{'N':float('nan')}},
            {'covariance_MeV2':np.eye(4)}, {'covariance_MeV2':np.diag([1,1,1,1,-1])},
            {'uncertainties_MeV':[-1]*5},
            {'covariance_MeV2':np.eye(5),'uncertainties_MeV':[1]*5}]
        for kw in cases:
            with self.subTest(kw=kw), self.assertRaises(ValueError): NuclearPairingGapSolver(**kw)
        c = np.eye(5); c[0,1]=0.5
        with self.assertRaises(ValueError): NuclearPairingGapSolver(covariance_MeV2=c)


if __name__ == '__main__':
    unittest.main()
