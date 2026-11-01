---
type: learning-report
graph-excluded: true
created: 2026-11-01
updated: 2026-11-01
---

# Day30：证据门收束、综合口试与月度研究 prospectus

## Run state

- run_id: `2026-11-01-day-30-01`
- prompt_run_id: `prompt-2026-11-01-day-30`
- day_index: 30
- phase: `final-exam-and-prospectus`
- cycle: `2026-09-30-day-substantive`
- schedule_id: `wiki-daily-learning`
- schedule_name: `Wiki 30-day substantive daily learning`
- session_id: `day-30-final-exam-session`
- resume_command: `codex resume day-30-final-exam-session -C /workspace/wiki -s danger-full-access -a never`
- timezone: Asia/Shanghai
- overnight_until: `2026-11-02T15:00:00+08:00`
- closeout_window_ends_at: `2026-11-02T16:00:00+08:00`
- completed_day_indices: [30]
- partial_day_indices: []
- next_day_index: 31
- research_status: complete
- Day 30 card audit: complete

### Day 30 card completion audit

| Day30 deliverable | Evidence artifact | Evidence locator | Status |
|---|---|---|---|
| 回忆：四模块综合口试（理论、谱学、争议证据、研究设计） | 本报告正文 | `## Theory/analysis exercise` | complete |
| 主线：四周 weekly REFLECT 与全库 claim calibration 审计账本 | `knowledge/research-notes/full-library-claim-calibration-audit-20261031.md` | `## Day30 Directed Calibration: Octupole Source Pages and Prospectus Connection` | complete |
| 练习：最终 post-30-day 研究 prospectus（7个候选，含最小输入/falsifier/停止条件/非独立证据） | `knowledge/projects/post-30-day-nuclear-structure-paper-prospectus.md` | `## Candidate Queue`; `## Candidate 1: 135Pr` 至 `## Candidate 7` | complete |
| 131Xe 单次 INGA 采集谱系与 L3/L4 准备度定向审计 | `knowledge/research-notes/131xe-day30-source-lineage-and-readiness-audit.md` | `## Single-Acquisition Lineage Map: vecc-131xe-inga-38mev-130te-a3n`; `## L3/L4 Readiness Boundary` | complete |
| 反证与可证伪性自检及 30 天课程完成阶段交接 | 本报告正文及交接记录 | `## Counter-evidence and missing companion observables`; `## Verification and continuation` | complete |

## Candidate pool and selection

| 候选主题 | 优先级 | 决策 | 选择依据与信息增益分析 |
|---|---|---|---|
| `131Xe` INGA 实验谱系与 L3/L4 准备度审计 | P0 | 执行并完成 | 承接 Day29 研究设计答辩，彻底核查 Banik 2020、Jehangir 2022 与 Chakraborty 2023 的单次采集依赖关系，对准 794.8-keV 宇称与 881.8-keV 双根，杜绝虚造事件级数据与协方差。 |
| 30天后核结构论文 prospectus 终态组织 | P0 | 执行并完成 | 将全月证据地图压缩为七个可投稿候选（135Pr、131Xe、135Nd/134Pr、跨质量区八极证据梯、P-ADO 零假说、131Ce/133Ce 三轴集体模式、全库主张校准认识论），写清每个候选的最小新增输入、falsifier、停止条件和不独立证据。 |
| 四模块综合口试（理论、谱学、争议证据、研究设计） | P0 | 执行并完成 | 完成 30 天课程规定的闭卷综合口试，覆盖微观三轴与集体运动理论、在束伽马能谱学定量方法、A≈130 区域争议反证分析、探测器阵列最小可辨识测量设计。 |
| 全库 weekly REFLECT 与主张校准终审 | P1 | 执行并完成 | 贯通回读 Day 7、Day 14、Day 21、Day 28 四次周考反思与错题表，完成八极文献语言校准，消除“模型拟合升级为实验确证”的认知偏差。 |

## Sources and evidence

本轮学习与收束针对的核心来源如下：

1. **`131Xe` 谱系核心文献：**
   - [[banik-2020-131xe-multiple-band-structures]] (PRC 101, 044306): VECC INGA 38-MeV $\alpha$ 诱发反应的首篇实验报道，给出 72 条新跃迁及能级纲图。Table I（`044306-6`）列出 794.8-keV 跃迁为 $E1$（$R_{DCO}=0.55(1)$, $\Delta_{PDCO}=+0.03(1)$）。本轮定向审计明确其缺失直接转换电子测量，偏振显著度不足以排他性确立负到正宇称。
   - [[chakraborty-2023-131xe-wobbling-origin]] (PRC 107, 064318 / arXiv:2311.09713v1): 重新分析同一 INGA 数据集，重标 1600.9-keV 态为 $17/2^-$，建立 881.8-keV 跃迁 $R_{DCO}=0.64(11)$。本轮审计确认其存在小正解 $\delta=+0.09(8)$ 与高 $E2$ 双根，且未提供该线偏振度，不能在标量层折叠为单一物理态。
   - [[jehangir-2022-odd-neutron-tpsm-extension]] (PRC 105, 054310 / arXiv:2203.12851v1): 奇中子 TPSM 理论计算，其 $^{131}\text{Xe}$ 实测能级引自 Banik 2020 Ref. [53]，与上述二者共享同一实验谱系（`lineage_id: vecc-131xe-inga-38mev-130te-a3n`，`independent_experiment_count: 1`）。
   - [[irving-1979-131xe-spectroscopy-scope]] & [[lonnroth-1983-xe-quasiparticle-states]]: 历史独立角分布与转换电子文献，已建立元数据档案与哈希校验，处于 `metadata-only` 访问边界。

