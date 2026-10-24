#!/usr/bin/env python3
"""Literal PRL Table I arithmetic; rounding controls are NOT statistical CIs."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def audit():
    raw = ROOT / 'raw/papers/day21-20261023/burgunder-2014-35si-two-body-spin-orbit.pdf'
    digest = hashlib.sha256(raw.read_bytes()).hexdigest()
    assert digest == 'c8db651c453428630b450c53a38c28fba05ed7c0fa0dda3023383213c0e53aef'
    # (total_1/2, K0_1/2, K1_1/2, total_3/2, K0_3/2, K1_3/2)
    printed = [
        ('N3LO bare', ['-1.124', '-1.317', '.193', '-1.413', '-1.317', '-.096']),
        ('N3LO 2hw', ['-1.128', '-1.312', '.184', '-1.404', '-1.312', '-.092']),
        ('N3LO 4hw', ['-1.201', '-1.401', '.200', '-1.500', '-1.401', '-.100']),
        ('KLS', ['-1.180', '-1.374', '.194', '-1.471', '-1.374', '-.097']),
    ]
    result = []
    for name, values in printed:
        t1, c1, s1, t3, c3, s3 = map(F, values)
        trace = 2 * s1 + 4 * s3
        closure = (t1 - t3) - (s1 - s3)
        # Conditional nearest-.001 rounding, not measured error or new data.
        eps = F(5, 10000)
        assert abs(trace) <= 6 * eps
        assert abs(closure) <= 4 * eps
        result.append({'interaction': name, 'literal_values_MeV': values,
            'K0_printed_difference_MeV': float(c1 - c3),
            'K1_difference_MeV': float(s1 - s3), 'total_difference_MeV': float(t1 - t3),
            'weighted_K1_trace_MeV': float(trace),
            'total_vs_K1_difference_residual_MeV': float(closure),
            'rounding_compatible_with_zero_if_nearest001': True})
    assert result[0]['weighted_K1_trace_MeV'] == .002
    assert result[2]['total_vs_K1_difference_residual_MeV'] == -.001
    constrained_difference = F('-.844') - F('-1.101')
    reduction = F('1.47') * constrained_difference
    assert reduction == F('.37779')
    return {
        'scope': 'literal version/rounding and source-attribution audit; no original SM or reaction refit',
        'raw_path': str(raw.relative_to(ROOT)), 'sha256': digest,
        'locators': ['042502-2 Experiment', '042502-3 ADWA/Fig2', '042502-4 Eq1/TableI', '042502-5 Conclusions'],
        'rows': result,
        'printed_rounding_contract': {'nearest_MeV': .001, 'trace_half_width_MeV': .003,
            'difference_closure_half_width_MeV': .002, 'is_statistical_CI': False},
        'M3Y_K1_difference_MeV': float(F('.178') - F('-.089')),
        'calibrated_SM': {'constrained_monopoles_MeV': [-.844, -1.101],
            'difference_MeV': float(constrained_difference), 'calculated_occupancy_difference': 1.47,
            'Eq1_central_keV': float(reduction * 1000), 'paper_rounded_keV': 378,
            'Baranger_from_same_calculated_strengths_keV': 380,
            'independent_experiment_count': 0},
        'selected_source_limits': [
            '25% is proposed after SM correlation unfolding, not a direct spatial-density measurement',
            'Selected K2=0/K0 equality/K1 differences are model-space decomposition statements',
            'Author estimates residual continuum/binding effects below5% with constrained mean-field calculations',
            'Conclusion retains likely suppressed or modest for other force components',
            'No exact one-body/two-body theoretical duality is proved by these few numbers',
            'Published -.096 must not be changed to -.0965 merely to force an exact trace',
        ],
        'new_joint_covariance': None, 'experimental_CI': None,
        'actual_density_profile': None, 'scientific_certification': False,
    }


if __name__ == '__main__':
    d = audit()
    p = RUN / 'monopole-scope-result-106.json'
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'output': str(p.relative_to(ROOT)), 'bare_trace_MeV': d['rows'][0]['weighted_K1_trace_MeV'],
        'Eq1_keV': d['calibrated_SM']['Eq1_central_keV'], 'experimental_CI': None}, ensure_ascii=False))
