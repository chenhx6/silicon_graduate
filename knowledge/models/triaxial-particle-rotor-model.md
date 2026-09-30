---
type: model
title: 三轴粒子-转子模型
aliases: [triaxial particle rotor model, TPRM, quasiparticle triaxial rotor, QTR]
created: 2026-07-01
updated: 2026-09-30
status: active
review_status: unreviewed
model_family: core-particle-coupling
degrees_of_freedom: [triaxial-rotor, quasiparticle]
parameters: [epsilon2, gamma, moments-of-inertia, pairing, coriolis-attenuation]
tags: [triaxiality, odd-a, wobbling]
---

# 三轴粒子-转子模型（Triaxial Particle-Rotor Model）

## Purpose

描述奇 A 核中准粒子与三轴偶偶芯的耦合、signature splitting 和 wobbling 候选结构。

## Hamiltonian or Core Formalism

`H=H_core+H_sp+H_pair`；芯项按三个主轴的转动惯量写成 `Σ A_k(I_k-j_k)^2`。

## Degrees of Freedom

三轴芯转动、单粒子轨道、配对和 Coriolis 耦合。

## Assumptions

芯形变与转动惯量作为输入；模型参数可通过能级拟合调整。

[[lawrie-2020-tilted-precession-wobbling]] 区分完整 QTR/particle-rotor-type 3D solutions 与 wobbling approximation：前者在该文术语中产生 [[tilted-precession-bands]]，后者只有在两个非主转轴的 angular-momentum components 可视为小量、`f(n,I)<<1` 时，才能写成 principal-axis rotation 与 harmonic wobbling phonons 的耦合。

## Inputs and Parameters

- [[chakraborty-2023-131xe-wobbling-origin]] 最终采用 `ε2=0.13, γ=33°, ξ=1` 描述 `131Xe`；
- [[petrache-2020-137nd-multiple-chiral-bands]] 为 `137Nd` D2/D3 与 D5/D6 分别采用约 `(β,γ)=(0.20,20.9°)`、`(0.21,23.5°)`；
- [[budaca-budaca-2025-harmonic-chiral-vibration]] 将 constrained PRM 的平面经典能面在 stationary point 附近作 harmonic expansion，以 `ΔE(I)=ω_I` 拟合 chiral-partner splitting。对 `137Nd` D5/D6 的输入几何为 `j=11/2,j′=10`，输出 `γ=97.5°`（按该文 `120°−γ` sector mapping 为 `22.5°`）；这些 ΔE 数据沿用 Petrache 2020 Ref. [30]，并非独立 shape measurement。
- [[budaca-budaca-2025-harmonic-chiral-vibration]] 从约束 PRM classical-energy surface 推导 harmonic chiral-vibration frequency；对 `137Nd` D5/D6 (`πh11/2²⊗νh11/2⁻¹`) 以实验 `ΔE(I)` 拟合 paper-sector `γ=97.5°`，在该文 `120°−γ` 映射下为 `22.5°`。Fig.4 的 `137Nd` split 来自 Petrache 2020 Ref. [30] 的同一实验，只有少量拟合点且未对 `137Nd` 做 transition-ratio comparison；这不是独立形状或实验确认。
- [[ding-2021-131ba-133ce-signature-splitting]] 用 γ=15° 和 10° 分别描述 `131Ba`、`133Ce` 的 S(I)，并扫描 Coriolis attenuation。
- [[matta-2015-transverse-wobbling-135pr]] 的修改 QTR 用 `J_m,J_s,J_l=7.4,5.6,1.8 ħ²/MeV`、`c=0.116` 拟合 `135Pr` zero-/one-phonon 能量。
- [[sensharma-2019-two-phonon-wobbling-135pr]] 沿用 `135Pr` 的 `ε=0.16, γ=26°`、上述三个转动惯量和尺度因子，扩展比较逐级 wobbling-phonon energy 与相对 E2 ratios。
- [[guo-2022-low-spin-wobbling-187au]] 使用 `ε2=0.21, γ=12°`、Harris parameters `J0=25 ħ² MeV^-1, J1=8 ħ⁴ MeV^-3`、irrotational-flow-like γ dependence，并纳入 proton Fermi level 附近 9 个负宇称轨道。
- [[lv-2021-tilted-precession-135nd]] 对 `135Nd` 使用 `β=0.19, γ=25°`、Harris `J0=5 ħ² MeV^-1, J1=71.4 ħ⁴ MeV^-3`、Coriolis attenuation 0.7、`g_s=0.6g_free`、`g_R=0.44` 与 neutron Fermi level 附近 7 个负宇称 orbitals。
- [[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]] 对 `133Ce` 两对候选带使用 constrained RMF 的形变，调整 rotor moment of inertia 到实验能量，并对含低 `j` `g7/2` 的 Bands 2–3 使用 Coriolis attenuation `xi=0.7`。
- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]] 对 `78Br` 正/负宇称候选对采用 MDC-CDFT 的形变、MoI 16/18 hbar2/MeV 与 attenuation 0.6。
- [[xiao-2022-chirality-octupole-correlations-74as]] 对 `74As` Bands 1/2 固定 earlier-RMF `β2=0.37`，再以实验 energies/ratios 调整到 `γ=21.6°`、`J=12 hbar2/MeV`。
- [[bark-2024-investigations-nuclear-chirality-ithembalabs]] 对比 restricted single-orbital 与 realistic multi-orbital QTR/PRM spaces，并汇总 A≈80/190 多准粒子案例；其多个数值来自被综述的 earlier model papers。

