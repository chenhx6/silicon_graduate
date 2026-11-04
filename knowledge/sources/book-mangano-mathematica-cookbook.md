---
type: source
title: "Sal Mangano 2010 - Mathematica Cookbook"
aliases: [Mangano Mathematica Cookbook, Mathematica Cookbook]
created: 2026-11-04
updated: 2026-11-04
status: ai-draft
review_status: unreviewed
source_type: programming-cookbook
reading_depth: skimmed
title_original: "Mathematica Cookbook"
authors: [Sal Mangano]
publisher: "O'Reilly Media"
year: 2010
pages: "827"
isbn: "978-0-596-52099-1"
canonical_source: "Sal Mangano, Mathematica Cookbook, O'Reilly Media (2010)"
library_file: "raw/books/Mathematica Cookbook.pdf"
raw_file: "raw/books/Mathematica Cookbook.pdf"
raw_sha256: "e0db550c74888adf211725140f3c8549cdfc85aff79f279b1eeb1eb00de2a37d"
nuclei: []
reactions: []
experiments: []
models: []
methods: [numerical-analysis, functional-programming, statistics, scientific-computing, parallel-computing, software-testing]
tags: [books, mathematica, cookbook, numerical-analysis, statistics, visualization, python-bridge]
---

# Sal Mangano - Mathematica Cookbook

## Bibliographic Record

本地文件为 Mathematica 7 时代的 O'Reilly 实用手册，共 827 个物理 PDF 页面。全书按 recipe 组织，重点覆盖数值计算、函数式编程、数据结构、规则、可视化、统计、科学工程、并行、接口以及调试和测试。

## Scope and Reading Depth

本轮核对了版权、前言和完整章节目录（PDF pp. 5–26、27–827），并选读与未来 Python 核谱学工作最相关的章节开头和方法段：

- Ch. 1 `Numerics`：精确数、近似数、机器精度、区间和数值稳定性（PDF pp. 27–48）；
- Ch. 2 `Functional Programming`：高阶函数、纯函数和减少副作用（PDF pp. 49–110）；
- Ch. 3 `Data Structures`：列表、矩阵、张量、集合和图结构（PDF pp. 111–170）；
- Ch. 4 `Patterns and Rule-Based Programming`：模式匹配、规则替换和符号处理（PDF pp. 171–206）；
- Ch. 7 `Three-Dimensional Plots and Graphics`：符号化图形和可组合可视化（PDF pp. 301–354）；
- Ch. 11 `Calculus: Continuous and Discrete`：极限、级数、微积分、微分方程和离散算法（PDF pp. 451–480）；
- Ch. 12 `Statistics and Data Analysis`：统计量、分布、随机数和数据分析入口（PDF pp. 481–530）；
- Ch. 13 `Science and Engineering`：刚体动力学、数据源、`DSolve`/`NDSolve` 和科学建模组织（PDF pp. 531–574）；
- Ch. 16 `Parallel Mathematica`：主从 kernel、变量分发、副作用和竞态条件（PDF pp. 667–714）；
- Ch. 19 `Debugging and Testing`：增量调试、可重复单元测试和 MUnit 思想（PDF pp. 767–802）。

本卡是理解级、按主题选读记录，不宣称对 827 页每道 recipe 逐条复现。

## Summary

本书以 recipe 形式覆盖 Mathematica 的数值、函数式编程、数据结构、符号规则、科学建模、统计、并行和测试。对本 Wiki 的主要贡献是把 Mathematica 的快速原型能力转译为 Python 的显式数据结构、统计合同和回归测试。

## Key Results

| ID | Claim | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| MANGANO-1 | 精确数、机器数和高精度数具有不同的误差和性能行为，科学计算必须显式管理数值精度。 | numerical-principle | direct | PDF pp. 27–48 | false |
| MANGANO-2 | 函数式编程、结构化数据操作和符号图形是 Mathematica 科学工作流的核心组织方式。 | programming-principle | direct | PDF pp. 49–206, 301–354 | false |
| MANGANO-3 | 并行计算应先通过单 kernel 验证，并显式处理定义分发、副作用和竞态条件。 | reproducibility-principle | direct | PDF pp. 667–714 | false |
| MANGANO-4 | 可重复单元测试比只在 notebook 中交互试算更适合长期维护的科学代码。 | software-testing | direct | PDF pp. 767–802 | false |

## Transferable Knowledge

1. **数值类型必须显式区分**：精确算术、机器浮点、高精度浮点、区间和复数的行为不同。Python 研究代码应明确使用 `float64`、`Decimal`、`mpmath` 或区间/蒙特卡罗传播，并记录精度与舍入假设。
2. **科学代码应先组织模型，再调用求解器**：Ch. 13 的科学工程 recipes 强调变量、参数、方程、边界条件和可视化的组织。迁移到核物理时，反应运动学、PES、寿命线形和效率曲线应分层保存输入、模型、拟合和诊断。
3. **统计 recipe 不替代统计理论**：Mathematica 能快速调用均值、分位数、随机分布、拟合和绘图，但核实验的 Poisson 似然、协方差、覆盖率、边界和模型比较仍由朱永生/Bonamente 方法合同约束。
4. **符号图形便于构造可审查图**：图形对象可组合、变换和添加标注。Python 中对应 `matplotlib`/`plotly` 的显式 figure 构造；出版图必须保留单位、误差、数据来源和版本。
5. **并行化必须先单核验证**：书中明确提醒先在单 kernel 测试，再分发定义；副作用、文件写入和共享状态会造成竞态。Python 中对应先完成确定性单进程基准，再用 multiprocessing/joblib/Dask，并固定随机流和输入分片。
6. **测试是科学复现的一部分**：把 recipe 改造成 Python 时，应为极限值、单位、零计数、边界、随机种子、对称性和已知解析解写回归测试。交互式 notebook 只能作为探索界面，不能作为唯一证据链。

## Nuclear-Physics Use

- 为 `system/scripts/analysis/` 的数值精度、绘图、并行和测试约定提供迁移参考；
- 为 HPGe 效率、PES、寿命反演、角分布和蒙特卡罗脚本提供结构化 recipe 思路；
- 将 Mathematica 的快速符号探索与 Python 的正式计算分开：前者用于猜想和代数核验，后者用于长期可复现分析；
- 与 `zhu-experimental-statistics`、`nuclear-experimental-methods` 和 `phys-model` 配套使用。

## Evidence Boundary

本书面向 Mathematica 7，内置函数、并行接口、数据源和性能结论具有版本依赖性。它提供编程和工作流启发，不构成当前 Mathematica API 规范，也不替代 Python 包文档或核实验统计合同。

## Competing Interpretations and Limitations

- 本书以 Mathematica 7 为背景，内置函数、数据源和并行接口不能直接当作当前版本规范。
- recipe 中的示例数据多为演示或合成数据，不能作为实验事实。
- Mathematica 的统计函数调用不能替代核实验中的 Poisson 似然、协方差、覆盖率和模型比较审计。

## Extracted Pages

- PDF pp. 5–26：前言、结构和使用约定；
- PDF pp. 27–206：数值、函数式编程、数据结构和规则；
- PDF pp. 451–574：微积分、统计和科学工程；
- PDF pp. 667–714：并行 Mathematica；
- PDF pp. 767–802：调试和测试。

## Sources

- `raw/books/Mathematica Cookbook.pdf`, PDF pp. 5–26, 27–48, 49–206, 301–354, 451–574, 667–714, 767–802.
- [[mathematica-to-python-nuclear-analysis-bridge]]
