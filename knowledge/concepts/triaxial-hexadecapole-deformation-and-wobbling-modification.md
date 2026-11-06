---
type: concept
title: "Triaxial nuclear hexadecapole (beta_4, gamma_4) deformation perturbation, principal moments of inertia renormalization and wobbling frequency modification"
aliases: [triaxial-hexadecapole-deformation, beta4-wobbling-modification, hexadecapole-moi-renormalization, high-spin-hexadecapole, 163lu-beta4]
created: 2026-11-04
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
tags: [triaxiality, hexadecapole-deformation, beta4, wobbling-motion, moments-of-inertia, 163lu, 135pr]
---

# 十六极形变与惯量：表面多极展开不决定摆动稳定性

## Definition

表面可按球谐函数展开为 \(R(\theta,\phi)=R_0c(\alpha)[1+\sum_{\lambda\mu}\alpha_{\lambda\mu}Y_{\lambda\mu}]\)。其中rank4分量描述十六极形变；有限形变下体积约束需要相应归一化因子。非轴rank4张量的参数化应单独声明，不能默认由一个普适的gamma4参数完备描述。

[[book-bohr-mottelson-nuclear-structure-vol2]] BM2-9（PDF161–162／printed139–140，Eq.4-190及邻文）支持电多极矩与表面分量的关系，其中可包含四极形变的二阶贡献。电荷矩展开本身不产生动力学惯量公式。质量分布、流动假设、配对和单粒子响应仍需另行建模。

## Necessary Assumptions

本地`triaxial_hexadecapole_deformation_wobbling_modifier.py`采用的

\[
\mathcal J_k=\mathcal J_k^{(0)}
[1+\kappa_4\beta_4\cos(\gamma-2\pi k/3)+\kappa_{44}\beta_4^2]
\]

是指定参数化，不能归为已从BM-II、流体力学或微观推转普遍导出的结果。默认系数1.85和0.60只具有该程序输入的身份。实现还对乘法因子设置下限；大修正时不能把它当作受控微扰。

该函数将`beta2`记录为元数据，实际基准惯量由`J_base`和gamma确定，未独立使用beta2建立质量分布。实现折叠gamma并采用指定轴排列；跨轴／符号约定迁移需重新核对。

无附加粒子自由度的刚性转子在最大惯量轴附近的小振幅频率可写为 \(\hbar\omega_w=\hbar\omega_{\rm rot}\sqrt{(\mathcal J_m-\mathcal J_s)(\mathcal J_m-\mathcal J_l)/(\mathcal J_s\mathcal J_l)}\)。本工具把该类表达式与指定对齐量组合使用，不求完整粒子–转子本征态，不能据此识别横向摆动或TiP。

## Discriminating Observables

实际核素需要独立的形变／电多极矩约束、转动惯量和组态身份，并用绝对E2/M1、静态矩与相关能带资料检验。仅给定beta4符号或计算出频移，不能判定集体模式及稳定性。

## Supporting Evidence

旧页把beta4正负分别等同于稳定TW或加速TiP的普适判据，并列出核素频移作为benchmark validation；这些归属和物理验证身份已撤回。修正方向取决于三个轴的相对响应及所用动力学，不能只看一个形变系数的符号。

```bash
python3 system/scripts/analysis/nuclear_analyzer.py hexwob --preset pure_quadrupole_limit
```

此零beta4输入只应恢复程序自己的基准惯量及零频移。它是实现极限检查，不证明程序已复现完整BM模型。带核素名称的旧预设均按演示参数集解释。

## Counter-evidence and Competing Interpretations

同样的beta4可以在不同质量密度、惯量或配对模型下产生不同响应。电荷Q4也不直接等于表面alpha40。实频率只表明所代入近似的局部振荡条件，不能确认完整体系的模式或量子稳定性。

## Our Current Position

保留表面多极与条件参数化的区别，撤回未经建立的普适系数、符号判据及核素结果。相关代码保留演示接口，其输出需携带模型边界。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：BM2-9；BM2-1–4给出刚性转子近似及适用域。
- `system/scripts/analysis/triaxial_hexadecapole_deformation_wobbling_modifier.py`：演示参数化和输出，不是实验来源。
