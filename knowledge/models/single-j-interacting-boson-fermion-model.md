---
type: model
title: "单j IBFM：固定玻色子数与同波函数电磁算符"
aliases: [single-j IBFM executable contract]
created: 2026-11-06
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
model_family: interacting-boson-fermion
degrees_of_freedom: [s-d-bosons, single-j-fermion]
parameters: [boson-number, single-j, epsilon-d, kappa, chi, occupation, quadrupole-coupling, exchange-coupling, monopole-coupling]
evidence_sources: [nomura-2017-odd-mass-gamma-soft-shape-transitions]
tags: [ibfm, gamma-softness, a130, operator-contract, reproducibility]
---

# 单j核芯—费米子参考模型

## Purpose

提供与刚性转子不同的软核芯比较。对应
`system/scripts/analysis/single_j_ibfm.py`，不称PBOS复制品或原作者执行输入。
129Ba输入与结果见[[ba129-core-and-pairing-validity]]。

## Hamiltonian or Core Formalism

固定\(N_B\)个s、d玻色子及一个半整数j费米子：
\[
H_B=\epsilon_d n_d+\kappa Q_\chi\cdot Q_\chi,\quad
Q_\chi=s^\dagger\widetilde d+d^\dagger s+\chi[d^\dagger\widetilde d]^{(2)}.
\]
Q·Q保留普通乘积的单体收缩，不另除以N_B。
HBF按Nomura2017 Eqs.3–6，限制\(j=j'=j''\)：
\[
\Gamma_{jj}=\Gamma_0(1-2v^2)Q_{jj},\quad
\Lambda^j_{jj}=-2\Lambda_0\sqrt{\frac5{2j+1}}(2uvQ_{jj})^2,\quad
A_j=-A_0\sqrt{2j+1}.
\]
交换项的冒号保留费米正规排序的负号并去掉收缩。采用
\(\widetilde a_{jm}=(-1)^{j-m}a_{j,-m}\)后，
\([a^\dagger\widetilde a]^{(0)}=-n_f/\sqrt{2j+1}\)，
所以NF=1的单极项恰为\(A_0n_d\)。单j单粒子能只产生共同平移。

## Assumptions

玻色子数、核芯身份和有符号\(Q_{jj}=\langle j\Vert Y_2\Vert j\rangle\)
均由调用者明定。h11/2在本CS约定下
\(Q_{hh}=-\sqrt{525/(143\pi)}\)；该角向量不再乘任意径向r²。
真实核芯、占据和被排除轨道仍属于模型近似。
模型内固定NF/NB不等于已经执行完整核子的数目投影或严格微观Pauli处理。

## Predicted Observables

完整固定M能谱、J²分类、E2/M1矩阵元及强度。算符是
\[
T(E2)=e_B Q_{\chi'}-
\frac{e_F(1-2v^2)Q_{jj}}{\sqrt5}[a^\dagger\widetilde a]^{(2)},
\]
\[
\mu=g_B L+g_j j,\qquad T(M1)=\sqrt{3/(4\pi)}\,\mu.
\]
χ′与Hamiltonian χ独立；M1不乘E2的\(1-2v^2\)。
各算符使用同一本征矢相位；\(B=|\mathrm{RME}|^2/(2J_i+1)\)。
磁矩与标准M1张量分别返回。不同J跃迁中\(g_BJ\)项为零，可将剩余共同
\(g_j-g_B\)尺度单独定标。

## Numerical Contract

玻色子模式次序为\(s,d_{-2},d_{-1},d_0,d_1,d_2\)，归一化占据态；
完整算符稀疏存储，仅固定M块转为稠密。NB=8、j=11/2时完整空间15444，
M=1/2块965；核芯M=0块105。能量简并子空间用J²解析，再检查H/J²残差。
不以事后对称化掩盖非Hermitian误差，不把接近整数的J²均值单独当好J。

同M、q=0约化矩阵元要求非零CG分母；允许但零CG的情况报错或显式NaN，
不假装为选择定则零。不同M独立求解的相位不自动衔接。

## Known Limitations

无多j、显式质中玻色子区分、配置混合或完整转移算符；同E、同J的严格简并
内部基仍非唯一。占据来自外部均场，不由该单j核解BCS。
核芯B(E2)定eB、外核Q定eF或光子比定磁尺度时，所用量属于标定。
原文未给每核eB/gB及完整输入文件，数值重建应保留该边界。

25项解析/合成检查包括O(6)、旁观者多重态、独立Fock空间交换正规排序、
张量代数和归一。它们验证所写数学对象，不证明某核的物理机制或文章新颖性。

## 完整电荷矩与受限通道接口

`quadrupole_scalar_invariants.py`可对同一Spectrum执行五分量直接收缩和
全允许自旋的带符号6j闭合；`ba_quadrupole_closure_study.py`在冻结五Ba输入上
连接偶芯B(E2)电荷标定。J+2受限求和保留完整磁子多重态，仍为旋转标量，
但通常不同于完整电荷多项式矩。某个通道中增加态数不恢复其它自旋的贡献。
实质超过反余弦定义域的比值保留原值，角度返回undefined。

具体参数、通道强度、三次矩相消及35个算符/标定敏感性设置见
[[odd-ba-quadrupole-closure-and-spin-channel-redistribution]]。这条模型研究
不声称复制Nomura2017电磁不变量图，也不以能量子集一致认证其原算符生产链。

## Sources

- [[nomura-2017-odd-mass-gamma-soft-shape-transitions]]：pp.2–5，Eqs.1–11与TablesI–V。
- [[ba129-core-and-pairing-validity]]：128Ba/NB8的来源支持及实际129Ba检验。
