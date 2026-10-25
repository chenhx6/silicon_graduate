#!/usr/bin/env python3
"""Declared KS/RB/native photon-coordinate bridge, no spectroscopy data fit."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_halfspin_singles_response import LINEAR,photon_parts,population,ideal_pair


def amplitude(two_i,two_f,coordinate,theta,basis):
    m1,e2=photon_parts(two_i,two_f,theta)
    if basis=='RB':return (m1+coordinate*e2)/math.sqrt(1+coordinate*coordinate)
    if basis=='native_rank_phase':return (-m1+coordinate*e2)/math.sqrt(1+coordinate*coordinate)
    raise ValueError('Unsupported explicitly declared photon basis')


def density(a,weights):
    return np.einsum('hfi,i,kfi->hk',a,weights,a.conj())


def iquv(rho):
    linear=LINEAR@rho@LINEAR.T.conj()
    return np.array([np.trace(linear).real,(linear[0,0]-linear[1,1]).real,
                     2*linear[0,1].real,-2*linear[0,1].imag])


def calculate():
    max_global=max_density=max_stokes=max_pure=max_axis=max_psd_defect=0.
    wrong_difference=0.;points=0
    for two_i in [3,11,17,21]:
        for delta_ks_design in [-2.,-.5,0.,.5,2.]:
            d_rb=-delta_ks_design
            for width in [.2,.4,.8]:
                w=population(two_i,width)
                for angle in [0.,.37,math.pi/2,math.radians(154),math.pi]:
                    rb=amplitude(two_i,two_i-2,d_rb,angle,'RB')
                    native=amplitude(two_i,two_i-2,delta_ks_design,angle,'native_rank_phase')
                    wrong=amplitude(two_i,two_i-2,d_rb,angle,'native_rank_phase')
                    rho=density(rb,w);rn=density(native,w);rw=density(wrong,w)
                    max_global=max(max_global,float(np.max(abs(rb+native))))
                    max_density=max(max_density,float(np.max(abs(rho-rn))))
                    max_stokes=max(max_stokes,float(np.max(abs(iquv(rho)-iquv(rn)))))
                    wrong_difference=max(wrong_difference,float(np.max(abs(rho-rw))))
                    max_psd_defect=max(max_psd_defect,float(-np.linalg.eigvalsh(rho)[0]))
                    linear=LINEAR@rho@LINEAR.T.conj();swap=np.array([[0,1],[1,0]])
                    swapped=swap@linear@swap
                    max_axis=max(max_axis,abs(float(np.trace(swapped).real)-iquv(rho)[0]),
                                  abs(float((swapped[0,0]-swapped[1,1]).real)+iquv(rho)[1]))
                    for pure in photon_parts(two_i,two_i-2,angle):
                        max_pure=max(max_pure,float(np.max(abs(density(pure,w)-density(-pure,w)))))
                    points+=1
    controls={'proper_coordinate_map_is_one_global_phase':max_global<1e-13,
              'full_complex_photon_density_basis_invariant':max_density<1e-13,
              'all_IQUV_basis_invariant':max_stokes<1e-13,
              'pure_limits_blind_to_relative_multipole_phase_change':max_pure<1e-13,
              'unmapped_coordinate_changes_mixed_interference':wrong_difference>.1,
              'linear_axis_label_swap_flips_P_preserves_W':max_axis<1e-13,
              'all_checked_photon_densities_positive':max_psd_defect<1e-12}
    pure_rows=[]
    for kind,two_f,index in [('stretched_E2',13,1),('stretched_M1',15,0)]:
        pure=photon_parts(17,two_f,math.pi/2)[index]
        z=iquv(density(pure,population(17,.2)))
        p=float(z[1]/z[0])
        pure_rows.append({'kind_design':kind,'two_I':17,'two_If':two_f,'sigma_over_I_design':.2,
                          'theta_design_deg':90,'local_Efield_P_parallel_minus_perp':p})
    controls['chosen_lowM_stretched_E2_Efield_positive']=pure_rows[0]['local_Efield_P_parallel_minus_perp']>0
    controls['chosen_lowM_stretched_M1_Efield_negative']=pure_rows[1]['local_Efield_P_parallel_minus_perp']<0
    rows=[]
    for two_i,energy,reported_delta,reported_p,reported_r in [(17,747.3,-.47,.04,.37),(21,813.2,-.37,-.03,.48)]:
        values=[]
        for width in [.2,.4,.8]:
            r,p=ideal_pair(two_i,-reported_delta,width)
            values.append({'declared_Gaussian_input_sigma_over_I':width,
                           'ideal_point_W154_over_W90':float(r),'ideal_local_Efield_P90':float(p),
                           'not_actual_Rac_or_P_refit':True})
        rows.append({'source_line_energy_keV':energy,'two_I_source':two_i,'source_reported_delta_centre':reported_delta,
                     'source_reported_P_centre':reported_p,'source_reported_Rac_centre':reported_r,
                     'extra_unverified_application_assumption':'Use this exact LKH82 KS emission convention for the quoted source delta; original analysis producer convention not reconstructed.',
                     'conditional_d_RB_equals_minus_delta_KS':-reported_delta,'declared_width_forward_examples':values,
                     'fitted_width':None,'real_joint_likelihood_or_confidence_interval':None,
                     'boundary':'Single-photon point-angle examples, not the original Pr angle-ring groups/upstream gates/finite-array efficiency/feeding/attenuation response. Central numerical proximity is not experimental reproduction or root selection.'})
    controls['chosen_small_negative_KS747_can_have_positive_local_P']=all(v['ideal_local_Efield_P90']>0 for v in rows[0]['declared_width_forward_examples'])
    controls['chosen_small_negative_KS813_can_have_negative_local_P']=all(v['ideal_local_Efield_P90']<0 for v in rows[1]['declared_width_forward_examples'])
    return {'status':'conditional-photon-convention-and-axis-bridge','formal_day_index':23,'only_existing_uncredited_preview_day':24,
            'source_premises':['LKH82 printed122 Eqs2.8-2.11 and finalemissionKS/RB/BR relations','ST99 printed17Eq1/2 Efieldparallel/perp P andA=QP','L22Table1 actual747/813 sourcecentres'],
            'amplitude_identity':'d_native=-d_RB; native(-1)^L basis gives A_native=-A_RB forM1/E2. Fullrho/IQUV identical. In the defined LKH82 emission convention deltaKS=-deltaRB for both cascade photons.',
            'checked_design_points':points,'pure_stretched_axis_controls':pure_rows,'source_bound_conditional_forward_examples':rows,
            'control_errors':{'max_global_phase_error':max_global,'max_full_photon_density_error':max_density,
                              'max_IQUV_error':max_stokes,'max_pure_global_phase_error':max_pure,
                              'max_linear_axis_swap_error':max_axis,'max_PSD_defect':max_psd_defect,
                              'unmapped_coordinate_max_density_difference_design':wrong_difference},
            'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
                Path(__file__).with_name('day23_halfspin_singles_response.py'),Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            'limitations':['This certifies a declared photon-coordinate/axis mapping, not the historical Pr/Au analysis producer, exact experimental delta convention or actual gated response.',
                           'Efieldparallel/perp and Compton-scatteringparallel/perp refer to different physical axes. Their count-asymmetry bridge needs the same calibrated a/Q and actual selected acceptance, not a sign relabel alone.',
                           'Pure stretched chosen examples are axis controls, not a universal statement that all E orM transitions must have one polarization sign at every spin/angle/population.',
                           'No published central point is fitted and no width/branch/attenuation/efficiency/covariance is estimated. Actual Pr uses different ring groups and upstream796/450 gates.',
                           'The small-delta forward examples show the positiveP branch heuristic is conditional; they do not erase SH26 fixedsigma/I=.2 AD large-root support or prove real likelihood valleys equal.',
                           'No physical g/Q/newdelta/tau/CI/facility rate or beamtime generated. Checkpoint025 is not aDay25card; formalDay23 identity and deadline remain.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate();a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'design_points':r['checked_design_points'],'errors':r['control_errors'],
                      'conditional_forward':r['source_bound_conditional_forward_examples']},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
