---
type: source
title: "ENSDF 132Sn Coulomb-excitation subfile"
aliases: [ENSDF 132Sn CoulEx, 132Sn Coulomb excitation evaluation sheet]
created: 2026-09-28
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: deep-read
title_original: "132Sn Coulomb excitation"
authors: [Balraj Singh]
journal: ENSDF evaluation subfile
year: 2018
citation_key: "singh_2018_132sn-coulomb-excitation"
language: en
canonical_source: "https://www.nndc.bnl.gov/ensnds/132/Sn/coulex.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260928-DAY2-shell-gap-single-particle/ensdf-132Sn-coulex.pdf"
raw_sha256: 1fc046f50b2197f637a86591114e4956504ddf4099a7b51a1c4dde040bd708ea
data_url: "https://www.nndc.bnl.gov/ensnds/132/Sn/coulex.pdf"
data_sha256: 1fc046f50b2197f637a86591114e4956504ddf4099a7b51a1c4dde040bd708ea
data_bytes: 27352
nuclei: [132sn]
reactions: [132sn-coulomb-excitation]
experiments: [hribf-orln-coulomb-excitation]
models: []
observables: [b-e2]
methods: [evaluated-data-compilation]
tags: [ensdf, sn132, coulomb-excitation, b-e2, source-lineage]
---

# ENSDF `132Sn` Coulomb-excitation subfile

## Bibliographic Record

The single-page `Coulomb excitation` subfile for `132Sn` was retrieved from NNDC NuDat/ENSDF on 2026-09-28, visually checked and retained at `raw/papers/gpt/learning-daily/20260928-DAY2-shell-gap-single-particle/ensdf-132Sn-coulex.pdf`. The payload hash is `1fc046f50b2197f637a86591114e4956504ddf4099a7b51a1c4dde040bd708ea` (27,352 bytes). The sheet identifies Balraj Singh as evaluator, ENSDF cutoff date 28-Feb-2018, and cites conference-proceedings records.

## Scope and Reading Depth

This single-page subfile was read and visually checked in full. It covers the adopted `132Sn` Coulomb-excitation entry and source lineage only; it is not the primary measurement article.

## Summary

ENSDF adopts a preliminary `B(E2)↑=0.11 3` for the first `2+` state and traces it to two HRIBF-ORNL Coulomb-excitation references with different targets. The primary `48Ti`-target Varner article was checked directly; the carbon-target proceedings source remains unread.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ENSDF132C-1 | PDF 1 给 4040 keV 2⁺ 的两个初步向上强度 0.11(3)。2004Ra27 的前值 0.14(5)，2004Be56 的前值 0.14(6)，不同靶组分开记录。 | derived-observable | contextual | PDF p.1, `132Sn Levels` comments for the 4040-keV `2+` level | true |
| ENSDF132C-2 | The `2005Va31` measurement used a `48Ti` target; `2005Ra09` used a C target. The sheet says both ran at HRIBF-ORNL with different targets and identifies the citations as conference proceedings. | experimental-method | contextual | PDF p.1, paragraph under `Coulomb excitation` | true |
| ENSDF132C-3 | The ENSDF sheet records `B(E2)↑=0.11 3` for the `132Sn` Coulomb-excitation transition without printing units in that comments line. | evidence-boundary | direct | PDF p.1, `132Sn Levels` comments | true |

## Competing Interpretations and Limitations

This is an ENSDF evaluation summary, not a primary paper. `2005Va31` resolves to Varner et al., DOI `10.1140/epjad/i2005-06-128-7`, whose primary result is `0.11±0.03 e²b²` and whose photon-efficiency calibration was incomplete. The separate carbon-target `2005Ra09` record was not read as a primary paper in this run. Neither the NuDat display nor this ENSDF sheet is independent of the underlying Coulomb-excitation measurements.

## Extracted Pages

- PDF p.1: evaluation identity, target-reaction summaries, `132Sn` adopted `2+`/`B(E2)` and reference list.

## Related Knowledge

- [[varner-2005-coulomb-excitation-132-134sn]]
- [[iaea-livechart-132sn-134te-levels]]
- [[a130-shell-gap-orbital-observable]]

## Day19量化审计：ENSDF 132Sn B(E2)评估值物理时钟与寿命反演

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_sn132_coulomb_excitation_be2_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/sn132-coulomb-excitation-be2-result-057.json`，核准了 ENSDF 库仑激发子文件中 $^{132}\text{Sn}$ 评估值的物理时钟含义：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| ENSDF132C-D19-1 | 由 0.11(3) e²b² 向上强度得向下 0.022(6) e²b²。按 4.040 MeV 单 E2 辐射，τ≈3.45(94) fs。若强度用 e²b²，速率系数为 1.2252×10¹³ s⁻¹ MeV⁻⁵ (e²b²)⁻¹。该值由强度推得，实验方法可行性还需响应和靶条件。 | task-ensdf-be2-lifetime-audit | derived-and-boundary | PDF 1 及 Varner 2005 PDF 1 的量纲复核 | true |

## 2026-11-27 — 本地版本及科学覆盖

Complete PDF 1: History, reaction/target summary, 4040-keV level and γ row/diagram/footnote. Supporting primary: Varner PDF 1–3 targeted checks (print 391–393).

- The two preliminary strengths are each 0.11(3); C-target precursor 2004Ra27 used 0.14(5), ⁴⁸Ti-target precursor 2004Be56 used 0.14(6). Confirm e² b² for the Ti result from Varner. 原页 ENSDF PDF 1 level comments; Varner PDF 1 / p.391。
- At 4.040 MeV, 0.022(6) e² b² = 220(60) e² fm⁴ gives radiative mean life 3.45(94) fs under the stated single-line calculation. Use 1.2252×10¹³ for e² b²; 1.2254×10⁹ requires e² fm⁴. Withdraw the RDDS-feasibility inference. 原页 ENSDF PDF 1; Varner PDF 1; rate and unit rederivation in group-2.md。
