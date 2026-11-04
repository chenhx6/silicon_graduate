---
type: project
title: "30天后核结构论文 prospectus"
aliases: [post-30-day paper prospectus, nuclear-structure paper queue]
created: 2026-10-30
updated: 2026-10-30
status: active
review_status: unreviewed
project_stage: post-30-day-prospectus
confidentiality: private
nuclei: [131xe, 135pr, 135nd, 144ba, 146ba]
tags: [paper-prospectus, nuclear-structure, evidence-gate, l3, l4-readiness]
---

# 30天后核结构论文 prospectus

## Agent active summary

本页把30天学习计划中已经形成的证据地图压缩为五个可投稿研究候选。它们是研究队列，不是已完成稿件；每个候选都必须重新经过 `system/paper-evidence-gate.md`，补齐 source identity、locator、独立性、反证和适用条件。

## Research Question

在现有 Wiki 的实验谱学、混合比、偏振、寿命、形变和响应合同基础上，哪几条路线最可能在30天后形成有证据边界的期刊稿件？选择标准是：问题明确、已有 primary source、存在竞争解释、可写出 falsifier，并且缺失输入不会被模型或 toy 计算掩盖。

## Current Hypotheses

- P1 `135Pr` 最可能先形成方法学论文，因为支持链与反方链的差异已经落在可定义的观测量和响应合同上。
- P2 `131Xe` 最可能先形成对象身份/可识别性论文，因为当前主要增量是撤回过度解释并明确缺失 companion observables。
- P3/P4 需要更多真实绝对强度、寿命或多态 E3 输入；P5已有真实表格falsifier，但外部方法学新颖性仍需核查。

## Evidence Available

现有证据来自 `knowledge/sources/` 的直接论文、评估数据和方法原件，已在各 candidate 的 project/synthesis/source 页按 locator 分层。论文 prospectus 只汇总这些入口，不把 project、日报或 toy 工件当作新的独立实验。

## Candidate Queue

| 优先级 | 候选题目 | 研究核心 | 当前状态 | 最小新增输入 |
|---|---|---|---|---|
| P1 | `135Pr` common-response evidence audit | 统一 Matta–Lv–Sensharma 的 `δ` 分支、`P/A`、`R_ac`、取向和谱系，检验 wobbling/chirality/TiP 排序 | L3+ 条件性联合似然审计完成；Gammasphere 纯角分布双根退化（Δχ²=0.000），声明 toy response 下 JUROGAM II 偏振偏好小根（Δχ²=122.3）；不称为实验 11.1σ 排除 | 逐角净峰、sideband、`a(E)`/`Q(E)`、polarization counts、gate acceptance、联合 `Σ` |
| P2 | `131Xe` low-spin identity and branch boundary | 2020/2023 逐态对象交叉、795-keV宇称版本、RDCO双根和同母态强度可识别性 | L3 milestone；对象和缺口已固化，未裁决宇称/模式 | 1983 AD/ICE原件或逐线 raw/response、794.8-keV独立宇称判据、882偏振/AD和partner寿命 |
| P3 | `135Nd/134Pr` partner-resolved absolute EM benchmark | 绝对 `B(E2)`/`B(M1)`、寿命、crossing、γ-softness 与手征/混合竞争解释 | L3/L4 candidate；多条寿命证据已有，矩阵和共同协方差未闭合 | 同一 state mapping 下的完整 EM 矩阵、寿命 producer、feeding/systematic covariance |
| P4 | Cross-mass octupole evidence ladder | 直接 E3、E1 网络、交替宇称和 PES 形变之间的证据等级与静态/动态边界 | synthesis/data-map candidate；144/146Ba、220Rn/224Ra、208Pb与132Sn已有锚点 | 逐条 primary locator、统一跃迁方向/单位、分支归一、共同系统误差和更多多态 E3 |
| P5 | P-ADO shared-alignment null falsifier | 用Zobel 1983同一跃迁十行真实表格检验跨reaction共享`σ/J`的可识别性 | 有真实表格结果；方法学新颖性和外部文献差异仍需审计 | projectile-family分层、原始Cov/coverage或feeding-aware公开输入 |
| P6 | `131Ce/133Ce` collective-mode identifiability boundary | 结合中期报告 iThemba LABS PR295、CIAE HI-13 数据和 NuclearMap 邻核先验，用连接线 `δ`/偏振、寿命和响应合同区分三轴集体模式 | L3+ 条件性合成完成；`133Ce` 私有 workbook 派生量不支持简单单声子 wobbling，但尚不能确立 signature partner/TiP，也不能把 N=73→N=75 演化或共享质子回弯写成实验结论 | 逐线 `δ`/偏振、partner 寿命/`B(E2)`/`B(M1)`、直接 `133Ce` 微观 PES、producer lineage、holdout 与统一协方差 |
| P7 | Full-library claim calibration and epistemology ledger | 全库50+核心文献在实验事实、模型计算与作者解释之间的语言与证据边界校准 | 知识治理/方法学prospectus；自审账本已建立 | 逐篇历史source的动词重审、定位校准与独立性反证核查 |

