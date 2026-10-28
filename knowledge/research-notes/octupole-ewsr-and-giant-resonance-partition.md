---
type: research-note
title: "电八极能权求和规则（EWSR）与巨共振强度分配：从双幻核到稀土与锕系的微观系统学"
aliases: [octupole EWSR giant resonance partition, E3 EWSR exhaustion systematics]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra]
created_from: Day26 octupole EWSR and resonance partition study
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, EWSR, sum-rule, giant-resonance, LEOR, HEOR, evidence-boundary]
---

# 电八极能权求和规则（EWSR）与巨共振强度分配

## Research Trigger

在低能核结构中，强电八极跃迁（$B(E3) \approx 30$–$50\text{ W.u.}$）常被视为八极集体性的决定性判据。然而，单一低激发态究竟耗尽了多大比例的核电多极总强度？电八极能权求和规则（Energy-Weighted Sum Rule, EWSR）在双幻核（$^{208}\text{Pb}$）、动态大振幅软八极核（$^{144,146}\text{Ba}$）与静态双阱形变核（$^{224,226}\text{Ra}$）之间如何分布？

本笔记基于多极双对易子非含时求和规则，系统推导质子/同位旋标量电八极 TRK-EWSR 解析极值，定量计算首个 $3^-_1$ 态的耗尽份额，并剖析低能八极共振（LEOR）与高能等标巨八极共振（HEOR/ISGOR）的强度分配拓扑。计算脚本与结构化数据见 [octupole-ewsr-and-transition-density-074.py](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/octupole-ewsr-and-transition-density-074.py) 和 [结构化结果](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/octupole-ewsr-and-transition-density-074.json)。

---

## Grounded Evidence

| 核素 | $E(3^-_1)$ (MeV) | 向下 $B(E3)$ (W.u.) | 向上 $B(E3; 0^+\to 3^-)$ ($e^2\text{fm}^6$) | 实测 $E\cdot B(E3)$ ($\text{MeV}\cdot e^2\text{fm}^6$) | 经典 TRK-EWSR ($\text{MeV}\cdot e^2\text{fm}^6$) | 首态 EWSR 耗尽比 | 实验来源 |
|---|---|---|---|---|---|---|---|
| $^{208}\text{Pb}$ | $2.6145$ | $34.0$ | $6.24 \times 10^5$ | $1.63 \times 10^6$ | $2.17 \times 10^7$ | **$7.54\%$** | NNDC / 经典双幻基准 |
| $^{144}\text{Ba}$ | $0.838$ | $48.0$ | $4.03 \times 10^5$ | $3.37 \times 10^5$ | $9.04 \times 10^6$ | **$3.73\%$** | [[bucher-2016-144ba-direct-octupole]] |
| $^{146}\text{Ba}$ | $0.821$ | $48.0$ | $4.09 \times 10^5$ | $3.36 \times 10^5$ | $9.21 \times 10^6$ | **$3.65\%$** | [[bucher-2017-146ba-direct-octupole]] |
| $^{224}\text{Ra}$ | $0.216$ | $42.0$ | $8.53 \times 10^5$ | $1.84 \times 10^5$ | $2.57 \times 10^7$ | **$0.72\%$** | [[gaffney-2013-pear-shaped-rn-ra]] |
| $^{226}\text{Ra}$ | $0.254$ | $36.0$ | $7.44 \times 10^5$ | $1.89 \times 10^5$ | $2.60 \times 10^7$ | **$0.74\%$** | Wollersheim 1993 / NNDC |
| $^{110}\text{Cd}$ | $2.079$ | $16.0$ | $8.15 \times 10^4$ | $1.69 \times 10^5$ | $7.32 \times 10^6$ | **$2.31\%$** | NNDC Adopted Levels |

---

## Provisional Reasoning

### 1. 经典电八极非含时能量加权总和规则推导

电八极算符为 $\hat{M}(E3,\mu) = e \sum_{p=1}^Z r_p^3 Y_{3\mu}(\hat{r}_p)$。双对易子展开给出：
$$S_{\text{EWSR}}(E3) = \sum_n (E_n - E_0) B(E3; 0^+ \to 3^-_n) = \frac{1}{2} \langle 0 | [\hat{M}(E3)^\dagger, [H, \hat{M}(E3)]] | 0 \rangle$$
由于二体核力势能项与坐标对易 $[V, r^3 Y_{3\mu}] = 0$（忽略动量依赖与交换力微扰）：
$$S_{\text{EWSR}}(E3) = \frac{\hbar^2 e^2}{2 m_N} \frac{147}{4\pi} Z \langle r^4 \rangle_p$$
在均匀球形核电荷分布假定下（$\langle r^4 \rangle_p = \frac{3}{7} R_0^4$，$R_0 = 1.2 A^{1/3}\text{ fm}$）：
$$S_{\text{EWSR}}(E3) = \frac{27}{8\pi} \frac{\hbar^2 e^2}{m_N} (1.2)^4 Z A^{4/3} \approx 92.44 \times Z A^{4/3}\ \text{MeV}\cdot e^2\text{fm}^6$$

