# 2.3 配对、准粒子与阻塞

在低能核物理中，原子核并不是各核子在静态平均场势阱中独立运动的简单费米气体。由于短程吸引核力的存在，核子体系展现出强烈的两体关联。最为显著的经验证据是核结合能的奇偶交错与低能激发谱的系统学特征：所有偶偶核的基态总角动量与宇称无一例外地为 $I^\pi = 0^+$，且其第一个内禀单核子激发能级通常被推高至 $1\sim 2\text{ MeV}$ 以上；相比之下，奇 $A$ 核与奇奇核不仅基态自旋呈现多样性，其低能激发能级密度也显著高于邻近偶偶核。这种普遍存在的配对关联使得单粒子图像不能直接描述低激发态，必须引入超流配对与准粒子均场理论[@book-suhonen-from-nucleons-to-nucleus; @book-jain-nuclear-isomers]。

将固体物理中的 Bardeen–Cooper–Schrieffer（BCS）超导理论平移至有限原子核体系，需要处理有限核子数、时间反演对称性以及粒子数规范对称性破缺等一系列关键理论问题。本节旨在建立严格自洽的微观配对与准粒子理论框架：首先从时间反演成对与短程吸引力出发，阐明奇偶效应的微观成因，并澄清经验质量差与微观纯配对参数的边界；随后在静态约束变分框架下，推导 Bogoliubov–Valatin 正则变换、准粒子哈密顿量的 $2\times 2$ 矩阵对角化、占据几率以及自洽能隙方程与粒子数守恒方程；进而深入辨析配对能隙、配对张量振幅与规范角三个不同物理量，说明粒子数不守恒仅为平均场变分参考态的数学工具，并引出局域配对转动与粒子数投影接口；随后讨论奇核子诱发的阻塞效应及其自洽重排机制，厘清多准粒子激发态与 BCS 临界塌缩的物理本质；最后通过两能级模型的解析对准与无相互作用极限，提供严密的数学控制与物理澄清。

---

## 2.3.1 时间反演成对、短程吸引与奇偶效应的微观根源

原子核内部核子配对倾向的物理根源在于核力的短程强吸引性质。考虑球形或轴对称平均场势阱中的单核子轨道，空间反演与时间反演是对称哈密顿量的基本不变性。设单核子本征态为 $|k\rangle = |a, m_k\rangle$，其中 $a$ 综合代表径向量子数 $n$、轨道角动量 $l$ 与总单粒子角动量 $j$，$m_k$ 为角动量在对称轴（或量子化轴）上的投影分量。由反幺正时间反演算符 $\mathcal{T}$ 作用于该单粒子态，可定义其时间反演共轭轨道 $|\bar{k}\rangle$。在标准的 Condon–Shortley 相位约定下[@book-suhonen-from-nucleons-to-nucleus]：
$$
|\bar{k}\rangle \equiv \mathcal{T} |k\rangle = (-1)^{j - m_k} |a, -m_k\rangle.
$$
在此约定下，重复应用时间反演算符给出 $\mathcal{T}^2 |k\rangle = (-1)^{2j} |k\rangle = -|k\rangle$（对费米子体系，半奇数自旋 $2j$ 必为奇数），体现了费米子时间反演的双重简并定理（Kramers 简并）。

若两个同类核子（质子—质子或中子—中子）分别占据相互时间反演的共轭单粒子轨道 $|k\rangle$ 与 $|\bar{k}\rangle$，并将它们耦合为总角动量为零的状态：
$$
|k \bar{k}; J=0, M=0\rangle = \sum_{m_k} \frac{C_{j m_k j -m_k}^{0 0}}{\sqrt{2}} |k \bar{k}\rangle = \frac{1}{\sqrt{2j+1}} \sum_{m_k} (-1)^{j - m_k} |a, m_k; a, -m_k\rangle.
$$
这一双核子态在空间中具有球对称的空间概率密度分布。在经典半经典轨道图像中，处于 $|k\rangle$ 与 $|\bar{k}\rangle$ 的两个核子在同一几何轨道平面上沿相反方向环形巡游，彼此相向相遇的概率达到最大值。由于有效核力具有很短的作用力程（近似为接触相互作用或短程吸引势），两个处于时间反演态的核子波函数重叠积分显著大于耦合到任意非零总角动量 $J > 0$ 的双核子态。这种全空间重叠使得 $J = 0$ 配对基态获得极大的吸引结合能，从而在两体能级谱中与激发态之间撕开一条显著的能隙[@book-suhonen-from-nucleons-to-nucleus; @book-jain-nuclear-isomers]。

