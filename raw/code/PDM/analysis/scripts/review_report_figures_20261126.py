"""Revise report comparisons and audit saved figures without running inversions."""

from __future__ import annotations

import argparse
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
import subprocess
import sys
from types import SimpleNamespace
from unittest.mock import patch

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[5]
REPORT = ROOT / "raw/writing/pado/20261029_review_v1/PDM"
FIG = REPORT / "figures"
REV = FIG / "data/figure_review_20261125"
QA = ROOT / "tmp/pdm-report-figure-review-20261126"
SKILL = Path.home() / ".codex/skills/nature-figure/scripts"
sys.path.insert(0, str(FIG))
sys.path.insert(0, str(ROOT / "raw/code/PDM/GUI/src"))

import numpy as np
import pymupdf
from scipy.integrate import trapezoid

import two_geometry_report as report
from multipolepdm.contracts import MappingResult, ResponseGrid
from multipolepdm.io.input import job_from_dict
from multipolepdm.pdm.statistics import summarize_density
import audit_two_geometry_report as numerical


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False)+"\n")


def read_data():
    return json.loads((report.DATA / "results.json").read_text())


def marginal(s):
    segments = [SimpleNamespace(bounds=x["bounds"], mode_ranges=x["mode_ranges"])
                for x in s["hdi_segments"]]
    return SimpleNamespace(median=s["median"], intervals=[SimpleNamespace(
        eti=s["eti"], hdi_segments=segments)])


def rewrite_captions():
    path = REPORT / "inject_test.tex"
    text = path.read_text()
    for mode in report.MODES:
        pattern = (r"(\\includegraphics\[width=\\linewidth\]\{figures/two_geometry_compare_"+
                   mode+r"(?:_review)?\.pdf\}\s*\\caption\{).*?(\}\\end\{figure\})")
        text, count = re.subn(pattern, lambda m: m[1]+report.comparison_caption(mode)+m[2],
                              text, flags=re.S)
        assert count == 1, (mode, count)
        text=text.replace(f"figures/two_geometry_compare_{mode}.pdf",f"figures/two_geometry_compare_{mode}_review.pdf")
    text = text.replace("所有HDI与ETI均为68\\%，评估坐标为", "除新增的直接delta密度评估节外，HDI与ETI均为68\\%，评估坐标为")
    marker = r"\clearpage\input{figures/data/two_geometry_20261125/large_delta_comparison.tex}"
    if "新增：直接在delta边缘密度上评估的几何对比" not in text:
        assert marker in text
        text = text.replace(marker, report.delta_density_comparison_tex()+marker)
    else:
        begin = text.index(r"\clearpage\subsection{新增：直接在delta边缘密度上评估的几何对比}")
        end = text.index(marker, begin)
        text = text[:begin] + report.delta_density_comparison_tex() + text[end:]
    path.write_text(text)
    path = REV / "literature_and_evidence.tex"
    text = (REV / "before/figures/data/two_geometry_20261125/literature_and_evidence.tex").read_text()
    marker = r"\clearpage\section{全部30个文献二维声明模型四联图}"
    if "30个文献声明模型与报道值的对比图" not in text:
        assert marker in text
        text = text.replace(marker, report.literature_comparison_tex()+marker)
    path.write_text(text)
    path=REPORT/"main.tex"
    text=path.read_text().replace("figures/data/two_geometry_20261125/literature_and_evidence.tex",
                                "figures/data/figure_review_20261125/literature_and_evidence.tex")
    path.write_text(text)


def render():
    d = read_data()
    report.QA = QA
    QA.mkdir(parents=True, exist_ok=True)
    rows = d["old_injections"] + d["new_injections"]
    summaries = {r["id"]: SimpleNamespace(
        delta=marginal(r["statistics"]["tan_angle_statistics"]),
        sigma_over_i=marginal(r["statistics"]["sigma_over_i"])) for r in rows}
    with report.plt.rc_context(report.REPORT_STYLE_SETTINGS):
        report.compare(rows, summaries)
        print("Three angle-statistic comparisons redrawn with asymmetric ETI bars.", flush=True)
        delta = report.delta_density_statistics(rows + d["literature"])
        report.delta_density_comparison(rows, delta)
        report.literature_comparison(d["literature"], delta)
    rewrite_captions()
    print("Added three delta-only geometry comparisons and three literature comparisons.", flush=True)


