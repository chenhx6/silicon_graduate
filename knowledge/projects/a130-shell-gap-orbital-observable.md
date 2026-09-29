---
type: project
title: "A≈130 shell-gap, orbital and observable bridge"
aliases: [A130 shell gap observable bridge, A≈130 壳隙轨道观测量桥]
created: 2026-09-22
updated: 2026-09-28
status: active
review_status: unreviewed
project_stage: seed
confidentiality: private
nuclei: [131ce, 131ba, 133ce]
tags: [a130, shell-effects, orbitals, observables, durable-learning]
---

# A≈130 shell-gap, orbital and observable bridge

本页把 Day 2 的学习结果保存为长期知识：球形壳层闭合、形变/转动壳隙、轨道组态和实验观测量之间如何连接。它不是某个 A≈130 核素的定量壳隙结论。

## Research Question

如何把壳层闭合、形变依赖的 shell gap、轨道/组态指认和集体观测量连接起来，同时避免把模型计算或配置标签直接写成三轴形变事实？

## Current Hypotheses

- spherical closure、deformation-dependent shell gap、orbital assignment 和 shape/collectivity 是证据链中的不同层；
- A≈130 的 shell-effect 解释需要质量/分离能、谱学、alignment 和 calibrated electromagnetic observables 的组合；
- γ-soft、组态混合和 pairing 变化可能产生与固定 shell-gap/shape 标签相似的信号。

## Evidence basis

- [[haxel-jensen-suess-1949-magic-numbers]]：自旋—轨道分裂与历史 magic-number 闭合的模型背景；不是现代定量 shell-gap 测量。
- [[ragnarsson-nilsson-sheline-1978-shell-structure]]：Nilsson/modified-oscillator、Strutinsky shell correction、γ/β3、质量/分离能、`E(2+)`、形变和高自旋稳定性的综述边界；review/model synthesis，不是独立实验复制。
- [[ame2020-sn132-mass-curvature]]：AME2020 `130,132,134Sn` 质量 excess，允许构造 N=82 的两中子质量曲率指标。
- [[iaea-livechart-132sn-134te-levels]]：`130Sn/132Sn` isotope 与 `132Sn/134Te` isotone 的 adopted `2+` level-energy 对照；LiveChart/NuDat 都是评估数据库入口。
- [[ensdf-134te-coulomb-excitation]]：`134Te` 的 ENSDF Coulomb-excitation 子表给出 adopted `B(E2)↑=0.13(4)` 及其派生寿命，并回链 `2003Ba01`；原始论文全文尚不可访问，因此这里保留评估值与 primary-text boundary。
- [[jones-2010-133sn-single-particle-transfer]]：`132Sn(d,p)133Sn` 的粒子转移截面和 DWBA 比较；谱因子是模型派生反应量，不是直接占据数。
- [[ensdf-133sn-transfer-levels]]：`133Sn` 的 evaluated transfer-level 和反应引用入口；它与 Jones 原始实验共享数据谱系，不是独立重复。
- [[ensdf-131sn-neutron-hole-levels]]：`131Sn` 评估空穴侧能级与 unresolved isomer-energy 边界；该评估页不是新的反应测量。
- [[orlandi-2018-131sn-neutron-hole-transfer]]：`132Sn(d,t)131Sn` 的空穴转移强度、未分辨双重态和光学势/未观测能级系统误差；解释仍受 `d3/2` 假设限制。
- [[varner-2005-coulomb-excitation-132-134sn]]：直接 Coulomb-excitation `B(E2)`；保留 `132Sn` efficiency-calibration 尚不完整和 `134Sn` mixed-beam 边界。
- [[radford-2005-130sn-coulomb-excitation-126-130sn]]：纯束流逆运动学 CoulEx 直接给出 126/128/130Sn 的初级 B(E2)，130Sn 结果标为 preliminary。
- [[gray-2021-thesis-electromagnetic-moments-z50]]：ANU 学位论文 Table 3.13 将 Radford 130Sn 数据转列为 5.9(1.3) W.u.；它是同一数据的再表述，不是新实验。
- [[ensdf-132sn-coulomb-excitation]]：ENSDF 对 `132Sn` Coulomb-excitation 值的汇编，以及 `2005Ra09/2005Va31` 同场址、不同靶反应的谱系标记。
- [[li-2004-lifetimes-131ce]]：`131Ce` 高自旋寿命、派生 `B(E2)/Q_t` 和 `νh11/2/νg7/2` 作者解释。
- [[singh-2016-lifetime-131ce-133pr]]、[[ding-2021-131ba-133ce-signature-splitting]]：独立 `131Ce` lifetime dataset、`N=75` isotone signature splitting 及其模型竞争边界。
- [[a130-high-spin-collective-modes-evidence-map]]：A≈130 竞争集体模式的 owning project，负责把本页方法桥接到 `131Ce/133Ce` 等具体问题。