这一微观吸引机制直接导致了结合能的奇偶效应（odd-even staggering, OES）。在偶偶核中，所有价质子与价中子均两两配对成 $J=0$ 的时间反演对，体系处于完全配对的超流基态；在奇 $A$ 核中，至少存在一个未配对的奇核子，该奇核子无法享受配对吸引能，因而奇 $A$ 核的结合能明显低于相邻偶偶核结合能的内插平均值；在奇奇核中，存在未成对的奇质子与奇中子，其结合能进一步相对受损。

在核质量系统学中，人们常用相邻核素的束缚能 $B(N, Z)$ 构造离散差分公式来提取经验奇偶质量差。例如中子体系最常用的三点与四点差分公式定义为：
$$
\Delta_n^{(3)}(N, Z) \equiv \frac{(-1)^N}{2} \left[ B(N-1, Z) - 2B(N, Z) + B(N+1, Z) \right],
$$
$$
\Delta_n^{(4)}(N, Z) \equiv \frac{(-1)^N}{4} \left[ B(N-2, Z) - 3B(N-1, Z) + 3B(N, Z) - B(N+1, Z) \right].
$$
对于中重质量核，$(-1)^N \Delta_n^{(3)}$ 在偶偶核呈现正峰，在奇 $A$ 核呈现深谷，经验能标通常近似表示为 $\Delta_{\text{exp}} \approx 12 / \sqrt{A}\text{ MeV}$[@book-jain-nuclear-isomers]。

必须在此建立严格的物理边界：**经验提取的奇偶质量差 $\Delta^{(3)}$ 或 $\Delta^{(4)}$，并不等同于微观哈密顿量中的纯配对相互作用能隙参数 $\Delta$。** 从多体理论角度看，束缚能的三点差分展开不仅包含两粒子配对关联的净贡献，还直接混杂了费米面附近平均场单粒子轨道能的局域间距 $(\epsilon_{k+1} - \epsilon_k)$、核子数改变引起的核芯自洽重排能（rearrangement energy）、形变平衡点的移动以及壳层单极位移效应。在幻数闭壳邻近核区，单粒子能隙巨大，经验差分公式主要反映壳层跳变而非微观超流配对；即便在开壳核区，将 $\Delta_{\text{exp}}$ 直接作为单一不变的常数代入微观模型，也会抹杀轨道依赖的配对矩阵元结构与形状极化响应。

---

## 2.3.2 约束变分、Bogoliubov 变换与 BCS 均场推导

为了在包含宏观配对关联的同时保留单粒子物理图像，Bardeen、Cooper 与 Schrieffer 提出了凝聚态波函数的变分形式。在原子核壳模型空间中，选取一组正交单粒子产生算符 $c_k^\dagger$，其时间反演共轭轨道产生算符标记为 $c_{\bar{k}}^\dagger$。为了严格避免在配对求和中引入虚假的人为双重计数，规定指标 $k > 0$ 遍历半数单粒子态空间（例如对于球形或轴对称核，限制磁量子数或轴投影 $m_k > 0$）。

### 1. BCS 拟设与粒子数约束

BCS 基态拟设波函数定义为独立时间反演轨道对的相干凝聚态[@book-suhonen-from-nucleons-to-nucleus]：
$$
|\mathrm{BCS}\rangle = \prod_{k>0} \left( u_k + v_k c_k^\dagger c_{\bar{k}}^\dagger \right) |0\rangle,
$$
其中 $|0\rangle$ 为无核子的真实真空态，$u_k$ 与 $v_k$ 为待定实数变分参量。$v_k^2$ 代表轨道对 $(k, \bar{k})$ 被一对核子占据的几率，$u_k^2$ 代表该轨道对为空的几率。态矢的归一化条件要求：
$$
\langle\mathrm{BCS}|\mathrm{BCS}\rangle = \prod_{k>0} \left( u_k^2 + v_k^2 \right) = 1 \implies u_k^2 + v_k^2 = 1 \quad (\forall k > 0).
$$
显然，展开波函数式可知，$|\mathrm{BCS}\rangle$ 包含了 $0, 2, 4, \dots$ 个核子的不同粒子数本征态的线性叠加，因而自发破缺了粒子数守恒（即 $U(1)$ 规范不变性）。为保证该多体态能够合理描述给定的原子核体系，必须在变分原理中引入拉格朗日未定乘子 $\lambda$（化学势），对平均粒子数加以严格约束：
$$
\langle\mathrm{BCS}| \hat{n} |\mathrm{BCS}\rangle = \bar{n}, \quad \hat{n} = \sum_{k>0} \left( c_k^\dagger c_k + c_{\bar{k}}^\dagger c_{\bar{k}} \right).
$$
计算直接给出平均粒子数表达式：
$$
\bar{n} = 2 \sum_{k>0} v_k^2.
$$
式中的因子 $2$ 来源于每一对时间反演轨道包含两个单核子态，求和仅在 $k > 0$ 空间进行，计数准确无误。

