---
type: source
title: "PDM文献对比：角统计量经tan转换的delta表示"
title_original: "Literature comparison of tan-transformed angle statistics"
aliases: [PDM文献角统计tan对比20261126]
created: 2026-11-26
updated: 2026-11-26
status: ai-draft
review_status: unreviewed
source_type: research-code-and-data
reading_depth: read
year: 2026
canonical_source: "User-authorized report extension using saved angle marginals and quoted literature values"
raw_file: "raw/writing/pado/20261029_review_v1/PDM/figures/data/literature_tan_20261126/manifest.json"
raw_sha256: "b195816f693c459efc1bb59642f49fe3c67d079b40df2500bb553a7b62164567"
raw_storage_status: archived-local
archive_required: true
citation_key: PDMLiteratureTanComparison20261126
evidence_sources: [pdm-report-figure-review-20261126-source, pdm-two-geometry-recovery-20261125-source]
tags: [pdm, mixing-ratio, angle-statistics, figure-audit]
---

# 角统计量经tan转换与文献delta的对比

## Bibliographic Record

2026-11-26用户明确要求在原报告中新增角统计量逐项取tan的文献比较图，保留已有真实delta密度评估图。本次没有新反演，没有更改文献值、误差或原始保存密度。

## Scope and Reading Depth

包含L01–L30全部30个声明模型，P-ADO/P-DCO/PDCO分别9/17/4例，对应15条不同跃迁。逐项独立积分原有角边缘密度，核对全部HDI分支、局部峰位、分位数和tan转换；同时核对实际PDF中的点位、区间线段、ETI端帽和文献左右误差。

## Summary

报告新增10.3，三图将arctan(delta)边缘密度上评估的统计量逐项取tan后与文献delta比较。10.2的真实delta密度评估图保持原样，三张原图的PDF矢量路径回归一致。当前阅读版143页、106图；本轮新增3图，其余图的核查沿用[[pdm-report-figure-review-20261126-source]]。

## Extracted Pages

第108页为10.3的评估约定；第109–111页图74–76分别为P-ADO、P-DCO、PDCO。原10.2的三张真实delta密度对比图仍位于105–107页，图65仍位于93页。四联图之后的页码随新增内容顺延。

## Key Results

| ID | claim_kind | evidence_level | locator | 结论与边界 |
| --- | --- | --- | --- | --- |
| TAN26-1 | software-audit | direct | `evidence/data-audit.json:cases` | 30条角边缘独立积分，全部HDI端点、分支内mode、中位数与ETI逐项tan核对通过，容差2e-12 |
| TAN26-2 | software-audit | direct | `evidence/data-audit.json:new_figures` | 实际PDF矢量路径对应全部30行、全部分支及原报文献误差；ETI采用错位虚线、叉号与非对称端帽 |
| TAN26-3 | software-audit | direct | `evidence/data-audit.json:existing_delta_figures_unchanged`、`preservation-and-layout.json` | 三张真实delta原图回归一致，原注入章节字节未改，原10.2及全部案例叙述保留 |
| TAN26-4 | software-audit | direct | `evidence/rendered-qa.json`、`compile-2.log`、`report-inventory.json` | 新增三图字体和碰撞零失败；两次编译无未定义引用或超宽盒；106图连续编号 |

## Competing Interpretations and Limitations

逐点恒等式tan(arctan(delta))=delta不意味着密度的mode或HDI具坐标不变性。本节先在角PDF评估再转换，因此不能把这些峰位与区间称为delta密度重新排序后的mode/HDI；与10.2的区别正来自评估测度。中位数与ETI在单调转换下应一致，数值细化误差边界沿用前一来源。

蓝色实线为转换后的全部角HDI分支，方块为转换后的角分支内峰位；叉号和虚线端帽分别为转换后的角中位数、q16与q84。黑菱形及左右误差是文献原报量，误差定义不强行统一成68%HDI。164Yb约−21°参考值没有报误差，保持空心点。30个声明模型不是30次独立实验，文献值也不是注入真值。

## Artifact Locators

- `final_snapshot/main.pdf`：本次143页冻结阅读版。
- `literature_and_evidence.tex`：新10.3与保留的原文献章节。
- `final_snapshot/`：三张新增PDF、绘图程序及本轮复现/核验脚本。
- `evidence/paired-comparison-pages.png`：105–107与109–111页并排视觉核查。
- `evidence/summary.json`：本轮范围、计数及检查结果。
- 原输入、数组和前一103图审计通过两个依赖source回链，历史清单未改写。本次由Agent自审，未记录人工审核事件。
