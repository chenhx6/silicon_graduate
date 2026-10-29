---
type: research-note
title: "手征—八极四重态的 D2/单纯形离散对称与电磁跃迁选择定则"
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
category: research-notes
evidence_sources: [frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, butler-nazarewicz-1996-intrinsic-reflection-asymmetry, liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br, guo-2020-pseudospin-chiral-quartet-131ba, tonev-2006-134pr-lifetime-chiral, petrache-1996-rotational-bands-134pr]
aliases: [chiral-octupole-quadruplet-discrete-symmetries, chiral-octupole selection rules, 手征八极四重态选择定则]
created_from: Day26 chiral-octupole quadruplet discrete-symmetry and transition-rule investigation
promotion_target: chiral-octupole-coexistence
tags: [chirality, octupole, quadruplet, odd-odd, odd-a, D2, simplex, signature, E1, E2, E3, M1, branching-ratio]
worker_artifacts: outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/chiral-octupole
---

# 手征—八极四重态的 D2/单纯形离散对称与电磁跃迁选择定则

## Research Trigger

本笔记把两个局域二态自由度放进同一个最小投影模型：三轴形变在
`gamma` 约 `30 deg` 附近允许非共面角动量几何，反射不对称坐标由
`beta_3` 的两个局域井表示。目标是推导实验室系中
`(I+,1)`, `(I+,2)`, `(I-,1)`, `(I-,2)` 四个序列的群论选择规则，定义可从
分支比和寿命得到的无量纲判据，并标出需要两自由度同时翻转的交叉跃迁的阶数抑制。

## Grounded Evidence

这是一套对称性和可复核代数的研究模型。Frauendorf 2001 说明 aplanar
左右手平均场在角动量与对称性恢复后可形成同宇称、近简并的
`Delta I=1` 双带，并强调 TAC 几何本身不包含量子隧穿和严格的好角动量
投影（`F01-8`, `F01-9`，PDF pp.476, 484--485）。Butler--Nazarewicz 1996
把交替宇称、E1/E3 和静态八极极小、八极软性、振动及宇称恢复分开，且指出
E1 对质子--中子偶极相消敏感而 E3 更集体（`BN96-1`--`BN96-3`）。因此
下文的四态规则是 `D2`/单纯形约束下的可计算基线，不把任何单个核的候选
带直接升级为已经确证的静态手征—八极四重态。

现有实验前例提供动机和反证边界，而不是本模型的数值标定。`78Br` 有两对
候选手征双带和八条强 E1 连接，但作者把单核手征—宇称 quartet 写成未来
可观测方向；`beta_30` 势面是软的（`L16-9`, `L16-13`, `L16-14`）。
`131Ba` 的 D3--D6 是相互连接的正宇称四带流形，D7/D8 另成负宇称候选双带，
但能量和连接不能唯一把 D3--D6 分成两对，且 `beta_3=0.05` 只是 RAT-PRM
输入（`GU20-4`, `GU20-7`, `GU20-10`, `GU20-14`, `GU20-16`）。`134Pr` 的
寿命给出近简并区两带带内 `B(E2)` 约 2--3 倍差异、`B(M1)` 平滑且无预期交错，
模型比较因此不支持静态手征（`TO06-D24-003`--`TO06-D24-006`）。

## Provisional Reasoning

## 1. 局域四态、投影和双重隧穿

### 1.1 局域基底

令 `tau` 作用于左右手局域波包，`xi` 作用于两个八极井：

$$
 \mathcal B_{\rm loc}=
 \{|L,+\rangle,|R,+\rangle,|L,-\rangle,|R,-\rangle\},
 \qquad \tau_z|L,\xi\rangle=+|L,\xi\rangle,
 \quad \tau_z|R,\xi\rangle=-|R,\xi\rangle .
$$

这里 `+/-` 是局域 `beta_3` 井的标签，不是实验室宇称。八极反射操作
在这个截断空间中可写成 `P=xi_x`；有效左右交换写成 `U_chi=tau_x`。
微观手征操作通常记为
`C = T R_y(pi)`（或等价主轴约定），它含有反幺正时间反演，不能像普通
宇称那样把其“本征值 `+/-`”当成相位不变的实验量。下面的 `eta=+/-` 是
`U_chi` 的对称/反对称隧穿支标签，代表手征伙伴分支，而不是可直接测量
的左手或右手本征值。

