#!/usr/bin/env python3
"""Yamazaki printed-table conditional counterexample, not a fit to 135Pr data."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import sqrt
from pathlib import Path
from day14_unobserved_feeding_transfer import tensor
ROOT=Path(__file__).resolve().parents[2]
RAW=ROOT/'raw/papers/gpt/high-spin-20260920/multipolarity/angular distribution/ADO/1967_Yamazaki_Tables of coefficients for angular distribution of gamma rays from aligned.pdf'
SHA='e807782c580a0313ee3763f56df1dd424e5c97925d70e3d30a79a8b534c81f70'

def calculate():
 if hashlib.sha256(RAW.read_bytes()).hexdigest()!=SHA: raise ValueError('raw identity mismatch')
 # Five-place table values, not newly calculated exact Racah coefficients.
 f11,f12,f22,f4=map(F,['.26430','-.90951','.06955','.49211'])
 def g(d):return (f11+2*d*f12+d*d*f22)/(1+d*d)
 def fe(d):return d*d/(1+d*d)
 large=F(-7,5); y=g(large)
 small=(f11-y)/((f22-y)*large)
 rho2,rho4=F(-1,50),F(1,50)
 rho4_alt=rho4*fe(large)/fe(small)
 weights={}
 for k in [2,4]:
  v,c=tensor(17,k);weights[k]=[float(x)*sqrt(float(c)) for x in v]
 def population(p2,p4):
  return [(1+float(p2)*weights[2][i]+float(p4)*weights[4][i])/18 for i in range(18)]
 p=population(rho2,rho4); q=population(rho2,rho4_alt)
 def coeff(d,p4):return float(rho2*g(d)),float(p4*f4*fe(d))
 a=coeff(large,rho4);b=coeff(small,rho4);c=coeff(small,rho4_alt)
 # Polynomial equality gives equality of W(theta) for all theta; samples only control transcription.
 def w(x,coef):return 1+coef[0]*(3*x*x-1)/2+coef[1]*(35*x**4-30*x*x+3)/8
 max_dw=max(abs(w(i/100,a)-w(i/100,c)) for i in range(-100,101))
 x=fe(large);inverted=sqrt(float(x/(1-x)))
 controls={
  'exact_same_A2_in_printed_coefficient_model':g(large)==g(small),
  'fixed_alignment_A4_breaks_two_magnitudes':a[1]!=b[1],
  'both_constructed_populations_positive_normalized':min(p+q)>0 and abs(sum(p)-1)<1e-13 and abs(sum(q)-1)<1e-13,
  'moments_match_constructed_rho':all(abs(sum(pop[i]*weights[k][i] for i in range(18))-float(target))<1e-13 for pop,targets in [(p,{2:rho2,4:rho4}),(q,{2:rho2,4:rho4_alt})] for k,target in targets.items()),
  'different_populations_same_full_angular_polynomial':a==c and max_dw<1e-13,
  'known_nonzero_C4_recovers_delta_magnitude':abs(inverted-abs(float(large)))<1e-14,
 }
 return {'raw_sha256':SHA,'locator':'printed p1 Eq1; p2 Eqs3/4; p19 TableIIb Ji17/2 Jf15/2 rows11,12,22',
 'inputs':{'printed_F2_11_12_22':[float(z) for z in [f11,f12,f22]],'printed_F4_22':float(f4),'chosen_rho2_rho4':[float(rho2),float(rho4)],'population_basis':'Yamazaki t_k(m), using exact day14 tensor helper'},
 'results':{'chosen_delta_large':float(large),'derived_other_A2_root':float(small),'root_rational_in_printed_model':str(small),'A2_A4_first':a,'A2_A4_same_rho_other_root':b,'A2_A4_other_rho_other_root':c,'other_rho4':float(rho4_alt),'min_probability_first':min(p),'min_probability_second':min(q),'population_first':p,'population_second':q,'max_W_difference_201_sample_control':max_dw},'controls':controls,
 'boundaries':['Chosen rho and mixing ratios are a mathematical witness, not measured 135Pr alignment or a fit to SH26/Lv/Matta.',
 'The two-root equality is exact only for the five-place printed coefficient model; table rounding is not an experimental CI.',
 'Nonnegative symmetric distributions need not be Gaussian; this does not show a degeneracy within a fixed Gaussian family.',
 'Single-photon axial angular distribution only; no polarization, directional gate, detector convolution, confidence level or experimental significance inferred.',
 'No universal required A4 or Q sensitivity precision follows from this witness.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('output must be inside outputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'results':{k:v for k,v in d['results'].items() if not k.startswith('population')}}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
