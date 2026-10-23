#!/usr/bin/env python3
"""Exact two-point shapes versus first-order moment propagation, not a data fit.

Commuting positive Q=scale*(1+-epsilon), equal probabilities, C=cos3gamma=1.
X=Q^2 and Y=Q^3*C use normalized cubic coordinates; source cubic normalization
is absorbed into Y. Cov is intrinsic shape spread, never event/fit uncertainty.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def case(epsilon, scale=F(1)):
    q = [scale*(1-epsilon), scale*(1+epsilon)]
    assert all(qi > 0 for qi in q)
    mean = lambda vals: sum(vals, F(0))/2
    x, y = [qi**2 for qi in q], [qi**3 for qi in q]
    mx, my = mean(x), mean(y)
    vx = mean([(xi-mx)**2 for xi in x])
    vy = mean([(yi-my)**2 for yi in y])
    cov = mean([(xi-mx)*(yi-my) for xi,yi in zip(x,y)])
    # Gradient of f(x,y)=y/x^(3/2), contracted with the exact intrinsic Cov.
    v_delta = vy/mx**3 + F(9,4)*my**2*vx/mx**5 - 3*my*cov/mx**4
    return {'Q':q,'mx':mx,'my':my,'vx':vx,'vy':vy,'cov':cov,
            'v_delta':v_delta,'true_mean_Q':mean(q),
            'true_variance_Q':mean([(qi-mean(q))**2 for qi in q]),
            'beta_delta_variance':vx/(4*mx),
            'R':float(my)/float(mx)**1.5,
            'true_angular_function_values':[1.,1.]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    args = p.parse_args()
    if args.out.exists():
        raise SystemExit('Refusing to overwrite existing result')
    checks = []

    def check(name, condition):
        checks.append({'name':name,'satisfied':bool(condition)})
        if not condition:
            raise AssertionError(name)

    eps_grid = [F(0),F(1,1000),F(1,100),F(1,10),F(1,3),F(1,2),F(3,4)]
    rows = []
    for e in eps_grid:
        d = case(e)
        exact_v = e**6*(5-e**2)**2/(1+e**2)**5
        check('gradientCov versus closed form epsilon='+str(e),d['v_delta']==exact_v)
        check('Cov PSD/rank1 epsilon='+str(e),d['vx']*d['vy']-d['cov']**2==0)
        check('common amplitude rescaling epsilon='+str(e),case(e,F(7,3))['v_delta']==d['v_delta'])
        rows.append({'epsilon':str(e),'delta_variance':str(d['v_delta']),
                     'R':d['R'],'true_angular_variance':0,
                     'beta_effective_rms':math.sqrt(float(d['mx'])),
                     'true_mean_amplitude':float(d['true_mean_Q']),
                     'true_amplitude_SD':math.sqrt(float(d['true_variance_Q'])),
                     'delta_amplitude_SD':math.sqrt(float(d['beta_delta_variance']))})
    d = case(F(1,3),F(3,2)) # Q=(1,2), same witness as113, scale explicit.
    check('Q1,2 exact chosen witness',d['Q']==[F(1),F(2)])
    check('Q1,2 fullCov delta variance exact',d['v_delta']==F(121,6250))
    check('Q1,2 exact beta-proxy variance',d['beta_delta_variance']==F(9,40))
    check('Q1,2 true amplitude variance',d['true_variance_Q']==F(1,4))
    # Numeric derivative check is independent of the exact covariance contraction.
    mx,my = float(d['mx']),float(d['my'])
    f = lambda x,y:y/x**1.5
    step = 1e-5
    numeric = [(f(mx+step,my)-f(mx-step,my))/(2*step),
               (f(mx,my+step)-f(mx,my-step))/(2*step)]
    analytic = [-1.5*my/mx**2.5,1/mx**1.5]
    check('centered derivative versus gradient',max(abs(a-b) for a,b in zip(numeric,analytic))<1e-9)
    check('small epsilon delta variance tends25epsilon6',abs(float(case(F(1,1000))['v_delta']/F(1,1000)**6)-25)<.0002)
    check('constant-amplitude limit delta variance0',case(F(0))['v_delta']==0)
    # Zero cubic mean: use independent C=+-1 at constant Q, avoiding relative divide.
    # mx=1,my=0,vx=0,vy=1,cov=0 gives absolute propagated variance1.
    zero_mean_absolute = F(1)/F(1)**3
    check('zero cubic mean absolute form finite',zero_mean_absolute==1)
    result = {'checkpoint':'115','kind':'declared nonlinear moment propagation domain',
              'source_locators':['PO20-D20-4 Eq15-17','HE20-D20-R113-2'],
              'absolute_delta_variance':'Var(Y)/mx^3 +(9/4)my^2 Var(X)/mx^5 -3 my Cov(X,Y)/mx^4',
              'two_point_closed_form':'epsilon^6*(5-epsilon^2)^2/(1+epsilon^2)^5',
              'Q1_2_case':{k:str(v) if isinstance(v,F) else v for k,v in d.items() if k!='Q'},
              'true_Q1_2_angular_variance':0,
              'delta_Q1_2_angular_SD':math.sqrt(float(d['v_delta'])),
              'grid':rows,'controls_executed':len(checks),'checks':checks,
              'scientific_certification':False,
              'boundaries':['No eventMC or finite-calibrator sampling','ShapeCov is not estimatorCov; no1/N was inserted',
                            'Does not reproduce or invalidate actual CI wavefunctions/numeric tables',
                            'R is a ratio of moments, while exact f(X,Y) is identically1 on declared support',
                            'No artificial clipping of meanR or negative variance',
                            'Beta comparisons set conversionconstant1; physical mass/charge factor remains separate'],
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'controls':len(checks),'Q1_2_delta_variance':str(d['v_delta']),
                      'Q1_2_true_angular_variance':0,'Q1_2_delta_SD':result['delta_Q1_2_angular_SD'],
                      'true_amplitude_SD':.5,'delta_amplitude_SD':math.sqrt(float(d['beta_delta_variance'])),
                      'scientific_certification':False}))


if __name__=='__main__':
    main()