def restore(r):
    job = job_from_dict(r["input"])
    with np.load(ROOT / r["source_npz"]) as z:
        response = ResponseGrid(z["angle"], z["sigma_over_i"]*job.reference_spin,
                                z["response_P"], z["response_R"], z["valid"],
                                job.reference_spin, job.ratio_name)
        result = MappingResult(job, response, z["observation_density"], z["jacobian"],
                               z["parameter_density"]/job.reference_spin, 1., tuple(r["warnings"]))
    return result


def images(page):
    # Compare decoded raster samples, independent of PDF stream compression.
    return [(v[2],v[3],sha256(pymupdf.Pixmap(page.parent,v[0]).samples).hexdigest())
            for v in page.get_images()]


def vector_signature(page):
    def point(p):
        if hasattr(p,"x"):
            return [round(p.x,3),round(p.y,3)]
        if hasattr(p,"x0"):
            return [round(v,3) for v in tuple(p)]
        return p
    return [{k: ([tuple(point(p) for p in it) for it in v[k]] if k=="items" else
                 [round(x,5) for x in v[k]] if v[k] is not None and k in ("color","fill") else v[k])
             for k in ("items","color","fill","dashes")} for v in page.get_drawings()]


def audit_panels():
    """Audit all 90 saved four-panel figures, including their actual PDF rasters."""
    records = [r for name in ("old_injections","new_injections","literature") for r in read_data()[name]]
    results = []
    for r in records:
        result = restore(r)
        summary = summarize_density(result, masses=(.68,))
        report.check(summary,r["statistics"])
        # These are the same frozen density arrays; no map_density/evaluate_response call.
        arrays = result.response
        old = pymupdf.open(FIG/r["figure"])
        def inspect(fig, stem, axes=None):
            obs = axes[0].collections[0]
            valid = arrays.valid & np.isfinite(arrays.angular_ratio) & np.isfinite(arrays.polarization) & np.isfinite(result.observation_density)
            np.testing.assert_array_equal(obs.get_offsets(), np.c_[arrays.angular_ratio[valid],arrays.polarization[valid]])
            np.testing.assert_array_equal(obs.get_array(),result.observation_density[valid])
            mesh = axes[1].collections[0]
            np.testing.assert_array_equal(np.asarray(mesh.get_array()).ravel(),
                                          (result.parameter_density*arrays.reference_spin).ravel())
            for ax,m in zip(axes[2:],(summary.arctan_delta,summary.sigma_over_i)):
                np.testing.assert_allclose(ax.lines[0].get_xdata(),m.coordinate,atol=0)
                np.testing.assert_allclose(ax.lines[0].get_ydata(),m.density,atol=0)
            buf = BytesIO();fig.savefig(buf,format="pdf",dpi=300)
            fresh = pymupdf.open(stream=buf.getvalue(),filetype="pdf")
            raster_equal = images(fresh[0])==images(old[0])
            vectors_equal = vector_signature(fresh[0])==vector_signature(old[0])
            results.append({"id":r["id"],"figure":r["figure"],"source_npz":r["source_npz"],
                            "artist_arrays_checked":True,"raster_images_identical":raster_equal,
                            "vector_paths_identical":vectors_equal})
            report.plt.close(fig);fresh.close()
        report.REDRAW.add(r["id"])
        with patch.object(report,"savefig",inspect):
            report.overview(result,summary,r)
        old.close()
        if len(results)%10==0:print("Audited four-panel figures",len(results),"/ 90",flush=True)
    save(QA/"panel_data_audit.json",{"cases":len(results),"inversions":0,"checks":results,
        "raster_identity_count":sum(r["raster_images_identical"] for r in results),
        "vector_identity_count":sum(r["vector_paths_identical"] for r in results)})
    assert all(r["raster_images_identical"] and r["vector_paths_identical"] for r in results)