### 1.2 角动量和宇称恢复

从一个局域参考态 `|Phi_{L,+}>` 出发，角动量投影和两个离散投影的最小
写法为

$$
 |IM;\eta p\rangle = {cal N}_{I\eta p}
 P^I_{MK}(1+p\hat P)(1+\eta U_{\chi})|\Phi_{L,+}\rangle,
 \qquad \eta,p=\pm1 .
$$

`P^I_{MK}` 是好 `I,M` 投影算符；`p` 是实验室好宇称，`eta` 是有效左右
交换的隧穿支。对奇奇核 `I` 为整数，对奇-A 核 `I` 为半整数，四类标签
仍按 `(eta,p)` 组织。实际 PRM/GCM 中两个投影可能不正交，且组态混合会
让 `eta` 只成为近似标签；这正是需要寿命、偏振和绝对矩阵元的原因。

### 1.3 最小 Hamiltonian

在局域四态空间取

$$
 H_I=E_0(I){\bf 1}-t_\chi(I)\tau_x-t_\pi(I)\xi_x
      -t_{\chi\pi}(I)\tau_x\xi_x .
$$

由于 `tau_x` 和 `xi_x` 对易，投影支的能量为

$$
 E_I(\eta,p)=E_0(I)-\eta t_\chi(I)-p t_\pi(I)-\eta p t_{\chi\pi}(I),
$$

并得到

$$
 \begin{aligned}
 \Delta_\chi(p)&=E_I(-,p)-E_I(+,p)=2[t_\chi+p t_{\chi\pi}],\\
 \Delta_\pi(\eta)&=E_I(\eta,-)-E_I(\eta,+)=2[t_\pi+\eta t_{\chi\pi}].
 \end{aligned}
$$

`t_chipi` 是两个隧穿自由度最低阶的纠缠项。它使正、负宇称子空间的手征
劈裂不同，也使左右手性子空间的宇称劈裂不同。若它为零，两个双重劈裂
才在该模型中完全可分离；其非零本身仍是模型参数，不能由近简并能谱独立
反演。

## 2. `D2` 和单纯形 `S_x`

### 2.1 `D2` 约束

三轴内禀形状保留主轴半转生成的

$$
 D_2=\{1,R_x(\pi),R_y(\pi),R_z(\pi)\}.
$$

四个一维表示可用 `(R_x,R_y,R_z)` 的字符表示：

| 表示 | `R_x(pi)` | `R_y(pi)` | `R_z(pi)` | 典型作用 |
|---|---:|---:|---:|---|
| `A` | `+` | `+` | `+` | 标量和对角二阶张量组合 |
| `B_x` | `+` | `-` | `-` | `x` 方向极性/轴性矢量分量 |
| `B_y` | `-` | `+` | `-` | `y` 方向矢量分量 |
| `B_z` | `-` | `-` | `+` | `z` 方向矢量分量 |

对奇-A 核，严格说应使用 `D_2` 的双群；半整数 signature 的本征值为
`r_x=+-i`，而不是 `+-1`。算符选择规则用表示乘积表达：

$$
 \Gamma_f\subset\Gamma_i\otimes\Gamma_{X\lambda},
 \qquad
 \chi_{X\lambda}(R_k)\chi_i(R_k)=\chi_f(R_k).
$$

这条 `D2` 规则约束内禀分量和 signature 连接；它不取代实验室的角动量
三角条件。

### 2.2 单纯形本征值

取

$$
 \hat S_x=\hat P\hat R_x^{-1}(\pi),
 \qquad r_x=e^{-i\pi\alpha},
 \qquad s_x=p r_x,
$$

其中 `alpha=0,1` 对应奇奇整数自旋序列，`alpha=+-1/2` 对应奇-A
半整数序列。于是

$$
 \hat S_x|IM\alpha p\rangle=s_x|IM\alpha p\rangle .
$$

若球张量分量以 `x` 轴为量子化轴，且 `mu` 是该轴分量，则