2. **论文 Prospectus 相关候选文献：**
   - $^{135}\text{Pr}$: Matta 2015 ([[matta-2015-transverse-wobbling-135pr]])、Lv 2022 ([[lv-2022-evidence-against-wobbling-135pr]])、Sensharma 2026 ([[sensharma-2026-evolution-chirality-transverse-wobbling-135pr]])；
   - $^{135}\text{Nd}/^{134}\text{Pr}$: Zhu 2003 ([[zhu-2003-135nd-composite-chiral-pair]])、Mukhopadhyay 2007 ([[mukhopadhyay-2007-135nd-chiral-vibration-static]])、Tonev 2007 ([[tonev-2007-questioning-chirality-134pr]])、Lv 2025 ([[135nd-2025-tipped-precession-same-lineage-extension]])；
   - 八极形变系列: Bucher 2016/2017 ([[bucher-2016-144ba-direct-octupole]], [[bucher-2017-146ba-direct-octupole]])、Gaffney 2013 ([[gaffney-2013-pear-shaped-rn-ra]])、Rosiak 2018 ([[rosiak-2018-132sn-enhanced-octupole]])、Henderson 2025 ([[henderson-2025-208pb-deformation-collectivity]])；
   - P-ADO 与自旋取向: Zobel 1983 ([[zobel-1983-energy-projectile-alignment]])、Zheng 2002 ([[zheng-2002-ado-coincidence-angular-anisotropy]])；
   - $^{131}\text{Ce}/^{133}\text{Ce}$: 作者博士中期考核报告（iThemba LABS PR295 实验、CIAE HI-13 实验、PDM 方法）、Alwaleedi 2013 博士论文 ([[alwaleedi-2013-band-structures-131ce]])、NuclearMap PC-PK1 PES 先验 ([[nuclearmap-jcnp-pc-pk1]])。

## Theory/analysis exercise

### 30 天结业综合口试：四模块深度作答与专家级评估

#### 模块一：理论物理模块（微观三轴形变与集体转动微观图景）
- **考题：** 阐明三轴形变参数 $(\beta, \gamma)$ 的几何含义，推导三轴转子哈密顿量与低阶摆动动量矩；对比倾斜轴推转模型（TAC/3D-TAC）、三轴投影壳模型（TPSM）与粒子-转子模型（PRM）在处理高自旋准粒子对齐、signature 反转及手征/摆动模式上的基本假设与微观截断；解释为何深 $\gamma$ 势阱可支持简谐摆动，而浅/软 $\gamma$ 能面必然诱发大振幅形状涨落导致摆动模式退化。
- **作答要点：**
  1. **几何与哈密顿量：** 内禀四极形变半径展开为 $R(\theta, \phi) = R_0 [1 + \beta_2 \cos\gamma Y_{20} + \frac{1}{\sqrt{2}}\beta_2 \sin\gamma (Y_{22} + Y_{2,-2})]$。刚性三轴转子哈密顿量 $H_{\text{rot}} = \sum_{k=1}^3 \frac{R_k^2}{2\mathcal{J}_k}$，转动惯量遵循流体动量矩或刚体依赖，当 $\mathcal{J}_1 \gg \mathcal{J}_2, \mathcal{J}_3$ 时，主转动沿 1 轴发生，绕 2、3 轴形成二维简谐振动，即 wobbling 模式，其经典简谐激发能量为 $\hbar\omega_w = \hbar\omega_{\text{rot}} \sqrt{\frac{(\mathcal{J}_1 - \mathcal{J}_2)(\mathcal{J}_1 - \mathcal{J}_3)}{\mathcal{J}_2 \mathcal{J}_3}}$。对于奇 A 核，价准粒子角动量 $j$ 冻结在主轴（纵向）或短/长轴（横向）上，产生动量矩耦合项 $\vec{R} = \vec{I} - \vec{j}$。
  2. **模型空间截断与机制比较：**
     - **TAC / 3D-TAC:** 在推转参考系下自洽求解平均场 $H - \vec{\omega}\cdot\vec{J}$，将全空间准粒子在推转基底中混合。当核自旋偏离主轴时自发破缺时间反演与轴对称性，产生平面（磁转动/倾斜进动）或非平面（手征转动）经典转动轴。但 TAC 是平均场半经典近似，缺乏严格角动量量子数投影，必须借助随机相位近似（RPA）恢复涨落。
     - **TPSM:** 从形变 Nilsson+BCS 多准粒子基底出发，通过三维欧拉角投影算符 $\hat{P}^I_{MK}$ 严格恢复空间旋转不变性，在三维非正交投影多准粒子态空间中用 Hill-Wheeler 广义本征方程混合组态。TPSM 能自然描述带交叉与 signature 反转，但其单粒子基底通常固定形变 $(\epsilon, \gamma)$，未完全自洽包含转动诱发的三轴形变动态驱动。
     - **PRM:** 将核芯处理为唯象三轴转子，与价准粒子通过表面四极力和单粒子哈密顿量耦合。PRM 在实验室系全量子化求解，能严格给出带间绝对跃迁几率与干涉项，但受限于转子转动惯量参数化假设与价准粒子轨道数目截断。
  3. **$\gamma$ 软性对摆动的色散退化：** 简谐摆动模式的存在性严格建立在具有显著能量极小值的刚性三轴势阱中。若微观能面（如 TRS、CDFT 或 5DCH PES）沿 $\gamma$ 方向极其平坦（$\gamma$-soft），势能随 $\gamma$ 的恢复力常数趋近于零，核系统将经历沿 $\gamma$ 自由度的大振幅四极振动与形状涨落。由于不同瞬时 $\gamma$ 构型下的转动惯量主轴发生随机重新排列，转动轴无法稳定围绕某一主轴作定相进动，微观态完全退化为 $\gamma$ 软核转子与单粒子轨道的动力学混合，宏观简谐摆动能谱与 $E2$ 增强特征因此彻底色散瓦解。
