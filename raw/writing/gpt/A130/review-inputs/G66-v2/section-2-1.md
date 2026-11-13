# 2.1 实验室对称性与张量语言

研究原子核低能激发与电磁跃迁，首先需要确立描述多体量子体系的参考系与对称性语言。原子核是由核子依靠自洽强相互作用紧密束缚的有限量子系统。在不受外加电磁场扰动的实验室自由空间中，核体系的运动由满足空间旋转与空间反演对称性的哈密顿量所支配。然而，核结构文献中经常并存两套叙事视角：一类是直接对应实验室谱学测量的参考系，能级具有确定的总自旋量子数 $I$、磁投影 $M$ 与空间宇称 $\pi$；另一类则是为了直观反映核物质空间排布而引入的形变内禀参考系，核态常被赋予几何形变参数与主轴角动量投影标号。

这两类表象若不加区分，容易在谱学分析与微观模型的比对中产生混淆。例如，为何偶偶核基态的实验室一阶静电四极矩为零，却能在跃迁中表现出明显的四极集体性？微观模型计算给出的非对角约化矩阵元正负号是否构成独立的物理检验判据？实验测得的跃迁速率与逆过程吸收强度之间的数值比例又源自何处？

澄清这些问题需要将几何直觉收敛于不可约球张量语言。本节从实验室哈密顿量的基本时空对称性出发，阐明磁子态简并与宇称守恒的内涵；通过 Wigner–Eckart 定理将电磁跃迁算符的几何取向与微观动力学结构解耦；由初态统计平均与末态求和推导约化跃迁几率及其互易因子；进而通过态矢量的整体规范重定相，分析单个非对角约化矩阵元与闭合矩阵元干涉网络在物理可测性上的本质分野，为后续讨论微观单粒子演化、形变平均场参考态以及绝对跃迁速率反演提供统一规范的理论基准。

---

## 2.1.1 空间对称性、角动量量子数与实验室简并

在没有外加电磁场或外在取向制备的环境中，孤立原子核的多体哈密顿量 $\hat{H}$ 具有空间平移、旋转与反演不变性。三维空间旋转群的生成元为体系的总角动量算符 $\hat{\mathbf{J}}$，具有物理作用量的量纲（常用单位为 $\hbar$），其笛卡尔分量满足李代数对易关系：
$$
[\hat{J}_x, \hat{J}_y] = i \hbar \hat{J}_z, \quad [\hat{J}_y, \hat{J}_z] = i \hbar \hat{J}_x, \quad [\hat{J}_z, \hat{J}_x] = i \hbar \hat{J}_y.
$$
为使角动量代数运算简洁，定义无量纲角动量算符 $\hat{\mathbf{j}} \equiv \hat{\mathbf{J}}/\hbar$，其分量服从对易子关系 $[\hat{j}_x, \hat{j}_y] = i \hat{j}_z$。由于三维旋转群 $\mathrm{SO}(3)$ 的万有覆盖群为单连通李群 $\mathrm{SU}(2)$，量子力学中的角动量本征表示允许整数与半整数两类解：偶偶核与奇奇核对应于 $\mathrm{SO}(3)$ 的张量表示，而奇 $A$ 核则对应于旋量表示（即 $\mathrm{SO}(3)$ 的双值射影表示）。算符 $\hat{\mathbf{j}}^2$ 与某一空间投影分量（通常选为实验室坐标系的 $z$ 轴分量 $\hat{j}_z$）对易，二者具有共同本征基矢 $|I, M\rangle$：
$$
\hat{\mathbf{j}}^2 |I, M\rangle = I(I+1) |I, M\rangle, \quad \hat{j}_z |I, M\rangle = M |I, M\rangle,
$$
其中 $I$ 为总自旋量子数（非负整数或半整数），$M \in \{-I, -I+1, \dots, I\}$ 为磁量子数。需要说明，算符 $\hat{\mathbf{J}}$ 带作用量单位 $\hbar$，而量子数 $I$ 与 $M$ 是无量纲纯标量；在建立转动哈密顿量或计算跃迁频率时，二者不可混用。

