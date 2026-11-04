---
type: research-note
title: "133Ce private data wobbling vs signature reconstruction and collective-mode identifiability"
aliases: [133Ce South Africa wobbling vs signature audit, 133Ce collective mode reconstruction]
created: 2026-11-01
updated: 2026-11-01
status: ai-draft
visibility: private
publication_status: local-only-unpublished-user-data
review_status: unreviewed
reasoning_status: provisional
evidence_sources: [userdata-133ce-southafrica-dataset, nuclearmap-jcnp-pc-pk1]
created_from: "User-authorized South Africa 133Ce data audit and collective mode reconstruction"
promotion_target: "post-30-day-nuclear-structure-paper-prospectus"
scope: 133ce/private-data/wobbling-vs-signature-partner/identifiability-boundary
nuclei: [133ce, 131ce, 132ce, 134ce]
observables: [wobbling-frequency, mixing-ratio, branching-ratio, be2-ratio, bm1-ratio, signature-splitting, signature-inversion]
tags: [133ce, wobbling, signature-partner, signature-inversion, branching-ratio, mixing-ratio, be2-ratio, private-data, l4-readiness]
---

# `133Ce` private data wobbling vs signature reconstruction and collective-mode identifiability

## Research Trigger & Context

Following the user's doctoral midterm review directions (iThemba LABS PR295 experiment on $^{133}\text{Ce}$ and CIAE HI-13 experiment on $^{131}\text{Ce}$) and the user-authorized South Africa data archive cleanup, this research note executes a cell-level mathematical reconstruction of the private analysis workbooks (`raw/data/SouthAfrica/133Ce/analysis/figure/wobbling frequency.xlsx`, `raw/data/SouthAfrica/133Ce/analysis/intensity.xlsx`, and `raw/data/SouthAfrica/133Ce/analysis/energy.xlsx`).

The core scientific objective is to determine whether the excited band (designated $W1$ in workbook sheets) in $^{133}\text{Ce}$ ($N=75$) can physically represent a single-phonon transverse or longitudinal wobbling excitation ($n_w=1$), or whether it is an unfavored signature partner band of the $\nu h_{11/2}$ quasiparticle configuration undergoing Coriolis-induced signature inversion and triaxial core coupling.

## Grounded Evidence & Primary Sources

- [[userdata-133ce-southafrica-dataset]]: User-supplied private data archive from iThemba LABS PR295 ($^{118}\text{Sn}(^{18}\text{O}, 3n)^{133}\text{Ce}$, AFRODITE clover array). The derived workbook layer under `raw/data/SouthAfrica/133Ce/analysis/` provides count-level peak areas, ADO/DCO ratios, linear polarization asymmetries, and mixing ratios $\delta$.
- [[nuclearmap-jcnp-pc-pk1]]: Microscopic covariant density functional theory (PC-PK1) potential energy surfaces for neighboring even-even cores:
  - $^{132}\text{Ce}$ ($N=74$): Triaxial minimum at $\beta_2 \approx 0.22\text{--}0.24, \gamma \approx 17^\circ\text{--}20^\circ$;
  - $^{134}\text{Ce}$ ($N=76$): Triaxial minimum at $\beta_2 \approx 0.19\text{--}0.20, \gamma \approx 18^\circ\text{--}22^\circ$.
- [[knowledge/research-notes/133ce-triaxial-core-collective-mode-route-20261101.md]]: Autonomous research route entry point.
- [[knowledge/research-notes/133ce-southafrica-l4-data-contract-20261101.md]]: Local L4 data contract and matrix provenance audit.

## Mathematical & Formula Reconstruction of Workbook Data

### 1. Wobbling Frequency Formula Deconstruction (`wobbling frequency.xlsx`, Sheet 1)

In `raw/data/SouthAfrica/133Ce/analysis/figure/wobbling frequency.xlsx` (Sheet 1), the cell formulas explicitly compute the putative wobbling frequency using the standard literature formula:
$$\hbar\omega_w(I) = E_{\gamma,\text{out}}(I \to I-1) - \frac{1}{2} E_{\gamma,\text{in}}(I \to I-2)$$

When evaluated across the experimental levels of band $W1$ decaying into the yrast $\nu h_{11/2}$ band, the data split into two starkly divergent signature branches:

