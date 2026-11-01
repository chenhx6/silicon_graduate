---
type: source
title: "Ronning et al. 2026: magnetic character of the low-energy enhancement in 70Zn"
aliases: [70Zn magnetic LEE, Ronning 2026 low-energy enhancement, beta-Oslo 70Zn]
created: 2026-11-01
archive_required: true
updated: 2026-11-01
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Magnetic character of the low-energy enhancement in 70Zn"
authors: [E. K. Ronning, A. L. Richard, A. C. Larsen, J. E. L. Larsson]
journal: "Nature"
year: 2026
volume: 655
pages: "875–878"
doi: 10.1038/s41586-026-10758-3
language: en
canonical_source: "https://doi.org/10.1038/s41586-026-10758-3"
citation_key: ronning_2026_70zn_magnetic_lee
raw_file: "raw/papers/gpt/learning-daily/20261101-day29-70zn-lee/ronning-2026-70zn-lee.html"
raw_sha256: "5e03a5f49131459664332131d130a3a381fb3bf535e1a1ad53acfa45ebbe6c8a"
nuclei: [70zn, 70cu]
experiments: [frib-70zn-beta-decay-gamma-spectroscopy]
models: [shape-method, beta-oslo-method, geant4-response]
observables: [gamma-strength-function, nuclear-level-density, beta-decay, total-absorption, parity-distribution]
methods: [beta-decay, gamma-spectroscopy, total-absorption-spectroscopy, beta-oslo, shape-method, response-unfolding]
tags: [70zn, low-energy-enhancement, m1, gamma-strength-function, beta-oslo, cross-mass-method]
---

# Ronning et al. 2026：`70Zn` 低能 γSF 上弯的磁性

## Bibliographic Record

E. K. Ronning et al., *Magnetic character of the low-energy enhancement in `70Zn`*,
*Nature* **655** (2026) 875–878, DOI `10.1038/s41586-026-10758-3`。本地保存
的是 PMC 公开全文 HTML，SHA-256 为
`5e03a5f49131459664332131d130a3a381fb3bf535e1a1ad53acfa45ebbe6c8a`。Nature/PMC
文章给出的卷页和 DOI 是身份锚点；本文的局部方法与结果 locator 均指向公开全文
的章节或图表位置。

## Scope and Reading Depth

全文 HTML 的摘要、主文、Extended Data 说明和 Methods 相关段落已读取。另一次
PMC PDF 端点返回了 HTML challenge 页面，未将其作为原文；source→raw 绑定使用
可解析的 HTML 原件。没有把 `70Zn` 结果当作 `133I` 的实验事实。

## Summary

Ronning et al. use two spin/parity-selective `70Cu` β-decay parents together with
total-absorption excitation information, response unfolding and partial-NLD/parity
controls to establish a magnetic low-energy enhancement in `70Zn`. The cross-mass
value for the present `133I` design is methodological: an `E_x`-window comparison
must be accompanied by population and electromagnetic-character controls.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| RON26-1 | The paper reports that the low-energy enhancement in the `70Zn` γSF has magnetic character and attributes it to M1 transitions. | experimental-result-and-author-conclusion | direct | PMC full text, Abstract and opening Main paragraphs | true |
| RON26-2 | The experiment extracts two `70Zn` γSFs from β decay of two `70Cu` parents: a `1+` second isomer and a `6−` ground state. Allowed β decay selectively populates different spin/parity regions, approximately `J=0–3` positive-parity and `J=4–8` negative-parity regions in the quasi-continuum. | experimental-design-and-population-selectivity | direct | PMC full text, Main paragraph beginning “Specifically” and Methods β-Oslo population paragraph | true |
| RON26-3 | SuN++ total-absorption spectroscopy supplies excitation-energy population information; the same data produce `E_x`–`E_gamma` matrices, which are response-unfolded with a Geant4 detector response before primary-matrix extraction. | experimental-response-chain | direct | PMC full text, Extended Data Fig.1/2 descriptions and Methods β-Oslo section | true |
| RON26-4 | The β-Oslo extraction uses a statistical region with `E_gamma,min=1.1 MeV`, `E_min=3.3 MeV` and an upper `E_x` bound of `6.1 MeV` for the reported `70Zn` analysis; the limits are varied as a consistency check. | analysis-input-and-sensitivity | direct | PMC full text, Methods β-Oslo section | true |
| RON26-5 | The extracted level densities are partial spin-selected densities, not automatically total NLDs; the analysis normalizes them to discrete low-lying levels and models parity-asymmetric E1 availability separately. | analysis-boundary | direct | PMC full text, Methods β-Oslo and parity-asymmetry discussion | true |
| RON26-6 | The paper explains the difference between the two populated γSFs through E1 suppression caused by parity availability while the M1 contribution is unaffected, supporting the magnetic interpretation of the LEE. | model-supported-interpretation | mixed | PMC full text, Main parity-asymmetry discussion and Fig.3 explanation | true |

## Experimental and Analysis Chain

The critical design is not merely two excitation windows. The two β-decaying parents
provide different, independently identified spin/parity population filters. Total
absorption constrains the excitation-energy population, while the segmented γ
spectrometer supplies individual γ rays. The analysis then performs response
unfolding, primary-γ extraction, NLD/γSF separation and a parity-asymmetry correction.
The shape method supplies an energy-dependence constraint that helps stabilize the
β-Oslo slope.

## Cross-Mass Transfer to `133I`

This source changes the `133I` candidate design in one specific way. Two non-overlapping
`E_x` windows can test excitation-window stability, but they do not by themselves
identify M1 versus E1 if the windows have unknown or overlapping spin/parity
populations. A `133I` analysis needs at least one of:

1. a validated spin/parity-selective population contrast;
2. an independent angular-distribution or Compton-polarization observable;
3. a calibrated dipole-control network whose response and feeding are included in the
   joint likelihood.

The `70Zn` result therefore supports the bold `133I` hypothesis only at the level of
an experimental method template. It does not transfer the M1 mechanism, enhancement
amplitude, NLD normalization or Brink–Axel behavior to `133I`.

## Competing Interpretations and Limitations

- The `70Zn` paper's parity-asymmetry correction is tied to its selective β-decay
  population and evaluated parent-state identity; it cannot be copied into a
  stable-beam `130Te(α,pγ)133I` Oslo extraction.
- Shape-method and β-Oslo results still require response, statistical-window,
  NLD/spin and normalization checks. A low-energy excess remains insufficient without
  an electromagnetic-character discriminator.
- This source is an independent cross-mass method source, not an independent
  `133I` measurement and not a new dataset for the OCL acquisition.

## Knowledge Impact and Learning Decision

`supports`: a magnetic interpretation of LEE can be established when population
selectivity and response-folded γSF comparisons are available.

`revises`: the `133I` contract must treat spin/parity population as a first-class
nuisance/observable; two `E_x` windows alone are inadequate for an M1 claim.

`limits`: no `133I` event data, response, γSF, NLD, polarization, covariance or M1
strength is supplied by this source.

## Extracted Pages

- Abstract and Main opening: magnetic LEE result and experimental motivation.
- Main population-design paragraphs: two `70Cu` parent states and spin/parity selectivity.
- Extended Data Fig.1–2 descriptions: total absorption and `E_x`–`E_gamma` matrices.
- Methods β-Oslo and shape-method paragraphs: response unfolding, statistical windows,
  partial NLD and parity-asymmetry treatment.

## Human Review

This is a Codex self-audit of a primary experimental paper and remains `unreviewed`.
The cross-mass transfer to `133I` is a provisional design inference.
