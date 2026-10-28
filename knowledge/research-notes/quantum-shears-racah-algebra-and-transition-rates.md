---
type: research-note
title: "量子剪刀模型的 Racah 重耦合与有限自旋 M1 跃迁"
aliases: [quantum shears Racah algebra, QSM finite-j transition rates]
created: 2026-10-29
updated: 2026-10-29
created_from: Day26 QSM finite-j Racah algebra task
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [clark-2000-shears-mechanism, frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei, rose-brink-1967-phase-defined-angular-distributions, hubel-2005-magnetic-rotation-review]
tags: [quantum-shears, magnetic-rotation, M1, Wigner-Eckart, Racah, 6j, finite-spin]
---

# 量子剪刀模型的 Racah 重耦合与有限自旋 M1 跃迁

## Research Trigger

半经典剪刀图像把质子和中子高-$j$ 角动量当作两根矢量叶片，闭合时横向磁矩减小，因此通常写成 $B(M1)\propto\sin^2\theta$。本轮问题要求在有限 $j$ 的耦合态中把这一图像改写为 Racah 代数的精确矩阵元，并比较 $I=11/2$ 到 $23/2$ 的有限自旋修正。

本笔记的可复现工件是 [Racah 与半经典比较脚本](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/quantum-shears/qsm_racah_vs_semiclassical.py)、[逐点 CSV](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/quantum-shears/qsm_racah_vs_semiclassical.csv) 和 [JSON 结果](../../outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/workers/quantum-shears/qsm_racah_vs_semiclassical.json)。脚本只研究固定 $(j_p,j_n)$ 的两体耦合空间，不拟合任何实测寿命或绝对 $B(M1)$。

有一个必须先处理的角动量加法边界：两个半整数叶片 $j_p=j_n=11/2$ 只能耦合到整数 $I=0,1,\ldots,11$，不能产生半整数 $I=11/2,\ldots,23/2$。因此结果分成两条轨迹：对称的 $j_p=j_n=11/2$ 轨迹使用允许的整数 $I=5,\ldots,11$；用户指定的半整数窗口用 $j_p=11/2,j_n=10$ 作为粒子—空穴式控制，另加 $I=31/2$ 端点行。

## Grounded Evidence

- [Clark–Macchiavelli 综述](../sources/clark-2000-shears-mechanism.md) 的原 PDF p.15、Sec.4.4、Eqs.(5)–(7) 给出剪刀角的有限-$j$ 处方、$B(M1)$ 与横向磁矩的半经典关系，并明确区分两叶片夹角 $\theta$ 与单个叶片相对总自旋的角 $\theta_\pi$。该处是本笔记半经典对照式的直接文献定位。
- [Frauendorf 2001 RMP](../sources/frauendorf-2001-spontaneous-symmetry-breaking-rotating-nuclei.md) 的原 PDF pp.487–488、Sec.IV.A 将磁转动描述为近球形质量分布中的高-$j$ 粒子/空穴电流回路和剪刀闭合；pp.499–502、Sec.VIII 说明 TAC 的半经典取向和实验室系量子化/投影之间的边界。
- [Rose–Brink 1967](../sources/rose-brink-1967-phase-defined-angular-distributions.md) 的原 PDF pp.315–317、Eqs.(3.17)–(3.24) 给出相位一致的球张量与约化矩阵元约定；本笔记采用该类 Wigner–Eckart 约定，整体相位不影响 $B(M1)$。该来源不被冒称为打印了本笔记的特定双角动量闭式。
- [Hübel 2005 综述](../sources/hubel-2005-magnetic-rotation-review.md) pp.4–6、41–44、65–67 将实验剪刀带的判据放在组态、寿命得到的绝对强度、弱 E2 和核芯贡献的联合证据链中；这限制了固定-$j$ 代数结果向具体核素的迁移。

文献直接支持的是半经典几何、磁转动机制和约化矩阵元的规范。下列 6j 阶乘和、有限-$j$ 闭式和数值表是本任务的解析重构与计算结果，不能写成上述综述的原文实验结论。

## Provisional Reasoning

### 1. 算符和约化矩阵元

取可区分的两个角动量

$$\mathbf I=\mathbf j_p+\mathbf j_n,\qquad |(j_pj_n)IM\rangle,$$

并定义

$$\mathbf M(M1)=\sqrt{\frac{3}{4\pi}}\left(g_p\mathbf j_p+g_n\mathbf j_n\right),\qquad \Delta g=g_p-g_n.$$

