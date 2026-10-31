#!/usr/bin/env python3
"""Forward check of PE06 Eqs.4/5 and band-following labels, not a fit."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def ratios(q, ai, af):
    bi, bf = math.sqrt(1-ai*ai), math.sqrt(1-af*af)
    return (((q*af*bi-ai*bf)/(q*bf*bi+ai*af))**2,
            ((q*ai*bf-af*bi)/(q*ai*af+bi*bf))**2)


def main():
    rows = []
    # alpha_I is the coefficient of |1> in |y>, per Eq.1.
    # Table position next to ny is not a redefinition of that coefficient.
    for spin, ai, af, invert, printed in [(17,.118,.894,True,(.33,.70)),
                                          (18,.099,.427,False,(.17,.062))]:
        raw = ratios(2, ai, af)
        transformed = tuple(1/x for x in raw) if invert else raw
        rows.append(dict(spin=spin, alpha_I=ai, alpha_Iminus2=af,
                         Qratio_assumed=2, eq4_eq5=raw,
                         band_following_requires_reciprocal=invert,
                         reconstructed_table_ny_y=transformed,
                         printed_table_ny_y=printed,
                         residuals=[a-b for a,b in zip(transformed,printed)],
                         locator='PE06 printed 112502-3 Eqs.4/5 and Table I'))
    # A published possible interval, transformed monotonically; not Gaussian.
    checks = {'four_printed_calculations_reproduced_to_rounding':all(abs(v)<.005 for r in rows for v in r['residuals']),
              'odd_yrast_identity_exchange_retained':rows[0]['band_following_requires_reciprocal'],
              'even_labels_not_inverted':not rows[1]['band_following_requires_reciprocal']}
    raw = ROOT / 'raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/手征/2006_Petrache et al_Risk of Misinterpretation of Nearly Degenerate Pair Bands as Chiral Partners in.pdf'
    result = dict(raw_sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),
                  rows=rows, checks=checks,
                  conditional_Q_squared_range=[1.6**2,2.4**2],
                  Q_squared_scope='Square of author allowed transition-moment ratio; only maps to comparable unmixed E2 strengths under the adopted transition-moment convention, not measured mixed-level B ratio or beta ratio.',
                  new_fit=False,experimental_CI_recovered=False,
                  independence='Table I uses Ref.11 to-be-published branching input; Ref.9 lifetime data are a qualitative comparison, not a new experiment in this paper.',
                  not_inferred=['likelihood or Gaussian significance','all dynamic chirality excluded','135Nd branching measured by 134Pr','complete eight-row refit'])
    (RUN/'mixing-label-scope-045.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':checks,'experimental_CI_recovered':False}))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
