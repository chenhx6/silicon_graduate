# 2.4 形状坐标、测度与集体量子化

在低能核物理中，原子核的四极形变与集体激发通常超越了微观单核子的独立运动图像。当原子核展现出显著的四极关联时，核子体系的表面轮廓或单体密度分布偏离了各向同性的球形对称。为了在宏观或半微观层次上描述这种集体自由度，Aage Bohr 在其奠基性工作中引入了基于五维四极自由度的集体动力学框架[@bohr-1952-surface-particle-coupling]。这一框架通过引入随体旋转的瞬时内禀主轴系，将五个实验室维度的形变张量解耦为反映核体本征几何形状的两个变形参量与反映核体空间空间朝向的三个欧拉角。

然而，将几何坐标转化为满足量子力学规律的自伴动力学算符，必须处理曲线坐标系中内禀参数的几何测度、主轴标定的多重冗余以及坐标奇点处的边界正规性条件。更为重要的是，形状参数空间中的几率密度依赖于动力学度规所诱导的体积元，这深刻地影响了对“三轴刚性”与“$\gamma$ 软性”等物理概念的实验可识别性。本节系统阐述五维四极坐标的几何变换、经典无旋流转动动能、Pauli–Podolsky 微分几何量子化法则、黎曼测度对几率分布的统计效应，以及边界奇点处的解析正规条件与分立变换群，为后续探讨对称性恢复与微观响应奠定严密的宏观坐标与动能算符基础。

---

## 2.4.1 五维四极自由度与内禀主轴系的几何映射

在实验室坐标系下，描述原子核四极几何形变的最普适多极展开变量是二阶球张量 $\alpha_{2\mu}$（$\mu = -2, -1, 0, 1, 2$）。由于原子核表面半径或单体电荷四极矩在物理空间中为实物理量，球张量分量满足现实性条件（reality condition）[@prochniak-rohozinski-2009-bohr-collective-hamiltonian]：
$$
\alpha_{2\mu}^* = (-1)^\mu \alpha_{2,-\mu}.
$$
该条件限制下，五维复张量包含五个独立的实自由度：实分量 $a_{20} = \alpha_{20}$，以及非零分量的实部与虚部 $\alpha_{2\mu} = a_{2\mu} + i b_{2\mu}$（$\mu = 1, 2$），其中负磁分量由对称性完全确定。

### 1. 内禀主轴系的引入与 $(\beta, \gamma)$ 参数化

为了将原子核的内禀形状畸变与整个核体系在实验室空间中的刚性空间取向区分开来，Bohr 引入了与核四极质量张量主轴完全重合的瞬时内禀参考系 $K'$[@bohr-1952-surface-particle-coupling]。内禀参考系相对于固定实验室参考系 $K$ 的空间取向由三个欧拉角 $\Omega \equiv (\phi, \theta, \psi)$ 唯一指定。在内禀主轴系中，二阶张量的非对角剪切分量严格消失：
$$
a_{\pm 1} = 0, \quad b_{2} = 0, \quad a_2 = a_{-2}.
$$
因此，在内禀主轴系下，原本由五个分量构成的四极张量仅剩下两个独立的非零内禀形状参数：实数 $a_0$ 与 $a_2$。

