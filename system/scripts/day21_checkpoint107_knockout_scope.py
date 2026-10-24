#!/usr/bin/env python3
"""Selected published central values and normalization identities; no refit/CI."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def audit():
    pdf = ROOT / 'tmp/day21/mutschler2017/PDFs/A_proton_density_bubble_in_the_doubly_magic_34Si_nucleus.pdf'
    sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert sha == 'eb0450b2cfee9fc52098668d090db23b7e728899ec1116528d827e90a6b09a85'
    # Fig2 feeds are percentages for residue final states, not gamma intensities.
    b2101, b3704 = F('1.5') / 100, F('1.4') / 100
    sigma = F('27.7')  # mb, quoted inclusive KO central value
    partial = (b2101 + b3704) * sigma
    assert partial == F('.8033')
    n34, n36 = F('.17'), F('1.7')
    weak_extra = F('.07')  # author's alternative all-four-weak-states-as-l0 scenario
    assert n34 / n36 == F('.1')
    return {
        'scope': 'literal central bookkeeping and declared normalization identity, not knockout analysis replay',
        'source': {'arxiv': '1707.03583v1', 'doi': '10.1038/nphys3916', 'sha256': sha,
            'locators': ['arxiv PDF p3 Fig2', 'arxiv PDF p4 Methods Eq1']},
        'central_bookkeeping': {'sigma_inclusive_KO_mb': float(sigma),
            'selected_l0_final_state_branch_sum_fraction': float(b2101 + b3704),
            'selected_l0_partial_cross_section_mb': float(partial),
            'n34_reported': float(n34), 'n36_reported': float(n36),
            'central_occupancy_ratio': float(n34 / n36),
            'alternative_n34_if_all_four_weak_states_l0_central': float(n34 + weak_extra),
            'alternative_central_ratio': float((n34 + weak_extra) / n36),
            'quoted_cross_section_ratio_36_over_34_approximately': 12,
            'is_cross_section_ratio_independently_reconstructed': False},
        'normalization_contract': {'formula': 'C2S_f = (b_f/100)*sigma_inclusive/(Rs*sigma_sp_f) when b is in percent',
            'common_Rs_scale_lambda': 'all C2S values scale as1/lambda',
            'same_nucleus_ratio': 'b_i*sigma_sp_j/(b_j*sigma_sp_i) if the sameRs applies',
            'cross_nucleus_Rs_cancellation': 'requires an explicit transferable-Rs assumption; not automatic',
            'Rs_approx20percent_already_in_published_occupancy_errors': True,
            'additional_independent20percent_error_added': False},
        'inference_boundary': ['Fig3 proton/neutron profiles are RHFB/PKO2 calculations, not scattering images',
            'small2s occupancy does not uniquely specify radial wavefunctions or charge folding',
            'charge-density model depletion is not the same quantity as the proton density claim',
            'model dependence limits precision/exclusivity but does not erase observed differential support',
            'published weak-state alternative must be retained; no new CI from adding its quoted errors'],
        'raw_events_acquired': False, 'reaction_job_replayed': False,
        'new_CI': None, 'actual_joint_covariance': None, 'scientific_certification': False,
    }


if __name__ == '__main__':
    d = audit()
    p = RUN / 'knockout-scope-result-107.json'
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'output': str(p.relative_to(ROOT)), 'partial_central_mb': d['central_bookkeeping']['selected_l0_partial_cross_section_mb'],
        'occupancy_ratio_central': d['central_bookkeeping']['central_occupancy_ratio'], 'new_CI': None}, ensure_ascii=False))
