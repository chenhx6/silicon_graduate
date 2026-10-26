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
SOURCE = ROOT/'raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf'
EXPECTED = '48556dbfe5284efebdb901cd949f534ac5552c6504e2c744603afca386660080'
doc = fitz.open(SOURCE)
specs = []
assets = []


def h(parts, cn, level=3):
    specs.append(dict(type='heading', parts=parts, translation=cn, level=level))


def p(parts, key, refs=None, original=None):
    specs.append(dict(type='paragraph', parts=parts, translation_key=key,
                      refs=refs or [], original_override=original))

h([(75,0,1)], '第6章 讨论', 2)
h([(75,2,2)], '6.1 引言')
p([(75,3,12)],'region')
p([(75,13,19)],'two_parts')
h([(76,1,2)],'6.2 第一部分：133Ce与131Ba中g7/2[404]7/2+结构的解释')
p([(76,3,17)],'positive_assignment')
p([(76,18,23)],'n73_analogy')
p([(76,24,29)],'staggering_mechanisms')
h([(77,1,1)],'6.2.1 133Ce Band 2的旋称劈裂',4)
p([(77,2,10)],'positive_space')
p([(77,20,31)],'positive_pes',['T001','T002'])
p([(78,1,5)],'positive_moi')
p([(79,1,10)],'ce_gamma_low',['F001'])
p([(79,11,25)],'ce_gamma_large',['F002'])
p([(79,26,34)],'komega')
p([(80,1,4)],'basis_three',['T003'])
p([(81,3,8),(82,67,76)],'ce_wavefunction_plot',['F003'])
p([(82,77,86)],'ce_wavefunction_spin')
p([(82,87,90),(83,26,35),(84,1,2)],'ce_mixing')
p([(84,3,11)],'ce_chi_axial',['F004'])
p([(84,12,21)],'ce_chi_triaxial',['F005'])
h([(87,1,1)],'6.2.2 131Ba Band 2的旋称劈裂',4)
p([(87,2,10)],'ba_space_moi')
p([(87,11,20)],'ba_orbitals',['T004'])
p([(87,21,27)],'ba_axial',['F006'])
p([(87,28,34),(88,95,101)],'ba_gamma',['F007'])
p([(88,102,104)],'ba_result')
p([(90,3,7),(91,1,4)],'ba_wavefunction_head',['T005'])
p([(91,71,78)],'ba_wavefunction_plot',['F008'])
p([(91,79,87)],'ba_wavefunction_spin')
p([(91,88,90),(92,25,29)],'ba_klhalf')
p([(92,30,33),(93,1,2)],'ba_realign')
p([(93,3,10)],'ba_chi',['F009','F010'])
p([(93,11,23)],'positive_synthesis')
h([(96,1,2)],'6.2.3 Z=75同位素πg7/2[404]7/2+带中的旋称劈裂',4)
p([(96,3,10)],'proton_comparison')
p([(96,11,20)],'proton_levels')
h([(97,1,1)],'6.2.4 第一部分小结',4)
p([(97,2,7)],'positive_summary1')
p([(97,8,13)],'positive_summary2')
h([(98,1,2)],'6.3 第二部分：133Ce负宇称结构的解释')
h([(98,3,3)],'6.3.1 引言',4)
p([(98,4,15)],'negative_background')
p([(98,16,23)],'negative_assignment')
h([(98,24,25)],'6.3.2 133Ce h11/2带的倾斜进动（TiP）解释',4)
p([(98,26,30),(99,1,2)],'negative_inputs')
p([(99,3,10)],'negative_orbitals',['T006'])
p([(99,93,98),(100,1,3)],'negative_orbital18')
p([(100,4,14)],'negative_energy',['F011'])
p([(100,15,27)],'negative_bandheads')
h([(100,28,28)],'Band 1的波函数',5)
p([(100,29,32),(101,27,31),(102,1,2)],'negative_wavefunction_head',['T007','F012'])
p([(102,3,12)],'negative_wavefunction_lowspin')
p([(102,128,130)],'negative_wavefunction_midspin')
p([(103,22,24)],'negative_wavefunction_highspin')
p([(103,25,29)],'negative_wavefunction_stagger')
h([(104,1,1)],'Band 4的波函数',5)
p([(104,2,8)],'band4_coupling',['T008'])
p([(104,78,88)],'band4_head',['F013'])
p([(105,18,26)],'band4_lowspin')
p([(105,27,30),(106,1,3)],'band4_highspin')
h([(107,1,1)],'6.3.3 133Ce h11/2带的冻结对齐（FA）近似',4)
p([(107,2,18)],'fa_conditions')
p([(107,19,23)],'fa_invalid')
p([(107,24,31)],'fa_inputs')
p([(108,1,15)],'fa_energy',['F014'])
p([(108,16,22)],'fa_components1')
p([(108,23,28)],'fa_components4')
h([(110,1,1)],'6.3.4 电磁性质',4)
p([(110,2,4)],'em_controversy')
p([(110,5,13)],'em_hfa')
p([(110,14,18)],'em_comparison',['T009','T010'])
p([(110,19,29)],'em_criterion')
p([(110,30,31)],'em_pr_rejection')
p([(110,32,33),(111,1,15)],'em_experiment',['T011'])
p([(111,16,18)],'em_intraband',['F015'])
p([(113,24,27)],'em_fa_delta')
p([(114,26,33),(115,1,2)],'em_rates',['F016'])
h([(115,3,3)],'6.3.5 第二部分小结',4)
p([(115,4,15)],'negative_summary1')
p([(115,16,25)],'negative_summary2')


