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
- 用户目录包含不同版本的未发表手稿，不能将当前TeX当作15页PDF的逐字正文；代码目录为 `raw/writing/pado/Upload/p_ado`。方法计算不作为独立实验。

|版本|实际文件|physical页数|SHA-256|
|---|---|---|---|
|本页主原件|raw/writing/pado/20260722.pdf|15|f19b52b872432f6d615dae9350eef42d12cff27cfb621a041f09720699f74421|
|另一PDF版本|raw/writing/pado/nst_sample.pdf|11|9a558e7d51c5d87c1ce040d9dab9b39dbfa26071dae4dabd987cee0bb8eddff9|
|当前TeX|raw/writing/pado/nst_sample.tex|不适用|2c9ee0b7260d4b272465c875f09d84badd9e511727176816141866887a8619c2|
- 手稿摘要将 PDM 描述为 practical spectroscopic tool；方法适用性仍受响应函数、误差模型、对齐域和校准合同限制。

## Scope and Reading Depth

- 主原件覆盖：布居Eq1/PDF2；角响应Eqs4–8/PDF3及偏振响应Eq9/PDF4；角坐标PDF4–5 §III.A、映射Eq10/PDF5、Jacobian Eq11/PDF6；独立观测PDF与变换Eqs12–13/PDF7；边缘化Eq14/PDF8；Au示例PDF9 Figs6–7及PDF10 Fig8；Table1/PDF11；Appendix A标题在PDF12，误差密度公式在PDF13。
- checkpoint009定向版本核对：11页PDF的相应密度变换/边缘化为PDF5 Eq11/PDF6 Eq12，Table1在PDF7；当前TeX的参数密度、边缘化与HDI段仅按其自身标签引用。没有从文件名或mtime推定唯一最终版本，也未重新编译TeX。
- 代码入口：`raw/writing/pado/Upload/p_ado/main.py`；响应计算在 `p_ado/physics/pado.py`，雅可比与网格实现位于 `p_ado/compute/`，误差密度模型位于 `p_ado/pdf/`。

## Summary

本页记录用户提供的未发表PDM方法手稿及其代码合同。PDM输出是声明响应、误差、对齐和校准假设下的条件统计结果，不替代独立寿命或结构测量。

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH26-PDM-01 | 手稿以离散高斯磁子布居 $P_m\propto\exp[-m^2/(2\sigma^2)]$ 表示对齐态，并以 $\sigma/I$ 作为响应参数。 | method-definition | direct-original | 20260722.pdf physical PDF2 Eq1 | true |
| CH26-PDM-02 | 手稿定义 $R_{\rm ADO}$ 为指定小/大角度探测组强度比，并以角分布与线偏振响应共同约束 $\delta$ 和 $\sigma/I$。 | observable-contract | direct-original | 20260722.pdf physical PDF3 Eqs4–8 | true |
| CH26-PDM-03 | 手稿以 $\xi=\arctan\delta$ 参数化混合比，并在局部可逆分支使用 $f_{\mathcal P}=f_{\mathcal O}\lvert J\rvert$；全局折叠时逐分支计算后归一。 | method-equation | direct-original | 20260722.pdf physical PDF7 Eq13 | true |
| CH26-PDM-04 | 手稿对 $\sigma/I$ 作权重边缘化；权重及积分域是输入。观测误差采用独立近似，对称项用Gaussian，非对称项用skew-normal或split-normal。 | method-assumption | direct-original | 20260722.pdf physical PDF8 Eq14 | true |
| CH26-PDM-05 | 八条基准覆盖61Ni、187Au、135Pr；多数区间包含文献值，部分61Ni只有边界或部分重叠。这不是独立coverage检验，HDI在xi中求取后映至delta。 | result-with-scope | direct-original | 20260722.pdf physical PDF11 Table1 | true |
| CH26-PDM-06 | Au示例给条件小负、M1主导混合比密度，不是无模型带身份证明。 | conditional-interpretation | direct-original | 20260722.pdf physical PDF9 Figs6–7 | true |
| CH26-PDM-07 | 提供的代码、原始输入和依赖环境构成复现合同，但实际运行结果仍依赖代码版本、网格、响应函数、输入 PDF 和对齐权重；测试通过不自动复现稿件基准表。 | reproducibility-boundary | direct-plus-code | raw/writing/pado/Upload/p_ado/main.py | true |
| CH26-PDM-08 | 15页版Au对齐Gaussian宽度正文.02、Fig8 caption .1不一致；当前TeX写.1，不能据此认证旧版actual输入。 | version-and-input-conflict | direct-original-version-comparison | 20260722.pdf physical PDF10 Fig8 | true |
| CH26-PDM-09 | 原15页版PDF6称除各向同性点外处处局部可逆；当前TeX改为J非零条件。采用逆函数定理时须逐点检查J，不能沿用旧版普遍断言。 | version-and-identifiability-boundary | direct-original-plus-mathematical-audit | 20260722.pdf physical PDF6 Eq11 | true |

## Competing Interpretations and Limitations

- 手稿未提供所有实验输入的完整计数协方差；正文基准例采用独立一维误差密度作为近似，因此不能把输出区间称为无条件客观 coverage。
- $\xi$ 映射和雅可比只描述给定响应合同下的参数空间推断；Outside 折叠的分支保留不等于结构模型已被排他裁决。
- PDM 结果不能替代态寿命、完整分支比、ICC、静态矩、组态映射或独立结构 holdout；这些量缺失时结论必须降级。
- 本页不把手稿的基准结果或其代码输出当作新的实验测量，也不清除任何 `needs_review` 状态。

## Reproducibility checks

- 2026-10-28：仓库测试集未能启动，当前环境没有 `pytest`；`unittest discover` 也因测试依赖 `pytest`、且未设置包路径而失败。
- 设置 `PYTHONPATH=raw/writing/pado/Upload` 后，`python3 -m compileall -q raw/writing/pado/Upload/p_ado` 通过，说明代码树可编译，但不替代依赖完整的数值测试。
- 设置 `PYTHONPATH=raw/writing/pado/Upload` 后，独立检查 `theta_deg_to_delta` 与 `delta_to_theta_deg` 在 $\pm30^\circ$、$\pm60^\circ$ 和 $0^\circ$ 网格上的往返误差处于浮点舍入范围；依赖 `sympy` 的完整响应/雅可比测试仍未运行。
- 这些是运行环境边界，不把未运行的测试写成通过，也不改变方法稿的 `needs_review` 状态。
- checkpoint009续接：在仓库`tmp/`安装pytest/sympy，使用原运行Python的numpy/scipy并显式设置包路径后，现有测试集实际 **24 passed in 15.05s，exit0**。命令启用`PYTHONDONTWRITEBYTECODE=1`、关闭pytest缓存、临时目录置于tmp，未修改raw源码。此前“缺依赖”是历史失败记录，当前测试阻塞已解除。
- 24项覆盖响应代数/向量化、误差PDF、Jacobian、导出与报告等代码行为；未完整重放两版稿件的八条基准及HDI、实际探测器响应或输入Cov，不能将测试通过写成稿件数值/物理模式认证。环境和代码哈希见本run `pado-tests-009.json`。

## Extracted Pages

- [[pado-probability-density-mapping-mixing-ratios]]
- [[135pr-mixing-branch-input-contract]]
- [[chirality-shape-coexistence-companion-matrix]]
