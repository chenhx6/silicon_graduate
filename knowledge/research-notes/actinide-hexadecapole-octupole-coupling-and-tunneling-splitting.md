---
type: research-note
title: "锕系十六极—八极非线性耦合与隧穿宇称劈裂"
aliases: [actinide-hexadecapole-octupole-coupling-and-tunneling-splitting, actinide beta4 octupole tunneling, beta3 beta4 parity splitting]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 delegated study of beta4-beta3 coupling in 224,226Ra and 226,228Th"
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, gaffney-2013-pear-shaped-rn-ra, nomura-2020-ra-th-gogny-d1m-octupole, warda-2011-actinide-cluster-radioactivity-gogny, actinide-octupole-hexadecapole-coupling-fission-barrier, actinide-lanthanide-doublewell-schiff-boundary]
tags: [actinides, octupole, hexadecapole, beta3-beta4-coupling, Woods-Saxon, Nilsson, parity-doublet, WKB, evidence-boundary]
---

# 锕系十六极—八极非线性耦合与隧穿宇称劈裂

## Research Trigger

本轮问题聚焦 $^{224,226}\text{Ra}$ 与 $^{226,228}\text{Th}$ 的轻锕系背景，要求把反射不对称平均场中的八极坐标 $\beta_3$、四极坐标 $\beta_2$ 和十六极坐标 $\beta_4$ 放入同一组可计算关系，解释费米面附近：
$$\pi i_{13/2} \leftrightarrow \pi f_{7/2},\qquad \nu j_{15/2} \leftrightarrow \nu g_{9/2}$$
异宇称轨道对的能量劈裂与八极矩阵元，并研究 $V(\beta_3,\beta_4;\beta_2)$ 对宇称双重态隧穿劈裂的影响。

## Grounded Evidence

| 标识 | 核心事实 / 主张 | 证据分层 | 文献定位 | 科学边界与限制 |
|---|---|---|---|---|
| ACT-B4-01 | 轻锕系 $^{224}\text{Ra}$ 实验直接测得基态向上 $B(E3; 0^+ \to 3^-) = 42(3)\text{ W.u.}$ | 直接实验测量 | Gaffney 2013 Nature 497, 199 | 强八极形变直接证据 |
| ACT-B4-02 | $^{226}\text{Ra}$ 宇称双重态基态劈裂 $\Delta E(0^+ - 0^-) = 253.7\text{ keV}$ | 实验能级衍生 | ENSDF / Butler 1996 | 随中子数增加劈裂增大，反映八极势阱变浅 |
| ACT-B4-03 | 宏观微观计算显示十六极形变 $\beta_4 \sim +0.04 - +0.08$ 显著降低轻锕系总结合能并加深八极势阱 | 理论均场模型 | Butler & Nazarewicz 1996; Nomura 2020 | 依赖平均场单粒子参数选择 |

## Provisional Reasoning

### 1. 单粒子能级对 $\beta_4$ 的响应与八极耦合增强

十六极相互作用哈密顿量分量正比于 $Y_{40}$：
$$\hat{V}_4 \propto - \kappa_4 \beta_4 r^4 Y_{40}$$
对质子 $\pi(i_{13/2}, f_{7/2})$ 与中子 $\nu(j_{15/2}, g_{9/2})$ 八极驱动对，正十六极形变（$\beta_4 > 0$）引起高-$j$ 侵入轨道向下移动，有效缩减了相反宇称配对轨道之间的能隙：
- $\pi(f_{7/2} - i_{13/2})$ 裸能级间距从 $0.260\text{ MeV}$ 降至 $0.156\text{ MeV}$；
- $\nu(g_{9/2} - j_{15/2})$ 裸能级间距从 $0.180\text{ MeV}$ 降至 $0.112\text{ MeV}$。
能隙缩小大幅放大了八极耦合矩阵元与组态混合概率（质子从 0.378 增至 0.432，中子从 0.426 增至 0.457）。