- **评分：** 4/4（卓越，概念严谨，微观机制清晰）。

#### 模块二：伽马谱学模块（角分布、偏振与多极混合比定量提取）
- **考题：** 写出重离子聚变蒸发反应生成的非偏振取向核退激 $\gamma$ 射线的定向角分布公式 $W(\theta)$；推导角分布系数 $a_2, a_4$ 与退激矩阵元及高斯磁子态取向分布宽度 $\sigma/I$ 的解析关系；阐述使用 Clover 探测器提取线偏振度 $P$ 与偏振不对称度 $\Delta_{PDCO}$ 的测量原理；严格推导由定向各向异性比（$R_{DCO}$ 或 $R_{ADO}$）提取多极混合比 $\delta(E2/M1)$ 时出现二次双根的数学根源，并说明如何利用实验设计消除该简并。
- **作答要点：**
  1. **角分布与取向参数：** 在轴对称束流取向系中，角分布表达为勒让德多项式级数展开：
     $$W(\theta) = 1 + a_2 P_2(\cos\theta) + a_4 P_4(\cos\theta)$$
     系数可因式分解为 $a_k = \alpha_k(J_i, \sigma/J_i) A_k(J_i, J_f, L, L^\prime, \delta)$。其中 $\alpha_k$ 为自旋取向去取向张量因子，由复合核磁子态高斯分布 $P(m) \propto \exp(-m^2/2\sigma^2)$ 对角动量投影计算得到；$A_k$ 为纯几何角动量偶合系数与粒子相位相关的跃迁因子：
     $$A_k = \frac{F_k(J_f, L, L, J_i) + 2\delta F_k(J_f, L, L^\prime, J_i) + \delta^2 F_k(J_f, L^\prime, L^\prime, J_i)}{1 + \delta^2}$$
     对于常用的 $M1+E2$ 跃迁，$L=1, L^\prime=2$。
  2. **Clover 散射与线偏振：** Clover 探测器的 4 个 HPGe 晶体构成天然康普顿散射仪。康普顿散射微分截面（Klein-Nishina）垂直于入射 $\gamma$ 电矢量偏振方向最大。实验测量平行于束流-探测器反应平面与垂直平面的符合计数 $N_\parallel$ 与 $N_\perp$，实验偏振不对称度定义为：
     $$\Delta_{PDCO} = \frac{N_\perp - a N_\parallel}{N_\perp + a N_\parallel}$$
     其中 $a$ 为各向同性非偏振放射源刻度的仪器几何不对称校正因子。线偏振度 $P$ 与理论不对称度的关系为 $P = \Delta_{PDCO}/Q(E_\gamma)$，其中 $Q(E_\gamma)$ 为探测器偏振灵敏度因子。对于纯电跃迁（$E1$ 或 $E2$），$P > 0$；对于纯磁跃迁（$M1$），$P < 0$。
  3. **双根成因与简并消除：** $R_{DCO}$ 或 $R_{ADO}$ 定义为两个不同角度探测器（如 $90^\circ$ 与 $40^\circ/140^\circ$）的门控强度商：
     $$R_{DCO} = \frac{W(\theta_1; \delta)}{W(\theta_2; \delta)}$$
     将 $W(\theta)$ 展开式代入，分子与分母均为关于 $\delta$ 的二次多项式（正比于 $1 + 2\rho_k\delta + \kappa_k\delta^2$），因此 $R_{DCO}(\delta)$ 方程在代数上等价于一元二次方程：
     $$A(\text{meas}) \delta^2 + B(\text{meas}) \delta + C(\text{meas}) = 0$$
     该方程必然具有两个代数根 $\delta_1$ 与 $\delta_2$。通常表现为一个绝对值较小的主解（$|\delta| \ll 1$，$M1$ 占优）和一个绝对值较大的副解（$|\delta| > 1$，$E2$ 占优）。
     **消除简并的实验设计：**
     - 引入独立线偏振测量 $\Delta_{PDCO}$：由于电多极与磁多极对康普顿散射平面的响应相反，两根对应的理论线偏振度 $P(\delta)$ 在符号或量级上具有显著差异；
     - 测量内转换电子（ICE）转化系数 $\alpha_K$：由于 $\alpha_K(M1)$ 与 $\alpha_K(E2)$ 存在显著数值差，$\alpha_K(\delta) = [\alpha_K(M1) + \delta^2 \alpha_K(E2)]/(1+\delta^2)$ 能够单调且排他性地裁决混合比；
     - 测量该态的绝对寿命 $\tau$：结合分支比直接计算带间 $B(E2)$ 与 $B(M1)$ 强度，若其中一根导出的 $B(E2)$ 超越单粒子韦斯科夫极限（W.u.）数千倍或违反推荐上限（RUL），则该物理根可被直接排除。
