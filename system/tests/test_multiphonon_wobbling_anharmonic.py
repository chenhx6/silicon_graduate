#!/usr/bin/env python3
"""Source-bounded energy/branch arithmetic and independent oscillator checks."""
import sys
import unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'/'analysis'))
from multiphonon_wobbling_anharmonic_spectrum_solver import (
    MultiphononWobblingSolver,oscillator_operator_strengths,yrast_referenced_excitation,
    be2_ratios_for_mixing_branches,e2_photon_width_ratio,PRESETS)
from multiphonon_wobbling_anharmonic_calculator import audit_multiphonon_wobbling_candidate,evaluate_multiphonon_wobbling_energies


class TestConditionalPhononDescriptors(unittest.TestCase):
    def test_harmonic_energy_is_not_confirmation(self):
        r=MultiphononWobblingSolver(g4_anharmonicity_keV=0).solve_multiphonon_properties()
        self.assertEqual(r['energy_ratio_R21'],2)
        self.assertIsNone(r['is_two_phonon_confirmed'])
        self.assertEqual(r['electromagnetic_rates']['missing_strengths'],['10','21','20'])

    def test_g_does_not_determine_an_operator(self):
        a=MultiphononWobblingSolver(g4_anharmonicity_keV=-35,mixing_epsilon=.12,B_E2_in_e2b2=9.5).solve_multiphonon_properties()
        b=MultiphononWobblingSolver(g4_anharmonicity_keV=0).solve_multiphonon_properties()
        self.assertEqual(a['electromagnetic_rates'],b['electromagnetic_rates'])
        self.assertIsNone(a['electromagnetic_rates']['B_E2_2_to_0_e2b2'])
        self.assertTrue(a['legacy_parameters_ignored'])

    def test_fock_matrix_elements_independent_of_polynomial_energy(self):
        # Construct a and T explicitly, independent of the analytic implementation.
        a=np.diag(np.sqrt(np.arange(1,7)),1)
        q=a+a.T
        t=.7*q+.2*(q@q)
        r=oscillator_operator_strengths(.7,.2)
        self.assertAlmostEqual(r['squared_1_to_0'],abs(t[0,1])**2)
        self.assertAlmostEqual(r['squared_2_to_1'],abs(t[1,2])**2)
        self.assertAlmostEqual(r['squared_2_to_0'],abs(t[0,2])**2)
        self.assertGreater(r['squared_2_to_0'],0)
        self.assertEqual(MultiphononWobblingSolver(g4_anharmonicity_keV=0).solve_multiphonon_properties()['energy_ratio_R21'],2)

    def test_linear_operator_has_twofold_strength_and_zero_direct_element(self):
        r=oscillator_operator_strengths(1,0)
        self.assertEqual(r['squared_2_to_1']/r['squared_1_to_0'],2)
        self.assertEqual(r['squared_2_to_0'],0)

    def test_gamma_width_is_not_strength_ratio(self):
        self.assertAlmostEqual(e2_photon_width_ratio(.01,.1,1000,500),3.2)
        r=MultiphononWobblingSolver(transition_strengths={'10':.05,'21':.1,'20':.01},
            gamma_energies_keV={'20':1000,'21':500}).solve_multiphonon_properties()
        self.assertAlmostEqual(r['electromagnetic_rates']['strength_ratio_20_over_21'],.1)
        self.assertAlmostEqual(r['electromagnetic_rates']['e2_partial_photon_width_ratio_20_over_21'],3.2)
        self.assertIsNone(r['is_two_phonon_confirmed'])

    def test_jensen_table_two_branches_both_retained(self):
        # Jensen2002 Fig1: common parent 45/2+, E_in=627 keV; TableII lambda=.14.
        r=be2_ratios_for_mixing_branches(e_out_keV=476,e_in_keV=627,
            photon_intensity_ratio=.14,delta_branches=[-3.6,-.19],inband_e2_fraction=1,
            common_initial_state=True,efficiency_corrected=True)
        self.assertEqual(len(r['branches']),2)
        self.assertAlmostEqual(r['branches'][0]['BE2_out_over_in'],.51,delta=.01)
        self.assertAlmostEqual(r['branches'][1]['BE2_out_over_in'],.019,delta=.001)
        self.assertIsNone(r['branch_selected'])

    def test_common_parent_and_intensity_conditions_required(self):
        args=dict(e_out_keV=476,e_in_keV=627,photon_intensity_ratio=.14,
                  delta_branches=[-3.6],inband_e2_fraction=1,
                  common_initial_state=True,efficiency_corrected=True)
        for name in ('common_initial_state','efficiency_corrected'):
            with self.assertRaises(ValueError): be2_ratios_for_mixing_branches(**dict(args,**{name:False}))

    def test_spin_reference_and_curvature_offset(self):
        # A*I(I+1)+epsilon lies epsilon-A above mean of the two adjacent yrast levels.
        i=10.5;A=10.;eps=300.;e=A*i*(i+1)+eps
        refs={i-1:A*(i-1)*i,i+1:A*(i+1)*(i+2)}
        r=yrast_referenced_excitation(i,e,refs,covariance_keV2=np.eye(3))
        self.assertAlmostEqual(r['excitation_keV'],eps-A)
        self.assertAlmostEqual(r['sigma_keV']**2,1.5)
        r=yrast_referenced_excitation(i,e,{i:A*i*(i+1)},same_signature=True)
        self.assertEqual(r['excitation_keV'],eps)

    def test_missing_neighbour_no_extrapolation(self):
        r=yrast_referenced_excitation(10.5,1000,{9.5:600})
        self.assertIsNone(r['excitation_keV'])
        self.assertEqual(r['missing_reference_spins'],[11.5])

    def test_invalid_parameters_and_unordered_truncation(self):
        for kw in ({'hbar_omega_w_keV':0},{'spin':10.3},{'g4_anharmonicity_keV':float('nan')}):
            with self.assertRaises(ValueError): MultiphononWobblingSolver(**kw)
        with self.assertRaises(ValueError): MultiphononWobblingSolver(g4_anharmonicity_keV=-200).solve_multiphonon_properties()
        with self.assertRaises(ValueError): yrast_referenced_excitation(5,100,{4:50,6:70},covariance_keV2=np.eye(2))
        with self.assertRaises(ValueError): e2_photon_width_ratio(.1,0,1000,500)

    def test_old_audit_no_fixed_windows_or_fabricated_strengths(self):
        for e2 in (300,600,1500):
            r=audit_multiphonon_wobbling_candidate(0,320,e2)
            self.assertIsNone(r['physical_assignment']);self.assertIsNone(r['score'])
            self.assertIsNone(r['energy_ratio_R21'])
            self.assertIsNone(r['be2_ratio_stepover'])
        r=audit_multiphonon_wobbling_candidate(0,320,600,reference_is_common=True)
        self.assertEqual(r['energy_ratio_R21'],1.875)
        self.assertIsNone(r['physical_assignment'])

    def test_energy_ansatz_parameter_conversion(self):
        old=evaluate_multiphonon_wobbling_energies(280,-70)
        new=MultiphononWobblingSolver().solve_multiphonon_properties()
        self.assertAlmostEqual(old['two_phonon_energy_E2_keV'],new['excitation_energies_keV']['n_w_2'])
        self.assertAlmostEqual(old['anharmonicity_parameter_A'],new['energy_ratio_R21']/2-1)

    def test_all_legacy_presets_are_explicitly_synthetic(self):
        for name,p in PRESETS.items():
            self.assertIn('synthetic',p['nucleus'].lower())


if __name__=='__main__': unittest.main()