## Candidate 1: 135Pr common-response evidence audit

### Research Question & Core Objective
在 $^{135}\text{Pr}$ 低自旋横向摆动（transverse wobbling）争议中，统一 Matta 2015、Lv 2022 与 Sensharma 2026 三方证据，建立共同探测器响应、对齐参数 $\sigma/I$、门污染与多极混合比 $\delta$ 提取合同，判决各实验结论的兼容域与失效条件。

### Grounded Evidence & Primary Sources
- Matta et al. 2015 ([[matta-2015-transverse-wobbling-135pr]]): Gammasphere/INGA 数据报告若干 E2-rich、大 \(|\delta|\) 连接支和正的偏振不对称，并据此提出 \(n_w=1\) 横向 wobbling 解释；
- Lv et al. 2022 ([[lv-2022-evidence-against-wobbling-135pr]]): 独立多探测器阵列联合角分布、偏振和 \(R_{ac}\)，对 747、813、450 keV 线给出小 \(|\delta|\) 分支和 M1-dominated 解释；该结果是反方 source interpretation，不能写成无条件排除所有 wobbling；
- Sensharma et al. 2026 ([[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]]): 重新分析 Gammasphere 历史数据，在固定 $\sigma/I=0.2$ 条件下声称拟合优度偏好大 $\delta$ 解；
- 135Pr 联合似然比审计研究笔记 ([[pr135-gammasphere-vs-jurogam-joint-likelihood-audit-20261101]]): 在声明的 toy response 下，Gammasphere 角分布对 $\delta_1=-1.83$ 与 $\delta_2=-0.47$ 完全退化（$\Delta\chi^2_{\text{ang}}=0.000$），加入 Lv 报告的 JUROGAM II 偏振值后偏好小根（条件性 $\Delta\chi^2_{\text{joint}}=122.3$）；该结果不是实验 11.1σ，也不独立证明 signature-partner 机制。相对 $B(E2)$ ratio 只作条件性敏感性检查；
- Chen et al. 2026 贝叶斯转动惯量模型 (accepted record): 仅基于能谱能量约束的 MCMC 条件后验。

### Competing Hypotheses
1. 横向 wobbling 模式（Matta et al.）
2. 倾斜轴进动 / Tilted precession 模式（Lv et al.）
3. 单准粒子非对称核转动 / Signature partner 组态混合

### Minimal New Inputs
- 逐角净峰计数值、门污染分数（特别是 $747, 771, 800\text{ keV}$ 连接线周围的杂质扣除）；
- 真实的角分布响应矩阵 $a(E)$ 与线偏振探测灵敏度标定 $Q(E)$；
- 原始 Gammasphere 与 Lv22 探测器几何的统一联合误差协方差 $\Sigma$。

### Response Matrix & Joint Covariance Contract
必须联合考虑探测器效率、立体角有限角修正因子 $Q_2, Q_4$、门选择的角关联扰动以及多极干涉项的协方差；严禁采用标量误差的高斯平方反比加权。

### Falsifiers (证伪判据)
若在无预设立场（即放开 $\sigma/I$ 并在 $[0.15, 0.35]$ 全局边际化）且考虑门谱杂质时，Matta 数据与 Lv 数据的联合似然度在 $99\%$ 置信区间内完全不相交，则“单一统一物理态解释”被实验证伪，表明存在未识别的系统性实验效应或杂质污染。

