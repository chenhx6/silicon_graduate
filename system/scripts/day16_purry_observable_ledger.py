#!/usr/bin/env python3
"""Check primary target rows and the geometry of Purry's truncated P2 fit.

Equal weights are a diagnostic assumption; no actual angular data, errors or
response weights are reconstructed. This does not fit a new nuclear mixing ratio.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np
import pymupdf


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--ledger',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();cfg=json.loads(a.input.read_text());ledger=json.loads(a.ledger.read_text())
    assert cfg['identity']=='DAY16-PURRY97-A2-ESTIMATOR-01'
    pdf=Path(ledger['PDF_path']);assert hashlib.sha256(pdf.read_bytes()).hexdigest()==ledger['PDF_sha256']
    doc=pymupdf.open(pdf);assert len(doc)==112
    txt=doc[47].get_text();assert all(x in txt for x in ['920.8','1089.6','0.0067(11)','0.0031(5)'])
    experiment=doc[29].get_text()+doc[30].get_text();assert '50 and 400 ns' in experiment
    assert '1.5' in experiment and 'Si(Li)' in experiment and '152Eu' in experiment
    ang=np.array(cfg['angles_unique_deg'],float);x=np.cos(np.deg2rad(ang))
    p2=np.polynomial.legendre.legval(x,[0.,0.,1.]);p4=np.polynomial.legendre.legval(x,[0.,0.,0.,0.,1.])
    full=np.column_stack([np.ones_like(x),p2,p4]);trunc=full[:,:2]
    assert np.linalg.matrix_rank(full)==3
    w=np.diag(cfg['declared_equal_weights'])
    c=np.linalg.solve(trunc.T@w@trunc,trunc.T@w@p4)
    direct=np.linalg.lstsq(trunc,p4,rcond=None)[0]
    assert np.max(abs(c-direct))<1e-13
    # P4 = (35 P2^2 - 10 P2 - 7)/18; pair slopes bound any
    # positive diagonal-weight least-squares slope, by the covariance identity.
    polynomial=(35*p2**2-10*p2-7)/18
    assert max(abs(polynomial-p4))<1e-13
    slopes=[]
    for i,j in itertools.combinations(range(3),2):
        slopes.append({'angle_pair_deg':[ang[i],ang[j]],
                       'P4_on_P2_secant_slope':float((p4[i]-p4[j])/(p2[i]-p2[j]))})
    bounds=[min(s['P4_on_P2_secant_slope'] for s in slopes),max(s['P4_on_P2_secant_slope'] for s in slopes)]
    assert bounds[0]<=c[1]<=bounds[1]
    # Source-inspired estimator identity, without choosing an actual A4.
    for aa,bb in [(0.,0.),(.2,0.),(0.,.1),(-.3,-.1)]:
        y=np.ones(3)+aa*p2+bb*p4
        fit=np.linalg.lstsq(trunc,y,rcond=None)[0]
        predicted=(aa+c[1]*bb)/(1+c[0]*bb)
        assert abs(fit[1]/fit[0]-predicted)<1e-13
    comp=cfg['arithmetic_companion'];n,sn=comp['I1090'];d,sd=comp['I921'];ratio=n/d
    rhos=[]
    for rho in comp['correlation_sensitivity']:
        var=ratio**2*((sn/n)**2+(sd/d)**2-2*rho*sn*sd/(n*d))
        assert var>=-1e-14
        rhos.append({'rho':rho,'local_ratio_error_scale':math.sqrt(max(var,0))})
    result={'identity':cfg['identity'],'input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
            'ledger_sha256':hashlib.sha256(a.ledger.read_bytes()).hexdigest(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'verified_PDF_sha256':ledger['PDF_sha256'],'PDF_selected_target_row_tokens_verified':True,
            'angles_deg':ang.tolist(),'P2':p2.tolist(),'P4':p4.tolist(),'full_design_rank':3,
            'full_design_singular_values':np.linalg.svd(full,compute_uv=False).tolist(),
            'equal_weight_P4_projection_on_constant_P2':{'c0':float(c[0]),'c2':float(c[1])},
            'reported_a2_identity':'(A2+c2*A4)/(1+c0*A4) for the stated weights; source actual weights/response unknown',
            'P4_projection_residual_norm':float(np.linalg.norm(p4-trunc@c)),
            'positive_diagonal_weight_slope_bounds':bounds,'pair_slopes':slopes,
            'same_parent_gamma_intensity_arithmetic':{'central_ratio_1090_over921':ratio,'rho_sensitivity':rhos,
                'not_a_new_branch_or_independent_measurement':True},
            'boundary':'P2 estimator geometry and table arithmetic only; no measured A4, actual weighting, matched density, reconstructed covariance, significance or new delta fit.',
            'all_checks_passed':True}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,ensure_ascii=False));return 0


if __name__=='__main__':raise SystemExit(main())
