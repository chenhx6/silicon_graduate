#!/usr/bin/env python3
"""Conditional purity/sign design for actual Rh99 same-parent branches.

Phase independent absolute-amplitude thresholds are mathematical conditions,
not measured limits on the branches or an experimental parity assignment.
"""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo
import numpy as np
import sympy as sp
from sympy.physics.wigner import clebsch_gordan, wigner_6j
from day16_rh99_population_feasibility import basis


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--contract',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args();c=json.loads(a.contract.read_text())
    assert c['identity']=='RH99-MATCHED-REFERENCE-PURITY-DESIGN-01'
    r=a.contract.parent;root=Path(__file__).resolve().parents[2]
    assert sha(r/c['base_contract'])==c['base_contract_sha256']
    assert sha(r/c['official_result'])==c['official_result_sha256']
    for p,h in c['fixed_helpers'].items():assert sha(root/p)==h
    cfg=json.loads((r/c['base_contract']).read_text());J=sp.Rational(23,2)
    qmoment=np.array([(3*float(J-i)**2-float(J*(J+1)))/float(2*J*(2*J-1)) for i in range(12)])
    answer=[];kernels={}
    for kind,jf2 in [('dipole_stretched',21),('dipole_zero',23)]:
        jf=sp.Rational(jf2,2);setting=dict(cfg,Jf2=jf2)
        K,_=basis(setting,[[1,'M'],[2,'E']]);dual,_=basis(setting,[[1,'E'],[2,'M']]);kernels[kind]=K
        assert all(np.max(abs(K[k]-dual[k]))<1e-12 for k in ['A2','A4','I90'])
        def F(L,Lp):
            return sp.simplify((-1)**(J+jf-1)*sp.sqrt((2*L+1)*(2*Lp+1)*(2*J+1))*
                clebsch_gordan(L,Lp,2,1,-1,0)*wigner_6j(L,Lp,2,J,J,jf))
        f11=F(1,1);t=sp.simplify(F(2,2)/f11);r2=sp.simplify((F(1,2)/f11)**2)
        scale=sp.Integer(1) if jf2==21 else -(2*J-1)/(J+1)
        assert np.max(abs(K['A2'][0]-float(scale)*qmoment))<1e-12
        assert np.max(abs(K['A2'][1]-float(t)*K['A2'][0]))<1e-12
        ratio_cross=float(np.dot(K['A2'][2],K['A2'][0])/np.dot(K['A2'][0],K['A2'][0]))
        assert np.max(abs(K['A2'][2]-ratio_cross*K['A2'][0]))<1e-12
        assert abs(ratio_cross**2-float(r2))<1e-12
        d=sp.symbols('d',nonnegative=True);rr=sp.sqrt(r2)
        critical=sp.simplify(1/(rr+sp.sqrt(r2-t)))
        lower=1-2*rr*d+t*d*d
        assert critical>0 and sp.simplify(lower.subs(d,critical))==0
        # Concavity or location of the quadratic minimum establishes positivity
        # for every sign/convention and |delta| below the first positive zero.
        if t>0:assert sp.simplify(critical-rr/t)<0
        assert float(lower.subs(d,critical/2))>0
        upper_fraction=sp.simplify(critical**2/(1+critical**2))
        assert np.max(abs(K['A4'][0]))<1e-12
        # Uniform q gives no rank2/rank4 for every mixing amplitude. Hence
        # a4=0 by itself cannot certify a pure dipole reference.
        uniform=np.ones(12)/12
        assert np.max(abs(K['A2']@uniform))<1e-12
        assert np.max(abs(K['A4']@uniform))<1e-12
        answer.append({'path':kind,'Ji2':23,'Jf2':jf2,
            'pure_dipole_a2_over_u2':str(scale),'F22_over_F11':str(t),
            'F12_over_F11_squared':str(r2),'native_cross_ratio':ratio_cross,
            'phase_invariant_lower_polynomial':str(lower),
            'strict_abs_delta_threshold':str(critical),
            'threshold_numeric':float(critical),
            'strict_upper_multipole_intensity_fraction_threshold':str(upper_fraction),
            'fraction_threshold_numeric':float(upper_fraction),
            'not_a_measured_reference_purity':True})
    D1=kernels['dipole_stretched'];D0=kernels['dipole_zero'];ratio=-(2*J-1)/(J+1)
    assert np.max(abs(D0['A2'][0]-float(ratio)*D1['A2'][0]))<1e-12
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'script_sha256':sha(Path(__file__)),'contract_sha256':sha(a.contract),
        'source_and_helpers_unchanged':True,'path_designs':answer,
        'same_density_pure_dipole_relation':{'a2_D0_over_a2_D1':str(ratio),
            'linear_identity_valid_at_u2_zero_without_division':True,
            'conditional_on_samegate_feeding_density_and_point_or_corrected_response':True,
            'does_not_certify_purity_from_a4zero':True},
        'scope':{'no_new_counts_or_covariance':True,'no_experimental_delta_parity_or_CI':True,
            'no_Gaussian_width_assumed':True,'source_labels_and_calculatedICC_not_purity_measurements':True}}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
