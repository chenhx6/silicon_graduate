---
type: research-note
title: "多步库仑激发中的 Cline 不变量与八极动态柔软判据"
aliases: [Cline octupole invariants, octupole static dynamic criterion]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
confidence: medium
evidence_sources: [cline-1986-nuclear-shapes-coulomb-excitation, gosia-2012-manual-sigma-invariants, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution, nndc-224ra-adopted-cluster-decay]
created_from: Day26 Cline invariant and octupole softness study
promotion_target: octupole-and-rare-electromagnetic-decay
tags: [Cline-invariants, Coulomb-excitation, octupole, softness, 144Ba, 146Ba, 224Ra]
sources: [cline-1986-nuclear-shapes-coulomb-excitation, gosia-2012-manual-sigma-invariants, bucher-2016-144ba-direct-octupole, bucher-2017-146ba-direct-octupole, gaffney-2013-pear-shaped-rn-ra, butler-2020-222-228ra-octupole-evolution, nndc-224ra-adopted-cluster-decay]
---

# 多步库仑激发中的 Cline 不变量与八极动态柔软判据

## Research Trigger

本轮问题是把多步库仑激发得到的实验室系约化矩阵元网络，重写成内禀坐标无关的旋转标量，并检查一个大 `E3` 是否足以区分静态梨形与八极动态涨落。Cline 的原综述把二至六阶张量标量、符号/相位、有限中间态和缺失强度放在同一方法链中（Cline 1986, PDF p.698 的六行耦合式；pp.699–700 的完整性和算符限制）。本任务特别需要把八极二阶不变量 `⟨Q3²⟩` 与更高阶的 `⟨Q3⁴⟩` 分开，避免把 `B(E3)` 的单条强跃迁直接写成静态形变证明。

本页是 `research-note`，`review_status: unreviewed`、`reasoning_status: provisional`；它不是对所有输入 source 页的人工认证。可复现工件位于 [octupole-cline-invariants worker](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-cline-invariants/)。

## Grounded Evidence

### 1. Cline 不变量的实验输入和闭合求和

库仑激发直接拟合的是实验室系约化矩阵元 `⟨I_f||M(Eλ)||I_i⟩`。采用

\[
B(E\lambda;I_i\to I_f)=\frac{|\langle I_f\Vert M(E\lambda)\Vert I_i\rangle|^2}{2I_i+1},
\]

则对给定初态 `i` 的完整终态闭合，二阶电多极标量可以写成

\[
\mathcal I_\lambda(i)=\langle i|M_\lambda^\dagger\!\cdot M_\lambda|i\rangle
  =\sum_{f\;\mathrm{complete}}B(E\lambda;i\to f),
\]

其中“complete”包括所有相关终态、角动量分支、符号相干的耦合路径和实验可见/不可见的补足项。对 `I_i=0` 的 `0+→3−`，`B(E3;0+→3−)=|⟨3−||M(E3)||0+⟩|²`；反向衰变的 `B(E3;3−→0+)` 还要除以 `2J_i+1=7`。这正是本轮脚本同时输出 `B_up_or_closure` 和 `B_down` 的原因。

Cline 原件的二至六阶标量包括四极项 `⟨Q2²⟩`、`⟨Q2³ cos(3δ)⟩` 及更高阶 `Q2⁴`、`Q2⁵ cos(3δ)`、`Q2⁶` 和 `Q2⁶ cos²(3δ)`；多步产额中矩阵元的相对符号不可由 `B` 模单独恢复（Cline 1986, PDF p.698）。原文还明确指出高阶不变量对未观测强度、有限耦合网络和算符对易性质更敏感（PDF pp.699–700）。GOSIA 2012 手册则把实际 SIGMA 实现的奇次正幅度矩写成偶次矩根插值，并将误差近似与真实核内方差分开（Chapter 9, pp.223–226；源码 `sigma.f` lines 423–455）。

### 2. 八极二阶不变量的轴对称归一

本页固定电八极算符约定为球谐归一的 `M(E3)`，并把通常的轴对称内禀电八极矩记为 `Q30`（单位 `e fm³`）。对刚性 `K=0` 轴对称梨形，实验室闭合标量与内禀矩满足

\[
\boxed{\;\langle Q_3\!\cdot Q_3\rangle
      =\mathcal I_3
      =\frac{7}{16\pi}Q_{30}^{\,2}\;}.
\]

