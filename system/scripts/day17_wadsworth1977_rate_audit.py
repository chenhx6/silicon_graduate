#!/usr/bin/env python3
"""Conditional actual-branch check of WA77 Table4, preserving units and scope."""
import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    path=RUN/'wadsworth1977-rate-contract.json'
    c=json.loads(path.read_text())
    assert sum(c['all_gamma_branch_percent'])==100
    tau_ps=c['tau_fs']/1000
    radius=1.2*c['A']**(1/3)
    wu_e2_fm4=(3/5)**2*radius**4/(4*math.pi)
    wu_m1_mu2=(10/math.pi)*(3/4)**2
    result=[]
    for row in c['selected_branches']:
        e=row['Eg_keV']/1000
        d2=row['delta_E2_over_M1']**2
        bm=.0569*row['gamma_branch']/(tau_ps*e**3*(1+d2))
        be=.0816*row['gamma_branch']*d2/(tau_ps*e**5*(1+d2))
        recovered=(.0569/.0816)*e*e*be/bm
        assert abs(recovered-d2)<1e-16
        result.append({'Ef_keV':row['Ef_keV'],'BM1_muN2':bm,'BE2_e2b2':be,
                       'BM1_milliWU_in_declared_units':1000*bm/wu_m1_mu2,
                       'BE2_WU_in_declared_units':be*10000/wu_e2_fm4,
                       'reported_E2_WU':row['reported_E2_WU'],
                       'reported_M1_milliWU':row['reported_M1_milliWU'],
                       'not_tuned_to_close_reported_central_values':True})
    out={'at':datetime.now(timezone.utc).isoformat(),
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'contract_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'tau_fs_to_ps':tau_ps,'declared_Weisskopf_E2_e2fm4':wu_e2_fm4,
         'declared_Weisskopf_M1_muN2':wu_m1_mu2,'selected_branch_results':result,
         'wrong_37fs_would_multiply_both_strengths_by':c['tau_fs']/37,
         'Table4_908_lifetime_unit_bridge':{'fs':1600,'ps':1.6,'ns':.0016},
         'source_abstract_908_1500pm400fs_vs_Table4_1600pm500fs_retained':True,
         'same_photon_delta_magnitude_relation_control':True,
         'no_IC_delta_branch_Cov_fitted_or_invented':True,
         'no_new_experimental_Jpi_delta_tau_B_or_CI':True,'ok':True}
    (RUN/'wadsworth1977-rate-result.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
