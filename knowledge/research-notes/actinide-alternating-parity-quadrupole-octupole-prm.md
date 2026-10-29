---
type: research-note
title: "锕系偶偶核交替宇称能带的四极—八极粒子—转子模型"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [actinide alternating-parity quadrupole-octupole PRM, quadrupole-octupole particle-rotor model, Ra-Th parity bands]
tags: [actinides, alternating-parity-bands, octupole-deformation, particle-rotor-model, radium-thorium]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 directed study: quadrupole-octupole particle-rotor model for actinide alternating-parity bands"
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, gaffney-2013-pear-shaped-rn-ra, bucher-2016-144ba-direct-octupole]
---

# 锕系偶偶核交替宇称能带的四极—八极粒子—转子模型

## Research Trigger

本任务考察轻锕系偶偶核 `220,222,224,226,228Ra` 与
`222,224,226,228,230Th` 的正负宇称转动序列、单纯形对称性、离心八极稳定化和
`B(E1)/B(E2)` 反演。目标是把“随自旋升高，正负宇称能量交错位移趋近于零”压缩成
一个可复现的四极—八极粒子—转子（PRM）最小模型，同时保持实验事实、作者解释、模型
输出和本任务推断四层分开。

交错位移定义为

\[
 \Delta E(I)=E(I^-)-\frac{1}{2}[E((I+1)^+)+E((I-1)^+)] .
\]

对偶偶 `K=0` 交替宇称带，偶数 `I` 的正宇称态和奇数 `I` 的负宇称态组成一条
`s=+1` 单纯形（simplex）序列。单纯形是 `P R_x(\pi)` 的复合离散对称标签；它把
宇称和半转动联系起来，但并不等同于“已经证明了静态梨形”。若 `beta_3` 是软坐标，
宇称投影后的最低正、负态可以仍有较大能隙；若双阱作用量增大，隧穿劈裂会快速变小。

## Grounded Evidence

### 1. 实验谱学和证据层

仓库现有来源和评价数据支持以下量级：

| 对象 | 直接或评价输入 | 证据性质 |
| --- | --- | --- |
| `224Ra` | `Delta E(1-)` 约 `173.8 keV`，高自旋示例约 `20.2 keV` | Gaffney 2013 及现有位移审计；实验能级和带配对需沿原件复核 |
| `226Th` | `Delta E(1-)` 约 `194.3 keV`，高自旋评价示例约 `0.8 keV` | ENSDF 评价能级；负宇称带寿命缺失，不能单独给绝对 `B(E1)` |
| `222Ra` | 多条 E3 矩阵元的转子模型 `Q3` 约 `3120(190) e fm^3` | Butler 2020，Coulomb-excitation/GOSIA；作者解释支持稳定梨形，但保留声子替代解释 |
| `228Ra` | `0+ -> 3-` 聚合 `Q3` 约 `2230(290) e fm^3`，部分 E3 链接接近零 | Butler 2020；作者将其与八极振动相容 |
| `144Ba` | `B(E3;3- -> 0+) = 48^{+25}_{-34} W.u.` | Bucher 2016 直接库仑激发；是强八极集体性而非单独静态形变证明 |

`Butler & Nazarewicz 1996` 的综述给出交替宇称带、E1/E3、宇称恢复和高自旋
Routhian 的统一历史框架，并强调 E1 对质子—中子位移和相消很敏感，E3 更接近八极
集体坐标。`Gaffney et al. 2013` 的放射性束库仑激发将 `220Rn` 与 `224Ra` 的
`Q2/Q3` 和能级位移放在同一实验链上。`Bucher et al. 2016` 的 `144Ba` 结果说明
单条大 E3 足以确立强集体性，却不足以区分静态极小、软双阱和振动波函数。

