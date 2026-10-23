#!/usr/bin/env python3
"""Conditional additivity/operator controls and literal source-role ledger; no new fit or CI."""
import argparse,hashlib,json,math
from pathlib import Path
import numpy as np


def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--run-dir',type=Path,required=True);args=p.parse_args()
 pairs=[['133Nd nu_i13/2',5.8,.2,6.5,.2],['135Nd nu_i13/2',5.1,.2,5.7,.2],['136Pm band1',4.8,.3,5.2,.3],['136Pm band2',4.8,.4,5.2,.4],['137Sm nu_i13/2',4.4,.3,4.8,.4]]
 gates=[{'band':name,'default_Qt_eb':a,'default_printed_error_eb':ea,'above_level_gate_Qt_eb':b,'gate_printed_error_eb':eb,'central_increase_percent':100*(b/a-1),'conditional_tau_ratio_fixed_rate_inputs':(a/b)**2,'dependency':'Alternative gate/fit on same experimental collection; covariance unavailable, not independent repeats.'} for name,a,ea,b,eb in pairs]
 controls=[]
 def check(name,ok):
  if not ok:raise AssertionError(name)
  controls.append(name)
 check('five b pairs span8.33 to12.07percent',math.isclose(min(v['central_increase_percent'] for v in gates),100/12) and math.isclose(max(v['central_increase_percent'] for v in gates),100*.7/5.8))
 # Own variable contract: component A=R cosg, B=R sing, y-cranking Qt=A-B/sqrt3.
 grid=np.linspace(-math.pi,math.pi,241);radial=4.2;A=radial*np.cos(grid);B=radial*np.sin(grid)
 component=A-B/math.sqrt(3);trig=radial*np.cos(grid+math.pi/6)/math.cos(math.pi/6)
 check('trig identity requires radial amplitude not Cartesian component as prefactor',np.allclose(component,trig,atol=3e-15))
 incorrect=A*np.cos(grid+math.pi/6)/math.cos(math.pi/6)
 check('reusing symbol Q20 as both component and radial prefactor produces counterexample',np.max(abs(component-incorrect))>1)
 check('passive xy exchange changes B sign and cranking sign together',np.allclose(A+(-B)/math.sqrt(3),component))
 # Chosen nonlinear response, not nuclear data: q(n,w)=qcore+a*n+b*n*w+c*n^2.
 qcore,a,b,c=6.,.3,-.2,.1
 q=lambda n,w:qcore+a*n+b*n*w+c*n*n
 step1=q(1,.5)-q(0,.5);step2=q(2,.5)-q(1,.5)
 crossing_difference=q(2,1.5)-q(1,.5)
 check('same-frequency finite particle increments can differ if curvature exists',math.isclose(step2-step1,2*c))
 check('two bands at different frequencies do not yield controlled particle increment',not math.isclose(crossing_difference,step2))
 # If actual independent equal-error assumptions were imposed, inferential result
 # would change with unknown covariance, which cannot be chosen from band count.
 ea,eb=.2,.2
 sigmas=[math.sqrt(ea*ea+eb*eb-2*rho*ea*eb) for rho in [0,.5,.9]]
 check('difference precision depends on unpublished covariance',sigmas[0]>2*sigmas[-1])
 table_coeffs=[{'orbital':'nu6_2,+i','qt_eff_CHF_eb':.37,'printed_fit_error_CHF_eb':.03,'qt_eff_CRMF_eb':.37,'printed_fit_error_CRMF_eb':.01},
 {'orbital':'pi[404]9/2,+i','qt_eff_CHF_eb':-.38,'printed_fit_error_CHF_eb':.02,'qt_eff_CRMF_eb':-.38,'printed_fit_error_CRMF_eb':.01,'conditional_hole_sign':'c=-1 gives positive contribution only if defined relative to occupied core; do not override TableI/p7 label conflict'},
 {'orbital':'pi[541]3/2,+i','qt_eff_CHF_eb':.52,'printed_fit_error_CHF_eb':.04,'qt_eff_CRMF_eb':.54,'printed_fit_error_CRMF_eb':.01}]
 out={'checkpoint':'035','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'experimental_fit_or_CI':False,
 'Riley_TableI_b_pairs':gates,'Riley_other_analysis_role':'135Sm5.8(4),6.4(4)c uses alternative feeding-time structure; not sixth high-gate pair. Authors expect ~10percent extension to other HD bands; this is extrapolation, not measurement.',
 'operator_contract':{'declared_variables':'A=R cosgamma, B=R singamma, Qt(y)=A-B/sqrt3; R radial amplitude','scope':'Trig identity does not identify Singh Q20 with Matev component Q20, rotate actual experiment, or certify their producer. Preserve Eq14 literal label mismatch.'},
 'Matev_selected_TableII_coefficients':table_coeffs,'model_scope':'arXiv0707.4324v1, SLy4 CHF183 / NL1 CRMF105 selected calculated configurations; core131Ce, hbaromega=.65MeV; excluded crossings and ambiguous assignments; errors are conditional model-regression errors.',
 'Matev_literal_residual_statements':{'PDF11_Q20_CHF':'97.8percent within +/-0.1eb','PDF11_Q20_CRMF':'more than90percent within +/-0.05eb','PDF12_Q22_CRMF':'nearly95percent within +/-0.025eb;98percent within +/-0.1eb','PDF12_Q22_CHF':'more than90percent within +/-0.2eb','boundary':'No source-wide Qt residual sigma .12/.15eb certified by these statements; no reconstructed histogram variance.'},
 'chosen_nonlinear_counterexample':{'parameters':[qcore,a,b,c],'first_increment_same_frequency':step1,'second_increment_same_frequency':step2,'different_frequency_band_difference':crossing_difference,'boundary':'Demonstration only; not actual self-consistent solution or fitted nuclear coefficient.'},
 'covariance_demonstration':{'chosen_errors':[ea,eb],'chosen_correlations':[0,.5,.9],'difference_standard_deviations':sigmas,'boundary':'No inferred source covariance.'},
 'rejected_inferences':['Universal empirical feeding correction','2.0/3.1eb as controlled effective single-particle coefficients','9.9eb prediction and35.4percent experimental saturation deficit','Ce2.58(10) as directly measured RDM point','HD moments close implies shell-gap locking/geometric rigidity','Conditional TableII residuals establish official typo/sign repair'],
 'controls':controls,'certification_scope':'Input ledger and explicitly chosen algebra only; no original experimental precision or universal mechanism certification.'}
 target=args.run_dir/'additivity-contract-result-035.json';target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'artifact':str(target),'controls':len(controls),'gate_increases':[r['central_increase_percent'] for r in gates],'experimental_fit_or_CI':False}))
if __name__=='__main__':main()
