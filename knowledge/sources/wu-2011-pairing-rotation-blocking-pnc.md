---
type: source
title: "Wu et al. 2011 — 转动与阻塞导致的核配对减弱：PNC关联能与BCS/LN边界"
aliases: [Wu 2011 pairing rotation blocking, 1104.3385]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: theoretical-research
reading_depth: read
title_original: "Nuclear pairing reduction due to rotation and blocking"
authors: [X. Wu, Z.H. Zhang, J.Y. Zeng, Y.A. Lei]
journal: "Physical Review C"
year: 2011
volume: 83
pages: "034323"
doi: "10.1103/PhysRevC.83.034323"
citation_key: wu_2011_pairing_rotation_blocking
citation_key_origin: crossref-and-arxiv
citation_key_verified: 2026-10-29
canonical_source: "doi:10.1103/PhysRevC.83.034323"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/wu-2011-pairing-rotation-blocking-arxiv1104.3385.pdf"
raw_sha256: "3e0a00171798bed92006eac788d578fbcb73fb2d64338dfab33bf7a7793f2979"
nuclei: [168Yb, 168Hf, 177Ta, 178W]
models: [PNC-CSM, BCS, HFB, Lipkin-Nogami]
observables: [pairing-correlation-energy, effective-pairing-gap, angular-momentum-alignment]
methods: [CMPC-diagonalization, exact-number-blocking]
tags: [pairing, PNC, rotational-response, evidence-boundary]
---

# 转动、阻塞与有限核配对关联

## Bibliographic Record

Wu等，PRC83,034323(2011)，DOI `10.1103/PhysRevC.83.034323`。实际取得arXiv1104.3385v2 PDF15页，318222字节；SHA见frontmatter。PDF页头为2011-04-19，内文Dated为2021-03-23，保留该载荷差异，不改写期刊年份。

## Scope and Reading Depth

定向阅读PDF pp1–5的摘要、BCS/HFB与LN讨论、PNC哈密顿量和Eq10关联能型gap定义，及pp6–12相关转动/阻塞结果文字。未逐点数字化图像，不声称重现其所有核的计算。该来源不包含105/106Cd或104Pd的AMR新实验。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WU11-01 | PNC在固定粒子数的多粒子组态空间直接对角化，显式保留Pauli阻塞；与BCS/HFB的破缺粒子数变分态不同。 | model-definition | direct-original | PDF pp2–5 Eqs1–9 | true |
| WU11-02 | 原文将BCS/HFB的锐配对崩溃作为有限核近似问题，讨论LN近似投影在弱配对时可能失效；不能说所有LN计算都会在同一临界频率崩溃。 | author-method-assessment | direct-original | PDF pp2–3 | true |
| WU11-03 | Eq10用配对相互作用能定义tildeΔ=sqrt(−G0〈HP〉)型诊断量；它不是固定N态的异常平均〈aa〉。自配对对角项和单极/四极项的约定必须随模型记录。 | model-definition-and-boundary | direct-original plus operator audit | PDF p5 Eq10、Eqs11–12 | true |
| WU11-04 | 对文中研究的正常/超形变及多准粒子带，PNC给出的关联能型gap随频率总体缓降或近常数；这些结果不能升级为所有核任意频率下永不消失的定理。 | model-result | direct-original | abstract and PDF pp6–12 | true |

## Summary

本文为“粒子数守恒并不等于没有配对关联”提供方法依据。其gap须按关联能定义解释，不能与BCS异常场Δ直接等同。

## Competing Interpretations and Limitations

有限空间中的固定N是精确的，但单粒子势、配对强度、截断空间和选定多体哈密顿量仍是模型输入。文中有限例子的平滑关联变化不排除其它体系中的真实构型交叉。阻塞处理的“exact”指指定空间中的Pauli代数，不是全核哈密顿量无近似。

## Extracted Pages

- [[amr-pnc-bcs-ln-pairing-coherence-band-evolution-audit]]

## Human Review

Codex source/claim self-audit；保持`unreviewed`。

## Review Status

方法与关联能定义定向已读；未重现多核PNC数值。
