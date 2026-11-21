---
type: source
title: "Hyperfine Fields at 66Ga, 67,69Ge Implanted into Iron and Gadolinium Hosts at 6 K, and Applications to g-Factor Measurements"
aliases: [Gray 2020 hyperfine fields, Gray 2020 TDPAD g-factor, Gray 2020 sigma-over-I alignment example]
created: 2026-07-09
updated: 2026-07-09
status: ai-draft
review_status: human-reviewed
source_type: experiment-article
reading_depth: deep-read
title_original: "Hyperfine Fields at 66Ga, 67,69Ge Implanted into Iron and Gadolinium Hosts at 6 K, and Applications to g-Factor Measurements"
authors: [T. J. Gray, A. E. Stuchbery, B. J. Coombes, J. T. H. Dowie, M. S. M. Gerathy, T. Kibedi, G. J. Lane, B. P. McCormick, A. J. Mitchell, M. W. Reed]
journal: Physical Review C
year: 2020
volume: 101
pages: 054302
doi: 10.1103/PhysRevC.101.054302
language: en
canonical_source: doi:10.1103/PhysRevC.101.054302
arxiv: 2206.07294v1
local_edition: arxiv-post-publication
citation_key: gray_2020_Hyperfinefields
raw_file: "raw/papers/2020_Gray et al_Hyperfine fields at Ga 66 , Ge 67 , 69 implanted into iron and gadolinium hosts at 6 K, and applicat.pdf"
raw_sha256: 5374E17E491552A3BA5C68A37732BF4BE27A98C4086DCBC3B63F1C727EE239BF
nuclei: [66ga, 67ge, 69ge]
reactions: ["56Fe(12C,pn)66Ga", "54,56Fe(16O,2pn)67,69Ge", "54Fe(16O,2pn)67Ge"]
observables: [g-factor, attenuation-coefficient]
methods: [time-differential-perturbed-angular-distribution, g-factor-measurement]
tags: [tdpad, g-factor, hyperfine-field, ferromagnetic-host, alignment, sigma-over-i, pado-support]
---

# Gray et al. (2020): Hyperfine Fields and `g`-Factor Measurements

## Bibliographic Record

T. J. Gray et al., *Physical Review C* **101**, 054302 (2020), DOI `10.1103/PhysRevC.101.054302`, citation key `gray_2020_Hyperfinefields`.

The local PDF is the ten-page arXiv:2206.07294v1 posted in June 2022. The journal publication is dated 2020. Its publisher full text was unavailable through the routes checked for this audit. Locators in this note point to the locally verified arXiv PDF.

## Scope and Reading Depth

The 2026-11-21 source audit rechecked the arXiv version and explicitly separated DOI publication identity from the PDF edition and date.

Full PDF text layer was read across pp.1--10. Verification focused on the abstract, experimental setup, the `R(t)` formalism, the amplitude discussion in Sec.VB, the host-comparison boundary, and the conclusion.

This is an `experiment-ingest + method-ingest + project-ingest` source. Its primary subject is TDPAD hyperfine-field / `g`-factor work in Fe and Gd hosts. For the current `sigma-over-i` project, it is a boundary example showing that an empirical alignment expectation can fail in a host-specific isomer / hyperfine-field context.

## Summary

The paper studies `66Ga`, `67Ge`, and `69Ge` isomers recoil-implanted into iron and gadolinium hosts at about `6 K`, using Time Differential Perturbed Angular Distribution (TDPAD) to determine hyperfine magnetic fields and measure `g` factors. The authors conclude that gadolinium can serve as a suitable host for precision TDPAD `g`-factor work under controlled conditions, and they report new `g`-factor values consistent with previous literature.

For the current project, the key point is the amplitude analysis: the paper compares measured `R(t)` amplitudes with empirical alignment expectations and concludes that the produced alignment is significantly lower than the empirically expected `sigma/I ≈ 0.35`. If one assumes `100%` full-field implantation sites, the observed amplitudes would require `sigma/I ≈ 0.9`. The authors warn that `R(t)` amplitude alone is not a reliable measure of field-free fraction unless the alignment is independently constrained.

## Experimental or Theoretical Setup

