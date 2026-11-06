---
type: research-note
title: "固定形状未配对粒子—转子：四极受限 proxy 的独立模型反例"
aliases: [fixed-shape particle-rotor quadrupole proxy control, 固定几何四极通道反例]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [nomura-2017-odd-mass-gamma-soft-shape-transitions, book-bohr-mottelson-nuclear-structure-vol2, book-greiner-nuclear-models]
created_from: "project; authorized bounded exact-unpaired rigid-core control and subsequent knowledge writeback"
promotion_target:
tags: [a130, particle-rotor, quadrupole-invariants, rigid-core, angular-momentum, model-control]
---

# 固定形状粒子—转子中的四极受限量

## Research Trigger

**独立未配对模型中，严格固定内禀电荷形状和惯量，仍可使 \(J+2\) 受限
proxy 大幅变化并越出反余弦的实数域。** 本页保存这一已完成的数学模型反例。
它补充 [[odd-ba-quadrupole-closure-and-spin-channel-redistribution]] 的解释边界：
IBFM 中近乎恒定的 \(q_2\) 本身不能证明几何不变，而本控制通过预先固定电荷
张量并证明算符恒等式，确实保证了本模型的几何不变。

这里的逻辑是“受限 proxy 变化不充分推出形状变化”；**不能据此证明实际
IBFM 波函数的几何不变**，不能把该反例的耦合强度、惯量或角度赋给实际 Ba
核素，也不声称新定理或复现原作者的电磁图件。

## Grounded Evidence

本次知识回写只复用既有 source 定位和已经冻结的计算，没有新增计算、文献
检索或原书回读。文献背景与本任务数值结果分开归属：

