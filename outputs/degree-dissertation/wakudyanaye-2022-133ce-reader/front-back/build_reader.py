"""Front matter, complete Chapter7 bilingual reader, and original bibliography.
Reference items are preserved, not independently verified or translated.
"""
from pathlib import Path
import json,re,unicodedata,hashlib
import fitz

OUT=Path(__file__).parent
SRC=Path('raw/papers/degree dissertation/Triaxiality and Rotational bands in 133Ce.pdf')
DOC=fitz.open(SRC)
RAW=json.loads((OUT/'extracted_blocks.json').read_text())
BY={(x['pdf_page'],x['block']):x for x in RAW}
spec=[]
def add(page,lo,hi,zh,kind='paragraph',original=None):
    spec.append(dict(page=page,source_blocks=list(range(lo,hi+1)),translation=zh,type=kind,original_override=original))
def clean(s):
    s=unicodedata.normalize('NFC',s)
    for a,b in [('ﬁ','fi'),('ﬀ','ff'),('ﬂ','fl'),('ﬃ','ffi'),('ﬄ','ffl')]:s=s.replace(a,b)
    s=re.sub(r'(?<=[A-Za-z])-\s*\n\s*(?=[A-Za-z])','',s)
    return ' '.join(s.split())
def union(boxes):return [min(b[0] for b in boxes),min(b[1] for b in boxes),max(b[2] for b in boxes),max(b[3] for b in boxes)]

