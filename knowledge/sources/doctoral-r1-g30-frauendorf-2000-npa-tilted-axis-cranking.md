---
type: source
title: 'Frauendorf 2000: 倾斜轴推转模型描述多准粒子带与轴对称进动理论 (NPA全文56页)'
aliases: [Frauendorf 2000 NPA TAC, Nucl. Phys. A 677 115, 10.1016/S0375-9474(00)00308-0]
created: 2026-11-08
updated: 2026-11-08
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: Description of multi-quasiparticle bands by the tilted axis cranking model
authors: [S. Frauendorf]
journal: Nuclear Physics A
year: 2000
volume: 677
pages: 115-170
doi: 10.1016/S0375-9474(00)00308-0
canonical_source: https://doi.org/10.1016/S0375-9474(00)00308-0
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G30/frauendorf-2000-npa677-tilted-axis-cranking.pdf
raw_sha256: c7487e240ab561d9fafa089ce449a864fe892efbdc880845bf2355eeb848c135
raw_storage_status: archived-local
archive_required: true
learning_candidate: true
nuclei: []
models: [tilted-axis-cranking, pairing-plus-quadrupole, strutinsky-renormalization]
observables: [rotational-energy, b(m1), b(e2), mixing-ratio, tilt-angle]
methods: [cranked-mean-field, semiclassical-quantization, diabatic-tracing]
tags: [tilted-axis-cranking, tac, high-k-bands, precession, wobbling-boundary, multiquasiparticle, rare-earth, fulltext-read]
---

# Frauendorf2000：多准粒子带的TAC理论与带内电磁算符

## Bibliographic Record

S. Frauendorf，*Description of multi-quasiparticle bands by the tilted axis cranking model*，NPA677,115–170(2000)，DOI `10.1016/S0375-9474(00)00308-0`。
实际出版PDF为56页，哈希见frontmatter。

## Scope and Reading Depth

G30报告读取理论主线；总控独立核PDF1、5、10–11/printed115、119、124–125。
本页只保留已定位的自洽关系、参数化与带内EM，不声称总控重读全部56页或复算全套多准粒子带。
作者主要实例范围为N=102,103、Z=71,72,73；178W的具体实验来自另一个source，不能归作本文新测。

## Summary

TAC是自洽倾斜均场及半经典离散谱对应的方法。
带内ΔI=1 E2振幅可因倾角非零而存在，因此“存在E2”本身不唯一识别正交摆动伴带。
形状、角速度/角动量和电磁算符约定须共同使用。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| F00-1 | 自洽定态的E′、E及dE′/dω=−J、dE/dJ=ω；角速度向量与角动量期望平行 | mean-field-theory | direct-original | PDF5/printed119 Eqs.15–24 | false |
| F00-2 | SCTAC中总Routhian对形变等变量求定态；在良好形变带中冻结形变只是精度/代价相关近似 | model-construction | direct-original | PDF10/printed124 Eqs.38–39及末段 | false |
| F00-3 | 带内M1振幅涉及μ₃sinϑ−μ₁cosϑ；磁矩有指定有效自旋因子和量子修正 | operator-convention | direct-original | PDF10–11 Eqs.40–43 | false |
| F00-4 | Eq.45的带内ΔI=1 E2振幅为√(5/4π)(eZ/A)sinϑcosϑ[√(3/2)⟨Q′₀⟩−(⟨Q′₂+Q′₋₂⟩)/2] | operator-convention | direct-original | PDF11/printed125 Eq.45 | false |

Eq.45按本文Q′定义保留(eZ/A)，不擅自丢失电荷/质量归一。
Eq.43采用η=0.7，作者明确其它质量区可不同、质中也可不同；没有原文依据的±15%误差已删。

## Competing Interpretations and Limitations

均场倾斜解不自动给正交多声子伴带；带内半经典矩阵元不是所有带间跃迁的通用公式。
本页不由电荷轴对称推出真实K严格守恒或Pauli普适零惯量。
自洽条件、离散自旋对应、假态消除须按作者约定和具体解检验，不能写“高自旋精确等同”。

## Extracted Pages

[[doctoral-r1-g30-a160-precession-wobbling-20261108]]区分三个对称模型合同，
另用Purry论文核178W实验。跨区使用须重建实际组态和算符。

## Agent Self-audit Triage

P0：原件与算符归一核查已完成；旧稿遗漏eZ/A及惯量普适化已撤回。
P1：作者代码、全带数值与全部离散量子化细节未重放。
