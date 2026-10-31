---
type: source
title: "Tilted rotation of triaxial nuclei"
aliases: []
created: 2026-07-01
updated: 2026-10-26
status: active
review_status: human-reviewed
source_type: journal-article-theory
reading_depth: deep-read
title_original: "Tilted rotation of triaxial nuclei"
authors: [S. Frauendorf, J. Meng]
journal: Nuclear Physics A
year: 1997
volume: 617
pages: 131-147
doi: 10.1016/S0375-9474(97)00004-3
arxiv:
language: en
canonical_source: doi:10.1016/S0375-9474(97)00004-3
zotero_item_key:
citation_key: frauendorf_1997_Tiltedrotation
zotero_uri:
library_file:
raw_file: "raw/papers/1997_Frauendorf et al_Tilted rotation of triaxial nuclei.pdf"
raw_sha256: 9DC81B3147A786189DD0C2F31D79A56E9BB5D83E16FD0C8137BCCAF2A43D81E2
alternate_version_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/三轴/手征/1997_Frauendorf_Jie Meng_Tilted rotation of triaxial nuclei.pdf"
alternate_version_sha256: 2bd27510b61b1ca7e9d0eff559f8c0bcde46939249d7c5a720bf8425f7114f81
alternate_version_identity: "FZR-156 preprint, November 1996; same title/authors and precursor to NPA 617 (1997) 131-147"
nuclei: [134pr]
reactions: []
experiments: []
models: [tilted-axis-cranking, particle-rotor-model]
observables: [interband-transition-strengths]
methods: []
tags: [triaxiality, chirality, tilted-axis-cranking, high-spin]
---

# Frauendorf 与 Meng（1997）：三轴核的倾斜轴转动与手征性

## Bibliographic Record

Nuclear Physics A 617 (1997) 131-147。理论论文，共 17 页。

## Scope and Reading Depth

规范期刊版已全文精读；本批提供的 FZR-156 (Nov. 1996) preprint 21-page version was reread end-to-end to audit the same theory chain, figures 1–9, equations, transition-probability discussion, `134Pr` comparison and conclusion. Pagination and OCR artefacts differ from the journal PDF, so locators below retain section/figure semantics rather than silently transferring page numbers.

## Summary

论文把倾斜轴推转（TAC）应用于“两粒子耦合三轴转子”模型，并与精确粒子-转子模型（PRM）解比较。角动量位于主平面内时是 planar 解，对应一条 ΔI=1 带；角动量离开所有主平面时是 aplanar 解，对称性产生两条同宇称、近简并 ΔI=1 带。两条带对应主轴相对角动量矢量的相反手征性。论文将这种现象称为 chiral doubling，并讨论了从 planar 到 chiral 的转变及其跃迁特征。

## Experimental or Theoretical Setup

- 固定三轴形变的两粒子-转子模型；
- TAC 平均场近似与数值精确 PRM 解比较；
- 高 j 粒子/空穴与三轴转子的角动量几何；
- 以 `134Pr` 已知双带作为可能的早期实验案例，但不是本文的新实验。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FM97-1 | planar TAC 解中角动量位于主平面；aplanar 解中角动量不位于任一主平面。 | model-result | direct | Journal Sec.3.1; preprint Sec.3, Fig.1/5 | false |
| FM97-2 | planar TAC 表示一条 ΔI=1 带；aplanar TAC 表示两条简并、同宇称 ΔI=1 带。 | model-result | direct | PDF pp.8-9 | false |
| FM97-3 | aplanar 解的两组带具有相反的内禀手征性；planar 解是 achiral。 | model-result | direct | PDF pp.9-10, Figs.5-6 | false |
| FM97-4 | PRM 中左右手态之间的隧穿可使双带仍有劈裂；只有隧穿足够小时才接近简并。 | model-result | direct | PDF pp.11-12 | false |
| FM97-5 | 模型计算中，进入 aplanar 区后低多极阶的带间跃迁被抑制；TAC 只定性再现带内跃迁，不能计算带间跃迁。 | model-result | direct | PDF pp.12-13, Fig.7 | false |
| FM97-6 | 作者认为 A≈130 与 A≈190 是寻找手征双重带的有希望区域，但稳定三轴形变是否足够仍需微观 TAC 判断。 | author-interpretation | contextual | PDF pp.15-16, conclusion | false |

## Nuclear Structure Information

论文主要建立一般理论框架。`134Pr` bands 1/2 被讨论为接近手征性起始的候选，但作者明确保留隧穿和三轴稳定性的疑问。

## Authors' Interpretation

核转动手征性是动态对称性破缺：非转动三轴核本身是 achiral；角动量方向使短、中、长轴形成左右手几何。

## Model Results

- TAC 给出角动量取向和平均场几何；
- PRM 恢复量子隧穿与能级劈裂；
- 模型最有利区间约为 `25° < -γ < 40°`（使用本文 Lund convention）；
- 手征双带应是同宇称 ΔI=1 带，并具有强带内 M1/E2；理想极限下带间低多极跃迁受抑。

## Competing Interpretations and Limitations

- 固定 γ 的简化模型不能证明真实核具有稳定刚性三轴势；
- 近简并双带本身不足以证明手征性；
- TAC 平均场不处理左右手态之间的量子隧穿，也不能给出带间跃迁；
- γ 的正负与轴标号依赖约定，引用数值时必须注明 Lund convention。

## Extracted Pages

- Concepts: [[chiral-doublet-bands]], [[triaxial-deformation]]
- Models: [[tilted-axis-cranking]], [[particle-rotor-model]]
- Observables: [[interband-transition-strengths]]
- Synthesis: [[chiral-rotation-from-aplanar-tac]]

