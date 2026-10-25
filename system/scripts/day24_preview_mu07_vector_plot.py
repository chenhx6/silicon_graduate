#!/usr/bin/env python3
"""Read literal author TeX/vector coordinates; never execute PostScript/TeX.

This reduces graphical transcription error only. No line/parent identity,
experimental producer, uncertainty coverage or new acquisition is inferred.
"""
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import re


NUMBER=r'-?\d+(?:\.\d+)?'
CIRCLE=re.compile(rf'^n ({NUMBER}) ({NUMBER}) ({NUMBER}) ({NUMBER}) 0 360 EARC s$',re.M)
VERTICAL=re.compile(rf'^n\s*\n({NUMBER}) ({NUMBER}) m\s*\n({NUMBER}) ({NUMBER}) l\s*\ns$',re.M)


def central(raw):
    return float(raw.split('(')[0])


def table_rows(tex):
    band=None;rows=[]
    for line_number,line in enumerate(tex.splitlines(),1):
        if 'multicolumn{3}{c}{Band A}' in line:band='A'
        if 'multicolumn{3}{c}{Band B}' in line:band='B'
        m=re.search(r'\\frac\s*\{(\d+)\}\{2\}',line)
        if m and '&' in line:
            values=re.findall(r'\d+(?:\.\d+)?\(\d+\)',line)
            if len(values)!=3 or band is None:raise ValueError('Unexpected TableI row structure')
            rows.append({'band':band,'two_I':int(m.group(1)),'tex_line':line_number,
                         'mean_tau_ps_raw':values[0],'B_M1_muN2_raw':values[1],'B_E2_e2b2_raw':values[2]})
    return rows


def transformed(y,zero,one,value):
    return (Fraction(y)-Fraction(zero))/(Fraction(one)-Fraction(zero))*Fraction(value)


def coordinate_sensitivity(y,zero,one,value):
    e=Fraction(1,20000)  # Explicit four-decimal nearest-rounding design.
    points=[transformed(Fraction(y)+s0*e,Fraction(zero)+s1*e,Fraction(one)+s2*e,value)
            for s0,s1,s2 in itertools.product([-1,1],repeat=3)]
    return [float(min(points)),float(max(points))]


def parse_plot(path,kind,rows):
    source=path.read_text();page=source.split('%%Page: 1 1',1)[1]
    data_zone=page.split('(Band A) show',1)[0]
    circles=list(CIRCLE.finditer(data_zone));all_circles=list(CIRCLE.finditer(page))
    if len(circles)!=4 or len(all_circles)!=5:raise ValueError('Data/legend marker count changed')
    if kind=='M1':x0,x1,zero,one,value='0.1500','1.2500','0.1000','0.2889','1'
    else:x0,x1,zero,one,value='0.1600','1.2500','0.1000','0.2545','.1'
    data=[]
    block_start=data_zone.rfind('Color4 SC',0,circles[0].start())
    error_block=data_zone[block_start:circles[0].start()]
    strokes=list(VERTICAL.finditer(error_block))
    for circle in circles:
        x,y,rx,ry=circle.groups()
        spin=13+(float(x)-float(x0))/(float(x1)-float(x0))*10
        two_i=int(round(2*spin))
        bars=[]
        for line in strokes:
            sx,sy,ex,ey=line.groups()
            if abs(float(sx)-float(x))<1e-10 and sx==ex and abs(float(sy)-float(y))<1e-10:
                bars.append(ey)
        if len(bars)!=2:raise ValueError('Expected two literal vertical errorbar segments')
        lower,upper=sorted(bars,key=float)
        point=float(transformed(y,zero,one,value))
        den=next(r for r in rows if r['band']=='B' and r['two_I']==two_i)
        den_raw=den['B_M1_muN2_raw' if kind=='M1' else 'B_E2_e2b2_raw']
        data.append({'plotted_I_coordinate':spin,'nearest_two_I':two_i,
                     'source_coordinate_strings':{'x':x,'y':y,'radius_x':rx,'radius_y':ry,'error_y_low':lower,'error_y_high':upper},
                     'drawn_B_centre':point,'drawn_errorbar_endpoints':[float(transformed(lower,zero,one,value)),float(transformed(upper,zero,one,value))],
                     'declared_four_decimal_coordinate_sensitivity':coordinate_sensitivity(y,zero,one,value),
                     'conditional_TableI_B_denominator_raw':den_raw,
                     'conditional_out_over_in_if_same_parent_component':point/central(den_raw),
                     'source_line':source[:source.find(circle.group(0))].count('\n')+1,
                     'boundary':'Rounded author-vector plot coordinate, not original unrounded experimental data. Errorbar coverage/jointCov and gamma parent/daughter/component mapping are not supplied.'})
    checks={'four_data_one_legend_markers':True,
            'frame_and_calibration_commands_present':all(t in data_zone for t in [f'{x0} {zero} m',f'{x1} {zero} l',f'{x0} {one} m']),
            'major_axis_value_label_present':f'({value[1:] if value.startswith(".") else value}) show' in page if kind=='M1' else '(0.1) show' in page,
            'x_axis_13_and_23_labels_present':'(13) show' in page and '(23) show' in page,
            'four_plotted_halfspins':all(abs(r['plotted_I_coordinate']-i)<.001 for r,i in zip(data,[15.5,16.5,17.5,18.5])),
            'positive_data_and_bracketing_drawn_bars':all(r['drawn_errorbar_endpoints'][0]<r['drawn_B_centre']<r['drawn_errorbar_endpoints'][1] for r in data),
            'declared_rounding_envelopes_contain_literal_centres':all(r['declared_four_decimal_coordinate_sensitivity'][0]<=r['drawn_B_centre']<=r['declared_four_decimal_coordinate_sensitivity'][1] for r in data)}
    return {'kind':kind,'units':'muN2' if kind=='M1' else 'e2b2','calibration':{'x_I13':x0,'x_I23':x1,'y_B0':zero,'y_Breference':one,'B_reference':value},
            'rows':data,'controls':checks}