因此 `0+→3−` 的转子约化矩阵元在同一约定下为

\[
|\langle3^-\Vert M(E3)\Vert0^+\rangle|
 =\sqrt{\mathcal I_3}
 =\sqrt{\frac{7}{16\pi}}|Q_{30}|.
\]

这不是把任意 `B(E3)` 直接等同于 `Q30²`；它依赖 `K=0` 轴对称转子关系、完整或近完整闭合和统一的 `e fm³` 约定。脚本把 `1 e b^{3/2}=1000 e fm³` 显式写入并复算：`144Ba` 的 `0.65 e b^{3/2}` 给 `Q30≈1742 e fm³`，与 Bucher 报告的 `Q3=1.73(^{+0.45}_{−0.62})×10³ e fm³` 相容；`224Ra` 的 `940(30) e fm³` 给 `Q30≈2519 e fm³`，与 Gaffney 的 `Q3=2520(90) e fm³` 相符（Bucher 2016 PDF p.4；Gaffney 2013 PDF Tables 1–2）。这是一致性重算，不是新实验提取。

### 3. 四极和混合不变量

在 Cline 的内禀坐标参数化中，可把四个最低阶标量记作

\[
\mathcal I_{22}=\langle Q_2^2\rangle,\qquad
\mathcal I_{23}=\langle Q_2^3\cos3\delta\rangle,
\]
\[
\mathcal I_{33}=\langle Q_3^2\rangle,\qquad
\mathcal I_{233}=\langle Q_2Q_3^2\rangle.
\]

若只做固定内禀点的代数控制，`Q2=q2`、`δ`、`Q3=q3` 给 `q2²`、`q2³cos(3δ)`、`q3²` 和 `q2q3²`。真实实验中的这些量是矩阵元网络和耦合系数的标量求和，不能用一个 `β2,β3,γ` 代替。尤其 `Q2Q3²` 需要同时覆盖四极和八极激发路径；单条 `E3` 不能测出它。

### 4. 静态与动态的严格代数分层

**刚性内禀点。** 若把八极坐标约束为 `Q30=q0`，则

\[
\langle Q_{30}\rangle=q_0,\quad
\langle Q_{30}^{2}\rangle=q_0^2,\quad
\langle Q_{30}^{4}\rangle=q_0^4,
\]
\[
\operatorname{Var}(Q_{30}^{2})
 =\langle Q_{30}^{4}\rangle-\langle Q_{30}^{2}\rangle^2=0,
\qquad
\mathcal I_3=\frac{7}{16\pi}q_0^2.
\]

这里的零方差是“刚性坐标分布”的理想极限。有限核的宇称恢复态满足 `⟨0+|Q3|0+⟩=0`，即使其内禀波函数集中在 `±q0` 两个井上；所以实验室 `⟨Q3⟩=0` 不是静态形变的否定条件。

**简谐八极振子。** 对

\[
H_3=\frac{P_3^2}{2B_3}+\frac12C_3Q_{30}^2,
\qquad \omega_3=\sqrt{C_3/B_3},
\]

基态是偶宇称高斯态：

\[
\langle Q_{30}\rangle=0,\qquad
\langle Q_{30}^2\rangle_{\rm zp}=\frac{\hbar}{2\sqrt{B_3C_3}},
\]
\[
\langle Q_{30}^4\rangle=3\langle Q_{30}^2\rangle^2,
\quad
\operatorname{Var}(Q_{30}^{2})=2\langle Q_{30}^2\rangle^2,
\quad
\langle Q_3^2\rangle=\frac{7}{16\pi}\frac{\hbar}{2\sqrt{B_3C_3}}.
\]

用户问题中的 `σ²(Q3)=⟨Q3⁴⟩−⟨Q3²⟩²` 按字面是 `Var(Q3²)`；若要写 `Var(Q3)`，简谐基态应为 `⟨Q3²⟩−⟨Q3⟩²=⟨Q3²⟩`。二者不能混用。非简谐软势仍满足偶宇称基态 `⟨Q3⟩=0`，但 `⟨Q3⁴⟩` 不再必为 `3⟨Q3²⟩²`；因此高阶不变量是区分“固定幅度”和“宽分布”的必要信息。

