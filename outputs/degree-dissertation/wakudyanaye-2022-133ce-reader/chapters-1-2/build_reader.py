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
specs=[]
assets=[]


def h(parts, cn, level=3):
    specs.append(dict(type='heading',parts=parts,translation=cn,level=level))


def p(parts,key,refs=None,original=None):
    specs.append(dict(type='paragraph',parts=parts,translation_key=key,refs=refs or [],original_override=original))


def bounds(page,start,end,padding=6):
    bs=doc[page-1].get_text('blocks');r=fitz.Rect(bs[start][:4])
    for b in bs[start+1:end+1]:r|=fitz.Rect(b[:4])
    r+=(-padding,-padding,padding,padding)
    return list(r & doc[page-1].rect)


def eq(num,page,start,end,label):
    specs.append(dict(type='equation',id=f'E{num:03d}',page=page,parts=[(page,start,end)],number=f'2.{num}',bbox=bounds(page,start,end),label=label,cn='原式保留于上方裁图；译文不补写、改号或修正公式系数。'))

h([(12,0,1)],'第1章 引言',2)
h([(12,2,2)],'1.1 引言')
p([(12,3,11)],'excitation')
p([(12,12,19)],'vibration_rotation')
p([(12,20,22),(13,1,4)],'triaxial_regions')
p([(13,5,18)],'spectroscopy')
p([(13,19,27)],'work_roles')
p([(13,28,28)],'outline_intro')
p([(13,29,32)],'outline2')
p([(13,33,34),(14,1,2)],'outline3')
p([(14,3,4)],'outline4')
p([(14,5,9)],'outline5a')
p([(14,10,12)],'outline5b')
p([(14,13,18)],'outline6a')
p([(14,19,25)],'outline6b')
p([(14,26,27)],'outline7')
h([(15,0,1)],'第2章 理论基础',2)
h([(15,2,2)],'2.1 引言')
p([(15,3,4)],'schrodinger')
eq(1,15,5,5,'定态Schrödinger方程')
p([(15,6,8)],'hamiltonian_intro')
eq(2,15,9,16,'多核子Hamiltonian')
p([(15,17,19)],'momentum')
p([(15,20,22)],'models')
h([(16,1,1)],'2.2 核势与壳模型')
p([(16,2,8)],'magic_intro')
eq(3,16,9,9,'原文列出的幻数')
p([(16,10,17)],'meanfield')
p([(16,18,22)],'residual')
eq(4,16,23,32,'平均场与剩余相互作用')
p([(16,33,35)],'square_intro',['F001'])
eq(5,17,1,6,'无限深方势阱')
p([(17,7,10)],'square_magic',['F002'])
p([(17,11,12)],'ho_intro')
eq(6,17,13,14,'谐振子势')
p([(17,15,17)],'ho_spectrum')
eq(7,17,18,19,'谐振子能级')
p([(17,20,26)],'oscillator_quantum')
p([(17,27,30)],'ws_intro')
eq(8,17,31,31,'Woods–Saxon势')
p([(18,3,8)],'ws_parameters')
p([(18,9,15)],'modified_ho')
h([(19,1,1)],'2.2.1 自旋–轨道项',4)
p([(19,2,5)],'spinorbit_intro')
eq(9,19,6,6,'自旋–轨道相互作用')
p([(19,7,12)],'spinorbit_splitting')
p([(19,13,14)],'ws_modified')
eq(10,19,15,15,'包含自旋–轨道项的W–S势')
p([(19,16,16)],'ho_modified')
eq(11,19,17,18,'修正谐振子势')
p([(19,19,24)],'coulomb')
p([(19,25,30)],'spectroscopic_labels')
h([(21,1,1)],'2.3 核形变')
p([(21,2,6)],'deformation_evidence')
eq(12,21,7,13,'核表面球谐展开')
p([(21,14,17)],'surface_symbols')
p([(21,18,23)],'quadrupole_coefficients')
eq(13,21,24,24,'α20与β2、γ')
p([(21,25,25)],'and')
eq(14,21,26,27,'α22与β2、γ')
p([(21,28,33),(22,1,2)],'beta_gamma')
eq(15,22,3,6,'三个轴向半径偏离：保留原系数')
p([(22,7,16)],'lund',['F003'])
p([(22,17,21)],'epsilon_beta')
p([(22,22,26)],'higher_multipoles')
h([(22,27,27)],'2.3.1 Nilsson模型',4)
p([(22,28,30),(23,3,9)],'nilsson_intro')
p([(23,10,11)],'nilsson_ham_intro')
eq(16,23,12,15,'三轴修正谐振子Hamiltonian')
p([(23,16,22)],'nilsson_frequencies_intro')
eq(17,24,1,2,'x方向振动频率')
eq(18,24,3,4,'y方向振动频率')
eq(19,24,5,6,'z方向振动频率')
p([(24,7,7)],'axial_ham_intro')
eq(20,24,8,10,'轴对称形变Hamiltonian')
p([(24,11,15)],'volume_conservation')
p([(24,16,21)],'nilsson_splitting')
p([(24,22,39)],'gseven_example',['F005','F006'])
p([(24,40,43),(25,3,5)],'nilsson_quantum')
p([(25,6,11)],'nilsson_coupling',['F004'])
p([(25,12,20)],'pairing')
h([(28,1,1)],'2.4 核集体性')
p([(28,2,14)],'collectivity')
h([(28,15,15)],'2.4.1 核转动',4)
p([(28,16,23)],'rotation_symmetry')
p([(28,24,25)],'rigid_rotor')
eq(21,28,26,27,'经典刚性转子能量')
p([(28,28,29)],'quantize')
eq(22,29,1,2,'量子转子能量')
p([(29,3,7)],'even_even_band')
p([(29,8,15)],'rotational_band')
p([(29,16,18)],'triaxial_rotation')
h([(29,19,19)],'2.4.2 粒子–转子耦合',4)
p([(29,20,22)],'particle_rotor_intro')
eq(23,29,23,23,'总角动量的粒子–核芯耦合')
p([(29,24,29)],'coupling_limits',['F007'])
h([(30,1,1)],'2.4.2.1 强耦合极限',4)
p([(30,2,9)],'strong_quantum')
p([(30,10,12)],'strong_wavefunction')
p([(30,13,13)],'strong_ham_intro')
eq(24,30,14,18,'粒子–核芯Hamiltonian展开：保留交叉项')
p([(30,19,23)],'strong_ham_symbols')
eq(25,30,24,25,'升降算符表示的耦合项')
p([(30,26,30),(32,1,5)],'coriolis_recoil')
p([(32,6,8)],'nilsson_intrinsic')
p([(32,9,9)],'strong_energy_intro')
eq(26,32,10,11,'K不等于1/2时的能量')
p([(32,12,20)],'strong_energy_band')
p([(32,21,24)],'khalf_intro')
eq(27,32,25,26,'K=1/2退耦能谱')
p([(32,27,28)],'decoupling_intro')
eq(28,32,29,34,'退耦参数a')
p([(33,1,10)],'decoupling_effect')
h([(33,11,11)],'2.4.2.2 转动对齐极限',4)
p([(33,12,23)],'rotation_alignment')
p([(33,24,24)],'aligned_energy_intro')
eq(29,33,25,26,'原文的转动对齐能量式')
h([(33,27,27)],'2.5 旋称劈裂')
p([(33,28,32),(34,1,3)],'signature_intro')
eq(30,34,4,4,'原文的旋转算符')
p([(34,5,7)],'signature_definition')
eq(31,34,8,8,'r与α的原文定义')
p([(34,9,10)],'signature_spin')
eq(32,34,11,11,'α与自旋的模2关系')
p([(34,12,12)],'signature_even')
eq(33,34,13,13,'偶质量核的α=0支')
eq(34,34,14,14,'偶质量核的α=1支')
p([(34,15,15)],'signature_odd')
eq(35,34,16,16,'奇质量核的正旋称支：保留原号')
eq(36,34,17,17,'奇质量核的负旋称支：保留原号')
p([(34,18,20),(35,1,5)],'signature_partners')
eq(37,35,6,7,'能量交错参数S(I)')
p([(35,8,13)],'signature_inversion',['F008'])
eq(38,35,14,15,'高j单准粒子组态的有利旋称')


