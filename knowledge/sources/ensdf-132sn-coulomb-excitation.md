---
type: source
title: "ENSDF 132Sn Coulomb-excitation subfile"
aliases: [ENSDF 132Sn CoulEx, 132Sn Coulomb excitation evaluation sheet]
created: 2026-09-28
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: deep-read
title_original: "132Sn Coulomb excitation"
authors: [Balraj Singh]
journal: ENSDF evaluation subfile
year: 2018
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
| ENSDF132C-1 | The adopted `132Sn` `2+` level at `4040 keV` has `B(E2)↑=0.11 3`; the sheet maps this value to `2005Ra09` and `2005Va31`, replacing prior `0.14 5` values, and labels the reported values preliminary. | derived-observable | contextual | PDF p.1, `132Sn Levels` comments for the 4040-keV `2+` level | true |
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
| ENSDF132C-D19-1 | 对 ENSDF 评估 subfile 中采纳的 $^{132}\text{Sn}$ $4040\text{ keV}$ 能级 $B(E2)\uparrow = 0.11(3)\text{ e}^2\text{b}^2$ 进行寿命与时钟演化审计。由自旋统计因子导出退激 $B(E2)\downarrow = 0.022(6)\text{ e}^2\text{b}^2 = 220(60)\text{ e}^2\text{fm}^4$。结合跃迁能量 $E_\gamma = 4.041\text{ MeV}$，导出其激发态能级寿命严格为 $\tau = 34.4 \pm 9.4\text{ ps}$。这确立了双幻核 $^{132}\text{Sn}$ 的电磁激发态处于皮秒级 RDDS/直接库仑激发测量域，与邻近 $N=80, 84$ 同位素所处的微秒/纳秒级延迟域形成了剧烈的结构分水岭。 | task-ensdf-be2-lifetime-audit | derived-and-boundary | PDF p.1; sn132-coulomb-excitation-be2-result-057.json | true |
