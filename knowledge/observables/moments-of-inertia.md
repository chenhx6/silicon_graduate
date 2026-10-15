---
type: observable
title: 转动惯量
aliases: [moments of inertia, kinematic moment of inertia, dynamic moment of inertia, J1, J2]
created: 2026-07-02
updated: 2026-10-15
status: active
review_status: unreviewed
observable_kind: rotational-response
symbol: "J^(1), J^(2)"
units: "hbar^2/MeV"
tags: [rotation, backbending, band-crossing, alignment]
---

# 转动惯量（Moments of Inertia）

## Definition

运动学转动惯量 \(J^{(1)}\) 描述角动量与转动频率的比值，动力学转动惯量 \(J^{(2)}\) 描述角动量随转动频率的变化率。离散能级分析中需使用论文明确给出的有限差分约定。

## How It Is Obtained

由同一能带中已定自旋的相邻 γ 跃迁能量构造转动频率，再按原文约定计算 \(J^{(1)}\) 与 \(J^{(2)}\)。[[de-voigt-dudek-szymanski-1983-high-spin-phenomena]] 在 pp.974-975 给出连续形式和 aligned-angular-momentum 参照。

For a `Delta I=1` doublet sequence, [[peng-chen-2022-chiral-rotation-rhodium-isotopes]] uses `J^(1)=2I/[E_gamma(I+1→I)+E_gamma(I→I-1)]`, `J^(2)=2/[E_gamma(I+1→I)-E_gamma(I-1→I-2)]`, and `hbar omega_exp` equal to half the first denominator. This source-specific finite-difference convention must not be mixed with a `Delta I=2` formula.

## Diagnostic Use

用于识别转动响应、[[backbending]]、band crossing、[[angular-momentum-alignment]] 与可能的配对变化。

## Model Dependence

数值依赖自旋指认、频率/有限差分定义、参考转子和带成员选择。刚体值只是参照，不自动代表真实刚性形变。

## Failure Modes and Ambiguities

\(J^{(2)}\) 对带交叉和二阶差分很敏感。综述在 pp.996-997 明确警告，带交叉与 alignment 可混淆对 pairing collapse 的推断。

[[domscheit-1999-triaxial-superdeformation-163lu]] 的 Fig.4 给出具体限制：SD1 低频 `J^(2)` 的强波动可由同自旋宇称 SD-ND 态混合造成；校正约 5 keV 的能级排斥后曲线更平滑。SD2 的 `J^(1)` 还依赖最低自旋 `39/2` 的暂定假设。两带相近的转动惯量支持相近形变，但不能单独确定三轴性或 wobbling。

Peng and Chen 2022 provides another failure mode: its mean-field `J^(2)` curves are smooth while imported Rh data oscillate, tentatively attributed to normal-deformed-band mixing. Similar yrast/side `J^(1)` and convergence of calculated `J^(1),J^(2)` above `omega_crit` are supportive rotational-response patterns, not unique chirality tests.

## 绝对标签、有限差分与有序路径

[[petrache-2015-nd-exotic-rotations-triaxiality]] PT15-9称J^(2)不依赖band spin assignment和excitation energy。需分开**绝对自旋/能量起点**与**相对自旋步长、跃迁顺序和path**；后者仍是输入。[[peng-chen-2022-chiral-rotation-rhodium-isotopes]] PC22-19已回原PDF6核Eqs.(2)–(3)与ω句：保留其跨两条photon的分母、numerator2及源图的频率标签，不用本任务的坐标取代它。

### 本任务明确选定的edge-pair估计

令自旋数i以ℏ为单位、两条跃迁有相同`k=Δiγ>0`，光子能量e用MeV；本任务给每条edge选`x=e/k`、spin location `i_parent−k/2`。两edge母态差为Δip时，取

`J2_hat/ℏ²=Δip/Δx=kΔip/Δe`，
`x_bar=(ea+eb)/(2k)`，`i_bar=(ia+ib−k)/2`。

这是声明的finite-response定义。只有相邻edges沿同一路且parentstep=k时，分离d条edge才给`d k²/Δe`。ΔI1相邻差分分子1，跨两条分子2；ΔI2同signature相邻edges的分子4。若比较交错signature的连续parent而parentstep=1，分子是2，不能默套4；该交错估计也不等于一条connected E2 path。

绝对i整体平移不改Δip；激发能起点平移在形成Eγ前就消去。**光子能量**共同offset则移动x而不改这个曲率，共同gain会同时缩放x并反比缩放J2，不能说校准全部取消。若改变k、错配branch或次序，结果可改变。不同差分有不同spin/frequency位置；不能当同一位置的独立重复测量。