def bounds(page, first, last, padding=5, include_images=False):
    blocks=doc[page-1].get_text('blocks')
    rect=fitz.Rect(blocks[first][:4])
    for b in blocks[first+1:last+1]:rect|=fitz.Rect(b[:4])
    if include_images:
        for im in doc[page-1].get_image_info():rect|=fitz.Rect(im['bbox'])
    rect+=(-padding,-padding,padding,padding)
    return list(rect & doc[page-1].rect)


def table(num,page,bodyparts,captionparts,title,rotate=0):
    rect=bounds(page,bodyparts[0][1],bodyparts[-1][2],5)
    assets.append(dict(id=f'T{num:03d}',page=page,number=f'6.{num}',type='table',bbox=rect,
                       parts=bodyparts,caption_parts=captionparts,key=f'table{num}',title=title,rotate=rotate))


def figure(num,page,captionparts,title,bodyparts=None):
    if bodyparts:
        rect=bounds(page,bodyparts[0][1],bodyparts[-1][2],6,True)
    else:
        rect=list(fitz.Rect(doc[page-1].get_image_info()[0]['bbox']))
    assets.append(dict(id=f'F{num:03d}',page=page,number=f'6.{num}',type='figure',bbox=rect,
                       parts=bodyparts or [],caption_parts=captionparts,key=f'fig{num}',title=title))


