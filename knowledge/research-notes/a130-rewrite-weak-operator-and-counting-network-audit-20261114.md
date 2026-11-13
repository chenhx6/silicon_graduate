---
type: research-note
title: "A130重写：弱算符约定、计数网络与衰变微观接口核验"
aliases: [weak-operator-counting-network-audit, section-4-7-audit-20261114]
created: 2026-11-14
updated: 2026-11-14
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "G96 对第4.7节弱衰变多极算符、Ikeda差和定则、缓发中子级联网络与0vbb矩阵元的系统定点核验"
promotion_target: ""
evidence_sources: [dimitriou-2021-beta-delayed-neutron-reference-database, cirigliano-2018-leading-short-range-double-beta, engel-menendez-2017-double-beta-matrix-elements-review, doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives, wang-2026-axial-coupling-quenching-joint-effects, book-suhonen-from-nucleons-to-nucleus]
tags: [doctoral-thesis, section-4-7, weak-operators, ikeda-sum-rule, delayed-neutron, double-beta]
---

# 弱算符约定、计数网络与衰变微观接口核验

## Research Trigger

在 A130 博士论文前置重写稿（五章 39 节架构）的定点返修中，独立审核（Terra T21 窄审与父总控审查）对第 4.7 节（弱衰变与壳演化的互补探针）的数学递推、同位旋代数、相空间前因子、微观多体机制与弱相互作用有效场论边界提出了 8 项具体技术意见（T21-01 至 T21-08）。
为了保证正文 LaTeX 稿、证据台账及后续附录推演具有可追溯的科学证据链，本笔记系统核验原件 PDF 定位符，严格区分直接实验事实、作者理论解释、模型数值计算与本任务数学推导，并确立自洽的物理适用边界。

## Grounded Evidence

1. **直接实验报告与标准数据规范（Direct Experimental / Evaluated Data）：**
   - IAEA 评估参考数据库（Dimitriou et al. 2021, NDS 173, 144, PDF p. 4 / 8 / 11）：明确规范单中子发射几率 $P_{1n}$ 为恰发射一个中子的衰变分支比；定义全中子发射几率 $P_{\ge 1n} = \sum_{x \ge 1} P_{xn}$ 与平均中子多重度 $\langle M_n \rangle = \sum_{x \ge 1} x P_{xn}$；实验探测器响应矩阵 $R_{y|x}$ 受出射能谱与时间窗口调制，非折叠展开需基于精确蒙特卡罗标定。
   - Zhi et al. (2013, PRC 87, 025803, PDF p. 2 Eq. 2): 相空间积分率的参考常数取 $K = 6146\text{ s}$；Eq. (4) 给出了跃迁强度与比较半衰期 $ft$ 的关系，而非微分发射能谱。
   - 0+ -> 0+ 超允许 Fermi 衰变实验数据（Suhonen 2007, PDF p. 178）：纯同位旋矢量超允许跃迁的核矩阵元为 $\sqrt{2}$，经辐射修正后测定矢量耦合常数 $G_V = G_F V_{ud}$。

2. **作者理论解释与模型断言（Author Interpretation）：**
   - Cirigliano et al. (2018, PRL 120, 202001, PDF pp. 1–4): 在手征有效场论（Chiral EFT）框架下，当以非微扰方式求解两核子 $^1S_0$ 散射态时，单轻中微子势的紫外发散要求引入领头阶（LO）两核子短程接触算符 $V_{\nu,\mathrm{short}}^{(R)}$；作者指出电荷独立性破缺（CIB）核子--核子散射数据约束反项低能常数组合 $C_1 + C_2$，其对单一耦合常数 $g_\nu^{NN} = C_1$ 的数值估计基于 $C_1 \approx C_2$ 的唯象近似假定。
   - Engel & Menéndez (2017, RPP 80, 046301, PDF pp. 4, 17–18): $0\nu\beta\beta$ 衰变中的特征虚动量转移峰位于 $|\mathbf{q}| \sim 100\text{--}200\text{ MeV}/c$（对应短程 $1\text{--}2\text{ fm}$）；超流 BCS 态中 $T=1$ 配对相干增强核矩阵元，而母子核四极形变错位则显著压低内禀波函数重叠。
   - Zhi et al. (2013, PDF pp. 3–4): 弱轴电荷算符在核介质中受软介子交换流影响表现出显著的介质增强（$q_A \approx 1.266$），而空间矢量与张量算符则呈现不同程度的淬灭。

