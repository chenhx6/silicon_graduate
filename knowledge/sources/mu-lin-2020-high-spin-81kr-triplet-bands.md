---
type: source
title: "穆琳 2020 硕士论文：81Kr 两对三重带结构"
aliases: [穆琳81Kr论文, Mu Lin 81Kr triplet bands thesis]
created: 2026-09-10
updated: 2026-09-10
status: ai-draft
review_status: unreviewed
source_type: masters-thesis-experiment-and-model
reading_depth: deep-read
title_original: "First observation of two pairs of triplet bands in atomic nuclei: Study of high-spin states in 81Kr"
authors: [穆琳]
journal: "山东大学硕士学位论文"
year: 2020
pages: 73
language: zh/en
canonical_source: "穆琳. 首次在原子核中观测到两对三重带结构：81Kr的高自旋态研究[D]. 山东大学, 2020."
citation_key: ""
raw_file: "raw/papers/degree dissertation/穆林_硕士.pdf"
raw_sha256: "D2723499E0298C02D64692577228D638A94A725A73A287C1D19D4DCC0E50D620"
nuclei: [81kr]
experiments: [ithembalabs-afrodite-81kr-se82-alpha]
models: [relativistic-mean-field, multiparticle-rotor-model]
observables: [ado-ratio, linear-polarization, signature-splitting, bm1-be2-ratio]
methods: [in-beam-gamma-spectroscopy, gamma-gamma-coincidence]
tags: [a80, chiral-doublet-bands, pseudospin, triplet-bands, masters-thesis]
---

# 穆琳 2020：`81Kr` 两对三重带

## Bibliographic Record

穆琳，*首次在原子核中观测到两对三重带结构：81Kr的高自旋态研究*，山东大学硕士学位论文，2020，73 页。原始 PDF SHA-256 为 `D2723499E0298C02D64692577228D638A94A725A73A287C1D19D4DCC0E50D620`。

## Scope and Reading Depth

- `deep-read`：读取题名页、摘要（PDF p.8）、目录、实验与能级图章节、物理讨论（Ch.4）和总结与展望（PDF p.61）；核对反应、统计量、带数、最高自旋及三重带判据。
- 未覆盖：参考文献逐篇复核、所有弱跃迁的独立谱图测量；文本中部分组态符号有扫描/OCR 缺陷。

## Key Results

实验用 `82Se(α,5n)`、65/68 MeV，在 iThemba LABS 的 AFRODITE 阵列记录约 `1.45×10^9` γγ 事件（摘要 p.8；总结 p.61）。

| issue_id | 主张 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| DD-20260910-MP-026 | `81Kr` 能级图相对早期工作增加 77 条跃迁、17 个能级，最高自旋约拓展到 `(37/2+)`；建立 7 条带。 | experimental-fact | direct | 摘要 p.8；总结 PDF p.61 | true |
| DD-20260910-MP-027 | 依据顺排、`E(I)`、signature splitting 和 `B(M1)/B(E2)`，作者提出两对近简并三重带及多重手征带。 | experimental-criterion + author-interpretation | indirect | 摘要 p.8；Ch.4；总结 p.61 | true |
| DD-20260910-MP-028 | 负宇称三带被提出为手征–赝自旋三重带，RMF 与 MPRM 计算支持该解释。 | model-result + author-interpretation | indirect | 摘要 p.8；Ch.4.2–4.3 | true |

## Summary

论文用 iThemba LABS 的 AFRODITE 数据扩展 `81Kr` 能级图，提出两对三重带及手征–赝自旋三重带；解释依赖 ADO、偏振、跃迁比和 RMF/MPRM。

## Competing Interpretations and Limitations

三重带/手征/赝自旋解释依赖 ADO、偏振、`B(M1)/B(E2)` 相位和 RMF/MPRM；“首次”是作者范围性表述。该来源可与 `78Br` 手征/八极关联比较，但不能把近简并三重带直接等同于静态手征。

- Related: [[chiral-doublet-bands]]、[[multiple-chiral-doublet-bands]]、[[pseudospin-chiral-quartet-bands]]、[[gamma-ray-linear-polarization]]、[[xiao-2022-chirality-octupole-correlations-74as]]。

### P0

- `DD-20260910-MP-026/027`：核对新增能级/跃迁数、带号、最高自旋和“two pairs”统计。

### P1

- `DD-20260910-MP-028`：核对三重带的宇称、组态、RMF/MPRM 参数和反证边界。

`knowledge_increment`: 提供 A≈80 奇 A 核多重手征/赝自旋三重带的 thesis-level 证据；`boundary-knowledge`: 三重带近简并与静态手征仍需几何和绝对强度判据。

## Extracted Pages

- 题名页/摘要：PDF p.8；实验与能级图：Chs.2–3；物理讨论：Ch.4；总结：PDF p.61。
