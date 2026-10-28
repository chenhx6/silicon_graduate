---
type: source
title: "Zhang 2019 — 104Pd反磁转动的粒子数守恒推转壳模型"
aliases: [Zhang 2019 104Pd PNC CSM, 1912.11990v1]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: theoretical-research
reading_depth: read
title_original: "Theoretical investigation of the antimagnetic rotation in 104Pd"
authors: [Zhen-Hua Zhang]
journal: "Chinese Physics C"
year: 2019
volume: 43
issue: 5
pages: "054107"
doi: "10.1088/1674-1137/43/5/054107"
citation_key: Zhang2019_104Pd_PNC
citation_key_origin: arxiv-and-crossref
citation_key_verified: 2026-10-29
canonical_source: "doi:10.1088/1674-1137/43/5/054107"
raw_file: "raw/papers/gpt/day26-20261028/zhang-2019-104pd-pnc-amr-arxiv1912.11990v1.pdf"
raw_sha256: "d0938039dd5c75f223bac9eca1d75e3c3d55f406504c41dc9f816a11d439de91"
nuclei: [104Pd]
models: [particle-number-conserving-cranked-shell-model]
observables: [BE2, angular-momentum-alignment, occupation-probability, moments-of-inertia]
methods: [cranked-many-particle-configuration, pairing-diagonalization]
tags: [104Pd, antimagnetic-rotation, pairing, shape-evolution, evidence-boundary]
---

# 104Pd反磁转动：配对、占据重排与形变变化的角色

## Bibliographic Record

Zhen-Hua Zhang, *Chinese Physics C* **43**, 054107 (2019), DOI `10.1088/1674-1137/43/5/054107`。Crossref与arXiv API分别核对作者、卷43、期5、054107及DOI。期刊元数据出版日期为2019-05-01；实际阅读字节为2019-12-27上传的arXiv `1912.11990v1`，8页。上传晚于期刊日期不等于新实验或新发表版本；未把arXiv PDF冒称出版商PDF。

## Scope and Reading Depth

实际读取8/8 PDF页；重点为p2 Eqs.1–11、p4 Fig.3与形变拟合说明、pp4–7 Figs.4–7的占据/对齐与两阶段机制。PDF签名、字节数、SHA及覆盖记录保存于Day26 worker工件`amr_tensor_core_audit.json`。本来源为理论计算，实验点取自Rather2014，不构成第二次独立寿命测量。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ZH19-PD-01 | 使用Nilsson项、Coriolis项−ωJx和单极配对项构造PNC-CSM；在截断多粒子组态中直接对角化配对，保粒子数。 | model-definition | direct-original | PDF p2 Eqs.1–8 | true |
| ZH19-PD-02 | 跃迁量采用半经典B(E2)=3/8〈Q20^p〉²；N=0–3闭壳对alignment为零，但对电四极矩仍重要。本文无另加有效电荷，不能据此把所有E2强度都归给未配对剪刀。 | model-definition | direct-original | PDF p2 Eqs.10–11与截断空间说明 | true |
| ZH19-PD-03 | 固定ε2=0.18的模型不能重现实验在ℏω>0.6 MeV的B(E2)快速下降。作者以随频率下降、约0.75 MeV趋零的ε2拟合数据；这条形变路径来自拟合而非独立形变观测。 | model-limitation-and-fit | direct-original | PDF p4 Fig.3及前两段 | true |
| ZH19-PD-04 | 加入配对改善惯量与B(E2)对比，但配对/双剪刀几何本身不足以解释该模型中的全部下降。作者还指出所引自洽TAC-CDFT也未重现高频快速下降，保留未决性。 | author-interpretation | direct-original | PDF p4 Fig.3讨论 | true |
| ZH19-PD-05 | 相对于100Sn，忽略配对的组态为π(g9/2)^−4⊗ν[(h11/2)^2(g7/2,d5/2)^6]；不能沿用简化两空穴组态作全核占据账。 | model-configuration | direct-original | PDF p1组态分歧；pp5,7总结 | true |
| ZH19-PD-06 | 约0.45–0.55 MeV质子对齐增益比中子快；更高频率中子(g7/2,d5/2)对齐增长更快。两种贡献的相对变化支持作者所称两阶段AMR；不是实测的固定核芯自旋百分比。 | model-result | direct-original | PDF pp5–6 Figs.5–6 | true |
| ZH19-PD-07 | 低频配对产生非零off-diagonal alignment，难以唯一拆成四支独立经典刃；>0.60 MeV时忽略较小off-diagonal项才近似画四刃。Jz采用sqrt(〈Jz²〉)而非〈Jz〉，应保留RMS几何性质。 | model-geometry-boundary | direct-original | PDF pp6–7 Fig.7与Eq.13 | true |

## Summary

PNC-CSM支持104Pd随频率变化的配对、占据重排与双剪刀图像，同时暴露固定形变计算对快速E2下降的不足；额外形变拟合不可当独立实验。

## Extracted Pages

- [[amr-double-shears-tensor-core-coupling-audit]]
- [[antimagnetic-rotation]]

## Competing Interpretations and Limitations

形变随频率变化由同一组B(E2)拟合，不能作为独立实验来确认原模型；本文无新的寿命数据。PNC-CSM的固定形变近似、截断空间及半经典E2处方仍限制外推。把normal-rotation的中子对齐当作唯象粒子加转子模型里的独立inert core，或把RMS刃几何当直接测量，均超过原文证据。

## Knowledge Impact and Learning Decision

`supports` [[amr-double-shears-tensor-core-coupling-audit]] 对几何相消、核芯运动学与电荷形变动力学分层；`limits` “Cd/Pd正常转动贡献一律产生平缓平台”及“固定四刃足以解释全部B(E2)”的普适措辞。

## Sources

- [[rather-2014-104pd-antimagnetic-first-page]]
- [[roy-2011-cd110-systematics-antimagnetic]]
- [[antimagnetic-rotation]]

## Review Status

Codex source self-audit；全部新claims保持`needs_review: true`与`review_status: unreviewed`。
