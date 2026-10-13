#!/usr/bin/env python3
"""Day13 synthetic pair-selection and cross-event axis-anisotropy checks.

The first fixture uses smooth user-chosen pair acceptance and full-sphere
geometry to demonstrate why multiplying single efficiencies can miss joint
tracking losses. No real tracking code, detector geometry or events are used.
The second draws independent photons with a common beam-axis marginal
q(n)=1+A2*P2(n.z), showing an angle correlation from shared anisotropy despite
independent draws. This is not a real cascade/alignment or delta extraction.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss, legval


def p2(x):
    return (3*np.asarray(x)**2-1)/2


def p4(x):
    return (35*np.asarray(x)**4-30*np.asarray(x)**2+3)/8


def pair_acceptance(u):
    # Deliberately smooth and positive, so inverse normalization is defined.
    # Real angular holes cannot be restored by division alone.
    return 1-.60*np.exp(-.5*((np.asarray(u)-.90)/.08)**2)-.25*np.exp(-.5*((np.asarray(u)+.85)/.06)**2)


def shape_coefficients(u, w, observed):
    design=np.column_stack((np.ones_like(u),p2(u),p4(u)))
    coef=np.linalg.lstsq(design*np.sqrt(w[:,None]),observed*np.sqrt(w),rcond=None)[0]
    return {'scale':float(coef[0]),'a2':float(coef[1]/coef[0]),'a4':float(coef[2]/coef[0])}


def axis_photons(rng, count, a2):
    # Rejection sample the polar density (1+A2P2)/2, with uniform azimuth.
    accepted=[];size=0
    envelope=max(1+a2,1-a2/2)
    while size<count:
        candidates=rng.uniform(-1,1,count)
        keep=rng.uniform(0,envelope,count)<1+a2*p2(candidates)
        block=candidates[keep];accepted.append(block);size+=len(block)
    z=np.concatenate(accepted)[:count];phi=rng.uniform(0,2*math.pi,count)
    return np.column_stack((np.sqrt(1-z*z)*np.cos(phi),np.sqrt(1-z*z)*np.sin(phi),z))


def calculate():
    # Known source-correlation central coefficients are taken as an example
    # scale from LG20-11; response is entirely self-chosen.
    a2,a4=.102,.0091
    u,w=leggauss(256);true=1+a2*p2(u)+a4*p4(u);selected=true*pair_acceptance(u)
    after=shape_coefficients(u,w,selected)
    before=shape_coefficients(u,w,selected/pair_acceptance(u))
    u2,w2=leggauss(512);selected2=(1+a2*p2(u2)+a4*p4(u2))*pair_acceptance(u2)
    after2=shape_coefficients(u2,w2,selected2)
    assert abs(before['a2']-a2)<1e-12 and abs(before['a4']-a4)<1e-12
    assert abs(after['a2']-after2['a2'])<1e-10 and abs(after['a4']-after2['a4'])<1e-10
    assert abs(after['a2']-a2)>.1
    # Addition theorem: independent axial marginals with coefficient A2 give
    # g(u)=(1+A2^2/5 P2(u))/2 after integrating the absolute orientations.
    rng=np.random.default_rng(131017);samples=500000;beam_a2=1.
    first=axis_photons(rng,samples,beam_a2);second=axis_photons(rng,samples,beam_a2)
    cos_pair=np.einsum('ij,ij->i',first,second)
    pair_a2_MC=5*float(np.mean(p2(cos_pair)))
    pair_a4_MC=9*float(np.mean(p4(cos_pair)))
    expected=beam_a2*beam_a2/5
    standard_error_a2=5*float(np.std(p2(cos_pair)))/math.sqrt(samples)
    standard_error_a4=9*float(np.std(p4(cos_pair)))/math.sqrt(samples)
    assert abs(pair_a2_MC-expected)<4*standard_error_a2
    assert abs(pair_a4_MC)<4*standard_error_a4
    # Independently integrate over both polar angles and relative azimuth,
    # without using the analytic pair-density formula.
    z,zw=leggauss(48);phi=(np.arange(256)+.5)*(2*math.pi/256)
    means2=0.;means4=0.
    for i,z1 in enumerate(z):
        for j,z2 in enumerate(z):
            relative=z1*z2+math.sqrt(1-z1*z1)*math.sqrt(1-z2*z2)*np.cos(phi)
            weight=zw[i]*zw[j]*(1+beam_a2*p2(z1))*(1+beam_a2*p2(z2))/4
            means2+=weight*float(np.mean(p2(relative)))
            means4+=weight*float(np.mean(p4(relative)))
    exact_a2=5*means2;exact_a4=9*means4
    assert abs(exact_a2-expected)<1e-12 and abs(exact_a4)<1e-12
    # If an isotropic desired angular shape is divided by this aligned mixed
    # normalizer, a spurious residual emerges. This is a separate fixture,
    # not a derivation of a specific real in-beam cascade normalization.
    distorted=shape_coefficients(u,w,1/(1+expected*p2(u)))
    zero_pair=shape_coefficients(u,w,true)
    assert abs(zero_pair['a2']-a2)<1e-12
    assert abs(distorted['a2'])>.15
    return {'schema_version':1,'kind':'synthetic joint-acceptance and independent-axis-photon exercise',
            'source_scale_boundary':'LG20-11 central theoretical source coefficients supply scale only; all response choices and beam A2 are self-chosen',
            'pair_response_fixture':{'true_a2':a2,'true_a4':a4,'after_tracking_product_normalizer_fit':after,
                                     'before_tracking_matching_joint_normalizer_fit':before,
                                     'pair_acceptance_min':float(np.min(pair_acceptance(u))),
                                     'boundary':'full-sphere geometry; before/after are response-level fixtures, not replay of actual OFT'},
            'independent_beam_axis_fixture':{'self_chosen_single_photon_A2':beam_a2,'sample_size':samples,
                                            'predicted_pair_a2':expected,'quadrature_pair_a2':exact_a2,
                                            'quadrature_pair_a4':exact_a4,'MC_pair_a2':pair_a2_MC,
                                            'MC_a2_standard_error':standard_error_a2,'MC_pair_a4':pair_a4_MC,
                                            'MC_a4_standard_error':standard_error_a4,
                                            'isotropic_fixture_divided_by_aligned_normalizer_fit':distorted},
            'verification':{'correct_joint_response_recovers_coefficients':True,'quadrature256_512_converged':True,
                            'addition_theorem_checked_by_orientation_integral_and_MC':True,
                            'zero_pair_response_limit_passed':True,'passed':True},
            'boundaries':['Not real detector geometry, event replay, alignment, spin assignment or mixing ratio.',
                          'Zero-acceptance angular bins cannot be restored by division.',
                          'A reused mixed-event histogram and same-source calibrations generate shared statistical/systematic covariance.'],
            'numpy_version':np.__version__}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    result=calculate();args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output),'verification':result['verification'],
                     'joint_fixture':result['pair_response_fixture'],
                     'axis_fixture':result['independent_beam_axis_fixture']}))


if __name__=='__main__':
    main()