### Stop Conditions (停止条件)
在未获得 Gammasphere 原始符合矩阵或各角原始拟合峰面积前，停止生成代理 $L4$ 联合置信区间；不得将模型先验伪造成实验拟合结果。

### Non-Independent Evidence Ledger (非独立证据边界)
Matta 2015 与 Sensharma 2026 共享同一套 Gammasphere 数据集谱系（`independent_experiment_count: 1`），Sensharma 2026 是同一数据的重新参数化条件拟合，不能与 Matta 2015 一起算作支持 wobbling 的两份独立实验证据。

## Candidate 2: 131Xe low-spin identity and branch boundary

### Research Question & Core Objective
在 $^{131}\text{Xe}$ 低自旋带间连接跃迁中，检验 1600.9-keV 节点 794.8-keV 宇称指认版本冲突，以及 881.8-keV 跃迁混合比 $\delta$ 双根的分辨边界，建立同母态强度商可识别性与停止规则。

### Grounded Evidence & Primary Sources
- Banik et al. 2020 ([[banik-2020-131xe-multiple-band-structures]]): 报道 794.8-keV $E1$ 跃迁与 $R_{DCO}=0.55(1)$、$\Delta_{PDCO}=+0.03(1)$；
- Chakraborty et al. 2023 ([[chakraborty-2023-131xe-wobbling-origin]]): 重新分析同一数据，将 1600.9-keV 态标为 $17/2^-$，给出 881.8-keV $R_{DCO}=0.64(11)$ 并选择小正根 $\delta=+0.09(8)$ 解释为 signature partner；
- Jehangir et al. 2022 ([[jehangir-2022-odd-neutron-tpsm-extension]]): 奇中子 TPSM 比较（引用 Banik 2020 数据）；
- Irving 1979 ([[irving-1979-131xe-spectroscopy-scope]]) & Lönnroth 1983 ([[lonnroth-1983-xe-quasiparticle-states]]): 历史角分布与转换电子谱学（当前处于 metadata-only 边界）。

### Competing Hypotheses
1. 负宇称 yrare 序列为单准中子 signature partner 跃迁（Chakraborty et al.）
2. 纵向/横向 low-spin wobbling 激发态（Banik et al. 早期候选与多核素系统学讨论）
3. 偶极/四极微观三轴组态混合态

### Minimal New Inputs
- 794.8-keV 跃迁的高分辨率内转换电子（ICE）谱或明确的转化系数 $\alpha_K$；
- 881.8-keV 跃迁的高统计线偏振不对称度测量或 880.1-keV 双线的完整解谱；
- 历史 Irving 1979 / Lönnroth 1983 的逐行实验数据表。

### Response Matrix & Joint Covariance Contract
881.8-keV 与 880.1-keV 双线必须建立成对符合响应函数，且对同母态 1055.1-keV 与 815.6-keV 跃迁的比值 $B(M1)/B(E2)$ 建立统一协方差矩阵。

### Falsifiers (证伪判据)
若新的高统计偏振或内转换实验证实 881.8-keV 跃迁选择大绝对值混合比根（$|\delta| > 1.5$ 且 $B(E2)$ 占优），则会削弱当前的纯 signature-partner 解释；反之若测得 $\delta \approx 0$ 且 $\Delta_{PDCO} < 0$（在声明响应约定下偏向磁偶极），则会削弱最简单的 wobbling 参数化。两种结果都不能脱离共同 response、branch、feeding 和协方差合同完成机制终局裁决。

### Stop Conditions (停止条件)
在未获得原始符合计数矩阵、偏振计数或内转换数据前，严禁伪造连续高斯响应或给出任一混合比分支的后验概率；保持 L3 readiness 状态。

### Non-Independent Evidence Ledger (非独立证据边界)
Banik 2020、Jehangir 2022 和 Chakraborty 2023 全部基于加尔各答 VECC K-130 回旋加速器上的同一次 38-MeV INGA 实验（`vecc-131xe-inga-38mev-130te-a3n`，`independent_experiment_count: 1`）。三者绝不可当作三次独立的实验确认。