**最小严格判据。** 在同一算符与同一闭合约定下，静态候选要求：`I3` 非零、多个独立 E3 路径转成的 `Q3(I_i,I_f)` 在协方差允许范围内近似恒定、`Var(Q3²)` 足够小，并由交错宇称能级和 E1/E3 分支作 companion test。动态候选要求：`I3` 非零但存在显著四阶宽度、低激发 `3−` 与接近 `2ℏω3` 的多声子结构、以及随自旋/路径变化的 E3 图样。前者是联合判据，后者也是联合判据；单项 `B(E3)` 均不足以排他裁决。

### 5. 144Ba、146Ba 与 224Ra 的证据落点

| 核素 | 实验直接层 | 不变量可做什么 | 两声子/分支比边界 |
|---|---|---|---|
| `144Ba` | Bucher 2016 的 `0+↔3−` 直接 E3：`⟨3−||E3||0+⟩=0.65^{+0.17}_{−0.23} eb^{3/2}`，`B(E3;3−→0+)=48^{+25}_{−34} W.u.`，并报告转子约定 `Q3≈1.73×10³ e fm³`（PDF pp.3–4, Table I）。 | 可给一个强 `I3` 项并检查单位/转子换算；不能完成 `Q3²` 的终态闭合，也不能测 `Q2Q3²` 或 `Var(Q3²)`。 | 本源没有闭合 `0+,2+,4+,6+` 八极两声子 quartet；当前不能把大 E3 写成静态刚性证明。 |
| `146Ba` | Bucher 2017 的 `0+↔3−` E3 与 `144Ba` 相容：`B(E3)=48^{+21}_{−29} W.u.`；E1/dipole 强度显著受中子占据与相消影响（PDF pp.2–5, Table I/Figs.3–5）。 | 可复算同一 `I3` 约四十多万 `e²fm⁶` 的单项，并显示强 E3 与小 E1 可共存；不能由 E1/E3 比值给出闭合八极分布。 | 没有源中可复核的两声子 quartet；E1 是相消敏感的 companion，不能设定普适静态/振动阈值。 |
| `224Ra` | Gaffney 2013 的多态库仑激发给 `Q3≈2520(90) e fm³`，`Q2≈632(10) e fm²`，并把更相干的多跃迁图样与梨形/静态解释联系起来；该文同时保留静态宇称投影与八极振动的不可区分边界（PDF pp.199–203，Tables 1–2/Figs.3–5）。 | 多跃迁 `Q3` 平坦度比单条 E3 更有判别力；仍需释放耦合项、保留完整协方差，不能把转子转换当密度成像。 | ENSDF 224Ra 给 `3−=290.352 keV`，所以简谐两声子目标约 `580.704 keV`；`0+=916.38`、`2+=965.65 keV` 只是候选/未指派，`4+=250.782` 与 `6+=479.12 keV` 明确是基带成员，不能冒充两声子 quartet（ENSDF PDF pp.1–2）。 |

Butler 2020 的 `222Ra/228Ra` 多条 E3 是跨核的强方法参照：`222Ra` 的多条 `Q3` 近似稳定，而 `228Ra` 存在近零 `2+→3−` 链；但星号项由转子关系耦合，不能直接作为完整独立 closure（PRL pp.3–5, Table I/Fig.4）。它支持“多条 E3 图样优于单条强度”的方法层判断，不替代 `224Ra` 的能级审计。

### 6. E1/E3 分支比的正确用法

在静态反射不对称转子中，E1、E2、E3 由同一内禀波函数产生，交错宇称带之间可同时出现 E1 和 E3；在八极振动中，E3 主要跟随八极坐标的声子数改变，而 E1 还受质子/中子偶极算符、有效电荷、组态混合和相消影响。因此应比较同一 GOSIA 网络、相同 feeding/效率校正、同一相位约定下的 E1/E3 分支，不应规定一个跨核的 `B(E1)/B(E3)` 硬阈值。

`146Ba` 是直接反例：强 E3 保持而 E1/dipole 显著降低，Bucher 2017 将其联系到中子轨道占据和偶极贡献相消（PDF pp.3–5）。这支持“E1 小不能否定八极集体性”，但不能单独选择静态或动态模型。`224Ra` 的 E1/E3 多跃迁与交错宇称能级可以作为联合判据，仍需注意 GOSIA 中耦合项和未观测态的 closure 缺口。

## Provisional Reasoning

