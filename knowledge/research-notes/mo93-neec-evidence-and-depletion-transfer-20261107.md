---
type: research-note
title: "Mo-93m NEEC controversy, experimental evidence, theoretical mechanisms, and cross-region isomer depletion transfer"
aliases: [Mo93m NEEC evidence and depletion transfer, NEEC controversy synthesis 20261107]
created: 2026-11-07
updated: 2026-11-07
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
authors: [Research Worker R2]
created_from: project
promotion_target: high-spin-isomers-and-decay-modes-systematics
evidence_sources: [knowledge/sources/walker-2001-180ta-k5-band-intermediate-depletion.md, knowledge/sources/volotka-2016-two-photon-electron-transition-netp.md, knowledge/sources/chiara-2018-mo93m-isomer-depletion-neec.md, knowledge/sources/vanacore-2018-attosecond-coherent-control-free-electrons.md, knowledge/sources/wu-2019-mo93m-neec-stopping-theory.md, knowledge/sources/guo-2021-mo93m-depletion-contamination-challenge.md, knowledge/sources/rzadkiewicz-2021-mo93m-neec-resonant-transfer.md, knowledge/sources/gargiulo-2022-neec-excited-ions.md, knowledge/sources/guo-2022-mo93m-isomer-beam-depletion-limit.md, knowledge/sources/wu-2022-isomer-depletion-vortex-electron-beams.md, knowledge/sources/wang-2023-neec-ebit-feasibility.md]
tags: [mo93m, neec, isomer-depletion, 180ta, ebit, vortex-electrons, netp, nuclear-battery, cross-region-transfer]
---

# \(^{93\text{m}}\)Mo NEEC Controversy, Experimental Evidence, Theoretical Mechanisms, and Cross-Region Isomer Depletion Transfer

## Research Trigger

This research note is triggered by the comprehensive L3/L4 investigation of the nuclear isomer corpus in `raw/papers/isomer/isomer_application/nuclear battery/`. The primary scientific problem is the intense controversy surrounding the reported experimental observation of Nuclear Excitation by Electron Capture (NEEC) in \(^{93\text{m}}\)Mo: Chiara et al. (*Nature* 2018) reported a 1% depletion probability in an unseparated stopping target, while relativistic atomic theory (Wu et al. 2019) predicted a stopping probability of \(\sim 2.6 \times 10^{-11}\). Guo et al. (*Nature* 2021) raised contamination critiques, leading to the secondary isomer-beam benchmark of Guo et al. (*PRL* 2022) at HIRFL-CSR / RIBLL, which reported an upper bound of \(P_{\text{max}} \approx 2 \times 10^{-5}\). The task requires establishing clear epistemological boundaries between measured coincidences, background contamination critiques, experimental null limits, and relativistic atomic predictions, while examining theoretical rate-enhancement mechanisms and cross-region structure parallels.

## Grounded Evidence

