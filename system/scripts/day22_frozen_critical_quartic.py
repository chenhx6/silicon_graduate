#!/usr/bin/env python3
"""Chosen frozen-j critical family: finite-spin gap versus quartic oscillator, not nuclear fit."""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from day22_frozen_alignment_domain import frozen_matrix
ROOT=Path(__file__).resolve().parents[2]

def quartic_levels(n):
 # Pad beforepowers,thenproject: avoidsboundaryalias inq^4/P^2.
 size=n+4;a=np.diag(np.sqrt(np.arange(1,size,dtype=float)),1)
 q=(a+a.T)/math.sqrt(2);p=(a-a.T)/complex(0,math.sqrt(2))
 h=(p@p+q@q@q@q)[:n,:n]
 return np.linalg.eigvalsh(h)[:2]
def calculate():
 levels64=quartic_levels(64);levels96=quartic_levels(96);limit=float(levels96[1]-levels96[0])
 a0=.01;rows=[]
 for spin in [10,20,40,80,160]:
  J=math.sqrt(spin*(spin+1));aligned=J/2;axes=(3*a0,a0,2*a0)
  m,h=frozen_matrix(spin,aligned,axes);vals,vecs=np.linalg.eigh(h)
  gap=float(vals[1]-vals[0]);scale=a0*J**(2/3)
  signature=np.power(-1.0,spin-m)
  parities=[float(np.sum(np.abs(vecs[:,i])**2*signature)) for i in [0,1]]
  rows.append({'I':spin,'J_classical_sqrtI_Iplus1':J,'chosen_j':aligned,'curvature_c1':2*a0,'curvature_c2':0.0,'HFA_frequency_at_critical':0.0,'finite_gap_MeV':gap,'quartic_scale_MeV':scale,'gap_over_quartic_scale':gap/scale,'gap_over_A0J':gap/(a0*J),'two_lowest_signature_eigenvalues':parities})
 errors=[abs(r['gap_over_quartic_scale']-limit) for r in rows]
 controls={
  'quartic_Galerkin64to96_low_gap_converged':abs(float(levels64[1]-levels64[0])-limit)<1e-8,
  'critical_family_HFA_curvature_zero_but_finite_gaps_positive':all(r['curvature_c2']==0 and r['finite_gap_MeV']>0 for r in rows),
  'lowest_pair_have_opposite_signature':all(abs(r['two_lowest_signature_eigenvalues'][0]-1)<1e-10 and abs(r['two_lowest_signature_eigenvalues'][1]+1)<1e-10 for r in rows),
  'scaled_gaps_approach_independent_quartic_limit_on_chosen_grid':all(x>y for x,y in zip(errors,errors[1:])) and errors[-1]<.001,
  'gap_relative_to_A0J_decreases_on_chosen_grid':all(x['gap_over_A0J']>y['gap_over_A0J'] for x,y in zip(rows,rows[1:])),
 }
 return {'scope':'mathematicalchosenfamilyonly;notfullQTR/PTRoractualnuclearcriticalspin','source_formula':'F14Eq11frozenalignedHamiltonian andlocalHFAexpansion;newquarticderivationisourconditionalmodelanalysis','Hamiltonian':'H=3A0J1²+A0J2²+2A0(J3-j)²','units':'hbar=1,A0=.01MeV;Iintegerchosenmodelrepresentations','critical_family':'J=sqrt[I(I+1)],j=J/2,soAbar3=A0;c2=0,c1=2A0','expansion':'J3=J-(J1²+J2²)/(2J)-(J1²+J2²)²/(8J³)+...;classicalquarticcoefficientA3*j/(4J³)','leading_critical_operator':'q=J2/sqrtJ,p=J1/sqrtJ;Hleading=2A0J*p²+(A0/4)*q⁴;leadinggaps scaleA0*J^(2/3)','independent_quartic_oscillator':{'H':'p²+q⁴','Fock_basis64_levels':levels64.tolist(),'Fock_basis96_levels':levels96.tolist(),'gap_limit':limit,'padding':4},'finite_spin_results':rows,'controls':{k:bool(v) for k,v in controls.items()},'boundaries':['jischangedwithIonlytodefineasymptoticmodelsequence;notafixedphysicalquasiparticleorparameterfit.','Classicalnorth-polequarticexpansionhasoperator-orderingsubleadingterms;onlyleadinglimitistested.','Finitepositivegapdoesnotbyitselfidentifyawobblingphonon,nuclearmodestabilityortransitionB.','NoRPAfullquasiparticledegreesofreorientation,experimentalenergies,responseorCIreplayed.','GridmonotonicityisobservedonlyforchosenIvalues,notaproof forall spins orotherHamiltonians.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('outputmustbeinsideoutputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'quartic_gap_limit':d['independent_quartic_oscillator']['gap_limit'],'scaled_gaps':[r['gap_over_quartic_scale'] for r in d['finite_spin_results']]}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