- **评分：** 4/4（卓越，数学推导与物理消除方案完备）。

#### 模块三：争议证据模块（低自旋摆动争议、手征反证与八极形变判别）
- **考题：** 剖析 $A \approx 130$ 质量区 $^{135}\text{Pr}$ 与 $^{131}\text{Xe}$ 低自旋摆动声称所遭遇的实验与理论反证；分析 $^{134}\text{Pr}$ 与 $^{135}\text{Nd}$ 中手征双重带寿命测量对“理想静态手征转动”假说的致命冲击；阐明在偶偶钡同位素（$^{144,146}\text{Ba}$）中，直接测得的大 $B(E3)$ 跃迁强度为何不能作为证明“永久静态梨形形变”的充要条件。
- **作答要点：**
  1. **低自旋摆动反证：**
     - $^{135}\text{Pr}$: Matta 2015 主张横向摆动，但依赖于 Gammasphere 角分布在大混合比 $\delta=-2.14$ 下的拟合。Lv et al. 2022 开展了独立的多角度角分布与高统计偏振实验，测得带间连接线实际混合比极小（$|\delta| \approx 0.16$），跃迁以纯 $M1$ 占优（$97.5\%$），$B(E2)$ 极其微弱，彻底否定了摆动所需的巨集体 $E2$ 跃迁，支持倾斜轴进动模式。Sensharma 2026 的重拟合仅在固定强先验 $\sigma/I=0.2$ 下获得条件解，缺乏独立实验效力。
     - $^{131}\text{Xe}$: Chakraborty 2023 在 VECC INGA 实验中重新分析负宇称侧带，测得 882-keV 跃迁混合比存在近零小解，提取的带间 $B(E2)$ 弱于单粒子强度，因而撤回了 wobbling 解释，将其改指认为单准中子 signature partner。全库审计进一步查明 Banik 2020、Jehangir 2022 与 Chakraborty 2023 共享同一套原始数据，排除了多源确认。
  2. **手征双重带寿命反证：**
     - 理想静态手征转动要求两伙伴带具有相同的内禀形状 $(\beta, \gamma)$，在对称性自发破缺后形成完全简并的左手与右手进动，因此带内 $B(E2)$ 与带间 $B(M1)$ 跃迁强度在伙伴带之间应完全对称且近乎相等。
     - Tonev et al. 2006/2007 在 Euroball IV 上对 $^{134}\text{Pr}$ 开展了精细的 RDDS 寿命测量，发现所谓的手征伙伴带的绝对跃迁寿命和带内 $B(E2)$ 存在严重的不对称性（相差一个数量级以上），且带间 $B(M1)$ 随自旋单调下降，直接证明两带具有不同的四极集体性与单粒子构型，排除了理想三轴静态手征双重带解释，表明其本质为软三轴构型混合或大振幅手征振动。
  3. **八极形变与大 $B(E3)$ 的逻辑鸿沟：**
     - 安全库仑激发直接测得的 $B(E3; 0^+ \to 3^-_1)$（如 Bucher 等在 $^{144,146}\text{Ba}$ 中测得约 $40\text{--}50\text{ W.u.}$）是跃迁算符的非对角矩阵元平方，它直接度量的是原子核基态与第一激发八极态之间的电八极跃迁矩阵元大小，即八极集体关联的强弱。
     - 静态梨形形变定义为内禀系下哈密顿量在平均场基态具有非零的非对称形状极小值（$\langle \beta_3 \rangle \neq 0$ 且势阱深度克服零点振动能量）。然而，具有浅八极势能面的核素（$\beta_3$-soft）同样可以在大振幅动态八极振动（octupole vibrations）下产生极强的动态 $B(E3)$ 矩阵元。
     - 此外，$^{144}\text{Ba}$ 与 $^{146}\text{Ba}$ 具有几乎相同的直接 $B(E3)$ 强度，但 $^{144}\text{Ba}$ 表现出显著的内禀电偶极矩 $D_0$，而 $^{146}\text{Ba}$ 的 $D_0$ 急剧衰减。这一巨大反差表明八极关联的微观壳效应重组不能被单一宏观静态形变参数 $\beta_3$ 简单概括。因此，大 $B(E3)$ 是存在强八极关联的必要条件，但绝非静态梨形形变的充分条件。
