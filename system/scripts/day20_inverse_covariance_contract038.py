#!/usr/bin/env python3
"""Declared inverse-model counterexamples and GLS nuisance identities; not experimental fits/CI."""
import argparse,hashlib,json,math
from fractions import Fraction
from pathlib import Path
import numpy as np


def gls(X,y,V):
 wX=np.linalg.solve(V,X);C=np.linalg.inv(X.T@wX);b=C@(wX.T@y);return b,C


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);args=p.parse_args();checks=[]
 def check(name,ok):
  if not ok:raise AssertionError(name)
  checks.append(name)
 ledger=json.loads((args.run_dir/'singh-table-ledger-001.json').read_text());rows=[r for r in ledger['case_Pr133']['rows'] if r['Qt']['kind']=='finite']
 x=np.array([float(Fraction(str(r['spin']))) for r in rows]);y=np.array([r['Qt']['value'] for r in rows]);err=np.array([(r['Qt']['plus']+r['Qt']['minus'])/2 for r in rows]);xc=x-np.mean(x);X=np.column_stack([np.ones(len(x)),xc]);D=np.diag(err**2);b,C=gls(X,y,D)
 base={'coefficient_centered_intercept_slope':b.tolist(),'slope_se':math.sqrt(C[1,1]),'slope_z':b[1]/math.sqrt(C[1,1])};sigma_b=.05;G=np.diag([.2**2,sigma_b**2]);V=D+X@G@X.T;bb,CC=gls(X,y,V)
 check('nuisance exactly in design span leaves GLS coefficients unchanged',np.allclose(bb,b,rtol=1e-12,atol=1e-12))
 check('design-span nuisance adds parameter covariance exactly',np.allclose(CC,C+G,rtol=1e-12,atol=1e-12))
 mult=[]
 for k in [.8,1.2]:
  bk,Ck=gls(X,k*y,k*k*D);mult.append({'chosen_scale':k,'slope_z':bk[1]/math.sqrt(Ck[1,1])})
 check('all-y and all-Cov common scale preserves z',all(math.isclose(v['slope_z'],base['slope_z'],rel_tol=1e-12) for v in mult))
 # Observed-vector rank1 covariance vs fixed fitted-mean response are different models.
 scale=.1;Vobs=D+scale**2*np.outer(y,y);bo,Co=gls(X,y,Vobs);res=y-X@b;chi=float(res@np.linalg.solve(D,res));den=1+scale*scale*chi
 check('observed-y rank1 covariance rescales coefficient by residual chi2',np.allclose(bo,b/den,rtol=1e-12,atol=1e-12))
 check('observed-y rank1 covariance exact Woodbury parameter covariance',np.allclose(Co,C+scale**2*np.outer(b,b)/den,rtol=1e-12,atol=1e-12))
 mean=X@b;bm,Cm=gls(X,y,D+scale**2*np.outer(mean,mean));check('fixed fitted-mean response has different coefficient rule',np.allclose(bm,b) and not np.allclose(bo,b))
 # Selected mixing matrices. Full operator contributions retained.
 q=3.5;ratio=2.5/q;theta=math.acos(math.sqrt(ratio));rot=lambda t:np.array([[math.cos(t),-math.sin(t)],[math.sin(t),math.cos(t)]])
 U=rot(theta);same=U.T@(q*np.eye(2))@U;dark=U.T@np.diag([q,0.])@U
 check('equal intrinsic E2 matrices and same initial final mixing preserve full matrix',np.allclose(same,q*np.eye(2)))
 check('cos2 attenuation requires dark partner in this symmetric chosen example',math.isclose(dark[0,0],2.5))
 check('mixing redistributes full Frobenius norm only for complete orthogonal spaces',math.isclose(float(np.sum(dark*dark)),q*q))
 # Serial feeding: same mean as one exponential, different full time response.
 tau,feed=1.4,1.344;mean_tau=tau+feed;var_serial=tau*tau+feed*feed;var_single=mean_tau**2
 s_values=[.2,.5,1.];lap=[{'chosen_inverse_time_per_ps':s,'serial_Laplace':1/((1+s*tau)*(1+s*feed)),'mean_matched_single_Laplace':1/(1+s*mean_tau)} for s in s_values]
 check('serial feeding mean equality does not imply equal full spectra',all(r['serial_Laplace']<r['mean_matched_single_Laplace'] for r in lap) and var_serial<var_single)
 # A genuinely nonunique scalar triaxial inversion in Singh's signed chart.
 g=math.degrees(math.acos(ratio*math.cos(math.pi/6)));roots=[g-30,-g-30]
 check('two signed-chart gamma roots reproduce chosen scalar amplitude',all(math.isclose(q*math.cos(math.radians(v+30))/math.cos(math.pi/6),2.5) for v in roots))
 out={'checkpoint':'038','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
 'literal_Pr_finite_rows_contract':'SinghPresent Table2, average asymmetric errors and independent fixed Gaussian covariance; limits/old refs excluded, source originalCov unavailable',
 'baseline_GLS_conditional':base,'design_span_nuisance':{'chosen_G_centered_intercept_slope':G.tolist(),'coefficient':bb.tolist(),'slope_se':math.sqrt(CC[1,1]),'slope_z':bb[1]/math.sqrt(CC[1,1]),'identity':'V=D+XGX^T implies betaGLS unchanged and Cov(beta)=C0+G'},
 'multiplicative_control':mult,'observed_y_rank1':{'chosen_fractional_scale':scale,'residual_chi2':chi,'coefficient_shrink_denominator':den,'coefficient':bo.tolist(),'slope_se':math.sqrt(Co[1,1]),'slope_z':bo[1]/math.sqrt(Co[1,1]),'se_relative_change':math.sqrt(Co[1,1]/C[1,1])-1,'boundary':'Data-dependent covariance direction y is a chosen statistical construction, not known stopping response.'},
 'fixed_mean_rank1':{'coefficient':bm.tolist(),'slope_se':math.sqrt(Cm[1,1]),'boundary':'Mean response frozen from this diagnostic; not actual source nuisance or unique experimental model.'},
 'mixing_counterexamples':{'chosen_theta_deg':math.degrees(theta),'equal_diagonal_operator_result':same.tolist(),'dark_partner_operator_result':dark.tolist(),'scope':'Initial/final identical real orthogonal mixing; interconfiguration matrix elements set zero, equal vs dark diagonal explicitly distinguished. No inferred actual admixture.'},
 'serial_feeding_counterexample':{'chosen_tau_ps':tau,'chosen_feed_ps':feed,'same_mean_ps':mean_tau,'serial_variance_ps2':var_serial,'single_variance_ps2':var_single,'Laplace_responses':lap,'scope':'Independent exponential waiting times, exact sums/Laplace transforms. Same scalar mean not same DSAM/RDDS response; no original data likelihood claim.'},
 'chosen_gamma_roots':roots,'inversion_scope':'Signed scalar chart only, gamma periodicity/axis identification and magnitude-only branch alternatives remain; not two uniquely measured physical shapes.',
 'withdrawn':['Generic mixing cos² suppression with both intrinsic matrices equal','Full experimental indistinguishability from single mean equality','Actual feeding delay=1.344ps inferred from Qt drop','Uniform stopping uncertainty cannot eliminate actual trend','Rank1 covariance predominantly intercept hence universal small slope impact','TDPAD always independent of feeding','complete companion-observable one-to-one discriminator'],
 'controls':checks,'certification_scope':'Explicit models and algebra only; no original spectrum/Cov/precision or universal mechanism certification.'}
 target=args.run_dir/'inverse-covariance-result-038.json';target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'artifact':str(target),'controls':len(checks),'baseline':base,'rank1_se_relative_change':out['observed_y_rank1']['se_relative_change'],'rank1_beta_shrink_denominator':den,'theta':math.degrees(theta),'serial_variance':var_serial,'single_variance':var_single}))
if __name__=='__main__':main()
