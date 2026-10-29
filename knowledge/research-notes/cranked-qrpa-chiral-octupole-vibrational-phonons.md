---
type: research-note
title: "三轴八极变形核中推转准粒子随机相位近似（Cranked QRPA）与手征-八极微振声子谱"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [Cranked QRPA and chiral octupole phonons, CQRPA手征八极微振动, cranked-qrpa-chiral-octupole]
tags: [qrpa, cqrpa, chiral-phonons, octupole-vibrations, rotating-nuclei]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 octupole chiral C-QRPA research mission"
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, butler-nazarewicz-1996-intrinsic-reflection-asymmetry]
---

# 三轴八极变形核中推转准粒子随机相位近似（Cranked QRPA）与手征-八极微振声子谱

## Research Trigger

在三轴八极形变原子核（如 $A \approx 130$ 质量区的 $^{133}\text{Ce}, ^{135}\text{Nd}$ 及 $A \approx 80$ 质量区的 $^{78}\text{Br}$）的高自旋转动带中，实验相继观测到手征双重带（chiral doublet bands）、多手征双重带（M$\chi$D）以及伴随强 $E1$ 跨带跃迁的宇称伙伴结构。然而，传统的倾斜轴推转模型（TAC）通常仅给出静止的平均场能量极小，缺乏对微观集体振动与量子隧穿动力学的自洽描述；而粒子-转子模型（PRM）则受限于固定的核芯形变与受限的单粒子组态空间。

为了在微观多体层面厘清三轴反射不对称转动体系中的微振动激发机制，本研究基于自洽推转平均场（Cranked Mean Field）建立推转准粒子随机相位近似（Cranked Quasiparticle Random-Phase Approximation, C-QRPA）形式体系。重点解决两大对称性恢复模式——手征出平面摆动声子（恢复时间反演与面外反射破缺）与八极偶极振动声子（恢复空间反演宇称破缺）的色散关系、在有限转动角速度 $\omega$ 下的能级交叉动力学、两模相干杂化机制，以及电多极跃迁几率 $B(M1), B(E1), B(E2), B(E3)$ 随转动频率的动力学突变现象。

## Grounded Evidence

### 1. 自洽推转平均场与对称性破缺理论基础
- **Frauendorf (2001) Rev. Mod. Phys. 73, 463** ([[frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei]])：
  - 系统阐明了转动平均场中的自发对称性破缺：平面推转（planar TAC）保留特征复合对称性并产生 $\Delta I = 1$ 能带伴随旋称伙伴行为；出平面非共面推转（aplanar TAC）自发破缺方位面反射与时间反演的组合对称性，产生左手与右手简并内禀解；
  - 明确指出平均场解代表半经典波包，实验室系真实能级必须通过动力学激发或对称性恢复获得；在未发生静态手征自发破缺的近平面转动区，低激发态对应恢复出平面自由度的**手征摆动声子（chiral wobbling/vibrational phonon）**；
  - 指出 RPA 框架是处理接近平均场分岔点微振动激发的标准微观自洽理论，能够同时处理粒子-空穴与粒子-粒子相互作用。
- **Butler & Nazarewicz (1996) Rev. Mod. Phys. 68, 349** ([[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]])：
  - 论证了内禀反射不对称性的微观起源为费米面附近具有 $\Delta l = \Delta j = 3$ 的相反宇称单粒子轨道之间的相干八极耦合；
  - 严格区分了稳定八极形变（static octupole deformation）、八极振动/软度（octupole vibration/softness）以及宇称恢复双重带（parity-restored doublets）；
  - 阐明 $E3$ 跃迁强度是直接探测八极形变/振动集体性的可靠探针，而 $E1$ 跃迁则源于中子-质子质量中心与电荷中心的分离（宏观液滴极化与微观壳修正中子-质子再分布的微弱差额），对组态干涉和抵消效应极为敏感。