- Four runs at the ANU Heavy Ion Accelerator Facility with pulsed `48 MeV` `12C` and `60 MeV` `16O` beams.
- Reaction/target combinations include `56Fe(12C,pn)66Ga`, `54,56Fe(16O,2pn)67,69Ge`, and `54Fe(16O,2pn)67Ge`.
- Host foils were iron or gadolinium, polarized by an external `~0.1 T` field and cooled to `5.7(1) K`.
- Two HPGe and two LaBr3 detectors were used in runs 1, 2, and 4; four LaBr3 detectors in run 3.
- The measured observables are time-dependent perturbed angular distributions `R(t)`, from which Larmor frequencies, hyperfine fields, and `g` factors are extracted.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| G20-1 | 本文把 `66Ga`, `67Ge`, `69Ge` isomers recoil-implant 到 `Fe` 和 `Gd` ferromagnetic hosts（约 `6 K`），并用 TDPAD 测量 hyperfine magnetic fields；同时给出 `g(66Ga,7-) = +0.126(4)`、`g(67Ge,9/2+) = -0.1932(22)` 和 `g(67Ge)/g(69Ge) = 0.869(9)`。 | observed-fact | direct | Abstract; p.8, Sec.VI | false |
| G20-2 | TDPAD 分析中构造 `R(t) = (N1-N2)/(N1+N2) ≈ [3a2/(4+a2)] sin(2ωL t)`，其中 `a2 = A2 B2`，`B2` 表示 isomeric state 的 spin alignment，`ωL` 与 `g` 和 `Bhf` 相关。 | method-formalism | direct | p.3, Sec.III, Eqs.1--2 | false |
| G20-3 | 若有比例 `p` 的 implantation 位点为 low-field 或 field-free，`R(t)` 振幅会按 `R(t) ≈ (1-p)[3a2/(4+a2)] sin(2ωL t)` 缩小；因此只有在 alignment 已知时，`R(t)` 振幅才能被安全用于估计 field-free fraction。 | method-formalism | direct | p.4, Sec.III, Eq.3 and following text | false |
| G20-4 | 论文把 fusion-evaporation 后的 nuclear alignment 经验地写成 oblate Gaussian `m`-substate distribution，典型 standard deviation 为 `sigma ≈ 0.35 I`；作者把这条经验规则当作估计 `B2` 与 `a2` 的背景。 | experimental-practice | direct | p.4, Sec.III, text after Eq.3 | false |
| G20-5 | 本文观测到的初始 `R(t)` amplitudes 在不同案例间彼此相近，也与先前 Fe/Cu host 的 full-alignment-style amplitudes 相近。 | observed-fact | direct | p.7, Sec.VB, first two paragraphs | false |
| G20-6 | 作者据 `R(t)` amplitudes 解释：这些 isomeric states 的 alignment 明显低于经验预期 `sigma/I ≈ 0.35`；若假设 `100%` full-field implantation sites，则需要 `sigma/I ≈ 0.9` 才能解释 Fig.3、6、7 的 amplitudes。 | author-interpretation | direct | Abstract; p.7, Sec.VB | false |
| G20-7 | 作者强调 `R(t)` 单独并不是可靠的 field-free fraction 指标；需要 external-field measurement、对 full-field-site amplitude 的独立标定，或对附近非 isomeric states 的 angular-distribution measurement 来验证 nuclear alignment。 | author-interpretation | direct | p.7, Sec.VB; p.8, Sec.VI | false |
| G20-8 | 本文进一步警告，经验规则 `sigma/I ≈ 0.35` 源自 prompt decays；若直接把它套用于可能具有不同 feeding pattern 的 isomeric states，需要谨慎。 | author-interpretation | direct | p.7, Sec.VB, paragraph beginning "The empirical rule..." | false |
| G20-9 | 对 gadolinium hosts，作者认为在较低 beam intensity 和稳定条件下可以得到可重复的 `Bhf` 分布，并据此认为 Gd 可作为 precision TDPAD `g`-factor measurement 的合适 host。 | author-interpretation | direct | Abstract; p.8, Secs.VC and VI | false |

## Nuclear Structure Information

This source is not mainly a level-scheme paper. Its nucleus-specific structure content is limited to the isomer properties used for the TDPAD and `g`-factor analyses, plus the configuration interpretation supported by the measured `g` factors.

## Authors' Interpretation

