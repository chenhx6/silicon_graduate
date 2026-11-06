---
type: method
title: "Bohr & Mottelson Vol. II：转动与内禀运动耦合、Coriolis 带混合与 Mikhailov 展开合同"
aliases: [BM2 rotational intrinsic coupling, BM2 Section 4-4 band mixing, Mikhailov formula E2, delta K=2 gamma-ground mixing, Coriolis delta K=1 Inglis cranking]
method_type: "rotational-intrinsic-coupling-contract"
created: 2026-11-03
updated: 2026-11-06
status: active
review_status: unreviewed
scope: "Bohr & Mottelson Nuclear Structure Vol. II, Section 4-4 (printed pp.145-174 / PDF pp.167-196)"
confidence: "conditional BM-II strength algebra; mechanism and coupling not identified"
tags: [bohr-mottelson, vol2, band-mixing, coriolis-coupling, mikhailov-formula, gamma-vibration, alaga-deviation, inglis-cranking, 166er, 175lu]
sources: [book-bohr-mottelson-nuclear-structure-vol2]
---

# Bohr–Mottelson II：转动–内禀耦合与 Mikhailov 强度合同

## Purpose

在明确的弱混合有效强度关系下，建立参数映射、比值反演及其可识别性边界。

依据 [[book-bohr-mottelson-nuclear-structure-vol2]] BM2-5、BM2-12：§4-4，PDF181／printed159，Eqs.4-230–4-231；PDF183／printed161，Eqs.4-232–4-235。PDF173／printed151，Eq.4-211 后文提醒不同耦合可给出相同自旋依赖；PDF184／printed162 保留不同内禀四极矩等限制。以下参数换算和分支比是从这些已核定义进行的本次代数推导。

弱混合有效 E2 强度关系为
\[
B_{if}=2M_1^2 C_{if}^2(1+a_2\Delta_{fi})^2,\quad
C_{if}=\langle I_i\,2\,2\,-2\mid I_f\,0\rangle,\quad
\Delta_{fi}=I_f(I_f+1)-I_i(I_i+1),\quad a_2=-M_2/M_1.
\]
这里是强度式，不能漏掉标准约化矩阵元与 \(B=|\langle f\Vert\mathcal M\Vert i\rangle|^2/(2I_i+1)\) 的归一关系，或将 \(M_1+M_2\Delta\) 无条件代入同一符号约定。\(M_1,M_2\) 是有效电四极矩阵元，单位相同；\(a_2,z_2,\epsilon_2\) 均无量纲，但物理意义不同。

## Inputs and Assumptions

以下换参要求使用同一有符号振幅约定，输入为E2约化强度比。

### 两个旧接口的严格映射

令第一份脚本的旧 `z_gamma` 为 \(u\)，第二份的旧 `z_gamma` 为 \(t\)。第一份使用 \(1+u\Delta\)，故 \(u=a_2\)。第二份用
\[
R_{02}=\frac7{10}\left(\frac{1-2t}{1+t}\right)^2.
\]
比较**有符号振幅**，选取连接零混合的同一约定，要求
\[
1-6a_2=\frac{1-2t}{1+t}
\quad\Longrightarrow\quad
 a_2=\frac{t}{2(1+t)},\quad t=\frac{2a_2}{1-2a_2}.
\]
这只建立代数重参数化，不证明第二份实现来自 Davydov–Rostovsky 动力学。BM-II 另定义
\[
z_2=\frac{2a_2}{1-4a_2},\quad
 a_2=\frac{z_2}{2(1+2z_2)},\quad
 z_2=\frac{t}{1-t},\quad t=\frac{z_2}{1+z_2}.
\]
有限坐标排除各自分母为零；\(a_2=1/4\) 是 \(z_2\) 无穷而非物理解消失，\(a_2=1/2\) 是 \(t\) 无穷。有限 \(t=-1\) 不定义原比值；有限 \(z_2=-1/2\) 不对应有限 \(a_2\)。接口用 `null` 加 `coordinate: infinite` 保留坐标极点的分支，并仍输出有限 \(a_2\) 与强度预测。