| 来源 | 精确 locator | 本页使用范围 |
|---|---|---|
| [[nomura-2017-odd-mass-gamma-soft-shape-transitions]] | 所持 arXiv v2，PDF p.11，Eqs.(12)–(15)；source 页“2026-11-06 原式、输入与重放补核” | \(J'=J+2\)、最低五态和三次和取绝对值的受限定义。本文反例是独立模型计算，不是该文报告的结果。 |
| [[book-bohr-mottelson-nuclear-structure-vol2]] | §4-5e，印刷 pp.190–192 / PDF pp.212–214；Eqs.4-296–4-308；source claims BM2-1–BM2-4 | 固定惯量转子、D2 与轴/E2 约定背景。本控制没有采用该段高自旋谐近似。 |
| [[book-greiner-nuclear-models]] | 印刷 pp.145–146，Eqs.6.169–6.174；source claim SRC-1 | 固定惯量 D2 转子的模型恒等式背景。未把偶芯三态能量关系当作刚性的实验充分判据。 |

计算证据根目录为
`outputs/l4/20261106-a130-next-evidence/rigid-core-control/`，下文短文件名均相对
该目录。关键原件为：

- [protocol.json](../../outputs/l4/20261106-a130-next-evidence/rigid-core-control/protocol.json)：
  `model`、`closure_scope`、`predeclared_controls`；实际 UTC
  `2026-11-06T08:30:38.890261+00:00` 冻结，早于求解。
- [results.json](../../outputs/l4/20261106-a130-next-evidence/rigid-core-control/results.json)：
  `/cases/0` 至 `/cases/4` 分别对应 \(C=0,1,2,4,8\) MeV；
  每项 `/proxies/0,1,2,3` 分别对应 \(n=1,5,10,\mathrm{all}\)。
- [summary.csv](../../outputs/l4/20261106-a130-next-evidence/rigid-core-control/summary.csv)：
  以列 `C_MeV`、`proxy_n` 唯一定位全部20种组合。
- [proof.md](../../outputs/l4/20261106-a130-next-evidence/rigid-core-control/proof.md)、
  [run_control.py](../../outputs/l4/20261106-a130-next-evidence/rigid-core-control/run_control.py)：
  几何恒等式、窗口精确性与显式未配对实现。
- [checks.json](../../outputs/l4/20261106-a130-next-evidence/rigid-core-control/checks.json)：
  `/checks` 的45项核查与 `/metrics`；[closeout.json](../../outputs/l4/20261106-a130-next-evidence/rigid-core-control/closeout.json)
  保存收束时的哈希复核及未证明的边界。

冻结协议 SHA-256：
`40142b140bebfd5f326ffb56081dd4364559df32c59d65882bf7a5a4e694a109`；
结果 JSON SHA-256：
`68c8f78d02a57097b23e00f4e1d45c121454baf9f3a9e30cc1e9fe2ef4282cf8`。
它们标识本页采用的既有计算版本。不同代数/数值核查仍属于同一模型计算的
验证，不能计成多项独立实验。

| ID | 主张 | claim_kind | evidence_level | source_independence | confidence | locator | needs_review |
|---|---|---|---|---|---|---|---|
| FRC-1 | 固定本页电荷张量时，初始11/2全部态的完整二/三次矩为1与0.5，与 \(C\) 无关。 | model-result | direct | single | high | `proof.md` 点态恒等式与选择定则；`results.json:/geometric_operator_identity` | false |
| FRC-2 | all-\(J+2\) raw ratio 从0.3226168512变为1.0262502334；末点角度未定义。 | model-result | direct | single | high | `results.json:/cases/0/proxies/3`、`/cases/4/proxies/3` | false |
| FRC-3 | 对该 proxy，选定自旋通道内态数收敛不保证完整几何矩闭合或实角换算。 | our-inference | direct | single | high | `results.json:/cases/4/proxies`；`/finite_window/closure_scope` | false |
| FRC-4 | 该独立反例不能推出另一个 IBFM 模型的几何不变。 | our-inference | direct | single | high | 本页 Assumptions、Transfer Conditions；`protocol.json:/model` | false |

## Assumptions

模型取 \(j=11/2\)，所有角动量算符以 \(\hbar\) 为单位。各自旋块在完整裸
转子—粒子乘积空间建立，再投影到全部物理 D2 态：

\[
H(C)=\sum_{k=1}^{3}\frac{(I_{k,\mathrm{right}}\otimes1-1\otimes j_k)^2}
{2\mathcal J_k}+C\,1\otimes Q_j(\gamma).
\]

使用异常对易的右体坐标
\(I_{\rm right}=(J_x,-J_y,J_z)\)，粒子 \(j_k\) 则服从普通对易关系。
这是显式**未配对** Hamiltonian；没有调用 paired solve，没有
\(\Delta=0\) 极限、Nambu doubling 或正能/eta 投影。

\(C\) 的归一化明确规定为

\[
Q_j(\gamma)=
\frac{\cos\gamma[3j_z^2-j(j+1)1]
+\sqrt3\sin\gamma(j_x^2-j_y^2)}{4j(j+1)},\qquad
C=0,1,2,4,8\ {\rm MeV}.
\]

\(Q_j\) 无量纲，\(C\) 包含这个定义下的全部强度及符号。不能把它直接当成
另一篇文献中乘 \(Y_{2\mu}\) 的系数、IBFM 的 \(\Gamma_0\)，或经核质量与
\(\beta\) 标定的实际 Ba 耦合。**改变 \(C\) 不改变电荷算符。**

内禀电荷幅度固定为 \(\mathcal Q=1\)，\(\gamma=20^\circ\)：

\[
a_0=\cos\gamma,\quad a_{\pm2}=\frac{\sin\gamma}{\sqrt2},\quad
a_{\pm1}=0,\qquad
Q_{2\mu}(\Omega)=\mathcal Q\sum_\nu D_{\mu\nu}^{2*}(\Omega)a_\nu\,1_j .
\]

这里只固定归一化电荷几何，没有用核半径/有效电荷将 \(\mathcal Q\) 换成实际
核的数值 \(\beta\)。电荷仅由芯携带，粒子电荷项为零。

惯量采用现有 helper 的明确约定，保持轴序而不排序：

\[
\mathcal J_k=\frac43\mathcal J_0
\sin^2\!\left(\gamma-\frac{2\pi k}{3}\right),\quad
\mathcal J_0=30\ \hbar^2/{\rm MeV},
\]
\[
(\mathcal J_1,\mathcal J_2,\mathcal J_3)
=(38.793852416,\ 16.527036447,\ 4.679111138)\ \hbar^2/{\rm MeV}.
\]

该 \(4/3\) 因子不能省略后仍称相同控制参数。电荷幅度、\(\gamma\)、三惯量
在整条路径固定；初态恒取最低 \(I=11/2\) 态。

## Provisional Reasoning

电荷算符是取向空间上的乘法算符。旋转正交性使
\[
Q\cdot Q=\mathcal Q^2\,1.
\]
按本任务相位约定，
\[
-\sqrt{\frac72}[Q\times Q]^{(2)}\cdot Q
=\mathcal Q^3\cos3\gamma\,1 .
\]
例如对应的实对称无迹 Cartesian 张量主值为
\[
-\frac{\cos\gamma}{\sqrt6}+\frac{\sin\gamma}{\sqrt2},\quad
-\frac{\cos\gamma}{\sqrt6}-\frac{\sin\gamma}{\sqrt2},\quad
\sqrt{\frac23}\cos\gamma .
\]
其平方迹为1，\(\sqrt6\) 倍三次迹为
\(\cos^3\gamma-3\cos\gamma\sin^2\gamma=\cos3\gamma\)。
这给出与 Hamiltonian 本征态无关的几何证明，并非从 \(q_2\) 数值接近倒推
形状。此处 \(q_2=1,\ q_3=\cos60^\circ=0.5\)，完整等效角为20°。

RME 采用
\[
\langle I_fM_f|Q_{2\mu}|I_iM_i\rangle
=\frac{\langle I_iM_i,2\mu|I_fM_f\rangle}{\sqrt{2I_f+1}}R_{fi}.
\]
电磁矩阵元先由 \(P_f^\dagger T_{\rm product}P_i\) 构造，再施加本征矢，
没有使用 paired embedding。复用入口分别是
`paired_single_j_rotor.py` L199–222、L234–252，以及
`paired_single_j_em.py` L5–15、L127、L235–249；
这些模块的冻结哈希在协议 `/input_sha256`。

对 \(I+2\) 内按能量排序的 \(n\) 个完整多重态定义
\[
S_n=\sum_a|R_{ai}|^2,\quad
C_n=\sum_{ab}R_{ai}^{*}R_{ab}R_{bi},\quad
z_n=\sqrt{\frac7{10}}\frac{|C_n|}{S_n^{3/2}}.
\]
这里 \(C_n\) 是三次链，不能与 Hamiltonian 强度 \(C\) 混淆。
仅在 \(0\le z_n\le1\) 时报告 \(\arccos z_n/3\)。

以下均为已冻结的独立模型结果，locator 为 `summary.csv` 的
`C_MeV,proxy_n` 行键；完整 \(q_2=1,q_3=0.5\) 在每行共同成立：

| \(C\)（MeV） | \(z_1\) | \(z_5\) | \(z_{10}\) | \(z_{\rm all}\) | all 条件角 |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.578501 | 0.322617 | 0.322617 | 0.322617 | 23.7262° |
| 1 | 0.814612 | 0.716370 | 0.717145 | 0.716734 | 14.7382° |
| 2 | 0.958418 | 0.853502 | 0.851472 | 0.851096 | 10.5563° |
| 4 | 1.078496 | 0.971119 | 0.966264 | 0.966276 | 4.9741° |
| 8 | 1.140119 | 1.027976 | 1.026226 | 1.026250 | 无实数值 |

20种组合全部保留，五种越域；所有越域角度为 null，未截成0°。
“all”包含全部48个 \(15/2\) 态，因此最后的越域在补全该自旋通道后仍存在。
\(C=0\) 时，该通道只有两个 core-\(R=2\) 态带强度，序号为0和2；
\(n=5\) 已穷尽它们，但受限 ratio 仍不是完整的0.5。

机制由矩阵元收缩体现。在 \(C:0\to8\) 时，
\(S_{\rm all}:3.200000\to3.446951\)，
\(C_{\rm all}:-2.207308\to-7.849771\)。
三次链的中间对角项由−3.310962变为−8.296711，抵消它的非对角项由
+1.103654减至+0.446941。完整6j的其它自旋扇区则补偿，使正/负
spin-pair 和从 \(+0.5+0\) 变为
\(+0.886899009-0.386899009=0.5\)。
locator：`results.json:/cases/0`、`/cases/4` 中的 `proxies/3` 和 `cubic`；
全部19个角动量允许的有序 spin-pair 扇区见
[cubic-spin-sectors.csv](../../outputs/l4/20261106-a130-next-evidence/rigid-core-control/cubic-spin-sectors.csv)，
其余六对权重为零。

静态量也会在固定形状下改变：

| \(C\)（MeV） | \(Q_s/\mathcal Q\) | 静态 \(q_2\) 份额 | 其它同 \(I\) 份额 | all-\(I+2\) 份额 |
|---:|---:|---:|---:|---:|
| 0 | ≈0 | ≈0 | 0.200000 | 0.266667 |
| 1 | −1.089812 | 0.195471 | 0.052498 | 0.317060 |
| 2 | −1.281619 | 0.270332 | 0.029994 | 0.304759 |
| 4 | −1.412734 | 0.328473 | 0.014310 | 0.292793 |
| 8 | −1.477981 | 0.359515 | 0.006653 | 0.287246 |

locator：`results.json:/cases/*/static` 与 `proxies/3/q2_closure_contribution`。
\(Q_s=\sqrt{16\pi/5}\langle I,I|Q_{20}|I,I\rangle\)，与带符号对角 RME
转换一致；此处单位是 \(\mathcal Q\)，不是 \(eb\)。不能把 \(P(R=0)\)
变化单独当作形状改变或机制的因果证据。

## Competing Explanations

本例排除了“所有 proxy 变化均须由内禀电荷形状变化产生”的充分性解释。
受限量仍是旋转标量，因为所选投影包含完整磁多重态；问题在于单一自旋
通道、无完整6j权重的收缩及其形状换算条件，而非破坏旋转不变性。

前若干态的截断会改变数值，但末点的 all 结果说明这种截断不是该点越域的
唯一原因。相位错误、右体坐标符号错误与不完整闭合则由下面的独立控制
检验。本模型中的几何固定是建模输入和算符恒等式；不能借此排除 IBFM
中的实际形状变化、涨落、电荷算符依赖或耦合与几何共同变化。

## Falsification or Reverse Tests

以下均引用已有核查，没有在知识回写阶段重跑：

- `results.json:/geometric_operator_identity`：初始 \(I=11/2,M=1/2\)
  的36维 D2 坐标子空间上，二次矩阵为单位阵、三次矩阵为其0.5倍；
  最大残差均为 \(5.56\times10^{-16}\)，早于本征态选择。
- `/Euler_integral_checks`：独立构造 \(J_y\) 并指数化 Wigner \(d\) 矩阵，
  beta 角分别用24和48节点积分；积分内部不调用CG。与 product-RME/
  Wigner–Eckart 路线最大差 \(2.74\times10^{-14}\)。
- `/preflight_blocks`：独立 D2 群平均投影与 \(PP^\dagger\) 最大差
  \(1.29\times10^{-15}\)；Hamiltonian 与 charge 的泄漏及 Hermiticity
  均通过。实验室张量另检验了 rank-2 协变性。
- `/spectator_R0_checks`：\(C=0,I=j\) 的解析
  \(\sum_K|K,\Omega=K\rangle/\sqrt{2j+1}\) 被每个 \(R_k\) 湮灭，
  恢复零能量、零静态矩。E2 通道份额
  \((2I_f+1)/[5(2j+1)]=(2I_f+1)/60\) 的最大残差为
  \(5.83\times10^{-16}\)；十个带强度的末态均位于独立偶芯
  \(R=2\) 能量0.1267949192、0.4732050808 MeV。
- 同一 spectator 检查刻意把右体 \(I_y\) 符号用错，给解析 \(R=0\) 向量
  1.442081489 MeV 的伪能量。该错误模型只作负对照，没有混入五点生产结果。
- `/multiplet_rephasing_check`：\(C=2\) 时对所有多重态一致施加复相位，
  \(q_3\) 与 proxy 最大改变量分别为 \(1.12\times10^{-16}\)、
  \(3.34\times10^{-16}\)。
- `checks.json:/metrics`：所有生产点在 \(M=1/2\) 和 \(M=11/2\)
  的 direct/6j 最大差为 \(6.67\times10^{-16}\)（\(q_2\)）与
  \(3.61\times10^{-15}\)（\(q_3\)）。主计算含输出实测2.534 s，
  不含Python导入启动；两个加载的OpenBLAS库均运行时查询为1线程。

最低11/2态的相邻平方 fidelity 为0.647638、0.961761、0.964740、
0.978074；五点 same-I gap 为0.126795、0.385532、0.526891、0.617763、
0.717396 MeV。双向最佳匹配序号均为0，locator 为
`results.json:/adjacent_state_overlaps` 与 `/cases/*/state`。
首段存在较大波函数重排；五点采样不证明整个连续 \(C\) 区间无换态。
几何恒等式对该初始自旋的所有态成立，因此核心反例不依赖连续性假设。

## Transfer Conditions

registry 包含 \(I=1/2,\ldots,15/2\) 的所有物理 D2 态，共216个
multiplets、2448个磁子态。对初始 \(I=11/2\)，rank-2 的二次闭合中间
自旋只需7/2、9/2、11/2、13/2、15/2；三次闭合的两个中间态分别与初态
相连，因此也只需这五个自旋。其全部态及中间 RME 均已保留。

**有限窗口对这个初态的 \(q_2,q_3\) 精确，不对无限转子全局完备。**
`complete=True` 仅指所声明的投影窗口；结果另有
`globally_complete_rotor:false`。对窗口顶端初始 \(I=15/2\)，遗漏17/2和19/2
外通道，窗口 D2 坐标态平均 \(q_2=0.525\)；在 spectator 初始11/2处刻意
去掉15/2通道，则仅剩 \(q_2=11/15\)。locators：
`results.json:/high_I_boundary_check`、
`/spectator_R0_checks/deliberately_omit_I15half`。

可迁移的是区分几何恒等式、完整多项式矩、通道投影和条件角换算的检查方式。
换初始自旋须重新证明通道覆盖；加入粒子电荷、形状振动、不同算符或模型空间，
须重新检查恒等式。不能搬用本页的 \(C\) 数值或固定几何结论解释实际 Ba。

## Failure Conditions

若改变 charge 的内禀幅度/\(\gamma\)、把 \(C\) 偷换为另一归一、引入配对
投影、遗漏允许 RME，或 direct/6j 与几何恒等式不再一致，本页的具体数值
控制即不适用。将越域值裁剪为0°、把全 \(I+2\) 通道称为全核闭合，或把
反例当成“IBFM几何已证明不变”，均超出本页证据。

## Open Questions

本次有界控制的必需计算与核查已完成。未证明未采样 \(C\) 区间的连续
态身份，也未判断实际 IBFM 中几何、涨落和电荷算符的贡献。实际137Ba的
实验benchmark与论文整合属于父任务，本页不提供该实验结论，不据此开启
新计算或检索。

## Human Review

用户已表示读过本 sidecar 的 report/checks，并要求将其收束纳入固定形状
反例。该事件不等同于审阅本次新建知识页；本页保留
`review_status: unreviewed`。数值与来源定位的 self-audit 不写作
human-reviewed，也不代替实验验证。

## Promotion or Rejection History

- 2026-11-06：按预定协议完成显式未配对五点控制、独立几何/积分/spectator
  核查，收束产物并保持输入模块不变。
- 2026-11-06：用户授权仅将已完成结果写入本专属 research-note；
  `reasoning_status: provisional`，未晋升为核素事实或正式实验判据。
  本次回写没有修改 index、handoff、共享稿件或既有 sidecar。
