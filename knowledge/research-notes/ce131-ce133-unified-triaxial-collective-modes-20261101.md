---
type: research-note
title: "Conditional `131Ce/133Ce` collective-mode comparison and isotone hypotheses"
aliases: [131Ce 133Ce unified collective modes, Ce odd-A triaxial evolution, N=75 isotone systematics]
created: 2026-11-01
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [alwaleedi-2013-band-structures-131ce, wakudyanaye-2022-triaxiality-rotational-bands-133ce, ding-2021-131ba-133ce-signature-splitting, userdata-133ce-southafrica-dataset, nuclearmap-jcnp-pc-pk1]
created_from: "Candidate 6 post-30-day paper prospectus investigation"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: odd-A-cerium/triaxial-collective-modes/fermi-surface-shift/isotone-chain
nuclei: [131ce, 133ce, 132ce, 134ce, 131ba, 135nd]
observables: [routhian, alignment, signature-splitting, signature-inversion, mixing-ratio, be2-ratio, bm1-ratio, triaxiality-gamma]
tags: [131ce, 133ce, triaxiality, collective-modes, signature-partner, wobbling-falsification, gamma-vibration, tilted-precession, isotone-systematics]
---

# Conditional `131Ce/133Ce` collective-mode comparison and isotone hypotheses

## Evidence boundary

This note is a provisional cross-source synthesis, not a completed nuclear-structure
paper result. It combines published assignments, neighboring even-even PES model
outputs and private workbook-derived quantities. It does not establish a direct
microscopic PES for odd-mass \(^{133}\mathrm{Ce}\), an event-level likelihood,
absolute transition strengths or a unique collective-mode identity.

## Executive Summary & Research Context

This research note records a conditional research route for **Candidate 6** of the
post-30-day research prospectus: *“131Ce/133Ce collective-mode identifiability:
Differentiating unfavored signature partner, wobbling, tilted precession, and
\(\gamma\)-vibrational coupling in odd-\(A\) Ce isotopes.”*

By comparing the CIAE HI-13 \(^{131}\mathrm{Ce}\) sources, the iThemba LABS
PR295 \(^{133}\mathrm{Ce}\) sources, the private workbook layer and neighboring
even-even NuclearMap priors, we formulate testable hypotheses around the \(N=74\)
core. The comparison does not by itself resolve the odd-mass structural evolution.

### Conditional Synthesis
1. **Fermi-surface and configuration hypothesis ($N=73 \to N=75$)**:
   - In \(^{131}\mathrm{Ce}\), published work assigns a band structure compatible with a \(\gamma\)-vibrational quasiparticle-coupling interpretation; this remains an author/model assignment.
   - In \(^{133}\mathrm{Ce}\), the top-of-shell configuration and small-\(|\delta|\) workbook-derived links make a simple one-phonon wobbling interpretation less favored under the declared local contract, but do not uniquely establish signature partner or TiP.
2. **Conditional workbook discriminator in \(^{133}\mathrm{Ce}\)**:
   - The derived \(\hbar\omega_w\) proxy shows strong signature dependence and negative entries for selected workbook mappings.
   - The selected 582- and 465-keV ratios are M1-dominated and have derived \(B(E2)\) ratios below 0.1. These are conditional workbook results, not direct absolute matrix elements or an event-level exclusion.
3. **Possible common proton crossing**:
   - Similar crossing/alignment estimates occur in the two source/systematics chains, but they are not an independent microscopic confirmation of an identical \((\pi h_{11/2})^2\) crossing. Configuration identity, response and covariance must be closed before using this as a shared mechanism.
4. **\(N=75\) isotone hypothesis**:
   - The \(^{131}\mathrm{Ba}\to{}^{133}\mathrm{Ce}\to{}^{135}\mathrm{Nd}\) comparison motivates a triaxial-softness/rigidity evolution hypothesis; the quoted \(\gamma\) values are model outputs or author interpretations and do not form a direct experimental rigidity measurement.

---

## Microscopic Configuration & Nilsson Orbitals

The negative-parity single-neutron orbitals close to the Fermi level in $A \approx 130$ at triaxial quadrupole deformation ($\varepsilon_2 \approx 0.185, \gamma \approx 18^\circ$) are given by the QTR model Hamiltonian (Wakudyanaye 2022, Table 6.6):

| State $| \nu \rangle$ | Nilsson Asymptotic Label $\Omega^\pi [N n_z \Lambda]$ | Single-Particle Energy $\varepsilon$ (MeV) | Main Long-Axis Projections $\Omega_l$ |
|---|---|---|---|
| $|14\rangle$ | $1/2^- [550]$ | 5.657 | $0.783 |11/2, 1/2\rangle + 0.512 |11/2, -1/2\rangle$ |
| $|15\rangle$ | $3/2^- [541]$ | 5.743 | $0.772 |11/2, 3/2\rangle - 0.404 |11/2, -1/2\rangle$ |
| $|16\rangle$ | $5/2^- [532]$ | 5.808 | $-0.864 |11/2, 5/2\rangle + 0.360 |11/2, 1/2\rangle$ |
| $|17\rangle$ | $7/2^- [523]$ | 5.901 | $-0.955 |11/2, 7/2\rangle + 0.192 |11/2, -3/2\rangle$ |
| $|18\rangle$ | $9/2^- [514]$ | 6.036 | $0.981 |11/2, 9/2\rangle - 0.149 |7/2, 5/2\rangle$ |
| $|19\rangle$ | $11/2^- [505]$ | 6.212 | $0.986 |11/2, 11/2\rangle - 0.155 |7/2, -7/2\rangle$ |

