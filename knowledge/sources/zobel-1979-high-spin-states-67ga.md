---
type: source
title: "High spin states in 67Ga"
aliases: [Zobel 1979 67Ga high-spin states, Zobel 1979 alignment primary]
created: 2026-11-05
updated: 2026-11-05
status: ai-draft
review_status: unreviewed
reasoning_status: provisional
source_type: experiment-article
reading_depth: deep-read
title_original: "High spin states in 67Ga"
authors: [V. Zobel, L. Cleemann, J. Eberth, W. Neumann, N. Wiehl]
journal: Nuclear Physics A
year: 1979
volume: 316
pages: 165--188
doi: 10.1016/0375-9474(79)90678-X
language: en
canonical_source: doi:10.1016/0375-9474(79)90678-X
raw_file: "raw/papers/gpt/query/20261105-zobel-1979-67ga/High spin states in 67Ga.pdf"
raw_sha256: 69497888ea9e0b25fead2a28800ec2d14a58242ef0d6a9c214e6861f7fbffba5
archive_required: true
nuclei: [67ga, 66zn, 69as]
reactions: ["57Fe(12C,pnγ)67Ga"]
observables: [level-scheme, gamma-gamma-coincidence, angular-distribution, linear-polarization, mixing-ratio, side-feeding, alignment-attenuation]
methods: [in-beam-gamma-spectroscopy, angular-distribution, gamma-ray-polarimetry]
tags: [67ga, high-spin, nuclear-alignment, magnetic-substate-population, gaussian-hypothesis, pado-support, source-lineage]
---

# Zobel et al. (1979): High spin states in \(^{67}\)Ga

## Bibliographic Record

V. Zobel, L. Cleemann, J. Eberth, W. Neumann and N. Wiehl, “High spin states in
\(^{67}\)Ga,” *Nuclear Physics A* **316**, 165–188 (1979), DOI
`10.1016/0375-9474(79)90678-X`. The local primary PDF is 24 pages and its
SHA-256 is recorded in the frontmatter and the query manifest.

## Scope and Reading Depth

The user downloaded the subscribed ScienceDirect PDF and placed it at the
frontmatter path after the agent's direct-link attempts failed. Its 24-page text
layer was read through the experimental methods, results, discussion and
references, including table text and figure captions. Pixel-level checks in this
session covered PDF p.7 / printed p.171 (Table 2), PDF p.14 / printed p.178
(Fig.8 and Table 3), and PDF p.17 / printed p.181 (Fig.9c–d).
This is not a claim of visual verification of every plotted point in Figs.1–10
or every model amplitude in Table 4. OCR contains spin/parity and Greek-symbol
errors; the printed PDF takes precedence.

No matching BibTeX entry was found in the local Zotero BibTeX search, so
`citation_key` is deliberately omitted. The DOI and primary title identify the
work; no BibTeX file was changed.

This source is the primary 1979 experiment cited as Ref. 9 in Zobel 1980 and
Ref. 4 in Zobel 1983. It closes the previously missing primary-text access
boundary, but it does not provide event-level spectra, a producer response
matrix or a numerical joint covariance for the later source-lineage question.

## Summary

The paper reports a high-spin and alignment study of
\(^{67}\)Ga populated through \(^{57}\)Fe(\(^{12}\)C,pn\(\gamma\)) at 40 MeV.
It establishes a positive-parity level sequence, measures angular distributions
and linear polarization, extracts mixing ratios and attenuation coefficients,
and compares the resulting magnetic-substate populations with a Gaussian shape
hypothesis. The Gaussian comparison is conditional on the observed feeding and
cascade structure; the 359-keV level provides a direct example where cascade
and large mixing-ratio effects visibly disturb the Gaussian pattern.

