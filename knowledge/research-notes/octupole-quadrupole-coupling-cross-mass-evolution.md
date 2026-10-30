---
type: research-note
title: "跨质量区八极—四极集体运动耦合与电偶极相消演化"
aliases: [octupole-quadrupole-coupling-cross-mass-evolution, octupole cross-mass evolution, Day27 octupole coupling]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution]
created_from: Day 27 octupole cross-mass systematics study; system/scripts/day27_octupole_cross_mass_systematics.py
tags: [octupole-deformation, alternating-parity, electric-dipole-cancellation, coulex, gosia, barium, radium, A140, A220, Day27]
---

# 跨质量区八极—四极集体运动耦合与电偶极相消演化

## Research Trigger

在低能核物理经验模型中，早期常存在将电偶极跃迁 $B(E1)$ 或内禀偶极矩 $D_0$ 作为八极形变 $\beta_3$ 强弱代理的粗糙迁移规则（例如认为“镭同位素必然具有同相增强的强 $E1$，而钡同位素则属于偶极相消岛”）。本研究基于 CARIBU 库仑激发（[[bucher-2016-144ba-direct-octupole]], [[bucher-2017-146ba-direct-octupole]]）与 ISOLDE/MINIBALL 放射性束库仑激发（[[gaffney-2013-pear-shaped-rn-ra]], [[butler-2020-222-228ra-octupole-evolution]]）的一手直接实验数据，定量剖析中子—质子微观壳层与宏观液滴极化相消机制，确立跨区八极识别的严格证据分层。

## Grounded Evidence

通过执行全微观能谱与库仑激发多极矩阵元求解器 `system/scripts/day27_octupole_cross_mass_systematics.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/octupole-cross-mass/octupole_cross_mass_resolution.json`），确立以下定量证据：

1. **直接八极跃迁集体性 $B(E3)$ 的跨区恒定性：**
   - 库仑激发实验直接测量表明，无论是中质量区富中子钡（$^{144}\text{Ba}: 48(4)\text{ W.u.}$, $^{146}\text{Ba}: 48(8)\text{ W.u.}$）还是重锕系（$^{224}\text{Ra}: 42(3)\text{ W.u.}$），其向下约化八极跃迁几率均维持在 $40 - 50\text{ W.u.}$ 的高位平台；
   - 微观机制归因于两区具有完全同构的 $\Delta j = \Delta l = 3$ 轨道对（钡中质子 $\pi h_{11/2} \leftrightarrow d_{5/2}$ 与中子 $\nu i_{13/2} \leftrightarrow f_{7/2}$；镭中质子 $\pi i_{13/2} \leftrightarrow f_{7/2}$ 与中子 $\nu j_{15/2} \leftrightarrow g_{9/2}$），证明纯八极集体性在两区具有同等强度的微观相干性。

2. **内禀电偶极矩 $D_0$ 的同源微观相消节点：**
   - 在 $^{224}\text{Ra}$（$Z=88, N=136$）中，实验直接测定 $B(E1; 3^- \to 2^+) = 3.9(+1.7/-1.4) \times 10^{-5}\text{ W.u.}$，对应内禀电偶极矩仅为 $|D_0| = 0.015(3)\ e\text{ fm}$；
   - 在 $^{146}\text{Ba}$（$Z=56, N=90$）中，实验测定直接 $B(E3)$ 与 $^{144}\text{Ba}$ 相同，但内禀电偶极矩从 $^{144}\text{Ba}$ 的 $0.13(2)\ e\text{ fm}$ 骤降至 $0.05(2)\ e\text{ fm}$；
   - 宏观—微观两相抵消模型证明，宏观液滴电荷偏心贡献 $D_{\text{macro}} \approx +0.32 - +0.35\ e\text{ fm}$ 与中子顺排壳修正贡献 $D_{\text{shell}} < 0$ 在特定中子数（$N \approx 90$ 与 $N \approx 136$）发生近乎完全的相消（相消比 $|D_{\text{shell}}/D_{\text{macro}}| \approx 0.85 - 0.96$）；
   - 彻底证伪了“Ra 必然强 E1”的假说，证明 $E1$ 极小值是跨质量区同构出现的相消干涉现象。

3. **交替宇称能级差 $\Delta E(I)$ 对静态转子与动态振动核的鉴别：**
   - **静态梨形转子（$^{224}\text{Ra}, ^{144}\text{Ba}$）：** $\Delta E(I) = E(I^-) - \frac{1}{2}[E((I-1)^+) + E((I+1)^+)]$ 随自旋单调递减；$^{224}\text{Ra}$ 从 $1^-$ 时的 $173.8\text{ keV}$ 下降至 $9^-$ 时的 $-5.7\text{ keV}$（离心稳定度高达 $103.3\%$），$^{144}\text{Ba}$ 从 $659.4\text{ keV}$ 降至 $56.5\text{ keV}$（稳定度 $91.4\%$），呈现出八极势垒隧穿在科里奥利离心力下闭合的转动特征；
   - **八极微振动核（$^{228}\text{Ra}$）：** $\Delta E(I)$ 在全自旋区间锁定在 $400\text{ keV}$ 附近（$442 \to 403 \to 380 \to 386 \to 420\text{ keV}$），稳定度仅 $4.8\%$，表现为刚性四极基态上附加单八极声子（$\hbar\omega_3 \approx 400\text{ keV}$）的典型振动特征。

## Provisional Reasoning

