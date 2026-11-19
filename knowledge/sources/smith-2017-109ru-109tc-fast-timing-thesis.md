---
type: source
title: "Smith 2017 - Fast timing and triaxiality in 109Ru and 109Tc"
aliases: ["Mallory K. Smith doctoral thesis 2017", "109Ru 109Tc fast timing thesis"]
created: 2026-11-20
updated: 2026-11-20
status: ai-draft
review_status: unreviewed
source_type: doctoral-thesis-experiment
reading_depth: read
title_original: "Chasing Triaxiality: Probing Structure in the A ~ 110 Region via Lifetime Measurements of 109Ru and 109Tc with Fast Timing"
authors: ["Mallory K. Smith"]
year: 2017
institution: "University of Notre Dame"
doi: "10.7274/v979v121d86"
url: "https://doi.org/10.7274/v979v121d86"
canonical_source: "Notre Dame PhD thesis, title January 2017, CurateND Version 1"
raw_file: "raw/theses/gpt/query/20261119-international-nuclear-structure/SmithMK012017D.pdf"
raw_sha256: "fa8bc8fa2d6d2056fb62e7b154e204a3d6f59d45c5d8abaac5252eef7a9119a5"
raw_storage_status: archived-local
archive_required: true
nuclei: ["109Ru", "109Tc", "109Pd"]
tags: ["fast-timing", "ATD", "LaBr3", "triaxiality", "CQPC", "thesis"]
---

# Smith 2017：109Ru、109Tc快定时与三轴解释的边界

## Bibliographic Record

作者Mallory K. Smith，导师Ani Aprahamian，Notre Dame物理学博士论文。
题名页January2017，CurateND自身登记2017-01-31与上述DOI（PDF1-2）；
不把仓储日当答辩日，也不与John/J. F. Smith的其它论文合并。

## Scope and Reading Depth

- Covered scope：十个Gemini主单元实际覆盖193个PDF页，PDF18=printed1，以后PDF-17。
  九处章节/附录实际标题经守卫核对，原件SHA匹配。
- EXP-3/4因管理层把通用斜率/质心法细节也分给了止于PDF63的任务而partial。
  不是补发其所猜的64-75便自动闭环：PDF64已是Chapter4结果；本轮结合实际能级案例、
  AppendixA及定向问题核查，未给出的通用PRF/严格分界继续保持未定，不伪造推导。
- 两个定向单元返回六项答复与可复用短段，管理层核原页后编辑合入。
  INTERPRET自报complete却列PDF160/162未读，记录为有范围限制；这两张能级图的主读覆盖仍在，
  不把定向请求所有输入页计作已核。源笔记不认证全部曲线或每个模型矩阵元。
- FRAME曾把书目printed171写成PDF171；已核实际供给的PDF188/ref66并从缓存修定位，
  原响应/旧结果保留，无新API调用。worker的complete不是独立科学证据。
- Not covered：未重跑ATD拟合、CQPC或作者级联模拟，未核原始事件/硬件卡，
  未逐篇核所有引用/ICC原测量。仅作half-life/mean-life、详细平衡和理想波形代数，无PDM。

## Summary

本论文用IGISOL的A109同量异位素beta衰变链研究低能级，利用塑料beta探测器、
LaBr3快定时与HPGe选能构建三重符合；重点扩展109Ru方案并提供Ru/Tc时间信息。
寿命到强度仍依赖多极性、分支及ICC，不能因测得时间就得出唯一刚性三轴形状。
CQPC的QTR/QTD比较与gamma角属于有输入/拟合条件的模型解释，非直接形状测量。

## Key Results

| ID | claim_kind | evidence_level | locator | statement / boundary |
| --- | --- | --- | --- | --- |
| SM17-1 | experiment / calibration | direct-original-pages | PDF54-60 | beta-LaBr3时间由HPGe能量门选择；实际CFD仍需beta与gamma事件类走时校准。 |
| SM17-2 | analysis / adopted-limit | direct-original-pages | PDF69,79-82 | Ru185.1keV拟合63(5)ps最终按作者规则报<73ps；不作为普通精确点。 |
| SM17-3 | convention / evidence-boundary | direct-original-pages | PDF123-130 | Tc表题/列头/图注及级联lambda定义不统一；保留原报口径，误差仅统计。 |
| SM17-4 | adopted-input / interpretation | direct-original-pages | PDF69,77-80,184 | 69.1keV的多极假设、185.1keV采用的delta及ICC壳层口径不同，不冒认P测量。 |
| SM17-5 | model-input / author-interpretation | direct-original-pages | PDF154-159 | QTR核芯2+能可调，QTD采用实测；gamma20/19.3度不是独立实测形状刚性。 |
| SM17-6 | normalization-boundary | direct-original-pages | PDF158,161,163 | M1单位、QTC列名、opp及跨表数值映射有待澄清，不据此发布统一绝对强度表。 |

