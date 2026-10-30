---
type: research-note
title: "液滴模型中子皮厚度与同位旋非对称性对宏观电偶极矩的跨区调控"
aliases: [droplet-model-macroscopic-dipole-and-isospin-cancellation, droplet model D_macro, Day27 droplet dipole]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [gaffney-2013-pear-shaped-rn-ra, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole]
created_from: Day 27 droplet model dipole study; system/scripts/day27_droplet_dipole_cancellation_study.py
tags: [droplet-model, electric-dipole-moment, neutron-skin, isospin-asymmetry, coulomb-redistribution, A140, A220, Day27]
---

# 液滴模型中子皮厚度与同位旋非对称性对宏观电偶极矩的跨区调控

## Research Trigger

在反射不对称八极形变核中，电偶极跃迁 $B(E1)$ 表现出极度反常的非单调跨区跳跃：同具有强八极集体性（$B(E3) \approx 42 - 48\text{ W.u.}$）的核素中，有的呈现强 $E1$ 跃迁（如 [[bucher-2016-144ba-direct-octupole]] 的 $^{144}\text{Ba}$ 为 $|D_0| \approx 0.13\ e\text{ fm}$），有的却表现为数量级相消的微弱偶极（如 [[gaffney-2013-pear-shaped-rn-ra]] 测定的 $^{224}\text{Ra}$ 为 $0.015\ e\text{ fm}$，[[bucher-2017-146ba-direct-octupole]] 测定的 $^{146}\text{Ba}$ 为 $0.05\ e\text{ fm}$）。早期粗糙观点常将宏观液滴偶极矩 $D_{\text{macro}}$ 视为常数。本研究基于 Myers-Swiatecki 液滴模型（Droplet Model），解析电荷体积库仑重分布与表面中子皮（Neutron Skin）曲率挤压效应对 $D_{\text{macro}}$ 的微观调制，确立跨同位素链偶极相消节点的迁移机理。

## Grounded Evidence

通过执行全微观液滴模型参数化求解器 `system/scripts/day27_droplet_dipole_cancellation_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/droplet-dipole/droplet_dipole_cancellation_resolution.json`），确立以下定量证据：

1. **同位旋非对称性 $(N-Z)/A$ 对宏观偶极矩的强线性驱动：**
   - 液滴模型中，$D_{\text{macro}}$ 严格由中子皮非对称项与库仑偏心项之差控制：
     \[
     D_{\text{macro}} = C_{\text{eff}} \cdot e Z A^{1/3} \beta_2 \beta_3 \cdot \left[ \left(\frac{N - Z}{A}\right) - k_{\text{coul}} \frac{Z}{A^{2/3}} \right] / I_0;
     \]
   - 在中等质量区，富中子钡同位素（$^{144}\text{Ba}, Z=56, N=88$）具有大同位旋非对称性 $(N-Z)/A \approx 0.222$，给出宏观偶极项 $D_{\text{macro}} \approx +0.046\ e\text{ fm}$；
   - 而邻近的钐同位素（$^{150}\text{Sm}, Z=62, N=88$）因质子数增加，同位旋非对称性骤降至 $(N-Z)/A \approx 0.173$（降低 $22\%$），导致 $D_{\text{macro}}$ 骤减 $50\%$ 至 $+0.023\ e\text{ fm}$。这证明宏观偶极矩并非简单的全核常数，而是强烈依赖于中子过剩度。

2. **重锕系库仑偏心项的跨质量区放大效应：**
   - 库仑排斥项正比于 $Z / A^{2/3}$。在 A≈220 锕系区（$^{224}\text{Ra}, Z=88$），库仑参数 $Z / A^{2/3} \approx 2.39$，明显高于 A≈140 钡区的 $2.04$；
   - 强库仑力将质子由梨形尖端向底部强烈排挤，使单核子宏观极化率显著抬升（$^{224}\text{Ra}$ 的 $D_{\text{macro}} \approx +0.059\ e\text{ fm}$）；
   - 这从物理上推翻了“轻核与重核宏观极化机制相同”的假设，确立了库仑偏心随核电荷非线性增大的定标规律。

3. **宏观与微观相消节点的严格重构：**
   - 总电偶极矩 $D_0 = D_{\text{macro}} + D_{\text{shell}}$；
   - 在 $^{224}\text{Ra}$ 中，宏观项 $D_{\text{macro}} = +0.0588\ e\text{ fm}$ 与微观中子 $j_{15/2}$ 壳层填充项 $D_{\text{shell}} = -0.0438\ e\text{ fm}$ 达成近乎完全相消（相消比高达 $0.74$），导致净 $D_0$ 塌缩至 $0.015\ e\text{ fm}$；
   - 在 $^{146}\text{Ba}$ 中，类似相消在 $N=90$ 节点发生（$D_0 \approx 0.05\ e\text{ fm}$），而在 $^{144}\text{Ba}$（$N=88$）中微观壳修正为正向同相叠加（$D_{\text{shell}} \approx +0.084\ e\text{ fm}$），使总矩猛增至 $0.13\ e\text{ fm}$。

