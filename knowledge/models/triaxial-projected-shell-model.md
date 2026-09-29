---
type: model
title: 三轴投影壳模型
aliases: [triaxial projected shell model, TPSM]
created: 2026-07-01
updated: 2026-09-29
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

## Evolution Log

- 2026-07-01：建立 `131Xe` 与 wobbling 综述中的用途。
- 2026-07-03：加入 Sensharma 2019 的 `135Pr` TPSM 参数、模型比较与几何分析缺口。
- 2026-07-05：加入 `136Sm` 带交叉前后两套 TPSM 形变输入及其解释边界。
- 2026-09-20：加入奇质量 Nb/Tc γ2（`K0−2`）案例，保留第四带 γ2/3γ/组态混合的实验验证边界。
