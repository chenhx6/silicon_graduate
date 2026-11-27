---
type: source
title: "ENSDF 134Te Coulomb-excitation subfile"
aliases: [ENSDF 134Te CoulEx, 134Te Coulomb excitation evaluation sheet]
created: 2026-09-28
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
title_original: "134Te Coulomb excitation"
authors: [A. A. Sonzogni]
journal: Nuclear Data Sheets
year: 2004
citation_key: "sonzogni_2004_134te-coulomb-excitation"
volume: 103
pages: 1
language: en
canonical_source: "https://www.nndc.bnl.gov/ensnds/134/Te/coulex.pdf"
raw_file: "raw/papers/gpt/learning-daily/20260928-DAY2-shell-gap-single-particle/ensdf-134Te-coulex.pdf"
raw_sha256: 37f02b8998302844bd7e1d7816c405e1779e335b5f4a1ef5743ffd01c8e505ea
data_url: "https://www.nndc.bnl.gov/ensnds/134/Te/coulex.pdf"
data_sha256: 37f02b8998302844bd7e1d7816c405e1779e335b5f4a1ef5743ffd01c8e505ea
data_bytes: 21210
related_doi: 10.1016/S0370-2693(02)03066-6
nuclei: [134te]
reactions: [134te-12c-coulomb-excitation]
experiments: [coulomb-excitation]
models: []
observables: [b-e2, level-energy, lifetime]
methods: [evaluated-data-compilation]
tags: [ensdf, te134, n82, coulomb-excitation, b-e2]
---

# ENSDF `134Te` Coulomb-excitation subfile

## Bibliographic Record

The one-page NNDC/ENSDF Coulomb-excitation subfile was retrieved and visually checked on 2026-09-28. The payload is 21,210 bytes with SHA-256 `37f02b8998302844bd7e1d7816c405e1779e335b5f4a1ef5743ffd01c8e505ea`. It identifies A. A. Sonzogni as evaluator, *Nuclear Data Sheets* **103**, 1 (2004), literature cutoff 31-Jul-2004.

The cited primary record `2003Ba01` is bibliographically identified by Crossref and the NNDC reference route as C. J. Barton et al., “B(E2) values from low-energy Coulomb excitation at an ISOL facility: the N=80,82 Te isotopes,” *Physics Letters B* **551**(3–4), 269–276 (2003), DOI `10.1016/S0370-2693(02)03066-6`. The publisher article endpoint returned HTTP 403 in this run; the primary full text was not read.

The 2026-10-31 access recheck found the same boundary: OpenAlex marks the DOI as closed
with no repository full-text location, and no lawful public PDF was found. The evaluation
value therefore remains `evaluation-grounded`; this page does not upgrade it to a
primary-text-verified measurement.

## Scope and Reading Depth

This one-page evaluation subfile was read and visually checked in full. It covers the adopted `134Te` Coulomb-excitation record, not the full primary 2003 paper.

## Summary

The adopted `134Te` `2+` level is at `1279.11(10) keV`; the sheet attributes `B(E2)↑=0.13 4` and its derived lifetime to `2003Ba01`.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ENSDF134TE-1 | The adopted `134Te` `2+` level at `1279.11(10) keV` is associated with `B(E2)↑=0.13 4` from Coulomb-excitation reference `2003Ba01`; the sheet also lists `T₁/₂=0.64(20) ps` as derived from that strength. | derived-observable | contextual | PDF p.1, `134Te Levels`, 1279.11-keV row | true |
| ENSDF134TE-2 | The `2003Ba01` reaction is `134Te(12C,12C′)` at 350 MeV. | experimental-method | contextual | PDF p.1, header paragraph under `Coulomb excitation` | true |
| ENSDF134TE-3 | 1279.11(10) keV 的 † 指向 Adopted Levels 的能量、Jπ。B(E2) 和由其计算的半衰期属于 2003Ba01 实验谱系。 | evidence-boundary | direct | PDF p.1, 1279.11-keV level comments | true |

## Competing Interpretations and Limitations

NuDat 3 displays the same adopted level as `B(E2)(W.u.)=6.3 20` and the adopted-level comment `B(E2)=0.13 4`. These are two views of the same ENSDF evaluation, not independent measurements. The primary DOI metadata confirms identity, but the full paper could not be read from the publisher endpoint; retain the evaluated value and its locator without calling it independently verified against the article text.

## Extracted Pages

- PDF p.1: evaluator metadata, `134Te(12C,12C′)` reaction, adopted `2+` level, `B(E2)`, lifetime and reference identifier.

## Related Knowledge

- [[iaea-livechart-132sn-134te-levels]]
- [[a130-shell-gap-orbital-observable]]

## Day19量化审计：第一性原理跃迁常数核算、价质子有效电荷增强与飞秒寿命反演

> checkpoint088审计状态：本节旧“核准/定理/全绿”是待复核草稿；脚本算术通过不认证原文支持或实验结论。已指出的错误按本页checkpoint088修订，未逐条核者不得引用为已验证结果。


依据独立审计程序 `system/scripts/day19_te134_sn132_coulex_lifetime_audit.py` 的 10 项检验与基准输出 `outputs/learning-daily/20261021-DAY19-rdds-fast-timing-time-response-run-01/te134-sn132-coulex-lifetime-result-058.json`，核准了 $^{134}\text{Te}$ 库仑激发 $B(E2)$ 与半衰期反演的第一性原理物理契约：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| ENSDF134TE-D19-1 | 若输入 0.13(4) e²b² 为向上强度，按下行自旋因子 1/5 和单路 E2 辐射导出 T₁/₂≈0.636 ps，与同一强度的评价换算相符。相对 ¹³⁴Sn 的强度平方根比是所选矩阵元振幅比，提取有效电荷还需核结构模型。 | task-first-principles-coulex-audit | derived-and-boundary | PDF p.1; te134-sn132-coulex-lifetime-result-058.json | true |

## 2026-11-27 — 本地版本及科学覆盖

Complete PDF 1: History, reaction, both level rows, comments and dagger. Supporting Radford PDF 2 §2/Table 1 and PDF 5 reference; Varner PDF 4 for comparator.

- The dagger refers energy and Jπ to Adopted Levels. The 1279.11(10)-keV row gives B(E2)↑=0.13(4) without printed units and T₁/₂=0.64(20) ps derived from the strength. 原页 PDF 1 reaction heading, 2⁺ row and dagger。
- The same input yields conditional radiative T₁/₂≈0.636 ps. The square root of the selected ¹³⁴Te/¹³⁴Sn strength ratio is an amplitude ratio; its interpretation as e_p^eff/e_n^eff requires a nuclear matrix-element model. 原页 ENSDF PDF 1; Varner PDF 4 / print 394; derivation in group-3.md。
