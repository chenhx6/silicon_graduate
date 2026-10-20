#!/usr/bin/env python3
"""SC94 actual calibration/efficiency inputs and independent appendix closure."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def qprime(e):
    a=e/510.99895
    return (1+a)/(1+a+a*a)


def w(a2,p,x):
    return 1+a2*(3*x*x-1)/2+(2*p-a2*(p+3))/(10-6*p)*(35*x**4-30*x*x+3)


def main():
    path=RUN/'schlitt1994-calibration-contract.json'
    c=json.loads(path.read_text())
    rows=[]
    for nucleus,e,eps,seps,p,spol,q,sq in c['calibration_rows']:
        derived=100*eps/p
        sigma=100*math.hypot(seps/p,eps*spol/(p*p))
        fit=qprime(e)*(c['fit_a']+c['fit_b_per_keV']*e)
        rows.append({'identity':[nucleus,e],'Q_replayed_percent':derived,
                     'reported_Q_percent':q,'conditional_diagonal_sigma_Q_percent':sigma,
                     'Q_nominal_printed_fit_percent':100*fit,
                     'fit_comparison_not_new_fit_or_independent_measurement':True})
    x,p,a2=sp.symbols('x p a2',real=True)
    ws=1+a2*(3*x*x-1)/2+(2*p-a2*(p+3))/(10-6*p)*(35*x**4-30*x*x+3)
    derivative=sp.diff(ws,a2)
    polynomial=sp.expand(-(10-6*p)*derivative)
    expected=35*(p+3)*x**4-3*(7*p+35)*x*x+14
    assert sp.simplify(polynomial-expected)==0
    intersection=[]
    for value in c['appendix_P_values']:
        aa=35*(value+3);bb=-3*(7*value+35)
        discriminant=bb*bb-4*aa*14
        y=[(-bb+math.sqrt(discriminant))/(2*aa),(-bb-math.sqrt(discriminant))/(2*aa)]
        angles=[math.degrees(math.acos(math.sqrt(v))) for v in y]
        for xx in [math.sqrt(v) for v in y]:
            assert abs(w(.3,value,xx)-w(.5,value,xx))<2e-14
        literal_y=[-bb/aa,0]
        literal_angles=[math.degrees(math.acos(math.sqrt(min(1,v)))) for v in literal_y]
        ratio=w(.3,value,math.sqrt(y[0]))/w(.3,value,math.sqrt(y[1]))
        approx=1+.6572*value-.0923*value*value
        intersection.append({'P':value,'derived_constant14_angles_deg':angles,
                             'literal_constant0_angles_deg':literal_angles,
                             'constant14_W_ratio_at_intersections':ratio,
                             'printed_Eq30_approximation':approx,
                             'difference_ratio_minus_polynomial':ratio-approx})
    geo=c['declared_geometry_upper_bound_only']
    radius=geo['front_face_diameter_mm']/2
    distance=geo['source_face_distance_mm']
    fraction=(1-distance/math.sqrt(distance*distance+radius*radius))/2
    result={'at':datetime.now(timezone.utc).isoformat(),
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'actual_calibration_rows':rows,
            'Q150_nominal_fit_at4438_percent':100*qprime(4438)*(.304+8.9e-5*4438),
            'raw_null_asymmetry_from_measured_a_if_a_correction_omitted':(1-c['apparatus_a'])/(1+c['apparatus_a']),
            'same_a_sigma_propagated_to_raw_null_A_only':2*c['apparatus_sigma_a']/(1+c['apparatus_a'])**2,
            'relative_coincidence_efficiency_denominator':'detected core singles full-energy peak Ns',
            'absolute_coincidence_efficiency_identity':'epsilon_abs_coinc=epsilon_abs_core_fullpeak*epsilon_relative_coinc',
            'declared_geometry_solid_angle_fraction_upper_bound_only':fraction,
            'upper_bound_times_relative025':fraction*.25,
            'not_original_absolute_efficiency_or_reference_standard_recovered':True,
            'appendix_derived_dWa2_polynomial':str(expected),
            'appendix_intersections':intersection,
            'literal_Eq28_does_not_close_quoted_angle_ranges':True,
            'derived_constant14_closes_Eq27_and_quoted_ranges':True,
            'not_official_erratum_or_executed_appendix_calibration':True,
            'no_actual_covariance_rawcounts_or_new_P_Q_CI':True,'ok':True}
    (RUN/'schlitt1994-calibration-result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