### 2. Bogoliubov–Valatin 正则变换

为了求解体系的低能元激发，引入准粒子产生算符 $\alpha_k^\dagger$ 与消灭算符 $\alpha_k$。Bogoliubov–Valatin 变换将物理粒子算符与空穴算符进行线性混合[@book-suhonen-from-nucleons-to-nucleus]：
$$
\alpha_k^\dagger = u_k c_k^\dagger - v_k c_{\bar{k}}, \quad \alpha_{\bar{k}}^\dagger = u_k c_{\bar{k}}^\dagger + v_k c_k,
$$
其厄米共轭消灭算符为：
$$
\alpha_k = u_k c_k - v_k c_{\bar{k}}^\dagger, \quad \alpha_{\bar{k}} = u_k c_{\bar{k}} + v_k c_k^\dagger.
$$
利用 $u_k^2 + v_k^2 = 1$，容易严格验证准粒子算符满足费米子的反对易关系：
$$
\{\alpha_k, \alpha_{k^\prime}^\dagger\} = \delta_{kk^\prime}, \quad \{\alpha_{\bar{k}}, \alpha_{\bar{k}^\prime}^\dagger\} = \delta_{kk^\prime}, \quad \{\alpha_k, \alpha_{\bar{k}^\prime}^\dagger\} = 0, \quad \{\alpha_k, \alpha_{k^\prime}\} = 0.
$$
因此，该变换是一个保持量子力学正则反对易关系的正则变换。作用消灭算符于 BCS 基态可知：
$$
\alpha_k |\mathrm{BCS}\rangle = 0, \quad \alpha_{\bar{k}} |\mathrm{BCS}\rangle = 0 \quad (\forall k > 0),
$$
表明 $|\mathrm{BCS}\rangle$ 即为准粒子的物理真空态。

### 3. 辅助哈密顿量与 $2\times 2$ 矩阵对角化

考虑由球形或变形单粒子均场能 $\epsilon_k$ 及纯配对相互作用构成的单极配对哈密顿量：
$$
\hat{H} = \sum_{k>0} \epsilon_k \left( c_k^\dagger c_k + c_{\bar{k}}^\dagger c_{\bar{k}} \right) - \sum_{k, k^\prime > 0} G_{k k^\prime} c_k^\dagger c_{\bar{k}}^\dagger c_{\bar{k}^\prime} c_{k^\prime},
$$
其中 $G_{k k^\prime} > 0$ 为正的配对散射矩阵元。在粒子数约束下，构造辅助变分哈密顿量 $\hat{H}^\prime = \hat{H} - \lambda \hat{n}$。通过逆变换将粒子算符表达为准粒子算符：
$$
c_k^\dagger = u_k \alpha_k^\dagger + v_k \alpha_{\bar{k}}, \quad c_{\bar{k}}^\dagger = u_k \alpha_{\bar{k}}^\dagger - v_k \alpha_k,
$$
并应用准粒子正规编序（Wick 定理），辅助哈密顿量可精确分解为四项之和[@book-suhonen-from-nucleons-to-nucleus]：
$$
\hat{H}^\prime = H_0^\prime + H_{11}^\prime + H_{20}^\prime + V_{\mathrm{RES}},
$$
其中：
- $H_0^\prime = \langle\mathrm{BCS}| \hat{H}^\prime |\mathrm{BCS}\rangle$ 为基态平均能量；
- $H_{11}^\prime$ 仅包含 $\alpha^\dagger \alpha$ 形式的一体准粒子数算符；
- $H_{20}^\prime$ 包含成对产生或消灭准粒子的项 $\alpha_k^\dagger \alpha_{\bar{k}}^\dagger + \alpha_{\bar{k}} \alpha_k$；
- $V_{\mathrm{RES}}$ 包含四个准粒子算符正规积的高阶残余作用。