3. **微观模型数值计算（Model Calculations）：**
   - Wang et al. (2026, arXiv:2605.21218v1, PDF pp. 3–4, Fig. 1 & Table I): 对双闭壳核 $^{56}\mathrm{Ni}$、$^{100}\mathrm{Sn}$ 与 $^{132}\mathrm{Sn}$ 进行 RPA 与粒子-振动耦合（PVC）计算。对于 $^{56}\mathrm{Ni}$（涉及电子俘获），引入 PVC 打破了闭壳阻塞并在低能区开通微弱跃迁；但对于 $^{132}\mathrm{Sn}$，在采用 SGII Skyrme 参数时，即便引入 PVC，其在物理 $Q_\beta$ 能窗内预测的 Gamow-Teller 强度依然严格为零（仅在 SkM* 参数下出现微弱低能尾部）。
   - Suhonen (2007, PDF p. 556, Eqs. 17.83–17.84): 在质中准粒子 Tamm-Dancoff 近似（pnQTDA）与准粒子随机相位近似（pnQRPA）中，主动粒子数之差的和定则为 $S_- - S_+ = 3(N_{\mathrm{act}} - Z_{\mathrm{act}})$；该公式要求模型空间包含成对完整的自旋-轨道劈裂伙伴轨道（如 $j_> = l + 1/2$ 与 $j_< = l - 1/2$），若伙伴轨道缺失，则单体求和定则在截断空间中被破坏。

4. **本任务推导与边界确立（Task Derivations）：**
   - 证明了相继缓发中子级联差分方程在任意非终止瞬态能级必须显式递减发射中子数：$\Pi_x(a) = \sum_{b, r} [\Gamma_{a\to b}^{(r)} / \Gamma_{\mathrm{tot}}(a)] \Pi_{x-r}(b)$（$x < 0$ 时置零），终态条件为 $\Pi_x(t) = \delta_{x0}$。
   - 明确了母核总衰变归一（$\sum I_\beta = b_\beta \le 1$）与条件 $\beta$ 衰变归一的数学关系，确立了非 $\beta$ 衰变道（裂变、带电粒子）在无门母衰变观测中的独立响应项。
   - 确立了在 $t_3(n) = +1/2, t_- |n\rangle = |p\rangle, [t_+, t_-] = 2 t_3$ 规范下的裸一体 Ikeda 差和定则，证明了非零自旋初态必须包含统计平均因子 $1/(2J_i + 1)$，并给出了常数有效淬灭 $q^2$ 缩放与两体流修正边界。
   - 澄清了 $0\nu\beta\beta$ 机制为核内两弱流顶点之间的一条轻 Majorana 虚中微子传播子，规范了相空间 $G_{0\nu} g_A^4$ 归一与单位一致性，界定了手征领头阶短程接触项的重整化自洽性前提。

## Provisional Reasoning

### 1. 级联退激吸收马尔可夫链与发射中子数递减递推

设前驱母核衰变布居子核处于连续谱上的瞬态能级 $a \in \mathcal{S}_T$。体系通过连续粒子发射（发射 $r$ 个中子，部分宽度 $\Gamma_{a\to b}^{(r)}$）或电磁辐射跃迁（$r=0$，部分宽度 $\Gamma_{a\to b}^{(0)}$）退激。
若 $\Pi_x(a)$ 定义为从状态 $a$ 出发的级联最终总共释放 $x$ 个中子的吸收概率，则体系在第一步跃迁至中间能级 $b$ 释放了 $r$ 个中子，后续级联必须且只能从能级 $b$ 释放剩余的 $x - r$ 个中子。因此，任意瞬态能级满足递推平衡方程：
$$
\Pi_x(a) = \sum_{b, r} \frac{\Gamma^{(r)}_{a \to b}}{\Gamma_{\mathrm{tot}}(a)} \Pi_{x-r}(b), \qquad \Pi_{x < 0}(a) \equiv 0.
$$
对于被定义为终止吸收的状态 $t \in \mathcal{S}_A$（在所选实验时间窗内不再发中子的束缚基态或超长寿命同核异能态），它不能再产生任何中子释放，故其固有吸收边界条件为：
$$
\Pi_x(t) = \delta_{x, 0}.
$$
若采用经典吸收马尔可夫链的基本逆矩阵 $\mathbf{N} = (\mathbf{I} - \mathbf{Q})^{-1}$，一种实现是采用累计发射中子数增广态 $(a,m)$（完整子核质量标签或生成函数也可保留计数，不要求冗余扩维），边携带中子增量 $r$ 更新至 $(b, m+r)$，终态为 $(c, x)$；或引入计数生成函数 $G_a(s) = \sum_{x=0}^\infty \Pi_x(a) s^x$，满足矩阵方程 $\mathbf{G}(s) = \mathbf{M}(s) \mathbf{G}(s) + \mathbf{R}_0$。若状态未增广且仅在终态矩阵 $\mathbf{R}$ 上按单步标记 $x$，则无法记录早期步骤的中子发射历史。

