---
type: source
title: "Sheikh et al. 2002 — HFB、PAV、Lipkin–Nogami与投影变分的精确模型比较"
aliases: [Sheikh Ring 2002 number projection comparison, nucl-th/0207080]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: theoretical-research
reading_depth: read
title_original: "Pairing correlations and particle-number projection methods"
authors: [J.A. Sheikh, P. Ring, E. Lopes, R. Rossignoli]
journal: "Physical Review C"
year: 2002
volume: 66
pages: "044318"
doi: "10.1103/PhysRevC.66.044318"
citation_key: sheikh_2002_number_projection_pairing_comparison
citation_key_origin: crossref-and-arxiv
citation_key_verified: 2026-10-29
canonical_source: "doi:10.1103/PhysRevC.66.044318"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/sheikh-2002-pairing-number-projection-arxivnucl-th0207080.pdf"
raw_sha256: "9e34140ffe31c15e0753d9e50f91de24886c29149f0b78bb67d9775299f4696c"
nuclei: []
models: [exact-cranked-deformed-shell-model, HFB, PAV, Lipkin-Nogami, number-projected-HFB]
observables: [pairing-energy, total-energy, aligned-angular-momentum, moment-of-inertia]
methods: [exact-model-benchmark, particle-number-projection]
tags: [pairing, particle-number-projection, Lipkin-Nogami, evidence-boundary]
---

# 有限模型中的投影方法比较

## Bibliographic Record

Sheikh、Ring、Lopes和Rossignoli，PRC66,044318(2002)，DOI `10.1103/PhysRevC.66.044318`。本地arXiv nucl-th/0207080v1为24页、237297字节，SHA见frontmatter；arXiv摘要页comments写18页，以实际PDF页数记录阅读覆盖。页头上传时间2002-07-27，内文日期2018-10-20；记录实见差异，不将该内文日期当新实验或期刊年份。

## Scope and Reading Depth

定向阅读PDF pp1–13的方法、可精确求解的推转变形单j壳模型、Figs1–6结果讨论与总结，以及LN与PHFB定义。未重写或逐点重放论文代码；研究对象是模型基准，不是105/106Cd或104Pd实测比较。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SH02-01 | 在文中可精确求解的推转变形壳模型内，HFB配对能在临界强度/频率出现锐崩溃；PHFB保留非零配对能，其总能与对齐角动量在该基准内与精确解吻合。 | exact-model-comparison | direct-original | PDF pp8–13 Figs1–6讨论及总结 | true |
| SH02-02 | Fig2的特定模型中，HFB配对能在ħω约0.45G以上消失；LN使下降略平滑并把零点推到较高频率，但在弱配对极限仍失效。这个0.45G不是核素普适临界值。 | model-specific-result | direct-original | PDF pp9–10 Fig2讨论 | true |
| SH02-03 | PAV从已有HFB态投影；在文中HFB配对消失后的区域，其结果回到未投影解，因而不自动修复丢失的变分配对关联。 | model-method-boundary | direct-original | PDF pp9–10 Fig2讨论、p12总结 | true |
| SH02-04 | 本基准说明PNC之外，合适的粒子数投影变分也能处理有限体系配对关联；不能把PNC描述成消除锐崩溃的唯一方法。 | method-comparison | direct-original | abstract、PDF pp11–13 | true |

## Summary

LN通常改善HFB的粒子数问题，但不是严格数投影，也不是弱配对极限的无条件保证。比较必须固定相同哈密顿量、空间、阻塞和观测量。

## Competing Interpretations and Limitations

单j壳基准的优劣排序不能直接当作完整Nilsson/EDF空间中的核素结果。PNC-CSM和PHFB不必使用相同单粒子势或相同相互作用；只有统一输入后才可定量比较。

## Extracted Pages

- [[amr-pnc-bcs-ln-pairing-coherence-band-evolution-audit]]

## Human Review

Codex source/claim self-audit；保持`unreviewed`。

## Review Status

方法和关键基准结果定向已读；未重放原论文数值。
