---
type: research-note
title: "A130重写研学：磁矩型、电荷型M1与辐射率数值归一"
aliases: [A130 M1 magnetic and charge-type normalization]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "T15窄审、Suhonen原PDF134及A130第5.9节整合"
promotion_target: ""
reading_depth: selected-pages
source_type: multi-source-analysis
evidence_sources: [book-suhonen-from-nucleons-to-nucleus, lange-kumar-hamilton-1982-multipole-admixtures]
tags: [transition-probabilities, magnetic-dipole, unit-systems, SI-vs-Gaussian, rate-constants]
---

## Research Trigger

第5.9节的实用辐射率与第2.7节的常规磁矩算符需要统一。问题是带单位物理量
和除以命名单位后的数值被混淆，而非两套实用公式可任意额外乘除光速。

## Grounded Evidence

总控回读Suhonen原PDF p.134／印刷p.119的Eq.(6.7)、(6.9)与footnote 6，
核对辐射率和磁算符中的光速因子。T15仅承担这一窄范围复核。
这里首先比较SI中的磁矩型与电荷型算符；完整Gaussian和SI的互换
还需同时处理电荷单位及电磁常数，不能仅用一个裸 $c$ 代表。

## Provisional Reasoning

## Claims and Thesis Relevance

1. **磁偶极算符的两种主要量纲约定：**低能核结构文献中并存两类磁偶极跃迁算符定义。第一类为常规核物理教材（如第2.7节、Bohr--Mottelson卷I与Rose--Brink体系）采用的**磁矩型算符** $\mathcal{M}_\mu(M1)$，其以核磁子 $\mu_N = e\hbar/(2m_p)$（SI单位：$\mathrm{A\cdot m^2}$ 或 $\mathrm{J/T}$）为基础单元，对应的约化跃迁几率 $B_\mu(M1)$ 量纲为 $\mu_N^2$。第二类为 J. Suhonen 专著《From Nucleons to Nucleus》采用的**电荷型磁算符** $\mathcal{M}_S(M1)$，通过显式引入 $1/c$ 因子使电多极与磁多极算符具有统一步调的电荷乘长度量纲（$\lambda=1$ 时为 $\mu_N/c \sim e\cdot\mathrm{fm}$），其约化跃迁几率记作 $B_S(M1)$，量纲为 $(\mu_N/c)^2$。
2. **两套算符的精确量纲与代数映射：**二者在算符层面的严格关系为 $\mathcal{M}_S(M1) = \mathcal{M}_\mu(M1)/c$；在约化矩阵元模平方层面，物理量满足 $B_S(M1) = B_\mu(M1)/c^2$。
3. **无量纲基准数值的完全恒等性：**当将物理跃迁几率按各自选定的基准单位归一化为无量纲纯数值 $b_{M1}$ 时：
   $$b_{M1} \equiv \frac{B_S(M1)}{(\mu_N/c)^2} = \frac{B_\mu(M1)}{\mu_N^2}$$
   由于分子与分母中各自携带的 $c^2$ 量纲因子严格相消，两套体系定义的无量纲数值 $b_{M1}$ 完全恒等。
4. **实用跃迁率常数的数值不变性与错误更正：**在实用光子辐射跃迁率公式 $\lambda_\gamma(M1) = C_{M1} (E_\gamma/\mathrm{MeV})^3 b_{M1}$ 中，印出常数 $C_{M1} \approx 1.7584 \times 10^{13}\,\mathrm{s}^{-1}$。以 $(\mu_N/c)^2$ 表达的单位系数与以常规 $\mu_N^2$ 表达的单位系数在数值上完全相同。**历史版本中关于在不同单位制转换时对实用率系数乘以或除以光速 $c^2$ 的表述已被确认为严重量纲混淆并定点更正：不可对已经按命名单位归一后的数值 $b_{M1}$ 或实用常数 $C_{M1}$ 重复乘除带量纲的光速数值 $c^2$。**
5. **多极混合比 $\delta(E2/M1)$ 的分母约定：**混合比定义为辐射场几率振幅之比，与约化矩阵元之比的关系中分母必须明确为电荷型算符 $\mathcal{M}_S(M1)$，即 $\delta = \frac{\sqrt{3}}{10} \frac{E_\gamma}{\hbar c} \frac{\langle I_f \| \mathcal{M}(E2) \| I_i \rangle}{\langle I_f \| \mathcal{M}_S(M1) \| I_i \rangle}$；若分母采用常规磁矩型算符 $\mathcal{M}_\mu(M1)$，则需在分子配入 $c$ 因子（与动量项结合为 $E_\gamma/\hbar$）以保持 $\delta$ 无量纲及数值自洽。

本笔记与 [[a130-rewrite-absolute-rates-and-selection-boundaries-20261108]] 形成直接回链：原研究笔记中关于 $M1$ 速率公式需由光速 $c^2$ 进行数值缩放的推断已被撤销并由本笔记定点纠正。

## Sources and Reading Depth

本研究笔记基于以下文献原件特定页码的直接核读（selected-pages）：

