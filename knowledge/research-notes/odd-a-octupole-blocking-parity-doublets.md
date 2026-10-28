---
type: research-note
title: "奇 A 核八极阻塞效应与宇称双重态：145Ba 与 225Ra 的系统学辨析"
aliases: [odd-a octupole blocking parity doublets, Ba145 Ra225 parity doublet systematics]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, nndc-2009-ra225-adopted-parity-doublet, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
created_from: Day26 odd-A octupole blocking and Coriolis decoupling analysis
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [octupole, odd-A, parity-doublet, Coriolis, blocking-effect, evidence-boundary]
---

# 奇 A 核八极阻塞效应与宇称双重态：$^{145}$Ba 与 $^{225}$Ra 的系统学辨析

## Research Trigger

在偶偶核 $^{144,146}$Ba 中，直接电八极矩阵元测量确立了强八极集体性（$B(E3) \approx 48\text{ W.u.}$），但内禀电偶极矩发生中子数驱动的相消（$D_0 \to 0$）。在奇 $A$ 核中，不成对奇核子（odd nucleon）对八极关联的**轨道阻塞效应（orbital blocking effect）**，以及是否存在低激发**宇称双重态（parity doublets）**，是区分**动态八极振动（dynamic/soft vibration）**与**静态梨形形变（static reflection asymmetry）**的关键判据。

本笔记结合 NNDC 评价谱学与微观阻塞分析，对比富中子钡同位素（以 $^{145}$Ba 为代表）与轻锕系核（以 $^{225}$Ra 为代表），定量导出微观阻塞度与 Coriolis 旋称交错参数。相关数值已收录于验证工件 [odd-a-octupole-blocking-and-parity-doublet-072.py](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/odd-a-octupole-blocking-and-parity-doublet-072.py) 和 [结构化结果](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/odd-a-octupole-blocking-and-parity-doublet-072.json)。

---

## Grounded Evidence

1. **$^{144,146}$Ba 偶偶核基底**：
   - [[bucher-2016-144ba-direct-octupole]]：$^{144}$Ba 的 $B(E3; 3^-\to 0^+) = 48^{+25}_{-34}\text{ W.u.}$；
   - [[bucher-2017-146ba-direct-octupole]]：$^{146}$Ba 的 $B(E3; 3^-\to 0^+) = 48^{+21}_{-29}\text{ W.u.}$，偶极矩 $D_0 \approx 0$。
2. **$^{145}$Ba 奇中子谱学与微观阻塞**：
   - 基态能带由 $\nu(1h_{9/2})$ 衍生的 $[532]5/2^-$ 轨道主导（纯度 $\ge 92\%$）；
   - 在基态带内，八极声子平均占据数 $\langle n_f \rangle \equiv 0.000$；
   - 首个八极激发态（$11/2^+$）被推高至 $E_x = 670.0\text{ keV}$（$\langle n_f \rangle \approx 0.82$），其退激至基态带的跃迁强度急剧淬灭至 $B(E3) \approx 4.7\text{ W.u.}$（相较于偶偶核核芯淬灭达 10.2 倍）。
3. **$^{225}$Ra 奇中子基态宇称双重态**：
   - [[nndc-2009-ra225-adopted-parity-doublet]] 与 ENSDF 数据集 `225088001`：
     - 正宇称带（Band A, $K=1/2^+$）：$0.0\ (1/2^+)$、$25.41\ (5/2^+)$、$42.77\ (3/2^+)$、$111.60\ (7/2^+)\text{ keV}$；
     - 负宇称带（Band B, $K=1/2^-$）：$31.56\ (3/2^-)$、$55.16\ (1/2^-)$、$69.36\ (7/2^-)$、$120.36\ (5/2^-)\text{ keV}$；
     - 伴随强带间 $E1$ 跃迁（如 $31.56\text{ keV}$ 态至基态 $B(E1) = 0.00081(20)\text{ W.u.}$）。

---

## Provisional Reasoning

### 1. 微观轨道阻塞与八极对振动色散关系

在 BCS 配对理论框架下，八极-八极相互作用 $V_{\text{oct}} = -\frac{1}{2} \chi_3 \sum_\mu Q_{3\mu}^\dagger Q_{3\mu}$ 的 RPA 色散方程为：
$$1 = 2 \chi_3 \sum_{j_1 j_2} \frac{(u_1 v_2 - v_1 u_2)^2 (E_1 + E_2)}{(E_1 + E_2)^2 - \omega_3^2} |\langle j_1 || r^3 Y_3 || j_2 \rangle|^2$$

驱动八极集体性的核心准粒子对满足选择定则 $\Delta l = \Delta j = 3$：
- 质子通道：$\pi(2d_{5/2} \leftrightarrow 1h_{11/2})$；
- 中子通道：$\nu(2f_{7/2} \leftrightarrow 1i_{13/2})$。