| Spin $I$ ($\hbar$) | Signature $\alpha$ | Connecting line $E_{\gamma,\text{out}}$ (keV) | In-band line $E_{\gamma,\text{in}}$ (keV) | Formula in Workbook | $\hbar\omega_w$ (keV) |
|---|---|---|---|---|---|
| $13/2^-$ (6.5) | $-1/2$ | 625 | 620 | `=625-620/2` | 315.0 |
| $17/2^-$ (8.5) | $-1/2$ | 582 | 763 | `=582-763/2` | 200.5 |
| $21/2^-$ (10.5) | $-1/2$ | 710 | 896 | `=710-896/2` | 262.0 |
| $25/2^-$ (12.5) | $-1/2$ | 798 | 947 | `=798-947/2` | 324.5 |
| $15/2^-$ (7.5) | $+1/2$ | 608 | 751 | `=608-751/2` | 232.5 |
| $19/2^-$ (9.5) | $+1/2$ | 464 | 856 | `=464-856/2` | 36.0 |
| $23/2^-$ (11.5) | $+1/2$ | 479 | 930 | `=479-930/2` | 14.0 |
| $27/2^-$ (13.5) | $+1/2$ | 485 (1129-644) | 1001 | `=1129-644-1001/2` | $-15.5$ |

**Physical Diagnostics:**
1. **Signature composition**: In the simple harmonic one-phonon picture, the candidate band is expected to follow a definite signature branch. The workbook ledger contains entries assigned to both signatures, which disfavors that simple assignment under the current band mapping; it does not by itself establish a signature-partner identity.
2. **Branch-sensitive staggering**: The workbook construction gives values separated by more than $240\text{ keV}$ between selected entries. This is evidence that the derived quantity is sensitive to signature and line mapping, not an independent measurement of a phonon frequency.
3. **Negative derived entry**: The $-15.5\text{ keV}$ value is a warning about the chosen branch and transition combination. It should not be described as a physical negative phonon energy until the level ledger and response-aware analysis are closed.

### 2. Electromagnetic Transition Ratios & $B(E2)$ Suppression (`intensity.xlsx`)

In `raw/data/SouthAfrica/133Ce/analysis/intensity.xlsx` (`Sheet: branchingratio`), the electromagnetic branching ratios and transition strengths are calculated using:
$$\frac{B(E2,\text{out})}{B(E2,\text{in})} = \frac{I_\gamma(E2,\text{out})}{I_\gamma(E2,\text{in})} \times \left(\frac{E_{\gamma,\text{in}}}{E_{\gamma,\text{out}}}\right)^5$$
and for mixed $\Delta I = 1$ transitions:
$$\frac{B(E2,\Delta I=1)}{B(E2,\Delta I=2)} = \frac{I_\gamma(\Delta I=1)}{I_\gamma(\Delta I=2)} \times \left(\frac{E_2}{E_1}\right)^5 \frac{\delta^2}{1+\delta^2}$$
$$\frac{B(M1,\Delta I=1)}{B(E2,\Delta I=2)} = 0.697 \times 10^{-6} \frac{I_\gamma(\Delta I=1)}{I_\gamma(\Delta I=2)} \left(\frac{E_2^5}{E_1^3}\right) \frac{1}{1+\delta^2} \quad [\mu_N^2 / (e^2 b^2)]$$

The extracted experimental parameters from the workbook are:

| Initial Spin $I_i$ | Transition | $E_\gamma$ (keV) | $\delta$ (workbook) | Multipolarity | $B(E2,\text{out})/B(E2,\text{in})$ | $B(M1)/B(E2)$ [$\mu_N^2/(e^2 b^2)$] |
|---|---|---|---|---|---|---|
| $17/2^-$ (8.5) | $W1 \to \text{yrast}$ ($\Delta I=1$) | 582 | $-0.55$ ($-0.43$ to $-0.80$) | $M1 + E2$ ($76.8\% M1$) | $0.325$ | $0.254$ |
| $17/2^-$ (8.5) | $W1 \to \text{yrast}$ ($\Delta I=2$) | 818 | pure $E2$ | $E2$ | $0.063(25)$ | --- |
| $19/2^-$ (9.5) | $W1 \to \text{yrast}$ ($\Delta I=1$) | 465 | $-0.17$ ($-0.08$ to $-0.37$) | $M1 + E2$ ($97.2\% M1$) | $0.090$ | $0.470$ |
| $19/2^-$ (9.5) | $W1 \to \text{yrast}$ ($\Delta I=2$) | 982 | pure $E2$ | $E2$ | $0.088(33)$ | --- |
| $21/2^-$ (10.5) | $W1 \to \text{yrast}$ ($\Delta I=1$) | 710 | $-5.0$ ($-3.0$ to $-20.0$) | $E2 + M1$ ($96.2\% E2$) | $2.69$ | $0.038$ |
| $21/2^-$ (10.5) | $W1 \to \text{yrast}$ ($\Delta I=2$) | 957 | pure $E2$ | $E2$ | $1.919$ | --- |
| $23/2^-$ (11.5) | $W1 \to \text{yrast}$ ($\Delta I=1$) | 480 | $-5.0$ ($-1.0$ to $-20.0$) | $E2 + M1$ | $2.59$ | $0.017$ |
| $23/2^-$ (11.5) | $W1 \to \text{yrast}$ ($\Delta I=2$) | 1091 | pure $E2$ | $E2$ | $0.068$ | --- |
| $25/2^-$ (12.5) | $W1 \to \text{yrast}$ ($\Delta I=1$) | 798 | $-5.0$ ($-1.0$ to $-20.0$) | $E2 + M1$ | $0.998$ | $0.018$ |
| $25/2^-$ (12.5) | $W1 \to \text{yrast}$ ($\Delta I=2$) | 1084 | pure $E2$ | $E2$ | $0.269$ | --- |

