#!/usr/bin/env python3
"""Synthetic RDDS component-inventory controls, not a foil-transport simulation.

Vacuum decay S, slowing-tail T and fully stopped U are partitioned using a fixed
invented stopper transit time. This tests peak-assignment and normalization;
it does not infer the actual Radeck/Klemme stopping time or distance producer.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def inventory(tf, tau, ts):
    if tf < 0 or tau <= 0 or ts < 0:
        raise ValueError('nonnegative times and positive lifetime required')
    at_foil=math.exp(-tf/tau)
    return (-math.expm1(-tf/tau),at_foil*(-math.expm1(-ts/tau)),
            at_foil*math.exp(-ts/tau))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True,type=Path)
    q=p.parse_args()
    tau,ts=2.0,1.0
    checks=[]
    def check(name,ok):
        checks.append({'name':name,'passed':bool(ok)})
        if not ok:raise AssertionError(name)
    rows=[]
    for tf in [0,.25,.5,1,2,4,8,20]:
        S,T,U=inventory(tf,tau,ts)
        z=math.exp(-tf/tau)
        check(f'complete inventory t={tf}',math.isclose(S+T+U,1,abs_tol=1e-14))
        check(f'nonnegative inventory t={tf}',min(S,T,U)>=0)
        complete_US=(T+U)/(S+T+U)
        drop_tail=U/(S+U)
        check(f'full tail in US recovers vacuum survival t={tf}',math.isclose(complete_US,z,abs_tol=1e-14))
        check(f'no-tail limit recovers survival t={tf}',math.isclose(
            inventory(tf,tau,0)[2],z,abs_tol=1e-14))
        k=math.exp(-ts/tau)
        denominator=1-(1-k)*z
        check(f'dropping tail has rational survival t={tf}',math.isclose(drop_tail,k*z/denominator,abs_tol=1e-14))
        # The local log-slope time is tau*(1-(1-k)*z), not the true tau.
        rows.append({'vacuum_time_ps':tf,'S_vacuum':S,'T_slowing':T,'U_stopped':U,
                     'full_tail_US_survival':complete_US,'tail_dropped_survival':drop_tail,
                     'tail_dropped_local_log_slope_time_ps':tau*denominator,
                     'naive_point_tau_tail_dropped_ps':-tf/math.log(drop_tail) if tf>0 else None})
    offsets=[]
    for qt in [0,.3,1]:
        # qT of the tail assigned to US, remaining (1-q)T to SH; no count dropped.
        C=qt+(1-qt)*math.exp(-ts/tau)
        offset_time=-tau*math.log(C)
        for tf in [.5,2,8]:
            S,T,U=inventory(tf,tau,ts)
            R=(U+qt*T)/(S+T+U)
            check(f'tail allocation is constant-amplitude model q={qt} tf={tf}',math.isclose(R,C*math.exp(-tf/tau),abs_tol=1e-14))
            check(f'constant amplitude aliases origin q={qt} tf={tf}',math.isclose(R,math.exp(-(tf+offset_time)/tau),abs_tol=1e-14))
        offsets.append({'tail_fraction_assigned_US':qt,'survival_amplitude_C':C,
            'equivalent_additional_vacuum_time_ps':offset_time,
            'equivalent_distance_at_beta016_um':offset_time*.016*299.792458,
            'equivalent_distance_at_beta045_um':offset_time*.045*299.792458})
    check('different peak assignments need different effective origins',offsets[0]['equivalent_additional_vacuum_time_ps']>offsets[1]['equivalent_additional_vacuum_time_ps']>offsets[2]['equivalent_additional_vacuum_time_ps'])
    check('tail-drop endpoints do not certify correct response',math.isclose(rows[0]['tail_dropped_survival'],1) and rows[-1]['tail_dropped_survival']<1e-4 and rows[4]['tail_dropped_local_log_slope_time_ps']<tau)
    # Independent finite-difference derivative verifies the analytic local slope.
    for tf in [.5,2,8]:
        def observed(t):
            S,T,U=inventory(t,tau,ts)
            return U/(S+U)
        h=1e-4
        derivative=(math.log(observed(tf+h))-math.log(observed(tf-h)))/(2*h)
        analytic=tau*(1-(1-math.exp(-ts/tau))*math.exp(-tf/tau))
        check(f'independent derivative of tail-drop survival tf={tf}',math.isclose(-1/derivative,analytic,rel_tol=1e-8))
    raw=Path('raw/papers/2012_Radeck et al_Simultaneous deorientation and lifetime measurement in 98 Ru using the recoil distance Doppler shift.pdf')
    check('Radeck raw hash',hashlib.sha256(raw.read_bytes()).hexdigest()=='21ed965eb3fd0f57059d2bfe3367ecc39fa6cc2761b1f23ec95875d1a6fe3642')
    result={'created_at_utc':datetime.now(timezone.utc).isoformat(),
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'inputs':{'synthetic_tau_ps':tau,'synthetic_stopper_interval_ps':ts,'feeding':False,
                'vacuum_time_is_physical_not_paper_relative_distance':True},
      'scope':'component counting/normalization design only; no microscopic stopping, actual job, lifetime fit or CI',
      'rows':rows,'tail_allocation_origin_alias':offsets,
      'source_contracts':['Radeck2012 PDF3 slowing tail explicitly added to US','Nolan1979 PDF38 Sec2.4.3 constant finite-stopping factor with no feeding'],
      'required_companions':['zero-distance full lineshape and integration inventory','shifted/unshifted/tail acceptance and normalization','independent mechanical zero versus response-induced effective origin','per-ring/energy efficiencies and feeding/velocity distributions'],
      'checks':checks,'check_count':len(checks)}
    q.output.parent.mkdir(parents=True,exist_ok=True)
    q.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':len(checks),'offsets':offsets,'tf2_row':rows[4]},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
