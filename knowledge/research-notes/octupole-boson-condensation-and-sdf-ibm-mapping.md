---
type: research-note
title: "八极玻色子凝聚、sdf-IBM 代数映射与反射不对称相变"
date: 2026-10-29
created: 2026-10-29
updated: 2026-10-29
category: research-notes
aliases: [octupole boson condensation, sdf-IBM octupole mapping, finite-N octupole phase transition]
tags: [octupole, ibm, sdf-ibm, boson-condensation, phase-transition]
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
created_from: "Day26 directed study: octupole boson condensation and sdf-IBM algebraic mapping"
evidence_sources: [butler-nazarewicz-1996-intrinsic-reflection-asymmetry, bucher-2016-144ba-direct-octupole, nomura-2018-odd-ba-octupole]
---

# 八极玻色子凝聚、sdf-IBM 代数映射与反射不对称相变

## Research Trigger

本轮把八极集体性从微观反射不对称平均场与实验 `B(E3)` 连接到一个可复现的
`sdf-IBM` 代数基准。目标有四项：建立包含 `s(L=0,+)、d(L=2,+)、f(L=3,-)` 的
宇称守恒哈密顿量；从相干凝聚态得到 `E(beta2,beta3)`；给出 `E2/E3` 在转子极限和
有限玻色子数下的代数标度；用 `144,146Ba` 与 `148Ce` 的数据可得性检查有限 `N`
效应的解释边界。

可复现工件位于
`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/sdf-ibm-octupole/`。

## Grounded Evidence

### 来源事实

| ID | 事实 | 证据性质 | 定位 |
| --- | --- | --- | --- |
| BN96-1 | 反射不对称应同时检查交替宇称能级、E1/E3、内禀矩和模型；静态极小、八极软振动和宇称恢复不能合并。 | 综述框架 | [[butler-nazarewicz-1996-intrinsic-reflection-asymmetry]]，PDF Secs. II–VII |
| BN96-2 | 费米面附近相反宇称、`Delta l=Delta j=3` 轨道对是八极不稳定性的常见微观驱动；E1 对质子—中子相消敏感，E3 更接近八极集体坐标。 | 综述机制 | Butler–Nazarewicz 1996，PDF Sec. III.A、II.B、IV.C–D |
| BU16-1 | `144Ba` 垒下库仑激发给出 `M(E3;0+↔3−)=0.65(+0.17/-0.23) eb^(3/2)`，即向下 `B(E3;3−→0+)=48(+25/-34) W.u.`。 | 直接实验 | [[bucher-2016-144ba-direct-octupole]]，PDF pp. 3–4、Table I |
| BU16-2 | `144Ba` 转子约定下 `Q3=1.73(+0.45/-0.62)×10^3 efm^3`、`beta3=0.17(+0.04/-0.06)`；该形状换算含转子和高阶多极假设。 | 实验加模型换算 | Bucher 2016，PDF p. 4 |
| NO18-1 | DD-PC1 约束 RHB 势能面被映射到 `sdf`-IBM/IBFM；`144,146Ba` 偶偶芯的 `beta3` 非零极小沿八极方向较软。 | 微观模型方法 | [[nomura-2018-odd-ba-octupole]]，PDF pp. 2–5、Sec. II、Fig. 1 |
| NO18-2 | 奇 Ba 的低能态可主要是 `sd` 芯加奇中子，高激发态才出现明显 `f` 玻色子成分；预测的奇核 `B(E3)` 是模型输出。 | 模型结果 | Nomura 2018，PDF pp. 6–10、Tables V–IX |
| EXT146-1 | `146Ba` 直接库仑激发给出 `B(E3;3−→0+)=48(+21/-29) W.u.`，与 `144Ba` 中心值相同；其 E1 抑制被作者联系到中子轨道占据和偶极相消。 | 直接实验加模型解释 | [[bucher-2017-146ba-direct-octupole]]，PDF pp. 2–5、Table I、Figs. 3–5 |
| ENSDF148-1 | NNDC ENSDF 2026-01 adopted levels 给出 `148Ce` 的 `3−` 候选 `841.41(5) keV`，但评价页没有 `B(E3)` 字段。 | 评价数据可得性检查 | `https://www.nndc.bnl.gov/ensdf/getadopted.jsp?nuc=148CE`，Adopted Levels, p. 1 |

