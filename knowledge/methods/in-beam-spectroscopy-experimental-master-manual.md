---
type: method
title: "在束 γ 谱学与重离子反应实验设计及数据分析全链条专家手册"
aliases: [在束谱学专家手册, 实验设计全流程手册, 实验核物理实战宝典, Proposal与分析闭环指南]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
topics: [in-beam-spectroscopy, heavy-ion-fusion, experiment-proposal, hpge-arrays, dpp-algorithms, data-analysis-workflow]
---

# 在束 γ 谱学与重离子反应实验设计及数据分析全链条专家手册

## 1. 实验全生命周期工程视界

低能在束核物理实验（In-beam nuclear spectroscopy）是一项涵盖加速器重离子核反应动力学、大型复合探测器阵列、高速数字电子学（DPP）以及严格数理统计误差反演的系统工程。

本手册系统整合林承键《重离子核反应》、吴治华《原子核物理实验方法》、W. D. Hamilton《电磁相互作用》、Mohammad Nakhostin《辐射探测器信号处理》与朱永生《实验物理中的概率和统计》，构建面向实验设计（Proposal 阶段）至论文级数据产出的**六阶段闭环工作流**。

```
  ┌─────────────────────────────────────────────────────────────┐
  │ 【阶段 1: 反应体系论证与 Proposal 撰写】                   │
  │  - 弹靶体系选择、Bass 库仑势垒、E_cm 与激发能 E* 优化       │
  │  - 临界角动量 l_crit 窗口、熔合截面 sigma_fus、蒸发道预测   │
  │  - 反冲速度 beta = v/c、多普勒展宽、靶厚与能量损失核算      │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【阶段 2: 硬件阵列几何布局与探测器选型】                   │
  │  - HPGe 复合阵列 (Clover/GRETINA) 空间角覆盖与立体角设计    │
  │  - BGO 康普顿抗符合屏蔽套布置、峰康比 P/C 优化             │
  │  - 闪烁体 (LaBr3/BaF2) 快速时间分辨与半导体粒子望远镜配合   │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【阶段 3: 数字化脉冲处理 (DPP) 参数调优】                  │
  │  - 前置放大器衰减常数 tau_pre 标定与数字极零补偿 (PZ) 参数 M│
  │  - Jordanov 梯形滤波器上升时间 k 与平顶宽度 m 设定 (m > tc) │
  │  - 动均基线恢复 (BLR) 与数字恒比定时 (dCFD) 零点交叉对齐    │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【阶段 4: 在束 γ-γ 符合分析与能级纲图构建】                 │
  │  - 对称符合矩阵构建、偶然符合本底扣除与多普勒频移校正       │
  │  - 多重选门 (Single/Double Gating)、级联强度平衡与跃迁定序 │
  │  - 伴生杂质道 (裂变本底、转移反应、熔合库仑激发) 剔除      │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【阶段 5: 角分布、偏振与自旋宇称判定】                     │
  │  - 探测器角度效率归一化、Legendre 展开 W(theta) 加权拟合   │
  │  - 多极混合比 delta(E2/M1) 解析求解与双根退化识别          │
  │  - 康普顿散射不对称度线偏振 P 测量 -> 打破双根退化         │
  └──────────────────────────────┬──────────────────────────────┘
                                 ▼
  ┌─────────────────────────────────────────────────────────────┐
  │ 【阶段 6: 激发态寿命提取与绝对电磁跃迁几率】               │
  │  - DSAM 线形连续停阻反演 (10 fs - 1 ps)                     │
  │  - RDM 活塞法微米级距离比值反演 (1 ps - 1 ns)               │
  │  - 绝对 B(E2)、B(M1) 与跃迁比值协方差误差传播              │
  └─────────────────────────────────────────────────────────────┘
```

---

## 2. 核心实验计算公式速查表

