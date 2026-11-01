---
type: concept
title: "四叶草（Clover）HPGe探测器康普顿加和（Add-Back）、自散射偏振测量与几何不对称度校正法典"
aliases: [Clover探测器, 康普顿加和, Add-Back, 康普顿偏振仪, 散射不对称度, 几何校正系数, 偏振灵敏度, 宇称判定, 电多极与磁多极区分]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [clover-detector, compton-addback, compton-polarimetry, linear-polarization, geometric-asymmetry, parity-assignment, in-beam-spectroscopy, gamma-detectors]
---

# 四叶草（Clover）HPGe探测器康普顿加和（Add-Back）、自散射偏振测量与几何不对称度校正法典

## 1. 物理全景：四叶草几何对核谱仪探测效率与跃迁宇称判定的双重革命

在现代在束 $\gamma$ 谱学与核结构衰变实验中，单晶高纯锗探测器（HPGe）虽然具有卓越的能量分辨能力，但在探测高能 $\gamma$ 光子（$E_\gamma > 1\text{ MeV}$）时，绝大部分事件发生康普顿散射逃逸出晶体，使得全能峰绝对探测效率（Peak-to-Total, P/T）大幅萎缩。
同时，确定激发态的宇称（$\pi = \pm$）以及区分跃迁的电性与磁性（$E1$ vs $M1$，$E2$ vs $M2$）需要测量发射光子的线偏振度，传统外加散射体偏振仪因效率过低而极难应用于弱反应通道。

由欧洲核谱学合作组（EUROGAM / EUROBALL）研发的**四叶草（Clover）HPGe 探测器**，由 4 块紧密排列在同一杜瓦瓶内的独立 $n$ 型同轴高纯锗晶体（各 $50 \times 70\text{ mm}$）集成构成。
根据 G. Duchêne 等（Nucl. Instrum. Methods A 432, 481, 1999）、P. M. Jones 等（NIM A 362, 556, 1995）以及吴治华《原子核物理实验方法》（第三版）：
Clover 探测器实现了核仪器学上的两大核心飞跃：
1. **晶体间跨界康普顿加和技术（Compton Add-Back）**：
   当入射高能光子在一个晶体中发生康普顿散射后穿透至相邻晶体并被完全吸收时，通过数字电子学将两晶体在符合时间窗（$\Delta t \le 100\text{ ns}$）内的能量相加：
   $$E_{\text{add-back}} = E_1 + E_2$$
   **在高能区将光电全能峰探测效率大幅暴增 $40\% \sim 60\%$**，同时极度压低了康普顿平原连续谱背景；
2. **内嵌式自散射康普顿极化仪（Intrinsic Compton Polarimeter）**：
   4 块晶体两两构成了天然的正交散射散射体与吸收体。利用 Klein-Nishina 极化散射截面，单个 Clover 探测器即可直接充当高精度线偏振仪，**无任何额外硬件即可物理裁决光子的电/磁多极性与能级宇称**！

---

## 2. 严格物理推导与实验数据校正算法

### (1) 康普顿加和增强因子 $F_{\text{add-back}}(E_\gamma)$
定义加和增强因子为加和模式全能峰面积与单晶直接记录面积之比：
$$F_{\text{add-back}}(E_\gamma) = \frac{I_{\text{add-back}}(E_\gamma)}{I_{\text{direct}}(E_\gamma)}$$
在低能区（$E_\gamma < 200\text{ keV}$），光电效应占绝对优势，很少发生跨晶体飞溅散射，加和增益微弱（$F \approx 1.05$）；
随着能量升高（$E_\gamma > 600\text{ keV}$），康普顿散射成为主导相互作用，经验饱和形式为：
$$F_{\text{add-back}}(E_\gamma) \approx 1.05 + 0.48 \left[ 1 - \exp\left( - \frac{E_\gamma}{650\text{ keV}} \right) \right]$$
在典型 $E_\gamma = 1.33\text{ MeV}$ 处，$F_{\text{add-back}} \approx 1.47$，探测效率净提升近 $50\%$！

---