## Candidate 3: 135Nd/134Pr partner-resolved absolute EM benchmark

### Research Question & Core Objective
在手征候选核 $^{135}\text{Nd}$ 与 $^{134}\text{Pr}$ 中，通过严格对齐能级寿命、带间/带内绝对跃迁几率 $B(M1)$ 与 $B(E2)$，区分理想静态手征双重带（static chiral doublet）、手征振动（chiral vibration）与软三轴组态混合（shape/configuration mixing）。

### Grounded Evidence & Primary Sources
- Zhu et al. 2003 ([[zhu-2003-135nd-composite-chiral-pair]]): 报道 $^{135}\text{Nd}$ 具有准简并手征候选伙伴带；
- Mukhopadhyay et al. 2007 ([[mukhopadhyay-2007-135nd-chiral-vibration-static]]): 提出从手征振动向静态手征转动的演化；
- Tonev et al. 2006/2007 ([[tonev-2007-134pr-dynamic-chirality]]): Euroball IV 测量 $^{134}\text{Pr}$ 伙伴带寿命，发现带间与带内 $B(E2)$ 存在严重不对称性，质疑静态手征转动；
- Lv et al. 2025 ([[135nd-2025-tipped-precession-same-lineage-extension]]): JUROGAM II 阵列扩展 $^{135}\text{Nd}$ 高自旋能级纲图（报道 $17/2^-_3$ 态与 band T）。

### Competing Hypotheses
1. 静态手征双重带（三轴刚性转动下的非平面取向自发对称性破缺）
2. 手征大振幅振动模式（左手与右手坐标系间的量子隧穿）
3. $\gamma$ 软核转子与准粒子相互作用导致的形状共存/混合态

### Minimal New Inputs
- 同一能级标记下的伙伴态绝对寿命测定（通过 DSAM 或 RDDS）；
- 统一算符约定（operator convention）下的带间连接跃迁 $E2/M1$ 混合比与线偏振；
- 扣除 feeding 延迟与衰减过程的完整系统协方差矩阵。

### Response Matrix & Joint Covariance Contract
必须统一不同实验（如 Euroball IV vs JUROGAM II）的能级退激分支比与分支归一化，冻结多步级联符合效率和减速介质阻止本领（stopping powers）不确定度。

### Falsifiers (证伪判据)
若高精度寿命测量确证两伙伴带的对应带内 $B(E2)$ 强度相差超过 3 倍，或两伙伴带带间跃迁的 $B(M1)$ 强度随自旋单调下降而非出现手征对称恢复峰值，则“理想手征双重带”假说被严格证伪。

### Stop Conditions (停止条件)
禁止在未取得原始寿命衰减曲线或直接多普勒频移峰形时，用唯象模型参数反推实验 $B(E2)$ 绝对值。

### Non-Independent Evidence Ledger (非独立证据边界)
Tonev 2006 与 Tonev 2007 共享同一套 Euroball IV 实验谱系；Lv 2025 沿用 2021 JUROGAM II 采集谱系。不能把同一实验团队在不同刊物上发表的相似寿命数值当成独立测定。

## Candidate 4: Cross-mass octupole evidence ladder and source-page map

### Research Question & Core Objective
跨越偶偶核 $^{144,146}\text{Ba}$、双幻核 $^{132}\text{Sn}$、轻锕系 $^{220}\text{Rn}/^{224}\text{Ra}$ 及 $^{208}\text{Pb}$，建立从直接 $E3$ 矩阵元、交替宇称能带、$E1$ 跃迁电偶极矩到微观八极能面的证据梯级（evidence ladder），严格界定“增强的八极集体性”与“永久静态梨形形变”之间的判定边界。

