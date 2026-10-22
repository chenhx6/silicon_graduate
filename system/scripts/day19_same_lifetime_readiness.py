#!/usr/bin/env python3
"""Compare necessary response controls for one invented 20 ps lifetime.

All N, slowing times, amplitude errors and distance errors are synthetic design
inputs. Fisher information refers only to the declared binary survival model,
with calibrated efficiencies and no feeding; it is not an experiment CI.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',required=True,type=Path)
    q=p.parse_args()
    tau=20.0;target_fraction=.05; sigmaF=.005
    checks=[]
    def check(name, ok):
        checks.append({'name':name,'passed':bool(ok)})
        if not ok:raise AssertionError(name)
    dsam=[]
    for slowing,label in [(.3,'synthetic solid slowing'),(20.,'synthetic gas slowing')]:
        F=slowing/(slowing+tau)
        estimate=slowing*(1/F-1)
        relativeFerror=sigmaF/(F*(1-F))
        check('DSAM inversion '+label,math.isclose(estimate,tau))
        # Independently differentiate log(tau(F)) numerically.
        h=1e-7
        derivative=(math.log(slowing*(1/(F+h)-1))-math.log(slowing*(1/(F-h)-1)))/(2*h)
        check('DSAM response derivative '+label,math.isclose(abs(derivative),1/(F*(1-F)),rel_tol=1e-8))
        for scale in [.5,2]:
            check(f'DSAM unknown-clock scaling {label} {scale}',math.isclose((scale*slowing)/(scale*slowing+scale*tau),F))
        dsam.append({'label':label,'slowing_ps':slowing,'F':F,'assumed_absolute_F_standard_error':sigmaF,
            'local_fractional_tau_error_from_F_only':relativeFerror,
            'required_F_error_for_5pct_tau_control':target_fraction*F*(1-F),
            'unknown_slowing_clock_identifiable_from_F_alone':False})
    # Optimal one-distance binary survival information only when distance zero,
    # velocity, amplitudes, efficiencies and feeding response are known.
    lo,hi=.01,3.0
    for _ in range(80):
        x=(lo+hi)/2
        if 2*(1-math.exp(-x))-x>0:lo=x
        else:hi=x
    x=(lo+hi)/2
    info=x*x/math.expm1(x)
    check('optimal point beats characteristic x=1',info>1/math.expm1(1))
    h=1e-5
    fn=lambda y:y*y/math.expm1(y)
    check('optimal point stationary by finite difference',abs((fn(x+h)-fn(x-h))/(2*h))<1e-8)
    beta=.016;v=beta*299.792458;N=10000;d=x*v*tau
    # Fisher parameters are log(tau) and eta=d0/(v*tau_reference).
    def fisher(xs):
        f00=f01=f11=0.0
        for y in xs:
            weight=N/math.expm1(y)
            f00+=weight*y*y;f01+=weight*y;f11+=weight
        return [[f00,f01],[f01,f11]]
    one=fisher([x]);two=fisher([.5,2])
    det=lambda a:a[0][0]*a[1][1]-a[0][1]**2
    check('one distance tau/zero Fisher rank deficient',abs(det(one))<1e-12*one[0][0]*one[1][1])
    check('two distinct distances resolve tau/zero in this model',det(two)>0)
    # Even all distances measure v*tau; they cannot calibrate v independently.
    base_p=math.exp(-d/(v*tau))
    check('velocity lifetime product has exact calibration ridge',math.isclose(math.exp(-d/((v*1.1)*(tau/1.1))),base_p))
    rdds={'beta':beta,'v_um_per_ps':v,'characteristic_distance_vtau_um':v*tau,
          'conditional_optimum_x':x,'conditional_optimum_distance_um':d,
          'survival_at_optimum':math.exp(-x),'invented_total_counts_per_distance':N,
          'conditional_fractional_CR_lower_bound_known_nuisances':1/math.sqrt(N*info),
          'invented_delta_distance_um':1.0,'fractional_tau_sensitivity_at_x1':1/(v*tau),
          'fractional_tau_sensitivity_at_optimum':1/d,
          'Fisher_one_distance':one,'Fisher_two_distances':two,
          'velocity_separate_measurement_required':True}
    sigma=80.0
    timing_sigma_tau=.5*math.sqrt(2*(sigma*sigma+tau*tau)/N)
    timing={'Gaussian_PRF_sigma_ps':sigma,'invented_independent_counts_per_branch':N,
            'conditional_statistical_tau_standard_error_ps':timing_sigma_tau,
            'required_PRD_bias_bound_ps_for_5pct_tau_if_other_errors_zero':2*target_fraction*tau,
            'source_8ps_PRD_2sigma_sensitivity_ps':8/2,
            'source_convention_is_not_assumed_single_sigma':True,
            'finite_time_window_and_role_tag_required':True}
    check('timing PRD coefficient is one half',timing['required_PRD_bias_bound_ps_for_5pct_tau_if_other_errors_zero']==2)
    check('counts alone do not remove PRD calibration sensitivity',timing_sigma_tau<4)
    result={'created_at_utc':datetime.now(timezone.utc).isoformat(),
      'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'scope':'one lifetime, necessary design sensitivities only; not overall method ranking, actual performance or fitted CI',
      'inputs':{'invented_tau_ps':tau,'target_fractional_control':target_fraction,'feeding':False},
      'DSAM':dsam,'RDDS':rdds,'FastTiming':timing,
      'decision':'RDDS enters evaluation if its distance/velocity/SH-US calibration exists; gas DSAM needs density/stopping clock; timing needs valid role tags, windows and tighter pair PRD. Missing actual inputs remains readiness, not an awarded precision.',
      'checks':checks,'check_count':len(checks)}
    q.output.parent.mkdir(parents=True,exist_ok=True)
    q.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':len(checks),'DSAM':dsam,'RDDS_optimum':rdds['conditional_optimum_distance_um'],'Timing':timing},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
