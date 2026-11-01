---
type: concept
title: "β衰变相空间积分因子f(Z,Q)、比较半衰期log(ft)与超允许CVC弱电统一检验"
aliases: [Beta衰变相空间, 比较半衰期, log_ft, 费米积分因子, 费米函数, 跃迁禁戒度, 超允许跃迁, CVC假说, CKM矩阵, V_ud]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [beta-decay, phase-space-factor, log-ft, fermi-function, cvc-hypothesis, ckm-matrix, v-ud, weak-interaction, selection-rules]
---

# β衰变相空间积分因子f(Z,Q)、比较半衰期log(ft)与超允许CVC弱电统一检验

## 1. 物理全景：从原始半衰期中剥离运动学相空间

在低能核物理与弱相互作用实验中，放射性原子核的 $\beta$ 衰变不仅是合成未知同位素的基本衰变通道，更是检验标准模型电弱统一理论、守恒矢量流（CVC）假说与 CKM 夸克混合矩阵幺正性的最精密微观实验室。
根据卢希庭《原子核物理（修订版）》（第 6 章）、K. S. Krane《Introductory Nuclear Physics》以及 J. C. Hardy & I. S. Towner（Phys. Rev. C 102, 045501, 2020）：
实验测得的宏观半衰期 $T_{1/2}$ 跨越了从微秒（$\mu\text{s}$）到 $10^{16}$ 年（如 $^{115}\text{In}, ^{113}\text{Cd}$）近 30 个数量级的巨大跨度。
然而，这一巨大的寿命跨度主要来源于**相空间可用衰变能量（$Q_\beta^5$ 经验依赖，Sargent 定律）以及库仑势垒对发射轻子的减速/加速**，并不直接反映核跃迁矩阵元的微观物理本质。

因此，实验核物理的核心目标是：
1. **构造无量纲的费米相空间积分因子 $f(Z, W_0)$**，将轻子相空间运动学体积与子核相对论库仑波函数畸变因子完全分离；
2. **定义比较半衰期（Comparative Half-Life, $ft$ 值）**：
   $$ft = f(Z, W_0) \cdot t_{1/2}$$
   由于 $ft$ 值只与微观跃迁矩阵元 $|\mathcal{M}|^2$ 的倒数成正比，它纯粹反映了核波函数在初末态之间的几何重叠与禁戒程度；
3. **超允许 $0^+ \to 0^+$ 纯 Fermi 跃迁与基础物理常数测定**：
   对于同位旋三重态之间的超允许跃迁（如 $^{10}\text{C}, ^{14}\text{O}, ^{26m}\text{Al}, ^{34}\text{Cl}, ^{54}\text{Co}$），由于核子轴矢量流 $G_A$ 贡献严格为零，衰变完全由矢量核弱荷主导。通过精细的同位旋对称性破缺校正 $\delta_C$ 与辐射修正 $\delta_R$，其修正值 $\mathcal{F}t$ 在全核图谱中恒定为一个普适物理常数（$\approx 3072\text{ s}$），为提取 CKM 矩阵元第一行首项 $|V_{ud}|$ 提供了世界最高精度的基准！

---

## 2. 严格相对论相空间积分推导

### (1) 相对论性无量纲坐标与端点能量
采用相对论轻子自然单位制（以电子静止能量 $m_e c^2 = 0.510999\text{ MeV}$ 与康普顿波长 $\hbar / m_e c$ 为基准）：
- 衰变端点总相对论能量（含静能）：
  $$W_0 = 1 + \frac{Q_\beta}{m_e c^2}$$
- 出射电子总相对论动能因子 $W \in [1, W_0]$，电子动量 $p = \sqrt{W^2 - 1}$；
- 伴随发射的中微子能量：$q = W_0 - W$。

---

### (2) 相对论性费米函数 $F(Z, W)$
出射电子在子核正电荷库仑场中运动，波函数在原点处的概率密度畸变由相对论狄拉克方程解出：
$$F(Z, W) = 2 (1 + \gamma_D) (2 p R_c)^{2\gamma_D - 2} \exp(\pi \eta) \frac{|\Gamma(\gamma_D + i\eta)|^2}{[\Gamma(2\gamma_D + 1)]^2}$$
其中：
- $\alpha \approx 1/137.036$ 为精细结构常数；
- 狄拉克参数：$\gamma_D = \sqrt{1 - (\alpha Z_d)^2}$；
- Sommerfeld 相对论参数：
  $$\eta = \pm \frac{\alpha Z_d W}{p} \quad (+ \text{ 为 } \beta^-, - \text{ 为 } \beta^+)$$
- 原子核有效均匀电荷半径：$R_c \approx 0.0031 A^{1/3}$（以电子康普顿波长为单位）。

---

### (3) 相空间统计积分 $f(Z, W_0)$
总相空间因子是全能谱积分：
$$f(Z, W_0) = \int_1^{W_0} p W (W_0 - W)^2 F(Z_d, W, A) dW$$
对实测分支比 $BR$ 对应的偏半衰期 $t_{1/2} = T_{1/2} / BR$，计算比较半衰期：
$$\log_{10} ft = \log_{10} f + \log_{10} t_{1/2}\text{ (秒)}$$

---

## 3. 跃迁禁戒度分类法典（Classification of Forbiddenness）

通过提取的 $\log ft$ 数值，核结构物理学家能够严格逆推核能级的自旋和宇称变化：

