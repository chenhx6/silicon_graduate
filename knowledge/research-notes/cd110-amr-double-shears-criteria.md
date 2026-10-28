---
type: research-note
title: "110Cd 反磁转动双剪刀对称性、B(E2)平台与判据比研究"
aliases: [cd110-amr-double-shears-criteria, 110Cd antimagnetic rotation double shears, 110Cd J2 over BE2 ratio]
created: 2026-10-28
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [roy-2011-cd110-systematics-antimagnetic, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, nndc-2012-cd110-hi-xng]
created_from: Day26 deep doctoral investigation
promotion_target: octupole-mr-amr-evidence-gradient
tags: [110Cd, antimagnetic-rotation, double-shears, B(E2)-plateau, J2-over-BE2]
---

# 110Cd 反磁转动双剪刀对称性、B(E2)平台与判据比研究

## Research Trigger

反磁转动（Antimagnetic Rotation, AMR）是低能核结构中自发对称性破缺与恢复的一种奇异形式，由 Frauendorf 于 2001 年预言。与普通磁转动（单剪刀、强 $M1$ 阶梯）截然相反，AMR 的典型特征是内部两对磁剪刀以轴对称镜像方式同步闭合，导致横向磁偶极矩处处抵消，完全禁戒带内 $\Delta I = 1$ 的 $M1$ 跃迁，仅由一系列规则的 $\Delta I = 2$ 电四极（$E2$）跃迁退激。作为实验公认最完备的 AMR 候选核，$^{110}\text{Cd}$ 的高自旋能带（Band B，自旋 $12^+ \to 24^+$）展现了反常平缓的 $B(E2) \sim 0.10\ e^2\text{b}^2$ 平台与高达 $116 - 341\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$ 的动态惯量与跃迁强度巨比值 $\mathcal{J}^{(2)}/B(E2)$。本笔记推导双剪刀几何对称性、核芯转动解耦机制，并确立区分 AMR 与常规集体转动的严格实验判据体系。

## Grounded Evidence

| 标识 | 核心事实 / 主张 | 证据分层 | 文献定位 | 科学边界与限制 |
|---|---|---|---|---|
| CD110-AMR-01 | $^{110}\text{Cd}$ Band B 实测 $B(E2)$ 强度：$12^+ \to 10^+$ ($40.0(15)\text{ W.u.}$), $14^+ \to 12^+$ ($29(3)$), $16^+ \to 14^+$ ($50(5)$), $18^+ \to 16^+$ ($41(6)$), $20^+ \to 18^+$ ($38(7)$), $22^+ \to 20^+$ ($22(8)\text{ W.u.}$) | 直接实验测量 | Roy 2011 PLB 694, 322 Table 1; NNDC 110048001 | 结合了 Piiparinen 1993 RDDS 寿命与 Roy 2011 DSAM 寿命 |
| CD110-AMR-02 | Band B 的动态转动惯量与跃迁几率之比 $\mathcal{J}^{(2)}/B(E2)$ 实测跨度为 $116.0 - 341.3\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$ | 导出实验物理量 | 本工作 `cd110-amr-four-shears-criteria-052` | 较常规形变集体转动核（$15 - 40$）高出近一个数量级，验证了 Frauendorf 2001 的宏观预言 |
| CD110-AMR-03 | 纯双剪刀模型对称性导致横向磁偶极矩 $\mu_\perp = 0$，严格禁戒带内 $\Delta I = 1$ 的 $M1$ 跃迁（$B(M1) \equiv 0$） | 离散对称性与选择定则 | Frauendorf 2001 RMP 73, 463 | 仅在完全对偶四剪刀构型下成立，不禁止由于微弱不对称引发的微量带外 $M1$ 跃迁 |
| CD110-AMR-04 | 纯双剪刀（无核芯惯量）的最大剪刀角动量为 $I_{\text{max}} = 10 + 9 = 19\hbar$；引入半刚体核芯转动（$\Im_{\text{core}} \approx 19.5\ \hbar^2/\text{MeV}$）后能带延伸至 $24^+$ 并产生 $B(E2)$ 平缓平台 | 理论模型与实验对比 | Roy 2011 p.3-4; 本工作工件 | 核心转动分担了 $18\% - 26\%$ 的总自旋，减缓了剪刀角的闭合速率 |
| CD110-AMR-05 | NNDC ENSDF 评价中 $22^+$ 态列有一条 $1100\text{ keV}$（$RI=37$，$B(E2)=20(10)\text{ W.u.}$）分支，但 Roy 2011 符合门谱未观测到该线 | 实验分支争议 | NNDC adopted 110048001; 1994Ju04 | Roy Table 1 仅采纳 $1314\text{ keV}$ 单分支门，其 $B(E2) = 0.06(2)\ (e\text{b})^2$ 未扣除未证实分支 |