### Grounded Evidence & Primary Sources
- Bucher et al. 2016/2017 ([[bucher-2016-144ba-direct-octupole]], [[bucher-2017-146ba-direct-octupole]]): GRETINA+CHICO2 安全库仑激发直接测量 $^{144,146}\text{Ba}$ 的 $B(E3; 0^+ \to 3^-_1)$；
- Gaffney et al. 2013 ([[gaffney-2013-pear-shaped-rn-ra]]): REX-ISOLDE/MINIBALL 测量 $^{220}\text{Rn}$ 与 $^{224}\text{Ra}$ 库仑激发，揭示 $^{224}\text{Ra}$ 的强八极关联；
- Rosiak et al. 2018 ([[rosiak-2018-132sn-enhanced-octupole]]): HIE-ISOLDE 库仑激发测得双幻核 $^{132}\text{Sn}$ 的增强单声子 $B(E3)$；
- Henderson et al. 2025 ([[henderson-2025-208pb-deformation-collectivity]]): 多次库仑激发提取 $^{208}\text{Pb}$ 的 $3^-_1$ 态内禀四极矩。

### Competing Hypotheses
1. 稳定的静态非对称内禀形变（永久梨形 / rigid pear shape）
2. 动态八极振动声子激发现象（harmonic or anharmonic octupole vibrations）
3. 浅能面中的八极软核构型涨落与粒子-声子耦合态

### Minimal New Inputs
- 多重库仑激发下的完整对角化跃迁矩阵元集合（包括非对角 $E1, E2, E3$）；
- 统一的跃迁方向定义（退激 $B(E3; 3^- \to 0^+)$ 与激发 $B(E3; 0^+ \to 3^-)$ 的统计权重因子 $(2J_i+1)/(2J_f+1)$ 审计）；
- 独立于库仑激发的绝对寿命（如 GRIFFIN fast-timing / plunger 实验）。

### Response Matrix & Joint Covariance Contract
GOSIA 库仑激发多参数拟合中必须保留不同探测角与散射核碰撞参数之间的完全协方差，严禁仅摘录对角矩阵元而忽略对角与非对角参数间的强相关性。

### Falsifiers (证伪判据)
若对同一核素（如 $^{144}\text{Ba}$），直接测得的内禀电偶极矩 $D_0$ 与直接测得的 $Q_3$ 矩阵元之间不存在平均场自洽约束所要求的正相关关系，或高激发态 $3^-_2$ 呈现单声子而非两声子多重态结构，则“稳定静态八极形变”解释被证伪。

### Stop Conditions (停止条件)
严禁将单个 $B(E3)$ 测量值直接转化为固定的 $\beta_3$ 形变参数并宣称“证实了梨形形变”；必须保持直接矩阵元与唯象模型形变之间的分层边界。

### Non-Independent Evidence Ledger (非独立证据边界)
Bucher 2016 与 2017 共享 GRETINA+CHICO2 方法框架；Gaffney 2013 的 $^{220}\text{Rn}$ 与 $^{224}\text{Ra}$ 数据来自同一轮 MINIBALL 束流运行。

## Candidate 5: P-ADO shared-alignment null falsifier

### Research Question & Core Objective
在在束核谱学提取跃迁多极混合比 $\delta$ 的角分布各向异性（ADO）分析中，检验“跨不同重离子聚变蒸发反应共享自旋取向参数 $\sigma/J$”假设的统计可辨识性与零假说成立条件。

### Grounded Evidence & Primary Sources
- Zobel et al. 1983 ([[zobel-1983-energy-projectile-alignment]]): 系统报道同一 $958\text{ keV}$ 纯 $E2$ 跃迁在 10 种不同反应入射通道（包括不同入射弹核与能量）下的自旋取向宽度 $\sigma$ 与对齐比；
- Zheng et al. 2002 ([[zheng-2002-ado-coincidence-angular-anisotropy]]): 给出 ADO 各向异性比的标准双探测器角排布计算公式；
- P-ADO 零假说审计账本 ([[pado-shared-alignment-null-profile]]): 基于 Zobel 1983 数据的联合剖面似然分析。

### Competing Hypotheses
1. 共享取向假说（不同反应具有普适的 $\sigma/J$ 或可通过固定比例因子迁移）
2. 反应通道敏感假说（$\sigma/J$ 强烈依赖于反应入射角动量带入量、蒸发中子数及侧线 feeding 衰减特征）

### Minimal New Inputs
- 原始各反应通道的逐角拟合原始计数与非对角统计误差；
- 离散能级前级侧线 feeding 的微观角动量取向保留因子。