## Predicted Observables

有利/不利 signature 带能级、[[signature-splitting]]、[[bm1-be2-ratio]] 和 mixing ratio。

## Strengths

能直接连接组态、三轴形变和实验能带。

## Known Limitations

拟合 γ 不是直接测量；转动惯量和 Coriolis attenuation 可引入模型依赖。

[[budaca-budaca-2025-harmonic-chiral-vibration]] 给出 harmonic approximation 的明确适用边界：低于 planar critical spin `I_c` 的单一 stationary point，并要求 quartic/quadratic correction `R_I` 不大；`R_I` 接近 `I_c` 增长，HA 会失效。其 `137Nd` D5/D6 `γ=97.5°` 来自少量归一化 energy-splitting 点，不能视为 shape measurement。用 Eq. (2)/(7) 与 `j=11/2,j′=10` 复算 `I_c≈17.804ℏ`；Fig.4f 中 `I=17.5ℏ` 的纳入点低于此模型值、`18.5ℏ` open point 高于它，但论文未称该点正是据此排除。 P25 `137Nd` data reuses P20 energy splits and lacks its own `B(M1)/B(E2)` comparison.

QTR 中近邻轨道混合会与 γ 同时改变 S(I)，因此单个最佳 γ 往往不是唯一反演。

Lawrie 2020 指出，QTR 对能带能量或大 E2 connecting transitions 的再现本身不能证明 transverse wobbling。对典型 transverse one-quasiparticle coupling，wobbling approximation 要求最大 MoI 轴——在该文 irrotational-flow convention 中为 intermediate axis（1 轴）——上的 rotational component 也为小量；作者计算的 `f(n,I)` 对 `135Pr/105Pd` 参数并不满足 `<<1`。该结论依赖 frozen-`j`、MoI ordering 和参数集合，仍是理论模型边界，不是实验裁决。

`135Pr` QTR 低估 `B(E2_out)`、高估 `B(M1_out)`，并把 signature-partner excitation 高估约 500 keV；拟合能量后的转动惯量不能作为独立验证。

`133Ce` TPRM 较好再现两对带的能量和总体 `B(M1)/B(E2)` 趋势，但没有再现实验中的小幅 odd-even staggering；RMF shape inputs、MoI adjustment 和 `xi` 使其属于模型支持而非独立实验验证。

`78Br` TPRM 比较 energies、`S_chiral(I)`、`B(M1)/B(E2)` 和 effective angles；nonplanar angles 是模型几何。Band 3 deviations 被归因于计算忽略 `f5/2-p3/2` mixing，configuration 仍非唯一实验事实。

`74As` TPRM reproduces pair energies, `S(I)` and the magnitude/staggering phase of `B(M1)/B(E2)`, but `γ` and `J` are fitted to those observables. Core/proton favor intermediate/short axes while the neutron mixes across all three; total `I` is aplanar without the ideal long-axis neutron alignment.

Bark 2024 汇总的 restricted/non-restricted calculation 显示，固定 particle/hole angular momenta 的 ideal model 才产生 exact partner equality、prescribed `B(M1)` staggering 与 vanishing `S(I)` staggering。扩大 single-particle space 后，Coriolis-driven orbital mixing 和 `<10%` planar components 可造成显著差异，即使 dominant geometry 仍 aplanar。该结果限制 universal fingerprints，但不能反向证明任意 nondegenerate doublet 都是 chiral。

同一综述中的多带计算还显示：按能量把 4-6 条 same-configuration bands 分对可能与 quasiparticle angular-momentum similarity 不一致；`193,194Tl` 的 observed/calculated band counts 进一步暴露 missing-band 和 non-unique-pairing 问题。

Sensharma 2019 的 QTR 给出
`E_TW1(I+1)-E_yrast(I) ≈ 2[E_TW2(I+2)-E_TW1(I+1)]`
的强 anharmonicity，并再现较小的 TW2→TW1/TW2→yrast 相对 E2 ratios。这里比较的是 successive wobbling-phonon spacings，不是把某条带的绝对能量直接取两倍；由于参数沿用 Matta 2015，这也不是对 zero-/one-phonon assignment 的独立验证。

