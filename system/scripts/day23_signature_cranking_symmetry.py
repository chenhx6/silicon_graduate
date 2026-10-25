#!/usr/bin/env python3
"""Signature/T/C in a declared intrinsic spin Routhian, not nuclear bands."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import spin_matrices


def calculate():
    controls,rows={},[]
    for two_j in [1,2,3,4,5,11]:
        j=two_j/2;jx,jy,jz=spin_matrices(two_j);n=two_j+1;identity=np.eye(n)
        rz=np.diag(np.exp(-1j*math.pi*np.diag(jz)))
        values,vectors=np.linalg.eigh(jy)
        ry=(vectors*np.exp(-1j*math.pi*values))@vectors.T.conj()
        t=ry;c=ry@ry;anti=lambda u,op:u@op.conj()@u.T.conj()
        h0=.3*jz@jz+.07*(jx@jx-jy@jy)
        tag=f'j2_{two_j}'
        controls[tag+'_signature_unitary_and_twofold_phase']=bool(np.allclose(rz.T.conj()@rz,identity,atol=1e-12) and np.allclose(rz@rz,(-1)**two_j*identity,atol=1e-12))
        controls[tag+'_time_and_chiral_squares']=bool(np.allclose(t@t.conj(),(-1)**two_j*identity,atol=1e-12) and np.allclose(c@c.conj(),identity,atol=1e-12))
        data=[]
        for omega in [0.,.2]:
            h=h0-omega*jz;reverse=h0+omega*jz
            symmetry={'signature_commutator':float(np.max(abs(h@rz-rz@h))),
                      'T_links_opposite_frequency':float(np.max(abs(anti(t,h)-reverse))),
                      'fixed_frequency_C_symmetry':float(np.max(abs(anti(c,h)-h))),
                      'fixed_frequency_T_change_norm':float(np.max(abs(anti(t,h)-h)))}
            controls[tag+f'_omega_{omega}_h_Hermitian']=bool(np.allclose(h,h.T.conj(),atol=1e-12))
            controls[tag+f'_omega_{omega}_Rz_Tbridge_C']=max(symmetry[k] for k in ['signature_commutator','T_links_opposite_frequency','fixed_frequency_C_symmetry'])<1e-12
            if omega:
                controls[tag+'_nonzero_frequency_breaks_T']=symmetry['fixed_frequency_T_change_norm']>.01
            eigenvalues,eigenvectors=np.linalg.eigh(h)
            psi=eigenvectors[:,0];unitphase=complex(np.vdot(psi,rz@psi))
            shifted=np.exp(.317j)*psi
            controls[tag+f'_omega_{omega}_unitary_signature_phase_independent']=abs(complex(np.vdot(shifted,rz@shifted))-unitphase)<1e-12
            # Only half-integer j has two equal-size +/-i blocks exchanged by T.
            blocks=None
            if two_j%2:
                indices=[np.where(np.diag(rz).imag>0)[0],np.where(np.diag(rz).imag<0)[0]]
                spectra=[np.linalg.eigvalsh(h[np.ix_(ids,ids)]) for ids in indices]
                diff=float(np.max(abs(spectra[0]-spectra[1])))
                lowest=float(abs(spectra[0][0]-spectra[1][0]))
                controls[tag+f'_omega_{omega}_halfspin_Kramers_scope']=(diff<1e-12 if omega==0 else lowest>1e-4)
                for ids in indices:
                    test=np.zeros(n,complex);test[ids[0]]=1
                    partner=t@test.conj();signature=complex(np.vdot(test,rz@test))
                    controls[tag+f'_omega_{omega}_T_conjugates_signature_{ids[0]}']=float(np.linalg.norm(rz@partner-signature.conjugate()*partner))<1e-12
                blocks={'r_plus_i_energies_design':spectra[0].tolist(),'r_minus_i_energies_design':spectra[1].tolist(),
                        'lowest_branch_gap_dimensionless_design':lowest,'spectrum_difference_design':diff}
            data.append({'omega_dimensionless_design':omega,'errors_and_time_change':symmetry,
                         'halfspin_signature_blocks':blocks,
                         'scope':'Intrinsic fixed-j matrix only, not a sequence of nuclear total-spin levels or measured signature splitting.'})
        rows.append({'two_j_representation':two_j,'design_Routhian':'0.3*jz^2+0.07*(jx^2-jy^2)-omega*jz','results':data})
    phase_rows=[]
    for alpha in [.5,-.5,0.,1.]:
        spins=[alpha+2*k for k in range(3,7)]
        r0=np.exp(-1j*math.pi*alpha)
        controls[f'alpha_{alpha}_rotational_projection_step2_same_phase']=all(abs(np.exp(-1j*math.pi*i)-r0)<1e-12 for i in spins)
        controls[f'alpha_{alpha}_step1_opposite_phase']=all(abs(np.exp(-1j*math.pi*(i+1))+r0)<1e-12 for i in spins)
        phase_rows.append({'signature_exponent_alpha':alpha,'r_real_imag':[float(r0.real),float(r0.imag)],
                           'trial_I_values_alpha_plus_even_integers':spins,'source_projection_rule_not_toy_spectrum':True})
    return {'status':'declared-signature-cranking-symmetry-controls','execution_day_index':23,
            'source_premise':'F01 printed474-476 TableII/Eqs51-54, FM97 PAC/planar/aplanar classification',
            'representation_results':rows,'projection_phase_design':phase_rows,'controls':{k:bool(v) for k,v in controls.items()},
            'all_controls_pass':all(controls.values()),
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            'limitations':['The fixed-j Routhian is an arbitrary dimensionless single-particle-like intrinsic algebra example, not a rotationally invariant laboratory nuclear Hamiltonian or an actual band spectrum.',
                           'Routhian time reversal changes omega. Kramers pairing at zero omega does not demand equal signature branches at one nonzero cranking frequency.',
                           'The projection I=alpha+2n is the source band-organization condition, not identification of this fixed-j matrix eigenvalues with different total-I nuclear levels.',
                           'A unitary signature phase is invariant under a global state phase, unlike the antiunitary eigenphase discussed in preview017. No new parity/signature/chiral assignment is measured here.',
                           'Pseudospin is a different approximate intrinsic symmetry; it is not generated or modeled by this pi rotation or C=Ry(pi)T.',
                           'Opposite signature alone does not select ordinarySP/wobbling/TiP/MR or physical configuration. No nuclear energy, g,delta,Q,tau,CI orbeamtime predicted; noDay24credit/Day25.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate();a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'halfspin_lowest_signature_gaps_dimensionless':[{'two_j':v['two_j_representation'],
                          'omega0':v['results'][0]['halfspin_signature_blocks']['lowest_branch_gap_dimensionless_design'],
                          'omega_point2':v['results'][1]['halfspin_signature_blocks']['lowest_branch_gap_dimensionless_design']} for v in r['representation_results'] if v['two_j_representation']%2]},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
