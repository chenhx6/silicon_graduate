# Glossary: Greiner & Maruhn 核模型与集体运动专业术语规范

本术语表汇编 Walter Greiner & Joachim A. Maruhn《Nuclear Models》（Springer-Verlag，1996）中的核心专业术语、中英文对照及严密物理定义，为原子核三轴集体运动、转动振动耦合与巨多极共振分析提供统一理论语言。

---

## 1. 表面形变几何与集体坐标 (Deformation Geometry and Collective Coordinates)

- **Collective Coordinates (集体坐标 $\alpha_{\lambda\mu}$)**: 描述原子核可变形表面在球谐函数基底上展开的五个二阶四极多极张量分量：$R(\theta, \phi) = R_0 [1 + \sum_{\mu} \alpha_{2\mu}^* Y_{2\mu}(\theta, \phi)]$。
- **Hill-Wheeler Coordinates (Hill-Wheeler 形变坐标 $(\beta, \gamma)$)**: 将五维四极张量变换到核体固主轴参考系后的两个独立内禀内禀形变参量：$a_0 = \beta \cos\gamma, a_2 = a_{-2} = \frac{1}{\sqrt{2}} \beta \sin\gamma$。$\beta$ 衡量总形变偏离球形的幅度，$\gamma$ 衡量非轴对称三轴度。
- **Triaxiality Parameter ($\gamma$, 三轴形变角)**: 描述核三主轴长短比例的角向坐标。$\gamma = 0^\circ$ 对应轴对称长椭球形（Prolate）；$\gamma = 60^\circ$ 对应轴对称扁椭球形（Oblate）；$\gamma = 30^\circ$ 对应极大三轴不对称形变。
- **Incompressibility (体积不可压缩性)**: 核物质密度饱和性要求原子核在发生表面四极形变时体积严格守恒，由此导出表面展开系数中的二阶形状因子修正 $\alpha_{00} = -\frac{1}{\sqrt{4\pi}} \sum_\mu |\alpha_{2\mu}|^2$。

---

## 2. 非轴对称转子与 Davydov-Filippov 模型 (Asymmetric Rotor)

- **Davydov-Filippov Model (Davydov-Filippov 模型 / DF 模型)**: 假定原子核为具有固定的刚性内禀四极形变 $(\beta, \gamma)$ 的三轴非轴对称转子，主轴转动惯量遵循水动力学角分布律的模型。
- **$D_2$ Symmetry ($D_2$ 四元群对称性 / 欧氏内禀四面反演群)**: 由于内禀参考系三个主轴在几何上不可分辨，转动哈密顿量在绕任意主轴旋转 $180^\circ$（$\mathcal{R}_k(\pi)$）下严格不变；该对称性要求物理波函数的角动量投影 $K$ 只能取偶数（$K = 0, 2, 4, \dots$），且宇称必须为正。
- **Hydrodynamic Moments of Inertia (水动力学转动惯量 $\mathcal{J}_k$)**: 无旋无摩擦理想流体在三轴表面旋转时产生的转动惯量：$\mathcal{J}_k = 4 B \beta^2 \sin^2(\gamma - \frac{2\pi}{3} k)$。
- **Three-State Energy Sum Rule (三态能量求和恒等式)**: Davydov-Filippov 模型在三主轴惯量取任意有限值下均严格成立的代数恒等式：$E(2_1^+) + E(2_2^+) \equiv E(3_1^+)$。
- **$E(2_2^+)/E(2_1^+)$ Ratio ($2_2^+/2_1^+$ 能量比)**: 反常转动态与基态带首态的能量比值，随 $\gamma$ 从 $0^\circ$ 到 $30^\circ$ 单调从 $\infty$ 降至 $2.00$，是提取原子核三轴形变度的经典标尺。

---

## 3. 转动振动模型 (Rotation-Vibration Model, RVM)

