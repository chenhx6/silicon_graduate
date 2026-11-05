---
type: model
title: "单j配对转子：正能BCS投影与算符合同"
aliases: [paired single-j positive BCS rotor, single-j rotor executable contract]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
model_family: core-particle-coupling
degrees_of_freedom: [single-j-quasiparticle, fixed-triaxial-core]
parameters: [field-strength, gamma, principal-moments-of-inertia, fermi-level, fixed-pairing-gap]
evidence_sources: [meyer-ter-vehn-1975-triaxial-rotor-particle-model, gizon-1977-ba129-angular-distribution-primary]
tags: [triaxiality, prm, bcs, operator-contract, model-validation]
---

# 单j正能BCS转子的可重放定义

## Purpose

为能谱、转移与电磁分支使用同一组波函数提供一个显式参考模型。
它属于[[triaxial-particle-rotor-model]]的一个受限实现；
方程一致性与物理适用性分别检验，不自动给出wobbling或signature标签。
实际129Ba比较见[[ba129-model-input-and-holdout-contract]]。

## Assumptions

固定形状核芯、完整单j一准粒子空间、严格正的固定配对隙及主轴惯量。
正能BCS块保留全部取向混合而舍去准粒子/准空穴非对角耦合。
核芯、粒子电磁项和转移算符必须分别定义；能谱定标不同时定标所有算符。

## Predicted Observables

给定参数下的各I本征能、core-E2与particle-j约化矩阵元、unit-B，以及
声明偶芯R=0真空到I=j的裸加/移除强度。相对光子率还需能量因子和
共同物理算符尺度；绝对B、实验δ符号或结构模式不由裸unit-B自动给出。

## Hamiltonian or Core Formalism

本任务选择的无量纲单j四极场是
\[
Q_j=\frac{\cos\gamma[3j_3^2-j(j+1)]
 +\sqrt3\sin\gamma(j_1^2-j_2^2)}{4j(j+1)},\qquad h_{\rm sp}=C Q_j.
\]
\(C\)包含符号及全部强度；不能不经转换就把它等同原文的\(Y_{2\mu}\)
场系数、β或Nilsson参数。能量用MeV，角动量用\(\hbar\)，
\(\mathcal J_k\)用\(\hbar^2/\mathrm{MeV}\)。主轴按输入顺序保留，不排序。

令\(\epsilon_\nu\)为单粒子本征值，
\[
E_\nu=\sqrt{(\epsilon_\nu-\lambda_F)^2+\Delta^2},\quad
u_\nu^2=\tfrac12[1+(\epsilon_\nu-\lambda_F)/E_\nu],\quad
v_\nu^2=1-u_\nu^2.
\]
取正平方根，要求\(\Delta>0\)。U、V、E是在完整单j空间中的矩阵函数。
指定的正能投影近似为
\[
H_R=\sum_k\frac{(I_k-j_k)^2}{2\mathcal J_k},\qquad
H_+=U H_R U+V H_R V+E.
\]
体坐标总I采用异常对易关系，粒子j采用通常对易关系；二者的矩阵不能
不加区分地使用同一套\(y\)分量。D₂投影保留半整数总自旋与完整粒子取向。

[[meyer-ter-vehn-1975-triaxial-rotor-particle-model]] Eqs.2.25–2.33
区分完整准粒子/准空穴耦合和舍弃\(h\eta\)后的近似。
本实现采用后一类正能块，不声称对角化了完整Nambu哈密顿量。
λ和Δ是输入，未解粒子数/能隙方程；没有blocking自洽或额外轨道。

## Operator Conventions

旋转基为归一化\(D^{I*}_{MK}\)，CG使用Condon–Shortley相位，
\[
\langle I_fM_f|T_{L\mu}|I_iM_i\rangle
=\frac{\langle I_iM_i,L\mu|I_fM_f\rangle}{\sqrt{2I_f+1}}
\langle I_f\Vert T_L\Vert I_i\rangle.
\]
集体四极张量的内禀分量为\(q_{20}=\cos\gamma\)、
\(q_{2,\pm2}=\sin\gamma/\sqrt2\)，作用于粒子空间的单位阵。
particle-j算符为标准秩1球张量。两者在本time-reversed-hole规范中均为
\(\operatorname{diag}(T,T)\)；其正能投影是
\(X_f^\dagger\operatorname{diag}(T,T)X_i\)，不可把time-even单粒子
电算符的minus coherence factor借给集体核芯算符。

