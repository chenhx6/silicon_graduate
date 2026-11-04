# 第 11 章：电磁多极场量子化、辐射跃迁几率与 Weisskopf 基准

**来源专著**：W. D. Hamilton《The Electromagnetic Interaction in Nuclear Spectroscopy》（1975）第 11 章
**对应页码**：印刷 pp. 441–504 / 物理 PDF pp. 441–504

---

## 1. 核心理论推导与麦克斯韦多极场量子化

### 1.1 电多极与磁多极向量势展开
辐射电磁场满足真空中齐次波动方程。在球坐标系下，电多极场 $\vec{A}_{LM}^{(E)}$ 与磁多极场 $\vec{A}_{LM}^{(M)}$ 通过规范不变的电磁场算符展开：
$$\vec{A}_{LM}^{(M)}(\vec{r}) = - \frac{1}{\sqrt{L(L+1)}} (\vec{r} \times \nabla) [j_L(k r) Y_{LM}(\hat{r})],$$
$$\vec{A}_{LM}^{(E)}(\vec{r}) = - \frac{i}{k \sqrt{L(L+1)}} \nabla \times (\vec{r} \times \nabla) [j_L(k r) Y_{LM}(\hat{r})].$$
- **宇称选择定则**：
  - 电多极场（$EL$）的内禀空间宇称为：$\pi(EL) = (-1)^L$；
  - 磁多极场（$ML$）的内禀空间宇称为：$\pi(ML) = (-1)^{L+1}$；
  - 核初态 $\pi_i$ 与终态 $\pi_f$ 满足：$\pi_i \cdot \pi_f = \pi(\sigma L)$。宇称不改变时允许 $E2, M1, E4, M3 \dots$；宇称改变时允许 $E1, M2, E3, M4 \dots$。

### 1.2 长波近似下的电磁多极多极矩算符
在低能核物理中，跃迁 $\gamma$ 射线能量通常 $E_\gamma \le 5\text{ MeV}$，光子波长 $\lambda = \hbar c / E_\gamma \ge 40\text{ fm}$ 远大于原子核半径（$R_0 \approx 5 - 7\text{ fm}$），满足极其精准的**长波近似 (Long-Wavelength Approximation, $k R \ll 1$)**：
Bessel 球函数近似展开为 $j_L(kr) \approx \frac{(kr)^L}{(2L+1)!!}$。
1. **电多极矩算符 (Electric Multipole Operator)**：
   $$\mathcal{M}(EL, M) = \sum_{i=1}^A e_i r_i^L Y_{LM}(\hat{r}_i);$$
2. **磁多极矩算符 (Magnetic Multipole Operator)**：
   $$\mathcal{M}(ML, M) = \mu_N \sum_{i=1}^A \left[ \frac{2}{L+1} g_l^{(i)} \vec{l}_i + g_s^{(i)} \vec{s}_i \right] \cdot \nabla [r_i^L Y_{LM}(\hat{r}_i)].$$

---

## 2. 约化跃迁几率 $B(\sigma L)$ 与 Weisskopf 单粒子单位标度

### 2.1 跃迁几率与约化矩阵元
从初态 $|I_i M_i\rangle$ 到终态 $|I_f M_f\rangle$ 的总辐射跃迁率：
$$T(\sigma L) = \frac{8\pi (L+1)}{L [(2L+1)!!]^2} \frac{k^{2L+1}}{\hbar} B(\sigma L; I_i \to I_f),$$
其中约化跃迁几率（Reduced Transition Probability）：
$$B(\sigma L; I_i \to I_f) = \frac{1}{2I_i + 1} |\langle I_f || \mathcal{M}(\sigma L) || I_i \rangle|^2.$$

### 2.2 Weisskopf 单粒子估计单位 ($W.u.$)
假设单个质子在半径为 $R_0 = 1.2 A^{1/3}\text{ fm}$ 的球形方势阱中发生单核子跃迁，径向积分取极端上限：
1. **Weisskopf 电跃迁单位**：
   $$B_{\text{W}}(EL) = \frac{1}{4\pi} \left( \frac{3}{L+3} \right)^2 e^2 R_0^{2L} \approx \frac{1.2^{2L}}{4\pi} \left( \frac{3}{L+3} \right)^2 A^{2L/3}\ e^2\text{fm}^{2L};$$
   - **四极 $B_{\text{W}}(E2)$**：$B_{\text{W}}(E2) = 0.05940 \cdot A^{4/3}\ e^2\text{fm}^4 = 5.940 \times 10^{-6} \cdot A^{4/3}\ e^2\text{b}^2$；
2. **Weisskopf 磁跃迁单位**：
   $$B_{\text{W}}(ML) = \frac{10}{\pi} \left( \frac{3}{L+3} \right)^2 \mu_N^2 R_0^{2L-2} \approx \frac{10 \times 1.2^{2L-2}}{\pi} \left( \frac{3}{L+3} \right)^2 A^{(2L-2)/3}\ \mu_N^2\text{fm}^{2L-2};$$
   - **偶极 $B_{\text{W}}(M1)$**：$B_{\text{W}}(M1) = \frac{10}{\pi} \left(\frac{3}{4}\right)^2 \mu_N^2 = \frac{90}{16\pi} \mu_N^2 \a1.790\ \mu_N^2$。

---

## 3. 在束谱学应用：集体增强与多极阻碍裁决
在实验能级寿命测定中：
- **集体转动增强**：若实测 $B(E2) \sim 50 - 200\text{ W.u.}$，证明大量价核子协同相干参与宏观形变转动，彻底排除纯单粒子跃迁；
- **单粒子阻碍与 $K$ 禁戒**：若实测 $B(E2) \sim 10^{-3} - 10^{-6}\text{ W.u.}$，预示存在高阶空间投影量子数禁戒（$K$-Isomer）或严重的球形组态阻碍。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/hamilton-angular-distribution-dco-polarization-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`alaga-transition` 子命令)
- **上游来源**：`knowledge/sources/book-hamilton-electromagnetic-interaction.md`