## Experimental setup and direct observations

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Z79-1 | The experiment populated \(^{67}\)Ga through \(^{57}\mathrm{Fe}(^{12}\mathrm{C},pn\gamma)^{67}\mathrm{Ga}\); the principal angular-distribution, coincidence and level-scheme data were taken at \(E_{^{12}\mathrm C}=40\) MeV, with beams spanning 32–44 MeV for the yield study. | observed-fact | direct | printed pp.165, 167–170; Abstract; §2.2 | true |
| Z79-2 | The coincidence measurement used an enriched \(^{57}\)Fe target, two Ge(Li) detectors at approximately \(90^\circ\), prompt timing selection and summed gated spectra; a partial \(\gamma\)-\(\gamma\) matrix is given in Table 1. | observed-fact | direct | printed pp.167–168, Table 1 | true |
| Z79-3 | Singles angular distributions used twelve detector angles from \(160^\circ\) to \(0^\circ\), with separate monitor and movable Ge(Li) detectors; excitation/yield curves were measured across the incident-energy scan. | observed-fact | direct | printed pp.169–170, Fig. 2, §2.2 | true |
| Z79-4 | The paper reports linear-polarization measurements with a three-crystal Ge(Li) Compton polarimeter, including plane-efficiency calibration and polarization sensitivity checks using known \(^{67}\)Ga transitions. | observed-fact | direct | printed pp.175–177, Fig. 6–7, §2.5 | true |
| Z79-5 | The partial level scheme places levels at 3577.9, 3855.9, 4198.5, 4290.4, 5225.6, 5491.5, 6380.0, 6589.5 and 7618 keV. Parentheses on upper spin/parity assignments are retained; the 7618-keV level has no spin/parity assignment in Fig.8. | author-interpretation | direct/author interpretation | printed pp.176–185, Fig. 8, §§3.1–3.6 | true |

## Key Results

The claim tables below separate direct measurements, author analyses and
methodological interpretations. All new claims remain `needs_review: true`.

## The 958-keV primary transition and alignment inputs

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Z79-6 | Table 2 identifies the 958.010(50)-keV transition as \(3031.67\to2073.68\) keV, with relative intensity \(58.17(86)\), angular coefficients \(A_2=0.349(7)\) and \(A_4=-0.093(7)\), mixing ratio \(\delta=-0.001(9)\), and the assignment \(13/2^+\to9/2^+\). | observed-fact | direct | printed p.171, Table 2; visual check of PDF p.7 | true |
| Z79-7 | Table 3 gives the 3031.67-keV level side-feeding intensity \(12.53(64)\), \(\alpha_2=0.794(16)\) and \(\alpha_4=0.431(32)\); for the 2073.68-keV level it gives side feeding \(0.69(60)\), \(\alpha_2=0.733(16)\) and \(\alpha_4=0.326(32)\). | observed-fact | direct | printed p.178, Table 3; visual check of PDF p.14 | true |
| Z79-8 | Because the 2073.7-keV level has very small side feeding, the authors use the 958-keV transition and the 3031.7-keV alignment to determine the 2073.7-keV attenuation coefficients; they compare these with values propagated through the 554.5- and 871.5-keV cascades in the same experimental study. This does not establish statistically independent estimates. | author-interpretation | author analysis | printed pp.173–175, Eq. (3), Table 3 | true |
| Z79-9 | The authors derive \(\alpha_2=0.481(18)\), \(\alpha_4=0.070(20)\) for the 359.1-keV level by cascade propagation while explicitly neglecting the effects of 17.6% side feeding and 0.8% beta decay feeding from 67Ge. They attribute its departure from a Gaussian distribution to the cascade, including the high-mixing-ratio 843-keV branch. | author-interpretation | author analysis | printed p.175, §2.4; Table 3 prints alpha2 as 0.48 ± 0.018 | true |

## Gaussian substate hypothesis and its limits

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| Z79-10 | The authors define \(\alpha_2\) and \(\alpha_4\) through the second and fourth moments of the magnetic-substate population and use a Gaussian population as a one-parameter shape hypothesis, while citing an \(A\approx40\) compilation that does not universally support the assumption. | observed-fact | direct | printed pp.173–174, Eqs. (1)–(2), Fig. 5 | true |
| Z79-11 | The 1202- and 3031-keV levels are consistent with Gaussian substate populations within errors; the 1519-keV level is close to the Gaussian region despite cascade feeding; the 359-keV level is a visible non-Gaussian example under the stated cascade/mixing conditions. | author-interpretation | direct/author interpretation | printed pp.173–175, Fig. 5 and §2.4 | true |
| Z79-12 | The authors report near-Gaussian alignment above 3 MeV from simultaneous angular-distribution/polarization fits. They mention compensating feeding effects but argue that their polarization data refute this explanation. This is their interpretation of these data; this source note does not generalize it to all reactions or levels. | author-interpretation | direct/author interpretation | printed p.175, §2.4 | true |
| Z79-13 | The transition-propagation relation in Eq. (3) requires the preceding state, multipolarity/mixing information and the relevant statistical-tensor factors; it is not a direct event-level covariance model. | method-formalism | direct/method boundary | printed pp.174–175, Eq. (3) | true |