table(1,77,[(77,11,17)],[(77,18,19)],'PES计算给出的形变参数')
table(2,78,[(78,6,96)],[(78,97,98)],'133Ce正宇称单粒子轨道')
table(3,82,[(82,1,64)],[(82,65,66)],'133Ce Band 2波函数的主要分量')
table(4,88,[(88,1,92)],[(88,93,94)],'131Ba正宇称单粒子轨道')
table(5,91,[(91,5,68)],[(91,69,70)],'131Ba Band 2波函数的主要分量')
table(6,99,[(99,11,90)],[(99,91,92)],'133Ce负宇称单粒子轨道')
table(7,102,[(102,13,125)],[(102,126,127)],'133Ce yrast带波函数的主要分量')
table(8,104,[(104,9,75)],[(104,76,77)],'133Ce Band 4波函数的主要分量')
table(9,111,[(111,19,23)],[(111,24,25)],'Band 4的QTR电磁跃迁性质')
table(10,111,[(111,26,30)],[(111,31,31)],'Band 4的FA电磁跃迁性质')
table(11,112,[(112,1,13)],[(112,14,14)],'Band 4混合比及相对跃迁几率实验值',rotate=-90)
figure(1,80,[(80,5,6)],'133Ce：全强度Coriolis、γ=0°/10°')
figure(2,81,[(81,1,2)],'133Ce：全强度Coriolis、γ=15°/20°')
figure(3,83,[(83,24,25)],'133Ce Band 2波函数沿长轴的投影',[(83,1,23)])
figure(4,85,[(85,1,1)],'133Ce：70%Coriolis、γ=0°/10°')
figure(5,86,[(86,1,1)],'133Ce：70%Coriolis、γ=15°/20°')
figure(6,89,[(89,1,2)],'131Ba：全强度Coriolis、γ=0°/10°')
figure(7,90,[(90,1,2)],'131Ba：全强度Coriolis、γ=15°/20°')
figure(8,92,[(92,23,24)],'131Ba Band 2波函数',[(92,1,22)])
figure(9,94,[(94,1,2)],'131Ba：70%Coriolis、γ=0°/10°')
figure(10,95,[(95,1,1)],'131Ba：70%Coriolis、γ=15°/20°')
figure(11,101,[(101,25,26)],'133Ce负宇称带能量与旋称劈裂',[(101,1,24)])
figure(12,103,[(103,20,21)],'133Ce yrast带波函数沿长轴的投影',[(103,1,19)])
figure(13,105,[(105,16,17)],'133Ce Band 4波函数沿长轴的投影',[(105,1,15)])
figure(14,109,[(109,23,24)],'FA近似的能量和旋称劈裂',[(109,1,22)])
figure(15,113,[(113,22,23)],'带内与带间混合比的逐项比较',[(113,1,21)])
figure(16,114,[(114,24,25)],'Band 4→Band 1相对电磁强度',[(114,1,23)])
# The top frame/curves of this vector figure extend above its highest text label.
next(a for a in assets if a['id']=='F014')['bbox']=[20,147,538,615]


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
    original_overrides=translations.get('_original_overrides',{})
    blocklist=[];figures=[];tables=[];equations=[];counter=0;captions=0;placed=set()
    md=['---','title: "133Ce论文第6章：讨论逐段中英对照"',
        'scope: "PDF75–115 / printed64–104 only"', 'status: chapter-reader-complete-with-audit-boundaries',
        'source_sha256: '+EXPECTED,'---','',
        '# 第6章逐段中英对照','',
        '来源为用户提供的Wakudyanaye 2022硕士论文。仅覆盖第6章PDF75–115（印刷64–104页）；不代表全论文翻译完成。Original保留原论断、引文及疑点；中文忠实翻译。独立审计集中在文末，不能当作原文结论。公式和表格采用原件裁图，图注逐条对照。',
        '', '## 页码与章节索引','',
        '- [第6章：讨论](#chapter6) · PDF75–115 / 印64–104',
        '- [第一部分：g7/2旋称劈裂](#part1) · PDF76–97',
        '- [第二部分：h11/2负宇称带](#part2) · PDF98–115',
        '- [术语表](#glossary) · [独立审计与使用边界](#audit)',
        '', '本章没有新增编号的独立公式。表中公式与矩阵元按原图保留；正文中的行内数学按原意排版。','']
    for s in specs:
        if s['type']=='equation':
            md.append(f"- [{s['id']} · 式({s['number']})](#{s['id']}) · PDF{s['page']} / 印{s['page']-11}：{s['label']}")
    md.extend(['','页面导航：'+' · '.join(f'[PDF{n}](#page{n})' for n in range(75,116)),''])
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
        caption=original_overrides.get(asset['key']) or extract(asset['caption_parts']);cn=translations[asset['key']]
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
            md.extend(['**表头对照：** '+(asset.get('table_legend','原数值、振幅符号、下标、空缺横线、单位和误差均以裁图为准。')),''])

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
        raw=extract(s['parts']);original=s.get('original_override') or original_overrides.get(s.get('translation_key')) or raw
        cn=s['translation'] if s['type']=='heading' else translations[s['translation_key']]
        item=dict(id=sid,page=page,type=s['type'],order=len(blocklist)+1,
                  original_text=original,extracted_text_raw_reflow=raw,translation=cn,
                  source_segments=boxes(s['parts']),refs=s.get('refs',[]),confidence='high')
        blocklist.append(item)
        if s['type']=='heading':
            if page==75 and s['parts'][0][1]==0:md.append('<a id="chapter6"></a>')
            if page==76 and s['parts'][0][1]==1:md.append('<a id="part1"></a>')
            if page==98 and s['parts'][0][1]==1:md.append('<a id="part2"></a>')
            md.extend(['#'*s['level']+' '+cn,''])
        md.extend([f'<a id="{sid}"></a>',f'**Source:** {source_label(s["parts"])} · {sid}','',
                   '**Original:** '+original,'','**中文:** '+cn,''])
        for ref in s.get('refs',[]):add_asset(aid[ref],sid)
    # Page-only figure/table sheets have already been inserted at the first discussion.
    for pg in range(75,116):
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
                          any(q['page']==n for q in b.get('source_segments',[]))]) for n in range(75,116)]
    result=dict(paper=dict(title='Triaxiality and Rotational Bands in 133Ce — Chapter 6',
                    author='Ignasio Wakudyanaye',degree='Magister Scientiae',year=2022,
                    source_type='pdf-text',source_path=str(SOURCE.relative_to(ROOT)),sha256=EXPECTED,
                    assigned_PDF_pages=[75,115],assigned_printed_pages=[64,104],whole_thesis_complete=False),
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
