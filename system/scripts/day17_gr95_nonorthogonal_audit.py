#!/usr/bin/env python3
"""GR95 actual point geometry, inverse and small-P merit audit; no new MC."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def response(q0,p,phi,phiprime):
    n=1-q0*p*math.cos(2*math.radians(phi))
    np=1-q0*p*math.cos(2*math.radians(phiprime))
    return (np-n)/(np+n)


def merit_finite(a,eff,f):
    return 4*f/((1+f)**2-(1-f*f)*a)*eff*a*a/(1-a*a)


def main():
    path=RUN/'garciaraffi1995-geometry-contract.json'
    c=json.loads(path.read_text())
    rows=[]
    for energy in c['energies_MeV']:
        r=1/(1+energy/.51099895)
        q0=r/(r*r-r+1)
        q1=-q0/4;q2=3*q0/4
        sample=[]
        for p in c['P_grid']:
            a=response(q0,p,0,60)
            direct_formula=q2*p/(1+q1*p)
            assert abs(a-direct_formula)<1e-14
            inverse=a/(q2*(1+a/3))
            assert abs(inverse-p)<1e-14
            assert abs(response(q0,p,0,90)-q0*p)<1e-14
            assert abs(response(q0,p,45,135))<1e-14
            assert abs(response(q0,p,60,0)+a)<1e-14
            assert abs(response(q0,0,0,60))<1e-14
            ao=q0*p
            ratio=None if p==0 else merit_finite(a,3,2)/merit_finite(ao,1,1)
            sample.append({'P':p,'A':a,'inverse_P':inverse,
                           'incorrect_linear_P_AoverQ':a/q2,
                           'finite_A_merit_ratio_nonorth_over_rotated':ratio})
        # Two distinct nonzero known P values identify Q1/Q2; one does not.
        p1,p2=-.5,.5
        a1,a2=response(q0,p1,0,60),response(q0,p2,0,60)
        y1,y2=p1/a1,p2/a2
        slope=(y2-y1)/(p2-p1)
        intercept=y1-slope*p1
        recovered_q2=1/intercept;recovered_q1=slope/intercept
        assert abs(recovered_q1-q1)<1e-14 and abs(recovered_q2-q2)<1e-14
        # Alternative extended-channel kernels: still positive/normalized,
        # but the point alpha=-1/3 is no longer imposed by the direction labels.
        k0=.8*q0;k60=-.3*q0
        ext_q1=-(k0+k60)/2;ext_q2=(k0-k60)/2
        rows.append({'energy_MeV':energy,'point_Q0':q0,'point_Q1':q1,'point_Q2':q2,
                     'point_Q3':0,'alpha_point':-1/3,'samples':sample,
                     'two_known_P_recovery_Q1_Q2':[recovered_q1,recovered_q2],
                     'declared_alternative_extended_kernels':{
                         'k0':k0,'k60':k60,'alpha_effective':ext_q1/ext_q2,
                         'boundary':'conditional response countercontrol, not actual CLUSTER prediction'}})
    small=3*(3/4)**2*(8/9)
    assert abs(small-1.5)<1e-14
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'point_geometry_results':rows,
            'uncorrected_efficiency_only_null_offset_for_f2':(2-1)/(2+1),
            'simple_source_smallP_merit_ratio':small,
            'source_pair_groups':{'phi0':c['adjacent_pairs_phi0'],'phi60or120':c['adjacent_pairs_phi60_or120']},
            'inverse_orthogonal_zero_labelswap_null_controls':True,
            'normalized_point_Q3_zero_not_generic_geometry_offset':True,
            'extended_alpha_is_a_response_contract_not_guaranteed_by_angle_labels':True,
            'not_actual_POL_Geant3_replay_or_experimental_merit':True,
            'no_new_P_Q_counts_or_CI':True,'ok':True}
    (RUN/'garciaraffi1995-geometry-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
