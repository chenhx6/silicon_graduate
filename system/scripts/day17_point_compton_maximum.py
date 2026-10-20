#!/usr/bin/env python3
"""Global single-Compton analyzing maximum vs the 90-degree reference."""
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def point(alpha,mu):
    t=1+alpha*(1-mu)
    return (1-mu*mu)/(t+1/t-1+mu*mu)


def optimum(alpha):
    if alpha==0:
        return 0.,1.
    def polynomial(w):
        return (4*w**4+(12+8*alpha)*w**3+(12+16*alpha+2*alpha**2)*w*w
                +(4+8*alpha)*w-alpha*alpha*(2+alpha))
    low,high=0.,1.
    while polynomial(high)<=0:
        high*=2
    for _ in range(150):
        middle=(low+high)/2
        if middle==low or middle==high:
            break
        if polynomial(middle)>0:
            high=middle
        else:
            low=middle
    w=(low+high)/2;mu=w/(1+w)
    return mu,point(alpha,mu)


def main():
    path=RUN/'pointQ-contract.json';c=json.loads(path.read_text())
    aa=sp.Symbol('alpha',positive=True);mu,w=sp.symbols('mu w',real=True)
    t=1+aa*(1-mu);den=t+1/t-1+mu**2
    q=(1-mu**2)/den
    numerator=aa*(1-mu**2)*(t*t-1)-2*mu*(t**3+t)
    assert sp.simplify(sp.diff(q,mu)-numerator/(t*t*den*den))==0
    quartic=4*w**4+(12+8*aa)*w**3+(12+16*aa+2*aa**2)*w*w+(4+8*aa)*w-aa**2*(2+aa)
    assert sp.simplify(-numerator.subs(mu,w/(1+w))*(1+w)**4-quartic)==0
    coefficients=sp.Poly(quartic,w).all_coeffs()
    assert all(x.is_positive for x in coefficients[:-1]) and coefficients[-1].is_negative
    assert sp.simplify(q.subs(mu,0)-(1+aa)/(1+aa+aa*aa))==0
    assert sp.simplify(numerator.subs(mu,0)-aa**2*(2+aa))==0
    rows=[];rest=c['electron_mass_energy_keV']
    for energy in c['gamma_grid_keV']:
        alpha=energy/rest;best,maximum=optimum(alpha)
        q90=(1+alpha)/(1+alpha+alpha*alpha)
        assert maximum>=q90-5e-15 and 0<=best<1 and 0<maximum<=1
        rows.append({'Egamma_keV':energy,'alpha':alpha,'theta_max_deg':math.degrees(math.acos(best)),
                     'single_point_qmax':maximum,'q90_reference':q90,'qmax_over_q90':maximum/q90})
    cutrows=[]
    for energy,threshold in c['single_scatter_two_hit_threshold_examples_keV']:
        row={'Egamma_keV':energy,'each_hit_min_keV':threshold,'point_only_not_detector_efficiency':True}
        if energy<2*threshold:
            row['single_collision_two_hit_feasible']=False
            row['reason']='insufficient total energy'
        else:
            low=max(-1.,1-rest*(1/threshold-1/energy))
            high=min(1.,1-rest*threshold/(energy*(energy-threshold)))
            row['single_collision_two_hit_feasible']=low<=high
            if low<=high:
                best,_=optimum(energy/rest);clamped=min(max(best,low),high)
                eprime=energy/(1+energy/rest*(1-clamped))
                assert eprime>=threshold-1e-10 and energy-eprime>=threshold-1e-10
                row.update({'theta_min_deg':math.degrees(math.acos(high)),
                            'theta_max_deg':math.degrees(math.acos(low)),
                            'best_allowed_theta_deg':math.degrees(math.acos(clamped)),
                            'best_allowed_q':point(energy/rest,clamped),
                            'Eprime_keV_at_optimum':eprime})
            else:
                row['reason']='energy exceeds 2T but one-collision kinematics cannot satisfy both hits'
        cutrows.append(row)
    alow=1e-4;slow,_=optimum(alow)
    low_ratio=(math.pi/2-math.acos(slow))/alow**2
    ahigh=1e8;shigh,qhigh=optimum(ahigh)
    high_ratio=qhigh/point(ahigh,0)
    assert abs(low_ratio-.5)<.001 and abs(high_ratio-2)<.002
    result={'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
        'stationary_quartic':str(quartic),'unique_positive_root_by_Descartes':True,
        'negative_mu_derivative':'both terms of numerator positive for -1<mu<0, alpha>0',
        'source_q90_exact_control':True,'global_point_rows':rows,'two_hit_threshold_controls':cutrows,
        'asymptotic_controls':{'small_alpha_angle_shift_over_alpha2':low_ratio,'large_alpha_qmax_over_q90':high_ratio},
        'single_scatter_not_full_transport_or_FOM':True,
        'no_actual_Qrel_or_calibration_counts_CI_changed':True,'ok':True}
    (RUN/'pointQ-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'rows':rows,'threshold_controls':cutrows,'asymptotic':result['asymptotic_controls']},indent=2))


if __name__=='__main__':
    main()
