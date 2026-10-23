#!/usr/bin/env python3
"""Declared aligned-j K mixing and literal Petrache Table I audit, no experimental fit/CI."""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy.linalg import expm
from day19_evidence_repair_audit import signed_cg, rotor_cg_squared


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);args=p.parse_args()
    controls=[]
    def check(name,value):
        if not value: raise AssertionError(name)
        controls.append(name)
    j=F(11,2);ks=[j-n for n in range(12)]
    amplitudes=np.array([(-1)**int(j-k)*math.sqrt(math.comb(11,int(j+k)))/2**float(j) for k in ks])
    jp=np.zeros((12,12),complex)
    for col in range(1,12):
        k=float(ks[col]);jp[col-1,col]=math.sqrt((float(j)-k)*(float(j)+k+1))
    jy=(jp-jp.T.conj())/(2j)
    rotation=expm(-1j*math.pi/2*jy)
    check('binomial phases and amplitudes match independent ladder-operator matrix exponential',np.allclose(rotation[0],amplitudes,rtol=1e-13,atol=1e-14))
    check('rotation unitary',np.allclose(rotation.conj().T@rotation,np.eye(12)))
    check('amplitude probabilities normalized',abs(sum(amplitudes**2)-1)<1e-14)
    curves=[]
    for two_i in [15,19,23,27,31,35]:
        i=F(two_i,2);pure=signed_cg(i,2,i-2,F(1,2),0,F(1,2));mix=0.
        for k,a in zip(ks,amplitudes):
            if abs(k)>i-2: continue
            c=signed_cg(i,2,i-2,k,0,k)
            check(f'signed factorial CG square vs rotor formula I={i},K={k}',math.isclose(c*c,float(rotor_cg_squared(i,k)),abs_tol=1e-14))
            mix+=a*a*c
        curves.append({'I':str(i),'CG_pure_half':pure,'CG_mixed_same_initial_final_a':mix,'CG_relative_change':mix/pure-1,'Qt_multiplier_fixed_rate':abs(pure/mix)})
    ledger=json.loads((args.run_dir/'singh-table-ledger-001.json').read_text())
    impact=[]
    for case in ['case_Ce131','case_Pr133']:
        for row in ledger[case]['rows']:
            if row['Qt']['kind']!='finite':continue
            spin=str(F(str(row['spin']))) if 'spin' in row else None
            # Literal ledger spin upper uses I field (see frozen ledger).
            if spin is None:spin=str(F(str(row['I'])))
            c=next(v for v in curves if v['I']==spin);q=row['Qt'];delta=q['value']*(c['Qt_multiplier_fixed_rate']-1)
            impact.append({'case':case,'I':spin,'printed_Qt_eb':q['value'],'printed_minus_eb':q['minus'],'printed_plus_eb':q['plus'],'conditional_upward_shift_eb':delta,'shift_below_both_printed_error_sides':bool(delta<min(q['minus'],q['plus']))})
    check('all Ce finite points smaller than both printed error sides under declared limit',all(r['shift_below_both_printed_error_sides'] for r in impact if r['case']=='case_Ce131'))
    check('Pr lowest spin disproves universal below-error extension',not next(r for r in impact if r['case']=='case_Pr133' and r['I']=='15/2')['shift_below_both_printed_error_sides'])
    # Preserve eight literal rows, fit dependence and absent/approximate entries.
    table=[
      ['134Nd yrast HD','6.8(3)','6(1)','0.35(1)',[7.4,19,5.9,39],'constant-Q fit'],
      ['134Nd excited HD','6.4(4)','6(1)','0.33(2)',[6.9,18,6.4,40],'whole-band fit, one intruder below/two above backbend'],
      ['134Nd band3 lower','4.9(3)','2.5(5)','0.26(2)',[4.8,18,6.1,26],'segmented fit conditioned on approximate upper Q'],
      ['134Nd band3 upper','~6.5','~6','~0.34',[6.07,32,6.07,40],'four insensitive top points; body error order20–30%; theory footnote estimate'],
      ['134Nd band3 lower+upper','5.0(3)','4(1)','0.26(2)',None,'same data alternative unique-Q fit, not independent experiment'],
      ['135Nd HD','7.3(10)','3.0(5)','0.37(5)',[6.4,24.5,5.5,38.5],'body R13 instead prints Qsf4.0(5); unresolved literal discrepancy'],
      ['131Ce yrast HD','7.3(4)','6(1)','0.38(2)',[7.5,20.5,6.7,40.5],'constant-Q fit'],
      ['132Ce yrast HD','7.4(3)',None,'0.38(2)',[8.0,24,6.6,52],'external Ref6, not new experiment here']]
    rows=[dict(zip(['band','Q0exp_literal_eb','Qsf_literal_eb','beta_literal','theory_Q_I_endpoints','role'],r)) for r in table]
    for r in rows:
        t=r['theory_Q_I_endpoints']
        if t:r['calculated_endpoint_relative_change']=(t[2]-t[0])/t[0]
    check('literal TableI eight rows retained',len(rows)==8)
    check('excited HD theory decline is only7.25percent',math.isclose(rows[1]['calculated_endpoint_relative_change'],-.5/6.9))
    out={'checkpoint':'034','experimental_fit_or_CI':False,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'K_mixing_contract':'Single rotation-aligned j11/2, identical real aK at initial/final spins, axial quadrupole operator diagonal in K, fixed observed E2 rate. No actual K/producer inference.',
         'phase_matrix_max_difference':float(np.max(abs(rotation[0]-amplitudes))),
         'K_amplitudes':[{'K':str(k),'a':float(a)} for k,a in zip(ks,amplitudes)],'CG_and_Qt_scaling':curves,'literal_Qt_conditional_shift':impact,
         'author_scope':'Singh PDF6 first paragraph justifies Eq1 K1/2 for Table1 in Ce discussion; no blanket experimental Pr precision certification.',
         'Petrache_TableI_literal':rows,
         'Petrache_boundaries':['Q0exp is band-fit parameter, not levelwise lifetime.', 'No firm distinction of single vs segmented band3 fit; cannot certify jump.', 'R13: predicted shrinking could not be determined experimentally; calculated Q curves generally reproduce fractional Doppler shifts.', 'Shrinking versus polarization and weakened additivity are author cranked-Strutinsky interpretation, not controlled occupancy derivative or universal saturation.', 'No original F(tau), likelihood, covariance or producer; no AIC, CI, universal15percent sensitivity or A150 strict law.'],
         'controls':controls,'certification_scope':'Declared matrix/CG algebra and literal ledger only; controls are not original experimental validation.'}
    target=args.run_dir/'kmix-shrinkage-result-034.json';target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'artifact':str(target),'control_count':len(controls),'impacts':impact},ensure_ascii=False))

if __name__=='__main__':main()