### Response Matrix & Joint Covariance Contract
必须考虑不同角度探测器间的立体角几何减缩因子 $Q_k$ 与束流摆动（beam wander）带来的系统偏移协方差。

### Falsifiers (证伪判据)
Zobel 1983 十行表格的 table-level Gaussian profile analysis shows that, under
the declared covariance contract, the shared-response discrepancy is large and
requires a sensitivity scale above unity. This is a conditional calibration
warning, not a general experimental falsification of all shared-alignment models.

### Stop Conditions (停止条件)
若实验未对特定反应进行原位（in-situ）自旋取向标定，停止将其他反应通道提取的 $\sigma/I$ 强行代入该实验作混合比精细提取。

### Non-Independent Evidence Ledger (非独立证据边界)
Zobel 1983 表格包含同一实验室在不同能量下的测量系列，需按弹核家族（$\alpha$ 系列 vs $^{12}\text{C}$ 系列）分层考查，不得混为独立样本。

## Candidate 6: 131Ce/133Ce collective-mode identifiability

### Research Question & Core Objective
结合作者博士中期报告（iThemba LABS PR295 实验与 CIAE HI-13 实验）及 NuclearMap 微观先验，以 $^{132}\text{Ce}$ 三轴形变偶偶芯（$\beta=0.22, \gamma=17^\circ$）为基准，在 $^{133}\text{Ce}$（$N=75$）与 $^{131}\text{Ce}$（$N=73$）中利用新能级连接跃迁的混合比 $\delta$、线偏振度 $P$、寿命及绝对电磁跃迁几率，鉴别单准粒子非对称核转动（signature partner）、横向/纵向摆动（wobbling）、倾斜进动与 $\gamma$ 软核转子涨落。

### Grounded Evidence & Primary Sources
- 作者博士学位中期报告 (2026):
  - $^{133}\text{Ce}$ (iThemba LABS PR295 实验): 发现 21 条新 $\gamma$ 跃迁，确立带头为 $13/2^-$ 的新低自旋带（含 12 条跃迁）；测得带间连接线具有小的负混合比（$|\delta| \lesssim 0.5$，$M1$ 主导）；发现 signature splitting 随自旋升高发生反转（signature inversion）；揭示三轴转子核芯沿 $N=75$ 同中子素链（$^{131}\text{Ba} \to {}^{133}\text{Ce} \to {}^{135}\text{Nd}$）由 $\gamma$ 软向 $\gamma$ 刚性演化；
  - $^{131}\text{Ce}$ (中国原子能科学研究院 CIAE HI-13 串列实验): 在束谱学确立高自旋能级纲图与多极性，对称性夹抱 $N=74$ 三轴核芯 $^{132}\text{Ce}$；
  - PDM 偏振-方向关联方法 (Chen, Guo et al., *NST* 审稿中): 解决无预设 $\sigma/I$ 下非对称误差传递问题；
- Alwaleedi 2013 博士论文 ([[alwaleedi-2013-band-structures-131ce]]): 建立 $^{131}\text{Ce}$ Bands 1–7 骨架（但存在 $\delta=0$ 条件假设）；
- NuclearMap JCNP PC-PK1 PES 先验 ([[nuclearmap-jcnp-pc-pk1]]): 提供 $^{132}\text{Ce}$ 与 $^{134}\text{Ce}$ 的微观三轴能面先验；
- 私有分析工作簿逐单元格反演研究笔记 ([[133ce-private-data-wobbling-vs-signature-reconstruction-20261101]]): 从 iThemba PR295 私有工作簿（`wobbling frequency.xlsx`、`intensity.xlsx`）复原了关键电磁跃迁比率与签名反转参数，确立 $B(E2)_{\text{out}}/B(E2)_{\text{in}} < 0.1$、$M1$ 占优（$77\%\text{--}97\%$）及 $\hbar\omega_w$ 在两 signature 分支间错动超 $240\text{ keV}$ 并降入负值（$-15.5\text{ keV}$）。
- 131Ce 与 133Ce 统一三轴集体模式与同中子素演化研究笔记 ([[ce131-ce133-unified-triaxial-collective-modes-20261101]]): 该页给出 CIAE HI-13 与 iThemba PR295 的条件性跨核素综合，提出 $N=73\to N=75$ 费米面和组态演化假设；邻核 PES、私有 workbook 派生量和质子回弯趋势均需 response、producer、绝对 EM 和 holdout 进一步验证，不能写成直接确立的三轴刚性化动力学。