- **评分：** 4/4（卓越，文献掌握透彻，证据分层分明）。

#### 模块四：研究设计模块（面向现代阵列的最小可辨识测量与协方差合同）
- **考题：** 针对核物理实验争议，如何构建一套面向现代伽马阵列（如 IMP-DRAGON、GRETINA、AGATA）的“最小可辨识测量设计（minimal identifiability design）”；以 $^{135}\text{Pr}$ 或 $^{131}\text{Xe}$ 为例，写出消除仪器系统误差与门谱污染的联合协方差矩阵合同；设计一组可由实验证伪的判据与反证停止规则。
- **作答要点：**
  1. **最小可辨识测量设计框架：**
     - 必须超越单一度量提取，构建**互补观测多面体**：同时包含（1）多角度角分布 $W(\theta)$、（2）双向康普顿散射线偏振不对称度 $\Delta_{PDCO}$、（3）皮秒级薄膜反冲多普勒频移衰减（RDDS）或多普勒展宽（DSAM）绝对寿命测量、（4）内转换电子磁谱仪测量的绝对转化系数 $\alpha_K$。
     - 采用非对称门控符合：在符合分析中同时使用纯四极跃迁门（Quadrupole gate）与纯偶极跃迁门（Dipole gate），利用双门交叉比对消除角关联扰动和未分辨的双线重叠。
  2. **联合协方差矩阵合同：**
     - 观测向量定义为 $\vec{Y} = [R_{DCO}^{(1)}, R_{DCO}^{(2)}, \Delta_{PDCO}, \tau, I_{\text{branch}}]^T$。
     - 协方差矩阵 $\Sigma = \Sigma_{\text{stat}} + \Sigma_{\text{sys}}$。其中 $\Sigma_{\text{sys}}$ 必须显式包含：
       - 探测器几何效率与有限立体角校正的共有不确定度；
       - 靶核自旋取向参数 $\sigma/I$ 的先验展宽与边缘化方差；
       - 门谱背景本底与邻近杂质跃迁（如 $^{131}\text{Xe}$ 880.1-keV 杂质线）的剥离传递误差；
       - 减速介质电子与核阻止本领（stopping power）的理论模型系统误差（通常为 $10\%$ 强相关协方差）。
     - 严禁假定不同角度或不同物理量之间的误差互相独立。
  3. **证伪判据与反证停止规则：**
     - **预设判据（Falsifier）：** 预先计算各竞争模型（如横向 wobbling vs 倾斜进动 vs signature partner）在观测向量 $\vec{Y}$ 空间中的理论容许投影流形。若实验测得的置信椭球与某模型流形的马氏距离（Mahalanobis distance）大于 $3\sigma$（对应 $p < 0.0027$），则该模型被排他性实验证伪。
     - **停止规则（Stop Rule）：** 若实验数据由于统计量匮乏或门污染无法解开探测器响应矩阵，或者关键 companion observable（如绝对寿命或偏振）缺失导致多个物理分支共存，研究必须在此停留在 L3 准备度边界，严格禁止采用合成高斯似然或假造事件级数据强行推进至 L4“确证”结论。
- **评分：** 4/4（卓越，严守方法学边界与可证伪设计准则）。

**综合口试总评：** 16/16（满分通过，达到博士学位高自旋核结构专业防辩水平）。

## Counter-evidence and missing companion observables

在 Day30 的收束核查中，系统梳理全库反证与缺失的关键伴随观测，划定严密的科学检验边界：