1. **不变量层级。** `Q2²`、`Q2³cos3δ`、`Q3²` 和 `Q2Q3²` 是实验室矩阵元网络的旋转标量；“内禀坐标无关”指旋转标量，不表示对有限终态截断、GOSIA 先验或电荷密度模型无关。
2. **静态/动态不可由二阶项唯一识别。** 刚性点和简谐基态都能给出非零 `⟨Q3²⟩`。要区分它们，至少需要四阶宽度或等价的多跃迁/多声子/宇称能量伴随信息。
3. **最小可操作判据。** 对每个初态建立 `E3` closure ledger，逐条用 `B(E3;I_i→I_f)` 求 `I3(I_i)`；把每条转换为 `Q3(I_i,I_f)` 后做协方差加权平坦度检验，同时报告被转子关系耦合的星号项。静态候选需要平坦 `Q3` 加近似刚性的宇称交错/分支图样；动态候选需要显著宽度、`2ω3` 多声子结构或路径依赖。
4. **三核当前判断。** `144,146Ba` 已有强直接 E3，却只有单条主跃迁，故应写作“强八极集体性/强八极涨落，静态刚性尚不可由该测量独立裁决”。`224Ra` 有更丰富多态 E3/Q3 图样和低位交错宇称带，静态梨形解释更有支持，但仍须保留八极振动、配对和转子耦合的竞争解释。

## Assumptions

- `Q30` 采用 `e fm³` 的常用轴对称电矩约定；不同球谐/无量纲 `β3` 定义需重新换算 `7/(16π)` 因子。
- Wigner–Eckart 约定为 `B(Eλ;Ji→Jf)=|RME|²/(2Ji+1)`；向上和向下 B 值不能混写。
- `I3=ΣB` 只有在相关终态与耦合路径达到 closure 时才可称完整不变量；Ba 的单条 E3 在本页只称有限和项。
- 简谐公式假定正质量 `B3`、正恢复力 `C3` 和基态高斯波函数；非简谐势、双阱隧穿和宇称投影需另行计算。
- `Q2Q3²` 与三阶四极标量的数值归一受张量耦合约定影响；脚本的固定内禀点只作代数控制。

## Competing Explanations

- 大 `B(E3)` 可以来自深静态双阱、浅软势的零点涨落、转动耦合八极声子或组态混合；Cline 与 Gaffney 的限制不允许由单条 E3 选择其中一个。
- 多条 `Q3` 近恒定支持转子图样，但星号耦合、有限态空间和共同模型约束会降低独立性；`228Ra` 的近零链是有用反例，但不自动构成所有核的振动定理。
- E1 强弱受偶极相消控制。`146Ba` 的强 E3/弱 E1 组合反驳“E1 是八极集体性的单调代理”，却不能反向证明其静态或动态本质。
- `224Ra` 的 0+、2+ 候选不能仅因能量接近就称两声子八极态；基带 4+、6+ 已有 ENSDF 带成员归属。

## Transfer Conditions

- 将 Cline 不变量迁移到新核素时，必须取得带符号或相位一致的实验室 RME、初态自旋、E1/E2/E3 feeding、寿命/分支约束和联合协方差。
- 将 `Q3` 迁移为静态 `Q30` 时，需说明 `K=0`、轴对称转子和高阶多极忽略；若存在 γ 软度、三轴性或强带混合，改用完整张量耦合。
- 将 `2ω3` 两声子测试迁移到 `144,146Ba` 时，需先建立 `0+,2+,4+,6+` 候选集及其 E1/E3 分支；当前 Bucher 单条 E3 网络不满足该条件。
- 跨核比较 E1/E3 必须统一单位、初末态方向、`2J_i+1` 简并因子、相位和 feeding；不可把 `B(E3;3−→0+)` 与 `RME(0+→3−)` 直接相除。

## Failure Conditions

- 只用 `B(E3;3−→0+)` 或拟合 `β3` 宣称静态梨形已被无模型证明。
- 把 `⟨Q3⟩=0` 当作“无静态形变”；宇称恢复后的双阱态同样给零实验室一阶矩。
- 把 `⟨Q3⁴⟩−⟨Q3²⟩²` 写成 `Var(Q3)` 而不说明它实际是 `Var(Q3²)`。
- 把有限 E3 部分和当完整 closure，或把 GOSIA 的转子耦合星号项当独立实验矩阵元。
- 把 ENSDF 224Ra 基带 4+、6+ 与未指派的 0+/2+ 合并成两声子 quartet。
- 以 E1/E3 比值设置跨核普适阈值，忽略 `146Ba` 的偶极相消和实验 feeding。

