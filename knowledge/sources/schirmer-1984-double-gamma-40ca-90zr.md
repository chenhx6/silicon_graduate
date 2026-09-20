---
type: source
title: "Schirmer et al. 1984 - Double Gamma Decay in 40Ca and 90Zr"
aliases: [Schirmer 1984 double gamma decay, 40Ca 90Zr two-gamma decay]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Double Gamma Decay in 40Ca and 90Zr"
authors: [J. Schirmer, D. Habs, R. Kroth, N. Kwong, D. Schwalm, M. Zirnbauer, C. Broude]
journal: "Physical Review Letters"
year: 1984
volume: 53
issue: 20
pages: "1897-1900"
canonical_source: "Schirmer et al., Phys. Rev. Lett. 53, 1897-1900 (1984)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/1984_Schirmer et al_Double Gamma Decay in Ca 40 and Zr 90.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/1984_Schirmer et al_Double Gamma Decay in Ca 40 and Zr 90.pdf"
raw_sha256: "2e84b4c7bda5077f41edd381e9c225c4e1a898fe988c3c7824e9ecefaaa9adfa"
nuclei: [40Ca, 90Zr]
reactions: [40Ca(p,p'), 90Zr(p,p')]
experiments: [heidelberg-darmstadt-crystal-ball]
models: [shell-model, second-order-electromagnetic-decay]
observables: [double-gamma-branching, gamma-gamma-angular-correlation, linear-polarization, M1-quenching]
methods: [gamma-gamma-coincidence, angular-correlation, compton-polarimetry]
tags: [double-gamma-decay, two-photon-decay, 40Ca, 90Zr, rare-branch, electromagnetic]
---

# Double Gamma Decay in 40Ca and 90Zr

## Bibliographic Record