## Orbit–gap–observable map

| Layer | What it means | Useful observables | Boundary |
|---|---|---|---|
| Spherical closure | Large separation/bunching in a near-spherical single-particle spectrum, affected by spin–orbit ordering | masses, one-/two-nucleon separation energies, low `E(2+)`, reduced collectivity | One excitation energy or one model diagram does not establish a shell gap |
| Deformation-dependent shell gap | Level bunching depends on `β`, `γ`, rotational frequency, pairing and potential parameterization | aligned configurations, crossings, signature, moments of inertia, termination and transition strengths | Calculated gap is model output; inputs and smoothing/pairing choices must be stated |
| Orbital/configuration assignment | Occupation label such as `nℓj` or a Nilsson asymptotic orbital | spin/parity, transfer/decay, multipolarity, DCO/ADO, polarization, crossings and alignment | A configuration label is not itself a measurement of shape |
| Shape/collectivity | Collective response of the nucleus or band | lifetime-derived `B(E2)`, absolute `B(M1)`, `Q_t`, linking transitions, g-factor and consistent systematics | `β`, `γ` and γ-soft/γ-rigid interpretations remain model-assisted unless companion observables close the chain |

## Evidence Available

本页依托 Haxel–Jensen–Suess 1949 和 Ragnarsson–Nilsson–Sheline 1978 的 source 页面，以及 A≈130 集体模式 project。两份 anchor 是历史模型/综述谱系，不是独立目标核实验。

## Day 2 calculation and design result

For the historical spin–orbit ordering, the cumulative degeneracies can be checked through `N=50` as `2 + 6 + 10 + 2 + 4 + 8 + 6 + 12 = 50`.

This is an occupancy/closure arithmetic check. It does not estimate an energy gap in MeV. For a deformed high-spin case, the corresponding analysis requires a specified potential/deformation parameterization, pairing prescription, rotational-frequency grid, occupied Nilsson branches and a level-density/crossing comparison. No numerical A≈130 gap was invented because the required model table and covariance were not available.

## A≈130 shell-gap/orbital case study (Day 2; 2026-09-28)

### Spherical N=82 closure indicators

| Comparison | evaluated evidence | Result | Boundary |
|---|---|---|---|
| 130Sn–132Sn–134Sn isotope chain (Z=50, N=80→82→84) | IAEA/ENSDF first 2+ levels: 1221.26(5) keV tentative (2+), 4041.2(15) keV and 725.6 keV. Radford et al. directly report preliminary 130Sn B(E2)=0.023(5) e2b2; Varner et al. report preliminary 132Sn=0.11±0.03 and 134Sn=0.029(5) e2b2. NuDat displays 132Sn B(E2)=5.5(15) W.u. in its gamma table and 0.11(3) without a unit on the adopted-level row; the 2+ lifetime 2.4 fs is explicitly marked as derived from a B(E2), so it is not an independent confirmation. | E(2+) peaks at N=82; Radford’s 130Sn value converts to 5.88(1.28) W.u.; the quoted primary 132Sn/130Sn B(E2) ratio is 4.78±1.67 if errors are treated as independent | All Sn CoulEx values are preliminary; Varner’s 132Sn photon-efficiency calibration was incomplete. The 5.5-W.u. gamma field is paired with a 2.4-fs lifetime explicitly derived from B(E2); this is not a third independent experiment. The adopted-level 0.11(3) field carries the Coulomb-excitation XREF and matches Varner’s direct preliminary value. The primary input behind the alternate 5.5-W.u. field remains to be traced; do not average the displayed values. |
| `132Sn`–`134Te` isotone chain (`N=82`, `Z=50→52`) | IAEA/ENSDF first `2+`: `4041.2(15) keV` in `132Sn`; `1279.11(10) keV` in `134Te`. NuDat adopted `B(E2)` values are `5.5 15` and `6.3 20 W.u.`, respectively. | The `2+` energy is lower by `2762.09(18) keV` after adding two protons, while the adopted `B(E2)` central values are similar within their quoted uncertainties | The `134Te` primary citation is `2003Ba01`; its full text was blocked at the publisher endpoint, so this comparison remains database-grounded |
| `132Sn`–`134Sn` isotope chain across `N=82` | Varner et al. report preliminary `B(E2;0+→2+)=0.11±0.03` and `0.029(5) e²b²`, respectively; the `134Sn` beam was mixed | The nominal strengths differ by a factor of about `3.8` | Both results rely on the same experiment family/response treatment; the authors say the `134Sn` value is close to `130Sn` and do not claim a sharp B(E2) asymmetry at N=82 |