**Conditional interpretation of the electromagnetic decays:**
1. **Suppression of Interband $E2$ Strengths**:
   - In wobbling motion, the wobbling phonon is an oscillatory collective mode about the principal axis of inertia, which generates strong collective $E2$ transitions:
     $$B(E2; n_w=1, I \to n_w=0, I-1) \sim \frac{1}{I} B(E2; \text{in-band}) \sim 0.2\text{--}0.5 \times B(E2; \text{in-band})$$
     and the cross-over interband $E2$ ($I \to I-2$) is strictly forbidden in first order harmonic wobbling.
   - In $^{133}\text{Ce}$, the interband $E2$ strength ratio $B(E2,\text{out})/B(E2,\text{in})$ for the cross-over transitions is severely suppressed:
     $B(E2; 818)/B(E2; 578) = 0.063(25)$ and $B(E2; 982)/B(E2; 608) = 0.088(33)$.
     These selected workbook ratios are below $0.1$, which conditionally disfavors an enhanced interband $E2$ component. Because the mixing-ratio, feeding, efficiency and covariance inputs are not fully closed, the values do not prove the absence of a collective component.
2. **Dominant $M1$ Multipole Character**:
   - For the connecting $\Delta I = 1$ lines at lower spins ($17/2^-$ and $19/2^-$), the measured mixing ratios are small and negative: $\delta(582) = -0.55$ and $\delta(465) = -0.17$.
   - Under the workbook convention, these central values correspond to an $M1$-dominated decomposition. The percentages are derived from workbook mixing-ratio inputs and should not be presented as independently measured multipolarity fractions before the response-aware reanalysis.
   - An $M1$-dominated link is compatible with a signature-partner interpretation, but it is not unique to that interpretation without a frozen transition identity, response model and competing-mode calculation.

### 3. Signature Splitting & Inversion Dynamics (`wobbling frequency.xlsx`, Sheet 2)

In `wobbling frequency.xlsx` Sheet 2 and `energy.xlsx` sheet `133Ce`, the signature splitting function:
$$S(I) = E(I) - \frac{1}{2}[E(I-1) + E(I+1)]$$
was calculated for both the yrast $\nu h_{11/2}$ band and the excited band $W1$:

| Spin $I$ ($\hbar$) | Yrast Band $S(I)$ (keV) | Excited Band $W1$ $S(I)$ (keV) | Phenomenological Pattern |
|---|---|---|---|
| $13/2^-$ | $+182.5$ | --- | Favored signature |
| $15/2^-$ | $-215.5$ | $+137.5$ | Regular staggering |
| $17/2^-$ | $+275.5$ | $-174.5$ | Regular staggering |
| $19/2^-$ | $-316.5$ | $+48.5$ | Staggering dampens |
| $21/2^-$ | $+342.5$ | $+103.5$ | **Signature Inversion** ($S(I)$ stays positive) |
| $23/2^-$ | $-339.5$ | $-171.0$ | Staggering restored |
| $25/2^-$ | $+349.0$ | $+251.5$ | Large staggering restored |

