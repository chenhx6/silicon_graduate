---
type: research-note
title: "102Ru：内禀有效 E1、旋转协变和逐态数据可辨识性"
aliases: [102Ru effective E1 covariant reconstruction, T02]
created: 2026-11-07
updated: 2026-11-07
status: active
review_status: unreviewed
created_from: "T02 conditional tensor derivation and primary-source audit"
promotion_target:
reasoning_status: provisional
evidence_sources: [saracino-2026-102ru-scissors-octupole-resonances, continuation-g15-hamamoto-1989-plb226-dipole-octupole, continuation-g15-hagemann-1993-prc47-octupole-softness]
tags: [102ru, e1, e3, qrpa, rotational-covariance, identifiability]
---

# 102Ru：内禀有效 E1、旋转协变和逐态数据可辨识性

## 范围与原件

**来源直接核对。** Saracino 等，PRL **136**, 252501 (2026)，本地出版 PDF 物理页 1–7，重点 p.4、p.5 Eq.(2)、p.6 和 Figs.3–4；[[saracino-2026-102ru-scissors-octupole-resonances]] 的“SI 未取得”是旧批次状态；本轮总控已同步更新共享source。真实 SI 物理页 1–5：Table I 在 pp.1–3；Hamiltonian Eqs.(1)–(4) 在 p.3；SI Fig.2 和校准在 pp.3–4。两者分别为

- `raw/papers/Low-Energy Dipole Strength Distribution in ¹⁰²Ru Coexistence of Scissors and Octupole Resonances.pdf`，SHA-256 `4bc6bb6c613b121bae9def9d9bedf37e9c02db89eca265c4c16d5dd9ecf43a89`。
- `raw/papers/gpt/query/20261107-continuation-G14/102Ru-PRL-136-252501-Supplemental-Material.pdf`，SHA-256 `8b9fba94fd43ea2af1860029889c0cb3e30ebb3c2cc29a5e0d749649c93a2df0`。
- Hamamoto, Höller, Zhang, PLB **226**, 17–21 (1989)，G15 已登记原件 `raw/papers/gpt/query/20261107-continuation-G15/Hamamoto-1989-PLB-226-17.pdf`，SHA-256 `5b31944f6183f1e66fcd9863d584f7221f52d0cbb18da8d79eaa6d545af30a98`，本次读 pp.17–20，尤其 p.19 Eqs.(2),(3)、Fig.2。
- Hagemann, Hamamoto, Satuła, PRC **47**, 2008–2018 (1993)，`raw/papers/gpt/query/20261107-continuation-G15/Hagemann-1993-PRC-47-2008.pdf`，SHA-256 `cc286cb71fc568db818ff926cfce70e9842af79a1438f9eccd10f4536bb60cb4`；本次重点读 pp.2011–2012 Eqs.(3)–(6)、pp.2013、2018。G14/G15 两个 manifest 的 archive gate 在本次检查通过。G15 所获原件不是 T02 新下载。本笔记没有重转录 SI 表。

以下将**文献陈述**、**条件推导**与**实验可验证性建议**分开。所有页码是出版物页码；SI 页码以 SI 自己的 1–5 为准。结果不是作者代码、QRPA 数值结果或拟合复现。

## 1. SI 哈密顿量实际提供了什么

**来源：SI p.3 Eqs.(1)–(4)。** 按其符号保留标量耦合而不擅改正负号或归一：

\[
\begin{aligned}
H={}&h_{\rm mho}-\boldsymbol\omega\cdot\mathbf J^{\rm IS}
-\tfrac12\kappa_{\rm ISDD}[D^{\rm IS}\otimes D^{\rm IS}]_0
-\tfrac12\kappa_{\rm ISJJ}[J^{\rm IS}\otimes J^{\rm IS}]_0\\
&-\tfrac12\kappa_{\rm IVSS}[S^{\rm IV}\otimes S^{\rm IV}]_0
-\tfrac12\kappa_{\rm IVJJ}[J^{\rm IV}\otimes J^{\rm IV}]_0\\
&-\tfrac12\kappa_{\rm IVDD}[D^{\rm IV}\otimes D^{\rm IV}]_0
-\tfrac12\kappa_{\rm IVOO}[O^{\rm IV}\otimes O^{\rm IV}]_0 .
\end{aligned}
\]