哈密顿量 $\hat{H}$ 的空间旋转不变性表明它与旋转群的所有生成元对易：$[\hat{H}, \hat{\mathbf{J}}] = 0 \implies [\hat{H}, \hat{\mathbf{j}}] = 0$。引入无量纲阶梯算符 $\hat{j}_\pm = \hat{j}_x \pm i \hat{j}_y$，显然满足 $[\hat{H}, \hat{j}_\pm] = 0$。若某一能态满足 $\hat{H} |I, M\rangle = E(I, M) |I, M\rangle$，则：
$$
\hat{H} (\hat{j}_\pm |I, M\rangle) = \hat{j}_\pm \hat{H} |I, M\rangle = E(I, M) (\hat{j}_\pm |I, M\rangle).
$$
由 $\hat{j}_\pm |I, M\rangle = \sqrt{I(I+1) - M(M \pm 1)} \, |I, M \pm 1\rangle$ 可知，只要该态非零，产生的新态仍是 $\hat{H}$ 的能量本征态且本征值完全相同。因此，对于任意给定的自旋量子数 $I$，该多重态中的全部 $2I+1$ 个磁子态 $M$ 必定具有相等的能量：
$$
E(I, M) = E(I), \quad \forall M \in \{-I, -I+1, \dots, I\}.
$$
这种由空间各向同性导致的能级简并称为磁子态简并。需要注意，能级简并不等于磁子态在物理上不可区分。在实验中，通过重离子熔合蒸发反应中的角动量转移、极化靶或激光光抽运，可以制备出磁子态布居不均等的核取向或核顺排系综。无外场仅仅意味着体系哈密顿量自身不包含打破各向同性的势能项，并不限制实际初态波函数的布居分布。

在空间反演变换下，宇称算符 $\hat{P}$ 将核子坐标与动量同时反向：$\hat{P} \mathbf{r}_k \hat{P}^\dagger = -\mathbf{r}_k$，$\hat{P} \mathbf{p}_k \hat{P}^\dagger = -\mathbf{p}_k$。轨道角动量与核子自旋在反演下保持不变，因而总角动量算符为轴矢量，满足 $\hat{P} \hat{\mathbf{j}} \hat{P}^\dagger = \hat{\mathbf{j}}$。在本节讨论的核结构近似框架中，哈密顿量由强相互作用与电磁相互作用主导，二者均严格守恒空间反演宇称，因此满足 $[\hat{H}, \hat{P}] = 0$。微弱的弱相互作用核子力虽然会在某些特定核跃迁中引入可观测的宇称不守恒效应，但常规低能核结构与电磁跃迁通常在严格宇称守恒的近似下处理。算符 $\hat{P}$ 为线性的单体/多体幺正算符，满足 $\hat{P}^2 = \mathbf{1}$，其本征值为 $\pi = \pm 1$。实验室系中的孤立能级可同时标定为具有确定宇称的本征态：$\hat{P} |I^\pi, M\rangle = \pi |I^\pi, M\rangle$。

在讨论核多体波函数时，需要澄清实验室定态与内禀参考构型之间的逻辑界限。自由空间中实际可测的实验室物理定态均具有确定的角动量与宇称 $|I^\pi, M\rangle$。而在微观平均场计算中，为了方便处理核子之间的四极吸引相互作用，理论常采用自洽打破空间旋转对称性的平均场假定（如未投影的形变 Hartree-Fock、Nilsson 或推转波函数）。在轴对称形变场的大形变极限下，单粒子轨道常用渐近量子数 $\Omega^\pi [N n_z \Lambda]$ 标记，其中 $\Omega$ 为单粒子角动量沿对称轴的投影；奇核子与轴对称核芯耦合常引入总投影量子数 $K$。必须注意，这种未投影的形变参考构型并非实验室哈密顿量的能量本征态，而是包含了多种实验室自旋成分的取向波包。真实实验室态的性质需通过角动量投影等对称性恢复手段导出。