The Radford Table 1 value gives a second unit check. Using the standard Weisskopf E2 expression B_W(E2,A)=(1/(4π))(3/5)^2(1.2 A^(1/3))^4 e², one Weisskopf unit at A=130 is 0.003912 e²b²; therefore 0.023(5) e²b² is 5.88(1.28) W.u. Gray’s 2021 thesis Table 3.13 re-tabulates the core value as 5.9(1.3) W.u. and cites Radford 2005, so this checks the conversion but is not a second experiment. In the same e²b² units, the central Varner/Radford 132Sn/130Sn ratio is 4.78; diagonal propagation of the quoted errors gives 1.67 under an independence assumption. This is descriptive only because the 132Sn photon-efficiency calibration was incomplete and NuDat displays separate adopted fields.

The AME2020 mass excesses give a complementary mass-curvature indicator:

\[
S_{2n}(N,Z)=ME(N-2,Z)+2ME_n-ME(N,Z),\qquad
\delta_{2n}(82,50)=S_{2n}(82,50)-S_{2n}(84,50)
=ME(130Sn)-2ME(132Sn)+ME(134Sn).
\]

Using `ME(130Sn)=−80132.217±1.873`, `ME(132Sn)=−76546.554±1.976` and `ME(134Sn)=−66433.759±3.167 keV` from AME2020 `mass_1.mas20.txt` gives `δ₂n=6.527132 MeV`. The matching `rct1.mas20.txt` table independently reproduces `S₂n(132Sn)=12.5569730±0.0027224 MeV` and `S₂n(134Sn)=6.0298413±0.0037328 MeV`; these are the same AME2020 evaluation, not an independent mass dataset. Diagonal propagation through the mass second difference gives `σ(δ₂n)=0.005400 MeV` if the three quoted mass uncertainties are treated as independent. The retrieved files do not provide the fitted-mass covariance matrix, so this is a reproducible diagonal estimate, not a covariance-complete uncertainty. `δ₂n` includes pairing and smooth mass-surface contributions; it is not identical to a microscopic single-particle spacing.

### N=82 particle-hole sides and one-neutron mass difference

The particle side is directly sampled by 132Sn(d,p)133Sn. Jones et al. report the transfer experiment and interpret the resulting levels as predominantly single-particle; the open Supplementary Information gives local/global DWBA spectroscopic-factor pairs of 0.86/0.85 for the ground state, 0.92/0.80 at 854 keV, 1.1/1.0 at 1363 keV and 1.1/1.1 at 2005 keV (JON10-1, JON10-4). The main Fig.3 preview also shows alternative orbital fits with different l and extracted factors (JON10-5). These factors are model-derived reaction quantities, not direct occupancies; the evaluated 133Sn table connects the ground and 853.7-keV states to L(d,p)=3 and 1, respectively (ENSDF133SN-1, ENSDF133SN-3). The 1560.9-keV h9/2 candidate lacks the 132Sn(d,p) XREF (ENSDF133SN-5).

For the hole side, the NuDat 131Sn evaluation lists a 3/2+ ground state, an unresolved-energy 11/2− isomer, and positive-parity levels at 331.73 and 1654.53 keV (ENSDF131SN-2–5). Orlandi et al. 2018 provide a separate 132Sn(d,t)131Sn neutron-removal dataset. The summed spectrum does not resolve the 0–65-keV doublet at about 270-keV FWHM; a pure d3/2 fit gives S=5.0(5), while assuming full h11/2 strength 12 changes it to S(d3/2)=4.3(5), near the 2j+1 maximum of 4 (ORL18-3/4). The 332-keV s1/2 state gives 2.4(2), and the 1654-keV d5/2 state gives 6.4(1.8), with the latter near maximum 6 (ORL18-5/6). Other optical potentials shift factors by about 10–20%; the proposed 2343-keV 7/2+ hole state was not observed (ORL18-7/8).