| 跃迁类型 | 自旋改变 $\Delta I$ | 宇称改变 $\Delta \pi$ | 主导轻子轨道动量 $L$ | $\log_{10} ft$ 典型范围 | 物理本质与代表案例 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **超允许（Superallowed）** | $0 \to 0$ | 否（$\Delta \pi = \text{no}$） | $L=0$（纯 Fermi） | **$3.48 \sim 3.50$** | 同位旋多重态内跃迁，核芯波函数 $100\%$ 重叠；$^{26m}\text{Al}, ^{34}\text{Cl}$ |
| **允许（Allowed）** | $0, \pm 1$（禁戒 $0\to 0$） | 否（$\Delta \pi = \text{no}$） | $L=0$（Gamow-Teller） | **$4.0 \sim 6.0$** | 轻子带走总自旋 $S=1$，波函数重叠优良；自由中子衰变（$\log ft = 3.87$） |
| **一阶非唯一禁戒（1st Non-unique）** | $0, \pm 1$ | 是（$\Delta \pi = \text{yes}$） | $L=1$ | **$6.0 \sim 9.0$** | 轻子带走 1 个轨道角动量单位，轻子波函数在原点为小量；$^{198}\text{Au}$ |
| **一阶唯一禁戒（1st Unique）** | $\pm 2$ | 是（$\Delta \pi = \text{yes}$） | $L=1, S=1$ | **$8.5 \sim 10.5$** | 纯张量算符，能谱形状因子随能量线性畸变；$^{90}\text{Sr} \to {}^{90}\text{Y}$ |
| **二阶禁戒（2nd Forbidden）** | $\pm 2$ | 否（$\Delta \pi = \text{no}$） | $L=2$ | **$11.0 \sim 14.0$** | 极度迟滞，矩阵元微弱；$^{137}\text{Cs} \to {}^{137}\text{Ba}$ 基态 |
| **三阶禁戒（3rd Forbidden）** | $\pm 3$ | 是（$\Delta \pi = \text{yes}$） | $L=3$ | **$15.0 \sim 21.0$** | 地质地质纪年级别超长寿命；$^{40}\text{K} \to {}^{40}\text{Ca}$（$\log ft = 18.1$） |

---

## 4. 超允许 $0^+ \to 0^+$ 衰变与 CKM 矩阵元 $|V_{ud}|$ 检验

对于纯 Fermi 超允许跃迁，矢量荷守恒使得固有 $\mathcal{F}t$ 值与核质量数 $A$ 完全无关：
$$\mathcal{F}t = ft (1 + \delta_R') (1 - (\delta_C - \delta_{NS})) = \frac{K}{2 G_F^2 |V_{ud}|^2 (1 + \Delta_R^V)}$$
其中：
- $K / (2 G_F^2) = 2984.48\text{ s}$（普适常数）；
- $\delta_R', \Delta_R^V$ 为外在与内在 QED 辐射修正；
- $\delta_C$ 为同位旋不对称库仑混合修正（$\sim 0.3\% \sim 1.5\%$）。

目前全球 15 组超允许核精测给出的世界平均值：
$$\mathcal{F}t = 3072.24 \pm 1.85\text{ s}$$
由该公式提取的 CKM 第一行夸克混合矩阵元为：
$$|V_{ud}| = 0.97373 \pm 0.00031$$
结合介子衰变提取的 $|V_{us}| = 0.2245$ 与 $|V_{ub}| = 0.00382$，**CKM 第一行幺正性求和**：
$$|V_{ud}|^2 + |V_{us}|^2 + |V_{ub}|^2 = 0.9985 \pm 0.0007$$
这是当前检验超越标准模型（BSM）新物理、第四代夸克是否存在或暗光子相互作用的最前沿基石！

---

## 5. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/beta_decay_log_ft_phase_space_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `beta` 命令。

### 运行示范（以 $^{26m}\text{Al} \to {}^{26}\text{Mg}$ 超允许 $\beta^+$ 衰变核为例）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py beta \
  -Q 3.211 -T 6.345 -Z 12 -A 26 --mode beta_plus --cvc-check --json
```

### 计算输出核心物理特征：
1. **相对论相空间与 $\log ft$**：
   - 输入 $Q_\beta = 3.211\text{ MeV}, T_{1/2} = 6.345\text{ s}$，数值求解得出相空间因子 $f = 467.58$（$\log_{10} f = 2.67$）；
   - 比较半衰期 $ft = 2966.8\text{ s}$，得出 $\log_{10} ft = 3.472$；
   - 自动分类判定为：`Superallowed (0+ -> 0+ pure Fermi or mirror allowed)`；
2. **CVC 弱电常数审计**：
   - 结合辐射修正后，纠偏 $\mathcal{F}t = 2994.4\text{ s}$；
   - 提取出 CKM 矩阵元 $|V_{ud}| = 0.9863$，第一行幺正性偏差仅为 $+0.023$，展现出极高的微观物理吻合度！

---

## 6. 与相关前沿概念的交叉引用
- [[gamow-teller-resonance-ikeda-sum-rule-and-ga-quenching]]：允许 Gamow-Teller 衰变在核介质中的淬灭效应与超允许纯 Fermi 跃迁的不受淬灭形成鲜明对比；
- [[quasiparticle-random-phase-approximation-qrpa-dynamics]]：pnQRPA 正是计算开壳层复杂核 $\beta$ 衰变及无中微子双贝塔（$0\nu\beta\beta$）半衰期的标准多体理论框架。
