#!/usr/bin/env python3
"""Audit six printed finite-stop corrections and conditional relative Qt response."""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--contract',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();d=json.loads(a.contract.read_text());rows={}
    actual_hash=hashlib.sha256(Path(d['source_raw']).read_bytes()).hexdigest()
    if actual_hash != d['source_sha256']:
        raise ValueError('source identity differs from frozen contract')
    for x in d['rows']:
        t,c,q=map(F,[x['standard_tau_ps'],x['corrected_tau_ps'],x['Qt_eb']])
        delta=c-t
        half=t+delta/2
        rows[x['state']]={**x,'delta_tau_ps':float(delta),'corrected_over_standard':float(c/t),
            'exact_corrected_over_standard':str(c/t),'half_chart_tau_ps':float(half),
            'B_half_over_adopted_fixed_inventory':float(c/half),
            'Qt_half_over_adopted_fixed_geometry':math.sqrt(float(c/half))}
    comparisons=[]
    for top,base in d['comparisons']:
        r,s=rows[top],rows[base]
        t,c,q=map(F,[r['standard_tau_ps'],r['corrected_tau_ps'],r['Qt_eb']])
        u,v,z=map(F,[s['standard_tau_ps'],s['corrected_tau_ps'],s['Qt_eb']])
        ratio=q/z
        # The ratio is monotonic in f: derivative sign of (u+f(v-u))/(t+f(c-t)).
        derivative=(v-u)*t-(c-t)*u
        factor=(c/((t+c)/2))/(v/((u+v)/2))
        comparisons.append({'states':[top,base],'adopted_Qt_ratio':float(ratio),
            'half_chart_Qt_ratio':float(ratio)*math.sqrt(float(factor)),
            'half_over_adopted_B_ratio_factor_exact':str(factor),
            'relative_Qt_ratio_change':math.sqrt(float(factor))-1,
            'derivative_sign_for_squared_ratio_vs_f':(derivative>0)-(derivative<0),
            'endpoints_bound_chart_not_CI':True})
    exact_factors=[F(x['exact_corrected_over_standard']) for x in rows.values()]
    out={'scope':d['scope'],'contract_sha256':hashlib.sha256(a.contract.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'chart':d['declared_chart'],'rows':list(rows.values()),'comparisons':comparisons,
        'common_multiplicative_tau_correction_matches_all_printed_centers':len(set(exact_factors))==1,
        'ratio_factor_range':[float(min(exact_factors)),float(max(exact_factors))],
        'no_original_fit_or_Cov_recovered':True,'no_Ag106_lifetime_data':True,
        'actual_source_hash':actual_hash}
    a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'rows':len(rows),'common_scale':out['common_multiplicative_tau_correction_matches_all_printed_centers'],'factor_range':out['ratio_factor_range'],'comparisons':comparisons},ensure_ascii=False))


if __name__=='__main__':
    main()
