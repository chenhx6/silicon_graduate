---
type: source
title: "Novel Penning-trap techniques reveal isomeric states in 128In and 130In for the first time"
aliases: [Nesterenko2020, Nesterenko 2020 PLB, 128In 130In isomers]
created: 2026-11-07
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Novel Penning-trap techniques reveal isomeric states in 128In and 130In for the first time"
authors: [D. A. Nesterenko, A. Kankainen, J. Kostensalo, C. R. Nobs, A. M. Bruce, O. Beliuskina, L. Canete, T. Eronen, E. R. Gamba, S. Geldhof, R. de Groote, A. Jokinen, J. Kurpeta, I. D. Moore, L. Morrison, Zs. Podolyák, I. Pohjalainen, S. Rinta-Antila, A. de Roubin, M. Rudigier, J. Suhonen, M. Vilén, V. Virtanen, J. Äystö]
journal: "Physics Letters B"
year: 2020
volume: 808
pages: 135642
doi: "10.1016/j.physletb.2020.135642"
language: en
canonical_source: "doi:10.1016/j.physletb.2020.135642"
citation_key:
raw_file: "raw/papers/gpt/query/20261107-campaign-G09/Nesterenko_2020_PLB_808_135642_128In_130In_isomers.pdf"
raw_sha256: cc0999c3ef1facb24725ca119e0852c2d1b94df4100fe0c847f20ffec1b31022
archive_required: true
nuclei: [128in, 130in, 128sn, 130sn, 132sn]
reactions: [proton-induced-fission]
experiments: [jyu-igisol-jyfltrap, penning-trap-pi-icr, post-trap-decay-spectroscopy]
models: [shell-model, cd-bonn-g-matrix, nushellx]
observables: [excitation-energy, mass-excess, isomer-splitting, beta-delayed-gamma]
methods: [phase-imaging-ion-cyclotron-resonance, time-of-flight-icr, trap-assisted-decay-spectroscopy]
tags: [penning-trap, pi-icr, isomeric-states, indium-isotopes, tin-isotopes, spin-trap, shell-model-interaction]
---

# Nesterenko2020：128/130In异能态的质量与结构约束

## Bibliographic Record

D. A. Nesterenko et al., PLB808,135642(2020)，DOI10.1016/j.physletb.2020.135642。
实际本地arXiv:2005.09398v1，8物理页，题名/版本/哈希见元数据。

## Scope and Reading Depth

### Covered scope

Worker通读8页；总控回查摘要、质量/态标识和理论解释。
JYFLTRAP分离/质量与阱后衰变关联，模型解释另列。

### Not covered

未恢复频率/相位原始数据、完整误差Cov、壳模型波函数或全部β强度。
该文不独立提取全核区有效gA。

## Key Results

| ID | 原文内容 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NE20-1 | JYFLTRAP分离并测六个β衰变态的质量，结合阱后衰变识别 | experimental-fact | direct | PDF1摘要、Table1及实验段 | false |
| NE20-2 | 128In在1797.6(20)keV的新高自旋β异能态，馈送128Sn的15−异能态；壳模型建议16+ spin trap | experimental-fact + model-interpretation | direct | PDF1摘要、Table1与讨论 | false |
| NE20-3 | 130In低(10−)异能态在58.6(82)keV，由PI-ICR分辨；相对于1−的能差比该壳模型预测低约200keV | experimental-fact + model-comparison | direct | PDF1摘要、Table1/Fig4 | false |

## Summary

精确的母态/异能态能量能限制残余相互作用与β相空间输入。
16+是模型建议，不把质量峰或衰变关联说成独立直接自旋测量。

## Competing Interpretations and Limitations

强度或寿命差不能由质量差唯一解释，仍需电弱算符与组态。
高多极E6/M9等在相应选择规则下可能允许，不能称“非物理跃迁”；
低能高多极性可使γ慢，但没有完整开放宽度时不凭定则宣称100%β。
有效CD-Bonn G矩阵模型不是裸相互作用直接预测，也不由一个劈裂确定全部TBME。

## Knowledge Impact and Learning Decision

`supports + focused comparison`：[[campaign-g09-shell-weak-isomer-20261107]]。
与129Cd的β谱学是独立装置/观测，但不是同一核素的重复GT测量。

## Agent Self-audit Triage

P0: none identified in original identity/hash。
P1：暂定自旋、模型spin-trap解释、能量与率的区别、允许但极慢的高多极γ保持分层。

## Extracted Pages

8页作者v1；非作者原数据或生产计算重放。

## 2026-11-27 — 馆藏原件与覆盖核对