定义单粒子有效能量 $\xi_k \equiv \epsilon_k - \lambda - \mu_k$（其中 $\mu_k$ 为自洽相互作用引起的自能修正，在单极配对力下通常较小），以及轨道自洽配对能隙：
$$
\Delta_k \equiv \sum_{k^\prime > 0} G_{k k^\prime} u_{k^\prime} v_{k^\prime}.
$$
代入展开后，非对角的准粒子对产生项系数写为：
$$
H_{20}^\prime = \sum_{k>0} \left[ 2\xi_k u_k v_k - \Delta_k (u_k^2 - v_k^2) \right] \left( \alpha_k^\dagger \alpha_{\bar{k}}^\dagger + \alpha_{\bar{k}} \alpha_k \right).
$$
Rayleigh–Ritz 变分原理 $\delta \langle\mathrm{BCS}| \hat{H}^\prime |\mathrm{BCS}\rangle = 0$ 要求真空态能量对于变分参量达到极小值。这严格等价于要求“危险项”系数恒为零，即 $H_{20}^\prime \equiv 0$：
$$
2\xi_k u_k v_k - \Delta_k (u_k^2 - v_k^2) = 0.
$$
这一关系可以极其优雅地表述为准粒子空间中的 $2\times 2$ 厄米均场矩阵本征值方程：
$$
\begin{pmatrix}
\xi_k & -\Delta_k \\
-\Delta_k & -\xi_k
\end{pmatrix}
\begin{pmatrix}
u_k \\
v_k
\end{pmatrix}
= E_k
\begin{pmatrix}
u_k \\
v_k
\end{pmatrix}.
$$
对角化该 $2\times 2$ 行列式：
$$
\det \begin{pmatrix} \xi_k - E_k & -\Delta_k \\ -\Delta_k & -\xi_k - E_k \end{pmatrix} = E_k^2 - (\xi_k^2 + \Delta_k^2) = 0,
$$
直接得到具有正能物理本征值的单一准粒子激发能：
$$
E_k = \sqrt{\xi_k^2 + \Delta_k^2}.
$$
结合归一化条件 $u_k^2 + v_k^2 = 1$，即可严格解析解出占据振幅与非占据振幅：
$$
v_k^2 = \frac{1}{2} \left( 1 - \frac{\xi_k}{E_k} \right) = \frac{1}{2} \left( 1 - \frac{\xi_k}{\sqrt{\xi_k^2 + \Delta_k^2}} \right),
$$
$$
u_k^2 = \frac{1}{2} \left( 1 + \frac{\xi_k}{E_k} \right) = \frac{1}{2} \left( 1 + \frac{\xi_k}{\sqrt{\xi_k^2 + \Delta_k^2}} \right),
$$
$$
u_k v_k = \frac{\Delta_k}{2 E_k} = \frac{\Delta_k}{2 \sqrt{\xi_k^2 + \Delta_k^2}}.
$$

### 4. 自洽能隙方程与粒子数方程

将乘积项 $u_k v_k$ 的显式代回 $\Delta_k$ 与粒子数定义式，即构成了著名的 BCS 自洽方程组：
$$
\Delta_k = \sum_{k^\prime > 0} G_{k k^\prime} \frac{\Delta_{k^\prime}}{2 \sqrt{\xi_{k^\prime}^2 + \Delta_{k^\prime}^2}},
$$
$$
\bar{n} = \sum_{k>0} \left( 1 - \frac{\xi_k}{\sqrt{\xi_k^2 + \Delta_k^2}} \right).
$$
若采用常用的常配对相互作用力模型，假定有效相互作用在相关壳层内为常数 $G_{k k^\prime} = G$，则配对能隙在所有活跃能级上蜕化为统一常数 $\Delta_k = \Delta$。此时能隙方程简化为：
$$
\frac{2}{G} = \sum_{k>0} \frac{1}{\sqrt{(\epsilon_k - \lambda)^2 + \Delta^2}}.
$$
消除危险项后，辅助哈密顿量在准粒子基底下的均场部分完全对角化：
$$
\hat{H}^\prime = H_0^\prime + \sum_{k>0} E_k \left( \alpha_k^\dagger \alpha_k + \alpha_{\bar{k}}^\dagger \alpha_{\bar{k}} \right) + V_{\mathrm{RES}}.
$$
在忽略准粒子间高阶残余作用 $V_{\mathrm{RES}}$ 的独立准粒子近似下，多体激发态的能量直接由单准粒子能量 $E_k$ 的代数和给定。

---

## 2.3.3 规范对称性破缺、配对转动与物理粒子数守恒

BCS 理论成功将强关联两体相互作用化为准粒子真空与其上的独立元激发，但代价是破坏了严格的粒子数守恒定律。深入理解配对物理必须厘清相关态与物理参量的本质。

### 1. 三个不同对象的概念辨析