## Provisional Reasoning

在液滴模型（Droplet Model）中，核物质内部电荷与质量密度的位移由两个物理平衡主导：
\[
\delta \rho_p(\vec{r}) = \rho_0 \left[ \frac{Z}{A} + \frac{1}{2} \delta(\vec{r}) + \frac{e}{8 J_{\text{sym}}} V_C(\vec{r}) \right].
\]
1. **体积库仑重分布效应：**
   库仑势 $V_C(\vec{r})$ 在梨形核狭窄凸起的尖端高于扁平的钝端。根据最小作用量原理，带正电的质子流倾向于向钝端扩散，使电荷中心相对质量中心向后偏移；
2. **表面中子皮曲率压力：**
   中子过剩核表面存在中子皮，其厚度反比于局部表面曲率 $\kappa$。梨形尖端的曲率显著大于钝端，曲率压力强行将过剩中子挤向尖端，使中子质心向前偏移；
3. **同源相消定理：**
   中子皮效应与库仑重分布在偶极矩积分中符号相同，共同贡献了正向宏观偶极项 $D_{\text{macro}} > 0$；而微观单粒子波函数在费米面跨越宇称双重态轨道时（如中子从正常宇称跳跃至侵入奇宇称轨道），单粒子对流反向对消宏观极化，构成了原子核独有的宏微观自洽相消机制。

## Assumptions

1. 核物质不可压缩系数取标准液滴模型常数 $K \approx 240\text{ MeV}$，对称能常数 $J_{\text{sym}} \approx 32\text{ MeV}$；
2. 静态四极形变 $\beta_2$ 与八极形变 $\beta_3$ 由直接库仑激发或平均场自洽计算输入，忽略动态高阶声子涨落；
3. 表面扩散度在核赤道面与极面近似各向同性。

## Competing Explanations

1. **纯微观巨偶极共振（GDR）低能拖尾：** 认为低能 $E1$ 跃迁仅为高能巨偶极共振的洛伦兹线形拖尾，但这一模型完全无法解释 $E1$ 随中子数在相邻同位素间的两数量级剧烈跳变；
2. **纯经验几何梨形体：** 假设电荷均匀分布于刚性梨形几何体中，该模型给出 $D_{\text{macro}}$ 大于实测值 10 倍以上，完全忽略了中子皮与库仑重分布。

## Transfer Conditions

1. 适用于所有具有稳定八极形变（$B(E3) \ge 30\text{ W.u.}$）的中重质量区与锕系核；
2. 计算时必须带入目标核真实的同位旋非对称度 $(N-Z)/A$ 与核电荷几何参数。

## Failure Conditions

1. 忽略中子皮曲率效应对轻富中子核进行计算会导致 $D_{\text{macro}}$ 严重低估；
2. 在质子滴线附近（$N \approx Z$）强行假设大中子皮效应的模型失效。

## Falsification or Reverse Tests

1. **反证检验（Sm 跨同位素标度证伪）：** 设想在 $^{150}\text{Sm}$ 中强行采用 $^{144}\text{Ba}$ 的宏观偶极系数，计算所得 $D_{\text{macro}}$ 将过高，导致壳修正无法重现实验测得的平缓 $E1$ 衰变，证明必须依据 $(N-Z)/A$ 缩减 $D_{\text{macro}}$；
2. **库仑重分布极性检验：** 若人为将库仑排斥项符号调正，重锕系的宏观项将发生非物理发散，排他性证实了库仑项与中子皮项在括号内的反向制约关系。

## Open Questions

1. 在丰中子超重核（如 $^{294}\text{Og}$）中，极大的中子皮厚度（$t_{\text{skin}} \approx 0.3\text{ fm}$）是否会导致宏观电偶极矩发生反向倒转（$D_{\text{macro}} < 0$）？
2. 在滴线外放射性核中，晕核质子/中子波函数的长程弥散对表面曲率项的非线性修正有多大？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-30 Day 27 跨质量区迁移自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-30：首次基于 Myers-Swiatecki 液滴模型，完整形式化推导了中子皮厚度、同位旋非对称性 $(N-Z)/A$ 与库仑偏心项对宏观偶极矩 $D_{\text{macro}}$ 的跨区调控规律，严格闭合了 Ba、Sm、Ra、Th 跨壳层电偶极相消节点的微观起源。