add(1,0,0,'西开普大学','heading')
add(1,1,2,r'$^{133}\mathrm{Ce}$ 中的三轴性与转动带','heading')
add(1,3,4,'作者：Ignasio Wakudyanaye')
add(1,5,6,'本论文按理学硕士（Magister Scientiae）学位要求提交。')
add(1,7,9,'理学院　物理与天文学系')
add(1,10,10,'导师：Elena A. Lawrie 博士（iThemba LABS）')
add(1,11,11,'共同导师：José N. Orce 教授（UWC）')
add(1,12,12,'2022年3月')
add(2,0,0,'声明','heading')
add(2,1,4,r'本人 Ignasio Wakudyanaye 声明，本论文《$^{133}\mathrm{Ce}$ 中的三轴性与转动带》为本人独立完成，此前未曾向其他大学提交以申请任何学位或参加考核；本人使用或引用的全部来源均已通过完整参考文献注明并致谢。')
add(2,5,5,'签名：…………　日期：…………')
add(3,0,1,'“物理学就像性：当然，它也许会带来一些实际成果，但那并不是我们做这件事的原因。”')
add(3,2,2,'理查德·P.费曼')
add(4,0,0,'摘要','heading')
add(4,1,10,r'在 $N=50$ 与 $N=82$ 壳闭合之间的缺中子核，为理解核形状和结构提供了丰富信息。$^{133}\mathrm{Ce}$ 与 $^{131}\mathrm{Ba}$ 这对 $N=75$ 同中子素位于核素图的该区域。本研究考察了近期发现的两条基于 $g_{7/2}$ 轨道的正宇称转动带；两个核中的这些带均建立在 $7/2^+$ 态上。采用准粒子加三轴转子（QTR）模型，研究这些带的激发能及签名劈裂如何依赖三轴性。除三轴性外，还研究了 Coriolis 相互作用对激发能和签名劈裂的影响。')
add(4,11,22,r'本研究还在 $^{133}\mathrm{Ce}$ 中识别出一条新的负宇称带，建立在 $I=13/2^-$ 态上。发现了13条新的带内跃迁，以及把该激发带连接到晕带的15条新带间跃迁。为该结构提出三轴度约20°的三轴单准粒子 $\nu(h_{11/2})^{-1}[514]9/2^-$ 组态。将这些新实验结果与两组QTR模型计算比较：(i)组态空间包含费米面附近的9个负宇称轨道，对应原子核三维倾斜进动的描述；(ii)组态空间仅含1个负宇称轨道，即此前用于描述摆动的冻结排列近似。包含费米面附近9个负宇称轨道的QTR，对实验观测到的能带性质的描述优于冻结排列情况。')
add(4,23,23,'关键词','heading')
add(4,24,25,'签名劈裂；摆动；原子核三轴性；倾斜进动；转动带')
add(5,0,0,'致谢','heading')
add(5,1,1,'首先，我要感谢自己一路走到这里！')
add(5,2,4,'感谢家人坚定地支持我继续求学。在他们的引导和支持下，我走到了今天。前面还有很长的路要走。')
add(5,5,8,'我特别要向导师 Elena Lawrie 博士表达长久的谢意，感谢她出色的指导、启发和鼓励。谢谢您对我的理解与耐心。也感谢共同导师 José Nicolás Orce 教授在我求学期间的支持和指导。')
add(5,9,14,'也要感谢 iThemba LABS 核结构组和 UWC Nuclear Warriors 团队的同事。感谢西开普大学物理与天文学系、iThemba LABS，以及南非国家研究基金会（NRF），通过 MANuS/MatSci 项目为我的学业提供经费支持。')
add(5,15,17,'一路帮助我的人很多，对此我深感幸运和感激！感谢所有曾参与这段旅程的人，衷心谢谢你们！尤其感谢 Robert Lindsay 教授。')
add(116,0,1,'第7章　结论','heading')
add(116,2,7,r'由南非、中国和法国研究人员组成的合作团队，针对 $N=75$ 同中子素 $^{133}\mathrm{Ce}$ 与 $^{131}\mathrm{Ba}$ 采集并分析了详细数据。$^{133}\mathrm{Ce}$ 实验在南非开普敦附近 iThemba LABS 的分离扇形回旋加速器上进行；$^{131}\mathrm{Ba}$ 实验则在意大利 Legnaro 国家实验室的 XTU 串列加速器上完成。')
add(116,8,16,r'这些实验的γ衰变谱学研究取得了多项新结果。在 $^{133}\mathrm{Ce}$ 与 $^{131}\mathrm{Ba}$ 中，各发现一条建立在 $I^\pi=7/2^+$ 态上的正宇称带。本论文的一部分工作是研究 $^{133}\mathrm{Ce}$ 数据中的γ–γ符合关系。符合分析在 $^{133}\mathrm{Ce}$ 中揭示出一条新的强耦合正宇称带，包含9条新跃迁和4个新能级。$^{131}\mathrm{Ba}$ 数据由合作者分析，在一条同样建立于 $I^\pi=7/2^+$ 态的类似强耦合正宇称带中发现13条新跃迁和8个新能级。两条带均表现出明显的签名劈裂。')
add(116,17,21,r'合作者提供了势能面（PES）计算：对 $^{133}\mathrm{Ce}$，建议四极形变 $\varepsilon_2=0.185$、$\gamma\sim10^\circ$；对 $^{131}\mathrm{Ba}$，建议 $\varepsilon_2=0.170$、$\gamma\sim9^\circ$。本论文对两条能带进行了解释，基础是准粒子加三轴转子（QTR）计算。')
add(116,22,23,'本论文对这些正宇称带进行了详细QTR研究，计算采用费米面附近10个QTR模型轨道构成的空间。〔原段续下页〕')
add(117,1,12,r'〔续上页原段〕这些带主要基于QTR轨道 $|\nu\rangle=|20\rangle$，其沿长轴的投影为7/2，近似对应 $\nu g_{7/2}[404]7/2^+$ Nilsson轨道。$^{133}\mathrm{Ce}$ 的计算与 $0^\circ\leq\gamma\leq15^\circ$ 的三轴度一致；对 $^{131}\mathrm{Ba}$，需要 $\gamma\sim15^\circ$ 才能再现实验激发能和能量交错。此外，两核能带均受到 Coriolis 相互作用的强烈影响，它使 $\nu g_{7/2}$ 中子的角动量重新排列、偏离长轴。附近的 $\nu s_{1/2}$ 与 $\nu d_{3/2}$ 轨道的波函数含显著 $K=1/2$ 成分，与带内占主导的 $\nu g_{7/2}$ 组态强烈混合。本论文提出的理论结果已收入一篇刚发表于 Physical Review C 的论文[22]。',original=r'in the calculations. The bands are mainly based on QTR orbital $|\nu\rangle=|20\rangle$, with a projection of 7/2 on the long axis, which corresponds approximately to the $\nu g_{7/2}[404]7/2^+$ Nilsson orbital. The calculations for $^{133}\mathrm{Ce}$ were consistent with a triaxiality of $0^\circ\leq\gamma\leq15^\circ$, while for $^{131}\mathrm{Ba}$, a triaxiality of $\gamma\sim15^\circ$ was required to reproduce the observed excitation energies and energy staggering of the bands. In addition, it was found that the bands in both nuclei are strongly influenced by the Coriolis interaction which causes re-alignment of the angular momentum of the $\nu g_{7/2}$ neutron away from the long axis. Furthermore, the nearby $\nu s_{1/2}$ and $\nu d_{3/2}$ orbitals which have a significant $K=1/2$ component in their wave functions strongly mix with the dominant $\nu g_{7/2}$ configuration of the band. The theoretical results presented in this work were included in a paper that was just published in Physical Review C [22].')
add(117,13,22,r'本论文还分析了 $^{133}\mathrm{Ce}$ 数据中的符合关系，发现许多新跃迁，将其置于一条建立在 $I^\pi=13/2^-$ 态之上的新负宇称带。发现了13条新带内跃迁、15条带间跃迁和8个新能级。新能级的自旋、宇称及跃迁混合比由中国合作者确定。新带衰变到已知的 $\nu(h_{11/2})^{-1}[514]9/2^-$ 负宇称带。本论文解释了已知晕带和新的激发负宇称带。测得的这些能带跃迁混合比，排除了将它们解释为可能摆动带的方案。')
add(117,23,33,r'针对 $^{133}\mathrm{Ce}$ 的这些负宇称带进行了详细QTR模型计算，采用费米面附近9个负宇称QTR轨道。其中6个来自 $h_{11/2}$ 子壳，长轴投影从1/2到11/2。晕带主要建立在长轴单粒子投影9/2的 $h_{11/2}$ 轨道上；激发带则建立在相对晕带沿长轴多出 $2\hbar$ 转动角动量的态上。计算表明，除长轴投影9/2的 $h_{11/2}$ 轨道外，投影5/2、7/2和11/2的 $h_{11/2}$ 轨道也对两条带的态具有显著作用。这些成分的混合产生了带内观测到的较大能量交错。')
add(117,34,35,'还进行了冻结排列（FA）近似计算，将价核子的角动量牢固固定在……〔续下页〕')
add(118,1,10,'〔续上页原段〕……长轴方向。这组计算未能描述晕带和激发带中实验观测到的签名劈裂及各态激发能。研究发现，当价中子的角动量固定沿长轴排列时，原本有利于构造转动态的某些波函数成分被排除；因此FA近似预言的转动态能量高于大组态空间计算的转动态。此外，研究发现能量交错来自与其他轨道的混合，因此采用FA运行QTR计算，原则上不能产生能量交错。')
add(118,11,13,r'一篇介绍 $^{133}\mathrm{Ce}$ 中 $h_{11/2}$ 带新结果及基于本论文QTR模型计算的解释的稿件，正在准备投稿至 Physical Review C。')

