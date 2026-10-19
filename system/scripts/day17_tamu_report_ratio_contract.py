#!/usr/bin/env python3
"""Actual lab-report ratios/time label printing audit, not an experimental refit."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math
ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'tamu2006-2007-report-exercise-contract.json';c=json.loads(path.read_text())
    assert c['identity']=='TAMU06-07-DOUBLETRATIO-LABEL-01'
    for p,h in c['pdfs'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    r=c['r_proton_over_gamma'];b=r/(1+r);sb=c['r_scale']/(1+r)**2
    g=(2*c['fixed_J']+1)/14
    omega=lambda tau:g*c['hbar_meV_fs']/tau*b*(1-b)
    mean=omega(c['printed_time_fs']);literalhalf=omega(c['printed_time_fs']/math.log(2))
    gs=c['gamma_ratios'];fractions=[x/sum(gs) for x in gs]
    result={'at':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'proton_over_gamma_r':r,'daughter_Bp_from_r':b,'local_scale_from_r_only':sb,
            'omega_if_mean10_meV':mean,'omega_if_literal_half10_meV':literalhalf,
            'reported_omega_meV':c['reported_omega_meV'],
            'three_listed_photon_fractions':fractions,
            'matches_S11_old_reference_branch_printing':[round(100*x,1) for x in fractions],
            'literal_time_label_not_reconciled_by_edit':True,
            'absolute_gamma_feed_3p95_not_recovered':True,
            'no_new_experimental_branch_tau_spin_or_CI':True,'ok':True}
    (RUN/'tamu2006-2007-report-exercise-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0


if __name__=='__main__':raise SystemExit(main())
