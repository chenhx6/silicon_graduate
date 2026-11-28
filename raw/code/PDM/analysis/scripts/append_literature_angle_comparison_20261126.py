"""Add literature comparisons of tan-transformed angle statistics to the report."""

from __future__ import annotations

import argparse
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from unittest.mock import patch

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[5]
REPORT = ROOT / 'raw/writing/pado/20261029_review_v1/PDM'
FIG = REPORT / 'figures'
REV = FIG / 'data/literature_tan_20261126'
QA = ROOT / 'tmp/pdm-literature-tan-20261126'
sys.path.insert(0, str(FIG))

import numpy as np
import pymupdf
import two_geometry_report as report
import review_report_figures_20261126 as prior


def save(name, value):
    (QA/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')


def rows():
    records = prior.read_data()['literature']
    assert len(records) == 30
    assert {m:sum(r['mode']==m for r in records) for m in report.MODES} == {'P_ADO':9,'P_DCO':17,'PDCO':4}
    return records


def render():
    report.QA = QA
    with report.plt.rc_context(report.REPORT_STYLE_SETTINGS):
        report.literature_comparison(rows(), angle_statistics=True)
    source = FIG / 'data/figure_review_20261125/literature_and_evidence.tex'
    text = source.read_text()
    marker = r'\clearpage\section{全部30个文献二维声明模型四联图}'
    assert text.count(marker) == 1
    text = text.replace(marker, report.literature_angle_comparison_tex()+marker)
    (REV/'literature_and_evidence.tex').write_text(text)
    main = REPORT/'main.tex'
    text = main.read_text()
    old = 'figures/data/figure_review_20261125/literature_and_evidence.tex'
    new = 'figures/data/literature_tan_20261126/literature_and_evidence.tex'
    assert old in text or new in text
    main.write_text(text.replace(old,new))
    print('Added three tan(angle-statistic) literature comparisons and section 10.3.', flush=True)


def ordered(values):
    return sorted(tuple(np.asarray(v).ravel()) for v in values)


def audit():
    records=rows();checks=[]
    for r in records:
        a=r['statistics']['arctan_delta'];s=r['statistics']['tan_angle_statistics']
        np.testing.assert_allclose(np.tan([a['mode'],a['median'],*a['eti']]),
                                   [s['mode'],s['median'],*s['eti']],atol=2e-12,rtol=2e-12)
        assert len(a['hdi_segments'])==len(s['hdi_segments'])
        for aa,ss in zip(a['hdi_segments'],s['hdi_segments']):
            np.testing.assert_allclose(np.tan(aa['bounds']),ss['bounds'],atol=2e-12,rtol=2e-12)
            np.testing.assert_allclose(np.tan(aa['mode_ranges']),ss['mode_ranges'],atol=2e-12,rtol=2e-12)
            assert aa['mass']==ss['mass']
        # Independently integrate the original saved angle density.
        with np.load(ROOT/r['source_npz']) as z:
            x=z['angle'];p=prior.trapezoid(z['parameter_density'],z['sigma_over_i'],axis=0)
            metrics=prior.numerical.check_marginal(x,p,a)
        checks.append({'id':r['id'],'angle_pdf_independently_integrated':metrics,
                       'tan_quantiles_hdi_endpoints_and_all_local_modes_checked':True})
    plotted=[]
    def inspect(fig,stem,axes=None):
        mode=next(m for m in report.MODES if stem.endswith(m))
        rr=[r for r in records if r['mode']==mode];ax=fig.axes[0]
        hdi=[];eti=[];modes=[];medians=[];quotes=[];quote_bars=[]
        for pos,r in enumerate(rr):
            s=r['statistics']['tan_angle_statistics']
            # Expected positions come from the angle statistics directly.
            a=r['statistics']['arctan_delta']
            for seg in a['hdi_segments']:
                lo,hi=np.tan(seg['bounds']);hdi.append(((lo,pos-.19),(hi,pos-.19)))
                for lo,hi in np.tan(seg['mode_ranges']):modes.append(((lo+hi)/2,pos-.19))
            lo,hi=np.tan(a['eti']);eti.append(((lo,pos-.04),(hi,pos-.04)))
            medians.append((np.tan(a['median']),pos-.04))
            for b in r['literature']['delta_branches']:
                quotes.append((b['center'],pos+.20))
                if b.get('minus') is not None and b.get('plus') is not None:
                    quote_bars.append(((b['center']-b['minus'],pos+.20),(b['center']+b['plus'],pos+.20)))
        actual_eti=[];actual_quote_bars=[];errorcollections=set()
        for c in ax.containers:
            if not hasattr(c,'lines'):continue
            center,caps,bars=c.lines
            target=actual_eti if center.get_marker()=='x' else actual_quote_bars
            for collection in bars:
                errorcollections.add(id(collection));target.extend(collection.get_segments())
            if center.get_marker()=='x':
                assert len(caps)==2
                assert all(c.get_linestyle()[0][1] is not None for c in bars)
        actual_hdi=[s for c in ax.collections if id(c) not in errorcollections and hasattr(c,'get_segments')
                    for s in c.get_segments()]
        for actual,expected in ((actual_hdi,hdi),(actual_eti,eti),(actual_quote_bars,quote_bars)):
            np.testing.assert_allclose(ordered(actual),ordered(expected),atol=2e-12,rtol=2e-12)
        for marker,expected in [('s',modes),('x',medians),('D',quotes)]:
            actual=[(x,y) for line in ax.lines if line.get_marker()==marker
                    for x,y in zip(line.get_xdata(),line.get_ydata())]
            np.testing.assert_allclose(ordered(actual),ordered(expected),atol=2e-12,rtol=2e-12)
        xmin,xmax=sorted(ax.get_xlim())
        all_x=[point[0] for segment in hdi+eti+quote_bars for point in segment]
        all_x += [point[0] for point in modes+medians+quotes]
        assert xmin <= min(all_x) <= max(all_x) <= xmax
        buffer=BytesIO();fig.savefig(buffer,format='pdf',dpi=300)
        with pymupdf.open(stream=buffer.getvalue(),filetype='pdf') as fresh,pymupdf.open(FIG/f'{stem}.pdf') as old:
            assert prior.vector_signature(fresh[0])==prior.vector_signature(old[0])
        plotted.append({'figure':stem+'.pdf','cases':len(rr),'actual_pdf_vectors_match':True,
                        'all_hdi_endpoints_local_modes_medians_eti_caps_and_quoted_errors_checked':True})
        report.plt.close(fig)
    with report.plt.rc_context(report.REPORT_STYLE_SETTINGS),patch.object(report,'savefig',inspect):
        report.literature_comparison(records,angle_statistics=True)
    # The default path must still reproduce the three existing true-delta figures.
    raw=json.loads((FIG/'data/figure_review_20261125/evidence/delta_density_statistics.json').read_text())
    default_checks=[]
    def unchanged(fig,stem,axes=None):
        b=BytesIO();fig.savefig(b,format='pdf',dpi=300)
        with pymupdf.open(stream=b.getvalue(),filetype='pdf') as fresh,pymupdf.open(FIG/f'{stem}.pdf') as old:
            assert prior.vector_signature(fresh[0])==prior.vector_signature(old[0])
        default_checks.append(stem);report.plt.close(fig)
    with report.plt.rc_context(report.REPORT_STYLE_SETTINGS),patch.object(report,'savefig',unchanged):
        report.literature_comparison(records,{k:prior.marginal(v) for k,v in raw.items()})
    save('data-audit.json',{'status':'passed','cases':checks,'new_figures':plotted,
                           'existing_delta_figures_unchanged':default_checks,'new_inversions':0})
    print('30 angle marginals, all transformed interval endpoints/peaks and actual PDF points verified.',flush=True)


def qa():
    checks=[]
    for mode in report.MODES:
        p=FIG/f'literature_tan_comparison_{mode}.pdf'
        font=subprocess.run([sys.executable,str(prior.SKILL/'audit_pdf_text.py'),str(p),'--json'],capture_output=True,text=True)
        (QA/f'{p.stem}.fonts.json').write_text(font.stdout)
        collision=subprocess.run([sys.executable,str(prior.SKILL/'audit_figure_collisions.py'),str(p),
                                  '--json-out',str(QA/f'{p.stem}.collision.json')],capture_output=True,text=True)
        checks.append({'figure':p.name,'font_exit':font.returncode,'collision_exit':collision.returncode})
        if font.returncode or collision.returncode:print(font.stdout,collision.stdout,collision.stderr)
    static=subprocess.run([sys.executable,str(prior.SKILL/'validate_figure.py'),str(FIG/'two_geometry_report.py'),'--json'],capture_output=True,text=True)
    (QA/'plot-source-audit.json').write_text(static.stdout)
    assert static.returncode==0
    save('rendered-qa.json',checks)
    assert all(v['font_exit']==v['collision_exit']==0 for v in checks)
    print('Three new figures: rendered text, collision and plotting-source checks passed.',flush=True)


def compile_report():
    out=QA/'tex';out.mkdir(exist_ok=True)
    for i in (1,2):
        with (QA/f'compile-{i}.log').open('w') as log:
            r=subprocess.run(['xelatex','-halt-on-error','-interaction=nonstopmode','-output-directory='+str(out),'main.tex'],cwd=REPORT,stdout=log,stderr=subprocess.STDOUT)
        if r.returncode:print((QA/f'compile-{i}.log').read_text()[-4000:])
        assert r.returncode==0
        print('XeLaTeX pass',i,'passed',flush=True)
    text=(QA/'compile-2.log').read_text()
    assert not re.search(r'undefined|Rerun to get cross|Overfull',text)
    shutil.copy2(out/'main.pdf',REPORT/'main.pdf')
    doc=pymupdf.open(stream=(REPORT/'main.pdf').read_bytes(),filetype='pdf')
    inventory=[]
    for i,page in enumerate(doc):
        for line in page.get_text().splitlines():
            if re.match(r'^图\d+:',line):inventory.append({'page':i+1,'caption_start':line})
    assert len(inventory)==106
    assert [int(re.search(r'\d+',v['caption_start'])[0]) for v in inventory]==list(range(1,107))
    assert '图65:' in doc[92].get_text()
    normalize=lambda s:re.sub(r'\s+','',s)
    assert all('真实delta' in normalize(doc[i].get_text()) for i in (104,105,106))
    new=[v for v in inventory if '角统计量经tan转换与文献' in normalize(v['caption_start'])]
    assert len(new)==3
    assert [i+1 for i,p in enumerate(doc) if '10.3' in p.get_text() and '新增：角统计量' in normalize(p.get_text())]
    save('report-inventory.json',{'pages':len(doc),'figures':len(inventory),'new_comparisons':new,'inventory':inventory,
                                  'figure65_preserved_on_page93':True,'compile_undefined_references':0,'overfull_boxes':0})
    print('Final report:',len(doc),'pages;',len(inventory),'figures; new pages',[v['page'] for v in new],flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('stage',choices=('render','audit','qa','compile'))
    args=p.parse_args();QA.mkdir(parents=True,exist_ok=True)
    {'render':render,'audit':audit,'qa':qa,'compile':compile_report}[args.stage]()


if __name__=='__main__':main()
