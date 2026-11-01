---
type: concept
title: "无中微子双贝塔衰变（0νββ）核矩阵元（NME）、有效马约拉纳中微子质量与gA淬灭动力学"
aliases: [无中微子双贝塔衰变, 0nu-beta-beta, 核矩阵元, NME, 马约拉纳质量, gA淬灭, 闭合近似, 76Ge, 136Xe, 倒序质量谱]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [double-beta-decay, 0nu-beta-beta, nuclear-matrix-elements, nme, majorana-neutrino-mass, ga-quenching, closure-approximation, legend-gerda, nexo]
---

# 无中微子双贝塔衰变（0νββ）核矩阵元（NME）、有效马约拉纳中微子质量与gA淬灭动力学

## 1. 物理全景：粒子物理标准模型之外的轻子数破坏与核多体物理桥梁

在粒子物理学与原子核物理学的最高前沿，中微子是否为其自身的反粒子（马约拉纳粒子，Majorana Fermion）是揭示宇宙正反物质不对称性（重子数轻子数生成机制, Leptogenesis）的决定性谜题。
**无中微子双贝塔衰变（Neutrinoless Double Beta Decay, $0\nu\beta\beta$）**：
$$(A, Z) \to (A, Z+2) + 2 e^-$$
是目前全人类在实验室中唯一能够直接检验总轻子数不守恒（$\Delta L = 2$）、证明中微子具有马约拉纳属性并测量其绝对质量标度的物理过程。

根据 J. Engel & J. Menéndez（Rep. Prog. Phys. 80, 046301, 2017）、J. Suhonen & O. Civitarese（Phys. Rep. 300, 123, 1998）以及国际大型深地实验组（GERDA/LEGEND、KamLAND-Zen、CUORE、nEXO）：
衰变半衰期与有效马约拉纳质量直接相连：
$$(T_{1/2}^{0\nu})^{-1} = G_{0\nu}(Q_{\beta\beta}, Z) \cdot |M^{0\nu}|^2 \cdot \left( \frac{\langle m_{\beta\beta} \rangle}{m_e} \right)^2$$
式中：
- $G_{0\nu}$ 为高精度原子物理相空间因子；
- $\langle m_{\beta\beta} \rangle = |\sum_i U_{ei}^2 m_i|$ 为有效马约拉纳中微子质量；
- **$M^{0\nu}$ 为无量纲的核矩阵元（Nuclear Matrix Element, NME）**。

**核物理学的决定性责任与瓶颈**：
即便未来深地探测器测得清晰的 $0\nu\beta\beta$ 峰值半衰期，若不能精确计算出初末态核之间的核矩阵元 $M^{0\nu}$，物理学界依然**无法将寿命转化为绝对中微子质量**！当前不同核多体模型（大壳模型 ISM、准粒子无规相位近似 QRPA、相互作用玻色子模型 IBM-2、能量泛函 EDF）给出的 $M^{0\nu}$ 存在近 2 倍的理论弥散，直接导致中微子质量提取带来高达 4 倍的物理不确定度。

---

## 2. 严格微观多体表述与中微子势算符

### (1) 核矩阵元 $M^{0\nu}$ 的算符分解
在电弱 $V-A$ 理论下，通过交换虚轻中微子，$0\nu\beta\beta$ 跃迁矩阵元分解为 Gamow-Teller 项（自旋翻转）、Fermi 项（同位旋标量）与张量项：
$$M^{0\nu} = M_{\text{GT}}^{0\nu} - \left( \frac{g_V}{g_A} \right)^2 M_{\text{F}}^{0\nu} + M_{\text{T}}^{0\nu}$$
其中轴矢量与矢量耦合常数比值 $g_V / g_A \approx 1 / 1.27$。
在核子空间坐标下，两体跃迁算符表示为对所有核子对的求和：
$$M_{\text{GT}}^{0\nu} = \langle 0_f^+ | \sum_{a, b} H_{\text{GT}}(r_{ab}, \bar{E}) (\vec{\sigma}_a \cdot \vec{\sigma}_b) \tau_a^- \tau_b^- | 0_i^+ \rangle$$
$$M_{\text{F}}^{0\nu} = \langle 0_f^+ | \sum_{a, b} H_{\text{F}}(r_{ab}, \bar{E}) \tau_a^- \tau_b^- | 0_i^+ \rangle$$

---

### (2) 闭合近似（Closure Approximation）与中微子虚势
由于传播的中间虚中微子动量极高（$q \sim 100 \sim 200\text{ MeV}/c$），远大于中间核态能级差（典型 $\Delta E \sim 2 \sim 5\text{ MeV}$），中间态激发能总和可应用**闭合近似**替换为一个平均能量 $\bar{E} \approx 8\text{ MeV}$。
中微子交换虚势在坐标空间退化为经典的库仑型中微子势：
$$H(r_{ab}, \bar{E}) = \frac{2 R_0}{\pi r_{ab}} \int_0^\infty \frac{j_0(q r_{ab}) q}{q + \bar{E}} dq \approx \frac{R_0}{r_{ab}}$$
其中 $R_0 = 1.2 A^{1/3}\text{ fm}$ 为核半径归一化标度。在包含核子有限大小偶极形状因子 $f(q^2) = (1 + q^2 / \Lambda^2)^{-2}$ 与核子短程排斥关联（Short-Range Correlation, SRC）后，势能奇点被平滑截断。

---

