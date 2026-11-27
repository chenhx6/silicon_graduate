---
type: source
title: Crider等2016：68,70Ni寿命与分支比测定及形状共存两态混合模型分析
aliases: [Crider 2016 68Ni shape coexistence, Crider 2016 PLB, 10.1016/j.physletb.2016.10.020]
created: 2026-11-08
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: Shape coexistence from lifetime and branching-ratio measurements in 68,70Ni
authors: [B. P. Crider, C. J. Prokop, S. N. Liddick, M. Al-Shudifat, A. D. Ayangeakaa, M. P. Carpenter, J. J. Carroll, J. Chen, C. J. Chiara, H. M. David, A. C. Dombos, S. Go, R. Grzywacz, J. Harker, R. V. F. Janssens, N. Larson, T. Lauritsen, R. Lewis, S. J. Quinn, F. Recchia, A. Spyrou, S. Suchyta, W. B. Walters, S. Zhu]
journal: Physics Letters B
year: 2016
volume: 763
pages: 108-113
doi: 10.1016/j.physletb.2016.10.020
arxiv: null
language: en
canonical_source: https://doi.org/10.1016/j.physletb.2016.10.020
zotero_item_key: null
citation_key: ''
zotero_uri: null
library_file: null
raw_file: raw/papers/gpt/query/20261108-foundations-G26/crider-2016-68ni-shape-coexistence.pdf
raw_sha256: 923ce537b505cecd49cdf75901bdd1be76896da0326ce29e8b049f10143d4b28
nuclei: [68Ni, 70Ni]
reactions: ['9Be(76Ge, X) fragmentation at 130 MeV/u', 68Fe(beta-)68Co(beta-)68Ni, 70Co(beta-)70Ni]
experiments: [NSCL-A1900-SeGA-LaBr3]
models: [LNPS-SM, MCSM-A3DA, two-level-mixing-model]
observables: [t1/2, branching-ratio, B(E2), rho2(E0), delta-r2, Q0]
methods: [electronic-fast-timing, beta-gamma-coincidence, GeDSSD-implantation]
tags: [shape-coexistence, a60, 68ni, e0-transition, e2-transition, two-state-mixing, doctoral-foundations]
archive_required: true
---

# Crider2016：先区分新测、采用量与两态模型

## Bibliographic Record

B. P. Crider等，*Shape coexistence from lifetime and branching-ratio measurements in 68,70Ni*，
PLB763,108–113(2016)，DOI `10.1016/j.physletb.2016.10.020`。
底本为六物理页出版PDF，原件路径/哈希见frontmatter。

## Scope and Reading Depth

G26读取主文；总控本轮独立核PDF2–5/printed109–112，尤其Table1、Fig1–3与两态分析。
已读实验链、寿命/分支、条件形状抽取与理论比较；没有事件级数据、完整Cov或作者计算代码。
参考文献所引Suchyta等并未因此全部重新原读；其量标为本文采用。

## Summary

新测68Ni的0₃半衰期与弱430keV分支，将绝对EM信息补入构型混合问题。
作者在限定两态模型中求混合度，再结合采用的E0强度求半径差与轴向内禀Q。
这条推断链不能压缩成“直接测到0⁺椭球”。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CR16-1 | 68Ni0₃的t₁/₂=0.57(5)ns；70Ni候选(0₂)的t₁/₂=1.65⁺⁰·³⁰₋₀·₂₅ns | reported-experiment | direct-original | PDF2、PDF4 Table1 | false |
| CR16-2 | 430keV的2₁→0₂分支为0.12(3)%；结合采用的2₁半衰期0.31(5)ps得到B=147(46)e²fm⁴，向0₁为52.5(84) | experiment-with-adopted-input | direct-original | PDF2末、PDF4 Table1及脚注b | false |
| CR16-3 | 0₂能量1604keV，0₃为2511keV；其球/扁/长形状与组态联系来自模型比较 | state-identity-and-model-attribution | direct-original | PDF2首、PDF4 Fig3及模型段 | false |
| CR16-4 | 两态模型给cos²θ=0.74(7)；采用ρ²=0.0076(4)后得半径差0.17(2)fm²；轴向等附加假设下\|Q₀\|=93(5)efm² | conditional-model-extraction | direct-original | PDF3/printed110右栏 | false |
| CR16-5 | 原文所引A3DA/LNPS对68Ni0₃半衰期预测108ns/1.5ns，与0.57(5)ns不同 | cited-model-comparison | direct-original-comparison | PDF4/printed111 | false |

寿命实验用像素快塑闪及LaBr3/SeGA，弱分支实验另用GeDSSD和SeGA。
两次实验的共同采用量仍须保留依赖；0₃→0₁/0₂的E0为上限，不是零值。

## Competing Interpretations and Limitations

