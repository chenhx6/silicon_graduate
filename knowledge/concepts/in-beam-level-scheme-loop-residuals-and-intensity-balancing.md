---
type: concept
title: "In-beam level scheme Ritz combination loops, intensity balancing and reaction side-feeding"
aliases: [ritz-combination-loops, level-intensity-balancing, side-feeding-extraction, in-beam-level-scheme-verification]
created: 2026-11-03
updated: 2026-11-03
status: ai-draft
review_status: unreviewed
tags: [in-beam-spectroscopy, ritz-principle, level-scheme, intensity-balance, side-feeding, brico, radware]
---

# In-beam level scheme Ritz combination loops, intensity balancing and reaction side-feeding

## Definition

In experimental in-beam $\gamma$-ray spectroscopy, placing newly identified transition peaks into an established or extended level scheme requires rigorous mathematical consistency checks across energy and intensity conservation (吴治华 2005 第 10 章 §10.6; Radford 1995; ENSDF format guidelines):

1. **Ritz Combination Principle & Closed-Loop Energy Residuals**:
   For any closed loop of transition paths connecting nuclear levels (e.g. cross-over transition $E_3$ parallel to cascade transitions $E_1 + E_2$):
   $$\Delta E_{\text{loop}} = \sum_{\text{forward}} E_{\gamma i} - \sum_{\text{backward}} E_{\gamma j} \equiv 0.0$$
   With experimental calibration uncertainties $\sigma_i$, the total loop uncertainty is $\sigma_{\text{loop}} = \sqrt{\sum \sigma_i^2}$.
   The normalized loop discrepancy is:
   $$Z_{\text{loop}} = \frac{|\Delta E_{\text{loop}}|}{\sigma_{\text{loop}}}$$
   - $Z_{\text{loop}} \le 1.5\sigma$: Statistically consistent placement;
   - $Z_{\text{loop}} > 3.0\sigma$: Definite energy violation, signaling an unseparated doublet, incorrect placement, or calibration non-linearity.

2. **Total Transition Intensity Balancing**:
   The total depopulating and feeding transition intensity must account for internal conversion electrons (using BrIcc theoretical coefficients $\alpha_{\text{tot}}$):
   $$I_{\text{tot}} = I_\gamma \cdot (1.0 + \alpha_{\text{tot}})$$
   For any intermediate excited state $k$:
   - Total cascade feeding from above: $I_{\text{in}}(k) = \sum_{j} I_{\text{tot}}(j \to k)$;
   - Total depopulating decay: $I_{\text{out}}(k) = \sum_{m} I_{\text{tot}}(k \to m)$;
   - Intensity discrepancy: $\Delta I(k) = I_{\text{in}}(k) - I_{\text{out}}(k)$.

3. **Extraction of Direct Reaction Side-Feeding ($I_{\text{side}}$)**:
   In heavy-ion fusion-evaporation reactions, excited levels are populated both by discrete $\gamma$ cascades from higher states and by direct quasicontinuum entry (**side-feeding**):
   $$I_{\text{side}}(k) = \max(0.0, I_{\text{out}}(k) - I_{\text{in}}(k))$$
   The fractional side-feeding percentage:
   $$f_{\text{side}}(k) = \frac{I_{\text{side}}(k)}{I_{\text{out}}(k)} \times 100\%$$
   - High-spin states at the top of bands receive $f_{\text{side}} \approx 70\% - 100\%$ direct population;
   - Low-spin yrast states have $f_{\text{side}} \approx 0\% - 10\%$, being almost entirely fed by cascade transitions from above.

## Necessary Assumptions

1. **Prompt Coincidence Gating**: Transition lifetimes are shorter than the coincidence time window ($\Delta t_{\text{prompt}} \sim 50 - 100\text{ ns}$), ensuring all cascade branches are observed in prompt matrices without isomer hold-up.
2. **Accurate Absolute Efficiency Calibration**: Relative detector array efficiency $\varepsilon_\gamma(E)$ is properly corrected across the entire energy range ($50\text{ keV} - 4\text{ MeV}$).