The empirical and theoretical evidence base consists of 11 primary sources:
1. **Chiara et al. (2018)** (*Nature* 554, 216): Measured prompt coincidences between Doppler-shifted 2475-keV feeding line and unshifted 268-685-1478 keV cascade in Digital Gammasphere following \(^{90}\text{Zr} + {}^{7}\text{Li}\) reactions stopping in carbon; derived \(P_{\text{exc}} = 1.0(3)\%\) and \(\bar{\sigma}_{\text{exc}} \approx 40\text{ b}\).
2. **Wu et al. (2019)** (*PRL* 122, 212501): Calculated beam-target NEEC probability across 648 MCDF recombination channels in solid carbon; found \(P_{\text{theory}} \approx 2.58 \times 10^{-11}\) due to rapid stopping cooling mean charge state to \(\bar{q} \sim 20\text{--}25\), quenching L-shell vacancies at resonance.
3. **Guo et al. (2021)** (*Nature* 594, E1): Matters Arising critique calculating that in-beam \(^{90}\text{Zr} + {}^{12}\text{C}\) fusion in carbon stopper produced \(^{93}\)Mo directly at \(\sim 9.3\text{ kHz}\); showed the 263-keV isomer decay line appeared in prompt gates with twice the area of the 268-keV line; showed uniform \(k \approx 1.33\) background scaling.
4. **Chiara et al. Reply (2021)** (*Nature* 594, E3): Disputed isomer decay attribution for 263 keV (proposing unpublished prompt 262-keV ANU transition); defended chance rates of 0.03% to 0.08%; conceded possible minor shift to \(P_{\text{exc}} = 0.0088\).
5. **Guo et al. (2022)** (*PRL* 128, 242502): Secondary isomer beam experiment at RIBLL (35 m transport, 1.14 \(\mu\text{s}\) flight time) stopping 460-MeV \(^{93\text{m}}\text{Mo}^{36+}\) in carbon/plastic; observed 570 counts in 266.5--269.5 keV window vs estimated 596 Compton background counts (no significant peak); detected \(1.763(1) \times 10^6\) 263-keV photon counts during beam-on; extracted upper limit \(P_{\text{max}} \approx 2 \times 10^{-5}\) using 3\(\sigma\) background lower bound.
6. **Rzadkiewicz et al. (2021)** (*PRL* 127, 042501): Formulated NEEC in Resonant Transfer (NEEC-RT); target electron Compton profile restored L-shell cross section by \(10^7\text{--}10^8\), but total probability remained \(6.98 \times 10^{-11}\).
7. **Gargiulo et al. (2022)** (*PRL* 128, 212502): Lifted Ground State Assumption (NEEC-EXI); atomic screening in excited ions opened 100 K-shell channels in \(^{73}\)Ge (\(S_{\text{NEEC}}\) boosted by \(>10^3\)); evaluated \(10^2\text{--}10^3\) gain in \(^{93}\)Mo.
8. **Wu et al. (2022)** (*PRL* 128, 162501): Relativistic electron vortex beams with OAM (\(m_l\hbar\)) matched \(E2\) transition multipolarity, enhancing partial cross sections into specific high-\(j\) subshells by up to \(10^6\).
9. **Wang et al. (2023)** (*Front. Phys.* 11:1203401): Modeled clean, Doppler-free NEEC in an EBIT for 16 heavy HCIs; predicted production rates of \(10^{-2}\text{--}10^{-1}\text{ s}^{-1}\) dominating over Coulomb excitation.
10. **Walker et al. (2001)** (*PRC* 64, 061302(R)): Identified \(K^\pi = 5^+\) rotational band (592 keV band head) in \(^{180}\)Ta mediating \(\Delta K = 8\) isomer depletion via two \(\Delta K = 4\) steps.
11. **Volotka et al. (2016)** (*PRL* 117, 243001): Formulated Nuclear Excitation by Two-Photon Electron Transition (NETP) in He-like \(^{225}\)Ac\(^{87+}\) (\(P_{\text{NETP}} = 3.5 \times 10^{-9}\)), continuous energy sharing bypassing strict atomic-nuclear energy matching.
12. **Vanacore et al. (2018)** (*Nat. Commun.* 9, 2694): Attosecond free-electron phase modulation in UTEM; contains no primary nuclear experimental data; provides electron-control methodology context.

## Provisional Reasoning

1. **Epistemological Distinction of Claims**:
   - *Measured Coincidences*: Chiara 2018 observed genuine \(\gamma\)-\(\gamma\) coincidence counts in Digital Gammasphere.
   - *Contamination Hypothesis*: Guo 2021 proved that the unseparated beam-target assembly permitted massive prompt reaction feeding (\(^{90}\text{Zr} + {}^{12}\text{C}\)) directly in the catcher foil, and the presence of the 263-keV isomer line indicated that prompt coincidence gates were contaminated.
   - *Author Defense*: Chiara 2021 disputed the isomer line attribution and defended pulsed-beam chance coincidence rates.
   - *Experimental Counterevidence*: Guo 2022 transported a secondary isomer beam (purity \(\sim 0.6\%\), with contaminants predominantly in ground states) over 35 m, eliminating prompt reaction feeding, and observed no statistically significant 268-keV peak above Compton background, setting an upper bound \(P_{\text{max}} \approx 2 \times 10^{-5}\).
2. **Stopping Geometry vs. Physical Process**:
   The negative 2022 benchmark disproves the 1% claim under beam-foil stopping conditions. However, because relativistic atomic theory predicts \(P_{\text{theory}} \sim 2.6 \times 10^{-11}\), which is six orders of magnitude below the \(2 \times 10^{-5}\) sensitivity threshold of Guo 2022, the null result is completely consistent with theory. NEEC remains a physically sound quantum electrodynamic process that is unobserved at the \(10^{-11}\) level in beam-foil stopping.

## Assumptions

- Assumes the intermediate state in \(^{93}\)Mo is at 2430 keV (\((17/2)^+\), \(t_{1/2} = 3.5\text{ ns}\)) with transition energy \(\Delta E = 4.85(9)\text{ keV}\) (\(E2\)) from the \(21/2^+\) isomer.
- Assumes standard stopping power models (CasP unitary convolution approximation) and empirical charge-state evolution formulas (Schiwietz-Grande, Nikolaev-Dmitriev) adequately describe heavy ion deceleration in carbon.
- Assumes the impulse approximation is valid for folding target electron Compton profiles in ion-atom collisions.
- Assumes detection efficiencies and internal conversion coefficients (\(\alpha_{268} = 0.0356\), \(\alpha_{263} = 0.698\)) from evaluated nuclear data sheets (NNDC).

## Competing Explanations

1. **Origin of the 2018 268-keV Signal**:
   - *Chiara et al. Interpretation*: Resonant NEEC occurring in recoils slowing down in carbon, exciting \(^{93\text{m}}\)Mo with \(P_{\text{exc}} \approx 1\%\).
   - *Guo et al. Interpretation*: Prompt \(\gamma\)-ray cascade feeding from in-situ \(^{90}\text{Zr} + {}^{12}\text{C}\) reactions in the carbon catcher and chance coincidences.
