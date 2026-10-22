#!/usr/bin/env python3
"""Ideal DDCM rate-equation design and calibration failures, not a data refit.

Direct/indirect gates refer to Klemme1999 Eqs1-3. All feeder mixtures, tau,
normalization slopes and distance gains are declared synthetic controls.
"""
import argparse
from datetime import datetime,timezone
import hashlib
import json
import math
from pathlib import Path


def cascade(t,ta,tb):
    """Feeder B waits Exp(tb), then level A waits Exp(ta), branching one.

    Returns feeder survival, A occupancy, A decay CDF, A decay density.
    """
    if min(t,ta,tb)<0 or min(ta,tb)==0:raise ValueError('time domain')
    eb=math.exp(-t/tb)
    if math.isclose(ta,tb,rel_tol=0,abs_tol=1e-12):
        occ=(t/ta)*eb;surv=(1+t/ta)*eb
    else:
        ea=math.exp(-t/ta)
        occ=ta*(eb-ea)/(tb-ta)
        surv=(tb*eb-ta*ea)/(tb-ta)
    return eb,occ,1-surv,occ/ta


def mixture(t,ta,components):
    vals=[cascade(t,ta,tb) for _,tb in components]
    return tuple(sum(w*row[j] for (w,_),row in zip(components,vals)) for j in range(4))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True,type=Path)
    q=p.parse_args()
    checks=[]
    def check(name,ok):
        checks.append({'name':name,'passed':bool(ok)})
        if not ok:raise AssertionError(name)
    ta=2.0;v=.016*299.792458
    families={'fast':[(1.,.5)],'equal':[(1.,2.)],
              'slow':[(1.,10.)],'mixed':[(.8,.5),(.2,50.)]}
    rows=[]
    for family,parts in families.items():
        for t in [.5,1,2,5,10,20]:
            sb,occ,cdf,rate=mixture(t,ta,parts)
            direct=occ/rate
            indirect=(1-cdf-sb)/rate
            check(f'population conservation {family} {t}',math.isclose(sb+occ+cdf,1,abs_tol=1e-13))
            check(f'direct gate rate ratio {family} {t}',math.isclose(direct,ta,abs_tol=1e-12))
            check(f'indirect gate feeding subtraction {family} {t}',math.isclose(indirect,ta,abs_tol=1e-9))
            h=1e-4
            fd=(mixture(t+h,ta,parts)[2]-mixture(t-h,ta,parts)[2])/(2*h)
            check(f'independent CDF derivative {family} {t}',math.isclose(fd,rate,rel_tol=1e-7))
            rows.append({'family':family,'vacuum_time_ps':t,'B_survival':sb,'A_occupancy':occ,
                         'A_CDF':cdf,'direct_DDCM_ps':direct,'indirect_DDCM_ps':indirect,
                         'incorrect_unsubtracted_survival_over_rate_ps':(1-cdf)/rate})
    # Coordinate translation changes no derivative; a distance gain does.
    t=2;parts=families['slow'];sb,occ,cdf,rate=mixture(t,ta,parts)
    translated=[]
    for offset in [0,8,42,100]:
        x=offset+v*t;dx=1e-3
        f=lambda xx:mixture((xx-offset)/v,ta,parts)[2]
        grad=(f(x+dx)-f(x-dx))/(2*dx)
        recovered=occ/grad/v
        check(f'constant origin translation offset={offset}',math.isclose(recovered,ta,rel_tol=1e-7))
        translated.append({'offset_um':offset,'recovered_tau_ps':recovered})
    gain=1.02
    gained_tau=occ/(rate/(v*gain))/v
    check('distance gain creates flat biased tau',math.isclose(gained_tau,gain*ta))
    # An unknown run normalization must be removed BEFORE differentiating.
    norm_slope=.02
    wrong=occ/(rate+norm_slope*cdf)
    check('unnormalized exposure gradient biases DDCM',abs(wrong-ta)>.01)
    # Incorrect direct-feeder subtraction normalization creates a residual.
    alpha_wrong=1.05
    wrong_indirect=(1-cdf-alpha_wrong*sb)/rate
    check('indirect subtraction alpha calibration matters',abs(wrong_indirect-ta)>.5)
    # Delayed feeding puts some short-lived A occupancy at accessible distances.
    short_ta=.5;long_tb=10.;flight_time=10.
    short=cascade(flight_time,short_ta,long_tb)
    prompt_occ=math.exp(-flight_time/short_ta)
    delayed_tau=short[1]/short[3]
    check('delayed feeding extends occupancy window',short[1]>prompt_occ*1e6)
    check('ideal DDCM can recover short tau at long flight time',math.isclose(delayed_tau,.5))
    raw=Path('raw/papers/1999_Klemme et al_Lifetimes measurements for 134 Nd and neighboring nuclei with the.pdf')
    check('Klemme raw hash',hashlib.sha256(raw.read_bytes()).hexdigest()=='2a6dfcdac12de9dbf61b2a63c274aed8e286249a3dd28d1a2c6c5a46f1c00604')
    result={'created_at_utc':datetime.now(timezone.utc).isoformat(),
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'ideal branch-one gates, constant velocity, complete corrected components; not finite-foil transport or experimental CI',
      'inputs':{'synthetic_tauA_ps':ta,'v_um_per_ps':v,'feeder_waiting_mixtures_weight_tau_ps':families},
      'gate_rows':rows,'origin_translation_controls':translated,
      'flat_distance_gain_bias':{'reported_distance_gain':gain,'apparent_tau_ps':gained_tau},
      'normalization_controls':{'invented_dlog_exposure_dt_ps_inv':norm_slope,'apparent_tau_ps':wrong,
          'invented_wrong_indirect_alpha':alpha_wrong,'indirect_apparent_tau_ps':wrong_indirect},
      'delayed_feeding_short_lifetime_control':{'tauA_ps':short_ta,'tauB_ps':long_tb,'vacuum_time_ps':flight_time,
          'distance_um':flight_time*v,'v_tauA_um':short_ta*v,'prompt_A_occupancy':prompt_occ,
          'delayed_A_occupancy':short[1],'ideal_DDCM_tau_ps':delayed_tau},
      'required_inputs':['causal direct feeder identity and shifted component purity','consistent I_su and I_ss efficiencies/inventory',
          'exposure normalization before differentiation','indirect alpha in matching intensity units','relative distance gain and independent recoil velocity',
          'finite stopping, deorientation and derivative covariance'],
      'checks':checks,'check_count':len(checks)}
    q.output.parent.mkdir(parents=True,exist_ok=True)
    q.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':len(checks),'gain_tau':gained_tau,'normalization_tau':wrong,
        'alpha_tau':wrong_indirect,'short_tau':result['delayed_feeding_short_lifetime_control']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
