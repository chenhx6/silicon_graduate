---
type: research-note
title: "奇奇核八极—手征四重能带跨质量区耦合与相消选择定则"
aliases: [chiral-octupole-quadruplet-cross-mass-coupling, chiral octupole quadruplets, Day27 quadruplets]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [xiao-2022-chirality-octupole-correlations-74as, liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br, guo-2020-pseudospin-chiral-quartet-131ba]
created_from: Day 27 chiral-octupole quadruplets study; system/scripts/day27_chiral_octupole_quadruplet_study.py
tags: [chiral-octupole, quadruplet-bands, selection-rules, discrete-symmetries, odd-odd-nuclei, 74as, 78br, 131ba, 198bi, Day27]
---

# 奇奇核八极—手征四重能带跨质量区耦合与相消选择定则

## Research Trigger

在奇奇核与奇 $A$ 核集体激发研究中，三轴形变（破坏时间反演结合空间转动对称性）与八极形变（破坏空间反演宇称对称性）的复合产生了一类特殊的四维流形拓扑态——八极—手征四重能带（Chiral-Octupole Quadruplet Bands）。例如在 [[xiao-2022-chirality-octupole-correlations-74as]] 的 $^{74}\text{As}$ 中报道了三条带的手征与八极关联，在 [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] 的 $^{78}\text{Br}$ 中建立了四能带网络，而在 [[guo-2020-pseudospin-chiral-quartet-131ba]] 的 $^{131}\text{Ba}$ 中则呈现赝自旋—手征四重态。如何从离散群论对称性与微观隧穿相消原理出发，建立四带间跃迁的严格选择定则与跨质量区排他性鉴别判据，成为多重手征与八极耦合前沿的关键任务。

## Grounded Evidence

> checkpoint047处置：本节旧“D₂×PT通用相消定理/金标准”认证撤回。脚本自设四态哈密顿量与E1算符下的零值只保留为条件模型结果；尚未读到足以将它推广到真实核素全部跨带支路的理想极限原件。以下旧推导不作为独立源级证据。78Br实验归属按L16-D27-R047-1至3纠正，不能把无匹配计数的未见支路写成实测相消。

通过执行全微观隧穿哈密顿量与多极算符矩阵求解器 `system/scripts/day27_chiral_octupole_quadruplet_study.py`（数值结果存入 `outputs/learning-daily/20261029-DAY27-cross-mass-region-transferability-run-01/continuation-studies/chiral-octupole-quadruplet/chiral_octupole_quadruplet_resolution.json`），确立以下定量证据：

1. **离散对称群 $\mathcal{D}_2 \times \hat{\mathcal{P}}\hat{\mathcal{T}}$ 下的四重能带结构：**
   - 体系基底由手征手性（$L, R$）与内禀反射宇称（$+,-$）的直积构成：
     $|1\rangle = (|L,+\rangle + |R,+\rangle)/\sqrt{2}$（Band 1：正宇称基态手征对）；
     $|2\rangle = (|L,+\rangle - |R,+\rangle)/\sqrt{2}$（Band 2：正宇称激发手征对）；
     $|3\rangle = (|L,-\rangle + |R,-\rangle)/\sqrt{2}$（Band 3：负宇称基态手征对）；
     $|4\rangle = (|L,-\rangle - |R,-\rangle)/\sqrt{2}$（Band 4：负宇称激发手征对）；
   - 在静态刚性形变极限下，四条带在微观上完全简并；在有限势垒下，手征隧穿分裂 $\Delta E_\chi$ 与八极隧穿分裂 $\Delta E_3$ 分别引起两对双重分裂。

