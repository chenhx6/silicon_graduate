#!/usr/bin/env python3
"""Typed primary Qt table, reported analysis alternatives and provenance guards.

Conditional E2 sensitivity is not a state-lifetime reconstruction. Parenthesis
errors/accuracy percentages are never silently converted to actual sigma/CI.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02'


def qt_value(literal):
    if literal.startswith('<'):
        return dict(kind='upper_limit',bound=float(literal[1:]),value=None,quoted_uncertainty=None,coverage=None)
    m=re.fullmatch(r'(\d+\.\d+)\((\d+)\)',literal)
    if not m:raise ValueError('unknown source Qt syntax')
    places=len(m[1].split('.')[1])
    return dict(kind='finite_reported_fit',value=float(m[1]),quoted_uncertainty=int(m[2])*10**(-places),coverage=None)


def finite_value(literal):
    v=qt_value(literal)
    if v['kind']!='finite_reported_fit':raise ValueError('censored bound cannot be an ordinary value')
    return v['value']


def analysis_alternative(row):
    if row['kind'] not in ['gate_pair_b','feeding_assumption_pair_c']:
        raise ValueError('not a declared same-band analysis-alternative pair')
    a,b=map(finite_value,row['Qt_literals_eb']);scale=b/a
    return dict(id=row['id'],nucleus=row['nucleus'],configuration=row['configuration_literal_transcribed'],
                kind=row['kind'],roles=row['roles'],Qt_literals=row['Qt_literals_eb'],Qt_scale=scale,
                percent_Qt_change=100*(scale-1),
                conditional_fixed_E2_strength_scale=scale**2,
                conditional_fixed_transition_lifetime_scale=scale**-2,
                conditions='same identified E2 energy/branch and geometry; scale-only response, not measured tau',
                numeric_state_lifetime=None,point_covariance=None)


def nucleus_identity(label):
    m=re.fullmatch(r'(\d+)(Ce|Pr|Nd|Pm|Sm)',label)
    a=int(m[1]);z={'Ce':58,'Pr':59,'Nd':60,'Pm':61,'Sm':62}[m[2]]
    return dict(A=a,Z=z,N=a-z)


def channels(label):
    q=nucleus_identity(label);da,dz=140-q['A'],63-q['Z'];out=[]
    for alpha in range(6):
        proton=dz-2*alpha;neutron=da-proton-4*alpha
        if min(proton,neutron)>=0:out.append(dict(alpha=alpha,proton=proton,neutron=neutron))
    return out


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=RUN/'riley2001-global-qt-audit.json')
    args=ap.parse_args();checks={}
    def check(name,value):
        checks[name]=bool(value)
        if not value:raise AssertionError(name)
    source=json.loads((RUN/'riley2001-table-I-input.json').read_text())
    proof=json.loads((RUN/'riley2001-pdf-verification-working.json').read_text())
    pdf=Path(proof['path']);sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
    check('actual_publisher_PDF_identity',sha==source['source_pdf_sha256']==proof['sha256'])
    pages=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True).split('\f')
    check('thirteen_page_input',len(pages)-1==13)
    rows=source['rows'];check('33_unique_source_rows',len(rows)==len({r['id'] for r in rows})==33)
    numbers=[v for r in rows for v in r['Qt_literals_eb'] if not v.startswith('<')]
    printed=re.findall(r'\d+\.\d+\(\d+\)',pages[7])
    check('39_finite_tokens_in_exact_source_order',numbers==printed and len(numbers)==39)
    check('three_censored_tokens_not_finite',[v for r in rows for v in r['Qt_literals_eb'] if v.startswith('<')]==['<3.0']*3)
    nc={r['nucleus'] for r in rows};check('15_nuclides_table_subset',len(nc)==15)
    kinds=dict(Counter(r['kind'] for r in rows))
    check('typed_semantics_not_one_flat_value_set',kinds==dict(single=21,upper_limit=3,band_pair=1,signature_pair=2,gate_pair_b=5,feeding_assumption_pair_c=1))
    gates=[analysis_alternative(r) for r in rows if r['kind']=='gate_pair_b']
    feeding=[analysis_alternative(r) for r in rows if r['kind']=='feeding_assumption_pair_c']
    check('five_actual_b_comparisons',len(gates)==5 and all(8<r['percent_Qt_change']<13 for r in gates))
    check('c_alternative_not_relabelled_gate',len(feeding)==1 and feeding[0]['nucleus']=='135Sm' and feeding[0]['kind']!='gate_pair_b')
    check('conditional_strength_time_inverse',all(math.isclose(r['conditional_fixed_E2_strength_scale']*r['conditional_fixed_transition_lifetime_scale'],1) for r in gates+feeding))
    check('no_absolute_state_tau_inferred',all(r['numeric_state_lifetime'] is None for r in gates+feeding))
    for name,action in [
        ('limit_not_replaced_by_boundary_value',lambda:finite_value('<3.0')),
        ('two_bands_not_gate_alternatives',lambda:analysis_alternative(next(r for r in rows if r['kind']=='band_pair'))),
        ('signature_pair_not_gate_alternatives',lambda:analysis_alternative(next(r for r in rows if r['kind']=='signature_pair')))]:
        try:action()
        except ValueError:check(name,True)
        else:check(name,False)
    check('upper_Qt_implies_lower_normalized_time',2.5<3 and 2.5**-2>3**-2)
    # Actual reported high-gate moments, with explicitly conditional propagation.
    ref=next(r for r in rows if r['nucleus']=='133Nd' and r['kind']=='gate_pair_b')
    other=next(r for r in rows if r['nucleus']=='135Nd' and r['kind']=='gate_pair_b')
    A,B=[qt_value(x['Qt_literals_eb'][1]) for x in [ref,other]]
    qa,qb=A['value'],B['value'];sa,sb=A['quoted_uncertainty'],B['quoted_uncertainty']
    ratio=qb/qa;difference=qb-qa
    ga,gb=-qb/qa**2,1/qa
    ratio_sigma=[abs(abs(ga)*sa-abs(gb)*sb),abs(ga)*sa+abs(gb)*sb]
    diff_sigma=[abs(sa-sb),sa+sb]
    check('selected_highgate_values',qa==6.5 and qb==5.7)
    check('conditional_unknown_correlation_interval',0<=ratio_sigma[0]<math.hypot(ga*sa,gb*sb)<ratio_sigma[1])
    scale_controls=[]
    for k in [.85,1.15]:
        scale_controls.append(dict(chosen_common_Qt_scale=k,ratio=(k*qb)/(k*qa),difference=k*qb-k*qa))
    check('common_scale_cancels_ratio_not_difference',all(math.isclose(x['ratio'],ratio) and not math.isclose(x['difference'],difference) for x in scale_controls))
    offset=.5
    check('common_additive_Qt_offset_cancels_difference',math.isclose((qb+offset)-(qa+offset),difference) and not math.isclose((qb+offset)/(qa+offset),ratio))
    sys=[]
    for f in [.1,.15,.2]:
        sys.append(dict(chosen_Qt_fraction=f,conditional_tau_factor_range=[(1+f)**-2,(1-f)**-2],
                        interpretation='deterministic sensitivity, no coverage/probability/absolute lifetime'))
    check('ten_percent_control',math.isclose(1.1**2,1.21) and math.isclose(1.1**-2,.8264462809917354))
    # Source figure provenance plus necessary nominal reaction budget.
    compound=dict(beam='35Cl',target='105Pd',A=35+105,Z=17+46,N=18+59)
    check('nominal_compound_140Eu',compound['A']==140 and compound['Z']==63 and compound['N']==77)
    check('current_table_products_pass_necessary_budget',all((q:=nucleus_identity(n))['A']<=140 and q['Z']<=63 and q['N']<=77 and channels(n) for n in nc))
    check('142Sm_not_nominal_fusion_evaporation_product',not channels('142Sm') and nucleus_identity('142Sm')['A']>140)
    check('feasible_Ce_not_acquisition_proof',bool(channels('131Ce')) and bool(channels('132Ce')) and not {'131Ce','132Ce'}&nc)
    # Sign/normalization is visually verified on printed2691; text extraction
    # drops the minus glyph, so no sign is inferred from OCR alone.
    q20,q22_hf=7.,.6
    q22_r=-q22_hf/math.sqrt(2)
    qt_r=q20+math.sqrt(2/3)*q22_r;qt_hf=q20-q22_hf/math.sqrt(3)
    check('source_negative_sqrt2_normalization_reconciles_Qt',math.isclose(qt_r,qt_hf,abs_tol=1e-12))
    check('dropped_minus_changes_observable',not math.isclose(q20+q22_hf/math.sqrt(3),qt_hf))
    candidates=[dict(id=r['id'],configuration=r['configuration_literal_transcribed'],role=r['roles'][j],literal=v)
                for r in rows if r['nucleus']=='133Nd' for j,v in enumerate(r['Qt_literals_eb'])
                if qt_value(v).get('value')==3.5]
    check('same_nuclide_central_Qt_not_unique_band',len(candidates)==2)
    out=dict(kind='typed author-report TableI/conditional Qt sensitivity and provenance audit; not FITFTAU/raw-event rerun',
             source=dict(url='https://www.actaphys.uj.edu.pl/fulltext?series=Reg&vol=32&page=2683',sha256=sha,pages=13,table_locator='printed2690 TableI / PDF8'),
             rows=rows,counts=dict(source_rows=33,finite_values=39,upper_limits=3,nuclides=15,types=kinds,independent_measurements_not_counted=True),
             default_constraint=source['default_constraint'],gate_alternatives_b=gates,feeding_alternative_c=feeding,
             highgate_Nd_comparison=dict(reference_id=ref['id'],other_id=other['id'],difference_eb=difference,ratio=ratio,
                                         conditional_if_parentheses_are_sigma=dict(ratio_sigma_range=ratio_sigma,difference_sigma_range_eb=diff_sigma,
                                                                                  ratio_sigma_diagonal=math.hypot(ga*sa,gb*sb)),
                                         actual_covariance=None,quoted_error_coverage=None),
             chosen_common_scale_controls=scale_controls,chosen_Qt_error_sensitivity=sys,
             source_reported_accuracy=dict(body_absolute_stopping_plus_feeding_percent=[15,20],tablecaption_stopping_only_percent=[10,15],body_relative_percent=[5,10],formal_coverage=None),
             reaction=compound,channel_enumeration_scope='n,p,alpha only, necessary examples not measured exit assignments or an impurity audit',
             Nd133_nominal_possible_channels=channels('133Nd'),
             external_plot_data=[dict(nucleus='131Ce/132Ce',source='Riley Ref21 Clark1996, bibliography lacks page',current_table=False),dict(nucleus='142Sm',source='Riley Ref24 Hackman1998',current_table=False)],
             source_Q22_conversion=dict(Q22_HFODD='-sqrt2 Q22_Riley',source_locator='printed2691 Eq3 and normalization sentence',sign_visually_checked=True),
             Figure1_TableI_quoted_variants=[dict(nucleus='133Pr',family='ND',figure='3.4(3)',table='3.3(3)'),dict(nucleus='134Pm',family='f7/2,h9/2',figure='3.9(3)',table='3.9(2)'),dict(nucleus='135Sm',family='i13/2,c',figure='6.4(5)',table='6.4(4)')],
             figure_table_variant_scope='family-level quote comparison; identical selection/fit not established, no correction/averaging',
             ambiguous_Nd133_central_value_candidates=candidates,
             missing_inputs=['per-transition energies/spins/branch assignments for numeric tau conversion','actual centroid counts/gate/ring covariance','stopping and side-feeding response/code parameters and fullFITFTAU input','exact Figure1/TableI fit selection binding','Laird2002 final source'],
             checks=checks,check_count=len(checks),passed=all(checks.values()))
    args.output.resolve().relative_to(ROOT);args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks),passed=out['passed'],counts=out['counts'],gate_percent_changes=[x['percent_Qt_change'] for x in gates],feeding_c_percent=feeding[0]['percent_Qt_change'],Nd_ratio=ratio,Nd_difference=difference),ensure_ascii=False))
    return 0


if __name__=='__main__':raise SystemExit(main())