Bohr 将这两个直角内禀坐标平移为极坐标形式，定义了著名的 Bohr 四极变形参量 $(\beta, \gamma)$[@bohr-1952-surface-particle-coupling]：
$$
a_0 = \beta \cos\gamma, \quad a_2 = a_{-2} = \frac{1}{\sqrt{2}} \beta \sin\gamma.
$$
利用 Wigner $D$ 矩阵的幺正性，从实验室坐标到内禀坐标的变换保持张量平方和不变：
$$
\sum_{\mu=-2}^2 |\alpha_{2\mu}|^2 = a_0^2 + 2 a_2^2 = \beta^2 \cos^2\gamma + \beta^2 \sin^2\gamma = \beta^2.
$$
由此可知，非负参量 $\beta \ge 0$ 直接度量了原子核总四极形变的绝对幅度。在核表面径向展开 $R(\theta', \phi') = R_0 [1 + \sum_\mu \alpha_{2\mu} Y_{2\mu}^*(\theta', \phi')]$ 的一阶近似下，三个内禀主轴方向（分别对应于 $x', y', z'$ 轴，指标标记为 $k = 1, 2, 3$）的核半径相对伸长量为[@bohr-1952-surface-particle-coupling]：
$$
\delta R_k = \sqrt{\frac{5}{4\pi}} R_0 \beta \cos\left( \gamma - \frac{2\pi}{3} k \right), \quad k = 1, 2, 3.
$$
形变角 $\gamma$ 表征了核形状偏离轴对称的程度：
- 当 $\gamma = 0$ 时，$\delta R_3 \propto \beta$，$\delta R_1 = \delta R_2 \propto -\frac{1}{2}\beta$。核椭球绕 $z'$ 轴长轴对称，对应长椭球（prolate spheroid）；
- 当 $\gamma = \pi/3 = 60^\circ$ 时，$\delta R_1 = \delta R_3 \propto \frac{1}{2}\beta$，$\delta R_2 \propto -\beta$。核椭球绕 $y'$ 轴短轴对称，对应扁椭球（oblate spheroid）；
- 当 $\gamma = \pi/6 = 30^\circ$ 时，三个主轴伸长量分别为 $\delta R_3 \propto \frac{\sqrt{3}}{2}\beta$，$\delta R_1 \propto -\frac{\sqrt{3}}{2}\beta$，$\delta R_2 = 0$。三个主轴长度各不相等，对应具有最大非对称性的三轴椭球（triaxial ellipsoid）。

### 2. 主轴标记的 24 重分立冗余与物理扇区

一个给定的三维空间椭球具有三个互相垂直的几何对称轴。在设定内禀笛卡尔坐标系时，将三个几何轴分别指定为第 1、2、3 轴共有 $3! = 6$ 种置换方式；对于每一种轴序指定，三个轴的正负方向各有 $2^3 = 8$ 种选择。若限制坐标系始终为右手系（坐标变换矩阵行列式为 $+1$），则每个轴序置换下保留 4 种合法的空间反向组合。因此，对于空间中同一个确定的核椭球，共有 $6 \times 4 = 24$ 种完全等价的右手内禀主轴选择方式[@bohr-1952-surface-particle-coupling]。

这 24 种坐标变换构成八面体旋转群 $O$（同构于 4 次置换群 $S_4$）。由于实验室张量分量 $\alpha_{2\mu}$ 在这些轴标定置换下必须保持不变，这 24 种变换将整个 $(\beta, \gamma)$ 极坐标平面划分为 6 个等价的 $60^\circ$ 扇区。为了消除这种坐标多值性，国际核结构理论通常选取标准主扇区（principal sector）：
$$
0 \le \gamma \le \frac{\pi}{3} \quad (0^\circ \le \gamma \le 60^\circ).
$$
全平面上任意一个形变点均可通过适当的主轴重新编号与欧拉角变换，唯一映射至该主扇区内。

### 3. 坐标退化与模型适用边界

在某些特殊几何构型处，上述从五个 $\alpha_{2\mu}$ 到 $(\beta, \gamma, \Omega)$ 的坐标映射会出现退化：
- **球形退化点（$\beta = 0$）：** 当原子核处于球形构型时，所有空间方向完全各向同性，三个主轴失去定义，欧拉角与形状角 $\gamma$ 均发生动力学退化；
- **轴对称退化线（$\gamma = 0, \pi/3, \dots$）：** 当核椭球具有旋转对称轴时，绕该对称轴的空间旋转不会引起核表面形状的任何可观测改变，对应欧拉角的取向失去确定性，雅可比行列式在此处消失。

必须在物理上明确：**宏观五维四极坐标模型仅是对低能核多体密度分布的截断近似描述。** 真实原子核是由核子波函数自洽构成的费米多体系统，其内部密度分布包含高阶多极形变（如八极形变 $\beta_3$、十六极形变 $\beta_4$）、表面弥散度（diffuseness）以及径向密度起伏；不能将五维四极坐标参数等同于微观核密度的完全表征。

