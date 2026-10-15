#!/usr/bin/env python3
"""Actual accepted-copy 136Pr table crosswalk, not event-level reanalysis.

Checks manual transcription against the immutable PDF, graph topology, shared
energy closures and the Q1 endpoint change. Any covariance used for GLS is a
declared control; author band partitions and parity proposals stay distinct.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from fractions import Fraction
from pathlib import Path

import numpy as np


def audit(fixture):
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise AssertionError(name)

    source=Path(fixture['source']).read_text()
    raw=Path(re.search(r'^raw_file: "(.*)"$',source,re.M).group(1))
    check('actual_raw_hash_immutable_copy',
          hashlib.sha256(raw.read_bytes()).hexdigest()==fixture['raw_sha256'])
    text=subprocess.check_output(['pdftotext','-layout',str(raw),'-'],text=True)
    pages=text.split('\f')
    check('accepted_copy_seventeen_pages_plus_final_separator',len(pages)==18)
    check('accepted_version_repository_cover_not_publisher_pagination',
          'Accepted version' in pages[0])
    table=[]
    for row in fixture['edges']:
        pattern=r'^\s*'+re.escape(row['energy_literal'])+r'\s+'+re.escape(row['Ei_literal'])+r'\s+.*$'
        matches=re.findall(pattern,pages[row['pdf_page']-1],re.M)
        check('unique_actual_table_row_'+row['name'],len(matches)==1)
        actual=' '.join(matches[0].split())
        if row['M'] is None:
            check('missing_R_and_M_preserved_'+row['name'],
                  row['R'] is None and row['dR'] is None and 'M1+E2' not in actual)
        else:
            check('reported_M_preserved_'+row['name'],row['M'] in actual)
        table.append(dict(row,actual_line=actual))
    nodes=list(fixture['nodes'])
    node_index={name:i for i,name in enumerate(nodes)}
    inc=np.zeros((len(table),len(nodes)))
    energies=np.array([row['energy'] for row in table])
    for i,row in enumerate(table):
        inc[i,node_index[row['parent']]]=1
        inc[i,node_index[row['daughter']]]=-1
    check('physical_downward_assigned_spin_step',all(
        fixture['nodes'][row['parent']]['J']-fixture['nodes'][row['daughter']]['J']==1
        for row in table))
    check('connected_five_levels_six_edges_rank_four',
          inc.shape==(6,5) and np.linalg.matrix_rank(inc)==4)
    check('global_energy_shift_null_mode',np.array_equal(inc@np.ones(5),np.zeros(6)))
    C=np.array([[1,1,-1,-1,0,0],[1,1,0,0,-1,-1]])
    check('two_cycle_space_rows',np.array_equal(C@inc,np.zeros((2,5)))
          and np.linalg.matrix_rank(C)==2)
    exact_energies=[Fraction(str(row['energy'])) for row in table]
    exact_residuals=[sum(Fraction(int(c))*e for c,e in zip(line,exact_energies)) for line in C]
    check('exact_printed_cycle_residuals_minus01_minus02',
          exact_residuals==[Fraction(-1,10),Fraction(-1,5)])
    Sigma=np.diag([row['sigma']**2 for row in table])
    residuals=C@energies
    cycle_cov=C@Sigma@C.T
    check('shared_path_cycle_covariance_control',
          np.max(abs(cycle_cov-np.array([[.54,.25],[.25,.50]])))<1e-14)
    check('cycle_covariance_not_diagonal',cycle_cov[0,1]>.24)
    chi=float(residuals@np.linalg.solve(cycle_cov,residuals))
    # Fit four independent anchored levels, and compare to the cycle projection.
    D=inc[:,:4]
    W=np.diag(1/np.diag(Sigma))
    fit=np.linalg.solve(D.T@W@D,D.T@W@energies)
    fitres=energies-D@fit
    gls=float(fitres@W@fitres)
    check('GLS_and_cycle_projection_same_conditional_chi',abs(chi-gls)<1e-12)
    check('conditional_chi_exact_point08_not_experimental_pvalue',abs(chi-.08)<1e-11)
    check('unknown_source_joint_covariance_preserved',
          fixture['controls']['energy_covariance_source'] is None)
    nominal_levels=np.array([fixture['nodes'][k]['energy'] for k in nodes])
    level_residuals=inc@nominal_levels-energies
    check('rounded_adjusted_levels_not_enforced_as_exact_edge_differences',
          np.max(abs(level_residuals))>.39 and np.max(abs(level_residuals))<.41)
    ep=fixture['q1_endpoint']
    check('Q1_new_endpoint_E_matches_table',abs(ep['Q1_E']-ep['link']-ep['Q2_18_E'])<1e-11)
    check('Q2_two_downstream_steps_match_table',
          abs(ep['Q2_18_E']-ep['Q2_14_E']-ep['Q2_18to16']-ep['Q2_16to14'])<1e-11)
    check('endpoint_change_four_hbar_under_author_stretched_assignment',
          ep['new_J']-ep['lower_candidate_J']==4)
    alternative_parent=ep['Q2_14_E']+ep['link']
    check('alternative_endpoint_current_anchor_energy_shift_1350point2',
          abs(ep['Q1_E']-alternative_parent-1350.2)<1e-10)
    check('Q1_parity_experiment_stays_unknown',ep['parity_experiment'] is None)
    check('full_branching_and_B_not_inferred',fixture['controls']['absolute_B'] is None)
    p3=pages[2]
    check('primary_same_dataset_sentence_present',
          'same data' in p3 and 'Refs. [16, 31]' in p3)
    check('same_campaign_ref16_is_actual_2019_Nd_paper',
          'Phys. Rev. C 100, 024314 (2019)' in pages[15])
    # Two identical printed energies in different bands do not prove physically
    # degenerate lines; the actual Fig4 caption explicitly documents shared gates.
    check('D3_D5_334point4_rows_both_reported',
          '334.4(2)' in pages[6] and '334.4(3)' in pages[6])
    check('shared_gate_contaminants_explicit_primary_caption',
          'also present in band D5' in pages[4])
    check('D6_limit_construction_not_invented',
          fixture['controls']['D6_upperlimit_confidence'] is None)
    return dict(source=fixture['source'],raw_sha256=fixture['raw_sha256'],
                source_rows=table,node_order=nodes,incidence=inc.tolist(),
                cycle_matrix=C.tolist(),cycle_residual_keV=residuals.tolist(),
                Sigma_control=Sigma.tolist(),cycle_cov_control=cycle_cov.tolist(),
                chi_control=chi,chi_GLS_control=gls,df_control=2,
                source_adjusted_level_edge_residual_keV=level_residuals.tolist(),
                Q1_endpoint=ep,
                alternative_parent_using_current14_anchor=alternative_parent,
                distinction='The alternative is a task counterfactual using current anchors, NOT a number attributed to the 1996 paper.',
                boundaries=fixture['controls'],checks=checks,checks_passed=len(checks))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fixture',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=audit(json.loads(args.fixture.read_text()))
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks_passed=result['checks_passed'],
                          all_checks_true=all(result['checks'].values()),
                          output=str(args.output))))


if __name__=='__main__':
    main()
