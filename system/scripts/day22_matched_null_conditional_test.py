#!/usr/bin/env python3
"""Matched independentnull four-count conditionaltest; chosenstatisticalmodel, no facilitybudget."""
import argparse,json,math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]

def logcomb(n,k):
 if k<0 or k>n:return -math.inf
 return math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
def normalize(logs):
 peak=max(logs);x=np.exp(np.array(logs)-peak);return x/x.sum()
def conditional_probs(table,odds=1.):
 xt,yt,xc,yc=table;nt=xt+yt;nc=xc+yc;K=xt+xc;N=nt+nc
 support=np.arange(max(0,K-nc),min(nt,K)+1)
 logw=[logcomb(K,int(x))+logcomb(N-K,nt-int(x))+int(x)*math.log(odds) for x in support]
 return support,normalize(logw)
def poisson_conditioned(table,a,ct,cc,A):
 xt,yt,xc,yc=table;nt=xt+yt;nc=xc+yc;K=xt+xc
 support,_=conditional_probs(table)
 mu=[a*ct*(1+A),ct*(1-A),a*cc,cc]
 logs=[]
 for x in support:
  cells=[int(x),nt-int(x),K-int(x),nc-K+int(x)]
  logs.append(sum(n*math.log(m)-m-math.lgamma(n+1) for n,m in zip(cells,mu)))
 return normalize(logs)
def estimate(table,Q):
 xt,yt,xc,yc=table;L=math.log(xt/yt)-math.log(xc/yc);A=math.tanh(L/2);p=A/Q
 K=(1-A*A)/(2*Q);signs=[1,-1,-1,1];jac=[K*s/n for s,n in zip(signs,table)]
 return {'A':A,'P':p,'Jacobian':jac,'local_varP':sum(g*g*n for g,n in zip(jac,table))}
def interval(table,alpha=.05):
 # Invert each one-sided conditional tail, including the observed table.
 support,_=conditional_probs(table);x=table[0]
 def tail(logodds,upper):
  _,p=conditional_probs(table,math.exp(logodds));return float(p[support>=x].sum() if upper else p[support<=x].sum())
 def root(target,upper):
  lo,hi=-60.,60.
  for _ in range(100):
   mid=(lo+hi)/2;y=tail(mid,upper)
   if (y<target)==upper:lo=mid
   else:hi=mid
  return (lo+hi)/2
 lower=-math.inf if x==support[0] else root(alpha/2,True)
 upper=math.inf if x==support[-1] else root(alpha/2,False)
 one_lower=-math.inf if x==support[0] else root(alpha,True)
 return {'log_odds_lower':lower,'log_odds_upper':upper,'A_lower':math.tanh(lower/2),'A_upper':math.tanh(upper/2),'one_sided_log_odds_lower':one_lower,'one_sided_A_lower':math.tanh(one_lower/2)}

