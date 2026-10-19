#!/usr/bin/env python3
"""Audit selected official Pb207 fixed fields and conditional calibration dependencies."""
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
import math

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def value_sigma(value,uncertainty):
    text=value.strip()
    if not text:return {'text':'','value':None,'sigma':None,'sign_marker':'blank'}
    number=Decimal(text);sigma=float(Decimal(uncertainty.strip())*(Decimal(10)**number.as_tuple().exponent)) if uncertainty.strip().isdigit() else None
    return {'text':text,'value':float(number),'sigma':sigma,'sign_marker':text[0] if text[0] in '+-' else 'unspecified'}


def records(path):
    result={'levels':[],'gammas':[],'ec':[],'normalization':[]};parent=None
    for no,line in enumerate(path.read_text().splitlines(),1):
        if len(line)<9 or line[5:7]!='  ':continue
        kind=line[7]
        base={'line':no,'raw':line}
        if kind=='L':
            parent={**base,'energy':value_sigma(line[9:19],line[19:21]),'Jpi':line[21:39].strip(),'half_life_field':line[39:49].strip(),'half_life_uncertainty_field':line[49:55].strip()};result['levels'].append(parent)
        elif kind=='G':
            result['gammas'].append({**base,'parent':parent,'energy':value_sigma(line[9:19],line[19:21]),'intensity':value_sigma(line[21:29],line[29:31]),'M':line[31:41].strip(),'MR':value_sigma(line[41:49],line[49:55]),'CC':value_sigma(line[55:62],line[62:64]),'placement_tail':line[64:]})
        elif kind=='E':
            result['ec'].append({**base,'parent':parent,'IB':value_sigma(line[21:29],line[29:31]),'IE':value_sigma(line[31:39],line[39:41]),'TI':value_sigma(line[64:74],line[74:76])})
        elif kind=='N':
            result['normalization'].append({**base,'NR':value_sigma(line[9:19],line[19:21]),'NT':value_sigma(line[21:29],line[29:31]),'BR':value_sigma(line[31:39],line[39:41]),'NB':value_sigma(line[41:49],line[49:55])})
    return result


