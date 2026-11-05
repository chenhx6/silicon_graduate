---
type: source
title: "Rouoof：DAE68 的129Ba TPSM先例"
aliases: [Rouoof 129Ba TPSM DAE68]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
source_type: conference-paper-model
reading_depth: read
title_original: "Microscopic study of wobbling motion in 129Ba"
authors: [S. P. Rouoof, Nazira Nazir, S. Jehangir, G. H. Bhat, J. A. Sheikh, N. A. Rather]
journal: Proceedings of the DAE Symposium on Nuclear Physics
volume: 68
pages: 167-168
year: 2025
volume_label_year: 2024
canonical_source: https://inspirehep.net/literature/2878218
citation_key: RouoofDAE68Ba129TPSM
citation_key_origin: task-bibliography-in-ba129-model-readiness
raw_file: raw/papers/gpt/query/20261105-ba129-model-precedents/rouoof-dae68.pdf
raw_sha256: 7c9be22bc25dec2661bb615334dc9d9cf2a4c755472560d5c7d716c8d968e0e5
archive_required: true
nuclei: [129ba]
models: [triaxial-projected-shell-model]
observables: [energy-spectrum, wobbling-energy]
tags: [a130, tpsm, model-precedent, conference]
---

# 129Ba TPSM：能量比较已有先例

## Summary

两页会议文展示四条负宇称带及候选摆动能的TPSM比较。其集体模式指定属于作者解释；
该文没有新增实验，也未列出可用于本任务的数值EM分支表。

## Bibliographic Record

PDF页眉为DAE68（2024）；INSPIRE记录2878218的publication year及imprint为2025。
两层日期保留，不把会议/卷年与登记出版年混为一项。
取得PDF和题录的清单为
`raw/papers/gpt/query/20261105-ba129-model-precedents/manifest.json`。

## Scope and Reading Depth

完整读取并视觉核两页、两幅图；未重建原TPSM代码、波函数或图上全部数值。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| RT-1 | 使用Nilsson+BCS、角动量投影及四极/配对相互作用；质中均取N=3,4,5。 | model-definition | direct-original | p.167 | true |
| RT-2 | 印刷形变参数写β=0.220、γ=0.150，未明确γ的角度单位/替代参数约定。 | convention-boundary | direct-original | p.167 Results | true |
| RT-3 | Figs.1–2比较能量，实验数据回引Chakraborty2024；band3的摆动解释不是新测量。 | model-comparison-and-lineage | direct-original | p.168 Figs.1–2及Ref.4 | true |
| RT-4 | 方法提及EM概率计算，但这两页未展示数值B值或光子分支结果。 | reported-output-scope | direct-original | pp.167–168 | true |

## Competing Interpretations and Limitations

“首次对129Ba做TPSM”不成立。对同一波函数作明确算符和未标定观测量的检验仍是
可研究问题，但不能据这份短文未列EM表便宣布没有其它先例。
不擅自把0.150转换成0.150°、弧度或ε′。

## Extracted Pages

- [[chakraborty-2024-possibility-wobbling-129ba]]
- [[ba129-model-input-and-holdout-contract]]
- [[triaxial-projected-shell-model]]

## Human Review

Codex原件self-audit；没有human-reviewed或论文接收资格认证。