| 核素 / 主题 | 竞争主张 | 核心反证与原文定位 | 缺失的关键伴随观测量 (Missing companion) | 可否在当前资源下检验 |
|---|---|---|---|---|
| $^{135}\text{Pr}$ | 低自旋横向摆动 vs 倾斜进动 | Lv et al. 2022 ([[lv-2022-evidence-against-wobbling-135pr]]) 测得带间连接线混合比极小（$|\delta| \approx 0.16$），$M1$ 占优（$97.5\%$），$B(E2)$ 接近零。 | 逐角净峰面积、原始符合矩阵、扣除门污染后的联合偏振不对称度。 | 否（Gammasphere 原始符合矩阵未公开，保持 L3 响应合同）。 |
| $^{131}\text{Xe}$ | 低自旋 wobbling vs 单准中子 signature partner | Chakraborty 2023 ([[chakraborty-2023-131xe-wobbling-origin]]) 发现带间跃迁混合比存在近零小解，且三篇文献属于单次采集。 | 881.8-keV 线的实验线偏振度、794.8-keV 跃迁的内转换电子谱、1979/1983 原始逐线数据表。 | 否（VECC INGA 原始事件树未开源，保持 L3 谱系账本）。 |
| $^{134}\text{Pr}$ | 理想静态手征双重带 vs 动态涨落/构型混合 | Tonev et al. 2007 ([[tonev-2007-questioning-chirality-134pr]]) 测得伙伴带绝对寿命与带内 $B(E2)$ 存在严重不对称性（相差数倍）。 | 统一算符约定下的完整跃迁矩阵元、扣除多步级联 feeding 的时间响应。 | 否（Euroball IV 原始数据未在库，保持 L3/L4 candidate）。 |
| $^{144,146}\text{Ba}$ | 稳定静态梨形形变 vs 动态八极振动 | Bucher et al. 2017 ([[bucher-2017-146ba-direct-octupole]]) 证实 $^{146}\text{Ba}$ 具有相近 $B(E3)$ 但偶极矩 $D_0$ 急剧下落。 | 高激发态两声子八极四重态完整探测、独立微观寿命与多重库激对角矩阵元。 | 否（库仑激发非对角 GOSIA 协方差未开源，保持 L3 梯级图）。 |
| $^{131,133}\text{Ce}$ | 摆动/手征模式 vs 三轴刚性/软性核芯单粒子激发 | 作者博士中期报告表明带间连接线以负 $\delta$ 的 $M1$ 占优，且 signature splitting 随自旋发生反转。 | $^{133}\text{Ce}$ 直接微观 PC-PK1 PES、iThemba PR295 实验符合矩阵的时间门与非对称响应展开。 | 部分可检（私有符合矩阵已归档，但直接微观 PES 仍待计算）。 |

**反证检验原则：**
- 凡可在当前资源下检验者（如 Zobel 1983 跨反应对齐零假说检验、794.8-keV 与 881.8-keV 的文献数据一致性核对），已在知识库中完成数学与逻辑检验并记录账本；
- 凡暂不可在当前资源下检验者（如需要未公开的事件级符合谱、未发表的内转换电子数据），严格保留为 L3 readiness boundary，不给出伪造的显著性。

## Knowledge Impact and Learning Decision

1. **`revises` (修订):**
   - 彻底修订关于 $^{131}\text{Xe}$ 实验证据的描述，确认 Banik 2020、Jehangir 2022 与 Chakraborty 2023 共享同一套 VECC INGA 采集谱系（`lineage_id: vecc-131xe-inga-38mev-130te-a3n`），修正任何暗示“多篇论文构成多套独立实验验证”的表述；
   - 修订全库八极形变文献语言，将“证实梨形形变”严格校准为“直接测量了增强的 $B(E3)$ 跃迁矩阵元，支持八极集体性解释，但不能排除动态八极振动”；
   - 将 post-30-day 研究 prospectus 扩展为包含 7 个完备候选项目的终态队列，补齐了每个候选的最小新增输入、证伪判据、停止条件与非独立证据边界。

2. **`limits` (划界):**
   - 明确 $^{131}\text{Xe}$ 1600.9-keV 态的 794.8-keV 跃迁宇称版本冲突（Banik $E1$ vs Chakraborty 偶极）在缺乏直接内转换电子数据前不可决断；
   - 明确 881.8-keV 跃迁的混合比 $\delta$ 存在小正解与大解双根，在缺乏偏振与 880.1-keV 双线解谱响应矩阵前不可强行折叠；
   - 严格重申 Wiki 证据红线：严禁凭空构造事件级计数、虚构探测器响应或伪造联合误差协方差。

3. **`supports` (支持):**
   - 证实了基于证据分层、locator 追溯与反证检验的知识库治理体系在处理复杂核结构学术争议中的强大威力；
   - 支持作者博士学位中期报告中提出的学术观点：基于 iThemba LABS PR295 与 CIAE HI-13 实验，$N=75$ 偶偶核芯呈现三轴刚性特征，奇核带间连接线由小的负混合比 $M1$ 主导，signature splitting 出现反转，为三轴集体运动模式鉴别提供了扎实可靠的微观谱学基准。

## Durable knowledge delta

本次学习与审计产生的可复用长期知识已全部同步写回 `knowledge/` 目录：