`144Ba` 与 `146Ba` 的直接 E3 中心值相同，并不等于它们的误差独立或势能面完全相同；
两次实验有相似的 GOSIA/粒子—伽马响应链。`148Ce` 的高自旋八极带和 `3−` 能级证据
不能填补缺失的绝对 `B(E3)`。

### 代数空间和哈密顿量

玻色子产生算符满足
`s†: L=0,+`、`d†_mu: L=2,+`、`f†_mu: L=3,-`，总数
`N=n_s+n_d+n_f` 固定。定义 `tilde b_{Lmu}=(-1)^mu b_{L,-mu}`，则一个最小的
旋转标量、宇称守恒哈密顿量为

\[
 H=\epsilon_d\hat n_d+\epsilon_f\hat n_f
 -\kappa_2 Q_2\cdot Q_2-\kappa_3 Q_3\cdot Q_3
 +\kappa_L L\cdot L+H_{3\text{-body}}.
\]

本轮工件暂不启用 `H_{3-body}`，以隔离有限 `N` 和八极二体作用。算符采用

\[
 Q_{2\mu}=s^\dagger\tilde d_\mu+d^\dagger_\mu\tilde s
 +\chi_d[d^\dagger\times\tilde d]^{(2)}_\mu
 +\chi_f[f^\dagger\times\tilde f]^{(2)}_\mu,
\]

\[
 Q_{3\mu}=s^\dagger\tilde f_\mu+f^\dagger_\mu\tilde s
 +\chi_{df}\{[d^\dagger\times\tilde f]^{(3)}_\mu
 +[f^\dagger\times\tilde d]^{(3)}_\mu\}.
\]

`Q2` 宇称偶、`Q3` 宇称奇，但 `Q3·Q3` 宇称偶；点积定义为
`A_lambda·B_lambda = sum_mu (-1)^mu A_{lambda,mu} B_{lambda,-mu}`，所以每一项
均为旋转标量。`H_{3-body}` 可用于调节有限 `N` 的相变阶数或三体反射不对称项，加入时
必须保持总宇称偶。

## Provisional Reasoning

### 相干态和势能面

取轴对称、`K=0` 凝聚态

\[
 |N;\beta_2,\beta_3\rangle={1\over\sqrt{N!}}
 (b_c^\dagger)^N|0\rangle,
 \quad b_c^\dagger={s^\dagger+\beta_2d_0^\dagger+\beta_3f_0^\dagger
 \over\sqrt{D}},\quad D=1+\beta_2^2+eta_3^2.
\]

直接得到
`<n_d>=N beta2^2/D`、`<n_f>=N beta3^2/D`。令单玻色子态
`|alpha>=(|s>+beta2|d0>+beta3|f0>)/sqrt(D)`，对任意一体张量 `q_lambda`，有

\[
 \langle Q_\lambda\cdot Q_\lambda\rangle_N
 =N(N-1)\,\bar q_\lambda\cdot\bar q_\lambda
 +N\langle\alpha|q_\lambda\cdot q_\lambda|\alpha\rangle,
 \quad \bar q_{\lambda\mu}=\langle\alpha|q_{\lambda\mu}|\alpha\rangle .
\]

因此

\[
 E_N(\beta_2,\beta_3)=\epsilon_d{N\beta_2^2\over D}
 +\epsilon_f{N\beta_3^2\over D}
 -\kappa_2[N(N-1)\bar q_2^2+Nr_2]
 -\kappa_3[N(N-1)\bar q_3^2+Nr_3]+E_L,
\]

其中 `r_lambda=<alpha|q_lambda·q_lambda|alpha>` 是有限数自身项。由于 `Q3` 为宇称奇，
在真实参数下 `E_N(beta2,beta3)=E_N(beta2,-beta3)`；非零极小必成 `+/- beta3`
简并对。`kappa3` 增大时，若其负的八极关联能超过 `epsilon_f` 和四极竞争项，原点
沿 `beta3` 方向失稳，出现八极序参量分岔。这是有限 `N` 的能量面分岔，不自动等同于
热力学极限中的严格二阶相变。

### `B(E2)` 和 `B(E3)`