- **Rotation-Vibration Model (Faessler-Greiner 转动振动模型 / RVM)**: 围绕轴对称长椭基态平衡形变 $(\beta_0, 0)$，将表面四极运动展开为平衡形变周围的小振幅标量振动（$\xi = a_0 - \beta_0, \eta = a_2$）并与整体空间转动自洽耦合的宏观理论。
- **Pauli-Podolsky Quantization (Pauli-Podolsky 黎曼度规量子化)**: 将经典拉格朗日量在非欧几里得弯曲坐标系中严格转换为自伴算符的量子化方法：$\hat{T} = -\frac{\hbar^2}{2} g^{-1/2} \partial_\mu (g^{1/2} g^{\mu\nu} \partial_\nu)$。
- **$\beta$-Vibrational Band ($\beta$ 振动带)**: 保持轴对称性（$K=0^+$）、原子核沿长轴发生周期性伸缩呼吸的集体振动激发带，带首为 $0_\beta^+$ 态。
- **$\gamma$-Vibrational Band ($\gamma$ 振动带)**: 破坏轴对称性（$K=2^+$）、原子核两短轴发生横向相对交替伸缩的非轴对称四极形变振动带，带首为 $2_\gamma^+$ 态。
- **Centrifugal Stretching (离心拉伸效应)**: 随着转动角动量增大，离心力拉伸原子核形变使 $\beta$ 增大，导致高自旋态转动惯量显著膨胀并降低能级间距。

---

## 4. $\gamma$ 不稳定核与 Wilets-Jean 模型 (Gamma-Soft Nuclei)

- **Wilets-Jean Model (Wilets-Jean 完全 $\gamma$ 软核模型)**: 假设集体势能仅依赖于总形变参量 $\beta$ 而对非轴对称角 $\gamma$ 完全平坦无阻碍（$V(\beta, \gamma) = V(\beta)$）的模型。
- **$O(5)$ Dynamical Symmetry ($O(5)$ 动力学五维旋转对称性)**: $\gamma$ 独立势能面在五维表面坐标空间中展示的连续转动不变群，其本征量子数为 Seniority 玻色量子数 $v$。
- **Staggering Index ($S(J)$, 能级交错指数)**: 衡量准 $\gamma$ 带奇偶自旋能级间距相对振荡的无量纲参数：$S(J) = \frac{[E(J) - E(J-1)] - [E(J-1) - E(J-2)]}{E(2_1^+)}$；刚性三轴核展现负交错，$\gamma$ 软核展现正交错。

---

## 5. 剪刀振动模式 (Scissors Mode)

- **Scissors Mode (磁偶极剪刀模式 $1_{\text{sc}}^+$)**: 在形变核中质子变形流体与中子变形流体绕两者公用的横向轴作反向相对角振荡的集体激发模式。
- **Symmetry Energy Restoring Force (对称能恢复力)**: 质子与中子主轴偏角破坏同位旋对称性，核力强大的体积与表面对称能提供极强的角弹性恢复力。
- **$B(M1)$ Strength ($B(M1)$ 磁偶极跃迁强度)**: 剪刀模式的核心实验指纹，从基态激发到 $1^+$ 态具有高达 $B(M1; 0^+ \to 1^+) \sim 1.0 - 3.5\ \mu_N^2$ 的特征超强跃迁。

---

## 6. 巨多极共振 (Giant Multipole Resonances)

- **Giant Resonances (巨共振 / GR)**: 全核所有核子高度相干协同参与的高激发集体振动模式，耗尽单粒子或多极求和规则的绝大部分强度。
- **Goldhaber-Teller Model (GT 模型)**: 假定质子与中子流体各自作为刚性不可压缩硬球，两者发生反相宏观相对位移的等矢巨共振模型（激发能 $\propto A^{-1/6}$）。
- **Steinwedel-Jensen Model (SJ 模型)**: 假定核表面固定不动，质子与中子声学流密度在核体边界内作流体动力学反相压缩驻波振荡的模型（激发能 $\propto A^{-1/3}$）。
- **IVGDR Splitting (等矢巨偶极共振形变分裂)**: 在轴对称变形核中，长轴振动（低频）与两短轴简并振动（高频）导致巨偶极共振共振峰精确分裂为能量不同的双峰，其共振面积比严格为 $1:2$。
- **TRK Sum Rule (Thomas-Reiche-Kuhn 能量加权求和规则)**: 经典非相对论等矢偶极光吸收总积分截面守恒定律：$\int \sigma(E) dE = \frac{2\pi^2 e^2 \hbar}{M c} \frac{N Z}{A} \approx 60 \frac{N Z}{A}\text{ MeV}\cdot\text{mb}$。
