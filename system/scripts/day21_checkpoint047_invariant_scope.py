#!/usr/bin/env python3
"""Exact finite scalar-closure controls and literal table ledger, no Ge76 fit."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def scalar_moments(a):
    # Declared 0+/2+ reduced-element block; S=A A^T (see HE20 R149).
    s = [[sum(x*y for x,y in zip(r,t)) for t in a] for r in a]
    q2 = s[0][0]
    q4 = sum(x*x for x in s[0])
    return dict(q2=q2, q4=q4, variance_Q2=q4-q2*q2)


def main():
    up = dict(full=scalar_moments([[1,1],[1,-1]]),
              internal_2plus_truncated=scalar_moments([[1],[1]]))
    down = dict(full=scalar_moments([[1,1],[1,1]]),
                internal_2plus_truncated=scalar_moments([[1],[1]]))
    checks = {'internal_truncation_can_increase_scalar_variance':up['full']['variance_Q2']==0 and up['internal_2plus_truncated']['variance_Q2']==1,
              'internal_truncation_can_decrease_scalar_variance':down['full']['variance_Q2']==4 and down['internal_2plus_truncated']['variance_Q2']==1,
              'single_scalar_endpoint_gives_zero':scalar_moments([[1,1]])['variance_Q2']==0,
              'q2_omission_positive_in_both_examples':all(x['full']['q2']==2 and x['internal_2plus_truncated']['q2']==1 for x in [up,down])}
    table4 = {
        'nominal':{'q2_relative_percent':[-9.4,6.9,3.4], 'sigma_Q2_relative_percent':[-23.1,10.0,14.6],
                   'cos3delta_absolute_difference':[0,.23,.11], 'sigma_cos3delta_absolute_difference':[-.13,.08,.14]},
        'bare':{'q2_relative_percent':[-15.6,7.8,5.4], 'sigma_Q2_relative_percent':[-30.6,11.6,13.3],
                'cos3delta_absolute_difference':[.01,.37,.19], 'sigma_cos3delta_absolute_difference':[-.16,.13,.19]}}
    raws = ['raw/papers/gpt/learning-daily/20261022-DAY20-be2-qt-deformation-systematics/henderson-2020-quadrupole-invariant-convergence.pdf',
            'raw/papers/gpt/learning-daily/20261022-DAY20-be2-qt-deformation-systematics/ayangeakaa-2019-rigid-triaxial-ge76.pdf']
    out = dict(upward_variance_control=up,downward_variance_control=down,checks=checks,
               model_table_nI4_literal=table4,
               table_scope='Manual original-table transcription [center,upper spread,lower spread]; not a recomputation of 34 nuclei or experimental CI.',
               order_ledger={'q2':2,'q3cos3delta':3,'variance_Q2_requires':4,'HE20_Eq27_requires':6},
               mathematical_scope='Exact finite Hermitian scalar closure with a declared reduced-E2 block. No commuting charge-coordinate realization or nuclear Hamiltonian is asserted; no Ge76 angular variance is calculated.',
               not_proven=['Ge76 gamma softness','universal monotonic suppression of softness','giant-resonance contribution in this finite valence-space sample','strong or pathological actual joint covariance'],
               raw_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in raws},
               missing=['full Ge76 higher-order input network','original GOSIA yields/response/job and joint covariance','actual omitted-strength bounds'],
               new_experimental_CI=False,Ge76_rigidity_falsified=False)
    (RUN/'invariant-scope-047.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':checks,'new_experimental_CI':False,'Ge76_rigidity_falsified':False}))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
