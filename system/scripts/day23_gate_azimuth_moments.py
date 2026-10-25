#!/usr/bin/env python3
"""Ideal gate azimuth moments, no measured array efficiency/acceptance."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_halfspin_singles_response import population
from day23_halfspin_upstream_gate import amplitudes,point_daughter,target_pair,channels,map_density


def acceptances(n,modulation=0.,offset=0.):
    phi=np.arange(n)*2*math.pi/n+offset
    weights=1+modulation*np.cos(2*(phi-offset))
    if np.min(weights)<=0:
        raise ValueError('This design requires strictly positive acceptance weights')
    return phi,weights/sum(weights)


def moments(phi,weights,max_q=4):
    if min(weights)<0 or abs(sum(weights)-1)>1e-12:
        raise ValueError('Acceptance weights must be normalized and nonnegative')
    return {q:complex(np.dot(weights,np.exp(1j*q*phi))) for q in range(-max_q,max_q+1)}


def twirl(daughter,phi,weights):
    mf=np.arange(-(len(daughter)-1),len(daughter),2)/2
    answer=np.zeros_like(daughter,dtype=complex)
    for angle,w in zip(phi,weights):
        z=np.exp(1j*mf*angle)
        answer+=w*z[:,None]*daughter*z[None,:].conj()
    return answer


def explicit_gate(two_i,two_f,kind,d_rb,theta,rho,phi,weights):
    a=amplitudes(two_i,two_f,theta,kind,d_rb)
    mi=np.arange(-two_i,two_i+1,2)/2
    mf=np.arange(-two_f,two_f+1,2)/2
    answer=np.zeros((two_f+1,two_f+1),complex)
    for angle,w in zip(phi,weights):
        g=a*np.exp(-1j*(mi[None,:]-mf[:,None])*angle)[None,:,:]
        answer+=w*np.einsum('hfi,ij,hgj->fg',g,rho,g.conj())
    return answer


def moment_route(daughter,eta):
    mf=np.arange(-(len(daughter)-1),len(daughter),2)/2
    return np.array([[daughter[f,k]*eta.get(int(round(m-mp)),0j)
                      for k,mp in enumerate(mf)] for f,m in enumerate(mf)])


def calculate():
    controls,details,rows={},{},[]
    for name,a,b,c,kind,gate_d in [('796_to_813_design',25,21,19,'E2',0.),
                                  ('450_to_747_design',19,17,15,'M1/E2',-.5)]:
        rho=np.diag(population(a,.2));theta=math.pi/2
        un=point_daughter(a,b,kind,gate_d,theta,rho)
        diagonal=np.diag(np.diag(un))
        mf=np.arange(-b,b+1,2)/2
        q=np.rint(mf[:,None]-mf[None,:]).astype(int)
        highrank=float(np.max(abs(un[abs(q)>4])))
        controls[name+'_gate_Lmax2_offdiagonal_rank_bound']=highrank<1e-12
        max_rotation_error=max_moment_error=max_explicit_error=0.
        minimum_eig=0.;case_rows=[];c4_remaining=0.
        for n,mod,label in [(4,0.,'uniform_C4'),(5,0.,'uniform_C5'),(12,0.,'uniform_C12'),
                            (12,.2,'C12_positive_cos2_weights')]:
            phi,w=acceptances(n,mod);eta=moments(phi,w)
            z=twirl(un,phi,w);via_eta=moment_route(un,eta)
            direct=explicit_gate(a,b,kind,gate_d,theta,rho,phi,w)
            max_moment_error=max(max_moment_error,float(np.max(abs(z-via_eta))))
            max_explicit_error=max(max_explicit_error,float(np.max(abs(z-direct))))
            znorm=z/np.trace(z);minimum_eig=min(minimum_eig,float(np.linalg.eigvalsh(znorm)[0]))
            offdiag=float(np.linalg.norm(znorm-np.diag(np.diag(znorm))))
            if label=='uniform_C4':
                c4_remaining=offdiag
            if label in ['uniform_C5','uniform_C12']:
                controls[name+'_'+label+'_removes_all_nonzero_gate_harmonics']=float(np.max(abs(z-diagonal)))<1e-12
            if mod:
                controls[name+'_cos2_acceptance_eta2_analytic']=abs(eta[2]-.1)<1e-13
                controls[name+'_cos2_acceptance_other_lowharmonics_zero']=max(abs(eta[t]) for t in [1,3,4])<1e-13
            alpha=.317;shifted=twirl(un,phi+alpha,w)
            zz=np.exp(1j*mf*alpha)
            max_rotation_error=max(max_rotation_error,float(np.max(abs(shifted-zz[:,None]*z*zz[None,:].conj()))))
            case_rows.append({'acceptance_design':label,'n':n,'positive_weight_min':float(min(w)),
                              'eta_q_0_to_4':{str(t):[eta[t].real,eta[t].imag] for t in range(5)},
                              'daughter_offdiagonal_Frobenius_norm':offdiag,
                              'target_design':target_pair(b,c,-.5,znorm)})
        controls[name+'_C4_can_retain_rank4_coherence']=c4_remaining>1e-3
        controls[name+'_Fourier_moment_route_matches_density_twirl']=max_moment_error<1e-12
        controls[name+'_explicit_photon_phase_route_matches_twirl']=max_explicit_error<1e-12
        controls[name+'_global_azimuth_rotation_covariance']=max_rotation_error<1e-12
        controls[name+'_positive_acceptance_preserves_density_PSD']=minimum_eig>-1e-12
        phi,w=acceptances(128);continuous=twirl(un,phi,w)
        controls[name+'_fine_uniform_phi_integral_is_diagonal']=float(np.max(abs(continuous-diagonal)))<1e-12
        full=map_density(channels(a,b,kind,gate_d),rho)
        fixed_polar=diagonal/np.trace(diagonal)
        controls[name+'_uniform_azimuth_is_not_full_fourpi']=float(np.max(abs(fixed_polar-full)))>1e-5
        details[name]={'max_abs_q_above4_matrix_element':highrank,
                       'max_density_twirl_vs_Fourier_error':max_moment_error,
                       'max_density_twirl_vs_explicit_phase_error':max_explicit_error,
                       'max_global_azimuth_rotation_error':max_rotation_error,
                       'min_density_eigenvalue':minimum_eig,
                       'uniform_fixedtheta_vs_fourpi_density_max_difference':float(np.max(abs(fixed_polar-full)))}
        rows.append({'case':name,'spins_twice':[a,b,c],'design_only':True,
                     'initial_sigma_over_I':.2,'gate_kind':kind,'gate_d_RB':gate_d,'gate_theta_deg':90.,
                     'target_d_RB':-.5,'target_phi_origin':0,
                     'point_coplanar_gate_target':target_pair(b,c,-.5,un/np.trace(un)),
                     'full_fourpi_gate_target':target_pair(b,c,-.5,full),'azimuth_acceptance_designs':case_rows})
    return {'status':'conditional-gate-azimuth-moment-component','scope':'Positive ideal fixed-polar-angle gate acceptance mixtures, not actual JUROGAM/HIRFL response or experimental error.',
            'rotation':'G(phi)[f,i]=exp[-i(mi-mf)phi]G(0)[f,i]; rho_f(phi)=Z(phi)rho_f(0)Zdagger, Z_ff=exp(i mf phi)',
            'moment_identity':'rho_bar[f,fprime]=rho0[f,fprime]*eta_(mf-mfprime), eta_q=sum w exp(iqphi), |q|<=4 for diagonal initial density and M1/E2 gate.',
            'controls':{k:bool(v) for k,v in controls.items()},'control_details':details,
            'all_controls_pass':all(controls.values()),'results':rows,
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),
                Path(__file__).with_name('day23_halfspin_upstream_gate.py'),Path(__file__).with_name('day23_halfspin_singles_response.py'),
                Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            'limitations':['Exact cancellation requires the effective weights for the selected target/gate detector pairs, not only uniformly spaced nominal array positions.',
                           'Per-detector efficiencies/live time, target-dependent coincidence selection/vetoes and Compton conditions can break a marginal gate symmetry.',
                           'Uniform azimuth at one polar angle still changes diagonal population relative to full fourpi; it does not certify an independent Gaussian daughter.',
                           'At varying polar angles combine unnormalized conditional densities/yields before forming normalized polarization; do not average P values.',
                           'The width and d_RB are declared design inputs. Source014 actual gate identities do not provide full array weights or an actual delta/P mapping.',
                           'No measured acceptance Fourier moment, actual bias, data fit, physical delta/Q/tau/CI or beamtime computed.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate();a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'controls':r['controls'],'details':r['control_details'],'results':r['results']},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