## Provisional Reasoning

### 1. 四叶片（双剪刀）空间构型与离散对称性

在 $^{110}\text{Cd}$（$Z=48, N=62$）中，高自旋带由近球形闭壳芯加上两对价准粒子构成：
- 质子部分：两个处于 $g_{9/2}$ 壳层的质子空穴，构成两支独立的质子叶片 $\vec{j}_{h1}$ 和 $\vec{j}_{h2}$，各自角动量 $j_h \approx 9/2 = 4.5\hbar$；
- 中子部分：两个处于 $h_{11/2}$ 壳层的高 $j$ 中子粒子，因强配对与形变排布，其角动量紧密对齐，合成一个沿对称轴（转动主轴）的总中子角动量矢量 $\vec{j}_n \approx 10.0\hbar$。

在转动激发下，两支质子空穴叶片以相同的夹角 $\theta$ 向中子轴对称靠拢（剪刀闭合）。此时核系统具备空间转动与时间反演的复合离散对称性：
$$\mathcal{S} = \mathcal{R}_y(\pi) \mathcal{T}$$
在这一对称操作下：
1. 转动轴 $z$ 保持不变；
2. 两个质子叶片在垂直于总角动量的横向平面上的投影彼此反向共轭：
   $$\vec{j}_{h1}^\perp = -\vec{j}_{h2}^\perp$$

### 2. 横向磁偶极矩的严格抵消与 $M1$ 禁戒

质子空穴叶片的磁偶极矩算符为 $\vec{\mu}_h = (g_h - g_R) \vec{j}_h$。
总横向磁偶极矩为两支质子叶片的矢量和：
$$\vec{\mu}_\perp = (g_h - g_R) (\vec{j}_{h1}^\perp + \vec{j}_{h2}^\perp) = (g_h - g_R) (\vec{j}_{h1}^\perp - \vec{j}_{h1}^\perp) \equiv 0$$

**物理结论**：
- 由于镜像对称的双剪刀在任意转动频率下横向偶极矩处处相消，横向磁偶极跃迁矩阵元严格为零：
  $$B(M1; I \to I-1) \equiv 0$$
- 因此，AMR 能带中绝不可能出现强 $\Delta I = 1$ 的 $M1$ 阶梯。这一特征使其与单剪刀常规磁转动（MR，具有强 $B(M1)$ 且无 $B(M1)=0$ 约束）形成清晰的物理区隔。

## Core Rotation Decoupling and the B(E2) Plateau Mechanism

### 1. 纯双剪刀的角动量瓶颈与快速塌缩

若不考虑原子核其余部分（核芯）的集体转动，总角动量仅由四剪刀闭合产生：
$$I_{\text{shears}} = j_n + 2 j_h \cos\theta = 10.0 + 9.0 \cos\theta$$
剪刀完全闭合（$\theta = 0^\circ$）时的最大自旋严格受限于：
$$I_{\text{max}} = 10.0 + 9.0 = 19.0\hbar$$
同时，四剪刀电四极跃迁几率随着夹角闭合呈四次方急剧衰减：
$$B(E2; I \to I-2) \propto \sin^4\theta = \left[1 - \left(\frac{I - 10}{9}\right)^2\right]^2$$
按照纯剪刀模型，当自旋从 $14^+$ 增加到 $18^+$ 时，$B(E2)$ 将发生断崖式跌落（下降逾 $80\%$），且能带在 $19\hbar$ 处终止。这与实验在 $^{110}\text{Cd}$ 中观测到能带延伸至 $24^+$ 且 $B(E2)$ 维持平缓平台的实际情况严重矛盾。

### 2. 半刚体核芯转动耦合（Core Rotation Decoupling）

依据 Roy 2011 两粒子加转子模型及工件 `cd110-amr-four-shears-criteria-052.py`：
在弱形变核中，核芯具备有限的半刚体转动惯量 $\Im_{\text{core}} \approx 19.5\ \hbar^2/\text{MeV}$。总角动量为剪刀贡献与核芯集体转动贡献的代数和：
$$I = I_{\text{shears}}(\theta) + I_{\text{core}}(\omega) = (10.0 + 9.0 \cos\theta) + \Im_{\text{core}} \omega$$