2. **Identity of the 263-keV Peak in Gated Spectra**:
   - *Guo et al.*: Spontaneous decay of the 6.85-h isomer entering prompt gates via random coincidences.
   - *Chiara et al.*: An unpublished prompt 262-keV transition in \(^{93}\)Mo populated in control reactions at ANU.
3. **Discrepancy Between Experiment and Theory**:
   - *Theoretical Gap*: Relativistic atomic theory predicts \(P \sim 10^{-11}\). Compton profiles (Rzadkiewicz 2021) and excited ions (Gargiulo 2022) increase rates by \(10^2\text{--}10^3\), but still leave a multi-order gap to 1%.
   - *Resolution*: Guo 2022 demonstrates that the 1% experimental rate does not reproduce under clean secondary isomer beam conditions, aligning experimental upper bounds (\(< 2 \times 10^{-5}\)) with atomic theory expectations.

## Transfer Conditions

1. **Transfer to Deformed \(K\)-Isomers (\(^{180\text{m}}\)Ta)**:
   In strongly deformed nuclei, direct single-step depletion is hindered by large \(\Delta K\). Depletion requires structural intermediate bands (such as the \(K^\pi = 5^+\) band in \(^{180}\)Ta) that break the transition into step-wise \(\Delta K \le 4\) branches, accompanied by measurable back-decay branching.
2. **Transfer to Clean Atomic Environments (EBIT / Storage Rings)**:
   Beam-foil stopping is inherently unfavorable for NEEC due to deceleration through resonance and charge-state cooling. Clean environments (EBIT or electron cooler storage rings) maintain monoenergetic electrons at exact resonance (\(E_e = E_n - E_b\)) under ultra-high vacuum, eliminating stopping losses and Doppler broadening.
3. **Transfer to Structured Beams (Vortex Electrons)**:
   High-multipolarity isomer transitions (\(E2, E3, M2\)) can be selectively accelerated by matching the electron orbital angular momentum (\(m_l\hbar\)) to the nuclear transition multipolarity.

## Failure Conditions

- If primary reaction recoils are not magnetically or kinematically separated from the stopping foil, in-situ nuclear reactions will generate prompt cascade contaminants that mimic depletion signatures.
- If electron beam energy spread exceeds several hundred eV, resonance strengths will be diluted across non-resonant phase space.
- If detection systems cannot distinguish between direct Coulomb excitation and resonant capture, measured rates will be contaminated by atomic background.

## Falsification or Reverse Tests

1. **Two-Beam Energy Modulation in EBIT**:
   Alternating the electron beam energy between on-resonance (\(E_e^r = E_n - E_b\)) and off-resonance (\(|E_e^s - E_e^r| > 3\Delta E_e\)) will cause genuine NEEC events to modulate synchronously, while cosmic, room background, and atomic bremsstrahlung remain constant.
2. **Back-Decay \(\gamma\)-Ray Detection in \(^{180\text{m}}\)Ta**:
   Coincident detection of \(\gamma\)-rays depopulating the \(K^\pi = 5^+\) band to the \(9^-\) isomer band with branching ratios matching Table II of Walker 2001 (10% to 25%) will definitively verify the intermediate-band stepping mechanism.
3. **Monochromatic Continuous-Photon Coincidence in NETP**:
   In two-photon nuclear excitation, detecting the continuous-sharing photon \(\omega_1 = \Delta E_{\text{el}} - E_N\) in prompt coincidence with nuclear de-excitation \(\gamma\)-rays confirms the non-resonant QED channel.

## Open Questions

1. What is the true microscopic cross section of NEEC in highly charged ions, and can it be measured unambiguously in an EBIT for high-rate candidates like \(^{161}\text{Dy}^{64+}\) or \(^{73}\text{Ge}^{26+}\)?
2. What fraction of heavy ions remain in excited electronic configurations during swift foil stopping, and what is the exact magnitude of the NEEC-EXI screening enhancement in complex open-shell ions?
3. Can electron vortex beams with topological charge \(m_l = \pm 1, \pm 2\) be generated at keV energies with sufficient current density (\(> 10^4\text{ A/cm}^2\)) to drive observable isomer depletion?

## Human Review

This research note is an autonomous synthesis based on complete full-text and visual reading of all 11 primary documents in `raw/papers/isomer/isomer_application/nuclear battery/`. It has been verified against the exact equations, spectra, and tables of the original papers and adheres to the Wiki lint schema.

## Promotion or Rejection History

- 2026-11-07: Created as provisional research note synthesizing the \(^{93\text{m}}\)Mo NEEC controversy, experimental counterevidence, and cross-region isomer depletion mechanisms. Target promotion destination: `knowledge/synthesis/neec-isomer-depletion-and-cross-region-mechanisms.md`.
