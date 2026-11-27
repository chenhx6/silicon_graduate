---
type: source
title: "Nuclear Excitation by Two-Photon Electron Transition"
aliases: [Volotka 2016 NETP, Volotka 2016 two-photon nuclear excitation]
created: 2026-11-07
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: theory-article
reading_depth: deep-read
title_original: "Nuclear Excitation by Two-Photon Electron Transition"
authors: [A. V. Volotka, A. Surzhykov, S. Trotsenko, G. Plunien, Th. Stöhlker, S. Fritzsche]
journal: Physical Review Letters
year: 2016
volume: 117
pages: 243001
doi: 10.1103/PhysRevLett.117.243001
language: en
canonical_source: doi:10.1103/PhysRevLett.117.243001
raw_file: "raw/papers/isomer/isomer_application/nuclear battery/2016_Volotka et al_Nuclear Excitation by Two-Photon Electron Transition.pdf"
raw_sha256: f5e8286a8662e1d869dbff49d51877647c182e190c078c59a343b7724978026f
archive_required: true
nuclei: [225ac]
reactions: []
observables: [two-photon-transition-probability, nuclear-excitation-rate, continuous-energy-sharing]
methods: [relativistic-qed, dirac-hartree-fock, second-order-perturbation-theory]
tags: [netp, nuclear-excitation, two-photon, non-resonant-matching, highly-charged-ions, isomeric-control]
---

# Volotka et al. (2016): Nuclear Excitation by Two-Photon Electron Transition

## Bibliographic Record

A. V. Volotka, A. Surzhykov, S. Trotsenko, G. Plunien, Th. Stöhlker, and S. Fritzsche, "Nuclear Excitation by Two-Photon Electron Transition," *Physical Review Letters* **117**, 243001 (2016), DOI: `10.1103/PhysRevLett.117.243001`. Primary PDF is 5 pages, SHA-256: `f5e8286a8662e1d869dbff49d51877647c182e190c078c59a343b7724978026f`.

## Scope and Reading Depth

The 5-page Letter was read completely. Reading covers relativistic bound-state QED derivations of second-order electron-nucleus transitions (PDF p. 1--2 / printed p. 243001-1--2), Feynman diagrams (Fig. 1), continuous energy-sharing differential decay rates (PDF p. 3 / printed p. 243001-3, Eq. 6, Fig. 2), and numerical evaluation for He-like \(^{225}\)Ac\(^{87+}\) in Table I (PDF p. 4 / printed p. 243001-4).

## Summary

The authors propose a new mechanism of nuclear excitation: Nuclear Excitation by Two-Photon Electron Transition (NETP). While single-photon NEET and single-electron NEEC require strict resonance matching between atomic and nuclear levels within level widths (\(10^{-7}\text{--}1\text{ eV}\)), NETP utilizes two-photon electron de-excitation where one photon carries continuous energy \(\omega_1\) into the continuum, while the second photon carries \(\omega_2 = \Delta E_{\text{el}} - \omega_1 = E_N\), exciting the nucleus. This continuous energy sharing bypasses the strict energetic matching bottleneck.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| V16-1 | Formulates NETP mechanism where continuous two-photon electronic decay automatically satisfies nuclear excitation without energetic degeneracy. | theoretical-proposal | theoretical derivation | printed p.243001-1--2, Fig. 1 | true |
| V16-2 | Calculates NETP probability P_NETP = 3.5e-9 for 1s2s 1S0 -> 1s2 1S0 in He-like 225Ac87+ (Delta E_el = 92.42 keV) exciting the 3/2+ state (40.09 keV). | model-calculation | derived value | printed p.243001-3--4, Table I | true |
| V16-3 | NETP probability is comparable to resonant NEET probabilities in neutral atoms (~1e-7 to 1e-10) while possessing continuous phase space. | model-calculation | comparative analysis | printed p.243001-4 | true |
| V16-4 | Proposes detection at heavy-ion storage rings via coincidence between monochromatic photon omega_1 = 52.33 keV and nuclear de-excitation gamma-ray. | method-proposal | experimental design | printed p.243001-4 | true |

## Competing Interpretations and Limitations

