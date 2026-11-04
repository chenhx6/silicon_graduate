---
type: research-note
title: "跨质量区摆动模式迁移性与转动惯量层级条件反例"
aliases: [wobbling-mode-transferability-and-moi-hierarchy, wobbling MoI hierarchy, Day27 wobbling transferability]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [frauendorf-2014-transverse-wobbling, odegard-2001-evidence-wobbling-163lu, biswas-2019-longitudinal-wobbling-133la]
created_from: Day 27 wobbling PRM and HFA cross-mass study; system/scripts/day27_wobbling_prm_cross_mass_study.py
tags: [wobbling, transverse-wobbling, longitudinal-wobbling, prm, hfa, moments-of-inertia, A130, A160, Day27]
---

# 跨质量区摆动模式迁移性与转动惯量层级条件反例

## Research Trigger

低能核结构高自旋实验中，曾将 A≈160 质量区超形变带（如 [[odegard-2001-evidence-wobbling-163lu]] 的 $^{163}\text{Lu}$ TSD2）中确立的“摆动频率随自旋下降（$d\hbar\omega_w/dI < 0$）与大 $B(E2_{\text{out}})/B(E2_{\text{in}})$”直接作为判据迁移至 A≈130 质量区（如 $^{135}\text{Pr}$ 与 $^{133}\text{La}$）。然而在 $^{135}\text{Pr}$ 中，为拟合下降的 $\hbar\omega_w$，早期唯象模型不得不人为假定颠倒的转动惯量序（$\mathcal{J}_s > \mathcal{J}_m$），与微观自洽推转及配对理论直接冲突；而随后在 [[biswas-2019-longitudinal-wobbling-133la]] 的 $^{133}\text{La}$ 中却观测到单调上升的 $\hbar\omega_w$（纵向摆动）。本研究基于 Frauendorf & Dönau（2014）调和涨落近似（HFA）与粒子-转子模型（PRM），推演准粒子顺排方向与转动惯量主轴层级在该模型中的控制关系，并把跨质量区直接迁移的风险记录为条件性边界。

## Grounded Evidence

通过执行参数化求解器 `system/scripts/day27_wobbling_prm_cross_mass_study.py`（数值结果存入对应 continuation 输出），得到以下模型结果；它们用于检查迁移条件，不是跨核素实验定理：

1. **横向摆动（TW）的代数判据与临界分岔自旋（$^{163}\text{Lu}$ 标杆）：**
   - 依据 [[frauendorf-2014-transverse-wobbling]] 公式 (24)：
     \[
     \hbar\omega_w = \frac{j}{\mathcal{J}_3} \left[ \left( 1 + \frac{J}{j} \left( \frac{\mathcal{J}_3}{\mathcal{J}_1} - 1 \right) \right) \left( 1 + \frac{J}{j} \left( \frac{\mathcal{J}_3}{\mathcal{J}_2} - 1 \right) \right) \right]^{1/2}
     \]
   - 在 $^{163}\text{Lu}$（TSD 形变 $\varepsilon_2 \approx 0.38, \gamma \approx 20^\circ$）中，$\pi i_{13/2}$ 准粒子处于壳层底部（纯粒子性），沿短轴（$s$ 轴，标号 3）对齐（$j=13/2=6.5\hbar$），而核芯转动惯量最大轴为中轴（$m$ 轴，标号 2，$\mathcal{J}_2 = \mathcal{J}_m = 65\ \hbar^2/\text{MeV}$，$\mathcal{J}_3 = \mathcal{J}_s = 40\ \hbar^2/\text{MeV}$）；
   - 由于 $\frac{\mathcal{J}_3}{\mathcal{J}_2} - 1 = \frac{40}{65} - 1 = -0.3846 < 0$，根号内第二项随自旋 $J$ 线性单调减小；
   - 在该组 HFA/PRM 参数下，摆动能量呈随自旋下降的横向特征：从 $J=8.5$ 时的 $204.3\text{ keV}$ 单调降至 $J=16.5$ 时的 $57.2\text{ keV}$；
   - 在该参数化中，$J_c = j / (1 - \mathcal{J}_s/\mathcal{J}_m) = 16.9\hbar$ 附近的频率趋近于零，提示平面摆动解向倾斜轴解分岔；该临界值依赖模型输入。
   - 电磁比值 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 由于小振幅展开系数 $x, y \propto 1/\sqrt{\hbar\omega_w}$ 的发散补偿，维持在 $0.50 - 1.39$ 的平台增强区间。

