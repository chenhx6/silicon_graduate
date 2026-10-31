#!/usr/bin/env python3
"""Zhu Fig.2 printed-energy loop arithmetic; no branching or B assignment."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def main():
    # Visual transcription of arXiv v2 PDF p.4 Fig.2. Parentheses retained.
    data = [(31, 648, 247.7, 896, 226, 670, False),
            (33, 639, 291.3, 930, 282, 648, False),
            (35, 591, 358.2, 949, 309, 639, False),
            (37, 556, 406, 963, 372, 591, True)]
    rows = []
    for spin, mixed, a_step, cross, b_step, lower_link, tentative in data:
        rows.append(dict(parent=f'B {spin}/2-', mixed_to=f'A {spin-2}/2-',
                         mixed_keV=mixed, cross_to=f'A {spin-4}/2-', cross_keV=cross,
                         tentative_links=tentative, a_step_keV=a_step, b_step_keV=b_step,
                         lower_mixed_keV=lower_link,
                         via_A_residual_keV=round(mixed+a_step-cross, 3),
                         via_B_residual_keV=round(b_step+lower_link-cross, 3),
                         locator='Zhu arXiv v2 PDF p.4 Fig.2'))
    adjacent_B = [173, 226, 282, 309, 372, 440]
    candidates = [dict(parent=f'B {spin}/2-', final=f'B {spin-4}/2-',
                       kinematic_difference_keV=adjacent_B[i]+adjacent_B[i+1],
                       observed_line_in_Fig2=False)
                  for i, spin in enumerate([31, 33, 35, 37, 39])]
    checks = {'four_two_path_loops':len(rows)==4,
              'printed_energy_residuals_within_1keV':all(abs(r[k])<=1 for r in rows for k in ['via_A_residual_keV','via_B_residual_keV']),
              'tentative_last_pair_preserved':rows[-1]['tentative_links'],
              'candidates_not_observations':all(not r['observed_line_in_Fig2'] for r in candidates)}
    raw = ROOT / 'raw/papers/gpt/learning-daily/20261009-PREPLAN-high-spin-library/2003_Zhu et al_A Composite Chiral Pair of Rotational Bands in 135Nd.pdf'
    result = dict(raw_sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),
                  rows=rows, unobserved_inband_deltaI2_kinematic_candidates=candidates,
                  checks=checks, experimental_CI_recovered=False,
                  scope='Rounded-energy topology check; 1 keV is a bookkeeping tolerance, not experimental uncertainty or goodness of fit.',
                  not_inferred=['row-specific MU07 E2 component identity','branch probability','B from arrow width','unique lifetime compensation mechanism'],
                  missing=['MU07 row-to-line strengths/branch extraction record','signed mixing/IC and branch covariance','DSAM response and joint covariance'])
    (RUN / 'level-loop-scope-044.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'checks': checks, 'experimental_CI_recovered':False}))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
