---
type: research-note
title: "A130重写研学：投影选择定则、度规子空间截断与对称性恢复边界"
aliases: [A130 projection selection rules and metric truncation boundaries]
created: 2026-11-13
updated: 2026-11-13
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "G81父内容审查、第2.5节起草与附录B代数核查"
promotion_target: ""
evidence_sources: [book-bohr-mottelson-nuclear-structure-vol2, bohr-1952-surface-particle-coupling, bohr-mottelson-1953-collective-individual-original, book-raduta-coherent-states, book-suhonen-from-nucleons-to-nucleus]
tags: [A130, doctoral-thesis, projection, symmetry-restoration, selection-rules, metric-truncation, nonorthogonal]
---

# 投影算符代数、度规子空间截断与破缺参考态的真实物理边界

## Research Trigger

在第2.5节与附录B的写作与父级审查中，针对微观破缺参考态投影和非正交度规代数梳理出六项易被模糊或错误扩展的理论边界：
1. 轴对称内禀投影 $K=0$ 不限制实验室磁量子数 $M$（$M \in \{-I, \dots, +I\}$），$M=0$ 仅是计算重叠核时的简便规范分量；
2. 轴对称带仅含偶自旋 $I = 0, 2, 4, \dots$ 的选择定则源自内禀波包在绕垂直主轴转动 $\pi$ 下的离散对称性（$R_{y, \text{intr}}(\pi) |\Phi\rangle = + |\Phi\rangle$），空间反演宇称 $\hat{\Pi}$ 本身不能单独选择偶自旋；
3. 角动量投影不单独推出严格的 $I(I+1)$ 刚体转子能谱，后者需要强变形、小倾角波包重叠急剧衰减以及转动能二阶展开等额外的动力学和绝热条件；
4. 度规矩阵的真正零范数冗余（$d_\alpha = 0$）与微小非零本征值的数值截断（$d_\alpha < \epsilon_{\text{cut}}$）具有根本区别，标准厄米本征问题仅在保留的主有效子空间内部等价；
5. 全哈密顿量常数平移在非正交基下必须对应 $H \to H + c N$，本征能量严格平移且本征子空间严格守恒；
6. 复非正交两态模型中代数无序根对、有序能谱与对称/反对称分类的区分，以及同时实化充要条件 $\operatorname{Im}(k S^*) = 0$ 中 $S=0$ 分支的严格补全。

本页系统沉淀上述推导与证据边界，作为正文第2.5节、第3.5节与附录B的理论支撑。

## Grounded Evidence

| 原件/核查本轮 locator | 载体路径与 SHA-256 | 支持范围与边界核对 |
|---|---|---|
| [[book-bohr-mottelson-nuclear-structure-vol2]]，PDF pp. 23–27, 197–215 | `raw/books/nuclear structure Ⅱ_Bohr, Mottelson.pdf`<br>`46015a1401bcbdd40d4fd7267a1b066b4aef662050dcf35693e4e3a10a6d417a` | World Scientific 1998 再版（1999 重印，PDF p. 6 版权页确认）。Section 4-1 明确转动自由度起源于内禀形变对连续空间转动不变性的破缺；Section 4-5e 纯转子高自旋近似 |
| [[bohr-1952-surface-particle-coupling]]，pp. 8–18 | `raw/papers/gpt/query/20261108-r3-bohr-1952/originals/bohr-1952-mfm26-14.pdf`<br>`aa1abb0377c020ecae64eb7735cf5156988682feb7f06617a8957d7d68ad818d` | Dan. Mat. Fys. Medd. 26, no. 14 (1952)。Section II 内禀体轴参考系构建与转动动能分离 |
| [[bohr-mottelson-1953-collective-individual-original]]，pp. 24–36 | `raw/papers/gpt/query/20261108-r3-bohr-1952/originals/bohr-mottelson-1953-mfm27-16.pdf`<br>`b0501e3e098869a7fb14527a3dc8c9b80444affdb265394a928e0794ae708945` | Dan. Mat. Fys. Medd. 27, no. 16 (1953)。强耦合绝热波函数、轴对称波包展开与对易对称性 |
| [[book-raduta-coherent-states]]，PDF pp. 54–55, 189–195 | `raw/books/nuclear structure with coherent states_Raduta.pdf`<br>`98b057e53e323b0f4781060ad5ae4a8c045ac36b32c0650033953360d951aca3` | Springer (2016)。Section 3.3（印刷 p. 43，PDF p. 54）Eqs.(3.3.3)–(3.3.5) 给出标准三维角动量投影算符 $P^J_{MK} = \frac{2J+1}{8\pi^2} \int D^{J*}_{MK}(\Omega) \hat{R}(\Omega) d\Omega$ 定义；Chapter 6 Section 6.1 CSM 相干态投影展开与度规矩阵元求解 |
| [[book-suhonen-from-nucleons-to-nucleus]]，PDF pp. 38–41, 44–45 | `raw/books/From nucleons to nucleus concepts of microscopic .pdf`<br>`4d4b799b8d91784638bac29e0749fe08ba9720f067fd76317f7e256d6f8cd27c` | Springer (2007)。Section 2.1.2 Wigner $D$ 矩阵欧拉角定义与单张积性质；Section 2.2 Wigner-Eckart 定理 |