For spin-orbit splitting, the article uses the 131Sn hole states together with earlier 133Sn particle energies from Jones and related measurements, rather than measuring both sides in one reaction (ORL18-18). The cited 2d binding energies −9.007(4) and −7.353(4) MeV differ by 1.654 MeV; the authors report about 50% lower Δso/(l+1/2) for weakly bound 3p than for well-bound 2d, with ±150-keV average uncertainty due to possible unobserved levels (ORL18-10/11/12). A Woods–Saxon model with fixed spin-orbit strength reproduces the measured trend and attributes it to extended weakly bound radial wavefunctions; calculated 3p radii of 7.48 and 8.29 fm exceed the 2d radii near 5.3 fm (ORL18-13/14/15). These calculations are author model results, not direct measurements, and spin-orbit splitting is not itself the full N=82 particle-hole gap.

With only marginal mass uncertainties and no covariance matrix, a conservative bound follows from the triangle inequality for any positive-semidefinite covariance matrix:
σ[D] ≤ Σi |ci| σi.
For δ₂n the maximum is 1.873+2×1.976+3.167=8.992 keV (the diagonal estimate is 5.400 keV); for Δn(82) it is 3.621+2×1.976+1.904=9.477 keV (diagonal 5.688 keV). These are formal uncertainty bounds on the finite differences under arbitrary correlations, not an estimate of the actual AME fit covariance and not a bound on pairing or smooth-mass model contributions. They are tiny relative to the MeV-scale central differences but do not turn either indicator into a microscopic orbital gap.

The AME2020 mass rows permit an adjacent one-neutron separation-energy indicator:
S_n(132Sn)=ME(131Sn)+ME(n)−ME(132Sn)=7.353293 MeV,
S_n(133Sn)=ME(132Sn)+ME(n)−ME(133Sn)=2.398654 MeV,
Δ_n(82)=S_n(132Sn)−S_n(133Sn)=ME(131Sn)−2ME(132Sn)+ME(133Sn)=4.954639 MeV.
Using the tabulated mass-excess errors as independent gives a diagonal uncertainty of 0.005688 MeV for this difference; the common neutron mass cancels exactly, while the AME file does not supply fitted-mass covariance. This one-neutron difference is a shell-gap indicator that still contains odd-even pairing and mass-surface contributions. It is not the 6.527132-MeV two-neutron curvature above, and neither finite difference is identical to the DWBA orbital spacing or a measured single-particle centroid.

The two sides now have direct transfer evidence at different depths: Jones 2010 supplies 133Sn particle-side cross sections and DWBA comparisons in its SI; Orlandi 2018 supplies the 131Sn neutron-removal differential cross sections and fits in the Surrey repository article. The 0–65-keV doublet assumption, 10–20% optical-potential sensitivity and ±150-keV unobserved-state boundary prevent a model-free occupancy or complete shell-gap claim. The ENSDF 133Sn and 131Sn records remain evaluation interfaces for cited data, not independent repetitions.

### High-spin orbital and collectivity example

`131Ce` has `N=73`, nine neutrons below the `N=82` closure. Li et al. measured line shapes and lifetimes for separate positive- and negative-parity high-spin sequences, then derived `B(E2)` and `Q_t`; the orbital-driving language for `[514]9/2− (h11/2)` and `[404]7/2+ (g7/2)` is the authors' interpretation (LI04-1–5). In the `27/2−→23/2−` row, the original `B(E2)=1723(322) e²fm⁴` and corrected `Q_t=2.72(25) eb` are internally reproduced by the strong-coupling rotor conversion with `I=27/2`, `K=11/2`:

\[
C^2=|\langle IK20|I-2,K\rangle|^2=0.233846,
\qquad Q_t=\sqrt{\frac{16\pi B(E2)}{5C^2}}=2.7216(254)\;eb.
\]

