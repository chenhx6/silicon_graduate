# 2.1 实验室对称性与张量语言

研究原子核低能激发与电磁跃迁，首先必须确立描述多体量子体系的参考系与对称性语言。原子核是由核子依靠自洽强相互作用紧密束缚的孤立量子多体系统。在不受外加电磁场扰动的自由实验室空间中，核哈密顿量严格服从空间旋转与空间反演不变性。然而，核结构研究中经常并存两套叙事视角：一类是直接对应实验谱学测量的实验室参考系，能级具有确定的总角动量 $I$、磁投影 $M$ 与空间宇称 $\pi$；另一类则是为了直观反映核物质空间排布而引入的形变内禀参考系，核态被赋予几何形变参数以及内禀角动量投影标号。

这种表象并存极易在定量分析中引发误解。例如，为何偶偶核基态的实验室一阶静电四极矩必为零，却仍能在跃迁中表现出强烈的四极集体性？微观模型计算给出的非对角约化矩阵元正负号是否构成直接的物理检验判据？在束谱学实验测得的跃迁强度与逆过程吸收强度之间的数值比例又源自何处？

要澄清这些问题，必须将宏观几何图像收敛于量子力学的不可约球张量语言。本节从实验室哈密顿量的基本时空对称性出发，阐明磁子态简并的微观起源；通过 Wigner–Eckart 定理将电磁算符的几何取向与微观动力学结构严格解耦；从无极化辐射场的微观统计平均推导约化跃迁几率及其上下行互易因子；通过态矢量的规范重定相变换，澄清单个非对角约化矩阵元与闭合矩阵元干涉网络在物理可测性上的本质分野，为后续微观壳模型演化、内禀形变投影以及绝对跃迁速率反演提供自洽的理论基准。

---

## 2.1.1 空间对称性、角动量量子数与实验室简并

在没有外加电磁场或外在极化环境的自由空间中，孤立原子核的多体哈密顿量 $\hat{H}$ 具有完全的空间平移、旋转与反演不变性。空间旋转群 $\mathrm{SO}(3)$ 的生成元对应于体系的总角动量算符 $\hat{\mathbf{J}}$。总角动量算符具有物理作用量的量纲（常用单位为 $\hbar$），其笛卡尔分量满足李代数对易关系：
$$
[\hat{J}_x, \hat{J}_y] = i \hbar \hat{J}_z, \quad [\hat{J}_y, \hat{J}_z] = i \hbar \hat{J}_x, \quad [\hat{J}_z, \hat{J}_x] = i \hbar \hat{J}_y.
$$
为了使角动量代数运算简洁，定义无量纲角动量算符 $\hat{\mathbf{I}} \equiv \hat{\mathbf{J}}/\hbar$，其分量服从对易子关系 $[\hat{I}_x, \hat{I}_y] = i \hat{I}_z$。算符 $\hat{\mathbf{I}}^2$ 与某一特定空间取向分量（通常取实验室坐标系 $z$ 轴分量 $\hat{I}_z$）对易，具有共同本征态 $|I, M\rangle$：
$$
\hat{\mathbf{I}}^2 |I, M\rangle = I(I+1) |I, M\rangle, \quad \hat{I}_z |I, M\rangle = M |I, M\rangle,
$$
其中量子数 $I$ 是非负整数或半整数，磁量子数 $M \in \{-I, -I+1, \dots, I\}$。算符 $\hat{\mathbf{J}}$ 包含物理作用量单位 $\hbar$，而量子数 $I$ 与 $M$ 是无量纲纯标量；在书写转动哈密顿量或跃迁频率时，二者不可随意混淆。