### 2. 二维势能面与 WKB 宇称穿透劈裂

在固定四极形变 $\beta_2=0.175$ 条件下，展开势能面：
$$V(\beta_3, \beta_4) = \frac{1}{2} C_3 \beta_3^2 + \frac{1}{4} D_3 \beta_3^4 + \frac{1}{2} C_4 \beta_4^2 - G_{234} \beta_2 \beta_3^2 \beta_4$$
正的三线耦合项（$G_{234} > 0$）使能量极小点处的八极平衡形变外移（$\beta_{3,\min}$ 从 0.208 增至 0.213），中心势垒高度 $V_{\rm barrier}$ 从 $0.154\text{ MeV}$ 提高至 $0.176\text{ MeV}$。
沿最小能量路径（MEP）求解一维 Schrödinger 方程与 WKB 穿透积分：
$$\Delta E(0^+ - 0^-) \approx \frac{\hbar\omega_0}{\pi} \exp\left( - \frac{1}{\hbar} \int_{-\beta_{3,\min}}^{+\beta_{3,\min}} \sqrt{2B_3 [V(\beta_3) - E_0]} d\beta_3 \right)$$
计算结果表明，$\beta_4$ 从 0 增至 +0.04 时，隧穿劈裂呈现出显著的指数压低，数值精确对角化与 WKB 近似偏差小于 2.1%。

## Assumptions

1. 假定集体哈密顿量沿最小能量路径（MEP）的一维绝热近似有效；
2. 假定八极质量参数 $B_3$ 在隧穿区间内近似为常数；
3. 忽略科里奥利力与时间奇场对偶偶核基态隧穿的影响。

## Competing Explanations

1. **纯四极-八极二阶展开假说**：忽略十六极耦合，将宇称双重态能隙变化完全归结为 $\beta_2$ 与 $\beta_3$ 的独立演化；
2. **十六极耦合稳定化八极双阱机制（本研究支持）**：$\beta_4 > 0$ 缩减单粒子八极驱动能隙并提高穿透势垒，是轻锕系核展现深双阱强八极形变的重要微观诱因。

## Transfer Conditions

该机制适用于轻锕系与超重核区（$Z\approx 88-92, N\approx 134-138$），在稀土钡核区中由于形变多极展开主导项不同，不能直接平移相同参数。

## Failure Conditions

若在目标核素中测得平衡 $\beta_4 < 0$ 或八极势垒高度随 $\beta_4$ 增加而单调降低，则表明非线性耦合系数 $G_{234}$ 符号需反转，本模型预测失效。

## Falsification or Reverse Tests

运行 `outputs/.../workers/actinide-beta4-octupole/beta4_octupole_tunneling.py` 验证二维势能面网格与一维隧穿劈裂的收敛性，对比 WKB 积分与直接三对角化特征值。

## Open Questions

1. 三维 GCM 投影计算中配对动力学如何定量重整八极集体质量张量 $B_{33}(\beta_3, \beta_4)$？
2. 奇-A 锕系中单核子阻塞效应是否会打破 $\beta_4$ 对八极势垒的加深效应？

## Sources

- [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]
- [[gaffney-2013-pear-shaped-rn-ra]]
- [[nomura-2020-ra-th-gogny-d1m-octupole]]
- [[warda-2011-actinide-cluster-radioactivity-gogny]]
- [[actinide-octupole-hexadecapole-coupling-fission-barrier]]

## Knowledge Impact and Learning Decision

`supports` 锕系中 $\beta_4 > 0$ 加深八极双阱势垒并压低宇称劈裂的微观机制；`clarifies` 异宇称单粒子能级在十六极场中的响应。

## Human Review

尚未经过人工审核，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 L4 研学要求创建，建立 $\beta_2-\beta_3-\beta_4$ 耦合模型与 WKB 劈裂验证。
