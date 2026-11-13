---
type: research-note
title: "单 j 半满跃迁、投影矩阵元与开放两态网络：适用边界"
aliases: [A130 seniority projection open network boundaries, T23 T24 物理边界]
created: 2026-11-14
updated: 2026-11-14
status: active
review_status: unreviewed
reasoning_status: provisional
created_from: human-instruction
evidence_sources: [book-jain-nuclear-isomers, doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives]
tags: [seniority, quasispin, angular-momentum-projection, first-forbidden, master-equation, research-audit]
---

# 单 j 半满跃迁、投影矩阵元与开放两态网络：适用边界

## Research Trigger

为 A≈130 博士前置研究稿的附录保留四项可复用边界：单 $j$ 资数选择定则、角动量投影的跃迁矩阵元、一阶禁戒电子能谱和被动两态速率网络。此处不提出新核素数据或寿命预测。下文把**原文直接给出的理论代数**与**本任务的数学推断、有限玩具**分开；二者均不冒充直接实验测量。

## Grounded Evidence

- [[book-jain-nuclear-isomers|Jain、Maheshwari 和 Goel, *Nuclear Isomers: A Primer* (2021)]]：本地原件 `raw/papers/isomer/isomer_review/2021_Jain et al_Nuclear Isomers.pdf`，SHA-256 `994816561cfb6e89bd215b7fe23e37ecf12e8a3e8f5ce88eafbbd388d02ed74a`。Ch. 3，PDF 物理页 50–51（印刷页 39–40），式 (3.8)–(3.10) 为纯配对谱；PDF 页 52–54（印刷页 41–43），式 (3.11)–(3.15)、(3.20) 为准自旋关系；PDF 页 55–56（印刷页 44–45），图 3.3 和式 (3.22) 为奇磁多极与单 $j$ 宇称边界。
- [[doctoral-r1-g34-zhi-2013-prc-shell-model-half-lives|Zhi 等, Phys. Rev. C 87, 025803 (2013)]]：本地原件为预印本 `raw/papers/gpt/query/20261108-foundations-G34/Zhi_2013_PRC_87_025803_SM_halflives_first_forbidden.pdf`，SHA-256 `eaedbd4539854e3d1f0e7860ef7ab9c647d4fa44cd8144b4989ba220ec639333`。PDF 物理页 2 的式 (5)–(7)、页 3 的秩标记说明和式 (8a)–(8d) 给出本笔记使用的形状因子分解及算符定义。

## Provisional Reasoning

### 单 $j$ 半满：偶阶电相消不封闭所有磁跃迁

**原文理论代数。** 在同种费米子的纯单 $j$ 空间，$\Omega=(2j+1)/2$，偶阶 $L>0$ 单体电算符的同资数矩阵元（$v<\Omega$）具有因子 $(\Omega-n)/(\Omega-v)$；只有该资数阶梯实际包含 $n=\Omega$ 时，半满节点才可取。$v=\Omega$ 的分母不能直接使用，应另由准自旋三角条件判断。奇秩单体张量是准自旋标量，保持 $v$，其沿同一准自旋阶梯的同资数矩阵元与 $n$ 无关。单 $j$ 体系内奇阶磁跃迁与同宇称相容；具体矩阵元是否非零仍需角动量及算符条件。上述归约来自 Jain 式 (3.11)–(3.15)、(3.20)、(3.22)，不是实验分支的直接测量。

**本任务推断与有限控制。** 取 $j=11/2$、$\Omega=6$、$n=6$、$v=2$，考察 $J_i=10\to J_f=8$ 的秩 $L=3$ 张量。按下式定义约化矩阵元并取单粒子 $\langle j\|T^{(3)}\|j\rangle=1$：

\[
\langle J_fM_f|T^{(L)}_\mu|J_iM_i\rangle
=(-1)^{J_f-M_f}
\begin{pmatrix}J_f&L&J_i\\-M_f&\mu&M_i\end{pmatrix}
\langle J_f\|T^{(L)}\|J_i\rangle .
\]

准自旋标量使六粒子矩阵元与 $n=v=2$ 参考矩阵元之比为 1；采用相容态相位，相关 6j 非零：