在不同总 $I$ 的不可约空间之间，$\mathbf I=\mathbf j_p+\mathbf j_n$ 没有跨-$I$ 矩阵元。因此对 $I_f=I-1$，

$$\langle I-1\Vert g_p\mathbf j_p+g_n\mathbf j_n\Vert I\rangle
=\Delta g\,\langle I-1\Vert\mathbf j_p\Vert I\rangle.$$

使用用户指定的相位 convention，Wigner–Eckart 重耦合为

$$
\begin{aligned}
&\langle (j_pj_n)I-1\Vert\mathbf j_p\Vert(j_pj_n)I\rangle\\
&=(-1)^{j_p+j_n+I}\sqrt{(2I+1)(2I-1)}
\sqrt{j_p(j_p+1)(2j_p+1)}
\begin{Bmatrix}
j_p&I-1&j_n\\
I&j_p&1
\end{Bmatrix}.
\end{aligned}
$$

相位可能随 Rose–Brink 或其它约化矩阵元的初末态次序 convention 改变，但强度只含模平方。由 $B(M1;I\to I-1)=|\langle I-1\Vert M1\Vert I\rangle|^2/(2I+1)$ 得

$$
B_q(M1)=\frac{3}{4\pi}\Delta g^2(2I-1)j_p(j_p+1)(2j_p+1)
\begin{Bmatrix}j_p&I-1&j_n\\ I&j_p&1\end{Bmatrix}^{\!2}.
\tag{1}
$$

这正是 6j 符号对有限-$j$ 磁偶极算符的重耦合；“高阶 Racah 算符重整化”在本笔记中仅指这个有限-$j$ 的精确重整化，不指场论意义的重整化。

### 2. 含一个 rank-1 元素的 Racah 闭式

将 Racah 阶乘和用于 Eq.(1) 中的 6j，得到

$$
\left|\langle (j_pj_n)I-1\Vert\mathbf j_p\Vert(j_pj_n)I\rangle\right|^2
=\frac{\left[(j_p+j_n+1)^2-I^2\right]
\left[I^2-(j_p-j_n)^2\right]}{4I}.
\tag{2}
$$

代回 $B$ 定义：

$$
B_q(M1;I\to I-1)=\frac{3}{4\pi}\Delta g^2
\frac{\left[(J+1)^2-I^2\right]\left[I^2-D^2\right]}{4I(2I+1)},
\quad J=j_p+j_n,\ D=j_p-j_n.
\tag{3}
$$

脚本以 Fraction 精确计算四个三角系数和 Racah 阶乘和，并逐点比较 Eq.(2) 左右两侧；本轮全部输出行的最大绝对误差为 $0$（机器表示前的有理数恒等式）。

### 3. 半经典式与内部区精确比值

按本任务指定的叶片长度 $j_p,j_n$，定义

$$\cos\theta_j=\frac{I^2-j_p^2-j_n^2}{2j_pj_n},\qquad
B_{sc}=\frac{3}{8\pi}\Delta g^2\left(\frac{j_pj_n}{I}\right)^2\sin^2\theta_j.
\tag{4}
$$

利用

$$
\left(\frac{j_pj_n}{I}\right)^2\sin^2\theta_j
=\frac{(J^2-I^2)(I^2-D^2)}{4I^2},
$$

在经典内部区（$I<J$ 且 $I>|D|$）可将量子/半经典比值化为无参数的精确表达式：

$$
\frac{B_q}{B_{sc}}
=\frac{2I}{2I+1}\frac{(J+1)^2-I^2}{J^2-I^2}.
\tag{5}
$$

若 $I,J\sim\lambda$ 且远离两个三角形端点，Eq.(5) 给出 $B_q/B_{sc}=1+O(1/\lambda)$。脚本的等长叶片内点 $I=0.8I_{max}$ 比值为

| $j_p=j_n$ | $I$ | $B_q/B_{sc}$ | 相对偏差 |
|---:|---:|---:|---:|
| 5 | 8 | 1.1111 | 11.11% |
| 10 | 16 | 1.0560 | 5.60% |
| 20 | 32 | 1.0281 | 2.81% |
| 40 | 64 | 1.0141 | 1.41% |
| 80 | 128 | 1.0071 | 0.71% |

这支持内部区的渐近收敛，但不支持把收敛率外推到终止端点。

### 4. 数值比较

采用 $\Delta g=1.42$ 作为统一示意值。它不是某个核素的实测有效 $g$ 因子。

对称 $j_p=j_n=11/2$ 的允许整数自旋轨迹：

