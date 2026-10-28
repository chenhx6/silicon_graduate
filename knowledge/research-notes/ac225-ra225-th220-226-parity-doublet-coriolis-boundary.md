---
type: research-note
title: "锕系奇 A 核与偶偶钍核的八极宇称伙伴：K=3/2 解耦边界、Coriolis 劈裂与 E1 证据"
aliases: [Ac225 Ra225 Th220-226 parity doublet Coriolis boundary, actinide octupole parity doublets]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nndc-2022-ac225-adopted-parity-doublet, nndc-2009-ra225-adopted-parity-doublet]
created_from: Day26 directed study of odd-A Ac and even-even Th octupole spectra
promotion_target: octupole-mr-amr-evidence-gradient
tags: [octupole, parity-doublet, Coriolis, decoupling-parameter, actinium, radium, thorium, E1, ENSDF, model-boundary]
---

# 锕系奇 A 核与偶偶钍核的八极宇称伙伴

## Research Trigger

本研究系统比较奇质子核 $^{225}$Ac 的 $K=3/2^\pm$ 与奇中子核 $^{225}$Ra 的 $K=1/2^\pm$ 宇称双重态，并核验 $^{227}$Ac 及 $^{220,222,224,226}$Th 的评价能谱与 E1 记录。首先修正一个过强的前提：NNDC/ENSDF 当前取得的 $^{225}$Ac 评价能级并不支持“所有 $\Delta E(I)$ 均为正且固定在 $36$–$47\text{ keV}$”。在最明确的 A/B 两带配对下，$\Delta_{+-}(I)=E(I^+)-E(I^-)$ 分别为 $40.10$、$34.78$、$27.88\text{ keV}$（$I=3/2,5/2,7/2$），表现为平滑下降。由此证明的是 **$K=3/2$ 的一阶对角解耦项消失（$a \equiv 0$），因而在纯带模型中不会产生 $K=1/2$ 式的剧烈符号交错**，阐明了自旋投影 $K$ 对八极双重态转动调制的微观物理机制。

## Grounded Evidence

### 1. $^{225}$Ac: $K=3/2$ 评价谱学对照

NNDC 评价将基态列为 $(3/2^-)$，A 带含 $(5/2^-)$ 29.91 和 $(7/2^-)$ 77.13 keV，B 带含 $(3/2^+)$ 40.10、$(5/2^+)$ 64.69、$(7/2^+)$ 105.01、$(9/2^+)$ 144.96 keV。A/B 同自旋配对的 $\Delta_{+-}=E_+-E_-$ 为：

| $I$ | $E(I^-)$ A (keV) | $E(I^+)$ B (keV) | $\Delta_{+-}$ (keV) | 评价特征 |
|---:|---:|---:|---:|---|
| $3/2$ | 0.00 | 40.10(4) | +40.10 | 纯对角解耦消失，$a=0$ |
| $5/2$ | 29.91(6) | 64.69(5) | +34.78 | 平滑单调下降 |
| $7/2$ | 77.13(9) | 105.01(7) | +27.88 | 无 $(-1)^{I+1/2}$ 符号交错 |

评价给出的 $40.09(5)$-keV E1 到基态，$B(E1)=0.00171(15)\text{ W.u.}$，是由 $^{225}$Ra $\beta^-$ 衰变中的转换电子亚壳层比得到的直接评价量（见 [[nndc-2022-ac225-adopted-parity-doublet]]）。

### 2. $^{225}$Ra: $K=1/2$ 旋称交错对照

NNDC 评价的 A/B 带为 $K=1/2^+$ 与 $K=1/2^-$。同自旋能级差呈现剧烈的符号交替：
$\Delta_{-+}(I) = E(I^-) - E(I^+) = +55.16\ (1/2),\ -11.21\ (3/2),\ +94.95\ (5/2),\ -42.24\ (7/2)\text{ keV}$。
评价记录包含 $31.50\text{ keV}$ $3/2^- \to 1/2^+$ 跃迁，$B(E1) = 0.00081(20)\text{ W.u.}$。

### 3. 偶偶钍同位素 $^{220,222,224,226}$Th 的八极特征

| 核素 | 评价带结构和能谱 | E1 记录 | 量化边界 |
|---|---|---|---|
| $^{220}$Th | $K=0^+$ 基带；$5^-$ 带头 993.77 keV，演化至 $11^-$ 2158.87 keV。 | $5^-\to 4^+$ 233.9、$7^-\to 6^+$ 162.9 keV 等带间 E1 跃迁。 | Adopted 表无负宇称态寿命，无法提取绝对 $B(E1)$。 |
| $^{222}$Th | 评价明确将 $K=0^+$ 基带与 246-keV $K=0^-$ 带解释为八极宇称双重态。 | 评价保留 $B(E1)/B(E2) \sim 1.1\times 10^{-4}$–$3.4\times 10^{-4}$。 | 最明确的偶偶核宇称双重态 + 相对 E1 强度基准。 |
| $^{224}$Th | $K=0^+$ 基带与候选 $K=0^-$ 带（$1^-$ 251.0 keV，$3^-$ 305.3 keV）。 | 多条 E1 带间跃迁；如 $3^-\to 2^+$ 207.2 keV。 | 评价给出 $D_0/Q_0 = (6.7$–$10.0)\times 10^{-4}\text{ fm}^{-1}$。 |
| $^{226}$Th | $K=0^+$ 基带；$K=0^-$ 八极振动带（$1^-$ 230.37 keV，$3^-$ 307.5 keV）。 | $1^-\to 0^+$ 230.37 与 $1^-\to 2^+$ 158.18 keV 强 E1。 | 缺寿命数据，不能从 NNDC 表单独反演绝对 $B(E1)$。 |

