#!/usr/bin/env python3
"""Uncredited Day24 preview: antiunitary algebra, not nuclear-state evidence."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import spin_matrices


def anti_transform(unitary,operator):
    return unitary@operator.conj()@unitary.T.conj()


def calculate():
    controls,rows={},[]
    for two_j in [1,2,3,5,8]:
        axes=spin_matrices(two_j);values,vectors=np.linalg.eigh(axes[1])
        r=(vectors*np.exp(-1j*math.pi*values))@vectors.T.conj()
        t=r  # Time reversal is T=t*K, where K conjugates coefficients.
        c=r@t  # C=R_y(pi)*T; T commutes with this physical rotation.
        ident=np.eye(two_j+1);phase=(-1)**two_j
        errors={'R_unitarity':float(np.max(abs(r.T.conj()@r-ident))),
                'R_square':float(np.max(abs(r@r-phase*ident))),
                'T_antiunitary_square':float(np.max(abs(t@t.conj()-phase*ident))),
                'C_antiunitary_square':float(np.max(abs(c@c.conj()-ident))),
                'C_is_phase_times_K':float(np.max(abs(c-phase*ident))),
                'T_reverses_all_J':max(float(np.max(abs(anti_transform(t,j)+j))) for j in axes),
                'C_reflects_only_Jy':max(float(np.max(abs(anti_transform(c,j)-s*j)))
                                        for s,j in zip([1,-1,1],axes))}
        for name,error in errors.items():controls[f'j2_{two_j}_{name}']=error<2e-12
        # A concrete mathematical C-symmetric, nondegenerate Hamiltonian.
        # It is NOT a rotationally invariant laboratory nuclear Hamiltonian.
        h=axes[2]+.37*axes[0]
        spectrum,ev=np.linalg.eigh(h)
        symmetry=float(np.max(abs(anti_transform(c,h)-h)))
        minimum_gap=float(np.min(np.diff(spectrum)))
        controls[f'j2_{two_j}_C_symmetric_can_be_nondegenerate']=symmetry<2e-12 and minimum_gap>.1
        psi=ev[:,0]
        overlap=complex(np.vdot(psi,c@psi.conj()))
        alpha=.317;rephased=np.exp(1j*alpha)*psi
        overlap_rephased=complex(np.vdot(rephased,c@rephased.conj()))
        controls[f'j2_{two_j}_antiunitary_eigenphase_is_not_fixed_sign']=abs(
            overlap_rephased-overlap*np.exp(-2j*alpha))<2e-12 and abs(abs(overlap)-1)<2e-12
        rows.append({'two_j':two_j,'T_square_phase':phase,'C_square':1,'matrix_errors':errors,
                     'counterexample_minimum_eigenvalue_gap_dimensionless':minimum_gap,
                     'C_partner_overlap_abs':abs(overlap),
                     'scope':'Representation/algebra counterexample only; no nuclear level, splitting, rotation domain or band assignment.'})
    sx=np.array([[0,1],[1,0]],complex);sz=np.diag([1.,-1.]);ident=np.eye(2)
    controls['localized_C_exchanges_L_R']=bool(np.allclose(sx@np.array([1.,0.]),[0.,1.]))
    controls['twolevel_C_square_plus1']=bool(np.allclose(sx@sx.conj(),ident))
    controls['twolevel_order_parameter_C_odd']=bool(np.allclose(anti_transform(sx,sz),-sz))
    controls['twolevel_dimensionless_operator_C_even']=bool(np.allclose(anti_transform(sx,sx),sx))
    tunnel=[]
    for tvalue in [.01,1.]:
        h=tvalue*sx;en,v=np.linalg.eigh(h)
        means=[float(np.vdot(v[:,n],sz@v[:,n]).real) for n in range(2)]
        variances=[float(np.vdot(v[:,n],sz@sz@v[:,n]).real) for n in range(2)]
        evenmeans=[float(np.vdot(v[:,n],sx@v[:,n]).real) for n in range(2)]
        controls[f't_{tvalue}_Csymmetry_with_nonzero_tunnelling']=bool(np.allclose(anti_transform(sx,h),h))
        controls[f't_{tvalue}_splitting_twice_abs_t']=math.isclose(en[1]-en[0],2*abs(tvalue),abs_tol=1e-14)
        controls[f't_{tvalue}_restored_mean0_fluctuation1']=max(abs(x) for x in means)<1e-14 and max(abs(x-1) for x in variances)<1e-14
        controls[f't_{tvalue}_C_even_stationary_values_need_not_equal']=bool(np.allclose(evenmeans,[-1,1],atol=1e-14))
        tunnel.append({'dimensionless_t_design':tvalue,'dimensionless_gap':float(en[1]-en[0]),
                       'order_parameter_means':means,'order_parameter_squared_means':variances,
                       'dimensionless_C_even_operator_means':evenmeans,
                       'physical_g_formula_only':'If a g-like C-even scalar were g0*I+g1*sigma_x, its two means would be g0-g1 and g0+g1; no physical coefficients assigned.'})
    r=spin_matrices(1)[1];values,v=np.linalg.eigh(r);ty=(v*np.exp(-1j*math.pi*values))@v.T.conj()
    psi=np.array([1.,0.]);c=ty@ty
    controls['spinhalf_Kramers_T_partner_orthogonal']=abs(np.vdot(psi,ty@psi.conj()))<1e-14
    controls['same_vector_chiral_C_partner_not_forced_orthogonal']=abs(abs(np.vdot(psi,c@psi.conj()))-1)<1e-14
    return {'status':'uncredited-Day24-antiunitary-math-preview','execution_day_index':23,
            'formal_credit':False,'source_premises':['F01 printed476/PDF14 T*Ry(pi) chirality operation','FM97 printed138–142 intrinsicplanar/aplanar/signature and quantum tunnelling boundary'],
            'conventions':'Ordinary spin algebra, |j,mz> basis, K=complex conjugation, R=exp(-i*pi*Jy), T=R*K, C=R*T. Coordinate y selected by convention.',
            'conclusion':'T^2=(-1)^(2j), but [R_y(pi)T]^2=+1. This chiral antiunitary symmetry alone does not impose Kramers degeneracy or fixed +/- symmetry labels.',
            'representation_results':rows,'twolevel_design_results':tunnel,
            'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            'limitations':['No actual nuclear state, spectrum, physical tunnelling strength, g factor, chirality parameter or experimental confidence bound is calculated.',
                           'The C-symmetric spin matrix counterexample is not a rotationally invariant lab nuclear Hamiltonian; it only checks that the antiunitary algebra does not force degeneracy.',
                           'Intrinsic mean-field solutions and laboratory good-spin bands are distinct; ordinary magnetic-substate/Kramers degeneracy is not two distinct partner bands.',
                           'Zero signed order parameter in a finite symmetry-restored eigenstate does not alone disprove intrinsic chirality; a nonzero model fluctuation does not establish it experimentally.',
                           'C-even operator equality is not automatic for different eigenstates. The dimensionless example does not prove an actual measured g difference or establish a universal chirality test.',
                           'Existing Qt-proxy CI and225.8keV P-sign/beamtime exclusions remain withdrawn; no Day24 credit or Day25 preview.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=calculate();a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':result['all_controls_pass'],'checks':len(result['controls']),
                      'maximum_spin_matrix_error':max(max(r['matrix_errors'].values()) for r in result['representation_results']),
                      'twolevel_design_results':result['twolevel_design_results']},ensure_ascii=False))
    return 0 if result['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
