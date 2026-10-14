#!/usr/bin/env python3
"""Shared-POL algebra and a declared point-detector, pure-E2 outer bound.

Uses no measured counts. The angular model assumes axial symmetry, incoherent
multipole-projection weights, common conditional selection, known positive Q, and no background.
Here m_gamma=-2..2 is the multipole magnetic projection; photon helicity is
lambda=+/-1. Q_sens(E) is detector sensitivity, distinct from the ENSDF Q label.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog
from scipy.spatial import ConvexHull


def a_cal(energy):
    return 1.113 - 5.4e-5 * energy


def q_cal(energy):
    alpha = energy / 510.99895
    return (1+alpha)/(1+alpha+alpha**2) * (.42-1.9e-4*energy)


def e2_gradient_kernel(q, theta):
    # In these two kernels q denotes m_gamma, not photon helicity lambda.
    """Normalized E2 intensities from transverse grad_angular Y_2q."""
    s, c = np.sin(theta), np.cos(theta)
    if abs(q) == 0:
        itheta, iphi = 36*5/(16*np.pi)*s*s*c*c, np.zeros_like(theta)
    elif abs(q) == 1:
        itheta, iphi = 15/(8*np.pi)*(c*c-s*s)**2, 15/(8*np.pi)*c*c
    else:
        itheta, iphi = 4*15/(32*np.pi)*s*s*c*c, 4*15/(32*np.pi)*s*s
    return 4*np.pi/6*(itheta+iphi), 4*np.pi/6*(itheta-iphi)


def e2_rotation_kernel(q, theta):
    """Separate RB helicity construction: coherent difference/sum, not W alone."""
    m = np.arange(2,-3,-1)
    raising = np.zeros((5,5))
    for col, mi in enumerate(m):
        if mi < 2:
            raising[col-1,col] = math.sqrt(6-mi*(mi+1))
    d = expm(theta/2*(raising.T-raising))
    plus, minus = math.sqrt(5)*d[2-q,1], math.sqrt(5)*d[2-q,3]
    return (plus*plus+minus*minus)/2, -plus*minus


def stretched_weights(ji, mi):
    """Exact squared CG for Ji=Jf+2 by the maximal-coupling binomial formula."""
    jf = ji-2
    qs = np.arange(-2,3)
    result = []
    for q in qs:
        mf = mi-q
        value = (math.comb(round(2*jf),round(jf+mf))*math.comb(4,2+q)
                 /math.comb(round(2*ji),round(ji+mi))) if abs(mf)<=jf else 0
        result.append(value)
    return np.array(result)


def range_feasibility(vertices, radius):
    r, aa = vertices[:,0], vertices[:,1]
    rlo, rhi = 1.26-radius*.16, 1.26+radius*.16
    alo, ahi = -.076-radius*.011, -.076+radius*.011
    constraints = np.vstack((r-rhi, rlo-r, aa-ahi, alo-aa))
    fit = linprog(np.zeros(len(r)), A_ub=constraints, b_ub=np.zeros(4),
                  A_eq=np.ones((1,len(r))), b_eq=[1], bounds=(0,None), method="highs")
    return {"radius_in_reported_errors":radius,"R_range":[rlo,rhi],"A_range":[alo,ahi],
            "feasible":bool(fit.success),"solver_status":int(fit.status),
            "predicted":(vertices.T@fit.x).tolist() if fit.success else None,
            "not_a_joint_confidence_region":True}


def audit():
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)
    energies = np.array([393.4,394.0])
    amean = a_cal(energies.mean())
    reported_a, sigma_a = -.076, .011
    # The recorded I_gamma values do NOT appear in these mixture weights.
    rng = np.random.default_rng(2026101403)
    for k in range(12):
        component_a = rng.uniform(-.8,.8,2)
        nparallel = rng.uniform(20,5000,2)
        nperp = nparallel*(1+component_a)/(amean*(1-component_a))
        weights = amean*nperp+nparallel
        direct = (amean*nperp.sum()-nparallel.sum())/(amean*nperp.sum()+nparallel.sum())
        check("positive_count_mixture_identity_"+str(k),np.isclose(direct,np.dot(weights,component_a)/weights.sum()))
    mismatch_floor = min((common-a_cal(energy))/(common+a_cal(energy))
                         for common in a_cal(energies) for energy in energies)
    check("nearby_energy_miscalibration_floor_small", abs(mismatch_floor)<2e-5)
    check("two_nonnegative_components_cannot_reproduce_mean_under_this_calibration", reported_a<mismatch_floor)
    raw_ratio = (1+reported_a)/(amean*(1-reported_a))
    required_cal = 1/raw_ratio
    check("calibration_shift_formula",np.isclose(required_cal/amean,(1-reported_a)/(1+reported_a)))
    upper_normal_example = reported_a+1.96*sigma_a
    check("quoted_error_only_normal_example_negative",upper_normal_example<mismatch_floor)
    # Two distinct physical pairs have exactly the same measured shared asymmetry.
    equivalent_pairs = []
    for aa in [np.array([-.20,.10]),np.array([.10,-.20])]:
        fraction = (reported_a-aa[1])/(aa[0]-aa[1])
        check("opposite_component_identity_can_share_A_"+str(len(equivalent_pairs)),0<fraction<1 and np.isclose(fraction*aa[0]+(1-fraction)*aa[1],reported_a))
        equivalent_pairs.append({"component_A":aa.tolist(),"corrected_count_weight_first":fraction})
    tlong, tside = np.deg2rad([157.6,75.5])
    angles = np.array([.17,.43,.91,tside,tlong])
    for q in range(-2,3):
        for i,t in enumerate(angles):
            g=e2_gradient_kernel(q,t);rot=e2_rotation_kernel(q,t)
            check("gradient_matches_RB_rotation_q"+str(q)+"_t"+str(i),np.allclose(g,rot,atol=2e-14))
    x, gw = np.polynomial.legendre.leggauss(32)
    for q in [0,1,2]:
        w,n=e2_gradient_kernel(q,np.arccos(x))
        check("each_photon_q_angular_average_one_"+str(q),np.isclose(np.dot(gw,w)/2,1))
        check("nonnegative_linear_intensities_"+str(q),np.all(w+1e-12>=abs(n)))
    # Isotropic weights over all five photon-q states yield W=1 and N=0.
    wk,nk=zip(*(e2_gradient_kernel(q,np.arccos(x)) for q in range(-2,3)))
    check("isotropic_photon_q_W_one",np.allclose(np.mean(wk,axis=0),1))
    check("isotropic_photon_q_linear_zero",np.allclose(np.mean(nk,axis=0),0))
    # Six vertices are a spin-independent OUTER set, not all realizable for a chosen J.
    vertices=[]
    for energy in energies:
        for q in [0,1,2]:
            wl,_=e2_gradient_kernel(q,tlong);ws,ns=e2_gradient_kernel(q,tside)
            vertices.append([wl/ws,q_cal(energy)*ns/ws])
    vertices=np.array(vertices)
    intervals=[range_feasibility(vertices,k) for k in [0,1,2,3]]
    check("joint_mean_outside_E2_outer_set",not intervals[0]["feasible"])
    check("two_reported_error_box_outside_outer_set",not intervals[2]["feasible"])
    check("wider_declared_box_can_be_feasible",intervals[3]["feasible"])
    bound=[]
    for sign in [1,-1]:
        fit=linprog(sign*vertices[:,1],A_eq=np.vstack((np.ones(6),vertices[:,0])),b_eq=[1,1.26],bounds=(0,None),method="highs")
        check("fixed_R_bound_exists_"+str(sign),fit.success)
        bound.append(float(vertices[:,1]@fit.x))
    check("at_observed_R_outer_A_is_positive",bound[0]>0)
    # Construct a linear separating inequality from the lower hull facet.
    low=vertices[np.argmin(vertices[:,1])];high=vertices[np.argmax(vertices[:,0])]
    high_candidates=vertices[np.isclose(vertices[:,0],high[0])]
    high=high_candidates[np.argmin(high_candidates[:,1])]
    slope=(high[1]-low[1])/(high[0]-low[0]);intercept=low[1]-slope*low[0]
    check("outer_set_obeys_separating_inequality",np.all(vertices[:,1]>=slope*vertices[:,0]+intercept-1e-12))
    gap=reported_a-(slope*1.26+intercept)
    check("reported_mean_violates_inequality",gap<0)
    orientations=[]
    physical_vertices=[]
    for ji in [7.5,9.5]:
        ms=np.arange(-ji,ji+1,1)
        weights=np.array([stretched_weights(ji,mi) for mi in ms])
        check("stretched_CG_Vandermonde_"+str(ji),np.allclose(weights.sum(axis=1),1))
        check("unpolarized_nucleus_has_uniform_photon_q_"+str(ji),np.allclose(weights.mean(axis=0),.2))
        for mi in np.arange(.5,ji+1,1):
            qp=stretched_weights(ji,mi)
            ws=sum(qp[q+2]*e2_gradient_kernel(q,tside)[0] for q in range(-2,3))
            ns=sum(qp[q+2]*e2_gradient_kernel(q,tside)[1] for q in range(-2,3))
            wl=sum(qp[q+2]*e2_gradient_kernel(q,tlong)[0] for q in range(-2,3))
            energy=energies[0 if ji==7.5 else 1]
            physical_vertices.append([float(wl/ws),float(q_cal(energy)*ns/ws)])
        for name,pop in [("Gaussian_sigma_over_J_point3",np.exp(-ms**2/(2*(.3*ji)**2))),
                         ("max_abs_M_aligned",(abs(ms)==ji).astype(float))]:
            pop=pop/pop.sum();qp=pop@weights
            ws=sum(qp[q+2]*e2_gradient_kernel(q,tside)[0] for q in range(-2,3))
            ns=sum(qp[q+2]*e2_gradient_kernel(q,tside)[1] for q in range(-2,3))
            wl=sum(qp[q+2]*e2_gradient_kernel(q,tlong)[0] for q in range(-2,3))
            orientations.append({"Ji":ji,"Jf":ji-2,"chosen_population":name,"R_point":float(wl/ws),"P_side":float(ns/ws),"A_at_mean_Q":float(q_cal(energies.mean())*ns/ws)})
            check("E2_sign_changes_with_population_"+str(ji)+name,ns>0 if name.startswith('Gaussian') else ns<0)
    # With different effective selection, a positive-R population and negative-A
    # population can each match their scalar. This is a model-boundary example.
    separate=[]
    physical_vertices=np.array(physical_vertices)
    for which,value,column in [('R',1.26,0),('A',reported_a,1)]:
        fit=linprog(np.zeros(len(physical_vertices)),A_eq=np.vstack((np.ones(len(physical_vertices)),physical_vertices[:,column])),b_eq=[1,value],bounds=(0,None),method='highs')
        check("unmatched_selection_scalar_feasible_"+which,fit.success)
        separate.append({"observable":which,"weights":fit.x.tolist(),"pair_prediction":(physical_vertices.T@fit.x).tolist(),"nuclear_CG_vertex_basis":True})
    # EM duality flips N for pure M2 without changing W. For the proposed
    # spins, this mathematical alternative requires opposite endpoint parities.
    magnetic_vertices=physical_vertices.copy();magnetic_vertices[:,1]*=-1
    magnetic_fit=linprog(np.zeros(len(magnetic_vertices)),A_eq=np.vstack((np.ones(len(magnetic_vertices)),magnetic_vertices.T)),b_eq=[1,1.26,reported_a],bounds=(0,None),method='highs')
    check("pure_M2_nuclear_CG_set_can_contain_joint_mean",magnetic_fit.success)
    magnetic_case={"nuclear_CG_feasible":bool(magnetic_fit.success),"joint_prediction":(magnetic_vertices.T@magnetic_fit.x).tolist(),
                   "not_a_line_assignment":True,"required_condition":"M2 requires opposite endpoint parities; the tentative same-parity E2 scheme cannot be kept unchanged"}
    return {"kind":"L2 algebra/point-response limit, not193Bi likelihood fit","checks":checks,"checks_passed":sum(checks.values()),
            "reported_shared":{"R":1.26,"sigma_R":.16,"A":reported_a,"sigma_A":sigma_a,"source":"HE15-9 / N193-5"},
            "calibration":{"a_mean":float(amean),"Q_mean":float(q_cal(energies.mean())),"nearby_a_floor":float(mismatch_floor),"raw_Nperp_over_Nparallel_counterfactual":raw_ratio,"a_required_for_zero_A":required_cal,"relative_a_increase_required":required_cal/amean-1,"quoted_error_only_95percent_normal_example_upper":upper_normal_example,"not_source_significance":True},
            "same_shared_A_opposite_component_pairs":equivalent_pairs,"E2_outer_vertices_R_A":vertices.tolist(),"E2_outer_hull_indices":ConvexHull(vertices).vertices.tolist(),
            "fixed_R_A_outer_range":bound,"separating_inequality":{"form":"A >= slope*R+intercept","slope":float(slope),"intercept":float(intercept),"observed_mean_margin":float(gap)},
            "declared_error_boxes":intervals,"pure_E2_orientation_counterexamples":orientations,"unmatched_selection_examples":separate,"conditional_M2_outer_example":magnetic_case,
            "boundaries":["No observed component counts/weights or calibration covariance; the reported0.011 was not reinterpreted as full experimental uncertainty.","Pure E2 photon-q outer set assumes axial symmetry, diagonal populations/unobserved final spin, point angles157.6/75.5, common conditional selection and relative weights forR/POL, positive sourceQ and no background. It is not a JUROGAM replay.","Pure E2 can have negativeP under different populations, but negativeP alone does not identifyM2. The joint outer-set exclusion is conditional; changed gate/acceptance/coherence/multipole/calibration assumptions can change it.","Error boxes are sensitivity ranges, not joint confidence regions. Q/a coefficient covariance and R/POL covariance were not supplied.","Gamma relative intensities are not corrected two-crystal polarimetry weights; no parenttau,delta,spin orshape is inferred."]}


def plot_result(result, prefix):
    import os
    root=Path(__file__).resolve().parents[2]
    prefix.resolve().relative_to(root)
    os.environ['MPLCONFIGDIR']=str(root/'tmp/day14-20261014/mplconfig')
    import matplotlib
    matplotlib.use('Agg')
    matplotlib.rcParams['svg.hashsalt']='day14-response-checkpoint003'
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    v=np.array(result['E2_outer_vertices_R_A']);order=result['E2_outer_hull_indices']
    fig,ax=plt.subplots(figsize=(7.7,4.9))
    ax.fill(v[order,0],v[order,1],color='#4477aa',alpha=.19,label='Pure E2: axial point-response outer set')
    ax.plot(np.r_[v[order,0],v[order[0],0]],np.r_[v[order,1],v[order[0],1]],color='#4477aa',lw=1.5)
    ax.errorbar(1.26,-.076,xerr=.16,yerr=.011,fmt='o',color='#bb3322',capsize=3,label='Herzan Table I shared estimate')
    ax.add_patch(Rectangle((.94,-.098),.64,.044,fill=False,ec='#bb3322',ls='--',lw=1,label='2 x printed errors: sensitivity box'))
    for name,marker,color in [('Gaussian_sigma_over_J_point3','D','#228833'),('max_abs_M_aligned','s','#aa8833')]:
        rows=[x for x in result['pure_E2_orientation_counterexamples'] if x['chosen_population']==name]
        ax.scatter([x['R_point'] for x in rows],[x['A_at_mean_Q'] for x in rows],marker=marker,color=color,s=37,label=('Chosen Gaussian populations' if marker=='D' else 'Chosen aligned |M|=J populations'))
    ax.axhline(0,color='.55',lw=.7)
    ax.set(xlabel=r'$R=W(157.6^\circ)/W(75.5^\circ)$',ylabel=r'$A=Q P(75.5^\circ)$',xlim=(.15,2.22),ylim=(-.275,.29))
    ax.set_title('Shared 393.4/394.0 keV: conditional pure-E2 response limit',fontsize=11)
    ax.legend(loc='upper left',fontsize=8,frameon=False)
    ax.spines[['top','right']].set_visible(False)
    fig.text(.12,.045,'Axial, incoherent point response; common selection; Q fixed.\nFinite acceptance and covariance require the original analysis inputs.',fontsize=8,color='.35')
    fig.subplots_adjust(left=.12,right=.98,top=.9,bottom=.2)
    svg=Path(str(prefix)+'.svg')
    fig.savefig(svg,metadata={'Date':None})
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    fig.savefig(str(prefix)+'.png',dpi=180);plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--plot-prefix',type=Path)
    args=parser.parse_args();args.output.resolve().relative_to(Path(__file__).resolve().parents[2])
    result=audit();args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if args.plot_prefix:plot_result(result,args.plot_prefix)
    print(json.dumps({"checks_passed":result['checks_passed'],"calibration":result['calibration'],"fixed_R_A_outer_range":result['fixed_R_A_outer_range'],"inequality":result['separating_inequality'],"boxes":result['declared_error_boxes'],"orientations":result['pure_E2_orientation_counterexamples']},ensure_ascii=False))


if __name__=='__main__':main()
