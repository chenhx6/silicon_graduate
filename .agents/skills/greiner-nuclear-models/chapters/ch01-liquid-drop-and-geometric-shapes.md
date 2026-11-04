# 第 1 章：液滴模型、表面形变几何与多极谐波展开

**来源专著**：Walter Greiner & Joachim A. Maruhn《Nuclear Models》（Springer 1996）第 1、6 章
**对应页码**：印刷 pp. 1–32, 106–117 / 物理 PDF pp. 17–48, 125–136

---

## 1. 核心理论推导与表面形变几何

### 1.1 原子核可变形表面的球谐展开
在宏观液滴图像下，假定原子核表面边界由质心到表面的半径矢量 $R(\theta, \phi)$ 唯一确定。由于核力具有短程饱和性，原子核表面为一封闭光滑曲面，在球谐函数 $Y_{\lambda\mu}(\theta, \phi)$ 基底上展开：
$$R(\theta, \phi) = R_0 \left[ 1 + \alpha_{00} + \sum_{\lambda=1}^\infty \sum_{\mu=-\lambda}^\lambda \alpha_{\lambda\mu}^* Y_{\lambda\mu}(\theta, \phi) \right],$$
其中：
- $\lambda = 0$ 对应单极呼吸形变（受核物质不可压缩性严格约束）；
- $\lambda = 1$ 对应质心平移偶极位移（在质心固定参考系中，恒有 $\alpha_{1\mu} \equiv 0$）；
- $\lambda = 2$ 对应四极表面形变（低能核集体运动的主导自由度，包含 5 个复数分量 $\alpha_{2\mu}$）；
- $\lambda = 3$ 对应八极梨形宇称破缺形变（包含 7 个复数分量 $\alpha_{3\mu}$）。

### 1.2 核物质不可压缩性与体积守恒约束
核物质饱和密度要求原子核在发生形变时的体积 $V$ 严格保持不变：
$$V = \frac{1}{3} \int R^3(\theta, \phi) d\Omega \equiv \frac{4\pi}{3} R_0^3.$$
代入展开式并保留至形变振幅的二阶微扰小量，直接导出单极收缩系数 $\alpha_{00}$：
$$\alpha_{00} = -\frac{1}{\sqrt{4\pi}} \sum_{\mu=-2}^2 |\alpha_{2\mu}|^2 = -\frac{1}{\sqrt{4\pi}} \beta^2.$$
该式表明：当原子核发生任何非零四极形变（$\beta > 0$）时，球形基准半密度半径必须发生向内的微小收缩，以严格保持全核总核子数与体积守恒。

---

## 2. 内禀主轴坐标系与 Hill-Wheeler 形变参数 $(\beta, \gamma)$

五维四极多极张量 $\alpha_{2\mu}$ 包含 5 个自由度。在空间经过三维 Euler 角 $(\theta_1, \theta_2, \theta_3)$ 旋转至核体固主轴参考系（使得非对角惯性积为零）后，剩余 2 个独立的内禀形状参量 $a_0$ 与 $a_2$（满足 $a_2 = a_{-2}, a_1 = a_{-1} = 0$）。
- **Hill-Wheeler 极坐标变换**：
  $$a_0 = \beta \cos\gamma, \quad a_2 = a_{-2} = \frac{1}{\sqrt{2}} \beta \sin\gamma;$$
- **不变量与二次曲面主轴半轴长**：
  总四极形变量由张量不变量严格定义：$\sum_{\mu} |\alpha_{2\mu}|^2 = a_0^2 + 2 a_2^2 = \beta^2$。
  核表面在内禀系中的三主轴半轴伸长量为：
  $$\delta R_k = R(\text{axis } k) - R_0 = \sqrt{\frac{5}{4\pi}} R_0 \beta \cos\left(\gamma - \frac{2\pi}{3} k\right) \quad (k = 1, 2, 3).$$
- **主轴几何图景**：
  1. **$\gamma = 0^\circ$（长椭球 Prolate）**：$\delta R_3 = +\sqrt{\frac{5}{4\pi}} R_0 \beta > 0$，$\delta R_1 = \delta R_2 = -\frac{1}{2}\sqrt{\frac{5}{4\pi}} R_0 \beta < 0$；原子核沿 $z$ 轴拉长，横截面为圆形；
  2. **$\gamma = 60^\circ$（扁椭球 Oblate）**：$\delta R_1 = +\sqrt{\frac{5}{4\pi}} R_0 \beta > 0$，$\delta R_2 = \delta R_3 = -\frac{1}{2}\sqrt{\frac{5}{4\pi}} R_0 \beta < 0$；原子核沿 $x$ 轴压扁成饼状；
  3. **$\gamma = 30^\circ$（极大三轴 Triaxial）**：$\delta R_1 = 0, \delta R_2 = -\frac{\sqrt{3}}{2} \sqrt{\frac{5}{4\pi}} R_0 \beta, \delta R_3 = +\frac{\sqrt{3}}{2} \sqrt{\frac{5}{4\pi}} R_0 \beta$；三主轴长短各不相同，非轴对称性达到几何极大。

---

## 3. 在束谱学应用：内禀四极矩与电四极跃迁强度基准
在长波极限下，原子核内禀带电表面的静态内禀四极矩为：
$$Q_0 = \int \rho_e (\vec{r}) (3 z^2 - r^2) d^3 r \approx \frac{3}{\sqrt{5\pi}} Z e R_0^2 \beta \cos\gamma.$$
通过在束库仑激发（Coulomb Excitation）或能级寿命反演得到的约化跃迁几率 $B(E2; 0^+ \to 2_1^+)$：
$$B(E2; 0^+ \to 2_1^+) = \frac{5}{16\pi} e^2 Q_0^2 = \frac{45}{64\pi^2} Z^2 e^2 R_0^4 \beta^2 \cos^2\gamma.$$
建立了宏观表面形变几何与实验辐射跃迁截面之间的坚实解析桥梁。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/greiner-asymmetric-rotor-and-rvm-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`collective-quadrupole-pes` 子命令)
- **上游来源**：`knowledge/sources/book-greiner-nuclear-models.md`
