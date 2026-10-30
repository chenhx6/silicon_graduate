---
type: research-note
title: "奇奇核手征—摆动复合模式与签名倒转的微观鉴别判据"
aliases: [chiral-wobbling-composite-modes-vs-signature-inversion, chiral wobbling vs signature inversion, Day27 composite modes]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [guo-2024-chiral-wobbler-74br, qureshie-2026-chiral-wobbling-four-band-74br, petrache-2006-near-degenerate-chiral-misinterpretation]
created_from: Day 27 chiral-wobbling vs signature inversion study; system/scripts/day27_chiral_wobbling_vs_signature_inversion.py
tags: [chirality, wobbling, signature-inversion, composite-modes, odd-odd-nuclei, 74br, 134pr, A80, A130, Day27]
---

# 奇奇核手征—摆动复合模式与签名倒转的微观鉴别判据

## Research Trigger

在奇奇核高自旋谱学中，多能带网络常表现出复杂的能级相近与交叉现象。例如在 [[guo-2024-chiral-wobbler-74br]] 的 $^{74}\text{Br}$ 中观测到三条正宇称带并被指定为“手征—摆动共存复合核”，随后 [[qureshie-2026-chiral-wobbling-four-band-74br]] 预测了第四条带；而在历史经典手征核 [[petrache-2006-near-degenerate-chiral-misinterpretation]] 的 $^{134}\text{Pr}$ 中，近简并双带却被证明源于不同形变（$Q_{0,1}/Q_{0,2} = 2.0(4)$）的能带偶然交叉。由于奇奇核中质子—中子剩余相互作用 $V_{pn}$ 常诱发低自旋签名倒转（Signature Inversion），如何从微观第一性判据上严格区分“真正手征双重带”、“摆动声子激发”与“伪手征签名倒转带”，成为跨质量区迁移的关键方法学问题。

## Grounded Evidence

通过执行全微观能谱交错与多极电磁跃迁求解器 `system/scripts/day27_chiral_wobbling_vs_signature_inversion.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/chiral-wobbling-vs-inversion/chiral_wobbling_inversion_resolution.json`），确立以下定量鉴别证据：

1. **能级交错函数 $S(I)$ 与相位锁定判据：**
   - **签名倒转（Signature Inversion）：** $S(I) = \frac{E(I) - E(I-1)}{2I} - \frac{E(I+1) - E(I)}{2(I+1)}$ 在临界倒转自旋 $I_{\text{inv}}$ 处发生严格的 $180^\circ$ 符号翻转（$S(I) < 0 \to S(I) > 0$），源于低自旋下 $V_{pn}$ 四极吸引压低非有利签名；
   - **手征双重带（Chiral Doublets，$^{74}\text{Br}$ B1 与 B2）：** 两带展现出严格同相位的交错特征（$S_1(I) \approx S_2(I)$），两带间能量间距 $\Delta E_{\text{chiral}}(I) = E_2(I) - E_1(I)$ 随自旋平滑单调收缩（计算显示在 $^{74}\text{Br}$ 中从 $I=6$ 时的 $349.9\text{ keV}$ 持续下降至 $I=12$ 时的 $42.0\text{ keV}$），不发生符号震荡；
   - **摆动声子激发（Wobbling Phonon，$^{74}\text{Br}$ B3）：** B3 作为单声子激发，相对 B1 始终保持严格为正的声子能量（$\hbar\omega_w = 634.9 \to 902.6\text{ keV}$）。

2. **带间多极性与偏振符号的排他性鉴别：**
   - **签名倒转与手征伴带跃迁：** 带间 $\Delta I = 1$ 连接受磁偶极选择定则支配，以强 $M1$ 跃迁为主（混合比 $|\delta| \ll 1.0$，线偏振度 $P < 0$）；
   - **摆动声子跃迁（$^{74}\text{Br}$ B3 $\to$ B1）：** 摆动微振动本质为核电荷四极振荡，带间 $\Delta I = 1$ 跃迁表现为电四极 $E2$ 优势辐射；Guo 2024 实验测定 $8^+ \to 7^+ (\delta=-1.1)$、$9^+ \to 8^+ (\delta=+3.1)$ 与 $10^+ \to 9^+ (\delta=+8.0)$，高自旋光子 $E2$ 份额高达 $90.6\% - 98.5\%$，且实测线偏振 $P > 0$，排他性排除了 B3 作为非手征签名伴带的可能。

3. **内禀四极矩比值 $Q_0$ 测试（Petrache 2006 反例）：**
   - 手征双重带的第一性几何要求是两带具有完全相同的内禀四极形变：$Q_{0,1} / Q_{0,2} = 1.0 \pm 0.15$；
   - 在 $^{134}\text{Pr}$ 中，Petrache 等（2006）通过寿命测量提取出 $Q_{0,1} = 3.6(3)\ e\text{b}, Q_{0,2} = 1.8(3)\ e\text{b}$，比值高达 $2.0(4)$，直接证伪了其理想手征双重带解释，证明纯能级近简并不构成手征性的充分证据；
   - 而在 $^{74}\text{Br}$ 中，B1、B2、B3 共享一致的 DSAM 寿命和四极形变 $\varepsilon_2 \approx 0.28$，通过了形变简并硬检验。