$$
 \hat S_x T_{X\lambda\mu}\hat S_x^{-1}
 =\sigma_{S_x}(X\lambda\mu)T_{X\lambda\mu},
 \qquad
 \sigma_{S_x}=\pi_X e^{-i\pi\mu},
$$

其中

$$
 \pi_{E\lambda}=(-1)^\lambda,
 \qquad
 \pi_{M\lambda}=(-1)^{\lambda+1}.
$$

因此一个固定 simplex 分量的非零矩阵元必须满足

$$
 s_f^*s_i=\sigma_{S_x}(X\lambda\mu).
$$

这是 `S_x` 版本的严格选择规则；不同的轴、球张量相位和 signature 约定
只会改变表中的相位表示，不改变宇称规则和可测的平方模。对约化跃迁还要
同时满足

$$
 |I_i-I_f|\leq\lambda\leq I_i+I_f.
$$

宇称选择规则是普适的：

$$
 E\lambda:\ p_f=p_i(-1)^\lambda,
 \qquad
 M\lambda:\ p_f=p_i(-1)^{\lambda+1}.
$$

所以 `E1/E3` 变宇称，`M1/E2` 保持宇称；`Delta I=1` 的 M1/E2 混合和
`Delta I=2` 的 E2 crossover 都必须另行检查 `D2`/simplex 连接。所谓“强”
是波函数和几何的结论，不是以上宇称等式的群论必然性。

## 3. 两个二态自由度的算符代数

把局域算符统一写成

$$
 O_{ab}=\tau_z^a\xi_z^b,\qquad a,b\in\{0,1\} .
$$

在 `(eta,p)` 投影基底中有

$$
 \langle\eta_f,p_f|O_{ab}|\eta_i,p_i\rangle
 \propto
 \delta_{\eta_f,(-1)^a\eta_i}
 \delta_{p_f,(-1)^b p_i} .
$$

这给出一个比“左右手标签”更稳妥的跃迁记账法：`a=0/1` 表示是否翻转
手征隧穿支，`b=0/1` 表示是否翻转宇称。主导低阶项可以写成

| 类别 | 主导算符 | `Delta eta` | `Delta p` | 典型通道 | 振幅阶数 |
|---|---|---:|---:|---|---|
| 带内 M1 | `tau_0 xi_0` | 0 | 0 | `Delta I=1 M1` | `O(1)` 或组态混合压低 |
| 带内 E2 | `tau_0 xi_0` | 0 | 0 | `Delta I=1 E2` 混合、`Delta I=2 E2` | `Delta I=2` 为 `O(1)` |
| 手征伙伴 M1 | `tau_z xi_0` | 1 | 0 | 同宇称 `Delta I=1 M1` | `O(1)` 的手征奇电流项 |
| 手征伙伴 E2 | `tau_z xi_0` | 1 | 0 | 同宇称 `Delta I=1,2 E2` | `O(epsilon_chi)` 或相位相消 |
| 宇称伙伴 E1 | `tau_0 xi_z` | 0 | 1 | `Delta I=1 E1` | `O(beta_3)` 或八极关联 |
| 宇称伙伴 E3 | `tau_0 xi_z` | 0 | 1 | 首选 `Delta I=3 E3` 网络 | `O(beta_3 Q_3)`，通常更集体 |
| 交叉 E1 | `tau_z xi_z` | 1 | 1 | `Delta I=1 E1` | 因子化一声子极限为零；首个项 `O(epsilon_chi beta_3)` |
| 交叉 E3 | `tau_z xi_z` | 1 | 1 | 首选 `Delta I=3 E3` | 混合核 `O(epsilon_chi beta_3)`；双声子核可为 `O(epsilon_chi epsilon_3)` |

这里的“首选 `Delta I=3`”来自轴向/准轴向集体 E3 的转动几何；严格允许
范围仍由 `|I_i-I_f|<=3` 和具体 `K`/simplex 耦合给出。交叉 E1/E3 在
完全因子化的低阶一体算符中没有 `tau_z xi_z` 分量，因而不是“必须强”的
网络。它们的出现反而是手征—八极混合、组态混合或双声子有效核的检验。

