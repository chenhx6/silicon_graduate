#!/usr/bin/env python3
"""Derived E2/M1 ratio vector: transformed inputs, not independent evidence."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day24_preview_mu07_inventory_hypothesis import coefficients


def transform(y,d,k,ell):
    return np.array([k*y*d*d/(1+d*d),ell*y/(1+d*d)])


def jacobian(y,d,k,ell):
    return np.array([[k*d*d/(1+d*d),2*k*y*d/(1+d*d)**2],
                     [ell/(1+d*d),-2*ell*y*d/(1+d*d)**2]])


def inverse(e,m,k,ell):
    y=e/k+m/ell
    return y,(e/k)/(m/ell)


def correlation(cov):
    return float(cov[0,1]/math.sqrt(cov[0,0]*cov[1,1]))


def calculate():
    cm,ce,_,_=coefficients()
    eo,ed=.8132,.7260;x=6.4/3.7;d=-.37;h=1.;y=x/h
    k=(ed/eo)**5;ell=(ce/cm)*ed**5/eo**3
    centre=transform(y,d,k,ell);j=jacobian(y,d,k,ell)
    controls={};max_inverse=max_det=max_sign=max_fd=max_convergence=0.
    for yy in [.5,y,3.]:
        for dd in [-2.,-.5,-.37,0.,.37,.5,2.]:
            e,m=transform(yy,dd,k,ell);yi,di2=inverse(e,m,k,ell)
            max_inverse=max(max_inverse,abs(yi-yy),abs(di2-dd*dd))
            max_sign=max(max_sign,float(np.max(abs(transform(yy,dd,k,ell)-transform(yy,-dd,k,ell)))))
            ja=jacobian(yy,dd,k,ell)
            determinant=-2*k*ell*yy*dd/(1+dd*dd)**2
            max_det=max(max_det,abs(float(np.linalg.det(ja))-determinant))
            def finite(step):
                return np.column_stack([(transform(yy+step,dd,k,ell)-transform(yy-step,dd,k,ell))/(2*step),
                                        (transform(yy,dd+step,k,ell)-transform(yy,dd-step,k,ell))/(2*step)])
            fd1,fd2=finite(1e-4),finite(5e-5)
            max_fd=max(max_fd,float(np.max(abs(fd2-ja))))
            max_convergence=max(max_convergence,float(np.max(abs(fd2-fd1))))
    controls['exact_photon_fraction_inverse_recovers_same_inputs']=max_inverse<1e-12
    controls['derived_B_vector_is_even_in_delta']=max_sign<1e-13
    controls['analytic_J_determinant_matches']=max_det<1e-13
    controls['analytic_J_matches_finite_difference']=max_fd<1e-7
    controls['finite_difference_step_halving_converges']=max_convergence<1e-7
    controls['nonzero_delta_map_has_local_rank2']=abs(float(np.linalg.det(j)))>1e-3
    controls['delta_zero_map_loses_a_local_dimension']=np.linalg.matrix_rank(jacobian(y,0,k,ell),tol=1e-12)==1
    controls['common_denominator_purity_rescales_both']=bool(np.allclose(transform(x/.5,d,k,ell),2*centre,atol=1e-13))
    yh,di2=inverse(*transform(x/.5,d,k,ell),k,ell)
    controls['inverse_with_unknown_purity_recovers_y_not_count_ratio']=abs(yh-2*x)<1e-13 and abs(yh-x)>.1 and abs(di2-d*d)<1e-13
    cov_y=j@np.diag([1.,0.])@j.T
    cov_d=j@np.diag([0.,1.])@j.T
    controls['y_only_differential_covariance_rank1_positive_corr']=np.linalg.matrix_rank(cov_y,tol=1e-12)==1 and abs(correlation(cov_y)-1)<1e-12
    controls['delta_only_differential_covariance_rank1_negative_corr']=np.linalg.matrix_rank(cov_d,tol=1e-12)==1 and abs(correlation(cov_d)+1)<1e-12
    controls['phase_sign_not_recovered_from_B_inverse']=abs(inverse(*transform(y,d,k,ell),k,ell)[1]-d*d)<1e-13 and bool(np.allclose(transform(y,d,k,ell),transform(y,-d,k,ell)))
    return {'status':'source-bound-derived-vector-dependency-control','formal_day_index':23,
            'source_input_role':{'source':'L22 mainTable1/SITable1, sourcealreadyread/hashpreserved',
                'E_out_MeV':eo,'E_den_MeV':ed,'I_gamma_out':6.4,'I_gamma_den':3.7,
                'quoted_delta_centre':d,'denominator_E2_photon_fraction_assumption':h,
                'source_reported_rE2_centre':.12,'source_reported_rM1_centre':.4,
                'new_experimental_information':False},
            'model':'M1/E2 photon truncation, y=(Iout/Iden)/h_E2den; e=K*y*d2/(1+d2),m=L*y/(1+d2). Same-parent scale/tau cancelled only within this quantity contract.',
            'coefficients':{'K_dimensionless':k,'L_muN2_over_e2b2':ell,'C_E2_over_C_M1_declared_formula_units':ce/cm},
            'conditional_central_arithmetic':{'y':y,'rE2':float(centre[0]),'rM1_muN2_over_e2b2':float(centre[1]),
                'inverse_y_same_input_control':inverse(*centre,k,ell)[0],
                'inverse_delta_squared_same_input_control':inverse(*centre,k,ell)[1],
                'not_new_delta_extraction_or_original_producer_verification':True},
            'local_J_rows_e_m_columns_y_delta':j.tolist(),'local_determinant':float(np.linalg.det(j)),
            'covariance_formula':'Sigma_derived=J Sigma_(y,delta) J^T locally; actual Sigma is not supplied/assigned.',
            'actual_joint_covariance':None,'actual_ratio_confidence_interval':None,
            'differential_coordinate_designs_not_experimental_errors':{
                'unit_y_variance_delta_fixed_output_correlation':correlation(cov_y),
                'unit_delta_variance_y_fixed_output_correlation':correlation(cov_d),
                'scope':'Unit coordinate variances are rank/direction controls of a differential map only, not nuclear error magnitudes, distribution assumptions or real correlations.'},
            'control_errors':{'max_inverse_error':max_inverse,'max_delta_sign_invariance_error':max_sign,
                'max_determinant_error':max_det,'max_J_finite_difference_error':max_fd,
                'max_J_step_halving_difference':max_convergence},
            'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
                Path(__file__).with_name('day24_preview_mu07_inventory_hypothesis.py')]},
            'limitations':['The two derived strengths are a transformation of the same intensity/mixing inputs. Adding their separate printed errors/fit agreement as new independent evidence would ignore their common genealogy/covariance.',
                           'The B-ratio vector loses delta sign even when locally invertible within one nonzero-sign branch. It cannot recover relative multipole phase without interference-sensitive inputs.',
                           'Unknown denominator E2 purity h introduces a common scale. The inverse gives y=x/h, not an independently measured photon-count ratio or h/delta_den estimate.',
                           'The source central arithmetic is not a fit, a reconstruction of the actual published covariance/likelihood or an extra experimental validation; no marginal errors are silently made Gaussian.',
                           '747/526 is a pair of different cross-band outlets, not the sameband denominator;526 multipolarity/Rac is blank in SI, so its pureE2 adoption remains conditional. No unreported747 rM1 is filled as a measurement.',
                           'No new physicaldelta/g/Q/tau/CI/rate/beamtime and no universalM1/E2 cutoff or equal-valley claim. OnlyoriginalDay23 andalreadyopenedDay24uncreditedpreview, noDay25+.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate();a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'central_arithmetic':r['conditional_central_arithmetic'],'J':r['local_J_rows_e_m_columns_y_delta'],
                      'controls':r['controls'],'errors':r['control_errors']},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
