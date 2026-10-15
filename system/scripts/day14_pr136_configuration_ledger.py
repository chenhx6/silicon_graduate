#!/usr/bin/env python3
"""Literal Table-II count audit; not a reconstruction of the TAC-CDFT state.

Only LISTED powers are summed. Missing terms stay unlisted, not measured zero.
The pair-completion test is CONDITIONAL on the column being a complete list
above an even paired reference. Species tests assume like-particle pairs;
the total-number parity condition also applies to proton-neutron pairs.
Active-only labels or unlisted spectators
require an additional input contract; no orbital is silently inserted.
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


PARITY={'gd':1,'sd':1,'h11/2':-1,'h9/2':-1,'f7/2':-1}


def normalized_orbital(literal):
    base=literal.split(';')[0]
    return {'g7/2d5/2':'gd','s1/2d3/2':'sd'}.get(base,base)


def parse_species(literal):
    compact=re.sub(r'\s+','',literal)
    terms=[]
    position=0
    for m in re.finditer(r'\(([^()]*)\)([−-]?\d+)',compact):
        if m.start()!=position:
            raise ValueError('unparsed text before orbital '+compact[position:m.start()])
        key=normalized_orbital(m[1])
        if key not in PARITY:
            raise ValueError('orbital parity not specified: '+m[1])
        n=int(m[2].replace('−','-'))
        terms.append(dict(orbital_literal=m[1],group_for_counting=key,power=n,
                          assumed_good_orbital_parity=PARITY[key]))
        position=m.end()
    if not terms or position!=len(compact):
        raise ValueError('unsupported/incomplete orbital string '+literal)
    return terms


def parse_configuration(literal):
    # The tensor separator alone defines the species columns. Omega annotations
    # remain literal, and are irrelevant to the integer number-parity test.
    compact=re.sub(r'\s+','',literal)
    parts=compact.split('⊗')
    if len(parts)!=2 or not parts[0].startswith('π') or not parts[1].startswith('ν'):
        raise ValueError('unsupported proton/neutron notation '+literal)
    return dict(p=parse_species(parts[0][1:]),n=parse_species(parts[1][1:]))


def listed_summary(terms):
    signed=sum(t['power'] for t in terms)
    absolute=sum(abs(t['power']) for t in terms)
    parity=1
    for term in terms:
        if abs(term['power'])%2:
            parity*=term['assumed_good_orbital_parity']
    return dict(listed_signed_power_sum=signed,listed_particle_hole_terms_count=absolute,
                listed_number_parity=signed%2,label_spatial_parity_product=parity)


def actual_table_rows(page):
    body=page.split('TABLE II.',1)[1]
    rows=[]
    started=False
    for line in body.splitlines():
        if started and not line.strip():
            break  # Do not parse the Fig16 legend's Config* names as table rows.
        if re.match(r'^\s*Config[DQ]',line):
            cells=re.split(r'\s{2,}',line.strip())
            if len(cells)!=4:
                raise ValueError('wrapped or malformed TableII row needs source inspection')
            rows.append(dict(name=cells[0].replace('∗','*'),source_name_literal=cells[0],
                             valence_literal=cells[1],unpaired_literal=cells[2],
                             deformation_literal=cells[3],source_raw_line=line))
            started=True
    return rows


def audit():
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise AssertionError(name)
    source=Path('knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md').read_text()
    raw=Path(re.search(r'^raw_file: "(.*)"$',source,re.M).group(1))
    sha=re.search(r'^raw_sha256: (\w+)',source,re.M).group(1)
    check('actual_accepted_copy_hash',hashlib.sha256(raw.read_bytes()).hexdigest()==sha)
    pages=subprocess.check_output(['pdftotext','-layout',str(raw),'-'],text=True).split('\f')
    rows=actual_table_rows(pages[14])
    check('tableII_ten_rows_not_legend_duplicates',len(rows)==10 and len(set(x['name'] for x in rows))==10)
    check('correct_valence_and_unpaired_column_headers',
          'Valence-nucleon configuration' in pages[14]
          and 'Unpaired-nucleon configuration' in pages[14])
    target={'p':9,'n':-5}
    results=[]
    for row in rows:
        v=parse_configuration(row['valence_literal'])
        u=parse_configuration(row['unpaired_literal'])
        sv={s:listed_summary(v[s]) for s in ('p','n')}
        su={s:listed_summary(u[s]) for s in ('p','n')}
        delta={s:sv[s]['listed_signed_power_sum']-su[s]['listed_signed_power_sum']
               for s in ('p','n')}
        omitted={s:{key:None for key in {x['group_for_counting'] for x in v[s]}
                    -{x['group_for_counting'] for x in u[s]}} for s in ('p','n')}
        check(row['name']+'_valence_Z59_N77_relative_to_50_82',
              all(sv[s]['listed_signed_power_sum']==target[s] for s in ('p','n')))
        check(row['name']+'_holes_numberparity_signed_equals_absolute',
              all(su[s]['listed_signed_power_sum']%2==su[s]['listed_particle_hole_terms_count']%2
                  for s in ('p','n')))
        vPi=sv['p']['label_spatial_parity_product']*sv['n']['label_spatial_parity_product']
        uPi=su['p']['label_spatial_parity_product']*su['n']['label_spatial_parity_product']
        check(row['name']+'_positive_label_spatial_parity_both_columns',vPi==uPi==1)
        # This boolean is a necessary condition under a stated interpretation,
        # not a validation of the actual state when it returns True.
        passes=all(delta[s]%2==0 for s in ('p','n'))
        total_passes=sum(delta.values())%2==0
        count=sum(su[s]['listed_particle_hole_terms_count'] for s in ('p','n'))
        results.append(dict(**row,valence_terms=v,unpaired_listed_terms=u,
                            valence_summary=sv,unpaired_listed_summary=su,
                            unlisted_valence_groups_not_zero_filled=omitted,
                            residual_if_column_complete=delta,
                            pair_completion_numberparity_necessary_condition=passes,
                            any_two_fermion_pair_completion_total_parity_necessary_condition=total_passes,
                            listed_unpaired_absolute_count=count,
                            total_I_class_if_complete_even_paired_reference=('integer' if count%2==0 else 'half-integer'),
                            actual_blocked_configuration=None,actual_reference_or_spectators=None))
    fails=[x['name'] for x in results if not x['pair_completion_numberparity_necessary_condition']]
    check('Q1_and_Q1star_fail_only_complete_list_interpretation',fails==['ConfigQ1','ConfigQ1*'])
    for name in fails:
        row=next(x for x in results if x['name']==name)
        check(name+'_literal_unpaired_neutron_sum_zero_not_minusfive',
              row['unpaired_listed_summary']['n']['listed_signed_power_sum']==0)
        check(name+'_sd_absence_retained_as_unlisted',
              row['unlisted_valence_groups_not_zero_filled']['n'].get('sd','missing') is None)
        check(name+'_odd_neutron_residual',row['residual_if_column_complete']['n']==-5)
        check(name+'_odd_total_residual_not_fixed_even_with_pn_pairs',
              sum(row['residual_if_column_complete'].values())==1
              and not row['any_two_fermion_pair_completion_total_parity_necessary_condition'])
        check(name+'_listed5fermions_half_integer_only_if_complete',
              row['listed_unpaired_absolute_count']==5
              and row['total_I_class_if_complete_even_paired_reference']=='half-integer')
        # A symbolic unknown ODD spectator changes number parity. It is not
        # identified with an orbital or inserted into the source configuration.
        residual=row['residual_if_column_complete']['n']
        check(name+'_abstract_odd_spectator_can_restore_necessary_mod2',
              all((residual-k)%2==0 for k in (-3,-1,1,3)))
        check(name+'_additional_pairs_alone_never_fix_odd_residual',
              all((residual-2*k)%2==1 for k in range(-5,6)))
    generators=((2,0),(0,2),(1,1))
    check('all_like_and_pn_pair_generators_preserve_total_numberparity',
          all((p+n)%2==0 for p,n in generators))
    check('species_even_residual_is_not_general_when_pn_pairing_allowed',
          generators[2]==(1,1) and generators[2][0]%2==generators[2][1]%2==1)
    # Figure captions list different amounts of active structure. Number parity
    # does not settle the identity difference: both caption strings can pass.
    caption10=re.search(r'FIG\. 10\.(.*?)\n\s*\n',pages[10],re.S).group(1)
    caption9=re.search(r'FIG\. 9\.(.*?)\n\s*\n',pages[10],re.S).group(1)
    cap_configs={
        'D4_caption':('π(h11/2;Ω≈3/2 )1 ⊗ ν(h11/2;Ω≈11/2 )−1',caption9,'ConfigD4'),
        'D6_caption':('π(g7/2 d5/2 )4 (h11/2 )1 ⊗ ν(h11/2 )−1',caption10,'ConfigD6')}
    caps=[]
    for name,(literal,caption,table_name) in cap_configs.items():
        check(name+'_source_caption_literal_verified',
              re.sub(r'\s+','',literal) in re.sub(r'\s+','',caption))
        terms=parse_configuration(literal)
        sums={s:listed_summary(terms[s]) for s in ('p','n')}
        allowed=all((target[s]-sums[s]['listed_signed_power_sum'])%2==0 for s in ('p','n'))
        listed=sum(sums[s]['listed_particle_hole_terms_count'] for s in ('p','n'))
        table=next(x for x in results if x['name']==table_name)
        check(name+'_parity_condition_does_not_resolve_caption_table_blocking',
              allowed and listed!=table['listed_unpaired_absolute_count'])
        caps.append(dict(name=name,source_literal=literal,listed_count=listed,
                         source_caption=caption,necessary_mod2_passes=allowed,
                         table_listed_count=table['listed_unpaired_absolute_count'],
                         physical_equivalence=None))
    # SINGLE-species like-particle pairing toy: <N>=77 still has even N support.
    # Not the author's state. With pn pairing, only TOTAL fermion parity is the
    # universal condition; an individual species parity need not be fixed.
    support=(76,78)
    probabilities=(Fraction(1,2),Fraction(1,2))
    mean=sum(p*n for p,n in zip(probabilities,support))
    number_parity=sum(p*((-1)**n) for p,n in zip(probabilities,support))
    projection_to77=sum(p for p,n in zip(probabilities,support) if n==77)
    check('toy_even_vacuum_mean77_does_not_fix_odd_number_sector',
          mean==77 and number_parity==1 and projection_to77==0)
    for blocked in range(6):
        support_all=[70+blocked+2*sum(bits) for bits in itertools.product((0,1),repeat=4)]
        check('paired_superposition_keeps_blocked_numberparity_'+str(blocked),
              all(n%2==blocked%2 for n in support_all))
    check('passing_mod2_does_not_fill_actual_input',
          all(x['actual_blocked_configuration'] is None and x['actual_reference_or_spectators'] is None
              for x in results))
    return dict(
        source=dict(path='knowledge/sources/lv-2025-136pr-tac-covariant-density-functional.md',
                    locator='acceptedPDF15 TableII; acceptedPDF11 Figs9/10captions',
                    actual_pdf_sha256=sha),
        chosen_count_reference=dict(Zcore=50,Ncore=82,Ztarget=59,Ntarget=77),
        interpretation_tested='ONLY IF the unpaired column is a COMPLETE inventory above an even reference; species criterion for like-particle pairs, total parity criterion for any two-fermion pairs',
        table_results=results,failed_complete_list_interpretation=fails,caption_comparisons=caps,
        toy_pair_vacuum=dict(number_support=support,probabilities=['1/2','1/2'],
                             meanN=str(mean),mean_number_parity=str(number_parity),probability_N77=str(projection_to77),
                             pairing_scope='single species with like-particle pairs only; not a general pn-paired vacuum'),
        boundaries=['unlisted groups are not measured zero; no spectator orbital is inserted',
                    'species-even residuals presume like-particle pairing; general pn pairing preserves total fermion parity instead',
                    'passing number parity is necessary only, not proof of capacity/blocking/pairing/wavefunction validity',
                    'failing this COMPLETE-LIST reading does not establish a bug in actual TAC-CDFT code',
                    'good label spatial parity does not substitute for species number-parity audit or measured Q1 parity',
                    'unprojected <I> is not required to be an integer; the complete-even-reference I-class statement concerns a projected physical sector',
                    'actual reference, occupied/blocked orbitals and omitted spectator convention remain unavailable'],
        checks=checks,checks_passed=len(checks))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    out=audit()
    a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks_passed=out['checks_passed'],all_checks_true=all(out['checks'].values()),
                          conditional_incomplete_lists=out['failed_complete_list_interpretation'],output=str(a.output))))


if __name__=='__main__':
    main()
