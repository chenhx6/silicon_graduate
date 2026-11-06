---
type: concept
title: "Gamma-vibrational band mixing, Mikhailov z_gamma parameter and Alaga rule corrections"
aliases: [gamma-band-mixing, mikhailov-z-gamma, alaga-rule-corrections, rotational-vibrational-coupling]
created: 2026-11-03
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
tags: [collective-model, gamma-vibrations, alaga-rules, mikhailov-parameter, band-mixing, clebsch-gordan, gamma-softness, triaxiality]
---

# γ 振动带混合、Mikhailov 参数与 Alaga 强度比

## Definition

本页使用 [[book-bohr-mottelson-nuclear-structure-vol2]] BM2-5、BM2-12，§4-4，PDF181／printed159 Eqs.4-230–4-231 与 PDF183／printed161 Eqs.4-232–4-235。完整换算与限制见 [[bm2-rotational-intrinsic-coupling-and-mikhailov-contract]]。

\[
B_{if}=2M_1^2 C_{if}^2(1+a_2\Delta_{fi})^2,\quad
 a_2=-M_2/M_1,\quad z_2=2a_2/(1-4a_2).
\]
`gamma_band_mixing_z_gamma_alaga_inverter.py` 的旧 `z_gamma` 是 \(a_2\)，合法但不同于书中的 \(z_2\) 和波函数混合系数 \(\epsilon_2\)。\(a_2,z_2,\epsilon_2\) 均无量纲，不能因此混用。

## Necessary Assumptions

使用上述弱混合有效强度关系、纯E2约化强度比与一致相位约定；代数实根不自动满足弱混合适用域。

## Discriminating Observables

从 CG 平方 \(1/5,2/7,1/70\) 推得
\[
R_{02}=0.7(1-6a_2)^2,\quad R_{42}=0.05(1+14a_2)^2.
\]
对有限 \(R_{02}\ge0\)，令 \(q=\sqrt{R_{02}/0.7}\)，两分支 \(a_{2,s}=(1-sq)/6\)，\(s=\pm1\)；零比值时合并。零混合正演给 \(0.7,0.05\)，但 \(R_{02}=0.7\) 还允许 \(a_2=1/3\)。旧 scalar 默认显示正平方根分支；`branches` 给全部候选及对应 \(z_2\) 与 \(R_{42}\)，不自动按“小根”认定物理机制。反演代数可解不等于弱混合条件已验证。

纯 E2 光子强度比需先去掉光子能量五次方因子，并处理效率、混合比和内转换；不能把未修正光子比当 \(B\) 比。预测的 \(2_\gamma\to4_g\) 强度在能量允许时才对应实际退激。

## Counter-evidence and Competing Interpretations

书中 \(c(I)=\epsilon_2\sqrt{2(I-1)I(I+1)(I+2)}\)、\(h_2=\epsilon_2\Delta E\)。\(h_2\) 随 \(\Delta E\) 使用 keV，但该能隙和一条强度比不能确定 \(\epsilon_2\)。撤回 \(h_2=a_2\Delta E/\sqrt6\)；旧耦合字段返回 `null`，结构归属为未确定。

PDF173／printed151 与 PDF184／printed162 保留不同耦合贡献及不同内禀四极矩的限制。刚性三轴转子、振动混合、组态混合及数据修正问题须由更多独立观测量区分；本页不再声称 Mikhailov 展开普遍等价于某一模型的小 γ 极限，也不借未经核查的 IBM 选择定则裁决机制。

## Our Current Position

旧 Er/Sm/Ba presets 没有在本次建立逐线原始来源，保留名称和输入仅作数值 fixture；旧实验误差、\(h_2\) 数字、形状阈值与“普遍压低”说法撤回。模块 112 / `zgamma` 旧名称继续可读；只有限定的强度参数反演及分支预测得到本次验证。


## Supporting Evidence

原书只支持已定位的条件强度关系；标准CG平方和正反映射在本轮专用测试中独立核对。测试通过不建立实际核素的耦合或形状。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：BM2-5、BM2-12。
- [[bm2-rotational-intrinsic-coupling-and-mikhailov-contract]]：参数定义、分支与来源边界。
