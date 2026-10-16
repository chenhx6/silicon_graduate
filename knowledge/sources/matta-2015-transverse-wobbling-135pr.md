---
type: source
title: "Transverse wobbling in 135Pr"
aliases: [Matta 2015 135Pr, transverse wobbling in 135Pr]
created: 2026-07-03
updated: 2026-10-17
status: active
review_status: human-reviewed
source_type: journal-article-experiment-and-model
reading_depth: deep-read
title_original: "Transverse Wobbling in 135Pr"
authors: [J. T. Matta, U. Garg, W. Li, S. Frauendorf, A. D. Ayangeakaa, et al.]
journal: Physical Review Letters
year: 2015
volume: 114
pages: 082501
doi: 10.1103/PhysRevLett.114.082501
arxiv:
language: en
canonical_source: doi:10.1103/PhysRevLett.114.082501
zotero_item_key:
citation_key: matta_2015_TransverseWobbling
zotero_uri:
library_file:
raw_file: "raw/papers/2015_Matta et al_Transverse Wobbling in Pr 135.pdf"
raw_sha256: 8DB644705DCCFD58016753B759D19314A65284C48EFC1758F95F1B3CE23551D6
nuclei: [135pr]
reactions: [123sb-o16-4n-135pr]
experiments: [atlas-gammasphere-135pr-o16-80mev, tifr-inga-135pr-o16-80mev]
models: [tilted-axis-cranking, triaxial-particle-rotor-model]
observables: [multipole-mixing-ratio, interband-e2-strengths, wobbling-energy]
methods: [gamma-gamma-coincidence, dco-ratio, linear-polarization-asymmetry]
tags: [a130, 135pr, transverse-wobbling, gammasphere, inga, tac, qtr]
---

# Matta 等（2015）：`135Pr` 横向摇摆支持方实验

## Bibliographic Record

J. T. Matta et al., *Physical Review Letters* **114**, 082501 (2015)，DOI `10.1103/PhysRevLett.114.082501`。题名、作者年份和 DOI 与只读 BibTeX 条目唯一匹配，使用用户指定 citation key `matta_2015_TransverseWobbling`。

## Scope and Reading Depth

全文精读，并视觉核对 Fig.1 的部分能级纲图、Fig.2 的角分布、Fig.3 的线偏振不对称、Table I 的 mixing ratio/E2 fraction/跃迁概率比、Fig.4 的 TAC 比较和 Fig.5 的 QTR 及 wobbling-energy 比较。

本页按 `experiment-ingest + project-ingest` 建立 Matta 2015 对 `135Pr` transverse-wobbling 解释的支持方证据链。它不裁决后来对低自旋带 wobbling 性质的争议。

## Summary

作者用 ATLAS/Gammasphere 和 TIFR-BARC/INGA 的互补数据扩展 `135Pr` 能级结构。论文把 yrast E2 带指认为 zero-phonon band，把一条侧带指认为 one-phonon wobbling band；角分布提取的大 mixing ratio 和 INGA 偏振被作者用于支持两带间 ΔI=1 跃迁以 E2 为主，计算得到的 wobbling energy 随自旋先下降。作者据此解释为 low-deformation transverse wobbling，并用 TAC 与修改的 QTR 模型比较能级、组态和带间跃迁。

## Experimental or Theoretical Setup

