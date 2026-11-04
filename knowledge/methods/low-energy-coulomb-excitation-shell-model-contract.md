---
type: method
title: "低能库仑激发：壳模型、形状和实验设计合同"
aliases: [Rocchini Zielinska Coulomb excitation, low-energy Coulex shell-model contract]
method_type: "low-energy-coulomb-excitation"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "Nuclear Shell Model 70 Years article 7, article pp.175-192 / physical PDF pp.186-203 selected sections"
confidence: "high for reviewed Coulex formalism and observable boundaries"
tags: [coulomb-excitation, coulex, b-e2, quadrupole-moment, shape-coexistence, triaxiality, shell-model]
sources: [book-nuclear-shell-model-70-years]
---

# 低能库仑激发：壳模型、形状和实验设计合同

## Purpose

把低能库仑激发从“测 \(B(E2)\)”扩展成完整实验设计和矩阵元提取合同，连接
壳模型波函数、形状共存、三轴性、四极矩和相对 E2 矩阵元符号。

## Inputs and Assumptions

- 碰撞必须满足安全距离条件，使核力贡献足够小；
- 半经典 Alder–Winther 描述适用于重离子、低能和合适的 de Broglie 波长；
- 轻粒子或不满足半经典条件时，需要完整量子散射/耦合道处理；
- 输入包括束流能量、靶/束 \(Z,A\)、散射角、效率、符合门、寿命、已知分支和
  E2/M1 矩阵元；
- 多步激发、重取向效应和相对符号必须作为同一响应模型中的干涉项处理。

## What It Can Establish

### First-order and higher-order observables

弱激发一级近似下，激发截面主要与
\[
B(EL;I_i\to I_f)
\]
相关。低能库仑激发通常选择性增强低能集体 E2/E3 状态，并可测量：

- 约化跃迁几率；
- 激发态谱学四极矩 \(Q_s\)；
- 重取向效应；
- 多步激发中的相对 E2 矩阵元符号；
- 通过多个中间态构造的四极不变量。

### Safe distance and geometry

实验设计必须先检查最近接距离和核力污染。安全距离条件的核心思想是让碰撞表面
之间保留约数 fm 的间隔，使激发主要由已知电磁场驱动。重离子、低能和大角度门
可增强高阶效应，但也会增加多步路径和模型参数之间的相关性。

### Interference and relative signs

某些状态既可以由直接一级路径又可以由二级路径布居，激发概率具有
\[
P=\left|a^{(1)}+a^{(2)}\right|^2
\]
结构。交叉项包含未平方的矩阵元乘积，因此可携带相对符号信息。实验上需要：

- 选择足够敏感的角度/质量组合；
- 同时测量多个 \(\gamma\) 分支；
- 明确 E2 符号约定；
- 将已知寿命、分支比和 \(B(E2)\) 作为外部约束；
- 保留相对符号的等价变换和拟合协方差。

### Reorientation effect

重取向效应是同一激发态不同磁子态之间的二阶过程，截面修正与对角 E2 矩阵元、
即 \(Q_s\) 成正比。因为它不是 \(Q_s^2\)，其符号可以通过干涉进入实验观测。
散射角分布、不同靶/束组合和多步路径有助于区分重取向项与其它干涉项。

### Quadrupole invariants

Kumar–Cline 四极不变量把实验室 E2 矩阵元组合成内禀形状描述：
\[
\langle Q^2\rangle,\qquad
\langle Q^3\cos3\delta\rangle.
\]

最低阶不变量主要由平方项组成，对未观测中间态的敏感性相对较低；三阶不变量
包含三个 E2 矩阵元乘积，需要：

- 对角矩阵元；
- 所有相关跃迁的相对符号；
- 足够完整的中间态集合；
- 对未观测强度的收敛评估。

因此四极不变量可以对 \(\beta_2,\gamma\) 提供比单个 \(B(E2)\) 更稳健的约束，
但仍需检查求和收敛和实验缺失态。

## Experimental Design Mapping

```text
目标：绝对 B(E2)
  -> 轻粒子/前角度/抑制多步 -> 一级近似

目标：相对符号与 Q_s
  -> 重离子/后角度/多步路径 -> 干涉与重取向敏感

目标：形状不变量
  -> 多个中间态、对角矩阵元、寿命和符号合同 -> 求和规则收敛审计
```

