#!/usr/bin/env python3
"""KO01's 3->2->0 example as a phase-defined two-shape-observable check.

The ratios derived from printed calculated coefficients are not measured counts
or a digitization of Fig2's confidence bands. No experimental covariance is made.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_d96_eq4_erratum_audit import coefficient
from day16_kf89_w178_gate_audit import gram, roots, value, finite_delta, preimage, intersection


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);a=p.parse_args();cfg=json.loads(a.input.read_text())
    assert cfg['identity']=='DAY16-KO01-THREE-ANGLE-1003-01'
    spins=tuple(cfg['spins']);pop=np.ones(7)/7;reference=(("E",2,1.),)
    angles=np.array([0.,45.,90.]);xs=np.cos(np.deg2rad(angles))
    leg=np.column_stack([np.polynomial.legendre.legval(xs,[0.]*k+[1.]) for k in (0,2,4)])
    # Reconstruct each coefficient's 2x2 form through exact homogeneous probes.
    forms=[]
    for angle in angles:forms.append(16*math.pi**2*gram(spins,pop,reference,[0.,float(angle),0.]))
    raw=np.array(forms);matrices=np.einsum('ij,jkl->ikl',np.linalg.inv(leg),raw)
    assert np.max(abs(matrices[0]-np.eye(2)))<1e-12
    comparisons=[]
    for d in [0.,.3,-.3,1.,4.5,-4.5]:
        parts=(("M",1,1.),("E",2,d));v=np.array([1.,d])/math.hypot(1.,d)
        observed=np.array([v@m@v for m in matrices])
        expected=np.array([coefficient(3,2,parts,k,0,k,False)*coefficient(2,0,reference,0,k,k,False)
                           for k in (0,2,4)])
        assert np.max(abs(observed-expected))<1e-12
        comparisons.append(float(np.max(abs(observed-expected))))
    d=-cfg['source_delta_RB'][0];alpha=math.atan(d);modelcoef=[value(m,alpha) for m in matrices]
    sourcecoef=np.array([1.,cfg['source_example_coefficients_calculated']['A2'],
                        cfg['source_example_coefficients_calculated']['A4']])
    # A mismatch is retained rather than requiring source/model exact agreement.
    diagnostics=[];openings=cfg['angles_opening_deg']
    def harmonic(theta):
        x=math.cos(math.radians(theta))
        return np.array([np.polynomial.legendre.legval(x,[0.]*k+[1.]) for k in (0,2,4)])
    geom=np.array([harmonic(t) for t in openings]);sourceW=geom@sourcecoef
    assert min(sourceW)>0
    R180,R55=sourceW[0]/sourceW[1],sourceW[2]/sourceW[1]
    # First ratio alone permits two roots within this fixed point forward model.
    n180=np.einsum('i,ijk->jk',geom[0],matrices)
    denominator=np.einsum('i,ijk->jk',geom[1],matrices)
    n55=np.einsum('i,ijk->jk',geom[2],matrices)
    for x in roots(n180-R180*denominator):
        diagnostics.append({'d_D96':finite_delta(x),'d_RB':-math.tan(x),
                            'R180_from_printed_coefficient_witness':value(n180,x)/value(denominator,x),
                            'R55_model_prediction':value(n55,x)/value(denominator,x),
                            'R55_witness_difference':value(n55,x)/value(denominator,x)-R55})
    # The two exact shape ratios recover normalized angular coefficients.
    H=np.array([geom[0,1:]-R180*geom[1,1:],geom[2,1:]-R55*geom[1,1:]])
    recovered=np.linalg.solve(H,np.array([R180-1,R55-1]))
    assert np.max(abs(recovered-sourcecoef[1:]))<1e-13
    # For fixed pureE2 reference, rank4 has no M1 or interference term.
    assert np.max(abs(matrices[2,:1,:]))<1e-12 and np.max(abs(matrices[2,:,:1]))<1e-12
    q=sourcecoef[2]/matrices[2,1,1]
    sign_candidates=[]
    if 0<q<1:
        magnitude=math.sqrt(q/(1-q))
        for dd in [-magnitude,magnitude]:
            sign_candidates.append({'d_D96':dd,'d_RB':-dd,
                                    'A2_prediction':value(matrices[1],math.atan(dd)),
                                    'A2_witness_difference':value(matrices[1],math.atan(dd))-sourcecoef[1]})
    # Four-decimal printed calculated coefficients are not exact simultaneous data.
    rounded_preimages=[preimage(matrices[k],np.eye(2),sourcecoef[k]-.00005,
                                sourcecoef[k]+.00005) for k in (1,2)]
    rounded_joint=intersection(*rounded_preimages)
    assert any(lo<=math.degrees(alpha)<=hi for lo,hi in rounded_joint)
    # Jacobian for (X180/X90, X55/X90), never an invented experimental Sigma.
    z,x,y=sourceW # X180,X90,X55
    J=np.array([[1/x,-z/x**2,0.],[0.,-y/x**2,1/x]])
    assert abs(J[0,1]*J[1,1]-R180*R55/x**2)<1e-12
    result={'identity':cfg['identity'],'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'A0_A2_A4_quadratic_matrices_D96':matrices.tolist(),
            'sourceF_vs_photon_max_coefficient_error':max(comparisons),
            'source_RB_delta_central':cfg['source_delta_RB'][0],
            'point_model_coefficients_at_source_mapped_central':modelcoef,
            'authors_printed_calculated_coefficients':sourcecoef.tolist(),
            'point_minus_printed_coefficients':(np.array(modelcoef)-sourcecoef).tolist(),
            'computed_shape_witness':{'W180_W90_W55':sourceW.tolist(),'R180':R180,'R55':R55,
                                      'measured_counts_or_fitbands':False},
            'single_ratio_all_roots':diagnostics,'two_ratio_linear_inversion':{
                'H':H.tolist(),'determinant':float(np.linalg.det(H)),
                'recovered_A2_A4':recovered.tolist()},
            'rank4_then_rank2_sign_check':sign_candidates,
            'printed_calculation_rounding_box':{'half_last_digit':.00005,
                 'atan_d_D96_degrees_preimage':rounded_joint,
                 'mapped_source_central_d_inside':True,
                 'confidence_level':None,'kind':'printing precision, not experimental uncertainty'},
            'ratio_jacobian_at_computed_witness':J.tolist(),
            'independent_count_only_crosscov_formula':'Cov(R180,R55) = R180*R55*Var(X90)/X90^2 if all three raw yields independent; actual background/efficiency/event covariance must be added via J Sigma J^T.',
            'experimental_covariance_known':False,
            'boundary':'Fixed-path unoriented point calculation with printed author-calculated coefficients. Approximate published coefficients are not independent measured angular coefficients; no new delta, confidence or array-response replay.',
            'all_internal_checks_passed':True}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:result[k] for k in ['sourceF_vs_photon_max_coefficient_error','point_model_coefficients_at_source_mapped_central',
                                           'authors_printed_calculated_coefficients','point_minus_printed_coefficients',
                                           'computed_shape_witness','single_ratio_all_roots','rank4_then_rank2_sign_check']},ensure_ascii=False));return 0


if __name__=='__main__':raise SystemExit(main())