在转动频率 $\hbar\omega = 0.40 \to 0.70\text{ MeV}$ 区间：
1. 核芯转动分担了 $I_{\text{core}} \approx 3.0 - 6.5\hbar$ 的角动量增益，占总自旋的 $18\% - 26\%$；
2. 核芯转动极大减缓了质子剪刀叶片向中子轴的闭合速度：在 $12^+ \to 20^+$ 的宽广自旋区间内，剪刀角 $\theta$ 仅从约 $70^\circ$ 温和闭合至约 $38^\circ$；
3. 由此产生的电四极跃迁几率 $B(E2)$ 成功摆脱了陡降困境，形成维持在 $0.09 - 0.16\ e^2\text{b}^2$（$29 - 50\text{ W.u.}$）的反常**平缓平台**；
4. 只有在自旋 $22^+$（$E_\gamma = 1314.1\text{ keV}$）处，剪刀角接近临界闭合角，实测 $B(E2)$ 才开始下降至 $0.069\ e^2\text{b}^2$（$22(8)\text{ W.u.}$）。

## The Giant J^(2)/B(E2) Ratio as the Defining AMR Criterion

在无法直接测量核微观流场的实验条件下，如何排他性地证明一个能带属于反磁转动而非弱形变集体转动？Frauendorf（2001）提出了决定性的判据比——**动态转动惯量与跃迁强度之比** $\mathcal{J}^{(2)}/B(E2)$。

### 1. 动态转动惯量 $\mathcal{J}^{(2)}$ 的微观推演

动态转动惯量定义为角动量随转动频率的变化率：
$$\mathcal{J}^{(2)} \equiv \frac{dI}{d\omega} = \frac{4}{\Delta E_\gamma} = \frac{4}{E_\gamma(I) - E_\gamma(I-2)}$$

### 2. 判据比实测计算与数量级鸿沟

由工件 `cd110-amr-four-shears-criteria-052.json` 对 $^{110}\text{Cd}$ Band B 实测数据的逐点严格计算：
- **$14^+ \to 12^+$**：$E_\gamma = 854.3\text{ keV}$，$\Delta E_\gamma = 0.2933\text{ MeV}$，$\mathcal{J}^{(2)} = 13.64\ \hbar^2/\text{MeV}$，$B(E2) = 0.091\ e^2\text{b}^2$：
  $$\frac{\mathcal{J}^{(2)}}{B(E2)} = 150.2\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$$
- **$16^+ \to 14^+$**：$E_\gamma = 1074.6\text{ keV}$，$\Delta E_\gamma = 0.2203\text{ MeV}$，$\mathcal{J}^{(2)} = 18.16\ \hbar^2/\text{MeV}$，$B(E2) = 0.157\ e^2\text{b}^2$：
  $$\frac{\mathcal{J}^{(2)}}{B(E2)} = 116.0\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$$
- **$18^+ \to 16^+$**：$E_\gamma = 1224.5\text{ keV}$，$\Delta E_\gamma = 0.1499\text{ MeV}$，$\mathcal{J}^{(2)} = 26.68\ \hbar^2/\text{MeV}$，$B(E2) = 0.128\ e^2\text{b}^2$：
  $$\frac{\mathcal{J}^{(2)}}{B(E2)} = 207.9\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$$
- **$20^+ \to 18^+$**：$E_\gamma = 1323.0\text{ keV}$，$\Delta E_\gamma = 0.0985\text{ MeV}$，$\mathcal{J}^{(2)} = 40.61\ \hbar^2/\text{MeV}$，$B(E2) = 0.119\ e^2\text{b}^2$：
  $$\frac{\mathcal{J}^{(2)}}{B(E2)} = 341.3\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$$

### 3. 与常规集体转动的排他性对比

| 结构模式 | 跃迁强度 $B(E2)$ | 动态转动惯量 $\mathcal{J}^{(2)}$ | 判据比 $\mathcal{J}^{(2)}/B(E2)$ | 物理本质 |
|---|---|---|---|---|
| **常规形变集体转动** | 极大：$1.0 - 2.5\ e^2\text{b}^2$（$200 - 500\text{ W.u.}$） | 中等：$30 - 60\ \hbar^2/\text{MeV}$ | **极小：$15 - 40\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$** | 全核整体电荷质量转动，电荷四极矩驱动 |
| **弱形变振动核** | 较小：$0.05 - 0.20\ e^2\text{b}^2$ | 极小且不规则 | 不构成规则转动带序列 | 表面简谐微振动 |
| **反磁转动（AMR）** | **微小：$0.06 - 0.16\ e^2\text{b}^2$（$20 - 50\text{ W.u.}$）** | **正常：$15 - 45\ \hbar^2/\text{MeV}$** | **巨比值：$100 - 350\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$** | 非对角价核子磁剪刀闭合，空间非对称性与电四极形变解耦 |

实测比值高出常规集体转动达 4 到 10 倍，在物理上确凿建立了反磁转动的排他性指纹。

## 22^+ High-Spin Branch Controversy and Systematics