| $I$ | $2I$ | $B_q$ ($\mu_N^2$) | $B_{sc}$ ($\mu_N^2$) | $B_q/B_{sc}$ |
|---:|---:|---:|---:|---:|
| 5 | 10 | 6.5096 | 5.7766 | 1.1269 |
| 6 | 12 | 5.9987 | 5.1147 | 1.1729 |
| 7 | 14 | 5.3353 | 4.3324 | 1.2315 |
| 8 | 16 | 4.5306 | 3.4298 | 1.3209 |
| 9 | 18 | 3.5913 | 2.4069 | 1.4921 |
| 10 | 20 | 2.5215 | 1.2636 | 1.9955 |
| 11 | 22 | 1.3238 | 0 | 经典端点 |

用户要求的半整数窗口以 $j_p=11/2,j_n=10$ 计算：

| $I$ | $2I$ | $B_q$ ($\mu_N^2$) | $B_{sc}$ ($\mu_N^2$) | 相对偏差 |
|---:|---:|---:|---:|---:|
| 11/2 | 11 | 4.4127 | 4.1773 | 5.63% |
| 13/2 | 13 | 6.6917 | 6.2038 | 7.86% |
| 15/2 | 15 | 7.7984 | 7.0859 | 10.05% |
| 17/2 | 17 | 8.1803 | 7.2757 | 12.43% |
| 19/2 | 19 | 8.0695 | 7.0007 | 15.27% |
| 21/2 | 21 | 7.5958 | 6.3857 | 18.95% |
| 23/2 | 23 | 6.8370 | 5.5036 | 24.23% |

同一控制轨迹的有限-$j$ 端点 $I=31/2$ 给 $B_q=1.7081\,\mu_N^2$ 而 $B_{sc}=0$。一般端点闭式为

$$B_q(I=J)=\frac{3}{4\pi}\Delta g^2\frac{j_pj_n}{j_p+j_n},
\tag{6}
$$

只要 $j_pj_n\Delta g\ne0$ 就不为零。经典端点零值是几何近似的非一致极限，不能当作有限量子空间中的选择定则。相对于内部 $O(j^2)$ 强度，端点残留的相对尺度仍会随大-$j$ 变小，因此这不是说真实剪刀带终止点必然保留该绝对强度。

### 5. 与 Clark–Macchiavelli 角度 convention 的分离

Clark–Macchiavelli Eq.(5) 使用 $\sqrt{j(j+1)}$ 和 $I(I+1)$ 的有限-$j$ 角度处方，而用户给定 Eq.(4) 使用 $j_p,j_n$ 和 $I$。二者在经典大-$j$ 极限一致，但在 $j\sim 11/2$ 时数值不同。脚本额外输出 `BM1_classical_sqrtjj_muN2`，用于审计这一 convention 差异；主表的量子/半经典偏差按用户给定式 Eq.(4) 计算，不能把两种半经典处方混用。

## Assumptions

- $j_p,j_n$ 是可区分的固定角动量；若两叶片来自同种费米子且需要交换反对称化，必须先删去 Pauli 禁态。
- $g_p,g_n$ 是常数有效因子；无核芯角动量、配对、组态混合、两体 M1 算符、带交叉和能量 Hamiltonian。
- $I\to I-1$ 末态存在，且 $I\ge1$；$I=|j_p-j_n|$ 处可能没有同组态的下一级。
- $B(M1)$ 使用 $|\langle I-1\Vert M1\Vert I\rangle|^2/(2I+1)$，磁算符前因子为 $\sqrt{3/(4\pi)}$。
- 半经典式只作为固定叶片长度的几何对照；它不是由量子态期望值唯一推出的实验室系角度测量。

## Competing Explanations

真实核素中的 $B(M1)$ 变化可能来自有效 $g$ 因子淬灭、核芯转动、准粒子重排、配对、组态交叉、带混合或额外两体电磁算符。Clark–Macchiavelli 综述 pp.15–18、23–27 和 Hübel 综述 pp.20–31、43–64 都把这些因素放在实验寿命、$B(E2)$、组态和核芯贡献的联合判据中。因而“量子 6j 结果高于半经典式”只能解释固定-$j$ 基准中的有限自旋重耦合，不能单独说明某一核素的实验偏差。

另一竞争解释是普通核芯转动或 band termination：它们也能给出规则能级和自旋增长。Frauendorf 2001 pp.492–495 将终止解释为角动量逐渐对齐和离散对称性恢复；这与本笔记的两叶片固定空间并非同一个 Hamiltonian。

## Transfer Conditions

