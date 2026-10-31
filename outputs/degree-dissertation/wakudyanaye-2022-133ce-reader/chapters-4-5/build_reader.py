#!/usr/bin/env python3
"""Build a local bilingual reader for the explicitly assigned chapters only."""
from pathlib import Path
import hashlib
import json
import re
import unicodedata
import pymupdf as fitz
from PIL import Image

OUT = Path(__file__).resolve().parent
ROOT = Path('/workspace/wiki')
SOURCE = ROOT/'raw/theses/degree-dissertation/Triaxiality and Rotational bands in 133Ce.pdf'
EXPECTED = '48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080'
doc = fitz.open(SOURCE)
specs = []


def h(parts, cn, level=3):
    specs.append(dict(type='heading', parts=parts, translation=cn, level=level))


def p(parts, key, refs=None, original=None):
    specs.append(dict(type='paragraph', parts=parts, translation_key=key,
                      refs=refs or [], original_override=original))


h([(51,0,1)], '第4章 实验技术', 2)
h([(51,2,2)], '4.1 引言')
p([(51,3,11)], 'intro4')
h([(51,12,12)], '4.2 重离子融合蒸发')
p([(51,13,20),(52,1,3)], 'fusion')
specs.append(dict(type='equation', id='E001', page=52, parts=[(52,4,5)], number='4.1',
                  bbox=[270,148,530,197], label='库仑势垒：保留原式', cn='原文给出的库仑势垒近似式；请以裁图中的原式为准。'))
p([(52,6,10)], 'radius', original='with $r=1.2(A_p^{1/3}+A_t^{1/3})$ fm. Here $Z_p$ and $A_p$ are the atomic number and the mass number of the incident projectile nucleus, and $Z_t$ and $A_t$ represent the atomic number and the mass number of the target nucleus.')
p([(52,11,19)], 'compound')
p([(52,20,26)], 'statistical')
h([(52,27,27)], '4.3 γ衰变')
p([(52,28,32),(53,1,2)], 'gamma_decay')
specs.append(dict(type='equation', id='E002', page=53, parts=[(53,3,3)], number='4.2',
                  bbox=[250,137,530,177], label='多极阶数的角动量选择范围', cn='式中初态与末态自旋对多极阶数的约束，保留原式。'))
p([(53,4,16)], 'multipolarity', ['T001'])
h([(53,20,20)], '4.4 γ射线的探测')
p([(53,21,28)], 'germanium')
h([(54,1,1)], '4.5 AFRODITE探测阵列')
p([(54,2,15)], 'afrodite', ['F001'])
h([(54,16,16)], '4.6 数据分析')
p([(54,17,30)], 'data_roles')
p([(55,3,12)], 'matrix', ['F002'])
p([(55,13,14),(56,3,13)], 'gated', ['F003'])
p([(56,14,15),(57,3,4)], 'coincidence_tools')
h([(57,5,5)], '4.7 γ跃迁的角关联')
h([(57,6,6)], '4.7.1 角分布', 4)
p([(57,7,9),(58,1,3)], 'angular_distribution')
specs.append(dict(type='equation', id='E003', page=58, parts=[(58,4,4)], number='4.3',
                  bbox=[195,155,531,192], label='角分布的勒让德展开', cn='归一化实验强度所拟合的勒让德展开，保留原式。'))
p([(58,5,6)], 'coefficients')
specs.append(dict(type='equation', id='E004', page=58, parts=[(58,7,9)], number='4.4',
                  bbox=[247,253,530,305], label='原文混合比定义', cn='原文写出的E2/M1矩阵元比；未在译文中补入其它章节的能量或单位因子。'))
p([(58,10,14)], 'mixing_definition')
p([(58,15,17)], 'attenuation')
h([(58,18,18)], '4.7.2 角关联', 4)
p([(58,19,28)], 'dco_intro')
specs.append(dict(type='equation', id='E005', page=59, parts=[(59,1,3)], number='4.5',
                  bbox=[215,80,532,135], label='DCO比：互换门与目标角度', cn='DCO比的分子、分母具有互换的目标角与门角；保留原式。'))