def calculate(source_root):
    allowed={'fig1.ps','fig2.ps','fig3.ps','fig4.ps','ndchiralrev4.bbl','ndchiralrev4.tex'}
    if {p.name for p in source_root.iterdir()}!=allowed:raise ValueError('Unexpected archive member names')
    tex=(source_root/'ndchiralrev4.tex').read_text();rows=table_rows(tex)
    expected={'A':[(29,'1.00(5)','3.2(2)','0.32(2)'),(31,'0.75(8)','2.5(3)','0.32(3)'),(33,'0.44(2)','2.2(2)','0.32(3)'),
                   (35,'0.28(2)','2.4(3)','0.32(3)'),(37,'0.23(2)','1.7(3)','0.32(4)'),(39,'0.22(2)','2.1(3)','0.13(3)'),
                   (41,'0.18(2)','2.1(3)','0.19(3)'),(43,'0.16(2)','2.0(3)','0.21(4)')],
              'B':[(31,'1.46(2)','2.7(3)','0.28(3)'),(33,'0.87(6)','2.1(2)','0.28(3)'),(35,'0.64(5)','2.2(2)','0.28(4)'),
                   (37,'0.48(3)','1.7(2)','0.29(4)'),(39,'0.24(4)','1.9(3)','0.11(3)')]}
    controls={'safe_extracted_expected_regular_files_only':True,'thirteen_TableI_rows':len(rows)==13,
              'TeX_TableI_matches_journal_literal_rows':all([(r['two_I'],r['mean_tau_ps_raw'],r['B_M1_muN2_raw'],r['B_E2_e2b2_raw']) for r in rows if r['band']==band]==vals for band,vals in expected.items()),
              'TableI_header_has_lifetime_B_columns_not_gamma_energy':any(
                  'Spin I' in line and 'Lifetime[ps]' in line and 'B(M1)' in line and 'B(E2)' in line
                  and 'gamma' not in line for line in tex.splitlines()),
              'author_caption_links_fig2_M1_fig3_E2':r'\label{fig:bm1}' in tex and r'\label{fig:be2}' in tex}
    plots=[parse_plot(source_root/'fig2.ps','M1',rows),parse_plot(source_root/'fig3.ps','E2',rows)]
    for plot in plots:
        controls.update({plot['kind']+'_'+k:bool(v) for k,v in plot['controls'].items()})
    return {'status':'author-vector-representation-audit-only','formal_day_index':23,'uncredited_preview_day':24,
            'source_identity':'arXiv0708.1493 currentv2 officialarchive, DOI99.172501; same paper, no independent acquisition',
            'archive_content_executed':False,'source_member_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in source_root.iterdir()},
            'TableI_rows_raw':rows,'plots':plots,'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'implementation_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'limitations':['Coordinates are rounded author graphics, not full precision input data or the experiment/fit producer. Exact literal extraction does not certify unrounded B accuracy.',
                           'The +/-0.00005 coordinate/axis corner envelope is a declared graphic-rounding sensitivity, not an experimental confidence interval; truncation or other rendering changes require a different design.',
                           'Drawn errorbar endpoints have no supplied joint covariance/coverage or source systematics here.',
                           'Neither archive TableI nor figure legends provide rowwise gamma energy/final spin or a component ledger. PlottedI-to-parent and out/in denominator bindings remain conditional.',
                           'The archive contains four drawings, TeX andbibliography; no raw coincidence spectra, branch tables or analysis producer is recovered.',
                           'No new data vote, physical delta/ICC/Q/g/lifetime CI, paper-error claim or beamtime generated. Original budget ambiguities and earlier withdrawals remain.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    result=calculate(a.source_root);a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':result['all_controls_pass'],'checks':len(result['controls']),
                      'controls':result['controls'],'plot_centres':{p['kind']:[{'I':r['plotted_I_coordinate'],'B_drawn':r['drawn_B_centre'],'conditional_out_in':r['conditional_out_over_in_if_same_parent_component']} for r in p['rows']] for p in result['plots']}},ensure_ascii=False))
    return 0 if result['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
