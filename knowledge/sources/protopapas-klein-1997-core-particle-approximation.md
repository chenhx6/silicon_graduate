---
type: source
title: "Protopapas–Klein 1997：芯—粒子近似和物理解选择"
aliases: [Protopapas Klein1997 strong coupling core particle]
created: 2026-11-06
updated: 2026-11-22
status: ai-draft
review_status: unreviewed
source_type: theory-method
reading_depth: deep-read
title_original: "Derivation and assessment of strong coupling core-particle model from the Kerman-Klein-Dönau-Frauendorf model"
authors: [Pavlos Protopapas, Abraham Klein]
year: 1997
journal: Physical Review C
volume: 55
pages: 699-713
doi: 10.1103/PhysRevC.55.699
canonical_source: https://doi.org/10.1103/PhysRevC.55.699
citation_key: ProtopapasKlein1997CoreParticle
citation_key_origin: task-primary-source-audit
raw_file: raw/papers/gpt/query/20261105-pairing-rotor-foundations/protopapas-klein1997-prc55-699.pdf
raw_sha256: b7ba75ea84348c3c6f877be6ce21c522428d19f9f226f6f1929111313c284053
archive_required: true
models: [core-particle-coupling, particle-rotor-model]
tags: [pairing, physical-subspace, approximation, cfp]
---

# 旋转项开启路径与固定转子K路径不同

## Bibliographic Record

作者公开站点取得15页期刊PDF，题名、作者、卷页及刊头相符。

## Scope and Reading Depth

核定刊版 PDF1–15（印刷 pp.699–713），包括 CFP 与电磁算符、内禀变换、耦合近似、物理解排序、Gd/Tb 算例及附录。未重放数值算例。

## Summary

标准芯—粒子近似的物理/非物理空间混合已有明确先例。
其数值方法不能只凭形式相似就移给另一个固定矩阵。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| PK-1 | 激发态问题中总能量正负不能直接分离物理解；CFP归一和两偶芯定义需保留。 | method-boundary | direct-original | pp.701–702，Eqs2.11–2.24 | true |
| PK-2 | §VII先从共轭反对称部分的BCS极限识别半空间，再开启对称部分；还提出固定J下的不交叉排序处方。 | algorithm-description | direct-original | p.709，§VII | true |
| PK-3 | 本任务固定完整转子、仅缩放K的路径起点不同；尚未完成CFP、能量和两偶芯字典。 | task-transfer-boundary | source-plus-explicit-comparison | p.709；本轮continuation/report.md附注 | true |

## Competing Interpretations and Limitations

Sec. VIII 的 \(^{157}\mathrm{Gd}\) 算例采用五个主壳的 Woods–Saxon 单粒子空间，两个偶芯含基态带和若干激发带。偶芯激发能由符合实验的唯象公式给出。作者先用完整 KKDF 调整四极场强度和单粒子能量，再固定同一组参数求近似模型。因此 Fig. 1 的能谱和 Fig. 2 的 \(B(E2)\) 是同一参数下的模型比较。\(^{157}\mathrm{Tb}\) 的实验 \(B(E2)\) 点过少，作者只在 Fig. 3 比较能谱。Sec. IX 把这两例的近似相合归于开启耦合时物理态与非物理态混合小，并指出多重避免交叉的情形可能改变这一结论。

原文方法依赖所述模型和谱/对称性条件；额外守恒量、真简并及截断需另查。
排序或连续追踪本身不提供实验模式标签，也不是新方法主张。

## Extracted Pages

- [[ba129-core-and-pairing-validity]]
- [[paired-single-j-positive-bcs-rotor]]

## Human Review

Codex定向self-audit；非原程序复现或human-reviewed。