### (2) Klein-Nishina 极化散射与正交符合计数
根据量子电动力学，线偏振光子与自由电子发生康普顿散射的微观截面方程：
$$\frac{d\sigma}{d\Omega} = \frac{r_e^2}{2} \left( \frac{E'}{E} \right)^2 \left[ \frac{E'}{E} + \frac{E}{E'} - 2 \sin^2\theta \cos^2\phi \right]$$
其中 $\phi$ 为散射平面与入射光子线偏振电场矢量 $\vec{E}$ 之间的夹角。
**核心物理规律**：项 $- 2 \sin^2\theta \cos^2\phi$ 表明，**光子以最大几率垂直于其电场偏振方向发生康普顿侧向散射（$\phi = 90^\circ$ 极大）**！

当将 Clover 探头放置在相对束流轴呈 $\theta_{\text{lab}} = 90^\circ$ 的反应平面时：
- **垂直散射事件数 $N_\perp$**：在晶体对 $1 \leftrightarrow 3$ 与 $2 \leftrightarrow 4$ 之间发生的跨晶体散射（垂直于反应平面）；
- **平行散射事件数 $N_\parallel$**：在晶体对 $1 \leftrightarrow 2$ 与 $3 \leftrightarrow 4$ 之间发生的跨晶体散射（平行于反应平面）。

---

### (3) 几何不对称性标定因子 $a_{\text{geom}}$
由于加工中 4 块锗晶体的体积尺寸微差、电极间隙不均匀及前放电子学阈值漂移，即便对于完全无偏振（Unpolarized）的各向同性光子源，两组晶体对记录的散射数也不严格相等。
必须使用无偏振放射源（如 $^{152}\text{Eu}, ^{60}\text{Co}$）严格标定仪器几何因子：
$$a_{\text{geom}}(E_\gamma) = \left. \frac{N_\perp^{\text{unpol}}}{N_\parallel^{\text{unpol}}} \right|_{E_\gamma}$$
标准优质探头的 $a_{\text{geom}}$ 在 $0.98 \sim 1.02$ 之间。

---

### (4) 实验不对称度 $A_{\text{corr}}$ 与线偏振度 $P$ 提取
经过几何刻度纠偏后的真实物理不对称度为：
$$A_{\text{corr}} = \frac{N_\perp - a_{\text{geom}} N_\parallel}{N_\perp + a_{\text{geom}} N_\parallel}$$
误差由泊松统计方差严格传递：
$$\sigma_A = \frac{2 a_{\text{geom}}}{(N_\perp + a_{\text{geom}} N_\parallel)^2} \sqrt{N_\parallel^2 \sigma_\perp^2 + N_\perp^2 \sigma_\parallel^2}$$

线偏振度定义为散射不对称度与 Clover 固有偏振灵敏度 $Q(E_\gamma)$ 之比：
$$P = \frac{A_{\text{corr}}}{Q(E_\gamma)}$$
其中 Clover 偏振灵敏度函数在 $E_\gamma \sim 300 \sim 1500\text{ keV}$ 范围内参数化为：
$$Q(E_\gamma) \approx 0.24 \exp\left( - 0.00040 \cdot E_\gamma\text{ (keV)} \right) + 0.02$$
典型数值在 $0.15 \sim 0.22$ 之间。

#### 跃迁性质刚性裁决法典：
- **若 $P > 0$（显著大于零）**：电多极性跃迁（Electric, $E1, E2$）；
- **若 $P < 0$（显著小于零）**：磁多极性跃迁（Magnetic, $M1, M2$）。
这构成了在束核谱学中终结宇称争议的最强利器！

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/clover_compton_addback_polarization_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `clover` 命令。

### 运行示范（模拟典型在束测量 $E_\gamma = 846\text{ keV}$ 纯电四极跃迁）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py clover \
  -E 846.0 --n-perp 14200.0 --n-para 10500.0 --a-geom 1.01 --json
```

### 计算输出核心物理特征：
1. **加和增益计算**：在 $846.0\text{ keV}$ 下，Clover 加和系数 $F_{\text{add-back}} = 1.399$，单色峰探测效率获得 $+39.9\%$ 的巨大跃升；
2. **偏振参数解析**：
   - 探头灵敏度计算得出 $Q(846\text{ keV}) = 0.1911$；
   - 考虑 $a_{\text{geom}} = 1.01$ 仪器纠偏后，实测散射不对称度 $A_{\text{corr}} = 0.1449 \pm 0.0063$；
   - 绝对线偏振度反演得出：
     $$P = + 0.7584 \pm 0.0330$$
   - 显著大于零（$P / \sigma_P > 20\sigma$），自动判定为：
     `Electric (E1, E2) [Positive Polarization]`
   - 彻底排除了任何磁跃迁假象，确立了能级跃迁的不变宇称！

---

## 4. 与相关前沿概念的交叉引用
- [[angular-distribution-and-multipole-mixing-ratios]]：角分布系数 $a_2, a_4$ 只能确定跃迁多极阶数（偶极 vs 四极），必须与此处测得的偏振度 $P$ 联合才能彻底锁定电/磁属性与宇称；
- [[hpge-digital-pulse-processing-pzc-and-ballistic-deficit]]：Clover 各叶片输出的数字化能量与定时是实施亚微秒跨晶体 Add-Back 积分的电子学基础；
- [[experimental-uncertainty-propagation-and-double-root-triage]]：偏振度测量是解决多极混合比 $\delta(E2/M1)$ 双实数解退化歧义的最终仲裁法则。
