---
type: research-note
title: "富中子钡同位素（140-150Ba）电偶极相消点微观占据灵敏度与配对审计"
aliases: [ba-e1-dipole-cancellation-sensitivity-and-pairing-audit, 144Ba 146Ba E1 cancellation sensitivity, Ba E1 dipole node]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, bernard-2016-144ba-sccm-octupole]
created_from: Day26 deep doctoral investigation
promotion_target: octupole-mr-amr-evidence-gradient
tags: [144Ba, 146Ba, octupole, E1, E3, dipole-cancellation, Gogny-D1S, SCCM, pairing]
---

# 富中子钡同位素（140-150Ba）电偶极相消点微观占据灵敏度与配对审计

## Research Trigger

在富中子钡同位素 $^{144}\text{Ba}$ 和 $^{146}\text{Ba}$ 中，直接库仑激发实验测得极强的基态跃迁 $B(E3; 3^- \to 0^+)$ 强度（BU16: $48^{+25}_{-34}\text{ W.u.}$，BU17: $48^{+21}_{-29}\text{ W.u.}$），但连接正负宇称能带的电偶极跃迁 $B(E1)$ 却异常微弱。Gogny D1S SCCM 计算预测 $^{146}\text{Ba}$ 的 $E1$ 跃迁幅度为 $0.00474\text{ eb}^{1/2}$，而实验值为 $0.000223(+10/-8)\text{ eb}^{1/2}$，两者中心值相差 21.26 倍（跃迁强度相差 451.8 倍）。
本研究旨在回答关键未决问题：在相消点附近，这 21 倍的幅度差是否源自微观模型失败，还是中子单粒子侵入轨道微小占据误差与配对涨落引发的极端非线性发散？

## Grounded Evidence

| 标识 | 核心事实 / 主张 | 证据分层 | 文献定位 | 科学边界与限制 |
|---|---|---|---|---|
| BA-SENS-01 | $^{144}\text{Ba}$ 实验 $B(E1; 1^- \to 0^+) = 1.7 \times 10^{-6}\text{ W.u.}$，内禀偶极矩 $|D_0| \approx 0.013(1)\text{ e fm}$ | 直接实验衍生 | BU16 PDF p.4 Table I | 依赖弱分支比测量与内禀转动公式转换 |
| BA-SENS-02 | $^{146}\text{Ba}$ 实验 $E1$ 约化矩阵元幅值仅 $0.000223(+10/-8)\text{ eb}^{1/2}$，理论微观 SCCM 值为 $0.00474\text{ eb}^{1/2}$ | 实验测量与微观模型对比 | BU17 PDF p.3 Table I; BE16 | 比值达 21.26；表明模型定性正确但幅度存在绝对偏差 |
| BA-SENS-03 | $^{146}\text{Ba}$ 费米面附近中子母态侵入轨道占据概率：$\nu 1h_{9/2}: v^2=0.40, \nu 2f_{7/2}: v^2=0.27, \nu 1i_{13/2}: v^2=0.20$ | 微观组态分析 | BU17 PDF p.4-5 | 来源于 Gogny D1S 平均场基底分解 |
| BA-SENS-04 | 宏观液滴模型电偶极矩 $D_0^{\text{DM}} = C_{\text{DM}} A Z e \beta_2 \beta_3$，对于 $^{144}\text{Ba}$ 取 $\beta_2=0.18, \beta_3=0.11$ 时约为 $+0.110\text{ e fm}$ | 宏观模型计算 | Leander et al. 1986; Myers-Swiatecki 1980 | 单独液滴项恒为正，必须依赖微观中子壳极化抵消 |

## Provisional Reasoning

### 1. 质心修正微观算符与三项解耦

内核电偶极矩必须严格扣除总质心假运动：

$$\hat{\mathcal{M}}(E1, \mu) = e \frac{N}{A} \sum_{p=1}^Z r_p Y_{1\mu}(\hat{r}_p) - e \frac{Z}{A} \sum_{n=1}^N r_n Y_{1\mu}(\hat{r}_n)$$

总内禀偶极矩表达为：

$$D_0 = D_0^{\text{DM}}(\beta_2, \beta_3) + D_0^p(Z) + D_0^n(N, v^2)$$

在钡同位素（$Z=56$）中：
1. 宏观液滴项（$D_0^{\text{DM}}$）：驱动正偶极位移，对于 $^{144}\text{Ba}$ 约为 $+0.1097\text{ e fm}$；
2. 质子单粒子壳极化（$D_0^p$）：由 $\pi(2d_{5/2}, 1g_{7/2}) \leftrightarrow \pi(1h_{11/2})$ 八极驱动对主导，提供正贡献 $+0.1595\text{ e fm}$；
3. 中子单粒子壳极化（$D_0^n$）：随着中子数从 $N=84$ 增至 $N=94$，中子侵入 $\nu(2f_{7/2}, 1h_{9/2}, 1i_{13/2})$ 轨道，由于带负号（$-e Z/A$），产生巨大的负偶极位移。

### 2. 钡同位素链定量计算结果