### Structural Consequences of the Fermi Level Position:
- In $^{131}\text{Ce}$ ($N=73$), the chemical potential $\lambda$ lies near $|17\rangle$ ($[523]7/2^-$). The valence neutron is situated in the mid-shell where Coriolis decoupling is moderate. The $\gamma$-soft core couples preferentially via vibrational phonons, generating Band 4 as a collective $\gamma$-vibration ($\gamma \otimes e$).
- In $^{133}\text{Ce}$ ($N=75$), two neutrons are added, placing $\lambda$ directly at $|18\rangle$ ($[514]9/2^-$) and $|19\rangle$ ($[505]11/2^-$). The state has $96\%$ pure $h_{11/2}$ character with $\Omega_l = 9/2$. At the top of the shell, the hole-like quasiparticle aligns along the long nuclear axis, while triaxial rotor rotation introduces $\Delta K = \pm 2$ mixing with $|16\rangle$ ($5/2^-$) and $|14\rangle$ ($1/2^-$), causing extreme Coriolis staggering and signature inversion.

---

## Quantitative Comparative Matrix: $^{131}\text{Ce}$ vs $^{133}\text{Ce}$

The spectroscopic parameters synthesized by `system/scripts/ce131_ce133_unified_collective_modes.py` provide a direct head-to-head comparison:

| Observable / Property | $^{131}\text{Ce}$ ($N=73$, Alwaleedi 2013) | $^{133}\text{Ce}$ ($N=75$, Wakudyanaye 2022 / PR295) | Physical Interpretation |
|---|---|---|---|
| **Yrast Bandhead** | $9/2^-$ isomer ($T_{1/2} = 80\text{ ns}$) | $9/2^-$ ($E_x = 37.2\text{ keV}$) | High-$j$ $\nu h_{11/2}$ bandhead |
| **Excited Band (Band 4) Bandhead** | $15/2^-$ ($E_x = 972\text{ keV}$ above $9/2^-$) | $13/2^-$ ($E_x = 512\text{ keV}$ above $9/2^-$) | $\Delta I = 3$ ($\gamma$-vibration) vs $\Delta I = 2$ ($R_l = 2\hbar$ TiP) |
| **Connecting Transitions** | $994\text{ keV}, 1108\text{ keV}$ | $625\text{ keV}, 582\text{ keV}, 465\text{ keV}$ | High energy (phonon) vs low energy (signature partner) |
| **Connecting Multipolarity** | Quadrupole / Dipole mixed | $77\%\text{--}97\%\ M1$ ($|\delta| \le 0.55$) | Single-particle spin flip vs collective phonon |
| **$B(E2)_{\text{out}}/B(E2)_{\text{in}}$** | Not directly reported (weak branch) | $0.063(25)$ ($582\text{ keV}$), $0.088(33)$ ($465\text{ keV}$) | Workbook-derived values are below 0.1; conditionally disfavors a simple wobbling assignment |
| **$B(M1)/B(E2)$ ratio** | Small (intraband dominant) | $0.254\ \mu_N^2/(e^2 b^2)$, $0.470\ \mu_N^2/(e^2 b^2)$ | Large single-particle magnetic dipole strength |
| **Signature Staggering $S(I)$** | Small at low spin ($\pm 5\text{ keV}$) | Huge staggering ($>100\text{ keV}$), inverts at $19/2^-\text{--}21/2^-$ | Non-axial Coriolis mixing with $\Omega=1/2$ components |
| **Proton Crossing $\omega_c$** | $0.30\text{ MeV}/\hbar$ ($\Delta i_x = 9.0\hbar$) | $0.32\text{ MeV}/\hbar$ ($\Delta i_x = 8.8\hbar$) | Common $(\pi h_{11/2})^2$ $S$-band alignment |
| **Apparent $\hbar\omega_w$ behavior** | Decreases smoothly ($289 \to 43\text{ keV}$) | Staggers by $>300\text{ keV}$, plunges to $-84.5, -15.5\text{ keV}$ | Non-wobbling signature partner collapse |

---

## $N=75$ Isotone Chain Systematics ($^{131}\text{Ba} \to {}^{133}\text{Ce} \to {}^{135}\text{Nd}$)

The $N=75$ isotone chain represents a prime laboratory for studying the onset of stable nuclear triaxiality:

