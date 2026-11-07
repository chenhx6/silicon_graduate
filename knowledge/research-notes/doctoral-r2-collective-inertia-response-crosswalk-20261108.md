---
type: research-note
title: "博士前置 R2：形状坐标、集体惯量与响应的比较合同"
aliases: [collective inertia response crosswalk, 惯量与响应比较]
created: 2026-11-08
updated: 2026-11-08
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [prochniak-rohozinski-2009-bohr-collective-hamiltonian, hinohara-2010-local-qrpa-shape-mixing, sato-hinohara-2011-krypton-shape-mixing, hinohara-2015-nambu-goldstone-inertia-response, petrik-kortelainen-2018-rotational-tv-inertia, afanasjev-abusara-2010-time-odd-rotating-systems, xiang-2024-triaxial-pairing-collective-hamiltonian, washiyama-2024-five-dimensional-improved-inertia, sun-2025-iterative-atdhfb-rare-earth-inertia, matsuzaki-2004-nuclear-inertia-and-wobbling]
created_from: "博士论文前置研究；auto与brainstorm的有界理论比较"
promotion_target: ""
tags: [doctoral-foundations, collective-inertia, linear-response, pairing, identifiability]
---

# 同一幅形状图为什么还没有决定核怎样运动

## Research Trigger

R1 已比较六区的电荷形状与谱学案例，本轮补上其中的动力学环节。
长期复用价值在于：论文和模型讨论中常把名称都含“惯量”的量互相代入，
使一个本来有条件的解释变成看似直接的实验结论。
本页首先确定比较所需的合同；实际核的数值结论回到 source，而非本页的推导示例。

## Grounded Evidence

| evidence | source / locator | provenance | limitation |
|---|---|---|---|
| 势、惯量、测度与电磁算符需分别指定 | [[prochniak-rohozinski-2009-bohr-collective-hamiltonian]], Secs. 3.1, 4.1–4.3；PDF pp. 13–16, 27–35 | 综述中的理论结构 | 不等于所有实核已有唯一确定的输入 |
| 诱导场与冻结场在响应方程中不同 | 同来源 Eqs. (4.8), (4.11), (4.21)–(4.25) | ATDHFB 近似的明确区分 | 不能用固定倍数概括所有坐标和组态 |
| 六个 B 函数不是同一个常数，也不是三条实际转动惯量本身 | 同来源 Eqs. (3.5)–(3.8), Figs. 5–6 | 190Os 的特定 SLy4/HF+BCS 计算 | 不是从数据直接反演得到的张量 |
| 能量加权强度引入逆惯量的期望 | 同来源 Eqs. (3.64)–(3.67) | 集体空间的双对易子恒等式 | 需要探针—坐标映射与足够闭合 |

## Provisional Reasoning

### 先写动能，才能比较符号

在所选的慢集体坐标 \(q^a\) 中，定义

\[
T=\frac12 M_{ab}(q)\dot q^a\dot q^b .
\]

\(M\) 随坐标变换而变。若 \(q=q(Q)\)，

\[
M^{(Q)}_{ij}
=\frac{\partial q^a}{\partial Q^i}
 M^{(q)}_{ab}
 \frac{\partial q^b}{\partial Q^j}.
\]

这是本任务由二次动能直接推得的变换关系，不是新物理。
若 q 是长度平方单位的四极矩，M 的单位含其平方的倒数；
若改为无量纲 β，数值及单位均须相应变换。
只有在共同坐标、能量与 \(\hbar\) 约定下，两个“质量参数”才可比较。

对本篇综述的 β、γ 约定，振动块为

\[
T_{\rm vib}=\tfrac12\left[
B_{\beta\beta}\dot\beta^2+
2\beta B_{\beta\gamma}\dot\beta\dot\gamma+
\beta^2 B_{\gamma\gamma}\dot\gamma^2\right].
\]

因此坐标质量矩阵的 γγ 元为 \(\beta^2B_{\gamma\gamma}\)，
不是图上单独的 \(B_{\gamma\gamma}\)。
转动块则是 \(\tfrac12\sum_k{\cal J}_k\omega_k^2\)，
\({\cal J}_k=4B_k\beta^2\sin^2\gamma_k\)。
写出这些几何因子能防止将两幅同单位等高线直接当作同一个物理量。

### 静态能量与运动响应提供不同信息

约束静态参考态给出势能函数及其局部曲率。
慢运动还会诱导密度和场的变化。ATDHFB 一阶方程中的
\([\mathcal W_1,\mathcal R_0]\) 正是被冻结场近似舍去的部分。
它在静态时间反演不变参考态上的平均值可以消失，却仍进入运动时的响应。
“静态未出现”不能推出“对集体动力学没有贡献”。