SI 将 IS/IV 的 $D,J,S,O$ 分别称为偶极、总角动量、自旋、八极算符的组合；$[\ ]_0$ 是秩零耦合。写成表格可避免把正文泛称的 multipole 相互作用误读成每一个通道均实现：

| SI 显式通道 | 类型与维数线索 | 原文给出的作用或数值 |
| --- | --- | --- |
| ISDD | 质心平移相关偶极，坐标型 rank 1 | $\kappa_{\rm ISDD}=-10^3\,\mathrm{MeV/fm^2}$，人为将赝平动模推高，PRL p.4 |
| ISJJ | 总角动量 rank 1 | $\kappa_{\rm ISJJ}=-10^3\,\mathrm{MeV}/\hbar^2$，人为将赝转动重定向模推高，PRL p.4 |
| IVSS、IVJJ | 分别为等矢自旋和总角动量 rank 1 | M1 计算取 $-1.0$、$-0.1\,\mathrm{MeV}/\hbar^2$，PRL p.4 |
| IVDD | 等矢偶极 rank 1 | $-1.5\kappa_1^{sc}$，以 $^{100}$Mo IVGDR 峰校准；SI pp.3–4、Fig.2 |
| IVOO | 等矢八极 rank 3 | $4.0\kappa_3^{sc}$，与 $b$ 共同适配累计 E1；PRL p.6、SI Fig.2 |

SI 的式子**没有**显式列出 ISOO、ISSS、IS/IV 四极残余项、配对残余项或单独的 dipole–octupole 交叉项；$h_{\rm mho}$ 和所用 QRPA 的完整内部定义也没有由这四式展开。不能据此断言代码绝无这些处理：这只是已刊表达式的边界。PRL p.4 给 $\varepsilon=0.183,\gamma=0^\circ$、$\Delta_p=1.04$、$\Delta_n=0.97$ MeV；这两个 gap 是实验奇偶质量差的 80%。$-\omega\cdot J$ 是转动坐标系项，其数值在该低自旋 E1 计算中的具体实现未在 SI 明列，不应借高自旋 TAC 曲线倒推出 0。

**stretching/self-consistency 边界。** PRL p.4 说 $\kappa=\eta\kappa^{sc}_\lambda$，$\kappa^{sc}_\lambda$ 从 oscillator model [49] 得到；SI 没有给其显式公式、单/双 stretching 定义、$\omega_x,\omega_y,\omega_z$ 和 $\omega_0$、坐标变换、$r^\lambda Y_{\lambda\mu}$ 具体归一、IS/IV 的系数、模型空间及实际 $\kappa^{sc}_{1,3}$ 数值。常见 $x_i'=\omega_i x_i/\omega_0$ 或 $x_i''=(\omega_i/\omega_0)^2x_i$ 只能作为**命名示例**，不是已核实的该计算定义；更不能凭系数 $-1.5,4.0$ 单独恢复具有单位的矩阵元。SI Fig.2 caption 对 $\kappa_{\rm IVDD}$ 的校准及 $^{100}$Mo/$^{102}$Ru 比较可复核；同一单位约定在 SI 正文一处写有额外 MeV fm$^{-2}$，缺少 $\kappa_1^{sc}$ 的完整定义时不应自行消解。PRC 1993 p.2018 的 double-stretched 比较是**另一篇工作**，不是 2026 实现的证据。

**赝模的具体处理。** PRL p.4 声称两个大负耦合把质心平移和重定向赝模推至高能并有效解耦；这不同于展示真正零能 Goldstone 模、数值正交性、平移不变性或能量加权求和规则。SI 未给赝模频率、残余污染、截断收敛或校验表。非自洽平均场、有限空间、大耦合处理的误差不能从其声明定量。旋转赝模与平动赝模各有对应生成元，不可混成同一个检查。

## 2. 三个来源：裸电荷、状态混合、有效算符

### 2.1 平动不变的裸长波 E1

**本任务推导。** 对 $Z=44,N=58,A=102$，$R_{\rm cm}=A^{-1}\sum_a r_a$，在共同质量近似、忽略有限尺寸和高阶相对论修正下，实坐标的内禀电偶极为

\[
\boldsymbol D=e\sum_{p}(\boldsymbol r_p-\boldsymbol R_{\rm cm})
=e\left({N\over A}\sum_p\boldsymbol r_p-{Z\over A}\sum_n\boldsymbol r_n\right).
\]

