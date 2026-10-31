---
type: source
title: "Der Mateosian and Sunyar 1974 - Attenuation coefficients for partially aligned nuclei"
aliases: [Der Mateosian Sunyar 1974 attenuation tables]
created: 2026-09-21
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: reference-tables
reading_depth: deep-read
title_original: "Tables of Attenuation Coefficients for Angular Distribution of Gamma Rays from Partially Aligned Nuclei"
authors: [E. Der Mateosian, A. W. Sunyar]
journal: "Atomic Data and Nuclear Data Tables"
year: 1974
volume: 13
pages: "391-406"
pii: "0092-640X(74)90007-2"
doi: "10.1016/0092-640X(74)90007-2"
canonical_source: "Der Mateosian & Sunyar, ADNDT 13, 391-406 (1974)"
library_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of attenuation coefficients for angular distribution of gamma rays from.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of attenuation coefficients for angular distribution of gamma rays from.pdf"
raw_sha256: "d31d778674037b17ec2e47f3e9a2d917e46bf273b6cc6e01c607e3eccb843e90"
nuclei: [generic]
reactions: [heavy-ion-alignment]
experiments: [gamma-angular-distribution]
models: [Gaussian-magnetic-substate-alignment, Yamazaki-coefficients]
observables: [alpha2, alpha4, angular-distribution, alignment-width]
methods: [reference-tables, attenuation-correction]
tags: [angular-distribution, attenuation, alignment, tables]
---

# Attenuation coefficients for partially aligned nuclei

## Bibliographic Record

- E. Der Mateosian & A. W. Sunyar, *At. Data Nucl. Data Tables* **13**, 391–406 (1974), PII `0092-640X(74)90007-2`.
- 规范文件：`raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/multipolarity/angular distribution/ADO/1974_Der Mateosian_Sunyar_Tables of attenuation coefficients for angular distribution of gamma rays from.pdf`。

## Scope and Reading Depth

- PDF pp.391–406 (16 pages) fully read: Gaussian m-substate alignment, `α2/α4` formulas, use example (`Ji=10→Jf=8`, `σ/J=0.3`), integral/half-integral tables and Yamazaki appendix extension to `J=26/51/2`.
- Not covered: later computerized table implementations.

## Key Results

- Partial alignment is represented by Gaussian magnetic-substate populations `w_m∝exp(−m²/2σ²)`. Attenuation coefficients `α_k(J,σ/J)` multiply the complete-alignment `A_k^max` in `W(θ)=1+α2A2^maxP2+α4A4^maxP4` (PDF pp.391–394, Eqs.2–8).
- Tables cover integer and half-integer spins to `J=26` and `51/2`, with `σ/J=0.1–2.0`; the appendix extends Yamazaki complete-alignment angular functions to the same spin range (PDF pp.393–406).
- Worked `Ji=10→Jf=8`, pure E2 example gives `A2^max=0.41353`, `A4^max=−0.17514`; for `σ/J=0.3`, `α2=0.7560`, `α4=0.4093`, yielding attenuated `A2=0.3126`, `A4=−0.0717` (PDF p.393).
- The tables are intended to supply alignment attenuation, not to infer `σ/J` universally; reaction mechanism and side feeding determine the appropriate population model (PDF pp.392–394).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DA74-1 | Gaussian magnetic-substate alignment produces tabulated `α2/α4` attenuation coefficients. | reference-result | direct | PDF pp.391–394 | false |
| DA74-2 | Complete-alignment angular coefficients and partial-alignment attenuation must be applied separately. | method-boundary | direct | PDF pp.392–394 | false |
| DA74-3 | `σ/J` is a reaction/feeding model parameter, not a universal prior. | limitation | direct | PDF pp.392–394 | true |
| DA74-4 | 本文是391–406的attenuation对象，DOI90007-2；相邻407–462的mixed angular对象是DOI90008-4。相同作者/年份不等同同一paper，更不是两份独立实验。 | source-identity-boundary | direct-and-metadata | printed391 title/PII；printed394 refs；Crossref DOI identity | true |
| DA74-5 | Eq3将observed coefficients写为alpha_k A_k,max，Eq4/5的alpha=rho/B、half-integer参考absM=.5；Eq6虽称sigma为half-width，但明确exp[-m²/(2sigma²)]。本表是nuclear population attenuation，不是给定detector的Q(E)或geometry correction。 | reference-width-and-layer-definition | direct | printed392 Eqs3–5；printed393 Eq6；printed394 table explanation | true |
| DA74-6 | TableII J23/2、sigma/J=.2行印alpha2=8.94266E−01、alpha4=6.89096E−01；本任务同定义有限CG/Gaussian计算在末位舍入内复现。它确认SE21条件计算所用theory定义，不能恢复SE21实际校准程序/响应。 | primary-table-and-replay | direct-and-derived | printed400/PDF10 TableII J23/2 .2 | true |
| DA74-7 | AppendixB JI23/2→JF19/2行的B2F2(22)=.40373、B4F4=−.16149，符合本任务pureE2 complete-reference的65/161、−26/161。对应列是maximum coefficient，不能直接当observed A或alpha。 | maximum-coefficient-crosscheck | direct-and-derived | printed405/PDF15 AppendixB JI23/2 JF19/2 | true |
| DA74-8 | Crossref当前给本DOI issue4，而raw页脚明确Vol13 No5 May1974；title/authors/PII/pages仍唯一匹配，issue字段冲突独立保留needs_review，不据metadata改写原件。 | metadata-field-boundary | direct-and-metadata | printed391/PDF1 footer；Crossref10.1016/0092-640X(74)90007-2 | true |

