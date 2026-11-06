---
type: concept
title: "Davydov-Rostovsky non-adiabatic triaxial rotor beta- and gamma-band mixing, Mikhailov expansion and Alaga rule deviation"
aliases: [davydov-rostovsky-model, triaxial-band-mixing, z-gamma-mixing, mikhailov-expansion, alaga-rule-deviation]
created: 2026-11-04
updated: 2026-11-06
status: ai-draft
review_status: unreviewed
tags: [triaxiality, non-adiabatic-rotor, band-mixing, alaga-rule, davydov-rostovsky, mikhailov-expansion, 152sm]
---

# Davydov–Rostovsky 旧接口与 Mikhailov 带混合参数化边界

## Definition

当前 `davydov_rostovsky_triaxial_band_mixing_solver.py` / `rostovsky` 保留历史名称以兼容调用。它没有求解 Davydov–Rostovsky 哈密顿量，也没有由本次原文建立其 β–γ 三带动力学归属；旧波函数与机制宣称撤回，不新增模型补足。

本次依据 [[book-bohr-mottelson-nuclear-structure-vol2]] BM2-5、BM2-12：§4-4 PDF181／printed159 Eqs.4-230–4-231；PDF183／printed161 Eqs.4-232–4-235。推导详见 [[bm2-rotational-intrinsic-coupling-and-mikhailov-contract]]。

旧参数记为 \(t\)，有
\[
R_{02}=0.7\left(\frac{1-2t}{1+t}\right)^2.
\]
令有符号因子 \((1-2t)/(1+t)=1-6a_2\)，得到
\[
a_2=\frac{t}{2(1+t)},\quad t=\frac{2a_2}{1-2a_2},\quad
z_2=\frac{2a_2}{1-4a_2}=\frac{t}{1-t}.
\]
所以旧参数化可保留，但 \(t\ne a_2\ne z_2\)，也不是 \(\epsilon_2\) 或波函数混合振幅。有限 \(t=-1\) 不允许；\(a_2=1/2\) 对应 \(t\) 坐标无穷，仍须保留该 \(a_2\) 分支；\(a_2=1/4\) 对应 \(z_2\) 无穷。

## Necessary Assumptions

输入须为有限、非负的E2强度比，并遵守同一振幅约定；实际应用还要求弱混合有效关系成立。

## Discriminating Observables

对 \(q=\sqrt{R/0.7}\)、\(s=\pm1\)，
\[
a_{2,s}=(1-sq)/6,\quad t_s=(1-sq)/(2+sq).
\]
全部有限非负比值都保留实解；\(R=0\) 合根；\(R=2.8,s=-1\) 时 \(t\) 无穷，由有限 \(a_2=1/2\) 表示。`null` 加坐标状态区分极点与丢解。负值或非有限值拒绝，撤回旧正值截断。默认旧标量函数返回 \(+\sqrt{}\) 分支，完整结果提供 `branches`，不作物理选根。

由同一 BM-II 强度合同推得
\[
R_{42}=0.05(1+14a_2)^2
=0.05\left(\frac{1+8t}{1+t}\right)^2.
\]
旧 \(1+4t\) 是换参不一致，已修正；零混合时 \(R_{02}=0.7,R_{42}=0.05\)。所有结果仍须检查弱混合适用性、多极性和能量可达性。

## Counter-evidence and Competing Interpretations

\(h_2=\epsilon_2\Delta E\)，但本次无法从 \(t\) 确定 \(\epsilon_2\)，故旧 `coupling_matrix_element_h2_keV` 为 `null`。旧 \([E(2_g)/E(0_\beta)]^{1/4}\) 仅在 `legacy_energy_ratio_fourth_root` 留作无量纲数值代理；原文未建立其动态软度归属，旧 `non_adiabatic_softness_mu` 为 `null`。不以它或一个分支比指认 γ-softness、刚性三轴或某类耦合。

## Our Current Position

`PRESETS` 的旧名称、函数参数及 CLI 入口保留；Sm/Ba 数值仅为未核验 fixture，不是 BM-II 或实验基准。能量旧字段 `experimental_energies_keV` 仅为兼容键名，实际来源由 `energy_provenance` 明示。PDF173／printed151 和 PDF184／printed162 的机制退化与内禀矩限制仍保留；多自旋 E2、绝对矩阵元与独立动力学信息不足时，不宣称机制已识别。


## Supporting Evidence

严格换参建立两种既有比值表达的代数联系；专用测试独立核对CG、零混合、双分支和坐标极点。它没有验证Davydov–Rostovsky动力学或预设的实验身份。

## Sources

- [[book-bohr-mottelson-nuclear-structure-vol2]]：BM2-5、BM2-12和所列原页。
- [[bm2-rotational-intrinsic-coupling-and-mikhailov-contract]]：统一的参数映射及限制。