如果改变配对强度，准粒子能量、相干因子、参考态族、势能与残余响应均可能变化。
把某段能量改善全部叫作“惯量修正”，需要额外的共同输入控制。
同样，固定同一势面只改变惯量是有效的模型敏感性试验；
它本身没有证明实核中确有一个能独立作此变化的微观机制。

[[afanasjev-abusara-2010-time-odd-rotating-systems]] 的有限转动 NM/WNM
比较保留 Coriolis 诱导电流，只关闭所声明的空间矢量场并重新自洽求解。
因此该差值不是独立实验分离出的纯时间奇项，也不等于直接测得的 M1 强度。
它与零频 FAM 比较不同，进一步说明参考态、频率和干预对象必须明定。

### 三个不同的比较，不能共享一个“必然增大”

下面是本任务的局部响应推导，适用于正定二次型，不冒充实核 QRPA 计算。
令

\[
E(x,z;f)=\tfrac12 x^TAx+x^TCz+\tfrac12 z^TBz-fp^Tx ,
\qquad
\begin{pmatrix}A&C\\C^T&B\end{pmatrix}>0 .
\]

冻结 \(z=0\) 时，\(\chi_{\rm frozen}=p^TA^{-1}p\)。
释放 z 并令其平衡，得到

\[
A_{\rm eff}=A-CB^{-1}C^T,\qquad
\chi_{\rm relaxed}=p^TA_{\rm eff}^{-1}p
\geq\chi_{\rm frozen}.
\]

不等式的条件是**同一个正定二次型、同一外场、只释放先前冻结的自由度**。
它不保证把独立准粒子响应的 A 换成含残余作用的 A′ 时也同向变化；
后者可以增加或减少该方向的刚度。
更不能据此把零频响应与有限转动频率下的谱线导数当作相等。

这个区别使“自洽放松应增大响应”和“所有 TV 惯量必大于 IB”
不再被错误地当作同一句话。若要把前一个数学不等式用于具体模型，
须列出冻结/释放的变量、外场、稳定性及两种计算是否真的共享其余曲率。

### 对低能谱的缩放不能替代机制归因

在单个近谐坐标、固定曲率 C 和局部常数 M 的极限，
\(\omega^2=C/M\)。它说明能谱同时需要势的曲率与惯量，
不是“较低的 γ 激发能必意味着势更软”的充分判据。
存在大振幅形状混合、坐标依赖质量、交叉项和不同零点修正时，
必须求解相应 Hamiltonian；不能把该单模公式当作整个六区的定量标度律。

### 五种容易混用的量

| 对象 | 明确的定义/探针 | 数值单位约定 | 不能自动替代 |
|---|---|---|---|
| 形状坐标质量 \(M_{ab}\) | \(\frac12 M_{ab}\dot q^a\dot q^b\) | \(\hbar^2/(\mathrm{MeV}\,q^a q^b)\) | 静态势曲率或电荷形状矩 |
| 空间零频 TV 惯量 | 对 \(H-\omega J_k\) 的自洽局部响应 | \(\hbar^2/\mathrm{MeV}\) | 任意有限自旋区间的带内差分 |
| 沿带 \(J^{(1)},J^{(2)}\) | 同一有序能带的频率/有限差分 | \(\hbar^2/\mathrm{MeV}\) | 无额外模型限制的全部横向响应 |
| 摆动有效横向惯量 | RPA 色散式中 \({\cal J}_{y,z}^{\rm eff}(\omega_{\rm wob})\) | \(\hbar^2/\mathrm{MeV}\) | 三个与频率无关的核芯常数 |
| 配对规范转动惯量 | \(\partial N/\partial\lambda\) 或局部粒子数能面曲率 | \(\mathrm{MeV}^{-1}\) | 配对幅度质量、BCS gap 或空间转动惯量 |

定义来源分别为 PR09 的动能，
[[petrik-kortelainen-2018-rotational-tv-inertia]] Eq. (18)、
[[moments-of-inertia]] 的声明差分、
[[matsuzaki-2004-nuclear-inertia-and-wobbling]] Eqs. (11)–(12)、
[[hinohara-2015-nambu-goldstone-inertia-response]] 的局部配对转动。
“转动”二字没有将最后一行变成前三行。

Hinohara2010、Sato2011、Washiyama2024 的 D 已吸收几何因子，
\(D_{\beta\gamma}=\beta B_{\beta\gamma}\)、
\(D_{\gamma\gamma}=\beta^2B_{\gamma\gamma}\)，均回各自 Eq. (2) 核对。
β 无量纲，γ 采用弧度；自然单位下常写 MeV⁻¹，
恢复物理时间则为 \(\hbar^2/\mathrm{MeV}\)。
不能因记号不同再多乘一次 β。

