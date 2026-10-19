#!/usr/bin/env python3
"""Audit official S31 fixed fields and alternative rate inputs, not a new fit."""
from pathlib import Path
import json,hashlib,math
from datetime import datetime,timezone
from day17_pb207_reference_audit import records,value_sigma
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    path=RUN/'s31-mixing-contract.json';c=json.loads(path.read_text());assert c['identity']=='S31-OFFICIAL-MIXING-COMPANION-01'
    assert sha(ROOT/c['parser_helper'])==c['parser_helper_sha256']
    d={}
    for name,p in c['source_paths'].items():assert sha(ROOT/p)==c['source_hashes'][name];d[name]=records(ROOT/p)
    selected={}
    for name,obj in d.items():
        g=[g for g in obj['gammas'] if g['energy']['value'] and 1247<g['energy']['value']<1251 and g['parent'] and 1247<g['parent']['energy']['value']<1251];assert len(g)==1;g=g[0];assert g['MR']['text']=='+0.35' and abs(g['MR']['sigma']-.02)<1e-14
        raw_t,unit=g['parent']['half_life_field'].split();parsed=value_sigma(raw_t,g['parent']['half_life_uncertainty_field']);assert unit=='PS' and parsed['value']==.5 and parsed['sigma']==.12
        selected[name]={'gamma':g,'level_field_half_life':g['parent']['half_life_field'],'parsed_half_life_ps':parsed,'mean_tau_from_printed_half_life_ps':parsed['value']/math.log(2),'mean_tau_sigma_from_printed_half_life_scale_ps':parsed['sigma']/math.log(2)}
    t=c['Sun_total_mean_tau_ps'];em=c['Sun_USDB_E2_partial_tau_ps'];model_f=t/em;modeldelta=math.sqrt(t/(em-t));small=c['MR_small'];big=c['MR_large_comment'];rows=[]
    for label,delta in [('official_small_MR',small),('official_large_alternative_comment',big),('Sun_model_rate_equivalent_absdelta',modeldelta)]:
        fE=delta*delta/(1+delta*delta);tm=t*(1+delta*delta);te=t*(1+delta*delta)/(delta*delta);bM=c['modern_C_M1']/(tm*c['rounded_E_MeV']**3);bE=c['modern_C_E2']/(te*c['rounded_E_MeV']**5)
        assert abs(1/t-(1/tm+1/te))<1e-14
        rows.append({'input':label,'absdelta_for_rates':delta,'E2_photon_rate_fraction':fE,'M1_partial_tau_ps_conditional':tm,'E2_partial_tau_ps_conditional':te,'B_M1_muN2_conditional':bM,'B_E2_e2b2_conditional':bE,'not_a_new_measured_MR_or_posterior_CI':True})
    oldmean=.5/math.log(2);small_fraction=small*small/(1+small*small);fractionderivative=2*small/(1+small*small)**2
    cc=c['selected_CC_smallroot'];summed=cc['KC']+cc['LC']+cc['MC']+cc['IPC'];assert abs(cc['CC']-summed)<5e-8
    assert sha(ROOT/c['xundl_path'])==c['xundl_sha256']
    xd=records(ROOT/c['xundl_path']);compiled=[]
    input_tau={1248:(1120.,False),2234:(250.,False),3076:(11.,True),3435:(16.,True),4971:(7.,True),5156:(15.,True)}
    for level in xd['levels']:
        e=level['energy']['value']
        if e not in input_tau:continue
        value,unit=level['half_life_field'].split();unitfactor={'PS':1000.,'FS':1.}[unit];actual=float(value)*unitfactor;mean,upper=input_tau[e]
        assert (level['half_life_uncertainty_field']=='LT')==upper
        compiled.append({'energy':e,'level_line':level['line'],'T_field':level['half_life_field'],'DT_field':level['half_life_uncertainty_field'],'nominal_source_mean_tau_fs':mean,'converted_mean_tau_ln2_fs':mean*math.log(2),'compiled_half_life_fs':actual,'central_residual_fs':actual-mean*math.log(2),'not_new_lifetime_or_original_rounding_rule':True})
    l6390=[z for z in xd['levels'] if z['energy']['value']==6390][0];assert l6390['half_life_field']==''
    branches=[z for z in xd['gammas'] if z['parent'] and z['parent']['energy']['value']==3435];assert sorted(g['intensity']['value'] for g in branches)==[38,62]
    old2010=[]
    for row in c['Doornenbal2010_printed_half_life_summaries']:
        old2010.append({**row,'mean_tau_ps_from_half_life':row['T_half_ps']/math.log(2),'plus_scale_if_stat_syst_quadrature':math.hypot(row['stat_ps'],row['syst_plus_ps'])/math.log(2),'minus_scale_if_stat_syst_quadrature':math.hypot(row['stat_ps'],row['syst_minus_ps'])/math.log(2),'not_new_independent_measurement_or_original_Cov':True})
    result={'identity':c['identity'],'script_sha256':sha(__file__),'contract_sha256':sha(path),'selected_same_parent_records':selected,'conditional_rate_comparison':rows,'officialMR_to_model_bridge':{'source_MR_small':small,'source_MR_sigma':c['sigma_MR_small'],'model_subtracted_E2_fraction':model_f,'model_rate_equivalent_absdelta':modeldelta,'native_sign_or_phase_identified':False,'fraction_sigma_local_if_only_MR_varies':fractionderivative*c['sigma_MR_small'],'not_difference_over_SD_significance':True},'mean_vs_half_life':{'official_half_life_ps':.50,'official_scale_ps':.12,'converted_mean_tau_ps':oldmean,'converted_scale_ps':.12/math.log(2),'quoted_reaction_comment_mean_fs':720,'Sun_mean_tau_ps':t,'same_1971En02_as_Sun_literature_comparison':True,'no_new_measurement_from_unit_conversion':True},'2010_same_paper_detector_summaries_conditional_conversion':old2010,'selected_smallroot_CC_arithmetic':{'source':cc,'K_L_M_IPC_sum':summed,'CC_minus_components':cc['CC']-summed,'fixed_CC_M1_scaling_1_over_1plusCC':1/(1+cc['CC']),'not_reused_for_alternative_delta_or_as_new_measured_Cov':True},'XUNDL_samepaper_compilation':{'source_hash':c['xundl_sha256'],'compiled_lifetime_rows':compiled,'6390_lifetime_field_is_blank':True,'3435_gamma_branch_rows':branches,'not_independent_of_Sun_experiment':True,'not_attestation_of_finalVORbody':True},'input_layer_boundaries':c['assumptions'],'ok':True,'new_experimental_strength_CI_or_delta_fit':False,'actual_Sun_response_producer_or_A2_frame_recovered':False,'generated_at':datetime.now(timezone.utc).isoformat()};(RUN/'s31-mixing-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['conditional_rate_comparison','officialMR_to_model_bridge','mean_vs_half_life','ok']},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