---

## 2.4.2 教学 Bohr 模型的经典动能与流体惯量张量

为了推导集体运动哈密顿量，首先考察包含恒定正质量参数 $B > 0$ 的五维欧氏四极动能模型（教学 Bohr 模型）。在经典力学中，具有常质量参数 $B$ 的动能标量形式为[@bohr-1952-surface-particle-coupling]：
$$
T = \frac{1}{2} B \sum_{\mu=-2}^2 |\dot{\alpha}_{2\mu}|^2.
$$
利用从实验室坐标到内禀主轴坐标的时间微商关系，实验室速度分量 $\dot{\alpha}_{2\mu}$ 可严格分解为形状参数的时间变化率 $(\dot{\beta}, \dot{\gamma})$ 与内禀坐标系相对于空间的转动角速度矢量 $\boldsymbol{\omega}$。

### 1. 振动与转动的严格动力学分离

在内禀主轴系下展开动能项，由于主轴系消除了剪切分量（$a_{\pm 1} = 0, a_2 = a_{-2}$），形状振动速度与转动角速度之间的交叉项 $\sum_\nu \dot{a}_\nu \omega_k$ 在代数求和中严格相消。经典动能严格分裂为形状振动动能 $T_{\text{vib}}$ 与集体转动动能 $T_{\text{rot}}$ 两部分[@bohr-1952-surface-particle-coupling]：
$$
T = T_{\text{vib}} + T_{\text{rot}}.
$$
振动动能项具有平直极坐标动能的紧凑形式：
$$
T_{\text{vib}} = \frac{1}{2} B \sum_\nu |\dot{a}_\nu|^2 = \frac{1}{2} B (\dot{\beta}^2 + \beta^2 \dot{\gamma}^2).
$$
集体转动动能项则由内禀主轴系下的瞬时转动角速度分量 $\omega_k$（$k = 1, 2, 3$ 对应于主轴 $x', y', z'$）表达：
$$
T_{\text{rot}} = \frac{1}{2} \sum_{k=1}^3 \mathcal{J}_k \omega_k^2.
$$

### 2. 流体力学转动惯量张量与量纲规范

在不可压缩、无旋流动的核流体动力学假定下，绕三个主轴的流体转动惯量分量解析表示为[@bohr-1952-surface-particle-coupling]：
$$
\mathcal{J}_k = 4 B \beta^2 \sin^2\left( \gamma - \frac{2\pi}{3} k \right), \quad k = 1, 2, 3.
$$
声明三个主轴编号的对应关系：$k=1$ 对应 $x'$ 轴，$k=2$ 对应 $y'$ 轴，$k=3$ 对应 $z'$ 轴。各轴惯量显式写为：
$$
\mathcal{J}_1 = 4 B \beta^2 \sin^2\left( \gamma - \frac{2\pi}{3} \right), \quad \mathcal{J}_2 = 4 B \beta^2 \sin^2\left( \gamma + \frac{2\pi}{3} \right), \quad \mathcal{J}_3 = 4 B \beta^2 \sin^2\gamma.
$$
该流体惯量张量呈现出显著的动力学特征：
1. **形变依赖性：** 所有惯量分量均严格正比于形变平方 $\beta^2$。在球形极限 $\beta \to 0$ 下，三个转动惯量完全消失，表明各向同性的球形流体无法通过无旋流动实现刚性转动；
2. **轴对称极限下的消相：** 当 $\gamma = 0$（绕 $z'$ 轴的长椭球对称）时，$\sin^2\gamma = 0$，绕对称轴的惯量严格为零（$\mathcal{J}_3 = 0$），而垂直于对称轴的两个惯量相等：$\mathcal{J}_1 = \mathcal{J}_2 = 4 B \beta^2 \sin^2(2\pi/3) = 3 B \beta^2$。经典无旋流体无法围绕其连续几何对称轴旋转。