在文献讨论中，容易将配对能隙、配对振幅与规范角三者模糊混同。必须做出明确的概念界定：
1. **配对能隙 $\Delta$：** 具有能量量纲（单位通常为 $\text{MeV}$）。由准粒子能量公式 $E_k = \sqrt{\xi_k^2 + \Delta^2} \ge \Delta$ 可知，偶偶核中打破一个核子对并产生两个不相干准粒子，所需最小激发能量为 $2\Delta$。因此，$\Delta$ 本质上是偶偶核低能两准粒子连续态激发谱的阈值能标。
2. **配对张量振幅 $\kappa_k$：** 无量纲复数振幅，定义为破缺参考态下的两体反常跃迁密度（pairing tensor 或 anomalous density）：
   $$
   \kappa_k \equiv \langle\mathrm{BCS}| c_{\bar{k}} c_k |\mathrm{BCS}\rangle = u_k v_k = \frac{\Delta_k}{2 E_k}.
   $$
   它直接度量了单个时间反演轨道对的凝聚几率振幅。在费米面深处（$\xi_k \ll -\Delta$）$u_k \to 0, v_k \to 1$，$\kappa_k \to 0$；在费米面远上方（$\xi_k \gg \Delta$）$v_k \to 0, u_k \to 1$，$\kappa_k \to 0$；只有在费米面附近的弥散层内（$|\xi_k| \lesssim \Delta$），$\kappa_k$ 才呈现显著的非零峰值。
3. **配对规范角 $\theta$：** 全局粒子数规范变换群 $U(1)$ 的连续对称性变换角参数。在变换 $c_k \to e^{-i\theta} c_k$ 下，双核子湮灭算符变换为 $c_{\bar{k}} c_k \to e^{-2i\theta} c_{\bar{k}} c_k$。由于 $|\mathrm{BCS}\rangle$ 是不同粒子数态的相干叠加，其宏观相位 $\theta$ 被刚性固定，导致粒子数算符 $\hat{n} = -i \hbar \frac{\partial}{\partial \theta}$ 与配对规范角在量子力学上互为共轭变量。

### 2. 粒子数破缺的本质与局域配对转动

原子核作为真空中的孤立强相互作用体系，其实验物理哈密顿量与微观核子数算符严格对易（$[\hat{H}, \hat{n}] = 0$），核素在实验测量中具有绝对确定的核子数 $A$。**BCS 或 Hartree–Fock–Bogoliubov（HFB）态中展现的粒子数规范对称性破缺，纯属理论近似构建的内禀参考态数学手段，并不意味着物理原子核真实发生粒子数不守恒。**

在自发破缺连续规范对称性的均场态中，伴随而生的是无能隙的 Nambu–Goldstone（NG）零能激发模。Hinohara（2015）利用有限振幅法（FAM）线性响应理论深入剖析了这一机制[@hinohara-2015-nambu-goldstone-inertia-response]。破缺态中与粒子数算符 $\hat{N}$ 共轭的规范角算符 $\hat{\Theta}$ 诱发沿同位素链方向的等效转动，称为配对转动（pairing rotation）。在能量对微观粒子数偏离的泰勒展开中：
$$
B(N, Z_0) = B(N_0, Z_0) + \lambda_n(N_0, Z_0) \Delta N + \frac{(\Delta N)^2}{2 \mathcal{J}_{\text{pair}}(N_0, Z_0)},
$$
其中第二级展开系数定义了 Thouless–Valatin 配对转动惯量：
$$
\mathcal{J}_{\text{pair}} \equiv \frac{\partial \bar{N}}{\partial \lambda} = -S(\hat{N}, \omega = 0) \quad (\text{单位：}\text{MeV}^{-1}).
$$
必须严格注意：**配对转动惯量 $\mathcal{J}_{\text{pair}}$ 的量纲是 $\text{MeV}^{-1}$，它反映的是配对能面随化学势（费米面）变化的能谱曲率；而空间三维转动惯量 $\mathcal{J}_{\text{space}}$ 的量纲是 $\hbar^2/\text{MeV}$（或通常写为 $\text{MeV}^{-1} \hbar^2$），反映的是孤立体系绕真实空间几何轴旋转的动能响应。二者动力学自由度完全不同，绝对不能因同样冠以“转动惯量”之名而混为一谈。**