注：本页推导中的非正交 Ritz 变分方程、能量规范平移代数与复两态因式分解属于多体量子代数直接推导，不伪引任何未收录的外部教材。

## Provisional Reasoning

### 1. 轴对称投影的角积分与偶自旋选择定则

设变形单体参考态 $|\Phi\rangle$ 具备绕内禀 $z$ 轴的连续轴对称性，即 $\hat{J}_{z, \text{intr}} |\Phi\rangle = 0 \implies K = 0$。

角动量投影算符定义为：
$$
P^I_{MK} = \frac{2I+1}{8\pi^2} \int_0^{2\pi} d\phi \int_0^\pi \sin\theta \, d\theta \int_0^{2\pi} d\psi \, D^{I*}_{MK}(\phi, \theta, \psi) \hat{R}(\phi, \theta, \psi).
$$
对于 $K = 0$，表示矩阵分解为 $D^{I*}_{M0}(\phi, \theta, \psi) = d^I_{M0}(\theta) e^{i M \phi}$，对内禀角 $\psi$ 的积分直接给出因子 $2\pi$。投影态矢化为：
$$
P^I_{M0} |\Phi\rangle = \frac{2I+1}{4\pi} \int_0^{2\pi} d\phi \, e^{i M \phi} e^{-i \phi \hat{J}_z / \hbar} \int_0^\pi \sin\theta \, d\theta \, d^I_{M0}(\theta) e^{-i \theta \hat{J}_y / \hbar} |\Phi\rangle.
$$
在此必须纠正两个常见误区：
- **$M$ 的自由度**：上式清楚表明，态矢依然包含对实验室方位角 $\phi$ 的积分算符，它保证了态矢具有确定的实验室磁量子数 $M \in \{-I, -I+1, \dots, +I\}$。在无外场的各向同性空间中，全部 $2I+1$ 个磁子态严格简并。$M=0$ 绝非投影态非零的必要条件，只是在计算对角度规元时为简便所选择的一个代表性取向；
- **自旋选择定则源自内禀离散转动对称性**：空间反演宇称 $\hat{\Pi}$ 本身不能单独导出偶自旋。要求基带只含偶自旋 $I = 0, 2, 4, \dots$ 的物理前提是内禀参考波包满足绕垂直主轴（内禀 $y$ 轴）旋转 $\pi$ 的不变性（即离散 $D_2$ 转动点群对称性或正旋称 $r = +1$）：
$$
\hat{R}_{y, \text{intr}}(\pi) |\Phi\rangle = \exp(-i\pi \hat{J}_{y, \text{intr}} / \hbar) |\Phi\rangle = + |\Phi\rangle.
$$
利用结合规则 $P^I_{MK} \hat{R}(\Omega) = \sum_{K'} D^I_{K K'}(\Omega) P^I_{M K'}$（可由 $P^I_{MK} = \sum_\alpha |IM\alpha\rangle \langle IK\alpha|$ 一行验算）：
$$
P^I_{M0} |\Phi\rangle = P^I_{M0} \hat{R}_{y, \text{intr}}(\pi) |\Phi\rangle = D^I_{00}(0, \pi, 0) P^I_{M0} |\Phi\rangle = d^I_{00}(\pi) P^I_{M0} |\Phi\rangle = (-1)^I P^I_{M0} |\Phi\rangle.
$$
由此导出明确选择定则：若 $I$ 为奇数，$P^I_{M0} |\Phi\rangle \equiv 0$ 恒等于零；非零投影态只能具有偶数自旋（$I = 0, 2, 4, \dots$）。偶 $I$ 投影态是否实际非零，还取决于内禀参考态中该自旋分量的展开权重（若波包中某偶 $I$ 振幅为零，则投影仍为零）。

当且仅当两端夹上轴对称内禀态计算重叠度规核时，外层 $\phi$ 积分才因轴对称性化简为 $2\pi$，使度规核化为一维倾角积分：
$$
N^I_{00} = \langle \Phi | P^I_{00} | \Phi \rangle = \frac{2I+1}{2} \int_0^\pi \sin\theta \, d\theta \, d^I_{00}(\theta) \langle \Phi | \exp(-i \theta \hat{J}_y / \hbar) | \Phi \rangle.
$$

### 2. 角动量投影与转子能谱的动力学距离

在单 $K=0$ 投影近似下，态能量由核之比精确给出：
$$
E(I) = \frac{H^I_{00}}{N^I_{00}} = \frac{\int_0^\pi \sin\theta \, d\theta \, d^I_{00}(\theta) \langle \Phi | \hat{H} \exp(-i \theta \hat{J}_y / \hbar) | \Phi \rangle}{\int_0^\pi \sin\theta \, d\theta \, d^I_{00}(\theta) \langle \Phi | \exp(-i \theta \hat{J}_y / \hbar) | \Phi \rangle}.
$$
要从该积分比值导出行如 $E(I) \approx E_0 + \frac{\hbar^2}{2\mathcal{J}_{\text{eff}}} I(I+1)$ 的转子能谱，必须满足严格的物理近似条件：
1. **强变形条件**：核具有显著的静态四极变形，使得内禀态转动重叠函数 $\langle \Phi | e^{-i\theta \hat{J}_y/\hbar} | \Phi \rangle$ 随转角 $\theta$ 急剧衰减，仅在 $\theta \approx 0$ 与 $\theta \approx \pi$ 附近呈现狭窄的高斯型峰包；
2. **绝热局域展开**：在重叠峰包覆盖的小转角区域内，哈密顿量核与度规核的比值可以按转动能量二次型做收敛展开；
3. **单带与低自旋限制**：体系不存在显著的三轴 $\gamma$ 涨落、准粒子顺排带交叉或高自旋离心反配对效应。

若上述条件不满足（如过渡核、$\gamma$ 软核或交叉区），角动量投影态计算的能谱将严重偏离 $I(I+1)$。角动量投影本身只是恢复运动学连续对称性的算符操作，并不预设也不单独保证刚体动力学能谱。

### 3. 度规度量空间的真冗余与有限截断

在非正交基矢集合 $\{ |\phi_i\rangle \}_{i=1}^n$ 下，度规矩阵 $N_{ij} = \langle \phi_i | \phi_j \rangle$ 满足厄米半正定性。谱分解为：
$$
N = U D U^\dagger, \quad D = \operatorname{diag}(d_1, \dots, d_n), \quad d_\alpha \ge 0.
$$
必须严格区分两类本征模式：
- **精确零模（$d_\alpha = 0$）**：由算符或基矢的代数线性相关性引起（如前述奇自旋 $I$ 投影态）。其态矢范数严格为零，属于真正的多余冗余，必须精确剔除；
- **小范数模式（$d_\alpha > 0$）**：在有限基底展开中，某些态的本征值极小但严格为正。在数值计算中，过小的 $d_\alpha$ 会导致求逆条件数急剧恶化。引入有限阈值 $\epsilon_{\text{cut}}$ 舍弃 $d_\alpha < \epsilon_{\text{cut}}$ 属于**有界子空间截断近似**（numerical truncation），而非数学上的零模剔除。

在保留的 $m$ 维主有效子空间内构造规范正交基：
$$
|\chi_\alpha\rangle = \frac{1}{\sqrt{d_\alpha}} \sum_{i=1}^n (U_{\text{red}})_{i\alpha} |\phi_i\rangle \quad (\alpha = 1, \dots, m),
$$
原 Hill-Wheeler 广义本征方程转化为标准厄米本征问题：
$$
\mathcal{H} \mathbf{v} = E \mathbf{v}, \quad \mathcal{H} = D_{\text{red}}^{-1/2} U_{\text{red}}^\dagger H U_{\text{red}} D_{\text{red}}^{-1/2}.
$$
保留空间的投影驻值方程 $U_{\text{red}}^\dagger (H - E N) U_{\text{red}} D_{\text{red}}^{-1/2} \mathbf{v} = 0$ 等价于上述无度规标准厄米本征问题。该等价性严格限定于保留的主有效子空间内部；全空间中的残差矢量 $(H - EN)\mathbf{c}$ 一般并不逐行精确为零，除非保留子空间在哈密顿量作用下恰好闭合。在数值计算中必须测试能谱对截断阈值 $\epsilon_{\text{cut}}$ 变化的收敛性与稳定性，不能随意使用未经检验的经验阈值。

### 4. 能量规范平移不变性与简并子空间

若全物理哈密顿量整体平移标量势能零点 $\hat{H}' = \hat{H} + c \hat{\mathbf{1}}$（$c \in \mathbb{R}$）：
矩阵元变为：
$$
H'_{ij} = \langle \phi_i | (\hat{H} + c\hat{\mathbf{1}}) | \phi_j \rangle = H_{ij} + c N_{ij} \implies H' = H + c N.
$$
代入广义本征方程：
$$
(H + c N) \mathbf{c}' = E' N \mathbf{c}' \iff H \mathbf{c}' = (E' - c) N \mathbf{c}'.
$$
这证明了：
1. 本征值严格平移 $E' = E + c$，相对能级间距 $\Delta E$ 严格不变；
2. 特征零空间 $\ker(H' - E' N) = \ker(H - E N)$ 完全相同，本征子空间严格守恒。在非简并情形下本征矢量满足 $\mathbf{c}' = \mathbf{c}$；在简并子空间中可在简并流形内选取相同的基底矢量；
3. 若错误执行对角平移 $H' = H + c \mathbf{1}$，设 $E'$ 为平移后的实际能量，久期方程变为 $\det(H + c \mathbf{1} - E' N) = 0$。若定义相对于平移量的能量 $\varepsilon \equiv E' - c$，方程则写作 $\det[H + c(\mathbf{1} - N) - \varepsilon N] = 0$。非对角项 $c(\mathbf{1} - N)$ 作为人为扰动，在度规存在非对角元时一般会虚假改变能级相对间距，并可能引发非物理的态漂移或态混合。

### 5. 复非正交两态久期解与实化定理补全

设手征两阱基矢为 $|L\rangle$ 与 $|R\rangle = \mathcal{C}|L\rangle$。在系统满足反幺正手征对称性 $[\hat{H}, \mathcal{C}] = 0$ 且 $\hat{H}^\dagger = \hat{H}$ 的前提下：
$$
h \equiv \langle L|\hat{H}|L\rangle = \langle R|\hat{H}|R\rangle \in \mathbb{R}, \quad S \equiv \langle L|R\rangle \in \mathbb{C}, \quad k \equiv \langle L|\hat{H}|R\rangle \in \mathbb{C}.
$$
广义久期方程 $\det(H - E N) = 0$ 展开为关于 $E$ 的一元二次方程：
$$
(1 - |S|^2) E^2 - 2 \left[ h - \operatorname{Re}(k S^*) \right] E + \left( h^2 - |k|^2 \right) = 0.
$$
判别式的四分之一（$\Delta / 4$）严格化为平方和：
$$
\frac{\Delta}{4} \equiv \left[ h - \operatorname{Re}(k S^*) \right]^2 - (1 - |S|^2)(h^2 - |k|^2) = \left[ \operatorname{Re}(k S^*) - h |S|^2 \right]^2 + (1 - |S|^2) |h S - k|^2 \ge 0.
$$
由于 $|S| < 1$，$\Delta / 4 \ge 0$ 恒成立，方程有两个实数代数本征根构成的无序对 $\{E_+, E_-\}$：
$$
E_{\text{high}/\text{low}} = \frac{h - \operatorname{Re}(k S^*) \pm \sqrt{ \left[ \operatorname{Re}(k S^*) - h |S|^2 \right]^2 + (1 - |S|^2) |h S - k|^2 }}{1 - |S|^2},
$$
其中 $+$ 号对应能量上限 $E_{\text{high}}$，$-$ 号对应能量下限 $E_{\text{low}}$。

**同时实化充要条件（定理 B.4 完整证明）**：
在全局重定相 $|L\rangle \to e^{i\phi} |L\rangle$ 下，$S \to e^{-2i\phi} S$，$k \to e^{-2i\phi} k$，组合积 $k S^*$ 严格保持定相不变。
同时实化（存在 $\phi$ 使 $S', k' \in \mathbb{R}$）的充要条件为：
$$
\operatorname{Im}(k S^*) = 0.
$$
完整分类分支：
- **若 $S \ne 0$**：$\operatorname{Im}(k S^*) = 0$ 说明 $k$ 与 $S$ 具有相同或相反辐角。选取 $\phi = \frac{1}{2} \arg S$，变换后 $S' = |S| \in \mathbb{R}$，$k' = (k S^*) / |S| \in \mathbb{R}$，同时实化；
- **若 $S = 0$ 且 $k \ne 0$**：此时两态正交，$S = 0 \in \mathbb{R}$ 自动为实数，$\arg S$ 无定义，但 $\operatorname{Im}(k \cdot 0^*) = 0$ 平凡满足。选取 $\phi = \frac{1}{2} \arg k$，变换后 $k' = |k| \in \mathbb{R}$ 且 $S' = 0 \in \mathbb{R}$，同时实化；
- **若 $S = 0$ 且 $k = 0$**：两态正交且无耦合，对任意相位 $\phi$ 均有 $S'=0, k'=0$，平凡实化。

在实化条件下（取实相使 $S, k \in \mathbb{R}$），无序特征根简化为：
$$
E_s = \frac{h + k}{1 + S}, \quad E_a = \frac{h - k}{1 - S}.
$$
两根的相对代数差为 $E_a - E_s = \frac{2(h S - k)}{1 - S^2}$。按基矢对称/反对称分类，对称态 $|\psi_s\rangle$ 对应 $E_s$，反对称态 $|\psi_a\rangle$ 对应 $E_a$。在实轴上按能量从低到高排列：
$$
E_{\text{low}} = \min(E_s, E_a), \quad E_{\text{high}} = \max(E_s, E_a).
$$
物理非负能隙恒由绝对值给出：
$$
\Delta E_{\text{phys}} \equiv E_{\text{high}} - E_{\text{low}} = |E_a - E_s| = \frac{2|h S - k|}{1 - S^2}.
$$
若 $\operatorname{Im}k \ne 0$，物理非负能隙为：
$$
\Delta E_{\text{phys}} = \frac{2\sqrt{ (\operatorname{Re}k - h S)^2 + (1 - S^2)(\operatorname{Im}k)^2 }}{1 - S^2}.
$$

## Assumptions

1. 体系全核相互作用哈密顿量由强相互作用与电磁相互作用支配，忽略弱相互作用宇称破坏；
2. 投影所作用的对象是破缺对称性的微观自洽平均场单参考波包（或相干态），而非所有内禀坐标形式；
3. 非正交双态模型假定低能物理有效子空间可由两个手征对称相关的定域波包主导；
4. 轴对称角动量投影导出刚体转子谱假定波包具有强四极形变，且重叠函数小倾角局域展开收敛。

## Competing Explanations

1. **近似投影能谱 vs 大振幅动态涨落**：单参考态角动量投影所呈现的转子能谱属于受限试探空间的变分结果；与其竞争的微观假说包括 5DCH 或 GCM 包含的大振幅四极形变动力学涨落，以及三轴势能面极浅软核中的振动耦合机制；
2. **理想刚体转子 vs 动力学涌现偏离**：刚体转子能谱 $E(I) \approx E_0 + \frac{\hbar^2}{2\mathcal{J}_{\text{eff}}} I(I+1)$ 是在强形变和重叠函数陡峭高斯峰等绝热展开条件下的极限行为。真实变形核中的科里奥利反配对效应、准粒子排列引起的带交叉和非轴对称离心软化是造成偏离纯转子谱的本质物理原因；
3. **偶自旋选择的二度轴机制 vs 空间宇称混淆**：偶自旋序列由内禀参考波包在绕垂直主轴转动 $\pi$ 下的离散点群对称性（$R_{y, \text{intr}}(\pi) = +1$）严格导出，不可与空间反演宇称 $\hat{\Pi}$ 机制混淆。

## Transfer Conditions

1. **固定表示类的角域积分**：式中的 $8\pi^2$ 欧拉角积分与 Peter–Weyl 正交性仅在固定核子数奇偶的单一表示类（偶 $A$ 核对应整数群 $\mathrm{SO}(3)$，奇 $A$ 核对应覆盖群 $\mathrm{SU}(2)$）内部成立，不声称跨整数/半整数表示类同时具有单值正交性；
2. **度规严格正定子空间**：Hill-Wheeler 广义本征方程与久期行列式 $\det(H - EN) = 0$ 仅在剔除精确零模冗余并限制于度规严格正定（$N > 0$）的线性独立子空间内迁移使用；
3. **有限试探空间的 Ritz 变分定位**：投影态能量由受限投影空间的变分驻值确定，不声称其在全多体希尔伯特空间中的残差逐行恒为零；
4. **两态实对称退化条件**：定理 B.4 的实对称两态模型仅在系统满足定相不变量 $\operatorname{Im}(kS^*) = 0$ 时方可严格迁移适用。

## Failure Conditions

1. 若将轴对称 $K=0$ 误同化为实验室磁量子数 $M=0$，则会丢失全部 $2I+1$ 个简并磁子能级结构；
2. 若将偶自旋选择定则归因于空间宇称 $\hat{\Pi}$，则无法解释为什么只有具备内禀二度轴对称性（$R_{y, \text{intr}}(\pi) = +1$）的核才展现偶自旋带；
3. 若宣称角动量投影本身等价于严格刚体转子谱，则会掩盖微观动力学涨落、形变柔软度与顺排跃迁的物理实质；
4. 若将微小非零度规本征值一律斥为虚假零模并宣称截断后严格等价原全空间，则会忽视数值截断的近似本质与收敛性要求；
5. 若在非正交基下执行对角平移 $H \to H + c \mathbf{1}$，则会导致能谱相对间距产生非物理的常数依赖与态混合；
6. 若在同时实化证明中遗漏 $S=0$ 分支，则会导致定理在两态正交极限下因辐角无定义而逻辑断裂。

## Falsification or Reverse Tests

1. **数值 2x2 逆向代数核算（T13 独立审查）**：在复参数 $h=1, S=0.3+0.2i, k=0.4+0.1i$ 设定下，广义久期方程判别式的四分之一精确为 $\Delta/4 = 0.0175 \ge 0$，两个实本征根约为 $0.83645$ 与 $1.14056$；施加势能平移 $H \to H + 2N$ 后各本征根严格平移 $+2$；在 $S=0, k=0.4+0.1i$ 条件下取 $\phi = \frac{1}{2}\arg k$ 成功实现 $k' \in \mathbb{R}$ 与 $S'=0 \in \mathbb{R}$，数值代数测试全部闭环；
2. **反例与实核动力学边界**：上述数值逆向核查仅确立了非正交 $2 \times 2$ 广义本征方程的数学自洽性与下界，并不等同于实核动力学的微观检验。未开展全组态空间微观相互作用（如推转微观泛函或壳模型）的大尺度投影计算，不能将纯代数解冒充为真实多体谱学事实。

## Open Questions

1. **数值截断阈值 $\epsilon_{\text{cut}}$ 的收敛性**：在连续三轴形变与多组态相互作用投影中，度规本征值谱从小正值向零平滑延伸，截断阈值选取的物理稳定性区间仍需系统数值标定；
2. **全空间投影残差的定量评估**：受限投影子空间的 Ritz 变分解相对于全核多体哈密顿量 $\hat{H}$ 的残差矢量 $(H - EN)\mathbf{c}$ 在高自旋区与带交叉区的模长演化仍待微观量化；
3. **真实核复重叠参量提取**：真实候选手征核（如 A~130 区奇奇核）微观波包之间的复重叠积分 $S$ 与隧穿元 $k$ 满足同时实化充要条件 $\operatorname{Im}(kS^*) \approx 0$ 的物理容差区间尚待定量第一性原理计算核验。

## Human Review

本研究笔记内容基于 G81 推导、T13 独立窄范围数学核算与父 GPT 审校意见完成，属于纯 Agent 内部交叉核验与自审沉淀。
截至 2026-11-13，本页无真实用户人工审核事件。
依据本知识库工作约定，`review_status: unreviewed` 仅记录审核历史状态，不参与检索排序、置信度计算或论文使用判断；本研究笔记不作“发布级认证”，客观科学有效性由 Agent 根据直接数学推导、文献原件证据与适用边界自主判定。

## Promotion or Rejection History

- 2026-11-13：由 G81 在完成第2.5节起草与附录B代数核查后正式建档，沉淀轴对称投影选择定则、度规子空间截断、能量规范平移与复两态实化分支的完整数学与物理边界。
- 2026-11-13：采纳 T13 独立数学审查与结构 lint 意见，补齐 Competing Explanations、Transfer Conditions、Falsification or Reverse Tests、Open Questions 与 Human Review 五个核心段落，明确 2x2 代数核查与实核动力学计算的明确边界。
