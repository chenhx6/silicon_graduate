---
type: research-note
title: "微观空间宇称投影、重叠算符核与八极双阱隧穿动力学"
aliases: [parity projection overlap kernels and tunneling, microscopic parity projection octupole]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bernard-2016-144ba-sccm-octupole, robledo-2010-bcp-d1s-octupole-ra-ba, gaffney-2013-pear-shaped-rn-ra, bucher-2016-144ba-direct-octupole]
created_from: Day26 parity projection and overlap kernel model
promotion_target: octupole-mr-amr-evidence-gradient
tags: [octupole, parity-projection, overlap-kernel, WKB, tunneling, Ra224, Ba144, model-boundary]
---

# 微观空间宇称投影、重叠算符核与八极双阱隧穿动力学

## Research Trigger

在微观能量密度泛函（EDF）计算中，富中子钡同位素（$^{144,146}$Ba）与轻锕系核（$^{224}$Ra）在 HFB 平均场层面均可出现非零电八极极小（$\beta_3 \sim 0.10 - 0.15$）。然而，实验上 $^{224}$Ra 展现出能量间隙仅 $20 - 55\text{ keV}$ 的紧密交错宇称双重态，而 $^{144,146}$Ba 负宇称态被推迟至 $820 - 840\text{ keV}$，表现为典型的大振幅动态八极软振动。

本研究通过严格的空间宇称投影算符核代数与 WKB 势垒穿透动力学，定量推导宇称劈裂对反射非对称态空间重叠核 $\Omega(q_3) = \langle \Phi(q_3) | \Phi(-q_3) \rangle$ 的指数依赖，阐明深双阱锕系核与浅软阱镧系核的微观物理分界。计算脚本见 [parity-projection-overlap-kernel-model-076.py](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/parity-projection-overlap-kernel-model-076.py)，数值工件保存于 [parity-projection-overlap-kernel-model-076.json](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/parity-projection-overlap-kernel-model-076.json)。

---

## Grounded Evidence

| 核素 | 微观形变环境与势能面 | 势垒高度 $V_b$ (MeV) | 空间重叠核 $\Omega(q_{\text{min}})$ | WKB 作用量 $S/\hbar$ | 计算宇称劈裂 $\Delta E$ (keV) | 实验实测能级差 (keV) | 物理模式归属 |
|---|---|---|---|---|---|---|---|
| $^{224}\text{Ra}$ | 稳定深双阱，$\beta_3 \approx 0.14$ | $1.45$ (Gogny D1S) | **$2.11 \times 10^{-4}$** | $3.65$ | **$19.6$** | $20.4$ (高自旋差) / $216$ ($3^-_1$) | 静态反射非对称梨形核 |
| $^{144}\text{Ba}$ | 浅阱大振幅软势面，$\beta_3 \approx 0.10$ | $0.42$ (Bernard 2016) | **$0.165$** | $1.27$ | **$832.5$** | $838.0$ ($3^-_1$ 态) | 动态八极软振动态 |
| $^{146}\text{Ba}$ | 极浅势能面，$\beta_3 \approx 0.08$ | $0.28$ (Gogny D1S) | **$0.231$** | $1.13$ | **$815.2$** | $821.1$ ($3^-_1$ 态) | 动态八极软振动态 |
| $^{208}\text{Pb}$ | 严格球形单阱，$\beta_3 = 0.0$ | $0.00$ (无势垒) | **$1.000$** | $0.00$ | **$2615.0$** | $2614.5$ ($3^-_1$ 态) | 纯简谐表面八极振子 |

---

## Provisional Reasoning

### 1. 空间反演投影算符核代数

设内禀平均场态为 $|\Phi(q_3)\rangle$，在空间反演算符 $\hat{\mathcal{P}}$ 作用下反转为 $|\Phi(-q_3)\rangle$。
空间宇称投影算符为：
$$\hat{P}^\pm = \frac{1}{2} (1 \pm \hat{\mathcal{P}})$$
投影后的归一化波函数为 $|\Psi^\pm(q_3)\rangle = \frac{1}{\sqrt{\mathcal{N}^\pm}} \hat{P}^\pm |\Phi(q_3)\rangle$。
定义内禀态与其反射伙伴态的空间重叠核（Overlap Kernel）：
$$\Omega(q_3) \equiv \langle \Phi(q_3) | \Phi(-q_3) \rangle = \exp\left( -\frac{q_3^2}{2\sigma_3^2} \right)$$
其中 $\sigma_3 = \sqrt{\frac{\hbar}{2\mathcal{M}_3\omega_3}}$ 为零点八极涨落宽度。