为了消除均场近似带来的粒子数虚假涨落，理论上发展了粒子数投影技术（Particle Number Projection, PNP）。投影算符通过在配对规范角空间进行闭合围道积分：
$$
\hat{P}_N = \frac{1}{2\pi} \int_0^{2\pi} e^{i (\hat{n} - N) \theta} \mathrm{d}\theta,
$$
可以将包含多组分粒子的 $|\mathrm{BCS}\rangle$ 态投影回严格好粒子数的精确多体态 $|N\rangle \propto \hat{P}_N |\mathrm{BCS}\rangle$。这一内禀参考系与对称性恢复逻辑，为第 2.5 节处理三维空间旋转不变性恢复（角动量投影）提供了完全一致的数学范式。

---

## 2.3.4 阻塞效应与多准粒子态的微观重排

当原子核处于奇 $A$ 核、奇奇核，或偶偶核的高自旋断对激发态时，体系中存在未配对的独立核子。这些奇核子对周围核子介质的配对关联产生剧烈的反作用，这一核心物理机制称为阻塞效应（blocking effect）[@book-jain-nuclear-isomers]。

### 1. 泡利阻塞的微观机制

设某个单核子态 $|k_b\rangle$ 已被一个奇准粒子所单占。根据费米子泡利不相容原理：
1. 任何其他核子都无法再填入该态 $|k_b\rangle$；
2. 任何原本处于时间反演轨道对 $(k_b, \bar{k}_b)$ 的双核子配对无法被容纳；
3. 最关键的是，双核子配对散射过程 $\sum_{k^\prime} G_{k_b k^\prime} c_k^\dagger c_{\bar{k}}^\dagger c_{\bar{k}^\prime} c_{k^\prime}$ 中，所有涉及轨道 $k_b$ 的对散射矩阵元被全部强制切断！

这意味着，轨道 $k_b$ 被从活跃的配对模型空间中彻底“冻结”并剥离。在自洽均场计算中，针对被阻塞态的自洽能隙方程必须剔除被阻塞的指标：
$$
\Delta_k = \sum_{k^\prime > 0, k^\prime \ne k_b} G_{k k^\prime} \frac{\Delta_{k^\prime}}{2 \sqrt{\xi_{k^\prime}^2 + \Delta_{k^\prime}^2}},
$$
$$
\bar{n} - 1 = \sum_{k>0, k \ne k_b} \left( 1 - \frac{\xi_k}{\sqrt{\xi_k^2 + \Delta_k^2}} \right).
$$
由于费米面附近通常单粒子能级密度最为关键，而奇核子往往恰好占据在费米面附近的单粒子能级上，被剔除的能级对自洽求和的贡献权重最大。因此，阻塞效应会导致自洽配对能隙 $\Delta$ 产生显著的局域塌缩和减小，通常奇 $A$ 核的等效中子能隙较相邻偶偶核小 $15\% \sim 30\%$。

同时，阻塞奇核子所携带的固定轨道单体角动量与宇称，会通过单极与多极平均场引起周围核芯的自洽重排（self-consistent rearrangement）。化学势 $\lambda$ 发生自适应平移，变形势阱产生形状极化，其他非阻塞轨道的占据几率 $v_k^2$ 均会发生协同调整[@book-jain-nuclear-isomers]。

### 2. 多准粒子态与高 $K$ 异能态

在形变核区（如稀土 $A\sim 178$ 与中重 $A\sim 130$ 核区），强形变使得单粒子角动量沿对称轴的投影量子数 $\Omega$ 成为较好量子数。当断开多对时间反演对时，可以激发两个、三个甚至六个准粒子，其投影量子数平行极化耦合形成总内禀投影 $K = \sum_i \Omega_i$[@book-jain-nuclear-isomers]。

Jain 等人系统阐释了多准粒子（MQP）态的激发能构造[@book-jain-nuclear-isomers]：
$$
E(K) = E_0 + \sum_{i\in\mathrm{qp}} E_{\mathrm{qp}}(i) + E_{\mathrm{rot}} + \Delta E_{\mathrm{residual}},
$$
其中每个被激发的奇准粒子均对特定轨道施加阻塞。当多个高 $\Omega$ 轨道（如 $\nu i_{13/2}$ 或 $\pi h_{11/2}$）同时被单占时，核内配对散射通道被多重阻断，诱导低激发能下高 $K$ 态的稳定存在，形成具有极长半衰期的同核异能态（例如 $^{178}\mathrm{Hf}$ 中的 $16^+$ 异能态，寿命长达 $31\text{ 年}$）[@book-jain-nuclear-isomers]。

### 3. 破除常见误区：阻塞不等于无配对，塌缩不等于物理相变

在多准粒子物理中存在两个极其普遍的误读，必须在此确立清晰的理论界限：

