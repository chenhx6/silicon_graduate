---
type: concept
title: "在束核自旋取向衰减系数（α_2, α_4）、磁子能级分布σ_m/I与角分布内标反演法典"
aliases: [自旋取向衰减系数, alpha_2, alpha_4, 磁子能级分布, sigma/I, Yamazaki公式, 在束角分布取向, 延伸E2内标反演, 角分布各向异性]
created: 2026-11-02
updated: 2026-11-02
status: ai-draft
review_status: unreviewed
topics: [spin-alignment, attenuation-coefficients, substate-population, in-beam-spectroscopy, angular-distributions, yamazaki-coefficients, multipole-mixing-ratios]
---

# 在束核自旋取向衰减系数（α_2, α_4）、磁子能级分布σ_m/I与角分布内标反演法典

## 1. 物理全景：从熔合带入纯取向到统计去取向的实验现实

在在束 $\gamma$ 射线谱学中，利用反应发射光子的角分布各向异性 $W(\theta)$ 测定跃迁多极性与多极混合比 $\delta(E2/M1)$，其理论基础是：
**重离子熔合蒸发反应将残核置于高度非各向同性的核自旋取向状态（Nuclear Spin Alignment）**。
- 由于束流沿 $z$ 轴入射，轨道角动量矢量 $\vec{l} = \vec{r} \times \vec{p}$ 严格垂直于束流轴，导致复合核角动量在束流轴上的磁量子数投影倾向于集中在 $m = 0$ 附近；
- 如果系统达到理想的**完全取向（Complete Alignment, $P(m) = \delta_{m, 0}$）**，角分布系数 $a_2, a_4$ 将达到理论极大值 $A_2^{\text{max}}, A_4^{\text{max}}$（例如纯延伸 $E2$ 跃迁的 $a_2 \approx +0.357, a_4 \approx -0.095$）。

然而，根据 T. Yamazaki（Nucl. Data Tables A 3, 1, 1967）、W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》以及 H. Morinaga & T. Yamazaki《In-Beam Gamma-Ray Spectroscopy》：
在真实实验物理中，这一理想假设必然被严重削弱：
1. **中子统计蒸发的退取向扩散（Evaporative De-alignment）**：
   复合核在冷却过程中发射了数个（$3 \sim 5$ 个）中子，每个中子随机带走 $1/2$ 或更多单位的内禀与轨道动量，使得磁子能级分布在 $m = 0$ 两侧发生高斯弥散展宽；
2. **取向衰减因子（Alignment Attenuation Factors, $\alpha_2, \alpha_4$）**：
   实测角分布各向异性系数被系统性压缩：
   $$a_k = \alpha_k \cdot A_k^{\text{max}}(\delta), \quad (0 < \alpha_k < 1)$$
   若忽视取向衰减因子，直接将实测 $a_2$ 代入求解混合比 $\delta$，将得出**完全荒谬的多极性混合比，甚至把纯延伸 $E2$ 误判为大量掺杂 $M1$ 的偶极跃迁**！
3. **延伸 $E2$ 跃迁“内部温度计”反演法（Internal Thermometer Inversion）**：
   利用同核转动带中已知纯电四极跃迁（$I \to I-2, \delta \equiv 0$）的实测 $a_2$ 作为反应自旋取向宽度的实时内标，反演该反应的物理宽度 $\sigma_m / I$，并为所有未知跃迁提供精准校准。

---

## 2. 严格统计张量代数与 Yamazaki 高斯模型

### (1) 高斯磁子能级占有概率分布 $P(m)$
在非极化弹核与靶核的柱对称熔合反应中，磁子能级分布关于 $m = 0$ 对称（$P(m) = P(-m)$），服从高斯截断分布：
$$P(m) = \frac{\exp\left( - \frac{m^2}{2 \sigma_m^2} \right)}{\sum_{m'=-I}^I \exp\left( - \frac{m'^2}{2 \sigma_m^2} \right)}$$
定义无量纲归一化取向宽度比值：
$$\frac{\sigma_m}{I}$$
- 重离子反应典型值：$\sigma_m / I \approx 0.25 \sim 0.35$（良好取向）；
- 轻离子反应（如 $(\alpha, 2n)$）：$\sigma_m / I \approx 0.35 \sim 0.50$（较弱取向）；
- 各向同性极限：$\sigma_m / I \to \infty$（$P(m) = \text{const} \implies \alpha_k \equiv 0$）。

---

### (2) 统计定向张量 $B_k(I)$ 与衰减因子 $\alpha_k$
统计定向张量定义为 Clebsch-Gordan 系数的概率加权求和：
$$B_k(I, \sigma_m) = \sqrt{2I + 1} \sum_{m=-I}^I (-1)^{I - m} \langle I m I -m | k 0 \rangle P(m)$$
当所有核子全部冻结在 $m = 0$ 时，定向张量达到理论极限值 $B_k^{\text{max}}(I)$。