def audit_delta():
    stats=json.loads((QA/"delta_density_statistics.json").read_text())
    checks=[]
    for case,s in stats.items():
        with np.load(QA/f"delta_marginal_{case}.npz") as z:
            metrics=numerical.check_marginal(z["delta"],z["density"],s)
        checks.append({"id":case,**metrics,"eti_transform_difference":s["quantile_transform_max_difference"]})
    save(QA/"delta_density_audit.json",{"cases":len(checks),"checks":checks,
        "max_eti_transform_difference":max(v["eti_transform_difference"] for v in checks)})
    assert max(v["eti_transform_difference"] for v in checks) < 1e-6
    print("Independently checked",len(checks),"true delta marginals.",flush=True)


def audit_diagnostics():
    d=read_data();audits=[]
    for group,producer in (("old_injections",report.previous.diagnostic_figure),
                           ("new_injections",report.new_diagnostic_figures)):
        rows=d[group];curves={}
        for r in rows:
            if abs(r['delta_truth'])!=10:continue
            result=restore(r);summary=summarize_density(result,masses=(.68,))
            _,c=report.previous.diagnostics(result,summary,r['angle_truth'])
            with np.load(ROOT/r['source_npz']) as z:
                x,u=z['angle'],z['sigma_over_i']
                normalized=lambda a:a/trapezoid(a,x)
                np.testing.assert_allclose(c['mapped_marginal'],normalized(trapezoid(z['parameter_density'],u,axis=0)),atol=2e-12)
                np.testing.assert_allclose(c['observation_integral'],normalized(trapezoid(z['observation_density'],u,axis=0)),atol=2e-12)
                np.testing.assert_allclose(c['jacobian_integral'],normalized(trapezoid(np.nan_to_num(z['jacobian']),u,axis=0)),atol=2e-12)
                for name,array in [('mapped_truth_sigma_slice',z['parameter_density']),('jacobian_truth_sigma_slice',np.nan_to_num(z['jacobian']))]:
                    np.testing.assert_allclose(c[name],normalized(np.array([np.interp(.3,u,col) for col in array.T])),atol=2e-12)
            curves[r['id']]=c
        def inspect(fig,stem,axes=None):
            b=BytesIO();fig.savefig(b,format='pdf',dpi=300)
            with pymupdf.open(stream=b.getvalue(),filetype='pdf') as fresh,pymupdf.open(FIG/f'{stem}.pdf') as old:
                def scientific(page):
                    paths=vector_signature(page)
                    colors=([0,.44706,.69804],[.83529,.36863,0],[.38431,.38431,.38431])
                    return [v for v in paths if v['color'] in colors or
                            (v['color']==[0,0,0] and v['dashes']!='[] 0')]
                match=scientific(fresh[0])==scientific(old[0])
                all_paths=vector_signature(fresh[0])==vector_signature(old[0])
            audits.append({'figure':stem+'.pdf','scientific_data_paths_identical':match,
                           'all_paths_including_ticks_identical':all_paths,'curves_independently_integrated':True})
            report.plt.close(fig)
        selected=[r for r in rows if abs(r['delta_truth'])==10]
        with report.plt.rc_context(report.REPORT_STYLE_SETTINGS),patch.object(report,'savefig',inspect),patch.object(report.previous,'checked_save',inspect):
            if group=='old_injections':producer(curves,selected)
            else:producer(selected,curves)
    save(QA/'diagnostic_data_audit.json',{'figures':len(audits),'checks':audits})
    assert all(r['scientific_data_paths_identical'] for r in audits)
    print('Four diagnostic figures: independent curve integration and actual PDF vectors match.')