**误区一：多准粒子阻塞使核内核子配对完全消失。**
尽管阻塞若干高投影单粒子轨道显著削弱了有效配对能隙 $\Delta$，但未被阻塞的其他数十个空间轨道依然在费米面两侧广泛参与对散射过程。即便在四准粒子或六准粒子态中，剩余费米海中的核子依然维系着显著的超流配对关联。不能草率宣称多准粒子态的配对“严格为零”，更不能因此将多准粒子态的微观惯量直接置换为全刚体转动惯量。

**误区二：静态 BCS 解的临界塌缩是有限核体系的真实物理相变。**
在静态 BCS 变分方程中，若配对强度 $G$ 低于某一临界阈值 $G_{\text{crit}}$，或者在高速转动的 Coriolis 反对齐驱动下有效阻塞增多，能隙方程将无法找到非零实数解，$\Delta$ 发生阶跃式归零。这种现象在早期文献中常被称为“超流—正常相变”。然而，原子核是由几十到几百个核子构成的介观有限系统，根本不具备大热力学极限（$N \to \infty$）的严格连续对称破缺相变。**BCS 临界塌缩纯粹是固定平均场拟设波函数破缺粒子数对称性所产生的人为数学截断假象。** 若采用严格守恒粒子数的投影 BCS（PBCS）、变分后投影（VAP）或 Richardson 严格对角化方法，配对关联在所谓临界区始终保持平滑演化，弱配对极限下物理体系自然过渡为强烈的动态配对振动（pairing vibration）与量子涨落，核内的两体配对张量 Expectation value 绝不会发生突变性断裂。

---

## 2.3.5 解析控制：两能级教学极限与集体响应的配对反馈

为了获得超越定性断言的严格解析控制，考察一个完全可解的对称两能级模型（Lipkin–Meshkov–Glick 型配对模型空间）[@book-suhonen-from-nucleons-to-nucleus]。该模型能够清晰呈现配对能隙的临界存在条件与渐近行为。

### 1. 两能级模型的严格解析推导

设系统仅由两个相同的单 $j$ 壳层组成，能量分别为 $\epsilon_1 = -\frac{1}{2}\varepsilon$ 与 $\epsilon_2 = +\frac{1}{2}\varepsilon$，壳层间距为 $\varepsilon$。每个单 $j$ 壳层的轨道对简并度为 $\Omega = (2j+1)/2$。设系统的平均核子数严格等于一个单壳层的容量，即 $\bar{n} = 2\Omega$。在无相互作用的非受扰基态下，下能级完全被 $2\Omega$ 个核子填满（$v_1 = 1, v_2 = 0$），上能级完全排空。

引入单极配对散射相互作用，假定对散射矩阵元在两壳层间均为常数 $G$。根据 Suhonen 专著第 13.5 节的推导[@book-suhonen-from-nucleons-to-nucleus]：
由粒子—空穴镜像对称性，上下壳层的占据几率满足：
$$
v_1^2 + v_2^2 = 1 \implies v_2 = u_1, \quad v_1 = u_2.
$$
此时准粒子能量与自洽配对能隙在两壳层上严格相等：$E_1 = E_2 = E$，$\Delta_1 = \Delta_2 = \Delta = 2\Omega G u_1 v_1$。
能隙方程给出：
$$
\frac{2}{\Omega G} = \frac{1}{E_1} + \frac{1}{E_2} = \frac{2}{E} \implies E = \Omega G.
$$
考虑包含自能修正后的单粒子能量差 $\eta_1 \equiv \epsilon_1 - \lambda - \mu_1$。由粒子数条件与自能结构解出化学势 $\lambda = -\frac{3}{4}G$，进而求得自洽有效单粒子能量[@book-suhonen-from-nucleons-to-nucleus]：
$$
\eta_1 = -\frac{2\Omega \varepsilon}{4\Omega - 1} = -\eta_2 \equiv -\eta.
$$
根据准粒子能量本征方程 $E = \sqrt{\eta^2 + \Delta^2}$，配对能隙的解析表达式为：
$$
\Delta = \sqrt{E^2 - \eta^2} = \sqrt{(\Omega G)^2 - \left( \frac{2\Omega \varepsilon}{4\Omega - 1} \right)^2}.
$$
为了展示其临界行为，定义无量纲控制参数：
$$
x \equiv \frac{4\Omega - 1}{2} \frac{G}{\varepsilon}.
$$
则自洽配对能隙与占据振幅显式简化为令人瞩目的紧凑形式[@book-suhonen-from-nucleons-to-nucleus]：
$$
\Delta = \Omega G \sqrt{1 - \frac{1}{x^2}},
$$
$$
v_1 = \frac{1}{\sqrt{2}} \sqrt{1 + \frac{1}{x}}, \quad v_2 = \frac{1}{\sqrt{2}} \sqrt{1 - \frac{1}{x}}.
$$

