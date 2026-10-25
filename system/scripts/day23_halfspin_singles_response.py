#!/usr/bin/env python3
"""RB67 half-integer single-photon ideal response; no array/gate/data fit.

d_RB is an interaction-amplitude coordinate. It is not silently identified
with the published delta convention of any Pr/Au spectroscopy analysis.
"""
import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import clebsch_gordan, spin_matrices


@lru_cache(None)
def little_d(rank, theta):
    values, vectors = np.linalg.eigh(spin_matrices(2*rank)[1])
    return (vectors*np.exp(-1j*theta*values))@vectors.T.conj()


@lru_cache(None)
def photon_parts(two_i, two_f, theta, dual=False):
    """Source RB67 CG ordering, exp(-i theta Jy), and magnetic helicity factor."""
    matrices=[]
    for rank, magnetic in [(1,not dual),(2,dual)]:
        a=np.zeros((2,two_f+1,two_i+1),complex)
        d=little_d(rank,theta)
        for hi,h in enumerate([-1,1]):
            for fi,mf in enumerate(np.arange(-two_f,two_f+1,2)/2):
                for ii,mi in enumerate(np.arange(-two_i,two_i+1,2)/2):
                    m=int(round(mi-mf))
                    if abs(m)<=rank:
                        a[hi,fi,ii]=(math.sqrt((2*rank+1)/2)
                            *clebsch_gordan(two_f/2,mf,rank,m,two_i/2,mi)
                            *d[m+rank,h+rank]*(h if magnetic else 1))
        matrices.append(a)
    return matrices


def population(two_i,sigma_over_i=None):
    if sigma_over_i is None:
        return np.ones(two_i+1)/(two_i+1)
    if sigma_over_i<=0:
        raise ValueError("Declared Gaussian width must be positive")
    m=np.arange(-two_i,two_i+1,2)/2
    logw=-m*m/(2*(sigma_over_i*two_i/2)**2)
    w=np.exp(logw-max(logw))
    return w/sum(w)


LINEAR=np.array([[1,-1],[-1j,-1j]])/math.sqrt(2)


def response(two_i,two_f,d_rb,theta,weights,dual=False):
    dipole,quadrupole=photon_parts(two_i,two_f,theta,dual)
    amplitude=(dipole+d_rb*quadrupole)/math.sqrt(1+d_rb*d_rb)
    rho=np.einsum('hfi,i,kfi->hk',amplitude,weights,amplitude.conj())
    linear=LINEAR@rho@LINEAR.T.conj()
    intensity=float(np.trace(linear).real)
    stokes=np.array([(linear[0,0]-linear[1,1]).real,
                      2*linear[0,1].real,-2*linear[0,1].imag])
    return intensity,stokes,rho


def ideal_pair(two_i,d_rb,sigma_over_i):
    w=population(two_i,sigma_over_i)
    f=two_i-2
    i154,_,_=response(two_i,f,d_rb,math.radians(154),w)
    i90,s90,_=response(two_i,f,d_rb,math.pi/2,w)
    return np.array([i154/i90,s90[0]/i90])


def jacobian(two_i,d_rb,width,step):
    return np.column_stack([(ideal_pair(two_i,d_rb+step,width)-ideal_pair(two_i,d_rb-step,width))/(2*step),
                            (ideal_pair(two_i,d_rb,width+step)-ideal_pair(two_i,d_rb,width-step))/(2*step)])