### (3) 轴矢量耦合常数 $g_A$ 的介质淬灭难题（$g_A$ Quenching）
这是当前核物理最具争议的问题之一：
由于衰变率严格按轴矢量常数的四次方标度：
$$\Gamma_{0\nu} \propto g_A^4 \cdot |M^{0\nu}|^2$$
- 自由核子下：$g_A = 1.27$；
- 若核介质多体关联导致 $g_A$ 发生剧烈淬灭（如某些单 $\beta$ 拟合给出的 $g_A \approx 1.0$ 甚至 $g_A \approx 0.8$），衰变寿命将被**虚假拉长 3 到 6 倍**！
因此，现代从头计算（Ab Initio）框架极力主张将两体流（Two-body currents）显式纳入有效算符中，而非粗暴整体淬灭 $g_A$。

---

## 3. 全球主力同位素物理参数与倒序质量谱探测基准

| 同位素 | 衰变能 $Q_{\beta\beta}$ (keV) | 相空间因子 $G_{0\nu}$ ($\text{yr}^{-1}$) | 理论 NME 范围 $[M_{\text{min}}, M_{\text{max}}]$ | 实验现状（90% C.L. 寿命下限） | 对应 $\langle m_{\beta\beta} \rangle$ 质量上限 (meV) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **$^{76}\text{Ge}$** | $2039.0$ | $2.36 \times 10^{-15}$ | $2.8 \sim 5.5$ | GERDA / LEGEND-200: $> 1.8 \times 10^{26}\text{ yr}$ | **$142 \sim 280\text{ meV}$** |
| **$^{136}\text{Xe}$** | $2457.8$ | $1.46 \times 10^{-14}$ | $1.5 \sim 4.2$ | KamLAND-Zen: $> 2.3 \times 10^{26}\text{ yr}$ | **$66 \sim 186\text{ meV}$** |
| **$^{130}\text{Te}$** | $2527.5$ | $1.42 \times 10^{-14}$ | $1.5 \sim 4.0$ | CUORE: $> 2.2 \times 10^{25}\text{ yr}$ | **$90 \sim 300\text{ meV}$** |
| **$^{100}\text{Mo}$** | $3034.4$ | $1.59 \times 10^{-14}$ | $2.5 \sim 6.0$ | CUPID-Mo: $> 1.8 \times 10^{24}\text{ yr}$ | **$280 \sim 500\text{ meV}$** |

**中微子质量谱系层级（Hierarchy Regimes）**：
1. **简并质量区（Degenerate Hierarchy, $\langle m_{\beta\beta} \rangle > 50\text{ meV}$）**：当前百公斤级实验已全面覆盖；
2. **倒序质量谱区（Inverted Hierarchy, $15\text{ meV} \le \langle m_{\beta\beta} \rangle \le 50\text{ meV}$）**：下一代吨级实验（LEGEND-1000, nEXO, CUPID）的核心目标（要求寿命灵敏度达到 $T_{1/2} > 10^{27} \sim 10^{28}\text{ yr}$）；
3. **正序质量谱区（Normal Hierarchy, $\langle m_{\beta\beta} \rangle < 15\text{ meV}$）**：未来终极多吨级前沿。

---

## 4. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/double_beta_decay_nme_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `dbd` 命令。

### 运行示范（以 $^{76}\text{Ge}$ 与 $^{136}\text{Xe}$ 当前实验下限进行反演）：
```bash
# 1. 76Ge 现状反演与倒序谱所需灵敏度预测
python3 system/scripts/analysis/nuclear_analyzer.py dbd --iso 76Ge --t12 1.8e26 --json

# 2. 136Xe 现状反演
python3 system/scripts/analysis/nuclear_analyzer.py dbd --iso 136Xe --t12 2.3e26
```

### 计算输出核心物理特征：
1. **$^{76}\text{Ge}$ 反演结果**：
   - 在当前世界纪录 $T_{1/2} > 1.8 \times 10^{26}\text{ yr}$ 下，名义有效马约拉纳质量上限为 $\langle m_{\beta\beta} \rangle < 196.0\text{ meV}$；
   - 考虑核矩阵元区间 $[2.8, 5.5]$，物理不确定度区间为 $[142.5, 280.0]\text{ meV}$，判定处于 `Degenerate_Mass_Regime`；
   - 若要完全彻底覆盖倒序质量谱（目标 $\langle m_{\beta\beta} \rangle = 20\text{ meV}$），计算预言下一代 LEGEND-1000 实验必须达到：
     $$T_{1/2} > 1.73 \times 10^{28}\text{ yr}$$
2. **$^{136}\text{Xe}$ 反演结果**：
   - 在 $T_{1/2} > 2.3 \times 10^{26}\text{ yr}$ 下，名义质量上限压低至 $\langle m_{\beta\beta} \rangle < 93.0\text{ meV}$；
   - 覆盖倒序谱所需寿命灵敏度为 $T_{1/2} > 4.97 \times 10^{27}\text{ yr}$，展现出极高的理论定量穿透力！

---

## 5. 与相关前沿概念的交叉引用
- [[quasiparticle-random-phase-approximation-qrpa-dynamics]]：pnQRPA 中的粒子-粒子相互作用参数 $g_{pp}$ 灵敏度正是此处双贝塔衰变矩阵元计算的核心微观内核；
- [[gamow-teller-resonance-ikeda-sum-rule-and-ga-quenching]]：Ikeda 求和定则与电荷交换反应对 $g_A$ 介质淬灭的测定，直接决定了此处 $g_A^4$ 寿命标度的理论上限；
- [[beta-decay-phase-space-log-ft-and-cvc-unitarity]]：单 $\beta$ 衰变相空间积分在此处推广为双轻子相空间因子 $G_{0\nu}$。