必须在此确立严格的量纲界定：**在集体动力学中，惯量质量参数 $B$ 的物理量纲是 $\text{Energy} \cdot \text{time}^2 = \hbar^2 / \text{Energy}$。** 它属于刻画核物质流动惯性的质量参数，绝对不带有电荷 $e$ 或电四极算符的长度平方量纲，严禁与电四极跃迁算符的有效电荷或矩阵元相混淆。相应地，若引入内禀系下的无量纲角动量算符 $\hat{\mathbf{j}} \equiv \hat{\mathbf{J}} / \hbar$，则转动能量算符的能量尺度由 $\hbar^2 / (2B)$ 因子统一控制。

---

## 2.4.3 Pauli–Podolsky 量子化、黎曼测度与动力学算符

将经典广义动能转化为量子力学哈密顿算符时，由于曲线坐标变换引入了局部非平直度规，必须遵循微分几何中的自伴量子化规则。

### 1. 广义度规与 Pauli–Podolsky 量子化法则

设五维集体坐标为 $q^i = (\beta, \gamma, \phi, \theta, \psi)$（$i = 1, \dots, 5$），经典总动能可写为黎曼度规形式：
$$
T = \frac{1}{2} \sum_{i,j=1}^5 g_{ij}(q) \dot{q}^i \dot{q}^j.
$$
Pauli 与 Podolsky 提出，在任意曲线坐标系中，对应于动能二次型的量子动能算符必须表达为黎曼流形上的自伴 Laplace–Beltrami 算符[@prochniak-rohozinski-2009-bohr-collective-hamiltonian]：
$$
\hat{T} = -\frac{\hbar^2}{2} \frac{1}{\sqrt{g}} \sum_{i,j=1}^5 \frac{\partial}{\partial q^i} \left( \sqrt{g} g^{ij} \frac{\partial}{\partial q^j} \right),
$$
其中 $g^{ij}$ 为度规矩阵 $g_{ij}$ 的逆矩阵，$g \equiv \det(g_{ij})$ 为度规张量的行列式。在希尔伯特空间中，波函数内积的积分测度（不变量体积元）自然由度规行列式给出：
$$
\mathrm{d}\tau \equiv \sqrt{g} \, \prod_{i=1}^5 \mathrm{d}q^i.
$$

### 2. 常 $B$ 模型的黎曼测度与动能微分算符

在常质量参数 $B$ 的五维欧氏模型中，从五维笛卡尔四极分量到内禀变量的雅可比行列式计算直接给出度规行列式因子[@bohr-1952-surface-particle-coupling; @prochniak-rohozinski-2009-bohr-collective-hamiltonian]：
$$
\sqrt{g} \propto B^{5/2} \beta^4 |\sin 3\gamma| \sin\theta.
$$
由此导出该模型下的标准不变微分测度：
$$
\mathrm{d}\tau = \beta^4 |\sin 3\gamma| \, \mathrm{d}\beta \, \mathrm{d}\gamma \, \mathrm{d}\Omega,
$$
其中 $\mathrm{d}\Omega \equiv \sin\theta \, \mathrm{d}\theta \, \mathrm{d}\phi \, \mathrm{d}\psi$ 为三维旋转群 $SO(3)$ 上的标准不变 Haar 测度。