blocks=[];mapped={};count=0
for s in spec:
    count+=1;bid=f'S{count:03d}'
    bb=[BY[(s['page'],i)] for i in s['source_blocks']]
    for i in s['source_blocks']:assert (s['page'],i) not in mapped;mapped[(s['page'],i)]=bid
    raw=''.join(x['text'] for x in bb)
    blocks.append(dict(id=bid,page=s['page'],type=s['type'],order=len(blocks)+1,
                       original_text=s['original_override'] or clean(raw),raw_extraction=raw,
                       translation=s['translation'],translation_status='full-bilingual',
                       source_block_indices=s['source_blocks'],bbox=union([x['bbox'] for x in bb]),
                       confidence='medium',refs=[],needs_review=True))

# Contents and figure/table lists are explicitly original-image fallback, no line translation.
images=[]
for page in range(6,12):
    subset=[b for b in RAW if b['pdf_page']==page]
    if page in [7,8,10]:subset=[b for b in subset if b['bbox'][1]>70]
    subset=[b for b in subset if b['bbox'][3]<770]
    bid=f'T{page-5:03d}';box=union([b['bbox'] for b in subset]);path=f'assets/directories/{bid}.png'
    (OUT/'assets/directories').mkdir(parents=True,exist_ok=True)
    DOC[page-1].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(box)+(-4,-4,4,4)).save(OUT/path)
    for b in subset:mapped[(page,b['block'])]=bid
    label='Contents' if page<=8 else 'List of Figures' if page<=10 else 'List of Tables'
    zh='目录（原图保留，未逐行翻译）' if page<=8 else '插图清单（原图保留，未逐项翻译）' if page<=10 else '表格清单（原图保留，未逐项翻译）'
    blocks.append(dict(id=bid,page=page,type='original-directory',order=len(blocks)+1,
                       original_text=''.join(b['text'] for b in subset),translation=None,
                       translation_status='original-image-only-authorized',source_block_indices=[b['block'] for b in subset],
                       bbox=box,image_path=path,label=label,chinese_label=zh,confidence='high',needs_review=True))
    images.append(dict(id=bid,page=page,type='directory',image_path=path,bbox=box))