对用户要求的九个核素，完整交替序列的逐线核验尚未在本轮全部闭合。`220–228Ra` 和
`222–230Th` 的“每个自旋都完整”的表述应在使用前回到对应 ENSDF/原始能级图逐带确认；
本笔记只把 `224Ra` 与 `226Th` 的位移量作为有现有 locator 的锚点，其余核素在工件中
作为参数化系统学对象。

### 2. 微观八极驱动和粒子—转子结构

反射不对称的单粒子驱动通常来自费米面附近异宇称轨道对，尤其是
`Delta l = Delta j = 3` 的耦合。例如锕系区常讨论 `pi f7/2 <-> i13/2` 与
`nu g9/2 <-> j15/2`。在微扰语言中，八极场 `q_3 F_3` 使占据—空轨道产生二阶能移；
真正的响应还受能量分母、占据概率、配对相干因子、四极形变和阻塞影响。因此不能由
轨道名称直接推出一个普适 `beta_3` 或势垒。

`224Ra` 的放射性束库仑激发给出强 `Q3` 和较平坦的多跃迁图样，这是支持静态样八极
关联的直接证据。`222Ra` 的多 E3 图样与 `228Ra` 的近零链接则提醒：稳定梨形与八极
振动是可以由多跃迁图样区分的工作假设，但配对、对齐八极声子和 GOSIA 中的耦合矩阵元
仍是竞争解释。`B(E3)`、`Q3`、能级位移和 E1 必须联合使用。

### 3. 来源和独立性

- `butler-nazarewicz-1996-intrinsic-reflection-asymmetry`：综述与理论谱系，不能当作
  1996 年以后实验的独立重复测量。
- `gaffney-2013-pear-shaped-rn-ra`：`220Rn/224Ra` 的放射性束库仑激发；矩阵元来自
  GOSIA 和输入寿命/分支，`Q3` 到形状的转换有转子约定。
- `bucher-2016-144ba-direct-octupole`：`144Ba` 的直接 E3；E1/E3 相对符号、高阶
  多极和 `beta_3` 转换仍有边界。
- `butler-2020-222-228ra-octupole-evolution`：`222/228Ra` 多跃迁 E3 系统学；星号
  链接由转子关系耦合，不能算完全独立观测。
- `octupole-centrifugal-stabilization-and-energy-displacement`：已有离心稳定化和
  位移模型工件；本页进一步使用显式有限差分宇称投影。

## Provisional Reasoning

### 1. 四极—八极内禀哈密顿量

先把 `beta_2` 固定在一条有效四极形变路径上，把八极坐标写为
`q = beta_3`。轴对称、`K=0` 的最小 PRM 哈密顿量为

\[
 H_I(q) = -\frac{\hbar^2}{2B_{33}(q)}\frac{d^2}{dq^2}
 + V(q) + \frac{\hbar^2}{2\mathcal J(q)}[I(I+1)-K^2],
 \qquad K=0 .
\]

若只讨论内禀极小而暂时忽略 `q` 的集体动能，就得到题目给出的

\[
 H_{\rm intr,rot}=\frac{\hbar^2}{2\mathcal J(\beta_2,\beta_3)}[I(I+1)-K^2]+V(\beta_2,\beta_3).
\]

数值工件采用对称四次势

\[
 V(q)=V_b\left(q^2/q_0^2-1\right)^2,
 \qquad \mathcal J(q)=\mathcal J_0(1+c_3q^2),
\]

在 `[-0.42,0.42]` 的均匀网格上用中心差分对角化。最低偶、奇波函数由
`q -> -q` 的宇称期望值分类，再对各 `I` 计算转动能和 `Delta E(I)`。该求解保留了
宇称投影的基本结构，但不是自洽 EDF、GCM 或完整粒子—转子组态空间。

### 2. 离心拉伸的微商和势垒

令 `x=beta_3^2`，

\[
 V_{\rm eff}(x;I)=V_0(x)+\frac{\hbar^2 I(I+1)}{2\mathcal J(x)}.
\]

则

