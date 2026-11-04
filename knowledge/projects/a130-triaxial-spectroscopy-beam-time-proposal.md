---
type: project
title: "A≈130 质量区三轴手征与摆动运动高自旋在束 γ 谱学实验机时申请书（Beam-Time Proposal）"
aliases: [A130-beam-time-proposal, 131Ce-133Ce-proposal, 135Pr-wobbling-proposal, 在束谱学机时申请书]
created: 2026-11-04
updated: 2026-11-04
status: active
review_status: unreviewed
project_stage: beam-time-proposal-ready
confidentiality: private
tags: [experiment-proposal, beam-time, in-beam-spectroscopy, heavy-ion-fusion, 131ce, 133ce, 135pr, clover-polarimetry, dco-ratio, count-rate-budget]
---

# A≈130 质量区三轴手征与摆动运动高自旋在束 γ 谱学实验机时申请书（Beam-Time Proposal）

## Research Question

如何从实验上终局性澄清 $A \a$A \aA \a130$ 质量区奇中子核 $^{131,133}\text{Ce}$ 与奇质子核 $^{135}\text{Pr}$ 的高自旋激发模式争议（三轴量子摆动运动 vs 旋称伙伴带 / $\gamma$ 软核声子耦合）？
核心解决三大前沿科学问题：
1. **$^{131,133}\text{Ce}$ 跨带连接线电磁多极性与绝对跃迁几率**：实测带间 $\Delta I=1$ 跃迁的线偏振度 $P$ 与多极混合比 $\delta(E2/M1)$，以 $>3\sigma$ 置信度打破数学双根退化，判决其究竟为四极集体增强（$E2$ 占优）还是偶极占优（$M1$ 占优）；
2. **$^{135}\text{Pr}$ 横向摆动争议的独立重测与一致性仲裁**：在更优信噪比与高重数符合下，复核 $747.5\text{ keV}$ $17/2^+ \to 15/2^+$ 等关键退激跃迁的康普顿不对称度，裁决 Matta 2015 摆动解与 Lv 2022 伙伴带解；
3. **高自旋微观寿命与内禀形变 $Q_t$ 测定**：利用多普勒频移衰减法（DSAM）与反冲距离活塞法（RDM），提取带内与带间各能态皮秒至纳秒寿命，直接反演绝对过渡几率比值 $B(E2)_{\text{out}} / B(E2)_{\text{in}}$。

---

## Current Hypotheses

### 假设 1：真实三轴横向摆动运动（Transverse Wobbling, TW）
- **能谱与电磁特征**：横向摆动声子激发使摆动带（$n_w=1$）与 Yrast 轴能带（$n_w=0$）同宇称且自旋相差 $\Delta I=1$；摆动能量随自旋增加单调下降（$d\hbar\omega_{\text{wob}}/dI < 0$）；
- **决定性实验判据**：跨带连接线为强烈 $E2$ 占优（$|\delta| > 1.5, f_{E2} > 70\%$），线偏振度表现为特征正值（$P > 0$），跃迁强度比呈现集体增强（$B(E2)_{\text{out}}/B(E2)_{\text{in}} \a0.2 - 0.5$），而带间偶极跃迁被剧烈压低（$B(M1)_{\text{out}} \ll 0.1\ \mu_N^2$）。

### 假设 2（竞争解释）：旋称伙伴带与 $\gamma$ 软核声子耦合（Signature Partner / $\gamma$-Vibrational Coupling）
- **能谱与电磁特征**：核芯有效三轴势极浅，具有强烈的 $\gamma$ 自由度涨落；所谓的“摆动带”物理本质为单粒子轨道在主平面内的倾斜转动伴随微弱平面倾角摆动，或单准粒子与大振幅 $\gamma$ 振动声子耦合（$\gamma \otimes qp$）；
- **决定性实验判据**：跨带跃迁实际为 $M1$ 占优的小混合比解（$|\delta| \sim 0.2 - 0.5, f_{M1} > 80\%$），线偏振度表现为负值（$P < 0$），带间四极跃迁微弱无集体增强（$B(E2)_{\text{out}}/B(E2)_{\text{in}} \le 0.05$），彻底否定摆动解释。

