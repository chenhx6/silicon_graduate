---
type: source
title: "Chen et al. 2026 manuscript - A probability-density mapping method for extracting gamma-ray mixing ratios without preset spin alignment"
aliases: [Chen 2026 PDM, P-ADO manuscript, probability-density mapping mixing ratios]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: manuscript-method
reading_depth: deep-read
title_original: "A probability-density mapping method for extracting $\gamma$-ray mixing ratios without preset spin alignment"
authors: [Hong-Xing Chen, Yun-Hua Qiang, Song Guo, Xiao-Hong Zhou]
year: 2026
raw_file: "raw/writing/pado/20260722.pdf"
raw_sha256: "f19b52b872432f6d615dae9350eef42d12cff27cfb621a041f09720699f74421"
page_count: 15
canonical_source: "raw/writing/pado/20260722.pdf"
citation_key: "Chen_PDM_2026_manuscript"
code_dir: "raw/writing/pado/Upload/p_ado"
nuclei: [61Ni, 135Pr, 187Au]
observables: [R_ADO, linear-polarization, mixing-ratio, spin-alignment]
methods: [probability-density-mapping, Jacobian-transform, marginalization]
tags: [PDM, P-ADO, mixing-ratio, alignment, angular-distribution, polarization]
---

# A probability-density mapping method for extracting gamma-ray mixing ratios without preset spin alignment

## Bibliographic Record

- 本地原件：`raw/writing/pado/20260722.pdf`，15 physical PDF pages，SHA-256 `f19b52b872432f6d615dae9350eef42d12cff27cfb621a041f09720699f74421`。
- 方法手稿与其可运行代码分开保存：正文为 `raw/writing/pado/nst_sample.tex`，代码目录为 `raw/writing/pado/Upload/p_ado`。本页记录的是用户提供的未发表方法稿，不把稿件结果升级为独立实验事实。
- 手稿摘要将 PDM 描述为 practical spectroscopic tool；方法适用性仍受响应函数、误差模型、对齐域和校准合同限制。

## Scope and Reading Depth

- 精读主线：磁子布居与 $\sigma/I$（physical PDF pp. 2–3, Eq. 1）、$R_{\rm ADO}$ 与 $P$ 响应（pp. 3–5, Eqs. 4–8）、$\xi=\arctan\delta$ 参数化与映射曲面（pp. 5–7, Eqs. 9–11）、雅可比密度变换与对齐边缘化（pp. 7–9, Eqs. 12–14）、$^{187}$Au 示例和八条基准表（pp. 9–12, Table 1）、一维误差模型（p. 15）。
- 代码入口：`raw/writing/pado/Upload/p_ado/main.py`；响应计算在 `p_ado/physics/pado.py`，雅可比与网格实现位于 `p_ado/compute/`，误差密度模型位于 `p_ado/pdf/`。

## Summary

本页记录用户提供的未发表PDM方法手稿及其代码合同。PDM输出是声明响应、误差、对齐和校准假设下的条件统计结果，不替代独立寿命或结构测量。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH26-PDM-01 | 手稿以离散高斯磁子布居 $P_m\propto\exp[-m^2/(2\sigma^2)]$ 表示对齐态，并以 $\sigma/I$ 作为响应参数。 | method-definition | direct-original | physical PDF p. 3 Eq. 1 | true |
| CH26-PDM-02 | 手稿定义 $R_{\rm ADO}$ 为指定小/大角度探测组强度比，并以角分布与线偏振响应共同约束 $\delta$ 和 $\sigma/I$。 | observable-contract | direct-original | physical PDF pp. 3–5 Eqs. 4–8 | true |
| CH26-PDM-03 | 手稿以 $\xi=\arctan\delta$ 紧致化混合比轴，并在局部可逆处用 $f_{\mathcal P}=f_{\mathcal O}\lvert J\rvert$ 作面积测度变换。 | method-equation | direct-original | physical PDF pp. 5–8 Eqs. 9–13 | true |
| CH26-PDM-04 | 手稿对 $\sigma/I$ 进行显式权重边缘化，权重与积分上下界是方法输入；独立高斯观测误差是其基准示例假设。 | method-assumption | direct-original | physical PDF pp. 8–9 Eq. 14; p. 10 | true |
| CH26-PDM-05 | 手稿的八条基准比较覆盖 $^{61}$Ni、$^{187}$Au、$^{135}$Pr；作者报告多数提取区间包含文献值，但部分 $^{61}$Ni 区间只有边界或部分重叠，比较不是独立 coverage 检验。 | result-with-scope | direct-original | physical PDF pp. 10–12 Table 1 and discussion | true |
| CH26-PDM-06 | 手稿将 $^{187}$Au 示例的结果解释为在声明的观测 PDF、响应网格和对齐域下的小负、M1 主导后验；这不是无模型带身份证明。 | conditional-interpretation | direct-original | physical PDF pp. 9–11, Figs. 3–4 | true |
| CH26-PDM-07 | 公开代码、原始输入和依赖环境构成复现合同，但实际运行结果仍依赖代码版本、网格、响应函数、输入 PDF 和对齐权重。 | reproducibility-boundary | direct-plus-code | raw/writing/pado/Upload/README.md; p_ado/main.py | true |

## Competing Interpretations and Limitations

- 手稿未提供所有实验输入的完整计数协方差；正文基准例采用独立一维误差密度作为近似，因此不能把输出区间称为无条件客观 coverage。
- $\xi$ 映射和雅可比只描述给定响应合同下的参数空间推断；Outside 折叠的分支保留不等于结构模型已被排他裁决。
- PDM 结果不能替代态寿命、完整分支比、ICC、静态矩、组态映射或独立结构 holdout；这些量缺失时结论必须降级。
- 本页不把手稿的基准结果或其代码输出当作新的实验测量，也不清除任何 `needs_review` 状态。

## Reproducibility checks

## Reproducibility checks

- 2026-10-28：仓库测试集未能启动，当前环境没有 `pytest`；`unittest discover` 也因测试依赖 `pytest`、且未设置包路径而失败。
- 设置 `PYTHONPATH=raw/writing/pado/Upload` 后，`python3 -m compileall -q raw/writing/pado/Upload/p_ado` 通过，说明代码树可编译，但不替代依赖完整的数值测试。
- 设置 `PYTHONPATH=raw/writing/pado/Upload` 后，独立检查 `theta_deg_to_delta` 与 `delta_to_theta_deg` 在 $\pm30^\circ$、$\pm60^\circ$ 和 $0^\circ$ 网格上的往返误差处于浮点舍入范围；依赖 `sympy` 的完整响应/雅可比测试仍未运行。
- 这些是运行环境边界，不把未运行的测试写成通过，也不改变方法稿的 `needs_review` 状态。

## Extracted Pages

- [[pado-probability-density-mapping-mixing-ratios]]
- [[135pr-mixing-branch-input-contract]]
- [[chirality-shape-coexistence-companion-matrix]]