时间反演算符 $\hat{\mathcal{T}}$ 则具有反幺正性质（$\hat{\mathcal{T}} c |\psi\rangle = c^* \hat{\mathcal{T}} |\psi\rangle$）。对于奇 $A$ 核，$\hat{\mathcal{T}}^2 = -\mathbf{1}$ 导致无外磁场下的两重 Kramers 简并。在形变转动体系中，时间反演与绕特定主轴的旋转对称性相结合可定义条件性的 signature 对称性，而多准粒子三维倾斜转动中手征几何的出现还涉及复杂的动力学机制；关于反幺正时间反演、内禀对称性破缺及对称性恢复的系统讨论，见第 2.5 节与第 3.5 节。

---

## 2.1.2 球张量算符与 Wigner–Eckart 定理的几何分解

在不可约表示语言中，描述电磁跃迁与静态矩的多极算符通常以不可约球张量形式展开。阶数为 $\lambda$ 的球张量算符 $T_{\lambda\mu}$ 包含 $2\lambda + 1$ 个分量（$\mu = -\lambda, \dots, \lambda$）。在由欧拉角 $\boldsymbol{\theta}$ 描述的有限旋转 $\hat{R}(\boldsymbol{\theta})$ 下，算符分量按 Wigner $D$ 矩阵变换：
$$
\hat{R}(\boldsymbol{\theta}) \, T_{\lambda\mu} \, \hat{R}^\dagger(\boldsymbol{\theta}) = \sum_{\mu'=-\lambda}^\lambda D^\lambda_{\mu'\mu}(\boldsymbol{\theta}) \, T_{\lambda\mu'}.
$$
在李代数微元对易子语言中，等价于如下两式：
$$
[\hat{j}_z, T_{\lambda\mu}] = \mu \, T_{\lambda\mu}, \quad [\hat{j}_\pm, T_{\lambda\mu}] = \sqrt{\lambda(\lambda+1) - \mu(\mu \pm 1)} \, T_{\lambda, \mu \pm 1}.
$$

计算不可约球张量在两个具有确定角动量的实验室态 $|b I_b M_b\rangle$ 与 $|a I_a M_a\rangle$ 之间的多体矩阵元时，旋转协变性导出了 Wigner–Eckart 定理 [@book-suhonen-from-nucleons-to-nucleus]。采用 Racah 与 Edmonds 的标准约定，多体矩阵元可分解为几何定向因子与动力学结构因子的乘积：
$$
\langle a I_a M_a | T_{\lambda\mu} | b I_b M_b \rangle = (-1)^{I_a - M_a} \begin{pmatrix} I_a & \lambda & I_b \\ -M_a & \mu & M_b \end{pmatrix} R_{ab},
$$
其中圆括号阵列为 Wigner $3j$ 符号，$R_{ab} \equiv \langle a I_a || T_\lambda || b I_b \rangle$ 称为约化矩阵元。在 Clebsch–Gordan 系数表示中，该定理亦可表为：
$$
\langle a I_a M_a | T_{\lambda\mu} | b I_b M_b \rangle = \frac{1}{\sqrt{2I_a+1}} \, (I_b M_b \lambda \mu | I_a M_a) \, R_{ab}.
$$

Wigner–Eckart 定理实现了几何与动力学的严格解耦：
1. 矩阵元对磁量子数 $M_b, M_a$ 与多极投影分量 $\mu$ 的依赖，全部归结为纯几何耦合性质的 $3j$ 符号。几何非零条件直接给出了角动量三角不等式 $\Delta(I_a, \lambda, I_b)$（即 $|I_a - I_b| \le \lambda \le I_a + I_b$）以及代数磁投影选择定则 $M_a = M_b + \mu$。若不满足这些条件，矩阵元严格为零。
2. 约化矩阵元 $R_{ab}$ 完全独立于磁投影标号，集中包含了初末态多体波函数在空间积分与微观径向分布上的动力学信息。此外，由空间反演不变性，算符自身具有确定宇称 $\pi(T_\lambda)$（电多极为 $(-1)^\lambda$，磁多极为 $(-1)^{\lambda+1}$），矩阵元非零要求波函数宇称满足选择定则 $\pi_a \pi_b = \pi(T_\lambda)$。

本节统一采用厄米球张量算符约定：
$$
T_{\lambda\mu}^\dagger = (-1)^\mu \, T_{\lambda, -\mu}.
$$
根据矩阵元的共轭性质 $\langle a I_a M_a | T_{\lambda\mu} | b I_b M_b \rangle = (-1)^\mu \, \langle b I_b M_b | T_{\lambda, -\mu} | a I_a M_a \rangle^*$，代入 Wigner–Eckart 定理并结合 $3j$ 符号在列置换下的代数对称性 $\begin{pmatrix} I_b & \lambda & I_a \\ -M_b & -\mu & M_a \end{pmatrix} = \begin{pmatrix} I_a & \lambda & I_b \\ -M_a & \mu & M_b \end{pmatrix}$，可导出约化矩阵元在初末态互换下的共轭对称关系：
$$
R_{ba} = (-1)^{I_b - I_a} \, R_{ab}^*.
$$

在此需要明确约化矩阵元的测量含义：孤立的非对角约化矩阵元 $R_{ab}$（$a \neq b$）的复相位（或实基底下的正负号）不可独立观测。这是由于量子多体态具有全局规范重定相自由度。若对初末态实施纯相位变换 $|a\rangle \to |\tilde{a}\rangle = e^{i\phi_a} |a\rangle$ 与 $|b\rangle \to |\tilde{b}\rangle = e^{i\phi_b} |b\rangle$，约化矩阵元随之变为：
$$
\tilde{R}_{ab} = \langle \tilde{a} || T_\lambda || \tilde{b} \rangle = e^{i(\phi_b - \phi_a)} R_{ab}.
$$
相对相差 $\phi_b - \phi_a$ 依赖于分析者对基矢相位的人工选择。实验中能够直接提取的是其绝对模长 $|R_{ab}|$（通过跃迁几率）或涉及同一态的分支振幅相对比值，孤立非对角矩阵元的符号本身并不构成可直接测量的独立物理客体。

---

## 2.1.3 约化跃迁几率、统计权与上下行互易因子

将微观张量矩阵元联系到实验室谱学测量的能级寿命、跃迁截面与分支比，需要引入约化跃迁几率。考虑初态 $|i I_i\rangle$ 自发辐射一个多极阶为 $\sigma\lambda$ 的光子（$\sigma = E$ 或 $M$）退激至末态 $|f I_f\rangle$。在微扰论框架下，跃迁速率由初末态之间电磁多极算符矩阵元的模平方决定。

约化跃迁几率 $B(\sigma\lambda; i \to f)$ 在理论上被定义为初态所有磁子态取各向同性统计平均、并对末态所有磁子态及光子投影求和的量 [@book-suhonen-from-nucleons-to-nucleus]：
$$
B(\sigma\lambda; i \to f) \equiv \frac{1}{2I_i + 1} \sum_{M_i=-I_i}^{I_i} \sum_{M_f=-I_f}^{I_f} \sum_{\mu=-\lambda}^\lambda |\langle f I_f M_f | \mathcal{M}(\sigma\lambda, \mu) | i I_i M_i \rangle|^2.
$$
这种等权平均定义提供了一个不依赖于特定实验室取向制备的内禀跃迁标度。代入 Wigner–Eckart 定理，可提取与投影无关的约化矩阵元模平方 $|R_{fi}|^2$：
$$
B(\sigma\lambda; i \to f) = \frac{1}{2I_i + 1} |R_{fi}|^2 \sum_{M_i, M_f, \mu} \begin{pmatrix} I_f & \lambda & I_i \\ -M_f & \mu & M_i \end{pmatrix}^2.
$$
利用 $3j$ 符号的正交归一求和恒等式 $\sum_{M_i, \mu} \begin{pmatrix} I_f & \lambda & I_i \\ -M_f & \mu & M_i \end{pmatrix}^2 = \frac{1}{2I_f + 1}$，对末态全部 $2I_f + 1$ 个子态求和后，几何因子之和精确为 1：
$$
\sum_{M_f=-I_f}^{I_f} \left[ \sum_{M_i, \mu} \begin{pmatrix} I_f & \lambda & I_i \\ -M_f & \mu & M_i \end{pmatrix}^2 \right] = (2I_f + 1) \times \frac{1}{2I_f + 1} = 1.
$$
由此导出约化跃迁几率的标准形式：
$$
B(\sigma\lambda; i \to f) = \frac{1}{2I_i + 1} |R_{fi}|^2 = \frac{1}{2I_i + 1} |\langle f I_f || \mathcal{M}(\sigma\lambda) || i I_i \rangle|^2.
$$
该式表明，定义的 $B$ 值正比于约化矩阵元模平方，统计权重因子 $1/(2I_i + 1)$ 源自对初态各磁子态的平均。

对于逆向的受激吸收或库仑激发过程（$f \to i$），其约化跃迁几率定义为：
$$
B(\sigma\lambda; f \to i) = \frac{1}{2I_f + 1} |R_{if}|^2 = \frac{1}{2I_f + 1} |\langle i I_i || \mathcal{M}(\sigma\lambda) || f I_f \rangle|^2.
$$
根据共轭关系 $R_{if} = (-1)^{I_i - I_f} R_{fi}^*$，二者的模平方相等：$|R_{if}|^2 = |R_{fi}|^2$。因此立即得到上下行跃迁强度的互易关系：
$$
(2I_i + 1) \, B(\sigma\lambda; i \to f) = (2I_f + 1) \, B(\sigma\lambda; f \to i), \quad \text{即} \quad \frac{B(\sigma\lambda; i \to f)}{B(\sigma\lambda; f \to i)} = \frac{2I_f + 1}{2I_i + 1}.
$$

在偶偶核基态 $0^+$（$I_i = 0$）与第一激发态 $2_1^+$（$I_f = 2$）之间，该互易因子呈现出明显的统计数值差：
$$
B(E2; 0^+ \to 2_1^+) = 5 \times B(E2; 2_1^+ \to 0^+).
$$
这一因子 5 反映了相空间维度的不同：从单重非简并的 $0^+$ 态吸收激发时，末态开放了 5 个简并的磁取向通道；而从无极化 $2^+$ 态自发退激至 $0^+$ 态时，初态几率平均分摊在 5 个子态上，导致去激跃迁几率被稀释为五分之一。

需要补充指出，虽然全角积分的总辐射跃迁几率由标量算符旋转不变性保证而独立于初态磁子态的取向分布，但在实际在束 $\gamma$ 谱学实验中，探测器阵列仅覆盖有限立体角，且核反应常产生显著的初态自旋顺排。真实的微分脉冲计数需要结合核取向张量 $B_k(I)$、角分布系数以及探测效率响应进行解耦，这些在束实验反演链条见第 5 章。关于特定算符基底与跃迁振幅的复相位映射，将在第 5.7 节与第 5.9 节中结合多极混合比 $\delta$ 予以讨论。

---

## 2.1.4 态重定相规范、静态矩与闭合干涉网络

通过基矢重定相变换，可以进一步阐明哪些张量组合具有不受人工相位影响的物理意义。

对于初末态相同的对角矩阵元（$a = b$），在任意重定相变换 $|a\rangle \to |\tilde{a}\rangle = e^{i\phi_a} |a\rangle$ 下：
$$
\tilde{R}_{aa} = \langle \tilde{a} || T_\lambda || \tilde{a} \rangle = e^{-i\phi_a} e^{i\phi_a} R_{aa} = R_{aa}.
$$
对角约化矩阵元在任何重定相变换下均严格不变。实验中，自旋为 $I$ 的能态的实验室静四极矩（spectroscopic quadrupole moment）$Q_s(I)$ 定义为四极张量零分量在最大投影子态 $M = I$ 上的期望值：
$$
Q_s(I) \equiv \sqrt{\frac{16\pi}{5}} \, \langle I, M=I | \mathcal{M}(E2, 0) | I, M=I \rangle.
$$
利用 Wigner–Eckart 定理，该物理量可写为对角约化矩阵元的倍数：
$$
Q_s(I) = \sqrt{\frac{16\pi}{5}} \, \begin{pmatrix} I & 2 & I \\ -I & 0 & I \end{pmatrix} \langle I || \mathcal{M}(E2) || I \rangle = \sqrt{\frac{16\pi}{5}} \sqrt{\frac{2I(2I-1)}{(2I+3)(2I+2)(2I+1)}} \, R_{aa}.
$$
根据 $3j$ 符号的三角定则，自旋 $I \ge 1$ 是产生非零静四极矩的必要几何条件；对于 $I = 0$ 和 $I = 1/2$ 能级，$Q_s$ 恒为零。若 $I \ge 1$，其实际数值是否非零取决于核电荷分布的非球形偏离。需要澄清，静四极矩的代数符号不能简单直接地等同于内禀长椭球或扁椭球：仅在理想的轴对称刚性转子模型且基态带为 $K=0$ 时，存在解析几何映射 $Q_s(2_1^+) = -\frac{2}{7} Q_0$（此时内禀长椭形变 $Q_0 > 0$ 对应于 $Q_s < 0$）。在包含三轴形变、$\gamma$ 振动涨落或混合能带的复杂核中，该简单对应不再适用。

进一步考察包含多个中间态的多步跃迁。对于由能态构成的闭合多边形跃迁路径 $s \to r \to t \to \dots \to s$，在态矢量重定相变换下，该闭合序列上约化矩阵元的乘积变换为：
$$
\tilde{R}_{sr} \tilde{R}_{rt} \dots \tilde{R}_{ws} = \left(e^{i(\phi_r - \phi_s)} R_{sr}\right) \left(e^{i(\phi_t - \phi_r)} R_{rt}\right) \dots \left(e^{i(\phi_s - \phi_w)} R_{ws}\right).
$$
各态的相位角 $\phi_k$ 沿闭合环路成对出现并互相抵消，使得复相因子严格为 1：
$$
\tilde{R}_{sr} \tilde{R}_{rt} \dots \tilde{R}_{ws} = R_{sr} R_{rt} \dots R_{ws}.
$$
这表明，不可约张量约化矩阵元的闭合环路乘积与波函数的相位约定无关，满足规范不变性。但需强调，相消不变性只是可测量的必要代数条件，并不保证任意闭合回路在实验中都能被无歧义地独立反演。

闭合乘积在实验谱学中的典型体现是库仑激发的再取向效应。在重离子库仑激发中，核从基态 $|s\rangle = |0^+\rangle$ 激发至末态 $|r\rangle = |2_1^+\rangle$。跃迁振幅包含直接单步激发（正比于 $R_{sr}$）与经由中间态的两步激发。当两步激发中的中间态选为末态自身时，过程对应于核被激发至 $|r\rangle$ 后，在该能级上受到外靶电场梯度的再取向电磁作用。总截面包含两条路径几率振幅的相干干涉项，其实部正比于：
$$
\mathrm{Re} \left[ (-1)^{I_r - I_s} R_{rs} R_{st} R_{tr} \right].
$$
当中间态为末态自身（$t = r$）时，该干涉项正比于 $|R_{sr}|^2 R_{rr} \propto B(E2; s \to r) Q_s(r)$。实验中利用不同散射角与束流能量下的微分散射截面开展多态联合拟合，可对激发态静四极矩 $Q_s(r)$ 的符号施加灵敏约束。若中间态为不同的低激发态（如 $t = 2_2^+$），则涉及跨带闭合环路 $R_{0 2_1} R_{2_1 2_2} R_{2_2 0}$ 的相干贡献。

由不可约球张量可直接构造旋转标量算符，建立与电荷分布几何特征的联系 [@cline-1986-nuclear-shapes-coulomb-excitation]。遵循全篇统一记号，定义二阶标量算符为张量标量积：
$$
\hat{A} \equiv T \cdot T = \sqrt{5} [T \times T]^0 = \sum_{\mu=-2}^2 (-1)^\mu T_{2\mu} T_{2, -\mu}.
$$
在自旋为 $I$ 的能态 $|s\rangle$ 中插入中间态完备集并对全部磁投影求和，Racah 代数给出二阶形状不变量 $q_2 \equiv \langle \hat{A} \rangle_s$ 的形式（一般重耦合见附录 A）：
$$
q_2 = \frac{1}{2I+1} \sum_r |R_{sr}|^2 = \sum_r B(E2; s \to r).
$$
对于偶偶核 $0^+$ 基态，受角动量守恒限制，中间态只能为 $I_r = 2$。二阶标量不变量即为全部 $2^+$ 激发态跃迁强度的非相干和：$q_2 = \sum_r B(E2; 0^+ \to 2_r^+)$。

三阶零耦合张量算符定义为：
$$
\hat{B} \equiv -\sqrt{\frac{35}{2}} [[T \times T]^2 \times T]^0.
$$
定义三阶旋转不变量为初态期望值 $q_3 \equiv \langle \hat{B} \rangle_s$。对于偶偶核 $0^+$ 基态，中间态自旋受约束为 $I_r = I_t = 2$，利用特殊 $6j$ 符号 $\begin{Bmatrix} 2 & 2 & 2 \\ 0 & 2 & 2 \end{Bmatrix} = \frac{1}{5}$，求和给出最小解析式：
$$
q_3 = -\sqrt{\frac{7}{10}} \sum_{r, t} R_{0r} R_{rt} R_{t0}.
$$
将该求和拆分为对角中间态项（$r = t$）与非对角项（$r \neq t$）：
$$
\sum_{r, t} R_{0r} R_{rt} R_{t0} = \sum_r |R_{0r}|^2 R_{rr} + \sum_{r < t} 2 \, \mathrm{Re}[ R_{0r} R_{rt} R_{t0} ].
$$
第一项由跃迁强度与激发态自身静四极矩的乘积组成；第二项则由包含跨带跃迁的三态闭合干涉网络构成。在玻尔经典坐标图像下，不变量 $q_2$ 与 $q_3$ 分别关联于有效电荷形变大小 $\langle Q^2 \rangle$ 与三轴不对称度 $\langle Q^3 \cos 3\gamma \rangle$。

在运用标量不变量推断原子核空间几何时，必须注意其理论适用条件：
1. **中间态求和截断**：完备集求和形式上要求包括全部激发态。在实际分析中，只能测量有限数目的低能集体态；虽然低能集体跃迁通常占据非能权四极求和规则的较大部分，但对于高阶不变量，遗漏高能态的累积效应与实验测量误差的非线性传递将对结果带来不可忽视的不确定度。
2. **有效算符性质**：在微观坐标表象中，不同核子的坐标算符自然对易；但在相互作用玻色子模型或微观截断壳模型空间中，重整化有效单体算符往往具有非对易性，导致连续坐标下的高阶几何恒等式在截断空间中可能出现偏离。
3. **几何解释的多样性**：正如第 1.2 节所强调的，矩比 $q_3 / q_2^{3/2}$ 并不等同于 $\cos 3\gamma$ 的无权平均，有限的二阶与三阶矩不足以唯一定出完整的形变概率分布，也不能直接判定核是处于刚性三轴极小点还是具有显著的 $\gamma$ 软振动涨落。

本节建立的旋转与宇称对称性语言、Wigner–Eckart 分解以及闭合干涉网络，构成了讨论低能核结构的基础框架。在后续各节中，这些张量与代数工具将直接服务于微观壳模型演化（第 2.2 节）、集体哈密顿量量子化（第 2.4 节）、破缺参考态的角动量投影（第 2.5 节）以及在束谱学中绝对跃迁几率的实验反演（第 5.7 与 5.9 节）。