矩阵行是末态，列是初态，\(B_{\rm unit}=|\mathrm{RME}|^2/(2I_i+1)\)。
物理Q₀、有效电荷、g因子及率常数须另给。particle-j只是
\(g_R I+(g_j-g_R)j\)中的一项；对不同总I的跃迁，I生成元项为零；
对角磁矩仍需\(g_R\sqrt{I(I+1)(2I+1)}\)项。
代码不猜测实验δ的辐射相位。

裸转移限定一个声明的偶芯R=0态：最终I=j，在积基中
\(v_{K\Omega}=\delta_{K\Omega}/\sqrt{2j+1}\)。对X的particle/hole块分别
投影得到加/移除振幅；完整保留谱满足
\(\sum S_{\rm add}=\sum u_\nu^2,\ \sum S_{\rm rem}=\sum v_\nu^2\)。
这是明定算符的求和规则，不是转移强度等于组态混合概率的规则。

## Symmetry and Tests

在本轴规范中，\(\gamma\to60^\circ-\gamma,\lambda_F\to-\lambda_F,
\mathcal J_2\leftrightarrow\mathcal J_3\)给能谱对偶。
源论文Eqs.2.11–2.22、2.40–2.51已讨论相应等谱和有符号EM关系；
原轴置换须转换到本规范。B值相等不能推得有符号δ或四极矩相等。
裸转移的加/移除强度在对偶间互换。

实现与必要验证：

- `system/scripts/analysis/paired_single_j_rotor.py`：自由转子谱、D₂、
  Nambu投影、场的独立角积分、参数对偶与输入边界；
- `system/scripts/analysis/paired_single_j_em.py`：独立最高权/降阶CG、
  R=0→2分辨强度与闭合、particle-j守恒spectator R、Hermitian reciprocity、
  相位不变性与选择定则；
- `system/scripts/analysis/paired_single_j_transfer.py`：完整加/移除求和、
  自由转子只到R=0、对偶互换、态重相位与最终自旋限制。

2026-11-05分别实际通过24、19、5项数学/数值检查。它们不认证核素适用、
原作者程序复现、固定算符的实验充分性或文章新颖性。

## Known Limitations

若低能空间含显著其它j、核芯软度、多准粒子或被舍弃的\(h\eta\)耦合，
应评估或扩展模型。即使能量RMS小，EM矩阵元的相消仍可使预测敏感。
可直接重建舍弃块\(P^\dagger(-U H_RV+V H_RU)P\)及逐态耦合范数，
结合互补块的谱间距检查近似；块范数不能直接当作能量修正。
129Ba自由C能量极小点附近已有约1-MeV的耦合范数，近似误差尚无小量保证，
详见对应研究笔记的条件结果。
拟合后调整态对应、g/Q比例或γ来追保留数据，必须登记为新标定，
不得继续称同一数据为盲检验。

同一套奇核能量参数不自动定义真实邻偶核的配对真空。
转移比较需独立说明偶芯波函数、占据、有效算符、反应归一及态匹配；
本裸算符不替代[[bucurescu-1998-129ba-neutron-pickup-ibfm]]的映射算符。

## Sources

- [[meyer-ter-vehn-1975-triaxial-rotor-particle-model]]：printed pp.113–121，
  Eqs.2.6–2.51，空间、Nambu近似、对偶和算符先例。
- [[gizon-1977-ba129-angular-distribution-primary]]：pp.473–475，Fig.4及
  历史129Ba参数与电磁符合边界；本实现不冒称该原程序的精确重放。
- [[bucurescu-1998-129ba-neutron-pickup-ibfm]]：pp.652–659，转移算符、
  多轨道空间及与γ谱的观测互补性。
