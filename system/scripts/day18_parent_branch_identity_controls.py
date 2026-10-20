#!/usr/bin/env python3
"""New typed-primary-input exercise: branch roles and conditional curvature.

Printed centers and deterministic controls only. No producer, covariance or CI.
"""
import argparse,hashlib,json,math
from pathlib import Path


def log_curvatures(values):
    return [math.log(a)-2*math.log(b)+math.log(c) for a,b,c in zip(values,values[1:],values[2:])]


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();c=json.loads(a.contract.read_text());checks=[]
    def check(name,ok,**evidence):
        checks.append({'name':name,'passed':bool(ok),**evidence});assert ok,name
    for src in c['sources']:check(src['source']+' raw hash',hashlib.sha256(Path(src['raw_file']).read_bytes()).hexdigest()==src['sha256'])
    k=1.225187e13/1.758366e13;pairs=[]
    for r in c['weak_parent_pairs']:
        label=r['band']+' '+r['spin']
        check(label+' dipole energy closure',abs(r['parent']-r['dip_final_Ex_keV']-r['dip_E'])<.25)
        check(label+' E2 energy closure',abs(r['parent']-r['e2_final_Ex_keV']-r['e2_E'])<.25)
        dip_role='in' if r['band']==r['dip_final_band'] else 'out';e2_role='in' if r['band']==r['e2_final_band'] else 'out'
        ratio=k*(r['e2_E']/1000)**5/(r['dip_E']/1000)**3*r['dip_I']/r['e2_I']
        check(label+' actual denominator is out of band',e2_role=='out')
        # The unknown lifetime and any common photon normalization cancel;
        # correct labels still cannot be changed from out to in.
        values=[]
        for tau in [.1,1.,10.]:
            bm=r['dip_I']/tau/(1.758366e13*(r['dip_E']/1000)**3)
            be=r['e2_I']/tau/(1.225187e13*(r['e2_E']/1000)**5)
            values.append(bm/be)
        check(label+' same-parent clock cancels',all(math.isclose(x,ratio,rel_tol=1e-12) for x in values))
        pairs.append({'parent_band':r['band'],'spin':r['spin'],'quantity':f'B(M1)_{dip_role}/B(E2)_{e2_role}','conditional_delta0_ratio':ratio,'conditional_delta1_ratio':ratio/2,'conditional_delta2_ratio':ratio/5,'ratio_unit':'muN2/(e2 b2)','can_replace_Fig6_in_over_in':False,'actual_delta_or_CI':None})
    check('two out/out and three in/out roles',sum(x['quantity']=='B(M1)_out/B(E2)_out' for x in pairs)==2 and sum(x['quantity']=='B(M1)_in/B(E2)_out' for x in pairs)==3)
    rh={}
    for nucleus,vals in c['suzuki'].items():
        m,e=vals['BM1'],vals['BE2'];ratio=[x/y for x,y in zip(m,e)];sm,se,sr=log_curvatures(m),log_curvatures(e),log_curvatures(ratio)
        check(nucleus+' exact log-ratio curvature identity',all(abs(z-(x-y))<1e-12 for x,y,z in zip(sm,se,sr)))
        check(nucleus+' monotonic M1 does not imply zero curvature',all(x>y for x,y in zip(m,m[1:])) and any(abs(x)>.01 for x in sm))
        rh[nucleus]={'spins':vals['spins'],'central_BM1_over_BE2':ratio,'log_curvature_BM1':sm,'log_curvature_BE2':se,'log_curvature_ratio':sr,'scope':'self-chosen second-log-difference diagnostic, not unique decomposition of physical staggering or a significance test'}
    br=c['br_this_letter_tau_matrix'];lookup={(r['band'],r['spin']):r for r in br}
    check('Br twenty printed this-Letter slots',len(br)==20)
    check('Br fifteen finite and five limits',sum(not r['upper_limit'] for r in br)==15 and sum(r['upper_limit'] for r in br)==5)
    check('Br1.79 assigned Band3 I7',lookup[3,7]['tau_ps_or_upper_cap']==1.79 and (2,7) not in lookup)
    check('Br no numerical central value substituted for limit',lookup[1,16]['upper_limit'] and lookup[3,11]['upper_limit'])
    tip=[dict(r,conditional_E2_fraction=r['delta']**2/(1+r['delta']**2)) for r in c['tip1_to_D1_known_delta_subset']]
    check('selected TiP subset has five distinct identities',len(tip)==5 and len({r['E_keV'] for r in tip})==5)
    check('selected TiP subset does not include inband410 or TiP2 518.3',all(r['E_keV'] not in [410.2,518.3] for r in tip))
    check('TiP missing AP is preserved',sum(r['AP_printed'] is None for r in tip)==1)
    br_delta=[dict(r,conditional_E2_fraction=r['delta']**2/(1+r['delta']**2)) for r in c['Br_SI_selected_delta_controls']]
    check('Br Band2 printed central exceptions to universal10percent',all(r['conditional_E2_fraction']>.1 for r in br_delta if r['from_band']==2))
    check('Br Band3 lowspin20percent example',math.isclose(br_delta[-1]['conditional_E2_fraction'],.2))
    out={'kind':'same-parent-role-and-central-diagnostic-not-experimental-fit','contract_sha256':hashlib.sha256(a.contract.read_bytes()).hexdigest(),'primed':True,'blind_test':False,'weak_pairs':pairs,'suzuki_central_curvature':rh,'Br_this_letter_tau_matrix':br,'TiP_selected_subset':tip,'TiP_selected_unweighted_E2_fraction_mean':sum(r['conditional_E2_fraction'] for r in tip)/len(tip),'TiP_subset_scope':'only five listed TiP1-to-D1 links with delta; not all links or complete polarization coverage','Br_SI_selected_fraction_controls':br_delta,'checks':checks,'valid':all(x['passed'] for x in checks),'independent_experiment_or_CI':False}
    a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'valid':out['valid'],'checks':len(checks),'weak_quantities':[x['quantity'] for x in pairs],'output':str(a.output)}))
if __name__=='__main__':main()
