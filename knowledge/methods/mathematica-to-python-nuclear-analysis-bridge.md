---
type: method
title: "Mathematica 编程思想到 Python 核实验分析的迁移合同"
aliases: [Mathematica-Python bridge, Mathematica to Python nuclear analysis]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
method_type: software-method-contract
tags: [mathematica, python, numerical-analysis, reproducibility, nuclear-spectroscopy]
topics: [python, scientific-computing, software-design, reproducible-analysis]
sources: [book-shifrin-mathematica-programming-advanced-introduction, book-mangano-mathematica-cookbook, book-zhu-probability-statistics-in-physics]
---

# Mathematica 编程思想到 Python 核实验分析的迁移合同

## Purpose

本合同吸收 Shifrin《Mathematica Programming: An Advanced Introduction》和 Mangano《Mathematica Cookbook》中对表达式、规则、函数式编程、数值精度、科学建模、并行和测试的可迁移思想，约束未来核结构与在束 $\gamma$ 谱学代码统一使用 Python 的实现方式。

## Inputs and Assumptions

1. Mathematica books are used as programming-method references; formal numerical results are implemented and tested in Python.
2. Physical inputs carry units, calibration metadata, covariance or uncertainty information, and source locators where applicable.
3. Any parallel implementation has a deterministic single-process reference and an explicit random-number policy.
4. Version-specific Mathematica behavior is not assumed to transfer to current software without executable verification.

## What It Can Establish

1. A reproducible separation between data schema, physical model, statistical inference, numerical solver and visualization.
2. A migration map from symbolic/procedural prototypes to tested Python functions and batch analysis pipelines.
3. A minimum software contract for precision, boundaries, random seeds, side effects, parallel execution and regression tests.

## What It Cannot Establish Alone

1. It cannot validate a nuclear-structure interpretation, detector calibration or experimental claim.
2. It cannot establish that a Mathematica recipe or historical timing comparison remains valid for current Mathematica, Python or library versions.
3. It cannot replace the statistical contracts for covariance, Poisson likelihood, coverage, profile errors or model comparison.

## Translation Table

| Mathematica 思想 | Python 研究实现 | 核谱学用途 |
|---|---|---|
| 表达式树、`Head`、模式 | `dataclass`、类型检查、显式解析器、结构化字典 | 能级/跃迁身份和输入 schema |
| `Map`/`Fold`/`Nest` | NumPy 向量化、生成器、`functools.reduce`、显式迭代 | 事件流、效率链、蒙特卡罗和迭代求解 |
| 规则替换 | 纯变换函数、映射表、模式分派 | ENSDF/能级纲图标准化、单位和符号约定 |
| 精确数与机器数区分 | `int`/`float64`/`Decimal`/`mpmath` | 公式核验、极小概率、寿命和高次幂误差 |
| 符号图形 | Matplotlib/Plotly figure 对象 | 角分布、PES、能级图和诊断图 |
| 主从 kernel | 进程池、Dask/joblib、分片随机流 | 大样本 Monte Carlo、效率和线形扫描 |
| MUnit/交互调试 | `unittest`、CLI selftest、固定 seed 和日志 | 物理极限、边界和回归验证 |

## Required Workflow

1. 用结构化输入对象保存单位、校准版本、协方差、随机种子和来源 locator；
2. 将物理模型、数值求解、统计推断和绘图拆为纯函数或明确状态对象；
3. 先用小数据、解析极限和单进程运行验证，再扩大样本或并行化；
4. 对零计数、物理边界、奇异混合比、共线矩阵和非正定协方差显式报错；
5. 保存中间量和诊断，而不是只输出最终峰面积、寿命或模式标签；
6. 任何 Mathematica 原型迁移后，都用独立 Python 实现或解析解交叉验证，不能以“两个软件给出相同数字”作为独立证据。

## Nuclear Analysis Mapping

- `nuclear_analyzer.py`：将每个子命令保持为可复现的输入—输出函数；
- `experimental_statistics_minimizer.py`：保留 profile likelihood、边界和非对称误差；
- `monte_carlo_integrator.py`：固定随机流，区分 proposal、权重和有效样本数；
- HPGe 效率、DSAM/RDM、DCO/偏振和三轴 PES：将 detector response、物理模型和统计似然分层；
- 图形输出：每幅图写入数据来源、单位、参数版本和误差定义。

## What This Contract Cannot Establish

- Mathematica recipe 的旧版本性能不能证明 Python 实现更快；
- 符号化简或数值拟合输出不能单独证明核结构模式；
- 并行结果一致不能替代统计覆盖率、物理边界和独立数据验证；
- 书中示例数据多为演示或合成数据，不能当作实验事实。

## Sources

- [[book-shifrin-mathematica-programming-advanced-introduction]]
- [[book-mangano-mathematica-cookbook]]
- [[zhu-advanced-statistics-and-parameter-estimation-contract]]
- [[book-wu-nuclear-experiment-methods]]