### 2. 母衰变总分支比归一与条件几率

母核基态在弱相互作用衰变中直接馈送子核激发态 $i$ 的无量纲概率记为 $I_\beta(i)$。由于母核可能存在竞争衰变通道（如极丰中子重核区的自发裂变、近质子滴线区的 $\alpha$ 衰变或带电粒子发射），母核弱衰变总分支比满足：
$$
\sum_i I_\beta(i) = b_\beta \le 1.
$$
按每次母核总衰变归一的 $\beta$ 缓发 $x$ 中子发射净分支比为：
$$
P_{xn}^{(\beta;\mathrm{parent})} = \sum_i I_\beta(i) \Pi_x(i), \qquad \sum_{x \ge 0} P_{xn}^{(\beta;\mathrm{parent})} = b_\beta.
$$
当 $b_\beta>0$ 时，按条件 $\beta$ 衰变事件归一的中子发射几率定义为：
$$
P_{xn}^{(\beta \mid \beta)} = \frac{P_{xn}^{(\beta;\mathrm{parent})}}{b_\beta} \quad (b_\beta > 0), \qquad \sum_{x \ge 0} P_{xn}^{(\beta \mid \beta)} = 1.
$$
在无门控母衰变实验中，观测记录的中子多重度分布受所有衰变道共同贡献：
$$
p_y^{\mathrm{obs}} = \sum_x R_{y|x} P_{xn}^{(\beta;\mathrm{parent})} + p_y^{\mathrm{non\text{-}\beta}}.
$$
若母核存在自发裂变，裂变本身释放瞬发中子（平均多重度可达 $2\text{--}4$），必须计入 $p_y^{\mathrm{non\text{-}\beta}}$ 项，绝对不可将自发裂变中子误作 $\beta$ 缓发中子，亦不可将非 $\beta$ 衰变默认当作 $x=0$ 无中子模式。

### 3. 裸一体 Ikeda 差和定则与初态自旋平均

在单核子同位旋空间中，采用如下标准物理约定（与第 2.7 节严格一致）：
$$
t_3 |n\rangle = +\frac{1}{2} |n\rangle, \quad t_3 |p\rangle = -\frac{1}{2} |p\rangle; \qquad t_- |n\rangle = |p\rangle, \quad t_+ |p\rangle = |n\rangle.
$$
在此约定下，$\beta^-$ 衰变将中子转变为质子，对应降阶算符 $t_-$，核系统的总同位旋第三分量 $T_3 = (N - Z)/2$ 降低 1。同位旋阶梯算符的换位子为：
$$
[t_+, t_-] = 2 t_3.
$$
定义裸单体 Gamow-Teller 算符为 $\hat{\boldsymbol{\beta}}^\mp_{GT} = \sum_{k=1}^A \boldsymbol{\sigma}(k) t_\mp(k)$。总跃迁强度定义为对所有可达末态的约化跃迁几率求和，并对初态自旋取统计平均：
$$
S_\mp \equiv \sum_{f_\mp} B(GT^\mp; J_i \to J_f) = \frac{1}{2J_i + 1} \sum_{f_\mp} |\langle f_\mp \| \sum_k \boldsymbol{\sigma}(k) t_\mp(k) \| J_i \rangle|^2 = \frac{1}{2J_i + 1} \sum_{M_i, f_\mp, M_f, \mu} |\langle f_\mp, M_f | \sum_k \sigma_\mu(k) t_\mp(k) | J_i, M_i \rangle|^2.
$$
利用中间态在无截断全 Hilbert 空间中的完备闭合性 $\sum_f |f\rangle \langle f| = \mathbf{I}$，算符代数给出：
$$
S_- - S_+ = \frac{1}{2J_i + 1} \sum_{M_i} \langle J_i, M_i | \sum_k \left( \boldsymbol{\sigma}(k) \cdot \boldsymbol{\sigma}(k) [t_+(k), t_-(k)] \right) | J_i, M_i \rangle.
$$
代入 $\boldsymbol{\sigma} \cdot \boldsymbol{\sigma} = 3$ 与 $[t_+, t_-] = 2 t_3$，求和给出 $6 \hat{T}_3 = 6 (N - Z)/2 = 3(N - Z)$。自旋平均因子 $\frac{1}{2J_i + 1} \sum_{M_i} 1 = 1$ 严格保持该系数。若缺失分母 $2J_i + 1$，对 $J_i = 1/2$ 的初态（如单核子）求和将得出 6 而非 3。
若对单体 GT 矩阵元引入唯象常数淬灭因子 $q \equiv g_A^{\mathrm{eff}} / g_A^{\mathrm{bare}}$，差和按二次方缩放为 $3 q^2 (N - Z)$；但在微观截断空间（如价空间壳模型或 RPA）中，差和的守恒严格要求包含完整的自旋-轨道劈裂对伙伴轨道（Suhonen 2007, Eqs. 17.83–17.84）。此外，手征有效场论中的两体弱轴流（2BC，介子交换流）打破了一体算符的简单对易子，带来额外的微观多体代数修正。

