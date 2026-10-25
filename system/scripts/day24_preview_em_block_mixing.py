#!/usr/bin/env python3
"""Fixed-projector RME invariants and actual export missing-cell readiness.

Abstract matrices, phases and frequencies are designs only. Nothing here
fits a nuclear mixing angle or supplies unobserved transition strengths.
"""
import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day24_preview_nd135_export_identity import read_csv


def rotation(angle,phase=0.):
    c,s=math.cos(angle),math.sin(angle)
    return np.array([[c,-s*np.exp(-1j*phase)],[s*np.exp(1j*phase),c]])


def loop(r):
    return r[0,0]*r[1,1]*r[0,1].conjugate()*r[1,0].conjugate()


def invariant(r):
    return {'Frobenius_squared':float(np.linalg.norm(r)**2),
            'singular_values':np.linalg.svd(r,compute_uv=False).tolist(),
            'absolute_determinant_squared':float(abs(np.linalg.det(r))**2),
            'loop_product_real_imag':[float(loop(r).real),float(loop(r).imag)]}


def calculate(gammas_path,levels_path):
    controls={};r=np.array([[1.,2.],[3.,4.]],complex);other=r.copy();other[1,1]*=-1
    ui,uf=rotation(.31),rotation(-.47,.23)
    transformed=uf.T.conj()@r@ui
    controls['chosen_unitaries_are_unitary']=max(float(np.max(abs(u.T.conj()@u-np.eye(2)))) for u in [ui,uf])<1e-13
    controls['closed_projector_Frobenius_invariant']=abs(np.linalg.norm(transformed)**2-np.linalg.norm(r)**2)<1e-12
    controls['closed_projector_singular_values_invariant']=bool(np.allclose(np.linalg.svd(transformed,compute_uv=False),np.linalg.svd(r,compute_uv=False),atol=1e-13))
    controls['labelled_entry_strengths_can_redistribute']=float(np.max(abs(abs(transformed)**2-abs(r)**2)))>1
    hi,hf=np.diag([0.,1.]),np.diag([.2,1.7])
    hi_basis,hf_basis=ui.T.conj()@hi@ui,uf.T.conj()@hf@uf
    eigen_amplitude_error=0.
    for ai in [0,1]:
        for af in [0,1]:
            vi=ui.T.conj()[:,ai];vf=uf.T.conj()[:,af]
            eigen_amplitude_error=max(eigen_amplitude_error,abs(np.vdot(vf,transformed@vi)-r[af,ai]))
    controls['consistent_basis_change_preserves_physical_eigenstate_matrix_elements']=eigen_amplitude_error<1e-13
    controls['arbitrary_mixing_not_nondegenerate_fixedH_relabel']=float(np.max(abs(ui@hi-hi@ui)))>.1
    hnew=ui@hi@ui.T.conj()
    controls['physical_isospectral_mixing_changesH']=float(np.max(abs(hnew-hi)))>.1 and bool(np.allclose(np.linalg.eigvalsh(hnew),np.diag(hi)))
    controls['changedH_fixedoperator_can_change_eigenstate_matrix_entries']=float(np.max(abs(transformed-r)))>.1
    # Exact real-sign example: every entry strength is unchanged; the loop
    # sign and determinant modulus are different, hence no left/right unitary
    # equivalence exists between these two complete RME blocks.
    rp=[[1,2],[3,4]];rm=[[1,2],[3,-4]]
    exact_sum=lambda a:sum(Fraction(x)**2 for row in a for x in row)
    exact_det=lambda a:Fraction(a[0][0]*a[1][1]-a[0][1]*a[1][0])
    controls['exact_all_four_entry_intensities_equal']=all(a*a==b*b for ra,rb in zip(rp,rm) for a,b in zip(ra,rb))
    controls['exact_same_sum_not_same_determinant']=exact_sum(rp)==exact_sum(rm)==30 and exact_det(rp)**2==4 and exact_det(rm)**2==100
    controls['same_B_moduli_need_not_fix_complete_block_singular_values']=not bool(np.allclose(np.linalg.svd(r,compute_uv=False),np.linalg.svd(other,compute_uv=False)))
    phase_i=np.diag(np.exp(1j*np.array([.11,-.37])));phase_f=np.diag(np.exp(1j*np.array([-.21,.43])))
    gauge=phase_f.T.conj()@r@phase_i
    controls['closed_loop_phase_is_invariant_under_state_rephasings']=abs(loop(gauge)-loop(r))<1e-12
    # The sum rule is lost if the physically participating subspace extends
    # outside the selected two-state projectors.
    large=np.zeros((3,3));large[:2,:2]=r.real;large[2,0]=5
    u3=np.eye(3);c,s=math.cos(.41),math.sin(.41);u3[np.ix_([0,2],[0,2])]=[[c,-s],[s,c]]
    newlarge=large@u3
    controls['full_three_state_Frobenius_is_invariant']=abs(np.linalg.norm(newlarge)**2-np.linalg.norm(large)**2)<1e-12
    controls['selected_pair_not_invariant_when_projector_leaks']=abs(np.linalg.norm(newlarge[:2,:2])**2-np.linalg.norm(large[:2,:2])**2)>.1
    # A gamma-width sum weights entries by distinct photon energies; it is
    # not the unweighted trace invariant. These are dimensionless weights.
    weights=np.array([[1.,2.],[3.,4.]])
    controls['energy_weighted_width_sum_not_the_unweighted_B_sum']=abs(float(np.sum(weights*abs(transformed)**2))-float(np.sum(weights*abs(r)**2)))>1e-3
    _,gr,_=read_csv(gammas_path);_,lr,_=read_csv(levels_path)
    levels={v['fields']['idx']:v['fields'] for v in lr}
    edges={(v['fields']['start_level_idx'],v['fields']['end_level_idx']) for v in gr}
    missing=[]
    for two_i,aid,bid in [(31,'55','56'),(33,'60','59'),(35,'63','61'),(37,'68','66')]:
        aa,bb=levels[aid],levels[bid];de=float(aa['energy'])-float(bb['energy'])
        observed=(aid,bid) in edges or (bid,aid) in edges
        missing.append({'candidate_two_I_initial':two_i,'A_initial_idx':aid,'B_final_idx':bid,
                        'A_energy_keV_string':aa['energy'],'B_energy_keV_string':bb['energy'],
                        'A_jp':aa['jp'],'B_jp':bb['jp'],'central_A_to_B_deltaE_keV':de,
                        'forward_or_reverse_row_present_in_snapshot':observed,
                        'B_final_level_half_life_string':bb['half_life'],'B_final_level_clock_unit':bb['unit_hl'],
                        'matrix_element_or_B_assigned':None,
                        'boundary':'No snapshot row is not an experimental absence/upperlimit/zeroB. A negative central decay energy does not zero the reverse/absorption matrix element; near1.4keV lacks energy covariance/IC/measurement readiness.'})
    controls['all_four_candidate_missing_cells_not_silently_filled']=all(not v['forward_or_reverse_row_present_in_snapshot'] and v['matrix_element_or_B_assigned'] is None for v in missing)
    controls['first_candidate_upward_not_set_zeroB']=missing[0]['central_A_to_B_deltaE_keV']<0 and missing[0]['B_final_level_half_life_string']==''
    return {'status':'closed-block-mixing-and-readiness-design','formal_day_index':23,'uncredited_preview_day':24,
            'scope':'Abstract fixed-projector/operator RME identities and official135Nd missing-cell inventory; no nuclear mixing fit or physical loop-phase observation.',
            'design_base_RME':r.real.tolist(),'design_transformed_entry_strengths':(abs(transformed)**2).tolist(),
            'invariants_base':invariant(r),'invariants_after_unitary_basis':invariant(transformed),
            'equal_intensity_different_loop_case':{'plus_R':rp,'minus_R':rm,'plus_invariants':invariant(r),'minus_invariants':invariant(other)},
            'basis_change_eigen_amplitude_error':float(eigen_amplitude_error),
            'declared_higher_space_leakage':{'full_Frob2':float(np.linalg.norm(large)**2),
                'selected_pair_before':float(np.linalg.norm(large[:2,:2])**2),'selected_pair_after':float(np.linalg.norm(newlarge[:2,:2])**2)},
            'chosen_dimensionless_weighted_sum':{'weights':weights.tolist(),
                'before':float(np.sum(weights*abs(r)**2)),'after':float(np.sum(weights*abs(transformed)**2)),
                'scope':'Arbitrary positive entry weights illustrate a non-invariant weighted functional, not actual photon energies/rates or a fitted nuclear effect.'},
            'actual_snapshot_missing_cells':missing,'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'input_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [gammas_path,levels_path]},
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('day24_preview_nd135_export_identity.py')]},
            'limitations':['Unitary mixing inside a fixed closed projector preserves Frobenius/singular values. A pure coordinate change also transforms H and eigenstate coordinates; labelled entry redistribution alone is not a changed experiment.',
                           'At fixed nondegenerateH, arbitrary multiplicity mixing does not preserve the energy eigenbasis. Physical isospectral mixing at fixed operator still changes H and is not configuration-only relabelling.',
                           'Four measured strength moduli can determine the unweighted block sum if complete, but not necessarily determinant/singular values without a relative loop phase. No measured nuclear phase is supplied here.',
                           'Unobserved/off-window/upward matrix elements, incomplete pair projectors or additional configurations block the closed-pair invariant test. Absence of an API row is not zero intensity or B.',
                           'A sum of B at one initial spin is not a photon-width or total-decay sum across entries with different energies/parents. No actual branching completeness is certified.',
                           'Dimensionless RME/sign/unitary designs are not actual nuclear one-body EM operators, mixing angles, partner assignments or new g/delta/Q/tau/CI/countingrate/beamtime.',
                           'Real135Nd dataset/model support and all previous quantity/normalization boundaries remain. Only the already openedDay24 uncredited preview, noDay25/formalcredit.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--gammas',type=Path,required=True);p.add_argument('--levels',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate(a.gammas,a.levels);a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'base_invariants':r['invariants_base'],'signflip_invariants':r['equal_intensity_different_loop_case']['minus_invariants'],
                      'missing_candidate_deltaE_keV':[v['central_A_to_B_deltaE_keV'] for v in r['actual_snapshot_missing_cells']]},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