哈密顿量 $\hat{H}$ 的空间旋转不变性意味着它与旋转群的所有生成元对易：$[\hat{H}, \hat{\mathbf{J}}] = 0 \implies [\hat{H}, \hat{\mathbf{I}}] = 0$。由于阶梯算符定义为 $\hat{I}_\pm = \hat{I}_x \pm i \hat{I}_y$，显然有 $[\hat{H}, \hat{I}_\pm] = 0$。若某一能态满足 $\hat{H} |I, M\rangle = E(I, M) |I, M\rangle$，则：
$$
\hat{H} (\hat{I}_\pm |I, M\rangle) = \hat{I}_\pm \hat{H} |I, M\rangle = E(I, M) (\hat{I}_\pm |I, M\rangle).
$$
已知 $\hat{I}_\pm |I, M\rangle = \sqrt{I(I+1) - M(M \pm 1)} \, |I, M \pm 1\rangle$。只要该态不为零，所产生的新态仍是 $\hat{H}$ 的能量本征态，且具有完全相同的能量。由此得出严格结论：对于任意给定的总角动量量子数 $I$，该多重态中的全部 $2I+1$ 个磁子态 $M$ 必定具有严格相等的能量：
$$
E(I, M) = E(I), \quad \forall M \in \{-I, -I+1, \dots, I\}.
$$
这种由空间各向同性导致的能级简并，称为磁子态简并或旋转简并。除非施加外加电磁场（如 Zeeman 分裂或外电场梯度超精细分裂），这 $2I+1$ 个子态在实验室系中不可区分。

空间对称性的另一支柱是空间反演对称性。空间反演变换由宇称算符 $\hat{P}$ 描述，其作用是将核子空间坐标与动量同时反号：$\hat{P} \mathbf{r}_k \hat{P}^\dagger = -\mathbf{r}_k$，$\hat{P} \mathbf{p}_k \hat{P}^\dagger = -\mathbf{p}_k$。轨道角动量算符 $\hat{\mathbf{L}}_k = \mathbf{r}_k \times \mathbf{p}_k$ 与自旋算符在反演下保持不变，因此总角动量算符为轴矢量（赝矢量），与宇称算符对易：$\hat{P} \hat{\mathbf{I}} \hat{P}^\dagger = \hat{\mathbf{I}}$。在低能核物理中，强相互作用与电磁相互作用严格保持空间宇称守恒（弱相互作用宇称破坏几率仅在 $10^{-7}$ 量级，对常规低能谱学完全可忽略）。因此哈密顿量满足 $[\hat{H}, \hat{P}] = 0$。由于 $\hat{P}^2 = \mathbf{1}$，算符 $\hat{P}$ 是线性的单体/多体幺正算符，本征值只能为 $\pi = \pm 1$。实验室系中的孤立能级可同时标定为具有确定宇称的本征态：$\hat{P} |I^\pi, M\rangle = \pi |I^\pi, M\rangle$。