def fig(num,page,captionparts,title,parts=None,bbox=None):
    if bbox is None:bbox=list(doc[page-1].get_image_info()[0]['bbox'])
    assets.append(dict(id=f'F{num:03d}',page=page,number=f'2.{num}',type='figure',bbox=bbox,
                       parts=parts or [],caption_parts=captionparts,key=f'fig{num}',title=title))


fig(1,18,[(18,1,2)],'不同核势的比较')
fig(2,20,[(20,68,69)],'不同核势预言的壳结构',[(20,1,67)],[105,112,532,624])
fig(3,23,[(23,1,2)],'Lund核形状与转动约定')
fig(4,25,[(25,1,2)],'Nilsson模型中的角动量耦合')
fig(5,26,[(26,21,22)],'中子Nilsson图',[(26,1,20)],[61,96,566,728])
fig(6,27,[(27,27,28)],'质子Nilsson图',[(27,1,26)],[90,140,536,702])
fig(7,31,[(31,29,30)],'强耦合与转动对齐的角动量和带结构',[(31,1,28)],[130,110,512,625])
fig(8,35,[(35,16,17)],'典型能量交错曲线')


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
    md=['---','title: "133Ce论文第1–2章：引言与理论基础逐段中英对照"',
        'scope: "PDF12–35 / printed1–24 only"', 'status: chapter-reader-complete-with-audit-boundaries',
        'source_sha256: '+EXPECTED,'---','',
        '# 第1–2章逐段中英对照','',
        '来源为用户提供的Wakudyanaye 2022硕士论文。仅覆盖第1、2章PDF12–35（印刷1–24页）；不代表全论文翻译完成。Original保留原论断、引文及疑点；中文忠实翻译。独立审计集中在文末，不能当作原文结论。公式和表格采用原件裁图，图注逐条对照。',
        '', '## 页码与章节索引','',
        '- [第1章：引言](#chapter1) · PDF12–14 / 印1–3',
        '- [第2章：理论基础](#chapter2) · PDF15–35 / 印4–24',
        '- [术语表](#glossary) · [独立审计与使用边界](#audit)',
        '', '## 公式索引','']
    for s in specs:
        if s['type']=='equation':
            md.append(f"- [{s['id']} · 式({s['number']})](#{s['id']}) · PDF{s['page']} / 印{s['page']-11}：{s['label']}")
    md.extend(['','页面导航：'+' · '.join(f'[PDF{n}](#page{n})' for n in range(12,36)),''])
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
        raw=extract(s['parts']);original=s.get('original_override') or original_overrides.get(s.get('translation_key')) or raw
        cn=s['translation'] if s['type']=='heading' else translations[s['translation_key']]
        item=dict(id=sid,page=page,type=s['type'],order=len(blocklist)+1,
                  original_text=original,extracted_text_raw_reflow=raw,translation=cn,
                  source_segments=boxes(s['parts']),refs=s.get('refs',[]),confidence='high')
        blocklist.append(item)
        if s['type']=='heading':
            if page in [12,15] and s['parts'][0][1]==0:
                md.append('<a id="chapter1"></a>' if page==12 else '<a id="chapter2"></a>')
            md.extend(['#'*s['level']+' '+cn,''])
        md.extend([f'<a id="{sid}"></a>',f'**Source:** {source_label(s["parts"])} · {sid}','',
                   '**Original:** '+original,'','**中文:** '+cn,''])
        for ref in s.get('refs',[]):add_asset(aid[ref],sid)
    # Page-only figure/table sheets have already been inserted at the first discussion.
    for pg in range(12,36):
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
                          any(q['page']==n for q in b.get('source_segments',[]))]) for n in range(12,36)]
    result=dict(paper=dict(title='Triaxiality and Rotational Bands in 133Ce — Chapters 1 and 2',
                    author='Ignasio Wakudyanaye',degree='Magister Scientiae',year=2022,
                    source_type='pdf-text',source_path=str(SOURCE.relative_to(ROOT)),sha256=EXPECTED,
                    assigned_PDF_pages=[12,35],assigned_printed_pages=[1,24],whole_thesis_complete=False),
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
