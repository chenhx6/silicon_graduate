#!/usr/bin/env python3
"""Two frozen W178 pure-component queries, with separate offline capture.

All responses stay in repository tmp. No credentials, raw archive, old Yb query
or reviewed KB08 source is modified. HTTP and numerical success are distinct.
"""
from __future__ import annotations

import argparse
from datetime import datetime
from decimal import Decimal
import hashlib
import json
import math
from pathlib import Path
import re
from zoneinfo import ZoneInfo

from bs4 import BeautifulSoup
import requests


def save(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def now() -> str:
    return datetime.now(ZoneInfo('Asia/Shanghai')).isoformat()


def query(cfg: dict, input_path: Path, receipt_path: Path, response_dir: Path) -> None:
    digest=hashlib.sha256(input_path.read_bytes()).hexdigest()
    if receipt_path.exists():
        receipt=json.loads(receipt_path.read_text());assert receipt['input_sha256']==digest
    else:
        receipt={'identity':cfg['identity'],'input_sha256':digest,
                 'query_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 'requests':[],'numerical_validation_performed':False}
    response_dir.mkdir(parents=True,exist_ok=True)
    for params in cfg['requests']:
        mode=params['multipole']
        if any(x['parameters']['multipole']==mode for x in receipt['requests']):
            print(json.dumps({'multipole':mode,'status':'already-attempted-no-repeat'}));continue
        path=response_dir/('bricc-Z74-E920p8-FO-'+mode+'.html');assert not path.exists()
        record={'parameters':params,'attempt_started_at':now(),'automatic_retries':0,'status':'attempt-started'}
        receipt['requests'].append(record);save(receipt_path,receipt)
        try:
            response=requests.post(cfg['endpoint'],data=params,
                                   headers={'User-Agent':'WikiResearchData/1.0'},timeout=(10,35))
            path.write_bytes(response.content)
            record.update(status='http-response',http_status=response.status_code,
                          response=str(path),sha256=hashlib.sha256(response.content).hexdigest(),
                          bytes=len(response.content),content_type=response.headers.get('Content-Type'),
                          redirect_statuses=[x.status_code for x in response.history])
        except requests.RequestException as e:
            record.update(status='transport-failed',error_type=type(e).__name__)
        record['completed_at']=now();save(receipt_path,receipt)
        print(json.dumps(record,ensure_ascii=False),flush=True)


def decode(value: str, error: str) -> dict:
    v=Decimal(value);m=re.fullmatch(r'\((\d+)\)',error)
    return {'printed':value,'printed_error':error,'value':float(v),
            'quoted_error':float(Decimal(m[1])*Decimal(10)**v.as_tuple().exponent) if m else None}


def capture(cfg: dict, input_path: Path, receipt_path: Path, output: Path) -> None:
    receipt=json.loads(receipt_path.read_text())
    assert receipt['input_sha256']==hashlib.sha256(input_path.read_bytes()).hexdigest()
    assert len(receipt['requests'])==2
    models=[]
    for record in receipt['requests']:
        assert record['status']=='http-response' and record['http_status']==200
        params=record['parameters'];assert params in cfg['requests']
        path=Path(record['response']);body=path.read_bytes();assert hashlib.sha256(body).hexdigest()==record['sha256']
        soup=BeautifulSoup(body,'html.parser');table=soup.find('table');assert table is not None
        rows=[[td.get_text(' ',strip=True) for td in tr.find_all(['td','th'],recursive=False)]
              for tr in table.find_all('tr',recursive=False)]
        flat=' '.join(' '.join(row) for row in rows)
        assert 'Z=74' in flat and 'Tungsten' in flat and '920.8' in flat
        assert 'BrIccFO' in flat and 'BrIccNH' not in flat
        version=next((' '.join(row) for row in rows if 'BrIccS' in ' '.join(row)),None);assert version
        start=next(i for i,row in enumerate(rows) if row[:2]==['Shell','E(ce)'])
        assert rows[start][2]==params['multipole']
        coefficients={};unknown=[]
        for row in rows[start+1:]:
            if not row or row[0].startswith('Reference'):break
            if len(row)>=4 and row[2]:
                coefficients[row[0]]={**decode(row[2],row[3]),'Ece_printed_keV':row[1] or None}
            elif row[0]:unknown.append({'shell':row[0],'row':row})
        assert coefficients['K']['value']>0
        assert coefficients['Tot']['value']>coefficients['K']['value']
        kinetic=float(coefficients['K']['Ece_printed_keV']);assert 0<kinetic<920.8
        warnings=[x for x in soup.stripped_strings if 'could not be calculated' in x]
        models.append({'multipolarity':params['multipole'],'program_version_echo':version,
                       'dataset':'BrIccFO','Z':74,'energy_keV':920.8,
                       'raw_snapshot':str(path),'raw_sha256':record['sha256'],
                       'all_printed_rows':rows[start:],'coefficients':coefficients,
                       'unknown_cells_not_zero':unknown,'warnings':warnings,
                       'implied_K_binding_from_display_keV':920.8-kinetic,
                       'published_2008_binding_reference_keV':cfg['documented_2008_K_binding_keV'],
                       'published_2008_mass_reference':cfg['documented_2008_mass_number'],
                       'current_backend_mass_or_datafile_hash_exposed':False})
    assert {x['multipolarity'] for x in models}=={'M1','E2'}
    result={'identity':cfg['identity'],'input_sha256':receipt['input_sha256'],
            'capture_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'query_receipt_sha256':hashlib.sha256(receipt_path.read_bytes()).hexdigest(),
            'models':models,'numerically_validated':True,
            'boundary':'Nominal-energy theoretical K-shell input; no A178-specific radius recalculation, measured ICC, complete total certification or experimental uncertainty budget.'}
    save(output,result)
    print(json.dumps({'output':str(output),'numerically_validated':True,
                      'models':[{'multipolarity':m['multipolarity'],'version':m['program_version_echo'],
                                 'K':m['coefficients']['K'],'Tot':m['coefficients']['Tot'],
                                 'unknown':m['unknown_cells_not_zero'],'warnings':m['warnings']} for m in models]},ensure_ascii=False))


def analyze(cfg: dict, input_path: Path, captured: Path, output: Path) -> None:
    data=json.loads(captured.read_text());assert data['numerically_validated']
    assert data['input_sha256']==hashlib.sha256(input_path.read_bytes()).hexdigest()
    c={x['multipolarity']:x['coefficients']['K'] for x in data['models']}
    m,e=[c[k]['value'] for k in ('M1','E2')]
    sm,se=[c[k]['quoted_error'] for k in ('M1','E2')]
    assert sm is not None and se is not None
    a=cfg['observed_KICC']['value'];sa=cfg['observed_KICC']['quoted_error'];results=[]
    for item in cfg['fixed_D96_point_candidates']:
        d=item['d'];wm=1/(1+d*d);we=1-wm;prediction=wm*m+we*e
        assert abs(prediction-(m+(-d)**2*e)/(1+(-d)**2))<1e-15
        theory_box=[wm*(m-sm)+we*(e-se),wm*(m+sm)+we*(e+se)]
        results.append({**item,'radiative_M1_fraction':wm,'radiative_E2_fraction':we,
                        'predicted_K':prediction,
                        'theory_error_covariance_family':{
                            'rho_minus1':abs(wm*sm-we*se),'rho_zero':math.hypot(wm*sm,we*se),
                            'rho_plus1':wm*sm+we*se,
                            'interpretation':'Given quoted pure error scales only; actual covariance/distribution not known'},
                        'literal_theory_marginal_box_image':theory_box,
                        'reported_experimental_literal_margin':[a-sa,a+sa],
                        'central_residual_Kexp_minus_model':a-prediction,
                        'experimental_confidence_or_pvalue':None,
                        'literal_boxes_overlap':max(theory_box[0],a-sa)<=min(theory_box[1],a+sa)})
    inverse={'status':'no-physical-central-root','not_a_new_measured_delta':True}
    margin={'confidence_level':None}
    if min(m,e)<a<max(m,e):
        f=(m-a)/(m-e);x=(m-a)/(a-e);assert 0<f<1 and x>0
        inverse={'status':'conditional-map-only','radiative_E2_fraction':f,
                 'abs_d':math.sqrt(x),'two_signs':[-math.sqrt(x),math.sqrt(x)],
                 'not_a_new_measured_delta':True}
        fr=sorted([(m-(a+sa))/(m-e),(m-(a-sa))/(m-e)])
        if 0<fr[0]<=fr[1]<1:
            margin.update(f_E2=fr,abs_d=[math.sqrt(x/(1-x)) for x in fr])
        else:margin.update(f_E2_unclipped=fr,domain_boundary='Do not clip data and report a central physical root.')
    result={'identity':'DAY16-W178-K-COMPANION-CONDITIONAL-CHECK-01',
            'query_input_sha256':hashlib.sha256(input_path.read_bytes()).hexdigest(),
            'captured_theory_sha256':hashlib.sha256(captured.read_bytes()).hexdigest(),
            'analysis_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'experimental_input':cfg['observed_KICC'],'theory_pure_K':c,
            'fixed_point_predictions':results,'central_conditional_inverse_only':inverse,
            'experimental_literal_margin_preimage_nominal_theory_only':margin,
            'boundary':'Ordinary BrIccFO M1/E2 with secondary reported Kexp. No primary calibration/gates/normalization covariance, penetration-parameter fit, energy-error propagation or DCO refit. Fixed root points are not whole allowed branch families; literal boxes are not confidence sets or experimental exclusions.'}
    save(output,result)
    print(json.dumps({'output':str(output),'predictions':[{k:v for k,v in x.items() if k in ['id','predicted_K','literal_boxes_overlap']} for x in results],
                      'conditional_inverse_only':inverse},ensure_ascii=False))


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase',choices=['query','capture','analyze']);p.add_argument('--input',type=Path,required=True)
    p.add_argument('--receipt',type=Path,required=True);p.add_argument('--response-dir',type=Path)
    p.add_argument('--output',type=Path);p.add_argument('--captured',type=Path);a=p.parse_args()
    root=Path(__file__).resolve().parents[2]
    for path in [a.input,a.receipt,a.response_dir,a.output,a.captured]:
        if path is not None:assert path.resolve().is_relative_to(root),'Wiki paths only'
    cfg=json.loads(a.input.read_text());assert cfg['identity']=='DAY16-BRICC-W178-K-REFERENCE-01'
    assert cfg['endpoint']=='https://bricc.anu.edu.au/' and cfg['max_queries']==2 and len(cfg['requests'])==2
    assert {x['multipole'] for x in cfg['requests']}=={'M1','E2'}
    assert all(x['atomic']=='74' and x['energy']=='920.8' and x['dataset']=='BrIccFO'
               and not x['eerror'] and not x['delta'] and not x['derror'] for x in cfg['requests'])
    if a.phase=='query':
        assert a.response_dir is not None;query(cfg,a.input,a.receipt,a.response_dir)
    elif a.phase=='capture':
        assert a.output is not None;capture(cfg,a.input,a.receipt,a.output)
    else:
        assert a.output is not None and a.captured is not None
        analyze(cfg,a.input,a.captured,a.output)


if __name__=='__main__':main()