def calculate():
 table=[954,940,900,1000];Q=.2;a=.9;ct=cc=1000.;A=.06
 e=estimate(table,Q);support,p0=conditional_probs(table);_,p1=conditional_probs(table,(1+A)/(1-A))
 pvalue=float(p0[support>=table[0]].sum())
 p0_direct=[poisson_conditioned(table,aa,tt,ccal,0) for aa,tt,ccal in [(.9,1000,1000),(1.8,400,800),(2.5,100,3000)]]
 p1_direct=poisson_conditioned(table,a,ct,cc,A)
 mu=np.array([a*ct*(1+A),ct*(1-A),a*cc,cc]);J=np.array([[mu[0],0,mu[0],a*ct*Q],[mu[1],0,0,-ct*Q],[0,mu[2],mu[2],0],[0,mu[3],0,0]],dtype=float)
 F=J.T@np.diag(1/mu)@J;fv=float(np.linalg.inv(F)[-1,-1])
 target_J=J[:2][:,[0,2,3]];target_F=target_J.T@np.diag(1/mu[:2])@target_J
 doubled=[n*4 for n in table];s4,p4=conditional_probs(doubled);pvalue4=float(p4[s4>=doubled[0]].sum())
 ci=interval(table)
 small=[3,2,3,4];ss,_=conditional_probs(small);small_ci={int(x):interval([int(x),5-int(x),6-int(x),1+int(x)]) for x in ss}
 coverages=[]
 for logodds in [-2.,-.12,0.,.12,2.]:
  _,p=conditional_probs(small,math.exp(logodds))
  coverage=sum(float(prob) for x,prob in zip(ss,p) if small_ci[int(x)]['log_odds_lower']<=logodds<=small_ci[int(x)]['log_odds_upper'])
  coverages.append({'logodds':logodds,'conditional_coverage':coverage})
 def at_tail(logodds,upper):
  _,p=conditional_probs(table,math.exp(logodds));return float(p[support>=table[0]].sum() if upper else p[support<=table[0]].sum())
 interval_controls={
  'inverted_central_tails_match_alpha_over_two':max(abs(at_tail(ci['log_odds_lower'],True)-.025),abs(at_tail(ci['log_odds_upper'],False)-.025))<1e-10,
  'one_sided_lower_tail_matches_alpha':abs(at_tail(ci['one_sided_log_odds_lower'],True)-.05)<1e-10,
  'central95_contains_zero_but_one_sided95_lower_positive':ci['A_lower']<0<ci['A_upper'] and ci['one_sided_A_lower']>0 and pvalue<.05,
  'small_margin_exact_enumeration_coverage_not_below95_at_chosen_parameters':min(x['conditional_coverage'] for x in coverages)>=.95-1e-12,
  'boundary_tables_retain_infinite_odds_limits':math.isinf(small_ci[int(ss[0])]['log_odds_lower']) and math.isinf(small_ci[int(ss[-1])]['log_odds_upper']),
 }
 ci['P_interval_with_chosen_knownQ']=[ci['A_lower']/Q,ci['A_upper']/Q]
 ci['P_one_sided_lower_with_chosen_knownQ']=ci['one_sided_A_lower']/Q
 mismatch={'target_A' :0.,'target_a':mu[0]/mu[1],'target_ct':mu[1],'calibration_a':a,'calibration_cc':cc}
 bad_means=[mismatch['target_a']*mismatch['target_ct'],mismatch['target_ct'],a*cc,cc]
 controls={
  'conditional_null_independent_of_a_and_exposure_parameters':max(float(np.max(np.abs(x-p0))) for x in p0_direct)<1e-11,
  'conditional_alt_equals_noncentral_hypergeometric_odds':float(np.max(np.abs(p1_direct-p1)))<1e-11,
  'four_count_local_variance_equals_full_Poisson_Fisher_inverse':abs(e['local_varP']-fv)<1e-12,
  'calibrator_restores_full_rank_but_target_alone_does_not':np.linalg.matrix_rank(F)==4 and np.linalg.matrix_rank(target_F)==2,
  'increased_chosen_exposure_retains_estimate_and_reduces_pvalue':abs(estimate(doubled,Q)['P']-e['P'])<1e-14 and pvalue4<pvalue,
  'unmatched_a_zeroP_can_mimic_entire_four_count_means':max(abs(x-y) for x,y in zip(bad_means,mu.tolist()))<1e-10,
 }
 return {'scope':'taskdefinedmatchednullcalibrationmodel;notactualtargetdataorproposalpower','source_context':'Miller2007Eqs5/6andcurrentconditionalcountcontract','convention':'MillerA=(x-a*y)/(x+a*y),a=Uperp/Uparallel','chosen_integer_table_target_perp_parallel_cal_perp_parallel':table,'declared_known_Q':Q,'declared_true_A':A,'estimate':e,'conditional_null':'Xtargetperp|row/columnmargins ~ Hypergeom(Ntotal,Kperp,Ntarget)','conditional_alternative_odds':'omega=(1+A)/(1-A)','exact_one_sided_null_pvalue_for_chosen_table':pvalue,'four_times_chosen_table_pvalue':pvalue4,'full_Fisher_local_varP':fv,'target_only_Fisher_rank':int(np.linalg.matrix_rank(target_F)),'unmatched_calibration_counter_witness':mismatch,'central95_conditional_interval':ci,'small_margin_coverage_enumeration':coverages,'interval_controls':{k:bool(v) for k,v in interval_controls.items()},'controls':{k:bool(v) for k,v in controls.items()},'boundaries':['IndependentrawpositivePoissoncells,exclusiveevents,no background,knownphysicalnullcalibration,shareda/matchedenergy/geometry/gates/weightsareassumptions.','Realnetpeakfitcountsandsharedreference/eventsubsetsneedactualjointlikelihood/Cov,notthisfourindependentcellmodel.','Qisknownonlybychoice;signtestrequiresknownpositiveQsign,absoluteP/amplituderequiresQcalibration.','Thechosenfourcountsarenotactualobservations,expectedfacilityratesorbeamtimeallocation.','Exactconditionalpvaluerejectsthedeclaredshared-aP0null,notallnonchiral/chiral/wobblingmodels.','Unmatchedaresponsecanmimiccontrast,soalowstatisticalpvaluealonecannotvalidatephysicalcalibration.','Localvarianceisnotafinite-sampleCIorunbiasednessclaim.','Exactconditionalintervals118applyonlytothisdeclaredfourcellmodelandknownQ,notactualtarget/calibrationuncertainty.']}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',required=True);a=p.parse_args();out=(ROOT/a.output).resolve()
 if not out.is_relative_to(ROOT/'outputs'):p.error('outputmustbeinsideoutputs/')
 d=calculate();out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'controls':d['controls'],'chosen_P':d['estimate']['P'],'local_sigmaP':math.sqrt(d['estimate']['local_varP']),'conditional_pvalue':d['exact_one_sided_null_pvalue_for_chosen_table'],'four_times_pvalue':d['four_times_chosen_table_pvalue'],'interval_controls':d['interval_controls'],'conditional_interval':d['central95_conditional_interval']}));return 0 if all(d['controls'].values()) and all(d['interval_controls'].values()) else 1
if __name__=='__main__':raise SystemExit(main())