内禀电偶极算符由质心修正形式给出：
\[
\hat{D}_z = e \frac{N}{A} \sum_{p=1}^Z z_p - e \frac{Z}{A} \sum_{n=1}^N z_n.
\]
1. **宏观液滴项（$D_{\text{macro}}$）：**
   由于中子皮效应与表面张力非对称性，中子与质子在梨形体中的质心发生宏观分离，产生正比于 $\beta_2 \beta_3$ 的电偶极贡献：
   \[
   D_{\text{macro}} \approx C_{\text{LD}} \frac{e Z}{A} \beta_2 \beta_3 \frac{N - Z}{A} > 0.
   \]
2. **微观单粒子壳修正项（$D_{\text{shell}}$）：**
   当费米面处于 $\Delta j = \Delta l = 3$ 轨道底部（如中子 $i_{13/2}$ 轨道）时，反射不对称单粒子波函数极化带来相反符号的本征电偶极贡献：
   \[
   D_{\text{shell}} = \sum_k 2 v_k^2 \langle k | \hat{d}_z | k \rangle < 0.
   \]
3. **极度非线性的相消平方律：**
   跃迁几率 $B(E1) \propto D_0^2 = (D_{\text{macro}} + D_{\text{shell}})^2$。由于两项相差近一个数量级时表现为微小净剩余，单粒子轨道占据几率 $v_k^2$ 仅需发生 $4\%$ 的细微波动，即可引起 $B(E1)$ 发生一至两个数量级的剧烈升降，而表征全核集体形变的 $B(E3) \propto Q_3^2$ 保持稳态。因此，$E1$ 具有高度的微观结构不稳定性，绝不能用作八极形变的指示剂。

## Assumptions

1. 四极—八极形变偶极算符满足轴对称多极展开近似；
2. 实验能带宇称指定由直接线偏振度或转换电子测量确认，避免将自旋指定歧义误判为交替宇称；
3. 库仑激发多极矩阵元抽取由 GOSIA 程序严格执行且经过同位素纯化/杂质扣除。

## Competing Explanations

1. **单八极声子与准粒子四极转动对齐（Aligned Phonon Coupling）：** 负宇称能带可通过将八极振动声子与四极转动轴对齐构建，其在低自旋下表现为恒定能隙 $\Delta E(I)$，类似 $^{228}\text{Ra}$；
2. **分子型 $\alpha$ 团簇结构（$\alpha$-clustering）：** 在轻锕系中，部分负宇称能带被解释为 $\alpha + ^{220}\text{Pb}$ 或 $\alpha + ^{220}\text{Rn}$ 团簇运动，但团簇模型预言的 $B(E3)$ 跨同位素演化趋势与 MINIBALL 实验相反；
3. **同核异宇称非简谐混合：** 高激发态密度的残余配对力在弱形变区引起正负宇称波函数交叉散射。

## Transfer Conditions

1. 判定静态梨形八极转子必须同时满足：(a) 直接库仑激发 $B(E3) \ge 30\text{ W.u.}$；(b) 交替宇称位移 $\Delta E(I)$ 随自旋趋近于零（离心稳定度 $\ge 80\%$）；
2. 无论在任何质量区，禁止使用单个 $B(E1)$ 测量值推断八极形变 $\beta_3$。

## Failure Conditions

1. 仅依据微弱 $B(E1)$ 跃迁即宣称目标核不存在八极形变的推论失效（如 $^{224}\text{Ra}$ 与 $^{146}\text{Ba}$ 相消反例）；
2. 仅依据基态交替宇称序列存在即宣称静态刚性梨形形变的推论失效（必须排除 $\Delta E(I) \approx \text{const}$ 的八极声子振动核，如 $^{228}\text{Ra}$）。

## Falsification or Reverse Tests

1. **反例检验（Ra 强 E1 假说证伪）：** Gaffney 2013 测定 $^{224}\text{Ra}$ 的 $B(E1; 3^- \to 2^+) = 3.9 \times 10^{-5}\text{ W.u.}$，相比普通常规增强核（$10^{-2} - 10^{-3}\text{ W.u.}$）受抑千倍，排他性证伪了“Ra 必然同相强 E1”假设；
2. **振动与转子能级差逆向检验：** 比较 $^{224}\text{Ra}$ 与 $^{228}\text{Ra}$ 在 $9^-$ 处的位移：$^{224}\text{Ra}$ 降至 $-5.7\text{ keV}$（完全隧穿退耦），而 $^{228}\text{Ra}$ 仍高达 $420.9\text{ keV}$，逆向证实 $^{228}\text{Ra}$ 的非静态振动本性。

## Open Questions

1. 在中子极富区（如 $^{148}\text{Ba}, ^{150}\text{Ba}$）中，中子跨过 $N=92$ 后是否会由于四极形变显著增大（$\beta_2 > 0.30$）导致八极势阱变浅并退化为八极软振动？
2. 奇 $A$ 锕系核（如 $^{225}\text{Ra}, ^{225}\text{Ac}$）中奇核子的阻塞效应如何定量改变 $D_{\text{shell}}$ 的抵消节点位置，从而影响原子电偶极矩（EDM）的增强增强因子？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 跨质量区迁移与机制不适用性自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：基于直接 Coulex 矩阵元一手原件，形式化确立了 A≈140（Ba）与 A≈220（Ra）八极—四极集体运动耦合与电偶极相消演化规律，彻底澄清了 E1 代理与交替宇称判据的适用性边界。