- [[book-suhonen-from-nucleons-to-nucleus]]：
  - PDF 第 133 页（印刷第 118 页），式 (6.3)：给出真空介电常数 $\varepsilon_0$ 表达的自发多极辐射跃迁几率基本积分定义。
  - PDF 第 134 页（印刷第 119 页），式 (6.4)、(6.6)–(6.9) 及脚注 6：明确电磁多极算符定义，式 (6.7) 显式包含 $\mu_N/(\hbar c)$，脚注 6 特别指出高斯单位制下核磁子定义为 $\mu_N = e_{\mathrm{G}}\hbar/(2m_pc)$，提醒不可将高斯定义与 SI 荷质数值混淆。
  - PDF 第 135 页（印刷第 120 页），式 (6.10)–(6.14)：给出电磁多极相位因子 $\zeta_\lambda$（对 $M1$ 在 Condon-Shortley 与 Rose-Brink 约定下均为 $+1$），$B(M\lambda)$ 单位明确印为 $(\mu_N/c)^2\,\mathrm{fm}^{2\lambda-2}$；式 (6.14) 给出数值前因子 $C_{M1} = 6.080 \times 10^{20} \times (2/9) / (197.33)^3\,\mathrm{s}^{-1} \simeq 1.7584 \times 10^{13}\,\mathrm{s}^{-1}$。
  - PDF 第 137 页（印刷第 122 页），式 (6.19)–(6.21)：定义多极混合比 $\Delta$ 与无量纲系数 $d$，印出常数验证式 (6.21) 给出 $0.835\,E_\gamma[\mathrm{MeV}]$，与由 $\sqrt{C_{E2}/C_{M1}} \times 100 \approx 0.83468$ 完全吻合。
- [[lange-kumar-hamilton-1982-multipole-admixtures]]：
  - PDF 第 3–4 页（印刷第 121–122 页），式 (2.1)–(2.6)：明确电多极与磁多极发射场幅度之比的定义式，光子波数 $k = E_\gamma/(\hbar c)$ 与混合比平方 $\delta^2 = \lambda_\gamma(E2)/\lambda_\gamma(M1)$ 的普遍关系。

## Methodological Audit

以下磁矩表达式中的轨道和自旋算符均已除以 $\hbar$，使用无量纲角动量分量。
混合比的符号还须沿用第5.9节同一套算符与辐射相位约定，不能只凭单位关系另定符号。

1. **算符与量纲的自洽链条：**
   在 SI 单位制下，单核子内禀磁矩算符为：
   $$\boldsymbol{\mu} = \mu_N \left( g_l \mathbf{l} + g_s \mathbf{s} \right), \qquad \mu_N \equiv \frac{e\hbar}{2m_p}$$
   第2.7节定义的球张量磁矩算符为 $\mathcal{M}_\mu(M1) = \sqrt{\frac{3}{4\pi}} \mu_N \sum_{k} \left[ g_l^{(k)} \mathbf{l}_k + g_s^{(k)} \mathbf{s}_k \right]$，具有磁偶极矩量纲 $\mathrm{J/T}$。
   而在 Suhonen 式 (6.7) 中，取 $\lambda=1$ 并在球坐标下利用 $\nabla(r Y_{1m}) = \sqrt{\frac{3}{4\pi}} \mathbf{e}_m$，电荷型磁算符表达为：
   $$\mathcal{M}_S(M1) = \frac{\mu_N}{c} \sqrt{\frac{3}{4\pi}} \sum_{k} \left[ g_l^{(k)} \mathbf{l}_k + g_s^{(k)} \mathbf{s}_k \right] = \frac{\mathcal{M}_\mu(M1)}{c}$$
   该算符直接除以光速 $c$，使得量纲为 $\mathrm{A\cdot m^2 / (m/s) = A\cdot s\cdot m = C\cdot m} \sim e\cdot\mathrm{fm}$。
2. **跃迁几率常数的代数展开：**
   辐射场的自发跃迁几率为物理量，其数值不随所选表象或算符记号改变：
   $$\lambda_\gamma(M1) = K_S B_S(M1) = K_\mu B_\mu(M1)$$
   对这里含标准球谐归一的约化跃迁算符，电荷型M1辐射率系数为：
   $$K_S(E_\gamma) = \frac{1}{4\pi\varepsilon_0} \frac{16\pi}{9\hbar} \left(\frac{E_\gamma}{\hbar c}\right)^3.$$
   不能将这个完整球张量系数误换成 $4/(9\hbar)$；后者会漏掉 $4\pi$。
   当 $B_S(M1) = B_\mu(M1)/c^2$ 时，代入得：
   $$K_\mu(E_\gamma)=\frac{K_S(E_\gamma)}{c^2}
   =\frac{\mu_0}{4\pi}\frac{16\pi}{9\hbar}
      \left(\frac{E_\gamma}{\hbar c}\right)^3.$$
   两式完全等价。当引入命名基准单位 $\mu_N$ 与 $\mu_N/c$ 后，由于 $b_{M1}$ 相同，提取出无量纲比值后的数值系数：
   $$C_{M1}=K_S(1\,\mathrm{MeV})(\mu_N/c)^2
   =K_\mu(1\,\mathrm{MeV})\mu_N^2
   \simeq1.7584\times10^{13}\,\mathrm{s}^{-1}.$$
   在 $\lambda_\gamma=C_{M1}(E_\gamma/\mathrm{MeV})^3b_{M1}$ 中，
   两套表述使用相同的带率单位系数，不能再乘一次能量三次方的单位。