标准球谐写法 $\mathcal M_{1\mu}=e\sum_p r_pY_{1\mu}(\hat r_p)-e(Z/A)\sum_a r_aY_{1\mu}(\hat r_a)$，故精确去共同质心时的平动有效电荷为 $e_p=(58/102)e$、$e_n=-(44/102)e$；笛卡尔 $D$ 与球谐 $\mathcal M_1$ 有 $\sqrt{3/(4\pi)}$ 的规范因子。这些是质量相等时的质心修正，不是自动含巨共振屏蔽的经验极化电荷。

**来源与适用条件。** PRL pp.5–6 明确对式(2)两项均用 $e_{\rm eff}^p=e,e_{\rm eff}^n=0$；作者称 IVGDR 屏蔽已通过 IVDD 考虑，并在 p.4 把 IS 赝模推高。若状态及算符无赝模污染，$\langle f|\sum_a r_aY_{1\mu}|0\rangle=0$，裸质子形式的物理跃迁矩阵元可等于上述平动修正形式；这需要条件，而不是由所列电荷本身保证。此等价并不自动推广到 $r^3Y_3$：逐粒子三阶矩对共同平移非不变，平移修正、两体项及其矩阵元要单独建立，不能用一次型 E1 的简单有效电荷公式证明。2026 的 $e_{\rm eff}(d+b o)$ 与 Hamamoto 1989 p.19 Eq.(3) 的 $e_{\rm eff}d+e b_\nu o$、Hagemann 1993 p.2011 Eq.(4) 相比，**八极项的电荷因子有实际差别**：不能直接将旧文献 $b_\nu$ 不作电荷和定义换算搬入 102Ru。旧文献还讨论巨偶极屏蔽，其 $e_{\rm eff}$ 不仅是质心修正（Hamamoto pp.17–18）。

### 2.2 改变 QRPA 本征模与改变探针是两件事

**本任务推导；对应 PRL p.5–6 与 SI p.3。** 在轴对称且宇称良好的四极形变平均场中，$D_{1K}$ 与 $O_{3K}$ 对同一 $K^\pi$ 扰动可耦合同一组两准粒子态。把残余相互作用参数写成 $\kappa_{\rm OO}$，QRPA 响应或本征矢依 $\kappa$ 改变；即使电磁探针保持裸 E1，也可能因为态混合而产生偶极响应。打开 $b$ 则另外改变探针。示意线性响应

\[
\chi_{FF}(\omega)=\chi_{DD}(\omega)+b\chi_{DO}(\omega)+b\chi_{OD}(\omega)+b^2\chi_{OO}(\omega),\quad F=D+bO,
\]

其中每个 $\chi$ 均在**同一个指定 Hamiltonian、同一个 $\kappa$** 下计算；强度取相应虚部及规范因子。线性项是相干交叉响应，不可把单独的 $DD$ 和 $OO$ 强度当成全强度相加。零 $b$、改变 $\kappa$ 与固定 $\kappa$ 改变 $b$ 是两个不同的数值控制；PRL Fig.3 灰线还改变了 $\kappa_{\rm IVOO}$，所以它不是单纯去掉算符第二项的严格控制。该式不替作者补造未发表的响应矩阵。

### 2.3 极化有效算符的模式和能量依赖

**来源：Hamamoto 1989 p.19 Eqs.(2)–(3)、Fig.2；Hagemann 1993 p.2011 Eqs.(3)–(6)。** 两文将内禀分量 $t_\nu=e_{\rm eff}rY_{1\nu}+e b_\nu r^3Y_{3\nu}$ 由 $D^1_{\mu\nu}(\Omega)$ 转到实验室；符号中 $D^1$ 是旋转 Wigner 矩阵而非上面的偶极 $D$。Hamamoto 以粒子–八极振动微扰图给出该结构，并指出其 $^{177}$Hf 实例中跃迁能低于八极模频率，静态极化近似才可接受；$b_0$ 和 $b_{\pm1}$ 载有模频率、集体性和电偶极矩等信息，不是纯几何 CG 系数。Hagemann p.2011 Eq.(5) 更显式地给出：$b_\nu$ 是各同 $K$ RPA 模、同/异种核子耦合、八极矩阵元、E1 矩阵元和模能量的加权和；p.2013 指出质心污染、IS/IV 关联及质子中子径向分布都会影响它。该论文用 $\chi_3(\tau)=\kappa_3+\tau\kappa'_3$ 等旧文献约定；其系数和 2026 的单一 IVOO 参数不应擅自等同。

