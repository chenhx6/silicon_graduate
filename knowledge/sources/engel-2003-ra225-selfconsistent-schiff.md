---
type: source
title: "Time-Reversal Violating Schiff Moment of 225Ra"
aliases: [engel-2003-ra225-selfconsistent-schiff]
created: 2026-10-29
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "Time-Reversal Violating Schiff Moment of 225Ra"
authors: ["J. Engel", "M. Bender", "J. Dobaczewski", "J. H. de Jesus", "P. Olbratowski"]
year: 2003
journal: "Phys. Rev. C"
volume: "68"
pages: "025501"
doi: "10.1103/PhysRevC.68.025501"
citation_key: "engel_2003_225ra-time-reversal"
canonical_source: "Phys. Rev. C 68, 025501 (2003); arXiv:nucl-th/0304075v2"
source_url: "https://arxiv.org/abs/nucl-th/0304075v2"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2003-engel-ra225-schiff.pdf"
raw_storage_status: raw-pdf-archived
raw_sha256: "f7e70d8ceddcb7c43e9cef9c137d2118f0d29cc6dc8239dc019120ccbd680009"
nuclei: [225Ra, 224Ra]
observables: [E1, Schiff-moment, octupole-deformation]
methods: [Skyrme-Hartree-Fock, selfconsistent-core-polarization]
tags: [octupole, parity-doublet, Schiff-moment, model-boundary]
---

# Time-Reversal Violating Schiff Moment of 225Ra

## Bibliographic Record

arXiv API的作者、题名、期刊引用、DOI与PDF首页作者/题名相符。实际取得nucl-th/0304075v2预印本，10页；已归档至 `raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2003-engel-ra225-schiff.pdf`。文件签名、字节与SHA256见同名机制审计JSON。

## Summary

本工作基于自洽 Skyrme-Hartree-Fock 与芯极化模型研究 $^{225}\text{Ra}$ 的时间反演破坏 Schiff 矩。确认内禀偶极矩 $D_0$ 随中子数在 $N=134-138$ 穿过零点，并严格区分普通电偶极算符与带 $r^2$ 权重的 Schiff 算符，为宇称双重态核中的奇宇称可观测量提供了微观理论基准。

## Scope and Reading Depth

定向阅读覆盖：PDF4–6; Fig3; odd-A selfconsistency and projection limitations。不声明所有参考文献、原始实验数据或数值代码已复现。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| EN03-1 | Fig. 3 中部的实验图点是从激发带 E1 强度推的 \|D₀\|。过零与变号来自模型计算。 | model-result | derived | PDF pp.4–5, Fig. 3 | true |
| EN03-2 | 末粒子与核芯相互自洽极化。实验室量的提取用刚性转子 1/3 因子，计算未显式做宇称投影。 | model-analysis | derived | PDF p.6 | true |
| EN03-3 | Eq. (3) 的 Schiff 算符含 −(5/3)⟨r_ch²⟩ 项，Eqs. (5)–(6) 限定双重态近似，最终实验室估计采用零程直接近似。 | theory-formulation | derived | PDF pp.2–3, Eqs. (1)–(4) | true |

## Competing Interpretations and Limitations

这是模型研究；普通E1、八极跃迁、PT奇Schiff响应的算符和证据谱系必须分开。跨EDF或奇偶核不能搬运分项值与相消点。Codex self-audit不是human review。

## Knowledge Impact and Learning Decision

支持逐算符、逐组态讨论芯极化；限制从小E1直接推断Schiff响应或从偶核占据直接推断奇核阻塞。

## Extracted Pages

- [[ba-ra-blocking-cancellation-operator-boundary]]

## Sources

- arXiv nucl-th/0304075v2; DOI 10.1103/PhysRevC.68.025501。

## 2026-11-27 — 馆藏原件与覆盖核对

Complete PDF 1–10, adding PDF 1–3 definitions and approximations; 7–9 Eq. (10), Tables I–II, Eq. (12) and conclusions; 10 references/experimental lineage.

- Fig. 3 middle plots |D₀| inferred from excited-band E1 strengths. The sign change is in the calculations; the near-zero magnitude is consistent with it. 原页 PDF 5 Fig. 3 and text; PDF 10 Ref. [22]。
- The odd particle changes the self-consistent solution and can polarize the core. Retain the rigid-rotor factor 1/3 and the absence of explicit parity projection; remove blanket quantified consequences for deformation and pairing. 原页 PDF 6 §IV.A; PDF 8 Table I。
- Use Eq. (3) including the −(5/3)⟨r_ch²⟩ subtraction and the parity-doublet reduction in Eqs. (5)–(6). Specify the zero-range direct approximation for the final laboratory estimate. 原页 PDF 2 Eqs. (3), (5)–(6); PDF 9 Eq. (12)。
