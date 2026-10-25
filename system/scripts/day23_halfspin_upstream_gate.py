#!/usr/bin/env python3
"""Declared halfspin cascade trace/gate component, not the actual Pr response."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import clebsch_gordan
from day23_halfspin_singles_response import LINEAR, photon_parts, population


def amplitudes(two_i,two_f,theta,kind,d_rb=0):
    dipole,quadrupole=photon_parts(two_i,two_f,theta)
    if kind=='E2':
        return quadrupole
    if kind=='M1':
        return dipole
    if kind=='M1/E2':
        return (dipole+d_rb*quadrupole)/math.sqrt(1+d_rb*d_rb)
    raise ValueError('Unsupported declared multipoles')


def channels(two_i,two_f,kind,d_rb=0):
    """Exact complete solid-angle channel in photon magnetic substates."""
    parts={'E2':[(2,1.)],'M1':[(1,1.)],
           'M1/E2':[(1,1/math.sqrt(1+d_rb*d_rb)),(2,d_rb/math.sqrt(1+d_rb*d_rb))]}[kind]
    matrices=[]
    for rank,a in parts:
        for mu in range(-rank,rank+1):
            matrix=np.zeros((two_f+1,two_i+1))
            for f,mf in enumerate(np.arange(-two_f,two_f+1,2)/2):
                for i,mi in enumerate(np.arange(-two_i,two_i+1,2)/2):
                    if abs(mi-mf-mu)<1e-12:
                        matrix[f,i]=a*clebsch_gordan(two_f/2,mf,rank,mu,two_i/2,mi)
            matrices.append(matrix)
    return matrices


def map_density(kraus,rho):
    return sum(k@rho@k.T.conj() for k in kraus)


def point_daughter(two_i,two_f,kind,d_rb,theta,rho):
    a=amplitudes(two_i,two_f,theta,kind,d_rb)
    return np.einsum('hfi,ij,hgj->fg',a,rho,a.conj())


def full_daughter_quadrature(two_i,two_f,kind,d_rb,rho,nodes):
    if np.max(abs(rho-np.diag(np.diag(rho))))>1e-12:
        raise ValueError('This azimuth-integrated route explicitly assumes initial Mi-diagonal density')
    x,w=np.polynomial.legendre.leggauss(nodes)
    result=np.zeros((two_f+1,two_f+1),complex)
    # At each theta the azimuth integral removes nuclear off-diagonal terms
    # for this axisymmetric initial state. This is not point-gate dephasing.
    for c,weight in zip(x,w):
        daughter=point_daughter(two_i,two_f,kind,d_rb,math.acos(float(c)),rho)
        result+=weight/2*np.diag(np.diag(daughter))
    return result


def photon_density(two_i,two_f,kind,d_rb,theta,rho):
    a=amplitudes(two_i,two_f,theta,kind,d_rb)
    return np.einsum('hfi,ij,kfj->hk',a,rho,a.conj())


def observable(h):
    linear=LINEAR@h@LINEAR.T.conj()
    intensity=float(np.trace(linear).real)
    q=float((linear[0,0]-linear[1,1]).real)
    return {'intensity':intensity,'P_stokes':q/intensity if intensity>1e-14 else None,
            'min_helicity_eigenvalue':float(np.linalg.eigvalsh(h)[0])}


def target_pair(two_i,two_f,d_rb,rho):
    p90=observable(photon_density(two_i,two_f,'M1/E2',d_rb,math.pi/2,rho))
    p154=observable(photon_density(two_i,two_f,'M1/E2',d_rb,math.radians(154),rho))
    return {'point_W154_over_W90':p154['intensity']/p90['intensity'],
            'local_P_stokes90':p90['P_stokes'],'normalized_daughter_trace':float(np.trace(rho).real)}


def calculate():
    controls,details,rows={},{},[]
    for name,spins,gate,gate_d in [('796_to_813_spins_only',[25,21,19],'E2',0.),
                                  ('450_to_747_spins_only',[19,17,15],'M1/E2',-.5)]:
        a,b,c=spins;rho=np.diag(population(a,.2));target_d=-.5
        ck=channels(a,b,gate,gate_d)
        effect=sum(k.T.conj()@k for k in ck)
        full=map_density(ck,rho)
        q24=full_daughter_quadrature(a,b,gate,gate_d,rho,24)
        q40=full_daughter_quadrature(a,b,gate,gate_d,rho,40)
        iso=map_density(ck,np.eye(a+1)/(a+1))
        unit_error=float(np.max(abs(effect-np.eye(a+1))))
        quad_error=float(np.max(abs(full-q40)))
        conv_error=float(np.max(abs(q24-q40)))
        iso_error=float(np.max(abs(iso-np.eye(b+1)/(b+1))))
        controls[name+'_fourpi_channel_trace_preserving']=unit_error<1e-12
        controls[name+'_fourpi_CG_vs_Wigner_integral']=quad_error<1e-12
        controls[name+'_quadrature_node_convergence']=conv_error<1e-12
        controls[name+'_isotropic_channel_limit']=iso_error<1e-12
        details[name]={'channel_effect_identity_error':unit_error,'CG_quadrature_error':quad_error,
                       'quadrature_24_40_error':conv_error,'isotropic_channel_error':iso_error}
        full_outputs=target_pair(b,c,target_d,full)
        reset_outputs=target_pair(b,c,target_d,np.diag(population(b,.2)))
        m=np.arange(-b,b+1,2)/2
        row={'case':name,'spins_twice':spins,'gate_kind':gate,'gate_d_RB_design':gate_d,
             'initial_Gaussian_input_sigma_over_I':.2,'target_d_RB_design':target_d,
             'fourpi_upstream_daughter':{'actual_rms_M_over_I':float(math.sqrt(np.dot(np.diag(full).real,m*m))/(b/2)),
                                         **full_outputs},
             'independently_reset_target_Gaussian_is_another_model':reset_outputs,'point_coplanar_gates':[]}
        min_eig,trace_error,direct_error=0.,0.,0.
        max_coherence,max_dephase_delta=0.,0.
        for theta in [0.,45.,90.,135.,180.]:
            un=point_daughter(a,b,gate,gate_d,math.radians(theta),rho)
            gate_yield=float(np.trace(un).real)
            daughter=un/gate_yield
            min_eig=min(min_eig,float(np.linalg.eigvalsh(daughter)[0]))
            trace_error=max(trace_error,abs(float(np.trace(daughter).real)-1))
            coherence=float(np.linalg.norm(daughter-np.diag(np.diag(daughter))))
            max_coherence=max(max_coherence,coherence)
            output=target_pair(b,c,target_d,daughter)
            dephased=target_pair(b,c,target_d,np.diag(np.diag(daughter)))
            max_dephase_delta=max(max_dephase_delta,abs(output['local_P_stokes90']-dephased['local_P_stokes90']))
            g=amplitudes(a,b,math.radians(theta),gate,gate_d)
            t=amplitudes(b,c,math.pi/2,'M1/E2',target_d)
            joint=np.einsum('bfj,aji->abfi',t,g)
            direct=np.einsum('abfi,ij,acfj->bc',joint,rho,joint.conj())
            sequential=photon_density(b,c,'M1/E2',target_d,math.pi/2,un)
            direct_error=max(direct_error,float(np.max(abs(direct-sequential))))
            row['point_coplanar_gates'].append({'theta_gate_deg':theta,'relative_gate_directional_yield':gate_yield,
                'daughter_offdiagonal_Frobenius_norm':coherence,'target_conditional':output,
                'target_after_discarding_coherence_is_another_model':dephased})
        controls[name+'_normalized_positive_daughter']=min_eig>-1e-12 and trace_error<1e-12
        controls[name+'_direct_joint_equals_sequential_density']=direct_error<1e-12
        controls[name+'_finite_coplanar_gate_creates_coherence']=max_coherence>.01
        controls[name+'_discarded_coherence_can_change_target_P']=max_dephase_delta>.01
        details[name].update({'min_daughter_eigenvalue':min_eig,'max_trace_error':trace_error,
                              'direct_joint_vs_sequential_error':direct_error,'max_coherence':max_coherence,
                              'max_dephasing_P_shift_design':max_dephase_delta})
        # Complete FUTURE gamma trace: compose with every exact integrated
        # Kraus, retaining the already-emitted photon's helicity coherence.
        g=amplitudes(a,b,.47,gate,gate_d)
        gate_h=np.einsum('hfi,ij,kfj->hk',g,rho,g.conj())
        after=np.zeros((2,2),complex)
        for k in channels(b,c,'M1/E2',target_d):
            composed=np.einsum('fj,hji->hfi',k,g)
            after+=np.einsum('hfi,ij,kfj->hk',composed,rho,composed.conj())
        future_error=float(np.max(abs(after-gate_h)))
        controls[name+'_future_fourpi_trace_preserves_earlier_photon']=future_error<1e-12
        details[name]['future_trace_error']=future_error
        rows.append(row)
    # Known halfspin M1/M1 correlation for an isotropic initial ensemble.
    initial=np.eye(2)/2
    un=point_daughter(1,3,'M1',0,0,initial);daughter=un/np.trace(un)
    analytic_error=0.
    for angle in [0.,30.,60.,90.,120.,180.]:
        actual=observable(photon_density(3,1,'M1',0,math.radians(angle),daughter))['intensity']
        expected=1+.25*(3*math.cos(math.radians(angle))**2-1)/2
        analytic_error=max(analytic_error,abs(actual-expected))
    controls['halfspin_onehalf_threehalf_onehalf_M1_cascade_analytic']=analytic_error<1e-12
    details['halfspin_M1_M1_analytic_error']=analytic_error
    return {'status':'conditional-halfspin-upstream-gate-component','scope':'Declared cascade design with source spin/gate identities only, no original experimental response refit.',
            'source_premises':['L22-14 and SI Table1: upstream796/450 gate identities','RB67 printed325 Eqs3.65/66 and326Eqs3.71-73','DR96 printed521Eqs13-15'],
            'convention':'source013 RB interaction coordinates, coplanarphi0; full-azimuth integration handled as a diagonal-density channel, no directed-azimuth convention claim',
            'results':rows,'controls':{k:bool(v) for k,v in controls.items()},'control_details':details,
            'all_controls_pass':all(controls.values()),
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [
                Path(__file__),Path(__file__).with_name('day23_halfspin_singles_response.py'),
                Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            'limitations':['The selected initial sigma/I and target/gate d_RB are mathematical design inputs, not measured Lv feeding or delta values.',
                           'Only the upstream796 pureE2 identity is source given;450-shaped gate d_RB=-.5 is a declared probe, not the published -.31 mapped to RB.',
                           'A point coplanar directional gate is not the actual all-detector array. Azimuth-averaged ring results/weights are not silently substituted.',
                           'Finite gate effects can exist mathematically; their actual size or residual correction in the published analysis is not inferred.',
                           'Source-clean spectra and detector/gating conditional-density response are separate issues; no contamination or experimental error is established here.',
                           'No physical P/Rac fit, delta/Q/a/tau/CI/count rate or beamtime generated. Published conditional SH26 support and unresolved joint likelihood remain.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=calculate();a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':result['all_controls_pass'],'checks':len(result['controls']),
                      'controls':result['controls'],'details':result['control_details'],'results':result['results']},ensure_ascii=False))
    return 0 if result['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
