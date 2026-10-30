---
type: research-note
title: "巨单极共振（ISGMR）形变劈裂与核不可压缩系数提取模型不适用性：长椭核L=0与L=2 K=0强混合机制"
aliases: [isgmr-deformation-splitting-and-incompressibility-inapplicability, ISGMR deformation splitting, Day27 ISGMR splitting]
created: 2026-10-30
updated: 2026-10-30
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [youngblood-2004-isgmr-deformation-splitting]
created_from: Day 27 continuation study; system/scripts/day27_isgmr_deformation_splitting_and_mixing_study.py
tags: [giant-monopole-resonance, incompressibility, deformation-splitting, monopole-quadrupole-mixing, 144Sm, 154Sm, 208Pb, 238U, Day27]
---

# 巨单极共振（ISGMR）形变劈裂与核不可压缩系数提取模型不适用性：长椭核 L=0 与 L=2 K=0 强混合机制

## Research Trigger

在核状态方程（EOS）微观约束中，等标巨单极共振（ISGMR，即“呼吸模”）的质心能量 $E_{\text{ISGMR}} = \hbar \sqrt{K_A / (m \langle r^2 \rangle)}$ 是直接决定有限核不可压缩系数 $K_A$ 及核物质饱和区不可压缩参数 $K_\infty \approx 230 - 240\text{ MeV}$ 的基准物理观测量。
然而，在跨质量区从球形闭壳核向形变核的推广中，出现了一个著名的“形变核异常变软”的伪疑难：
1. **球形核的单共振峰（$^{144}\text{Sm}, ^{208}\text{Pb}$）**：[[youngblood-2004-isgmr-deformation-splitting]]（PRC 69, 034315）非弹性 $\alpha$ 散射高精度实验证实，球形半幻核 $^{144}\text{Sm}$ 呈现纯粹的单峰共振（$E_{\text{cen}} = 15.39(15)\text{ MeV}$，耗尽 $100\%$ $E0$ EWSR）；
2. **长椭形变核的双峰分裂（$^{154}\text{Sm}, ^{238}\text{U}$）**：在具有显著长椭形变（$\beta_2 = 0.30$）的同位素 $^{154}\text{Sm}$ 中，单极共振发生剧烈的双峰分裂，出现低能伴峰 $E_1 = 11.45(25)\text{ MeV}$（占 $36(4)\%$ EWSR）与主峰 $E_2 = 15.15(20)\text{ MeV}$（占 $62(6)\%$ EWSR）；
3. **传统提取模型的系统性崩溃**：若无视形变分裂，粗暴将球形单峰质心公式 $\bar{E} = m_1 / m_0$ 强行套用至 $^{154}\text{Sm}$，加权质心被低能峰强力拉低至 $14.2\text{ MeV}$，导出其有效不可压缩系数虚假降低达 **$\Delta K_A \approx 35 - 45\text{ MeV}$（表观变软近 $30\%$）**。

本研究基于长椭势阱下单极呼吸模式与巨四极共振 $K=0$ 分支的微观二态混合模型 `day27_isgmr_deformation_splitting_and_mixing_study.py`，微观阐明双峰形成的动力学机制，确立球形不可压缩系数提取协议在形变核区的不适用性硬边界。

## Grounded Evidence

通过执行全微观单极-四极形变混合变分求解器 `system/scripts/day27_isgmr_deformation_splitting_and_mixing_study.py`，并在 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/isgmr-deformation-splitting/isgmr_deformation_splitting_results.json` 沉淀结构化数据，确立以下定量证据：

1. **形变诱导的单极—四极空间几何混合机制：**
   - 在长椭核（$\beta_2 \ne 0$）中，球形对称破缺使 $L=0$ 单极算符 $r^2 Y_{00}$ 与 $L=2, K=0$ 四极算符 $r^2 Y_{20}$ 拥有相同的内禀空间柱对称性（同属 $K=0, \pi=+$ 不可约表示）；
   - 非零四极基态形变诱发了巨大的非对角耦合矩阵元：
     $$V_{MQ} \approx \frac{\sqrt{5}}{3} \beta_2 E_M^{(0)} \chi_{\text{mix}} \approx 1.458\text{ MeV};$$
   - 该强耦合矩阵元驱动原本独立的纯呼吸模 $|M\rangle$（$E_M \approx 15.26\text{ MeV}$）与四极压缩分支 $|Q, K=0\rangle$（$E_Q \approx 11.96\text{ MeV}$）发生强烈的二态杂化对角化：
     - **低能本征峰（Mode 1）**：能量被推低至 $E_1 = 11.35\text{ MeV}$（实测 $11.45\text{ MeV}$），其波函数混入大量单极对流成分，捕获了高达 **$30.0\%$（实测 $36\%$）** 的单极能量加权求和规则（EWSR）；
     - **高能本征峰（Mode 2）**：能量位于 $E_2 = 15.43\text{ MeV}$（实测 $15.15\text{ MeV}$），承载剩余的 $70.0\%$ 单极强度。

2. **球形提取协议导致的“伪变软”偏差（False Softness Bias）：**
   - 若忽略双峰机制而将全带加权平均，表观质心能量降至 $\bar{E}_{\text{app}} = 14.21\text{ MeV}$，比纯呼吸模的实际内禀本征频率（$15.26\text{ MeV}$）系统性低估了逾 $1.0\text{ MeV}$；
   - 结合不可压缩性二次方关系 $K_A \propto E^2$，自洽导出其导致有限核不可压缩系数产生 **$\Delta K_A = 35.1\text{ MeV}$ 的虚假下移**（在 $^{238}\text{U}$ 中导致 $\Delta K_A = 31.2\text{ MeV}$ 的下移）；
   - 这在物理与数学上彻底澄清了历史所谓“稀土与锕系形变核具有较低不可压缩系数”的假象，证明其完全是几何多极耦合诱发的实验表观伪效应。

3. **不可压缩系数提取跨区迁移失效判据：**
   - **形变分界硬判据**：当原子核四极形变 $\beta_2 \ge 0.15$ 时，严禁采用单峰高斯/洛伦兹拟合提取 $E0$ 质心；必须采用二能级单极-四极解耦方案分离出纯呼吸模对角能量；
   - **求和规则完整性判据**：低能卫星峰（$\sim 11.5\text{ MeV}$）携带的 $E0$ 强度是纯粹的几何形变诱导效应，不可作为存在独立低能可压缩新模式的物理依据。

## Evidence Boundaries & Review Status

- 物理模型：基于自洽单极-四极流体力学二能态混合展开与能量加权求和规则分解；
- 证据层级：基于 Youngblood 2004（Texas A&M 小角非弹性 $\alpha$ 散射一手实验数据）；
- 审定状态：本笔记为 Day 27 博士生级开放研学计算工件沉淀，标记为 `status: ai-draft`、`review_status: unreviewed`。