2. **纵向摆动（LW）的单调上升判据（$^{133}\text{La}$ 标杆）：**
   - 在 $^{133}\text{La}$（正形变 $\varepsilon_2 \approx 0.18, \gamma \approx 20^\circ$）中，$\pi h_{11/2}$ 准粒子沿最大转动惯量轴（$m$ 轴，标号 3，$\mathcal{J}_3 = \mathcal{J}_m = 65\ \hbar^2/\text{MeV}$）对齐，其余两轴为 $\mathcal{J}_1 = \mathcal{J}_l = 15, \mathcal{J}_2 = \mathcal{J}_s = 40$；
   - 此时 $(\mathcal{J}_3/\mathcal{J}_1 - 1) = +3.333 > 0$，$(\mathcal{J}_3/\mathcal{J}_2 - 1) = +0.625 > 0$，两项均随自旋线性上升；
   - $在该组参数下，$\hbar\omega_w$ 随自旋上升：从 $J=6.5$ 时的 $248.0\text{ keV}$ 线性攀升至 $J=22.5$ 时的 $610.5\text{ keV}$，在扫描区间内未见该参数化的分岔临界点；
   - 电磁比值 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 中 $x, y$ 趋于常数，在该近似下近似呈现 $1/J$ 稀释趋势，从 $J=6.5$ 时的 $0.480$ 单调衰减至 $J=22.5$ 时的 $0.161$。

3. **$^{135}\text{Pr}$ 历史伪横向摆动的反例解析：**
   - 在 $^{135}\text{Pr}$ 中，早期为拟合实测低自旋下降的 $\hbar\omega_w$，被迫采用唯象拟合参数 $\mathcal{J}_1=7, \mathcal{J}_2=21, \mathcal{J}_3=13$（给出假想 $J_c \approx 14.4\hbar$），其实质是人为颠倒流体力学与微观 HFB 计算给出的惯量序（将最大惯量强加于短轴），且无法自洽重现绝对 $B(M1)$ 强度；
   - 随后的实验与模型分析削弱了原始横向摆动解释，并支持组态/能带交叉或 TiP 等替代路线；这里不把它写成由单一证据完成的唯一机制证明。

## Provisional Reasoning

在三轴转子加单准粒子体系中，摆动频率的自旋导数符号严格由下式控制：
\[
\frac{d(\hbar\omega_w)}{dJ} = \frac{1}{2\hbar\omega_w} \left(\frac{j}{\mathcal{J}_3}\right)^2 \frac{1}{j} \left[ \left(\frac{\mathcal{J}_3}{\mathcal{J}_1} - 1\right)\left(1 + \frac{J}{j}\left(\frac{\mathcal{J}_3}{\mathcal{J}_2} - 1\right)\right) + \left(\frac{\mathcal{J}_3}{\mathcal{J}_2} - 1\right)\left(1 + \frac{J}{j}\left(\frac{\mathcal{J}_3}{\mathcal{J}_1} - 1\right)\right) \right].
\]
1. **横向对齐几何（$\vec{j} \parallel s$ 轴）：** 取 $\mathcal{J}_3 = \mathcal{J}_s$。由于流体惯量序满足 $\mathcal{J}_l < \mathcal{J}_s < \mathcal{J}_m$，因此 $(\mathcal{J}_3/\mathcal{J}_1 - 1) > 0$，而 $(\mathcal{J}_3/\mathcal{J}_2 - 1) = (\mathcal{J}_s/\mathcal{J}_m - 1) < 0$。在低自旋下，后一项的负贡献占据主导，导致 $d(\hbar\omega_w)/dJ < 0$；
2. **纵向对齐几何（$\vec{j} \parallel m$ 轴）：** 取 $\mathcal{J}_3 = \mathcal{J}_m$。因 $m$ 轴为最大惯量轴，两括号因子均恒大于零，导数在该扫描区间为正，支持 $d(\hbar\omega_w)/dJ > 0$；
3. **电磁跃迁的模型预期差异：** 在该小振幅参数化中，横向与纵向解的电磁比值呈现不同趋势；这些趋势依赖展开、惯量、组态和响应合同，不能写成所有核素的必然定律。