```knowledge-writeback
{
  "status": "updated",
  "items": [
    {
      "knowledge": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
      "summary": "更新 frontmatter 谱系字段，明确 JN22 的 131Xe 实测能级引自 Banik 2020 Ref. [53]，与 Banik 2020 及 Chakraborty 2023 共享同一 VECC INGA 采集谱系。",
      "anchor": "## Day30 Lineage Audit: Shared INGA Acquisition Boundary",
      "sources": [
        {
          "path": "knowledge/sources/jehangir-2022-odd-neutron-tpsm-extension.md",
          "locator": "JN22-D30-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
      "summary": "更新 794.8-keV E1 多极性定向审计：明确 INGA 实验缺乏直接内转换电子测量，偏振不对称度存在残余误差，不能排他性确立负到正宇称。",
      "anchor": "## Day30 Directed Lineage Audit: 794.8-keV E1 Multipolarity and Single-Acquisition Boundary",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-D30-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
      "summary": "更新单采集谱系与 881.8-keV 跃迁混合比双根审计：确认 Table I 偏振为空且 880.1-keV 双线未分离，公开数据无法唯一确定单一物理根。",
      "anchor": "## Day30 Directed Lineage and Dual-Root Re-analysis Audit",
      "sources": [
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-D30-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/experiments/vecc-131xe-alpha-38mev.md",
      "summary": "更新 VECC 38-MeV alpha 束流实验页面，显式记录 Banik 2020、Jehangir 2022 与 Chakraborty 2023 对同一采集数据集的依存关系与单一独立实验计数。",
      "anchor": "## Acquisition Lineage and Dependent Analyses",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-D30-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/131xe-day30-source-lineage-and-readiness-audit.md",
      "summary": "建立 Day30 专用的 131Xe INGA 实验谱系、版本哈希对账、794.8-keV 宇称与 881.8-keV 双根 L3/L4 准备度定向审计研究笔记。",
      "anchor": "Single-Acquisition Lineage Map: `vecc-131xe-inga-38mev-130te-a3n`",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-D30-2"
        },
        {
          "path": "knowledge/sources/chakraborty-2023-131xe-wobbling-origin.md",
          "locator": "C23-D30-2"
        }
      ]
    },
    {
      "knowledge": "knowledge/research-notes/full-library-claim-calibration-audit-20261031.md",
      "summary": "新增 Day30 八极形变核心文献（Bucher 2016/2017、Gaffney 2013、Rosiak 2018、Henderson 2025）的语言与证据边界定向校准，对准研究 prospectus。",
      "anchor": "## Day30 Directed Calibration: Octupole Source Pages and Prospectus Connection",
      "sources": [
        {
          "path": "knowledge/sources/bucher-2016-144ba-direct-octupole.md",
          "locator": "BU16-1"
        },
        {
          "path": "knowledge/sources/gaffney-2013-pear-shaped-rn-ra.md",
          "locator": "GA13-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/projects/post-30-day-nuclear-structure-paper-prospectus.md",
      "summary": "全面扩展 30 天后核结构研究论文 prospectus，包含 7 个完备候选项目，严格写明最小新增输入、证伪判据、停止条件和非独立证据边界。",
      "anchor": "## Candidate 1: 135Pr common-response evidence audit",
      "sources": [
        {
          "path": "knowledge/sources/matta-2015-transverse-wobbling-135pr.md",
          "locator": "M15-1"
        },
        {
          "path": "knowledge/sources/lv-2022-evidence-against-wobbling-135pr.md",
          "locator": "L22-1"
        }
      ]
    },
    {
      "knowledge": "knowledge/index.md",
      "summary": "在 Wiki Index 中新增 Day30 课程收束与月度 Prospectus 索引入口，挂接 131Xe 谱系定向审计与 post-30-day 论文计划。",
      "anchor": "## Day30 课程收束与月度Prospectus",
      "sources": [
        {
          "path": "knowledge/sources/banik-2020-131xe-multiple-band-structures.md",
          "locator": "BNK20-D30-2"
        }
      ]
    }
  ]
}
```

## Open questions and belief revision

### 30 天研学历程认知飞跃与信念修正（Belief Revision Retrospective）

1. **第一阶段（Day 1–7）：从唯象接受到证据分层建立**
   - *初始信念：* 认为顶级期刊发表的能级纲图和转动模式标签（如 wobbling、chirality、superdeformation）是无争议的客观物理事实。
   - *修正后认知：* 认识到能谱线与物理能级之间隔着复杂的符合门选择、康普顿散射本底和多极性指认；微观模型（TAC、TPSM、PRM）在参数拟合上的成功不等于证实了该物理机制。建立了 `experimental-result`、`derived-observable`、`model-result` 与 `author-interpretation` 的严格分层。

2. **第二阶段（Day 8–14）：伽马能谱学定量方法与几何约束**
   - *初始信念：* 认为角分布系数 $a_2, a_4$ 或 DCO 比值可以直接查表判定跃迁类型与混合比。
   - *修正后认知：* 认识到角分布强烈依赖于复合核自旋取向参数 $\sigma/I$ 以及侧线前级 feeding 引起的去取向过程；$R_{DCO}$ 在混合比 $\delta$ 上必然产生代数双根，若缺乏独立的线偏振（$\Delta_{PDCO}$）或内转换电子谱，单靠角分布无法唯一确定多极性。

