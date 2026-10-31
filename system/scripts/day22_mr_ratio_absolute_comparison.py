#!/usr/bin/env python3
"""137Pr printed ratio reconstruction and108In measured-strength comparison; no new fit."""
import argparse,hashlib,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
RAW={
 'AG07':('raw/papers/gpt/learning-daily/20260929-DAY3-mean-field-nilsson-csm-hfb-projection/137pr-2007-magnetic-rotation/PDFs/Bandcrossing_of_magnetic_rotation_bands_in_137Pr.pdf','83ccf538913d777f60832ee7ff304ffa8ca0678399b893f827236a6ab33c6a55'),
 'CHI01':('raw/papers/gpt/learning-daily/20261009-PREPLAN-high-spin-library/2001_Chiara et al_Spectroscopy in 108,110In isotopes_Lifetime measurements in shears bands.pdf','5672ffce1e4049245b3107e6132af0ff7501d14182a03d803cd66828e6660a4e')}
def calculate():
 hashes={}
 for key,(p,sha) in RAW.items():
  hashes[key]=hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
  if hashes[key]!=sha:raise ValueError('raw identity mismatch '+key)
 # Same-parent branch row pairs transcribed from AG07 Table I.
 rows=[]
 for spin,em,im,ee,ie,printed in [(14.5,321,50.9,432.6,1.6,10.4),(15.5,341.5,34,662.5,7.1,10.5),(16.5,483.4,26.8,824.1,3.6,17.2),(17.5,478,17.9,961.7,2.3,41.2),(18.5,341.4,14.7,819.4,1.4,62.1),(19.5,408.4,14.6,749.2,1,33.3),(20.5,465.5,8.9,872.3,1.9,17.2),(21.5,507.2,5.7,972.1,1.1,18.5),(22.5,576.7,2.4,1083.6,1,12.8),(23.5,657.4,2.6,1233.7,1,18.9)]:
  value=.697*im*(ee/1000)**5/(ie*(em/1000)**3)
  rows.append({'spin':spin,'EM1_keV':em,'IM1':im,'EE2_keV':ee,'IE2':ie,'R_computed_muN2_per_e2b2':value,'R_printed':printed,'fractional_central_residual':(value-printed)/printed})
 # Source ratio does not identify both absolute factors; positive constructed witnesses.
 Rs=[r['R_printed'] for r in rows]
 altA=[{'B_E2_e2b2':.02,'B_M1_muN2':.02*r} for r in Rs]
 altB=[{'B_E2_e2b2':1/r,'B_M1_muN2':1.0} for r in Rs]
 in108={'Band2':{'spin_parity':['14-','15-','16-'],'B_M1_muN2':[.911,.600,.398]},'Band3':{'spin_parity':['16+','17+','18+','19+'],'B_M1_muN2':[2.48,2.38,1.71,5.22],'B_E2_e2b2_at18_19':[.059,.169],'tau_ps_at18_19':[.158,.055]}}
 controls={
  '29half_ratio_center_reproduces_print_within_3percent':abs(rows[0]['fractional_central_residual'])<.03,
  '43half_central_nonclosure_is_retained':rows[7]['R_computed_muN2_per_e2b2']>23.9 and rows[7]['R_printed']==18.5,
  'ratio_not_monotone_across_observed_sequence':not all(a>=b for a,b in zip(Rs,Rs[1:])) and not all(a<=b for a,b in zip(Rs,Rs[1:])),
  'two_positive_absolute_witnesses_same_ratios':all(min(a['B_E2_e2b2'],a['B_M1_muN2'],b['B_E2_e2b2'],b['B_M1_muN2'])>0 and math.isclose(a['B_M1_muN2']/a['B_E2_e2b2'],r) and math.isclose(b['B_M1_muN2']/b['B_E2_e2b2'],r) for a,b,r in zip(altA,altB,Rs)),
  'actual_108In_band3_has_alignment_upturn':in108['Band3']['B_M1_muN2'][-1]>in108['Band3']['B_M1_muN2'][-2],
 }
 return {'raw_sha256':hashes,'AG07_locator':'024321-4 TableI and024321-5/6 ratio equation','AG07_rows':rows,'constructed_absolute_witness_A':altA,'constructed_absolute_witness_B':altB,'CHI01_locator':'054314-19 TableV;054314-21–23 discussion andFig12','In108_reported':in108,'all_ten_centers_reproduced_within_3percent':False,'43half_input_rounding_box_R':[.6965*5.65*(.97205)**5/(1.15*(.5073)**3),.6975*5.75*(.97215)**5/(1.05*(.5071)**3)],'central_ratios_no_new_CI':{'137Pr_R37over41':62.1/17.2,'108In_BM1_band2_14over16':.911/.398,'108In_BM1_band3_19over18':5.22/1.71},'controls':controls,'boundaries':['AG07 assumes negligible M1/E2 mixing in dipole branch; no absolute lifetime measured there.','Initial all-ten-centers within3percent hypothesis failed; largest43/2 central residual29.9percent retained rather than changing table inputs.',
 'No uncertainties, covariance, confidence interval or experimental significance reconstructed.','Chosen positive absolute witnesses are arbitrary scale examples, not measurements or claims of physical model feasibility.','CHI01 rates are author-derived fromDSAM/branching/ICC; quoted errors exclude stopping systematics up to20percent.','No universal shears angle, deformation threshold or cross-nucleus M1 magnitude gate follows.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('output must be inside outputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'central_ratios':d['central_ratios_no_new_CI'],'max_fractional_rounding_residual':max(abs(x['fractional_central_residual']) for x in d['AG07_rows'])}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