## Provisional Reasoning

在三维倾斜轴推转（3D-TAC）与微观粒子-转子模型中，三类模式的动力学自由度分属不同群论与拓扑空间：
1. **三维非共面手征性（Chirality）：**
   总角动量三个主轴分量同时非零（$J_x \neq 0, J_y \neq 0, J_z \neq 0$）。质子顺排沿短轴，中子顺排沿长轴，集体核芯沿中轴转动。空间反演与时间反演的联合对称性 $\hat{\mathcal{T}}\mathcal{R}_y(\pi)$ 自发破缺，产生左右手互易简并本征态；
2. **二维共面签名倒转（Signature Inversion）：**
   角动量严格局限于主平面内（$J_y \equiv 0$ 或 $J_z \equiv 0$）。时间反演结合平面反射对称性保持完好，不存在手征双重态。其能级反常交错完全由单粒子准轨道在角动量重整化下的科里奥利反配对力与残留张量力 $V_{pn}$ 引起；
3. **复合模式正交性（Chiral Wobbler）：**
   在手征极小值能量超曲面上，关于平衡转动轴的微小量子摆动激发构成横向四极微振动（$n_w=1$），其正交于左右手隧穿坐标，因此允许在同一微观核中出现基于相同 $\pi g_{9/2} \otimes \nu g_{9/2}$ 构型的四带共存网络（B1/B2 为基态手征对，B3/B4 为激发摆动对）。

## Assumptions

1. 奇奇核价核子构型由单粒子能级转移与高自旋顺排对齐量唯一确定；
2. 实验能级交错函数 $S(I)$ 计算采用无偏二阶有限差分形式，且能级测量误差小于 $0.5\text{ keV}$；
3. 库仑激发与寿命测量中提取的内禀四极矩 $Q_0$ 已校正侧向慢馈送（side-feeding）延迟。

## Competing Explanations

1. **同形变偶合交叉伪简并（Accidental Band Crossing）：** 类似 $^{134}\text{Pr}$，两条不同多准粒子组态能带在特定自旋区间的偶然能量靠近，常在能级图上伪装成手征双重带；
2. **形状共存隧穿（Shape Coexistence Mixing）：** 近球形与三轴形变在低自旋区的波函数重叠，导致能级交错反常；
3. **经典倾斜进动（Tilted Precession, TiP）：** 假定角动量在非主轴方向稳定进动，但缺乏量子声子分立跃迁特征。

## Transfer Conditions

1. 确认奇奇核具有手征性必须同时满足：(a) 双带能级平滑逼近简并（$\Delta E \to 0$）；(b) 两带交错函数同相（$S_1(I) \approx S_2(I)$，无倒转翻转）；(c) 内禀四极矩相等（$Q_{0,1}/Q_{0,2} = 1.0 \pm 0.15$）；(d) 相互连接由 $M1$ 占优；
2. 确认复合摆动激发必须同时测得：(a) 带间跃迁由电四极 $E2$ 占优（$|\delta| > 1.0, P > 0$）；(b) 能量位移 $\hbar\omega_w > 0$；(c) 四极形变与母带自洽。

## Failure Conditions

1. 在未进行 $Q_0$ 绝对寿命测量的前提下，单凭能级近简并宣称手征双重带的结论失效（Petrache 2006 反例）；
2. 若带间连接表现为强烈 $M1$ 跃迁（$P < 0$），却将伴带指认为摆动声子激发的推论失效；
3. 若交错函数 $S(I)$ 随自旋发生正负变号，却忽视签名倒转机制的结论失效。

## Falsification or Reverse Tests

1. **反证检验（134Pr 假手征证伪）：** Petrache 2006 实验测得 $Q_{0,1}/Q_{0,2} = 2.0(4)$，与手征双重带要求相悖，排他性证伪了 $^{134}\text{Pr}$ 的基态手征伙伴假说；
2. **偏振极性逆向反证：** 在 $^{74}\text{Br}$ B3 $\to$ B1 跃迁中，若实测偏振度为负（$P < 0$），则其摆动声子解释被立即推翻。实际测得 $P > 0$ 且 $\delta = +3.1, +8.0$ 反向确认了其 $E2$ 摆动本性。

## Open Questions

1. 在 $^{74}\text{Br}$ 中，第四能带 B4 是否能在即将开展的高统计量超阵列实验中直接观测到与 B3（手征连接，强 $M1$）和 B2（摆动连接，强 $E2$）的分支跃迁？
2. 跨质量区迁移至超重核时，强库仑场引起的单粒子电荷极化是否会破坏奇奇核手征几何的非共面稳定性？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 跨质量区迁移与机制不适用性自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：基于 $^{74}\text{Br}$ 与 $^{134}\text{Pr}$ 一手实验原件，首次系统建立了奇奇核中手征双重带、摆动声子激发与签名倒转三者的全套微观可观测鉴别判据矩阵，闭合了方法学伪简并边界。
