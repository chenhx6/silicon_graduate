---
name: in-beam-gamma-spectroscopy
description: 在束 γ 谱学、重离子核反应实验设计与数据分析技能：HPGe/Clover 阵列、数字脉冲成形（DPP）、符合矩阵构建、DCO/偏振双根仲裁、激发态寿命测量（DSAM/RDM）与实验统计推断。
---

<!-- argument-hint: [topic, method, detector, reaction, or analysis tool] -->

# 在束 γ 谱学与重离子反应实验分析技能

本技能整合吴治华《原子核物理实验方法》、汪晓莲《粒子探测技术》、朱永生《实验物理中的概率和统计》、林承键《重离子核反应》、Nakhostin《辐射探测器信号处理》与 Hamilton《核谱学电磁相互作用》，
为低能实验核物理研究者提供从反应物理论证、探测阵列几何优化、数字脉冲成形调优（DPP）、符合能级纲图构建、角分布/线偏振判决到跨设备 Python 离线数据分析的专家级操作指南与数学物理规范。

---

## 核心思维模型与实验物理法典

### 1. 探测物理与信号成形（吴治华 vs 汪晓莲 vs Nakhostin）
- **定时走动与时间抖动**：
  - 定时走动（Walk）：脉冲幅度与上升时间涨落导致恒定阈值（LED）触发时刻偏移；必须使用恒定比值定时（CFD）寻找零点交叉消除走动；
  - 时间晃动（Jitter）：前放白噪声引起的有效时间不确定度 $\sigma_t \approx \sigma_n / (dV/dt)$；
  - 偶然符合规律：两路单计数率 $N_1, N_2$ 在分辨时间 $2\tau$ 内的偶然符合率为 $N_{\text{chance}} = 2\tau N_1 N_2$。
- **死时间模型对账**：
  - 非麻痹型（Non-paralyzable / 不扩展型）：死时间期间到达的脉冲被完全丢弃，不延长死时间，真计数率 $n = m / (1 - m\tau)$；
  - 麻痹型（Paralyzable / 扩展型）：死时间期间到达的脉冲重新重置死时间时钟，真计数率 $m = n e^{-n\tau}$；
  - 混合级联系统：前端闪烁体/前放（通常呈麻痹型）与后端数字化 ADC（通常呈非麻痹型）构成级联，高计数率下必须通过脉冲发生器（Pulser Injection）在线连续标定全系统活时间分数。
- **数字滤波与弹道亏损根除**：
  - 极零相消（PZC）：通过消除前放长衰减时间（$\tau_{\text{pre}} \approx 50\ \mu\text{s}$）产生的下冲拖尾，防止基线位移；
  - 梯形滤波平顶（Flat Top）：平顶宽度必须大于探测器内最大电荷收集时间（$FT \ge t_{\text{coll}}^m_{\max} \approx 200 - 400\text{ ns}$），彻底消除弹道亏损；
  - 移动窗口反褶积（MWD）：将前放指数拖尾在时域反褶积为有限矩形，结合自适应基线恢复（BLR），支持 $> 50\text{ kHz}$ 高计数率谱学。

### 2. 统计学裁判与多极双根退化（朱永生《实验物理中的概率和统计》）
- **角分布与 DCO 比值的数学双根退化**：
  - 方向角关联比值 $R_{\text{DCO}}(\delta)$ 是混合比 $\delta(E2/M1)$ 的二次分式；
  - 判别式 $\Delta > 0$ 时恒存在两个实数解：偶极占优的小 $|\delta|$ 根与四极占优的大 $|\delta|$ 根；
  - **黄金禁律**：在缺乏独立偏振度或内转换系数时，**严禁凭理论偏见（如预设为摆动带）主观挑选大根**，必须在数据中保留双根！
- **打破退化的物理正交手段**：
  - Clover 康普顿线偏振度 $P$：磁跃迁与电跃迁在偏振灵敏度公式中的交叉项符号相反，联合似然卡方 $\chi^2_{\text{joint}}(\delta) = \chi^2_{\text{DCO}} + \chi^2_P$ 可在 $>3\sigma$ 水平彻底排除伪根；
  - 内转换电子（ICE）：利用 $\alpha_K$ 区分 $E1$（极小）、$M1$ 与 $E2$。
