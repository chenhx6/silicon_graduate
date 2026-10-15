#!/usr/bin/env python3
"""Versioned 136Pr fields and a declared two-line flow identifiability test.

This is a fixed-column ENSDF SUBSET reader; expressions, limits, flags and
unplaced gammas stay literal. Flow/tag controls assume zero IC and a specified
observed subnetwork. They neither establish completeness nor re-fit the data.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import re
import subprocess
from fractions import Fraction
from pathlib import Path

from day14_ensdf_crosswalk import number, uncertainty


def ensdf_subset(path,nuclide):
    lines=path.read_text().splitlines()
    levels,gammas=[],[]
    level,gamma=None,None
    for n,raw in enumerate(lines,1):
        row=raw.ljust(80)
        if row[:5].strip()!=nuclide.upper().strip():
            continue
        if row[5:7]=='  ' and row[7]=='L':
            level=dict(line=n,energy_text=row[9:19].strip(),
                       E=number(row[9:19]),dE=uncertainty(row[9:19],row[19:21]),
                       Jpi=row[21:39].strip(),T_text=row[39:49].strip(),
                       T_error_text=row[49:55].strip(),raw=raw,continuations=[])
            levels.append(level)
            gamma=None
        elif row[5:7]=='  ' and row[7]=='G':
            gamma=dict(line=n,parent_line=None if level is None else level['line'],
                       parent_E=None if level is None else level['E'],
                       energy_text=row[9:19].strip(),E=number(row[9:19]),
                       dE=uncertainty(row[9:19],row[19:21]),
                       RI=number(row[21:29]),dRI=uncertainty(row[21:29],row[29:31]),
                       RI_error_or_limit=row[29:31].strip(),
                       M=row[31:41].strip(),MR_text=row[41:49].strip(),
                       MR_error_or_limit=row[49:55].strip(),CC=number(row[55:62]),
                       flag=row[76:77].strip(),raw=raw,continuations=[])
            gammas.append(gamma)
        elif row[7]=='G' and gamma is not None:
            gamma['continuations'].append(dict(line=n,raw=raw))
        elif row[7]=='L' and level is not None:
            level['continuations'].append(dict(line=n,raw=raw))
    return dict(lines=lines,levels=levels,gammas=gammas)


def unique(items,**wanted):
    matches=[x for x in items if all(x[k]==v for k,v in wanted.items())]
    if len(matches)!=1:
        raise ValueError('ambiguous/missing record '+repr(wanted))
    return matches[0]


def ledger(top,bottom,extra=Fraction(0)):
    T,B=map(Fraction,(top,bottom))
    feed=max(B-T,0)+extra
    loss=max(T-B,0)+extra
    return dict(top=T,bottom=B,feeding=feed,unobserved_loss=loss,
                total_out=B+loss,loss_fraction=loss/(B+loss))


def projected_categories(top_name,low_flow,high_flow):
    """Observed 263/405 photon sets, plus parent-tag eligibility.

    Low/high here mean photon ENERGY, not position in the cascade. The shared
    pair rate is min(flow). Excess of the top line represents an unseen exit;
    excess of the bottom line represents direct middle feeding. Neither unseen
    route is asserted to be present in the experiment.
    """
    flows={'263':Fraction(low_flow),'405':Fraction(high_flow)}
    bottom_name='405' if top_name=='263' else '263'
    pair=min(flows.values())
    categories=[dict(rate=pair,photons=('263','405'),parent_entry=True)]
    for name,flow in flows.items():
        if flow>pair:
            categories.append(dict(rate=flow-pair,photons=(name,),
                                   parent_entry=(name==top_name)))
    return categories,ledger(flows[top_name],flows[bottom_name])


def observed_distribution(categories,eps263=Fraction(1,10),eps405=Fraction(2,25),
                          tag_efficiency=Fraction(0)):
    out={bits:Fraction(0) for bits in itertools.product((0,1),repeat=3)}
    total=sum(x['rate'] for x in categories)
    for cat in categories:
        probabilities=[eps263 if '263' in cat['photons'] else Fraction(0),
                       eps405 if '405' in cat['photons'] else Fraction(0),
                       tag_efficiency if cat['parent_entry'] else Fraction(0)]
        for bits in out:
            prob=cat['rate']/total
            for bit,p in zip(bits,probabilities):
                prob*=p if bit else 1-p
            out[bits]+=prob
    return out


def json_fraction(value):
    if isinstance(value,Fraction):
        return dict(exact=str(value),value=float(value))
    if isinstance(value,dict):
        return {str(k):json_fraction(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [json_fraction(v) for v in value]
    return value


def audit(input_dir,receipts):
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise AssertionError(name)
    parsed={}
    for label in ('adopted','pd30si'):
        path=input_dir/(label+'.ensdf')
        rec=next(x for x in receipts['objects'] if x['label']==label)
        check('actual_object_hash_'+label,hashlib.sha256(path.read_bytes()).hexdigest()==rec['text_sha256'])
        parsed[label]=ensdf_subset(path,'136PR')
        check('actual_201810_cut2018_'+label,'201810' in parsed[label]['lines'][1]
              and '1-Apr-2018' in parsed[label]['lines'][2])
    reaction=parsed['pd30si']
    adopted=parsed['adopted']
    unplaced=[g for g in reaction['gammas'] if g['parent_line'] is None]
    check('leading_unplaced_gamma_not_attached_to_ground',len(unplaced)==1
          and unplaced[0]['E']==311.7 and unplaced[0]['line']==37)
    g263=unique(reaction['gammas'],parent_E=3677.7,E=262.9)
    g405=unique(reaction['gammas'],parent_E=3414.8,E=404.9)
    check('old_top263_RI_and_error_literal',g263['RI']==25.7 and g263['dRI']==.5)
    check('old_lower405_RI_and_error_literal',g405['RI']==27.6 and g405['dRI']==.3)
    check('old_CC_and_MR_missing_not_zero',all(g['CC'] is None and g['MR_text']==''
                                             for g in (g263,g405)))
    for g in (g263,g405):
        lev=unique(reaction['levels'],line=g['parent_line'])
        check('old_reaction_tentative_parity_'+str(g['E']),'(-)' in lev['Jpi'])
    for E,J in ((3677.6,'(15)'),(3414.7,'(14)'),(3009.8,'(13)')):
        check('adopted_retains_weaker_no_parity_'+str(E),unique(adopted['levels'],E=E)['Jpi']==J)
    ag263=unique(adopted['gammas'],parent_E=3677.6,E=262.9)
    ag405=unique(adopted['gammas'],parent_E=3414.7,E=404.9)
    check('adopted_each_parent_RI100_not_global_same_flow',ag263['RI']==ag405['RI']==100)
    lim=unique(reaction['gammas'],parent_E=2528.7,E=617.)
    check('upper_limit_qualifier_preserved_not_symmetric_error',
          lim['RI']==1 and lim['RI_error_or_limit']=='LT' and lim['dRI'] is None)
    anomaly=unique(reaction['gammas'],parent_E=1803.,E=754.4)
    check('compiler_perhaps_typo_comment_literal',any('perhaps is typo' in c['raw']
          for c in anomaly['continuations']))
    source=Path('knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md').read_text()
    raw=Path(re.search(r'^raw_file: "(.*)"$',source,re.M).group(1))
    sha=re.search(r'^raw_sha256: (\S+)',source,re.M).group(1)
    check('accepted_copy_raw_hash',hashlib.sha256(raw.read_bytes()).hexdigest()==sha)
    pp=subprocess.check_output(['pdftotext','-layout',str(raw),'-'],text=True).split('\f')
    newrows=[]
    for energy,parent,RI,dRI in [('263.1(2)','3273.3(10)','18.8(7)',.7),
                                ('405.1(1)','3678.4(10)','14.9(7)',.7)]:
        pattern=r'^\s*'+re.escape(energy)+r'\s+'+re.escape(parent)+r'\s+'+re.escape(RI)+r'.*$'
        rows=re.findall(pattern,pp[6],re.M)
        check('new_direct_table_literal_'+energy,len(rows)==1 and 'M1+E2' in rows[0])
        newrows.append(dict(energy=energy,parent=parent,RI=RI,dRI=dRI,raw=rows[0]))
    # Same current endpoints/energies; the alternate middle is a CONTROL,
    # explicitly distinct from the legacy evaluator's 3414.8-keV value.
    top=Fraction('3678.4');end=Fraction('3010.2')
    check('current_energy_closure_both_orders_exact',
          top-end==Fraction('263.1')+Fraction('405.1'))
    middles={'405_first':top-Fraction('405.1'),'263_first_control':top-Fraction('263.1')}
    check('current_middle3273point3_vs_control3415point3',
          middles=={'405_first':Fraction('3273.3'),'263_first_control':Fraction('3415.3')})
    check('control_middle_not_legacy_literal',middles['263_first_control']!=Fraction('3414.8'))
    cases=[]
    for name,Il,Ih,favored in [('new2025',Fraction('18.8'),Fraction('14.9'),'405'),
                               ('old2018reaction',Fraction('25.7'),Fraction('27.6'),'263')]:
        c1,L1=projected_categories('263',Il,Ih)
        c2,L2=projected_categories('405',Il,Ih)
        for top_name,cat,L in [('263',c1,L1),('405',c2,L2)]:
            check(name+'_positive_ledger_'+top_name,
                  L['top']+L['feeding']==L['bottom']+L['unobserved_loss']
                  and L['feeding']>=0 and L['unobserved_loss']>=0)
            shifted=ledger(L['top'],L['bottom'],extra=Fraction(5))
            check(name+'_continuous_feed_loss_family_'+top_name,
                  shifted['top']+shifted['feeding']==shifted['bottom']+shifted['unobserved_loss'])
        favored_L=L1 if favored=='263' else L2
        inverse_L=L2 if favored=='263' else L1
        check(name+'_no_loss_control_prefers_reported_order',
              favored_L['unobserved_loss']==0 and inverse_L['unobserved_loss']>0)
        untag1=observed_distribution(c1)
        untag2=observed_distribution(c2)
        check(name+'_all_observed_two_line_detection_cells_identical',untag1==untag2)
        check(name+'_normalized_observed_cells',sum(untag1.values())==1)
        tagged1=observed_distribution(c1,tag_efficiency=Fraction(7,100))
        tagged2=observed_distribution(c2,tag_efficiency=Fraction(7,100))
        tv=sum(abs(tagged1[k]-tagged2[k]) for k in tagged1)/2
        check(name+'_known_parent_entry_tag_breaks_constructed_equivalence',tv>0)
        check(name+'_tag_difference_exact_bound',tv==abs(Il-Ih)/max(Il,Ih)*Fraction(7,100))
        cases.append(dict(case=name,photon_flow_263=Il,photon_flow_405=Ih,
                          favored_no_loss_order=favored+'_first',
                          ledger_263first=L1,ledger_405first=L2,
                          event_categories_263first=c1,event_categories_405first=c2,
                          untagged_cell_distribution=untag1,
                          tagged_cells_263first=tagged1,tagged_cells_405first=tagged2,
                          TV_tag_control=tv))
    check('new_reversed_zeroIC_min_loss_fraction_39over188',
          cases[0]['ledger_263first']['loss_fraction']==Fraction(39,188))
    check('old_reversed_zeroIC_min_loss_fraction_19over276',
          cases[1]['ledger_405first']['loss_fraction']==Fraction(19,276))
    equal1,_=projected_categories('263',Fraction(10),Fraction(10))
    equal2,_=projected_categories('405',Fraction(10),Fraction(10))
    check('equal_flow_tag_does_not_create_branch_discriminator',
          observed_distribution(equal1,tag_efficiency=Fraction(1))==
          observed_distribution(equal2,tag_efficiency=Fraction(1)))
    # Current 495.4 link is an actual possible parent selector; using it as
    # the unique parent-entry tag and its efficiency 0.07 are NOT source facts.
    check('actual495point4_parent_entry_link_in_published_table',
          re.search(r'^\s*495\.4\(2\)\s+4173\.8\(10\)',pp[6],re.M) is not None)
    return json_fraction(dict(
        actual_objects={x['label']:x['text_sha256'] for x in receipts['objects']},
        parser_scope='fixed primary L/G columns and literal continuations only, not full ENSDF interpretation',
        actual_old_selected_gammas=[g263,g405],actual_new_selected_rows=newrows,
        unplaced_records=unplaced,current_control_middles=middles,cases=cases,
        IC_input_contract='Use F_j=I_gamma,j(1+alpha_j). alpha/delta and unseen inventory unknown; zero IC above is a declared control.',
        delta_uncertainty_contract='Var(I263-I405)=s263^2+s405^2-2Cov263405; covariance unknown; no significance calculated.',
        boundaries=['different campaign/normalization rows never merged into one flow dataset',
                    'hidden-loss fractions are conditional mathematical minima, not experimental branching limits',
                    'equivalence applies to the selected two-line event projection, not every spectrum in the paper',
                    'independent parent tag distinguishes this constructed pair; does not prove global order identifiability with arbitrary unknown feeding/calibration',
                    'no actual order choice, source-error verdict, absolute strength or L4 event replay'],
        checks=checks,checks_passed=len(checks)))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input-dir',type=Path,required=True)
    p.add_argument('--receipts',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    result=audit(a.input_dir,json.loads(a.receipts.read_text()))
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks_passed=result['checks_passed'],
                          all_checks_true=all(result['checks'].values()),output=str(a.output))))


if __name__=='__main__':
    main()