将本式用于具体 MR/QSM 候选带，需要同时给出：

- 逐态 $j_p,j_n$ 或微观组态、宇称和 $I$ 的可靠指认；
- 绝对寿命和分支以获得 $B(M1)$，而不是只使用相对 $B(M1)/B(E2)$；
- 有效 $g$ 因子、核芯自旋贡献和可能的组态交叉；
- 选择同一约化矩阵元、相位和 $B$ 归一化 convention。

若只拥有 Garg 2015 的相对跃迁比，现有来源页已标记其为“possible magnetic rotation”且缺少绝对寿命；因此不能用本笔记的固定-$j$ 数值反演 $^{135}$Pr 的实测强度。[Garg 2015 来源页](../sources/garg-2015-135pr-magnetic-rotation.md) pp.6–9 是这一边界的直接入口。

## Failure Conditions

- 输入的 $I$ 不满足 $|j_p-j_n|\le I\le j_p+j_n$ 或整数/半整数加法规则；例如 $j_p=j_n=11/2$ 与半整数 $I$ 窗口不相容。
- 同种费米子交换对称性、芯角动量或多准粒子配置使固定两体积空间不再闭合。
- $g$ 因子随自旋变化或 M1 算符存在两体/芯项；此时 $\mathbf I$ 跨-$I$ 消项仍成立，但 $\Delta g\mathbf j_p$ 的算符分解不再完整。
- 终止点附近使用 $B_q/B_{sc}$ 的内部比值式；其经典分母在 $I=J$ 消失，极限非一致。
- 把 TAC 内禀取向、半经典叶片角或模型计算当作实验室系直接观测量。

## Falsification or Reverse Tests

已执行的反向检验包括：

1. Racah 阶乘和与 Eq.(2) 的有理数恒等式逐点相等，最大误差为 0。
2. $g_p=g_n$ 时 $M1\propto I$，所有跨-$I$ M1 强度严格为零；这检验了总角动量项的消去。
3. $I=J$ 时 Eq.(3) 给有限量子端点，而 Eq.(4) 给零；这是经典端点的明确反例，不是数值舍入。
4. 等长叶片 $j=5,10,20,40,80$ 的内点比值按 $1+O(1/j)$ 收敛到 1。

可反驳本固定模型的直接路线是：在组态、$j_p,j_n$、有效 $g$ 和 $I\to I-1$ 可达性均独立受限的体系中，若绝对寿命给出与 Eq.(3) 不相容的强度，则必须引入芯、混合或算符修正；若仍坚持纯两体模型，则该数据反驳模型。单独测得经典几何端点附近的零强度不能反驳量子模型，因为它可能来自 $\Delta g$、组态混合或实验灵敏度，而非 6j 恒等式。

## Open Questions

- 如何把可测静态磁矩、带内寿命和微观组态同时用于约束 $g$ 淬灭、核芯转动和 6j 重耦合的相对贡献？
- 在 3qp$\to$5qp 交叉附近，是否需要把两个固定-$j$ Racah 扇区做相干带混合，才能描述 $B(M1)$ 的反弹？
- 在粒子—转子或 PNC/TAC 模型中，哪类两体 M1 算符修正会首先破坏 Eq.(3) 的单一 $\Delta g$ 结构？
- 对 $j_p=j_n=11/2$ 的整数-$I$ 轨迹，能否用带终止附近的绝对寿命和磁矩判断有限-$j$ 端点残留，而不把它误认作普通芯转动？

## Human Review

本笔记及其计算结果是 Codex 的解析和数值 self-audit，`review_status: unreviewed`。文献页仍按原页面状态管理；本笔记没有把 review 页的背景内容升级为人工确认，也没有把计算值升级为实验事实。需要论文级使用时，应逐条回到原 PDF 的 Sec.4.4、页码和方程，并确认算符与初末态 convention。

## Promotion or Rejection History

- 2026-10-29：建立 provisional 研究笔记；新增精确 Fraction Racah 阶乘和、半整数角动量加法边界、$I=11/2$–$23/2$ 控制轨迹和内部比值 Eq.(5)。
- 2026-10-29：保留“有限-$j$ 端点经典零值非一致”作为模型结果；拒绝将其写成所有真实 MR 带终止态的普适实验结论。
- 待人工定向复核：用户给出的半经典式与 Clark–Macchiavelli Eq.(5) 的 $j$ 对 $\sqrt{j(j+1)}$ convention；若论文级引用，需补查用户点名的 Macchiavelli et al. 1998 PRC 原件并记录其精确页码/方程。