3. **更正历史推论中的物理错误：**
   此前部分技术笔记误认为“若 $B(M1)$ 单位由 $(\mu_N/c)^2$ 改为 $\mu_N^2$，前因子 $C_{M1}$ 必须除以 $c^2$（以 $\mathrm{fm/s}$ 计算约 $9\times 10^{46}$）”，该错误在于将**物理量系数变换**与**实用单位归一化数值**混为一谈。一旦除以光速数值，算得的跃迁率将产生 47 个数量级的荒谬偏差。

## Empirical Boundaries

- 适用的测量技术：在束伽马符合谱学中由激发态平均寿命 $\tau$、分支比 $b_k$、内转换系数 $\alpha_k$ 与多极混合比 $\delta$ 反演绝对 $B(M1)$。
- 适用能区：低能核物理离散能级跃迁（典型的 $E_\gamma \sim 0.05 - 5\,\mathrm{MeV}$）。
- 绝热假定：本关系建立在单光子偶极辐射算符基础上，未包含双光子虚激发或连续谱直接衰变通道。

## Assumptions

引用的实用公式保留其能量、强度命名单位及算符定义；两种物理量先分别
除以对应的命名单位，再比较无量纲数值。总分支、光子分支与ICC另行归一。

## Competing Explanations

- **体系一（Suhonen SI体系）：**所有电磁算符均具有电荷乘长度幂次量纲 $e\cdot\mathrm{fm}^\lambda$，优点是多极形式高度统一，缺点是与核物理传统磁矩习惯（$\mu_N$）存在量纲换算隔阂。
- **体系二（Bohr--Mottelson / Rose--Brink 体系）：**电多极算符采用 $e\cdot\mathrm{fm}^\lambda$，磁算符采用 $\mu_N\cdot\mathrm{fm}^{\lambda-1}$，优点是直观对应壳模型磁矩预测，缺点是多极混合比 $\delta(E2/M1)$ 公式中需显式包含 $\hbar c$ 与动量因子。

## Transfer Conditions

- 从壳模型微观计算（输出单位通常为 $\mu_N^2$）到实验寿命预测：直接代入实用公式 $\lambda_\gamma(M1) = 1.7584 \times 10^{13} \times (E_\gamma/\mathrm{MeV})^3 \times [B(M1)/\mu_N^2]\,\mathrm{s}^{-1}$。
- 从在束寿命实验反演微观跃迁几率：直接将无量纲比值赋予单位 $\mu_N^2$（磁矩型）或 $(\mu_N/c)^2$（电荷型），数值完全一致。

## Failure Conditions

- 在实用反演公式中对已归一的 $B(M1)$ 额外乘除带单位的光速 $c$ 或 $c^2$。
- 将高斯单位制下的无量纲电荷公式与 SI 制下的绝对磁子数值混用。
- 将混合比 $\delta$ 误作初末态裸多极矩阵元的直接无量纲相除而忽略辐射场光子能量因子。

## Falsification or Reverse Tests

- **1 MeV 命名单位基准的反向验证：**
  取 $E_\gamma = 1.000\,\mathrm{MeV}$，$b_{M1} = 1.000$（即 $B_\mu = 1\,\mu_N^2$ 或 $B_S = 1\,(\mu_N/c)^2$）。
  根据 Suhonen 式 (6.14)：
  $$\lambda_\gamma = 1.7584 \times 10^{13}\,\mathrm{s}^{-1}$$
  对应纯光子辐射分寿命 $\tau_\gamma = 1/\lambda_\gamma \approx 5.687 \times 10^{-14}\,\mathrm{s} = 56.87\,\mathrm{fs}$。
  无论采用磁矩型定义还是电荷型定义，其物理寿命与辐射速率完全一致，验证了代数变换的零误差闭环。

## Open Questions

- 相对论自旋-轨道重整化与动量相关算符在高阶禁戒跃迁中的量纲自洽性。
- 手征两体流（2BC）与介子交换流在超精细能级磁偶极跃迁中的有效算符定义对齐。

## Human Review

- 本研究笔记非人类专家人工审核（unreviewed），由智能体依据 J. Suhonen (2007) 原书第 6 章印刷页码与 Terra T15 窄范围数学审查回执（`outputs/.../T15/report.json`）自主推导建立。

## Promotion or Rejection History

- 2026-11-13：根据总控授权与 Terra T15 审查意见正式建立；更正了此前技术笔记中关于 $M1$ 速率公式需乘除 $c^2$ 的历史错误推论，为博士论文第 2.7 节与第 5.9 节的电磁单位体系对齐提供底层微观证据支持。
