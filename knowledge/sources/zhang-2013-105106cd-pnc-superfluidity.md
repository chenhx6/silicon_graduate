---
type: source
title: "Zhang et al. 2013 — 105,106Cd反磁转动与粒子数守恒配对"
aliases: [zhang-2013-105106cd-pnc-superfluidity]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: theoretical-research
reading_depth: read
title_original: 'Nuclear superfluidity for antimagnetic rotation in 105Cd and 106Cd'
authors: [Zhen-Hua Zhang, Peng-Wei Zhao, Jie Meng, Jin-Yan Zeng, En-Guang Zhao, Shan-Gui Zhou]
journal: "Physical Review C"
year: 2013
volume: 87
pages: "054314"
doi: "10.1103/PhysRevC.87.054314"
citation_key: zhang_2013_105106cd_pnc_superfluidity
citation_key_origin: crossref-and-primary-record
citation_key_verified: 2026-10-29
canonical_source: "doi:10.1103/PhysRevC.87.054314"
raw_file: "raw/papers/gpt/day26-20261028/zhang-2013-105106cd-pnc-superfluidity-arxiv1303.3346v2.pdf"
raw_sha256: "8de4f9800f7b0cd52e6ea597f3d1eb58e0e3be3852054ef570bbc5fda9928c9b"
nuclei: [105Cd, 106Cd]
models: [antimagnetic-rotation]
observables: [BE2, angular-momentum-alignment]
methods: [source-claim-audit]
tags: [antimagnetic-rotation, evidence-boundary, Day26]
---

# Zhang et al. 2013 — 105,106Cd反磁转动与粒子数守恒配对

## Bibliographic Record

Nuclear superfluidity for antimagnetic rotation in 105Cd and 106Cd，*Physical Review C* **87**, 054314 (2013)，DOI `10.1103/PhysRevC.87.054314`。期刊元数据由Crossref原始API回包核验，学术版本身份与本地实际载荷分开记录。

## Scope and Reading Depth

实际PDF14页、%PDF-1.4、232718字节；阅读14/14页，重点pp4–10模型与结果。arXiv页头为1303.3346v2、2013-05-16，内文另印Dated: June27,2018；保留实见差异，不改写期刊2013身份。原字节/签名/哈希与元数据回包记录于worker工件；实验点沿用既有105/106Cd测量，不是新独立实验。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH13-01 | PNC-CSM在截断Fock空间对角化单极配对；固定粒子数并显式处理Pauli阻塞。 | model-definition | direct-original | PDF pp4–5 Eqs1–11 | true |
| ZH13-02 | 采用ε2=0.12/0.14；Gp=0.45 MeV，Gn=0.80/0.45 MeV分别用于105/106Cd。Gn的差异依惯量选取，不能说全部差异仅由自动阻塞产生。 | model-input | direct-original | PDF pp5–6 | true |
| ZH13-03 | 105Cd约0.4MeV的首交叉归于g7/2中子对齐；106Cd约0.3MeV交叉归于中子由g7/2到h11/2的占据变化。 | author-model-interpretation | direct-original | PDF pp7–8 | true |
| ZH13-04 | 105Cd配对计算Q20在0.45–0.75MeV由0.55降至0.41eb；106Cd高频B(E2)需ε2约0.14→0.12，固定形变不足。 | model-result-and-limitation | direct-original | PDF p9 Fig3讨论 | true |
| ZH13-05 | 配对使105Cd剪刀闭合更明显并平滑/延迟交叉；模型中配对仍重要，不支持“AMR必先配对崩溃”。 | model-result | direct-original | PDF pp9–10 Fig4 | true |
| ZH13-06 | 因签名守恒〈Jz〉=0，刃方向图的Jz近似采用sqrt〈Jz²〉；RMS不可冒称有向期望。 | model-geometry-boundary | direct-original | PDF p10 Eq12 | true |

## Summary

配对、阻塞、占据变化与形变变化共同影响AMR；“纯剪刀”不是微观无配对定理。

## Extracted Pages

- [[amr-cd-isotopes-quantum-termination-oddA-signature-audit]]

## Competing Interpretations and Limitations

固定Nilsson形变与有效配对强度属于输入/拟合。本文没有终止点全核波函数或实测配对坍缩。105Cd原实验另有Roy2013评论，正文未取得；保留该争议入口。

## Knowledge Impact and Learning Decision

为[[amr-cd-isotopes-quantum-termination-oddA-signature-audit]]提供限定范围的原始模型或来源身份依据；不升级人工审核，不把本载荷之外的正文内容写成已读。

## Human Review

Codex self-audit；review_status仍为unreviewed。

## Links

- [[antimagnetic-rotation]]
- [[amr-double-shears-tensor-core-coupling-audit]]
