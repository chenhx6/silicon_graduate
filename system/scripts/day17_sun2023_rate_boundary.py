#!/usr/bin/env python3
"""Check model-subtracted M1 rate and a conditional width, not a data refit."""
from pathlib import Path
import hashlib,json,math
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=RUN/'sun2023-rate-contract.json';c=json.loads(p.read_text());assert c['identity']=='SUN23-MODEL-SUBTRACTED-RATE-01'
    for path,h in c['source_hashes'].items():assert sha(ROOT/path)==h,path
    t,e,s=c['tau_mean_ps'],c['tau_E2_USDB_model_ps'],c['tau_reported_scale_ps'];tau_M=t*e/(e-t);rate_M=1e12*(1/t-1/e);der_t=1/(1-t/e)**2;der_e=-t*t/(e-t)**2;sig_cond=abs(der_t)*s
    B=c['modern_C_M1']/(tau_M*c['E_gamma_rounded_MeV']**3);sigB=B*sig_cond/tau_M;rme=math.sqrt((c['Ji2']+1)*B)
    assert t>0 and e>t and tau_M>t and rate_M>0
    assert abs(1/t-(1/tau_M+1/e))<1e-15
    exact=Fraction(28,25)*Fraction(69,10)/(Fraction(69,10)-Fraction(28,25));assert abs(float(exact)-tau_M)<1e-14
    width_meV=c['hbar_eV_s']/(c['illustrative_tau_fs']*1e-15)*1000
    result={'identity':c['identity'],'script_sha256':sha(__file__),'contract_sha256':sha(p),'author_reported':c['author_reported'],'conditional_model_subtracted':{'tau_M1_ps':tau_M,'tau_M1_exact_from_printed':str(exact),'rate_M1_s-1':rate_M,'E2_photon_rate_fraction_at_central':t/e,'d_tauM_d_tau':der_t,'d_tauM_d_model_tauE2':der_e,'conditional_linear_sigma_tauM_ps_model_fixed':sig_cond,'B_M1_muN2':B,'conditional_linear_sigma_B_model_fixed':sigB,'RME_abs_muN':rme},'conditional_width_conversion':{'illustrative_tau_fs':c['illustrative_tau_fs'],'Gamma_total_meV_if_tau_below_value':width_meV,'not_reported_finite_90percent_bound_on6390':True},'jacobian_covariance_formula':'Var(tauM)=a^2 Var(t)+b^2 Var(e)+2ab Cov(t,e); model e uncertainty not supplied','scope':c['assumptions'],'no_experimental_refit_or_new_CI':True,'ok':True};(RUN/'sun2023-rate-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