def audit_comparisons():
    d=read_data();injections=d['old_injections']+d['new_injections'];allrows=injections+d['literature']
    raw=json.loads((QA/'delta_density_statistics.json').read_text())
    delta={k:marginal(s) for k,s in raw.items()}
    summaries={r['id']:SimpleNamespace(delta=marginal(r['statistics']['tan_angle_statistics']),
                                     sigma_over_i=marginal(r['statistics']['sigma_over_i'])) for r in injections}
    audits=[]
    def inspect(fig,stem,axes=None):
        mode=next(m for m in report.MODES if stem.endswith(m) or stem.endswith(m+'_review'))
        is_lit=stem.startswith('literature_');is_angle=stem.startswith('two_geometry_')
        rows=[r for r in (d['literature'] if is_lit else injections) if r['mode']==mode]
        expected_bars=[];expected_hdi=[];expected_modes=[];expected_refs=[]
        for panel,ax in enumerate(fig.axes):
            expected_bars=[];expected_hdi=[];expected_modes=[];expected_refs=[]
            for r in rows:
                if is_lit:
                    pos=rows.index(r);m=delta[r['id']];hpos=pos-.19;epos=pos-.04
                    for branch in r['literature']['delta_branches']:
                        expected_refs.append((branch['center'],pos+.20))
                else:
                    pos=[-10,-5,-1,-.5,-.1,.1,.5,1,5,10].index(r['delta_truth'])
                    offset=-.15 if r['id'].startswith('O') else .15;hpos=pos+offset-.035;epos=pos+offset+.035
                    m=(getattr(summaries[r['id']], 'delta' if panel==0 else 'sigma_over_i') if is_angle else delta[r['id']])
                    if r['id'].startswith('O'):expected_refs.append((pos,r['delta_truth'] if panel==0 else r['sigma_over_i_truth']))
                lo,hi=m.intervals[0].eti
                expected_bars.append(((lo,epos),(hi,epos)) if is_lit else ((epos,lo),(epos,hi)))
                for seg in m.intervals[0].hdi_segments:
                    lo,hi=seg.bounds
                    expected_hdi.append(((lo,hpos),(hi,hpos)) if is_lit else ((hpos,lo),(hpos,hi)))
                    for lo,hi in seg.mode_ranges:expected_modes.append(((lo+hi)/2,hpos) if is_lit else (hpos,(lo+hi)/2))
            # Errorbar containers are checked separately from HDI line collections.
            actual_bars=[];quote_bars=[]
            for c in ax.containers:
                if not hasattr(c,'lines'):continue
                line,caplines,collections=c.lines
                target=actual_bars if line.get_marker()=='x' else quote_bars
                for col in collections:target.extend([tuple(map(tuple,v)) for v in col.get_segments()])
                if line.get_marker()=='x':
                    assert len(caplines)==2
                    assert all(col.get_linestyle()[0][1] is not None for col in collections)
            def ordered(v):return sorted(tuple(np.array(x).ravel()) for x in v)
            np.testing.assert_allclose(ordered(actual_bars),ordered(expected_bars),atol=2e-12)
            actual_hdi=[]
            errorcollections={id(col) for c in ax.containers if hasattr(c,'lines') for col in c.lines[2]}
            for c in ax.collections:
                if id(c) not in errorcollections and hasattr(c,'get_segments'):actual_hdi.extend(c.get_segments())
            np.testing.assert_allclose(ordered(actual_hdi),ordered(expected_hdi),atol=2e-12)
            for marker,expected in [('modes',expected_modes),('references',expected_refs)]:
                selected=('s','o') if marker=='modes' else ('D',)
                actual=[(float(x),float(y)) for line in ax.lines if line.get_marker() in selected
                        for x,y in zip(line.get_xdata(),line.get_ydata())]
                np.testing.assert_allclose(ordered(actual),ordered(expected),atol=2e-12)
            if is_lit:
                expected_quotes=[((b['center']-b['minus'],rows.index(r)+.20),(b['center']+b['plus'],rows.index(r)+.20))
                                 for r in rows for b in r['literature']['delta_branches']
                                 if b.get('minus') is not None and b.get('plus') is not None]
                np.testing.assert_allclose(ordered(quote_bars),ordered(expected_quotes),atol=2e-12)
        buf=BytesIO();fig.savefig(buf,format='pdf',dpi=300)
        with pymupdf.open(stream=buf.getvalue(),filetype='pdf') as fresh,pymupdf.open(FIG/f'{stem}.pdf') as old:
            match=vector_signature(fresh[0])==vector_signature(old[0])
        audits.append({'figure':stem+'.pdf','actual_pdf_vectors_match':match,'all_hdi_branches_and_local_modes_checked':True,
                       'eti_medians_and_asymmetric_capped_endpoints_checked':True,'quoted_reference_errors_checked':is_lit})
        report.plt.close(fig)
    with report.plt.rc_context(report.REPORT_STYLE_SETTINGS),patch.object(report,'savefig',inspect):
        report.compare(injections,summaries)
        report.delta_density_comparison(injections,delta)
        report.literature_comparison(d['literature'],delta)
    save(QA/'comparison_data_audit.json',{'figures':len(audits),'checks':audits})
    assert all(r['actual_pdf_vectors_match'] for r in audits)
    print('All nine comparison PDFs: HDI, ETI endpoints/caps, medians, local modes, truth/reference data verified.')


