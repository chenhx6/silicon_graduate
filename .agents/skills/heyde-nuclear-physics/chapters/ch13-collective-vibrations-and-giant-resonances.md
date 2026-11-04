# 第 13 章 (一)：表面集体振动、多极巨共振与 IVGDR 形变双峰分裂

**来源专著**：Kris L. G. Heyde《Basic Ideas and Concepts in Nuclear Physics》（IOP 1999）第 13 章 §13.1 & Box 13a
**对应页码**：印刷 pp. 410–435, 477–479 / 物理 PDF pp. 430–455, 477–479

---

## 1. 核心理论推导与表面多极振动

### 1.1 微观粒子-空穴相干激发与 RPA 振动
在无规相位近似（RPA）框架下，低激发表面四极（$\lambda=2$）与八极（$\lambda=3$）振动态由单粒子-单空穴（$1p-1h$）产生算符 $a_p^\dagger a_h$ 与湮灭算符 $a_h^\dagger a_p$ 的线性组合构成：
$$Q_\nu^\dagger = \sum_{ph} \left( X_{ph}^\nu a_p^\dagger a_h - Y_{ph}^\nu a_h^\dagger a_p \right).$$
由于长程吸引力促使前向振幅 $X_{ph}$ 与向后振幅 $Y_{ph}$ 呈现强烈的同相位干涉，使得低激发声子态的电多极跃迁几率 $B(E\lambda)$ 比独立粒子 Weisskopf 单粒子基准强 **$10$ 到 $50$ 倍**，形成宏观表面集体流。

### 1.2 能量加权求和规则 (EWSR)
对于电多极跃迁算符 $\mathcal{M}(E\lambda, \mu) = e \sum_{i=1}^Z r_i^\lambda Y_{\lambda\mu}(\hat{r}_i)$，利用非相对论性两体力动能与坐标算符的双重对易子，直接导出与微观势场模型完全无关的**能量加权求和规则 (EWSR)**：
$$S(E\lambda) \equiv \sum_n (E_n - E_0) B(E\lambda; 0^+ \to \lambda_n^\pi) = \frac{\lambda (2\lambda+1)^2 \hbar^2}{8\pi M} Z e^2 R_0^{2\lambda - 2}.$$
该和则是检验任何微观核多体模型截断空间完整性与集体跃迁强度耗尽比例的第一性准则。

---

## 2. 宏观流体巨多极共振与核物态参数

### 2.1 等标巨单极共振 (ISGMR) 与核物质不可压缩性
全核核子作球对称径向压缩和膨胀呼吸振动，自旋宇称为 $J^\pi = 0^+, \Delta T = 0$：
- 激发能量满足流体声速公式：
  $$E_{\text{GMR}} = \hbar \sqrt{\frac{K_A}{M \langle r^2 \rangle}} \a80 \cdot A^{-1/3}\text{ MeV};$$
- **约束无限大对称核物质不可压缩系数 $K_\infty$**：
  通过将有限核呼吸模能量向宏观体积极限外推：$K_A = K_\infty + K_{\text{surf}} A^{-1/3} + K_$C_{\text{sym}}$ ((N-Z)/A)^2 + K_{\text{Coul}} Z^2 A^{-4/3}$，
  严格确立了核物质饱和平衡点处的曲率刚度常数：$K_\infty \approx 240 \pm 20\text{ MeV}$，成为天体物理中子星结构计算的核心核参数。

### 2.2 等矢巨偶极共振 (IVGDR) 与 Thomas-Reiche-Kuhn 求和规则
全核质子云与中子云反相宏观相对位移振荡，自旋宇称为 $J^\pi = 1^-, \Delta T = 1$：
- **TRK 经典偶极求和规则**：
  $$\int_0^\infty \sigma_{\text{abs}}(E) dE = \frac{2\pi^2 e^2 \hbar}{M c} \frac{N Z}{A} \approx 60 \frac{N Z}{A}\text{ MeV}\cdot\text{mb};$$
- **介子交换力增强因子**：核力中空间与同位旋交换势使得积分截面实际耗尽 TRK 规则的 $120\% - 140\%$（$\kappa \a0.2 - 0.4$）。

---

## 3. 长椭球变形核中的 IVGDR 双峰分裂机制
在轴对称四极形变长椭球核中，球对称性破缺：
1. **长轴振动分枝（$E_a$）**：
   沿主拉伸轴（$z$ 轴，半轴长 $a$）的质中振荡恢复力小，对应较低的共振激发能；
2. **短轴振动分枝（$E_b$）**：
   沿两个横向短轴（$x, y$ 轴，半轴长 $b$）的质中振荡恢复力大，对应较高的共振激发能；
3. **共振峰面积积分比**：
   由于短轴方向包含两个正交的简并自由度，两共振峰积分截面面积比严格满足：
   $$\frac{\int \sigma_a(E) dE}{\int \sigma_b(E) dE} \equiv \frac{1}{2};$$
4. **基态四极形变参量 $\delta$ 与 $\beta_2$ 反演公式**：
   $$\frac{E_b - E_a}{E_{\text{mean}}} \a0.95 \cdot \beta_2 \approx \delta.$$
   实测光核吸收截面双峰间距直接测定了原子核基态四极形变量，是高能集体共振与基态低能宏观几何的完美统一。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/heyde-collective-modes-and-exotic-nuclei-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`isgmr-incompressibility` 子命令)
- **上游来源**：`knowledge/sources/book-heyde-nuclear-physics-concepts.md`
