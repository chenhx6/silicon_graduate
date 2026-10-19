#!/usr/bin/env python3
"""Thesis printed normalization and selection-rule audit, not a new measurement."""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib
import math

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    p=RUN/'saastamoinen2011-thesis-exercise-contract.json'
    c=json.loads(p.read_text())
    assert c['identity']=='SA11-THESIS-PROTON-GAMMA-ROLE-01'
    assert sha(ROOT/c['pdf'])==c['pdf_sha256']
    normal=c['I451_absolute_percent']/100
    snormal=c['I451_absolute_scale_percent']/100
    rows=[]
    for r in c['Table5p4']:
        absolute=r['relative']*normal
        scale=math.hypot(r['relative_scale']*normal,r['relative']*snormal)
        rows.append({**r,'absolute_percent_from_relative':absolute,
                     'conditional_scale_from_two_independent_printed_inputs':scale,
                     'nominal_absolute_residual_percent':absolute-r['absolute_percent']})
    values=[c['proton_relative_per100_I451'],*c['gamma_relative_per100_I451']]
    total=sum(values)
    fractions=[x/total for x in values]
    width=c['hbar_meV_fs']/c['tau_mean_fs_fixed']
    g=(2*c['J_fixed']+1)/((2*c['target_spin']+1)*(2*c['projectile_spin']+1))
    gp=width*fractions[0]
    gg=width*(1-fractions[0])
    omega=g*gp*gg/width
    assert abs(sum(fractions)-1)<1e-15
    # A physical common absolute-I451 scale cancels in the daughter branching.
    cancel=[[(scale*x)/sum(scale*y for y in values) for x in values] for scale in [.1,1,4]]
    assert all(max(abs(a-b) for a,b in zip(fractions,row))<1e-15 for row in cancel)
    # Allowed S from target3 and proton1/2, then allowed J from S and even L.
    channels=[]
    for L in [0,2,4]:
        for twice_s in [5,7]:
            allowed=[j/2 for j in range(abs(2*L-twice_s),2*L+twice_s+1,2)]
            channels.append({'L':L,'channel_spin':twice_s/2,'allowed_J':allowed})
    assert not any(1.5 in x['allowed_J'] for x in channels if x['L']==0)
    assert any(1.5 in x['allowed_J'] for x in channels if x['L']==2)
    rv=[x['relative'] for x in c['Table5p4']]
    common_cov=[[a*b*snormal**2 for b in rv] for a in rv]
    total_common_scale=sum(rv)*snormal
    assert abs(sum(sum(row) for row in common_cov)-total_common_scale**2)<1e-15
    result={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
            'contract_sha256':sha(p),'pdf_sha256':c['pdf_sha256'],'rows':rows,
            'absolute_beta_proton_percent':rows[0]['absolute_percent_from_relative'],
            'daughter_channel_fractions_from_printed_Fig5p7':fractions,
            'fixed_tau_J_width_control':{'Gamma_total_meV':width,'Gamma_p_meV':gp,
                'Gamma_gamma_meV':gg,'omega_gamma_meV':omega,
                'boundary':'fixed old mean tau/J and only listed p,gamma branches; no new widths or CI'},
            'Table5p4_total_printed_absolute_percent':sum(x['absolute_percent'] for x in rows),
            'Table5p4_total_from_relative_percent':sum(rv)*normal,
            'common_I451_only_covariance_percent_squared':common_cov,
            'total_common_I451_only_scale_percent':total_common_scale,
            'allowed_channel_angular_momenta':channels,
            'J3p2_evenL_is_allowed_not_forbidden':True,
            'no_new_experimental_spin_branch_lifetime_width_or_CI':True,'ok':True}
    (RUN/'saastamoinen2011-thesis-exercise-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['rows','common_I451_only_covariance_percent_squared']},ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