def validate():
    controls,details={},{}
    # The known spin-one d matrix verifies direction of the rotation generator.
    angle=.713;d1=little_d(1,angle)
    controls['spin1_d_rotation_sign']=abs(d1[2,1]+math.sin(angle)/math.sqrt(2))<1e-13
    nodes,weights=np.polynomial.legendre.leggauss(24)
    high=np.array([.5,0,0,.5]);low=np.array([0,.5,.5,0])
    analytic_error=0.0
    for d in [-2.,-.5,0.,.5,2.]:
        a2=(.5+math.sqrt(3)*d-.5*d*d)/(1+d*d)
        for x in [-.83,0,.41,1.]:
            for w,sign in [(high,1),(low,-1)]:
                val=response(3,1,d,math.acos(x),w)[0]
                analytic_error=max(analytic_error,abs(val-(1+sign*a2*(3*x*x-1)/2)))
    controls['halfspin_RB67_appendix_R2_analytic']=analytic_error<1e-12
    details['halfspin_analytic_W_error']=analytic_error
    # I=1/2 single-photon pure and mixed cases cannot carry linear polarization.
    half_error=0.0
    for d in [-2.,0.,.5]:
        for w in [np.array([.2,.8]),np.array([.5,.5])]:
            for angle in [0.,.47,math.pi/2,2.23]:
                intensity,s,_=response(1,3,d,angle,w)
                half_error=max(half_error,abs(intensity-1),abs(s[0]),abs(s[1]))
    controls['spinhalf_singles_intensity_isotropic_linear_zero']=half_error<1e-12
    details['spinhalf_intensity_linear_error']=half_error
    max_isotropic=max_symmetry=max_dual=max_norm=max_highrank=0.0
    max_psd_defect=max_stokes_defect=0.0
    for two_i in [3,11,15,17,21]:
        two_f=two_i-2
        for d in [-2.,-.5,0.,.5,2.]:
            w=population(two_i,.2)
            y=[]
            for x,weight in zip(nodes,weights):
                theta=math.acos(float(x))
                intensity,s,rho=response(two_i,two_f,d,theta,w)
                iy,sy,_=response(two_i,two_f,d,theta,w,True)
                ir,sr,_=response(two_i,two_f,d,math.pi-theta,w)
                iz,sz,_=response(two_i,two_f,d,theta,population(two_i))
                max_isotropic=max(max_isotropic,abs(iz-1),float(max(abs(sz))))
                max_symmetry=max(max_symmetry,abs(ir-intensity),float(max(abs(sr-s))))
                max_dual=max(max_dual,abs(intensity-iy),abs(s[0]+sy[0]),abs(s[1]+sy[1]))
                max_psd_defect=max(max_psd_defect,float(-np.linalg.eigvalsh(rho)[0]))
                max_stokes_defect=max(max_stokes_defect,float(np.dot(s,s)-intensity**2))
                y.append(intensity)
            y=np.array(y)
            max_norm=max(max_norm,abs(float(np.dot(y,weights)/2)-1))
            coeff=np.array([float(np.dot(weights*y,np.polynomial.legendre.legval(nodes,[0]*k+[1]))*(2*k+1)/2)
                            for k in range(9)])
            max_highrank=max(max_highrank,float(max(abs(coeff[[1,3,5,6,7,8]]))))
    controls.update({'isotropic_population_W1_all_Stokes0':max_isotropic<1e-12,
                     'aligned_reflection_about90':max_symmetry<1e-12,
                     'electromagnetic_dual_same_W_opposite_linear':max_dual<1e-12,
                     'full_angular_normalization':max_norm<1e-12,
                     'direction_angular_rank_0_2_4_only':max_highrank<1e-11,
                     'positive_photon_density':max_psd_defect<1e-12,
                     'physical_Stokes_ball':max_stokes_defect<1e-12})
    details.update({'max_isotropic_W_Stokes_error':max_isotropic,'max_reflection_error':max_symmetry,
                    'max_dual_error':max_dual,'max_angular_normalization_error':max_norm,
                    'max_forbidden_Legendre_moment':max_highrank,
                    'max_photon_PSD_defect':max_psd_defect,'max_positive_Stokes_ball_defect':max_stokes_defect})
    # Mixing is coherent. Incoherent intensity weighting omits a real cross term.
    w=population(17,.2);theta=math.radians(154);d=.5
    mixed=response(17,15,d,theta,w)[0]
    plus=response(17,15,-d,theta,w)[0]
    a,b=photon_parts(17,15,theta)
    pure=lambda x:float(np.einsum('hfi,i,hfi->',x,w,x.conj()).real)
    incoherent=(pure(a)+d*d*pure(b))/(1+d*d)
    cross_error=abs((mixed+plus)/2-incoherent)
    controls['mixed_sign_average_restores_incoherent_terms']=cross_error<1e-12
    controls['mixed_interference_cannot_be_omitted']=abs(mixed-incoherent)>.05
    details['chosen_coherent_minus_incoherent_W']=mixed-incoherent
    details['odd_interference_reversal_error']=cross_error
    j1=jacobian(17,-.5,.2,1e-4);j2=jacobian(17,-.5,.2,5e-5)
    jac_error=float(max(abs(j1-j2).flat))
    controls['ideal_response_jacobian_step_converged']=jac_error<1e-5
    controls['chosen_ideal_pair_local_rank2']=abs(np.linalg.det(j2))>1e-3
    details['chosen_ideal_jacobian']={'two_I':17,'d_RB':-.5,'sigma_over_I':.2,
          'coordinates':['point_W154_over_W90','P_stokes90'],'matrix':j2.tolist(),
          'determinant':float(np.linalg.det(j2)),'step_halving_error':jac_error,
          'boundary':'Local noiseless ideal-map diagnostic only; no Fisher/likelihood/CI, global unique root or actual experiment.'}
    return {k:bool(v) for k,v in controls.items()},details