### 3.1 手征伙伴 M1 与 E2 的相消

若左右局域流对某个多极通道给出 `m_L,m_R`，则投影后的同支和伙伴支是

$$
 m_{\rm intra}=\frac{m_L+m_R}{2},
 \qquad
 m_{\rm chiral}=\frac{m_L-m_R}{2},
$$

相位规范改变时两式的正负号可交换，但平方模和相消边界不变。E2 具有
完全相同的和/差结构，且 `q_L,q_R` 还会被三轴核芯四极矩和 `gamma` 几何
重整。故 `B(M1)` 或 `B(E2)` 的一个低值不能独自决定手征是否存在；需要
同一组态、同一自旋区的 partner-resolved 寿命和相位敏感量共同约束。

对 `Delta I=1` 的 M1/E2 混合跃迁，定义角分布/偏振中的相干振幅代理

$$
 A_{\rm ang}=M1+\delta E2,
 \qquad
 C_{\rm int}=\frac{|M1+\delta E2|^2}
 {|M1|^2+|\delta E2|^2}.
$$

`C_int=0` 是同一角分布张量分量的完全相消条件；`C_int` 接近零表示相位
和几何项抵消。它不是总辐射宽度：对全角积分的未极化总宽度，正交多极
贡献按 `Gamma_M1+Gamma_E2` 相加。实验上必须用 DCO、线偏振、角分布或
混合比的联合拟合确定 `delta`，不能从一个未校正分支比直接取其符号。

## 4. 无量纲实验判据矩阵

### 4.1 归一化定义

由于 `B(M1)` 和 `B(E1)` 的传统单位不同，直接写物理单位比值并不是无量纲
量。定义固定质量数和约定下的 Weisskopf 归一化

$$
 \widehat B(X\lambda)=\frac{B(X\lambda)}{B_{\rm W}(X\lambda)} .
$$

同一初态的已校正分支比可给出

$$
 \frac{\widehat B(M1)}{\widehat B(E1)}
 =\frac{I_\gamma(M1)}{I_\gamma(E1)}
 \left(\frac{E_{\gamma,E1}}{E_{\gamma,M1}}\right)^3
 \frac{1+\alpha_{E1}}{1+\alpha_{M1}}\,C_{\rm unit},
$$

其中 `alpha` 是内转换系数，`C_unit` 固定磁、电 Weisskopf 规范。若已有
绝对寿命，则直接用两个 `B` 值，避免 feeding、人口和未观测分支把
branching ratio 伪装成矩阵元比。

本笔记使用三个核心无量纲量：

$$
 \begin{aligned}
 R_{B}^{M1/E1}(I)&=
 \frac{\widehat B(M1;I\to I-1)_{\rm chiral}}
      {\widehat B(E1;I\to I-1)_{\rm octupole}},\\
 R_{\Gamma}^{M1/E1}(I)&=R_B^{M1/E1}(I)
 \left(\frac{E_{\gamma,M1}}{E_{\gamma,E1}}\right)^3,\\
 R_{E2}(I)&=\frac{\widehat B(E2;I\to I-2)}
                 {\widehat B(E2;I_0\to I_0-2)_{\rm same\ band}},\\
 \sigma_{\rm cross}^{E\lambda}(I)&=
 \frac{\widehat B(E\lambda)_{\Delta\eta=1,\Delta p=1}}
      {\widehat B(E\lambda)_{\Delta\eta=0,\Delta p=1}} .
 \end{aligned}
$$

`R_B` 对应矩阵元尺度，`R_Gamma` 对应同初态部分宽度尺度，`R_E2` 追踪
四极集体基线，`sigma_cross` 直接检验双自由度同时翻转的抑制。不同核和
不同 `A` 的比较必须保留 `B_W`、内转换、初态简并因子和 feeding 协方差。

### 4.2 判据矩阵

