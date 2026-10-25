#!/usr/bin/env python3
"""Domscheit1999 printed central two-state mixing control; no new lifetime measurement."""
import argparse,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/'raw/papers/1999_Domscheit et al_Triaxial superdeformation in 163Lu.pdf'
SHA='edde41a90870cba7451da6d93579017eeb046d060513aa69b24661ba5a72b7c8'
def calculate():
 if hashlib.sha256(RAW.read_bytes()).hexdigest()!=SHA:raise ValueError('raw identity mismatch')
 ratio1=12.5/68.1*(314.9/426.5)**5
 p=ratio1/(1+ratio1)
 ratio2=23.3/18.7*(263.1/697.1)**5
 q=math.sqrt(ratio2/ratio1)
 gap=2198-2087;V=gap*math.sqrt(p*(1-p));detuning=gap*(1-2*p);shift=gap*p
 # Direct real symmetric2x2 eigensystem invariants; arbitrary energy origin.
 h={'E_SD_bare':gap*(1-p),'E_ND_bare':gap*p,'V':V}
 center=(h['E_SD_bare']+h['E_ND_bare'])/2
 disc=math.sqrt(((h['E_SD_bare']-h['E_ND_bare'])/2)**2+V*V)
 eigen=[center-disc,center+disc]
 controls={
  'mixing_probability_matches_printed_point04_to_print_precision':abs(p-.04)<.005,
  'coupling_matches_source22plusminus3_interval_no_newCI':19<V<25,
  'quadrupole_ratio_matches_printed_point48plusminus07_interval':.41<q<.55,
  'two_state_eigenvalue_gap_reconstructed':abs((eigen[1]-eigen[0])-gap)<1e-12,
  'unperturbed_detuning_plus_repulsions_restores_observed_gap':abs(detuning+2*shift-gap)<1e-12,
 }
 return {'raw_sha256':SHA,'locator':'printed385Table1;387Eq1;388Eq2;391Ref2','input_roles':{'mixed_states_keV':[2087,2198],'state_spin_parity':'both21/2+ SD1 andND411; notSD1/SD2','same_parent25half_photon_intensity_out_in':[12.5,68.1],'same_parent21half_photon_intensity_out_in':[23.3,18.7]},'central_results':{'rE2_426over315':ratio1,'mixing_probability':p,'rE2_697over263':ratio2,'Q_ND_over_Q_SD':q,'V_keV':V,'bare_detuning_keV':detuning,'level_repulsion_shift_each_keV':shift,'two_state_eigenvalues_relative_keV':eigen},'controls':controls,'boundaries':['The paper interprets two-state mixing and assumes its branch/operator model; no alternative mechanism is newly fitted.','Source22(3)keV and.48(.07)intervals are comparison intervals only; no new uncertainty/covariance propagated.','QuotedQ_ND6.0(.5)b andQ_SD10.7(.7)b originate fromSchmitz1993Ref2; this is not a new lifetime experiment orQ_SD2.','DO99Table1 notes697.1keV unresolved from a similarSD line; printed intensity reconstruction does not certify decontamination.',
 'Output has no absoluteB(M1),B(E2),gamma rigidity measurement or universal wobbling criterion.','Central shift4.30keV vs authorsabout5keV is rounding/model-description compatibility, not an independent energy measurement.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('output must be inside outputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'central_results':d['central_results']}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