p([(59,4,13)], 'dco_values')
p([(59,14,15)], 'rad_intro')
specs.append(dict(type='equation', id='E006', page=59, parts=[(59,16,18)], number='4.6',
                  bbox=[197,351,532,407], label='角分布比：全部探测器设门', cn='目标γ的两个角度强度相除，门γ在全部探测器中选取；保留原式。'))
p([(59,19,24)], 'rad_definition')
p([(59,25,30)], 'rad_values')
h([(60,0,1)], '第5章 实验结果', 2)
h([(60,2,2)], '5.1 引言')
p([(60,3,7)], 'intro5')
p([(60,8,13)], 'two_experiments')
p([(60,14,14)], 'discussion_next')
h([(61,1,1)], '5.2 133Ce的结果')
h([(61,2,2)], '5.2.1 实验细节', 4)
p([(61,3,14)], 'ce_experiment')
h([(61,15,15)], '5.2.2 133Ce的实验结果', 4)
p([(61,16,21)], 'ce_scheme', ['F004'])
h([(61,22,22)], '5.2.2.1 负宇称带', 4)
h([(61,23,23)], 'Band 1', 5)
p([(61,24,28),(62,1,3)], 'ce_band1', ['T002'])
h([(62,4,4)], 'Band 4', 5)
p([(62,5,16)], 'ce_band4', ['T003','F005'])
p([(62,17,21)], 'gate_871')
p([(62,22,35),(63,1,3)], 'doublet')
p([(63,4,8)], 'gate_936')
p([(63,9,14)], 'gate_795')
h([(63,15,15)], '5.2.2.2 正宇称带', 4)
h([(63,16,16)], 'Band 2', 5)
p([(63,17,26)], 'ce_band2', ['T004'])
p([(63,27,31),(64,1,5)], 'gate_positive', ['F006'])
h([(64,6,6)], 'Band 3', 5)
p([(64,7,14)], 'ce_band3', ['T005'])
h([(72,1,1)], '5.3 131Ba的结果')
h([(72,2,2)], '5.3.1 实验细节', 4)
p([(72,3,12)], 'ba_experiment')
p([(72,13,20)], 'ba_daq')
h([(72,21,21)], '5.3.2 131Ba的实验结果', 4)
p([(72,22,27)], 'ba_scheme', ['F007'])
h([(73,3,3)], '5.3.2.1 负宇称带', 4)
h([(73,4,4)], 'Band 1', 5)
p([(73,5,12)], 'ba_band1')
h([(74,1,1)], '5.3.2.2 正宇称带', 4)
h([(74,2,2)], 'Band 2', 5)
p([(74,3,14)], 'ba_band2')
h([(74,15,15)], 'Band 3', 5)
p([(74,16,19)], 'ba_band3')

# Crops exclude captions; the captions remain separate bilingual source blocks.
assets = [
 dict(id='T001',page=53,number='4.1',type='table',bbox=[113,435,488,489],parts=[(53,17,17)],caption_parts=[(53,18,19)],key='table41',title='γ跃迁多极性与宇称'),
 dict(id='F001',page=55,number='4.1',type='figure',bbox=[76,80,560,445],parts=[],caption_parts=[(55,1,2)],key='fig41',title='AFRODITE探测器方位'),
 dict(id='F002',page=56,number='4.2',type='figure',bbox=[107,80,534,414],parts=[],caption_parts=[(56,1,2)],key='fig42',title='对称γ–γ矩阵示意'),
 dict(id='F003',page=57,number='4.3',type='figure',bbox=[107,80,572,391],parts=[],caption_parts=[(57,1,2)],key='fig43',title='符合关系、纲图与门谱'),
 dict(id='F004',page=65,number='5.1',type='figure',bbox=[172,74,490,720],parts=[],caption_parts=[(65,1,1)],key='fig51',title='133Ce部分能级纲图',rotate=90),
 dict(id='T002',page=66,number='5.1',type='table',bbox=[121,78,513,450],parts=[(66,1,4)],caption_parts=[(66,5,6)],key='table51',title='133Ce yrast Band 1的跃迁'),
 dict(id='T003',page=67,number='5.2',type='table',bbox=[121,78,513,606],parts=[(67,1,5)],caption_parts=[(67,6,7)],key='table52',title='133Ce Band 4的跃迁'),
 dict(id='F005',page=68,number='5.2',type='figure',bbox=[17,99,546,570],parts=[(68,1,73)],caption_parts=[(68,74,75)],key='fig52',title='133Ce Band 4的四组门谱'),
 dict(id='T004',page=69,number='5.3',type='table',bbox=[121,78,487,330],parts=[(69,1,5)],caption_parts=[(69,6,7)],key='table53',title='133Ce Band 2的跃迁'),
 dict(id='F006',page=70,number='5.3',type='figure',bbox=[8,181,544,601],parts=[(70,1,60)],caption_parts=[(70,61,62)],key='fig53',title='133Ce Band 2的四组门谱'),
 dict(id='T005',page=71,number='5.4',type='table',bbox=[121,78,487,399],parts=[(71,1,5)],caption_parts=[(71,6,7)],key='table54',title='133Ce Band 3的跃迁'),
 dict(id='F007',page=73,number='5.4',type='figure',bbox=[107,80,563,387],parts=[],caption_parts=[(73,1,2)],key='fig54',title='131Ba部分能级纲图'),
]


