---
type: method
title: "BM-II 附录 4A：粒子–转子绝热、Coriolis 耦合与有效惯量合同"
aliases: [BM-II particle-rotor appendix, adiabatic particle-rotor, Coriolis recoil contract]
method_type: "particle-rotor-model"
created: 2026-11-03
updated: 2026-11-03
status: active
review_status: unreviewed
scope: "BM-II Vol. II Appendix 4A selected pages and Regge continuation"
confidence: "high for selected equations and stated approximation boundaries"
tags: [bohr-mottelson, particle-rotor, coriolis, recoil, decoupling-parameter, high-spin]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# BM-II 附录 4A：粒子–转子绝热、Coriolis 耦合与有效惯量合同

## Purpose

把 BM-II 的轴对称粒子–转子附录与三轴高自旋、奇 A 摆动代码分开。附录 4A
提供的是奇 A 低能带的轴对称基线、绝热近似和 Coriolis/反冲修正；它不是完整
三轴 QTR、TAC 或 TPSM。

## Inputs and Assumptions

- 转子具有轴对称性，\(R_3=0\)，偶偶核芯转动量子数为 \(R=0,2,4,\ldots\)；
- 轴对称转子哈密顿量为
  \[
  H_{\mathrm{rot}}
  =\frac{\hbar^2}{2\mathcal J_0}(R_1^2+R_2^2)
  =\frac{\hbar^2}{2\mathcal J_0}R^2;
  \]
- 粒子内禀哈密顿量为 \(T+V\)，\(V\) 保持空间反演、时间反演和轴对称
  \(\mathcal R_2(\pi)\) 不变；
- 绝热条件要求转动频率小于不同取向内禀轨道的激发频率；
- 总角动量分解为 \(\mathbf R=\mathbf I-\mathbf j\)，其中 \(\mathbf I\) 作用在
  总体转动波函数，\(\mathbf j\) 作用在内禀变量。

## What It Can Establish

### Coupled Hamiltonian and Coriolis term

BM-II Appendix 4A 的式 (4A-7) 将转子能量写为
\[
H_{\mathrm{rot}}
=\frac{\hbar^2}{2\mathcal J_0}
\left[
I^2+j_1^2+j_2^2-j_3^2
-\left(j_+I_-+j_-I_+\right)
\right].
\]

等价地，式 (4A-8a–c) 分为 \(H=H_0+H_c\)：\(H_0\) 含内禀粒子、轴对称
转子和反冲项，\(H_c\) 含 Coriolis 耦合。\(H_c\) 在 \(K\) 表象中具有
\(\Delta K=\pm1\) 结构，因此会把不同内禀带和转动运动混合起来。

### Adiabatic basis and observables

式 (4A-3) 的内禀波函数 \(\Phi_K(q)\) 以总角动量在对称轴上的分量 \(K\)
标记。对费米子，\(K\) 取半整数；式 (4A-4) 的时间反演/旋转相位关系把
\(\pm K\) 组分联系起来。对称化波函数式 (4A-5) 构成绝热条件下的正交基。

把绝热基变换到弱耦合 \((jR)IM\) 表象后，式 (4A-6) 给出不同核芯转动
\(R=0,2,\ldots\) 分量的权重。这是从内禀组态、转动能带到实验能级和电磁矩阵元
的接口。

### Decoupling and electromagnetic operators

对于 \(K=1/2\) 带，式 (4A-9)–(4A-10) 引入解耦参数
\[
a=-\langle K=\tfrac12 \vert j_+ \vert \overline{K=\tfrac12} \rangle.
\]

式 (4A-11)–(4A-12) 把 M1 算符写成转子、轨道和自旋 \(g\) 因子的组合，并引入
磁解耦参数 \(b\)。因此 \(K=1/2\) 的能级旋称交错和 M1 分支不能只用一个
几何转动惯量解释。

### Nonadiabatic inertia renormalization

对小转动频率，式 (4A-13) 的二阶 \(H_c\) 扰动给出
\[
\delta E^{(2)}_{K I}
=-\sum_\nu
\frac{ \vert \langle \nu I M \vert H_c \vert K I M  \rangle|^2}{E_\nu-E_K}.
\]

式 (4A-14)–(4A-15) 把这项写成转动常数修正 \(\delta A\) 和有效惯量修正
\[
\mathcal J=\mathcal J_0+\delta\mathcal J.
\]

这说明准粒子 Coriolis 耦合可以重整化实验提取的转动惯量；用固定 \(\mathcal J\)
的纯转子或冻结对齐 HFA 拟合数据时，应把这种重整化作为模型不确定度来源。

### Convergence and higher-order terms