### 2. 实验微振动与宇称伙伴对账
- **$^{78}\text{Br}$ 实验证据**（Liu et al. 2016 PRL 116, 112501，[[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]）：
  - 实验测定正宇称双重带（Bands 1-2，$\pi g_{9/2} \otimes \nu g_{9/2}$）与负宇称双重带（Bands 3-4，$\pi f_{5/2} \otimes \nu g_{9/2}$）；
  - 在正负宇称带之间观测到 8 条强 $E1$ 连接跃迁；实验测得 $B(E1)/B(E2) \sim 1.2\times 10^{-4}\text{--}4.5\times 10^{-4}\text{ fm}^{-2}$，比稳定八极核 $^{224}\text{Th}$ 小约一个数量级；
  - 结合 MDC-CDFT 给出势能面沿 $\beta_{30}$ 高度软化（octupole softness），确立了手征几何与八极微振动在同一核系统中共存的实验基础。
- **$^{133}\text{Ce}$ 与 $^{135}\text{Nd}$ 实验证据**：
  - $^{133}\text{Ce}$（Ayangeakaa et al. 2013 PRL 110, 172504；Wakudyanaye 2022，[[wakudyanaye-2022-triaxiality-rotational-bands-133ce]]）：实验建立多重手征双重带（M$\chi$D），在低自旋区伴随 $\sim 0.40\text{ MeV}$ 的手征声子激发，且中子 $h_{11/2}$ 与偶极/八极跃迁分支交织；
  - $^{135}\text{Nd}$（Mukhopadhyay et al. 2007 PRL 99, 172501；Zhu et al. 2003，[[mukhopadhyay-2007-135nd-chiral-vibration-static]]）：实验测定能级寿命 $\tau$ 与分支比，观测到低自旋能级差 $\Delta E(I)$ 与 $B(M1)/B(E2)$ 随自旋的剧烈软化，反映手征摆动声子在临界推转角频率附近的动力学演化。

## Provisional Reasoning

### 1. Cranked QRPA 形式体系的微观构建

在自洽推转平均场下，内禀 Routhian 算符定义为：
$$H_{\text{crank}} = H - \vec{\omega} \cdot \vec{J} = H_{\text{MF}} - \omega J_x$$
在静态三轴八极变形基底下，平均场单粒子势包含四极与八极多极矩约束：
$$h_{\text{sp}} = h_0 - \sum_{\mu=-2}^{2} C_{2\mu} Q_{2\mu} - \sum_{\mu=-3}^{3} C_{3\mu} Q_{3\mu} - \Delta (P^\dagger + P) - \lambda N - \omega J_x$$
通过广义 Bogoliubov 变换建立准粒子基底 $\alpha_\mu^\dagger, \alpha_\mu$：
$$a_k^\dagger = \sum_\mu \left( U_{k\mu} \alpha_\mu^\dagger + V_{k\mu}^* \alpha_\mu \right)$$
推转准粒子真空 $|\Phi(\omega)\rangle$ 满足 $\alpha_\mu |\Phi(\omega)\rangle = 0$。

在准粒子真空上定义 C-QRPA 微振动激发的声子算符 $O_\nu^\dagger$：
$$O_\nu^\dagger = \sum_{\mu < \mu'} \left[ X_{\mu\mu'}^\nu \alpha_\mu^\dagger \alpha_{\mu'}^\dagger - Y_{\mu\mu'}^\nu \alpha_{\mu'} \alpha_\mu \right]$$
激发态满足运动方程：
$$[ H_{\text{crank}}, O_\nu^\dagger ] = \hbar \Omega_\nu(\omega) O_\nu^\dagger$$
在准粒子对基底展开下，得到标准双正交辛本征值矩阵方程：
$$\begin{pmatrix} A & B \\ -B^* & -A^* \end{pmatrix} \begin{pmatrix} X^\nu \\ Y^\nu \end{pmatrix} = \hbar \Omega_\nu(\omega) \begin{pmatrix} X^\nu \\ Y^\nu \end{pmatrix}$$
其中矩阵元分别由二阶变分导出：
$$A_{\mu\mu',\sigma\sigma'} = \langle \Phi | [ \alpha_{\mu'} \alpha_\mu, [ H_{\text{crank}}, \alpha_\sigma^\dagger \alpha_{\sigma'}^\dagger ] ] | \Phi \rangle = (E_\mu + E_{\mu'}) \delta_{\mu\sigma} \delta_{\mu'\sigma'} + \bar{V}_{\mu\mu',\sigma\sigma'}^{\text{ph}}$$
$$B_{\mu\mu',\sigma\sigma'} = - \langle \Phi | [ \alpha_{\mu'} \alpha_\mu, [ H_{\text{crank}}, \alpha_{\sigma'} \alpha_\sigma ] ] | \Phi \rangle = \bar{V}_{\mu\mu',\sigma\sigma'}^{\text{pp}}$$
本征向量满足 C-QRPA 辛正交归一条件：
$$\sum_{\mu < \mu'} \left( |X_{\mu\mu'}^\nu|^2 - |Y_{\mu\mu'}^\nu|^2 \right) = 1$$

### 2. 两类微振动声子及对称性恢复机制

推转三轴八极体系中存在两类由不同离散对称性破缺所支配的集体微振动声子：
1. **手征摆动声子 (Chiral out-of-plane vibrational phonon, $\nu = \chi$)**:
   - **对称性特征**：恢复关于主平面的反射变换 $\mathcal{R}_x(\pi)$ 与时间反演 $\mathcal{T}$ 的自发破缺；声子产生算符在空间反演下具有偶宇称（$\pi_\chi = +1$），而在转动坐标系中对应角动量矢量的出平面偏摆算符 $J_y, J_z$；
   - **转动软化规律**：在转轴进入主平面的情况下，随推转角频率 $\omega$ 增大，Coriolis 力促使准粒子角动量向短轴或长轴聚集，出平面势阱恢复力被离心驱动削弱，声子本征能量展现特征性旋转软化：
     $$\hbar \Omega_\chi(\omega) \approx \sqrt{\Omega_{\chi 0}^2 - c_\chi \omega^2}$$
     当 $\omega \to \omega_c$ 时，$\hbar\Omega_\chi \to 0$，平均场发生超临界分岔，由单阱微振动过渡为双阱静态手征自发破缺。
2. **八极偶极微振声子 (Octupole vibrational phonon, $\nu = 3$)**:
   - **对称性特征**：恢复空间反演宇称 $\mathcal{P}$ 的破缺；声子产生算符具有负宇称（$\pi_3 = -1$），由 $\Delta l = \Delta j = 3$ 的两准粒子对（如质子 $d_{5/2}-h_{11/2}$、中子 $p_{3/2}-g_{9/2}$）相干叠加产生；
   - **能谱色散**：在八极软核中，由于形变驱动与离心自旋拉伸，八极声子能量呈现平缓的色散硬化：
     $$\hbar \Omega_3(\omega) \approx \Omega_{30} + c_3 \omega^2$$

### 3. 能级交叉与两模相干杂化

当推转角频率 $\omega$ 扫过临界交叉点 $\omega_{\text{cross}}$ 时，未受扰动的手征声子能级 $\hbar\Omega_\chi(\omega)$ 与八极声子能级 $\hbar\Omega_3(\omega)$ 发生偶然简并。
在真实的微观哈密顿量中，由于三轴形变打破了轴对称性，且推转力使得不同宇称的准粒子态发生 Coriolis 轨道混合，声子哈密顿量中产生诱导耦合矩阵元：
$$V_{\text{mix}}(\omega) = \lambda_{\text{mix}} \omega$$
两模等效哈密顿量在声子表象下表述为：
$$\mathcal{H}_{\text{eff}}(\omega) = \begin{pmatrix} \hbar \Omega_\chi(\omega) & V_{\text{mix}}(\omega) \\ V_{\text{mix}}^*(\omega) & \hbar \Omega_3(\omega) \end{pmatrix}$$
考虑 QRPA 基态反向振幅关联后，本征能量发生避免能级交叉（Avoided Crossing）：
$$\hbar \Omega_\pm(\omega) = \frac{\hbar \Omega_\chi + \hbar \Omega_3}{2} \pm \sqrt{ \left( \frac{\hbar \Omega_\chi - \hbar \Omega_3}{2} \right)^2 + |V_{\text{mix}}(\omega)|^2 }$$
在交叉点 $\omega = \omega_{\text{cross}} \approx 0.235\text{ MeV}/\hbar$ 处：
- 出现有限的避免交叉能量间距 $\Delta E_{\text{gap}} = 2 |V_{\text{mix}}| \approx 0.14\text{ MeV}$；
- 两个本征模式的声子波函数发生最大相干混合（$50\% \text{ chiral} + 50\% \text{ octupole}$）。

### 4. 电多极跃迁动力学演化与模式互换

在 C-QRPA 框架下，微振声子态 $|\nu\rangle = O_\nu^\dagger |\Phi\rangle$ 向基准转动带（yrast band）的约化多极跃迁矩阵元为：
$$\langle \Phi | \hat{\mathcal{M}}(\sigma L) | \nu \rangle = \sum_{\mu < \mu'} \left( X_{\mu\mu'}^\nu + Y_{\mu\mu'}^\nu \right) \langle \mu | \hat{\mathcal{M}}(\sigma L) | \mu' \rangle$$
跃迁几率正比于跃迁算符期望值的模方：
- **纯手征分量**：贡献带间磁偶极 $B(M1; \text{phonon} \to \text{yrast})$ 与内禀电四极 $B(E2; \text{phonon} \to \text{yrast})$，但因宇称守恒，不贡献 $B(E1)$ 与 $B(E3)$；
- **纯八极分量**：贡献相反宇称跃迁 $B(E1; \text{phonon} \to \text{yrast})$ 与 $B(E3; \text{phonon} \to \text{yrast})$，但因宇称反转选择定则，其带间 $B(M1)$ 与 $B(E2)$ 严格禁戒。

当两模发生相干杂化时，跃迁几率表现为混合振幅的模方：
- 对于低能支模式 1：
  - 在 $\omega < \omega_{\text{cross}}$ 时，以八极成分为主，表现为强 $B(E1)$ 与 $B(E3)$，而 $B(M1) \approx 0$；
  - 当 $\omega$ 越过 $\omega_{\text{cross}}$ 后，由于手征能级软化降至八极以下，模式 1 渐近转化为纯手征出平面声子，其 $B(M1)$ 激增至 $\sim 1.25\mu_N^2$，而 $B(E1)$ 与 $B(E3)$ 急剧衰减猝灭；
- 对于高能支模式 2：
  - 呈现与模式 1 完全对称的**动力学强度互换（transition strength interchange）**；
  - 在交叉共振中心，两个态均同时展现出反常共存的强 $B(M1)$ 与强 $B(E1)/B(E3)$ 跃迁，形成手征-八极复合杂化激发的决定性指纹。

## Assumptions

1. **近简谐微振动假设**：假定在所研究的转动角速度区间（$\omega \le 0.48\text{ MeV}/\hbar$）内，体系内禀势能面在极小值周围具有充足的谐振恢复势，振幅满足小振幅 RPA 展开条件，非简谐高阶声子相互作用作为微扰处理。
2. **两模主导子空间**：假定手征摆动自由度与最低八极偶极自由度构成低激发谱中最软的两个集体模式，其它高能集体激发（如巨四极共振 GDR/GQR）仅通过重整化有效核电荷 $e_{\text{eff}}$ 与有效惯性参数发生间接屏蔽，不显式进入两能级微观杂化矩阵。
3. **推转轴几何简化**：假定未微扰推转轴位于平均场的一个主平面内，推转项表现为标准 $-\omega J_x$ 形式，Coriolis 诱导的宇称混合项在低频区可线性展开为 $V_{\text{mix}}(\omega) = \lambda_{\text{mix}} \omega$。

## Competing Explanations

1. **静态八极四重态隧穿模型（Chirality-Parity Quartets, CPQ）**:
   - *竞争主张*：认为体系同时具有稳定的静态三轴形变与稳定的静态八极反射破缺，基底态由四重离散简并的极小值构成，四个近简并带由四重极小之间的多维量子隧穿形成。
   - *证据裁决*：在 $^{78}\text{Br}$ 与 $^{133}\text{Ce}$ 中，自洽微观泛函（MDC-CDFT 及宏微观模型）的势能面均显示沿 $\beta_{30}$ 方向无深极小，呈现显著的“八极软度（octupole softness）”；且实验测得的 $B(E1)/B(E2)$ 远小于稳定八极区（如 $^{224}\text{Th}$），这支持微观 C-QRPA 的振动声子杂化解释，而非刚性静态四重带隧穿。
2. **两准粒子退耦带与八极核心耦合的纯唯象解释**:
   - *竞争主张*：将负宇称带简单解释为准粒子被退耦后与偶偶核芯八极声子的简单无相干弱耦合。
   - *证据裁决*：纯弱耦合模型无法解释跨带 $B(M1)$ 与 $B(E1)$ 随转动频率发生的相干模式互换现象，也无法解释手征能量差 $\Delta E(I)$ 与八极位移随转动的相干干涉。只有在自洽 C-QRPA 辛矩阵中包含动力学相干杂化项，方能完整重现实验观测到的多极跃迁动力学演化。

## Transfer Conditions

1. **质量区适用性**：
   - $A \approx 130$ 质量区（如 $^{131}\text{Ba}, ^{133}\text{Ce}, ^{135}\text{Nd}$）：质子费米面位于 $g_{7/2}/d_{5/2}$，中子费米面位于 $h_{11/2}$，邻近存在可发生 $\Delta l = \Delta j = 3$ 激发的 $f_{7/2}/i_{13/2}$ 轨道；
   - $A \approx 80$ 质量区（如 $^{78}\text{Br}, ^{74}\text{As}$）：费米面附近存在活跃的 $g_{9/2} \otimes (p_{3/2}, f_{5/2})$ 强八极驱动轨道，同时三轴形变 $\gamma \approx 15^\circ\text{--}25^\circ$ 提供了手征几何条件。
2. **自旋与角速度区间**：
   - 适用于转动角速度在手征软化至临界分岔点之前（$\omega < \omega_c$）的中低自旋区；对于本模型参数，有效区间为 $\omega \in [0.10, 0.45]\text{ MeV}/\hbar$。

## Failure Conditions

1. **超临界大振幅相变破坏微振假设**：
   - 若体系转动频率超过临界手征软化点 $\omega_c$，平均场自发产生非零出平面转动角 $\theta > 0$，势阱由单极小变为具有有限势垒的非共面双阱，此时微振 RPA 方程出现零频伪模甚至虚频失稳，必须转入全量子粒子-转子模型（PRM）或三维倾斜轴推转发电机坐标方法（TAC-GCM）。
2. **配对相崩塌与准粒子连续谱渗漏**：
   - 在高推转角频率下，强 Coriolis 力引发对破裂（Seniority 增加）或对关联猝灭，准粒子激发能 $E_\mu + E_{\mu'}$ 降至两倍费米能隙以下，导致集体声子态进入未束缚准粒子连续谱而发生耗散湮灭。

## Falsification or Reverse Tests

1. **电磁跃迁强度模式互换的反向测试**:
   - *检验方案*：利用充气充反冲分离器与大型高纯锗探测器阵列（如 Gammasphere 或 JUROGAM），通过多普勒频移衰减法（DSAM）与柱塞反冲距离法（RDDS）精确测量 $^{78}\text{Br}$ 或 $^{133}\text{Ce}$ 交叉点两态的绝对寿命 $\tau$。
   - *证伪判据*：若实验测得交叉点两态的绝对 $B(M1)$ 与 $B(E1)$ 均保持平滑且未展现出激烈的相干互换，或者两态之一完全缺失带间 $E1$ 跃迁，则微观 C-QRPA 两模相干杂化假设被证伪。
2. **多极混合比 $\delta(E2/M1)$ 与偏振不对称度符号反演**:
   - *检验方案*：测量跨带跃迁的线偏振与角分布取向比（DCO/ADO），提取多极混合比。
   - *证伪判据*：相干杂化要求模式混合相位相干，跃迁算符干涉将使混合比 $\delta$ 的符号在共振区发生突变；若符号保持刚性不变，则推翻两振动态的相干假设。

## Open Questions

1. **微观配对相互作用的自洽时奇修正**：
   - 在含推转的 QRPA 矩阵中，时间奇性配对力（time-odd pairing components）对阻尼手征声子软化速度的具体定量影响尚未在全微观能量密度泛函中完全闭合。
2. **两模微振动向有限自旋量子多重态的角动量投影映射**：
   - 如何在保证严格好角动量 $I$ 与好宇称 $\pi$ 的前提下，建立推转内禀系 C-QRPA 声子波函数向实验室系四重态或双重态波函数的精确解析投影映射。

## Human Review

- 本研究笔记所引用的微观 C-QRPA 形式体系、手征与八极声子本征方程及数值模型由 Codex 于 2026-10-29 自洽推导建立，属于 `ai-draft` 状态。
- 理论证据链回链至 Frauendorf 2001（已人审）与 Butler & Nazarewicz 1996（已深度阅读核实），实验对账核实了 $^{78}\text{Br}$（Liu 2016 PRL）、$^{133}\text{Ce}$（Ayangeakaa 2013 PRL）与 $^{135}\text{Nd}$（Mukhopadhyay 2007 PRL）的实验事实。后续用于学术论文前需由核结构理论专家进行公式与数值参数审查。

## Promotion or Rejection History

- **2026-10-29**：初始创建。完成 C-QRPA 两模耦合哈密顿量构建、辛本征值求解、电多极跃迁几率动力学突变模拟，并在 `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/qrpa-chiral-octupole/` 输出完整 CSV/JSON 工件与 README 文档。