**本任务条件推导。** 把粒子–声子耦合 $V$ 看作一阶微扰，若 $P$ 是保留空间、$Q=1-P$ 是被消去空间，则任一跃迁 $i\to f$ 的有效算符矩阵元示意为

\[
\langle f|D_{\rm eff}|i\rangle=\langle f|D|i\rangle+
\sum_{n\in Q}\left({\langle f|D|n\rangle\langle n|V|i\rangle\over E_i-E_n}+
{\langle f|V|n\rangle\langle n|D|i\rangle\over E_f-E_n}\right)+O(V^2).
\]

求和上下态、声子归一、复相位和相应时间反向项必须按所选模型确定；这个式子只展示极化来源，不声称它就是作者实现。远离相关中间态的静态极限下，分母才可能被近似为模能量倒数而压缩到近似常数 $b_\nu$。若正在显式求同一能区的八极 QRPA 态，是否对部分关联同时放进本征态和有效算符而重复计数，取决于实际 $P/Q$ 定义、参数拟合和算符推导；现有原文没有给这些匹配信息，既不能断言必然重复计数，也不能宣布已排除。直接把旧文献低能跃迁相对高能声子条件移植到 102Ru 约 5 MeV 目标模，没有依据。

## 3. 旋转协变构造及精确系数