The `K` conversion is an assumption of this exercise; it does not promote the derived `Q_t` to a direct observable. Singh et al. report a separate current `131Ce` lifetime result, `Q_t=2.26^{+0.37}_{-0.23} eb`, for the same spin transition. Their Table 1 also re-evaluates Li's same `1.23(23) ps` lifetime as `2.28(21) eb` using their Eq. (1)–(3) rotor/Clebsch–Gordan convention (SI16-2/4/16). A reconstruction of their rotationally aligned `j=11/2` basis uses `a_K²=2^{-11}\binom{11}{11/2+K}` and `C_eff=Σ_K a_K²⟨IK20|I−2,K⟩=0.580021`; with the same `B(E2)`, it gives `Q_t=2.269±0.212 eb`, consistent with the re-tabulated `2.28(21) eb`. By contrast, a pure `K=11/2` conversion gives `2.722±0.254 eb`, reproducing Li's `2.72(25)`. Thus the apparent `Q_t` mismatch between Li's original table and Singh's re-tabulation is explained by the angular-momentum conversion convention applied to the same lifetime, not by a third measurement. Singh's present result remains a separate experiment; no cross-experiment average is formed.

`131Ba` and `133Ce` are `N=75` isotones. Ding et al. directly establish strong-coupled `νg7/2[404]7/2+` bands, while their Nilsson interpretation places an `N=74` gap between the `νg7/2` and `νh11/2` orbitals (D21-1/2/9). CSM/QTR calculations also show signature splitting can respond to both triaxiality and nearby `νs1/2` Coriolis mixing; attenuating Coriolis coupling removes the low-γ staggering in their calculations (D21-4–6). The `N=74` gap, PES deformations and competing mechanisms are model results, not experimentally measured single-particle spacings or shapes.

### Source lineage, missing observables and next checks

- The 130/132/134Sn masses and `S₂n` values are from one AME2020 evaluation. IAEA LiveChart and NNDC NuDat expose the same ENSDF level evaluation; querying both interfaces is a transfer check, not independent spectroscopy. The `132Sn` `B(E2)` is directly reported by Varner et al.'s `48Ti`-target experiment; the `134Te` strength remains evaluation-grounded pending the primary 2003 paper.
- Li 2004 and Singh 2016 are separate `131Ce` lifetime experiments. Singh's Ref. [32] entry for Li is a re-calculation of the earlier lifetime and remains in Li's lineage. Ding 2021 contains separate `131Ba` and `133Ce` reactions/arrays in one paper; its N=73 comparison points back to older sources and is not a new `131Ce` measurement.
- To separate a mass-curvature closure signal from a microscopic orbital gap, the next checks need the AME mass covariance/measurement chain and configuration-sensitive transfer or decay observables. Radford 2005 now supplies preliminary direct 130Sn B(E2)=0.023(5) e²b², but the short proceedings paper omits a full uncertainty decomposition; the 1981 130Sn transition-probability paper is still closed. Varner 132Sn photon-efficiency response and the conflict between NuDat B(E2) display fields also remain open. The 134Te primary citation 2003Ba01 and the carbon-target 2005Ra09 132Sn route are identified but their full texts were not obtained here.
- For high-spin A≈130 orbital/shape interpretation, needed companions remain transition-level mixing ratios, polarization, matched lifetimes/absolute strengths and a documented CSM/QTR sensitivity set. No event-level spectra, response, covariance or code package was available for an L4 fit.

## Counter-evidence and next observables

Pairing changes can mimic separation-energy curvature; configuration mixing can shift nominal single-particle levels; γ-soft potential-energy surfaces can blur a fixed deformation label; and changes in diffuseness, pairing or smoothing can move a calculated gap. The next A≈130 comparison therefore needs neighboring mass/systematics plus configuration-sensitive spectroscopy and calibrated electromagnetic strengths.

For `131Ce/133Ce`, this bridge feeds the competing-mode question but does not rank signature/configuration coupling, γ-soft response, wobbling, chirality or shape coexistence by itself. That ranking remains in [[131ce-collective-mode-discrimination]].

## Risks and Blockers

- 当前没有目标 A≈130 核素的统一自洽 shell-gap 数值表和协方差；
- HJS49/RS78 是模型与综述背景，不能替代现代目标核实验；
- pairing、diffuseness、smoothing、γ-softness 和 configuration mixing 会改变计算解释；
- 本页不提供 L4 输入，也不产生代理结果。

## Status and provenance

This is a Codex self-audit durable learning asset created from the Day 2 source reading and exercise. It is `review_status: unreviewed`; all scientific claims must return to the linked source pages and raw locators for paper use.

## Next Actions

1. 选择一个 A≈130 目标核，补充 modern mean-field/cranked model 与实验 observable 的一一对应。
2. 将本页与 `131Ce/133Ce` project 的竞争模式矩阵连接，记录 shell-effect 解释可被什么结果推翻。
3. 不把历史 closure arithmetic 当作目标核的定量 shell gap。
