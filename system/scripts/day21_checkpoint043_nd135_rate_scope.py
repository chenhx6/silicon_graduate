#!/usr/bin/env python3
"""Published Table I central arithmetic, not a refit or experimental CI."""
import hashlib
import json
import math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def main():
    # Manual transcription, visually checked against printed 172501-2 Table I.
    # Tuples: 2I, tauA, tauB, BA, BB, sigmaBA, sigmaBB.
    data=[(31,.75,1.46,.32,.28,.03,.03),
          (33,.44,.87,.32,.28,.03,.03),
          (35,.28,.64,.32,.28,.03,.04),
          (37,.23,.48,.32,.29,.04,.04),
          (39,.22,.24,.13,.11,.03,.03)]
    rows=[]
    for spin,ta,tb,ba,bb,sa,sb in data:
        rows.append({'spin':str(spin)+'/2-', 'tau_A_ps':ta,'tau_B_ps':tb,
                     'BE2_A_e2b2':ba,'BE2_B_e2b2':bb,
                     'tau_B_over_A':tb/ta,'BE2_B_over_A':bb/ba,
                     'same_input_rate_identity_factor':bb/ba*tb/ta,
                     'factor_scope':'q_E2,B/q_E2,A * (E_A/E_B)^5 if transition identities and rate convention match; no separate q or E extraction',
                     'locator':'printed 172501-2 Table I'})
    # Conditional covariance design: only if the printed uncertainties can be
    # treated as marginal standard deviations. No fitted rho or experiment CI.
    difference=.28-.32
    covariance_sweep=[]
    for rho in [-1,0,.5,.9,1]:
        sd=math.sqrt(.03**2+.04**2-2*rho*.03*.04)
        covariance_sweep.append({'assumed_rho':rho,'conditional_sigma_difference_e2b2':sd,
                                 'absolute_difference_over_conditional_sigma':abs(difference)/sd})
    rho_for_three=(.03**2+.04**2-(abs(difference)/3)**2)/(2*.03*.04)
    checks={
        'five_matched_rows':[x['spin'] for x in rows]==['31/2-','33/2-','35/2-','37/2-','39/2-'],
        'first_four_lifetime_ratios_between_1_9_and_2_3':all(1.9<x['tau_B_over_A']<2.3 for x in rows[:4]),
        'last_E2_pair_preserved':rows[-1]['BE2_A_e2b2']==.13 and rows[-1]['BE2_B_e2b2']==.11,
        'correlation_changes_conditional_significance':covariance_sweep[0]['absolute_difference_over_conditional_sigma']<1 and covariance_sweep[-1]['absolute_difference_over_conditional_sigma']>3,
    }
    raw=ROOT/'raw/papers/gpt/high-spin-20260920/三轴/手征/2007_Mukhopadhyay et al_From Chiral Vibration to Static Chirality in Nd 135.pdf'
    out={'source':'Mukhopadhyay et al. PRL 99, 172501 (2007)',
         'doi':'10.1103/PhysRevLett.99.172501','raw_sha256':hashlib.sha256(raw.read_bytes()).hexdigest(),
         'rows':rows,'covariance_design_35_over_2':{'difference_BminusA_e2b2':difference,
             'scope':'assumed marginal standard deviations; rho hypothetical; not actual significance',
             'sweep':covariance_sweep,'rho_needed_for_conditional_3sigma':rho_for_three},
         'checks':checks,'all_arithmetic_checks_pass':all(checks.values()),
         'experimental_CI_recovered':False,'new_experimental_fit':False,
         'not_inferred':['unique branch/energy compensation','universal electromagnetic chirality criterion','static chirality spin threshold'],
         'missing':['line-resolved E2 branch and final state mapping from primary level scheme','mixing/conversion and intensity covariance','actual DSAM producer/response and joint covariance']}
    (RUN/'nd135-rate-scope-043.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':checks,'experimental_CI_recovered':False},ensure_ascii=False))
    return 0 if all(checks.values()) else 1


if __name__=='__main__':
    raise SystemExit(main())
