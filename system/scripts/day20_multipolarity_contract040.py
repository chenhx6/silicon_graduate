#!/usr/bin/env python3
"""Original KO01 selected table plus bounded radiative multipole/branch algebra."""
import argparse,hashlib,json,math
from pathlib import Path


def fraction(d):return d*d/(1+d*d)

def envelope(d,e):
 lo,hi=sorted([d-e,d+e]);amin=0 if lo<=0<=hi else min(abs(lo),abs(hi));amax=max(abs(lo),abs(hi));fmin,fmax=fraction(amin),fraction(amax)
 return {'printed_delta_endpoints':[lo,hi],'photon_higher_multipole_fraction_endpoints':[fmin,fmax],'pure_higher_multipole_B_factor_endpoints':[1/fmax if fmax else None,1/fmin if fmin else None],'unbounded_upper_if_delta_interval_contains_zero':fmin==0,'scope':'Rectangular input-endpoint transform, not experimentalCI or likelihood.'}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);a=p.parse_args();checks=[]
 def check(name,ok):
  if not ok:raise AssertionError(name)
  checks.append(name)
 entries=[['2_3+','2_1+',1557.,1199.8,-.30,.02,'E2/M1'],['4_3+','4_1+',1844.,942.5,.15,.09,'E2/M1'],['3_1+','2_1+',1360.5,1003.3,-4.5,.4,'E2/M1'],['3_1-','4_1+',1918.3,1016.7,.06,.05,'M2/E1'],['3_1-','2_1+',1918.3,1561.2,.03,.08,'M2/E1']]
 fields=['parent','daughter','parent_energy_keV','Egamma_keV','delta_Rose_Brink','delta_printed_error','lowest_multipole_pair'];ledger=[]
 for row in entries:
  r=dict(zip(fields,row));r['photon_higher_multipole_fraction']=fraction(r['delta_Rose_Brink']);r['photon_lower_multipole_fraction']=1-r['photon_higher_multipole_fraction'];r['conditional_B_overestimate_if_line_treated_pure_higher_multipole']=1/r['photon_higher_multipole_fraction'];r['input_endpoint_transform']=envelope(r['delta_Rose_Brink'],r['delta_printed_error']);ledger.append(r)
 check('central quoted M1 contents reproduced at correct energy/state',math.isclose(100*ledger[0]['photon_lower_multipole_fraction'],91.74311926605505) and math.isclose(100*ledger[1]['photon_lower_multipole_fraction'],97.799511002445))
 check('printed small delta error propagates asymmetrically and broadens reciprocal correction',ledger[1]['input_endpoint_transform']['pure_higher_multipole_B_factor_endpoints'][1]>270)
 check('delta interval crossing0 yields unbounded reciprocal not finiteGaussianerror',ledger[-1]['input_endpoint_transform']['unbounded_upper_if_delta_interval_contains_zero'])
 # Chosen mixed-line IC algebra. These are arbitrary inputs, not KO01 coefficients.
 d=.3;alpha_m1=.20;alpha_e2=.05;f=fraction(d);alpha_mix=(alpha_m1+d*d*alpha_e2)/(1+d*d)
 check('mixed IC is radiative fraction weighted',math.isclose(alpha_mix,(1-f)*alpha_m1+f*alpha_e2))
 # Complete two-line photon-normalized ledger, no additional decay channel assumed.
 r=[.7,.3];alphas=[alpha_mix,.4];den=sum(v*(1+c) for v,c in zip(r,alphas));photons=[v/den for v in r]
 check('normalized photon branches require complete mixedIC denominator',math.isclose(sum(p*(1+c) for p,c in zip(photons,alphas)),1) and sum(photons)<1)
 # A known full radiative line rate permits upper E2 bounds even without measureddelta.
 chosen_tgamma=2.;allowed=[chosen_tgamma*fraction(v) for v in [0,.15,.3,1,10]]
 check('without delta one can bound rather than uniquely extract E2partialrate',all(0<=v<=chosen_tgamma for v in allowed))
 out={'checkpoint':'040','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
 'KO01_TableI_selected_literal':ledger,'KO01_unresolved_case':{'parent':'4_3+','daughter':'3_1+','Egamma_keV':483.5,'delta_literal':'E2/M1; no unique numericdelta','branch_literal':'92*','B_E2_ratio_literal':'<130*','scope':'Asterisk denotes contamination estimate without error; no Gaussian numeric treatment.'},
 'KO01_source_scope':'All3pages text and Figs1–3/TableI visually reread; selected5numeric rows typed, not claim of all40 derived columns reconstructed. Two opening-angle ratios with shared denominator and referenceE2/gates; actualresponse/Cov absent.',
 'multipole_contract':'delta gives ratio of radiative multipole amplitudes in source sign convention. delta²/(1+delta²) is higher multipole fraction within this photon line, not total levelE2branch. Same parity lowest allowedM1/E2 vs opposite parity E1/M2 kept distinct; no universalDeltaI0/1 rule.',
 'chosen_IC_control':{'chosen_delta':d,'chosen_alpha_M1':alpha_m1,'chosen_alpha_E2':alpha_e2,'mixed_alpha':alpha_mix,'chosen_photon_normalized_intensities':r,'chosen_second_line_alpha':alphas[1],'p_gamma_per_parent':photons,'scope':'Declared mathematical example only. No source ICC/actual branch denominator inferred.'},
 'without_delta_boundary':'Given known whole-photon-line rate and M1/E2-only model, E2partialgamma rate is between0andthat rate; absoluteB requires lifetime/branch/rate and covariance contract. Delta measurement or bound/justifiedpure assumption constrains it, not always all-or-nothing impossible.',
 'structure_boundary':'StrongM1 supports author mixed-symmetry interpretation but absoluteM1 needed for unambiguous assignment. Photon fraction alone does not prove TiP/wobbling/chirality or strengthcollectivity.',
 'controls':checks,'certification_scope':'Literal table and declared radiative algebra only; no original experimentalCI/response or general modeclassifier.'}
 path=a.run_dir/'multipolarity-contract-result-040.json';path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'artifact':str(path),'controls':len(checks),'first2':[{'energy':v['Egamma_keV'],'M1percent':100*v['photon_lower_multipole_fraction'],'Bfactor':v['conditional_B_overestimate_if_line_treated_pure_higher_multipole'],'endpoint':v['input_endpoint_transform']} for v in ledger[:2]]}))
if __name__=='__main__':main()