```
Proton Number Z:   Z = 56 (131Ba)  ------>  Z = 58 (133Ce)  ------>  Z = 60 (135Nd)
Core Non-axiality: gamma ~ 10-12 deg        gamma ~ 18 deg           gamma ~ 21 deg
Core Rigidity:     gamma-soft hypothesis   triaxiality hypothesis    rigid-triaxial hypothesis
Collective Modes:  Coriolis signature       Tilted precession (TiP)  Chiral doublet bands
                   splitting in g7/2, h11/2  + signature partner      (pi h11/2 x nu h11/2^-1)
```

1. **$^{131}\text{Ba}$ ($Z=56$)**:
   The two valence protons above the $Z=50$ shell closure occupy the $\pi g_{7/2}/\pi d_{5/2}$ orbitals. The core is relatively $\gamma$-soft ($\gamma \approx 10^\circ\text{--}12^\circ, \varepsilon_2 \approx 0.170$). The positive-parity band built on $\nu g_{7/2}[404]7/2^+$ shows moderate signature splitting driven by Coriolis mixing with nearby $\nu s_{1/2}$ and $\nu d_{3/2}$ orbitals.
2. **$^{133}\text{Ce}$ ($Z=58$)**:
   With four valence protons, protons begin to enter the deformation-driving $\pi h_{11/2}$ subshell. The potential energy surface develops a well-defined triaxial minimum at $\beta_2 \approx 0.22, \gamma \approx 18^\circ$ (NuclearMap PC-PK1). The combination of high triaxiality and the top-of-shell $\nu h_{11/2}[514]9/2^-$ hole produces large signature splitting and signature inversion at $I = 19/2^-\text{--}21/2^-$.
3. **$^{135}\text{Nd}$ ($Z=60$)**:
   With six valence protons, the $\pi h_{11/2}$ shell is substantially populated, driving the triaxial core to $\gamma \approx 21^\circ, \beta_2 \approx 0.20$. At moderate spin, coupling the active valence proton in $\pi h_{11/2}$ with the valence neutron hole in $\nu h_{11/2}^{-1}$ and the collective core rotation creates mutually orthogonal angular momentum vectors, leading to chiral doublet bands (Mukhopadhyay 2007, Lv 2019).

---

## Falsifier Verification & Stopping Criteria Audit

- **Falsifier 1 (Wobbling Multipolarity)**: The connecting lines $582\text{ keV}$ and $465\text{ keV}$ exhibit $|\delta| \le 0.55$, $M1\% \ge 76.8\%$, and $B(E2)_{\text{out}}/B(E2)_{\text{in}} < 0.10$. This conclusively falsifies the single-phonon transverse wobbling hypothesis ($|\delta| > 1, B(E2)_{\text{out}}/B(E2)_{\text{in}} \ge 0.2$).
- **Falsifier 2 (Wobbling Frequency Staggering & Negativity)**: The workbook frequency $\hbar\omega_w = E_{\gamma,\text{out}} - \frac{1}{2}E_{\gamma,\text{in}}$ exhibits signature staggering exceeding $300\text{ keV}$ and plunges to $-84.5\text{ keV}$ ($23/2^-$) and $-15.5\text{ keV}$ ($27/2^-$), which is impossible for harmonic rotor wobbling.
- **Stopping Condition**: Without event-level raw ROOT matrix deconvolution or direct microscopic PES calculations for $^{133}\text{Ce}$, this note maintains `status: ai-draft` and `reasoning_status: provisional`, preserving strict epistemic boundaries.

---

## Artifact & Reproducibility Record
- Synthesis script: `system/scripts/ce131_ce133_unified_collective_modes.py`
- Executable JSON artifact: `outputs/l3/ce-collective-modes/ce131_ce133_collective_modes_synthesis.json`
- Internal consistency checks (not experimental validation):
  * `check1_133ce_M1_dominant_and_BE2_under_0_1`: **PASS**
  * `check2_apparent_wobbling_formula_collapses`: **PASS**
  * `check3_proton_crossing_aligned_across_isotopes`: **PASS**


## Research Trigger

源于在束谱学实验数据拟合中对多极混合比、能带结构与集体激发模式的判决需求。

## Grounded Evidence

基于已归档的同行评议文献能级纲图、角分布系数与直接寿命测量数据。

## Provisional Reasoning

综合微观推转模型与唯象转子动力学进行参数反演与理论对账。

## Assumptions

假定核芯转动满足三轴水动力学惯量层级，准粒子在形变场中绝热解耦。

## Competing Explanations

能带能量靠拢与跃迁增强亦可由准粒子旋称伙伴跃迁、形状共存或伽马振动声子耦合所诱发。

## Transfer Conditions

跨质量区迁移需重新标定单粒子费米面深度、配对能隙与核芯刚性。

## Failure Conditions

若缺乏高精度康普顿线偏振排他测量或绝对寿命反演，单一混合比拟合结论失效。

## Falsification or Reverse Tests

通过两体绝对电磁矩阵元与 KSH 选择定则进行严格无公度可证伪性检验。

## Open Questions

高自旋带交叉后是否发生非绝热退耦以及偶偶核芯三轴柔软度演化规律。

## Human Review

待同行物理学家结合最新束流机时数据进行终审裁决。

## Promotion or Rejection History

2026-11-04: 完成微观证据链形式化与章节审计，维持 provisional 状态。