BM-II 式 (4A-16)–(4A-17) 说明高阶 Coriolis 项会生成更高次的 \(I\) 依赖：
例如 \(K=3/2\) 可出现三次项，\(K=1/2\) 可出现带旋称因子的高次项。原书用
\[
\delta E^{(n)}
\sim
\frac{\hbar^2j}{\mathcal J_0}
\left(\frac{\hbar j}{\mathcal J_0\omega_{\mathrm{int}}}\right)^{n-1}
I^n
\sim
\hbar\omega_{\mathrm{int}}
\left(\frac{\omega_{\mathrm{rot}}}{\omega_{\mathrm{int}}}\right)^n
\]
估计级数项的尺度，其中 \(\hbar\omega_{\mathrm{int}}\sim E_\nu-E_K\)，
\(\omega_{\mathrm{rot}}\) 是角动量除以转动惯量的频率。

因此，内禀振动谱下的基本绝热条件是
\[
\omega_{\mathrm{rot}}\ll\omega_{\mathrm{int}},
\]
但大 \(j\) 轨道还会引入更严格的收敛要求。原书同时指出，波函数扰动本身不必
非常小，能量和矩阵元级数仍可能因高阶项系统性相消而收敛。

### Effective operators and two-particle caution

式 (4A-21)–(4A-28) 用正则变换
\[
H'=e^{iS}He^{-iS},\qquad
F'=e^{iS}Fe^{-iS}=F+\delta F
\]
把 Coriolis 带混合转移到有效跃迁算符。领先阶
\(\delta F=i[S,F]\)，并可产生 \(\Delta K=0,\pm2\) 的算符修正。

对两个独立粒子，式 (4A-20) 给出反冲项与两次 Coriolis 耦合共同产生的三阶
惯量贡献；原书特别警告，这一般不能简单等同于把两个单粒子惯量修正相加后
直接展开总惯量的倒数。只有自由度可重复、例如振动模的情形，才可以采用这种
简化。

## Regge Continuation

BM-II 印刷 p.198（PDF p.220）说明，图 4-34 中两组轨迹分别对应最低态和最高态
的简化耦合方案。具有相同内禀振动运动、不同 \(I_1\) 的状态落在 \(I_3\)
轨迹上，表现为转动带；\(I_1\) 轨迹则表现为振动序列。两组轨迹各自可以贯穿
整个谱，因此各自完整且互斥，但要完整描述转动关系必须同时使用两组轨迹。

这进一步限制了常见的带标签迁移：

- \(I_3\) 或 \(I_1\) 表象中的轨迹序号不是普遍的实验 \(K\)；
- 高自旋渐近区的 \(n\) 只是在特定极限下描述进动型振动；
- Regge 轨迹、轴对称粒子–转子 \(K\) 带和三轴 wobbling 量子不能直接互换。

## What It Cannot Establish Alone

- 轴对称 Appendix 4A 不能给出三轴静态形变、手征几何或完整 wobbling 模式；
- 绝热粒子–转子能谱不能单独确认实验组态；
- \(K=1/2\) 解耦参数和 Coriolis 旋称交错不能自动等同于三轴 wobbling；
- 二阶惯量重整化的符号和大小依赖内禀激发能、矩阵元和截断；
- \(\omega_{\mathrm{rot}}\ll\omega_{\mathrm{int}}\) 是绝热/摄动展开边界，不是
  一个普适的实验模式判据；
- 有效算符修正和多粒子反冲项不能由单粒子 \(K\) 带公式直接外推；
- 实验使用仍需结合能级身份、分支比、混合比、寿命、偏振、feeding 和替代模型。

## Verification

2026-11-03 直接核验：

- Regge 轨迹图与说明：PDF pp.219–220 / printed pp.197–198；
- 粒子–转子哈密顿量和绝热波函数：PDF pp.221–224 / printed pp.199–202，
  Eqs. (4A-1)–(4A-10)；
- M1 内禀 \(g\) 因子和二阶 Coriolis 惯量重整化：PDF p.225 / printed p.203，
  Eqs. (4A-13)–(4A-15)；
- 高阶项、绝热收敛、反冲修正和 \(K=1/2\) 双重态：PDF pp.226–228 /
  printed pp.204–206, Eqs. (4A-16)–(4A-20)；
- 正则变换和有效跃迁算符重整化：PDF pp.228–230 / printed pp.206–208，
  Eqs. (4A-21)–(4A-32)。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]
- [[wobbling-model-common-input-and-evidence-boundary]]
- [[bm2-asymmetric-rotor-d2-and-transition-contract]]
- [[bm2-nilsson-deformed-shell-model-and-coriolis-alignment-contract]]：Bohr & Mottelson Vol. II 第 5 章 Nilsson 变形单粒子能级、解耦参数与 Stephens 顺排合同。
- [[bm2-rotational-intrinsic-coupling-and-mikhailov-contract]]：Bohr & Mottelson Vol. II §4-4 转动与内禀运动耦合合同（\(\Delta K=2\) Mikhailov 展开与 \(\Delta K=1\) Coriolis 耦合）。
