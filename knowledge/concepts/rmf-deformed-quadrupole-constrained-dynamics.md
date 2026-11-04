---
type: concept
title: "相对论平均场（RMF）轴对称四极约束形变、NL3参数化与核电荷半径动力学"
aliases: [相对论平均场形变, RMF约束计算, NL3参数集, 四极约束势能曲线, 标量矢量势抵消, 中子皮形变, 形状共存极小]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
tags: [relativistic-mean-field, rmf, deformed-rmf, quadrupole-constraint, nl3-parameter-set, charge-radius, neutron-skin-deformation, potential-energy-curve]
---

# 相对论平均场（RMF）轴对称四极约束形变、NL3参数化与核电荷半径动力学

## Definition

### 物理全景：协变核多体自洽场中的宏观四极形变演化

在现代微观核结构理论中，**相对论平均场理论（Relativistic Mean Field, RMF）**以洛伦兹协变性、天然包含大自旋-轨道耦合力以及成功解释相对论饱和机制而著称。
根据 J. Boguta & A. R. Bodmer（Nucl. Phys. A 292, 413, 1977）、G. A. Lalazissis, J. Konig, & P. Ring（Phys. Rev. C 55, 540, 1997，NL3 参数集）以及孟杰《Relativistic Continuum Field Theory》：
在开壳层原子核（如 $A \approx 130$ 的 Ba, Ce 同位素）中，原子核往往偏离球形平均场，呈现自洽的轴对称四极变形（Prolate 长椭或 Oblate 扁椭）。

为了从微观泛函角度探索不同四极形变状态下的势能面结构，**四极约束自洽场方法（Quadrupole Constrained Self-Consistent RMF）**是无可替代的微观标准手段：
1. **强标量势与强矢量势的相对论抵消**：
   在核内部，核子与标量介子 $\sigma$ 耦合产生极深的吸引标量势（$S(\mathbf{r}) \approx -400\text{ MeV}$），与矢量介子 $\omega$ 耦合产生强烈的排斥矢量势（$V(\mathbf{r}) \approx +350\text{ MeV}$）。两者在狄拉克大分量中相消为净中心结合势（$V+S \approx -50\text{ MeV}$），而在小分量中相加形成巨大的自旋-轨道耦合场（$V-S \approx 750\text{ MeV}$），并使得核子在核介质中的有效狄拉克质量大幅下降至 $M^* / M \approx 0.60$；
2. **四极动量二次约束拉格朗日乘子**：
   通过在总能量泛函中引入四极矩偏离惩罚项 $\frac{1}{2} C_Q (\langle \hat{Q}_{20} \rangle - Q_0)^2$，强制约束自洽迭代收敛在任意指定的形变 $\beta_2$ 处，从而完整扫描出从扁椭（$\beta_2 < 0$）经球形鞍点（$\beta_2 = 0$）到长椭（$\beta_2 > 0$）的全域微观势能曲线 $E(\beta_2)$；
3. **同位旋矢量质子-中子形变差异（Deformation Neutron Skin）**：
   在丰中子核中，由于对称能和等标/等矢介子场空间分布不同，**中子四极形变 $\beta_{2n}$ 与质子四极形变 $\beta_{2p}$ 并不完全一致**，诱发核表面的空间同位旋极化。

---

## Necessary Assumptions

### 严格相对论物理方程与能量泛函推导

### (1) RMF 协变有效拉格朗日量密度
$$\mathcal{L} = \bar{\psi} \left[ i\gamma^\mu \partial_\mu - M - g_\sigma \sigma - g_\omega \gamma^\mu \omega_\mu - g_\rho \gamma^\mu \vec{\tau} \cdot \vec{\rho}_\mu - e \gamma^\mu \frac{1 - \tau_3}{2} A_\mu \right] \psi + \mathcal{L}_{\text{mesons}}$$
在静态轴对称基态平均场近似下，时间分量与空间对称导数保留：
- 有效狄拉克质量：$M^*(\mathbf{r}) = M + S(\mathbf{r}) = M - g_\sigma \sigma(\mathbf{r})$；
- 狄拉克旋量方程（大分量 $f_i$ 与小分量 $g_i$）：
  $$\begin{pmatrix} M^* + V & \vec{\sigma} \cdot \vec{p} \\ \vec{\sigma} \cdot \vec{p} & -M^* + V \end{pmatrix} \begin{pmatrix} f_i \\ g_i \end{pmatrix} = E_i \begin{pmatrix} f_i \\ g_i \end{pmatrix}$$

