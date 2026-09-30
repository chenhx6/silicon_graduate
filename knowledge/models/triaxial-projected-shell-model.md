---
type: model
title: 三轴投影壳模型
aliases: [triaxial projected shell model, TPSM]
created: 2026-07-01
updated: 2026-09-30
status: active
review_status: unreviewed
model_family: projected-shell-model
degrees_of_freedom: [triaxial-quasiparticle-configurations, angular-momentum-projection]
parameters: [epsilon, epsilon-prime, pairing, quadrupole-interaction]
tags: [triaxiality, wobbling, gamma-softness]
---

# 三轴投影壳模型（Triaxial Projected Shell Model）

## Purpose

从三轴准粒子基底进行角动量投影和组态混合，描述能带、signature partner、wobbling 和 γ-soft 特征。

## Hamiltonian or Core Formalism

通常使用 pairing-plus-quadrupole-quadrupole 哈密顿量，并在投影后的多准粒子基底中对角化。

## Degrees of Freedom

三轴平均场、准粒子组态、角动量投影与组态混合。

## Assumptions

结果依赖基底截断和输入形变；从波函数提取经典角动量图像需要额外工具。

## Inputs and Parameters

ε、ε′/γ、配对与相互作用强度。

[[sensharma-2019-two-phonon-wobbling-135pr]] 对 `135Pr` 使用 `ε=0.17, ε'=0.12`（`γ=35°`）。

[[babra-2019-deformation-change-136sm]] 对 `136Sm` 分别使用 `β=0.30, γ=26°` 与 `β=0.22, γ=-25°` 比较带交叉前后的 yrast/γ 带和 `Q_t`。前一平均场较适合低自旋，后一平均场较适合交叉以上；两套输入不是实验直接反演的连续形状轨迹。

## Predicted Observables

能级、B(E2)、B(M1)、signature splitting、wobbling energy 和 SCS 图。

## Strengths

能同时处理芯与价粒子，并可通过组态混合表现 γ-softness。

## Known Limitations

[[frauendorf-2024-wobbling-review]] 指出，虽然模型再现多类数据，如何从截断壳模型结果提炼清晰物理图像仍需发展。

Sensharma 2019 的 TPSM 尚未给出角动量几何分析；它比 QTR 更高估 one-phonon energy，但给出相近的相对 E2 ratios，并更好再现 signature-partner band energy。

Babra 2019 在交叉前后切换固定形变输入；这种比较支持形变变化解释，但不能替代对多极小共存和连续形状演化的动态计算。

[[jahangir-2026-tpsm-gamma-bands-nb-tc]] 提供奇质量 `103,105,107,109Nb` 和 `103,105,107,109Tc` 的 γ1/2γ/γ2/3γ 统一计算案例。对半整数父组态 `K0`，`K0−2` 与 `K0+2` 是不同投影结构；该来源用 `103,105Nb` 第四条观测带的能量、对齐和 `B(E2)` 比较支持 γ2（`K0−2`）解释，但保留其对既有实验标签、Table I 形变和模型截断的依赖，不把 γ2 归类升级为直接实验事实。

[[hara-sun-1995-projected-shell-model-high-spin]] 是 PSM 的历史方法综述，给出变形 Nilsson+BCS 基底、角动量投影、配置混合、Q·Q+配对 Hamiltonian、band-crossing/signature 和 electromagnetic observables 的统一谱系。其 A≈130 Table 5 在 `N=76–78` 的七个核素单元格标为“presumably triaxial”；这属于早期 axial-PSM inference，原文明确说需三轴投影代码确认。

### Bhat et al. 2014: A≈130 odd–odd transfer boundary

[[bhat-2014-tpsm-cs-doublet-bands]] 用三轴 Nilsson+BCS 基底和多准粒子投影计算 `124,126,130,132Cs`。`130Cs` Fig.3 能量比较与 Fig.8 的 `B(M1)/B(E2)` 比值说明 TPSM 可用于邻近 odd–odd A≈130 候选，但 Fig.8 的绝对 `B(E2)`、`B(M1)` 曲线是模型结果，论文没有给 `130Cs` lifetime/绝对强度测量。它不是 `131Ce` 数据，也不检验 Hara–Sun 的 `N=76–78` 候选。Table 1/Eq. (3) 对 `130,132Cs` 的输入映射到 `γ≈42°`，与 PDF p.6 的“约 30°”表述不一致，暂留 `needs_review`，未把计算角度当作实验形状。

[[simons-2005-130cs-chiral-structures]] 是 Bhat 2014 Fig.8 所引 Ref. [32] 的 `130Cs` primary Euroball experiment。它测得能级、DCO/偏振和强度派生 ratios，未给 lifetime/absolute transition strengths；Bhat 是复用该数据的理论比较，不能算第二份实验确认。SIM05 的 `B(M1)/B(E2)` 与 crossing 边界说明，TPSM 相符本身不能消除实验指标内部的限制。

### Hara Table 5 的后续 TPSM 覆盖（2026-09-29）

