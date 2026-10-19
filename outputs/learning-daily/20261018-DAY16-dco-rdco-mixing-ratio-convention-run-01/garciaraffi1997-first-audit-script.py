#!/usr/bin/env python3
"""GR97 printed Table I and linear-Stokes transport controls.

Free-electron point controls are distinct from the unavailable GEANT3 detector
producer. Inferred efficiencies and time ratios are not new measurements.
"""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import numpy as np
import sympy as sp


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rotation(phi):
    co,si=math.cos(2*phi),math.sin(2*phi)
    return np.array([[1.,0.,0.],[0.,co,si],[0.,-si,co]])


def recoil(E,theta,me):
    return 1/(1+E/me*(1-math.cos(theta)))


def transfer(E,theta,me):
    r=recoil(E,theta,me);co=math.cos(theta);sn2=math.sin(theta)**2;S=r+1/r
    F=np.array([[S-sn2,-sn2,0.],[-sn2,1+co*co,0.],[0.,0.,2*co]])
    return .5*r*r*F,r


def stokes_density(p):
    I,Q,U=p
    return .5*np.array([[I+Q,U],[U,I-Q]])


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--contract',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args();c=json.loads(a.contract.read_text());assert c['identity']=='GR97-STOKES-TABLE-AND-RESPONSE-CONTRACT-01'
    root=Path(__file__).resolve().parents[2];assert sha(root/c['raw'])==c['raw_sha256']
    assert hashlib.sha256((root/c['source']).read_bytes()[:c['source_prefix_bytes']]).hexdigest()==c['source_prefix_sha256']
    # Algebraic PSD decomposition: the Thomson part is a Jones map, while
    # S-2>=0 contributes unpolarized intensity. It covers the entire input disk.
    C,S=sp.symbols('cosTheta S',real=True)
    T=sp.Matrix([[S-1+C*C,-1+C*C,0],[-1+C*C,1+C*C,0],[0,0,2*C]])
    Jones=sp.Matrix([[1+C*C,C*C-1,0],[C*C-1,1+C*C,0],[0,0,2*C]])
    assert T-Jones==sp.diag(S-2,0,0)
    phi=sp.symbols('phi',real=True)
    R=sp.Matrix([[1,0,0],[0,sp.cos(2*phi),sp.sin(2*phi)],[0,-sp.sin(2*phi),sp.cos(2*phi)]])
    vec=sp.simplify(T*R*sp.Matrix([1,1,0]))
    target=sp.Matrix([S-2*(1-C*C)*sp.cos(phi)**2,
        -2*sp.sin(phi)**2+2*C*C*sp.cos(phi)**2,-4*C*sp.sin(phi)*sp.cos(phi)])
    assert all(sp.trigsimp(x)==0 for x in vec-target)
    assert sp.trigsimp(target[1]**2+target[2]**2-4*(1-(1-C*C)*sp.cos(phi)**2)**2)==0
    I,Q,U=sp.symbols('I Q U',real=True)
    rho=sp.Matrix([[I+Q,U],[U,I-Q]])/2;J=sp.diag(C,1)
    jr=2*J*rho*J.T
    jo=sp.Matrix([sp.trace(jr),jr[0,0]-jr[1,1],2*jr[0,1]])
    assert jo==Jones*sp.Matrix([I,Q,U])
    rows=[];time_bounds=[]
    for row in c['TableI']:
        Q=row['Q'];M=row['M'];sQ=row['sigma_Q'];sM=row['sigma_M'];eps=M/Q**2
        mterm=sM/Q**2;qterm=2*M*sQ/Q**3
        rows.append(dict(row,inferred_epsilon=eps,
            sigma_epsilon_PSD_range=[abs(mterm-qterm),mterm+qterm],
            epsilon_is_algebraic_derived_not_independent_MC_measurement=True))
    for E in sorted({x['E_MeV'] for x in rows}):
        group={x['geometry']:x for x in rows if x['E_MeV']==E};ref=group['5coax']
        for kind in ['4coax','clover']:
            t=group[kind];mr=t['M']/ref['M'];assert ref['Q']>t['Q']
            lower=mr*(1-ref['Q']**2)/(1-t['Q']**2)
            assert lower>1
            time_bounds.append({'E_MeV':E,'comparison':'5coax time / '+kind+' time',
                'at_P0':mr,'at_absP1':lower,
                'monotone_decreasing_in_Psquared':True,
                'valid_only_fixed_flux_ideal_independent_counts_symmetric_no_background_no_calibrationerror':True,
                'absolute_epsilon_ratio':t['inferred_epsilon']/ref['inferred_epsilon']})
    me=c['electron_rest_MeV'];checks=[];max_binary=max_degree=max_rotation=0.;wrong_prefactors=[]
    for E in [0.,.5,1.5,4.]:
        for degree in c['angles_deg']:
            theta=math.radians(degree);tm,r=transfer(E,theta,me);co=math.cos(theta);sn2=math.sin(theta)**2;ss=r+1/r
            for azi in c['azimuth_deg']:
                ph=math.radians(azi);out=tm@rotation(ph)@np.array([1.,1.,0.])
                assert np.linalg.eigvalsh(stokes_density(out)).min()>-1e-12
                # Reference-axis changes must carry the Stokes 2phi rotation.
                alpha=math.radians(31.)
                for pol in [0.,.5,1.]:
                    p=np.array([1.,pol,0.]);pnew=rotation(alpha)@p
                    same=tm@rotation(ph-alpha)@pnew
                    original=tm@rotation(ph)@p
                    max_rotation=max(max_rotation,float(np.max(abs(same-original))))
                    assert np.linalg.eigvalsh(stokes_density(original)).min()>-1e-12
                D=1-sn2*math.cos(ph)**2
                if out[0]<1e-14:
                    assert E==0. and abs(D)<1e-12
                    checks.append({'E_MeV':E,'theta_deg':degree,'phi_deg':azi,
                        'zero_intensity_Thomson_node_degree_undefined':True});continue
                deg=math.hypot(out[1],out[2])/out[0]
                expected=2*D/(ss-2*sn2*math.cos(ph)**2)
                max_degree=max(max_degree,abs(deg-expected));assert deg<=1+1e-12
                # Eq15's pure-state mixture lies in the plane of incident
                # polarization and outgoing direction. A zero projection at
                # finite E gives an unpolarized state with no preferred axis.
                if D<1e-14:
                    assert deg<1e-12
                    expected_rho=np.eye(2)*out[0]/2
                else:
                    axis=np.array([co*math.cos(ph),-math.sin(ph)])/math.sqrt(D)
                    orth=np.array([-axis[1],axis[0]])
                    w=(1+expected)/2
                    assert 0<=w<=1+1e-12
                    expected_rho=out[0]*(w*np.outer(axis,axis)+(1-w)*np.outer(orth,orth))
                max_binary=max(max_binary,float(np.max(abs(expected_rho-stokes_density(out)))))
                if E>0 and degree==90 and azi==0:
                    wrong_prefactors.append({'E_MeV':E,'theta_deg':degree,
                        'literal_Eq13_intensity_over_Eq11_product':r**-4,
                        'normalized_polarization_cannot_detect_common_factor':True})
                checks.append({'E_MeV':E,'theta_deg':degree,'phi_deg':azi,
                    'intensity_without_re2':float(out[0]),'linear_degree':deg})
    assert max_binary<1e-12 and max_degree<1e-12 and max_rotation<1e-12
    double=[]
    for E in [.5,1.5,4.]:
        t1,r1=transfer(E,math.pi/2,me);p1=t1@np.array([1.,0.,0.]);p1/=p1[0]
        E1=E*r1;t2,_=transfer(E1,math.pi/2,me)
        a0=float((t2@p1)[0]);a90=float((t2@rotation(math.pi/2)@p1)[0])
        asym=(a0-a90)/(a0+a90)
        analyzing=lambda energy:(1+energy/me)/(1+energy/me+(energy/me)**2)
        assert abs(asym-analyzing(E)*analyzing(E1))<1e-12
        reset=t2@np.array([1.,0.,0.]);reset90=t2@rotation(math.pi/2)@np.array([1.,0.,0.])
        assert abs(reset[0]-reset90[0])<1e-12
        double.append({'initial_E_MeV':E,'E_after_first90_MeV':E1,
            'induced_first_linear_degree':float(abs(p1[1])),
            'conditional_second90_orthogonal_asymmetry':asym,
            'if_polarization_reset_second_asymmetry':0.,
            'point_control_not_GR97_40percent_or_detector_Q_reproduction':True})
    cal=c['calibration5coax'];calculation=[]
    for E in [.5,1.5]:
        e=E/me;Q0=(1+e)/(1+e+e*e);fit=Q0*(cal['a']+cal['b_perMeV']*E)
        terms=[Q0*cal['sigma_a'],Q0*E*cal['sigma_b_perMeV']]
        calculation.append({'E_MeV':E,'Q0_point90':Q0,'Qfit60keV70to110':fit,
            'calibration_sigma_PSD_range':[abs(terms[0]-terms[1]),sum(terms)],
            'TableI_Q50keV':next(x['Q'] for x in rows if x['geometry']=='5coax' and x['E_MeV']==E),
            'different_threshold_and_unspecified_TableIwindow_not_a_closure_test':True})
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(a.contract),'raw_and_old_prefix_unchanged':True,
        'symbolic_controls':{'T_times_rotation_components_match':True,
            'positive_map_Jones_plus_unpolarized_term':True,'Eq14_linear_degree_identity':True,
            'Eq13_literal_prefactor_inverse_to_Eq11':True,
            'general_numerical_positivity_does_not_detect_positive_scalar_error':True},
        'TableI_derived_rows':rows,'ideal_count_time_ratio_bounds':time_bounds,
        'max_binary_eigenmixture_density_error':max_binary,'max_degree_formula_error':max_degree,
        'max_reference_rotation_error':max_rotation,'literal_prefactor_controls':wrong_prefactors,
        'unpolarized_two_scatter_point_controls':double,'fivecoax_calibration_object_checks':calculation,
        'point_matrix_checks':checks,
        'scope':{'no_original_GCOMPOL_execution_or_full_detector_MC':True,
            'not_new_experimental_Q_delta_or_parity':True,
            'no_total_10percent_budget_or_FOM_recommendation_for_userarray':True,
            'Day17_preview_uncredited':True}}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['symbolic_controls','TableI_derived_rows','ideal_count_time_ratio_bounds',
        'literal_prefactor_controls','unpolarized_two_scatter_point_controls','fivecoax_calibration_object_checks']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
