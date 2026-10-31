#!/usr/bin/env python3
"""Read-only source identity and claim-locator validation for this comparison."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import pymupdf as fitz

ROOT=Path('/workspace/wiki')
OUT=Path(__file__).resolve().parent
identities=json.loads((OUT/'identity.json').read_text())
expected={
    'Ding-canonical':'752d3c5da690c20ec7e188dcc043f9da2a7f062deefc371dd8a497a190b66c37',
    'Ding-alternate':'47451ae95676399c72b907b0efa10bdeb07e82c794a1ed480759ee20bae0c652'}
docs={};checks=[];claims=[]
for r in identities:
    path=ROOT/r['path'];sha=hashlib.sha256(path.read_bytes()).hexdigest();assert sha==expected[r['tag']]
    d=fitz.open(path);docs[r['tag']]=d
    assert len(d)==r['pages']
    body='\n'.join(p.get_text() for p in d)
    no982=[i+1 for i,p in enumerate(d) if '982' in p.get_text()]
    assert not no982
    checks.append(dict(source=r['path'],sha256_after=sha,pages=len(d),text_layer_982_matches=no982,
                       scope='All pages text-layer search; absence alone is not an eigenvector proof'))
    p2=d[1]
    bs=p2.get_text('blocks')
    indices=[9] if r['tag']=='Ding-canonical' else [10,11]
    excerpt=' '.join(bs[i][4] for i in indices)
    norm=re.sub(r'\s+',' ',excerpt)
    assert 'eight Compton-suppressed clover' in norm
    assert '90' in norm and '135' in norm and '57 MeV' in norm and '5 pnA' in norm
    assert '95.3%' in norm and '2 mg/cm2' in norm and '8 mg/cm2' in norm
    claims.append(dict(id=r['tag']+'-Ce-experiment',source=r['path'],sha256=sha,PDF_page=2,
                       section='II.A Measurements, second experiment paragraph',
                       text_block_indices_zero_based=indices,
                       bboxes=[list(bs[i][:4]) for i in indices],original_text=norm,
                       extracted_values=dict(clovers=8,angle_groups={'90deg':4,'135deg':4},
                            beam_MeV=57,beam_pnA=5,Te125_mg_per_cm2=2,Au_mg_per_cm2=8,enrichment_percent=95.3,
                            double_events=2.8e10,triple_or_higher_events=5.4e9),
                       boundary='Printed report only; actual detector/event configuration not independently recovered'))
    qpage=11 if r['tag']=='Ding-canonical' else 10
    qbs=d[qpage-1].get_text('blocks');qi=7 if r['tag']=='Ding-canonical' else 3
    claims.append(dict(id=r['tag']+'-QTR-inputs',source=r['path'],sha256=sha,PDF_page=qpage,section='III.C',
                       text_block_indices_zero_based=[qi],bbox=list(qbs[qi][:4]),original_text=re.sub(r'\s+',' ',qbs[qi][4]),
                       extracted_values=dict(Ce133_epsilon2=.185,Ce133_gamma_deg=10,Ce133_epsilon4=.01,
                                             Ba131_epsilon2=.170,Ba131_gamma_deg=8,Ba131_epsilon4=.003,
                                             positive_parity_orbitals=10),
                       boundary='Author model-description inputs; not recovered actual input deck'))
thesis=ROOT/'raw/theses/degree-dissertation/Triaxiality and Rotational bands in 133Ce.pdf'
tsha=hashlib.sha256(thesis.read_bytes()).hexdigest();assert tsha=='48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080'
tdoc=fitz.open(thesis)
checks.append(dict(source=str(thesis.relative_to(ROOT)),sha256_after=tsha,pages=len(tdoc)))
clips=json.loads((OUT/'crop_manifest.json').read_text())
assert len(clips)==16
for c in clips:
    assert (ROOT/c['path']).is_file()
    assert hashlib.sha256((ROOT/c['source']).read_bytes()).hexdigest()==c['sha256']
    d=fitz.open(ROOT/c['source']);assert 1<=c['PDF_page']<=len(d)
    assert (fitz.Rect(c['bbox_PDF_points']) & d[c['PDF_page']-1].rect).get_area()>0
coef=[.982,-.202,.185]
record=dict(timestamp_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat(),sources=checks,
            crops=len(clips),all_crop_paths_and_source_hashes_verified=True,
            thesis_partial_amplitude_square_sum=sum(a*a for a in coef),
            thesis_normalization_boundary='Under stated orthonormal basis; no coefficient correction or renormalization',
            actual_detector_configuration_recovered=False,actual_event_ledger_recovered=False,
            actual_model_input_deck_recovered=False,canonical_or_review_state_modified=False,
            scope='Targeted current-source crosswalk only; not publication gate or scientific final mode decision')
(OUT/'atomic_claims.json').write_text(json.dumps(claims,ensure_ascii=False,indent=2)+'\n')
(OUT/'validation_receipt.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(record,ensure_ascii=False,indent=2))