### 136Pr D4：实际能量与路径

直接输入是[[lv-2025-136pr-tac-covariant-density-functional]] LV25-31、LV25-34、LV25-35的TableI D4及Fig1。所选子链母态自旋16–23；23仍tentative，表中4个M空栏保持。k来自作者reported spin path的条件，不补成逐线实测pure M1/E2。

| 母态i | Δi1 γ (keV) | Δi2 crossover γ (keV) |
| --- | ---: | ---: |
| 16 | 273.6(1) | 481.0(5)，M空 |
| 17 | 370.8(6)，M空 | 644.1(3) |
| 18 | 409.3(3) | 780.3(4) |
| 19 | 440.0(2) | 849.4(5) |
| 20 | 503.6(2) | 943.8(6) |
| 21 | 510.3(2) | 1014.2(4) |
| 22 | 530.1(3) | 1040.0(5) |
| (23) | 587.4(5)，M空 | 1117.9(7)，M空 |

同signature crossover路径为16/18/20/22与17/19/21/23。Dipole相邻曲率如下；数值是该声明估计的名义变换，不是论文报告的另一组实测惯量或shape测量：

| i_bar | x_bar (MeV) | J2_hat (ℏ²/MeV) |
| --- | ---: | ---: |
| 16 | .32220 | 10.288 |
| 17 | .39005 | 25.974 |
| 18 | .42465 | 32.573 |
| 19 | .47180 | 15.723 |
| 20 | .50695 | 149.254 |
| 21 | .52020 | 50.505 |
| 22，含(23)输入 | .55875 | 17.452 |

跨两条dipole的6点为14.738、28.902、21.209、28.450、75.472、25.940，`i_bar=16.5…21.5`，对应x为.34145、.40540、.45645、.47515、.51685、.54885 MeV。它们是相邻两个J2_hat的harmonic mean而非arithmetic mean，不能把峰值75.472和149.254当同位置矛盾。偶/奇crossover路径各3点名义值分别为13.365/24.465/41.580和19.484/24.272/38.573，位置与取样窗也不同；完整pair/位置保存在下方回执，不能汇成26个独立数据点。

### 误差与筛选只作声明控制

在把photon括号误差**当σ且相互独立**的一阶模型下，149.254点的σ约6.301；只约束两条marginal σ而允许其相关性变化时，一阶σ范围为0–8.911。真实共同Σ和coverage没有给出，这些不是实验置信区间。相邻曲率共享一条γ，即使photon误差独立也产生负的neighbor covariance；不能把各J2误差再假设独立。

参照PT15-4只做一次明确的counterfactual：保持本练习全部selected interaction点，以x>.3 MeV为范围，再删去达到初始mean两倍的显示点。名义均值43.110变为25.419，被删点149.254及mask均保留。**这不是作者对Pr136的筛选，也不是Nd51/23的复现或其偏差检验**；源实际interaction/选带mask缺失。负secant与零分母也必须显式标记，不可自动消失。

[day14_pr136_inertia_paths.py](../../system/scripts/day14_pr136_inertia_paths.py)与[71-check回执](../../outputs/learning-daily/20261014-DAY14-week-two-spectrum-to-level-scheme-exam-run-02/pr136-inertia-paths.json)核actualPDF/16条主输入、branch/closure、两种stencil、signature、source Eq3、quadratic-rotor极限、offset/gain和conditional covariance。首次68项后补了direct PC22式和能量起点控制，最终71项通过。实际crossing机制、γ/转轴或shape coexistence仍不能由这些曲率唯一决定。

## Sources

- [[lv-2025-136pr-tac-covariant-density-functional]] LV25-31、LV25-34、LV25-35：实际D4能量/路径及原输入边界。
- [[petrache-2015-nd-exotic-rotations-triaxiality]] PT15-4、PT15-9：源惯量系统学的筛选和绝对标签边界。
- [[de-voigt-dudek-szymanski-1983-high-spin-phenomena]]
- [[domscheit-1999-triaxial-superdeformation-163lu]]
- [[peng-chen-2022-chiral-rotation-rhodium-isotopes]]

## Evolution Log

- 2026-10-15：补D4有序path、stencil位置/交错signature与71-check能量练习；不重算Nd均值或赋新γ/轴。
- 2026-07-03：加入 `163Lu` 的带混合校正和自旋假设依赖案例。
- 2026-08-11: added the `Delta I=1` Rh finite-difference convention and smooth-theory/oscillatory-data mixing boundary.
