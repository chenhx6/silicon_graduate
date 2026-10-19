#!/usr/bin/env python3
"""Published attenuation/geometry and comparison arithmetic; no centroid refit."""
from pathlib import Path
import hashlib,json,math
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    p=RUN/'schuermann2008-attenuation-contract.json';c=json.loads(p.read_text());assert c['identity']=='SCH08-ATTENUATION-GEOMETRY-COMPARISON-01'
    for f,h in c['source_hashes'].items():assert sha(ROOT/f)==h,f
    P=c['finite_detector_Doppler_P'];F=c['F6792'];ratio=P*F;geom={'source_equation':'F=Delta/(Delta_full*P)','P_role':'finite-detector Doppler correction, not linear polarization','Delta_over_Delta_full_if_source_centers':ratio,'apparent_F_if_P_incorrectly_set_one':ratio,'apparent_minus_source_F':ratio-F,'relative_factor_if_P_omitted':P-1,'correction_ratio_1_over_P':1/P,'scope':'conditionalmappingofsourcecenters; nooriginalDeltaCov or lifetimebias recovered'}
    comparisons=[]
    for row in c['tableI_secondaries']:
        difference=row['F_new']-row['F_old'];sd=math.hypot(row['sigma_F_new'],row['sigma_F_old']);a={'E_keV':row['E_keV'],'difference':difference,'Z_if_independent_reported_scales_are_SD':difference/sd,'Z_if_old_central_is_fixed_new_only_scale':difference/row['sigma_F_new'],'not_original_profile_significance_or_CI':True}
        if 'tau_new' in row:
            a['lifetime_center_difference']=row['tau_new']-row['tau_old'];a['lifetime_Z_if_independent_SD']=(row['tau_new']-row['tau_old'])/math.hypot(row['sigma_tau_new'],row['sigma_tau_old'])
        comparisons.append(a)
    width=c['hbar_eV_s']/(c['tau_upper_fs']*1e-15)
    assert abs(width-.85)<.005
    assert abs(geom['apparent_minus_source_F']+.01287)<1e-12
    result={'identity':c['identity'],'script_sha256':sha(__file__),'contract_sha256':sha(p),'source_tableI':c['tableI_all'],'source_tableII_reused_F':c['tableII'],'geometry_mapping':geom,'conditional_summary_contrasts':comparisons,'width_conversion':{'source_tau_upper_fs':c['tau_upper_fs'],'hbar_over_tau_lower_eV':width,'author_calls_Gamma_gamma_lower_eV':.85,'boundary':'formula gives totalwidth; authorradiative interpretation/inventory separate; doesnotupgrade source1sigma-limitlanguage to90percentCI'},'assumptions':c['assumptions'],'original_centroids_cov_or_stopping_polynomial_recovered':False,'experimental_refit_or_new_CI':False,'ok':True,'generated_at':datetime.now(timezone.utc).isoformat()};(RUN/'schuermann2008-attenuation-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['geometry_mapping','conditional_summary_contrasts','width_conversion','ok']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
