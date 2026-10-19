#!/usr/bin/env python3
"""Rest-frame spin-half angular constraints, not a reconstruction of Sun's fit."""
from pathlib import Path
import hashlib,json,math
from functools import lru_cache
import numpy as np
import sympy as s
from sympy.physics.wigner import clebsch_gordan as cg
from day16_co60_conditional_stokes import operators,stokes
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact_effect(jf2,parts):
    d=s.symbols('d',real=True);norm=0;B=[]
    for kind,L,a in parts:norm+=a*a
    for h in [-1,1]:
        matrix=s.zeros(jf2+1,2)
        for f,mf in enumerate(range(-jf2,jf2+1,2)):
            for i,mi in enumerate([-1,1]):
                for kind,L,a in parts:
                    if mi-mf==2*h:
                        matrix[f,i]+=(-1)**L*a*s.sqrt(s.Rational(2*L+1,2))*cg(s.Rational(jf2,2),L,s.Rational(1,2),s.Rational(mf,2),h,s.Rational(mi,2))*(h if kind=='M' else 1)
        B.append(matrix)
    E=s.simplify((B[0].T*B[0]+B[1].T*B[1])/norm)
    coherence=s.simplify(B[0].T*B[1]/norm)
    return E,coherence

def main():
    p=RUN/'spinhalf-angular-contract.json';c=json.loads(p.read_text());assert c['identity']=='SUN23-SPINHALF-RESTFRAME-ANGULAR-CONTRACT-01'
    for path,h in c['source_and_helper_hashes'].items():assert sha(ROOT/path)==h,path
    d=s.symbols('d',real=True);cases=[('M1_to_half',1,(('M',1,s.Integer(1)),)),('M1_E2_to_threehalf',3,(('M',1,s.Integer(1)),('E',2,d))),('E2_M3_to_fivehalf',5,(('E',2,s.Integer(1)),('M',3,d))),('E1_M2_to_threehalf',3,(('E',1,s.Integer(1)),('M',2,d)))]
    exact=[]
    for name,jf,parts in cases:
        E,C=exact_effect(jf,parts);assert E==s.eye(2) and C==s.zeros(2)
        exact.append({'case':name,'fourpi_intensity_effect_exact':str(E),'fourpi_helicity_coherence_effect_exact':str(C)})
    blochs=c['Bloch_vectors'];pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1.,-1.])]
    # Basis of helpers is ascending m=(-1/2,+1/2); Bloch coordinates here refer
    # to this declared matrix basis, not the paper's lab spin components.
    rhos=[(np.eye(2,dtype=complex)+sum(z*P for z,P in zip(v,pauli)))/2 for v in blochs]
    assert all(np.linalg.eigvalsh(r).min()>-1e-12 for r in rhos)
    maximum_I=maximum_linear=maximum_physical=0.;maxV=0.;points=0
    for name,jf,formalparts in cases:
        for delta in ([0.] if len(formalparts)==1 else c['delta_design_values']):
            parts=tuple((k,L,float(a.subs(d,delta))) for k,L,a in formalparts)
            for theta in c['theta_deg']:
                for phi in c['phi_rad']:
                    T=operators(1,jf,parts,math.radians(theta),phi,'native')
                    E=4*math.pi*np.einsum('afi,afj->ij',T.conj(),T);maximum_I=max(maximum_I,float(np.max(abs(E-np.eye(2)))))
                    for rho in rhos:
                        H=np.einsum('afi,ij,bfj->ab',T,rho,T.conj());z=stokes(H,4*math.pi);I,Q,U,V=z['IQUV'];maximum_I=max(maximum_I,abs(I-1));maximum_linear=max(maximum_linear,abs(Q),abs(U));maxV=max(maxV,abs(V));maximum_physical=max(maximum_physical,Q*Q+U*U+V*V-I*I);points+=1
    assert maximum_I<1e-11 and maximum_linear<1e-11 and maximum_physical<1e-11 and maxV>.9
    # Genuine rank2 control: Ji=3/2 with equal low-|m| population, pureM1.
    rho=np.diag([0.,.5,.5,0.]);control=[]
    for angle in [0.,30.,60.,90.,120.,180.]:
        T=operators(3,1,(('M',1,1.),),math.radians(angle),0.,'native');H=np.einsum('afi,ij,bfj->ab',T,rho,T.conj());I=stokes(H,4*math.pi)['IQUV'][0];x=math.cos(math.radians(angle));expected=1-.5*(3*x*x-1)/2;assert abs(I-expected)<1e-12;control.append({'theta_deg':angle,'I_native':I,'I_1_minus_half_P2':expected})
    # Counterexample to extending singles rank bound to a photon gate after
    # the transition: 1/2 -> 3/2 -> 1/2, pure M1/M1, isotropic initial rho.
    finalgate=[]
    for angle in [0.,30.,60.,90.,120.,180.]:
        T1=operators(1,3,(('M',1,1.),),math.radians(angle),0.,'native')
        T2=operators(3,1,(('M',1,1.),),0.,0.,'native')
        joint=np.einsum('bfj,aji->abfi',T2,T1)
        intensity=float((4*math.pi)**2*np.sum(abs(joint)**2)/2)
        xg=math.cos(math.radians(angle));expected=1+.25*(3*xg*xg-1)/2
        assert abs(intensity-expected)<1e-12
        finalgate.append({'theta_deg':angle,'joint_native_I':intensity,'I_1_plus_quarter_P2':expected})
    # Explicit assumption-failure control: parity-violating E1+M1 is not one
    # same-parity nuclear transition. It can carry rank1, still no rank2.
    E,C=exact_effect(1,(('E',1,s.Integer(1)),('M',1,d)));assert C==s.zeros(2) and s.simplify(s.trace(E)-2)==0
    # An isotropic rest source becomes anisotropic in the lab after a boost.
    beta=c['boost_design_beta'];x=s.symbols('x',real=True);b=s.symbols('b',positive=True);J=(1-b*b)/(1-b*x)**2;assert s.simplify(s.integrate(J,(x,-1,1))/2)==1
    n,w=np.polynomial.legendre.leggauss(120);v=(1-beta*beta)/(1-beta*n)**2;legendre=[float((2*k+1)/2*np.sum(w*v*np.polynomial.legendre.legval(n,[0]*k+[1]))) for k in range(5)];assert abs(legendre[0]-1)<1e-12 and legendre[2]>.01
    result={'identity':c['identity'],'script_sha256':sha(__file__),'contract_sha256':sha(p),'exact_spinhalf_effects':exact,'native_points_declared_models_not_data':points,'max_I_minus1_or_effect_identity_residual':maximum_I,'max_linear_Q_U':maximum_linear,'max_circular_abs_V_in_declared_states':maxV,'max_positive_PSD_residual':maximum_physical,'Ji_threehalf_rank2_countercontrol':control,'postselected_final_gamma_gate_countercontrol':finalgate,'parity_violating_rank1_assumption_control_effect':str(E),'boost_design':{'beta':beta,'angular_Jacobian':'(1-beta^2)/(1-beta*cos(theta_lab))^2','Legendre_a0_to_a4':legendre,'small_beta_series':'1+2 beta P1+2 beta^2 P2+O(beta^3)','not_actual_Sun_velocity_or_A2':True},'conclusion':'rest nuclearA2=0 forJi1/2 conditionalmodel; doesnotidentifySunA2frame/phenomenologicalrole or actualtauimpact','actual_paper_A2_object_unknown':True,'experimental_refit_or_new_CI':False,'assumptions':c['assumptions'],'ok':True};(RUN/'spinhalf-angular-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['ok','exact_spinhalf_effects','max_I_minus1_or_effect_identity_residual','max_linear_Q_U','max_circular_abs_V_in_declared_states','boost_design','actual_paper_A2_object_unknown']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
