---
type: source
title: "Jones et al. 2010 - The magic nature of 132Sn explored through 133Sn single-particle states"
aliases: [Jones 2010 133Sn transfer, 132Sn to 133Sn particle-addition spectrum]
created: 2026-09-29
updated: 2026-09-29
status: active
review_status: unreviewed
source_type: journal-article-transfer-experiment
reading_depth: skimmed
citation_key: Jones2010Nature09048
title_original: "The magic nature of 132Sn explored through the single-particle states of 133Sn"
authors: [K. L. Jones, et al.]
journal: Nature
year: 2010
volume: 465
issue: 7297
pages: 454-457
doi: 10.1038/nature09048
language: en
canonical_source: doi:10.1038/nature09048
raw_file: "raw/papers/gpt/day2-shell-gap-20260928/jones-2010-nature09048-supplement.pdf"
raw_sha256: 1854f8e4225ca93038e170845b8a6d45e53ccba2a1e62eca50e54aa46bda5d3d
related_raw_files: ["raw/papers/gpt/day2-shell-gap-20260928/jones-2010-nature09048-preview.html", "raw/papers/gpt/day2-shell-gap-20260928/nudat-133Sn-levels.html"]
supplement_url: "https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnature09048/MediaObjects/41586_2010_BFnature09048_MOESM312_ESM.pdf"
nuclei: [132sn, 133sn]
reactions: ["132Sn(d,p)133Sn"]
experiments: [hribf-132sn-transfer]
models: [dwba, local-and-global-optical-potential]
observables: [single-particle-levels, differential-cross-section, spectroscopic-factor]
methods: [inverse-kinematics-transfer-reaction, dwba]
tags: [sn132, sn133, n82, transfer-reaction, single-particle-orbitals]
---

# `132Sn(d,p)133Sn` single-particle transfer evidence

## Bibliographic Record

K. L. Jones et al., *Nature* **465**, 454–457 (2010), DOI `10.1038/nature09048`. Crossref and the Nature publisher page agree on article identity. The Nature landing page identifies the article as subscription content and exposes its abstract and figure legends; the direct `.pdf` endpoint returned HTML, not a PDF. The publisher's Supplementary Information is openly accessible and contains the transfer cross-section tables and DWBA sensitivity plots used below.

## Scope and Reading Depth

Read the Nature abstract and Figs.1–3 captions from the publisher preview, and all six pages of the linked Supplementary Information. Figures 2–4 and Tables 2–4 were inspected; the supplementary file was hash-verified at `1854f8e4225ca93038e170845b8a6d45e53ccba2a1e62eca50e54aa46bda5d3d`. The full main-article text was not accessible and is not represented as read.

## Summary

The article reports a `132Sn(d,p)133Sn` one-neutron-addition experiment and interprets the observed `133Sn` levels as predominantly single-particle states outside the `N=82` closure. The open supplementary file provides angular-distribution data and comparisons of spectroscopic factors extracted with local and global optical potentials. The latter are reaction-model-derived quantities rather than direct occupancies.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| JON10-1 | The abstract reports `132Sn(d,p)133Sn` single-neutron transfer and interprets the single-particle character of the `133Sn` levels as evidence for the doubly magic character of `132Sn`. | author-interpretation | direct | Nature HTML preview, Abstract | true |
| JON10-2 | The article's Fig.3 caption says proton angular distributions were measured for the two lowest `133Sn` states; the two highest states have angle-integrated cross-section measurements. | experimental-fact | direct | Nature HTML preview, Fig.3 caption | true |
| JON10-3 | Supplementary Tables 2–4 tabulate differential cross sections for the ground state and 854-keV state, and angle-integrated cross sections `8.7±1.7` and `11.3±1.9 mb/sr` for the 1363- and 2005-keV states. | experimental-fact | direct | Supplementary PDF pp.4–5, Tables 2–4 | true |
| JON10-4 | Supplementary Fig.4 gives local/global optical-potential spectroscopic-factor pairs: ground `0.86/0.85`, 854 keV `0.92/0.80`, 1363 keV `1.1/1.0`, and 2005 keV `1.1/1.1`. | derived-observable | direct | Supplementary PDF p.2, Fig.4 | true |
| JON10-5 | The Nature Fig.3 preview shows alternative local/global orbital fits with distinct `l` and spectroscopic-factor labels: e.g. ground-state `2f7/2 (0.86)` vs `3p3/2 (0.55)`, and the 854-keV state `2f7/2 (1.22)` vs `3p3/2 (0.92)`. | model-result | direct | Nature HTML preview, Fig.3 image and caption | true |
| JON10-6 | The SI says that for the `132Sn(d,p)` reaction local and global potential calculations have similar angular-distribution shapes and agree in magnitude to better than 15%; a `208Pb(d,p)` control shows larger global-potential disagreement at high angular momentum transfer. | model-boundary | direct | Supplementary PDF p.1 and p.3, Fig.5 | true |
| JON10-7 | The Nature publisher page provided abstract and figure captions, while the article PDF request returned `text/html`; only the Supplementary Information was available as a verified PDF. | evidence-boundary | direct | Nature article page and attempted `.pdf` endpoint; SI PDF metadata | true |

## Competing Interpretations and Limitations

- The transfer angular distributions constrain `l`, but extracted spectroscopic factors depend on DWBA, optical potentials and the selected orbital fit. The Fig.3 alternative curves and the SI local/global comparison show the size of this model dependence.
- Values near one support substantial single-particle strength in the chosen fit; they are not direct orbital occupancies and do not independently measure the energy gap across `N=82`.
- The main article text was not available in the publisher response. Claims beyond its accessible abstract/captions and the SI are not included. The SI values and the ENSDF level evaluation refer to the same `2010Jo03` experiment, not independent replications.

## Extracted Pages

- Nature HTML preview: abstract and figure captions for Figs.1–3.
- Supplementary PDF p.1: DWBA potential sensitivity and the `208Pb(d,p)` method control.
- Supplementary PDF p.2: Fig.4 `133Sn` local/global spectroscopic-factor comparisons.
- Supplementary PDF pp.4–5: Tables 2–4 with `132Sn(d,p)133Sn` differential/integrated cross sections.

## Related Knowledge

- [[ensdf-133sn-transfer-levels]]
- [[iaea-livechart-132sn-134te-levels]]
- [[ame2020-sn132-mass-curvature]]
- [[a130-shell-gap-orbital-observable]]
