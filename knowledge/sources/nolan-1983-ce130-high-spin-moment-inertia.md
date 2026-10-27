---
type: source
title: "Nolan1983：130Ce高spin离散谱与关联谷宽惯量"
aliases: [The moment of inertia of 130Ce above spin 30 hbar, Nolan1983 130Ce]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: experimental-paper
reading_depth: deep-read
title_original: The moment of inertia of 130Ce above spin 30ℏ
authors: [P. J. Nolan, R. Aryaeinejad, A. H. Nelson, D. J. G. Love, D. M. Todd, P. J. Twin]
year: 1983
journal: Physics Letters B
volume: 128
issue: 5
pages: 285–289
doi: 10.1016/0370-2693(83)90261-7
canonical_source: https://doi.org/10.1016/0370-2693(83)90261-7
citation_key: ""
raw_file: raw/papers/1983_Nolan_Ce130_HighSpinMomentInertia.pdf
raw_sha256: 9085414a3cf1daafdeb3e7b685ea9bc6fdbfa44ee91f2e484c5eda353af6f927
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-nolan1983-ce130-companion-052/attachment-object-response.pdf
nuclei: [130ce]
methods: [gamma-gamma-coincidence, sum-energy-multiplicity-selection, energy-correlation-valley]
observables: [gamma-energy, dynamic-moment-of-inertia, alignment]
tags: [130Ce, 133Ce-method-blueprint, continuum-versus-resolved, model-interpretation]
---

# 实验谷宽约束J_band，不直接测得另一刚性形状

## Bibliographic Record

P. J. Nolan等，Physics Letters B128(5),285–289(1983)，DOI10.1016/0370-2693(83)90261-7。Crossref精确核作者/题名/卷页，首页1983-09-01、received1983-03-02。配置的出版商FULL XML→返回exact MAIN EID→Object API取得5页、307863bytes、SHA见frontmatter，首末页/身份已核；未宣称OA许可证或可再分发。候选在tmp、raw归档未做，不发布PDF/XML/OCR/整页图。

本篇为[[bengtsson-ragnarsson-1985-rotational-bands-particle-hole]] Ref63；Ref77另为Physica Scripta T5(1983)153–156，DOI10.1088/0031-8949/1983/t5/028，当前只核书目未读body，不能自动判same campaign或独立重复。

## Scope and Reading Depth

052全文5页/全部Figs1–4、唯一谷宽公式、方法/误差/限制和参考已原读并fresh visual；root另读全部文本、视觉核PDF2–4四图/原公式及assignment/污染/模型段，并fresh回核BR85 PDF61/printed74的J_band字样。没有数字化曲线、重拟谷宽/背景、生成误差条或复跑cranked shell model。

## Summary

实验看到高spin离散谱延伸、关联谷及约ℏω>.6MeV处接近常数的J_band^(2)，支持高spin转动/对齐研究。它的continuum量来自谷宽，不是所有E2计数的J_eff。具体i13/2对齐、形状不大变及rigid-body比较依模型/假设；原文保污染、最高离散线顺序和直接feeding替代。不能把BR85二级概括反写为本primary已测两形状或独立精确52/45差。

## Experimental or Theoretical Setup

150MeV 34S束轰击100Mo，目标通道100Mo(34S,4n)130Ce，三片97.3%enriched薄靶总约1.5mg/cm²。TESSA1为5个escape-suppressed Ge与7个BGO，BGO约50%4π，记录>50M ESS γγ事件并有sum energy/multiplicity信息。quoted ESS photopeak/total 662/1332keV为63%/52%，不能混成绝对photopeak效率。

Fig1为≥5BGO选择下5ESS谱，yrast用16+–22+跃迁门、isomer用14−–20−若干门；关联矩阵为512²、4keV/channel，沿负斜率作垂直对角谷的cut、按指定能窗平均。Fig2/3展示raw γγ+≥5BGO，没有减uncorrelated background；同campaign不同选样不等同一事件向量或独立重复实验。

## Key Results

