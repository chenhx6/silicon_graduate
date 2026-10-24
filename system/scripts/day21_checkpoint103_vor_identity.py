#!/usr/bin/env python3
"""Selected literal VoR cells and conditional identity controls, not a refit."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261023-DAY21-week-three-experimental-boundaries-exam-run-01'


def audit():
    pdf = ROOT / 'tmp/day21-checkpoint103/lv2019-vor.pdf'
    digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
    assert digest == '450a3032d7fecfdbc16f5a848be3d63842a536b0508dda73f3de55270fbf2066'
    rows = [
        # Printed entries manually read from Table I and checked visually.
        {'band': 'D6', 'Egamma': 591.8, 'Ei': 4599.6, 'Ef_D6': 4007.8, 'multipolarity': None},
        {'band': 'D6', 'Egamma': 681.0, 'Ei': 4971.2, 'Ef_D6': 4290.2, 'multipolarity': None},
        {'band': 'D6', 'Egamma': 812.0, 'Ei': 5411.6, 'Ef_D6': 4599.6, 'multipolarity': None},
    ]
    for row in rows:
        row['central_energy_residual_keV'] = row['Ei'] - row['Ef_D6'] - row['Egamma']
        assert abs(row['central_energy_residual_keV']) < 1e-9
    # Literal table parent vs. the independently printed parent on D6 in-band rows.
    table_parent, other_parent, target, printed_gamma = 5412.6, 5411.6, 4414.5, 998.1
    row998 = {
        'table_parent_keV': table_parent, 'other_D6_39over2_parent_keV': other_parent,
        'D5_35over2_target_keV': target, 'table_gamma_keV': printed_gamma,
        'literal_table_residual_keV': table_parent - target - printed_gamma,
        'using_other_parent_residual_keV': other_parent - target - printed_gamma,
        'conditional_gamma_from_other_parent_keV': other_parent - target,
        'body_and_Fig1_rounded_label_keV': 997,
        'selected_as_measured_correction': False,
    }
    assert abs(row998['literal_table_residual_keV']) < 1e-9
    assert abs(row998['using_other_parent_residual_keV'] + 1) < 1e-9
    # General parity selection rule, evaluated on the literal 334.4-keV row.
    # This detects inconsistency in the printed tuple, not which field is wrong.
    parity_control = {
        'gamma_keV': 334.4, 'literal_initial': '27/2-', 'literal_final': '25/2+',
        'literal_multipolarity': 'M1/E2',
        'M1_parity_factor': (-1) ** (1 + 1), 'E2_parity_factor': (-1) ** 2,
        'literal_state_parity_ratio': -1,
        'literal_tuple_satisfies_parity': False,
        'actual_initial_parity_inferred_by_this_script': None,
    }
    assert parity_control['M1_parity_factor'] == parity_control['E2_parity_factor'] == 1
    return {
        'scope': 'VoR selected-line identity plus declared central algebra/parity; no experimental likelihood',
        'source_pdf': str(pdf.relative_to(ROOT)), 'sha256': digest,
        'DOI': '10.1103/PhysRevC.100.024314', 'VoR_pages': 9,
        'locators': {'table': '024314-4/5 Table I', 'level_scheme': '024314-2 Fig1',
            '997_text': '024314-6 first left paragraph', 'model_and_B_lineage': '024314-8 left column'},
        'rows': rows, 'row998': row998, 'parity_control': parity_control,
        'other_literal_boundaries': {
            '934point9': {'D5_Ei': 5787.6, 'D6_labelled_Ei': 5787.6, 'D5_Igamma': .91, 'D6_labelled_Igamma': .70},
            '966point3': {'D5_Ei': 6281.5, 'D6_labelled_Ei': 6281.5, 'D5_Igamma': .68, 'D6_labelled_Igamma': .68},
            'D3_text_I': '29 hbar', 'D3_table_328point5_initial_I': '29/2+',
        },
        'model_inputs_as_reported': {'D5_D6_CDFT_beta': .24, 'D5_D6_CDFT_gamma_deg': 22.2,
            'D5_D6_PRM_gamma_deg': 20.2, 'J0_hbar2_per_MeV': 23.5, 'Coriolis_xi': .98},
        'absolute_B_source_reference': 'Ref36 Mukhopadhyay2007, explicitly stated on VoR p8',
        'actual_MU07_line_binding': None, 'actual_joint_covariance': None,
        'experimental_CI': None, 'scientific_certification': False,
    }


if __name__ == '__main__':
    result = audit()
    p = RUN / 'vor-line-identity-result-103.json'
    p.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'output': str(p.relative_to(ROOT)), 'conditional_998_residual_keV': result['row998']['using_other_parent_residual_keV'], 'literal_parity_tuple_consistent': result['parity_control']['literal_tuple_satisfies_parity'], 'experimental_CI': None}, ensure_ascii=False))