对用户的在束实验设计，必须把 \(E_\gamma\) 谱、散射粒子、角度、效率、随机符合、
feeding 和目标厚度一起放进响应合同，不能只根据一张 \(\gamma\) 能级图提出形状结论。

## Case Studies

- \(^{42}\mathrm{Ca}\)：重取向和多步库仑激发同时约束 \(Q_s\)、弱分支和相对 E2
  符号；\(2_2^+\) 的大 \(B(E2;2_2^+\to0_2^+)\) 与不确定性反映低能
  superdeformed/triaxial 结构。LSSM 的多粒子–多空穴组态可以与这些矩阵元比较，
  但剩余的带间偏差仍提示构型混合未完全再现。
- Ge/Zn/N=50 区：\(\langle Q^2\rangle\) 与
  \(\langle Q^3\cos3\gamma\rangle\) 的同位素趋势可区分近球形、形状共存和三轴/
  \(\gamma\)-soft 倾向，但需要完整中间态求和。
- Zr/Sr/Mo：激发 \(0^+\)、\(Q_s\) 和四极不变量共同展示球形—变形共存及快速形状
  转变，单个 \(E(2^+)\) 不足以完成判定。
- Sn/Cd：低能库仑激发的 \(B(E2)\) 系统学、\(Q_s\) 和壳模型有效电荷共同约束
  \(Z=50\) 附近的壳演化、质子跨壳层激发和形状混合。
- \(^{130}\mathrm{Xe}\)、\(^{140}\mathrm{Sm}\)：多级激发和高自旋观测可同时访问
  带内矩阵元、对角矩阵元和三轴不变量，是把壳模型与集体转动比较的重质量区接口。

在 \(^{130}\mathrm{Xe}\) 和 \(^{140}\mathrm{Sm}\) 的案例中，低能库仑激发与大模型空间
壳模型共同给出：

- 地面态约 \(\beta_2\approx0.15,\ \gamma\approx30^\circ\) 的集体/三轴倾向；
- \(^{140}\mathrm{Sm}\) 的 \(Q_s(2_1^+)\) 与增强的 \(B(E2)\) 对形状判断的互补作用；
- shell-model 能谱和跃迁总体可以再现，但需要明显高于默认值的有效电荷；
- \(^{130}\mathrm{Xe}\) 相关 \(B(E2)\) 和四极不变量还与 \(0\nu\beta\beta\) 母核矩阵元
  计算的实验约束有关。

这说明“能谱再现良好”与“模型空间已经充分”可以同时不成立；有效电荷偏大提示
跨壳层极化和更大模型空间仍然重要。

## What It Cannot Establish Alone

- 单个 \(B(E2)\) 不能唯一确定 \(\beta_2,\gamma\)；
- \(Q_s\) 的一个符号不能单独确认刚性三轴或 \(\gamma\)-soft；
- 四极不变量需要完整性和相对符号，不能把缺失中间态当作零；
- 壳模型再现 \(B(E2)\) 不能单独证明波函数组态；
- 库仑激发的形状结果需要与寿命、能级、\(g\) 因子、半径和竞争模型交叉验证。

## Evidence and Locators

- article pp.175–178 / physical PDF pp.186–189：低能库仑激发、半经典条件、一级/多步、
  重取向效应；
- article pp.178–180 / physical PDF pp.189–191：四极不变量和矩阵元符号；
- article pp.180–192 / physical PDF pp.191–203：\(^{42}\mathrm{Ca}\)、Ge/Zn、Zr/Mo、
  Sn/Cd、\(^{130}\mathrm{Xe}\)/\(^{140}\mathrm{Sm}\) 形状与壳模型案例。

本轮完成文章形式主义和实验设计主线的有界核读，案例和全部公式仍需继续逐项核验。

## Sources

- [[book-nuclear-shell-model-70-years]]
- [[coulomb-excitation-and-kumar-invariants]]
- [[experimental-uncertainty-propagation-and-double-root-triage]]
- [[wu-experimental-methods-deadtime-hpge-rdm-contract]]