| 判据 | 无量纲实现 | 四重态基线 | 竞争解释/反证 | 必要 companion |
|---|---|---|---|---|
| 同宇称手征近简并 | `S_chi(I)=Delta_chi(I)/E_gamma`，配合两种宇称分别计算 | 两个宇称子空间均可见相近 `S_chi`，但允许 `t_chipi` 造成有系统的宇称依赖 | 只有一对近简并、另一宇称不闭合，或 `S_chi` 可由 signature/组态交叉解释 | 逐自旋四带、`S(I)`、对齐和组态同一性 |
| `M1` 手征伙伴 / `E1` 八极伙伴 | `R_B^(M1/E1)` 和 `R_Gamma^(M1/E1)` | 同一自旋窗口有稳定、可重复的同宇称 M1 partner link 与异宇称 E1 network；具体大小无普适门限 | `M1` 只在单条线出现、E1 只由 feeding 选择造成，或两者来自不同组态 | partner-resolved lifetime、DCO/偏振、绝对 `B(M1),B(E1)` |
| 四极带内基线 | `R_E2(I)=Bhat(E2;I->I-2)/Bhat(E2;I0->I0-2)` | 同一组态的 `R_E2` 平滑；手征伙伴的对应 E2 在静态极限趋近且相位/交错一致 | 像 `134Pr` 一样持续 2--3 倍不对称且 M1 无预期交错，静态手征应降级 | 同一方法的两带寿命、feeding 完整度、模型含形状涨落 |
| E1 cancellation / E3 collectivity | `Bhat(E1)`、`Bhat(E3)` 及 `Bhat(E3)/Bhat(E1)` | E1 可因质子—中子相消而小，E3 仍形成同一异宇称网络；E3 是更稳健的八极伴随量 | 只有 E1 峰而没有绝对 E3，不能区分八极关联、组态混合和偶极相消 | 直接 E3 寿命或库仑激发、内转换、完整异宇称闭环 |
| 交叉双翻转 | `sigma_cross^E1`、`sigma_cross^E3` | 相对于 direct parity links 至少显示阶数抑制；其自旋依赖可随 `t_chi`, `t_pi` 变化 | 交叉线与 direct 线同阶且不需混合核，说明因子化四态模型不适用或带号错误 | 同初态相对强度、角分布相位、组态混合计算 |
| M1/E2 干涉 | `C_int=|M1+delta E2|^2/(|M1|^2+|delta E2|^2)` | 某些 partner 分支允许相消、另一些分支增强，且相位由偏振/DCO 约束 | 只看总分支比得到的“相消”无法确定；总宽度不发生跨多极干涉 | 线偏振、DCO、角分布和同一线的 `delta` 双根检验 |
| `D2`/simplex 闭合 | `s_f^*s_i=pi_X exp(-i pi mu)` 逐线检查 | 所有带内和互连线可用同一轴约定、`alpha` 和宇称解释 | 只有换轴或换相位才可闭合，或不同线需要互相矛盾的 signature | 逐线多极性、混合比、`R_ac`/ADO 和角动量投影 |
| 绝对矩阵元一致性 | 由 `tau`, feeding 和 `B(Xlambda)` 重建 `R_B` | 能谱、`R_B`, `R_E2`, `sigma_cross` 可由同一 `t_chi,t_pi,t_chipi` 和同一波函数空间拟合 | 仅相对 branch 能拟合而绝对寿命失败，优先判为候选四重态或模型缺自由度 | 完整寿命、内转换、未观测分支上限和协方差矩阵 |

这里“基线”是结构性预期，不是跨核通用的数值阈值。若没有绝对寿命，
`R_B` 只能作为条件性、同一初态和同一 feeding 处理下的相对指标；不能把
相对 `E1` feeding 直接当成 `B(E1)`。`131Ba` 已明确给出相对 E1 模式但无
寿命和绝对约化几率，正是这一限制的实验例子（`GU20-11`, `GU20-16`）。

## 5. 可复核模型与数值输出

本任务的 worker 位于：

`outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/chiral-octupole/`

新增文件为：

- `chiral_octupole_selection_rule_matrix.py`：标准库 Python 验证脚本；
- `chiral_octupole_selection_rule_matrix.json`：`D2` 字符、simplex 表、算符
  选择规则和数值诊断；
- `chiral_octupole_selection_rule_matrix.csv`：通道级选择定则矩阵；
- `chiral_octupole_dimensionless_criteria.csv`：`I=10..14` 的无量纲示意
  判据矩阵；