### 4. 守恒矢量流假设（CVC）的流守恒与禁戒形状因子代数关系

CVC 假说断言弱矢量流与同位旋电磁流构成同一守恒流的三态矢量（$\partial_\mu V^\mu_\pm = 0$）。
在零动量转移极限下，时间分量弱矢量荷 $\hat{T}_\pm = \int V_0^\pm d^3r$ 在核介质中不发生微观重整化（$g_V = 1$），从而保证了 Fermi 超允许跃迁矩阵元的模型无关几何代数表达式 $\sqrt{T(T+1) - T_z(T_z \pm 1)}$。
然而，流守恒的场论内涵远不止于零动量点：在有限动量转移下，CVC 提供了空间矢量流与特定禁戒跃迁形状因子之间的严格代数关系（例如在 Zhi 等 2013 的一阶禁戒分析中，依据 CVC 导出了矢量流矩阵元 $\xi' y$ 与电荷形状因子的固定联系）。但弱轴矢量流不满足严格守恒（仅满足 PCAC 轴矢流部分守恒），因此受强相互作用介质重整化显著淬灭或增强。不能将 CVC 窄化为“仅在零动量点有效”，亦不可外推为“所有弱相互作用矩阵元在核内均不受重整化”。

### 5. 微分能谱最低阶近似、量纲与修正常数对照

最低阶允许微分发射速率公式写作：
$$
\frac{d\lambda}{dW} = \frac{(G_F^{(E)})^2 |V_{ud}|^2 (m_e c^2)^5}{2\pi^3 \hbar} F(Z, W) p W (W_0 - W)^2 C(W).
$$
当 $G_F^{(E)}$ 采用 $\mathrm{MeV}^{-2}$ 单位（$\approx 1.16638 \times 10^{-11}\text{ MeV}^{-2}$），$m_e c^2$ 采用 $\mathrm{MeV}$，$\hbar$ 采用 $\mathrm{MeV}\cdot\mathrm{s}$，各无量纲变量 $W = E_e / (m_e c^2)$、$p = \sqrt{W^2 - 1}$ 时，前因子量纲自洽为 $\mathrm{s}^{-1}$。未加任何辐射与有限尺寸修正的前因子积分常数为：
$$
K_0 \equiv \frac{2\pi^3 \hbar \ln 2}{(G_F^{(E)})^2 |V_{ud}|^2 (m_e c^2)^5} \approx 6292\text{ s}.
$$
Zhi 等采用 $K=6146\text{ s}$；它与本任务所声明常数下的最低阶 $K_0\simeq6292\text{ s}$ 不同。比较时需核对弱耦合、辐射修正与强度定义，不能仅由二者数值差反推该文纳入了哪一项修正。同时，Zhi 等 2013 的 Eq. (4) 给出的是跃迁强度定义式，相空间积分是 Eq. (2)，不可将 Eq. (4) 误标为微分发射谱。

### 6. 粒子-振动耦合（PVC）在双闭壳核中的核区特异性