- 反应：80 MeV `123Sb(16O,4n)135Pr`；
- [[atlas-gammasphere-135pr-o16-80mev]]：`3.7×10^9` 个三重及以上 γ 符合事件，用于高统计符合与角分布；
- [[tifr-inga-135pr-o16-80mev]]：`4.5×10^8` 个二重及以上 γ 符合事件，用于 clover 偏振分析；
- 新能级自旋宇称依据 DCO、角分布、偏振和 crossover 跃迁综合赋值；
- TAC：计算 1qp yrast、3qp dipole 和 5qp high-spin yrast 组态；
- QTR：以角动量相关的三个转动惯量拟合 zero-/one-phonon 与 signature-partner 能量和跃迁比。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| M15-1 | 两次实验均用 80 MeV `123Sb(16O,4n)135Pr`：Gammasphere 收集 `3.7×10^9` 个 fold≥3 事件，INGA 收集 `4.5×10^8` 个 fold≥2 事件。 | experimental-fact | direct | p.2, right column, experimental setup | false |
| M15-2 | Fig.1 展示四组结构：yrast E2 带、一条通过 ΔI=1 跃迁连接 yrast 的侧带、在该侧带之上建立的强 M1 dipole band，以及一条较弱的 signature-partner band。 | experimental-fact | direct | pp.2-3, Fig.1 and surrounding text | false |
| M15-3 | 作者把 yrast 带和侧带分别指认为 `n_w=0` zero-phonon 与 `n_w=1` one-phonon wobbling bands。 | author-interpretation | direct | pp.2-3, Fig.1; paragraph below Fig.2 | false |
| M15-4 | Table I 报告三条 `n_w=1→0` 连接跃迁：747.0、812.8、754.6 keV 的 `δ` 分别为 `-1.24(13)`、`-1.54(9)`、`-2.38(37)`，对应 E2 fractions `60.6(51)%`、`70.3(24)%`、`85.0(40)%`。 | experimental-fact | direct | pp.3-4, Fig.2, Table I | false |
| M15-5 | 747.0 与 812.8 keV 连接跃迁的偏振不对称分别为 `0.047(12)`、`0.054(34)`；作者据正值将其判为主要电性质。 | experimental-fact | direct | pp.3-4, Fig.3, Table I | false |
| M15-6 | signature-partner 到 yrast 的 593.9 keV `13/2-→11/2-` 跃迁给出 `δ=-0.16(4)`、偏振不对称 `-0.092(23)` 和 E2 fraction `2.5(12)%`，被作者用作主要 M1 的对照。 | experimental-fact | direct | pp.3-4, Figs.2-3, Table I | false |
| M15-7 | 702.7 keV `17/2-→15/2-` signature-partner 连接跃迁因过弱而未给出完整角分布或偏振；正文称其 DCO ratio 支持 pure-dipole assignment，但未在本文列出该比值。 | experimental-fact | direct | p.3, right column, paragraph above Eq.1 | false |
| M15-8 | 本文采用的 wobbling 判据是候选带间 ΔI=1 跃迁具有显著 E2 性质；作者将其与 signature partners 间主要 M1 的连接作比较。 | experimental-criterion | direct | p.3, paragraphs below Fig.1 and Fig.2; Table I | false |
| M15-9 | 本文用 Eq.1 定义 `E_wob(I)=E(I,n_w=1)-[E(I-1,n_w=0)+E(I+1,n_w=0)]/2`；Fig.5 inset 的实验值从约 0.4 MeV 降至约 0.15 MeV 后回升。 | experimental-fact | direct | pp.3,5, Eq.1, Fig.5 inset | false |
| M15-10 | 作者把“带间 ΔI=1 E2 性质 + 低自旋区下降的 `E_wob`”联合解释为 `135Pr` transverse wobbling，并称其为 A≈130 区和低形变 `h11/2` 质子体系的首例。 | author-interpretation | direct | pp.2-3 and p.5, Summary | false |
| M15-11 | 1qp yrast 的 TAC 计算使用 `Δp=1.1 MeV`、`Δn=1.0 MeV`，得到并固定 `ε=0.16, γ=26°`；模型给出短轴为稳定转轴。 | model-result | direct | pp.3-4, paragraph spanning pages; Fig.4 | false |
| M15-12 | TAC 把 dipole band 与 `[πh11/2,νh11/2^2]` 3qp 组态联系，并把高自旋 yrast 延续与 `[πh11/2^3,νh11/2^2]` 5qp 组态联系；计算能量被作者评为较好再现实验。 | model-result | direct | p.4, left column; Fig.4 | false |
| M15-13 | 修改的 QTR 用 `J_m,J_s,J_l=7.4,5.6,1.8 ħ²/MeV` 和 `c=0.116` 拟合 zero-/one-phonon 能量；作者指出该拟合转动惯量比避免了 TAC 转动惯量导致的 transverse regime 过早坍塌。 | model-result | direct | p.4, right column; p.5; Fig.5 | false |
| M15-14 | QTR 对 zero-/one-phonon 能量及强 nonstretched E2 分量给出定性一致，但低估 `B(E2_out)`、高估 `B(M1_out)`；Table I 显示实验与 QTR 的跃迁概率比并非逐项一致。 | model-result | direct | pp.4-5, Table I, Fig.5 | false |
| M15-15 | QTR 还预测 one-quasiproton signature partner，但其激发能约高估 500 keV；TAC 对该 signature-partner 激发能给出更接近实验的结果。 | model-result | direct | p.5, left column, paragraph above Summary; Figs.4-5 | false |
| M15-16 | Table I的0.047/0.054是INGA count asymmetry A，Fig3纵轴有aNperp与Nparallel的归一化分式，不是已除Q的P。本文的angular-distribution数据来自另一次Gammasphere acquisition；短文未列该INGA的逐线Q(E)/a(E)系数、原始双向计数或完整Cov，不能把表列A直接与另一阵列P数值比较。 | observable-identity-and-readiness | direct-and-self-audit | printed082501-2实验；printed082501-3分析段；printed082501-4 TableI/Fig3 | true |
| M15-17 | 本文Ref21指向J.T.Matta的NotreDame2015 PhD thesis。新检索发现DataCite候选DOI10.7274/sj13902283h，注册题名Exotic Nuclear Excitations: The Transverse Wobbling Mode in 135Pr、creator J.T.Matta/year2015/publisher Curate ND；registry类型仅Text、无contentURL。候选登记不能代替机构/正文身份核验，当前未取得thesis正文、INGA Q或Cov。 | bibliographic-lead-boundary | metadata-and-self-audit | printed082501-6 Ref21；https://api.datacite.org/dois/10.7274/sj13902283h | true |