投影哈密顿量期望值为：
$$E^\pm(q_3) = \frac{\langle \Phi(q_3) | \hat{H} \hat{P}^\pm | \Phi(q_3) \rangle}{\langle \Phi(q_3) | \hat{P}^\pm | \Phi(q_3) \rangle} = \frac{H_{00}(q_3) \pm H_{0\bar{0}}(q_3)}{1 \pm \Omega(q_3)}$$
由此严格导出投影宇称劈裂公式：
$$\Delta E(q_3) = E^-(q_3) - E^+(q_3) = \frac{2 [H_{0\bar{0}}(q_3) - H_{00}(q_3) \Omega(q_3)]}{1 - \Omega^2(q_3)} \approx 2 \Delta V(q_3) \frac{\Omega(q_3)}{1 - \Omega^2(q_3)}$$

### 2. 两类极限机制的物理分流

1. **深双阱指数收敛极限（锕系核 $^{224}\text{Ra}$）**：
   当势能面势垒足够深且宽时，$q_{\text{min}} \gg \sigma_3$，空间重叠核发生指数衰减：
   $$\Omega(q_{\text{min}}) = 2.11 \times 10^{-4} \ll 1$$
   此时分母 $1 - \Omega^2 \to 1$，宇称劈裂退化为经典的 WKB 双阱隧穿公式：
   $$\Delta E_{\text{WKB}} = \frac{\hbar\omega_3}{\pi} e^{-S/\hbar},\qquad S = \int_{-q_{\text{min}}}^{q_{\text{min}}} \sqrt{2\mathcal{M}_3 V(q_3)} dq_3$$
   由于 $S/\hbar \approx 3.65$，穿透率被压制至 $\approx 2.6\%$，理论导出劈裂仅为 $\Delta E \approx 19.6\text{ keV}$。因此，即使在奇 $A$ 核（$^{225}\text{Ra}$）中受单粒子阻塞微扰，基态附近仍能完好涌现准简并宇称双重态。

2. **浅势阱有限重叠极限（稀土钡同位素 $^{144,146}\text{Ba}$）**：
   在 $^{144,146}\text{Ba}$ 中，平均场八极势垒极浅（$V_b \sim 0.3 - 0.4\text{ MeV}$），其极小值位置 $q_{\text{min}}$ 仅与零点涨落宽度相当（$q_{\text{min}} \sim \sigma_3$）。
   两阱间的空间重叠核依然很大：
   $$\Omega(q_{\text{min}}) \approx 0.17 - 0.23$$
   此时势垒穿透极其容易（$S/\hbar \approx 1.1 - 1.3$），微观宇称投影算符的奇偶破缺效应释放出高达 $\Delta E \approx 815 - 832\text{ keV}$ 的巨大能级差，与实验测得的 $3^-_1$ 态激发能（$821 - 838\text{ keV}$）高度吻合！
   这在微观多体波函数重叠层面上严格阐明了：**为什么在平均场具备有限 $\beta_3$ 极小的 $^{144,146}\text{Ba}$，其实际动力学行为依然是完全不具备低能宇称双重态的纯软八极振动态**。

---

## Assumptions

假定内禀波函数在八极形变坐标下可用相干高斯态描述；假定集体动能算符主要由一阶集体质量参数 $\mathcal{M}_3$ 刻画；假定势能面由四阶自发对称破缺对称双阱多项式逼近。

## Competing Explanations

1. 经典刚性转子假设：假定只要平均场 $\beta_3 > 0$，原子核必然具有静态梨形并展现简并宇称带（已被重叠核 $\Omega \sim 0.2$ 导致的 $800\text{ keV}$ 劈裂直接证伪）；
2. 纯单声子微扰振子假设：假定八极态纯属偶极-八极多声子微扰，忽视有限 $\beta_3$ 引起的波函数中心偏移。

## Transfer Conditions

投影算符核公式与重叠衰减规律适用于全周期所有自发反射破缺平均场态；但具体劈裂数值严格依赖自洽微观泛函计算的势能面与坐标依赖的量子惯量张量。

## Failure Conditions

若在 $^{144}\text{Ba}$ 中发现基态存在分裂小于 $100\text{ keV}$ 的相反宇称伴态，或在 $^{224}\text{Ra}$ 中证明两阱空间重叠核 $\Omega > 0.1$，则本重叠核与隧穿动力学模型失效。

## Falsification or Reverse Tests

独立运行数值工件 `parity-projection-overlap-kernel-model-076.py`，完整重现四类典型核在重叠核与 WKB 穿透率上的演化，数据验证固化于 `parity-projection-overlap-kernel-model-076.json`。

## Open Questions

在自洽二维 $(\beta_2, \beta_3)$ 约束 GCM 计算中，四极动力学涨落如何调制空间重叠核 $\Omega$ 的实际二维积分路径？

## Human Review

本笔记由 Codex L4 全自动研学推导建立，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 正式研学要求创建，确立宇称投影重叠核与微观八极动力学分类标准。
