#!/usr/bin/env python3
"""Thesis Ch4 input checks and declared transport scales; no source repair or fit."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp=RUN/'fougeres2022-thesis-ch4-exercise-contract.json';c=json.loads(cp.read_text())
    assert c['identity']=='F22-THESIS-CH4-GEOMETRY-INPUTS-01'
    assert sha(ROOT/c['pdf'])==c['pdf_sha256']
    p=ROOT/c['SRIM_beam_table'];assert sha(p)==c['table_sha256']
    rows=[]
    for no,line in enumerate(p.read_text().splitlines(),1):
        a=line.split()
        if len(a)>=4 and a[1] in ['eV','keV','MeV','GeV']:
            try:
                v=[float(a[k].replace(',','.')) for k in [0,2,3]]
                factor={'eV':.001,'keV':1,'MeV':1000,'GeV':1e6}[a[1]]
                rows.append({'line':no,'E_keV':v[0]*factor,'Se_keV_per_micron':v[1],'Sn_keV_per_micron':v[2]})
            except ValueError:pass
    energy=c['beam_energy_MeV']*1000;selected=None
    for a,b in zip(rows,rows[1:]):
        if a['E_keV']<=energy<=b['E_keV']:
            t=(energy-a['E_keV'])/(b['E_keV']-a['E_keV'])
            sp=sum((1-t)*a[x]+t*b[x] for x in ['Se_keV_per_micron','Sn_keV_per_micron'])
            selected={'bracket':[a,b],'linear_Se_plus_Sn_keV_per_micron':sp,
                      'constant_SP_loss_over_active_depth_MeV':sp*c['active_depth_micron']/1000}
            break
    assert selected
    beta=c['beta_declared'];tau=c['tau_mean_fs_declared'];gamma=1/math.sqrt(1-beta**2)
    v=beta*c['c_micron_per_fs'];meanpath=v*gamma*tau
    d=c['remaining_foil_micron_declared'];minlab=d/v
    survival=math.exp(-minlab/(gamma*tau))
    gapmicron=c['reported_gap_mm']*1000
    assert gapmicron==c['input_gap_micron']
    out={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':sha(Path(__file__)),
         'contract_sha256':sha(cp),'geometry_mm_to_micron_matches_public_input':True,
         'public_gap_is_supported_by_actual_thesis':True,
         'table_query':selected,'thesis_reported_beam_loss_MeV':c['reported_loss_MeV'],
         'nominal_lookup_minus_thesis_loss_MeV':selected['constant_SP_loss_over_active_depth_MeV']-c['reported_loss_MeV'],
         'Table4p1_printing_control_keV':c['Table4p1_fraction']*c['Doppler_E_keV_declared'],
         'declared_constant_beta_proper_mean_control':{'beta':beta,'proper_tau_fs':tau,
              'gamma':gamma,'mean_lab_path_micron':meanpath,'time_to_remaining_foil_fs':minlab,
              'survival_to_exit_firstfoil_if_beta_fixed':survival,
              'log_survival_to_traverse_gap_if_beta_fixed':-gapmicron/v/(gamma*tau),
              'boundary':'fixed hypothetical kinematics/mean only; no experimental CI, full slowing/long-lived benchmark not replayed'},
         'no_new_experimental_lifetime_response_or_CI':True,'ok':True}
    (RUN/'fougeres2022-thesis-ch4-exercise-result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':raise SystemExit(main())