## Falsification or Reverse Tests

1. **静态平坦度反证：** 为同一核取得至少三条未由同一转子约束生成的 E3 路径；若协方差加权后的 `Q3(I_i,I_f)` 随初态/终态显著漂移，静态刚性解释降级为模型条件结果。
2. **四阶宽度反证：** 完成高阶矩阵元网络后计算 `Var(Q3²)`。若显著大于实验协方差传播和刚性模型预期，固定内禀点被否定；若接近零，只说明幅度分布窄，仍需宇称能级/分支确认。
3. **两声子反向检验：** 若发现 `0+,2+,4+,6+` 在 `2E(3−)` 附近成组，且 E3/E1 分支符合同一声子波函数的相对强度，静态解释需让位或与振动混合；若 quartet 缺失或严重非简谐，不能用 harmonic 标签强行解释。
4. **E1 相消控制：** 对 `144Ba→146Ba` 保持 E3 网络不变，显式释放 E1 先验并传播相位/feeding 协方差；若 E1 变化仍不改变 E3 `I3`，则支持算符解耦，若显著改变则说明网络相关性尚未隔离。
5. **等二阶不同四阶构造：** 用脚本把一个固定 `Q30=q0` 分布和一个调节 `B3C3` 的高斯分布设为相同 `⟨Q3²⟩`；它们二阶 E3 标量相同而四阶方差不同，说明单个 E3 不具备分布识别能力。

## Open Questions

- `144,146Ba` 是否存在可独立测量的 `0+,2+,4+,6+` 两声子八极候选？需要寿命、绝对 E1/E3 和 feeding-covariance，而不是只增加相对 γ 强度。
- `224Ra` 的 0+ 916.38 keV、2+ 965.65 keV 及更高 4+/6+ 候选能否在同一反应和同一模型中形成两声子 multiplet？当前 ENSDF 不支持把基带 4+/6+ 直接计入。
- 能否取得 Gaffney/Butler 的完整 GOSIA input、covariance 和未列 E3 高态，从而实作 `I3`, `Q2Q3²` 和四阶 closure，而不是只用表列中心值？
- 对 `146Ba`，在不把 SCCM 的偶极分解冒充实验证据的前提下，能否用共同 E1/E3 response 重新检验相消的模型敏感性？
- 在非简谐双阱中，实验可获得的四阶不变量、宇称劈裂和转动惯量怎样联合约束 `B3,C3` 与隧穿劈裂？

## Human Review

当前没有用户逐 claim 审核。本页保持 `review_status: unreviewed`，所有 `needs_review` 事实仍须在后续论文写作或正式引用时回到 source/raw 原件。优先人工核验：

- Cline PDF p.698 的张量耦合归一和 p.699 图示宽度公式字面差异；
- 224Ra 多态 E3 表、方向简并和 GOSIA 星号耦合项；
- Bucher 144/146Ba 的完整输入网络、E1 先验和协方差；
- 两声子候选能级的 ENSDF 版本与实验谱系。

## Promotion or Rejection History

- `2026-10-29 / created / provisional`: 创建研究笔记，基于 Cline 1986、GOSIA 2012、Bucher 2016/2017、Gaffney 2013、Butler 2020 和 ENSDF 224Ra 的现有 source 页/原件定位。
- 尚未晋升为 project/synthesis；没有 human-reviewed 事件，也没有 rejected/superseded 事件。

## Reproducibility Record

- Script: [cline_octupole_invariants.py](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-cline-invariants/cline_octupole_invariants.py)
- Results: [cline_octupole_invariants_results.json](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-cline-invariants/cline_octupole_invariants_results.json) and [cline_octupole_invariants.csv](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/octupole-cline-invariants/cline_octupole_invariants.csv)
- Command: `python3 cline_octupole_invariants.py --out-dir .`
- Run result: JSON parses successfully; central-value controls reproduce `I3(144Ba)=4.225×10^5 e²fm⁶`, `I3(224Ra)=8.836×10^5 e²fm⁶`; all values are finite-sum/rotor-convention controls, not new measurements.
