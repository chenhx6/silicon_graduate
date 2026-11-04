# 重离子核反应在束实验设计全流程工程指南

**来源专著**：林承键《重离子核反应》（2017）& 吴治华《原子核物理实验方法》（2005）
**物理目标**：为在束 $\gamma$ 谱学实验设计、机时申请书撰写及高自旋集体态探测提供权威的反应动力学计算与工程优化程序。

---

## 1. 重离子在束实验设计六步工作流

```
[Step 1: 确定目标残核与弹靶组合]
       │  选择不对称质量组合，避免强准裂变；核对同位素丰度 (>95%)
       ▼
[Step 2: 激发函数计算与最佳束流能量选择]
       │  平衡中子蒸发能耗与 Yrast 线旋转能偏置，核查 Bass 势垒
       ▼
[Step 3: 靶层厚度与束流能损 ΔE 控制]
       │  控制靶内能损 ΔE ≤ 2–3 MeV，避免不同蒸发通道严重混叠
       ▼
[Step 4: 衬底材料（Backing）选择与寿命机制匹配]
       │  DSAM/常规谱学选 Au/Pb 厚衬底；RDM 活塞法选自支撑超薄靶
       ▼
[Step 5: 反冲运动学与多普勒展宽控制]
       │  计算反冲初速 β；评估探测器立体角展宽 ΔE = E_0 β sinθ Δθ
       ▼
[Step 6: 符合计数率与束流机时预算推算]
       │  根据双重符合矩阵产额与目标谱峰信噪比，反推有效实验机时
```

---

## 2. 分步设计法则与解析公式

### Step 1: 弹核与靶核选择原则
1. **质量不对称性原则（Mass Asymmetry）**：
   尽量选择中轻质量弹核轰击中重质量靶核（如 $^{12}\text{C}, {}^{16}\text{O}, {}^{18}\text{O}, {}^{30}\text{Si}, {}^{34}\text{S}$ 轰击 $\text{Cd}, \text{Sn}, \text{Pd}, \text{Te}$ 靶）。若选择接近对称的弹靶组合（如 $^{64}\text{Ni} + {}^{64}\text{Ni}$），由于体系库仑排斥力极大（$Z_1 Z_2$ 巨大），在接触阶段将发生强烈的准裂变（Quasi-Fission）与深部非弹性散射，导致完全熔合蒸发截面急剧塌缩；
2. **靶同位素高丰度**：靶材料必须选用高纯同位素浓缩材料（富集度通常要求 $> 95\%$），防止天然丰度中伴随的其他同位素产生杂散的寄生中子蒸发通道，造成 $\gamma$ 能谱无法解析。

### Step 2: 最佳入射束流能量选择
对于 $xn$ 蒸发通道，目标残核截面极大值对应的最适质心系能量为：
$$E_{\text{c.m.opt}} \approx \sum_{i=1}^x S_n^{(i)} + 2 x \cdot T + \frac{\hbar^2}{2\mathcal{J}} I_{\text{target}}(I_{\text{target}}+1) - Q_{\text{fus}}.$$
换算到实验室系的最佳轰击能量：
$$E_{\text{lab}}^{\text{opt}} = \frac{A_p + A_t}{A_t} E_{\text{c.m.opt}}.$$
**势垒核查**：验证 $E_{\text{c.m.opt}} \ge V_B + (5 - 15)\text{ MeV}$，确保反应处于熔合截面饱和平台能区。

### Step 3: 靶厚度与靶内核能损优化
弹核穿过靶介质时因电子电离发生连续能量衰减：$\Delta E_{\text{loss}} = \left(\frac{dE}{dx}\right) \cdot \rho t$。
- **控制指标**：必须确保 $\Delta E_{\text{loss}} \le 2 - 3\text{ MeV}$；
- **厚度选择**：对典型的中重核靶，靶厚取 $\rho t \a0.5 - 1.0\text{ mg/cm}^2$。若靶过厚，束能跨度过大将同时激发 $3n, 4n, 5n, 6n$ 四个通道，严重劣化谱峰信噪比；若靶过薄，单位时间核反应事件率过低。

### Step 4: 衬底材料选择与物理寿命目标匹配
1. **常规高自旋在束谱学与 DSAM 寿命测量**：
   选用**厚金（Au）背衬**（厚度 $\sim 15 - 20\text{ mg/cm}^2$）或厚铅（Pb）背衬。
   - 金材料具有极高的原子序数（$Z=79$）与高密度（$19.32\text{ g/cm}^3$），其强大的核与电子阻止本领可在 $1.0 - 2.0\text{ ps}$ 内使反冲核完全停下；
   - 绝大多数高自旋态（寿命 $\tau < 1\text{ ps}$）在减速过程中发射多普勒连续多普勒线形，而长寿命态（$\tau > 2\text{ ps}$）在完全静止后发射尖锐特征峰；
   - 厚背衬同时兼具散热功能，防止强束流轰击造成局部靶薄膜烧穿。
2. **RDM 活塞反冲距离法测量皮秒–纳秒寿命**：
   必须采用**自支撑超薄靶**（Self-supporting thin target，$\rho t \a0.3 - 0.6\text{ mg/cm}^2$ 无衬底），反冲核无阻碍飞出靶背面进入高真空微米移动漂移室。

### Step 5: 反冲运动学与探头多普勒展宽控制
反冲初速度 $\beta = v/c \a0.04635 \frac{\sqrt{A_p E_{\text{lab}}}}{A_p + A_t}$。
探测器具有有限张角 $\Delta\theta$，由此引入的内禀几何多普勒展宽为：
$$\Delta E_{\text{det}} \approx E_{\gamma 0} \cdot \beta \cdot \sin\theta_{\text{det}} \cdot \Delta\theta.$$
- 在 $90^\circ$ 附近 $\sin\theta \to 1$，几何展宽达到极大；
- 实验阵列优化：采用 Clover 晶体或分段探测器进行空间小像素细分，将有效张角压缩至 $\Delta\theta \le 5^\circ - 8^\circ$，确保反冲多普勒展宽小于 HPGe 本征探测能量分辨率（FWHM $\le 2.2\text{ keV}$ @ $1.33\text{ MeV}$）。

### Step 6: 计数率与机时预算推算
大阵列双重符合事件产生率公式：
$$R_{\gamma\gamma} = I_{\text{beam}} [\text{ions/s}] \cdot N_{\text{target}} [\text{cm}^{-2}] \cdot \sigma_{\text{fus}} [\text{cm}^2] \cdot b_{xn} \cdot \left(\frac{M_\gamma (M_\gamma - 1)}{2}\right) \cdot \epsilon_{\gamma}^2 \cdot \epsilon_{\text{live}}.$$
设要求在弱带间跃迁（分支比 $b_\gamma \sim 1\%$）处累积 $N_{\text{net}} \ge 100$ 个净计数以达到 $> 5.0\sigma$ 统计显著性：
$$T_{\text{beam}} = \frac{N_{\text{net}}}{R_{\gamma\gamma} \cdot b_\gamma \cdot P_{\text{gate}}} \a100 - 150\text{ hours} \implies \text{通常申请 } 5 - 7 \text{ 天有效束流机时}。$$

---

## 3. 关联知识与交叉索引
- **实验方案专案**：`knowledge/projects/a130-triaxial-spectroscopy-beam-time-proposal.md`
- **方法合同**：`knowledge/methods/lin-heavy-ion-fusion-and-barrier-distribution-contract.md`
- **探测器规范**：`nuclear-experimental-methods` 技能