# Preserve all bibliography source pages and reconstruct74 contiguous original entries.
reftext='';ranges=[]
for page in range(119,131):
    subset=[b for b in RAW if b['pdf_page']==page and b['bbox'][1]>70 and b['bbox'][3]<770]
    body=[b for b in subset if b['text'].strip()!='Bibliography']
    for b in body:
        start=len(reftext);reftext+=b['text'];ranges.append((start,len(reftext),page,b['block']))
    box=union([b['bbox'] for b in subset]);path=f'assets/references/pdf{page:03d}.png'
    (OUT/'assets/references').mkdir(parents=True,exist_ok=True)
    DOC[page-1].get_pixmap(matrix=fitz.Matrix(1.8,1.8),clip=fitz.Rect(box)+(-4,-4,4,4)).save(OUT/path)
    images.append(dict(id=f'BIBPAGE{page}',page=page,type='bibliography-page',image_path=path,bbox=box))
starts=list(re.finditer(r'^\[(\d+)\]',reftext,re.M))
assert [int(m[1]) for m in starts]==list(range(1,75))
reference_blocks=[]
for n,match in enumerate(starts):
    start=match.start();end=starts[n+1].start() if n+1<len(starts) else len(reftext)
    original=reftext[start:end];locs=[dict(page=page,block=bi) for a,z,page,bi in ranges if a<end and z>start]
    rid=f'R{n+1:03d}'
    for loc in locs:mapped[(loc['page'],loc['block'])]=rid
    entry=dict(id=rid,reference_number=n+1,type='reference-original',page=locs[0]['page'],
               pages=sorted({x['page'] for x in locs}),order=len(blocks)+n+1,
               original_text=clean(original),raw_extraction=original,translation=None,
               translation_status='original-not-translated-authorized',source_locations=locs,
               independent_verification_status='not-independently-verified-in-this-reader',
               confidence='medium',needs_review=True)
    reference_blocks.append(entry)
blocks+=reference_blocks
for img in [x for x in images if x['type']=='bibliography-page']:
    blocks.append(dict(id=img['id'],page=img['page'],type='reference-page-image',order=len(blocks)+1,
                       original_text=None,translation=None,translation_status='original-image-not-translated-authorized',
                       image_path=img['image_path'],bbox=img['bbox'],confidence='high',
                       independent_verification_status='not-independently-verified-in-this-reader'))

excluded=[];unmapped=[]
for b in RAW:
    key=(b['pdf_page'],b['block'])
    if key in mapped:continue
    if b['bbox'][3]<70 or b['bbox'][1]>770 or b['text'].strip()=='Bibliography':
        excluded.append(dict(page=b['pdf_page'],block=b['block'],text=b['text'],reason='running header/footer or bibliography section heading repeated in reader'))
    else:unmapped.append(b)
assert not unmapped,unmapped
glossary=[dict(term=a,translation=b,note=c) for a,b,c in [
 ('signature splitting','签名劈裂','S(I)单独定义，不能等同声子能量'),('energy staggering','能量交错','保留作者与signature splitting的关系'),
 ('quasiparticle-plus-triaxial rotor (QTR)','准粒子加三轴转子','模型解释而非新实验'),
 ('frozen alignment (FA)','冻结排列','本论文特定截断近似，不赋予普适排除效力'),
 ('tilted precession','倾斜进动','与作者wobbling判据分层'),('yrast band','晕带','给定自旋最低能序列'),
 ('potential energy surface (PES)','势能面','合作者模型输入')]]
mapping=dict(paper=dict(title='Triaxiality and Rotational Bands in133Ce — Front Matter and Chapter7 with original bibliography',
                       author='Ignasio Wakudyanaye',institution='University of the Western Cape',year=2022,
                       source_path=str(SRC),source_type='pdf',source_format='pdf-text',language='en'),
             blocks=blocks,pages=[dict(page=page,block_ids=[b['id'] for b in blocks if page==b['page'] or page in b.get('pages',[])]) for page in list(range(1,12))+list(range(116,131))],
             images=images,equations=[],figures=[],glossary=glossary,
             source_identity=json.loads((OUT/'source_identity.json').read_text()),
             extraction_coverage=dict(mapped_raw_blocks=len(mapped),excluded_items=excluded,unmapped=[]),
             independent_bibliography_audit=False)