### 2. 极限检验与临界配对阈值

这一严格解析解为检验物理极限提供了绝佳范本：
1. **临界阈值 $G_{\text{crit}}$：** 观察根式 $\sqrt{1 - 1/x^2}$ 可知，非平凡 BCS 能隙解存在的充要条件是 $x > 1$。由此解析导出临界配对相互作用强度：
   $$
   G_{\text{crit}} = \frac{2\varepsilon}{4\Omega - 1}.
   $$
   当 $G \le G_{\text{crit}}$ 时，$x \le 1$，能隙方程无非平凡实根，$\Delta \equiv 0$，此时 $v_1 = 1, v_2 = 0$，体系回退为无相互作用的 Hartree–Fock 粒子—空穴基态；
2. **强配对极限（$G/\varepsilon \gg 1$ 即 $x \to \infty$）：** 当配对相互作用远大于单粒子壳间距时，$\Delta \to \Omega G$，此时 $v_1 \to 1/\sqrt{2}, v_2 \to 1/\sqrt{2}$。上下两个能级被核子均等平分占据，体系呈现完全最大化的超流相干态。
3. **无相互作用极限（$\Delta \to 0$）：** 当 $G \to G_{\text{crit}}^+$ 时，$\Delta \to 0$。两能级模型平滑过渡到不占据激发的极值点。

必须再次声明：**上述两能级解析解是高度简化的均场教学控制模型，绝不能直接包装为真实形变重核的微观计算结果。** 在真实核体系中，单粒子轨道密集且非简并，变形势阱诱发 Nilsson 轨道的分裂与复杂交叉，单粒子轨道能差分布不均匀，且残余作用包含四极—四极等高阶多极分量，真实原子核中的配对演化远比简化的两能级相变平缓得多。

### 3. 配对对集体转动与动态响应的多重调制

建立严格的准粒子理论后，便可透彻理解配对关联对宏观集体激发（如三轴核转动与摆动）的深刻调控机制：
1. **激发态能量的提升：** 由于单准粒子本征能为 $E_k = \sqrt{\xi_k^2 + \Delta^2}$，费米面附近的任意粒子—空穴激发均被施加了 $\ge 2\Delta$ 的两准粒子相干阈值。这大幅压低了低能区域内禀态的态密度，使得集体激发（如形状振动或基带转动）免受低能杂乱单粒子态的剧烈阻尼，从而保持高相干性的集体运动带；
2. **微观跃迁相干因子（Coherence Factors）：** 当在准粒子基底中展开电磁跃迁或多极算符时，由于正反向配对组分的干涉，跃迁矩阵元被相干因子 $(u_k v_{k^\prime} \mp v_k u_{k^\prime})$ 强烈调制。电四极跃迁（$E2$）通常受到相干增强，而磁偶极跃迁（$M1$）在某些特定对态上受到相消抑制[@book-suhonen-from-nucleons-to-nucleus]；
3. **集体转动惯量的配对压低：** 在 Inglis–Belyaev 显式曲率公式中，转动惯量分量正比于矩阵元平方除以双准粒子激发能 $\sum_{k k^\prime} \frac{|\langle k | \hat{j}_x | k^\prime \rangle|^2 (u_k v_{k^\prime} - v_k u_{k^\prime})^2}{E_k + E_{k^\prime}}$。由于分母包含了 $E_k + E_{k^\prime} \ge 2\Delta$，且分子受到相干因子干涉，使得超流核的集体转动惯量显著低于经典刚体转动惯量（通常仅为刚体值的 $30\% \sim 50\%$）。

然而，这一物理图像再次提示我们在第 2.6 节讨论势能面与动力学惯量时必须保持审慎：**转动惯量的大小是单粒子壳结构、配对能隙 $\Delta$、形状形变度 $\beta, \gamma$ 以及四极残余相互作用联合作用的微观响应函数，不能简单断言“只要改变配对能隙 $\Delta$，就能唯一线性调节转动惯量”；同样，更不能在没有微观两体动力学计算的情况下，把转动惯量的偏离盲目归咎于配对的彻底消失。** 这一自洽完整的微观配对框架，构成了后续章节深入剖析形变核激发、手征带双重态以及高自旋进动动力学的不可动摇的物理基石。
