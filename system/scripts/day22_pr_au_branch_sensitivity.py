#!/usr/bin/env python3
"""Printed-input branch sensitivity; never a shared-data fit or absolute lifetime result."""
import argparse
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SOURCES = {
 'guo2022': ('2022_Guo et al_Probing the nature of the conjectured low-spin wobbling bands in atomic nuclei3.pdf', 'de541977e4c8402c905ef8268ebc5707303f4b92f244eb4f59405a70c3473206'),
 'sensharma2020': ('2020_Sensharma et al_Longitudinal Wobbling Motion in Au 187.pdf', 'f348dce9976ad076fd9b1d5281a728e0923053aced33b0270f643d770729366a'),
 'lv2022': ('2022_Lv et al_Evidence against the wobbling nature of low-spin bands in 135Pr.pdf', '4b87c540bf9da5141fa88ef8f00859162cb08918d56a5da74726c7537df5e26b'),
}
def fraction(d):
 return d*d/(1+d*d)
def calculate():
 hashes={}
 for key,(name,expected) in SOURCES.items():
  digest=hashlib.sha256((ROOT/'raw/papers'/name).read_bytes()).hexdigest()
  if digest!=expected: raise ValueError(f'raw identity mismatch: {key}')
  hashes[key]=digest
 rows=[]
 for energy,old,new,lo,hi in [(376,-2.67,-.26,-.41,-.10),(462,-2.98,-.28,-.97,-.05)]:
  rows.append({'energy_keV':energy,'sensharma_delta_center':old,'guo_delta_center':new,
   'guo_delta_printed_interval':[lo,hi], 'guo_e2_fraction_center':fraction(new),
   'guo_e2_fraction_mapped_interval':[fraction(hi),fraction(lo)],
   'e2_fraction_ratio_old_over_new':fraction(old)/fraction(new),
   'ratio_scope':'conditional same photon branching, energies and normalizer; different experiments are not jointly refitted'})
 # Same parent 2203.9 keV, 21/2-, SI Table1; in-band line is assigned pure E2.
 ratio=6.4/3.7; eout=.8132; ein=.726; delta=-.37
 re2=ratio*(ein/eout)**5*fraction(delta)
 rm1=(.835*eout)**2*re2/delta**2
 controls={
  'printed_guo_376_interval_stays_below_half_E2':max(rows[0]['guo_e2_fraction_mapped_interval'])<.5,
  'printed_guo_462_interval_stays_below_half_E2':max(rows[1]['guo_e2_fraction_mapped_interval'])<.5,
  '813_reconstruction_inside_printed_marginal_error_bands':abs(re2-.12)<.08 and abs(rm1-.4)<.3,
  'wrong_P_as_delta_reproduces_spurious_88_sensitivity':87< fraction(-2.67)/fraction(-.10)<89,
 }
 return {'raw_sha256':hashes,'au187':rows,'pr135_813_same_parent':{
  'locator':'Lv main p3 Table1, p5 Fig4(d); SI p5 Table1',
  'photon_intensities_out_in':[6.4,3.7],'Eout_Ein_MeV':[eout,ein],
  'delta':delta,'rE2':re2,'rM1_muN2_per_e2b2':rm1,
  'printed_rE2_error':[.12,.08],'printed_rM1_error':[.4,.3]},
  'controls':controls,'boundaries':[
  'No absolute B, lifetime, Weisskopf-unit or physical strength collapse is inferred.',
  'Mapped delta intervals retain the source graphical construction; no confidence level or joint covariance invented.',
  'Marginal interval agreement is a coarse arithmetic check, not a reproduction of source error analysis.',
  'For Au, conversion measurements are historical comparisons; external detector sensitivity is shared input lineage.',
  'The last control diagnoses the earlier P/delta identity error; it is not a physical alternative delta.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args()
 out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('output must be inside outputs/')
 data=calculate();out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'controls':data['controls'],'pr135_813_same_parent':data['pr135_813_same_parent']}))
 return 0 if all(data['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