### Competing Hypotheses
1. 低自旋 signature partner 与高自旋带交叉组态混合；
2. 奇中子三轴横向/纵向 wobbling 模式；
3. 倾斜轴进动（Tilted precession）与手征候选关联；
4. $\gamma$ 软核动力学涨落导致的伪摆动表象。

### Minimal New Inputs
- $^{133}\text{Ce}$ 实验矩阵的事件级时间门退卷积与逐角峰形拟合（区分 $g45/g90$ 瞬发门与符合矩阵）；
- Bands 1–7 关键带间连接跃迁的高精度偏振不对称度与直接 $\delta$ 拟合；
- $^{133}\text{Ce}$ 直接微观 PES 计算（当前仅有邻偶偶核 $^{132,134}\text{Ce}$ 映射）。

### Response Matrix & Joint Covariance Contract
必须在分析中区分瞬发符合窗（`g45/g90` prompt m4b arrays）与未切瞬发窗符合谱（`gg/hgg/vgg`）；严格记录几何立体角修正与符合效率矩阵。

### Falsifiers (证伪判据)
当前私有 workbook 的逐单元格反演给出：582、465 keV 连接线的派生 \(B(E2)_{\rm out}/B(E2)_{\rm in}\) 为 `0.063(25)` 和 `0.088(33)`，中心混合比为小 \(|\delta|\) 且 M1 占优；同时 workbook-derived \(\hbar\omega_w\) 在两个 signature 分支间明显不稳定。这些结果在当前 workbook、门条件和未闭合 response/covariance 合同下条件性不支持简单单声子 wobbling，但不能单独裁决 signature partner、TiP 或 configuration mixing。高自旋段若获得独立强 E2 与 holdout，才可能进一步更新模式排序。

### Stop Conditions (停止条件)
在未获得 $^{133}\text{Ce}$ 真实直接微观 PES、ROOT 原始事件树及符合时间响应展开前，不得虚构事件级计数或宣称已完成正式 L4 科学发现；保持受控 L3/partial-L4 准备度。

### Non-Independent Evidence Ledger (非独立证据边界)
iThemba LABS PR295 的 ROOT 矩阵（2751 个文件，4.52 GB）属于单一物理采集；作者中期报告提取的能谱与本 Wiki 分析共享该独占实验输入。

## Candidate 7: Full-library claim calibration and epistemology ledger

### Research Question & Core Objective
对低能核结构领域近数十篇代表性文献中存在的“将唯象模型拟合、平均场能面极小值或作者假说升级为实验确立事实”的认知偏差进行系统性自审与语言校准，建立严谨的跨质量区知识治理与可证伪方法学框架。

### Grounded Evidence & Primary Sources
- 全库主张校准审计账本 ([[full-library-claim-calibration-audit-20261031]]);
- 博士认知自审与核结构综合研究笔记 ([[doctoral-cognitive-calibration-and-nuclear-structure-synthesis-20261101]]): 系统梳理并纠正六大认知偏差（能量摆动假象、双根退化、静态手征假设、E1/E3 抵消混淆、模型输出客体化、单次采集伪独立），确立低能核谱学“五道门”证据裁判标准；
- 近期重点核查源：Hendrie 1968、Rohozinski 1988、Zagrebaev 2001、Piekarewicz 2004、Karmakar 2025、Bucher 2016/2017、Gaffney 2013、Rosiak 2018、Henderson 2025 等。

### Competing Hypotheses
1. 实验观测与理论模型自洽等价论（即认为高质量拟合等同于证实了物理机制）
2. 证据分层与欠定性认识论（即同一实验能谱可由不同微观机制以相近精度再现）

### Minimal New Inputs
- 全库历史 source 页的 claim table 动词对照（将 `proved/confirmed` 改为 `consistent with/supports/within model space`）；
- 逐篇文献的 primary locator、evidence level 与 independent experiment count 补全。