- The measured `g` factors support the `[pi f5/2 ⊗ nu g9/2]7-` assignment for the `66Ga` isomer.
- The reduced `R(t)` amplitudes are interpreted primarily as an alignment issue rather than direct evidence for large field-free fractions.
- Gadolinium is interpreted as a viable TDPAD host when beam conditions avoid the radiation-damage problems encountered in earlier work.

## Model Results

None in the shell-model / collective-structure sense. The paper uses empirical host/alloy arguments and magnetic-precession formalism rather than a dedicated nuclear-structure calculation.

## Competing Interpretations and Limitations

- The source is a TDPAD / hyperfine-field / `g`-factor paper, not a P-ADO or mixing-ratio paper.
- The `sigma/I ≈ 0.35` statement is an empirical background rule imported into the amplitude discussion, not a directly measured universal constant.
- The stronger `sigma/I ≈ 0.9` inference depends on assuming `100%` full-field implantation sites.
- The host behavior is material-specific; Fe/Gd implantation-site physics and radiation-damage issues should not be generalized to all fusion-evaporation spectroscopy contexts.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source provides a useful boundary case: even when an empirical alignment expectation such as `sigma/I ≈ 0.35` is common in practice, an actual isomeric TDPAD dataset can show substantially lower effective alignment and can require independent verification of what the amplitude means.

The boundary is equally important: this is not a direct angular-distribution or mixing-ratio extraction source. It should be cited as host- and method-specific evidence that empirical alignment assumptions may fail, not as a universal correction for P-ADO.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts: [[sigma-over-i]], [[spin-alignment]]
- Methods: [[time-differential-perturbed-angular-distribution]], [[g-factor-measurement]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Human Review Triage

- P0 focus resolved: `G20-4`, p.4 Sec.III. The paper presents `sigma ≈ 0.35 I` as an empirical alignment background for fusion-evaporation reactions, not as a measurement from this experiment.
- P0 focus resolved: `G20-6`, Abstract + p.7 Sec.VB. The Wiki keeps the "lower than expected" alignment statement and the inferred `sigma/I ≈ 0.9` explicitly tied to the `100%` full-field assumption.
- P0 focus resolved: `G20-7/G20-8`, p.7--8. The source explicitly warns against reading field-free fraction directly from `R(t)` amplitude and against blindly transferring the prompt-decay empirical rule to isomeric states.
- Remaining P0: none identified beyond the host-specific / empirical-rule boundary after the 2026-07-09 user review.
- P1: `G20-2/G20-3`, p.3--4, for the `R(t)` and amplitude formalism.
- P1: `G20-1`, Abstract / p.8, for the reported `g` values and overall host-comparison scope.
- P1: `G20-9`, p.8 conclusion, for the qualified statement that gadolinium can serve as a suitable TDPAD host.

## Personal Notes

This source is valuable to the project precisely because it is not a P-ADO paper. It shows that an empirical alignment-width expectation can fail in a nearby spectroscopy method, and that one must separate "reduced amplitude due to weaker alignment" from "reduced amplitude due to field-free sites" unless independent information is available.

Additional sigma-scale factors worth retaining from this source:

- `R(t)` amplitude depends on `A2 B2`, so the inferred alignment scale is coupled to both the transition anisotropy term and the state-alignment term.
- A field-free or low-field site fraction `p` suppresses the same amplitude, so weaker `R(t)` does not map one-to-one onto weaker alignment.
- The empirical `sigma/I ≈ 0.35` benchmark was built from prompt decays; isomeric feeding can populate different magnetic-substate patterns.
- Independent angular-distribution measurements on nearby non-isomeric states can provide an external alignment calibration.
- Host/site assumptions matter: full-field occupancy, host material, and beam-damage conditions all feed into the apparent sigma-scale inference.

## 2026-11-21 — Conditional amplitude interpretations

ArXiv pp. 6–7, Sec. V B states two conditional interpretations of the small \(R(t)\) amplitudes. Adopting the prompt-state empirical \(\sigma/I\approx0.35\) gives about 60% field-free sites. Assuming full-field sites gives a width near 0.9. The authors prefer weaker initial alignment based on comparison with other implantation and external-field experiments, and call for independent alignment information. The two widths are model conditions for isomeric TDPAD, with no numerical \(P\)–\(\delta\) result for this survey.
