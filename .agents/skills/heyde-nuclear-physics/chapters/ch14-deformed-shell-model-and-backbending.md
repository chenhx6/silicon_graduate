# 第 14 章：Nilsson 变形壳模型、转动推转与高自旋回弯动力学

**来源专著**：Kris L. G. Heyde《Basic Ideas and Concepts in Nuclear Physics》（IOP 1999）第 14 章
**对应页码**：印刷 pp. 466–519 / 物理 PDF pp. 486–519

---

## 1. 核心理论推导与 Nilsson 变形单粒子势

### 1.1 各向异性变形谐振子哈密顿量
S. G. Nilsson (1955) 将独立粒子球形平均场推广到轴对称椭球形变空间：
$$H = -\frac{\hbar^2}{2m} \nabla^2 + \frac{1}{2} m \left[ \omega_\perp^2 (x^2 + y^2) + \omega_z^2 z^2 \right] + C \vec{l} \cdot \vec{s} + D \vec{l}^2,$$
体积守恒要求振荡频率乘积为常数：$\omega_x \omega_y \omega_z = \omega_0^3$。
引入椭球形变参数 $\epsilon$（与 Bohr 形变关系为 $\epsilon \a0.95 \beta_2$）：
$$\omega_z = \omega_0 \left( 1 - \frac{2}{3}\epsilon \right), \quad \omega_\perp = \omega_0 \left( 1 + \frac{1}{3}\epsilon \right).$$

### 1.2 渐近量子数 $[N n_z \Lambda \Omega^\pi]$ 与高-$j$ 独宇称轨道
在强形变极限下，单粒子状态由渐近量子数标记：
- $N$：主谐振子壳量子数；
- $n_z$：沿主对称轴方向的振动声子数；
- $\Lambda$：轨道角动量沿对称轴的投影量子数；
- $\Omega = \Lambda \pm 1/2$：总角动量沿对称轴投影；
- **独宇称侵入轨道（Unique-Parity Intruder Orbitals）**：
  来自上一壳层的高-$j$ 轨道（如质子 $1h_{11/2}$、中子 $1i_{13/2}$）具有相反宇称，与周围同宇称轨道无近距离强两体混合；
  随长椭形变 $\beta$ 增大，低 $\Omega$ 分支（如 $1/2^+[660]$、$1/2^-[550]$）受强烈表面吸引急剧向下坠落，成为高自旋顺排的核心载体。

---

## 2. 推转壳模型 (Cranking Model) 与 Coriolis 解耦

### 2.1 Inglis 转动推转哈密顿量
D. R. Inglis (1954) 在绕垂直于对称轴的主轴（如 $x$ 轴）以角频率 $\omega$ 旋转的坐标系中描述单核子运动：
$$H_{\text{crank}} = H_{\text{sp}} - \vec{\omega} \cdot \vec{j} = H_{\text{sp}} - \omega \hat{j}_x.$$
由此导出一阶微扰推转转动惯量公式：
$$\mathcal{J}_{\text{Inglis}} = 2\hbar^2 \sum_{m \neq 0} \frac{|\langle m | \hat{j}_x | 0 \rangle|^2}{E_m - E_0}.$$

### 2.2 Coriolis 旋转顺排 (Rotational Alignment, RAL)
Coriolis 力算符 $-\omega \hat{j}_x$ 具有强烈的解耦作用：
- 倾向于打破核子对在时间反演轨道上的配对（破坏 $J=0^+$ 凝聚，Coriolis Anti-Pairing, CAP）；
- 强力迫使核子单粒子角动量 $\vec{j}$ 偏离自身内禀对称轴，强行转向沿旋转轴（$x$ 轴）顺排平行排列；
- 单对顺排角动量可达 $i_x \approx 2 j - 1$（对于 $i_{13/2}$ 中子对，顺排量高达 $10 - 12\hbar$！）。

---

## 3. 高自旋回弯现象 (Backbending) 动力学机制

在转动带随自旋持续上升至临界转动频率 $\hbar\omega_c \a0.25 - 0.35\text{ MeV}$（自旋 $I \a12 - 16\hbar$）处：
1. **双带能级交叉**：
   基态完全配对转动带（Ground Band, $g$-band）与对齐的双准粒子解耦带（Stockholm Band, $s$-band）发生能级相交；
2. **回弯图像（Backbending Plot）**：
   绘制有效动力学转动惯量 $\frac{2\mathcal{J}}{\hbar^2} = \frac{4I - 2}{E_\gamma}$ 随转动频率平方 $(\hbar\omega)^2 = (E_\gamma / 2)^2$ 的演化曲线；
   由于 $s$-带带入巨额对齐角动量，跃迁 $\gamma$ 能量在相交点处发生急剧停滞甚至反常变小，使得曲线展示出典型的“S”形反向折返弯曲；
3. **相互作用矩阵元 $|V_{12}|$ 决定弯曲形态**：
   - 弱相互作用（$|V_{12}| < 30\text{ keV}$）：尖锐回弯（Backbending）；
   - 强相互作用（$|V_{12}| \ge 60\text{ keV}$）：平滑上弯（Upbending）。

---

## 4. 关联知识与交叉索引
- **方法合同**：`knowledge/methods/heyde-collective-modes-and-exotic-nuclei-contract.md`
- **代码实现**：`system/scripts/analysis/nuclear_analyzer.py` (`routhian-alignment` 子命令)
- **上游来源**：`knowledge/sources/book-heyde-nuclear-physics-concepts.md`
