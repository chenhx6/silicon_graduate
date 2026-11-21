---
type: source
title: "Core-Coupled Protons, f7/2 Intruder States, and Competing g9/2 Proton and Neutron Structures in 65,67 Cu"
aliases: [Chiara 2012 Cu65 Cu67 high-spin spectroscopy, Chiara 2012 sigma-over-I example, Chiara 2012 core-coupled protons]
created: 2026-07-09
updated: 2026-07-09
status: ai-draft
review_status: human-reviewed
source_type: experiment-article
reading_depth: deep-read
title_original: "Core-Coupled Protons, f7/2 Intruder States, and Competing g9/2 Proton and Neutron Structures in 65,67 Cu"
authors: [C. J. Chiara, I. Stefanescu, W. B. Walters, S. Zhu, R. V. F. Janssens, M. P. Carpenter, R. Broda, B. Fornal, A. A. Hecht, N. Hoteling, E. G. Jackson, B. P. Kay, W. Krolas, T. Lauritsen, E. A. McCutchan, T. Pawlat, D. Seweryniak, X. Wang, A. Wohr, J. Wrzesinski]
journal: Physical Review C
year: 2012
volume: 85
pages: 024309
doi: 10.1103/PhysRevC.85.024309
language: en
canonical_source: doi:10.1103/PhysRevC.85.024309
citation_key: chiara_2012_Corecoupledprotons
raw_file: "raw/papers/2012_Chiara et al_Core-coupled protons, f 7  2 intruder states, and competing g 9  2 proton and neutron structures i.pdf"
raw_sha256: 04DE66C55BF90B676E23ADFDA513686CA5497DC7A0691E1A6288C38D833EB10C
nuclei: [65cu, 67cu]
reactions: ["238U(64Ni,X)65Cu", "238U(64Ni,X)67Cu", "26Mg(48Ca,X)65Cu"]
observables: [angular-distribution-coefficient, multipole-mixing-ratio]
methods: [angular-correlation, angular-distribution]
tags: [cu65, cu67, deep-inelastic, angular-distribution, angular-correlation, sigma-over-i, pado-support]
---

# Chiara et al. (2012): `65,67Cu` Core-Coupled Proton Structures

## Bibliographic Record

C. J. Chiara et al., *Physical Review C* **85**, 024309 (2012), DOI `10.1103/PhysRevC.85.024309`, citation key `chiara_2012_Corecoupledprotons`.

The raw PDF is `1025484` bytes with local timestamp `2026-07-01 03:01:07`; SHA-256 is recorded above.

## Scope and Reading Depth

Full PDF text layer was read across pp.1--20. The main verification target for this ingest was the experimental setup, the AC/AD methodology, Table II-III, Fig.3, the 65Cu `1115 keV` mixing-ratio discussion, and the concluding shell-model interpretation.

This is an `experiment-ingest + targeted-ingest + project-ingest` source. Its primary value is as a `65,67Cu` nuclear-structure experiment. For the current `sigma-over-i` project, the `σ/I` content is only a targeted experimental-practice example and should not be promoted to a universal alignment prescription.

## Summary

The paper studies moderate-spin states in `65,67Cu` using a `430 MeV` `64Ni` beam on a thick `238U` target at ATLAS with the Gammasphere array. The authors extend the decay schemes of both nuclei, use angular correlations and angular distributions to constrain spin/parity assignments, identify positive-parity structures in both nuclei, and in `67Cu` observe a negative-parity dipole band built on a `πf7/2^-1` configuration.

For the current project, the key targeted point is methodological rather than structural: the `65Cu` angular-distribution analysis assumes `σ/I = 0.5` because that choice reproduces known `E2` and `E1` transitions. The same paper then notes that for the `1115 keV` transition a fit with `σ/I = 0.5` gives `δ ≈ -0.1`, while `σ/I ≈ 0.7` shifts the fit toward the larger-magnitude adopted / literature `δ` values. This is a practice-level example that extracted `δ` can depend on the assumed alignment width.

## Experimental or Theoretical Setup