(OUT/'source_map.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n')

parts=['# 133Ce学位论文：前置材料与第7章对照读本',
       '来源：用户提供的 Ignasio Wakudyanaye，University of the Western Cape，2022年3月学位论文。',
       '**范围声明：** PDF1–5（封面、声明、题记、摘要、关键词、致谢）及PDF116–118（第7章）逐段Original／中文；PDF6–11目录与图表清单保留原图；PDF119–130参考文献完整原文保留，不逐条翻译、未逐条独立验证。本文件不是130页中文全译完成声明。',
       '## 页索引','\n'.join(f'- [PDF{p}](#page{p})' for p in list(range(1,12))+list(range(116,131))),
       '## 术语表','| Original | 中文 | 边界 |\n|---|---|---|\n'+'\n'.join(f'| {g["term"]} | {g["translation"]} | {g["note"]} |' for g in glossary)]
for page in list(range(1,12))+list(range(116,119)):
    parts.append(f'<a id="page{page}"></a>\n## PDF{page}'+(f'／印刷页{page-11}' if page>=116 else ''))
    parts.append(f'[完整原页](visual-pages/pdf{page:03d}.png)')
    for b in [b for b in blocks if b['page']==page and b['type']!='reference-original']:
        parts.append(f'<a id="{b["id"]}"></a>\n**Source:** PDF{page} · {b["id"]}')
        if b['type']=='original-directory':
            parts.append(f'**Original:** {b["label"]}\n\n![{b["label"]} PDF{page}]({b["image_path"]})\n\n**中文说明：** {b["chinese_label"]}。此说明仅标识材料，不代表清单条目已翻译。')
        else:parts.append(f'**Original:** {b["original_text"]}\n\n**中文:** {b["translation"]}')
parts+=['## 参考文献完整原文（74项，未逐条独立验证）',
         '跨页条目已连续拼接；原始页图和未归一文字保存在同目录。以下只保留作者列出的参考文献，不表明它们已逐篇阅读或元数据已获验证。',
         '\n'.join(f'- [{r["id"]} · [{r["reference_number"]}]](#{r["id"]}) — PDF'+','.join(map(str,r['pages'])) for r in reference_blocks)]
for page in range(119,131):
    image=next(x for x in images if x['page']==page)
    parts.append(f'<a id="page{page}"></a>\n<a id="{image["id"]}"></a>\n### 参考文献原页 PDF{page}／p.{page-11}\n\n**Source:** PDF{page} · {image["id"]}\n\n![Bibliography original PDF{page}]({image["image_path"]})')
    for r in [r for r in reference_blocks if r['page']==page]:
        parts.append(f'<a id="{r["id"]}"></a>\n**Source:** PDF'+','.join(map(str,r['pages']))+f' · {r["id"]}\n\n**Original reference:** {r["original_text"]}\n\n**状态：** 原文保留；未逐条翻译，未在本reader逐条独立验证。')
parts.append('## 阅读与覆盖边界\n\n[translation_notes.md](translation_notes.md)区分作者结论与本任务审计；[coverage.json](coverage.json)明确哪些内容已译、哪些保持原文。没有把书目保留当成文献证据审查完成。')
(OUT/'paper.md').write_text('\n\n'.join(parts)+'\n')

coverage=dict(scope_pdf_pages=list(range(1,12))+list(range(116,131)),
              fully_bilingual_pdf_pages=[1,2,3,4,5,116,117,118],
              directories_original_image_pdf_pages=list(range(6,12)),
              bibliography_original_pdf_pages=list(range(119,131)),bibliography_entries=74,
              bibliography_translated=False,bibliography_independently_verified=False,
              bilingual_source_blocks=len(spec),chapter7_bilingual_blocks=sum(s['page']>=116 for s in spec),
              mapped_raw_blocks=len(mapped),excluded_running_items=len(excluded),unmapped_count=0,
              pending_authorized_translation_blocks=[],scope_complete=True,whole130pages_chinese_translation_complete=False,
              raw_sha_unchanged=hashlib.sha256(SRC.read_bytes()).hexdigest()==mapping['source_identity']['sha256'],
              no_canonical_git_raw_mutation=True)
(OUT/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(coverage,ensure_ascii=False,indent=2))