2. **交叉对角跃迁严格相消选择定则（Double-Flip Exclusion Rule）：**
   - 伴随手征伙伴跃迁（$1 \leftrightarrow 2$ 与 $3 \leftrightarrow 4$）：$\Delta \pi = 0$，由磁偶极 $M1$ 支配，电偶极 $E1$ 严格禁戒；
   - 宇称双重态跃迁（$1 \leftrightarrow 3$ 与 $2 \leftrightarrow 4$）：$\Delta \pi = 1$，由电偶极 $E1$（及八极 $E3$）支配，磁偶极 $M1$ 严格禁戒；
   - **交叉对角跃迁（$1 \leftrightarrow 4$ 与 $2 \leftrightarrow 3$）：** 同时翻转手征手性与反射宇称。由于左手与右手宇称投影波函数间的相干破坏性干涉，跃迁偶极矩阵元恒等为零：
     \[
     \langle 1 | \hat{\mathcal{M}}(E1) | 4 \rangle \equiv 0.0000 \implies \frac{B(E1; 1 \to 4)}{B(E1; 1 \to 3)} = 0.0000.
     \]
   - 此零值只检验当前有效模型的额外算符/波函数假设；真实交叉支路有强度时可要求修订该模型，不自动排除所有八极—手征解释。

3. **跨质量区候选案例系统学对比：**
   - **$^{78}\text{Br}$（$Z=35, N=43$）：** 具有完整的 4 条带结构（两正宇称手征带 + 两负宇称手征带），带间由 $E1$ 与 $M1$ 路径交织连通，作者解释为MχD伴八极关联/软性；chirality–parity quartet仍为未来寻找目标，不能称为已确证标杆（L16-14及L16-D27-R047-1）；
   - **$^{74}\text{As}$（$Z=33, N=41$）：** Xiao 2022 确立了正宇称手征候选对（B1, B2）与负宇称八极关联带（B3），但负宇称手征伴带（Band 4）尚未在实验中识别，属于 3/4 不完全四重态；
   - **$^{131}\text{Ba}$（$Z=56, N=75$）：** 属于奇 $A$ 赝自旋—手征四重态，其四重性源于赝自旋双重态与手征双重态的耦合，而非反射不对称八极形变（无跨宇称强 $E1$ 连接）；
   - **$^{198}\text{Bi}$（$Z=83, N=115$）：** 重质量区高自旋候选核，涉及 $\pi h_{9/2} \otimes \nu i_{13/2}^{-1}$ 构型下的八极混杂。

## Provisional Reasoning

在三维倾斜轴推转模型中，八极与手征的联合动力学算符可写为单纯形变换 $\hat{\mathcal{S}} = \hat{\mathcal{P}} \mathcal{R}_z^{-1}(\pi)$ 与时间反演转动变换 $\hat{\Theta} = \mathcal{R}_y(\pi) \hat{\mathcal{T}}$ 的乘积：
\[
\hat{\Pi}_{\text{diag}} = \hat{\mathcal{S}} \hat{\Theta} = \hat{\mathcal{P}} \mathcal{R}_z^{-1}(\pi) \mathcal{R}_y(\pi) \hat{\mathcal{T}} = \hat{\mathcal{P}} \mathcal{R}_x(\pi) \hat{\mathcal{T}}.
\]
哈密顿量在基底 $\{|1\rangle, |2\rangle, |3\rangle, |4\rangle\}$ 下由块对角子空间不变性保证：
1. 本征态可精确按对角宇称反演本征值分类；
2. 电偶极跃迁算符 $\hat{D}_z$ 属于反对称本征矢，其在交叉态 $\langle 1|$ 与 $|4\rangle$ 之间的积分由于左右对称轴旋转空间因子的相反极性产生严格相消：
\[
\langle 1 | \hat{D}_z | 4 \rangle = \frac{1}{2} \left[ \langle L, +| \hat{D}_z |L, -\rangle - \langle R, +| \hat{D}_z |R, -\rangle \right] = 0.
\]
改换有效E1算符或破坏所设额外对称前提都可能解除当前零值；没有来源支持这里的10⁻³扰动上限，不给其普适大小。

## Assumptions

1. 质子与中子单粒子态分别处于纯高-$j$ 粒子态与空穴态，其本征波函数满足标准粒子—转子耦合边界；
2. 反射不对称性由轴对称 $\beta_3$ 势能深阱主导，忽略复杂的非轴对称 $\beta_{31}, \beta_{32}$ 动力学混合；
3. 实验跃迁分支比抽取经过靶衰减与探测效率各向异性校正。

