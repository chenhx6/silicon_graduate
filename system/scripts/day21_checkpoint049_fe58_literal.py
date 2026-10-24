#!/usr/bin/env python3
"""WO26 literal phase ledger, Doppler normalization and lifetime centers."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def main():
    # Visually transcribed from arXiv v1 PDF p.8 Table VII.
    rows = [("+++",46.78,.509,22,2),("++-",38.56,.571,27,3),
            ("+-+",41.75,.543,25,2),("+--",42.74,.545,25,3),
            ("-++",70.57,.474,19,2),("-+-",46.69,.531,24,2),
            ("--+",53.24,.505,21,2),("---",51.94,.502,21,2)]
    phases = [dict(signs=p,chi2=c,RME_eb=m,BE2_Wu=b,printed_error_Wu=e,
                   excluded_by_authors_95percent_rule=p=='-++') for p,c,m,b,e in rows]
    retained = [x for x in phases if not x['excluded_by_authors_95percent_rule']]
    f = 3.55/(1266*.01226)
    tau_updates = [dict(state='2_2+ (1675 keV)',old_ps=2.30,new_ps=2.4,ratio=2.4/2.30),
                   dict(state='4_1+ (2077 keV)',old_ps=.54,new_ps=.66,ratio=.66/.54)]
    checks = {'eight_distinct_literal_phase_rows':len({x['signs'] for x in phases})==8,
              'retained_nominal_range_21_to_27':min(x['BE2_Wu'] for x in retained)==21 and max(x['BE2_Wu'] for x in retained)==27,
              'one_author_exclusion_not_unique_solution':len(retained)==7,
              'F_tau_matches_printed_rounding':abs(f-.229)<.0005,
              'nominal_lifetime_update_factors_differ':abs(tau_updates[0]['ratio']-tau_updates[1]['ratio'])>.1}
    raw='raw/papers/2026_Woodside_Fe58_collectivity_Coulex_Dsam.pdf'
    out=dict(raw_sha256=hashlib.sha256((ROOT/raw).read_bytes()).hexdigest(),
             phase_rows=phases,phase_source='PDF p.8 Table VII; author exclusion paragraph',
             F_2077=dict(value=f,deltaE_keV=3.55,Egamma_keV=1266,delta_mean_beta_cos=.01226,locator='PDF p.11 Table VIII'),
             lifetime_center_updates=tau_updates,
             electronic_scaling={'Mn':.608,'Ta':.515,'nuclear_scaled':False},
             checks=checks,new_fit=False,new_experimental_CI=False,
             statistical_scope='Printed chi2 values retained; no new threshold, likelihood ratio, posterior weights, phase average or experimental significance.',
             missing=['matching yields/response and Gosia weights/job','fit excluding target lifetime constraint','original DSAM listing/logbook and covariance'])
    (RUN/'fe58-literal-scope-049.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':checks,'F_2077':f,'new_experimental_CI':False}))
    return 0 if all(checks.values()) else 1


if __name__=='__main__':
    raise SystemExit(main())