\[
\begin{Bmatrix}11/2&8&11/2\\10&11/2&3\end{Bmatrix}
=\sqrt{\frac{22}{29393}},\qquad
\left|\langle j^6,v=2,8\|T^{(3)}\|j^6,v=2,10\rangle\right|^2
=\frac{264}{247}.
\]

这里 $|10-8|\le3\le10+8$，$M3$ 宇称因子为 $(-1)^{3+1}=+1$。这说明偶阶电矩阵元半满相消不能从代数上排除奇阶磁矩阵元；不意味着任意 $M3$ 都非零。纯单 $j$ 的 $M1\propto\mathbf J$，故不同能级之间的 $M1$ 矩阵元为零；不能将这一 $M1$ 特性推广到所有奇秩。

**能量和实验边界。** Jain 的纯配对哈密顿量 $H_{\rm pair}=-2G S^+S^-$ 本征值仅依赖 $n,v$（式 (3.10)）。故在该纯配对模型中，上例两个 $v=2$ 态简并，均为 $-12G$，不能产生有限光子能量的 $10\to8$ 辐射。若要将非零矩阵元用于形式上开放的跃迁，需另有保持所需纯单 $j$/资数结构的能级分裂，且 $E_{10}>E_8$、实际单粒子 $M3$ 矩阵元非零。本例不标识真实核素，也不计算实际寿命或分支。

## 投影、范数与约化矩阵元

**本任务推断。** 对角动量投影算符 $P^I_{MK}$，构造初末态及其非正交度规：

\[
|\Psi_s^{I_sM_s}\rangle=\sum_{aK}f^{(s)}_{aK}P^{I_s}_{M_sK}|\Phi_a\rangle,\quad
N^I_{aK,bK'}=\langle\Phi_a|P^I_{KK'}|\Phi_b\rangle,\quad
(f^{(s)})^\dagger N^{I_s}f^{(s)}=1.
\]

以 $s=i,f$ 表示始末态，保留非零范数子空间，利用 $(P^I_{MK})^\dagger=P^I_{KM}$，实验室系张量矩阵元为

\[
\langle\Psi_f^{I_fM_f}|T_{L\mu}|\Psi_i^{I_iM_i}\rangle
=\sum_{aK_f,bK_i}f^{(f)*}_{aK_f}f^{(i)}_{bK_i}
\langle\Phi_a|P^{I_f}_{K_fM_f}T_{L\mu}P^{I_i}_{M_iK_i}|\Phi_b\rangle.
\]

选非零 $3j$ 系数，通过上一节给出的 Wigner–Eckart 约定恢复 RME；其相位与归一由该定义确定，无需额外引入统计因子。Haar 测度与投影范数核是不同对象；投影本身也不证明某个绝热近似的小形变发散自动消失。这里采用稿件附录 A 的 Wigner–Eckart 约定与附录 B 的投影定义作为内部约定，而不是独立实验来源。

**有限反例。** 在该 Wigner–Eckart 约定中取 $I_i=1,M_i=0$、$I_f=0,M_f=0$、$L=1,\mu=0$ 且 RME 为 1，则实验室矩阵元为 $-1/\sqrt3$。若把末态 $I_f=0$ 的单个 $D^0_{00}$ 加权旋转平均直接作用到纯初态，积分掉 $J=1$ 态得到零；两个纯态各自的投影范数均为 1。此例验证单个末态权重不能代替双端投影及 Wigner–Eckart 约化。

## 一阶禁戒谱：分秩相加与同秩干涉

**原文理论代数。** Zhi 等式 (5)–(8) 的一阶禁戒形状因子 $C(W)=k+k_aW+k_b/W+k_cW^2$，在所述未极化初态、未观测末态磁子态且轻子角度积分后的电子能谱中，将核总角动量秩 0、1、2 的贡献分块相加。同一秩的多个算符振幅仍可相干：式 (6) 有秩 0 项 $-[\zeta_0w]^{(0)}$，其中式 (7) 的 $\zeta_0=V+wW_0/3$；秩 1 含 $(x+u)^2$ 和 $\zeta_1(x+u)$，式 (8b)、(8c) 将 $x$、$u$ 分别关联到矢量、轴矢量算符。这一结论不排除其他极化或角关联观测量中的跨秩干涉；也不把各秩的模型矩阵元当作实验直接测量。

