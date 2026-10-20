#!/usr/bin/env python3
"""T71 typed tables and central 35Cl AD/P/population replay; not a fit CI."""
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import sympy as sp
from sympy.physics.wigner import clebsch_gordan as cg, racah

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
D=sp.Symbol('d',real=True)


@lru_cache(None)
def zvalue(ji2,jf2,ell,other,rank):
    ji,jf=sp.Rational(ji2,2),sp.Rational(jf2,2)
    return sp.simplify((-1)**(ell+other+sp.Rational(rank,2)+1)
        *sp.sqrt((2*ell+1)*(2*other+1)*(2*ji+1)**2)
        *cg(ell,other,rank,-1,1,0)*racah(ell,ji,other,ji,jf,rank))


def real_roots(expr):
    num=sp.fraction(sp.cancel(expr))[0]
    if not num.has(D):
        return []
    return sorted(float(sp.re(v)) for v in sp.nroots(num,n=40,maxsteps=200)
                  if abs(float(sp.im(v)))<1e-25)


def main():
    path=RUN/'taras1971-actual-contract.json';c=json.loads(path.read_text());tol=c['table_decimal_tolerance']
    tables=[]
    for ell,other,k,printed in c['Table3_K']:
        exact=-sp.sqrt(sp.factorial(k-2)/sp.factorial(k+2))*cg(ell,other,k,1,1,2)/cg(ell,other,k,1,-1,0)
        assert sp.simplify(exact-sp.sympify(printed))==0
        tables.append({'table':3,'id':[ell,other,k],'exact':str(exact),'passed':True})
    for row in c['Table4_rows']:
        theta=sp.pi*row[0]/180;x=sp.cos(theta)
        calculated=[float(sp.legendre(k,x)) for k in [2,4,6]]+[float(sp.assoc_legendre(k,2,x)) for k in [2,4,6]]
        errors=[abs(v-p) for v,p in zip(calculated,row[1:])]
        tables.append({'table':4,'theta_deg':row[0],'max_abs_print_difference':max(errors),'passed':max(errors)<=tol})
    for row in c['Table6_Z_rows']:
        ell=row['lowL'];pairs=[(ell,ell),(ell,ell+1),(ell+1,ell+1)]
        exact=[zvalue(row['Ji2'],row['Jf2'],l,lp,row['K']) for l,lp in pairs]
        errors=[abs(float(v)-p) for v,p in zip(exact,row['values'])]
        tables.append({'table':6,'input':row,'exact':list(map(str,exact)),
                       'max_abs_print_difference':max(errors),'passed':max(errors)<=tol})
    for ji2,k,printed in c['Table7_CG_rows']:
        ji=sp.Rational(ji2,2)
        exact=[cg(ji,ji,k,sp.Rational(m,2),-sp.Rational(m,2),0) for m in range(1,ji2+1,2)]
        errors=[abs(float(v)-p) for v,p in zip(exact,printed)]
        tables.append({'table':7,'Ji2':ji2,'K':k,'exact':list(map(str,exact)),
                       'max_abs_print_difference':max(errors),'passed':max(errors)<=tol})
    t=c['Table5'];a2,a4=map(lambda k:sp.Rational(str(t[k][0])),['a2','a4'])
    ji,jf=sp.Rational(t['Ji2'],2),sp.Rational(t['Jf2'],2)
    zz=[zvalue(t['Ji2'],t['Jf2'],l,lp,2) for l,lp in [(1,1),(1,2),(2,2)]]
    z11,z12,z22=zz;z4=zvalue(t['Ji2'],t['Jf2'],2,2,4)
    kernel=z11-2*D*z12+D**2*z22
    pcalc=sp.factor((1+a2*(z11+2*D*z12+D**2*z22)/kernel+a4)/
                     (1-2*a2*(z11+D**2*z22)/kernel-a4/4))
    p20=sp.factor(a2*(1+D**2)/kernel)
    p40=sp.factor(-a4*(1+D**2)/(D**2*z4));p00=1/sp.sqrt(2*ji+1)
    qs=[]
    for m2 in range(1,t['Ji2']+1,2):
        m=sp.Rational(m2,2)
        qs.append(sp.factor(2*(-1)**(ji-m)*sum(cg(ji,ji,k,m,-m,0)*pk
                  for k,pk in [(0,p00),(2,p20),(4,p40)])))
    assert sp.simplify(sum(qs)-1)==0
    for k,pk in [(2,p20),(4,p40)]:
        restored=sum((-1)**(ji-sp.Rational(m2,2))*cg(ji,ji,k,sp.Rational(m2,2),-sp.Rational(m2,2),0)*q
                     for m2,q in zip(range(1,t['Ji2']+1,2),qs))
        assert sp.simplify(restored-pk)==0
    candidates=[]
    for kind,target in [('M1E2',sp.Rational(str(t['p_field_ratio'][0]))),
                        ('E1M2',1/sp.Rational(str(t['p_field_ratio'][0])))]:
        for root in sp.solve(sp.together(pcalc-target),D):
            qnum=[float(q.subs(D,root).evalf(18)) for q in qs]
            candidates.append({'family':kind,'delta_central':float(root.evalf(18)),
                'folded_q':qnum,'positive_population':min(qnum)>=-1e-12,
                'higher_multipole_intensity_fraction':float((root**2/(1+root**2)).evalf(18))})
    bounds=sorted(set([0.]+real_roots(kernel)+sum([real_roots(q) for q in qs],[])))
    intervals=[]
    ext=[None]+bounds+[None]
    for low,high in zip(ext,ext[1:]):
        sample=(min(-1,2*high) if low is None else max(1,2*low) if high is None else (low+high)/2)
        if min(float(q.subs(D,sample)) for q in qs)>=-1e-12:
            intervals.append([low,high])
    rr,sr=t['R'];nn,sn=t['N90_over_N0']
    pfrom=(1-nn*rr)/(nn-rr);gn=(rr*rr-1)/(nn-rr)**2;gr=(1-nn*nn)/(nn-rr)**2
    terms=[abs(gn*sn),abs(gr*sr)]
    propagated={'p_from_rounded_R_N':pfrom,'p_printed':t['p_field_ratio'][0],
       'N_implied_printed_p_R':(t['p_field_ratio'][0]*rr+1)/(t['p_field_ratio'][0]+rr),
       'conditional_sigma_p_independent_R_N':math.hypot(*terms),
       'local_sigma_p_range_unknown_R_N_corr':[abs(terms[0]-terms[1]),sum(terms)],
       'not_original_fitCov_or_CI':True}
    result={'at':datetime.now(timezone.utc).isoformat(),
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
       'source_table_controls':tables,'all_typed_table_controls_pass':all(x['passed'] for x in tables),
       'Table5_ratio_and_partial_error_budget':propagated,'central_delta_population_candidates':candidates,
       'central_positive_population_intervals_only':intervals,
       'pure_M2_limit_p_from_central_AD':float(1/sp.limit(pcalc,D,sp.oo)),
       'population_formulas':list(map(str,qs)),
       'new_source_Z_and_population_inverse_controls':True,
       'no_original_band_uncertainty_J7half_fit_or_experimental_CI':True,
       'ok':all(x['passed'] for x in tables)}
    (RUN/'taras1971-actual-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'tables_pass':result['all_typed_table_controls_pass'],
       'failed_rows':[x for x in tables if not x['passed']],
       'candidates':candidates,'intervals':intervals,'ratio':propagated},indent=2))


if __name__=='__main__':
    main()
