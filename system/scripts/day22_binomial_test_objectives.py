#!/usr/bin/env python3
"""Exact two-bin test objectives for old unvalidated134 means; not a physical count budget."""
import argparse,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def tails(n,p):
 logs=[math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)+k*math.log(p)+(n-k)*math.log1p(-p) for k in range(n+1)]
 raw=[math.exp(x) for x in logs];mass=sum(raw);pmf=[x/mass for x in raw]
 tail=[0.]*(n+2)
 for k in range(n,-1,-1):tail[k]=tail[k+1]+pmf[k]
 return tail,mass

def design(n,A0,A1,z,objective):
 p0,p1=(1+A0)/2,(1+A1)/2;alpha=.5*math.erfc(z/math.sqrt(2))
 t0,m0=tails(n,p0);t1,m1=tails(n,p1)
 critical=next(k for k,x in enumerate(t0) if x<=alpha)
 return {'objective':objective,'N_selected':n,'null_A':A0,'alternative_A':A1,'one_sided_normal_equivalent_z':z,'alpha_target':alpha,'reject_if_Nperp_at_least':critical,'exact_null_tail_at_critical':t0[critical],'exact_null_tail_one_count_lower':None if critical==0 else t0[critical-1],'exact_alternative_rejection_power':t1[critical],'raw_pmf_masses':[m0,m1]}

def calculate():
 A0=-.0877008371162673;A1=.02885245901639344
 specs=[(663,A0,A1,3,'old_two_mean_separation'),(1841,A0,A1,5,'old_two_mean_separation'),(663,0,A1,3,'positive_asymmetry_against_zero'),(10803,0,A1,3,'positive_asymmetry_against_zero'),(1500,A0,A1,3,'chosen_larger_sample_two_mean_separation'),(23000,0,A1,3,'chosen_larger_sample_positive_asymmetry')]
 rows=[design(*x) for x in specs]
 controls={
  'all_numerical_binomial_masses_close_to_one':all(abs(m-1)<1e-8 for r in rows for m in r['raw_pmf_masses']),
  'critical_integer_controls_one_sided_alpha_and_is_smallest':all(r['exact_null_tail_at_critical']<=r['alpha_target'] and r['exact_null_tail_one_count_lower']>r['alpha_target'] for r in rows),
  'old_mean_separation_samples_give_near_half_not_high_power':all(.4<rows[i]['exact_alternative_rejection_power']<.6 for i in [0,1]),
  'old_N663_positive_sign_power_is_small':rows[2]['exact_alternative_rejection_power']<.05,
  'chosen_larger_samples_have_above90percent_power_only_in_declared_toy':all(rows[i]['exact_alternative_rejection_power']>.9 for i in [4,5]),
 }
 return {'scope':'test-targetdiagnosticofoldunvalidatedAmeans;notactualPprediction,apparatusfeasibilityorproposal','assumptions':['a=1known,exclusiveindependentBernoulliselectedsignalbins,Nfixed,no background orcalibrationuncertainty','one-sidedtestswithpredeclarednull/alternative','old134polarizationmodelisinvalid;meansusedonlytoaudittestsemantics'],'rows':rows,'controls':controls,'boundaries':['Chosen1500/23000samplesarenotminimaldesignsolutionsandarenotconvertedtohours.','No composite nuclear-model/nuisanceprediction setwasdefinedor tested.','Normal-equivalentzspecifiesalphaonly;powerisreportedseparately.','More targetcounts cannotresolve completelyfreea/Q nuisances established in111.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('outputmustbeinsideoutputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'results':[{'objective':r['objective'],'N':r['N_selected'],'alpha':r['exact_null_tail_at_critical'],'power':r['exact_alternative_rejection_power'],'critical':r['reject_if_Nperp_at_least']} for r in d['rows']]}));return 0 if all(d['controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