## Nuclear Structure Information

- [[135pr-yrast-band]]：Fig.1 中的主要 E2 序列，作者记为 `n_w=0`；
- [[135pr-side-band]]：通过 ΔI=1 mixed transitions 连接 yrast，作者记为 `n_w=1` wobbling band；
- [[135pr-signature-partner-band]]：较弱侧带，593.9 和 702.7 keV 连接主要表现为 dipole/M1；
- [[135pr-dipole-band]]：建立在侧带之上的 ΔI=1 强 M1 序列，作者与 3qp magnetic-rotation 组态联系。

## Authors' Interpretation

- yrast/side-band pair 分别是 zero-/one-phonon wobbling bands；
- 连接跃迁的 E2 主导性质确立 wobbling，下降的 `E_wob` 进一步确定 transverse 类型；
- 高自旋处 wobbling structure 演化到 3qp magnetic-rotation dipole band；
- wobbling excitation 与普通 signature-partner excitation 在同一核素中并存，被作者视为偏离轴对称的证据。

这些是 Matta 2015 的支持方解释，不是本 Wiki 对后来争议的裁决。

## Model Results

- TAC 给出 1qp、3qp、5qp 组态能量和角动量取向；
- QTR 拟合 zero-/one-phonon 能量、`E_wob` 和带间跃迁概率比；
- QTR 对 `B(E2_out)`、`B(M1_out)` 和 signature-partner 激发能存在定量偏差；
- QTR 转动惯量来自能量拟合，不能作为独立实验测量。

## Competing Interpretations and Limitations

- 本文是 transverse-wobbling 支持方原始实验；后续反对或替代解释尚未在本 project 中摄入，不能由本页代表争议全貌；
- PRL 仅给出部分能级纲图；正文明确称完整符合、角分布、asymmetry 分析和 full level scheme 将在后续工作中给出；
- 702.7 keV 跃迁的具体 DCO ratio 未列出；
- 710.2 keV 连接跃迁的 mixing ratio/偏振未直接测出，Table I 的概率比使用前一条 mixing ratio 的下限约束；
- E2 fraction 来自 mixed-transition 分解，不等于独立寿命测得的绝对 `B(E2)`；
- `E_wob` 下降是本文采用的 transverse 判据之一，但其解释依赖 zero-/one-phonon 带对应；
- TAC/QTR 的形变、转动惯量、配对和组态均具有模型依赖。

## Extracted Pages

- Nucleus: [[135pr]]
- Bands: [[135pr-yrast-band]], [[135pr-side-band]], [[135pr-signature-partner-band]], [[135pr-dipole-band]]
- Experiments: [[atlas-gammasphere-135pr-o16-80mev]], [[tifr-inga-135pr-o16-80mev]]
- Concepts: [[wobbling-motion]], [[transverse-wobbling]], [[signature-partner-bands]]
- Observables: [[multipole-mixing-ratio]], [[interband-e2-strengths]], [[wobbling-energy]]
- Methods: [[gamma-gamma-coincidence]], [[dco-ratio]], [[linear-polarization-asymmetry]]
- Models: [[tilted-axis-cranking]], [[triaxial-particle-rotor-model]]
- Project: [[135pr-wobbling-controversy]]

## Personal Notes

本页只建立 Matta 2015 的支持方证据链。用户已完成人工页面级审阅，并确认 M15-1 至 M15-15 与原文对照无误；这不构成对后续争议的裁决。

## 2026-10-17定向复核：A与P的数据身份

本次读6页文章主线及第7页版权附页，视觉核Fig1/2、TableI/Fig3；原SHA-256不变。原page级human-reviewed与M15-1–15逐字保留，新M15-16/17仅Codex self-audit、needs_review:true。原Personal Notes的用户审核范围仍限1–15，不扩到本节。

[[135pr-mixing-branch-input-contract]]把本表与Lv22主文P及SI的Ap逐量对齐；INGA与JUROGAM II不能共用Q或a。角分布/Gammasphere与偏振/INGA是独立采集，但两者分析仍共享transition/spin/取向与理论约定；不能从不同campaign自动推出所有nuisance独立。新计算仅核已发表摘要和标定身份，没有重拟合本文angular distributions或裁决wobbling。

后续全文入口：[注册DOI候选](https://doi.org/10.7274/sj13902283h)、[机构旧show记录](https://curate.nd.edu/show/sj13902283h)、[DataCite元数据](https://api.datacite.org/dois/10.7274/sj13902283h)。本run的GoogleScholar检索超时、Figshare API403、机构search/home202空body、doi landing ConnectionError已记录；未得到公开file URL，不原样重试失败入口，不以登记title补写全文结论。M15-17只是一项可恢复的文献线索。