## Structural interpretation and model boundary

The authors interpret the main positive-parity sequence as weak coupling of a
\(g_{9/2}\) proton to collective states of the \(^{66}\)Zn core. They associate
the second stretched-E2 band based at 3577.9 keV with a different internal
structure, tentatively involving a broken \(f_{5/2}\)-pair coupled to a
\(g_{9/2}\) proton. Their Alaga/particle-vibration calculation uses a
1.34-MeV phonon energy, a 1.2-MeV \(f_{5/2}\)-to-\(g_{9/2}\) single-particle
spacing, pairing strength \(G=0.35\) MeV and particle-field coupling
\(a=0.2\) MeV.

These are author-model interpretations. The paper explicitly says that more
detailed calculations should include electromagnetic properties and more than
three phonons for higher-spin states; the article does not provide the complete
electromagnetic dataset or an event-level producer package needed for a modern
joint reanalysis.

## Source-lineage relation to Zobel 1980 and 1983

The 1979 primary is now locally available and directly confirms the experiment
identity, the \(^{57}\)Fe+\(^{12}\)C reaction, the 40-MeV benchmark, the 958-keV
transition and the alignment observables later reused by Zobel 1980 and 1983.
It resolves the former “primary text unavailable” boundary in
[[zobel-1980-magnetic-substate-distributions]].

Specifically, the 1979 Table 2 958-keV row reports
\(A_2=0.349(7), A_4=-0.093(7)\), and Table 3 reports
\(\alpha_2=0.794(16), \alpha_4=0.431(32)\). These equal the printed
inputs already transcribed in Z80-17; together with the 1980 row's Ref.9
attribution, this supports reuse of published inputs. It is not evidence for
an additional independent measurement. The 1979 Table 2 value
\(\delta=-0.001(9)\) is distinct from the exact \(\delta=0\) assumption
used in the pure-quadrupole alignment analysis of §2.4.

It does not establish that the 1979, 1980 and 1983 papers used independent raw
acquisitions. The common reaction/level/alignment lineage and the citation chain
remain a dependent-source issue until raw acquisition records, fit logs or an
author/experiment-group statement are available.

## Evidence boundaries

- The paper reports fitted angular coefficients, mixing ratios, polarization
  results, side-feeding intensities and attenuation coefficients.
- It does not publish the raw event list, detector response matrix, full
  producer covariance or the complete unbinned likelihood inputs.
- OCR misreads several spin/parity and Greek-symbol glyphs; the printed PDF
  tables and figures take precedence over the extracted text.
- Upper-level spin/parity assignments at 5225.6, 6589.5, 5491.5 and 6380.0 keV
  remain tentative where the authors say so.
- For the 4198.5-keV level, printed p.178 Table 3 gives
  \(\alpha_4=0.61(8)\), whereas printed p.183 §3.5 says \(0.34(8)\).
  These values are retained as a source-internal discrepancy; no silent
  correction, averaging or claim of an official erratum is made.

## Competing Interpretations and Limitations

The weak-coupling and particle-vibration interpretations are the authors’ model
interpretations, not model-independent observations. The alignment results are
conditional on feeding, cascade propagation, multipolarity/mixing assignments,
and the angular-distribution and polarimeter response. The article does not
publish raw event data, a complete detector-response matrix or a full joint
covariance suitable for event-level reanalysis. Upper-level assignments marked
tentative by the authors remain tentative here.

## Extracted Pages

- [[zobel-1980-magnetic-substate-distributions]]
- [[zobel-1983-energy-projectile-alignment]]
- [[magnetic-substate-population]]
- [[spin-alignment]]
- [[sigma-over-i]]

## Human Review

This page is a Codex source self-audit based on the complete local PDF. It has
not received targeted user claim review and remains `review_status: unreviewed`.
