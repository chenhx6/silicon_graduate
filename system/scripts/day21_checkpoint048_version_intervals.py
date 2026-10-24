#!/usr/bin/env python3
"""AY23 Table III convention and interval-image controls; no new joint CI."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def square_image(lo, hi, divisor):
    return [0 if lo <= 0 <= hi else min(lo*lo, hi*hi)/divisor,
            max(lo*lo, hi*hi)/divisor]


def main():
    corrected = {'matrix_element_eb':-.220,'downward_initial_spin':4,
                 'central_BE2_e2b2':.220**2/9,
                 'old_printed_amplitude_interval_eb':[-.250,-.170],
                 'corrected_printed_amplitude_interval_eb':[-.223,-.215],
                 'old_square_image_e2b2':square_image(-.250,-.170,9),
                 'corrected_square_image_e2b2':square_image(-.223,-.215,9),
                 'locator':'AY23 PDF p.7 Table III footnote2 and 2_1->4_2 row'}
    weak = {'matrix_element_eb':.010,'printed_amplitude_interval_eb':[-.011,.019],
            'central_downward_BE2_e2b2':.010**2/5,
            'full_interval_square_image_e2b2':square_image(-.011,.019,5),
            'incorrect_endpoint_only_lower':min(.011**2,.019**2)/5,
            'locator':'AY23 PDF p.7 Table III 0_1->2_5 row'}
    checks = {'corrected_B_center_matches_printed_rounding':abs(corrected['central_BE2_e2b2']-.0054)<.00005,
              'ground_2_1_downward_spin_divisor':abs(.526**2/5-.0553)<.00005,
              'zero_crossing_has_zero_lower_image':weak['full_interval_square_image_e2b2'][0]==0,
              'endpoint_only_transform_loses_zero':weak['incorrect_endpoint_only_lower']>0}
    raw='raw/papers/day20-20261022/ayangeakaa-2023-ge76-coulomb-excitation-full.pdf'
    out=dict(raw_sha256=hashlib.sha256((ROOT/raw).read_bytes()).hexdigest(),
             correction=corrected,weak_amplitude=weak,checks=checks,
             scope='Deterministic image of printed scalar amplitude ranges and downward spin normalization; not a newly estimated experimental CI, joint confidence region or GOSIA replay.',
             errors_assumed_independent=False,new_experimental_CI=False,
             new_joint_covariance_recovered=False,
             version_note='Do not bind AY19 2_5 label to AY23 2_6 using numerical equality alone; preserve each table and resolve the state from its level identity before a merged network.')
    (RUN/'version-interval-scope-048.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'checks':checks,'new_experimental_CI':False}))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