**Physics of Signature Inversion in $A \approx 130$:**
- In the yrast band, the signature splitting is huge ($\pm 200\text{--}350\text{ keV}$), consistent with a decoupled $\nu h_{11/2}$ neutron quasiparticle.
- In band $W1$, the signature splitting starts with regular alternating signs ($+137.5, -174.5\text{ keV}$), but undergoes **signature inversion** around $I = 19/2^-\text{--}21/2^-$, where two consecutive levels have positive $S(I)$ ($+48.5$ and $+103.5\text{ keV}$).
- Signature inversion is an established characteristic of triaxial odd-A and odd-odd nuclei in the $A \approx 130$ region ($^{131}\text{Ba}, {}^{133}\text{Ce}, {}^{134}\text{Pr}$). It arises from the competition between triaxial shape deformation ($\gamma < -30^\circ$ in Lund convention or $\gamma \approx 20^\circ\text{--}30^\circ$), the Coriolis force aligning quasiparticle angular momentum with the rotational axis, and residual neutron-proton interactions or core polarization.

## Model Discrimination & Physical Conclusion

| Criterion | Wobbling Hypothesis ($n_w=1$) | Signature Partner Hypothesis | Experimental Private Data in $^{133}\text{Ce}$ | Verdict |
|---|---|---|---|---|
| Signature structure | A simple one-phonon assignment follows a definite branch | A signature-partner interpretation contains both branches | The workbook ledger contains both assigned signatures | **Disfavors the simple assignment conditionally**; motivates a signature-partner test |
| $\hbar\omega_w(I)$ stability | A phonon construction needs a consistent branch and smooth mapping | Signature splitting/crossing can make the construction branch-dependent | Workbook values show strong branch dependence and one negative derived value | **Shows a mapping problem to resolve**, not a direct phonon measurement |
| Interband multipolarity | Enhanced $E2$ character is a necessary wobbling test | Small $|\delta|$ is compatible with an $M1$-dominated signature link | Selected workbook rows have small central $|\delta|$ | **Conditionally disfavors wobbling**; response and root assumptions remain open |
| $B(E2,\text{out})/B(E2,\text{in})$ | Enhanced out-of-band $E2$ is expected in the relevant wobbling limit | Suppression is compatible with a signature/configuration link | Selected workbook ratios include $0.063(25)$ and $0.088(33)$ | **Supports a suppression pattern conditionally**; not a final absolute-$B(E2)$ result |
| $B(M1)/B(E2)$ strength | The selected wobbling limit requires a small $M1$ component | A sizable $M1$ component is compatible with a signature link | Values are derived from workbook branching and $\delta$ inputs | **Provides a conditional discriminator**; covariance is incomplete |
| Staggering / Inversion | Energy staggering is not a unique mode identifier | Signature inversion is a competing configuration/core explanation | The workbook shows a possible inversion pattern | **Motivates comparison with signature/TiP explanations** |

### Competing Explanations Ranking

1. **Working candidate**: **Unfavored signature partner/TiP-like interpretation**. The workbook-derived pattern is compatible with small-$|\delta|$ links, branch-dependent staggering and suppressed selected $E2$ ratios, but the response-aware joint analysis has not yet been run.
2. **Competing explanation**: **Band crossing and quasiparticle realignment**. The high-spin rows contain broad or incomplete mixing-ratio information and may reflect configuration changes; this requires a frozen transition ledger.
3. **Disfavored conditional hypothesis**: **Simple one-phonon wobbling excitation**. The current reconstruction does not provide the expected clean combination of a single branch, stable phonon spacing and enhanced connecting $E2$, but it is not a publication-grade falsification until response, covariance and holdout checks are complete.

## L4 Readiness & Epistemic Boundaries

- **Readiness State**: `partial-L4-readiness`.
- **Private Data Constraint**: The underlying matrices and workbooks belong to the private user dataset `raw/data/SouthAfrica/` (`publication_status: local-only-unpublished-user-data`). No private numerical tables or event-level matrices may be published without user authorization.
- **Missing Inputs for Full Bayesian L4 Model**:
  1. Full covariance matrix between gated 1D projections (peak fitting currently uses uncoupled 1D Gaussian backgrounds in `Area.cpp`);
  2. In-situ detector efficiency and polarization sensitivity $Q_k(E_\gamma)$ covariance across AFRODITE clover crystals;
  3. Direct conversion electron measurements to independently verify multipolarities without angular-distribution model dependence;
  4. An unexamined gate family reserved as an independent holdout.
- **Non-Fabrication Policy**: We strictly preserve these boundaries. We do not synthesize artificial event-level likelihoods, posterior parameter samples, or unmeasured lifetimes.


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
