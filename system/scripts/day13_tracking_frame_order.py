#!/usr/bin/env python3
"""Day13 exact free-electron fixture for tracking/Doppler order.

Compton tracking uses calibrated detector-lab energies/angles and an electron
at rest approximation. Premultiplying detector deposits by an emitter inverse
Doppler factor does not preserve that relation. Full Lorentz transformations
do preserve the scattering when the electron four-vector is transformed too.
This is not an AGATA/GRETINA production replay or code-error claim.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


ME_KEV=510.99895069


def boost_z(p4,beta):
    gamma=1/math.sqrt(1-beta*beta)
    return np.array([gamma*(p4[0]+beta*p4[3]),p4[1],p4[2],gamma*(p4[3]+beta*p4[0])])


def minkowski(a,b):
    return float(a[0]*b[0]-a[1:]@b[1:])


def calculate():
    incoming=1000.;scattering_cos=-.9
    scattered=incoming/(1+incoming/ME_KEV*(1-scattering_cos))
    first_deposit=incoming-scattered;second_deposit=scattered
    photon_in=np.array([incoming,0.,0.,incoming])
    photon_out=np.array([scattered,scattered*math.sqrt(1-scattering_cos**2),0.,scattered*scattering_cos])
    electron_in=np.array([ME_KEV,0.,0.,0.]);electron_out=electron_in+photon_in-photon_out
    assert abs(minkowski(electron_out,electron_out)-ME_KEV**2)<1e-6
    true_cos=1-ME_KEV*(1/second_deposit-1/(first_deposit+second_deposit))
    assert abs(true_cos-scattering_cos)<1e-12
    cases=[];max_invariant_residual=0.
    for emitter_beta in (0.,.07,.3):
        # Incoming lab photon is parallel to emitter velocity in this fixture.
        gamma=1/math.sqrt(1-emitter_beta**2)
        factor=gamma*(1-emitter_beta)
        naive_first=factor*first_deposit;naive_second=factor*second_deposit
        naive_cos=1-ME_KEV*(1/naive_second-1/(naive_first+naive_second))
        wrong_formula=1-(1-scattering_cos)/factor
        assert abs(naive_cos-wrong_formula)<1e-12
        ki=boost_z(photon_in,-emitter_beta);kf=boost_z(photon_out,-emitter_beta)
        pi=boost_z(electron_in,-emitter_beta);pf=boost_z(electron_out,-emitter_beta)
        residual=abs(minkowski(pi,ki)-minkowski(pi,kf)-minkowski(ki,kf))
        max_invariant_residual=max(max_invariant_residual,residual)
        assert np.max(np.abs(pi+ki-pf-kf))<1e-9
        assert abs(minkowski(pf,pf)-ME_KEV**2)<1e-6
        corrected_total=factor*(first_deposit+second_deposit)
        assert abs(corrected_total-ki[0])<1e-10
        cases.append({'emitter_beta':emitter_beta,'incoming_inverse_Doppler_factor':factor,
                      'correct_rest_incoming_gamma_keV':float(ki[0]),
                      'sum_of_naively_prescaled_deposits_keV':corrected_total,
                      'naive_Compton_cos_using_prescaled_deposits_and_lab_angle':naive_cos,
                      'naive_cos_is_physical':-1<=naive_cos<=1,
                      'transformed_initial_electron_energy_keV':float(pi[0]),
                      'transformed_initial_electron_pz_keV_per_c':float(pi[3]),
                      'full_scattering_invariant_residual_keV2':residual})
    assert cases[0]['naive_cos_is_physical']
    assert not cases[1]['naive_cos_is_physical'] and not cases[2]['naive_cos_is_physical']
    assert max_invariant_residual<1e-7
    return {'schema_version':1,'kind':'exact free-electron scattering/boost fixture; no production tracking replay',
            'detector_lab_fixture':{'incoming_gamma_keV':incoming,'scattering_cos':scattering_cos,
                                    'scattering_angle_deg':math.degrees(math.acos(scattering_cos)),
                                    'first_deposit_keV':first_deposit,'second_deposit_keV':second_deposit,
                                    'correct_lab_Compton_cos':true_cos},
            'cases':cases,'verification':{'free_electron_mass_shell_passed':True,
                                         'calibrated_lab_Compton_relation_passed':True,
                                         'noncommuting_prescaling_counterexample_passed':True,
                                         'complete_boost_conserves_four_momentum':True,
                                         'max_full_invariant_residual_keV2':max_invariant_residual,
                                         'static_order_limit_passed':True,'passed':True},
            'boundaries':['Electron binding/momentum spread, finite deposit range, detector materials and escape losses are absent.',
                          'The corrected incoming total energy alone can be right while the prescaled Compton classification is wrong.',
                          'Ancillary source/vertex information can enter tracking without changing the detector-frame energy convention.',
                          'No actual source pipeline is accused of prescaling or of a wrong FOM.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],
                     'naive_cosines':[c['naive_Compton_cos_using_prescaled_deposits_and_lab_angle'] for c in r['cases']]}))


if __name__=='__main__':
    main()
