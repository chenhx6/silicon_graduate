#!/usr/bin/env python3
"""Typed ENSDF identity audit and a declared same-parent A2 ratio check.

The numerical inverse is conditional on common coefficient layers and response;
it does not remeasure Dors1979/KF89 mixing ratios. Missing MR stays missing.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re

import numpy as np

from day14_ensdf_crosswalk import number, uncertainty
from day16_d96_eq4_erratum_audit import direct_operators
from day16_kf89_w178_gate_audit import preimage, roots, value, finite_delta
from day16_pdco_ambiguity_preview import orientation, source_f


def read_records(path: Path) -> tuple:
    lines=path.read_text().splitlines();gammas=[];levels=[];parent=None;current=None
    for no,raw in enumerate(lines,1):
        s=raw.ljust(80)
        if not s.startswith('178W '):continue
        if s[5:7]=='  ' and s[7]=='L':
            parent={'line':no,'energy_text':s[9:19].strip(),'energy_keV':number(s[9:19]),
                    'Jpi_literal':s[21:39].strip(),'raw':raw,'comments':[]}
            levels.append(parent);current=None
        elif s[5:7]=='  ' and s[7]=='G':
            current={'line':no,'energy_keV':number(s[9:19]),'energy_uncertainty_keV':uncertainty(s[9:19],s[19:21]),
                     'parent':parent,'multipolarity_literal':s[31:41].strip(),
                     'MR_literal':s[41:49].strip(),'MR_uncertainty_literal':s[49:55].strip(),
                     'CC':number(s[55:62]),'CC_uncertainty':uncertainty(s[55:62],s[62:64]),
                     'RI':number(s[21:29]),'RI_uncertainty':uncertainty(s[21:29],s[29:31]),
                     'RI_field':s[21:29],'RI_uncertainty_field':s[29:31],
                     'raw':raw,'comments':[]}
            gammas.append(current)
        elif s[7]=='G' and current is not None:
            current['comments'].append({'line':no,'text':raw})
        elif s[7]=='L' and parent is not None:
            parent['comments'].append({'line':no,'text':raw})
    return lines,levels,gammas


def match(gammas: list, parent: float, energy: float) -> dict:
    selected=[g for g in gammas if g['parent'] is not None and g['energy_keV'] is not None
              and abs(g['parent']['energy_keV']-parent)<1e-6 and abs(g['energy_keV']-energy)<1e-6]
    if len(selected)!=1:raise ValueError(('identity not unique',parent,energy,len(selected)))
    return selected[0]


def a2(gamma: dict) -> tuple | None:
    for c in gamma['comments']:
        m=re.search(r'A\{-2\}=([+−-]?[.\d]+)\s+\{I(\d+)\}',c['text'])
        if m:
            text=m[1].replace('−','-')
            return float(text),uncertainty(text,m[2])
    return None


def experimental_k(gamma: dict) -> tuple | None:
    for c in gamma['comments']:
        m=re.search(r'\|a\(K\)exp=([.\d]+)\s+\{I(\d+)\}',c['text'])
        if m:return float(m[1]),uncertainty(m[1],m[2])
    return None


def f_matrix(ji: int,jf: int,k: int) -> np.ndarray:
    return np.array([[source_f(k,0,k,l,lp,ji,jf) for lp in (1,2)] for l in (1,2)])


def photon_check(ji: int,jf: int,f: np.ndarray) -> float:
    # Highest-M pure state is a numerical validation input, not experimental rho.
    pop=np.zeros(2*ji+1);pop[-1]=1.;rho=np.diag(pop);b2=orientation(ji,rho,2)
    theta=np.array([0.,45.,90.]);x=np.cos(np.deg2rad(theta))
    leg=np.column_stack([np.polynomial.legendre.legval(x,[0.]*k+[1.]) for k in (0,2,4)])
    errors=[]
    for d in (-1.9,-.4,0.,.4,3.):
        parts=(("M",1,1.),("E",2,d));singles=[]
        for t in theta:
            singles.append(sum(float(np.sum(abs(op)**2*pop[None,:]))
                               for op in direct_operators(ji,jf,parts,math.radians(t),0.,None)))
        coefficients=np.linalg.solve(leg,singles);coefficients/=coefficients[0]
        v=np.array([1.,d])/math.hypot(1.,d)
        errors.append(abs(coefficients[1]/b2-float(v@f@v)))
    assert max(errors)<1e-12
    return float(max(errors))


def inverse_check(pair: dict,gs: list,cfg: dict) -> dict:
    t=match(gs,pair['parent_energy_keV'],pair['target_energy_keV'])
    r=match(gs,pair['parent_energy_keV'],pair['reference_energy_keV'])
    assert a2(t)==tuple(pair['target_A2']) and a2(r)==tuple(pair['reference_A2'])
    assert t['MR_literal']==r['MR_literal']=='' and r['multipolarity_literal']=='E2'
    ji,jt,jr=pair['spins']; f=f_matrix(ji,jt,2);fr=source_f(2,0,2,2,2,ji,jr)
    assert fr<0
    matrix=f/fr; eig=np.linalg.eigvalsh(matrix); assert eig[0]<0
    obs=pair['target_A2'][0]/pair['reference_A2'][0]
    alphas=roots(matrix-obs*np.eye(2));intervals=[]
    for scale in cfg['uncertainty_scales']:
        ta,te=pair['target_A2'];ra,re_=pair['reference_A2']
        assert ra-scale*re_>0
        corners=[(ta+st*scale*te)/(ra+sr*scale*re_) for st in (-1,1) for sr in (-1,1)]
        lo,hi=min(corners),max(corners)
        intervals.append({'quoted_margin_scale':scale,'ratio_rectangle_image':[lo,hi],
                          'atan_d_preimage_degrees':preimage(matrix,np.eye(2),lo,hi),
                          'necessary_positive_s2_for_any_margin_value':hi/eig[0],
                          'confidence_level':None})
    return {'pair':pair['id'],'source_target':t,'source_reference':r,
            'F2_target_M1_E2_matrix':f.tolist(),'F2_reference_pure_E2':fr,
            'Qratio_one_intrinsic_ratio_range':eig.tolist(),'observed_central_ratio':obs,
            'central_all_roots_D96':[{'d':finite_delta(a),'atan_d_deg':math.degrees(a)} for a in alphas],
            'necessary_positive_s2_for_central':obs/eig[0],
            'ratio_at_assumed_D96_d_minus1point9':value(matrix,math.atan(cfg['signed_delta_source_prior_not_to_fit'])),
            'quoted_margin_checks':intervals,'sourceF_vs_photon_max_error':photon_check(ji,jt,f),
            'boundary':'No sigma fitted. s2=1 and matched same-parent coefficient layer are conditional. No experimental confidence or new measured mixing ratio.'}


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);args=p.parse_args();cfg=json.loads(args.input.read_text())
    assert cfg['identity'] in ['DAY16-N178-SAME-PARENT-REFERENCE-01','DAY16-N178-SAME-PARENT-REFERENCE-02']
    data={}
    for key,obj in cfg['source_objects'].items():
        path=Path(obj['path']);assert hashlib.sha256(path.read_bytes()).hexdigest()==obj['sha256']
        data[key]=read_records(path)
    ad,ox,al=[data[k] for k in ('178074001','178074004','178074006')]
    assert '1989KR01' in ox[0][1] and '1979DO02' in al[0][1]
    assert any('125' in s and 'RI' in s for s in al[0])
    assert any('Complementary experiments' in s for s in al[0])
    assert any('170' in s and 'E,RI' in s for s in ad[0])
    chosen=[]
    for pair in cfg['pairs']:chosen.append(inverse_check(pair,al[2],cfg))
    cc=match(al[2],2133.93,168.71)
    assert cc['MR_literal']=='' and cc['CC']==.8 and cc['CC_uncertainty']==.3
    weak=match(al[2],3054.89,1089.7)
    assert weak['RI']==1.3 and weak['RI_uncertainty']==1.4
    target_o=match(ox[2],3055.2,920.9);target_a=match(ad[2],3053.81,920.8)
    assert target_o['multipolarity_literal']=='D' and target_o['parent']['Jpi_literal']=='(11)'
    assert target_a['multipolarity_literal']=='M1+E2' and target_a['MR_literal']==''
    nearby=[g for g in ad[2] if g['energy_keV'] is not None and abs(g['energy_keV']-137.34)<.8]
    assert len(nearby)>1 and len({g['parent']['energy_keV'] for g in nearby})>1
    new_companion=None
    if 'new_companion' in cfg:
        fields=cfg['new_companion'];carbon=data[fields['source_record']]
        assert '1999CU02,1998PU01' in carbon[0][1]
        kt=match(carbon[2],fields['parent_energy_keV'],fields['target_energy_keV'])
        kr=match(carbon[2],fields['parent_energy_keV'],fields['reference_energy_keV'])
        assert experimental_k(kt)==tuple(fields['target_experimental_KICC'])
        assert experimental_k(kr)==tuple(fields['reference_experimental_KICC'])
        assert a2(kt)==tuple(fields['target_A2']) and a2(kr)==tuple(fields['reference_A2'])
        assert kt['MR_literal']==kr['MR_literal']==''
        near168=[g for g in carbon[2] if g['energy_keV'] is not None and abs(g['energy_keV']-168.3)<.8]
        same_comment=[g for g in near168 if any('A{-2}=-0.67' in c['text'] for c in g['comments'])]
        assert len(same_comment)==2
        new_companion={'target':kt,'reference':kr,'target_KICC':experimental_k(kt),
                       'reference_KICC':experimental_k(kr),
                       'near168_repeated_literal_A2':[{'energy':g['energy_keV'],'parent':g['parent']['energy_keV'],'comments':g['comments']} for g in same_comment],
                       'boundary':'Secondary evaluation labels K-shell experimental values. Actual electron/photon calibration, gates, covariance and primary producer are unavailable; no ICC theory or new delta fit is supplied.'}
    obj={'identity':cfg['identity'],'input_sha256':hashlib.sha256(args.input.read_bytes()).hexdigest(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'same_parent_checks':chosen,
         'typed_crosswalk':{'CC_not_MR':cc,'weak_RI_fixed_fields':weak,'oxygen_target':target_o,
                            'adopted_target':target_a,
                            'near137_energy_only_ambiguity':[{'energy':g['energy_keV'],'parent_energy':g['parent']['energy_keV'],'line':g['line']} for g in nearby]},
         'carbon_source_companion':new_companion,
         'raw_storage_boundary':'Public text objects remain in repository tmp; raw archive untouched. Exact excerpts/provenance must be preserved in the source page.',
         'all_internal_checks_passed':True}
    args.output.write_text(json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'output':str(args.output),'all_internal_checks_passed':True,
                      'pairs':[{k:v for k,v in c.items() if k not in ['source_target','source_reference']} for c in chosen],
                      'CC_is_not_MR':{'MR':cc['MR_literal'],'CC':cc['CC'],'CC_error':cc['CC_uncertainty']},
                      'weak_RI_literal':{'value':weak['RI'],'error':weak['RI_uncertainty']}},ensure_ascii=False))
    return 0


if __name__=='__main__':raise SystemExit(main())
