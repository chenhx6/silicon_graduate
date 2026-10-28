---
type: source
title: "Rather 2014 — 104Pd反磁转动（实际取得期刊第一页）"
aliases: [Rather 2014 104Pd AMR excerpt]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: experimental-research
reading_depth: skimmed
title_original: "Antimagnetic rotation in 104Pd"
authors: [N. Rather, S. Roy, P. Datta, S. Chattopadhyay, A. Goswami, S. Nag, R. Palit, S. Pal, S. Saha, J. Sethi, T. Trivedi, H. C. Jain]
journal: "Physical Review C"
year: 2014
volume: 89
pages: "061303(R)"
doi: "10.1103/PhysRevC.89.061303"
citation_key: Rather2014_104Pd_AMR
citation_key_origin: crossref
citation_key_verified: 2026-10-29
canonical_source: "doi:10.1103/PhysRevC.89.061303"
raw_file: "raw/papers/gpt/day26-20261028/rather-2014-104pd-antimagnetic-prc.pdf"
raw_sha256: "873b08c05f041d702a2c82f6243e9d73768a902ed91782891353bc42dfb1025b"
nuclei: [104Pd, 110Cd]
models: [semiclassical-particle-plus-rotor]
methods: [DSAM]
observables: [BE2]
tags: [104Pd, antimagnetic-rotation, partial-source, evidence-boundary]
---

# Rather 2014：104Pd反磁转动的第一页依据与全文缺口

## Bibliographic Record

N. Rather et al., *Physical Review C* **89**, 061303(R) (2014), DOI `10.1103/PhysRevC.89.061303`；Crossref核对题名、作者与DOI。期刊第一页印出2014-06-10发表日期。

## Scope and Reading Depth

机构作者页面取得的PDF实际只有1页（印刷`061303-1`）；页脚明确整篇为5页。只读取这一页，不能称已读完整实验。APS harvest全文接口返回401，缺页保留；没有绕过认证。该字节文件是第一页节选，不能因文件名有`prc.pdf`就当作5页正文。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RA14-EX-01 | 作者定义对称两刃关于中子轴的角θ，Ish=jp+2jh cosθ；对称横向磁矩相消，保Rz(π)并给B(E2)=15/(32π)(eQeff)²sin⁴θ。 | model-definition | direct-excerpt | printed061303-1 Eqs.1–2及相邻段落 | true |
| RA14-EX-02 | 摘要报告本工作以DSAM测量104Pd高自旋yrast E2强度并用半经典粒子加转子模型解释其下降。 | experimental-report-scope | direct-excerpt | printed061303-1 abstract | true |
| RA14-EX-03 | 导论回述110Cd较106/108Cd缓慢下降及core–AMR混合，并引用Roy2011；该回述不能作为新Cd实验计票，也不提供固定20%–30%核芯比例。 | secondary-attribution | direct-excerpt | printed061303-1 left/right columns | true |

## Summary

已核第一页的定义、摘要范围与引文谱系；未取得全文实验表，因此没有发布104Pd逐点寿命或核芯惯量。

## Extracted Pages

- [[amr-double-shears-tensor-core-coupling-audit]]
- [[zhang-2019-104pd-pnc-antimagnetic-rotation]]

## Competing Interpretations and Limitations

未取得后4页，不提取104Pd逐点τ/B(E2)、核芯惯量拟合或误差；这一页的摘要不认证具体实验表。参数、sidefeeding与stopping细节尚缺，不能以[[zhang-2019-104pd-pnc-antimagnetic-rotation]]中的重用实验点替代缺页。

## Knowledge Impact and Learning Decision

支持[[amr-double-shears-tensor-core-coupling-audit]]的角定义与sin⁴θ原文依据；本文首段所称磁偶极跃迁消失限于对称AMR图像，不能升级为任意跨带矩阵元为零。

## Review Status

Codex excerpt self-audit；`needs_review: true`，非人审。未完成的正文获取缺口由研究流程追踪。