- Main spectroscopy dataset: `430 MeV` `64Ni` beam on a `55 mg/cm2` enriched `238U` target at ATLAS; Gammasphere with 100 Compton-suppressed HPGe detectors; `2.5 x 10^9` clean fold-3-or-greater events.
- Prompt triple-coincidence analysis used the PPP cube; delayed PPD/PDD/DDD cubes were also checked, but no `>= 20 ns` delayed decays were identified in `65,67Cu`.
- Angular-correlation analysis divided detector pairs into 10 angle groups and fitted `W(psi)=a0[1+a2 P2(cos psi)+a4 P4(cos psi)]`.
- Because many `65Cu` AC gates were inconclusive, the paper also used a separate `48Ca + 26Mg` Gammasphere dataset for double-gated angular distributions, with seven detector-angle groups at `17, 35, 50, 58, 70, 80, 90 deg`.

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| CH12-1 | 本文用 ATLAS `430 MeV` `64Ni` 束打厚 `238U` 靶，并用 100 探头的 Gammasphere 记录 `2.5 x 10^9` 个 clean fold-3-or-greater 事件，以扩展 `65,67Cu` 的中等自旋 decay scheme。 | observed-fact | direct | Abstract; p.2, Sec.III | false |
| CH12-2 | `65,67Cu` 的 angular-correlation 分析把探头对分成 10 个相对角度组，并用 `W(psi)=a0[1+a2 P2(cos psi)+a4 P4(cos psi)]` 的 Legendre 形式提取 `a2,a4` 以判别多极性。 | method-formalism | direct | p.2, Sec.IV; Table I | false |
| CH12-3 | 对 `65Cu`，作者另用 `48Ca + 26Mg` 实验做 double-gated angular-distribution 分析；Table II 明写计算时假设 spin-alignment parameter `σ/I = 0.5`，正文说明这样做是因为它对已知 `E2` 和 `E1` transitions 给出良好符合。 | experimental-practice | direct | p.3, Sec.IV; Table II | false |
| CH12-4 | `65Cu` 的 Table III 用 AD 结果给出若干 `M1/E2` 跃迁的近似 mixing ratios，例如 `1115.5 keV` 被写为 `I = 1 M1/E2 (δ = -0.1)`，`978.5 keV` 为 `δ = +0.4`，`281.1 keV` 也给出 `δ = +0.4`。 | observed-fact | direct | p.4, Table III | false |
| CH12-5 | 作者明确比较 `1115 keV` 跃迁的 alignment assumption effect：本文在 `σ/I = 0.5` 下给出 `δ ≈ -0.1`；用户复核指出 adopted-gamma 文献给出较大绝对值的 `δ = -0.437(15)`，且其他文献方法所得 `δ` 彼此并不一致，因此这里保守表述为：若取 `σ/I ≈ 0.7`，拟合会向 adopted / literature 中较大绝对值的 `δ` 范围移动。 | experimental-practice | direct | p.3, text below Fig.1 and above Table III; user audit against doi:10.1016/j.nds.2010.09.002 | false |
| CH12-6 | `65Cu` 在 `2534 keV` `9/2+` 态之上建立了新的 positive-parity band structure；`1126`, `697`, `350 keV` transitions 的 AD 与 `E2` 一致，而 `281` 与 `415 keV` 线与 `I = 1 M1/E2`、`δ ≈ +0.4` 和 `+0.3` 的解相容。 | observed-fact | direct | pp.3--4, Sec.VA; Fig.3; Table III | false |
| CH12-7 | `67Cu` 方面，论文在结论中总结已把正宇称结构延伸到至少 `17/2+`，并首次识别出一条 strongly coupled negative-parity band 和另外两条负宇称结构。 | observed-fact | direct | Abstract; p.18, Sec.VII | false |
| CH12-8 | 壳模型比较表明，`65,67Cu` 的正宇称谱更适合解释为 `p3/2` proton 对相邻 Ni core 负宇称态的 weak coupling；作者同时指出要完整再现实验，需要在计算中同时容纳 `f7/2` 与 `g9/2` 轨道。 | author-interpretation | direct | pp.17--18, Sec.VIB2; p.18, Sec.VII | false |

## Nuclear Structure Information

This source is mainly a `65,67Cu` spectroscopy paper. It extends the decay schemes, constrains spins/parities with AC/AD information, identifies a `67Cu` strongly coupled negative-parity structure, and discusses positive-parity states as weak-coupling/core-coupled configurations.

Because the current Wiki is centered on A≈130 and on the `sigma-over-i` project, this ingest does not create standalone `65Cu` or `67Cu` nucleus pages at this stage.

## Authors' Interpretation

