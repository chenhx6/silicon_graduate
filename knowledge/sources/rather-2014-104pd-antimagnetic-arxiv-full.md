---
type: source
title: "Rather et al. 2014 — 104Pd反磁转动（arXiv全文版）"
aliases: [Rather 2014 104Pd AMR full arXiv, 1402.3422]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: experimental-and-theoretical-research
reading_depth: read
title_original: "Observation of anti-magnetic rotations in 104Pd"
authors: [N. Rather, S. Roy, P. Datta, S. Chattopadhyay, A. Goswami, S. Nag, R. Palit, S. Pal, S. Saha, J. Sethi, T. Trivedi, H. C. Jain]
journal: "Physical Review C"
year: 2014
volume: 89
pages: "061303(R), arXiv 1402.3422v1"
doi: "10.1103/PhysRevC.89.061303"
citation_key: Rather2014_104Pd_AMR_full
citation_key_origin: arxiv-and-crossref
citation_key_verified: 2026-10-29
canonical_source: "arXiv:1402.3422v1"
raw_file: "raw/papers/gpt/day26-20261028/rather-2014-104pd-antimagnetic-arxiv1402.3422v1.pdf"
raw_sha256: "b4a74c3f549860e857b83ba87e39a34a14ad2ed30c402a981e681826f01b7e3b"
nuclei: [104Pd, 106Cd, 108Cd, 110Cd]
models: [semiclassical-particle-plus-rotor]
observables: [BE2, J2, level-lifetime, alignment, routhian]
methods: [DSAM, lineshape-analysis, semiclassical-model]
tags: [104Pd, antimagnetic-rotation, DSAM, J2-systematics, evidence-boundary]
---

# Rather 2014：104Pd全文版、动态惯量与Cd对照

## Bibliographic Record

N. Rather 等，*Physical Review C* **89**, 061303(R) (2014)，DOI `10.1103/PhysRevC.89.061303`；本页使用实际取得的arXiv `1402.3422v1`全文，11页，SHA-256 `b4a74c3f549860e857b83ba87e39a34a14ad2ed30c402a981e681826f01b7e3b`。arXiv题名为“Observation of anti-magnetic rotations in 104Pd”，与期刊第一页节选的实验范围一致。

## Scope and Reading Depth

实际读取PDF 11/11页，包括DSAM线形方法、Table 1、粒子加转子模型Eqs.1–9、104Pd的I(ω)和B(E2)比较。该arXiv版本补足了既有机构PDF只取得第一页的缺口；两份载荷保留为不同来源版本，不能重复计数为两次实验。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RA14-FULL-01 | 104Pd高自旋yrast级联的DSAM寿命给出B(E2)=0.26(2),0.22(2),0.19(1),0.13(1),0.07(1),0.02(1) (eb)^2，对应I=16,18,20,22,24,26。 | experimental-fact | direct-original | PDF p10 Table1 | true |
| RA14-FULL-02 | Table1列出的J(2)/B(E2)=112.3(8.6),140.9(12.8),334.2(17.6),282.3(21.7),554.3(79.2) for I=16–24；高频比值增大但I=20有明显峰值。 | derived-experimental-table | direct-original | PDF p10 Table1 | true |
| RA14-FULL-03 | 104Pd的半经典配置取πg9/2^-2⊗ν[h11/2^2,(g7/2/d5/2)^2]，j=4.5, a=3.55, Vπν=1.2 MeV, Vππ=0.2 MeV, n=8, shears max=24ℏ, observed max=26ℏ, fitted core inertia ℑ=5 MeV^-1ℏ^2。 | model-input | direct-original | PDF pp4–5 Eqs4–9 | true |
| RA14-FULL-04 | 104Pd的B(E2)计算使用Qeff=1.3 eb、β2=0.19的Nilsson单粒子四极矩；模型能描述实验I(ω)和B(E2)。 | model-result | direct-original | PDF p5 and Fig3 | true |
| RA14-FULL-05 | 论文把I=16–26ℏ的单调B(E2)下降和大J(2)/B(E2)作为AMR证据；这一判断依赖DSAM、模型及其参数化，不能与PNC四空穴波函数直接等同。 | author-interpretation | direct-original | PDF pp3,5 | true |
| RA14-FULL-06 | 论文明确把106,108Cd称为两质子空穴纯AMR对照，把110Cd称为AMR与核心转动耦合；104Pd实验构型与Zhang2019 PNC构型存在两空穴有效模型和四个部分空穴微观模型的层级差异。 | author-comparison | direct-original | PDF pp1–2 | true |

| RA14-VPN-01 | 作者未给104Pd一个较大的独立拟合Vπν；直接从Cd系统学沿用Vπν=1.2 MeV、Vππ=0.2 MeV，并使用有效两空穴构型、n=8、jν=16。这里与PNC四空穴的区别是模型空间/归一化，不是测得Vπν加倍。 | model-input-and-transfer-assumption | direct-original | PDF pp4–6 Eqs4–9及结论 | true |

## Summary

Rather 2014全文补足了104Pd的逐点B(E2)和J(2)/B(E2)表。由表中B(E2)与比值相乘得到的动态惯量约为29.2(3.2)、31.0(4.0)、63.5(4.7)、36.7(4.0)、38.8(7.8) ℏ²/MeV（I=16–24），说明I=20附近存在明显有限差分峰，不能把104Pd J(2)写成完全平坦平台。

## Extracted Pages

- [[amr-vpinu-neutron-number-core-polarization-audit]]

- [[amr-j2-dynamic-inertia-endpoint-audit]]
- [[amr-pd-four-hole-geometry-evolution-audit]]
- [[rather-2014-104pd-antimagnetic-first-page]]

## Competing Interpretations and Limitations

Table 1的J(2)/B(E2)是作者列出的观测派生量；本页将其与B(E2)相乘得到J(2)，因此保留“派生值”标签。直接从完整Eγ级联重算仍需对图1能级和自旋约定逐点读取。DSAM中的stopping、side-feeding和顶端26+ effective lifetime会影响绝对值。Rather的半经典模型使用两质子空穴有效构型，而Zhang2019的PNC计算得到四个部分空g9/2空穴；不能将两者混写成同一量子波函数。

## Knowledge Impact and Learning Decision

为[[amr-j2-dynamic-inertia-endpoint-audit]]提供104Pd直接Table1数据和模型参数；修正“104Pd J(2)近似平坦”的过强说法，保留I=20附近峰值及高频比值上升。

## Human Review

Codex source self-audit；保持`unreviewed`。

## Review Status

arXiv全文11页已读；期刊版本与arXiv版本未作为独立实验计数。原始线形输入、协方差和完整Eγ表未从图1逐点重建。