- J. Schirmer *et al.*, *Physical Review Letters* **53**(20), 1897–1900 (1984).
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/electromagnetic/1984_Schirmer et al_Double Gamma Decay in Ca 40 and Zr 90.pdf`。
- 4-page PRL PDF; title page, authors, volume/issue/pages and 1984 date agree. The isotope superscripts are normalized in this page only; raw filename is preserved.

## Scope and Reading Depth

- PDF pp.1897–1900 fully read, including the detector/background method, Figs.1–3, double-gamma angular-correlation Eq.(2), second-order matrix-element Eq.(3), polarization branch selection, shell-model/quenching discussion, limits on `2E2` and final 1+ feeding example.
- Figure audit: energy-angle matrix and PAF rejection (Fig.1), delayed sum-energy spectra (Fig.2), and corrected directional correlations/fits (Fig.3) were read with captions and surrounding text.
- Not covered: raw Crystal Ball event data, full detector response files, unpublished shell-model code and the cited theoretical papers.

## Paper Question and Experimental Logic

The experiment tests the rare `0_2^+→0_1^+` two-photon decay in `40Ca` and `90Zr`, where a one-photon transition is forbidden and two dipole photons share the transition energy. The central challenge is separating true simultaneous two-photon events from positron-annihilation-in-flight (PAF) and single-photon Compton background.

1. Populate the `0_2^+` states with pulsed `(p,p')` resonances (`E0=3.35 MeV` in `40Ca`, `1.76 MeV` in `90Zr`) and gate on delayed proton–gamma events (PDF p.1897).
2. Use the 162-module 4π Crystal Ball, Lucite stopping box and two-detector coincidence requirement. Eq.(1) identifies PAF kinematics; energy-sum, relative-angle and energy-difference cuts suppress it (PDF pp.1897–1898, Figs.1–2).
3. Fit the corrected γ–γ directional correlation and use one gamma ray as a 159-fold Compton polarimeter to choose between reciprocal `2E1/2M1` matrix-element solutions (PDF pp.1898–1899, Eq.(2), Fig.3).

## Key Evidence and Reasoning Chain

- The energy-angle matrix shows a continuous double-gamma spectrum peaking near half the `0_2^+→0_1^+` energy once the PAF band is excluded (Fig.1). Delayed sum-energy spectra show peaks at the expected transition energies (Fig.2).
- The γ–γ correlation is asymmetric about `90°`; the authors attribute the linear `cos θ12` interference term to a mixture of `2E1` and `2M1`, rather than pure `2E1` (Fig.3 and Eq.2).
- Polarization asymmetries select the dominant branch: `2M1` for `40Ca` and `2E1` for `90Zr`. The normalized ratios are reported as `Γγγ/Γe+ = (4.5±1.0)×10⁻4` for `40Ca` and `(1.8±0.2)×10⁻6` for `90Zr`; the quoted `2M1/2E1` matrix-element ratios are `0.43±0.07` and `1.9^{+0.6}_{−0.4}`, respectively (PDF p.1899).
- Fits including `2E2` give upper limits `Γγγ(2E2)/Γγγ(total)<4%` for `90Zr` and `<2%` for `40Ca`; shell-model estimates predict `<10⁻3` (PDF p.1899).
- Shell-model calculations give M1 quenching factors `γ=0.76±0.05` (`40Ca`) and `0.67±0.09` (`90Zr`), broadly consistent with electron/proton scattering constraints, while feeding through multiple `1+` states warns that double-gamma decay and inelastic-scattering observables weight intermediate states differently (PDF pp.1899–1900).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| SC84-1 | Delayed two-detector events at the `0_2^+` energies of `40Ca` and `90Zr` survive PAF/Compton background cuts and show the expected continuous two-photon energy sharing. | experimental-result | direct | PDF pp.1897–1898, Figs.1–2 | true |
| SC84-2 | The directional correlation is asymmetric around `90°`, requiring interference of `2E1` and `2M1` amplitudes. | experimental-result/author-interpretation | direct | PDF pp.1898–1899, Eq.(2), Fig.3 | true |
| SC84-3 | Polarization selects predominantly `2M1` in `40Ca` and `2E1` in `90Zr`; normalized branching and matrix-element ratios are reported. | experimental-result | direct | PDF p.1899 | true |
| SC84-4 | `2E2` contributions are constrained to `<4%` (`90Zr`) and `<2%` (`40Ca`) by the correlation fits. | experimental-limit | direct | PDF p.1899 | false |
| SC84-5 | M1 quenching factors agree with selected `(e,e')`/`(p,p')` constraints, but intermediate-state weighting differs between two-gamma decay and inelastic scattering. | model-comparison | mixed | PDF pp.1899–1900 | true |

## Summary

Delayed Crystal-Ball coincidences in `40Ca` and `90Zr`, combined with PAF rejection, γγ angular correlations and Compton polarization, establish rare two-photon branches with mixed `2E1/2M1` character and constrain `2E2` admixtures. Absolute ratios remain response- and intermediate-state dependent.

## Competing Interpretations and Limitations

The main alternatives are PAF/single-γ Compton contamination, unresolved sequential decay and reciprocal multipole-amplitude solutions. The source suppresses these with kinematic cuts, timing and polarization, but no raw event matrices or complete response files are supplied.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| SC84-AR-1 | Background control | Eq.(1), delayed gates, Lucite stopping and energy/angle cuts jointly address PAF; the source does not supply raw sideband spectra. | PDF pp.1897–1898, Figs.1–2 | self-checking |
| SC84-AR-2 | Branch ambiguity | Angular-correlation fitting alone has reciprocal `2E1/2M1` solutions; Compton polarization is the independent branch selector. | PDF p.1899, Eq.(2) | self-checking |
| SC84-AR-3 | Transfer condition | The ratios and `Q_c(Eγ)=0.53Q_c^opt(Eγ)` are Crystal-Ball-specific; no cross-array universal sensitivity is implied. | PDF p.1897 | self-checking |
| SC84-AR-4 | Failure condition | Residual PAF, detector granularity/efficiency corrections, unobserved `1+` feeding and shell-model cancellation can shift absolute matrix-element inference. | PDF pp.1898–1900 | active-L3 |
| SC84-AR-5 | Lineage | This is a direct rare-decay experiment; it is independent of Gade 2015's `137Ba` commentary and should not be counted as evidence for that later `137Ba` experiment. | Source identity and nuclei | self-checking |

## Knowledge Impact and Learning Decision

- Effect: `supports` rare two-photon decay methodology and `limits` any attempt to treat a double-gamma signal as a simple γγ coincidence without PAF/Compton controls.
- Persistence: add a direct source link beside [[gade-2015-gamma-rays-come-in-twos]], update [[gamma-gamma-coincidence]] with the PAF/angle/polarization chain, and retain the two-photon branch as a source-specific observable.
- Review state: Codex self-audited; not `human-reviewed`.

## Related Knowledge and Project Relations

| Relation type | Target | Specific relation |
|---|---|---|
| methodological-bridge | [[gamma-gamma-coincidence]] | Delayed timing, two-detector multiplicity, PAF kinematic rejection and corrected directional correlation. |
| methodological-bridge | [[angular-correlation]] | Two-photon directional correlation and interference term; not the same as ordinary cascade DCO. |
| supports | [[gade-2015-gamma-rays-come-in-twos]] | Historical direct rare-two-gamma precedent; different nuclei/experiment, so no shared experimental count. |
| supports | [[compton-polarimetry]] | Crystal Ball polarization branch selection with detector-specific `Q_c(Eγ)`. |

## Human Review Triage

### P0

- `SC84-P0-1`: reported branching/matrix-element ratios depend on PAF rejection, efficiency/granularity corrections and polarization calibration; quote only with the PRL locator and Crystal-Ball boundary.

### P1

- `SC84-P1-1`: the shell-model M1-quenching comparison is not a one-to-one observable because intermediate `1+` states are weighted differently in the two experiments.

## Extracted Pages

- Nuclei: `40Ca`, `90Zr` (source-level only; no new high-spin band pages).
- Concepts: [[two-photon-nuclear-decay]] (if later created), [[gamma-gamma-coincidence]]。
- Methods: [[angular-correlation]], [[compton-polarimetry]]。

## L3/L4 Follow-up

- L3 question: which background-control combination (PAF kinematic rejection, delayed timing, angular correlation and polarization) is minimally sufficient for rare two-photon branching measurements across detector geometries? The discriminant is a detector-response and sideband study, not another literature summary.
- No L4 run: raw event matrices and response files are absent; this source supplies reported ratios and limits only.