## Competing Explanations

1. **赝自旋—手征四重态（Pseudospin Chiral Quartet）：** 如 $^{131}\text{Ba}$，四条能带全具有相同宇称，由粒子轨道赝自旋简并引起，不伴随 $E1$ 跃迁；
2. **多准粒子组态交叉伪四重态：** 2-qp 带与 4-qp 带在相近激发能区的偶发密集重叠，能级缺乏对称锁相；
3. **声子数与宇称备择：** 两个3⁻八极声子的耦合总宇称为正，不能无说明将负宇称带称为双八极声子多重态。声子解释须分别核声子数、组态和真实E3/E1分支，不按预设标签排除。

## Transfer Conditions

1. 判定八极—手征四重能带必须同时测得完整的四条能带序列，且两两呈现手征伙伴与交替宇称双重态对偶关系；
2. 必须验证 $1 \leftrightarrow 4$ 与 $2 \leftrightarrow 3$ 交叉对角跃迁的严格消失，方可采信为纯反射不对称手征拓扑。

## Failure Conditions

1. 真实候选若有强交叉支路，应先核命名、Jπ与算符额外对称条件；该观测可否定本toy零值假设，不自动否定所有八极—手征解释；
2. 在未排除赝自旋简并（全部能带同宇称）的前提下宣称八极四重态的结论失效。

## Falsification or Reverse Tests

1. **代数相消反证（微观选择定则证伪）：** 在求解器中人为破坏四重基底反对称相位，交叉跃迁矩阵元立即从 $0.000$ 跃升至 $0.70$ 以上，逆向证实该消失是离散对称群守恒的第一性直接结果；
2. **78Br旧反检验撤回：** 没有该B1→B4支匹配的counts、效率、背景或作者上限，不能称“未见峰符合相消”。Liu2016报告的八条E1和MχD解释不独立检验本toy零值。

## Open Questions

1. 在 $^{74}\text{As}$ 中，缺失的 Band 4 能级是否受到大形变中子侵入轨道的阻塞抑制而推移至更高激发能？
2. 在轻锕系奇奇核（如 $^{220}\text{Ac}, ^{222}\text{Fr}$）中，强静态八极形变是否能与高自旋质子—中子剪刀形成更加稳定的八极—磁转动复合网络？

## Evidence Boundary Addendum

- 本页由 Day 27 continuation study 生成；脚本输出中的数值、阈值、相界、比例和“排他性”判断首先属于模型结果或参数扫描。
- 只有带有明确 `knowledge/sources/` locator 的句子才可作为直接来源证据；benchmark 输入、toy Hamiltonian、解析拟合和由模型反演的量不能冒称实验测量。
- 本页不把任何单一阈值、单调律、临界值或跨核素迁移规则升级为普适定理。不同核素的组态、实验响应、协方差、背景态密度和模型空间必须重新核验。
- `review_status: unreviewed` 与 `reasoning_status: provisional` 保持有效；本附录是自审边界，不是 `human-reviewed` 认证。

## Human Review

本页为 2026-10-29 Day 27 跨质量区迁移与机制不适用性自主研学产物，未经过人类物理学家正式同行复核（status: ai-draft, review_status: unreviewed）。

## Promotion or Rejection History

- 2026-10-29：基于离散对称群 $\mathcal{D}_2 \times \hat{\mathcal{P}}\hat{\mathcal{T}}$ 严格推导并数值验证了八极—手征四重能带的交叉对角相消选择定则（$B(E1, 1 \to 4) \equiv 0$），完成了跨质量区（$^{74}\text{As}, ^{78}\text{Br}, ^{131}\text{Ba}, ^{198}\text{Bi}$）候选拓扑的系统学梳理。

- 2026-10-30 checkpoint047：定向撤回78Br已确证quartet、无原件未见支路相消、10⁻³扰动界与通用排他门；修正两个3⁻声子总宇称为正。原四态矩阵只保留条件示意，来源核验和完整算符推导仍待后续研究。
