#!/usr/bin/env python3
"""Source Pr ring angles in conditional ideal groups, not actual Rac fitting."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_halfspin_singles_response import population,response,ideal_pair
from day23_halfspin_upstream_gate import point_daughter,photon_density,observable


FAR=[157.6,133.6]
NEAR=[75.5,104.5]


def group(photons,fraction):
    # Combine unnormalized helicity matrices first, never average P directly.
    return observable(fraction*photons[0]+(1-fraction)*photons[1])


def calculate():
    controls,rows={},[];max_mirror=max_convex_defect=max_scaling=max_group_formula=0.
    min_eigen=0.
    for two_i,quoted_delta,energy in [(17,-.47,747.3),(21,-.37,813.2)]:
        for width in [.2,.4,.8]:
            w=population(two_i,width)
            angle_rows=[];photons={}
            for theta in FAR+NEAR:
                intensity,s,h=response(two_i,two_i-2,-quoted_delta,math.radians(theta),w)
                photons[theta]=h
                min_eigen=min(min_eigen,float(np.linalg.eigvalsh(h)[0]))
                angle_rows.append({'theta_nominal_source_deg':theta,'ideal_W':intensity,'local_P_stokes':float(s[0]/intensity)})
            far=[photons[t] for t in FAR];near=[photons[t] for t in NEAR]
            wf=[observable(h)['intensity'] for h in far];wn=[observable(h)['intensity'] for h in near]
            lower,upper=min(wf)/max(wn),max(wf)/min(wn)
            max_mirror=max(max_mirror,float(np.max(abs(near[0]-near[1]))))
            for f in [0.,.1,.5,.9,1.]:
                for n in [0.,.1,.5,.9,1.]:
                    fg,ng=group(far,f),group(near,n)
                    ratio=fg['intensity']/ng['intensity']
                    max_convex_defect=max(max_convex_defect,lower-ratio,ratio-upper)
                    max_group_formula=max(max_group_formula,abs(ratio-(f*wf[0]+(1-f)*wf[1])/(n*wn[0]+(1-n)*wn[1])))
                    # An algebraic normalizer scaling control, not an estimate.
                    eta_design=2.
                    max_scaling=max(max_scaling,abs(eta_design*ratio/ratio-eta_design))
            equal_far,equal_near=group(far,.5),group(near,.5)
            nominal_r,nominal_p=ideal_pair(two_i,-quoted_delta,width)
            rows.append({'source_line_energy_keV':energy,'two_I_source':two_i,'quoted_source_delta_centre':quoted_delta,
                         'conditional_KS_application_d_RB':-quoted_delta,'declared_Gaussian_input_sigma_over_I':width,
                         'actual_source_nominal_angle_points_in_ideal_model':angle_rows,
                         'conditional_R_divided_by_unknown_eta_envelope_positive_group_weights':[lower,upper],
                         'equal_weights_illustration_only_R_divided_by_eta':equal_far['intensity']/equal_near['intensity'],
                         'equal_near_weights_ideal_Efield_P':equal_near['P_stokes'],
                         'nominal154_over90_old_ideal_ratio':float(nominal_r),'old_ideal_local90_P':float(nominal_p),
                         'actual_relative_group_normalizer_eta':None,'actual_group_efficiency_or_pair_weights':None,
                         'real_fit_width_delta_or_likelihood':None,
                         'boundary':'Only after normalized positive group-mean convention. Eta and actual finite detector/pair/gate/feeding/Compton response are not supplied; this is not an absolute bound or fit for measured Rac.'})
    controls['axisymmetric_singles_mirror_near_ring_photon_density_equal']=max_mirror<1e-12
    controls['positive_group_ratio_inside_conditional_convex_envelope']=max_convex_defect<1e-12
    controls['group_formula_matches_unnormalized_density_combination']=max_group_formula<1e-12
    controls['conditional_eta_scaling_is_explicit']=max_scaling<1e-12
    controls['all_declared_photon_densities_positive']=min_eigen>-1e-12
    controls['nominal154_over90_not_equal_to_equal_actual_angle_means']=any(abs(
        r['equal_weights_illustration_only_R_divided_by_eta']-r['nominal154_over90_old_ideal_ratio'])>.01 for r in rows)
    # Declared finite coplanar upstream gate, not the actual all-detector array.
    rho0=np.diag(population(25,.2))
    daughter=point_daughter(25,21,'E2',0.,math.radians(45),rho0)
    daughter/=np.trace(daughter)
    hs=[photon_density(21,19,'M1/E2',.37,math.radians(theta),daughter) for theta in NEAR]
    obs=[observable(h) for h in hs]
    weighted=group(hs,.5)
    weighted_formula=sum(o['intensity']*o['P_stokes'] for o in obs)/sum(o['intensity'] for o in obs)
    naive=sum(o['P_stokes'] for o in obs)/2
    asymmetry=float(np.max(abs(hs[0]-hs[1])))
    controls['finite_upstream_example_positive_density']=float(np.linalg.eigvalsh(daughter)[0])>-1e-12
    numerical_resolution=max(1e-12,100*max_mirror)
    controls['finite_upstream_mirror_difference_resolved_above_numeric_error']=asymmetry>numerical_resolution
    controls['polarization_of_sum_equals_intensity_weighted_P']=abs(weighted['P_stokes']-weighted_formula)<1e-12
    controls['naive_mean_P_difference_resolved_not_size_claim']=abs(weighted['P_stokes']-naive)>numerical_resolution
    reflected=point_daughter(25,21,'E2',0.,math.radians(135),rho0)
    reflected/=np.trace(reflected)
    combined_reflection_error=max(abs(observable(photon_density(21,19,'M1/E2',.37,
        math.radians(180-theta),reflected))['P_stokes']-o['P_stokes']) for theta,o in zip(NEAR,obs))
    controls['combined_gate_target_reflection_restores_symmetry']=combined_reflection_error<1e-12
    finite={'spins_twice':[25,21,19],'initial_Gaussian_sigma_over_I_design':.2,
            'upstream_gate':'pureE2 pointtheta45 phi0, unpolarized helicity sum','target_d_RB_design':.37,
            'near_angle_observables':[{'theta':theta,**o} for theta,o in zip(NEAR,obs)],
            'photon_density_mirror_difference_design':asymmetry,
            'summed_unnormalized_photon_P':weighted['P_stokes'],
            'intensity_weighted_P_same_quantity':weighted_formula,'naive_arithmetic_mean_P_other_quantity':naive,
            'P_mean_difference_design_only':weighted['P_stokes']-naive,
            'numeric_resolution_for_nonzero_checks':numerical_resolution,
            'combined_gate_target_reflection_error':combined_reflection_error,
            'scope':'Finite coplanar point-gate design only. Uniform azimuth or other actual acceptances can change/remove the coherence. No experimental bias or correction is inferred.'}
    return {'status':'conditional-source-angle-group-component','formal_day_index':23,'only_existing_uncredited_preview_day':24,
            'source_premises':['L22SI PDF1Eq1/2 source angle groups157.6+133.6 vs75.5+104.5','DR96 printed522/523 finitePDCO reflection boundary','source025 explicit conditional KS/RB application andideal013kernel'],
            'group_definition':'R=eta*[fW157.6+(1-f)W133.6]/[nW75.5+(1-n)W104.5], normalized positive group means only. Eta actual calibration and group/pair weights not provided.',
            'results':rows,'finite_upstream_coplanar_countercontrol':finite,
            'control_errors':{'max_axisymmetric_mirror_density_error':max_mirror,'max_convex_envelope_defect':max_convex_defect,
                              'max_group_formula_error':max_group_formula,'max_eta_scaling_error':max_scaling,'min_photon_eigenvalue':min_eigen},
            'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
                Path(__file__).with_name('day23_halfspin_singles_response.py'),Path(__file__).with_name('day23_halfspin_upstream_gate.py'),
                Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            'limitations':['Actual nominal polar angles are source inputs, but the declared normalized group-mean weights/eta, angular acceptance, efficiencies/live time and selected gate-detector pairs are not reconstructed.',
                           'The envelope bounds R/eta under the stated model, not actual Rac when eta is unknown. It does not assert original authors lacked calibration or that its nuisance range is unbounded.',
                           'Mirror cancellation of near-ring weights requires axisymmetric singles response. A selected finite upstream gate may break that condition; the point-gate example is not a measured effect.',
                           'Quoted source delta centres are used only under the extra KS definition application assumption. No actual width, delta, net count, Q/a, feeding density, covariance or likelihood is fitted.',
                           'Positive-group-weight averaging of a photon density preserves intensities; an arithmetic average of normalized P values is a different object unless weights are adjusted.',
                           'No actual Pr/Au response/experiment is certified, SH26 fixedsigma/I AD support is preserved and real likelihood valleys are not declared equal.',
                           'No g/Q/new tau/CI/facility rate/beamtime generated; checkpoint026 is a progress number, not a newDay26card.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate();a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'controls':r['controls'],'conditional_width_point4_results':[v for v in r['results'] if v['declared_Gaussian_input_sigma_over_I']==.4],
                      'finite_upstream_control':r['finite_upstream_coplanar_countercontrol']},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
