---
type: concept
title: "重离子线动量转移（LMT）、不完全熔合动力学与裂变碎片折叠角关联法典"
aliases: [线动量转移, LMT, 不完全熔合, ICF, 裂变折叠角, 动量丢失, 旁观者粒子, 预平衡发射, 中能重离子碰撞]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [linear-momentum-transfer, lmt, incomplete-fusion, icf, fission-folding-angle, spectator-emission, pre-equilibrium, heavy-ion-reactions]
---

# 重离子线动量转移（LMT）、不完全熔合动力学与裂变碎片折叠角关联法典

## 1. 物理全景：从中能碰撞到不完全熔合的动力学相变

在低能重离子碰撞中（束流能量 $E_{\text{lab}} < 5 \sim 8\text{ MeV/u}$，库仑势垒附近），相互作用时间远长于核内部自由程时间，弹核与靶核发生**完全熔合（Complete Fusion, CF）**：
弹核的所有质量 $A_p$ 与入射线动量 $p_0$ 被 $100\%$ 转移给复合核系统，线动量转移分数严格等于 1：
$$\rho = \frac{\Delta p}{p_0} = 1.0$$
然而，当中能加速器将束流能量提升至中能区（$10 \sim 100\text{ MeV/u}$，接近甚至超过核内核子 Fermi 动能时）：
核子-核子两体硬碰撞开始打破平均场的绝对凝聚，弹核在与靶核接触瞬间极易发生**破裂（Breakup）**或剧烈的**预平衡发射（Pre-equilibrium Emission）**：
1. **不完全熔合机制（Incomplete Fusion, ICF）**：
   弹核中仅有一部分“参与者（Participant）”核子团块 $A_{\text{trans}}$ 与靶核熔合，而另一部分“旁观者（Spectator）”核子（如前冲的高能 $\alpha$ 粒子、质子、快中子）携带着接近束流速度的动量逃逸到连续区！
2. **线动量转移分数 $\rho < 1$**：
   残余核系统接收的线动量显著小于全动量（$\Delta p / p_0 \approx 0.6 \sim 0.9$），形成的中间热核质量显著减轻，激发能量与角动量受到严重削减；
3. **二体裂变碎片折叠角实验关口（Fission Folding Angle, $\theta_{\text{fold}}$）**：
   根据林承键《重离子核反应》、V. E. Viola 等（Phys. Rev. C 26, 178, 1982）与 M. B. Tsang 等（Phys. Rev. C 28, 2163, 1983）：
   对于重靶系统，中间激发核最终发生二体裂变。在运动复合核静止标架中，两裂变碎片严格背对背（$180^\circ$）发射；但在实验室系中，前冲反冲速度 $v_{\text{rec}}$ 将两碎片向前推挤，使得**实验室系折叠角 $\theta_{\text{fold}} = \theta_1 + \theta_2 < 180^\circ$**。
   **折叠角 $\theta_{\text{fold}}$ 的大小与线动量转移分数 $\rho$ 构成严格的一对一单调映射**，成为实验上直接划分完全熔合与不完全熔合截面的最权威测量准则！

---

## 2. 严格相对论运动学与裂变角关联方程

### (1) 入射弹核动量与完全熔合反冲基准
设实验室系入射束流动能为 $E_{\text{lab}}$，弹核静能为 $m_p = A_p m_u$：
- 相对论因子：$\gamma_0 = 1 + \frac{E_{\text{lab}}}{m_p}$，束流速度 $\beta_0 = \sqrt{1 - 1/\gamma_0^2}$；
- 入射总线动量：$p_0 = \gamma_0 m_p \beta_0 c$。

若发生完全熔合（CF）：
复合核总质量为 $M_{\text{CN}} \approx (A_p + A_t) m_u$。
完全动量转移对应的复合核前冲反冲速度为：
$$\beta_{\text{rec, CF}} = \frac{p_0}{M_{\text{CN}} c} \approx \beta_0 \frac{A_p}{A_p + A_t}$$

---

### (2) 不完全熔合（ICF）转移质量与实际反冲速度
若仅发生部分动量转移，定义分数因子 $\rho = \Delta p / p_0 \in [0, 1]$：
- 实际转移至热核的有效质量：
  $$A_{\text{trans}} \approx \rho \cdot A_p$$
- 前冲逃逸旁观者质量：$A_{\text{spec}} = (1 - \rho) A_p$；
- 真实反冲核速度：
  $$\beta_{\text{rec}} = \rho \cdot \beta_{\text{rec, CF}} = \rho \cdot \beta_0 \frac{A_p}{A_p + A_t}$$
随着 $\rho$ 从 1 下降，反冲核在实验室系中的前冲速度成比例减弱。

---