### Response Matrix & Joint Covariance Contract
建立跨源 claim 的层级依赖关系，区分原始实验数据层、数据规约派生层、唯象模型拟合层与作者推测层。

### Falsifiers (证伪判据)
若发现某条所谓“已确立模式”在去除模型辅助假设（如固定 $\sigma/I$、预设有效电荷 $e_{\text{eff}}$ 或冻结内禀四极矩）后，其实验观测值完全能够被另一正交物理机制以同等显著性解释，则该模式的“排他性确立”结论被直接推翻。

### Stop Conditions (停止条件)
严禁在知识库正文或论文草稿中使用“首个确证”、“彻底证明”、“完全排除所有替代解释”等绝对化词汇，除非获得独立 holdout 观测的排他性检验。

### Non-Independent Evidence Ledger (非独立证据边界)
同一大型实验装置（Gammasphere、Euroball、JUROGAM、INGA）在同一周期内获取的数据集产生的多篇论文，必须显式登记为同一采集谱系下的衍生分析。
## Paper Evidence Gate

五个候选都需要：

1. 每条主张对应一个具体 source page、raw identity 和 page/figure/table/level locator；
2. 同一数据谱系、复测、综述和再分析明确标记 `multiple-dependent`；
3. 给出至少一个反证、一个必要 companion observable 和一个 falsifier；
4. 对 raw/response/Cov 缺口写 readiness boundary，停止生成代理 L4 结论；
5. 保留 `needs_review`、`unreviewed` 和 `provisional`，不以 Codex self-audit 代替人工审核。

## Risks and Blockers

- P1/P2 的关键 raw response、联合协方差、原始角分布或宇称判据未全部取得。
- 现有很多数值来自同一实验谱系的再分析，若不标 lineage 会虚增独立性。
- 任何模型参数、有效电荷、g 因子、`β`/`γ`/`β3` 或拟合端点都不能替代实验观测。
- 全库 lint 仍有继承基线 errors；它阻止自动发布，但不改变科学候选的 provisional 状态。

## Writing and Analysis Order

先写 P1 的方法合同和 source-lineage 图，再根据真实输入决定是否进入联合重析；P2
作为对象身份和识别性论文候选保留；P3 需要寿命/绝对 EM producer 后再写主结论；
P4 先完成统一数据表和单位/跃迁方向审计。每篇稿件都应先有 claim-to-source
matrix 和反证表，再开始正文写作；不要以“读过的论文数”替代可复核结果。

## Next Actions

1. 先完成 P1 的公开 source-lineage/observable ledger 和最小共同响应合同。
2. 并行维持 P2 的1983 AD、794.8-keV宇称和882偏振检索，但不重复受阻端点。
3. 对 P3/P4/P5 只补缺失 primary、数据身份和方法学对照，不用 synthetic 计算填充寿命、协方差、coverage 或多态跃迁。
4. 候选获得真实输入后，再建立 claim-to-source matrix、falsifier、图表目录和投稿期刊适配表。

## Sources

- [[matta-2015-transverse-wobbling-135pr]]、[[lv-2022-evidence-against-wobbling-135pr]]、
  [[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]]：P1的分支和谱系证据。
- [[chakraborty-2023-131xe-wobbling-origin]]、[[banik-2020-131xe-multiple-band-structures]]：
  P2的对象身份与版本边界。
- [[gaffney-2013-pear-shaped-rn-ra]]、[[bucher-2016-144ba-direct-octupole]]、
  [[bucher-2017-146ba-direct-octupole]]：P4的直接E3和静态/动态解释边界。

## Human Review

本页是 Codex self-audit 的研究队列，`review_status: unreviewed`。候选题目、优先级
和停止条件都需要在实际投稿或导师讨论前重新核验，不代表用户已选择投稿期刊或批准
任何未经取得的数据分析。

## Promotion or Rejection History

2026-10-30：由全库温故知新与Day28 L3研究产生。五个候选均保留为active/provisional
队列；尚未取得新的事件级数据、响应或联合协方差，未生成期刊稿件或实验新结论。
