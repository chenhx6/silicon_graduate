#!/usr/bin/env python3
"""Check the assigned source coverage, bilingual pairs, assets and source hash."""
from pathlib import Path
import importlib.util
import json
import re
import hashlib
import subprocess
import sys
import datetime

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('assigned_reader',BASE/'build_reader.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
used={}
for s in m.specs:
    for pg,a,b in s.get('parts',[]):
        for i in range(a,b+1):used.setdefault((pg,i),[]).append(s.get('translation_key',s.get('id','heading')))
for a in m.assets:
    for pg,i,j in a['parts']+a['caption_parts']:
        for k in range(i,j+1):used.setdefault((pg,k),[]).append(a['id'])
missing=[]
excluded=[]
for pg in range(75,116):
    for i,b in enumerate(m.doc[pg-1].get_text('blocks')):
        if (pg,i) in used:continue
        if (i==0 and pg!=75) or (pg==75 and b[1]>770):
            excluded.append({'PDF_page':pg,'block':i,'reason':'running header / printed page number'})
        else:missing.append({'PDF_page':pg,'block':i,'text':b[4]})
overlaps=[{'page_block':list(k),'assignments':v} for k,v in used.items() if len(v)>1]
assert not missing and not overlaps
sm=json.loads((BASE/'source_map.json').read_text());md=(BASE/'paper.md').read_text()
for b in sm['blocks']:
    if b['type'] in ['paragraph','heading','caption']:
        assert b['original_text'] and b['translation']
        assert f'id="{b["id"]}"' in md
        original_refs=re.findall(r'\[([0-9, ]+)\]',b['original_text'])
        translated_refs=re.findall(r'\[([0-9, ]+)\]',b['translation'])
        assert [re.sub(r'\s+','',x) for x in original_refs]==[re.sub(r'\s+','',x) for x in translated_refs],(b['id'],original_refs,translated_refs)
images=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',md)
assert len(images)==27
assert all((BASE/p).is_file() for p in images)
assert set(images)=={str(p.relative_to(BASE)) for p in (BASE/'assets').rglob('*.png')}
assert md.count('**Original:**')==81 and md.count('**中文:**')==81
assert md.count('**Original caption:**')==27 and md.count('**中文图注:**')==27
assert hashlib.sha256(m.SOURCE.read_bytes()).hexdigest()==m.EXPECTED
validator='/root/.codex/skills/nature-reader/scripts/validate_reader_math.py'
r=subprocess.run([sys.executable,validator,str(BASE/'paper.md'),'--source-map',str(BASE/'source_map.json'),'--strict','--json'],capture_output=True,text=True,check=True)
math=json.loads(r.stdout);assert math['ready'];(BASE/'validation_math.json').write_text(r.stdout)
receipt=dict(timestamp_UTC=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Chapter6 only; no full-thesis completion claim',
             PDF_pages=list(range(75,116)),printed_pages=[64,104],substantive_text_block_coverage_complete=True,
             missing_source_blocks=missing,duplicate_source_blocks=overlaps,
             excluded_running_headers_and_page_numbers=excluded,
             translated_body_paragraphs=66,translated_headings=15,translated_captions=27,
             figure_crops=16,table_crops=11,equation_crops=0,all_linked_assets_present=True,
             citation_markers_preserved=True,math_validation=math,
             source_sha256_after=m.EXPECTED,source_modified=False,
             visual_QA='All 16 figures and all 11 tables inspected in contact sheets; F014 vector frame/upper curves crop corrected against the full source page',
             scientific_boundary='Coverage/math/asset validation only, not validation of physical claims or author producer')
(BASE/'coverage_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['excluded_running_headers_and_page_numbers','PDF_pages']},ensure_ascii=False,indent=2))