### (3) 二体对称裂变折叠角 $\theta_{\text{fold}}$ 严格解析几何
设生成的热核在飞行中发生对称裂变（碎片质量 $A_{f1} \approx A_{f2} \approx A_{\text{CN}}/2$）：
根据 Viola 裂变总动能系统学，断裂释放总动能为 $\text{TKE}$。
在反冲核内禀随动坐标系中，各碎片的固有分离速度为：
$$\beta_{\text{frag}} = \sqrt{\frac{\text{TKE}}{\frac{1}{2} A_{\text{CN}} m_u c^2}}$$

在实验室系中，对垂直于束流轴方向（$\theta_{\text{c.m.}} = 90^\circ$）对称发射的两碎片施加沿束流方向的反冲速度 $\beta_{\text{rec}}$ 洛伦兹推移：
两碎片的实验室发射仰角满足严格几何对称：
$$\tan\left(\frac{\theta_{\text{fold}}}{2}\right) = \frac{\beta_{\text{frag}}}{\beta_{\text{rec}}}$$
从而得出闭合的 **折叠角公式**：
$$\theta_{\text{fold}} = 2 \arctan\left( \frac{\beta_{\text{frag}}}{\beta_{\text{rec}}} \right)$$

#### 物理极限分析：
1. **静止靶极限（$\rho \to 0, \beta_{\text{rec}} \to 0$）**：
   $\tan(\theta_{\text{fold}}/2) \to \infty \implies \theta_{\text{fold}} = 180^\circ$（两碎片背靠背完全反向分离）；
2. **完全熔合极限（$\rho = 1.0, \beta_{\text{rec}} = \beta_{\text{rec, CF}}$ 达到最大）**：
   $\beta_{\text{rec}}$ 最大导致 $\tan(\theta_{\text{fold}}/2)$ 达到极小值，**折叠角最为狭窄尖锐（典型值为 $150^\circ \sim 160^\circ$）**；
3. **不完全熔合过渡区（$0.5 \le \rho < 1.0$）**：
   随着动量丢失，$\beta_{\text{rec}}$ 变小，**折叠角从尖锐的角度向 $180^\circ$ 方向逐步展开**！
   在实验测量的 $d\sigma / d\theta_{\text{fold}}$ 谱图上，完全熔合表现为一个窄峰，而不完全熔合表现为向大角度拖延的宽弥散平台。

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/linear_momentum_transfer_incomplete_fusion_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `lmt` 命令。

### 运行示范（模拟典型中能反应 $^{16}\text{O} + {}^{238}\text{U}$ 在 $160\text{ MeV}$ 束流下的折叠角动力学）：
```bash
python3 system/scripts/analysis/linear_momentum_transfer_incomplete_fusion_calculator.py \
  -Zp 8 -Ap 16 -Zt 92 -At 238 -E 160.0 --json
```

### 计算输出核心物理特征：
1. **完全熔合基准（$\rho = 1.0$）**：
   - 束流速度 $\beta_0 = 0.1454$（$10.0\text{ MeV/u}$）；
   - 完全动量转移下，复合核反冲速度为光速的 $0.92\%$（$\beta_{\text{rec}} = 0.0092$）；
   - 裂变总动能 $\text{TKE} = 195.0\text{ MeV}$，碎片在内禀系速度 $\beta_{\text{frag}} = 0.0406$；
   - **完全熔合特征折叠角：$\theta_{\text{fold}} = 154.6^\circ$**；
2. **动量转移损失剖面（LMT Scan）**：
   - 当 $\rho = 0.90$（损失 1.6 个核子）时：折叠角展开至 $157.0^\circ$；
   - 当 $\rho = 0.70$（损失 4.8 个核子）时：折叠角展开至 $161.9^\circ$；
   - 当 $\rho = 0.50$（仅转移一半动量）时：折叠角大幅张开至 $166.9^\circ$；
   - 角度位移清晰可分（每 $10\%$ 动量转移损失对应 $\approx 2.5^\circ$ 的宏观角度变化），为在束裂变裂解探测器布局提供了完备的运动学基准！

---

## 4. 与相关前沿概念的交叉引用
- [[fission-fragment-mass-yield-calculator]]：此处裂变折叠角的内在碎片动力学参数 $\text{TKE}$ 正是由 Viola 裂变动能系统学生成；
- [[multi-nucleon-transfer-and-deep-inelastic-collisions]]：不完全熔合（ICF）是深部非弹性散射（DIC）向完全熔合（CF）演化过渡的中间动力学形态；
- [[heavy-ion-fusion-evaporation-and-statistical-decay]]：只有先通过 $\theta_{\text{fold}}$ 判定确认属于完全熔合通道，才能安全代入后续 Hauser-Feshbach 统计蒸发模型。
