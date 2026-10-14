#!/usr/bin/env python3
"""One uncredited Day15 worksheet: Zheng2002 grouping and chosen error inputs.

No experimental counts or efficiency curve is fitted. Two angular counts and
their efficiency ratio identify R_ADO, not f_ADO without an additional input.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import os
from pathlib import Path

import numpy as np


def angular(theta, a2, a4):
    x=np.cos(theta)
    return 1+a2*(3*x*x-1)/2+a4*(35*x**4-30*x*x+3)/8


def group_factor(w2, eps2, n):
    c=float(np.dot(w2,eps2))
    return (c-w2[0]*eps2[0]/n[0])/(c-w2[2]*eps2[2]/n[2])


def individual_counts(w1, w2, eps1, eps2, assignment, normalization=1):
    a=w1[assignment]*eps1
    b=w2[assignment]*eps2
    c=b.sum()
    counts=np.array([sum(a[i]*(c-b[i]) for i in range(len(a)) if assignment[i]==g)
                     for g in range(3)])*normalization
    return counts,c,b


def ratio_function(z):
    ns,nl,eff,reference=z
    return ns/nl/eff/reference


def audit():
    checks={}
    def check(k,c):
        checks[k]=bool(c)
        if not c:raise AssertionError(k)
    angles=np.deg2rad([32,58,90])
    n=np.array([4,4,4]);assignment=np.repeat(np.arange(3),n)
    eps1_group=np.array([.04,.06,.05])
    eps2_group=np.array([.04,.04,.04])
    w1=angular(angles,.24,-.07)
    w2=angular(angles,.30,.08)
    # Analytic reconstruction: complementary32/58 plus90 nearly integrate
    # the even K2/K4 basis with equal group weights. Not an author-stated design.
    def pk(t):
        x=np.cos(t)
        return np.array([(3*x*x-1)/2,(35*x**4-30*x*x+3)/8])
    printed_basis=pk(angles).sum(axis=1)
    magic=math.asin(2/math.sqrt(5))/2
    exact_angles=np.array([magic,math.pi/2-magic,math.pi/2])
    exact_basis=pk(exact_angles).sum(axis=1)
    check('complementary_angles_P2_sum_zero',abs(printed_basis[0])<1e-14)
    check('derived_equal_weight_magic_angles_P2_P4_zero',np.allclose(exact_basis,0,atol=1e-14))
    check('printed_P4_residual_is_small',abs(printed_basis[1])<.02)
    check('chosen_W_positive',np.all(w1>0) and np.all(w2>0))
    eps1=eps1_group[assignment]/n[assignment]
    eps2=eps2_group[assignment]/n[assignment]
    counts,c,b=individual_counts(w1,w2,eps1,eps2,assignment,1e6)
    f=group_factor(w2,eps2_group,n)
    intrinsic=w1[0]/w1[2]
    corrected=counts[0]/counts[2]/(eps1_group[0]/eps1_group[2])
    check('Eq1_Eq3_Eq4_individual_pair_agreement',np.isclose(corrected,intrinsic*f))
    direct=np.zeros(3)
    for i,j in itertools.permutations(range(12),2):
        direct[assignment[i]]+=1e6*w1[assignment[i]]*eps1[i]*w2[assignment[j]]*eps2[j]
    check('explicit_detector_pair_sum_agrees',np.allclose(direct,counts))
    check('reversed_ratio_reverses_f',np.isclose(1/corrected,(1/intrinsic)*(1/f)))
    check('shared_group_eff_scale_cancels_f',np.isclose(group_factor(w2,7*eps2_group,n),f))
    check('isotropic_equal_eff_gate_f_one',np.isclose(group_factor(np.ones(3),eps2_group,n),1))
    check('equal_per_group_4_detector_bound',.75<=f<=4/3)
    long_n=[]
    for multiplicity in [4,8,32,1024]:long_n.append(group_factor(w2,eps2_group,np.repeat(multiplicity,3)))
    check('many_detectors_limit_f_one',abs(long_n[-1]-1)<abs(long_n[0]-1)/100)
    check('unordered_ADO_hardware_pairs_38',math.comb(4,2)+4*4+4*4==38)
    check('DCO_cross_hardware_pairs_16',4*4==16)
    check('ordered_energy_assignments_44',4*(12-1)==44)
    # Same group totals can hide correlated heterogeneity between the two energies.
    hetero1=eps1.copy();hetero2=eps2.copy()
    hetero1[:4]=[.002,.002,.002,.034]
    hetero2[:4]=[.002,.002,.002,.034]
    hcounts,hc,hb=individual_counts(w1,w2,hetero1,hetero2,assignment)
    hf=hcounts[0]/hcounts[2]/(eps1_group[0]/eps1_group[2])/intrinsic
    check('heterogeneous_group_totals_unchanged',np.isclose(hetero1[:4].sum(),eps1_group[0]) and np.isclose(hetero2[:4].sum(),eps2_group[0]))
    check('group_approximation_can_fail',abs(hf-f)>.10)
    # Target-energy weights determine the exact excluded reference response.
    h=[np.dot((w1[assignment]*hetero1)[assignment==g],hb[assignment==g])
       /(w1[g]*eps1_group[g]) for g in range(3)]
    exact=(hc-h[0])/(hc-h[2])
    check('weighted_exclusion_reproduces_heterogeneous_result',np.isclose(hf,exact))
    eta=float(max(hb)/hc)
    check('reference_localization_bound_valid',1-eta<=hf<=1/(1-eta))
    # Two illustrative integer counts + calibrated ratio and an EXTRA reference input.
    z=np.array([5000.,4800.,.80,1.34])
    uncertainties=np.array([np.sqrt(z[0]),np.sqrt(z[1]),.016,.04])
    r_ado=z[0]/z[1]/z[2]
    f_est=ratio_function(z)
    grad=f_est*np.array([1/z[0],-1/z[1],-1/z[2],-1/z[3]])
    fd=[]
    for i in range(4):
        step=1e-5*z[i];hi=z.copy();lo=z.copy();hi[i]+=step;lo[i]-=step
        fd.append((ratio_function(hi)-ratio_function(lo))/(2*step))
    check('error_gradient_finite_difference',np.allclose(grad,fd,rtol=1e-8))
    cov=np.diag(uncertainties**2)
    sigma_f=np.sqrt(grad@cov@grad)
    formula=f_est*np.sqrt(1/z[0]+1/z[1]+(.016/.8)**2+(.04/1.34)**2)
    check('independent_error_formula',np.isclose(sigma_f,formula))
    covariance_cases=[]
    for rho in [-.8,0,.8]:
        cc=cov.copy();cc[2,3]=cc[3,2]=rho*uncertainties[2]*uncertainties[3]
        check('chosen_covariance_PSD_'+str(rho),np.linalg.eigvalsh(cc).min()>0)
        covariance_cases.append({'chosen_rho_eff_reference':rho,'sigma_f':float(np.sqrt(grad@cc@grad))})
    # Without the intrinsic reference, different f/W ratios preserve the observedR.
    family=[]
    for candidate_f in [.90,.97,1.05]:
        value=r_ado/candidate_f
        check('two_count_nonidentifiability_'+str(candidate_f),np.isclose(value*candidate_f,r_ado))
        family.append({'f_ADO':candidate_f,'intrinsic_ratio':value})
    check('circular_reference_f_is_one_tautologically',np.isclose(r_ado/r_ado,1))
    # Link to Day14 is conditional and uses generic A/B angles, not145Tb constants.
    slope,intercept=.26412346235270334,-.29954536695098155
    maximum_intrinsic_for_shared_a=(-.076-intercept)/slope
    minimum_f_required=1.26/maximum_intrinsic_for_shared_a
    eta_required=1-1/minimum_f_required
    check('four_equal_detectors_group_self_exclusion_insufficient_for_this_mean',minimum_f_required>4/3)
    return {'kind':'Day15 uncredited preview, selected equations and self-chosen model',
            'source':'Zheng2002 PDF p2 Eqs1-5; p3 group efficiency convention; p4 hardwarepair comparison',
            'chosen_geometry':{'group_angles_deg':[32,58,90],'number_per_group':n.tolist(),'target_group_efficiencies':eps1_group.tolist(),'gate_group_efficiencies':eps2_group.tolist(),'target_A2_A4':[.24,-.07],'gate_A2_A4':[.30,.08]},
            'task_derived_Legendre_sampling':{'printed_sum_P2_P4':printed_basis.tolist(),'derived_exact_angles_deg':np.rad2deg(exact_angles).tolist(),'derived_sum_P2_P4':exact_basis.tolist(),'not_author_stated_array_design':True},
            'homogeneous_model':{'intrinsic_ratio':float(intrinsic),'f_ADO':float(f),'expected_angle_counts':counts.tolist(),'expected_R_ADO':float(corrected)},
            'heterogeneous_model':{'same_group_totals':True,'exact_f_ADO':float(hf),'approximate_group_f_ADO':float(f),'largest_reference_detector_share_eta':eta,'excluded_gate_response_weighted':h},
            'worksheet':{'chosen_inputs':z.tolist(),'chosen_input_sigmas':uncertainties.tolist(),'R_ADO':float(r_ado),'f_ADO_with_extra_reference':float(f_est),'sigma_f_independent_chosen_covariance':float(sigma_f),'covariance_cases':covariance_cases,'without_extra_reference_family':family},
            'conditional_Day14_bridge':{'maximum_intrinsic_point_R_at_shared_A':maximum_intrinsic_for_shared_a,'minimum_geometric_f_to_bridge_mean':minimum_f_required,'minimum_reference_localization_eta_needed_for_that_self_exclusion_bound':eta_required,'not_JUROGAM_calibration_or_experimental_exclusion':True},
            'checks':checks,'checks_passed':sum(checks.values()),
            'boundaries':['All counts, efficiencies, A2/A4 and error covariance are chosen worksheet inputs, not145Tb or193Bi reanalysis.','The grouped Eq4 uses group efficiencies and equal within-group response approximation; gamma1/gamma2 angular factorization does not replace a full angular-correlation response.','The independent reference ratio is an extra input; two angle counts and target efficiency ratio only identify R_ADO.','The3.2/5.2percent source numbers are calculated maximum f deviations, not these worksheet standard errors or all systematic uncertainty.','The geometric-only Day14 bridge is conditional on the old point bound/common selection; actual angular correlation, acceptance, polarization weighting and covariance remain missing.','day_index stays14; partial15 only, noformal15audit or credit and noDay16 card.']}


def plot_result(data,prefix):
    root=Path(__file__).resolve().parents[2];prefix.resolve().relative_to(root)
    os.environ['MPLCONFIGDIR']=str(root/'tmp/day14-20261014/mplconfig')
    import matplotlib
    matplotlib.use('Agg')
    matplotlib.rcParams['svg.hashsalt']='day14-response-checkpoint003'
    import matplotlib.pyplot as plt
    x=np.linspace(0,.08,161);u=.04/1.34;v=1/5000+1/4800
    central=np.sqrt(v+x*x+u*u);lower=np.sqrt(v+x*x+u*u-1.6*x*u);upper=np.sqrt(v+x*x+u*u+1.6*x*u)
    fig,ax=plt.subplots(figsize=(6.8,4.4));ax.fill_between(100*x,100*lower,100*upper,alpha=.16,color='#4477aa',label='Chosen correlation range -0.8 to +0.8')
    ax.plot(100*x,100*central,color='#4477aa',label=r'$f_{ADO}$: chosen independent reference')
    ax.plot(100*x,100*np.sqrt(v+x*x),color='#ee7733',label=r'$R_{ADO}$: counts and efficiency only')
    ax.scatter([2],[100*np.sqrt(v+.02**2+u*u)],color='#4477aa',zorder=3)
    ax.set(xlabel='Relative efficiency-ratio uncertainty (%)',ylabel='Relative standard uncertainty (%)',title='Uncredited Day15: illustrative ADO uncertainty worksheet')
    ax.legend(frameon=False,fontsize=8);ax.spines[['top','right']].set_visible(False)
    fig.text(.12,.03,'Chosen inputs; no experimental counts or calibration curve fitted.',fontsize=8,color='.35');fig.subplots_adjust(left=.12,right=.98,top=.88,bottom=.19)
    svg=Path(str(prefix)+'.svg')
    fig.savefig(svg,metadata={'Date':None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    fig.savefig(str(prefix)+'.png',dpi=180);plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True);parser.add_argument('--plot-prefix',type=Path)
    args=parser.parse_args();args.output.resolve().relative_to(Path(__file__).resolve().parents[2]);data=audit()
    args.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if args.plot_prefix:plot_result(data,args.plot_prefix)
    print(json.dumps({'checks_passed':data['checks_passed'],'homogeneous':data['homogeneous_model'],'heterogeneous':data['heterogeneous_model'],'worksheet':data['worksheet'],'Day14_bridge':data['conditional_Day14_bridge']},ensure_ascii=False))


if __name__=='__main__':main()