多体多孔激发与表面振动声子耦合（PVC）打破了纯 RPA 静态平均场的刚性阻塞，能够引起强度的拓扑重分配。但在不同核区表现出高度特异性：
根据 Wang 等（2026, arXiv:2605.21218v1）的微观计算：
- 在自共轭闭壳核 $^{56}\mathrm{Ni}$ 中（实验涉及电子俘获通道），PVC 将高能 GT 强度下移，在低能窗内产生了有限的解阻塞强度；
- 在极丰中子双闭壳核 $^{132}\mathrm{Sn}$ 中，对于广泛使用的 SGII Skyrme 相互作用，即便引入 PVC，其在物理 $Q_\beta$ 衰变能窗内预测的 GT 强度依然严格为零（仅在 SkM* 相互作用下产生延伸入能窗的微弱低能尾部）。实验上 $^{132}\mathrm{Sn}$ 的衰变半衰期实际上由一阶禁戒跃迁主导。
因此，严禁将解阻塞表述为在所有双闭壳核中均普遍成立的开通机制。

### 7. 轻 Majorana 中微子交换与手征有效场论短程接触项

标准 $0\nu\beta\beta$ 机制为核内两个核子弱流顶点之间交换一条虚 Majorana 中微子传播子（单一虚中微子线，而非两个虚中微子交换）。其因式分解半衰期公式：
$$
[T_{1/2}^{0\nu}]^{-1} = G_{0\nu} g_A^4 |M_{0\nu}|^2 \left| \frac{m_{\beta\beta}}{m_e} \right|^2.
$$
相空间因子 $G_{0\nu}$ 与矩阵元 $M_{0\nu}$ 必须配套一致（明确是否外提 $g_A^4$ 与核半径规范 $R = 1.2 A^{1/3}\text{ fm}$）。
Cirigliano 等（2018）基于手征有效场论指出，由于单中微子长程势在两核子 $^1S_0$ 散射下存在紫外发散，手征领头阶（LO）自洽重整化要求显式引入一个 $\Delta L = 2$ 的两核子短程接触算符 $V_{\mathrm{CT}}^{(R)}(\mathbf{r}_{12}) = -2 g_\nu^{NN}(R) \delta_R^{(3)}(\mathbf{r}_{12}) t_{1,-} t_{2,-}$。
核子--核子散射的电荷独立性破缺数据仅能约束特定低能常数组合（$C_1 + C_2$），唯有结合对称性假定（$C_1 \approx C_2$）或相容格点 QCD 匹配才能估算 $g_\nu^{NN}$，不能单凭电磁数据宣称唯一独立标定。

## Assumptions

1. 经典马尔可夫级联退激模型假设原子核激发能级的退激速率远快于前驱母核的弱衰变周期，且连续退激步之间无相干相位干涉。
2. 裸单体 Ikeda 差和定则严格依赖全 Hilbert 空间的完备闭合性与一体算符性质。
3. 微分 $\beta$ 能谱公式基于极低核子反冲极限（$m_e / M_N \to 0$）与点核库仑近似。
4. 轻 Majorana $0\nu\beta\beta$ 机制假定有效轻中微子质量项主导轻子数破坏通道。

## Competing Explanations

1. **缓发中子发射阈上发射的必然性误区：** 早期简化分析常将 $Q_\beta > S_n$ 能窗等同于必然发射中子；现代微观数据证实离心势垒阻碍与辐射 $\gamma$ 级联竞争使阈上相当大部分布居退激回到子核束缚基态。
2. **闭壳核解阻塞机制的普遍性假说：** 部分文献认为多体关联必定消除闭壳阻塞；但在极丰中子核 $^{132}\mathrm{Sn}$ 中，SGII 微观计算表明物理能窗内 GT 强度依然严格为零，衰变由一阶禁戒主导。
3. **电磁数据标定短程双贝塔接触算符的唯一性争议：** 电荷独立性破缺数据仅约束低能反项的特定线性组合，单凭电磁数据无法无条件分离出单一手征耦合 $g_\nu^{NN}$。

## Failure Conditions

1. 若缓发中子级联差分方程未扣除当前步骤释放的中子数 $r$（写作 $\Pi_x(b)$ 而非 $\Pi_{x-r}(b)$），则任何 $1n$ 发射路径均会被错误归为 $0n$。
2. 若将母核总衰变分支比归一（$b_\beta \le 1$）与条件 $\beta$ 归一混同，将导致多重度概率守恒失真。
3. 若裸算符 Ikeda 差和缺失初态自旋平均因子 $1/(2J_i+1)$，对 $J_i \ne 0$ 核态的求和值将出现非物理发散（如单核子得出 6）。
4. 若将手征领头阶短程接触算符与单 $\beta$ 衰变的两体弱轴流（2BC）同名混用，将混淆轻子数破坏与轻子数守恒通道的物理本质。

## Transfer Conditions

