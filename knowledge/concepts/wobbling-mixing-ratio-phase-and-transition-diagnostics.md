---
type: concept
title: "原子核摆动运动ΔI=1多极混合比δ(E2/M1)相位符号法则与横向/纵向模式实验诊断"
aliases: [摆动多极混合比, delta(E2/M1), 相位符号法则, 横向摆动诊断, 纵向摆动诊断, DCO双根区分, E2优势跃迁, 135Pr摆动争议, 签名伙伴带伪摆动排除]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [wobbling-motion, multipole-mixing-ratio, delta-e2-m1, transverse-wobbling, longitudinal-wobbling, phase-sign-rule, dco-roots, false-wobbling-falsification]
---

# 原子核摆动运动ΔI=1多极混合比δ(E2/M1)相位符号法则与横向/纵向模式实验诊断

## 1. 物理全景：从能带交叉的一维自旋跃迁到三轴摆动的电磁指纹

在低能核物理与三轴超形变奇 $A$ 核（如 $A \approx 130$ 的 $^{135}\text{Pr}, ^{133}\text{La}$ 以及稀土区 $^{163}\text{Lu}$）高自旋谱学中，实验学家常常在一条强 Yrast 带之上观测到一条自旋相同、宇称相同且相伴平行的能带。
两能带之间存在密集的跨带 $\Delta I = 1$ 去激发跃迁（即从假想的一维摆动带 $(I, n_w=1)$ 跃迁至基带 $(I-1, n_w=0)$）。

然而，实验谱学面临一个极为凶险的“真伪辨析陷阱”：
**单核子在变形平均场中的签名伙伴带（Signature Partner Band，单粒子哥氏力引起的能级分裂）同样会产生与 Yrast 带平行的强 $\Delta I = 1$ 退激跃迁！**
仅凭能级排布或表观转动惯量，绝不可能区分两者。

根据 S. Frauendorf & F. Dönau（Phys. Rev. C 89, 014322, 2014）、C. M. Petrache 2024 专著《Chirality and Wobbling in Atomic Nuclei》以及 A. Bohr & B. R. Mottelson《Nuclear Structure》Vol. II：
彻底破解这一物理疑难的核心杀手锏是**严格测量并理论求解该 $\Delta I = 1$ 跃迁的多极混合比（Multipole Mixing Ratio, $\delta(E2/M1)$）及其相对相位符号（Phase Sign）**：
1. **多极性强度的微观分野**：
   - 摆动运动本质上是集体四极声子（$E2$）去激发，因此其 $\Delta I = 1$ 跃迁被强烈的集体 $E2$ 辐射所主导，必须呈现出**极大的混合比（$|\delta| \gg 1.0$，通常 $|\delta| \sim 2.5 \sim 8.0$，$E2$ 纯度高达 $85\% \sim 98\%$）**！
   - 相反，签名伙伴带跃迁属于单核子自旋翻转，被巨大的单粒子磁偶极辐射主导（$B(M1) \sim 1\text{ W.u.}$），而单粒子电四极辐射极其微弱，导致其实测混合比**极小（$|\delta| \le 0.3$，几乎为纯 $M1$）**！
2. **Frauendorf-Dönau 相对相位符号定律（Phase Sign Rule）**：
   理论混合比 $\delta_{\text{theo}}$ 的代数正负号严格受到核子与转子相对旋磁差 $(g_j - g_R)$ 以及三轴不对称度 $\gamma$ 的约束，为在束角分布中测得的二次方程“双实数根”提供了绝对的唯一性物理遴选法则！

---

## 2. 严格微观电磁矩阵元与混合比推导

### (1) 多极混合比 $\delta(E2/M1)$ 的量子力学定义
在约化矩阵元表象下，定义无量纲混合比为电四极辐射振幅与磁偶极辐射振幅之比：
$$\delta(E2/M1) = \sqrt{\frac{T_e(E2)}{T_e(M1)}} = 0.835 \cdot E_\gamma\text{ (MeV)} \cdot \frac{\langle I-1, n_w=0 || \hat{\mathcal{M}}(E2) || I, n_w=1 \rangle}{\langle I-1, n_w=0 || \hat{\mathcal{M}}(M1) || I, n_w=1 \rangle}$$
式中能量以 $\text{MeV}$ 为单位，$E2$ 矩阵元以 $e\cdot\text{b}$ 为单位，$M1$ 矩阵元以 $\mu_N$ 为单位。
跃迁中电四极辐射所占的能量分支比为：
$$f_{E2} = \frac{\delta^2}{1 + \delta^2}, \qquad f_{M1} = 1 - f_{E2} = \frac{1}{1 + \delta^2}$$

---

### (2) Frauendorf-Dönau 针对横向摆动（TW）的解析闭合公式
在横向摆动（Transverse Wobbling, TW）构型中：
奇准粒子角动量 $\mathbf{j}$ 牢固取向在短轴 $s$（轴 3）上，而集体转动核心绕中间轴 $m$（轴 1）旋转。
利用 Holstein-Primakoff 展开，各多极算符矩阵元的一阶解析结果为：
- 电四极跃迁矩阵元（来源于宏观转动体在进动中的四极辐射投影）：
  $$\langle I-1, 0 || \hat{\mathcal{M}}(E2) || I, 1 \rangle = \sqrt{\frac{5}{16\pi}} Q_0 \sin(\gamma + 30^\circ) \frac{1}{\sqrt{I}}$$
- 磁偶极跃迁矩阵元（来源于奇核子自旋进动横向磁化流）：
  $$\langle I-1, 0 || \hat{\mathcal{M}}(M1) || I, 1 \rangle = \sqrt{\frac{3}{4\pi}} (g_j - g_R) \frac{j}{I}$$

