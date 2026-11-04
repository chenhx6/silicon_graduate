# 第 4 章 (一)：半经典三轴转子相空间、能量马鞍点与分离线拓扑

**来源专著**：A. A. Raduta《Nuclear Structure with Coherent States》（Springer 2016）第 4 章 §4.1 & §4.4
**对应页码**：印刷 pp. 75–86, 109–123 / 物理 PDF pp. 82–93, 116–130

---

## 1. 核心理论推导与相空间映射

### 1.1 自旋相干态与经典动力量映射
在处理三轴转子量子自旋算符 $\hat{\vec{I}} = (\hat{I}_x, \hat{I}_y, \hat{I}_z)$ 时，引入自旋群 $SU(2)$ 的标准自旋相干态 $|\theta, \phi\rangle$：
$$|\theta, \phi\rangle = \exp\left( \zeta \hat{I}_+ - \zeta^* \hat{I}_- \right) |I, -I\rangle, \quad \zeta = \frac{1}{2}\theta e^{-i\phi}.$$
自旋算符在相干态上的经典量子化期望值直接映射为连续相空间球坐标：
$$\langle \hat{I}_x \rangle = I \sin\theta \cos\phi, \quad \langle \hat{I}_y \rangle = I \sin\theta \sin\phi, \quad \langle \hat{I}_z \rangle = I \cos\theta.$$
正则共轭变量为 $(p_\phi = I\cos\theta, \phi)$，满足泊松括号关系 $\{ \phi, p_\phi \} = 1$。

### 1.2 经典三轴 Hamilton 函数
将三轴转动哈密顿量 $\hat{H} = \frac{\hat{I}_1^2}{2\mathcal{J}_1} + \frac{\hat{I}_2^2}{2\mathcal{J}_2} + \frac{\hat{I}_3^2}{2\mathcal{J}_3}$ 在相干态上求期望值：
$$\mathcal{H}(\theta, \phi) = \frac{I^2}{2} \left[ \frac{\sin^2\theta \cos^2\phi}{\mathcal{J}_1} + \frac{\sin^2\theta \sin^2\phi}{\mathcal{J}_2} + \frac{\cos^2\theta}{\mathcal{J}_3} \right].$$
取轴长几何关系：轴 1 为中间形变轴（最大惯量轴 $\mathcal{J}_1$），轴 2 为长轴（最小惯量轴 $\mathcal{J}_2$），轴 3 为短轴（中间惯量轴 $\mathcal{J}_3$）：$\mathcal{J}_1 > \mathcal{J}_3 > \mathcal{J}_2$。

---

## 2. 相空间定点分析与分离线 (Separatrix) 能量临界条件

### 2.1 极值定点分类
对 Hamilton 函数求一阶导数置零：$\frac{\partial \mathcal{H}}{\partial \theta} = 0, \frac{\partial \mathcal{H}}{\partial \phi} = 0$：
1. **稳定极小椭圆点**：位于 $\theta = 90^\circ, \phi = 0^\circ$（角动量严格对齐最大惯量轴 1），能量为 $E_{\min} = \frac{I^2}{2\mathcal{J}_1}$；
2. **稳定极大椭圆点**：位于 $\theta = 90^\circ, \phi = 90^\circ$（角动量对齐最小惯量轴 2），能量为 $E_m_{\max} = \frac{I^2}{2\mathcal{J}_2}$；
3. **不稳定双曲马鞍点**：位于 $\theta = 0^\circ$（角动量对齐中间惯量轴 3），鞍点能量为：
   $$E_n_{\text{crit}} = \frac{I^2}{2\mathcal{J}_3}.$$

### 2.2 分离线拓扑与相轨道定域性
当系统总转动能量恰好等于鞍点能量 $E = E_n_{\text{crit}}$ 时，能量方程化为：
$$\frac{\sin^2\theta \cos^2\phi}{\mathcal{J}_1} + \frac{\sin^2\theta \sin^2\phi}{\mathcal{J}_2} + \frac{\cos^2\theta}{\mathcal{J}_3} = \frac{1}{\mathcal{J}_3}.$$
化简得到相空间在球面上的分界闭合双曲轨迹——**分离线 (Separatrix)**：
$$\tan^2\theta = \frac{\frac{1}{\mathcal{J}_3} - \frac{1}{\mathcal{J}_1}}{\frac{1}{\mathcal{J}_2} - \frac{1}{\mathcal{J}_3}} \cdot \frac{1}{\sin^2\phi}.$$
- **亚临界区域（$E < E_n_{\text{crit}}$）**：
  轨道封闭环绕最大惯量轴做微小周期性天平动（Libration），在量子力学中严格对应**多声子摆动运动 (Wobbling Mode)**；
- **超临界区域（$E > E_n_{\text{crit}}$）**：
  相点冲出分离线限制，绕长轴做全角循环环流（Circulation）；在奇奇核与多准粒子耦合下，系统分岔并自发破缺时间反演对称性，演变为**静态手征双阱轨道 (Chiral Orbitals)**。

---

## 3. 在束核谱学应用：高自旋摆动运动失稳临界线判定
在在束核谱学高自旋态演化中，摆动激发能量为 $E_{\text{wob}} = E(n_w=1, I) - E(n_w=0, I)$：
- 随着自旋上升，有效总转动能量快速抬升；
- 当基态带能量接近分离线临界能量 $E_n_{\text{crit}}$ 时，相空间鞍点附近的局部回复力常数迅速趋近于零，导致摆动频率剧烈下降软化；
- 超过分离线后，稳定主轴摆动模式彻底消亡，体系发生从摆动进动向量子手征取向的宏观拓扑相变。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/raduta-gcsm-chiral-and-triaxial-rotor-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`davydov-wobbling-rotor` 子命令)
- **上游来源**：`knowledge/sources/book-raduta-coherent-states.md`