## Personal Notes

该文是“aplanar TAC → 动态手征性 → 同宇称双带”的奠基来源，但不能被用作某个具体核已证明手征性的实验依据。Preprint audit confirms no material change to the existing source claims; it is the same theory source/version lineage, not an independent study or experiment.

## Alternate-version self-audit (2026-09-20)

- The FZR-156 preprint reproduces the published theory structure: TAC/PRM basics, planar versus aplanar solutions, D2 symmetry, chiral geometry, transition probabilities, the `134Pr` candidate comparison and the need for microscopic self-consistent TAC.
- No new independent claims were promoted. The existing journal-page locators remain canonical; preprint OCR corruption in equations and page numbers is retained as a version caveat rather than silently corrected.


## Day21 checkpoint050：同宇称身份前提的定向复核

本次在Wiki priming后冻结补充回忆，仅定向读实际VoR PDF1摘要与PDF8–11的planar/aplanar、Fig5/6相关正文和宇称段，未重读全17页/完整图表，也不改旧human review record或原flags。本节是Codex自审。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FM97-D21-R50-1 | 摘要明确aplanar解对应same-parity双带；正文第141页强调该手征对称性破缺中parity仍为好量子数，并与相反宇称的parity doubling区分。因此对本文这一普通转动手征双带构造，可靠确定候选两带相反宇称会否定这对具体伙伴的身份前提，而非仅产生一个强度偏差。它不排除其它同宇称配对或更复杂模式。 | model-symmetry-and-bounded-identity-test | direct-original-and-explicit-task-inference | printed p.141 parity-doubling paragraph | true |

本结论用于[[day21-135nd-same-input-falsification-design]]的身份层反证，不把本理论模型当135Nd新实验或重新给其它核的模式认证。实际raw SHA256 `9dc81b3147a786189dd0c2f31d79a56e9bb5d83e16fd0c8137bccaf2a43d81e2`匹配原记录；本轮没有改变source的原人工审核状态。

## Day23内的Day24无学分预习：intrinsic对称性与量子双带

本次定向读期刊printed138–142（PDF8–12）Sec3.1/Figs5–6与PRM splitting，已核17页raw SHA9dc81b3147a786189dd0c2f31d79a56e9bb5d83e16fd0c8137bccaf2a43d81e2；fresh渲染PDF8/9/11/12供本轮关键段核对。不是重读全部17页，原人审FM97-1–6及page flags保持。新增仅needs_review:true的无学分预习。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FM97-D24P-001 | Sec3.1把PAC的I=α+2n序列、planar TAC的相反signature组合成一条ΔI1，以及aplanar的两组intrinsic handedness分别组织；printed141–142明确finitePRM同I态仍有splitting，归因左右态之间tunnelling。因此普通signature序列、intrinsic meanfield双解和量子partner bands不是同一个“伙伴”定义，TAC的理想degeneracy不能直接认证实测两带精确简并。 | direct-model-symmetry-and-quantum-restoration-boundary | direct-original-and-bounded-inference | printed138–142 Sec.3.1, Figs.5–6 and finalPRM paragraph | true |

与[[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]] F01-D24P-001/002配合：C²=+1及两态toy仅检查逻辑，不代本文原PRM。未增加新实验、MχD/shape-coexistence卡内容或Day24课程信用；不恢复旧Qt代理CI/225.8偏振符号/机时排他认证。

## Day24原件主线回读：模型范围与未见跃迁的条件

本轮重新读期刊17页全部文本主线，fresh视觉检查PDF2/3/5–10/12–16，覆盖Figs1–9和Eqs3/6–12/16–19的关键条件；实际raw SHA与页首相符。图中文字/趋势作所述核验，未数字化曲线、未复现PRM producer。原FM97-1–6及human review保持；新增仅Codex self-audit、needs_review:true。Crossref本轮HTTP200核到相同DOI/题名/NPA617/131–147；元数据核验不增加物理证据。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| FM97-D24-001 | 模型在给定形状下耦合h11/2粒子/空穴和转子，Eq7取irrotational惯量，示例C=.25MeV、𝒥=40MeV⁻¹；TAC把I换为经典J并令〈j²〉≈〈j〉²。Fig8的25°<−γ<40°属于这套参数/约定的有利区间，不能作实核普适手征硬门；printed145要求对四极矩自洽的微观TAC来检查形状稳定。 | model-assumptions-and-transfer-boundary | direct-original | printed134 Eqs6–9; printed143–145 Sec3.3 and Fig8 | true |
| FM97-D24-002 | Fig7在本模型aplanar区显示低多极带间强度抑制，作者明确纯TAC不能计算带间概率；134Pr实例中crossing附近两向links与band mixing相关，crossing以上未见links同时受弱布居限制，不能当有效强度上限。结论又明确高j粒子/芯/空穴三分量只是实现chiral TAC的一种方式，未规定所有候选必须严格具有该理想对齐。 | model-result-and-negative-evidence-boundary | direct-original | printed143 Fig7 and finalSec3.2; printed144–146 Sec3.3/conclusion | true |

[[135nd-chiral-partner-resolved-evidence-map]]将本理论与MU07三qp实验/TAC-RPA分开；本文固定形状及未见links不替代目标核的形状分布、branch限或g观测。


### Day24 checkpoint001 Agent self-audit triage

P0: none identified（本次新增范围无未隔离技术hard P0）。P1：FM97-D24-001/002已对原参数、Fig7及弱布居字面回核；迁移/负证据边界保留，未核actualPRMproducer。后续论文/关键问答仍按具体claim回源，未触发用户人审事件。