将该度规代入 Laplace–Beltrami 展开式，常 $B$ 模型的量子动能算符精确呈现为两体解耦形式：
$$
\hat{T} = \hat{T}_{\text{vib}} + \hat{T}_{\text{rot}},
$$
其中振动动能微分算符为：
$$
\hat{T}_{\text{vib}} = -\frac{\hbar^2}{2B} \left[ \frac{1}{\beta^4} \frac{\partial}{\partial\beta} \left( \beta^4 \frac{\partial}{\partial\beta} \right) + \frac{1}{\beta^2 \sin 3\gamma} \frac{\partial}{\partial\gamma} \left( \sin 3\gamma \frac{\partial}{\partial\gamma} \right) \right],
$$
而转动动能算符则由内禀角动量算符构建：
$$
\hat{T}_{\text{rot}} = \sum_{k=1}^3 \frac{\hat{J}_k^2}{2\mathcal{J}_k} = \frac{\hbar^2}{2} \sum_{k=1}^3 \frac{\hat{j}_k^2}{4 B \beta^2 \sin^2\left( \gamma - \frac{2\pi}{3} k \right)}.
$$
对算符进行细致的量纲核对：前置系数 $\hbar^2 / (2B)$ 具有能量量纲；径向微商部分 $1/\beta^4 \partial_\beta (\beta^4 \partial_\beta)$ 与角向微商部分各带有 $1/\beta^2$ 的量纲因子；转动部分分母中的 $4B\beta^2$ 同样精确提供 $1/\beta^2$ 因子。所有各项在能量与空间坐标量纲上完全一致。

### 3. 微观质量函数与一般测度边界

必须在此指出一般微观集体模型的测度边界：上述导出的测度 $\beta^4 |\sin 3\gamma|$ 仅仅是常数质量参数 $B$ 在平直欧氏模型空间下的特有结果。在由微观自洽平均场（如约束 Hartree–Fock–Bogoliubov 或绝热含时 HFB 方法）导出的广义五维玻尔哈密顿量（5DCH）中，动能由六个坐标相关的质量张量函数表征（包含振动质量 $B_{\beta\beta}, B_{\beta\gamma}, B_{\gamma\gamma}$ 以及三个转动惯量函数 $I_x, I_y, I_z$）[@prochniak-rohozinski-2009-bohr-collective-hamiltonian]。

此时，度规行列式 $\sqrt{G} = \sqrt{\det B_{2,2}}$ 包含了坐标依赖的质量函数行列式以及额外的标量权重函数 $W(\beta, \gamma)$。在此类广义模型中，动能算符与测度必须重新依微观质量张量严格定义，**绝对不能盲目将常 $B$ 模型的 $\beta^4 |\sin 3\gamma|$ 测度当作所有坐标相关微观惯量模型的通用唯一测度。** 完整度规张量的微观代数构建将留待附录 C 展开。

---

## 2.4.4 测度诱发的统计取向与 $\gamma$ 软性辨识边界

内禀波函数在希尔伯特空间中的全概率归一，必须严格遵循几何测度 $\mathrm{d}\tau$。全空间归一化条件写为：
$$
\int |\Psi(\beta, \gamma, \Omega)|^2 \, \beta^4 |\sin 3\gamma| \, \mathrm{d}\beta \, \mathrm{d}\gamma \, \mathrm{d}\Omega = 1.
$$
这一测度的存在，对物理波函数的几率分布与形状参数的统计推断产生了深刻的几何调制。

### 1. 测度对几率密度的几何调制

在讨论形变角分布时，容易忽略测度而将波函数幅值的模方 $|\psi(\gamma)|^2$ 误当作实际物理几率。事实上，物理状态在微元 $[\gamma, \gamma + \mathrm{d}\gamma]$ 内被观测到的真实边缘几率密度为：
$$
P(\gamma) \mathrm{d}\gamma \propto \left[ \int |\Psi(\beta, \gamma, \Omega)|^2 \beta^4 \, \mathrm{d}\beta \, \mathrm{d}\Omega \right] |\sin 3\gamma| \, \mathrm{d}\gamma.
$$
测度中的几何因子 $|\sin 3\gamma|$ 在轴对称端点 $\gamma = 0$ 与 $\gamma = 60^\circ$ 处连续降为零，而在 $\gamma = 30^\circ$ 处取得极大值。