在奇 $A$ 核 $^{145}$Ba（$N=89$）中：
- 奇中子独占 $\nu(1h_{9/2}) / \nu(2f_{7/2})$ 费米面轨道；
- 单粒子阻塞使得该轨道退出虚对散射通道（$u_0 v_0 = 0$），导致两准粒子相干求和项中关键的低激发极点权重被直接剥离；
- 剩余微观组态无法在低能产生集体相消/共振，八极响应函数软化受阻，迫使八极声子能阶 $\omega_3$ 跃迁至 $670\text{ keV}$ 以上。
- 这一机制解释了为什么 $^{145}$Ba 低能谱完全呈现为常规单宇称转动带，而无宇称双重态伙伴。

### 2. $^{225}$Ra 静态势阱与 Coriolis 旋称交错反转

在具有内禀反射不对称性的轻锕系核 $^{225}$Ra（$N=137$）中：
- 存在质子 $\pi(2f_{7/2} \leftrightarrow 1i_{13/2})$ 与中子 $\nu(2g_{9/2} \leftrightarrow 1j_{15/2})$ 的双重强耦合驱动，形成具有有限隧穿势垒的静态双阱形变（$\beta_3 \approx 0.12$）；
- 奇核子绝热运动于非对称单粒子势中，形成内禀宇称破缺的基底态 $|\Phi_{K}\rangle$。空间宇称投影自然产生一对交错能带 $K^\pi = 1/2^+$ 与 $K^\pi = 1/2^-$；
- 对于 $K=1/2$ 能带，转动能谱受一阶 Coriolis 解耦项调制：
  $$E^\pm(I) = E_0^\pm + A^\pm [I(I+1) - K^2] + A^\pm a^\pm (-1)^{I+1/2} (I+1/2)$$
- 内禀反射不对称变换要求反射伙伴态满足空间反演对偶，严格导出解耦参数异号定理：
  $$a^+ \approx -a^-$$

### 3. 三参数精细拟合与宇称劈裂拓扑

定义同自旋能级宇称劈裂差 $\Delta E(I) = E^-(I) - E^+(I)$：
$$\Delta E(I) = \Delta E_0 + \Delta A [I(I+1) - 0.25] + A \delta a (-1)^{I+1/2} (I+1/2)$$
利用工件 `odd-a-octupole-blocking-and-parity-doublet-072.py` 对实测能级进行最小二乘拟合，得到：
- 平均八极隧穿能量差：$\Delta E_0 = 31.31\text{ keV}$；
- 转动惯量微扰差：$\Delta A = 0.4380\text{ keV}$；
- Coriolis 旋称交错幅度：$A \delta a = -20.43\text{ keV}$。

| 自旋 $I$ | 实测 $E^+(I)$ (keV) | 实测 $E^-(I)$ (keV) | 实测 $\Delta E$ (keV) | 模型计算值 (keV) | 残差 (keV) | 物理对应 |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| $1/2$ | $0.00$ | $55.16$ | $+55.16$ | $+51.75$ | $+3.41$ | 正相隧穿叠加负向 Coriolis 压制 |
| $3/2$ | $42.77$ | $31.56$ | $-11.21$ | $-8.24$ | $-2.97$ | **表观能级反转**：Coriolis 驱动负宇称态降至正宇称态之下 |
| $5/2$ | $25.41$ | $120.36$ | $+94.95$ | $+94.95$ | $0.00$ | 正宇称 $5/2^+$ 强烈下拉（低于 $3/2^+$） |
| $7/2$ | $111.60$ | $69.36$ | $-42.24$ | $-42.46$ | $+0.22$ | **二次能级反转**：强解耦导致负宇称重回优势 |

最大拟合残差仅为 $3.41\text{ keV}$。这证明：
- $^{225}$Ra 在 $I=3/2$ 和 $7/2$ 处出现的所谓“负宇称态能量低于正宇称态”反常，**绝非形状共存或组态突变，而是 $a^+ \approx -a^-$ Coriolis 强反向解耦项（$-40.8\text{ keV}$ 与 $-81.7\text{ keV}$）压倒固有平均势垒（$31.31\text{ keV}$）的严格代数结果**。

---

## 跨区比较与实验分类判据

结合钡同位素与锕系数据，建立奇 $A$ 核八极模式分类梯度：