## Assumptions

1. 准粒子高-$j$ 矢量采用“冻结顺排”（Frozen Alignment, FA）近似，与转子特定主轴刚性锁定；
2. 转子恢复力采用三轴流体力学惯量张量或参数化三轴转子模型，未包含高阶微观离心伸展项；
3. 摆动微振动幅度满足小振幅调和涨落展开条件（$J_1^2 + J_2^2 \ll J^2$）。

## Competing Explanations

1. **准粒子多带交叉（Band Crossing）：** 类似 $^{135}\text{Pr}$，1-准粒子带与 3-准粒子带的近简并交叉会在能谱上产生表观的能级差下降与带间电磁跃迁，伪装成横向摆动；
2. **手征双重带（Chiral Doublets）：** 在非共面转动下，两简并带能级差随自旋减小源于手征几何隧穿恢复，其伴随特征是强 $M1$ 跃迁，而纯横向摆动由大 $E2$ 跃迁主导；
3. **倾斜进动模式（Tilted Precession, TiP）：** 当转动轴脱离主轴在平面或空间连续倾斜时，能谱演化由平均场 TAC 主导而非谐振子单声子激发。

## Transfer Conditions

1. 模式向其他核素迁移前，必须同时验证 $\hbar\omega_w(I)$ 斜率符号与绝对/相对 $B(E2), B(M1)$ 跃迁几率网络；
2. 唯象拟合得出的惯量序必须与微观推转 HFB 或推转 Nilsson 势能面给出的三轴形变平衡点惯量自洽，禁止采用违背物理惯量序的自由参量拟合。

## Failure Conditions

1. 在未获得微观自洽惯量验证的前提下，单凭 $\hbar\omega_w$ 随自旋下降断言横向摆动的结论需要额外的惯量、偏振和绝对强度约束（如 $^{135}\text{Pr}$）；
2. 若观测到 $B(E2_{\text{out}})/B(E2_{\text{in}})$ 随自旋反常增长，却将其归因于纵向摆动的结论失效（违背 $1/I$ 稀释定理）；
3. 当费米面处于高-$j$ 壳层中上部（空穴性）时，强行假设准粒子沿短轴对齐的物理模型失效。

## Falsification or Reverse Tests

1. **反证检验（惯量序逆转证伪）：** 设想在 $^{163}\text{Lu}$ 中强行将对齐轴指定为最大惯量轴（$\mathcal{J}_3 = \mathcal{J}_m$），计算所得 $\hbar\omega_w$ 立即逆转为从 $204\text{ keV}$ 单调上升至 $500\text{ keV}$ 以上，彻底违背实验下降趋势，证明横向摆动必须依赖短轴对齐与中轴最大惯量；
2. **$1/I$ 衰减检验：** 在纵向候选核 $^{133}\text{La}$ 中，实验若测得带间比值不降反升，则会削弱该参数化下的纵向摆动解释，但不能单独完成机制排除。

## Open Questions

1. 在 A≈80 质量区（如 $^{74}\text{Br}$）四带手征—摆动网络中，三轴软度引起的 $\gamma$ 涨落如何重整有效惯量序并改变临界分岔自旋 $J_c$？
2. 偶偶核与奇奇核中双核子/多核子非相干耦合如何将单粒子摆动几何演化为复杂的多进动拓扑？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 跨质量区迁移与机制不适用性自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：基于 HFA 解析与 PRM 数值模型，记录了 A≈160 与 A≈130 示例的 HFA/PRM 转动惯量层级结果，并把 $^{135}\text{Pr}$ 的唯象参数风险整理为待实验约束的模型边界。