考虑一个对于形状角 $\gamma$ 完全没有束缚力的平坦势阱（即 Wilets–Jean $\gamma$ 极软极限，$V(\beta, \gamma) = V(\beta)$）[@prochniak-rohozinski-2009-bohr-collective-hamiltonian]。在此极限下，哈密顿量对 $\gamma$ 具有连续旋转旋转对称性，其自旋 $I=0$ 的基态内禀波函数在形状角上是完全均匀的常数：$\Psi_0(\gamma) = \text{const}$。然而，引入变量代换 $x \equiv \cos 3\gamma$（$x \in [-1, 1]$），微分测度变换为：
$$
\mathrm{d}x = -3 \sin 3\gamma \, \mathrm{d}\gamma \implies |\sin 3\gamma| \, \mathrm{d}\gamma = \frac{1}{3} \mathrm{d}x.
$$
因此，关于 $\gamma$ 平坦的态在变量 $x = \cos 3\gamma$ 上呈现严格均匀的概率分布：
$$
P(x) = \frac{1}{2} \quad (-1 \le x \le 1).
$$
由此可直接解析计算其统计期望值：
$$
\langle x \rangle = \langle \cos 3\gamma \rangle = \int_{-1}^1 x \cdot \frac{1}{2} \, \mathrm{d}x = 0,
$$
$$
\langle x^2 \rangle = \langle \cos^2 3\gamma \rangle = \int_{-1}^1 x^2 \cdot \frac{1}{2} \, \mathrm{d}x = \frac{1}{3} \approx 0.3333.
$$
根据第 1.2 节中有效形状角的定义 $\cos(3\gamma_{\text{eff}}) = \langle \cos 3\gamma \rangle = 0$，直接解出有效形状角：
$$
\gamma_{\text{eff}} = 30^\circ.
$$

### 2. 平均角 $30^\circ$ 的物理不可分辨性

上述解析结果揭示了一个至关重要的物理规律：**平均形状角 $\langle\gamma\rangle \approx 30^\circ$（或 $\langle\cos 3\gamma\rangle = 0$）绝不唯一证明原子核具有稳定的三轴刚性结构。**

一个对于 $\gamma$ 完全无阻碍的极软核（基态几率完全由相空间测度 $|\sin 3\gamma|$ 主导），与一个在 $\gamma = 30^\circ$ 具有极深势阱的三轴刚性核，二者在对称性驱动下均严格给出 $\langle\cos 3\gamma\rangle = 0$ 与 $\gamma_{\text{eff}} = 30^\circ$。

这一结论在 R1/T03 的受控模型基准计算（`results.csv`）中得到了严格的可重复验证：
- 在完全平坦的 $\gamma$ 软势阱（$\kappa = 0$）基态中，严格数值积分给出 $\langle x \rangle = 6.18 \times 10^{-18} \approx 0$，$\langle x^2 \rangle = 0.333333$，角向均方根展宽为 $\gamma_{\text{rms}} = 0.2279\text{ rad}$；
- 在包含深三轴极小（$\kappa = 18$）的势能模型中，数值积分给出 $\langle x \rangle = -1.41 \times 10^{-18} \approx 0$，$\langle x^2 \rangle = 0.2800$，角向展宽缩减为 $\gamma_{\text{rms}} = 0.2054\text{ rad}$。

两类截然不同的动力学模型在低阶不变量 $q_2$ 与三次矩 $q_3$ 上给出了完全相同的标量期望值。因此，仅凭实验提取的平均形状角 $\gamma_{\text{eff}} \approx 30^\circ$，无法断言体系是三轴刚性还是动态涨落；必须依赖高阶电四极不变量矩阵网络（如反映四极涨落的四阶矩与六阶矩）或激发能谱与跃迁率的动力学比值，方能对三轴刚性与极软动力学做出可信的物理鉴别。

---

## 2.4.5 边界奇点、正规性条件与分立主轴变换群

在求解集体薛定谔方程时，坐标端点处的数学行为往往引发对物理边界条件的误解。

### 1. 坐标奇点与边界正规性

在轴对称端点 $\gamma = 0$（长椭球）与 $\gamma = \pi/3$（扁椭球）处，微分算符中的系数 $\sin 3\gamma = 0$ 出现发散。然而，这种发散是选取 $(\beta, \gamma)$ 极坐标产生的几何网格奇点，类似于球坐标系中极点 $\theta = 0, \pi$ 处的奇点，并不对应任何物理势垒。