在轴对称强耦合转子约定下，定义 `Q_lambda,0=N qbar_lambda,0`，则

\[
 B(E2;2^+\to0^+)={5\over16\pi}Q_{20}^2,
 \qquad
 B(E3;3^-\to0^+)={7\over16\pi}Q_{30}^2.
\]

若只保留 `s†tilde d+d†tilde s` 与 `s†tilde f+f†tilde s`，则
`qbar_20≈2 beta2/D`、`qbar_30≈2 beta3/D`，因而

\[
 B(E2)\approx {5\over4\pi}{N^2\beta_2^2\over D^2},\qquad
 B(E3)\approx {7\over4\pi}{N^2\beta_3^2\over D^2},
\]

再乘以相应有效玻色子电荷平方和角动量约化系数。`chi` 项会把 `beta2 beta3` 的
交叉项加到 `qbar_lambda`，脚本不采用上述简化，而是用球张量 CG 系数直接计算。

有限数有两个不可混淆的层次：

1. 对能量面中的 `Q·Q`，两体项相对经典 `N²` 项缺少一个 `1/N`，两体近似因子是
   `(N-1)/N`。采用 50/82 核芯和粒子对计数时，`N_B(144Ba,146Ba,148Ce)=(6,7,8)`，
   该因子分别为 `0.8333, 0.8571, 0.8750`。
2. 对一个 `f` 声子向 `s/d` 凝聚背景的衰变，约化振幅由玻色子湮灭给出 `sqrt(N)`，
   因而 `B(E3)` 的 leading 标度是 `N`。把这个 one-phonon 矩阵元直接当作内禀转子
   `N²` 强度会人为夸大大 `N` 饱和。

这两种表达分别对应“凝聚能量/内禀矩”和“单声子跃迁”，应在比较 `B(E3)` 时说明采用
哪种态构造。实验的 `B(E3)` 还包含角动量投影、有效电荷、态混合和 GOSIA 协方差，
不能只用 `N` 比例重拟合。

### 工件结果

`order_parameter_scan.csv` 的示意参数 `N=7` 显示：`kappa3=0` 时最低点在
`beta3=0`；扫描到约 `kappa3≈0.07–0.08` 后最低点移到 `|beta3|>0`，并保持
宇称相关的 `+/-` 简并。临界位置只属于该组 `epsilon, kappa, chi`，不是实验临界常数。
`transition_scaling.csv` 同时给出 `N²` 转子量、有限 `Q·Q` 修正和 `N` one-phonon
标度，避免把不同的“饱和”定义混在一起。

## Assumptions

- 使用 IBM-1，质子和中子成对自由度合并；`N` 取相对于 `Z=50,N=82` 芯的价核子对数。
- 只保留轴对称 `d_0,f_0` 相干幅度；没有显式 `gamma`、非轴向八极分量或三轴投影。
- `epsilon_d, epsilon_f, kappa2, kappa3, chi_d, chi_f, chi_df` 是示意参数，不是某一核的
  微观 EDF 拟合。
- `B(E2/E3)` 公式是强耦合转子约定；完整 IBM 角动量投影会改变低 `N` 的数值。
- `148Ce` 仅有 `3−` 能级可核对；由于评价页没有绝对 `B(E3)`，不得填入外推值。
- 所有来源和本页状态为 `unreviewed/ai-draft/provisional`。

## Competing Explanations

1. 有限 `N` 代数分岔可能只是软势面和零点涨落的重排，未必是静态梨形的自发破缺。
2. 大 `B(E3)` 可来自动态八极声子、组态混合或浅双阱；Butler–Nazarewicz 的静态/软/振动
   分层不允许由一条 E3 单独裁决。
3. `146Ba` 的小 E1 可由中子轨道占据导致的质子—中子偶极相消产生，不能反推出 E3 被削弱。
4. 奇核 `sdf-IBFM` 中的阻塞和高激发 `f` 成分具有态依赖性，不能把偶偶芯的 `B(E3)`
   直接迁移到奇核基态。
5. `148Ce` 的交替宇称带或高自旋结构若缺少绝对寿命，可能是谱学关联证据而非直接 E3 证据。

## Transfer Conditions