\[
 \frac{\partial V_{\rm eff}}{\partial x}
 =\frac{\partial V_0}{\partial x}
 -\frac{\hbar^2 I(I+1)}{2\mathcal J(x)^2}
   \frac{\partial\mathcal J}{\partial x}.
\]

若 `dJ/dx > 0`，旋转项的导数严格为负：增大八极幅度提高惯量并降低转动能。
真正的极小点仍须满足总导数为零；“`dV_eff/d(beta_3^2)<0`”只在裸势斜率尚未抵消
离心项的区域成立，不能对所有 `x` 无条件宣称。

在 `x=0` 附近用 `V_0 = k_2 x + k_4x^2`，原点失稳的示意分岔条件是

\[
 k_2-\frac{\hbar^2 I(I+1)}{2\mathcal J_0}c_3=0.
\]

对已经存在八极双阱的 Ra/Th，转动主要把有限 `q_0` 极小相对于中心区降低并增大有效
中心势垒；对软势，转动可以把极小从 `q=0` 推向有限 `q`。当双阱作用量

\[
 \frac{S_I}{\hbar}=\frac{1}{\hbar}\int dq\sqrt{2B_{33}(q)[V_{\rm eff}(q;I)-E_0(I)]}
\]

增大时，最低宇称劈裂的半经典尺度约为
`Delta E ~ (hbar omega/pi) exp(-S_I/hbar)`。因此高自旋位移趋零的物理图像是
“八极坐标增加带来的惯量收益”与“宇称隧穿被加深势垒压制”共同作用，而非一个只由
`V_b` 决定的定理。

### 3. 单纯形与交替宇称能带

轴对称 `K=0` 内禀态在 `P R_x(pi)` 下可分类为 `s=+1` 或 `s=-1`。对偶偶核，
常见 `s=+1` 序列可写为 `0^+,1^-,2^+,3^-,...`。当 `q` 的双阱波函数局域在
`+q_0` 和 `-q_0` 两侧时，宇称投影态是左右内禀态的对称/反对称组合；其能量差会在
自旋升高、势垒有效加深时减小。若对齐准粒子发生带交叉，`s` 标签仍可有定义，但
相同的一条集体带可能不再连续，必须重新检查带身份。

### 4. E1/E2 分支和 `D0` 反演

对同一转动模型的 `K=0` 退激支，采用

\[
 B(E1;I\to I-1)=\frac{3}{4\pi}D_0^2 C_1^2,
 \quad
 B(E2;I\to I-2)=\frac{5}{16\pi}Q_0^2 C_2^2,
\]

其中 `C_1^2=I/(2I+1)`，`C_2^2=3I(I-1)/[2(2I-1)(2I+1)]`。若强度已统一为
`e^2 fm^2` 与 `e^2 fm^4`，则

\[
 |D_0|=Q_0\sqrt{\frac{B(E1)}{B(E2)}\frac{5}{12}\frac{C_2^2}{C_1^2}}.
\]

若输入是 W.u. 比值，必须先分别换算 E1 和 E2 的单粒子单位；未经换算的 W.u. 商不能
直接代入该式。工件同时输出 `B(E1)`、`B(E2)`、物理单位比值和反演 `D0`，并把输入
的 `D0` 状态写入 JSON。

题目给出的 `224Ra |D0|≈0.15 e fm` 与 `226Ra |D0|≈0.05 e fm` 被作为用户指定的
敏感性目标。现有 Wiki 审计曾记录 `224Ra |D0|≈0.03 e fm` 的另一数值；本轮没有取得
可逐字段对账的原始 E1 寿命/分支表，因此不能选择其中一个作为已核验事实。工件在
`results.json` 中保留这项冲突，避免把模型输入升级为实验结论。

