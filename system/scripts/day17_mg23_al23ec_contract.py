#!/usr/bin/env python3
"""Audit real official Al23EC normalization fields and role-specific energy mapping."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math
from day17_pb207_reference_audit import records
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp=RUN/'mg23-al23ec-exercise-contract.json';c=json.loads(cp.read_text())
    assert c['identity']=='M23-AL23EC-NORMALIZATION-01'
    assert sha(ROOT/c['parser'])==c['parser_sha256']
    p=ROOT/c['data'];assert sha(p)==c['data_sha256']
    d=records(p);n=d['normalization'][0]
    assert n['NR']['value'] is None and n['BR']['value']==n['NB']['value']==1
    g451=[g for g in d['gammas'] if g['parent'] and g['parent']['energy']['value']==451][0]
    gs=[g for g in d['gammas'] if g['parent'] and g['parent']['energy']['value']==7788]
    assert g451['intensity']['value']==100 and len(gs)==3
    gamma_values=[g['intensity']['value'] for g in gs]
    gamma_fractions=[x/sum(gamma_values) for x in gamma_values]
    ec=[x for x in d['ec'] if x['parent'] and x['parent']['energy']['value']==7788][0]
    total=sum(x['TI']['value'] or 0 for x in d['ec'])
    assert total<100 and ec['TI']['value']==4.89
    lines=p.read_text().splitlines()
    assert '1.53' in lines[134] and '1.53' in lines[136]
    mp,mna=c['atomic_masses_u'];factor=(mp+mna)/mna
    energy=[{'emitted_proton_lab_keV':a,'compiled_CM_keV':b,'derived_CM_keV':a*factor,
             'nominal_residual_keV':a*factor-b} for a,b in [(558.2,583.8),(828.8,866.8)]]
    assert all(abs(x['nominal_residual_keV'])<.05 for x in energy)
    # Conditional shared physical I451 normalization: p=a*r*relative866, gamma=a*G.
    rr,ref,grel=c['ratio204over866'],c['I866_per100I451'],c['declared_gamma_relative_sum']
    scales=[.2,.433,.7]
    bps=[(a*rr*ref)/(a*rr*ref+a*grel) for a in scales]
    assert max(bps)-min(bps)<1e-16
    out={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
         'contract_sha256':sha(cp),'data_sha256':sha(p),'normalization':n,'gamma451':g451,
         'three_key_parent_gamma_records':gs,'listed_photon_fractions':gamma_fractions,
         'key_parent_EC_record':ec,'sum_listed_EC_TI_percent':total,
         'gap_to100_not_assigned_to_any_unobserved_branch':100-total,
         'duplicate_1p53_comments_preserved':True,
         'two_lab_energy_roles':{'mass_factor':factor,'beta_delayed_proton_decay_CM_rows':energy,
              'capture_lab_to_CM_factor':1/factor,'capture_lab_for_Ecm206keV':206*factor,
              'emitted_proton_lab_for_total_decay206keV':206/factor,
              'boundary':'declared NR use of exact printed masses; gamma/recoil/beta-sum measurement response not recovered'},
         'conditional_common_absolute_I451_cancellation':{'scales':scales,'daughter_Bp':bps,
              'boundary':'only a hypothetical common multiplicative physical normalization; relative inventory/efficiency/feeding uncertainties remain'},
         'absolute_feed_and_fullCov_not_recovered':True,
         'no_new_experimental_branch_spin_tau_or_CI':True,'ok':True}
    (RUN/'mg23-al23ec-exercise-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ['normalization','gamma451','three_key_parent_gamma_records','key_parent_EC_record']},ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':raise SystemExit(main())