考虑自旋 $I=0$ 的无转动态，方程的角向部分退化为：
$$
\frac{1}{\sin 3\gamma} \frac{\partial}{\partial\gamma} \left( \sin 3\gamma \frac{\partial \Phi}{\partial\gamma} \right) = -9 \Lambda \Phi.
$$
将其利用自变量代换 $x = \cos 3\gamma$ 展开，方程形式变换为标准的一维球谐 Legendre 方程：
$$
\frac{\mathrm{d}}{\mathrm{d}x} \left[ (1 - x^2) \frac{\mathrm{d}\Phi}{\mathrm{d}x} \right] = -\Lambda \Phi.
$$
在物理上，量子力学算符的自伴性要求波函数在全空间单值、连续且具有有限的概率流。在区间端点 $x = \pm 1$（即 $\gamma = 0, \pi/3$）处，Legendre 方程满足正规解析条件的解正是通常的 Legendre 多项式 $\Phi_\lambda(x) = P_\lambda(\cos 3\gamma)$。

注意：Legendre 多项式在端点处取有限非零值（$P_\lambda(\pm 1) = (\pm 1)^\lambda \ne 0$）。因此，**将边界处的雅可比行列式归零误认为是物理势垒、强行要求波函数在边界处为零（$\Phi = 0$），在物理上是完全错误的。** 坐标奇点处施加的真实物理要求是波函数的解析正规性与有限性。

### 2. 变换群的区别：标定群 $O$ 与椭球点群 $D_2, D_{2h}$

在建立多体波函数的对称性分类时，必须严格区分以下两个范畴不同的对称群[@bohr-1952-surface-particle-coupling]：
1. **主轴标定群 $O$（阶数为 24）：** 纯属三维空间右手笛卡尔系 24 种主轴标记冗余构成的分立变换群。它要求物理波函数在 24 种欧拉角与 $(\beta, \gamma)$ 的联合变换下必须保持不变（单值性条件）；
2. **椭球内禀点群 $D_2$ 与 $D_{2h}$：** 当四极椭球在固定空间中冻结时，椭球自身几何对于绕三个主轴转动 $\pi$ 角度保持不变，构成四元群 $D_2 = \{E, R_1(\pi), R_2(\pi), R_3(\pi)\}$（阶数为 4）；若计入空间反演对称性，则构成群 $D_{2h} = D_2 \times C_i$（阶数为 8）。

Bohr（1952）证明，波函数在 24 重主轴标定变换下的单值性条件，要求内禀波函数必须按 $D_2$ 群的不可约表示进行对称化分类。对于偶偶核体系，这一对称性定则直接导致内禀角动量在主轴上的投影量子数 $K$ 必须全部为偶数，且角动量量子数 $I$ 与宇称呈现特征分类（例如不存在 $I=1$ 的纯四极转动态）。需要特别声明的是，这一结论属于偶偶核纯四极集体波函数的几何性质，绝不能不加修改地平移套用于包含未成对奇核子、具有时间反演和内禀自旋自由度的奇 $A$ 核体系中。

### 3. 静态形变与动力学响应的物理分立

最后，必须在理论上清晰割裂静态形变矩与微观动力学能标的关系：
- 静态四极矩 $q_2, q_3$ 与波函数模方 $|\Psi(\beta, \gamma)|^2$ 仅反映原子核在电荷空间中的几何空间分布轮廓；
- 绝对激发能量、集体带的能级间距以及集体转动惯量 $\mathcal{J}_k$，由哈密顿量中的动能惯量函数 $B$ 以及势能曲率联合决定。

在宏观玻尔模型中，即便通过静态矩拟合获得了特定的平均形变 $\beta$ 与 $\gamma$，体系的动态激发谱仍依赖于动能质量参数 $B$ 的绝对标定。不能仅凭较窄的几何分布就断言体系处于深微观势阱，也不能断言极软核无法采用内禀主轴坐标。详细的微观动力学惯量函数与推导机制将在第 2.6 节系统展开，而形状振动模与空间取向模的复杂耦合动力学将在第 3.6 节进行深度剖析。
