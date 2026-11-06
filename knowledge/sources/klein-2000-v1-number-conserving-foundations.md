---
type: source
title: "Klein 2000 v1：数守恒框架与附录迭代式边界"
aliases: [Klein2000 particle rotor foundations v1]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
source_type: theory-preprint
reading_depth: read
title_original: "Foundations of self-consistent particle-rotor models and of self-consistent cranking models"
authors: [Abraham Klein]
year: 2000
arxiv: nucl-th/0004051v1
canonical_source: https://arxiv.org/abs/nucl-th/0004051v1
citation_key: Klein2000FoundationsV1
citation_key_origin: task-primary-source-audit
raw_file: raw/papers/gpt/query/20261105-pairing-rotor-foundations/klein2000-v1.pdf
raw_sha256: 8dc1b32a948f542dee9ed6488a17015dd27b01bd2c8b6bb3ad79c2c6aa688461
archive_required: true
models: [core-particle-coupling, particle-rotor-model]
tags: [pairing, particle-number, cfp, source-consistency, iteration]
---

# 约束框架不等于固定矩阵的态选择器

## Bibliographic Record

所读为2000-04-23的arXiv v1，共29页；原TeX亦已归档。
对应PRC63,014316(2001)的最终版未核读，以下问题不外推到最终版。

## Scope and Reading Depth

定向读§II及AppendixA；视觉核PDF25–27，比较TeX原式。未复现全文模型。

## Summary

CFP连接同一奇核与A±1偶核，包含数目、归一和自洽约束；
不能以任意Nambu坐标扇区权重替代。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| KL-1 | V/U分别为到两邻偶核的移除/添加振幅；数目和轨道分辨归一是额外约束。 | formalism | direct-original | pp.4–7，Eqs2.9–2.10、2.24–2.28 | true |
| KL-2 | 按v1字面定义，A13乘√Λ把A12的范数变成Λ²Ω；未完成所称归一。 | source-consistency | original-plus-task-algebra | p.25，A12–A13 | true |
| KL-3 | A18/A21不能一般推出A22；A23及A25–A26的更新不满足所述投影切空间条件。 | source-consistency | original-plus-exact-counterexamples | pp.26–27，A18–A28 | true |

## Competing Interpretations and Limitations

30项有理数矩阵检查支持上述局部反例；不是对整个KK框架的否定。
没有验证勘误或最终期刊版，不把该迭代直接写入求解器。
详见[[ba129-core-and-pairing-validity]]；检查回执位于本轮`klein-review/`。

## Extracted Pages

- [[ba129-core-and-pairing-validity]]
- [[paired-single-j-positive-bcs-rotor]]

## Human Review

Codex选段与数学self-audit，非human-reviewed。
