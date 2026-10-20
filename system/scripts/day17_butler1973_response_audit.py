#!/usr/bin/env python3
"""B73 literal P/A/Q, actual seven-row calibration, and declared count design."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def asymmetry(perp, parallel, a):
    return (a*perp-parallel)/(a*perp+parallel)


def main():
    path=RUN/'butler1973-calibration-contract.json'
    c=json.loads(path.read_text())
    out=[]
    for row in c['rows']:
        nuc,ex,eg,em,a2,s2,a4,s4,p,sp,a,sa,q,sq=row
        q_replay=a/p
        diag_sigma_q=math.hypot(sa/p,a*sp/(p*p))
        # Cov(A,P) is not supplied; this is a conditional first-order bound.
        sigma_q_range=[abs(sa/p-abs(a)*sp/(p*p)),sa/p+abs(a)*sp/(p*p)]
        energy=eg/1000
        ratio=1/(1+energy/.51099895)
        qp=1/(1/ratio+ratio-1)
        point=None
        if em=='E2':
            d=1-a2/2+3*a4/8
            point=(1.5*a2+.625*a4)/d
        out.append({'identity':[nuc,ex,eg,em],'Q_A_over_P':q_replay,
                    'Q_reported':q,'conditional_diagonal_sigma_Q':diag_sigma_q,
                    'conditional_local_sigma_Q_range_unknown_Cov':sigma_q_range,
                    'Qprime_point_KN90':qp,'Q_nominal_original_B084_C0':.84*qp,
                    'Q_reported_over_Qprime':q/qp,
                    'nominal_normalized_pureE2_pointP90_not_paper_producer':point,
                    'pointP90_over_one_preserved_not_clipped':point is not None and point>1})
    d=c['design_counts_only']
    x,y,a=d['Nperp'],d['Nparallel'],d['a']
    den=a*x+y
    gradient=[2*a*y/den**2,-2*a*x/den**2,2*x*y/den**2]
    variables=[x,y,a]
    steps=[.01,.01,1e-6]
    numerical=[]
    for i,h in enumerate(steps):
        plus=variables.copy();minus=variables.copy()
        plus[i]+=h;minus[i]-=h
        value=(asymmetry(*plus)-asymmetry(*minus))/(2*h)
        numerical.append(value)
        assert abs(value-gradient[i])<2e-10
    aa=asymmetry(x,y,a)
    assert abs(asymmetry(y,x,1/a)+aa)<1e-14
    assert asymmetry(x,a*x,a)==0
    assert abs(asymmetry(3*x,3*y,a)-aa)<1e-14
    sigma_a=a*d['sigma_a_relative']
    variance_counts=gradient[0]**2*x+gradient[1]**2*y
    variance_a=gradient[2]**2*sigma_a**2
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'actual_seven_calibration_rows':out,
            'design_count_example':{'A':aa,'P_if_Q_fixed':aa/d['Q'],'gradient_Nperp_Nparallel_a':gradient,
                                    'finite_difference_gradient':numerical,
                                    'conditional_sigma_A_count_only':math.sqrt(variance_counts),
                                    'conditional_sigma_A_a_only':math.sqrt(variance_a),
                                    'conditional_sigma_A_independent_design':math.sqrt(variance_a+variance_counts),
                                    'actual_B73_counts_or_CI':False},
            'literal_Eq4_is_P_A_over_Q_no_extra_alpha_denominator':True,
            'count_gradient_label_swap_null_scale_controls':True,
            'no_pointP_clipped_or_Qfit_refitted':True,
            'no_actual_covariance_counts_or_efficiency_imputed':True,
            'not_matching_WA77_actual_response_attestation':True,'ok':True}
    (RUN/'butler1973-calibration-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