## 被动两态开放网络

**本任务推断。** 取 $a,b,D_1,D_2\ge0$ 与固定源 $\mathbf S\ge0$：

\[
\dot{\mathbf N}=A\mathbf N+\mathbf S,\quad
A=\begin{pmatrix}-(a+D_1)&b\\a&-(b+D_2)\end{pmatrix},\quad
d=\det(-A)=aD_2+bD_1+D_1D_2.
\]

$d>0$ 当且仅当对任意固定非负源，系统具有唯一非负定态且从任意初始状态全局渐近收敛；等价地，两态各自都能经有向通道到达非零漏失。$d=0$ 并不排除特殊源的有限非负定态：$a=b=0,D_1=1,D_2=0,\mathbf S=(1,0)^T$ 时，$\mathbf N_{\rm ss}=(1,c)^T,\ c\ge0$，故定态存在但不唯一。更一般地，令 $M=-A$；当 $M\ne0$ 且 $d=0$，非负源相容条件是 $\operatorname{adj}(M)\mathbf S=0$；$M=0$ 时则要求 $\mathbf S=0$。

判别式 $\Delta=(a-b+D_1-D_2)^2+4ab$ 为零当且仅当 $ab=0$ 且 $a-b+D_1-D_2=0$，并不限于无交换情形。例如 $a=0,b=1,D_1=2,D_2=1$ 给出

\[
A=\begin{pmatrix}-2&1\\0&-2\end{pmatrix},\qquad
e^{At}=e^{-2t}\begin{pmatrix}1&t\\0&1\end{pmatrix}.
\]

无源、初始布居非负时，正性与 $\frac{d}{dt}(N_1+N_2)=-D_1N_1-D_2N_2\le0$ 给出布居有界；这是被动网络的性质，并非 Jordan 形式一般都保证有界。该公式不声称对有源布居总数非增。

## Falsification or Reverse Tests

本任务的算术和有限基验证可通过 `system/scripts/a130_same_v_m3_open_network_control.py` 与 `system/scripts/a130_projection_ff_rank_control.py` 重现；前者使用 6j 与稀疏 Fock 态验证 $M3$ 及半满偶秩对照，后者使用投影玩具和角动量有限和验证。`system/scripts/a130_seniority_fock_controls.py` 是偶阶对角算符控制，不能单独验证本页的 $M3$ 非对角反例。这些脚本与对应结果只是本任务推导的可重复定位，不是原始实验或独立文献。

**接续摘要：** 以上矩阵元和网络结论已写明条件；把例子用于具体核素前仍须独立核查相互作用、能级顺序与物理跃迁算符。父任务可按所需位置引用本笔记和对应原始来源，不应把纯配对简并的代数例子写成已观测衰变。

## Assumptions

单 j 结论指同种粒子及声明的单体算符；投影态保留非零范数子空间；FF 分秩指未极化、末态磁子态未观测及轻子角积分能谱；网络速率与固定源为非负常数。

## Competing Explanations

真实有限寿命还可来自跨资数、混壳或核芯极化，非零 M3 算符也不等于有限能量辐射。网络无唯一吸引定态与特定源仍有定态不是同一命题。

## Transfer Conditions

迁移资数规则需核对允许占据与实际单粒子矩阵元；迁移投影式需统一 Wigner–Eckart 及范数约定；迁移速率结论需核对状态间通道和漏失可达性。

## Failure Conditions

将多 j 电奇阶相位规则套给纯单 j 磁算符、把 Haar 测度当范数、忽略极化角分辨信息，或把有源网络当被动无源网络，都会越出本页边界。

## Open Questions

用于具体核素的能级分裂、相互作用和环境反应率仍需逐项证据；这些未知参数不影响本页已声明的有限代数结论。

## Human Review

没有新增用户审核事件。总控核验和 Terra 窄审均作为 agent 自审记录。

## Promotion or Rejection History

2026-11-14：T23/T24 推演与实际重放后建立此页；T26 补充阈值宽度的非零领先系数条件，并由总控同步附录和旧笔记。
