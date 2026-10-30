---
type: research-note
title: "剪刀不对称度、核芯响应与相互作用归一：固定阈值的条件反例"
aliases: [Shears asymmetry core response, Delta j threshold audit]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, roy-2011-cd110-systematics-antimagnetic, rather-2014-104pd-antimagnetic-arxiv-full]
created_from: Day27 user-authorized continued L3 research and conditional numerical analysis
promotion_target: ""
tags: [shears, magnetic-rotation, normalization, core-rotation, model-validity]
---

# 不能用固定不对称度替代角动量动力学

## Grounded Evidence

[[clark-2000-shears-mechanism]] 原 PDF pp.19–21、Eqs.(10)–(13)把有效能量展开为偶多极项，P2 系数对粒子—空穴为正。p.19 单独讨论核芯对总自旋的贡献；p.21 明确区分整体相互作用和每一对核子的相互作用强度。以下加入核芯惯性项的模型由本任务构造，不是该综述已发表的完整模型，也不是实验拟合。

旧 Day27 分类器直接把 `Delta_j <= 0.35` 和 `Delta/V_pn <= 3.5` 写成 viability 条件，没有解角极小、配对方程或恢复曲率。旧掩盖比又使用固定 A=160、Z=66、Qeff=0.25 eb。脚本路径为 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/workers/microscopic-inapplicability-solver/microscopic_inapplicability_solver.py`。它是被审计的历史工件，不是科学来源。

## Assumptions

检验一个较窄的问题：固定叶片的经典平面剪刀加正惯量核芯，是否必然在不对称度 0.35 发生失稳？

假定两个非零定长叶片 jp、jn，夹角 θ 在 [0,π/2]；核芯角动量平行于叶片合矢量。令 c=cosθ，叶片合量

\[
j(c)=\sqrt{j_p^2+j_n^2+2j_pj_n c},\qquad
E(I,c)=\frac{[I-j(c)]^2}{2\mathcal J_c}
       +V\frac{3c^2-1}{2}.
\]

角动量以 ℏ 为单位，Jc 以 ℏ²/MeV、V 以 MeV 表示；Jc、V 均为正。没有配对、组态交叉、三轴核芯的方向响应、量子反对称化或终止效应。该模型不能认证任何真实核素的 MR/AMR 指认。

## Provisional Reasoning

记 p=jp jn，有 j'=p/j、j''=−p²/j³。固定 I 的内点驻值满足

\[
I(c)=j(c)\left(1+\frac{3\mathcal J_c V}{p}c\right).
\]

对于这条 c≥0 支，

\[
E_{cc}=\frac{(j')^2-[I-j]j''}{\mathcal J_c}+3V>0.
\]

因此，在本模型的闭合支内，只要叶片非零、Jc/V 正且有限，就存在条件稳定的内点极小；公式中没有 Delta_j=0.35 奇点。这是对“由一般剪刀几何必然推出固定阈值”的反例，不是证明真实核不存在失稳。

令 S=jp+jn、d=|jp−jn|/S。垂直叶片闭合到同向所能增加的价角动量分数为

\[
\frac{\Delta j}{S}
=1-\sqrt{\frac{1+d^2}{2}}.
\]

它由 d=0 时约 0.29289 连续降至 d→1 时的零。d=0.35 时约 0.25083，d=0.60 时约 0.17538。几何容量下降是连续变化，不能自动翻译为一个固定 d 上的“剪刀崩溃”。

核芯响应也不能只由 d 决定。令 a=3JcV/p，

\[
\frac{dj}{dI}
=\frac{j'}{j'(1+ac)+aj},\qquad 0<\frac{dj}{dI}<1.
\]

这给增量自旋分配，区别于某一点的 j/I 或 R/I。固定 d 而改变 JcV，就可改变核芯参与；把平均核芯份额与增量份额混用会改变比较含义。

## Falsification or Reverse Tests

实现：`system/scripts/day27_shears_core_continuation_study.py`。结果：`outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/shears-core/conditional-shears-core-result.json`。

以无量纲 κ=JcV/S² 扫描 380 个内点，独立有界极小化与解析驻值的最大 c 差约 2.85×10⁻⁸；各点曲率正、增量分数位于 (0,1)。中心差分步长 10⁻³、3×10⁻⁴、10⁻⁴ 的最大驻值力残差约为 2.84×10⁻⁵、2.55×10⁻⁶、2.84×10⁻⁷，表现为二阶收敛。零相互作用对照回到 j(c)=I 的可达解。

初次校验在极不对称、较大 κ 条件下失败：直接最小化含较大角度无关常数的 E 时，c 误差 2.12×10⁻⁷，已达能量浮点消减尺度。保留原 Hamiltonian，改算代数等价的 E(c)−E(0)，没有放宽验收阈值；随后通过。该记录是数值实现问题，不是物理失稳。

## Interaction Normalization Counterexample

同一个相互作用可写成

\[
H_{\rm int}=v\sum_{k=1}^{n}F_k
            =V\overline F,\qquad V=nv.
\]

于是同一配对隙满足 Delta/v=n Delta/V。示例 n=5、Delta=1、V=0.4 时，商分别为 12.5 与 2.5，而相互作用能逐点完全相同。未经归一合同的“3.5 阈值”会仅因记号改变而翻转分类。该代数反例没有给出物理上的配对临界值。

## Historical Masking Classifier Audit

复算旧脚本自己的 E2/E2 比值：θ=90° 时，β=0.05、0.18、0.25 分别约为 74.54、1056.87、2136.36。其“比值=50”的根约 β=0.04108，位于其采样下界之外，不在宣称的 0.25。这个根仍只是所选 Qeff、A、Z、角定义的结果，不是新的核结构临界形变。

E2/E2 比值没有包含 M1 算符和光子能量，不能单独判定 M1 级联的可见性。要评价实验可见性，须使用具体跃迁的电磁部分率、能量、分支、效率、背景与门条件。

## Competing Explanations

真实高自旋核可以有三轴取向失稳、配对重排、组态交叉及多叶片耦合；这些机制不在本二维简化能量中。下一步须将具体来源的角定义、整体/每对强度、价粒子空间、核芯参与和实测强度放入同一比较合同，不能把本次条件反例再升级为普适稳定定理。

## Promotion or Rejection History

- 2026-10-29：建立条件反例；撤回 Day27 旧固定 d、Delta/V 与 β 的普适 veto。保留原脚本与历史 Git 记录，供追溯。

## Agent self-audit triage

- P0: none identified after isolation。旧普适排除结论已撤回；计算不作为实验数据。
- P1：模型闭合、角域和经典定长叶片假设；RMS/量子角动量、配对及真实核芯方向动力学未覆盖。
- P2/P3：无拟合参数或新增测量精度声明；无需用户补充普通研究选择。

## Research Trigger

核查旧固定不对称度阈值是否由动力学导出，并建立可独立极小化的条件反例。

## Transfer Conditions

应用解析式时逐项保持定长经典叶片、平行核芯、正Jc/V与闭合角域；真实核数据另行验证。

## Failure Conditions

叶片为零、相互作用吸引、核芯方向自由度重要、配对重排或多叶片交叉时，本稳定性证明不适用。

## Open Questions

加入实际三轴惯量和阻塞后，角曲率变化能否解释实测谱学；增量核芯份额与平均份额应如何从数据区分？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

未发生人工审核；本页是Codex有界推导和数值检查，保持unreviewed与provisional。
