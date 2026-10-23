#!/usr/bin/env python3
"""Raw-anchored DSAM Qt regression boundary controls for 136Sm/131Ce/133Pr.

This is a conditional sensitivity design. It does not refit line shapes, recover
covariances, or convert an unquoted stopping/feeding systematic into a CI.
"""

raise SystemExit("Retired by Day20 source audit001: do not regenerate historical certification; use day20_literal_trend_audit.py and current canonical source boundaries.")
import hashlib,json,math,re
from pathlib import Path
import numpy as np
import pymupdf

RUN=Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
SM=Path('raw/papers/2019_Babra et al_Investigation of a large change in deformation for the γ -soft nucleus Sm 136.pdf')
SI=Path('raw/papers/2016_Singh et al_Lifetime measurements in the yrast band of the gamma-soft nuclei 131Ce and 133Pr.pdf')
SM_HASH='a26149bff0e7b3bdb5459ba5897b69bc7f8ed17a646f13ed59dd5b38ae425ba6'
SI_HASH='95e0831b9864a58fd1a896a1b20e227d88d9b7aa5de56c738c3792441caa1a30'

def weighted_fit(x,y,s):
    p,c=np.polyfit(np.asarray(x,float),np.asarray(y,float),1,w=1/np.asarray(s,float),cov=True)
    return {'slope':float(p[0]),'slope_sigma':float(math.sqrt(c[0,0])),'z':float(p[0]/math.sqrt(c[0,0]))}

def main():
    checks=[]
    def check(name,ok,**e):
        checks.append({'name':name,'passed':bool(ok),**e});assert ok,name
    check('Babra raw hash',hashlib.sha256(SM.read_bytes()).hexdigest()==SM_HASH)
    check('Singh raw hash',hashlib.sha256(SI.read_bytes()).hexdigest()==SI_HASH)
    with pymupdf.open(SM) as d:
        smtext=d[1].get_text()+d[2].get_text()
        check('Babra TableI and 15 percent text','TABLE I.' in smtext and '15%' in smtext and 'systematic' in smtext)
    with pymupdf.open(SI) as d:
        sitext=d[4].get_text()+d[7].get_text()
        check('Singh Table1/Table2 and feeding text','Table 1.' in sitext and 'Table 2.' in sitext and 'side-feeding' in sitext)
    I=[8,10,12,14,16,18];Q=[5.66,5.59,5.70,5.38,4.85,5.05];lo=[.19,.79,.20,.33,.32,.33];hi=[.19,.78,.21,.34,.34,.37];avg=[(a+b)/2 for a,b in zip(lo,hi)]
    fits={k:weighted_fit(I,Q,s) for k,s in [('avg',avg),('lower',lo),('upper',hi)]}
    check('Babra slope convention spread small',max(v['z'] for v in fits.values())-min(v['z'] for v in fits.values())<.1)
    w=1/np.square(avg);mean=float(np.sum(w*np.asarray(Q))/sum(w));meanerr=float(1/math.sqrt(sum(w)))
    check('Babra common 15 percent is multiplicative candidate',math.isclose(.15*mean,.8224029727345335,rel_tol=2e-3))
    # A common multiplicative scale changes slope and its standard error together;
    # an independent per-state envelope is a separate sensitivity, not a CI.
    common=[{'scale':a,'slope':a*fits['avg']['slope'],'slope_sigma':a*fits['avg']['slope_sigma'],'z':fits['avg']['z']} for a in [.85,1.,1.15]]
    statewise=[{'state':i,'Qt_low':q-.15*q,'Qt_high':q+.15*q} for i,q in zip(I,Q)]
    check('common scale leaves z invariant',all(math.isclose(x['z'],fits['avg']['z']) for x in common))
    prI=[7.5,9.5,11.5];prQ=[3.55,3.53,3.09];prE=[.14,.11,.135];prfit=weighted_fit(prI,prQ,prE);check('133Pr conditional slope below 2 sigma',abs(prfit['z'])<2)
    ceI=[7.5,13.5,15.5,17.5];ceQ=[2.93,2.26,2.66,2.43];ceE=[.45,.30,.125,.21];cefit=weighted_fit(ceI,ceQ,ceE);check('131Ce conditional slope below 1 sigma',abs(cefit['z'])<1)
    out={'kind':'raw-anchored-regression-and-systematic-boundary-design','sources':[{'path':str(SM),'sha256':SM_HASH},{'path':str(SI),'sha256':SI_HASH}], 'sm136':{'points':[{'I':i,'Qt':q,'minus':a,'plus':b} for i,q,a,b in zip(I,Q,lo,hi)],'fits':fits,'weighted_mean':mean,'weighted_mean_stat_error':meanerr,'common_scale_sensitivity':common,'statewise_15pct_envelope':statewise,'interpretation':'15 percent stopping uncertainty is unquoted/model systematic. Common multiplicative scale preserves slope z; independent per-state envelope is a sensitivity, not a confidence interval.'},'pr133':{'conditional_fit':prfit,'sidefeeding_input_ps':[1100,1.9,.014],'interpretation':'three-point fit and sidefeeding values are source-model conditional; no joint covariance'},'ce131':{'conditional_fit':cefit,'feeding_switch':'tau_SF at low spin versus Q_SF at higher spin'},'checks':checks,'valid':all(x['passed'] for x in checks),'independent_refit_or_CI':False}
    p=RUN/'qt-systematics-boundary-result-049.json';p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'valid':out['valid'],'checks':len(checks),'sm_z':fits['avg']['z'],'sm_z_range':[v['z'] for v in fits.values()],'pr_z':prfit['z'],'ce_z':cefit['z'],'output':str(p)}))
if __name__=='__main__':main()