微观上可写 `D_0 = D_p + D_n + D_shape`。费米面附近中子侵入轨道的占据改变
`D_n` 和质子—中子反向极化；当总和穿过零点时，`B(E1)` 对很小的占据变化呈二次
敏感，而 `B(E3)` 仍可保持大。已有 `144/146Ba` SCCM/库仑激发审计显示，
`nu h9/2`、`nu f7/2`、`nu i13/2` 占据改变可使质子偶极贡献近乎抵消；这一机制可以
作为 Ra/Th 的可检验迁移假设，但不能把 Ba 的占据数字直接复制到锕系。

## Assumptions

- `beta_2` 被吸收到 `J_0`、`Q_0` 和势参数；没有显式求解 `beta_2-beta_3` 二维耦合。
- `B_33`、`V_b`、`q_0`、`c_3` 和示意 `D_0` 是现象学输入，不是自洽 EDF 输出。
- `K=0`、轴对称、时间反演偶势和 `V(q)=V(-q)` 适用于最低模型；三轴、奇形变、
  time-odd 场和准粒子阻塞未纳入。
- 最低偶/奇有限差分本征态被当作每个自旋的有效带成员；实际带交叉时该映射可能失效。
- `D0` 反演要求同一初态/一致分支定义、可靠多极性和单位转换；ENSDF 中没有寿命的
  负宇称带不能被工件补成绝对强度。
- 页面状态保持 `ai-draft/unreviewed/provisional`；来源页中的 self-audit 不是
  `human-reviewed`。

## Competing Explanations

1. **离心稳定化**：`J(beta_3)` 随八极幅度增加，转动能使有限 `beta_3` 区域下降，
   作用量增加后 `Delta E` 收敛。
2. **八极振动或软双阱**：强 E3 和有限平均场极小可以来自零点涨落；波函数未局域化
   时不能使用静态梨形措辞。
3. **对齐和组态交叉**：高 `j` 质子/中子对齐可使八极相关增强，也可在更高自旋恢复
   反射对称；这会产生非单调位移。
4. **带混合和重新标记**：`Delta E(I)` 的骤变可能来自不同 `K` 带或组态相交，而非
   同一双阱中隧穿劈裂的变化。
5. **配对和坐标依赖惯性**：配对坍塌改变 `B_33` 和 `J`，会改变相同势垒下的劈裂；
   只比较势垒深度不够。
6. **偶极相消**：E1 低强度可能源于 `D_p+D_n≈0`，不能否定强八极集体性；E1 大小
   也不能单独证明静态形变。

## Transfer Conditions

- 把 `224Ra` 的位移趋势迁移到其它 Ra/Th，必须使用同一带配对、同一自旋范围、
  同一 `E1/E2` 单位和同一 `J(beta_3)` 定义。
- 把 `Ba` 的中子占据相消机制迁移到锕系，至少需要同一 EDF/基底的质子与中子过渡
  密度、占据概率、配对和四极形变；不能只迁移轨道名称。
- 将 `Q3` 转成 `beta_3` 时需保留转子几何、`beta_2`、高阶形变和相对矩阵元符号；
  直接 E3 证据不能替代完整二维投影计算。
- 将 `Delta E` 解释为隧穿劈裂，需要确认负宇称带确是同一 `K=0` 结构，并检查
  alignment、band crossing、零点能和 `B_33`。
- 由 `B(E1)/B(E2)` 反演 `D0` 只能约束所采用转子算符的有效矩；缺寿命时仅能报告
  相对分支或上/下限。

## Failure Conditions

- 若约束计算得到 `dJ/d(beta_3^2)<0`，离心外移机制的方向反转。
- 若有限差分结果对网格、盒边界或 `B_33` 强烈不收敛，则不能使用其绝对劈裂。
- 若 `Delta E` 的高自旋收敛只在带交叉后出现，单一双阱模型不能承担归因。
- 若 `226Th` 的负宇称评价带重标号或自旋指派改变，当前 `226Th` 锚点只保留为历史
  评价基线。