---

## Provisional Reasoning

### 1. Coriolis 解耦代数与 $K$ 依赖性

轴对称强耦合转子—粒子哈密顿量的 Coriolis 部分来自：
$$H_{\text{rot}} = A \left[ \vec{I}^2 + \vec{j}^2 - 2I_3 j_3 - I_+ j_- - I_- j_+ \right],\qquad A = \frac{\hbar^2}{2\mathcal{J}}$$
在对称化内禀态 $|\phi_K\rangle$ 上，$j_\pm$ 仅改变内禀投影 $K$ 一个单位（$\Delta K = \pm 1$）。
- 当 $K=1/2$ 时，$K \leftrightarrow -K$ 仅相隔 1 个单位，一次 Coriolis 操作即可直接耦合 $\pm K$，产生一阶对角解耦项：
  $$E_{K=1/2}(I) = A [I(I+1) + a (-1)^{I+1/2}(I+1/2)] + c$$
  在内禀反射不对称下，$a^+ \approx -a^-$ 导致能量差随自旋激荡变号；
- 当 $K=3/2$ 时，$K \leftrightarrow -K$ 相隔 3 个单位，一次 Coriolis 操作无法闭合矩阵元，故 **一阶对角解耦参数严格为 $a \equiv 0$**：
  $$E_{K=3/2}(I) = A [I(I+1) - K^2] + c$$
  宇称双重态劈裂演化为主导平滑形式：
  $$\Delta_{+-}(I) = \Delta_0 + (A_+ - A_-)[I(I+1) - K^2]$$
  这在微观机制上阐明了为何 $^{225}\text{Ac}$ 的宇称劈裂呈现平滑单调特征。

### 2. 偶偶核与奇核八极激发谱系的物理分界

偶偶 Th 核不存在奇核子解耦项，$K=0^-$ 与 $K=0^+$ 的交替排列反映了内禀轴对称反射破缺势阱中的宇称反演对偶；带间 $E1$ 跃迁反映了质子与中子质量/电荷中心的分离。随着中子数从 $N=130$（$^{220}\text{Th}$）向 $N=136$（$^{226}\text{Th}$）增加，八极极小逐步加深并在 $^{224,226}\text{Th}$ 达到集体度极值。

---

## Assumptions

假定核能谱满足轴对称强耦合粒子-转子模型；假定低激发态纯度受高阶 $\Delta K = \pm 1$ 混合干扰较小；假定 NNDC 评价数据中的自旋宇称指认在基准区间可靠。

## Competing Explanations

1. 稳定反射不对称双阱模型：预言近简并宇称双重态，旋称交错完全由 Coriolis 解耦项决定；
2. 八极对振动与转动耦合模型：低能带为微扰八极声子与四极转动带耦合，随着角动量增大能级位移逐渐收敛；
3. 形状共存模型：相反宇称带属于具备不同四极变形的侵入组态。

## Transfer Conditions

$a=0$ 对角解耦消失定理严格适用于所有纯 $K \ge 3/2$ 轴对称带；当核具备显著三轴非对称度（$\gamma \neq 0$）或存在强两带组态交叉时，非对角 Coriolis 混合可产生表观能级反转。

## Failure Conditions

若在纯 $K=3/2$ 孤立带中观测到明确的 $(-1)^{I+1/2}$ 符号交替震荡，则纯轴对称强耦合假设失效；若在 $^{226}\text{Th}$ 中测得基态带与负宇称带间无电偶极跃迁，则八极反射非对称图像失效。

## Falsification or Reverse Tests

运行工件 `ac225-ra225-th220-226-parity-doublet-coriolis-boundary.py`，再现 $^{225}\text{Ac}$ 的平滑劈裂与 $^{225}\text{Ra}$ 的交错拟合，结果与 7 份官方 ENSDF 数据核对固化于 `ac225-ra225-th220-226-parity-doublet-coriolis-boundary.json`。

## Open Questions

在 $^{225}\text{Ac}$ 高自旋端（$I \ge 11/2$），二阶 Coriolis 混合如何诱发负宇称带与近邻 $K=5/2$ 带的组态竞争？

## Human Review

本笔记由 Codex L4 全自动研学推导建立，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 正式研学要求创建，确立锕系奇 A 与偶偶核八极宇称伙伴的 Coriolis 解耦边界。
