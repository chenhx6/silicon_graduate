---
type: source
title: "PDM全图核查：ETI误差棒、真实delta边缘与文献对比"
title_original: "PDM report figure audit and direct delta-density comparisons"
aliases: [PDM图示修订20261126]
created: 2026-11-26
updated: 2026-11-26
status: ai-draft
review_status: unreviewed
source_type: research-code-and-data
reading_depth: read
year: 2026
canonical_source: "User-authorized saved-density analysis and direct report-artifact verification"
raw_file: "raw/writing/pado/20261029_review_v1/PDM/figures/data/figure_review_20261125/manifest.json"
raw_sha256: "c5395bd3236b79f92f4b205d51dbf52d7feee6fa27278438e8a8bda2db9f7098"
raw_storage_status: archived-local
archive_required: true
citation_key: PDMFigureReview20261126
evidence_sources: [pdm-two-geometry-recovery-20261125-source, pdm-deterministic-report-revision-20261124-source]
tags: [pdm, mixing-ratio, probability-density, figure-audit, finite-domain]
---

# PDM图示修订与真实delta密度评估

## Bibliographic Record

2026-11-26用户授权的报告修订与保存密度再评估。复用既有60个确定性注入和30个文献声明模型，不新增PDM反演，不改变响应、观测或历史计算。前一报告及受影响工件的精确字节保存在`before/`；历史清单绑定的原比较图及文献TeX仍保留原路径和哈希。

## Scope and Reading Depth

核查最终报告全部103张图及139页布局：90张四联图、4张诊断图、3张角统计/宽度几何对比、3张新增真实delta密度几何对比、3张新增文献对比。文献案例L01–L30对应15条跃迁，按P-ADO/P-DCO/PDCO分为9/17/4个声明模型，不视为30个独立实验。

## Summary

图65保留在第93页，修正P-ADO误写偏振符合门的图例与图注。三模式比较图的ETI统一采用中位数叉号、q16/q84非对称误差棒、虚线和端帽，并与HDI实线略作错开。原角统计转换图未被真实delta评估图替换。

新增真实delta几何对比为第97–99页图68–70；文献delta对比为第105–107页图71–73。全报告保留18–20及56–58页横向表格，其余为竖向。

## Extracted Pages

最终冻结PDF共139页。第93–95页为修订的角统计/宽度几何对比；第96页给出真实delta密度定义，第97–99页为其三模式对比；第104页声明文献比较边界，第105–107页绘制全部30个文献模型。其余图页通过案例ID及`caption_and_inventory_audit.json:inventory`逐项定位，原始图注输入与保存密度另以O/N/L案例ID回链。

## Key Results

| ID | claim_kind | evidence_level | locator | 结论与边界 |
| --- | --- | --- | --- | --- |
| FIG26-1 | software-audit | direct | `evidence/panel_data_audit.json` | 90张四联图的保存数组、重建PDF光栅样本和矢量路径全部一致；无反演重跑 |
| FIG26-2 | model-result | direct | `evidence/original_90_marginals_audit.json`、`delta_density_audit.json` | 原90套角/宽度边缘及另90套delta边缘独立积分核验；区间质量0.68、分位数16/50/84及局部峰位通过 |
| FIG26-3 | software-audit | direct | `evidence/comparison_data_audit.json` | 9张比较图逐条核对全部HDI分支、峰位、中位数、非对称ETI端点/端帽、真值或文献左右误差；实际PDF路径与重建一致 |
| FIG26-4 | software-audit | direct | `evidence/diagnostic_data_audit.json` | 4张诊断图的曲线独立积分及实际科学数据路径一致；旧分解图非数据刻度路径不要求重建字节相同 |
| FIG26-5 | software-audit | direct | `evidence/caption_and_inventory_audit.json`、`all_figure_qa.json`、`compile-6.log` | 全103图图注/顺序核查；90案例图注与输入和误差符号匹配；字体/碰撞零失败，最终编译无未定义引用或超宽盒 |
| FIG26-6 | model-result | direct | `evidence/delta_density_statistics.json:O01/N01` | O01的tan角mode为+6.2432，而delta密度mode约−0.48127；N01的tan角mode约−11.9087，而delta密度全局mode约−0.13876。峰位不具坐标不变性，不据此宣称真值恢复 |

## Method and Exact Locators

令ξ=arctan(δ)、u=σ/I。由保存的联合密度先对u积分，再乘坐标Jacobian，得到

\[
p_\delta(\delta)=\frac{\int f_{\xi,u}(\arctan\delta,u)\,du}{1+\delta^2}.
\]

自适应细化保留角坐标分段线性PDF的概率质量，在真实delta密度上重新评估HDI、mode、mean和std。`delta_density_statistics.json`按O/N/L案例存全部统计，`delta_marginal_<ID>.npz`存实际坐标与密度。ETI及中位数在单调变换下不变；90例中delta分位数与角分位数取tan的最大差异为3.7528624563520907e-7，属细化插值误差，HDI和mode则不具此不变性。

矩、分位数、HDI概率质量和峰位由独立两点Gaussian积分核查，容差2e-12。现有90张四联图保持原评估约定；新增6张delta图直接使用delta密度统计。

## Competing Interpretations and Limitations

旧、新delta有限域约为±572.96与±57.29；均值/标准差及边界结果依赖有限域。PDCO方向门也随几何组改变，不作单因素因果解释。文献混合比仅作比较，左右误差保留原报定义；164Yb约−21°仅画空心参考点，不补造未报误差。重复模型与读图敏感性不增加独立测量数。

本次核查证明图件与保存数据的对应和区间画法，不是对物理响应模型的独立正确性证明，也不是随机重复实验覆盖率验证。图注、图例和区间解释均由Agent自审，未记录人工审核事件。

## Artifact Locators

- `final_snapshot/main.pdf`：本次139页冻结报告；canonical仍为PDM/main.pdf。
- `final_snapshot/`：精确TeX、绘图程序、复现脚本及9张修订/新增比较PDF。
- `evidence/review-summary.json`：完整核验范围、页码和边界。
- `evidence/final-nine-pages.png`及六张`pages-*.png`：全页布局与比较图视觉核查记录。
- 数值输入身份沿用[[pdm-two-geometry-recovery-20261125-source]]，不改写其清单或输入。
