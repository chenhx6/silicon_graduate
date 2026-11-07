---
type: observable
title: 内禀电偶极矩（|D_0|）
aliases: [intrinsic electric dipole moment, D0, octupole dipole moment]
created: 2026-11-06
updated: 2026-11-07
status: active
review_status: unreviewed
observable_kind: intrinsic-electromagnetic-moment
symbol: |D_0|
units: e*fm
tags: [octupole, reflection-asymmetry, e1-transition, parity-doublets]
---

# 内禀电偶极矩（Intrinsic Electric Dipole Moment, $|D_0|$）

## Definition

这里的D0是从电偶极跃迁矩阵元、在指定转子约定下提取的内禀参数，单位e·fm。
它描述质子与中子空间分布的相对极化，可能包含宏观和壳结构贡献。
实验直接约束的是跃迁强度/矩阵元；D0的提取另含模型条件。
有限核的宇称本征态与内禀反射不对称图像须区分；此参数也不等于违反
宇称和时间反演的永久实验室电偶极矩。

## How It Is Obtained

同一母态的、已经做效率/角分布等必要修正的**光子**强度满足
\[
\lambda_\gamma(EL)=C_{EL}E_\gamma^{2L+1}B(EL),\qquad
\frac{B(E1)}{B(E2)}
=\frac{C_{E2}}{C_{E1}}
\frac{I_\gamma(E1)}{I_\gamma(E2)}
\frac{E_\gamma(E2)^5}{E_\gamma(E1)^3}.
\]
C系数随所用能量、长度和电荷单位固定；不能遗漏系数，也不能把E1能量写成五次方。
B(E1)/B(E2)的量纲为长度的负二次方，不是无量纲数。刘晨论文
PDF p.78 Eq.(5.1)提供本任务直接使用的E1/E2分支公式入口。

使用真正的光子强度比时，不再额外乘一次内转换系数之比。
若输入是包含转换电子的总分支b，先以b/(1+α)转换为辐射分支；
不同母态之间不能直接消去寿命和布居归一化。混合多极性须先分解。

## Model Dependence

在轴对称强耦合、相同K、相同内禀结构的转子约定中，令
C1=〈Ii K 1 0|If K〉、C2=〈Ii K 2 0|I'f K〉，有
\[
B(E1)=\frac{3}{4\pi}D_0^2 C_1^2,\quad
B(E2)=\frac{5}{16\pi}Q_0^2 C_2^2,\quad
\frac{B(E1)}{B(E2)}=\frac{12}{5}\frac{D_0^2}{Q_0^2}\frac{C_1^2}{C_2^2}.
\]
这是**声明算符归一化之后的模型换算**，不是对三轴核的无条件恒等式。
特别在K=0、E1: I→I−1及E2: I→I−2时，CG因子化简得到
\[
\frac{B(E1)}{B(E2)}
=\frac85\frac{2I-1}{I-1}\frac{D_0^2}{Q_0^2},\quad
|D_0|=|Q_0|\sqrt{\frac58\frac{I-1}{2I-1}\frac{B(E1)}{B(E2)}}.
\]
旧页最后这个K=0结果在该约定下成立，但旧页在未化简CG比前写8/5不成立。
必须知道Q0或绝对B(E1)才能得到绝对D0；相对分支本身不提供它。

100Ru的实际条件重建见[[ru100-e1-moments-and-covariance-round2-20261107]]。
从绝对B(E1)直接提取不需Q0；同母态D0/Q0比值中的共同寿命可消去，
其误差必须保留B(E1)、B(E2)的相关性，不能将边际误差一律独立相加。

## Diagnostic Use

八极振动、静态反射不对称、组态混合和偶极极化均可能影响E1。
不同质量区的质子/中子与壳贡献可以相消，弱E1不自动排除八极集体性，
强E1也不自动证明静态八极。Bucher2017的E1/E3比较是
[[bucher-2017-146ba-direct-octupole]]中的直接核查入口；
不以此页给出未经重新核验的相消百分比。

## Sources

- [[liu-chen-2016-78br-chirality-reflection-symmetry-thesis]] PDF pp.78–80、
  Eqs.(5.1–5.2)、Fig.5.16：分支比、能量位移和八极关联的原始例子。
- [[xiao-2022-chirality-octupole-correlations-74as]] PDF p.7、Fig.7：
  相对强度与稳定八极参照之间的区别。
- CG换算按上述明示的模型定义代数重建，并由本轮独立理论worker交叉核对；
  不能把K=0公式直接用于78Br/74As的三轴多准粒子带。
- P1：实验室直接量、算符约定、Q0/寿命、内转换、混合多极性和系统误差
  必须在具体D0提取时重新核对；不存在通用的0.1–0.3 e·fm“确证门”。

## Failure Modes and Ambiguities

三轴/组态混合、不同母态、未定Q0、内转换和混合多极性均可能使直接套用失效。
分支模方不提供D0符号；相消或振动能破坏D0与静态八极强弱的单调对应。