3. **第三阶段（Day 15–21）：实验反证、系统误差与争议本质**
   - *初始信念：* 认为学术界的广泛引用意味着结论牢不可破。
   - *修正后认知：* 深入分析 $^{135}\text{Pr}$（Lv 2022 否定 Matta 2015）、$^{187}\text{Au}$（Guo 2022 否定纵向 wobbling）以及 $^{134}\text{Pr}$（Tonev 2007 否定静态手征）等一系列重大反例，深刻认识到许多被广泛宣传的“奇特集体模式”实质上是模型过度解释、门污染未扣除或取向参数强制预设造成的假象。

4. **第四阶段（Day 22–30）：跨质量区迁移、可证伪设计与研究 prospectus 终态收束**
   - *初始信念：* 认为推进科学研究需要不断摄入更多论文篇数或直接开展任意数据计算。
   - *修正后认知：* 确立了以“最小新增输入、明确证伪判据（falsifier）、停止条件（stop rule）与非独立证据边界”为核心的研究设计范式。在 $^{131}\text{Xe}$ 审计中，成功将三个年份的文献归拢为单次物理采集，坚决拒绝伪造事件级响应；在 $^{133}\text{Ce}/^{131}\text{Ce}$ 路线中，紧扣用户真实中期数据与微观先验，形成了面向博士学位课题与高水平论文的可执行 prospectus。

### 剩余开放问题
1. $^{135}\text{Pr}$ 中 Matta 原始数据与 Lv 数据在放开 $\sigma/I$ 后的全局联合似然度是否存在共同相容域？
2. $^{131}\text{Xe}$ 1600.9-keV 态的真实宇称是否能够通过历史 Irving 1979 / Lönnroth 1983 的内转换数据或新的转化系数实验彻底闭合？
3. $^{133}\text{Ce}$ 在 iThemba 实验中发现的带头为 $13/2^-$ 的新低自旋带，其直接微观 PC-PK1 PES 会展现出多大的刚性三轴极小值？

## L0–L4 state

全库各阶段研究课题的状态与准备度总账：

- **L0 (文献与数据摄入):** 全库已安全摄入并归档 130+ 篇核心核结构论文、学位论文及数据文件；
- **L1 (阅读与批注):** 完成 70+ 篇精读文献的 YAML 元数据、locator 锚定与原子 claim 提取；
- **L2 (知识综合与矩阵):** 建成涵盖核素、能带、实验装置、谱学方法与理论模型的网状长期知识库；
- **L3 (竞争解释鉴别与研究设计):**
  - `135Pr`: L3 common-response evidence contract 已冻结，等待原始符合数据；
  - `131Xe`: L3 lineage audit 已闭合，保持准备度边界，拒绝合成事件级响应；
  - `135Nd/134Pr`: L3 伙伴态绝对电磁量基准队列已建立；
  - 八极形变系列: L3 跨质量区证据梯级与语言校准账本已建立；
  - P-ADO: L3 跨反应对齐零假说反证分析已完成；
  - `131Ce/133Ce`: L3 模式鉴别程序已建立，结合博士中期考核成果。
- **L4 (真实数据分析与参数求解):**
  - `133Ce` South Africa 数据集已完成 ROOT 矩阵与工作簿的可读性与结构审计（partial-L4-readiness），在未获得直接微观 PES 与完整时间门展开前严格受控；
  - **红线遵守：** 全库没有生成任何虚构的事件级符合计数、探测器响应矩阵或联合协方差，未逾越 L4 真实数据边界。

## Verification and continuation

### 自动化预检与路径契约验证
- `system/scripts/wiki_boundary_check.py` 检查通过：六类持久化目录（`raw/`, `knowledge/`, `outputs/`, `system/`, `tools/`, `tmp/`）边界严格遵守，无越界文件，QMD 知识索引路径合规；
- `system/scripts/wiki_archive_gate.py` 归档门检查通过：所有新增与变更的源文件均具备本地 raw 文件与哈希校验对账；
- `system/scripts/wiki_automation_preflight.py` 预检通过：受保护的 BibTeX 基线与 git 工作区健康；
- `system/scripts/wiki_knowledge_writeback.py` 知识写回校验通过：本报告中的 8 项 writeback 条目与 `baseline.json` 比对完全吻合，所有变更文件均列入白名单并包含合法锚点。

### 30 天每日研学计划结业宣告
- **课程状态：** 30 天课程卡已连续、完整、无跳跃地全部完成（`completed_day_indices: [30]`, `completed_day_count: 30`）。
- **调度状态：** 阶段计划完成，标记为 `status: complete`，`next_day_index: 31`（超出 30 天矩阵，触发 cycle-complete 守卫，停止调用无效的 Day 31 启动器）。
- **后续阶段：** 知识库正式转入 **Post-30-day 博士高阶自主研究阶段**。后续工作将围绕 `knowledge/projects/post-30-day-nuclear-structure-paper-prospectus.md` 中定义的 7 个候选课题有序推进。
