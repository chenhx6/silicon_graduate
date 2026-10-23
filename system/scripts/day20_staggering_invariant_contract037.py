#!/usr/bin/env python3
"""Declared collective-coordinate and closure algebra, plus literal MC07 benchmark ledger.

No Cline/Kumar original was read for this checkpoint. The following own controls
are not a reconstruction of their experimental method, matrix elements or CI.
"""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);args=p.parse_args();checks=[]
 def check(name,ok):
  if not ok:raise AssertionError(name)
  checks.append(name)
 # z=cos3gamma uniform on[-1,1] corresponds to normalized sin3gamma measure.
 z,w=leggauss(64);w=w/2
 moments={'flat_sin3gamma_measure':{'mean_c':float(w@z),'mean_c2':float(w@(z*z)),'variance_c':float(w@(z*z)-(w@z)**2)},'delta_gamma30':{'mean_c':0.,'mean_c2':0.,'variance_c':0.}}
 check('normalized flat angular measure gives1/3 variance',math.isclose(sum(w),1) and math.isclose(moments['flat_sin3gamma_measure']['variance_c'],1/3))
 # Coordinate invariants of degree2/3/4/6 in quadrupole amplitude. Constants
 # and tensor-coupling normalization intentionally not attributed to a source.
 contrast=[{'chosen_beta':1.,'angular_distribution':name,'mean_beta2':1.,'mean_beta3_c':m['mean_c'],'mean_beta4':1.,'mean_beta6_c2':m['mean_c2']} for name,m in moments.items()]
 check('same second third fourth coordinate moments need not fix angular variance',all(abs(r['mean_beta3_c'])<1e-14 for r in contrast) and contrast[0]['mean_beta6_c2']>.3 and contrast[1]['mean_beta6_c2']==0)
 # Beta fluctuations: factorization changes the normalization of q6/q2^3.
 beta=np.array([.5,1.5]);probs=np.array([.5,.5]);beta2=float(probs@(beta**2));beta6=float(probs@(beta**6));pseudo=beta6/(beta2**3)/3
 check('variable beta spoils fixed-beta mean-ratio shortcut',not math.isclose(pseudo,1/3))
 # For 0->2_i->2_j->0 closure, all i,j share angular factors. These real
 # reduced-element examples change the cubic sum while holding first diagonal.
 v=np.array([1.,1.]);closure=[]
 for off in [-1.,1.]:
  M=np.array([[0.,off],[off,0.]])
  closure.append({'chosen_0_to_2_reduced_vector':v.tolist(),'chosen_2_to_2_reduced_matrix':M.tolist(),'first_state_diagonal':0.,'cubic_closure_sum_up_to_common_angular_factor':float(v@M@v)})
 check('single zero static diagonal does not fix cubic scalar closure sum',closure[0]['cubic_closure_sum_up_to_common_angular_factor']==-2 and closure[1]['cubic_closure_sum_up_to_common_angular_factor']==2)
 # Source MC07 Fig1: U5 -1, axial+1/3, deformed gamma-soft -2, rigidgamma30 +1.67.
 S=lambda e4,e3,e2,e21:(e4-2*e3+e2)/e21
 bench={'vibrator':S(3,3,2,1),'axial_same_inertia_rotor':S(16,8,2,6),'gamma_soft_tau_tau_plus3':S(18,18,10,4)}
 check('three declared spectra reproduce source limiting benchmarks',math.isclose(bench['vibrator'],-1) and math.isclose(bench['axial_same_inertia_rotor'],1/3) and math.isclose(bench['gamma_soft_tau_tau_plus3'],-2))
 check('positiveS4 is not a unique rigidtriaxial criterion',bench['axial_same_inertia_rotor']>0)
 out={'checkpoint':'037','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
 'MC07_literal_Fig1_benchmarks':{'vibrator':-1.,'axial_rotor':.33,'gamma_soft':-2.,'rigid_gamma30':1.67},'declared_spectrum_controls':bench,
 'MC07_scope_boundary':'Eq2 defines S(J); Figs2–4 empirical curves, no four exact level energies per old013 nucleus supplied here. PDF3 notes reversed-like patterns for selected nuclei onlyJ>5. No unique shape from one sign.',
 'angular_measure_controls':moments,'fixed_beta_coordinate_moment_contrast':contrast,
 'beta_fluctuation_counterexample':{'chosen_beta':beta.tolist(),'chosen_probabilities':probs.tolist(),'mean_beta2':beta2,'mean_beta6':beta6,'q6_over_q2_cubed_if_flat_gamma_independent_beta':pseudo,'actual_var_cos3gamma':1/3},
 'static_diagonal_closure_counterexample':closure,
 'closure_contract':'Real E2 reduced elements, initial0 state and intermediate2 states; schematic cubic sum shares angular coefficient. Does not reconstruct an actual nucleus, tensor normalization, GOSIA fit or truncation errors.',
 'invariant_boundary':'beta3 cos3gamma has degree3, its square beta6 cos²3gamma degree6. Fourth-order beta4 does not fix angular variance. Fixed-beta quotient shortcuts fail under beta-gamma fluctuations. Complete signed matrix-element sums, intermediate-state coverage, conventions and Cov needed experimentally.',
 'withdrawn':['oldgamma_softS4=-2.5','unverified exact130Ba134Ba130Xe192Os level vectors and derivedS4','singleQs sign or zero determines cubic invariant or shape','fourthorder invariant suffices for angular variance','S4 sign rules out all rigidtriaxial models','singleQt measures only beta without gamma/operator assumptions'],
 'controls':checks,'certification_scope':'Declared coordinate/closure algebra and original selected S(J) locators only. No Cline1986/Kumar original reading or experimental certification claimed.'}
 target=args.run_dir/'staggering-invariant-result-037.json';target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'artifact':str(target),'controls':len(checks),'benchmarks':bench,'variable_beta_shortcut':pseudo}))
if __name__=='__main__':main()
