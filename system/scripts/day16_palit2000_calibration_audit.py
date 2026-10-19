#!/usr/bin/env python3
"""Palit2000 printed calibration and literal KN contract, without event refitting."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import sympy as sp


def sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main()->None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();cfg=json.loads(args.contract.read_text());assert cfg['identity']=='P00-CLOVER-CALIBRATION-REFERENCE-01'
    assert sha(Path(cfg['source_PDF']))==cfg['source_sha256']
    v=cfg['source_inputs'];E=v['target_E_keV'];me=v['me_keV'];eps=E/me
    q0=(eps+1)/(eps*eps+eps+1)
    attenuation=v['C_per_keV']*E+v['D'];q=attenuation*q0
    P=v['target_Delta']/q;sigma_from_delta_only=v['sigma_target_Delta']/q
    CMeV=v['C_per_keV']*1000
    q_units=(CMeV*(E/1000)+v['D'])*q0;assert abs(q_units-q)<1e-14
    wrong_units=(v['C_per_keV']*(E/1000)+v['D'])*q0
    independent_sigma_q=q0*math.hypot(E*v['sigma_C_per_keV'],v['sigma_D'])
    minimum_sigma_q=q0*abs(E*v['sigma_C_per_keV']-v['sigma_D'])
    maximum_sigma_q=q0*(abs(E*v['sigma_C_per_keV'])+v['sigma_D'])
    assert minimum_sigma_q<=independent_sigma_q<=maximum_sigma_q
    a2=v['target_a2'];a4=v['target_a4'];H4=-1/6
    numerator=3*a2*v['H2_puredipole']-7.5*a4*H4
    denominator=2-a2+.75*a4
    pureM=numerator/denominator;pureE=-pureM
    assert pureM<0<pureE
    # Literal Eq5 and correct KN both give identical point sensitivity when
    # their common prefactor cancels between azimuths at fixed scatter angle.
    r,s=sp.symbols('r s',positive=True)
    B=1/r+r
    correct0=r*r*(B-2*s);correct90=r*r*B
    literal0=(B-2*s)/(r*r);literal90=B/(r*r)
    qcorrect=sp.factor((correct90-correct0)/(correct90+correct0))
    qliteral=sp.factor((literal90-literal0)/(literal90+literal0))
    assert sp.simplify(qcorrect-qliteral)==0
    alpha=sp.symbols('alpha',positive=True)
    q90=sp.factor(qcorrect.subs({s:1,r:1/(1+alpha)}))
    assert sp.simplify(q90-(alpha+1)/(alpha**2+alpha+1))==0
    zero_energy_keV=-v['D']/v['C_per_keV']
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'source_sha256':cfg['source_sha256'],'contract_sha256':sha(args.contract),
        'source1117_calibration':{'Q0':q0,'CEplusD':attenuation,'Qfit':q,
            'P_Delta_over_Q':P,'source_P':v['reported_P'],'sigma_Delta_only':sigma_from_delta_only,
            'source_sigma_P':v['reported_sigma_P'],'sigma_residual':sigma_from_delta_only-v['reported_sigma_P'],
            'full_sigma_or_Cov_budget_recovered':False},
        'units':{'C_per_keV':v['C_per_keV'],'C_per_MeV':CMeV,
            'correct_keV_MeV_match':True,'wrong_mixedunits_Q':wrong_units,
            'Qfit_zero_if_invalid_global_extrapolation_keV':zero_energy_keV,
            'fit_range_keV':v['Q_calibration_range_keV']},
        'fitCov_CD_conditional':{'sigmaQ_ifCov0':independent_sigma_q,
            'sigmaQ_min_possible_given_two_marginals':minimum_sigma_q,
            'sigmaQ_max_possible_given_two_marginals':maximum_sigma_q,
            'missing_Cov_CD':True,'not_total_Q_error':True},
        'Eq3_pure_dipole_probe_given_printed_a2_a4':{'H2':1,'H4':'-1/6',
            'M1_Pcal':pureM,'E1_Pcal':pureE,'not_full_delta_branch_fit':True},
        'literal_Eq5_boundary':{'common_prefactor_ratio_wrong_over_correct':'r^-4',
            'fixed_angle_Q0_unchanged':True,'Q90_expression':str(q90),
            'at1117_and90_ratio':(1+eps)**4,
            'implication':'Angle-dependent weights differ; actual producer/calibration not inferred wrong'},
        'source1117_delta':{'reported_E1M2_delta':v['reported_delta_E1M2'],
            'reported_sigma':v['reported_sigma_delta'],'remeasured_here':False},
        'independence_and_companion':{'Eu_a_not_Q':True,
            'Na24_actual_direction_tag_acceptance_not_recovered':True,
            'unconditional_source_single_gamma_P0_does_not_set_actual_tagged_P':True,
            'P00_Q_coefficients_not_Garg2015_response':True,
            'no_toy_counts_or_newexperimental_fit':True}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['source1117_calibration','units','fitCov_CD_conditional','Eq3_pure_dipole_probe_given_printed_a2_a4']},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
