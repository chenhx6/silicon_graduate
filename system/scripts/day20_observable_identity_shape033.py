#!/usr/bin/env python3
"""Selected original-source ledger and explicitly declared shape-model controls.

No source producer, original fit, confidence interval or nuclear mode is inferred.
The axial surface model below is a separate mathematical exercise, not the
parameterization attributed to Petrache1998 or a fit of Ionescu-Bujor1998.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss, legval


def prefactor(z, a, radius):
    return 3*z*(radius*a**(1/3))**2/(100*math.sqrt(5*math.pi))


def invert_quadratic(q, z=58, a=131, radius=1.2, c22=.36):
    u = q/prefactor(z, a, radius)
    return 2*u/(1+math.sqrt(1+4*c22*u))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--run-dir', type=Path, required=True)
    args = parser.parse_args()
    checks = []

    def check(name, ok):
        if not ok:
            raise AssertionError(name)
        checks.append(name)

    ledger = json.loads((args.run_dir/'singh-table-ledger-001.json').read_text())
    finite = [r for r in ledger['case_Ce131']['rows'] if r['Qt']['kind']=='finite']
    q = np.array([r['Qt']['value'] for r in finite])
    error = np.array([(r['Qt']['minus']+r['Qt']['plus'])/2 for r in finite])
    weighted_mean = float(np.sum(q/error**2)/np.sum(1/error**2))
    # A constant-model diagnostic, not an independently measured state.
    mean_se = float(1/math.sqrt(np.sum(error**-2)))
    k_geometry_ratio = math.sqrt(169/114)
    candidate_q = 2.72/k_geometry_ratio
    ratio_central = 1.32/.92
    independent_ratio_error = ratio_central*math.hypot(.13/1.32,.10/.92)
    frequency_ratio = 52.6/36.4
    independent_frequency_error = frequency_ratio*math.hypot(1.4/52.6,1.6/36.4)
    qs_examples = []
    spin = Fraction(9,2)
    for k in [Fraction(1,2),Fraction(9,2)]:
        factor = (3*k*k-spin*(spin+1))/((spin+1)*(2*spin+3))
        qs_examples.append({'declared_I':str(spin),'declared_K':str(k),
                            'axial_pure_K_Qs_over_Q0':str(factor),
                            'absolute_Q0_if_abs_Qs_0p92_eb':.92/abs(float(factor))})
    check('pure K axial factor counterexamples', qs_examples[0]['axial_pure_K_Qs_over_Q0']=='-4/11' and qs_examples[1]['axial_pure_K_Qs_over_Q0']=='6/11')
    check('absolute moment uncertainty independence does not reproduce source ratio precision', independent_ratio_error>.19 and independent_frequency_error<.08)

    # Charge-conserving uniform sharp axial surface: R=cR0(1+b2Y20+b4Y40).
    # rho=3Ze/(4pi R0^3); c chosen for fixed volume, Y normalized to unity.
    x, w = leggauss(96)
    y2 = math.sqrt(5/(4*math.pi))*legval(x,[0,0,1])
    y4 = math.sqrt(9/(4*math.pi))*legval(x,[0,0,0,0,1])
    integrate = lambda v: float(2*math.pi*np.dot(w,v))
    gaunt = [integrate(y2**3),integrate(y2*y2*y4),integrate(y2*y4*y4)]
    measured = [2*gaunt[0],4*gaunt[1],2*gaunt[2]]
    closed = [2/7*math.sqrt(5/math.pi),12/(7*math.sqrt(math.pi)),20/77*math.sqrt(5/math.pi)]
    check('three Gaunt coefficients from independent quadrature', np.allclose(measured,closed,rtol=1e-11,atol=1e-12))
    check('harmonic normalization', np.isclose(integrate(y2*y2),1) and np.isclose(integrate(y4*y4),1) and abs(integrate(y2*y4))<1e-12)

    def exact_surface(b2,b4):
        f = 1+b2*y2+b4*y4
        if np.min(f)<=0:
            raise ValueError('nonpositive radial surface')
        cvolume = (integrate(f**3)/(4*math.pi))**(-1/3)
        return cvolume**5*integrate(f**5*y2)/5

    c22,c24,c44 = closed
    approx = lambda b2,b4: b2+c22*b2*b2+c24*b2*b4+c44*b4*b4
    expansion = []
    for eps in [.1,.05,.025]:
        b2,b4 = .35*eps,-.03*eps
        exact = exact_surface(b2,b4)
        expansion.append({'scale':eps,'exact_dimensionless_Q':exact,'second_order':approx(b2,b4),'absolute_remainder':abs(exact-approx(b2,b4))})
    remainder_ratio = expansion[0]['absolute_remainder']/expansion[1]['absolute_remainder']
    check('second order truncation has cubic leading remainder', 7<remainder_ratio<9)
    examples = []
    for b4 in [0,-.03,.03]:
        b2=.35
        exact = exact_surface(b2,b4)
        second = approx(b2,b4)
        examples.append({'chosen_beta2':b2,'chosen_beta4':b4,
                         'Q_exact_eb_if_Z58_A131_r0_1p2':prefactor(58,131,1.2)*exact,
                         'Q_second_order_eb':prefactor(58,131,1.2)*second,
                         'beta2_inverted_if_beta4_omitted_second_order':2*second/(1+math.sqrt(1+4*c22*second))})
    radius_ratio = (1.25/1.2)**2
    b120=invert_quadratic(7.3,radius=1.2)
    b125=invert_quadratic(7.3,radius=1.25)
    check('fixed Q quadratic beta ratio differs from inverse r squared', abs(b125/b120-1/radius_ratio)>1e-3)

    # Standard energy finite differences require ordered same-band transitions.
    spectra = {}
    for name,spins,energies in [('131Ce_nd',[7.5,9.5,11.5,13.5,15.5,17.5,19.5],[510,642,750,827,892,922,962]),('134Nd_gsb',[2,4,6,8],[294,495,631,706])]:
        spectra[name]={'spin_upper':spins,'printed_Egamma_keV':energies,
                       'effective_J1_hbar2_per_MeV':[(2*i-1)/(e/1000) for i,e in zip(spins,energies)],
                       'effective_J2_between_consecutive_entries':[4/((energies[i+1]-energies[i])/1000) for i in range(len(energies)-1)],
                       'boundary':'Printed central energies only; stencil-dependent derived quantities, no uncertainty or pairing inference. Not HD sequences.'}
    inertia=40.0
    spins=np.array([2,4,6,8],float)
    levels=spins*(spins+1)/(2*inertia)
    lower=(spins-2)*(spins-1)/(2*inertia)
    eg=levels-lower
    check('energy differences recover chosen exact rotor inertia', np.allclose((2*spins-1)/eg,inertia) and np.allclose(4/np.diff(eg),inertia))
    omega=np.array([.2,.4,.6]);aligned=5.;jr=40.
    j1=jr+aligned/omega;j2=j1+omega*(-aligned/omega**2)
    check('flat J2 need not imply flat J1', np.allclose(j2,jr) and np.ptp(j1)>10)
    output={'checkpoint':'033','kind':'original observable identity repair and conditional shape controls','experimental_fit_or_CI':False,
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'Li_Singh_crosswalk':{'Li2004_publication':'Chinese Physics Letters21,461–463; not PRC69,064320',
                                  'same_spin': '27/2-','Egamma_keV':827,'Li_tau_ps':1.23,'Li_tau_error_ps':.23,
                                  'Li_original_Qt_eb':2.72,'Li_Qt_error_eb':.25,
                                  'Singh_Present_tau_ps':1.25,'Singh_method':'DSAM','Singh_Ref32_reused_tau_ps':1.23,
                                  'Singh_Ref32_recalculated_Qt_eb':2.28,'Singh_Qt_error_eb':.21,
                                  'pure_K_candidate_ratio':k_geometry_ratio,'candidate_K_transformed_Li_Qt_eb':candidate_q,
                                  'candidate_K_transformed_Li_error_eb':.25/k_geometry_ratio,
                                  'boundary':'Candidate geometry, not author K identification, exact producer, 100% attribution or independent-technique validation.'},
            'static_transition_boundary':{'source_absolute_Q129_Q131_eb':[1.32,.92],'source_absolute_error_eb':[.13,.10],
                                          'source_EFG_free_ratio':1.44,'source_ratio_error':.07,
                                          'central_abs_Q_ratio':ratio_central,'ratio_se_if_abs_Q_errors_independent':independent_ratio_error,
                                          'source_frequencies_MHz':[52.6,36.4],'frequency_ratio':frequency_ratio,'se_if_frequencies_independent':independent_frequency_error,
                                          'source_PTR_Qcal_131_eb':[.91,.93],'source_PTR_epsilon2':[.14,.18],
                                          'conditional_pure_K_examples':qs_examples,'task_weighted_constant_Qt_mean_eb':weighted_mean,'task_conditional_mean_se_eb':mean_se,
                                          'boundary':'Measured absolute Qs lacks sign; common EFG covariance, state, K mixing, triaxial geometry and epsilon/beta convention matter. Weighted mean not a directly measured RDM Qt. No inferred isotope beta drop.'},
            'uniform_axial_surface_model':{'definitions':'R=cR0[1+b2Y20+b4Y40], c enforces volume; uniform charge; spherical harmonics norm1',
                                          'second_order_coefficients':dict(zip(['c22','c24','c44'],closed)),
                                          'expansion_remainders':expansion,'declared_examples':examples,
                                          'radius_squared_ratio':radius_ratio,'fixed_Q7p3_beta_if_Singh_Eq4_r1p2':b120,'fixed_Q7p3_beta_if_r1p25':b125,
                                          'boundary':'Model-derived sensitivity, not Petrache1998 parameter attribution or measured beta4. Higher-order/volume terms not negligible by declaration alone.'},
            'Petrache1998_literal_beta2':{'134Nd_yrast_HD':.35,'131Ce_yrast_HD':.38,'132Ce_yrast_HD':.38,'source_assumption':'no triaxiality; no uniquely specified r0/expansion in article'},
            'ordered_energy_controls':spectra,'flat_J2_counterexample':{'omega':omega.tolist(),'J1':j1.tolist(),'J2':j2.tolist(),'chosen_alignment':aligned,'boundary':'Continuum aligned-spin model; not a pairing model or nuclear measurement'},
            'controls':checks,'certification_scope':'Only declared algebra/input and original locators; no universal mode or precision certification.'}
    path=args.run_dir/'observable-identity-shape-result-033.json';path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'artifact':str(path),'controls':len(checks),'mean_Qt':weighted_mean,'mean_se':mean_se,'coefficients':closed,'experimental_fit_or_CI':False}))


if __name__=='__main__':
    main()
