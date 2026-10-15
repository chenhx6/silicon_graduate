#!/usr/bin/env python3
"""Reproducible candidate edges, never automatic 136Pr transition identities.

Table row counts are extraction counts only. Absolute energy windows are
chosen discovery filters, NOT confidence intervals. The old evaluation and
the accepted article differ in scope, normalization, assignments and version.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from fractions import Fraction
from pathlib import Path

from day14_pr136_flow_identifiability import ensdf_subset


VALUE=re.compile(r'^(\d+\.\d+)\s*\((\d+)\)$')
ROW=re.compile(r'^\s*(\d+\.\d+\(\d+\))\s+(\d+\.\d+\s*\(\d+\))\s+(.*)$')


def value_and_error(text):
    m=VALUE.fullmatch(text)
    if m is None:
        raise ValueError('unsupported printed value '+repr(text))
    value=Fraction(m[1])
    error=Fraction(int(m[2]),10**len(m[1].split('.')[1]))
    return float(value),float(error)


def table_rows(pages):
    out,rejected=[],[]
    band=None
    for page_number in range(6,10):
        for line_number,line in enumerate(pages[page_number-1].splitlines(),1):
            header=re.fullmatch(r'\s*Band ([DQ]\d)( bottom)?\s*',line)
            if header:
                band=header[1]+(' bottom' if header[2] else '')
            m=ROW.match(line)
            if m:
                E,dE=value_and_error(m[1])
                P,dP=value_and_error(m[2])
                arrow=m[3].split('→')
                if len(arrow)!=2 or band is None:
                    rejected.append(dict(pdf_page=page_number,line=line_number,raw=line,
                                         reason='missing band or unparsed spin arrow'))
                    continue
                # Retain the rest literally. Do not infer a blank M or extract
                # a DCO number without its footnote/reference gate convention.
                out.append(dict(id=f'PDF{page_number}:textline{line_number}',band=band,
                                pdf_page=page_number,text_line=line_number,
                                energy_text=m[1],E=E,dE=dE,parent_text=m[2],
                                P=P,dP=dP,daughter_difference_control=P-E,
                                remainder_literal=m[3],raw=line))
            elif re.match(r'^\s*\d+\.\d+\(\d+\)',line):
                rejected.append(dict(pdf_page=page_number,line=line_number,raw=line,
                                     reason='numeric-looking table row not accepted'))
    return out,rejected


def candidates(new,old,energy_window,parent_window=None):
    ewin=Fraction(str(energy_window))
    pwin=None if parent_window is None else Fraction(str(parent_window))
    out=[]
    for g in old:
        if g['parent_E'] is None or g['E'] is None:
            continue
        if abs(Fraction(str(new['E']))-Fraction(str(g['E'])))>ewin:
            continue
        if pwin is not None and abs(Fraction(str(new['P']))-Fraction(str(g['parent_E'])))>pwin:
            continue
        out.append(dict(old_line=g['line'],old_gamma_E=g['E'],
                        old_parent_E=g['parent_E'],old_M_literal=g['M'],
                        delta_gamma=new['E']-g['E'],delta_parent=new['P']-g['parent_E']))
    return out


def select(rows,band,E):
    matches=[x for x in rows if x['band']==band and x['E']==E]
    if len(matches)!=1:
        raise ValueError('ambiguous selected new row '+repr((band,E)))
    return matches[0]


def tally(adjacencies):
    n=[len(x) for x in adjacencies]
    return dict(no_candidate=n.count(0),one_candidate=n.count(1),
                multiple_candidates=sum(x>1 for x in n),edges=sum(n))


def audit(input_dir,receipts):
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise AssertionError(name)
    src=Path('knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md').read_text()
    raw=Path(re.search(r'^raw_file: "(.*)"$',src,re.M).group(1))
    sha=re.search(r'^raw_sha256: (\S+)',src,re.M).group(1)
    check('actual_accepted_copy_hash',hashlib.sha256(raw.read_bytes()).hexdigest()==sha)
    pages=subprocess.check_output(['pdftotext','-layout',str(raw),'-'],text=True).split('\f')
    rows,rejected=table_rows(pages)
    strict=[]
    for pn in range(6,10):
        for line in pages[pn-1].splitlines():
            tokens=line.split()
            if len(tokens)>2 and VALUE.fullmatch(tokens[0]) and VALUE.fullmatch(tokens[1]):
                strict.append(line)
    # Strict tokenization really misses this printed spacing, not a fabricated
    # malformed fixture. The new rule retains the source text unchanged.
    missing=set(x['raw'] for x in rows)-set(strict)
    check('strict_token_rule_missing_only_actual_spaced_parent',len(missing)==1
          and '1552.2 (3)' in next(iter(missing)))
    check('extraction156_is_table_rows_not_level_or_newline_count',len(rows)==156 and len(strict)==155)
    check('all_numeric_table_row_starts_accounted',not rejected)
    check('unique_source_row_ids',len(set(x['id'] for x in rows))==len(rows))
    spaced=select(rows,'D1',366.7)
    check('spaced_parent_uncertainty_parsed_correctly',spaced['P']==1552.2 and spaced['dP']==.3)
    limited=select(rows,'D5',237.)
    check('weak_I_limit_remains_literal','<0.1' in limited['remainder_literal'])
    check('no_blank_multipolarity_imputed','M1+E2' not in select(rows,'D6',320.4)['remainder_literal'])
    op=input_dir/'pd30si.ensdf'
    rec=next(x for x in receipts['objects'] if x['label']=='pd30si')
    check('actual_old_object_hash',hashlib.sha256(op.read_bytes()).hexdigest()==rec['text_sha256'])
    parsed=ensdf_subset(op,'136PR')
    old=parsed['gammas']
    check('old_gamma_records135placed_plus1unplaced',len(old)==136
          and sum(g['parent_E'] is None for g in old)==1)
    summaries=[]
    for window in (.5,1.,1.5,2.):
        adjE=[candidates(row,old,window) for row in rows]
        adjP=[candidates(row,old,window,parent_window=2.) for row in rows]
        te,tp=tally(adjE),tally(adjP)
        check('candidate_partition_conserves_rows_'+str(window),
              sum(te[k] for k in ('no_candidate','one_candidate','multiple_candidates'))==len(rows))
        check('parent_filter_only_removes_edges_'+str(window),
              all({x['old_line'] for x in p}<={x['old_line'] for x in e}
                  for e,p in zip(adjE,adjP)))
        summaries.append(dict(energy_window_keV_chosen=window,parent_window_keV_chosen=2.,
                              energy_only=te,energy_and_parent=tp))
    # Counterexamples are source-backed. A UNIQUE energy candidate can still
    # have an unrelated parent; uniqueness is not an identity proof.
    d3=select(rows,'D3',334.4)
    d5=select(rows,'D5',334.4)
    c3=candidates(d3,old,1.5)
    c5=candidates(d5,old,1.5)
    check('same_printed_gamma_has_different_new_parents',d3['P']==5086.3 and d5['P']==2779.4)
    check('both_have_same_unique_old_energy_candidate',len(c3)==len(c5)==1
          and c3[0]['old_line']==c5[0]['old_line']==208)
    check('parent_filter_rejects_D3_but_keeps_D5_in_this_control',
          not candidates(d3,old,1.5,2.) and len(candidates(d5,old,1.5,2.))==1)
    c_low=candidates(select(rows,'D6',611.1),old,1.5)
    c_high=candidates(select(rows,'D6',611.),old,1.5)
    check('611pair_same_unique_old_energy_candidate',len(c_low)==len(c_high)==1
          and c_low[0]['old_line']==c_high[0]['old_line']==296)
    check('611parent_control_separates_existing_and_highstate_candidate',
          len(candidates(select(rows,'D6',611.1),old,1.5,2.))==1
          and not candidates(select(rows,'D6',611.),old,1.5,2.))
    # Conversely, Q1 is explicitly re-anchored in the article, so rejecting
    # every large parent displacement would discard its reported old sequence.
    q1=[]
    for new_E,old_E,old_parent in [(875.6,876.1,3998.8),(546.,545.3,4544.1),
                                  (850.4,850.4,5394.5),(1075.4,1075.1,6469.6),
                                  (1283.1,1282.,7751.7)]:
        new=select(rows,'Q1',new_E)
        chosen=[g for g in old if g['E']==old_E and g['parent_E']==old_parent]
        check('anchor_guided_Q1_candidate_exists_'+str(new_E),len(chosen)==1)
        old_g=chosen[0]
        old_level=next(x for x in parsed['levels'] if x['line']==old_g['parent_line'])
        check('anchor_guided_old_band_A_marker_'+str(new_E),old_level['raw'].ljust(80)[76]=='A')
        check('absolute_parent_filter_misses_reanchored_Q1_'+str(new_E),
              not candidates(new,old,1.5,2.))
        q1.append(dict(new_id=new['id'],new_gamma=new_E,new_parent=new['P'],
                       old_gamma=old_E,old_parent=old_parent,old_line=old_g['line'],
                       parent_shift=new['P']-old_parent,
                       new_parent_uncertainty=new['dP'],old_parent_uncertainty=old_level['dE']))
    shifts=[x['parent_shift'] for x in q1]
    check('anchor_guided_Q1_shift_range_not_one_exact_global_offset',
          max(shifts)-min(shifts)>1 and max(shifts)-min(shifts)<3)
    for band,E in [('D5',263.1),('D5',405.1)]:
        row=select(rows,band,E)
        check('order_changed_D5_has_energy_candidate_but_no_fixed_parent_'+str(E),
              candidates(row,old,1.5) and not candidates(row,old,1.5,2.))
    # Most source-energy rows do not encode newness. Produce a complete graph
    # and old-node degree, including many-to-one conflicts, rather than a
    # nearest-neighbor or maximum matching advertised as scientific identity.
    edges=[]
    degrees=Counter()
    for row in rows:
        cs=candidates(row,old,1.5)
        for c in cs:
            edges.append(dict(new_id=row['id'],**c))
            degrees[c['old_line']]+=1
    check('bipartite_edge_degree_conservation',len(edges)==sum(degrees.values())
          and len(edges)==summaries[2]['energy_only']['edges'])
    check('many_new_candidates_compete_for_one_old_record',max(degrees.values())>1)
    check('unplaced_old_record_never_silently_matched',37 not in degrees)
    return dict(
        scope='accepted-copy Table I rows only; old 2018 reaction L/G records, not whole 136Pr scheme/new-transition count',
        actual_new_pdf_sha256=sha,actual_old_text_sha256=rec['text_sha256'],
        table_rows_extracted=len(rows),strict_token_rows=len(strict),old_gamma_records=len(old),
        old_placed_gamma_records=135,bands=dict(Counter(x['band'] for x in rows)),
        rejected_rows=rejected,parser_spacing_counterexample=list(missing),
        discovery_windows=summaries,source_rows=rows,energy_candidate_edges_1point5keV=edges,
        old_record_degrees_1point5keV=dict(degrees),anchor_guided_Q1_candidates=q1,
        controls=[dict(case='334.4 D3',new=d3,energy_only=c3),
                  dict(case='334.4 D5',new=d5,energy_only=c5)],
        boundaries=['all cutoffs chosen absolute keV windows, not sigma thresholds or p-values',
                    'one or zero candidates do not establish identity or newness',
                    'absolute parent window rejects real source-described reanchoring/order changes',
                    'Q1 anchor-guided candidates use source context, not blind automated discovery',
                    'R_DCO from different gates/arrays is not a universal numeric matching key',
                    'no automatic assignment or count of newly discovered gamma rays'],
        checks=checks,checks_passed=len(checks))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir',type=Path,required=True)
    p.add_argument('--receipts',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    out=audit(a.input_dir,json.loads(a.receipts.read_text()))
    a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks_passed=out['checks_passed'],all_checks_true=all(out['checks'].values()),
                          table_rows=out['table_rows_extracted'],output=str(a.output))))


if __name__=='__main__':
    main()