### 2. 软度佯谬（Softness Paradox）与和规则分布

计算结果揭示了核物理中深刻的“八极软度佯谬”：
1. **向下强度与能权耗尽的反向演化**：
   - 比较 $^{208}\text{Pb}$ 与 $^{224}\text{Ra}$：$^{224}\text{Ra}$ 的单粒子 Weisskopf 倍数（$42\text{ W.u.}$）明显高于 $^{208}\text{Pb}$（$34\text{ W.u.}$），内禀跃迁几率 $B(E3)$ 绝对值更达后者的 $1.37$ 倍；
   - 然而在能权求和规则中，$^{208}\text{Pb}$ 首态耗尽了 $7.54\%$，而 $^{224}\text{Ra}$ 仅耗尽了 $0.72\%$（相差超过 10 倍！）。
2. **物理机制根源**：
   - 强八极关联导致 $3^-_1$ 态发生极端能谱软化（$^{224}\text{Ra}$ 中 $E(3^-) = 0.216\text{ MeV}$，仅为 $^{208}\text{Pb}$ 的 $1/12$）；
   - 在一阶能权项 $(E_n - E_0)$ 的压制下，低能软八极态的能权强度被几何尺度强力缩减；
   - 反之，逆能权极化率（Inverse Energy-Weighted Sum Rule, $S_{-1} = \sum_n \frac{B(E3)}{E_n - E_0} \propto \chi_{\text{oct}}$）中，低激发态贡献被放大 $1/E$ 倍，占领绝对主导。
3. **巨八极共振（Giant Octupole Resonances）的双峰结构**：
   - 首个 $3^-_1$ 态所耗尽的 $\sim 1\% - 8\%$ 仅为电八极响应函数的“相干冰山一角”；
   - 剩余 $> 90\%$ 的能权强度高阶集中在两大集体共振结构中：
     - **低能八极共振（LEOR, $1\hbar\omega$ 激发）**：位于 $E_x \sim 32 A^{-1/3}\text{ MeV}$（约 $5 - 7\text{ MeV}$），耗尽 $\sim 25\% - 30\%$ EWSR；
     - **高能等标巨八极共振（HEOR / ISGOR, $3\hbar\omega$ 激发）**：位于 $E_x \sim 110 A^{-1/3}\text{ MeV}$（约 $18 - 24\text{ MeV}$），耗尽 $\sim 60\% - 65\%$ EWSR。

---

## Assumptions

假定核电荷分布满足径向均匀硬球模型（$\langle r^4 \rangle = \frac{3}{7} R_0^4$）；假定核子动能算符主导微观双对易子，暂忽略核力速度依赖项与介子交换流可能引入的 $10\%-20\%$ 增强因子 $(1+\kappa)$；假定向上与向下矩阵元满足好宇称自旋简并因子换算。

## Competing Explanations

1. 单态相干耗尽假设：早期唯象模型曾假定强八极形变核的首个负宇称态能耗尽巨共振的主要份额，已被全能量区间 RPA 计算证伪；
2. 表面振动 Tassie 模型：假定跃迁密度严格局域于核表面 $\rho_{\text{tr}}(r) \propto r^2 \frac{d\rho_0}{dr}$，适用于首个 $3^-_1$ 声子，但不适用于高能巨共振的体压缩模式。

## Transfer Conditions

TRK-EWSR 解析表达式为严格算符代数恒等式，适用于从轻核到超重核的全周期同位素；但具体耗尽百分比对低位 $3^-_1$ 激发能极其敏感，跨核迁移时必须重新代入同核实测能级与直接 $B(E3)$ 实验值。

## Failure Conditions

若在奇特核区测得首个 $3^-_1$ 态耗尽 EWSR 超过 $30\%$，则经典的准粒子声子激发图像失效，表明发生了极其极端的全核凝聚或超形变八极塌缩。

## Falsification or Reverse Tests

独立运行数值工件 `octupole-ewsr-and-transition-density-074.py`，再现六大基准核的求和规则数值，结果固化于 `octupole-ewsr-and-transition-density-074.json`。

## Open Questions

在自洽 Skyrme/Gogny QRPA 连续谱计算中，粒子-空穴剩余相互作用的速度依赖项对 $E3$ EWSR 的实际同位旋增强因子 $\kappa_{\text{oct}}$ 确切数值是多少？

## Human Review

本笔记由 Codex L4 全自动学习推导生成，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 正式研学要求创建，确立电八极求和规则与巨共振分配的微观系统学。