def calculate():
    controls,details=validate();rows=[]
    for two_i in [11,15,17,21]:
        for d in [-2.,-.5,0.,.5,2.]:
            for width in [.2,.4,.8]:
                w=population(two_i,width);r,p=ideal_pair(two_i,d,width)
                m=np.arange(-two_i,two_i+1,2)/2
                rows.append({'two_I_initial':two_i,'two_I_final':two_i-2,
                             'd_RB_design_coordinate':d,'Gaussian_input_sigma_over_I':width,
                             'actual_discrete_rms_M_over_I':float(math.sqrt(np.dot(w,m*m))/(two_i/2)),
                             'ideal_point_W154_over_W90':float(r),'ideal_local_P_stokes90':float(p)})
    return {'status':'conditional-halfspin-singles-kernel','scope':'Ideal single-photon rest-frame response only. No original PDCO/cascade/finite-detector/data fit.',
            'source_premises':['RB67 printed312fn7/316Eq3.24 and linear paragraph/319Eq3.39','DR96 printed522Eq19,523 singles versus finite coincidence boundaries'],
            'coordinate':'d_RB=a_E2/a_M1, RB67 interaction amplitude with initial state on left; not an assumed mapping of actual Pr/Au published delta',
            'population':'normalized exp[-M^2/(2sigma^2)], sigma input width; not equal to truncated discrete RMS in general',
            'linear_axes':'xprime=(cos(theta),0,-sin(theta)) in emission plane; yprime=(0,1,0); P_stokes=(Ix-Iy)/(Ix+Iy). Experiment axes and phase convention not certified.',
            'controls':controls,'control_details':details,'all_controls_pass':all(controls.values()),'results':rows,
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            'limitations':['No actual finite detector solid angles, efficiencies, selected all-angle gate/cascade, sidefeeding or deorientation response supplied.',
                           'Nominal154/90 point ratio and local90 Stokes are not measured Rac/P or a reconstruction of Pr angle groups/Au array.',
                           'Physical experiment delta phase/normalization and P analysis-axis mapping must be established from original analysis conventions before numerical fitting.',
                           'D96 explicitly defines Gaussian width; Lv variance wording is not silently certified to use this same parameter.',
                           'Local rank2 in a chosen ideal map does not prove global injectivity or actual likelihood root selection/equal minima.',
                           'No Q, a, count rates, covariance, actual delta/CI, lifetime or beamtime generated; SH26 fixed sigma/I conditional support retained.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=calculate();a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':result['all_controls_pass'],'checks':len(result['controls']),
                      'controls':result['controls'],'details':result['control_details'],'design_rows':len(result['results'])},ensure_ascii=False))
    return 0 if result['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