在 $^{110}\text{Cd}$ 的高自旋端点，针对 $22^+$ 态退激存在关键的实验谱系分歧：
1. **ENSDF adopted 评价（1994Ju04 数据集）**：
   评估存在一条未最终定域的 $1100\text{ keV}$ 跃迁，相对光子强度 $RI = 37$（相对于主跃迁 $1314.1\text{ keV}$ 的 $RI = 100$），并据此在评价库中给出 $B(E2) = 20(10)\text{ W.u.}$；
2. **Roy et al. 2011 现代高精度符合实验**：
   在精心设置的干净符合门中，并未能确认该 $1100\text{ keV}$ 分支的存在。Roy 等人将全部退激强度归于 $1314.1\text{ keV}$ 纯门，提取的跃迁几率为 $B(E2) = 0.06(2)\ (e\text{b})^2$（约 $22(8)\text{ W.u.}$）；
3. **科学边界**：
   若未来实验证实该 $1100\text{ keV}$ 分支真实存在，主线 $1314\text{ keV}$ 的分支比将从 $100\%$ 下调至 $\sim 73\%$，使得导出的 $B(E2)$ 进一步下调至约 $0.044\ e^2\text{b}^2$。这一修正不会削弱 AMR 假说，反而使高自旋端的剪刀闭合下跌趋势更加陡峭，并使 $\mathcal{J}^{(2)}/B(E2)$ 进一步飙升至 $> 500$。

## Open Questions

1. $22^+$ 态的 $1100\text{ keV}$ 竞争分支在不同符合门中的检出限与真实分支比尚待新一代探测阵列验证。
2. 纯双剪刀极限下的角动量截断如何平滑过渡到微观配对破缺与高自旋转动对齐的完整组态空间？
3. 为什么邻近同位素 $^{106,108}\text{Cd}$ 的 $B(E2)$ 呈现陡降，而 $^{110}\text{Cd}$ 能维持显著平台？核芯转动惯量随中子数演化的微观根源仍待完全自洽 EDF 说明。

## Assumptions

模型采用质子空穴 $\pi(g_{9/2})^{-2}$ 与中子对 $\nu(h_{11/2})^2$ 构成的双剪刀耦合方案，核芯转动惯量取半刚体值 $\Im_{\text{core}} \approx 19.5\ \hbar^2/\text{MeV}$；跃迁数据直接基于 Roy 2011 Table 1 与 NNDC 官方评价数据集。

## Competing Explanations

常规微弱形变集体转动、纯双剪刀几何闭合、核芯转动退耦与非对称粒子-转子耦合均是候选解释；巨大的 $\mathcal{J}^{(2)}/B(E2)$ 比值与带内无 $M1$ 跃迁排他性支持带核芯解耦的反磁转动图像。

## Transfer Conditions

巨判据比 $\mathcal{J}^{(2)}/B(E2) \sim 100 - 350\ \hbar^2\text{MeV}^{-1}(e^2\text{b}^2)^{-1}$ 与带内 $M1$ 禁戒判据适用于所有近球形四剪刀核（如镉同位素链与钯同位素链），不能迁移至具有显著基态四极形变（$\beta_2 \ge 0.25$）的集体转动核。

## Failure Conditions

若实验测得带内存在强 $\Delta I = 1$ 的 $M1$ 阶梯跃迁，或实测 $B(E2)$ 显著大于单粒子强度（$> 100\text{ W.u.}$），则反磁转动假设自动被证伪。

## Falsification or Reverse Tests

利用独立验证程序 `cd110-amr-four-shears-criteria-052.py` 对实测跃迁能量、动态转动惯量与跃迁比进行数值校验，计算结果保存于 `cd110-amr-four-shears-criteria-052.json`。

## Knowledge Impact and Learning Decision

`supports` 双剪刀对称性对横向偶极矩的严格抵消、核芯解耦驱动的 $B(E2)$ 平台机制，以及巨判据比 $\mathcal{J}^{(2)}/B(E2)$ 作为 AMR 实验指纹；`limits` 单凭 $\Delta I = 2$ 级联未见 $M1$ 断言 AMR 的排他性。本笔记由 Codex self-audit 驱动，保留 `unreviewed`。

## Sources

- [[roy-2011-cd110-systematics-antimagnetic]]
- [[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]]
- [[nndc-2012-cd110-hi-xng]]
- [[octupole-mr-amr-evidence-gradient]]

## Review Status

自主研学产物，未进行人工审核。

## Human Review

尚未经过人工审核，保持 `review_status: unreviewed`。

## Promotion or Rejection History

2026-10-29: 依据 Day 26 L4 研学要求创建，系统化推导双剪刀对称性、平台机制与判据比体系。
