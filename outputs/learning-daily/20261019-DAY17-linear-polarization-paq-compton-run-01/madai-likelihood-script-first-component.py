#!/usr/bin/env python3
"""Execute the pinned original MADAI Model likelihood with declared controls."""
from pathlib import Path
import hashlib,json,math,subprocess
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    path=RUN/'madai-likelihood-contract.json';c=json.loads(path.read_text());assert c['identity']=='MADAI2015-ORIGINAL-MODEL-COMPONENT-01'
    for p,h in c['source_hashes'].items():assert sha(ROOT/p)==h,p
    cmd=['g++','-std=c++11','-O1']+['-I'+x for x in c['include_dirs']]+[c['fixture']]+c['original_sources']+['-o',c['binary']]
    p=subprocess.run(cmd,cwd=ROOT,capture_output=True,text=True);result={'identity':c['identity'],'script_sha256':sha(__file__),'contract_sha256':sha(path),'compile':{'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr},'scope':c['assumptions'],'source_pin':c['source_pin']}
    if p.returncode!=0:
        (RUN/'madai-likelihood-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');return 1
    p=subprocess.run([str(ROOT/c['binary'])],cwd=ROOT,capture_output=True,text=True);result['run']={'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr};assert p.returncode==0
    rows={}
    for line in p.stdout.splitlines():
        name,code,value,calls=line.split(',');rows[name]={'native_status':int(code),'log_value':float(value) if math.isfinite(float(value)) else value,'covariance_calls':int(calls)}
    val=lambda name:float(rows[name]['log_value'])
    checks={'native_success_statuses':all(x['native_status']==0 for x in rows.values()),'default_modelcov_not_consumed':rows['default_modelcov_off']['covariance_calls']==0 and abs(val('default_modelcov_off')+.5)<1e-14,'equal_zero_residual_different_cov_equal_native':val('zerores_totalvar1')==val('zerores_totalvar4')==0,'nonzero_residual_quadratic_only':abs(val('res1_totalvar1')+.5)<1e-14 and abs(val('res1_totalvar4')+.125)<1e-14,'custom_loglike_escape':abs(val('custom_log_likelihood')-(-.125-.5*math.log(4)))<1e-14,'prior_already_in_returned_value':abs(val('finite_uniform_prior')-(-.5-math.log(2)))<1e-14 and rows['out_of_prior']['log_value']=='-inf','invalid_negative_cov_is_finite_in_native':abs(val('invalid_negative_totalcov')-.5)<1e-14,'constant_cov_mean_ratio_control':abs(val('res2_totalvar4')-val('res1_totalvar4')+.375)<1e-14}
    native_difference=val('res1_totalvar4')-val('res1_totalvar1');normal_difference=native_difference-.5*math.log(4)
    result.update(rows=rows,checks=checks,observed_behaviour_checks_ok=all(checks.values()),varying_covariance_contrast={'native_log_ratio_var4_over_var1':native_difference,'normalizedGaussian_log_ratio_omitting_only_fixed2pi_constant':normal_difference,'native_ratio':math.exp(native_difference),'normalizedGaussian_ratio':math.exp(normal_difference),'ranking_reversed':native_difference>0 and normal_difference<0},scientific_contract='nativebasequadratic lacks variable logdet normalizer; constantSigma and explicitloglikelihood override are necessarycountercontrols',paper_application_unknown=True,experimental_CI_or_refit=False,original_source_hashes_unchanged=all(sha(ROOT/p)==h for p,h in c['source_hashes'].items()),binary_sha256=sha(ROOT/c['binary']),generated_at=datetime.now(timezone.utc).isoformat())
    (RUN/'madai-likelihood-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['observed_behaviour_checks_ok','varying_covariance_contrast','paper_application_unknown','original_source_hashes_unchanged']},ensure_ascii=False,indent=2));return 0 if result['observed_behaviour_checks_ok'] else 1
if __name__=='__main__':raise SystemExit(main())