- `README-selection-rules.md`：运行和单位边界。

运行命令：

```bash
python3 outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/chiral-octupole/chiral_octupole_selection_rule_matrix.py
```

脚本检查 `D2` 四个一维表示、奇奇/奇-A 两类 simplex 行、十个选择规则行，
并验证 synthetic cross/direct 比值小于 `0.01`。示意输出在 `I=10--14`
中保持 `R_B^(M1/E1)约1.20`，能量五次方修正后的 `R_Gamma` 约
`1.45--1.64`，`sigma_cross^E1约5.10e-3`，`sigma_cross^E3约3.91e-3`。
这些数字只验证公式、相位和阶数记账；它们不是任何核素的测量结果。

## Assumptions

1. `tau` 与 `xi` 是两个有效的局域二态坐标；`eta` 是左右交换的隧穿支，
   不是反幺正手征算符的相位不变本征值。
2. `P=xi_x`、`O_ab=tau_z^a xi_z^b` 和 `H_I` 只在四态截断空间内成立；
   完整 PRM/GCM 可加入非正交核、组态混合和 `K` mixing。
3. 表中的 `O(1)`、`O(beta_3)` 和 `O(epsilon_chi beta_3)` 表示相对于
   固定 multipole-specific reduced scale 的振幅阶数，不是实验数值门限。
4. worker 里的能级、振幅、Weisskopf 归一化和能量因子均为 synthetic，
   不可移植为任何特定核的测量输入。

## 6. 竞争解释、转移条件和失败条件

## Competing Explanations

1. `E1` 网络可能来自八极软性、组态混合、`Delta j=Delta l=3` 轨道耦合或
   feeding 选择；`B(E1)` 小还可能只是质子—中子偶极相消，不能用来唯一反演
   `beta_3`。`78Br` 的 `beta_30` 软势面和 `131Ba` 的 tentative `beta_3`
   都要求保留这一层次。
2. 四带近简并可能来自两准粒子组态交叉、pseudospin、signature partner、
   `gamma`-phonon 或形状涨落。`131Ba` D3--D6 不能只由能量/连接唯一配对，
   `134Pr` 的寿命不对称则直接削弱静态手征极限。
3. `M1` 的左/右流相消受有效 `g` 因子、Coriolis 混合、核芯极化和相位约定
   影响；`B(M1)` 交错是支持性观测，不是手征的单独充要条件。

## Transfer Conditions

要把本矩阵用于某个奇奇或奇-A 核，至少需要：

- 逐自旋的四带能级和可靠 `I^pi`；
- 每条 `Delta I=1` 线的 DCO/ADO、线偏振和混合比双根检查；
- partner-resolved `tau`，并用 feeding/内转换校正得到绝对 `B(M1), B(E1), B(E2)`；
- 异宇称 direct E3 或可复核的上限；
- 同一 PRM/GCM/TAC 扩展同时含 `gamma`, `beta_3`, 两种隧穿以及组态混合，
  对 `R_B`, `R_E2`, `sigma_cross` 作联合拟合。

## Failure Conditions

- 若只有一对同宇称近简并带，或异宇称线不能逐自旋闭合，则只能保留
  chiral-doublet 或 octupole-correlation 解释，不能命名四重态。
- 若 partner-resolved 结果出现稳定的 `134Pr` 式 `B(E2)` 2--3 倍差异且
  `B(M1)` 没有预期交错，静态手征解释降级为动态手征/形状涨落。
- 若 `sigma_cross^E1` 和 `sigma_cross^E3` 与 direct 网络同阶，并且不需要
  chiral--octupole 混合核即可重现，最小张量积模型被否定或必须加入额外自由度。
- 若 `D2`/simplex 只在逐线更换轴、signature 或相位约定后才能闭合，优先
  检查带号和投影约定，不把不一致强行解释成新对称性。
- 若 E3 缺失但统计、效率、内转换或 gate 灵敏度不足以给出上限，记录为
  `conditional contradiction`，不能写成八极四重态已被证伪。

## Falsification or Reverse Tests