- PDF 第 1–2 页，题名、版本、引言、IGISOL/JYFLTRAP 实验装置、Ramsey 纯化与 TOF-ICR，含第 2 页图 1。
- PDF 第 3–5 页，PI-ICR 态分辨、阱后 β 门控 γ 谱、质量表、衰变归属、壳模型和主要结论，含第 3 页图 2、第 4 页表 1、表 2 与图 3，以及第 5 页图 4。
- PDF 第 6–8 页，结论末段、致谢、参考文献 [1]–[51]，含第 6 页图 5 的图注和第 7 页图 6 的能级文字与图注。
- 本次获取的具体覆盖：逐页核读第 1–8 页所给正文、两张表、六幅图的图注与可提取图中文字，以及致谢和参考文献。建议接受既有同版全文文字覆盖，修正结果定位和证据层级后，由管理者核验所列关键图表。本次未作视觉核验。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A19-1 | 表 1 给出 ¹²⁸In 和 ¹³⁰In 各三个 β 衰变态的质量结果。¹²⁸In 两个异能态的激发能为 285.1(25) 和 1797.6(20) keV。PI-ICR 分辨了 ¹³⁰In 三个态，给出暂定 (10⁻) 态相对 1(−) 基态的能差 58.6(82) keV。TOF-ICR 对低能双态未实现分辨，表 1 对该劈裂推荐 PI-ICR 值。 | 实验测量 | source-reported | PDF 第 2 页回旋频率无编号公式与图 1(b)，第 3 页分辨及混态说明，第 4 页表 1 和脚注 c。图 1(b) 的峰区和态标记待核第 2 页。 | true |
| A19-2 | 选纯 ¹²⁸In m2 后的 β 门控 γ 谱报告了 119.5(3)、207.5(3) 和 1779.1(3) keV 等 γ 线。前两条对应已知 ¹²⁸Sn 的 15⁻→13⁻→11⁻ 级联，1779.1 keV 线的相对总强度为 85(8)，以 119.5 keV 线归一。图 3 图注明示 79 keV 线未检出。 | 实验观察 | source-reported | PDF 第 3 页谱段与图 2，第 4 页表 2、内转换修正式及图 3 图注。 | true |
| A19-3 | 作者根据级联及强度判断新 ¹²⁸In 态的 β 衰变布居 ¹²⁸Sn 的 15⁻ 异能态，并提出 1779.1 keV 线由约 5878 keV 的候选 (15⁺) 能级馈入 15⁻。该路径属于作者的衰变纲图归属。 | 作者解释 | source-reported | PDF 第 3 页谱学讨论，第 4 页表 2 与图 3 左侧，第 5 页关于 1779 keV 归属的讨论。候选能级、箭头及括号待核第 4 页图 3。 | true |
| A19-4 | NuShellX@MSU 的 jj45pna 计算支持将新的 ¹²⁸In 态暂定为 (16⁺) 自旋陷阱。该计算把 ¹²⁸In 第一异能态预测为 452 keV 的 10⁻ 态，实验条目为 285.1(25) keV、暂定 (8⁻)。计算将 ¹³⁰In 的 10⁻ 态置于 264 keV，比测得的 58.6(82) keV 高约 205 keV。 | 模型结果及实验比较 | source-reported | PDF 第 3 页模型空间及有效相互作用段，第 4–5 页模型讨论，第 5 页图 4、第 6 页图 5 图注、第 7 页图 6。所列数值取自正文或表 1，第 5 页图 4 的逐级标签须按原图核对。 | true |

质量结果依赖参考离子频率比、阱纯化和时间分析。阱后衰变归属结合选纯样本及已知 ¹²⁸Sn 级联。结构解释依赖 jj45pna 价空间计算，该有效相互作用采用经微扰 G 矩阵重整化的 CD-Bonn 势。PDF 第 7 页参考文献 [7] 引用另一队列项 catalogue:LIT-000980，那里研究的是 ¹²⁹Cd β 衰变。

- NE20-1 的核心定位改为 PDF 第 2–3 页实验段和第 4 页表 1。注明 ¹³⁰In m1 的 TOF-ICR 结果带基态混入，推荐值来自 PI-ICR。
- NE20-2 分列质量测得的激发能、γ 级联支持的 15⁻ 布居、1779.1 keV 路径的作者归属，以及暂定 (16⁺) 的模型解释。分别定位到 PDF 第 3–4 页谱及两表、第 4–5 页衰变讨论和第 5 页图 4。
- NE20-3 把 ¹³⁰In 的 Fig. 4 改为 PDF 第 7 页 Fig. 6。实验数值定位至第 4 页表 1，态分辨定位至第 2 页图 1(b) 与第 3 页正文。图像相关证据保留待核标记。
- 书目中的 135642 按期刊文章号记录，本地页数单列为 8，并保留 arXiv v1 版本标识。