本笔记确立的吸收马尔可夫递推关系、初态自旋平均规范、电弱相空间量纲配套与手征 EFT 接触项重整化框架，可直接迁移至附录 D 的数学深入推导、附录 E 的反应网络分析以及第 5 章中子谱仪探测效率响应建模；迁移时需根据具体核素重新核定能级分离阈与自旋宇称。

## Validation Plan

1. 验证相继缓发中子吸收递推公式在边界条件下的自洽性：单一 $1n$ 步（$r=1$）衰变必须将目标中子数由 $x$ 递减为 $x-1$；
2. 验证裸 Gamow-Teller 算符求和在 $t_3(n) = +1/2, t_- |n\rangle = |p\rangle$ 规范下初态自旋平均的一致性，确保对 $J_i = 1/2$ 单核子系统差和严格为 3；
3. 验证未加辐射修正相空间常数 $K_0 \approx 6292\text{ s}$ 与Zhi 采用的参考常数 $K = 6146\text{ s}$ 的定义边界与量纲；
4. 验证轻 Majorana 中微子交换机制为单一虚中微子线，并核对手征 EFT 领头阶两核子短程接触项重整化自洽性前提。

## Falsification or Reverse Tests

1. **反向测试 1（未递减发射数）：** 若在递推中令 $\Pi_x(a) = \sum_b [\Gamma_{a\to b} / \Gamma_{\mathrm{tot}}(a)] \Pi_x(b)$，则纯 $1n$ 路径的 $\Pi_1(a)$ 计算结果为 0，而 $\Pi_0(a)$ 为 1，直接违背概率守恒与物理定义。
2. **反向测试 2（未除初态自旋统计权重）：** 若在 $S_\pm$ 中直接对磁量子数求和而不除以 $2J_i + 1$，则对自旋 $J_i = 1/2$ 初态求和值等于 6，无法与 $3(N-Z) = 3$ 几何和定则吻合。
3. **反向测试 3（CIB 单一标定假设）：** 若宣称核子--核子散射中的 CIB 数据能唯一确定 $g_\nu^{NN}$，则忽略了该数据仅提供反项线性组合约束，人为抹除了微观理论不确定度。

## Open Questions

1. 实验测得的有效 $q$ 值如何精确解耦两体弱介子交换流（2BC）与高能组态粒子-空穴截断（核芯极化）的各自份额？
2. 在复杂统计退激中，具有宽能级重叠的非正交共振态之间是否存在不可忽略的量子干涉项对中子-光子分支比产生微观调制？

## Human Review

- 本笔记由 G96 根据 Terra T21 窄审意见与父总控审查独立起草完成，所有引用与公式均经原件 PDF 定位符比对核实，未进行真实用户审核（human-reviewed 标记保持空缺，审核历史状态中立）。

## Promotion or Rejection History

- 2026-11-14 (R2)：响应父总控 R1 审查意见完成返修，修正 $S_\pm$ 约化强度定义中自旋平均的双重计入并统一 $t_\mp$ 对应关系；更新 Suhonen 真实 raw SHA256 值为 4d4b799b8d91784638bac29e0749fe08ba9720f067fd76317f7e256d6f8cd27c；规范 Cirigliano 接触势剥离形式为 $V_{\mathrm{CT}}^{(R)} = -2 g_\nu^{NN} \delta_R^{(3)} t_{1,-} t_{2,-}$；修正形变重整 GT 强度的组态依赖性与 $r$ 过程天体物理多因素共同影响边界；实读补全 Zhi 2013 PDF pp. 7, 9, 10, 11 定位符并更正 $u$ 为秩 1 轴流算符。
- 2026-11-14：由 G96 独立完成建立，严格吸收并响应 Terra T21 窄审（T21-01 至 T21-08）关于差分吸收网络递减指标、母核归一规范、全空间裸 Ikeda 差和定则自旋平均、CVC 流守恒界限、修正常数定义、Wang 2026 RPA/PVC 能窗特异性以及轻 Majorana 交换单中微子线与短程手征重整化条件的全部核验意见。

2026-11-14 总控追加核查：半满偶阶电相消不关闭所有奇秩磁矩阵元；$d>0$ 的结论限于任意源的唯一稳定定态；重根需保留单向交换反例。计数增广仅是一种实现，最终吸收归一与有限观测窗须分开。双端投影、FF 秩分块与可复现有限控制见 [[a130-rewrite-seniority-projection-open-network-boundaries-20261114]]。本条不是用户审核事件。
