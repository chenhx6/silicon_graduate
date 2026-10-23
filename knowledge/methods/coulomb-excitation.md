---
type: method
title: 库仑激发
aliases: [Coulomb excitation, radioactive-beam Coulomb excitation]
created: 2026-09-20
updated: 2026-10-23
status: ai-draft
review_status: unreviewed
method_type: electromagnetic-excitation
tags: [Coulomb-excitation, radioactive-beams, matrix-elements]
---

# 库仑激发（Coulomb Excitation）

## Purpose

通过低能重离子与靶核的电磁相互作用布居低激发态，并由 γ 产额/角度依赖反演 E1/E2/E3 等电磁矩阵元。

## Inputs and Assumptions

Beam energy below the dominant nuclear-interaction regime, target/projectile matrix elements, recoil/scattering-angle coverage, lifetimes/branching constraints and a validated Coulomb-excitation analysis such as GOSIA.

## Procedure

Measure γ rays in coincidence with scattered projectiles/recoils, separate angular ranges, correct efficiency/randoms/Doppler effects, and fit coupled-state matrix elements; use signed matrix-element networks to form rotational scalars; a single intrinsic-moment or shape parameter requires its stated geometry and shape convention.

## What It Can Establish

With sufficient angular coverage and independent normalization, it can determine relative/absolute electromagnetic matrix elements and transition probabilities, including E3 strengths.

## What It Cannot Establish Alone

It does not uniquely prove a rigid static shape, a single β3 value or an EDM enhancement without model comparison, parity-systematics and uncertainty/fit-correlation checks.

## Supporting Evidence

[[gaffney-2013-pear-shaped-rn-ra]] uses REX-ISOLDE radioactive beams, MINIBALL and GOSIA to extract E1/E2/E3 matrix elements for `220Rn` and `224Ra`.

[[alder-1956-coulomb-excitation-review]] is the historical foundation for the classical/quantum trajectory, higher-order, detector and normalization boundaries used in modern Coulomb-excitation analyses.

## Counter-evidence and Competing Interpretations

Fit correlations, target matrix-element assumptions, lifetime/branching inputs, contaminant beams and soft-vibrational versus static-octupole interpretations must be retained.

## Sources

- [[gaffney-2013-pear-shaped-rn-ra]]
- [[alder-1956-coulomb-excitation-review]]
- [[cline-1986-nuclear-shapes-coulomb-excitation]]

## Day20：四极不变量的完整性与解释

[[cline-1986-nuclear-shapes-coulomb-excitation]] CL86-D20-2–8来自本session实际原件阅读。多角度/多束流Z约束的是非线性耦合产额；波函数整体相位规范与闭合环干涉符号分开。原参数概率限、实验系统误差和核内形状涨落是不同对象，不能用一组对称独立误差替代全部原fit。

用完整电磁张量网络形成转动标量，并不要求先指定某一种转子Hamiltonian；但有限求和、算符对易以及电荷Q/δ到质量β/γ的映射各有边界。高阶宽度比低阶均值更敏感于缺失矩阵元；只保低频网络还需原文所说的模式分离/弱耦合条件。多种耦合的一致性是同源自检，不是独立重复实验或完备性普适证明。

原Cline Fig4与[[henderson-2020-quadrupole-invariant-convergence]] Eq27的归一字面不同，使用时须指明公式；有限六标量也不一般唯一决定完整角度分布（CL86-D20-R150-1）。原件/反例与数据范围见[[day20-quadrupole-collectivity-systematics-synthesis]]，不据此给现代具体实验补造CI或判定刚性。


### checkpoint151：公开SIGMA约定与原实验producer分开

[[gosia-2012-manual-sigma-invariants]] GM12-D20-1–9来自2012手册Chapter9全文及完整可得908行源码的实际阅读（手册其余章节仅指定段落，非310页通读）。p223以偶数阶根插值估计正幅度三/五阶矩，FINT443–455对应；INVR423–438使用这两个估计归一。故此可得实现既不等同HE20 Eq27分母，也不自动给Cline Fig4真实⟨Q³⟩。p224–226明确crude误差近似、单spin态零方差构造及有限网络的高阶系统误差；这补充了149–150的边界，而不是重建任何核的CI。

原AY23的版本/job/.smr/.err/6j与联合梯度未得；原文声称的逐元素相关误差仍保留。手册NST=-1免TAPE11与代码无条件open11有IO差异；main局部开方截零与SVAR大sentinel分开。Eq9.3正号与Eq9.10整数spin负号保literal，不补写统一相位。两个公开文件只在tmp、raw归档deferred；公开可访问不等于开放再分发许可。继续Day20原15:00窗口，不提前学分/发布。


### checkpoint152：公开代码可运行控制核验

使用官方可得 `sigma.f` 在声明双轴对称转子控制（Q=1与2，delta=0）上运行证实，FINT 奇次矩插值将正幅度三阶矩系统性低估（4.4458 vs 4.5），导致提取的 cos(3delta) = 1.0122 > 1 及表观负方差 -0.0245，被代码强制截零为 0.0000。此控制确立：形状宽度计算中的“零方差”可源于插值函数与截零规则，不能作为实验测定形状刚性的排他性证据（[[gosia-2012-manual-sigma-invariants]] GM12-D20-10）。