令 \(j=J/\hbar,\ h=\hbar\omega\)，
\({\cal I}=\hbar^2\partial\langle j\rangle/\partial h\)。
在明定反对称准粒子对矩阵元的约定下，任务静态变分给

\[
\chi^{\rm IB}_{FF}
=2\sum_{\mu<\nu}\frac{|F_{\mu\nu}^{20}|^2}{E_\mu+E_\nu}
=\sum_{\mu,\nu}\frac{|F_{\mu\nu}^{20}|^2}{E_\mu+E_\nu}.
\]

全单粒子 uv 式要先转换到同一 \(F^{20}\)，不能看见双重求和就盲加 2。
实 QRPA 的相关可逆子空间中，实/纯虚矩阵元分别涉及
\(2r^T(A+B)^{-1}r\)、\(2v^T(A-B)^{-1}v\)；
外场用 \(H+\eta F\) 时实静态 S 的符号反向。
原件为 Hinohara2015 APS Eqs. (22)–(23), (49)–(51)；
不把所有 NG 动量一律归到 A+B。复矩阵或时间反演破缺时用完整响应。

配对规范角在 QRPA 中是关于破缺参考态的局部共轭生成元，
不是在完整有限核 Hilbert 空间存在全局自伴角算符的证明。
离散质量差分、固定数投影与连续 HFB 延拓也不自动等价。
Hinohara2015 的出版修订、混合数曲率和真实 Lu 表的名义重算
见 [[doctoral-r2-inertia-evidence-and-band-reconstruction-20261108]]。

## Assumptions

- 每次比较先定义坐标、参考态、约束、外场、算符、\(\hbar\) 和求和范围。
- 基于偶偶时间反演/D₂ 参考态的分块，与有限转动、阻塞或倾斜轴参考态分别讨论。
- 与能谱对应的量子势不自动等于未经零点修正的约束平均场势。
- 配对幅度、配对规范角和空间取向是不同坐标；任何消去都需有时间尺度依据。

## Competing Explanations

低能谱相似可以来自势、惯量、配对、组态混合、有效算符或态对应的不同组合。
不能仅凭共同拟合宣称严格参数退化。
同一寿命产生的多个 B 值、同一能带的相邻差分或同一质量表的配对差分，
也不自动成为相互独立的实验约束。

## Transfer Conditions

从 A≈80 形状混合向 A≈130 软核或 A≈190 过渡核迁移时，先比较：
集体空间是否含相同自由度；壳占据与配对是否相似；时间尺度分离是否成立；
惯量与势是否用同一参考态族；探针是否测到所比较的响应。
质量数和平均 γ 只能帮助选择案例，不能替这些条件作决定。

## Failure Conditions

只有能谱、没有统一算符或状态映射时，不作唯一机制识别。
把 β 或 γ 改名但没有转换质量/测度，比较即失败。
若两套响应计算改变了不同相互作用或组态，结果只能列为模型差异，
不能将差值归因一个时间奇项。

## Falsification or Reverse Tests

对“惯量主导”的候选，固定完整输入合同，保留一组未拟合的谱间距、绝对 E2、
静态矩、E0、转移或磁观测；实际选择依据具体核与响应灵敏度。
先让最强替代模型作同样预测。若预测区间重叠、或关键探针映射不明，
则记录不可区分而不是命名新模式。

## Open Questions

哪些真实核的公开响应张量与电磁矩阵元足以完成共同输入比较？
有限频率响应与静态质量的差别，何时已经大到需要放弃绝热单模语言？
这些问题由本批原作应用继续检验，不从上面的二次型证明推出实核结论。

## Human Review

- Review scope: 用户授权自主研究和目标约束；未发生逐项用户科学审核。
- Decision: 概念比较与候选合同保持 provisional；推导的适用条件明确列出。
- Complete unresolved P0/P1 inventory: 坐标、QRPA 实/虚分块、几何因子、
  NG/配对与空间响应已回原作及 APS 版本交叉核验；
  二次型只证明其自身比较关系。出版式内部差异和混合数曲率边界保留，
  没有原生产代码，不能裁决其数值原因。Lu 的 20 行实际表已核，
  名义重算通过量子转子极限与独立标号算术，不产生实验误差条。

## Promotion or Rejection History

| Date | event | previous state | new state | reason / triggering evidence | target or successor |
|---|---|---|---|---|---|
| 2026-11-08 | 建立响应定义与比较合同 | R1后续问题 | provisional | 原件区分坐标质量、诱导场及不同量子化路线；补入有条件的响应推导 | doctoral-nuclear-structure-foundations |