Single-photon resonant excitation (NEET/NEEC) has higher peak cross sections at exact resonance, but requires fine-tuned matching of atomic and nuclear energies. NETP circumvents the resonance constraint, but its total probability is limited by the second-order electromagnetic coupling (\(\sim 3.5 \times 10^{-9}\)), requiring high ion luminosity in storage rings for experimental observation.

## Extracted Pages

- netp
- neet
- neec
- 225ac

## 2026-11-27 — 馆藏原件与覆盖核对

- 物理第1–2页（印刷243001-1至243001-2），书目、NEET与NEEC背景、NETP能量共享与级联、图1及算例输入。
- 物理第3页（印刷243001-3），图2、式(1)–(2)、核矩阵元、积分率与分支概率。
- 物理第4–5页（印刷243001-4至243001-5），图3–4、式(3)–(4)、两种探测方案、GSI计划、结论与参考文献[1]–[36]。
- 本次获取的具体覆盖：逐页读完物理第1–5页所供 Letter 文本及全部四条图注，覆盖机制、推导、数值计算、探测论证和参考文献。建议接受同版书目。既有深读条目的关键能量、图表定位和探测描述须更正并经图核后才可验收。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A20-1 | NETP 理论利用电子双光子衰变的连续能量分配。核激发能低于电子总跃迁能且多极性条件允许时，核可作为共振级联中间态。最终发射电子衰变光子 γ₁ 和核荧光光子 γ₂。 | 理论机制 | source-reported | 物理第2页图1及正文，物理第3页图2和式(1)–(2)。图1箭头和图2顶角顺序待图核。 | true |
| A20-2 | 类氦 ²²⁵Ac⁸⁷⁺ 算例的电子 E1E1 跃迁总能为89.218(2) keV，核 3/2⁺ 态激发能为40.09(5) keV。计算得到 W_NETP = 0.21 × 10⁵ s⁻¹，对应总双光子衰变的分支概率 P_NETP = 3.5 × 10⁻⁹。 | 模型计算 | source-reported | 物理第2页图1及能量输入正文，物理第3页式(1)后的总速率和概率定义。数值有正文依据，图1能级标注待图核。 | true |
| A20-3 | 模型预测连续双光子微分谱上出现两处 NETP 共振，中心分别约为49.13 keV和40.09 keV。前者由文中两项标称能量相减得到。 | 模型计算 | source-reported | 物理第2–3页能量守恒及共振近似，物理第4页图3和式(3)附近正文。图3 的能量共享轴和峰位置待图核。 | true |
| A20-4 | 作者比较以能量分辨辨认 γ₁ 和在电子背景衰减后观测约40 keV延迟核荧光 γ₂ 两种方案，判断后者更可行。GSI 方案拟将X射线与变为类氦电荷态的离子作时间符合。 | 实验提案 | source-reported | 物理第4页图3–4、式(3)–(4)及实验方案，物理第5页方案续文。图4时间曲线待图核。 | true |

核激发第一步按第三阶 QED S 矩阵处理，光子传播子取 Coulomb 项并采用共振近似。本算例忽略与纯电子双光子过程的微小干涉项。电子部分用有限核 Coulomb 势中的双动能平衡有限基表示 Dirac 谱，核部分借用外部约化跃迁概率。见物理第3页式(1)–(2)。

- V16-2 把92.42 keV改为89.218(2) keV，核能级补记为40.09(5) keV。删除 Table I 和式(6)定位，改引物理第2页图1及第3页的速率和概率段。Feynman 图位于物理第3页图2，微分谱位于物理第4页图3。
- 把方法字段中的 Dirac–Hartree–Fock 和第二阶微扰改为物理第3页明示的双动能平衡有限基和第三阶 QED S 矩阵。将“自动满足核激发”改为有能量与多极性条件的共振级联。删除正文未给出的通用共振宽度范围及峰值截面对比。
- V16-3 的 NEET 比较范围改为约 10⁻⁷ 至 10⁻¹²，并注明这是物理第3页对引文[19]–[20]所提算例的量级比较。
- V16-4 的52.33 keV改为约49.13 keV。将“双光子符合”替换为作者分别讨论的 γ₁ 能量辨认与 γ₂ 延迟荧光探测。GSI 方案的时间符合对象是X射线与电荷态改变的离子，见物理第4–5页。