- Positive-parity states in `65,67Cu` are argued to show competition between configurations involving `g9/2` protons and `g9/2` neutrons.
- The positive-parity structures are said to be better described by weak coupling of a `p3/2` proton to states of the neighboring Ni cores than by the available truncated shell-model interactions alone.
- The `67Cu` `7/2-` state is established as the bandhead of an intruder `πf7/2^-1` structure; a comparable structure is said not to develop clearly in `65Cu`.

## Model Results

- Shell-model calculations were performed with the JUN45 and jj44b interactions.
- For positive-parity levels, the paper finds JUN45 too compressed and jj44b somewhat better spaced but still offset in energy.
- The calculations are used qualitatively to help with tentative spin assignments where the AD/AC data are not fully decisive.

## Competing Interpretations and Limitations

- The paper is not a `σ/I` theory paper. The `σ/I = 0.5` choice appears only in the practical AD calculation setup for `65Cu`.
- The sensitive `1115 keV` example is one transition in one alignment-calibration context; it does not establish a recommended universal `σ/I` value.
- Many `65Cu` AC fits are said to be inconclusive, which is why the AD information from a separate `48Ca + 26Mg` experiment becomes important.
- The shell-model discussion itself emphasizes that the available valence spaces/interactions are incomplete for the full problem.

## Project Relation

For [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]], this source contributes a concrete experimental-practice example rather than a theory anchor. It shows that assumed alignment widths are used in spectroscopy fitting, that the assumption may be calibrated against known `E1/E2` transitions, and that the extracted `δ` for a specific transition can shift when the assumed `σ/I` changes.

The boundary is essential: Chiara 2012 should be cited as an A≈60 spectroscopy example of assumption-sensitive fitting practice, not as a primary source for P-ADO formalism and not as evidence for a universal `σ/I` prior.

## Extracted Pages

- Nuclei:
- Bands:
- Concepts: [[sigma-over-i]], [[spin-alignment]]
- Methods: [[angular-distribution]], [[angular-correlation]]
- Projects: [[sigma-over-i-uncertainty-in-pado-mixing-ratio-extraction]]

## Human Review Triage

- P0 focus resolved: `CH12-3`, p.3 Sec.IV + Table II. `σ/I = 0.5` is kept as an assumed AD calculation parameter justified by agreement with known `E2/E1` transitions.
- P0 focus resolved: `CH12-5`, p.3 text below Fig.1 / above Table III. The Wiki now states conservatively that `σ/I ≈ 0.7` shifts the fit toward larger-magnitude adopted / literature `δ` values rather than claiming an exact match to one literature number.
- P0 focus resolved: `Project Relation`. The source remains labelled as an experimental-practice example rather than a universal `σ/I` rule or a P-ADO formalism source.
- Remaining P0: none identified in this source after the 2026-07-09 user review.
- P1: `CH12-1/CH12-2`, pp.2--3, reaction + AC/AD setup and detector-angle grouping.
- P1: `CH12-4/CH12-6`, p.4 Table III and Fig.3, confirm which `65Cu` transitions carry approximate `δ` values and which are pure `E2/E1`.
- P1: `CH12-7/CH12-8`, p.18 conclusions, confirm the boundary between observed level-scheme extension and weak-coupling / shell-model interpretation.

## Personal Notes

This source is useful because it normalizes a real spectroscopy habit: alignment assumptions may be chosen pragmatically to fit calibration transitions. That is strong background for the project's "experimental practice" section, but the source remains outside the main A≈130 evidence chain and outside the primary P-ADO formalism chain.

## 2026-11-21 — 取向宽度与两次采集

024309-2 至 -3 区分两套数据。\(^{64}\mathrm{Ni}+{}^{238}\mathrm{U}\) 主实验的双光子角关联使用十组开角，较难为部分 \(^{65}\mathrm{Cu}\) 线找到干净的已知门。另一次 \(^{48}\mathrm{Ca}+{}^{26}\mathrm{Mg}\) 数据提供七角角分布。作者为后者选 \(\sigma/I=0.5\) 以再现已知 E2/E1 参考线。在此宽度下得到 1115.5 keV 的 \(\delta\approx-0.1\)，文字说明改用约 0.7 可与早期采用值 \(-0.450(16)\) 相符。Table IV 的 1114.9 keV 属 \(^{67}\mathrm{Cu}\)，\(\delta=-0.19\) 来自以 861 keV E2 为伴线的角关联。两条近同能量线的实验、门和取向处理各自对应。原文未给它们联合分析的数值化线偏振。