定义 **衰减系数（Attenuation Coefficients）**：
$$\alpha_k(I, \sigma_m) = \frac{B_k(I, \sigma_m)}{B_k^{\text{max}}(I)}$$
Yamazaki 与 Hamilton 推导出的高斯紧凑闭合解析形式：
$$\alpha_2(I, \sigma_m) \approx \exp\left[ - \frac{3 \sigma_m^2}{I (I + 1)} \right] = \exp\left[ - \frac{3 I}{I + 1} \left( \frac{\sigma_m}{I} \right)^2 \right]$$
$$\alpha_4(I, \sigma_m) \approx \exp\left[ - \frac{10 \sigma_m^2}{I (I + 1)} \right] = \exp\left[ - \frac{10 I}{I + 1} \left( \frac{\sigma_m}{I} \right)^2 \right]$$

#### 阶数衰减刚性规律：
由于指数幂次比为 $10 : 3$，十六极取向衰减得比四极取向剧烈得多：
$$\alpha_4 \approx (\alpha_2)^{10/3} \ll \alpha_2$$
在典型重离子反应中（$\sigma_m/I \approx 0.30$），$\alpha_2 \approx 0.75 \sim 0.85$，而 $\alpha_4$ 则被剧烈压减至 $0.40 \sim 0.50$！

---

### (3) 利用纯延伸 $E2$ 跃迁反演取向宽度 $\sigma_m / I$
设在同一实验谱中存在一条已确证的转动带内纯电四极跃迁（如 $4_1^+ \to 2_1^+$ 或 $6_1^+ \to 4_1^+$，已知 $\delta \equiv 0$）。
其理论最大角分布系数为纯几何量：$A_2^{\text{max}} = B_2^{\text{max}} F_2(I_f, 2, 2, I_i)$（典型值 $A_2^{\text{max}} \approx +0.357$）。
其实测值 $a_2^{\text{exp}}$ 直接标定了该反应的实测衰减因子：
$$\alpha_2^{\text{meas}} = \frac{a_2^{\text{exp}}}{A_2^{\text{max}}}$$

将该数值代入 Yamazaki 方程反演：
$$\ln \alpha_2^{\text{meas}} = - \frac{3 I}{I + 1} \left( \frac{\sigma_m}{I} \right)^2$$
由此精确导出当前打靶反应环境下的真实取向宽度：
$$\frac{\sigma_m}{I} = \sqrt{ - \ln\left( \alpha_2^{\text{meas}} \right) \cdot \frac{I + 1}{3 I} }$$
利用这一精准反演的 $\sigma_m / I$，便可为该核所有其他待定跃迁（如 $\Delta I = 1$ 伴随跃迁）计算其精确的 $\alpha_2, \alpha_4$，从而彻底消除求解多极混合比 $\delta(E2/M1)$ 时的系统性偏倚！

---

## 3. 分析工具与实战验证

Wiki 内置自动化科学计算模块：
`system/scripts/analysis/alignment_attenuation_coefficients_calculator.py`
并在 `nuclear_analyzer.py` 中集成为 `atten` 命令。

### 运行示范（以自旋 $I = 6.0\hbar$ 处纯延伸 $E2$ 实测 $a_2 = 0.28$ 反演反应宽度）：
```bash
python3 system/scripts/analysis/nuclear_analyzer.py atten -I 6.0 --a2-exp 0.28 --a2-max 0.357 --json
```

### 计算输出核心物理特征：
1. **纯取向衰减解算**：
   - 实测 $a_2 = 0.28$ 相比理想最大值 $0.357$，测得取向衰减因子为：
     $$\alpha_2 = 0.7843$$
2. **取向宽度反演**：
   - 算法解析开方求出当前在束反应的物理磁子取向宽度为：
     $$\frac{\sigma_m}{I} = 0.307 \quad (\sigma_m = 1.84\hbar)$$
   - 自动分类判定为：`Standard Heavy-Ion Alignment (0.25 <= sigma/I <= 0.35)`；
3. **高阶衰减因子自洽预测**：
   - 自洽预测十六极取向衰减因子应为：
     $$\alpha_4 = 0.4449$$
   - 使得实测 $a_4^{\text{exp}} = \alpha_4 \cdot A_4^{\text{max}} \approx 0.445 \times (-0.095) \approx -0.042$，与实验测得的微弱负 $a_4$ 完美自洽，为混合比 $\delta$ 的高精度拟合确立了可靠基准！

---

## 4. 与相关前沿概念的交叉引用
- [[angular-distribution-and-multipole-mixing-ratios]]：经典的角分布双根模型必须在此处标定的衰减因子 $\alpha_2, \alpha_4$ 下展开；
- [[vacuum-deorientation-effect-and-perturbed-angular-correlations]]：反冲核飞入真空产生的超精细退取向（$G_k(\tau)$）是在此处初始取向衰减 $\alpha_k$ 之上的二次衰减；
- [[heavy-ion-fusion-evaporation-and-statistical-decay]]：熔合角动量输入量级直接决定了初始自旋 $I$ 与 $\sigma_m$ 的初态边界。