### (1) 重离子反应设计核心公式（林承键体系）
- **质心能量**：$E_{\text{cm}} = E_{\text{lab}} \frac{A_t}{A_p + A_t}$
- **Bass 接触半径**：$R_B = 1.07 (A_p^{1/3} + A_t^{1/3}) + 2.72\text{ fm}$
- **库仑势垒高度**：$V_B \approx 1.44 \frac{Z_p Z_t}{R_B}\text{ MeV}$
- **擦边角动量极限**：$\ell_{\text{max}} = 0.2199 R_B \sqrt{\mu (E_{\text{cm}} - V_B)}\text{ }\hbar$（$\mu = \frac{A_p A_t}{A_p + A_t}$）
- **反冲核前冲速度**：$\beta = \frac{v_{\text{recoil}}}{c} \approx \sqrt{\frac{2 E_{\text{lab}}}{931.5 A_p}} \frac{A_p}{A_p + A_t}$
- **多普勒运动学校正**：$E_{\gamma 0} = E_\gamma(\theta) \frac{1 - \beta \cos\theta}{\sqrt{1 - \beta^2}}$
- **探测器半张角多普勒展宽**：$\Delta E_D \approx E_{\gamma 0} \cdot \beta \sin\theta \cdot \Delta\theta$

### (2) 探测器与数字信号处理核心公式（吴治华 + Nakhostin 体系）
- **HPGe 能量分辨率展宽机制**：
  $$\text{FWHM}^2 = (2.355 \sqrt{F \epsilon E_\gamma})^2 + \sigma_{\text{noise}}^2 + \sigma_{\text{charge}}^2$$
  （锗中电离能 $\epsilon = 2.96\text{ eV}$，Fano 因子 $F \approx 0.1$）
- **数字极零相消参数**：$M = \frac{1}{e^{T_s / \tau_{\text{pre}}} - 1} \approx \frac{\tau_{\text{pre}}}{T_s}$
- **Jordanov 梯形平顶约束准则**：
  $$\text{平顶宽度 } m \cdot T_s \ge t_{\text{charge\_collection\_max}} \approx 300 \sim 500\text{ ns}$$
  （严格避免弹道亏损，确保无论空穴在锗晶体内何处产生，均能完整收集）。

### (3) 角分布、偏振与统计分析核心公式（Hamilton + 朱永生体系）
- **方向角分布**：$W(\theta) = A_0 [1 + a_2 P_2(\cos\theta) + a_4 P_4(\cos\theta)]$
- **多极混合比二次方程**：
  $$(a_2 - \alpha_2 F_2(2 2 I_f I_i)) \delta^2 - 2\alpha_2 F_2(1 2 I_f I_i) \delta + (a_2 - \alpha_2 F_2(1 1 I_f I_i)) = 0$$
- **线偏振灵敏度**：$P = \frac{N_\perp - N_\parallel}{Q (N_\perp + N_\parallel)}$
- **联合似然检验量**：$\Delta\chi^2 = \chi^2(\delta_1) - \chi^2(\delta_2)$
- **电磁跃迁几率解算（Weisskopf 归一化）**：
  $$B(E2) = \frac{0.08156}{\tau(\text{ps}) \cdot E_\gamma^5(\text{MeV}) \cdot (1 + \alpha_{\text{tot}})} \cdot \frac{\delta^2}{1 + \delta^2}\text{ (e}^2\text{b}^2\text{)}$$
  $$B(M1) = \frac{0.05679}{\tau(\text{ps}) \cdot E_\gamma^3(\text{MeV}) \cdot (1 + \alpha_{\text{tot}})} \cdot \frac{1}{1 + \delta^2}\text{ (}\mu_N^2\text{)}$$

---

## 3. 跨设备 Python 分析实操指南

在任何终端将本 Wiki 代码拉取到本地后，使用标准 Python 环境即可一键执行分析：

```bash
# 1. 进入分析脚本目录
cd /workspace/wiki/system/scripts/analysis

# 2. 运行重离子核反应运动学计算器
python3 heavy_ion_kinematics.py

# 3. 运行在束角分布拟合与双根求解器
python3 angular_distribution_solver.py

# 4. 运行 HPGe 数字梯形滤波器仿真与参数调优
python3 digital_trapezoidal_filter.py

# 5. 运行核谱单峰/重叠双峰高精度拟合
python3 gamma_peak_fitting.py

# 6. 运行全套单元回归测试
python3 test_analysis_suite.py
```