[[sheikh-jehangir-bhat-2024-tpsm-wobbling]] 对 Table 5 七个星号核素中的 `133La (N=76)` 和 `135Pr (N=76)` 做了后续三轴投影计算。Table 1 采用固定模型输入：`133La` 的 `ε=0.150, ε′=0.110, γ=36°`；`135Pr` 的 `ε=0.160, ε′=0.100, γ=32°`。Figs. 11–14 将计算能级、摇摆频率、对齐角动量和跃迁比与已发表数据比较。该结果将“是否有直接后续 TPSM 应用”从未知修订为至少两例，但不是独立形状测量，也未覆盖 Hara 表中其余五个星号核素；`γ` 参数仍是模型输入。`135Pr` 的 wobbling/TiP 争议见 [[135pr-wobbling-controversy]]。

### Odd-neutron TPSM basis extension and N=77 transfer boundary (2026-09-30)

[[jehangir-2022-odd-neutron-tpsm-extension]] extends the odd-neutron TPSM basis from `1ν` and `1ν+2π` to `3ν` and `3ν+2π` five-quasiparticle configurations, then mixes the angular-momentum-projected states with a Hill–Wheeler generalized eigenproblem (JN22-1, JN22-2). The calculation uses neutron and proton oscillator shells `N=3,4,5`, quadrupole pairing `GQ=0.16 GM`, and effective charges `1.5e/0.5e` for E2 transitions (JN22-3). This supplies a concrete route for modeling additional alignment and high-spin crossings; proton/neutron crossing assignments remain model interpretations rather than direct occupancy measurements.

The same paper states that the quadrupole–quadrupole strength `χ` is related to `ε` through a self-consistent HFB condition (JN22-13). Its tabulated Xe deformations are nevertheless adopted from earlier studies (JN22-4), so this interaction constraint does not turn the shape inputs into a new measurement or an independently established minimum.

For `131Xe`, Table I uses `ε=0.160`, `ε′=0.090`, and `γ=29°`; the deformation values are inherited inputs, not a shape measurement (JN22-4). The yrast spectrum is compared with published levels, while the `131Xe` yrare sequence and its signature behavior remain predictions because that band was not observed in the paper (JN22-5, JN22-6). The projected-state amplitudes in Figs. 8–10 are not ordinary probabilities because the basis is nonorthogonal (JN22-8); a large plotted amplitude alone cannot establish configuration identity. The authors identify g-factor measurements as a useful future discriminator (JN22-10).

`131Xe` is `Z=54, N=77`, so it is an odd-neutron isotone method control for the Hara Table 5 candidates `134La`, `135Ce`, and `136Pr`, not direct model coverage of any of those nuclei. The primary INGA experiment is Banik et al. 2020 ([[banik-2020-131xe-multiple-band-structures]]): it places 72 new transitions and reports relative intensities, `R_DCO` and `Δ_PDCO`, but no lifetimes or absolute `B(E2)/B(M1)` (BNK20-1, BNK20-2, BNK20-5). Its Figs. 17–20 TRS minima are model outputs, not shape measurements (BNK20-6, BNK20-7). Jehangir et al. 2022 Fig. 7 compares with this published data, and Chakraborty et al. 2023 explicitly reanalyze the same Banik data; these are one experimental lineage, not three independent confirmations (JN22-11, JN22-12, BNK20-9). Banik calls B1(a) a signature partner, while C23 says the unfavored partner had not been identified and favors a low-spin yrare-13/2 interpretation; the exact band-label crosswalk remains unresolved within the same acquisition (BNK20-10, C23-6). The 2023 analysis finds M1-dominated links with little E2 admixture and reports no wobbling signal ([[chakraborty-2023-131xe-wobbling-origin]] C23-2, C23-3, C23-7). None of these `131Xe` results transfers to `131Ce` (`N=73`).

## Related Models

[[triaxial-particle-rotor-model]]、[[random-phase-approximation]]

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[frauendorf-2024-wobbling-review]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[babra-2019-deformation-change-136sm]]
- [[jahangir-2026-tpsm-gamma-bands-nb-tc]]
- [[hara-sun-1995-projected-shell-model-high-spin]]
- [[bhat-2014-tpsm-cs-doublet-bands]]
- [[sheikh-jehangir-bhat-2024-tpsm-wobbling]]
- [[jehangir-2022-odd-neutron-tpsm-extension]]
- [[banik-2020-131xe-multiple-band-structures]]

## Evolution Log

- 2026-07-01：建立 `131Xe` 与 wobbling 综述中的用途。
- 2026-07-03：加入 Sensharma 2019 的 `135Pr` TPSM 参数、模型比较与几何分析缺口。
- 2026-07-05：加入 `136Sm` 带交叉前后两套 TPSM 形变输入及其解释边界。
- 2026-09-20：加入奇质量 Nb/Tc γ2（`K0−2`）案例，保留第四带 γ2/3γ/组态混合的实验验证边界。
- 2026-09-30：加入 odd-neutron TPSM 的 3ν/3ν+2π 基底扩展与 `131Xe` N=77 方法控制；标明输入形变、未观测 yrare 预测、非正交振幅和既有实验数据复用边界。