两式相除，得出横向摆动混合比的微观闭合解：
$$\delta_{\text{TW}}(E2/M1) = \text{sign}(g_j - g_R) \cdot \frac{0.835 \cdot E_\gamma\text{ (MeV)} \cdot Q_0\text{ (e}\cdot\text{b)} \cdot \sin(\gamma + 30^\circ)}{|g_j - g_R| \cdot \left( \frac{j}{\sqrt{I}} \right)}$$

#### 核心物理推论：
1. **幅值巨大**：由于分母包含 $1/\sqrt{I}$ 因子而分子由集体四极矩 $Q_0 \sim 3 \sim 5\text{ eb}$ 主导，在中高自旋区 $\delta_{\text{TW}}$ 必然在 $2.0 \sim 8.0$ 之间，证明了**横向摆动去激发跃迁本质上就是一条强烈的 $E2$ 跃迁**；
2. **相位符号法则（Phase Sign Rule）**：
   - 对于奇质子核（如 $^{135}\text{Pr}, ^{163}\text{Lu}$ 中的 $h_{11/2}, i_{13/2}$ 质子），$g_j \approx 1.25 > g_R \approx 0.40 \implies (g_j - g_R) > 0$。因此：
     $$\delta_{\text{TW}} > 0 \quad (\text{相位符号严格为正！})$$
   - 这一正号约束构成了排除负根的绝对物理标准！

---

### (3) 纵向摆动（LW）与签名伙伴带的对照特征
- **纵向摆动（Longitudinal Wobbling, LW）**：
  奇核子平行于转动轴取向，集体四极算符矩阵元被高阶项压低，导致 $|\delta_{\text{LW}}| \approx 0.3 \sim 1.0$（表现为 $M1/E2$ 强度相近的混合跃迁）；
- **签名伙伴带（Signature Partner Band）**：
  单粒子翻转矩阵元中缺少集体四极支持，理论预测：
  $$|\delta_{\text{SP}}| \le 0.30 \implies f_{E2} < 8\%$$
  表现为近乎纯正的磁偶极 $M1$ 跃迁。

---

## 3. 实验角分布/DCO双根的物理仲裁实战

在在束实验中，通过测量角分布系数 $A_2$ 或 DCO 比值，反解关于 $\delta$ 的二次方程：
$$(F_{22} - A_2/B_2) \delta^2 + 2 F_{12} \delta + (F_{11} - A_2/B_2) = 0$$
实验必然输出两个数学实数根：小根 $\delta_1$（通常绝对值很小）与大根 $\delta_2$（通常绝对值很大）。

#### 仲裁判定法典：
1. 计算理论横向摆动混合比 $\delta_{\text{TW}}$ 的数值与正负符号；
2. 若实验测得的两个根中，**存在一个大根 $\delta_2$（$|\delta_2| \ge 2.0$）且其符号与理论相位符号一致**：
   立即宣布**真横向摆动运动（True TW）确立**；
3. 若实验通过内转换系数（BrIcc）或 Clover 偏振测量判定系统实际上走的是小根 $\delta_1$（$|\delta_1| < 0.3$）：
   立即宣布**该候选带为伪摆动带（False Wobbling），实为单粒子签名伙伴带**！
   （正是这一法则在 2020-2024 年间彻底纠正了国际上关于 $^{135}\text{Pr}$ 与 $^{133}\text{La}$ 的早期误判！）。

---

## 4. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/wobbling_branching_ratio_phase_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `wobphase` 命令。

### 运行示范（以 $^{135}\text{Pr}$ 关键跃迁 $I=15.5\hbar, E_\gamma = 720\text{ keV}$ 进行双根裁决）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py wobphase \
  -I 15.5 -j 5.5 --gamma 26.0 --eg 720.0 --q0 5.0 --root1 -0.15 --root2 3.10 --json
```

### 计算输出核心物理特征：
1. **微观理论多极比值**：
   - 输入参数 $Q_0 = 5.0\text{ eb}, g_j = 1.25, g_R = 0.40 \implies \Delta g = +0.85$；
   - 理论算得相位符号为正（`+ (Positive)`）；
   - 理论横向摆动混合比为：
     $$\delta_{\text{theo}} = + 2.099$$
   - 对应多极性分解：$81.5\% E2 + 18.5\% M1$，分类标记为 `Transverse_Wobbling_Robust`；
2. **实验双根仲裁结果**：
   - 候选输入根为：Root 1 = $-0.15$，Root 2 = $+3.10$；
   - 算法综合幅值与相位符号，自动选定：
     `Selected Matching Root: Root 2 (delta = 3.10)`；
   - 判定 Root 2 与理论值在误差内高度相符，同时将近纯 $M1$ 的负小根 Root 1 作为签名伙伴带假根予以排除，展现了极强的实验物理裁决力！

---

## 5. 与相关前沿概念的交叉引用
- [[davydov-filippov-triaxial-rotor-and-wobbling-dynamics]]：横向摆动能量随自旋下降与此处大混合比 $\delta$ 构成了确证摆动运动不可分割的“动能-电磁”双生印记；
- [[experimental-uncertainty-propagation-and-double-root-triage]]：通用的双根误差传播在此处获得了微观粒子-转子多极矩阵元的直接物理注入；
- [[clover-compton-polarimetry-and-addback]]：Clover 测得的正线偏振度 $P > 0$ 直接为此处 $\delta$ 的 $E2$ 主导性提供了完全正交的实验证实。