- **高级统计推断法典**：
  - 剖面似然（Profile Likelihood）：通过对连续本底、探测效率漂移等干扰参数逐点条件极大化，自然吸收系统不确定度并给出真实非对称误差带；
  - Feldman-Cousins 统一置信带：在物理边界（如分支比 $b_\gamma \in [0, 1]$）与弱计数极限下，消除翻转决策导致的覆盖率不足；
  - Bootstrap 蒙特卡罗重采样：对非线性函数（如从寿命和混合比导出 $B(E2)$ 比值）通过完全协方差矩阵重采样，消除一阶泰勒级数微分失效。

### 3. 重离子反应道与实验束流方案（林承键《重离子核反应》）
- **反应截面与入射能量优化**：
  - 经典临界角动量 $\ell_n_{\text{crit}}$ 限制了完全熔合反应截面上限；
  - Wong 单势垒公式在近垒区受静态形变与表面集体振动耦合产生多势垒分布；
  - 经验 $xn$ 反应道能量窗口：$E^*_{\text{opt}}(xn) \approx \sum S_n + x \langle E_{\text{kin}}^n \rangle$（$A\a$A \aA \a130$ 区 $4n$ 最佳激发能为 $45 - 55\text{ MeV}$）。
- **靶设计与运动学反冲**：
  - 角分布测量靶：采用高导电重金属衬底（如 Au 衬底），利用高密度传导电子在飞秒尺度中和离子外层电荷，彻底消除真空退取向效应（$G_k \to 1.0$）；
  - 寿命测量靶：RDM 活塞法需无衬底自支撑超薄靶（$\sim 0.5 - 0.8\text{ mg/cm}^2$），控制反冲速度色散 $\Delta v/v \le 3\%$。

---

## 跨设备 Python 分析工具链

本仓库的在束谱学分析工具集成于 `system/scripts/analysis/nuclear_analyzer.py`，支持无缝 pull 到其他实验设备（仅依赖 Python 3 + NumPy / SciPy）运行：

```bash
# 1. 混合比双根仲裁与联合偏振检验 (DCO + POL)
python3 system/scripts/analysis/nuclear_analyzer.py doubleroot --preset 135Pr_wobbling_candidate

# 2. 高计数率 HPGe 移动窗口反褶积与自适应基线恢复 (MWD + BLR)
python3 system/scripts/analysis/nuclear_analyzer.py mwdblr --preset standard_hpge_high_rate

# 3. 三轴双转子剪刀振动模式 M1 共振双峰分裂预测
python3 system/scripts/analysis/nuclear_analyzer.py scissm1 --preset 134Ba_triaxial_scissors_doublet

# 4. 非绝热 Mikhailov / Davydov-Rostovsky 混和参量反演
python3 system/scripts/analysis/nuclear_analyzer.py rostovsky --preset 152Sm_classic_transitional_nucleus

# 5. 运行全套 60+ 实验分析单元测试验证环境自洽性
python3 system/scripts/analysis/test_analysis_suite.py
```

---

## 实验 Proposal 机时核算快速模板

在撰写重离子束流机时申请书时，遵循标准化物理产额推演：
1. **生成速率**：$R_{\text{prod}} = I_p \cdot N_t \cdot \sigma_{xn}$（例如 $3\text{ pnA}$ 束流在 $1.0\text{ mg/cm}^2$ 靶上产生截面 $380\text{ mb}$ 的核素，生成率约为 $3.5 \times 10^4\text{ nuclei/s}$）；
2. **符合事件率**：$R_{\gamma\gamma} = R_{\text{prod}} \cdot \langle M_\gamma \rangle(\langle M_\gamma \rangle - 1) \cdot \epsilon_{\text{tot}}^2 / 2$；
3. **统计目标**：弱跨带连接线（分支比 $5\%$）获得 $> 1000$ 计数以实现 $>3\sigma$ 线偏振判定，通常需要累积 $1.0 - 2.0 \times 10^8$ 个二重符合事件；
4. **机时预算**：结合探测效率、死时间（典型 $20\% - 30\%$）与调束开销，申请物理机时一般为 $120 - 168\text{ 小时}$（5–7 个运行工作日）。