## Experiment and Method

### 门、校准与时间谱

原件PDF54将beta-HPGe-LaBr事件的记录触发窗写为50us，而PDF58要求LaBr3 Stop落在Start后50ns内；它们可能属于不同记录/快TAC阶段，但仅凭本原件不能认证全部硬件时序，也不将两值静默合并或断言必为同一笔误。LaBr3定时校准在本实验的400keV以下显示Compton事件与全能峰有不同走时（PDF59-60）；beta通道另按能区投影质心校正。实际安装CFD不等于不需要walk校准。能量门、本底与反符合过扣除也会影响所选时间谱（PDF63），不能由一个门宽直接推导普适寿命上限。

这里是beta-start ATD与HPGe门分析，不因同用LaBr3就自动等同gamma-gamma广义质心差法。
原件的不同时间窗必须按所在记录/电子学层次使用，不能擅自合成一个“50ns或50us已核全局门”。

### 半衰期、限值与级联

原件Tc Table4.25题为Half-life但列头为Lifetime（PDF124），图中又标T1/2；PDF127模拟级联时直接写lambda=1/136ps和1/155ps。若同一数值既作T1/2又作meanlife，便有ln2口径歧义；本轮无作者拟合代码，不能裁决实际拟合器约定或静默转换所有报值。Table4.25明确误差仅含统计误差。不同图/表/门谱还给出不同数值与误差：不能把单门、加权结果和方案图数值自动当作多个独立测量（PDF123-130）。Ru185.1keV正文拟合63(5)ps，但最终采用作者定义的2sigma上限<73ps（PDF69、79），不改写成普通对称误差点。

一般关系为T1/2=ln(2)*tau、lambda=ln(2)/T1/2=1/tau。
仅作示例：数值136ps若为半衰期，则meanlife约196.2ps；若为meanlife，半衰期约94.3ps。
这是定义检查，不裁决论文拟合器实际约定，不重新估算Tc的B值。

109Pd的既有ATD寿命结果由Bucher分析并在前人论文发表，本论文引用作比较，不是新测一套109Pd数据（PDF64）。Ru Table4.1明确列为T1/2：137.83keV为1144(70)ps、185.0keV为<73ps、197.41keV为684(31)ps、255.57keV为276(19)ps、332.20keV为68(21)ps、405.42keV为<86ps（PDF69-71）。Tc的333.1keV正文加权136(16)ps、423.8keV表值<=92(24)ps、745.0keV表值155(18)ps，须保留表头/图注定义和统计误差限定（PDF124-130）；原文说其自旋多极性未测，不能直接导出确定B值。

| Tc能级keV | 方案图4.26（PDF123） | 表4.25/正文（PDF124） | 单门图示/其它方法 | 使用边界 |
| --- | --- | --- | --- | --- |
| 333.1 | 150(40)ps | 三门141(36)、127(25)、138(17)ps；正文平均136(16)ps | Fig4.28标T1/2=140(16)ps | 不同门/汇总/图版本不作为独立重复观测。 |
| 423.8 | 79(8)ps | <=92(24)ps | Fig4.29标96(6)ps；质心法40(57)ps限值 | 保留限值与定义歧义，不平均成精确点。 |
| 745.0 | 143(36)ps | 155(18)ps | Fig4.32标T1/2=155(7)ps | 正文认为直接beta馈入而采纳数值，但误差/口径并不全相同。 |

图/表数值差异不自动等于多个相互矛盾的实验：单门与加权结果、后稿更新等可能不同，
本轮未取得版本/拟合记录以裁决。Ru的255keV表4.1为276(19)ps，附近正文又写267(19)ps，
同样不静默替换。不能将“没看见更高馈入”普遍等同严格证明没有feeding。

## Multipolarity, ICC and Model Comparison

### 实验输入与采用值

69.1keV的M1/E2与Table4.1两组B值是缺少实测ICC时的不同多极假设，不是已测得的两个混合分量或确定的大E2成分（PDF69、77-78）。185.1keV的delta=-0.25(6)采用此前角关联Ref82，不是本次P联合拟合（PDF79）。原件正文PDF77称Penttila把137.9keV定为E1，但附表B.3将该文列为M1（PDF184）；本轮未核其外部原件，不选一处覆盖另一处。正文有alpha_K标注，附表口径未全统一，不能默认全部是alpha_total。暂定宇称与未观测支路也不能升级为确定性判据。