def extract(parts):
    pieces=[]
    for page,start,end in parts:
        blocks=doc[page-1].get_text('blocks')
        pieces.extend(b[4] for b in blocks[start:end+1])
    raw=' '.join(pieces)
    # Join PDF line endings only; original spelling/claims are not corrected.
    normalized=unicodedata.normalize('NFKC',raw)
    normalized=re.sub(r'([A-Za-z])[-‐]\s+([a-z])',r'\1\2',normalized)
    normalized=re.sub(r'\s+',' ',normalized).strip()
    # Recover elementary inline typography from the visually checked text layer.
    normalized=re.sub(r'\b(\d{2,3})(Ce|Ba|Te|Sn|C)\b',r'$^{\1}$\2',normalized)
    normalized=re.sub(r'Iπ\s*=\s*(\d+/\d+)([−+])',lambda m:'$I^\\pi='+m[1]+('^-' if m[2]=='−' else '^+')+'$',normalized)
    normalized=re.sub(r'α\s*=\s*([+−-]?\d+/\d+)',lambda m:'$\\alpha='+m[1].replace('−','-')+'$',normalized)
    normalized=normalized.replace('2.8 × 1010',r'$2.8\times10^{10}$').replace('5.4 × 109',r'$5.4\times10^9$').replace('1.2 × 109',r'$1.2\times10^9$')
    normalized=normalized.replace('∼10−20s',r'$\sim10^{-20}$ s').replace('∼10−19s',r'$\sim10^{-19}$ s')
    normalized=normalized.replace('νh11/2',r'$\nu h_{11/2}$').replace('mg/cm2','mg/cm²')
    return normalized


def boxes(parts):
    return [{'page':n,'printed_page':n-11,'PDF_text_block_indices_zero_based':[a,b],
             'bbox':list(fitz.Rect(doc[n-1].get_text('blocks')[a][:4]) |
                         fitz.Rect(doc[n-1].get_text('blocks')[b][:4]))}
            for n,a,b in parts]


def render_crop(page, bbox, path, rotation=0):
    target=OUT/path;target.parent.mkdir(parents=True,exist_ok=True)
    doc[page-1].get_pixmap(matrix=fitz.Matrix(2.5,2.5),clip=fitz.Rect(bbox)).save(target)
    if rotation:
        with Image.open(target) as im:im.rotate(rotation,expand=True).save(target)


