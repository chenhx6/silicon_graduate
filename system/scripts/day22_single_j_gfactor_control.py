#!/usr/bin/env python3
"""Chosen single-j+rotor staticg identities; no actual isotopeg prediction or inversion."""
import argparse,json,math
from fractions import Fraction as F
from pathlib import Path
from day14_unobserved_feeding_transfer import cg_squared
ROOT=Path(__file__).resolve().parents[2]

def coupled_g(R,j,I,gj,gR):
 total=F(0);mu=F(0)
 for tmj in range(-int(2*j),int(2*j)+1,2):
  tmr=int(2*I)-tmj
  if abs(tmr)>2*R:continue
  weight=cg_squared(2*R,int(2*j),int(2*I),tmr,tmj,int(2*I))
  total+=weight;mu+=weight*(gR*F(tmr,2)+gj*F(tmj,2))
 return total,mu/I

def calculate():
 j=I=F(11,2);gR=F(2,5);RR=[0,2,4];rows=[]
 for gj in [F(6,5),F(-2,5),gR]:
  for R in RR:
   norm,g=coupled_g(R,j,I,gj,gR)
   dot=(I*(I+1)+j*(j+1)-R*(R+1))/2
   formula=gR+(gj-gR)*dot/(I*(I+1))
   inverse=None if gj==gR else I*(I+1)+j*(j+1)-2*I*(I+1)*(g-gR)/(gj-gR)
   rows.append({'R':R,'j':str(j),'I':str(I),'gj':str(gj),'gR':str(gR),'sumCGsquared':str(norm),'g_from_CG_squared':str(g),'g_from_scalar_identity':str(formula),'R_Rplus1_from_inverse':None if inverse is None else str(inverse)})
 # Distinct positiveRdistributions sameR²mean andstaticg.
 pa=[F(1,2),F(1,2),F(0)];pb=[F(17,20),F(0),F(3,20)];gj=F(6,5)
 gs=[coupled_g(R,j,I,gj,gR)[1] for R in RR]
 def mixed(p):return sum(w*g for w,g in zip(p,gs)),sum(w*R*(R+1) for w,R in zip(p,RR))
 ga,Ra=mixed(pa);gb,Rb=mixed(pb)
 controls={
  'all_exact_CG_probabilities_normalized':all(x['sumCGsquared']=='1' for x in rows),
  'CG_magnetic_expectation_equals_scalar_identity_exactly':all(x['g_from_CG_squared']==x['g_from_scalar_identity'] for x in rows),
  'inverse_recovers_exact_R_Rplus1_when_gcontrast_nonzero':all(x['R_Rplus1_from_inverse']==str(x['R']*(x['R']+1)) for x in rows if x['gj']!=x['gR']),
  'equal_gj_gR_gives_no_R_inversion':all(x['R_Rplus1_from_inverse'] is None and x['g_from_CG_squared']==x['gR'] for x in rows if x['gj']==x['gR']),
  'different_R_distributions_same_g_and_mean_Rsquared':ga==gb and Ra==Rb and pa!=pb and sum(pa)==sum(pb)==1 and min(pa+pb)>=0,
 }
 return {'scope':'taskdefinedsingle-j+coremagneticoperatorcontrol,notF14newdata','operator':'mu/muN=gR*R+gj*j=gR*I+(gj−gR)*j;hbar=1','identity':'gI=gR+(gj−gR)<I dotj>/[I(I+1)]','inverse':'<R²>=I(I+1)+j(j+1)−2I(I+1)(gI−gR)/(gj−gR),ifgj!=gR','rows':rows,'mixture_witness':{'R_basis':RR,'weights_a':[str(x) for x in pa],'weights_b':[str(x) for x in pb],'same_g':str(ga),'mean_Rsquared':str(Ra),'R_effective_moment_proxy':(math.sqrt(1+4*float(Ra))-1)/2},'controls':controls,'boundaries':['I=j=11/2andgvaluesarechosenrationalmodelinputs,notmeasurednuclearvalues.','AscalarmeanR²doesnotidentifyitsdistributionorbody-frameangularmomentumgeometry.','One-jspaceandgR/gjmustbejustified;orbitalmixing/corepolarizationoreffectiveoperatorsmayinvalidatethisinversion.','DynamicalinterbandM1quenchingcalibrationisnotautomaticallyastatic-goperatorcalibration.','NoTW/LW/chiralitymodeoractualfield/lifetime/CIinferred.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('outputmustbeinsideoutputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'mixture_witness':d['mixture_witness']}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