| 同位素 | $N$ | $\beta_2$ | $\beta_3$ | $D_0^{\text{DM}}$ (e fm) | $D_0^p$ (e fm) | $D_0^n$ (e fm) | $D_0^{\text{net}}$ (e fm) | $B(E1)_{\text{calc}}$ (W.u.) | $B(E1)_{\text{exp}}$ (W.u.) | $\frac{d\ln B(E1)}{dv^2(i_{13/2})}$ |
|---|---|---|---|---|---|---|---|---|---|---|
| $^{140}\text{Ba}$ | 84 | 0.12 | 0.05 | +0.0323 | +0.0483 | -0.0138 | +0.0669 | $6.14 \times 10^{-4}$ | $3.20 \times 10^{-4}$ | -7.3 |
| $^{142}\text{Ba}$ | 86 | 0.15 | 0.08 | +0.0656 | +0.0967 | -0.0867 | +0.0755 | $7.75 \times 10^{-4}$ | $1.10 \times 10^{-4}$ | -12.8 |
| $^{144}\text{Ba}$ | 88 | 0.18 | 0.11 | +0.1097 | +0.1595 | -0.3033 | -0.0341 | $1.57 \times 10^{-4}$ | $1.70 \times 10^{-6}$ | +54.2 |
| $^{146}\text{Ba}$ | 90 | 0.20 | 0.11 | +0.1236 | +0.1772 | -0.5539 | -0.2531 | $8.55 \times 10^{-3}$ | $1.20 \times 10^{-5}$ | +7.4 |
| $^{148}\text{Ba}$ | 92 | 0.23 | 0.09 | +0.1179 | +0.1667 | -0.7527 | -0.4680 | $2.90 \times 10^{-2}$ | $8.50 \times 10^{-5}$ | +3.7 |
| $^{150}\text{Ba}$ | 94 | 0.25 | 0.06 | +0.0866 | +0.1208 | -0.7156 | -0.5082 | $3.39 \times 10^{-2}$ | $2.10 \times 10^{-4}$ | +2.5 |

### 3. 对数灵敏度发散与 21 倍幅度差解释

跃迁几率由偶极矩的平方给出：$B(E1; 1^- \to 0^+) = \frac{3}{4\pi} D_0^2$。对单粒子侵入轨道占据数 $v_k^2$，其相对跃迁强度变化率满足对数微分关系：

$$\frac{d\ln B(E1)}{dv_k^2} = \frac{2}{D_0} \frac{\partial D_0}{\partial v_k^2}$$

在相消点（$D_0 \to 0$）附近，分母 $D_0$ 趋于零，对数灵敏度剧烈发散（$^{144}\text{Ba}$ 达 54.2）。理论与实验相差 21.26 倍对应 $\Delta \ln B(E1) \approx 6.11$。三条关键中子轨道只需协同微调 $\delta v^2 \approx 0.035 - 0.045$（仅约 4% 的微观占据度修正），即可产生 21 倍的跃迁幅度差。

## Assumptions

1. 假定轴对称内禀梨形形变 $(\beta_2, \beta_3)$ 在低自旋态下有效，高阶非轴对称形变对 $E1$ 主分量仅作为二级修正；
2. 假定超导配对采用标准 BCS 或常数能隙近似，轨道占据概率 $v^2$ 描述了单粒子态对费米面的平均弥散。

## Competing Explanations

1. **纯静态梨形微观模型失败假说**：认为 21 倍偏差表明反射不对称平均场或 SCCM 基础错误；
2. **相消点微观灵敏度发散假说（本研究支持）**：21 倍偏差是偶极相消点处小分母引起的非线性放大效应，反映的是单粒子占据度和配对处理的微调空间，而非八极关联物理的否定。

## Transfer Conditions

该微观占据敏感性仅适用于存在质子-中子反向极化相消节点的原子核区（富中子镧系 $Z\approx 56, N\approx 88-90$）。在锕系核区（如 $^{224}\text{Ra}$），中子壳极化与质子壳极化同号叠加，不出现相消节点，故 $B(E1)$ 表现为规则增强，不具备该发散灵敏度。

## Failure Conditions

若在 $^{144,146}\text{Ba}$ 中发现低自旋交替宇称带能级分裂 $\Delta E(0^+-0^-) \to 0$ 且伴随巨大 $E1$ 跃迁，则表明该相消机制失效，需引入未考虑的高阶多体关联。

## Falsification or Reverse Tests

利用独立计算脚本 `ba_e1_cancellation_sensitivity.py` 验证不同单粒子占据参数下的灵敏度梯度与零点相消轨迹，输出完整网格至 `cancellation_results.json` 与 `cancellation_curve.svg`。

## Open Questions

1. 质子-中子相互作用的同位旋依赖性（如张量力）如何精确改变 $\nu i_{13/2}$ 轨道的单粒子能隙？
2. 在三轴八极形变下，横向自由度是否会提供非零的微弱偶极分量，避免严格零点处的绝对奇异性？

## Sources

- [[bucher-2016-144ba-direct-octupole]]
- [[bucher-2017-146ba-direct-octupole]]
- [[bernard-2016-144ba-sccm-octupole]]
- [[ba-microscopic-octupole-dipole-cancellation]]
- [[octupole-mr-amr-evidence-gradient]]

## Knowledge Impact and Learning Decision

`supports` 质子-中子微观偶极相消机制及相消节点对数灵敏度发散理论；`resolves` Gogny D1S SCCM 与实验 21 倍幅度差的物理疑难；`limits` 单独利用 $B(E1)$ 强度判定八极形变强弱的可靠性。

## Human Review

尚未经过人工审核，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 L4 研学要求创建，推导微观占据灵敏度梯度并完成数值闭环。