---

### (2) 四极约束算符与形变参数 $\beta_2$
固有内禀四极矩算符：
$$\hat{Q}_{20} = 2 z^2 - x^2 - y^2 = \sqrt{\frac{16\pi}{5}} r^2 Y_{20}(\theta, \phi)$$
质子四极矩 $\langle Q_{20}^p \rangle$ 与中子四极矩 $\langle Q_{20}^n \rangle$ 分别定义。
无量纲 Bohr 四极形变参数 $\beta_2$ 的标准换算：
$$\beta_2 = \sqrt{\frac{5}{16\pi}} \frac{4\pi \langle \hat{Q}_{20} \rangle}{3 A R_0^2}, \quad (R_0 = 1.2 A^{1/3}\text{ fm})$$
总约束哈密顿量为：
$$\langle H' \rangle = \langle H_{\text{RMF}} \rangle + \frac{1}{2} C_Q \left( \langle \hat{Q}_{20} \rangle - Q_0 \right)^2$$
通过连续调节约束目标 $Q_0$，自洽求解变分基态，输出结合能作为 $\beta_2$ 的平滑函数。

---

### (3) 均方电荷半径与中子皮形变厚度
由于有限大小质子电荷分布及自旋-轨道重整化：
$$R_{\text{ch}} = \sqrt{\langle r_p^2 \rangle + 0.64\text{ fm}^2}$$
中子皮厚度为：
$$\Delta r_{np} = \sqrt{\langle r_n^2 \rangle} - \sqrt{\langle r_p^2 \rangle}$$
在长椭极小处，质子与中子主轴半径分别沿 $z$ 轴延伸：$R_z = R_0 (1 + \sqrt{5/4\pi}\beta_2)$。

---

## Discriminating Observables

### 特征谱学观测量

## Supporting Evidence

### 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/rmf_deformed_constrained_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `rmfdef` 命令。

### 运行示范（以经典过渡核 $^{130}\text{Ba}$ 为例进行四极约束势能面扫描）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py rmfdef -Z 56 -A 130 --json
```

### 计算输出核心物理特征：
1. **相对论平均场参数**：
   - NL3 参数集下，有效核子质量比达到 $M^*/M = 0.595$（有效核子质量 $558.6\text{ MeV}$）；
   - 标量引力势 $S = -377.2\text{ MeV}$，矢量斥力势 $V = +307.9\text{ MeV}$，中心势阱净深为 $-69.3\text{ MeV}$；
   - 球形电荷半径 $R_{\text{ch}} = 5.409\text{ fm}$，中子皮厚度 $\Delta r_{np} = 0.111\text{ fm}$；
2. **形变极小与形状共存**：
   - 扫描得出全局能量最低点位于长椭极小 $\beta_2 = 0.50$ 处，具有深度结合（能量相比球形深 $-15.43\text{ MeV}$）；
   - 次极小出现在扁椭侧 $\beta_2 = -0.40$ 处（能量相对球形深 $-7.43\text{ MeV}$）；
   - 长椭与扁椭之间的能量劈裂为 $8.0\text{ MeV}$，球形鞍点势垒达到 $15.43\text{ MeV}$，从微观相对论场论角度给出了强形变驱动的决定性证据！

---


## Counter-evidence and Competing Interpretations

1. **模型适用边界与唯象近似**：微观壳模型、准粒子平均场与宏观转子模型在不同角动量与激发能区具有内在自由度截断；
2. **实验替代解释**：能级能量简并与电磁跃迁比值可能受到形状共存、非简谐声子振动及准粒子组态重组的竞争干扰。

## Our Current Position

本 Wiki 将该物理概念建立于自洽微观动力学与严格实验可观测量之上，作为解析与裁判前沿集体运动模式的标准科学基准。

## Sources

### 参考文献与交叉引用

- [[relativistic-mean-field-spin-orbit-and-pseudospin]]：球形 RMF 势阱与狄拉克赝自旋对称性在此处自然拓展为轴对称四极形变场；
- [[collective-quadrupole-pes-and-gamma-softness]]：微观 RMF 四极约束能量曲线为宏观 5D Bohr 集体哈密顿量提供了微观能量输入基准；
- [[nuclear-charge-radii-isotope-shifts-and-king-plot]]：形变产生的均方电荷半径增量直接反映在激光同位素移动实验测量中。