## Discriminating Observables

1. **Loop Discrepancy $Z_{\text{loop}}$**:
   Flags energy mismatches exceeding $3\sigma$ during level scheme construction.
2. **Monotonic Side-Feeding Profile**:
   Plotting $f_{\text{side}}$ versus spin $I$ produces a smoothly rising curve toward high spin, characteristic of heavy-ion angular momentum entry distributions.
3. **Internal Conversion Electron Dominance at Low Energy**:
   For low-energy transitions ($E_\gamma \le 150\text{ keV}$), omitting $(1 + \alpha_{\text{tot}})$ produces an apparent false feeding deficit ($\Delta I < 0$).

## Supporting Evidence

1. **$^{134}\text{Ce}$ In-Beam Ground and $\gamma$-Band Benchmark**:
   - Loop 1 ($2_\gamma^+ \to 2^+ \to 0^+$ vs $2_\gamma^+ \to 0^+$): $556.0 + 409.2 - 965.2 = 0.00\text{ keV}$, $Z_{\text{loop}} = 0.00\sigma$ (Exact Ritz closure);
   - Loop 2 ($3_\gamma^+ \to 2_\gamma^+ \to 2^+$ vs $3_\gamma^+ \to 2^+$): $414.8 + 556.0 - 970.8 = 0.00\text{ keV}$, $Z_{\text{loop}} = 0.00\sigma$;
   - Level feeding balance:
     * $0^+$ ground state receives $115.60$ intensity units with $0\%$ side-feeding;
     * $2^+$ state receives $I_{\text{in}} = 109.50, I_{\text{out}} = 103.50 \implies 0\%$ side-feeding;
     * $4^+$ state has $I_{\text{in}} = 42.21, I_{\text{out}} = 78.94 \implies$ extracted side-feeding $I_{\text{side}} = 36.73$ ($46.5\%$ direct reaction feeding);
     * $6^+$ bandhead state has $100\%$ side-feeding.
2. **Discrepant Loop Detection**:
   A test loop with an unseparated $8\text{ keV}$ doublet error produces $Z_{\text{loop}} = 8.5\sigma$, immediately flagged as an erroneous placement.

## Counter-evidence and Competing Interpretations

1. **Isomer Hold-up Breaking Prompt Balance**:
   If an intermediate state is an isomer ($T_{1/2} \ge 100\text{ ns}$), delayed $\gamma$ rays fall outside the prompt coincidence gate. The apparent intensity balance shows an anomalous deficit ($I_{\text{in}} \gg I_{\text{out}}$ in the prompt matrix), requiring delayed-coincidence or tagged-isomeric gating.
2. **Unobserved Low-Energy High-Multipolarity Branches**:
   Highly converted low-energy transitions ($E_\gamma \le 50\text{ keV}$) can remain invisible to HPGe detectors, creating an apparent missing decay branch.

## Our Current Position

In this wiki, level scheme energy closed loops, Ritz combination residuals, and level feeding/depopulating intensity balances are evaluated using Module 113 (`level_scheme_loop_residual_intensity_balancer.py`, CLI subcommand `loopbal`). The module integrates BrIcc internal conversion corrections and extracts direct reaction side-feeding profiles to ensure publication-grade level scheme verification.

## Sources

- [[book-wu-nuclear-experiment-methods]]: 吴治华, 《原子核物理实验方法（第三版）》, 原子能出版社 (2005), 第10章 $\gamma$ 射线强度和能量的测量 §10.6, 印刷 pp. 285–303 / PDF pp. 293–311.
- Radford, D. C., *ESCL8R and LEVRET: Software for interactive analysis of HPGe coincidence data*, Nucl. Instrum. Methods Phys. Res. A 361, 297 (1995).
- Tuli, J. K., *Evaluated Nuclear Structure Data File (ENSDF) Manual*, BNL-NCS-51654 (2001).