**约定与条件。** 以下取 Condon–Shortley CG、标准 $Y_{\ell m}$、主动旋转球张量 $U(R)T^{(k)}_mU(R)^\dagger=\sum_{m'}T^{(k)}_{m'}D^{(k)}_{m'm}(R)$。令坐标型 $Q_2$ 为偶宇称、电型且时间反演偶，$O_3$ 为奇宇称、电型且时间反演偶，且不同阶张量可以按适当厄米顺序耦合。最低阶例子：

\[
T^{(1)}_M=D^{(1)}_M+c\sum_{m,k}\langle 2m\,3k|1M\rangle Q_{2m}O_{3k}.
\]

CG 正交关系保证整体旋转为 rank 1，宇称 $(-1)^2(-1)^3=-1$；对于坐标构成的电型张量，$\Theta T^{(1)}_M\Theta^{-1}=(-1)^M T^{(1)}_{-M}$（反幺正 $\Theta$ 使复系数共轭）。若 $Q_2,O_3$ 为 Hermitian 且 commute，$[Q_2\otimes O_3]^1$ 本身满足球张量 Hermiticity，因为交换相位 $(-1)^{2+3-1}=+1$；不对易时需用 $(Q\otimes O+O\otimes Q)/2$ 及一致共轭规范。取 $Q_2\sim\sum r^2Y_2$、$O_3\sim\sum r^3Y_3$ 且不含电荷，则 $[Q_2O_3]\sim\mathrm{fm}^5$，为了和 $D\sim e\,\mathrm{fm}$ 相加，$c$ 须为 $e\,\mathrm{fm}^{-4}$；若 $Q_2$ 定义成无量纲形变，$c$ 相应改为 $e\,\mathrm{fm}^{-2}$。不能把这不同定义的系数数值直接比较。

**冻结轴向背景的显式推导（本任务）。** 令 $Q_{2m}=q\delta_{m0}$，$q$ 在内禀坐标中为实常数，令 $O_{3K}$ 使用与 PRL $r^3Y_{3K}$ 同一球谐规范。于是

\[
 t_K=d_K+cq C_K O_{3K},\quad C_K=\langle 2\,0;3\,K|1\,K\rangle,\quad K=0,\pm1.
\]

按标准 CG 的阶乘求和及独立有理数平方验证（脚本见本任务输出）：

\[
 C_0=\frac{3}{\sqrt{35}},\qquad C_{+1}=C_{-1}=\sqrt{\frac6{35}},\qquad
 \frac{b_{+1}}{b_0}=\frac{b_{-1}}{b_0}=\sqrt{\frac23}\simeq0.81649658.
\]

所以在**同一标准 $O_{3K}$、同一单一 $c$、仅线性轴向 $Q_2$ 背景**下，PRL 的 $b_0=b_{\pm1}=0.009\,\mathrm{fm}^{-2}$ 不等于此最简单项的逐分量系数；这是具体受限模型的反例，而不是对所有协变补全的否定。将 $O_{3K}$ 按 $K$ 重新归一化能把这些数吸收到矩阵元定义，但必须同步改算符、模型响应和相位；原文并未列出足以判断其是否如此的实现。

**更一般的明确存在性构造。** 从 $Q_2$ 的二次耦合形成 rank-4 背景 $Q_4=[Q_2\otimes Q_2]^4$，再加入 $c_4[Q_4\otimes O_3]^1$。冻结轴向背景后，将 $q_4$ 吸入 $a_4=c_4q_4$、$a_2=c_2q$：

\[
 b_0=a_2\frac3{\sqrt{35}}-a_4\frac2{\sqrt{21}},\quad
 b_{\pm1}=a_2\sqrt{\frac6{35}}+a_4\frac1{\sqrt{14}}.
\]

只要 $a_4/a_2=(3/\sqrt{35}-\sqrt{6/35})/(2/\sqrt{21}+1/\sqrt{14})\simeq0.13223$，即可在本规范下得到共同非零系数。$Q_4$ 是从同一个 $Q_2$ 构造还是独立背景，只改变吸收进 $a_4$ 的幅度和有效阶数；这一项是可行的**本任务数学补全**，不是声称作者引入或拟合了它。对任意给定参考形变，内禀有效顶角也可含模式、能量和组态依赖，这些都可改变比例。不同旋转相位约定能改分量符号而不改变统一约定下的物理结论；本文 $K$ 比使用明确的球谐规范。

**实验室投影。** 在可用的轴对称转子近似中，可形式地写 $\mathcal T^{(1)}_M=\sum_{K=-1}^1D^1_{MK}(\Omega)t_K$；精确量子计算要包括投影态、K 与 $-K$ 的规范化、对称化及算符在转动自由度上的非对易性。Hamamoto p.19 Eq.(2) 正是这一旋转关系的明确原文，而非对 2026 代码已完整核实。严格角动量态的 $0^+\to1^-$ 对 rank 1 满足三角条件，纯 rank 3 则不满足；[2⊗3] 的**总 rank**为 1。这里冻结背景选定内禀方向，恢复整体旋转时必须同时旋转背景，不能把固定实验室 $q\delta_{m0}$ 当独立 rank 1 张量。

## 4. 从逐态振幅到可辨识性

**来源与数据边界。** SI pp.1–3 Table I 给 $E_i,E_\gamma$、BR、偏振不对称、指定多极性和 $B(E1/M1)\uparrow$，是新增逐态信息；带括号多极性需按原表保留。举两个与边界有关的例子：2953.2(1.9) keV 标作 **(E1)**、$0.016(5)\ e^2\mathrm{fm}^2$、BR=1；5081.22(31) keV 标为 E1、BR=$0.12(11)$、$B(E1)\uparrow=0.05(4)\ e^2\mathrm{fm}^2$。这说明峰及低 BR 支路的误差重要，BR=1 本身不证明完整衰变网络和无未观测分支。表中误差不是已公开的多态协方差、原始计数或完整探测响应。PRL p.4 明确说 QRPA 不逐态一一复现，因此不能机械地把表中第 $i$ 行与计算第 $i$ 根谱线配对；使用固定窗口强度、展宽谱或观测响应前向模型，并保留检测阈值和态指认不确定性。PRL Fig.3 的 $E_\gamma>6$ MeV 计算 E1 缩放 0.17、M1 缩放 0.25；Fig.4 $\Delta=0.6$ MeV，不可遗漏或擅自当探测效率模型。

**本任务推导。** 一旦固定 Hamiltonian、模型空间、态对应和惯例，写

\[
 A_i(b,\kappa)=d_i(\kappa)+b\,o_i(\kappa),\quad B_i=g_i|A_i|^2
 =g_i(|d_i|^2+2b\operatorname{Re}d_i^*o_i+b^2|o_i|^2),
\]

$g_i$ 包括具体 $J_i$、$K$ 重数和算符归一。激发 $0^+\to1^-$ 的约化概率按 $B=|\langle1^-\|\mathcal M(E1)\|0^+\rangle|^2$；反向多一个 $1/3$。实际振幅与响应尚未公开；因态整体相位任意，只有同一态中 $d_i^*o_i$ 的相对相位有干涉意义。改变每个态整体相位不改变 $B_i$。对某个实 $b$、可微的模型，

\[
\partial_b B_i=2g_i\operatorname{Re}(A_i^*o_i),\qquad
\partial_\kappa B_i=2g_i\operatorname{Re}\{A_i^*(\partial_\kappa d_i+b\partial_\kappa o_i)\}.
\]

还须加上能量 $E_i(\kappa)$、窗口响应、效率和缺失态的导数；发生能级交叉时应处理态混合及标签交换。若共同拟合一组观测期望 $\mu(\theta)$（包含展宽谱、线能或外部数据），$J_{ia}=\partial\mu_i/\partial\theta_a$、$\theta=(b,\kappa,\text{nuisance})$；在正定已知误差协方差 $\Sigma$ 的局部高斯近似里，剖除 nuisance 后的有效 Fisher 信息若对 $(b,\kappa)$ 满秩，才具有局部可辨识性的充分正则条件。更一般需要对应完整似然的局部信息；弱奇异值表示约束差而非自动严格不可辨识。实验误差依参数变化、非高斯分支比或选择机制都要求相应修正。

**离散与连续不确定性。** 对单个已知 $d,o$ 且固定 $\kappa$ 的非零 $o$，测量一个 $B$ 只能约束复平面中 $d+b o$ 的模，实 $b$ 可有两个、一个或无实解；多个态且不同相对相位/响应可解除某些分支。若 $d_i,o_i$ 本身完全未知，仅凭 $|d_i+bo_i|^2$ 可把 $b$ 改变吸收入未知 $d_i$，这是**扩大后的不受约束模型**中的显式不可辨识，不代表作者固定 QRPA 模型严格退化。即使局部满秩，$b\to-b$ 在 $d_i=0$ 等极限、不同谱对应或多个非线性极值仍可能产生全局离散多解。逐态数据原则上比单个总和提供更多约束，但表本身没有理论振幅、相对相位、$\partial_\kappa$ 响应或完整 Cov，因此无法据此宣称此模型 $b,\kappa$ 已唯一确定、严格退化或得到相关系数。

**累计相关性。** 对固定顺序、互不重叠的原始区间强度 $y_j$，$C_k=\sum_{j\le k}y_j$、$L_{kj}=\mathbf1(j\le k)$，有精确 $\mathrm{Cov}(C)=L\Sigma_yL^T$。$L$ 的代数定义本身不要求独立；只有原始区间/计数统计确实独立且没有共同系统误差时，才可取 $\Sigma_y=\operatorname{diag}(\sigma_j^2)$ 并写

\[
\mathrm{Cov}(C_k,C_l)=\sum_{j\le\min(k,l)}\sigma_j^2.
\]

即使逐态统计独立，共同通量、效率、branching 和选择/阈值也可使总协方差非对角。未知协方差不能按逐态表的边际误差默认为独立。用同一组 $C$ 和原始 $y$ 同时拟合、或把密集取样的累计曲线当独立测量，会重复计数；对可逆 $L$ 且完整协方差已知，累计并不产生新信息。非重叠区间没有独立原始数据时，保留完整 $\Sigma_y$ 或直接用事件级似然，不能从图中阴影凭空反演。

**可复核的下一步。** 向作者获取每个响应通道复振幅/相对相位或完整复响应函数、能量及 $\kappa$ 扫描，数据的效率/通量/分支协方差、阈值与匹配/展宽规则；分别比较 $b=0$ 但变 $\kappa$、固定 $\kappa$ 改 $b$、共同自由和不含该机制的竞争模型。对统一 observable 与 nuisance 作 profile likelihood 或 posterior、检查局部奇异值、全局多极值和预测未拟合区域；同源 $^{100}$Mo IVGDR 校准及 0.17 处理作为共同依赖显式呈现。没有这些输入不做真实核谱模拟拟合。

## 5. 哪些实验可约束不同解释

**实验设计推断，不是普适阈值。** 对每个同一已确认 $1^-_i$，优先测绝对 $\langle1^-_i\|E1\|0^+_1\rangle$ 的模、寿命与所有可见分支，并补上效率/漏检和相关误差；NRF 给已有 E1 模但不能分解 $d$ 和 $o$。若态混杂，须对同一能级而非仅同能窗建立对应。对实验可达的 $1^-_i\leftrightarrow 2^+_j$ 测 $E1$ 与可能的 $E3$ 多极分量及其相对符号/混合（满足三角和宇称时，具体可测性受 $E_\gamma$、转换及计数限制）；测 $1^-_i\leftrightarrow 3^-_j$ 的 $E2$，以及与可达 $4^+$ 态之间的 $E3$，可直接连接同一 $1^-$ 和四极/八极结构。$0^+_1\leftrightarrow3^-_j$ 的绝对 $E3$ 给八极跃迁强度，但它不是 $0^+_1\to1^-_i$ 的 rank-3 矩阵元：后者被角动量三角条件禁止。四极 $\langle2^+\|E2\|0^+\rangle$ 与适当 $E2/E3$ 网络有助测试两声子/四极–八极耦合；对 2.95 MeV 候选尤其如此，不能只凭一条强 E1 确定组态。

库仑激发的多步路径干涉、带偏振或角关联的多极混合、电子散射纵向形状因子、质子/α 非弹性散射和同位旋选择性探针可在可实现时增加**相对相位、跃迁密度或质子/中子敏感性**；各探针都有反应模型及系统误差，独立性取决于实际数据与分析链。每个单独 $B(E\lambda)$ 只有矩阵元模，不能给绝对相位；在可观测干涉回路中只能确定约定不变的相对符号/相位组合。M1 强度帮助分离磁响应，但不是八极 E3 的直接测量。

应在同一输入与测量响应下对比八极极化、一般低能等矢/皮肤振动、两声子及组态混合等替代解释，检验是否能同时预测未参与调参的同态 E1/E2/E3 分支、能量与其他探针响应。光有显著 $E3$ 或与 E1 同能区增强也不足唯一证明某个有效算符项是原因；仍须同态矩阵元、相位与预测性。对静态八极图像，还需跨自旋绝对多极矩阵元及宇称伙伴、适用的多步不变量，并与软振动、组态混合及投影动力学模型比较；有限核的宇称本征态中奇宇称算符单态对角期望为零，不存在本文声称的普适数值阈值或单一实验确证。

## 未解决问题与停止点

1. SI 不给 $D/O$ 具体拉伸、正负 IS/IV 组合与归一、$\kappa^{sc}$ 数值、模型单粒子截断、响应核、赝模诊断、逐态复振幅或作者代码，故不能唯一重构 Hamiltonian 实现、投影与统计结果。
2. PRL/SI 和 1989/1993 的拟合对象、能区、算符电荷因子不同，旧文静态极化推导不能自动验证 102Ru 的能量无关 $b$。需一致的空间划分以研究可能的双计数。
3. SI 有逐态强度，旧 T01 关于“SI 未可用”的历史条件已关闭；不等于实验事件级协方差及理论态相位已公开。未经响应和误差矩阵，参数精度与独立八极机制均不应声称已定。
4. 最有信息增益的是作者复响应/数值配置和同态 E3/E2/E1 多步测量；当前停止原因是缺少这类输入，而非以共同 $b$ 宣布协变性失败。

## G15原草案的审计与本轮集成记录

以下指 `knowledge/research-notes/continuation-g15-effective-e1-origin-20261107.md` 的原草案。总控已按下列问题收窄该页与两个source；以下保留问题及触发证据的历史，不指称当前页面仍保留这些错误。

1. §3(e) 的“旋转 $D^1$ 恢复等价于 $[Q_2\otimes O_3]^1$”过强。前者是可构造秩1实验室算符的转子表示；后者是协变补全之一，在标准 $O_{3K}$、单一线性轴向背景下给 $b_1/b_0=\sqrt{2/3}$，并非共同 $b$。可用本笔记 §3 的更一般背景示例，但不要归给作者。
2. §3(b)、§4 的“$\gamma\ne0$、所有 $K$ 强混合/全解禁”应改成：轴向 $K$ 不再严格守恒，准许的混合与强弱依对称性和动力学、具体波函数与探针而定；不推出所有分量必显著或所有选择定则消失。同理 $b_0=b_1$ 是所选参数化，不能单凭它证明真实介质各向同性或“完全抹杀”物理。
3. §4 的“$5\,\mathrm{MeV}>2E(3_1^-)$ 因而静态极化必失效”需撤回：与被消去中间态相关的是实际 $P/Q$ 分母和响应频率，$3_1^-$ 不必等于所有有效分母；现有来源不足以定量判定，但也不能自动迁移旧文的静态近似。Hamamoto 1989 p.19 和 Hagemann 1993 p.2017 对各自近似给出各自条件。
4. §3(e)、§5 的 $A\propto b\kappa$、反比补偿及“完全共线/极强相关”均无一般证明：$A=d(\kappa)+b o(\kappa)$，本征能、波函数和干涉项也随 $\kappa$ 变；共同拟合不等于秩缺失，必须用相应复响应、测量协方差及 profile 才能判断。
5. **数值硬错误：** §3(d) 把 Hagemann 1993 p.2017 Eq.(8) 的两个耦合值各写大 $10^2$。出版页直接写 $\bar\kappa_0\simeq3(-1.6\times10^{-5})=-4.8\times10^{-5}$、$\bar\kappa_1\simeq0.2(+7.9\times10^{-5})=+1.58\times10^{-5}\,\mathrm{MeV\,fm^{-6}}$；原式记号为 $\kappa_0,\kappa_1$，不应擅换作 $\kappa^{sc}$。本次检查了该出版页的图像。
6. §3(d) 说 2.95 MeV 强度“严格为零”且作者“明确归属于两声子”不符合 PRL p.6：作者说本计算未再现强孤立态，其“可能”是两声子样态；2.518 MeV 简和与 2.9532 MeV 相差约 0.435 MeV，是否接近属于作者模型性评价。SI p.1 Table I 对 2953.2 keV 多极性标记是 **(E1)**。线性 QRPA 不含显式两声子基底，不等于所有可能的 2.95 MeV 单声子响应被严格禁止。
7. §3(a) “因此必须使用裸电荷”、§3(c) “中子与质子贡献严格反号/所有 $b$ 必然实验标定”、§4 的“同阶量级证明宏观相似”：均需改成指定模型及参数下的陈述。2026 作者采用裸质子电荷并解释其屏蔽处理，不能据此排除平动修正或其他一致的有效算符方案；1993 微观绝对值难估和特定项相消不能证明所有模型必然如此。旧文八极项为 $e b_\nu$，2026 是 $e_{\rm eff}b_\nu$，需保留电荷差。
8. §3(c) 写 $D_0\propto AZe\beta_2\beta_3$ 量纲不闭合：$D_0$ 需要长度因子，且系数依电荷分布、质心约束及所用形变规范。没有重算的系数不得冒称原文公式。§3(b) $K=2,3$ 直接禁戒只在所陈述的轴对称参考态、指定 rank1 直接耦合和良好 $K$ 条件下成立，不排除复合态或其他多极跃迁。


总控在本轮独立执行CG核查脚本，六个系数的符号/有理数平方断言通过；没有真实核谱拟合。


## Research Trigger

内禀有效E1的旋转协变、极化匹配与参数识别性。


## Grounded Evidence

直接证据、实际版本和页码见本页来源段；证据入口为[[saracino-2026-102ru-scissors-octupole-resonances]], [[continuation-g15-hamamoto-1989-plb226-dipole-octupole]], [[continuation-g15-hagemann-1993-prc47-octupole-softness]]。


## Provisional Reasoning

本页比较从原表/算符到条件结论的推断；这些推断与作者实验报告分别标注，不视作新的独立测量。


## Assumptions

采用本页声明的态对应、单位、多极/旋转规范和所用模型范围；未给的联合Cov、原始响应或作者实现不补造。


## Competing Explanations

所选机制须与组态混合、占据变化及实际实验/有效算符依赖比较；与名义数据相容不等于唯一解释。


## Transfer Conditions

迁移到另一核素/核区前，重新核对同态身份、占据/配对、形状动力学和探针算符；仅质量数或名词相同不满足合同。


## Failure Conditions

若原件/态映射/算符规范改变、或必要响应未恢复，重新计算并收窄结论；不得以缺失伴随信号代替有灵敏度的排除。


## Falsification or Reverse Tests

六个CG的符号/平方精确核查；原始表不作无响应逐态拟合。 本页没有未执行的真实核模型排他认证。


## Open Questions

κsc/坐标/基底、复响应和相位、联合实验Cov。


## Human Review

本任务未发生用户逐项审核；记录的是Agent原件自审，未伪装human-reviewed。审核标注不作为检索或使用资格门。


## Promotion or Rejection History

本批根据直接原件与独立核查修订worker草案，撤回无源数值/普适断言；本页保持provisional。具体触发证据和仍存边界见正文，不以结构检查替代物理核验。
