---
type: concept
title: "Coriolis anti-pairing：配对减弱解释与条件惯量插值"
aliases: [coriolis-anti-pairing, cap-effect, mottelson-valatin-effect, pairing-gap-quenching, moi-cap-expansion]
created: 2026-11-04
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
tags: [high-spin, pairing-correlations, coriolis-anti-pairing, cap, moments-of-inertia]
---

# Coriolis anti-pairing：配对减弱解释与条件惯量插值

## Definition

本页将原书解释与本库人为指定的曲线分开。[[book-bohr-mottelson-nuclear-structure-vol2]] 的 BM2-11（§4-3a，物理 PDF64／printed42，编号1及前文）讨论随角动量增加配对关联减弱，并把较突发的配对相到正常相转变作为可能解释。该段没有给出下列平方根函数、普适临界自旋或统一二级相变定律。本轮沿用已更正的 source 定位，没有新增原书页面检查。

旧版本给出的核素临界自旋、配对隙数值、固定刚体比例和特定集体模式稳定化结论均撤回为未经实验标定的预设解释；它们不能作为目标核实验事实或原书结论使用。配对降低惯量与严格无旋流体惯量不是同一计算。

## Necessary Assumptions

以下是 `coriolis_anti_pairing_gap_quenching_moi_engine.py` 的模型合同，属于任务模型与代数推论，不是原书公式或微观自洽 BCS 解。记

$$x=\hbar\omega\quad[\mathrm{MeV}],\qquad i=I/\hbar,$$

$$\Delta(x)=\Delta_0\sqrt{\max(0,1-(x/x_c)^2)},\qquad
\mathcal J_k(x)=\mathcal J_{\mathrm{rig},k}f(x),\quad
f(x)=1-(1-r)\Delta(x)/\Delta_0.$$

输入需有限，$\Delta_0\ge0$、$x_c>0$、$\mathcal J_{\mathrm{rig},k}>0$、$0<r\le1$。配对隙函数对有符号 $x$ 是偶函数，自旋映射使用 $i\ge0$ 的非负频率支。$r$ 是选定的共同低频惯量比例，不是无旋流体模型的推导值；惯量单位为 $\hbar^2/\mathrm{MeV}$。当 $\Delta_0=0$ 时，直接定义所有惯量等于给定刚体参考值，不计算 $0/0$。

由于各轴乘同一正因子，

$$\frac{\mathcal J_m(x)}{\mathcal J_s(x)}=
\frac{\mathcal J_{\mathrm{rig},m}}{\mathcal J_{\mathrm{rig},s}},\qquad
\frac{\mathcal J_m(x)}{\mathcal J_l(x)}=
\frac{\mathcal J_{\mathrm{rig},m}}{\mathcal J_{\mathrm{rig},l}}.$$

较大的轴可有较大的绝对增量，但各轴相对缩放相同，轴比和惯量序不变。该模型不能生成新的惯量不对称，也不能据此确认横向摆动、手征性或其稳定化。

## Discriminating Observables

程序求解的是代数方程 $i=[\mathcal J_m(x)/\hbar^2]x$，没有单粒子能谱、配对强度、gap/number 方程或能量极小化。对上述输入域，惯量非减且严格为正，映射单调，根唯一。上界取 $\max(x_c,i/[\mathcal J_{\mathrm{rig},m}/\hbar^2])$，位于刚体支并显式检查根括号。零自旋解精确为零；零初始 gap 或 $r=1$ 时有解析刚体解。

`critical_transition_spin_I_CAP` 保留旧字段名，但现在明确定义为**输入采样中满足 $\Delta/\Delta_0<0.05$ 的最小 $i$**；输出演化仍保留输入顺序。没有符合点、空采样或 $\Delta_0=0$ 时为 null。这是严格小于5%的采样指标，不是连续根、普适临界自旋或相变阶数判据。正初始 gap 下，指定曲线的零隙点是 $x_c$，其映射自旋只是所选模型的 $i_c=[\mathcal J_{\mathrm{rig},m}/\hbar^2]x_c$；改变采样会改变旧字段的数值。

`rotational_frequency_MeV` 实际保存 $\hbar\omega$ 的 MeV 数值；`is_superfluid` 仅表示指定 gap 为正。零初始 gap 下，`gap_quenching_pct=100` 是兼容旧接口的零隙标记，没有归一化耗尽含义。

`wobbling_frequency_keV` 只是最大惯量主轴的刚性转子诊断量

$$E_{\mathrm{wob}}=x\sqrt{(\mathcal J_m/\mathcal J_s-1)(\mathcal J_m/\mathcal J_l-1)}.$$

轴比不变使根号因子不变；该量不是含顺排粒子的横向摆动计算。若 $m$ 轴非最大惯量，代码返回0作为旧接口标记，不能解释成已验证的稳定零模。

## Our Current Position

函数签名、预设键和 `capgap` CLI 保留。`163Lu`、`130Ba` 字样只是历史合成预设标签，无核素数据拟合或实验核验含义。例如：

```bash
python3 system/scripts/analysis/nuclear_analyzer.py capgap --preset 163Lu_TSD_superfluid_to_normal_phase_transition
python3 system/scripts/analysis/coriolis_anti_pairing_gap_quenching_moi_engine.py --preset rigid_rotor_zero_pairing_limit --json
```

## Counter-evidence and Competing Interpretations

要判断实际谱变化，仍需逐带实验能量、惯量提取约定和误差，以及组态顺排、带交叉、形变变化等竞争解释的独立检验。本页不提供这些输入，不以曲线连续或 gap 人为归零推断有限核的普适相变。

## Supporting Evidence

原书支持配对减弱的试探性解释，不支持本页人为函数。统一缩放的轴比恒等式和指定插值的极限可直接检验，11项专用测试验证数值合同而非实际核结构。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]，BM2-11：仅支持上述试探性配对解释及归属撤回。
- 本库 CAP engine：条件模型定义与解析极限；不是独立文献证据。
- [[coriolis-antipairing-and-superdeformed-alignment-transitions]]：Day27 指定交叉示意的独立边界。