在核结构分析中，必须严格区分实验室本征态与内禀模型状态。无论是偶偶核、奇 $A$ 核还是奇奇核，自由实验室系中稳定存在或通过探测器退激直接测量的微观量子态，都严格是由好自旋 $I$、磁投影 $M$ 及确切空间宇称 $\pi$ 标定的本征态 $|I^\pi, M\rangle$。而在形变平均场理论或 Nilsson 模型中，理论引入了随核形变共同旋转的辅助内禀坐标系 $(x', y', z')$。在该体系中，单粒子状态由渐近量子数 $\Omega^\pi [N n_z \Lambda]$ 标记（$\Omega$ 为沿内禀对称轴的投影），奇核子与核芯耦合引入内禀总投影 $K$。必须强调，形变内禀态 $|\Phi_K\rangle$ 破坏了空间旋转不变性，绝非实验室哈密顿量 $\hat{H}$ 的本征态，而是由一系列不同实验室自旋态构成的相干叠加波包：
$$
|\Phi_K\rangle = \sum_{I \ge |K|} c_I \, |I^\pi, M, K\rangle.
$$
真实物理上可测量的实验室定态，必须通过对内禀波包实施角动量投影算符 $\hat{P}^I_{MK}$ 进行对称性恢复而获得。将内禀量子数（如 $\Omega$ 或 $K$）误作实验室系中严格守恒的物理运动常数，是常见的概念混淆。

时间反演算符 $\hat{\mathcal{T}}$ 则具有反幺正性质（$\hat{\mathcal{T}} c |\psi\rangle = c^* \hat{\mathcal{T}} |\psi\rangle$）。对于奇 $A$ 核，$\hat{\mathcal{T}}^2 = -\mathbf{1}$，在无外磁场时导致两重 Kramers 简并。转动核打破单轴对称性时，时间反演与空间旋转结合将导出 signature 对称性乃至手征双重带；关于反幺正时间反演、内禀对称性破缺及实验室投影的系统推导，将在第 2.5 节与第 3.5 节展开。

---

## 2.1.2 球张量算符与 Wigner–Eckart 定理的几何分解

描述原子核与辐射场相互作用、电磁辐射以及核反应跃迁过程的物理算符，通常以空间旋转群的不可约球张量形式展开。阶数为 $\lambda$ 的不可约球张量算符 $T_{\lambda\mu}$ 包含 $2\lambda + 1$ 个分量（$\mu = -\lambda, \dots, \lambda$）。在空间旋转操作 $\hat{R}(\boldsymbol{\theta})$ 下，球张量分量服从标准变换律：
$$
\hat{R}(\boldsymbol{\theta}) \, T_{\lambda\mu} \, \hat{R}^\dagger(\boldsymbol{\theta}) = \sum_{\mu'=-\lambda}^\lambda D^\lambda_{\mu'\mu}(\boldsymbol{\theta}) \, T_{\lambda\mu'},
$$
其中 $D^\lambda_{\mu'\mu}(\boldsymbol{\theta})$ 为 Wigner $D$ 矩阵。在李代数微元对易子语言中，等价于换位关系：
$$
[\hat{I}_z, T_{\lambda\mu}] = \mu \, T_{\lambda\mu}, \quad [\hat{I}_\pm, T_{\lambda\mu}] = \sqrt{\lambda(\lambda+1) - \mu(\mu \pm 1)} \, T_{\lambda, \mu \pm 1}.
$$

计算不可约球张量算符在两个确定角动量态 $|b I_b M_b\rangle$ 与 $|a I_a M_a\rangle$ 之间的矩阵元时，旋转协变性使得矩阵元具有高度约束的几何结构。这就是核物理与量子力学中的 Wigner–Eckart 定理 [@book-suhonen-from-nucleons-to-nucleus]。采用 Racah 与 Edmonds 的标准约定，该定理将多体矩阵元因式分解为几何定向因子与微观动力学因子的乘积：
$$
\langle a I_a M_a | T_{\lambda\mu} | b I_b M_b \rangle = (-1)^{I_a - M_a} \begin{pmatrix} I_a & \lambda & I_b \\ -M_a & \mu & M_b \end{pmatrix} R_{ab},
$$
其中带大括号的阵列为 Wigner $3j$ 符号，$R_{ab} \equiv \langle a I_a || T_\lambda || b I_b \rangle$ 称为约化矩阵元（RME）。在等价的 Clebsch–Gordan 系数表示中：
$$
\langle a I_a M_a | T_{\lambda\mu} | b I_b M_b \rangle = \frac{1}{\sqrt{2I_a+1}} \, (I_b M_b \lambda \mu | I_a M_a) \, R_{ab}.
$$

Wigner–Eckart 定理展现了不可约张量语言的核心内涵：
1. **几何与动力学的彻底分离**：矩阵元中对初始态、终态磁量子数 $M_b, M_a$ 以及算符取向投影 $\mu$ 的全部依赖，被完全包容在纯粹由 $\mathrm{SO}(3)$ 角动量耦合决定的 $3j$ 符号之中，与核子强相互作用细节无关。相反，约化矩阵元 $R_{ab}$ 彻底独立于空间投影标号，凝聚了初末态波函数的微观动力学信息。
2. **选择定则的几何必然性**：根据 $3j$ 符号非零条件，矩阵元非零要求初态自旋 $I_b$、末态自旋 $I_a$ 与算符阶数 $\lambda$ 满足角动量三角不等式 $\Delta(I_a, \lambda, I_b)$：$|I_a - I_b| \le \lambda \le I_a + I_b$；同时磁投影必须满足代数守恒：$M_a = M_b + \mu$。若不满足三角关系或磁投影不守恒，矩阵元在几何上恒为零。此外，由于空间反演对称性，算符自身具有确定宇称 $\pi(T_\lambda)$（电多极 $E\lambda$ 为 $(-1)^\lambda$；磁多极 $M\lambda$ 为 $(-1)^{\lambda+1}$），要求波函数宇称满足 $\pi_a \pi_b = \pi(T_\lambda)$，否则 $R_{ab}$ 在多体积分中相消。

在 Condon–Shortley 相位约定下，标准的电多极与磁多极球张量算符满足厄米张量共轭条件 [@book-suhonen-from-nucleons-to-nucleus]：
$$
T_{\lambda\mu}^\dagger = (-1)^\mu \, T_{\lambda, -\mu}.
$$
根据内积共轭性质 $\langle a I_a M_a | T_{\lambda\mu} | b I_b M_b \rangle = (-1)^\mu \, \langle b I_b M_b | T_{\lambda, -\mu} | a I_a M_a \rangle^*$，代入 Wigner–Eckart 定理并利用 $3j$ 符号列置换对称性，立即得到约化矩阵元在态互换下的共轭对称关系：
$$
R_{ba} = (-1)^{I_b - I_a} \, R_{ab}^*.
$$

需要在此特别强调一个关键物理事实：**单个非对角约化矩阵元 $R_{ab}$（$a \neq b$）本身绝对不是一个可以直接测量的物理量！** 量子态具有任意选择纯位相反馈的规范自由度。若对态矢量做局域重定相变换 $|a\rangle \to |\tilde{a}\rangle = e^{i\phi_a} |a\rangle$ 与 $|b\rangle \to |\tilde{b}\rangle = e^{i\phi_b} |b\rangle$，约化矩阵元变为：
$$
\tilde{R}_{ab} = \langle \tilde{a} || T_\lambda || \tilde{b} \rangle = e^{-i\phi_a} e^{i\phi_b} R_{ab} = e^{i(\phi_b - \phi_a)} R_{ab}.
$$
由于相位差 $\phi_b - \phi_a$ 完全取决于分析者对基矢相位的人工约定，因此对于孤立非对角跃迁，单个矩阵元 $R_{ab}$ 的复相位（乃至实基底下的正负号）在实验上不可直接观测。唯有在构建闭合干涉网络或定义对角静态矩时，矩阵元的符号才获得不依赖于基底相位选取的真实物理意义。

---

## 2.1.3 约化跃迁几率、统计权与上下行互易因子

为了将微观张量矩阵元与在束实验测量的谱学跃迁截面、能级寿命及分支比相联系，必须考察宏观无极化实验室环境下的跃迁速率。考虑处于初态 $|i I_i\rangle$ 的原子核自发辐射一个多极阶为 $\sigma\lambda$ 的光子（$\sigma = E$ 或 $M$），跃迁至末态 $|f I_f\rangle$。根据费米黄金定则，跃迁速率正比于初末态之间电磁算符矩阵元的模平方。

在实际实验中，处于激发态能级的核子系统呈现各向同性的统计分布。初态中各个磁子态 $M_i \in \{-I_i, \dots, I_i\}$ 具有相等的占据概率 $1/(2I_i + 1)$。与此同时，常规 $\gamma$ 探测器对出射光子的空间偏振与投影方向通常不施加选择性吸收，而是测量向末态所有可能磁子态 $M_f$ 释放光子的总积分强度。因此，描述该多极跃迁固有强度的物理量被定义为在初态磁子态上取统计平均、并对末态所有磁子态及算符投影求和的约化跃迁几率 $B(\sigma\lambda; i \to f)$ [@book-suhonen-from-nucleons-to-nucleus]：
$$
B(\sigma\lambda; i \to f) \equiv \frac{1}{2I_i + 1} \sum_{M_i=-I_i}^{I_i} \sum_{M_f=-I_f}^{I_f} \sum_{\mu=-\lambda}^\lambda |\langle f I_f M_f | \mathcal{M}(\sigma\lambda, \mu) | i I_i M_i \rangle|^2.
$$

利用 Wigner–Eckart 定理，将电磁多极张量算符 $\mathcal{M}(\sigma\lambda, \mu)$ 的矩阵元代入，并提取约化矩阵元模平方 $|R_{fi}|^2$：
$$
B(\sigma\lambda; i \to f) = \frac{1}{2I_i + 1} |R_{fi}|^2 \sum_{M_i, M_f, \mu} \begin{pmatrix} I_f & \lambda & I_i \\ -M_f & \mu & M_i \end{pmatrix}^2.
$$
根据 Wigner $3j$ 符号的正交归一性求和恒等式 $\sum_{M_i, \mu} \begin{pmatrix} I_f & \lambda & I_i \\ -M_f & \mu & M_i \end{pmatrix}^2 = \frac{1}{2I_f + 1}$，对末态全部 $2I_f + 1$ 个分量 $M_f$ 求和后，几何求和项严格给出常数 1：
$$
\sum_{M_f=-I_f}^{I_f} \left[ \sum_{M_i, \mu} \begin{pmatrix} I_f & \lambda & I_i \\ -M_f & \mu & M_i \end{pmatrix}^2 \right] = (2I_f + 1) \times \frac{1}{2I_f + 1} = 1.
$$
代入上式，立即得到约化跃迁几率的严密解析表达式：
$$
B(\sigma\lambda; i \to f) = \frac{1}{2I_i + 1} |R_{fi}|^2 = \frac{1}{2I_i + 1} |\langle f I_f || \mathcal{M}(\sigma\lambda) || i I_i \rangle|^2.
$$
它由微观约化矩阵元模平方决定，前置因子 $1/(2I_i + 1)$ 完全源于初态磁子态的统计平均权重。

现在考察其逆过程。在低能库仑激发或光核吸收反应中，体系从初始态 $|f I_f\rangle$ 吸收能量跃迁至 $|i I_i\rangle$。逆过程的约化跃迁几率写作：
$$
B(\sigma\lambda; f \to i) = \frac{1}{2I_f + 1} |R_{if}|^2 = \frac{1}{2I_f + 1} |\langle i I_i || \mathcal{M}(\sigma\lambda) || f I_f \rangle|^2.
$$
利用先前证明的厄米球张量约化矩阵元共轭关系 $R_{if} = (-1)^{I_i - I_f} R_{fi}^*$，二者的模平方严格相等：$|R_{if}|^2 = |R_{fi}|^2$。因此，将上下行跃迁方程直接相除，即可确立量子力学互易统计权关系：
$$
(2I_i + 1) \, B(\sigma\lambda; i \to f) = (2I_f + 1) \, B(\sigma\lambda; f \to i), \quad \text{即} \quad \frac{B(\sigma\lambda; i \to f)}{B(\sigma\lambda; f \to i)} = \frac{2I_f + 1}{2I_i + 1}.
$$

这一互易关系在偶偶核低激发四极跃迁中展现出极为显著的数值效应。考虑偶偶核基态 $0^+$（$I_i = 0$）与第一激发态 $2_1^+$（$I_f = 2$）之间的电四极跃迁：
- 库仑激发上行过程：$0^+ \to 2_1^+$，初态简并度为 $2(0) + 1 = 1$，末态简并度为 $2(2) + 1 = 5$。其跃迁几率为 $B(E2; 0^+ \to 2_1^+) = |R_{20}|^2$。
- 自发 $\gamma$ 衰变下行过程：$2_1^+ \to 0^+$，初态简并度为 5，末态简并度为 1。其跃迁几率为 $B(E2; 2_1^+ \to 0^+) = \frac{1}{5} |R_{02}|^2 = \frac{1}{5} |R_{20}|^2$。

因此，二者满足严格的比例关系：
$$
B(E2; 0^+ \to 2_1^+) = 5 \times B(E2; 2_1^+ \to 0^+).
$$
在核结构实验报告与理论文献中，若不标明初末态次序，极易引发因子 5 的严重错误。该数值差异源于无极化统计系综中，自旋为 2 的能态在空间拥有 5 个独立的正交投影取向，因而在去激时将跃迁概率平均稀释为五分之一；反之，从各向同性的 $0^+$ 态受激跃迁时，全部 5 个终态通道均对吸收截面提供无阻碍的贡献。

在算符相位定义方面，Suhonen 等专著中区分了 Condon–Shortley 约定与 Biedenharn–Rose 约定 [@book-suhonen-from-nucleons-to-nucleus]。在 Condon–Shortley 约定中，球谐函数满足 $Y_{\lambda\mu}^* = (-1)^\mu Y_{\lambda, -\mu}$，电多极算符 $\mathcal{M}(E\lambda, \mu)$ 在标准时间反演基底下给出的约化矩阵元为实数；但由于磁多极算符包含微分算符，其单粒子矩阵元带有虚数因子 $i$。Biedenharn–Rose 约定通过引入相因子 $\zeta(E\lambda) = i^\lambda$ 与 $\zeta(M\lambda) = i^{\lambda-1}$，使得电、磁多极跃迁的单粒子矩阵元均保持为严格实数。本文在全篇分析中固定采用标准的实厄米球张量算符约定；当遇到包含非平凡时间反演破缺或复振幅干涉的混合跃迁时，涉及复相位的表达式将明确给出其模平方与干涉项分解。

---

## 2.1.4 态重定相规范、静态矩与闭合干涉网络

先前已经指出，单个非对角约化矩阵元 $R_{ab}$ 随微观波函数的整体相位任意漂移。现在深入分析何种代数组合能够构成不受重定相影响的真实物理可观测量。

首先考察初末态完全相同的对角矩阵元（$a = b$）。在任意整体重定相变换 $|a\rangle \to |\tilde{a}\rangle = e^{i\phi_a} |a\rangle$ 下：
$$
\tilde{R}_{aa} = \langle \tilde{a} || T_\lambda || \tilde{a} \rangle = e^{-i\phi_a} e^{i\phi_a} R_{aa} = R_{aa}.
$$
对角约化矩阵元在任何重定相变换下均严格恒等，具备客观实在性。原子核特定自旋态 $|I\rangle$ 的实验室内禀静电四极矩 $Q_s(I)$ 定义为四极张量零分量在最大投影子态 $M = I$ 上的量子期望值：
$$
Q_s(I) \equiv \sqrt{\frac{16\pi}{5}} \, \langle I, M=I | \mathcal{M}(E2, 0) | I, M=I \rangle.
$$
利用 Wigner–Eckart 定理，该物理量可直接用对角约化矩阵元表达：
$$
Q_s(I) = \sqrt{\frac{16\pi}{5}} \, (-1)^{I-I} \begin{pmatrix} I & 2 & I \\ -I & 0 & I \end{pmatrix} \langle I || \mathcal{M}(E2) || I \rangle = \sqrt{\frac{16\pi}{5}} \sqrt{\frac{2I(2I-1)}{(2I+3)(2I+2)(2I+1)}} \, R_{aa}.
$$
根据 $3j$ 符号的三角定则，当且仅当 $I \ge 1$ 时 $Q_s(I)$ 才能非零；对于偶偶核基态 $I = 0$ 以及半整数自旋基态 $I = 1/2$，由角动量耦合几何限制，其对角静四极矩必然恒等于零。对于 $I \ge 1$ 的能态（如 $2_1^+$ 态），$Q_s(I)$ 不仅绝对大小可测，其代数正负号同样是完全客观的物理观测量：$Q_s(2^+) < 0$ 对应于长椭球电荷分布（prolate），而 $Q_s(2^+) > 0$ 对应于扁椭球电荷分布（oblate）。

进一步考察包含多个不同能态的多步跃迁。设有一组闭合跃迁路径：$s \to r \to t \to \dots \to s$。在实施任意态重定相变换时，该闭合序列上所有约化矩阵元的乘积变换为：
$$
\tilde{R}_{sr} \tilde{R}_{rt} \dots \tilde{R}_{ws} = \left(e^{i(\phi_r - \phi_s)} R_{sr}\right) \left(e^{i(\phi_t - \phi_r)} R_{rt}\right) \dots \left(e^{i(\phi_s - \phi_w)} R_{ws}\right).
$$
将所有指数项相加，各态的相位角 $\phi_k$ 恰好以一正一负的形式沿闭合环路成对出现：$(\phi_r - \phi_s) + (\phi_t - \phi_r) + \dots + (\phi_s - \phi_w) \equiv 0$。因此复相因子严格归一：
$$
\tilde{R}_{sr} \tilde{R}_{rt} \dots \tilde{R}_{ws} = R_{sr} R_{rt} \dots R_{ws}.
$$
这一结论确立了量子多体谱学中最重要的规范不变性原理：**由不可约张量约化矩阵元构成的任意闭合环路乘积，与波函数的整体相位约定无关，是完全客观的物理观测量。**

这一闭合乘积在实验核物理中的典型代表是多步库仑激发的量子干涉与再取向效应。在重离子库仑激发中，靶核从基态 $|s\rangle = |0^+\rangle$ 激发到末态 $|r\rangle = |2_1^+\rangle$。激发振幅包含直接单步激发（幅度正比于 $R_{sr}$）与经由中间态 $|t\rangle$ 的两步虚激发。当中间态即为该激发态自身（$t = r$）时，对应于原子核在库仑场中先被激发到 $|r\rangle$，随后与靶核电场梯度的再取向相互作用再次作用于 $|r\rangle$。

库仑激发总截面包含两条路径跃迁振幅的相干叠加，干涉项正比于实部：
$$
\mathrm{Re} \left[ R_{sr}^* \, (R_{st} R_{tr}) \right] = \mathrm{Re} \left[ (-1)^{I_r - I_s} R_{rs} R_{st} R_{tr} \right].
$$
当 $t = r$ 时，该干涉项化为：
$$
(-1)^{I_r - I_s} R_{rs} R_{sr} R_{rr} = |R_{sr}|^2 \, R_{rr} \propto B(E2; s \to r) \, Q_s(r).
$$
由于 $B(E2)$ 恒正，实验测得的微分截面角分布中干涉项的正负，能够直接敏感地确定出激发态对角静四极矩 $Q_s(r)$ 的物理符号！当 $t \neq r$ 时（如基态与 $2_1^+$, $2_2^+$ 能级），该干涉项直接测量了三态闭合环路乘积 $R_{0 2_1} R_{2_1 2_2} R_{2_2 0}$ 的符号与幅度。

这一张量干涉网络通过旋转标量不变量方法与核的几何形状建立了直接对应 [@cline-1986-nuclear-shapes-coulomb-excitation]。在实验室系中直接构造旋转标量算符：
二阶零耦合张量算符定义为：
$$
\hat{A} \equiv [T \times T]^0 = \frac{1}{\sqrt{5}} \sum_{\mu=-2}^2 (-1)^\mu T_{2\mu} T_{2, -\mu}.
$$
在自旋为 $I$ 的能态 $|s\rangle$ 中插入中间态完备集并对全部磁投影求和，Racah 代数重耦合（详见附录 A）给出其期望值：
$$
\langle [T \times T]^0 \rangle_s = \frac{1}{\sqrt{2I+1}} \sum_r (-1)^{I + I_r} \begin{Bmatrix} 2 & 2 & 0 \\ I & I & I_r \end{Bmatrix} |R_{sr}|^2 = \frac{1}{\sqrt{5}(2I+1)} \sum_r |R_{sr}|^2,
$$
其中利用了特殊 $6j$ 符号解析值 $\begin{Bmatrix} 2 & 2 & 0 \\ I & I & I_r \end{Bmatrix} = \frac{(-1)^{I + I_r + 2}}{\sqrt{5(2I+1)}}$。按照 Cline 归一规范，定义二阶形状不变量 $q_2 \equiv \sqrt{5} \langle \hat{A} \rangle_s$：
$$
q_2 = \frac{1}{2I+1} \sum_r |R_{sr}|^2 = \sum_r B(E2; s \to r).
$$
特别地，当初态为偶偶核 $0^+$ 基态时，中间态自旋受约束只能为 $I_r = 2$，二阶标量不变量直接退化为全部 $2^+$ 激发态跃迁强度的非相干加和：$q_2 = \sum_r B(E2; 0^+ \to 2_r^+)$。

三阶零耦合张量标量算符定义为：
$$
\hat{B}' \equiv [[T \times T]^2 \times T]^0.
$$
在态 $|s\rangle$ 中插入两重完备中间态，对其期望值进行严格的磁投影收缩与 Racah 重耦合，得到一般自旋下的表达式：
$$
\langle [[T \times T]^2 \times T]^0 \rangle_s = \frac{(-1)^{2I}}{2I+1} \sum_{r, t} \begin{Bmatrix} 2 & 2 & 2 \\ I & I_r & I_t \end{Bmatrix} R_{sr} R_{rt} R_{ts}.
$$
对于自旋为 $I = 0$ 的偶偶核基态，中间态受角动量守恒限制只能具有自旋 $I_r = I_t = 2$。代入 $6j$ 符号特殊值 $\begin{Bmatrix} 2 & 2 & 2 \\ 0 & 2 & 2 \end{Bmatrix} = \frac{1}{5}$，三阶张量标量在 $I = 0$ 基态中的期望值简化为：
$$
\langle [[T \times T]^2 \times T]^0 \rangle_{I=0} = \frac{1}{5} \sum_{r, t} R_{0r} R_{rt} R_{t0}.
$$
在标准归一规范中，三阶旋转不变量定义为 $q_3 \equiv -\sqrt{35/2} \langle [[T \times T]^2 \times T]^0 \rangle_{I=0}$，从而得到：
$$
q_3 = -\sqrt{\frac{7}{10}} \sum_{r, t} R_{0r} R_{rt} R_{t0}.
$$

将该求和拆分为对角中间态项（$r = t$）与非对角中间态项（$r \neq t$）：
$$
\sum_{r, t} R_{0r} R_{rt} R_{t0} = \sum_r |R_{0r}|^2 R_{rr} + \sum_{r < t} 2 \, \mathrm{Re}[ R_{0r} R_{rt} R_{t0} ].
$$
第一项由基态向各个 $2_r^+$ 态跃迁强度与该激发态自身的内禀静电四极矩 $R_{rr} \propto Q_s(2_r^+)$ 的乘积组成；第二项则由包含跨带跃迁的三态闭合干涉网络构成。这两部分中的每一个乘积项在态重定相下都保持绝对守恒。在 Bohr 集体模型的经典坐标几何对应下，不变量 $q_2$ 直接映射为整体四极形变平方 $\langle Q^2 \rangle$，而 $q_3$ 则对应于三轴不对称度 $\langle Q^3 \cos 3\gamma \rangle$。通过实验测得的有限矩阵元闭合网络计算 $q_2$ 与 $q_3$，核物理学家无须假定波函数的任何未定相位，即可在实验室系中直接测定核波函数的有效电荷形变与非轴对称性。

这一张量不变量方法虽然在理论上极为优美，但在应用至真实数据与微观模型时，必须注意其物理边界：
1. **中间态截断误差**：上述展开要求对全希尔伯特空间的完备中间态求和。对于强形变集体核，低能前几个激发态占据了非能权 $E2$ 求和规则中 70% 至 95% 的绝大部分强度 [@cline-1986-nuclear-shapes-coulomb-excitation]。但对更高阶不变量（如四阶或六阶矩），高能连续谱与非集体背景的微小渗漏会被矩阵元的高次幂显著放大，截断误差迅速增加。
2. **有效算符的对易异质性**：在微观坐标表象下，核子坐标多极张量在不同核子间互相对易；但在相互作用玻色子模型（IBM）或截断壳模型有效电荷空间中，重整化的有效单体算符往往不再满足坐标算符的原生对易子恒等式，导致某些在连续场下成立的高阶恒等关系在截断模型中发生微观偏离。
3. **矩重心与势能面刚性的分野**：单凭 $q_3$ 的测量值并不能唯一区分该核究竟是处于固定三轴形状的刚性极小点，还是处于大振幅 $\gamma$ 软振动波包的动态涨落均值之中。对核形状动力学性质的完整判断，必须进一步结合能级序列的精细结构与微观响应机制。

建立在空间对称性与不可约张量语言之上的这些严格判据，构成了理解低能核结构的数学基石。在随后的各节中，这一语言将直接应用于微观壳模型的单极占据与轨道演化（第 2.2 节）、集体哈密顿量的形状坐标量子化（第 2.4 节）、破缺参考态的对称性投影（第 2.5 节）以及在束实验中由衰变寿命和分支比精确反演绝对跃迁几率的因果链条（第 5.7 与 5.9 节）。