## What It Can Establish

\(I_i=2\) 到 \(I_f=0,2,4\) 的 CG 平方依次为 \(1/5,2/7,1/70\)，故
\[
R_{02}=\frac7{10}(1-6a_2)^2
=\frac7{10}\left(\frac{1-z_2}{1+2z_2}\right)^2,
\]
\[
R_{42}=\frac1{20}(1+14a_2)^2
=\frac1{20}\left(\frac{1+8t}{1+t}\right)^2
=\frac1{20}\left(\frac{1+9z_2}{1+2z_2}\right)^2.
\]
旧第二份脚本的 \(1+4t\) 不满足该映射，已更正。对有限 \(R\ge0\)，令 \(q=\sqrt{R/(7/10)}\)，全部实解为
\[
a_{2,s}=\frac{1-sq}{6},\qquad
 t_s=\frac{1-sq}{2+sq},\qquad
 z_{2,s}=\frac{1-sq}{1+2sq},\quad s=\pm1.
\]
\(R=0\) 两根合并；\(R=7/10\) 同时有 \(a_2=0\) 与 \(1/3\)，不能仅凭比值宣布零混合。较大根可能不满足弱混合条件，但不得静默删根或声称它已满足模型适用域。负值、NaN、无穷输入拒绝，不截断为正值。零混合正演回到 \(R_{02}=0.7,R_{42}=0.05\)。

## What It Cannot Establish Alone

原书弱 \(\Delta K=2\) 解释中的波函数振幅及耦合能为
\[
c(I)=\epsilon_2\sqrt{2(I-1)I(I+1)(I+2)},\qquad h_2=\epsilon_2\Delta E.
\]
\(c(I)\) 无量纲，若 \(\Delta E\) 用 keV，\(h_2\) 才为 keV；例如 \(c(2)=\sqrt{48}\epsilon_2\)。\(a_2\) 是电磁有效参数，既非 \(c(2)\) 也非 \(\epsilon_2\)。从 \(a_2\) 到 \(\epsilon_2\) 需要特定耦合解释、相位与内禀矩的附加关系；本次没有足够原文输入建立该关系，撤回旧 \(h_2=z_\gamma\Delta E/\sqrt6\)、简单 \(M_2=\epsilon_2\sqrt{5/(16\pi)}eQ_0\) 等未核换算。

输入必须为 E2 的约化强度比。纯 E2 同母态光子强度比还需除以 \((E_{\gamma0}/E_{\gamma2})^5\)，并处理效率、多极混合、内转换和不确定度。\(2_\gamma\to4_g\) 只有能量允许时才是实际退激分支，否则只是矩阵元强度预测。弱混合要求混合振幅小、相关能隙不近简并，不能用固定自旋阈值替代。

一条强度比既丢失振幅符号，又不能确定耦合机制、\(h_2\)、刚性或 γ-softness；偏离也不必总是压低。需多自旋、多个绝对 E2 矩阵元、相位约束及独立动力学证据。既有带核素名的 presets 仅为未核验数值 fixtures，撤回旧 Er/Ba 数值的实验归属、误差和普适阈值，也撤回“完美再现全部高自旋”的断言。旧方法页其它规范变换／Inglis 系数和机制推演不在本次核验范围，故不再以本页作为其已完成严格推导的证明；相关问题可回到 [[bm2-particle-rotor-adiabatic-coriolis-contract]]，本次不扩展调查。

## Implementation and Compatibility

`gamma_band_mixing_z_gamma_alaga_inverter.py` 保留旧标量键，意义明确为 \(a_2\)；`davydov_rostovsky_triaxial_band_mixing_solver.py` 的旧标量仍为 \(t\)。标量按 \(+\sqrt{}\) 分支惯例输出，不作为物理选根。两者均输出 `branches`；耦合能和结构无法识别的旧字段保留为 `null` 或未确定说明，不继续提供伪数值。


## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：BM2-5、BM2-12及本页所列精确原文定位。
- 两个本地反演模块和专用测试：验证此处的条件代数与接口，不能作为独立实验来源。