---

## Evidence Available

### 1. 反应体系优选与束流能量优化
基于林承键《重离子核反应》熔合截面模型与 PACE4 统计蒸发模拟，优选重离子重核聚变出射道：
- **目标体系 A：$^{134}\text{Ce} / {}^{133}\text{Ce}$**：
  - 反应道：${}^{16}\text{O} + {}^{122}\text{Sn} \to {}^{138}\text{Ce}^* \to {}^{134}\text{Ce} + 4n \quad (E_{\text{lab}} = 76\text{ MeV})$
  - 反应道：${}^{16}\text{O} + {}^{122}\text{Sn} \to {}^{138}\text{Ce}^* \to {}^{133}\text{Ce} + 5n \quad (E_{\text{lab}} = 86\text{ MeV})$
  - 库仑势垒（Bass 模型）：$V_B = 53.8\text{ MeV}$，质心最佳能量 $E_{\text{c.m.}}(4n) = 67.1\text{ MeV}$；
  - 预测峰值截面：$\sigma(4n) = 385\text{ mb}$，$\sigma(5n) = 290\text{ mb}$；
  - 复合核平均角动量：$\langle \ell \rangle \approx 36\ \hbar$，最大入流角动量 $\ell_m_m_{\max} \approx 48\ \hbar$，完美匹配高自旋物理区。
- **目标体系 B：$^{131}\text{Ce}$**：
  - 反应道：${}^{36}\text{S} + {}^{100}\text{Mo} \to {}^{136}\text{Ce}^* \to {}^{131}\text{Ce} + 5n \quad (E_{\text{lab}} = 150\text{ MeV})$
  - 或采用 ${}^{16}\text{O} + {}^{120}\text{Sn} \to {}^{131}\text{Ce} + 5n \quad (E_{\text{lab}} = 90\text{ MeV})$。
- **目标体系 C：$^{135}\text{Pr}$**：
  - 反应道：${}^{16}\text{O} + {}^{123}\text{Sb} \to {}^{139}\text{Pr}^* \to {}^{135}\text{Pr} + 4n \quad (E_{\text{lab}} = 78\text{ MeV})$。

### 2. 靶设计与反冲运动学
- **角分布与偏振测量用靶**：$1.0\text{ mg/cm}^2$ 同位素富集靶（$^{122}\text{Sn}$ 富集度 $>98\%$），压制在 $15\text{ mg/cm}^2$ 金（Au）衬底上；反冲核在 $\sim 1.2\text{ ps}$ 内在金点阵中完全停阻，彻底消除真空退取向效应（$G_k \to 1.0$）；
- **反冲核运动学速度**：质心反冲初速度 $v/c = \sqrt{2 E_{\text{lab}} M_p} / (M_p + M_t) c \a1.82\%$；
- **薄靶自支撑（用于 RDM 活塞测寿命）**：$0.6\text{ mg/cm}^2$ 无衬底自支撑靶，反冲核穿出靶箔飞行速度色散 $\Delta v/v \le 3.5\%$。

### 3. HPGe/Clover 探测器阵列几何布局与性能参数
配置包含 12 台 Clover 探测器与 16 台同轴 HPGe 探测器的现代高精度核谱仪（如中国原子能院或南非 iThemba 阵列构型）：
- **垂直环配置（$90^\circ$ 环）**：布置 8 台四晶体复合 Clover 探测器，专门用于测量散射不对称度 $\Delta_{\text{IPDCO}}$ 与线偏振度 $P$；
- **前向与后向环配置（$30^\circ / 150^\circ$ 环）**：布置各 4 台探测器，用于精确测定角分布比值 $R_{\text{DCO}}$ 与 $R_R_{\text{ADO}}$；
- **康普顿抑制**：全探头配备 BGO 闪烁体反符合屏蔽套，将能量谱 Peak-to-Total 峰总比从未抑制的 $0.18$ 提升至 $0.54$ 以上。