本实验没有P参与的混合比联合求解。69.1keV在纯E2假设下很大的1013(194)Wu，
不能作为已测得大E2混合分量的证据。多数高能态仍有暂定自旋/未定多极性，
缺的量不填零、未见的线不直接判为不存在。

### CQPC：拟合与检验分开

论文在Section 5.3中对比了基于准粒子-三轴转子（QTR）与准粒子-Davidson势（QTD）的CQPC模型计算（PDF 154-159）。Table 5.3列出109Pd参数引自Li 2016（Ref. [9]），109Ru低能区参数引自其未发表私信（Ref. [125]）。QTD采用偶偶核采用的实验2+1能量，而QTR将核芯2+1能量作为自由可调参量以匹配奇A核低能级（PDF 156）。虽然作者以QTR较好复现基态自旋及部分跃迁为由倾向刚性三轴（γ=20°与19.3°），但文献系统学对该区γ软性结论存在显著分歧，须区分不同的拟合自由度与检验量，不能把拟合gamma视为形状刚性的直接测量。

Table5.4的B(M1)表头写e2fm4，不能当作已核磁偶极单位；Table5.5模型列写QTC，正文为QTD（PDF161、163）。Table4.1的Wu与这些表数值的映射尚未厘清，不任造统一转换因子。正文标opp为反向矩阵元（PDF158），核对正向B时必须考虑初态统计权重；缺实现说明时，不认证作者已换算或肯定未换算。若假定同一行采用共同归一，68.8/69.1keV等行仍并非所有模型都符合，不能以作者总体评价掩掉非吻合行。附录A EqA.7只写Jf=lambda+Ji，不是完整的三角条件，不能原样用作一般选择律（PDF171）。

例如Table5.5按所列共同归一读，68.8keV一行为实验0.092(42)、QTR 0.000001、QTD 0.0003；
69.1keV一行为17.7(34)、0.542090、0.0003(opp)。在单位/归一/方向未厘清前，
不将这些数值发布成已核物理单位的新B表；但作者“总体更好”的评价不能替代逐行符合度。

同一厄米电磁算符、同一约定下，B(Ji->Jf)=[(2Jf+1)/(2Ji+1)]*B(Jf->Ji)。
3/2到1/2的系数为1/2；此关系不证明作者是否已在opp列内完成转换。
EqA.7只给单侧等号，而一般必要条件为|Ji-Jf|<=lambda<=Ji+Jf；
如1/2到1/2的lambda1满足三角条件却不满足那个等号。宇称和实际矩阵元仍须另查。

## Competing Interpretations and Limitations

- 旋称劈裂、gamma交错、低gamma带与模型能谱可有不同解释；本论文汇总的IBA/TRS软度结果，
  不可与QTR拟合gamma简单按篇数投票，引用同数据不构成独立增强（PDF146-153）。
- [[li-2016-algebraic-collective-core-quasiparticle-thesis]]及Bucher论文是采用的模型/实验谱系，
  不是此学位论文新增一套109Pd实验；Ru参数来源也须按论文的私信/模型引用记载。
- Tc自旋、多极性未实测，不能从时间参数直接导出有确定电磁性质的B值。
  仅统计误差不覆盖所有walk、背景、feeding和时间零点系统效应。
- 不能以原件中的单位或一般选择律排印为已验证程序规范；未运行作者代码，
  不据源码缺失或内部差异断言其实现必然正确/错误。

## Extracted Pages

- PDF1-2、18、22、47、64、132、164、169、176、185：自身身份及实际章节/页码边界。
- PDF54-60、63：探测、触发、CFD、beta/LaBr3走时与本底处理。
- PDF69-80、94、98：Ru半衰期/限值、暂定指认、文献多极假设与表/正文差异。
- PDF123-130：Tc方案、表、门谱图、统计误差与级联lambda口径。
- PDF154-163：CQPC输入、核芯能量处理、相关参数、模型/实验表与单位边界。
- PDF171-175、184、188：通用强度/寿命条件、ICC对照及FRAME书目定位修正。

## Knowledge Impact and Open Questions

- [[constant-fraction-discriminator-and-fast-timing-walk-elimination]]：理想振幅抵消不等于实测零walk，
  不将固定fraction/delay作为经本论文验证的通用协议。另做自相似波形的小型代数检查，非硬件模拟。
- 正式复用需要追溯拟合器半衰期/meanlife约定、跨表B归一和ICC原件壳层口径，
  以及门谱之间共享系统量；不能凭“新测/更精确”自动覆盖另一表或文献。
- 本轮不跑PDM，不将这些无P的快定时结果冒充P联合delta数据，也不据此裁决领域通常如何固定sigma/I。