两态抽取忽略更高态与未混合交叉矩阵元；单体E0算符在任意构型基底并非自动对角。
内禀Q绝对值不能决定形变正负，0⁺的实验室Qs恒零。
能量或一个强度的符合不能消除模型对其它寿命的偏差；原文模型比较只代表其2016范围。
“基态球形”是内禀表示/模型语言，不自动意味着无四极关联或无量子涨落。

## Extracted Pages

持久推理与迁移问题见[[doctoral-r1-g26-a60-collectivity-20261108]]。
本页不把该实验当高自旋60Ni或其它核芯的直接测量。

## Agent Self-audit Triage

P0：原件身份/哈希已核；旧稿1770keV与混合实验装置等误写已纠正。
P1：未重读采用量的全部原始来源、没有完整Cov/事件重放；两态和轴向映射为条件模型。
没有发生用户逐项审核，不以历史review标签赋予事实资格。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"pages": "1–2", "sections": ["刊页108–109", "出版信息、引言、已知能级、快定时实验及独立弱分支实验"]}
- {"pages": "3–4", "sections": ["刊页110–111", "第3页图1–2、E0上限、两态混合与电荷半径关系式，第4页表1、图3和壳模型比较"]}
- {"pages": "5–6", "sections": ["刊页112–113", "结论、致谢、参考文献[1]–[50]"]}
- 本次获取的具体覆盖：通读 PDF 物理第1–6页的分页面文本，包括实验、图1–3图注、表1、两态模型、理论比较、结论和书目。建议接受对照笔记中可逐项回链的同版 PDF 第2–5页核心正文覆盖。第1及第6页的覆盖来自本次文本审计。图1–3及表1仍待版面目视核查。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | 快定时实验通过478 keV与307 keV γ线门分别得到⁶⁸Ni 0₃⁺的半衰期0.57(5) ns和⁷⁰Ni候选(0₂⁺)的半衰期1.65⁺⁰·³⁰₋₀·₂₅ ns。⁷⁰Ni的括号指认应保留。 | 实验测量 | source-reported | PDF 第2页快定时正文，第3页图1(c,d)，第4页表1。第3页时间谱门和本底曲线待核原图。 | true |
| A20-2 | 独立的弱分支实验首次报告⁶⁸Ni 430 keV的2₁⁺→0₂⁺分支为0.12(3)%。结合采用的2₁⁺半衰期0.31(5) ps，得到该支路B(E2)=147(46) e²fm⁴，通向0₁⁺的B(E2)=52.5(84) e²fm⁴。 | 实验测量结合文献采用量 | source-reported | PDF 第2页末，第3页图2(a,b)，第4页表1及脚注b。430 keV窗口和2033 keV归一化线待核第3页原图。 | true |
| A20-3 | 在仅保留⁶⁸Ni两个最低0⁺态显著混合的模型中，E2强度比给出cos²θ=0.74(7)。输入[10]的ρ²(E0)=0.0076(4)后，得到均方电荷半径差的量值0.17(2) fm²。进一步假设0₁⁺球形和轴对称形变，得到0₂⁺的&#124;Q₀&#124;=93(5) efm²。 | 条件模型推断 | source-reported | PDF 第3页右栏两条未编号关系式，第4页表1、图3。关系式的平方、下标和括号待核第3页版面。 | true |
| A20-4 | 作者援引的A3DA与LNPS计算对⁶⁸Ni 0₃⁺半衰期分别给出108 ns和1.5 ns，与实测0.57(5) ns存在不同程度的偏差。球形、扁形和长形的构型关联来自模型比较。 | 引用模型与实验比较 | source-reported | PDF 第2页低位能级讨论，第4页图3与模型比较正文，第6页参考文献[39]。能级图和模型标值待核第4页原图。 | true |

两次NSCL实验均以130 MeV/u的⁷⁶Ge束打⁹Be，经A1900分离。快定时采用像素快塑闪植入探测器、LaBr₃(Ce)和SeGA。弱分支使用另一套GeDSSD植入与SeGA测量，以2033 keV基态线归一。表1脚注a、b分别把采用量追溯至[10]和[35]。

- Wiki 的CR16-1和CR16-2应分别补入PDF 第3页图1(c,d)和图2(a,b)。第2页是对应实验正文，第4页表1保留数值与采用量脚注。将依赖图表的核查状态标为待目视。
- 旧稿的1770 keV误写不得回填。PDF 第2页给出⁶⁸Ni 0₂⁺为1604 keV、0₃⁺为2511 keV，比较弱分支所用的2033 keV线是2₁⁺→0₁⁺。继续分开记录快定时和弱分支的探测配置。
- PDF 第5页总结抽取有一处把新得强度写成电偶极。Wiki应依第2–4页正文、图注与表1记为电四极E2强度，并保留E0上限的区分。
- PDF 第3页的混合比关系式将平方与正文拆行，E0关系式的半径下标和括号也有抽取损坏。PDF 第4页表1的⁶⁸Ni 2₁⁺→0₁⁺分支负向误差排印待查。核对前沿用可从正文与表值确认的派生结果，暂缓逐字录入这些公式和误差。