def main():
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED
    translations=json.loads((OUT/'translations.json').read_text())
    blocklist=[];figures=[];tables=[];equations=[];counter=0;captions=0;placed=set()
    md=['---','title: "133Ce论文第4–5章：实验技术与结果逐段中英对照"',
        'scope: "PDF51–74 / printed40–63 only"', 'status: chapter-reader-complete-with-audit-boundaries',
        'source_sha256: '+EXPECTED,'---','',
        '# 第4–5章逐段中英对照','',
        '来源为用户提供的Wakudyanaye 2022硕士论文。仅覆盖第4、5章PDF51–74（印刷40–63页）；不代表全论文翻译完成。Original保留原论断、引文及疑点；中文忠实翻译。独立审计集中在文末，不能当作原文结论。公式和表格采用原件裁图，图注逐条对照。',
        '', '## 页码与章节索引','',
        '- [第4章：实验技术](#chapter4) · PDF51–59 / 印40–48',
        '- [第5章：实验结果](#chapter5) · PDF60–74 / 印49–63',
        '- [术语表](#glossary) · [独立审计与使用边界](#audit)',
        '', '## 公式索引','']
    for s in specs:
        if s['type']=='equation':
            md.append(f"- [{s['id']} · 式({s['number']})](#{s['id']}) · PDF{s['page']} / 印{s['page']-11}：{s['label']}")
    md.extend(['','页面导航：'+' · '.join(f'[PDF{n}](#page{n})' for n in range(51,75)),''])
    pageanchors=set()
    aid={a['id']:a for a in assets}

    def source_label(parts):
        nums=list(dict.fromkeys(x[0] for x in parts))
        return ', '.join(f'PDF{n} / 印{n-11}' for n in nums)

    def add_asset(asset, after):
        nonlocal captions
        if asset['id'] in placed:return
        placed.add(asset['id']);captions+=1
        cid=f'C{captions:03d}';path=f"assets/{asset['type']}s/{asset['id']}.png"
        render_crop(asset['page'],asset['bbox'],path,asset.get('rotate',0))
        caption=extract(asset['caption_parts']);cn=translations[asset['key']]
        item={**{k:v for k,v in asset.items() if k not in ('key','parts','caption_parts')},
              'caption_id':cid,'image_path':path,'placed_after':after,'placement_hint':'near_first_substantive_mention',
              'source_segments':boxes(asset['parts']) if asset['parts'] else [],
              'source_caption_segments':boxes(asset['caption_parts'])}
        (figures if asset['type']=='figure' else tables).append(item)
        blocklist.append(dict(id=asset['id'],page=asset['page'],type=asset['type'],order=len(blocklist)+1,
                              original_text=f"{'Figure' if asset['type']=='figure' else 'Table'} {asset['number']}",
                              translation=asset['title'],bbox=asset['bbox'],image_path=path,
                              refs=[cid],insert_after=after,confidence='high'))
        blocklist.append(dict(id=cid,page=asset['page'],type='caption',order=len(blocklist)+1,
                              original_text=caption,translation=cn,source_segments=boxes(asset['caption_parts']),
                              refs=[asset['id']],confidence='high'))
        name='图' if asset['type']=='figure' else '表'
        md.extend([f'<a id="{asset["id"]}"></a>',f'##### {name}{asset["number"]} · {asset["title"]}','',
                   f'**Placed near:** {after}；原图/表来源PDF{asset["page"]} / 印{asset["page"]-11}，裁图未改数字。','',
                   f'![{name}{asset["number"]} 原件裁图]({path})','',f'<a id="{cid}"></a>',
                   f'**Source:** PDF{asset["page"]} / 印{asset["page"]-11} · {cid}','',
                   '**Original caption:** '+caption,'','**中文图注:** '+cn,''])
        if asset['type']=='table':
            md.extend(['**表头对照：** '+('L：多极阶数；πiπf：初末态宇称乘积；E/M：电/磁多极类型。' if asset['id']=='T001' else 'Ei(keV)：初态能量；Iπi→Iπf：初末态自旋宇称；Eγ：γ能量；Iγ：相对γ强度；Multipolarity：多极性。原数值、空缺横线及误差均以裁图为准。'),''])

    for s in specs:
        page=s.get('page',s.get('parts',[(0,0,0)])[0][0])
        for pg,_,_ in s.get('parts',[]):
            if pg not in pageanchors:
                pageanchors.add(pg);md.extend([f'<a id="page{pg}"></a>',f'**页锚：PDF{pg} / 印{pg-11}**',''])
        if s['type']=='equation':
            path=f"assets/equations/{s['id']}.png";render_crop(page,s['bbox'],path)
            item=dict(id=s['id'],page=page,type='equation',order=len(blocklist)+1,equation_number=s['number'],
                      latex=None,bbox=s['bbox'],confidence='high',representation='original-crop-fallback',
                      image_path=path,original_text=extract(s['parts']),translation=s['cn'],source_segments=boxes(s['parts']))
            blocklist.append(item);equations.append(item.copy())
            md.extend([f'<a id="{s["id"]}"></a>',f'**Source:** PDF{page} / 印{page-11} · {s["id"]} · 原式({s["number"]})','',
                       f'![原式({s["number"]}) · {s["id"]}]({path})','',
                       '**中文说明:** '+s['cn'],'','*原件裁图回退；未另作LaTeX转写，公式只显示一次。*',''])
            continue
        counter+=1;sid=f'S{counter:03d}'
        raw=extract(s['parts']);original=s.get('original_override') or raw
        cn=s['translation'] if s['type']=='heading' else translations[s['translation_key']]
        item=dict(id=sid,page=page,type=s['type'],order=len(blocklist)+1,
                  original_text=original,extracted_text_raw_reflow=raw,translation=cn,
                  source_segments=boxes(s['parts']),refs=s.get('refs',[]),confidence='high')
        blocklist.append(item)
        if s['type']=='heading':
            if page in [51,60] and len(s['parts'][0])==3 and s['parts'][0][1]==0:
                md.append('<a id="chapter4"></a>' if page==51 else '<a id="chapter5"></a>')
            md.extend(['#'*s['level']+' '+cn,''])
        md.extend([f'<a id="{sid}"></a>',f'**Source:** {source_label(s["parts"])} · {sid}','',
                   '**Original:** '+original,'','**中文:** '+cn,''])
        for ref in s.get('refs',[]):add_asset(aid[ref],sid)
    # Page-only figure/table sheets have already been inserted at the first discussion.
    for pg in range(51,75):
        if pg not in pageanchors:
            pageanchors.add(pg)
            names=[a['id'] for a in assets if a['page']==pg]
            md.extend([f'<a id="page{pg}"></a>',f'**页锚：PDF{pg} / 印{pg-11}**；此页为已在首次讨论处插入的图表：'+', '.join(f'[{x}](#{x})' for x in names)+'。',''])
    glossary=translations['_glossary']
    md.extend(['<a id="glossary"></a>','## 术语表','','| Original term | 中文统一译法 | 使用说明 |','|---|---|---|'])
    for g in glossary:md.append('| '+g['term']+' | '+g['translation']+' | '+g.get('note','')+' |')
    md.extend(['','<a id="audit"></a>','## 独立审计与使用边界','',translations['_audit'],''])
    (OUT/'paper.md').write_text('\n'.join(md)+'\n')
    pages=[dict(page=n,printed_page=n-11,block_ids=[b['id'] for b in blocklist if b['page']==n or
                          any(q['page']==n for q in b.get('source_segments',[]))]) for n in range(51,75)]
    result=dict(paper=dict(title='Triaxiality and Rotational Bands in 133Ce — Chapters 4 and 5',
                    author='Ignasio Wakudyanaye',degree='Magister Scientiae',year=2022,
                    source_type='pdf-text',source_path=str(SOURCE.relative_to(ROOT)),sha256=EXPECTED,
                    assigned_PDF_pages=[51,74],assigned_printed_pages=[40,63],whole_thesis_complete=False),
                blocks=blocklist,pages=pages,figures=figures,tables=tables,equations=equations,glossary=glossary,
                normalization_notes=['NFKC ligature/spacing normalization','line-end English hyphen joining only',
                                     'original grammatical, numerical and scientific assertions are not silently corrected',
                                     'all display equations and table cells are preserved as exact source crops'])
    (OUT/'source_map.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    (OUT/'translation_notes.md').write_text(translations['_notes']+'\n')
    assert placed==set(aid)
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==EXPECTED
    print(json.dumps(dict(body_and_heading_blocks=counter,total_blocks=len(blocklist),figures=len(figures),
                           tables=len(tables),equations=len(equations),source_sha256=EXPECTED),ensure_ascii=False))


if __name__=='__main__':main()