def main():
    inp=RUN/'pb207-reference-audit-input.json';d=json.loads(inp.read_text());objects={}
    for name,path in d['source_paths'].items():
        p=ROOT/path;assert sha(p)==d['source_hashes'][name];objects[name]=records(p)
    selected={}
    for name,obj in objects.items():
        selected[name]={}
        for label,target,parent_energy in [('gamma570',569.698,569.7),('gamma1064',1063.656,1633.36)]:
            matches=[g for g in obj['gammas'] if g['energy']['value'] is not None and abs(g['energy']['value']-target)<.01 and g['parent'] and abs(g['parent']['energy']['value']-parent_energy)<.1]
            assert len(matches)==1,(name,label,matches);selected[name][label]=matches[0]
        selected[name]['normalization']=obj['normalization']
    ec=selected['bi207ec'];g570,g1064=ec['gamma570'],ec['gamma1064'];x=d['inputs'];a=x['alpha570'];sa=x['sigma_alpha570'];b=x['N_bypass_source_literal'];sb=x['sigma_bypass_declared'];normal=100-b
    literal_ri=normal/(1+a);d_alpha=-normal/(1+a)**2;d_bypass=-1/(1+a)
    var_ri=(d_alpha*sa)**2+(d_bypass*sb)**2;cov_ri_alpha=d_alpha*sa**2
    total=literal_ri*(1+a);var_total_joint=((1+a)*d_alpha+literal_ri)**2*sa**2+((1+a)*d_bypass)**2*sb**2
    var_total_if_independent=(1+a)**2*var_ri+literal_ri**2*sa**2
    ri1064=x['RI1064']/100;pair_probability=ri1064/(1+a);marginal_product=ri1064*g570['intensity']['value']/100
    delta=x['MR1064'];sigma_delta=x['sigma_MR1064'];fraction=lambda z:z*z/(1+z*z);interference=lambda z:2*z/(1+z*z)
    other_lines=[g for g in objects['adopted']['gammas'] if g['energy']['value'] is not None and abs(g['energy']['value']-1063.656)<1 and g['parent'] and g['parent']['energy']['value']>2397.5]
    checks={'exact_target_roles_unique':True,'explicit_positive_MR_not_empty':all(obj['gamma1064']['MR']['text']=='+0.02' and abs(obj['gamma1064']['MR']['sigma']-.01)<1e-12 for obj in selected.values()),'E2_MR_is_blank_not_zero':all(obj['gamma570']['MR']['value'] is None for obj in selected.values()),'source_N_NR_BR_one':ec['normalization'][0]['NR']['value']==1 and ec['normalization'][0]['BR']['value']==1,'literal_RI570_printed_last_digit_compatible':abs(literal_ri-g570['intensity']['value'])<.005,'conditional_total_identity':abs(total-normal)<1e-12,'conditional_covariance_cancels_alpha_in_total':abs(var_total_joint-sb**2)<1e-16,'derived_RI_alpha_covariance_PSD':var_ri*sa**2-cov_ri_alpha**2>=-1e-20,'conditional_pair_probability_physical':0<pair_probability<ri1064<1,'near_energy_other_parent_not_in_EC':bool(other_lines) and not any(g['parent'] and g['parent']['energy']['value']>2397.5 for g in objects['bi207ec']['gammas'])}
    result={'script_sha256':sha(Path(__file__)),'input_sha256':sha(inp),'source_hashes':d['source_hashes'],'selected_records':selected,'other_near1064_adopted_records':other_lines,'conditional_normalization_exercise':{'source_formula':'RI570=(100-0.131)/(1+alpha570)','declared_primitive_independence':d['assumptions'],'literal_RI570':literal_ri,'sigma_RI570_conditional':math.sqrt(var_ri),'cov_RI570_alpha570':cov_ri_alpha,'total_transition_yield':total,'sigma_total_with_derived_covariance':math.sqrt(var_total_joint),'sigma_total_if_RI_alpha_incorrectly_independent':math.sqrt(var_total_if_independent),'reported_RI570':g570['intensity']},'conditional_photon_pair_exercise':{'p_gamma570_given_gamma1064':1/(1+a),'p_both_photons_per_parent_from_EC_record':pair_probability,'product_of_marginal_singles_probabilities':marginal_product,'upper_total_transition_yield_per100':x['RI1064']*(1+x['alpha1064']),'source_EC_feed_upper':next(e['IE'] for e in objects['bi207ec']['ec'] if e['parent'] and abs(e['parent']['energy']['value']-1633.358)<.01),'boundary':'emission probability in selected cascade, not actual detector coincidence efficiency or complete feed/response/covariance replay'},'mixing_amplitude_design_boundary':{'source_delta':delta,'source_sigma_delta':sigma_delta,'upper_multipole_intensity_fraction':fraction(delta),'fraction_at_nominal_delta_plus_minus_one_sigma':[fraction(delta-sigma_delta),fraction(delta+sigma_delta)],'bilinear_interference_coefficient':interference(delta),'coefficient_at_nominal_delta_plus_minus_one_sigma':[interference(delta-sigma_delta),interference(delta+sigma_delta)],'boundary':'coefficients only; not a bound or CI on gated P. Native/operator/first-last convention and actual acceptance must be established before predicting P.'},'checks':checks,'ok':all(checks.values()),'experimental_P_or_CI_inferred':False,'generated_at':datetime.now(timezone.utc).isoformat()}
    (RUN/'pb207-reference-audit-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['selected_records','other_near1064_adopted_records']},ensure_ascii=False,indent=2));return 0 if result['ok'] else 1


if __name__=='__main__':raise SystemExit(main())
