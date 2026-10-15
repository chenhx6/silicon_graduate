#!/usr/bin/env python3
"""Versioned Matev2007 Qt operator/table audit, not a model or lifetime rerun.

Coefficient identities require the SAME design and estimator. Model-fit error
bars are never recast as experimental errors or an actual recovered covariance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

import numpy as np

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02'
SHA='40d485c653f2016cd6dc38ef95a7694e9ced6d09458004039b5be92541d07586'


def visual_labels():
    labels=[]
    for nl,omega in [('402','5/2'),('411','1/2'),('411','3/2'),('413','5/2'),('523','7/2'),('530','1/2'),('532','3/2'),('532','5/2'),('541','1/2')]:
        labels += [f'nu[{nl}]{omega},{sig}' for sig in ['+i','-i']]
    labels += ['nu6_1,-i','nu6_2,+i','nu6_3,-i','pi[301]1/2,+i']
    for nl,omega in [('404','9/2'),('411','3/2'),('422','3/2'),('532','5/2')]:
        labels += [f'pi[{nl}]{omega},{sig}' for sig in ['+i','-i']]
    labels += ['pi[541]1/2,-i','pi[541]3/2,+i','pi[541]3/2,-i','pi[550]1/2,-i']
    return labels


def number(literal):
    return float(literal.replace('–','-').replace('−','-'))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=RUN/'matev2007-qt-operator-audit.json')
    args=ap.parse_args();checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:raise AssertionError(name)
    proof=json.loads((RUN/'matev2007-pdf-verification.json').read_text())
    pdf=Path(proof['path']);check('actual_PDF_hash',hashlib.sha256(pdf.read_bytes()).hexdigest()==SHA)
    pages=subprocess.check_output(['pdftotext','-layout',str(pdf),'-'],text=True).split('\f')
    check('actual_fourteen_pages',len(pages)-1==14)
    check('actual_TableII_page','TABLE II:' in pages[10])
    check('operator_and_fit_markers',all(x in pages[4] for x in ['(15)','(19)','(22)']) and all(x in pages[5] for x in ['(24)','(26)','(27)','(28)']))
    a=1/math.sqrt(3);round_unit=.005
    extracted=[]
    for line in pages[10].splitlines():
        cells=re.findall(r'([–−-]?\d+\.\d+)±(\d+\.\d+)',line)
        if cells:extracted.append((line,cells))
    labels=visual_labels();check('34_visual_order_rows',len(extracted)==len(labels)==34)
    check('only3_or6_numeric_cells',all(len(cells) in [3,6] for raw,cells in extracted))
    data=[];discrepancies=[];missing=[]
    for ordinal,((raw,cells),label) in enumerate(zip(extracted,labels),1):
        for model,offset in [('CHF+SLy4',0),('CRMF+NL1',3)]:
            if offset>=len(cells):
                missing.append(dict(row=ordinal,label=label,model=model,value=None));continue
            tri=cells[offset:offset+3]
            q20,q22,qt=[number(x[0]) for x in tri]
            s20,s22,st=[number(x[1]) for x in tri]
            predicted=q20-a*q22;residue=qt-predicted
            # Necessary bound if each printed two-decimal central value is a
            # nearest-rounding interval and one shared linear estimator is used.
            central_bound=round_unit*(2+a)
            central_ok=abs(residue)<=central_bound+1e-14
            lo20,hi20=max(0,s20-round_unit),s20+round_unit
            lo22,hi22=max(0,s22-round_unit)*a,(s22+round_unit)*a
            lowest=max(0,lo20-hi22,lo22-hi20);highest=hi20+hi22
            std_ok=max(0,st-round_unit)<=highest+1e-14 and st+round_unit>=lowest-1e-14
            naive_rho=(s20*s20+a*a*s22*s22-st*st)/(2*a*s20*s22)
            entry=dict(row=ordinal,label_from_visual_order=label,model=model,source_raw_line=raw,
                       source_cell_literals=[v+'±'+s for v,s in tri],q20=q20,q22=q22,qt=qt,
                       quoted_theoretical_fit_errors=[s20,s22,st],
                       predicted_qt_if_shared_estimator=predicted,central_residual=residue,
                       assumed_two_decimal_rounding_bound=central_bound,central_rounding_compatible=central_ok,
                       naive_independent_error_qt=math.sqrt(s20*s20+a*a*s22*s22),
                       nominal_rho_if_shared_estimator=naive_rho,
                       conditional_sigma_rounding_necessary_range=[lowest,highest],
                       conditional_sigma_rounding_compatible=std_ok,
                       actual_cross_observable_covariance=None)
            data.append(entry)
            if not central_ok:discrepancies.append(dict(row=ordinal,label=label,model=model,residual=residue))
    check('61_available_triples_seven_missing',len(data)==61 and len(missing)==7)
    # Discovery is retained even if it exceeds the two visually suspected rows.
    suspected={('nu[402]5/2,+i','CHF+SLy4'),('pi[532]5/2,+i','CHF+SLy4')}
    observed={(p['label'],p['model']) for p in discrepancies}
    check('both_visual_suspicions_systematically_recovered',suspected<=observed)
    check('missing_CRMF_values_not_zero_filled',all(x['value'] is None for x in missing))
    check('fit_error_tokens_positive_not_experimental',all(min(x['quoted_theoretical_fit_errors'])>0 for x in data))

    # Independent linear algebra control, with declared nonadditive residuals.
    C=np.array([[1.,0.],[0.,1.],[1.,1.],[-1.,1.]])
    y20=np.array([.3,.4,1.1,-.2]);y22=np.array([.1,-.2,.6,.1]);yt=y20-a*y22
    fit=lambda y:np.linalg.lstsq(C,y,rcond=None)[0]
    b20,b22,bt=fit(y20),fit(y22),fit(yt)
    check('shared_design_full_rank',np.linalg.matrix_rank(C)==2)
    check('shared_OLS_coefficient_identity',np.allclose(bt,b20-a*b22,atol=1e-14))
    W=np.diag([1.,1.,4.,.5]);bt_other=np.linalg.solve(C.T@W@C,C.T@W@yt)
    check('different_estimator_control_breaks_coefficient_identity',not np.allclose(bt_other,b20-a*b22))
    # N>m alone is not enough; source also explicitly requires nonsingular B.
    singular=np.column_stack([C[:,0],2*C[:,0]])
    check('more_configurations_not_sufficient_rank',singular.shape[0]>singular.shape[1] and np.linalg.matrix_rank(singular)<2)
    axis_controls=[]
    for q0,q2 in [(4.,1.),(7.,-.5),(2.,0.)]:
        ty=q0-a*q2;tx_after=q0+a*(-q2)
        check('properly_relabelled_axis_terminal_identity_'+str(q0),math.isclose(ty,tx_after,abs_tol=1e-12))
        axis_controls.append(dict(chosen_Q20=q0,chosen_Q22=q2,Qt_y=ty,Qt_x_after_Q22_signflip=tx_after))
    family=[]
    for gamma in [-20.,0.,20.]:
        g=math.radians(gamma);Q=1/(math.cos(g)-a*math.sin(g))
        q0,q2=Q*math.cos(g),Q*math.sin(g)
        family.append(dict(chosen_gamma_degrees=gamma,Q2=Q,Q20=q0,Q22=q2,Qt_y=q0-a*q2))
    check('chosen_single_Qt_family',all(math.isclose(x['Qt_y'],1,abs_tol=1e-12) for x in family) and len({round(x['Q2'],10) for x in family})==3)
    check('common_additive_offset_difference_only',(5+.3)-(7+.3)==5-7)
    check('common_multiplicative_scale_ratio_only',math.isclose((.9*5)/(.9*7),5/7) and not math.isclose(.9*5-.9*7,5-7))
    compact=re.sub(r'\s+','',pages[6]);blocks=re.findall(r'\[(\d+),(\d+),(\d+),(\d+)\]([np])',compact)
    numbers={kind:sum(map(int,nums)) for *nums,kind in blocks}
    check('actual_reference_occupation_blocks',numbers=={'n':73,'p':58})
    check('actual_odd_A_reference_not_Pr_reference',sum(numbers.values())==131 and sum(numbers.values())%2==1)
    check('core_label_version_boundary_retained','131Cs' in re.sub(r'\s+','',pages[8]) and '131Ce' in compact)
    jlines=[]
    for needle in ['4.78±0.08','3.42±0.11']:
        found=[line for line in pages[11].splitlines() if needle in line]
        if len(found)!=1:raise ValueError('TableIII intruder row needs visual inspection')
        cells=re.findall(r'([–−-]?\d+\.\d+)±(\d+\.\d+)',found[0])
        jlines.append(dict(raw=found[0],values=[number(x[0]) for x in cells],error_literals=[x[1] for x in cells]))
    check('actual_TableIII_intruder_rows',jlines[0]['values']==[4.78,4.59] and jlines[1]['values']==[3.42,3.15])
    exchange=[]
    for model,col in [('CHF+SLy4',0),('CRMF+NL1',1)]:
        one=next(x for x in data if x['label_from_visual_order']=='nu6_1,-i' and x['model']==model)
        two=next(x for x in data if x['label_from_visual_order']=='nu6_2,+i' and x['model']==model)
        exchange.append(dict(model=model,declared_occupation_changes={'nu6_1,-i':-1,'nu6_2,+i':1},
                             neutron_number_change=0,intruder_count_change=0,
                             predicted_delta_Qt_eb=two['qt']-one['qt'],
                             predicted_delta_J_hbar=jlines[1]['values'][col]-jlines[0]['values'][col],
                             coefficient_covariance=None,actual_configuration_run=False,
                             kind='nominal additive application, not a measured spin or isotopic-N trend'))
    out=dict(kind='versioned source Qt/table/operator audit plus declared linear-estimator controls; no lifetime or selfconsistent-model rerun',
             source=dict(doi='10.1103/PhysRevC.76.034304',arxiv='0707.4324v1',sha256=SHA,pages=14,raw_archived=False),
             audited_operator='terminal Eq15 Qt_y=Q20-Q22/sqrt3; Eq14 right-end Qt_x=Q20+Q22/sqrt3',
             conditions=['same operator frame','same design/configuration set and linear estimator/weights','nearest rounding to two decimals for interval audit'],
             actual_table_rows=data,missing_cells=missing,conditional_central_discrepancies=discrepancies,
             conditional_sigma_interval_failures=[dict(row=x['row'],model=x['model']) for x in data if not x['conditional_sigma_rounding_compatible']],
             note='No author code-error verdict or replacement table values; actual C/weights/residuals and VOR unavailable',
             declared_estimator_control=dict(C=C.tolist(),y20=y20.tolist(),y22=y22.tolist(),shared_b20=b20.tolist(),shared_b22=b22.tolist(),shared_bt=bt.tolist(),different_weight_bt=bt_other.tolist()),
             declared_axis_controls=axis_controls,chosen_Qt1_inverse_family=family,
             source_reference_blocks=numbers,
             declared_intruder_exchange=exchange,source_TableIII_intruder_lines=jlines,
             version_boundaries=['Eq14 middle superscript omega||y in x-axis context','p9 core label131Cs vs p7 131Ce/occupation blocks','Fig4 inset label/body142Sm vs caption132Sm','Eq33 printed CG amplitude without visible square; notused for rate extraction','TableI pi404 p/h vs occupied reference text; notused to reconstruct actual C'],
             missing_inputs=['actual configuration design and calculated operator ensemble','weights/cross-observable covariance','publisher VOR/erratum verification','original Laird2002 lifetime/Qt analysis'],
             checks=checks,check_count=len(checks),passed=all(checks.values()))
    args.output.resolve().relative_to(ROOT);args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks),passed=True,triples=len(data),discrepancies=discrepancies,sigma_interval_failures=out['conditional_sigma_interval_failures'],reference=numbers),ensure_ascii=False))
    return 0


if __name__=='__main__':raise SystemExit(main())
