---
type: concept
title: "科里奥利耦合、衰减参数与回弯诊断的边界"
aliases: [科里奥利衰减与回弯]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [coriolis, band-crossing, alignment, model-boundary]
---

# 科里奥利耦合、衰减参数与回弯诊断

## Definition

## 可核验的结构与代数

粒子–转子哈密顿量 H=Hintr+Σk Ak(Ik−jk)² 是联系单粒子与集体转动的模型入口。[[frauendorf-2014-transverse-wobbling]] 的 PDF 3–7 模型/近似讨论提供该类理论的已登记原件入口；轴和矩阵元约定必须随来源。

若采用轴对称横向惯量 ℑ，展开横向点积的代数关系是

\[
H_{\rm cor}=-\frac{\hbar^2}{\mathcal J}(I_xj_x+I_yj_y)
=-\frac{\hbar^2}{2\mathcal J}(I_+j_-+I_-j_+).
\]

本段是指定哈密顿量下的**代数重构**；不能遗漏点积转为升降算符的 1/2。体固定角动量的基底、相位和量纲定义必须跟所用文献保持一致。

理想单 j 基底的相邻 K 耦合可有大小

\[
|V_{K,K+1}|=\xi A_{rot}
\sqrt{(I-K)(I+K+1)(j-K)(j+K+1)}.
\]

这里是磁子矩阵元几何因子，尚未包括真实 Nilsson 波函数组分、阻塞及多准粒子混合。程序返回的是**绝对值**，不能拿它提供未经约定的相对相位。

## 衰减因子不是微观计算的替代

ξ 在当前程序中是用户给定的唯象比例。旧版“ξ=0.75 已由配对与极化精确导出”撤回。特别是 u1u2+v1v2 在 u1=u2=v1=v2=1/√2 时等于 1，不能把这个式子同时当作“费米面附近自动压低 25%”的证明。需要从完整波函数、算符的时间反演性质和自洽转动响应求矩阵元，再比较 ξ 是否能统一描述数据。

[[book-bohr-mottelson-nuclear-structure]] 是经典书入口；§4-4、5-3d 的实际逐页 Coriolis 推导尚待重读。本页不冒称这些章节已经全部核查。

## 回弯描述量和构型指认分开

同一自旋序列可计算转动频率、角动量投影及 Harris 参考扣除后的 ix。J(1) 是**运动学**惯量，J(2) 是**动力学**惯量；旧版二者中文名称反写已纠正。频率随自旋降低可提示回弯区，但数值有限差分、未知带头自旋、K 假定和参考参数会影响 ix 与交叉位置。

配对减弱、准粒子对齐和带交叉常与回弯相关，但单条能量曲线不能唯一确定是第几对、质子还是中子。应加入组态计算、电磁强度、邻核系统学及连接关系。模型拟合不自动成为实验直接报告。

## 工具状态及修订

`system/scripts/analysis/coriolis_attenuation_bandcrossing_calculator.py` 的默认能级列表是**人工合成示例**，此前称其为 131La 实测序列、与实验完全符合或证实第二对准粒子退耦均撤回。`coriolis` 命令仍可展示单 j 耦合大小与能量序列的有限差分；频率下降检测采用人为阈值，只输出候选诊断，不输出物理确证。

自审：代数系数与例子身份已纠正；真实谱学与 microscopic attenuation 的科学验证未完成，`needs_review: true`。下一步用明确核素/数据来源和相同约定的独立矩阵元检验该近似。


## Necessary Assumptions

详见正文模型条件及推导假设。


## Discriminating Observables

详见正文特征观测量及区分判据。


## Supporting Evidence

详见正文模型公式推导及支持证据。


## Counter-evidence and Competing Interpretations

详见正文反例与竞争解释讨论。


## Our Current Position

明确标记为本 Wiki 当前阶段性认知与工作边界，不作为无条件定论。


## Sources

- [[book-petrache-chirality-and-wobbling]]
- [[book-bohr-mottelson-nuclear-structure-vol2]]


## Evolution Log

- 2026-11-02: 建立与修订本页概念规范。