- 若 E1/E2 分支混有未识别的多极性、内转换或不同母态，`D0` 反演不成立。
- 若后续原始来源支持 `224Ra |D0|≈0.15 e fm`，应撤回本页对 `0.03 e fm` 的冲突警示；
  在此之前不得把用户数字写成 settled fact。

## Falsification or Reverse Tests

1. 用同一 Gogny-D1S/D1M 或 covariant EDF 约束 `beta_2,beta_3`，在 `I=0` 到高自旋
   计算 `J(beta_3)`、配对和二维势能面，直接检查微商符号。
2. 对每个 `I` 做二维集体 Schrödinger 或 parity-projected GCM，比较投影 `Delta E(I)`
   与一维 PRM；若趋势反转，说明惯性和四极耦合不能忽略。
3. 逐线重建 `220–228Ra` 与 `222–230Th` 的正负宇称带，标记带交叉、未观测成员和
   不确定的 `J^pi`，再计算同一公式的位移。
4. 在 `226Th` 和 `226Ra` 获得负宇称带寿命，联合 `B(E1),B(E2),B(E3)`、`Q_t` 和
   `D0`，检查 E1 相消是否与位移收敛共存。
5. 用中子占据扫描 `D_p+D_n` 的过零点，比较 `B(E1)` 的二次灵敏度与 `B(E3)` 的
   稳定性；要求保留过渡密度相位和协方差。
6. 复现工件：
   `python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/actinide-parity-prm/quad_oct_prm.py`
   并检查 `results.json` 中的 `empirical_anchors`、`D0_status` 与 CSV 的来源标签。

## Open Questions

- `220,222,224,226,228Ra` 与 `222,224,226,228,230Th` 是否都能在同一评价版本中闭合
  到连续的 `0+,1-,2+,3-...` 带？需要逐线原件和依赖关系审计。
- `224Ra` 用户给定的 `0.15 e fm` 是否来自某个特定 E1/E2 分支、方向约定或 W.u. 换算？
  现有审计的约 `0.03 e fm` 与其冲突，必须找到 primary locator。
- `226Ra` 的 `0.05 e fm` 是否是同一转子约定下的量，还是模型/评价值？
- `226Th` 的高自旋 `Delta E` 接近零是否由深双阱、较小 `B_33`、带重标记或评价
  不确定度主导？
- 在同一 projected-GCM 中，`beta_2-beta_3` 耦合是否能把 E2、E3、E1 和位移四类量
  同时复现？
- 何种最低多跃迁 E3 完备度能排除“旋转对齐八极声子”对静态梨形的替代解释？

## Human Review

本页是 Codex self-audit 的 `ai-draft`，尚未人工审核。已使用的来源页均保留各自的
`review_status` 和 locator；本页没有把来源综述、ENSDF 评价、模型输出或用户给定 D0
目标升级为 `human-reviewed`。后续论文或正式报告使用前，应优先人工复核：

- `224Ra/226Th` 位移的逐线能级和带标签；
- `224Ra` 与 `226Ra` 的 E1/E2 原始分支、寿命、内转换和 W.u. 单位；
- Butler/Gaffney/Bucher 中 GOSIA 的耦合参数、星号矩阵元和高阶多极边界；
- 工件中所有示意势垒、惯性、WKB surrogate 和 D0 输入的非实验身份。

## Promotion or Rejection History

2026-10-29：建立研究笔记和 `actinide-parity-prm` 可复现工件。接受“`dJ/d(beta_3^2)>0`
时旋转项对八极坐标的负微商”这一条件性推导，接受 `224Ra` 和 `226Th` 的位移量作为
现有来源锚点；拒绝把单纯形标签、单条大 E3、示意势垒或 WKB surrogate 单独升级为
静态梨形的排他证据。将 `224Ra |D0|≈0.15 e fm` 与现有约 `0.03 e fm` 记录为待核对
冲突，将 `226Ra |D0|≈0.05 e fm` 记录为未核验用户目标。页面保持
`status: ai-draft`, `review_status: unreviewed`, `reasoning_status: provisional`。