- 要把相干态 `beta3` 与实验 `B(E3)` 比较，必须固定同一有效电荷、`N` 计数、初末态方向、
  `2J_i+1` 简并因子和角动量投影约定。
- 要把 DD-PC1/Gogny 势能面映射到本模型，需在同一 `beta2,beta3` 坐标、配对方案、零点能
  和投影约定下匹配势能差，而不是只匹配一个极小点。
- 可迁移的有限 `N` 结论是 `(N-1)/N` 的代数修正与 one-phonon `N` 标度；不可迁移的是
  本脚本的临界 `kappa3`、绝对 `beta3` 和 `148Ce` 的缺失 `B(E3)`。

## Failure Conditions

- `N` 太小或 `beta3` 网格过粗时，双极小可能被网格误判为单极小；需收窄步长并检查正负
  `beta3` 的能量差。
- 大 `chi` 或加入三体项后，简单 `N²` 标度不再适用；必须重新计算一体和多体矩阵元。
- 忽略角动量投影就把 `Q30` 当实验约化矩阵元，会混淆内禀矩、RME 和 `B(E3)`。
- 将 ENSDF `3−` 能级、理论 `B(E3)` 或邻近核数据填入 `148Ce` 会越过证据边界。
- 脚本未实现真实 EDF/GCM、波函数宇称投影和 E1/E3 协方差，不能用于论文级参数提取。

## Falsification or Reverse Tests

- 将 `N=6,7,8` 的相同 `beta3` 输入改为完整角动量投影态；若 `B(E3)` 不显示 one-phonon
  `N` 标度，则说明当前“声子—凝聚背景”近似不适用。
- 对 `beta3` 正负两侧逐点加密；若 `E(+beta3)-E(-beta3)` 超过机器误差，检查 Q3 算符
  的 tilde 相位和宇称守恒。
- 令 `kappa3=0`、`chi_df=0`、`beta3=0`；能量面应退化为反射对称 `sd`-IBM，且
  `B(E3)` 凝聚内禀项为零。
- 逐步增大 `N` 并比较临界曲率、`(N-1)/N` 和最低态宇称；若临界点不趋于稳定，说明
  有限数相变不能解释成热力学序参量。
- 对 `144Ba/146Ba` 采用完整 GOSIA 协方差而非中心值；若两核 E3 差异超出当前区间，
  应撤回“相同八极集体性”的强表述。

## Open Questions

- `148Ce` 是否已有可定位的绝对 `B(E3;3−→0+)` 测量？需要取得原始库仑激发/寿命论文，
  不能由 2026 ENSDF 能级页补齐。
- 在同一 GCM/EDF 势能面上，有限 `N` 的 sdf-IBM 映射能否同时再现 `B(E3)`、E1 相消和
  `beta3` 曲率，而不把 `chi` 当逐核自由拟合量？
- `N=6–8` 的玻色子数修正是否主要来自 `Q·Q` 自身项，还是来自显式三体八极相互作用和
  角动量投影？
- `144,146Ba` 的直接 E3 与 `148Ce` 的高自旋八极带能否在同一态标签和寿命网络下比较？
- 对奇 Ba，Nomura 的 `f` 玻色子占据与实验 E3 是否能用阻塞前后同一 EDF 的响应差分验证？

## Human Review

- `HR-1`：核对 `148Ce` 的原始绝对 E3 来源；目前仅确认 ENSDF 缺少字段，状态为 `needs_review`。
- `HR-2`：审查 `sdf-IBM` 的有效电荷、IBM-1/IBM-2 计数以及实验 `B(E3)` 的方向约定。
- `HR-3`：审查示意 `kappa3` 分岔是否适合使用“相变”措辞，或应改为有限系统的能量面分岔。
- 本页未标记 `human-reviewed`；来源页的 self-audit 也不等价于人工审核。

## Promotion or Rejection History

- `2026-10-29 / created / provisional`：建立本研究笔记和最小 sdf-IBM 数值工件；写入直接 E3、
  微观 sdf-IBM 映射和 `148Ce` 数据缺口。
- `2026-10-29 / self-audit / provisional`：检查旋转标量、宇称偶性、`N(N-1)+N` 有限数
  恒等式、`beta3 -> -beta3` 对称和 CSV/JSON 输出；未升级为已证实相变或静态梨形结论。