新增claims均needs_review:true；派生实验量、作者解释/模型和任务算术分开。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| NO83-D24-001 | 本次150MeV Mo+S的TESSA1 ESSγγ/sum/multiplicity采集同时支持选门离散谱与关联分析；不同选样/门不能当不同独立实验或同一修正yield。 | acquisition-and-source-lineage | direct-original | PDF1–3 printed285–287; Fig1caption | true |
| NO83-D24-002 | yrast1242keV定为26+退激；1285/1311/1327与彼此/低带符合但顺序难放。isomer带确认至28−、1322线到30−仅possible；本篇没有逐条唯一32+拓扑。 | observed-line-versus-assignment-boundary | direct-original | PDF1–2 Fig1及其前后段 | true |
| NO83-D24-003 | 关联谷宽量字面为J_band^(2)，W=8ℏ²/J_band^(2)；raw512²/4keV矩阵及选窗给谷延至约1600keV。不是J_eff全E2计数、逐态τ或已resolved band向量。 | measurement-definition-and-derived-observable | direct-original | PDF3 printed287 formula/Figs2–3 | true |
| NO83-D24-004 | ≥5BGO样本129Ce+129La贡献约20%，其它更小，作者称结构most likely归130Ce、不能完全排其它。误差条是估计，本文不交完整response/Cov/谷拟合producer。 | contamination-and-uncertainty-boundary | direct-original | PDF4 printed288 leftcolumn; Fig4caption | true |
| NO83-D24-005 | Fig4本采集低频离散/高频谷宽、另一个124Te(12C,6n) NaI关联源分列；高区J_band^(2)为just above50，52是ε2=.25假设下rigid reference，非本文精确discrete45数值或shape测量。 | observable-reference-and-data-independence | direct-original | PDF4 Fig4及两栏 | true |
| NO83-D24-006 | i13/2 neutron对齐解释基于ε2=.25、gap1.2MeV的cranked shell model与isomer blocking；作者保directfeeding替代，称需完整离散线才能clarify backbend。constantJ_band只suggest无大shape变化，不认证γ刚性/rigidshape或pairing为零。 | author-interpretation-model-and-alternative | direct-original | PDF4 rightcolumn | true |
| NO83-D24-007 | 按原W式，名义J52/45分别对应W153.85/177.78keV，差23.93keV。是将BR85比较尺度代入的任务条件算术，不是从Fig2重测的两宽度、显著性/精度或设施率。 | explicit-source-grounded-design-arithmetic | original-formula-plus-task-calculation | PDF3 valleyformula; BR85 printed74 | true |

## Observable and Inference Chain

低于(ℏω)²约.4MeV²，Fig4由discrete ΔI/Δω求J_band^(2)；更高由W反推，原primary只说常数just above50ℏ²/MeV。52ℏ²/MeV的rigid reference要求ε2=.25，不能倒过来据接近52证明形状就是.25或完全刚性。BR85正文另写52对discrete45，是后文比较的概括；本primary不提供literal45和它的匹配Cov，不合成独立精准差。

W按图横轴Eγ1−Eγ2及原式定义。把J52/45代入得8/52=.153846MeV、8/45=.177778MeV，差.023932MeV，仅显示名义尺度。4keV/channel不等净谷宽误差/分辨力，不能按约6个channel就给可分辨/显著性；背景、混合级联、能窗/强度权重和仪器响应仍需actualproducer。未把Fig4误差条像素当数值Cov。

谷填充窗1040–1080/1190–1220/1280–1320keV、两选门bump和最高近能线均有实际观测。作者以共同isomer/yrast特征、某h11/2被blocked及模型i13/2对齐讨论，而非直接测出occupation。其gap1.2模型与BR85 no-pairing CNS不是同一个Hamiltonian或独立同参预测；未读所引Ref11原模型不补数。

## Competing Interpretations and Limitations

同campaign选门谱可强支持line/family关系，未排序最高线仍不得逆造levelscheme；continuum结构归属有20%污染边界。raw背景未扣是原分析合同，不等自动无效或已证明无偏。另NaI campaign被本文引用比较，不与本实验合并selectedevents或共同Cov。

作者给直接reaction feeding解释的替代，并说明完整离散跃迁尚缺；形状“无重大变化”是从constantJ的推断，不是对γ分布/rigidity的独立测量。本文没有reported新寿命、g、signedδ/绝对B，不给133Ce补clock或Harris。支持高spincollectivity链，限制把平均惯量与模型PES拼为已observed另一shape。

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]：观测集合、model reference与邻核迁移合同。
- [[bengtsson-ragnarsson-1985-rotational-bands-particle-hole]]：Ref63 primary与后文概括分列。
- [[chirality-shape-coexistence-companion-matrix]]：continuous correlation不代partner-resolved EM/shape向量。