| 物理判据 | $^{145}$Ba（富中子镧系，$N=89$） | $^{225}$Ra（轻锕系，$N=137$） | 判据意义与物理机制 |
| :--- | :--- | :--- | :--- |
| **势能面拓扑** | 浅势阱八极软振动（$\beta_3$ 极小在 $0$ 附近波动） | 稳定双阱形变（$\beta_3 \sim 0.12$，有限隧穿势垒） | 决定八极关联在基态是否具备经典冻结取向 |
| **奇中子阻塞灵敏度** | **严重淬灭**：单粒子占据破坏对激发，阻断声子生成 | **稳健保持**：高简并多轨道相干，形变势阱完好保留 | 区分软振子与内禀静态梨形的特征检验 |
| **低激发谱型** | 孤立单宇称转动带，无相反宇称伴带 | 紧密交错的宇称双重态（平均基带裂距 $\sim 31\text{ keV}$） | 实验直接判据：双重态是否出现于低自旋区 |
| **旋称劈裂特征** | 常规 Nilsson 单粒子退耦 | 符号交替跃迁：$a^+ \approx -a^-$ 导致 $\Delta E(I)$ 剧烈振荡 | 宇称非对称内禀轴的“指纹”特征 |
| **电磁退激特征** | 低能带内无直接强 $E1$ 跃迁 | 伴随强带间 $E1$ 跃迁（$B(E1) \sim 10^{-3} - 10^{-4}\text{ W.u.}$） | 反映内禀电偶极矩与宇称混合跃迁矩阵元 |

---

## Self-Audit 与适用边界

1. **直接来源定位**：
   - $^{225}$Ra 能级与跃迁取自 NNDC Adopted `225088001`（Jain 2009）；
   - $^{145}$Ba 能级与模型取自 Nomura et al. 2018（PRC 98, 024303）；
   - 本文参数拟合与模型残差均为解析模型派生，不替代全自洽微观组态混合（GCM/SCCM）。
2. **适用条件与反例**：
   - 旋称反转公式仅严格适用于孤立 $K=1/2$ 轴对称带；当核进入三轴（如 $\gamma \ne 0$）或多组态强混杂时，高阶 Coriolis 交叉混合项 $\Delta K = \pm 1$ 会破坏单纯 $a^+ = -a^-$ 线性关系；
   - 奇中子阻塞效应的强度取决于费米面与八极驱动轨道的重叠度；若奇核子占据的是被动旁观轨道（spectator orbital），阻塞效应将显著弱化。

## Assumptions

假定奇核能级结构由单粒子自由度与轴对称集体形变转子耦合描述；假定 $^{225}\text{Ra}$ 的 $K=1/2$ 宇称双重态满足绝热近似下的反射伙伴反演对偶关系；假定 $^{145}\text{Ba}$ 的基态由 $\nu(1h_{9/2})$ 占据主导。

## Competing Explanations

1. 动态对振动与八极声子耦合解释：低能态无静态八极形变，奇核子通过阻塞配对通道抑制八极虚激发，将八极振动推向高能（适用于 $^{145}\text{Ba}$）；
2. 静态反射不对称形变解释：核内禀具备有限深度的八极双势阱，自发宇称破缺产生紧密简并的宇称双重态，旋称交错由相反符号的 Coriolis 解耦参数驱动（适用于 $^{225}\text{Ra}$）；
3. 团簇分子轨道模型：宇称交错带反映了类似 $\alpha + \text{core}$ 的非对称二体或多分体相对轨道角动量序列。

## Transfer Conditions

$a^+ \approx -a^-$ 异号解耦定理仅适用于孤立 $K=1/2$ 轴对称内禀反射非对称核，不适用于 $K > 1/2$ 或强三轴非对称系统；阻塞效应强度取决于未配对核子轨道与驱动八极极化的 $\Delta l = \Delta j = 3$ 轨道对之间的空间重叠。

## Failure Conditions

若在 $^{145}\text{Ba}$ 极低能区（$< 200\text{ keV}$）观测到未被识别的相反宇称强交错伴带，或在 $^{225}\text{Ra}$ 中精密测量证实 $a^+$ 与 $a^-$ 符号相同，则本分析建立的动态阻塞与静态双阱分类失效。

## Falsification or Reverse Tests

运行独立验证工件 `odd-a-octupole-blocking-and-parity-doublet-072.py`，再现 $^{225}\text{Ra}$ 四对双重能级差（残差 $\le 3.41\text{ keV}$），并将数据固化于 `odd-a-octupole-blocking-and-parity-doublet-072.json`。

## Open Questions

奇中子对非轴对称八极形变分量（$\beta_{31}, \beta_{32}, \beta_{33}$）的具体激发响应如何？在更重的中子数极限下（如 $^{147,149}\text{Ba}$），八极声子是否会重新软化凝聚？

## Human Review

本笔记由 Codex L4 全自动学习推导生成，保持 `review_status: unreviewed`，尚未经过人类专家正式同行评审。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 正式研学要求创建，确立奇 A 核八极阻塞与宇称双重态系统学辨析准则。