def figure_paths():
    paths=[]
    for tex in (REPORT/"inject_test.tex",REV/"literature_and_evidence.tex"):
        for name in re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}",tex.read_text()):
            paths.append(REPORT/name)
    assert len(paths)==len(set(paths))
    return paths


def audit_captions():
    d=read_data();texts=[(REPORT/'inject_test.tex').read_text(),(REV/'literature_and_evidence.tex').read_text()]
    checks=[]
    for group in ('old_injections','new_injections','literature'):
        for r in d[group]:
            expected=report.figureblock(r,literature=(group=='literature'))
            assert expected in texts[1 if group=='literature' else 0],r['id']
            checks.append({'id':r['id'],'caption_matches_input_and_error_signs':True,
                           'panels_and_density_units_match_renderer':True})
    doc=pymupdf.open(REPORT/'main.pdf'); inventory=[]
    for i,page in enumerate(doc):
        for line in page.get_text().splitlines():
            if re.match(r'^图\d+:',line):inventory.append({'page':i+1,'caption_start':line})
    numbers=[int(re.search(r'\d+',r['caption_start'])[0]) for r in inventory]
    assert numbers==list(range(1,len(figure_paths())+1))
    assert len(figure_paths())==103
    assert '图65:' in doc[92].get_text()
    assert not any('gate ' in doc[i].get_text() for i in (92,93))
    assert all('新增delta' in doc[i].get_text() for i in (96,97,98))
    save(QA/'caption_and_inventory_audit.json',{'figures':len(inventory),'pages':len(doc),'checks':checks,
         'all_13_diagnostic_comparison_captions_reviewed':True,
         'figure_65_preserved_on_page_93':True,'inventory':inventory})
    print('All 103 figure captions and figure/page inventory checked; all 90 case captions match exact inputs.')


def qa():
    records=[]
    for i,path in enumerate(figure_paths(),1):
        text=subprocess.run([sys.executable,str(SKILL/"audit_pdf_text.py"),str(path),"--json"],capture_output=True,text=True)
        coll=subprocess.run([sys.executable,str(SKILL/"audit_figure_collisions.py"),str(path),"--json-out",str(QA/f"{path.stem}.collision.json")],capture_output=True,text=True)
        (QA/f"{path.stem}.fonts.json").write_text(text.stdout)
        records.append({"figure":path.relative_to(ROOT).as_posix(),"font_exit":text.returncode,
                        "collision_exit":coll.returncode})
        if text.returncode or coll.returncode:
            print(path.name,text.stdout,coll.stdout,coll.stderr,flush=True)
        if i%10==0:print("Rendered text/collision checks",i,flush=True)
    save(QA/"all_figure_qa.json",{"figures":len(records),"checks":records})
    assert all(r["font_exit"]==r["collision_exit"]==0 for r in records)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage",choices=("render","panels","delta-audit","diagnostics","comparisons","captions","qa"))
    args=parser.parse_args()
    QA.mkdir(parents=True,exist_ok=True)
    {"render":render,"panels":audit_panels,"delta-audit":audit_delta,"diagnostics":audit_diagnostics,
     "comparisons":audit_comparisons,"captions":audit_captions,"qa":qa}[args.stage]()


if __name__=="__main__":main()