[[lv-2022-evidence-against-wobbling-135pr]] 使用 `ε2=0.16, γ=26°`、irrotational-flow moments of inertia 与 unfrozen single-particle angular momentum。Fig.3(d) 仅示意 single-particle-excitation realignment 机制；p.5 正文报告五条计算带均显著受该机制影响并发生 short-to-intermediate-axis realignment，逐带细节位于 supplementary material。Fig.4(c) 的近恒定 `j_parallel` 只支持 `j` 与 `I` 近乎平行、同步演化，不直接显示主轴分量。作者将低激发带解释为 tilted-precession bands；计算仍高估 bands 2、5 的部分高自旋能量。

[[guo-2022-low-spin-wobbling-187au]] 的 QTR 波函数把 `187Au` Bands 1/2 主要联系到 `h9/2` 来源的最低/次低轨道，并较好比较本文/早期 internal-conversion data 的 energies、mixing ratios 与相对 transition ratios；作者据此提出 dominant single-particle excitation。该模型结果与 Sensharma 2020 的 large-`δ`/LW PRM interpretation 竞争，不能写成实验事实。详细程序位于当前未收录的 supplementary material；本文提到 TiP 只是 broader low-spin alternative，不是该 `187Au` QTR calculation 的直接结论。

[[lv-2021-tilted-precession-135nd]] 的 QTR 将 D1、TiP1、TiP2 低自旋主要联系到 `[Ω_l,K_l]=[9/2,9/2]`、`[9/2,13/2]`、`[11/2,15/2]`，并比较 energies 与相对 `B(M1)out/B(E2)in`、`B(E2)out/B(E2)in`。TiP1 高自旋 wave functions 混合且 energies 被高估；Appendix 的 no-pairing calculation 对 TiP1/TiP2 更差，说明低自旋模型比较依赖 pairing。这些是 QTR model results，不是直接观测的 angular-momentum geometry。

## Related Models

[[particle-rotor-model]]、[[triaxial-projected-shell-model]]

## Sources

- [[chakraborty-2023-131xe-wobbling-origin]]
- [[frauendorf-2024-wobbling-review]]
- [[petrache-2020-137nd-multiple-chiral-bands]]
- [[budaca-budaca-2025-harmonic-chiral-vibration]]
- [[budaca-budaca-2025-harmonic-chiral-vibration]]
- [[ding-2021-131ba-133ce-signature-splitting]]
- [[matta-2015-transverse-wobbling-135pr]]
- [[sensharma-2019-two-phonon-wobbling-135pr]]
- [[lv-2022-evidence-against-wobbling-135pr]]
- [[guo-2022-low-spin-wobbling-187au]]
- [[lawrie-2020-tilted-precession-wobbling]]
- [[lv-2021-tilted-precession-135nd]]
- [[ayangeakaa-2013-evidence-multiple-chiral-doublet-bands-133ce]]
- [[liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br]]
- [[xiao-2022-chirality-octupole-correlations-74as]]
- [[bark-2024-investigations-nuclear-chirality-ithembalabs]]

## Evolution Log

- 2026-07-01：由 `131Xe` 试摄入建立。
- 2026-07-01：加入 `137Nd` 手征几何与 N=75 signature-splitting 的参数敏感性。
- 2026-07-03：加入 Matta 2015 的 `135Pr` QTR 能量/跃迁比较及定量偏差。
- 2026-07-03：加入 Sensharma 2019 的 TW2 anharmonicity/E2-ratio 比较及参数继承边界。
- 2026-07-03：加入 Lv 2022 的 standard-input QTR realignment/TiP counter-interpretation。
- 2026-07-04：加入 Guo 2022 的 `187Au` multi-orbital QTR single-particle reinterpretation 与 supplementary-material 边界。
- 2026-07-04：加入 Lawrie 2020 对完整 3D QTR/TiP 与 harmonic wobbling approximation 的理论边界。
- 2026-07-04：加入 Lv 2021 `135Nd` QTR parameters、wave-function assignment、transition ratios 与 pairing comparison。
- 2026-07-13：加入 Ayangeakaa 2013 `133Ce` RMF-input TPRM、Coriolis attenuation 与 staggering discrepancy。
- 2026-07-13：加入 Liu 2016 `78Br` MDC-CDFT-input TPRM、effective-angle geometry 与 orbital-mixing limitation。
- 2026-08-11：加入 Xiao 2022 `74As` fitted `β2/γ/J`、ratio comparison 和 aplanar/nonideal-neutron geometry。
- 2026-08-11：加入 Bark 2024 restricted-versus-realistic configuration-space test 与 same-configuration multi-band pairing limitation。
- 2026-09-30：加入 Budaca & Budaca 2025 harmonic chiral-vibration approximation、critical-spin/anharmonicity 边界与 `137Nd` 的 same-dataset γ fit 迁移限制。