## Summary

This companion to HS-081 supplies the attenuation half of the high-spin angular-distribution calculation. It makes explicit the numerical bridge between assumed m-substate populations and measured `A2/A4`, and therefore the uncertainty entering DCO/ADO/mixing-ratio inference.

## Competing Interpretations and Limitations

- Gaussian m-substate populations and `σ/J` are reaction/feeding assumptions, not universal alignment truths.
- Table attenuation factors cannot repair an incorrect spin sequence, detector geometry or side-feeding model.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| DA74-AR-1 | Population chain | Reaction/feeding → Gaussian `w_m` → `α_k(σ/J)` → measured angular coefficients. | PDF Eqs.3–8, worked example | self-checking |
| DA74-AR-2 | Transfer condition | Use table only with matching spin, alignment model, gate and convention; otherwise propagate model variance. | PDF pp.392–394 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]] and HS-081's mixed-multipole coefficient tables.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `DA74-P0-1`: Do not treat table `α2/α4` values or `σ/J` as detector-independent alignment truth.

## Extracted Pages

- Methods: [[angular-distribution]], [[angular-correlation]]。

## 2026-10-17原件回核：核attenuation、reference与实际校准分层

本次核原raw SHA，读printed391–394正文/用法及表/Appendix说明，视觉核printed400的J23/2 .2与printed405的23/2→19/2行；不是新逐项复核16页全部数值。原DA74-1–3和review状态保留，新4–8 true。源码未取得，不把作者1974程序当已重放；本run用自己的source-defined tensor代码核两个精确行。

[[se21-alignment-calibration-consistency]]的(.894266,.689096)及pureE2 reference与本原表相符，因此不能靠把sigma的名字改成HWHM解释SE21表列(.92,.30)。这仍只限定matchedrho/B的条件应用，SE21 actual alpha_exp的reference/geometry/gate/normalization操作未得；不认定作者代码或实验错误。sigma是连续Gaussian指数width参数，有限离散spin population的RMS另算。

[primary-control脚本](../../system/scripts/day16_ms74_primary_controls.py)与[冻结原表输入](../../outputs/learning-daily/20261016-DAY15-ado-angular-distribution-geometry-run-01/day16-ms74-primary-table-input.json)保存源末位、raw hash与同理论谱系边界。[[der-mateosian-sunyar-1974-angular-coefficients]]是另一个对象，Q符号/最大系数和正负列须各自核对，不能因同作者直接混用。