1. 用同一 `t_chi,t_pi,t_chipi` 和同一波函数空间联合拟合能谱、`R_B^(M1/E1)`、
   `R_E2`、direct E3 与 `sigma_cross`；若只有相对 branch 可拟合而绝对寿命
   失败，四态模型应降级或引入额外自由度。
2. 在相同统计、效率、gate 和内转换灵敏度下比较 direct 与 cross E1/E3。
   若 `sigma_cross` 不随混合强度按平方缩放，`tau_z xi_z` 的一阶独立核或
   带标记错误必须优先检查。
3. 对 `M1/E2` 混合线反演 `delta` 的双根，并用线偏振和角分布确认相位；若
   只有 branch ratio 而无相位敏感 observable，不把 `C_int` 的极小值当成
   已证实的流相消。
4. 用至少一个同组态异宇称窗口检查 `B(E3)` 和 `B(E1)` 的独立性；E1 的
   过零而 E3 保持集体并不等于静态 `beta_3`，但 E3 缺失的 upper limit
   可改变八极解释的排序。

## 7. 研究状态与自审

### Statement classes

- `F01-8/F01-9/F01-13/F01-14`, `BN96-1--3`：Wiki source-grounded review
  background and limitations。
- `L16-9/L16-13/L16-14`, `GU20-4/GU20-7/GU20-10/GU20-14/GU20-16`,
  `TO06-D24-003--006`：source-grounded experiment/model boundary。
- `D2`/simplex 方程、`O_ab` 张量积、`R_B`/`R_Gamma`/`sigma_cross` 和
  `C_int`：本任务的 general-background derivation 与 provisional inference。
- worker 数值：synthetic model result，不能冒充实验。

### Self-audit conclusion

本轮 `supports`：在同时存在三轴手征和反射不对称自由度的假设下，实验室
四分支可以用 `(eta,p)`、`D2` 和 `S_x` 统一记账；E1/E3 direct parity
网络、M1/E2 same-parity 网络和双翻转交叉网络具有可区分的算符阶数。

本轮 `limits`：`gamma约30 deg`、`beta_3不等于0`、四重简并和“强 E1/E3”
是模型前提或条件性预期，尚不是 `78Br`、`131Ba` 或 `134Pr` 的实验事实。
`R_B^(M1/E1)` 没有普适数值阈值；没有寿命、feeding 和内转换闭合时，只能
作为相对判据。

本页为 `status: ai-draft`, `review_status: unreviewed`。Codex self-audit
没有写成 `human-reviewed`；后续若用于论文主张，应回到 source 页、原文
locator、具体波函数和 paper evidence gate。

## Open Questions

- 是否有一个奇奇或奇-A 核能同时提供四带逐自旋闭合、绝对 `B(M1/E1/E2)`、
  direct E3 和 cross-link 上限？
- `t_chipi` 能否由两种宇称下的手征劈裂差稳定反演，还是会被组态混合和
  分辨率完全遮蔽？
- 对 `M1/E2` 混合线，能否用偏振和角分布确定相消相位，而不是只报告
  `B(M1)`/`B(E2)` 分支？
- 在八极软而非静态 `beta_3` 的体系中，`sigma_cross` 的自旋依赖是否能
  区分双声子核、组态混合和真正的手征—八极耦合？

## Human Review

本页由 Codex 依据 `F01`, `BN96`, `L16`, `GU20`, `TO06` 和 `PE96` source 页
完成 self-audit，`review_status: unreviewed`。未设置 `human-reviewed`，也
没有把 synthetic worker 结果写成实验事实。若后续用于论文主张，应对具体
`D2` 轴约定、混合比相位、绝对寿命和 E3 locator 触发定向审核。

## Promotion or Rejection History

- 2026-10-29：`supports` 以 `D2`/simplex 为基础的四态算符记账和
  `M1/E1/E2/E3` 分层选择规则。
- 2026-10-29：`supports` 用无量纲 Weisskopf 归一化改写
  `B(M1)/B(E1)` 判据，避免把传统磁、电单位的直接比值称为无量纲。
- 2026-10-29：`limits` “近简并 + E1 = 静态手征—八极四重态确证”；
  反证边界来自 `78Br`, `131Ba` 的 quartet/`beta_3` 资格限制和 `134Pr`
  的寿命不对称。
