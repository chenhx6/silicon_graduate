---
type: source
title: Tanabe与Sugawara-Tanabe 2018：wobbling稳定性回复
aliases: [Tanabe Sugawara Tanabe 2018 wobbling reply]
created: 2026-10-24
updated: 2026-10-24
status: ai-draft
review_status: unreviewed
source_type: theory-commentary
reading_depth: deep-read
title_original: 'Reply to “Comment on ‘Stability of the wobbling motion in an odd-mass nucleus and the analysis of 135Pr’”'
authors: [Kosai Tanabe, Kazuko Sugawara-Tanabe]
journal: Physical Review C
year: 2018
volume: 97
pages: '069802'
doi: 10.1103/PhysRevC.97.069802
canonical_source: doi:10.1103/PhysRevC.97.069802
citation_key:
language: en
raw_file: raw/papers/gpt/_incoming/20261024-day22-wobbling-comments/tanabe-2018-reply-stability-publisher.pdf
raw_sha256: 76185615c6d990f923926f21ca75b503fbe687b55625cb26eb9a228ee78dc3a8
source_version: publisher-version-of-record
public_fulltext_url: https://journals.aps.org/prc/pdf/10.1103/PhysRevC.97.069802
nuclei: [135pr, 163lu]
experiments: []
models: [particle-rotor-model, Holstein-Primakoff, cranking]
observables: [moments-of-inertia, angular-momentum-components]
tags: [wobbling, model-assumptions, phonon-quantization, counter-argument]
---

# Tanabe与Sugawara-Tanabe 2018：wobbling稳定性回复

## Bibliographic Record

Crossref精确DOI核作者/年份/期刊；正式PDF标题、DOI、刊号与069802-1–2页脚一致。公开accepted入口404，随后出版社PDF端点200并验证PDF签名/身份/哈希；没有使用机构GUI或登录凭据。正文可访问不等同开放再分发许可。citation_key未唯一匹配现有Bib，留空。

## Scope and Reading Depth

两页全文与唯一Fig.1已实际读取，并视觉核069802-2的RMS图、13:21:4输入与稳定性段落。未复跑所引2017/2008粒子转子程序或HFB计算；本篇不包含新实验数据。

## Summary

本文回复[[frauendorf-2018-comment-wobbling-stability]]，为rigid惯量的β/γ依赖与配对消退后的spin标度辩护，并以总角动量I和核芯角动量R的RMS分量及量子化增量讨论何种运动可称wobbling。它与Frauendorf的几何/稳定性判据并非完全相同的命题。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| TR18-1 | 作者主张以rigid MoI描述β/γ依赖、以共同g(I)模拟CAP/配对变化，并引用自己对163Lu/135Pr能量与跃迁比的计算。作者认为对称轴MoI不可直接观测，反对Comment中的零惯量表述；这是理论/可观测量定义争论，不能写成本任务测得惯量。 | author-theoretical-argument | direct | 069802-1, first three paragraphs and right-column model discussion | true |
| TR18-2 | Fig.1为163Lu计算的sqrt⟨Ik²⟩、sqrt⟨jk²⟩与sqrt⟨Rk²⟩；作者用TSD1/2/3之间约1、2的Ix增量及Rx跨相邻spin的规律支持wobbling，jx/jy曲线近重合被作者解释为无j进动。RMS非带符号经典矢量，也不是实验直接测到的主轴轨迹。 | model-result-and-inference-boundary | direct-and-bounded-inference | 069802-1, Fig.1 discussion; 069802-2, Fig.1 and first left-column paragraph | true |
| TR18-3 | 为回应惯量比问题，作者采用135Pr的Jx:Jy:Jz=13:21:4、γ=26°、V=1.6MeV；报告next-to-leading稳定域延伸到21/2，但其完整对角化仍不显示所要求的Ix/Rx量子化规律，且Ry>Rx，因而不将该transient称wobbling。较大稳定域并未自动满足他们的量子化判据。 | model-result-and-author-interpretation | direct | 069802-2, paragraph beginning “The stability equations” and final conclusion | true |
| TR18-4 | 本文比较的是其自身模型判据与所引F14安排，未重新测量135Pr偏振/寿命。后来的Lv2022和Lawrie2020须按其实际发表内容另行比较，不能将本文当作对后两文的直接回复。 | source-independence-and-chronology | direct-and-bounded-inference | 069802-1–2, model discussion and references | true |

## Competing Interpretations and Limitations

[[frauendorf-2018-comment-wobbling-stability]]强调medium最大惯量及完整PRM稳定性；本回复强调不同的RMS增量/phonon判据。[[frauendorf-2014-transverse-wobbling]]确实描述完整QTR的j重定向；不能把回复中的理论批评泛化为已核所有旧producer的冻结实现。

采用更大惯量稳定区与满足“能量/矩阵元/角动量分量量子化”需分开检验；源文的模型指标不直接提供实验唯一模式识别。所引“更好M1”比较仍依赖不同参数/算符/模型设置，未在本任务重拟合。

## Knowledge Impact and Learning Decision

Limits：补齐2018争论反方，说明“临界点向高spin移动”与“满足phonon判据”是不同问题。与[[lawrie-2020-tilted-precession-wobbling]]共同约束[[wobbling-geometry-phonon-observable-contract]]的结论范围；保留未复跑程序和未测伴随观测，不裁决两方胜负。

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| competing-interpretation | [[frauendorf-2018-comment-wobbling-stability]] | 正式回复，惯量和模式判据有分歧 |
| limits | [[frauendorf-2014-transverse-wobbling]] | 对给定惯量比提出不同的量子化检验；不自动反演其代码 |
| methodological-bridge | [[wobbling-geometry-phonon-observable-contract]] | 区分稳定性、几何与phonon量子化 |

## Agent self-audit triage

P0：未发现上述归属范围的来源身份问题；不升格为transverse模式已被普遍证伪。P1：原producer与跨模型波函数映射未得，RMS/实验向量对象不同，数值比较不能扩大为实测不相容。新增claims均needs_review:true，无human review。

研究锚点：[[135pr]]、[[163lu]]；模型入口[[particle-rotor-model]]；这些链接仅供已有机制与证据比较，不将理论图转为核素实测。

## Extracted Pages

- Nuclei: [[135pr]], [[163lu]]
- Concepts: [[wobbling-motion]], [[transverse-wobbling]]
- Models: [[triaxial-particle-rotor-model]], [[cranked-shell-model]]
- Observables: [[moments-of-inertia]], [[angular-momentum-alignment]]
- Methods: [[wobbling-geometry-phonon-observable-contract]], [[minimal-wobbling-identification-protocol]]
