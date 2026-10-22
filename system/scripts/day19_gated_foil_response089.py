#!/usr/bin/env python3
"""Gated DDCM versus single-survival slopes: declared counterexamples only.

No original spectra, fit, confidence interval, stopping job or acceptance model
is reconstructed. Suzuki Eq1's continuous-derivative limit is used for a
branch-one two-level cascade, with an explicitly assumed finite foil interval.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import math
import hashlib

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01'


def integrate(f, lo, hi, n=4000):
    h=(hi-lo)/n
    return h/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*h) for i in range(1,n)))


def cascade(t, ta, tb):
    """B survival, A occupancy, and A-decayed CDF at pre-foil time t."""
    if t<0 or min(ta,tb)<=0:raise ValueError('nonnegative time and positive rates required')
    b=math.exp(-t/tb)
    if ta==tb:a=t/ta*b
    else:a=ta/(tb-ta)*(b-math.exp(-t/ta))
    return b,a,1-b-a


def main():
    checks=[]
    def check(name,ok):
        checks.append({'name':name,'passed':bool(ok)})
        if not ok:raise AssertionError(name)
    # Source paper central velocities; no assumption that isotope labels swap.
    source={'103Rh':{'beta_before':.051,'beta_after':.031},
            '104Rh':{'beta_before':.057,'beta_after':.033},
            'degrader_areal_mass_mg_cm2':3.5,'degrader_material':'93Nb',
            'source_stated_max_transit_ps':.2,'source_distances_um_range':[8,100],
            'source_number_of_distances':7,
            '103Rh_29over2plus_tau_ps':.72,'104Rh_13minus_tau_ps':.71}
    cases=[]
    # ta,tb and ts are declared designs; ts=.16ps is not a source measurement.
    ta,tb,ts=2.,10.,.16
    k=math.exp(-ts/ta)
    for t in [1.,2.,4.,8.,16.,40.]:
        b,a,f=cascade(t,ta,tb)
        da=b/tb-a/ta
        df=a/ta
        n=a+f  # selecting B decayed before reaching foil, not fixed total yield
        dn=b/tb
        slow_lost_bridge=k*a
        fast_lost_bridge=f
        bridge=(1-k)*a
        gated_full=a/df
        gated_lost=slow_lost_bridge/df
        survival_log=-slow_lost_bridge/(k*da)
        norm_fast=f/n
        norm_slow=a/n
        derivative_norm_fast=(df*n-f*dn)/(n*n)
        normalized_estimate=norm_slow/derivative_norm_fast
        # Distinct numerical integral for A occupancy and finite-difference CDF.
        quad=integrate(lambda u:math.exp(-u/tb)/tb*math.exp(-(t-u)/ta),0,t)
        h=1e-4
        dnum=(cascade(t+h,ta,tb)[2]-cascade(t-h,ta,tb)[2])/(2*h)
        check(f'occupancy integral matches analytic at {t}',abs(quad-a)<1e-11)
        check(f'CDF derivative matches occupancy over ta at {t}',abs(dnum-df)<1e-10)
        check(f'full gate-conditioned inventory at {t}',abs(f+bridge+slow_lost_bridge-(1-b))<1e-14)
        check(f'ideal direct-gate identity at {t}',abs(gated_full-ta)<1e-13)
        check(f'bridge lost changes gated ratio by k at {t}',abs(gated_lost/ta-k)<1e-13)
        check(f'self-normalization changes selected-gate response at {t}',abs(normalized_estimate-ta)>.001)
        cases.append({'time_before_foil_ps':t,'B_survival':b,'A_occupancy':a,'A_CDF':f,
                      'gate_selected_total':n,'d_selected_total_dt':dn,
                      'bridge':bridge,'slow_if_bridge_lost':slow_lost_bridge,
                      'ideal_gated_ratio_ps':gated_full,'gated_lost_bridge_ratio_ps':gated_lost,
                      'single_slow_log_slope_time_ps':survival_log,
                      'normalizing_by_selected_total_ratio_ps':normalized_estimate})
    check('single slow-component slope can be negative while population builds',cases[1]['single_slow_log_slope_time_ps']<0)
    check('late slow-component slope follows feeder rather than A lifetime',abs(cases[-1]['single_slow_log_slope_time_ps']-tb)<.01)
    # Prompt, single exponential is the special case where the two estimators
    # can be confused: k cancels in a log slope, but not in u / fast derivative.
    t,ta_prompt=.8,.72
    kp=math.exp(-ts/ta_prompt);ap=math.exp(-t/ta_prompt)
    prompt={'ta_ps':ta_prompt,'synthetic_ts_ps':ts,
            'single_slow_log_slope_ps':-kp*ap/(-kp*ap/ta_prompt),
            'gated_lost_bridge_ratio_ps':kp*ap/(ap/ta_prompt),
            'survival_factor':kp}
    check('prompt log slope recovers ta even when bridge lost',abs(prompt['single_slow_log_slope_ps']-ta_prompt)<1e-14)
    check('same prompt lost bridge fails gate-ratio estimator',prompt['gated_lost_bridge_ratio_ps']<ta_prompt)
    # A depth- and acceptance-dependent slow fraction destroys even prompt
    # constant-amplitude cancellation. This is a synthetic response gradient.
    lam=1.5;eps=.03
    g=lambda x:math.exp(-x/lam)*(1+eps*x)
    x=1.;dx=1e-5
    ds=(math.log(g(x+dx))-math.log(g(x-dx)))/(2*dx)
    check('distance-dependent efficiency spoils single-exponential log slope',abs(-1/ds-lam)>.01)
    # Source velocity bounds do not give actual foil thickness/transit producer.
    c=299.792458
    v1=.051*c;v2=.031*c
    old_assumed_thickness_um=2.
    old_time=old_assumed_thickness_um/((v1+v2)/2)
    # Explicit density control only, not a claim about actual foil properties.
    rho_design=8.57
    areal=source['degrader_areal_mass_mg_cm2']*1e-3
    thickness_control=areal/rho_design*1e4
    minimum_transit_control=thickness_control/v1
    check('old two-micron calculation is a separate assumed thickness',abs(old_time-.16271419278)<1e-9)
    check('declared density gives different thickness from old script',thickness_control>4 and minimum_transit_control>.2)
    # Conservation of B+A+decays is valid even at equal lifetimes.
    for ta0,tb0 in [(2.,2.),(2.,10.),(10.,2.)]:
        b0,a0,f0=cascade(3.,ta0,tb0)
        check(f'cascade probability conservation {ta0},{tb0}',abs(b0+a0+f0-1)<1e-14 and min(b0,a0,f0)>=0)
    src=ROOT/'raw/papers/2008_Suzuki et al_Lifetime measurement of candidate chiral doublet bands in the Rh 103 , 104.pdf'
    result={'created_at_utc':datetime.now(timezone.utc).isoformat(),
            'session_id':'01a15dcc-49f9-7623-b0e9-75fd73c74a80',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
            'scope':'branch-one selected-feeder nonrelativistic rate design; no original fit or experimental bias estimate',
            'source_inputs':source,
            'synthetic_inputs':{'tau_A_ps':ta,'tau_B_ps':tb,'foil_interval_ps':ts,
                'feeding_at_reaction':'B only','gate':'B emitted before foil',
                'normalization':'independent reference unless explicitly self-normalized',
                'bridge_case':'A in-foil decay can be fully included or entirely excluded as declared',
                'all_other_efficiencies':1.},
            'cascade_controls':cases,'prompt_control':prompt,
            'foil_arithmetic_control':{'old_assumed_thickness_um':old_assumed_thickness_um,'old_time_ps':old_time,
                'rho_design_g_cm3':rho_design,'thickness_from_areal_mass_and_design_density_um':thickness_control,
                'minimum_time_with_design_density_and_v_before_ps':minimum_transit_control,
                'boundary':'Apparent tension in these added arithmetic assumptions does not identify the actual producer or establish a source erratum.'},
            'checks':checks,'check_count':len(checks),'all_checks_passed':all(x['passed'] for x in checks),
            'missing_inputs':['actual finite-foil trajectory and thickness/geometry calibration',
                'role-specific bridge ROI and SH/slow acceptance versus distance',
                'normalization reference and shared errors of distance-bin derivative',
                'direct/indirect feeder gate purity and alpha covariance']}
    (RUN/'gated-foil-response-result-089.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':len(checks),'all_passed':result['all_checks_passed'],
                      'prompt_control':prompt,'selected_cases':[cases[1],cases[3],cases[-1]],
                      'foil_control':result['foil_arithmetic_control']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
