#!/usr/bin/env python3
"""Literal central bookkeeping and conditional printing intervals; no fit or CI."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def main():
    files = {
        'yao': ('raw/papers/gpt/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam/yao-2012-34si-beyond-mean-field-bubble.pdf',
                'a3e8765895514298dc2479dc935617ed9972af418fcf9acb28fe83b497c0a0d2'),
        'mutschler': ('tmp/day21/mutschler2017/PDFs/A_proton_density_bubble_in_the_doubly_magic_34Si_nucleus.pdf',
                     'eb0450b2cfee9fc52098668d090db23b7e728899ec1116528d827e90a6b09a85'),
    }
    identity = {}
    for key, (path, expected) in files.items():
        sha = hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
        assert sha == expected
        identity[key] = {'path': path, 'sha256': sha}
    rows = [
        ('HF point proton', '.044', '.074', '.41', 'arxiv PDF7 Table I'),
        ('GCM point proton', '.057', '.073', '.21', 'arxiv PDF7 Table I'),
        ('HF charge', '.056', '.071', '.21', 'arxiv PDF7 Table II'),
        ('GCM charge', '.064', '.070', '.09', 'arxiv PDF7 Table II'),
    ]
    printing = []
    half_unit = F('.0005')
    for name, center, maximum, reported, locator in rows:
        c, m, q = F(center), F(maximum), F(reported)
        # Conditional nearest .001 density and nearest .01 Fmax printing only.
        # 1-c/m decreases with c and increases with m for positive densities.
        lo = 1-(c+half_unit)/(m-half_unit)
        hi = 1-(c-half_unit)/(m+half_unit)
        reported_lo, reported_hi = q-F('.005'), q+F('.005')
        compatible = max(lo, reported_lo) <= min(hi, reported_hi)
        assert compatible
        printing.append({
            'row': name, 'locator': locator,
            'F_from_printed_density_centers': float(1-c/m),
            'reported_F': float(q),
            'density_printing_interval_image': [float(lo), float(hi)],
            'reported_F_printing_bin': [float(reported_lo), float(reported_hi)],
            'intervals_overlap': compatible,
        })
    selected = (F('1.5')+F('1.4'))/100 * F('27.7')
    assert selected == F('.8033')
    result = {
        'scope': 'source central values and explicitly conditional printing bins; not original producer replay',
        'source_identity': identity,
        'yao_Fmax_printing': printing,
        'yao_collective_ratios': {'E0_center_ratio': float(F('58.1')/F('13.0')),
                                  'E2_center_ratio': float(F('60.5')/F('16.6'))},
        'yao_model_total_Fsat_all_rows': [-.08, -.08, -.06, -.07, -.07],
        'mutschler_selected_l0_partial_center_mb': float(selected),
        'mutschler_occupancy_central_ratio': float(F('.17')/F('1.7')),
        'mutschler_author_weak_state_alternative_central_ratio': float((F('.17')+F('.07'))/F('1.7')),
        'author_total_alternative_uncertainty': None,
        'new_CI': None,
        'actual_Cov': None,
        'density_smoothing_bias_identified': False,
        'source_read_scope_124': 'Mutschler PDF2-5 text and PDF4 visual; Yao PDF5-7 text and PDF7 visual',
        'limitations': ['Nearest-digit printing is a declared assumption, not an experimental uncertainty model.',
                       'Overlap of printing bins does not identify unrounded values or reproduce a GCM job.',
                       'The E0 discrepancy might indicate excessive mixing; no unique density correction follows.',
                       'No covariance was reconstructed and no occupancy errors were independently added.'],
    }
    out = RUN/'literal-rounding-scope-124.json'
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({'output': str(out.relative_to(ROOT)),
                      'all_four_conditional_printing_checks': all(x['intervals_overlap'] for x in printing),
                      'new_CI': None}))


if __name__ == '__main__':
    main()