### 4. 计数率与机时预算核算表
- 入射离子束流强：$I_p = 3.0\text{ pnA}$（粒子流强 $1.87 \times 10^{10}\text{ ions/s}$）；
- 靶原子面密度：$N_t = (1.0 \times 10^{-3}\text{ g/cm}^2 / 122\text{ g/mol}) \times 6.022 \times 10^{23} = 4.94 \times 10^{18}\text{ cm}^{-2}$；
- 目标核生成率：
  $$R_{\text{prod}} = I_p \cdot N_t \cdot \sigma_{4n} = (1.87 \times 10^{10}) \times (4.94 \times 10^{18}) \times (385 \times 10^{-27}) \approx 3.56 \times 10^4\text{ nuclei/s}$$
- 阵列总全能峰探测效率（$E_\gamma = 500\text{ keV}$）：$\epsilon_{\text{tot}} = 3.2\%$；
- 二重 $\gamma-\gamma$ 符合触发事件率：
  $$R_{\gamma\gamma} = R_{\text{prod}} \cdot \langle M_\gamma \rangle \cdot (\langle M_\gamma \rangle - 1) \cdot \frac{\epsilon_{\text{tot}}^2}{2} \approx 2.45\text{ kHz}$$
- **统计量目标**：为使强度仅为基带 $5\%$ 的弱带间跨带线（$\sim 500\text{ keV}$）获得 $N_{\text{peak}} \ge 1200$ 净计数，并在 Clover 垂直环上以 $>3\sigma$ 显著性判定线偏振度（$\sigma_P \le 0.04$），需要累积**总有效二重符合事件数 $\ge 1.2 \times 10^8$ 个**。
- **净物理机时需求**：
  $$T_{\text{beam}} = \frac{1.2 \times 10^8}{2450\text{ s}^{-1} \times 3600\text{ s/h}} \a13.6\text{ 小时 (纯有效曝光)}$$
  考虑加速器调束、能量扫描（3 个能量点）、靶更换、死时间（$\sim 25\%$）以及探测器在线标定（$^{152}\text{Eu}$ 源）：
  $$\text{总申请机时} = 144\text{ 小时（6 个物理运行工作日）}$$

---

## Risks and Blockers

1. **强束流靶箔热烧损风险**：$3.0\text{ pnA}$ 的 $^{16}\text{O}$ 束流在金衬底靶上沉积功率约为 $0.25\text{ W}$，若束斑面积较小（$< 2\text{ mm}^2$），容易引起局部过热熔融；**对策**：采用束流静电摇摆器（Beam Wobbler）扩大照射面积至 $5\text{ mm} \times 5\text{ mm}$，并在靶框背部加装水冷散热回路；
2. **多重近能重叠双峰污染（Multiplet Doublets）**：奇 $A$ 核能谱密度高，邻近存在相差 $< 1.5\text{ keV}$ 的同能跃迁；**对策**：在离线分析中采用多重门解卷积算法与三维对称立方体（$\gamma-\gamma-\gamma$）选门验证；
3. **高能区 Clover 偏振灵敏度衰减**：当跃迁能量高于 $1.2\text{ MeV}$ 时，康普顿散射不对称度参数 $Q(E_\gamma)$ 降至 $0.12$ 以下；**对策**：重点监测低中自旋区（$400 \sim 900\text{ keV}$）关键带头跨带跃迁。

---

## Next Actions

1. 向加速器大科学装置束流评审委员会（PAC）正式递交本 Proposal 文本；
2. 在实验室制作 $^{122}\text{Sn}/\text{Au}$ 与 $^{120}\text{Sn}/\text{Au}$ 夹层靶箔，并通过 $\alpha$ 粒子透射测厚仪标定实际面密度均匀性；
3. 利用标准放射源（$^{152}\text{Eu}, {}^{133}\text{Ba}, {}^{60}\text{Co}$）在实验大厅对 Clover 偏振阵列执行全角度几何不对称参数 $a_{\text{geo}}(E_\gamma)$ 离线精密标定；
4. 部署 `nuclear_analyzer.py` 工具链至实验离线处理服务器，确保实验期间 List-mode 数据的实时在线分选与符合矩阵构建。
