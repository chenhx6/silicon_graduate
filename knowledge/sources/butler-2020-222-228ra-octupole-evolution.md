---
type: source
title: "Butler et al. 2020 - Evolution of octupole deformation in 222Ra and 228Ra"
aliases: [Butler 2020 radium E3 matrix elements, PRL 124 042503]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: journal-article-experiment
reading_depth: deep-read
title_original: "Evolution of Octupole Deformation in Radium Nuclei from Coulomb Excitation of Radioactive 222Ra and 228Ra Beams"
authors: [P. A. Butler, L. P. Gaffney, P. Spagnoletti, K. Abrahams, M. Bowry, J. Cederkäll, G. de Angelis, H. De Witte, P. E. Garrett, A. Goldkuhle, C. Henrich, A. Illana, K. Johnston, D. T. Joss, J. M. Keatings, N. A. Kelly, M. Komorowska, J. Konki, T. Kröll, M. Lozano, B. S. Nara Singh, D. O'Donnell, J. Ojala, R. D. Page, L. G. Pedersen, C. Raison, P. Reiter, J. A. Rodriguez, D. Rosiak, S. Rothe, M. Seidlitz, T. M. Shneidman, B. Siebeck, J. Sinclair, J. F. Smith, M. Stryjczyk, P. Van Duppen, S. Vinals, V. Virtanen, N. Warr, K. Wrzosek-Lipska, M. Zielińska]
journal: "Physical Review Letters"
year: 2020
volume: 124
pages: "042503"
doi: "10.1103/PhysRevLett.124.042503"
citation_key: Butler_2020
citation_key_verified: 2026-10-28
canonical_source: "https://doi.org/10.1103/PhysRevLett.124.042503"
alternate_source: "https://arxiv.org/abs/2001.09681"
library_file: "outputs/literature-acquisition/day26-butler-027/Butler_2020_PRL124_042503.pdf"
raw_file: "raw/papers/gpt/day26-20261028/butler-2020-prl124-042503.pdf"
raw_sha256: "c0f8646afcd78d8647a7011046c036aa7c8ae7969839f72151646464a43b1502"
nuclei: [222Ra, 228Ra, 224Ra, 226Ra, 148Nd]
reactions: [sub-barrier-multistep-coulomb-excitation]
experiments: [HIE-ISOLDE, Miniball]
models: [GOSIA, rotational-model, octupole-vibrator]
observables: [E1, E2, E3, Q1, Q2, Q3, Coulomb-excitation-yields]
methods: [radioactive-beam-coulomb-excitation, gamma-ray-spectroscopy, silicon-particle-detection]
tags: [222Ra, 228Ra, octupole, E3, pear-shape, octupole-vibration]
---

# Evolution of octupole deformation in `222Ra` and `228Ra`

## Bibliographic Record

P. A. Butler *et al.*, *Phys. Rev. Lett.* **124**, 042503 (2020), DOI `10.1103/PhysRevLett.124.042503`. The published PDF was obtained from the APS harvest endpoint and verified as a six-page PDF. An arXiv v1 PDF (`2001.09681`, 16 pages) was also obtained; pages 7–16 contain the supplemental material appended to the preprint, including level schemes, selected fitted yields, E2 systematics, and Table II E1 matrix elements. The acquisition manifest records the downloader's separate CDP failure; the files here were retrieved from the public APS harvest and arXiv endpoints.

## Scope and Reading Depth

- Published PRL pages 1–6 read end-to-end, including the experiment, GOSIA fit, Table I, Figs. 1–5, competing vibrator interpretation, and correction note.
- ArXiv v1 pages 1–16 read end-to-end, including the supplemental pages 7–16. The arXiv source archive was downloaded but not used to infer additional numerical claims.
- No independent raw GOSIA yield matrices, covariance files, or analysis code were obtained.

## Experiment and Analysis

Sub-barrier multistep Coulomb excitation of radioactive `222Ra` and `228Ra` beams at HIE-ISOLDE used `60Ni` and `120Sn` targets, Miniball γ detection and a segmented silicon detector. The main paper reports 114 data fitted to 42 variables for `222Ra` and 121 data fitted to 41 variables for `228Ra` (PRL PDF p.2; arXiv PDF p.5). GOSIA fit E1–E3 matrix elements; higher E3 couplings marked with an asterisk in Table I were tied to lower matrix elements through rotational-model relations and were not completely independent (PRL PDF p.3; arXiv PDF p.6).

## Direct E3 Matrix-Element Results

Table I gives central E3 reduced matrix elements in `e b^(3/2)` and per-transition intrinsic `Q3` in `e fm^3`:

| Transition | `222Ra` m.e. / `Q3` | `228Ra` m.e. / `Q3` | Locator and independence |
|---|---:|---:|---|
| `0+ → 3−` | `1.13(9)` / `3030(240)` | `0.87(15)` / `2300(400)` | PRL PDF p.3 Table I; lowest coupling free |
| `2+ → 1−` | `0.85(24)` / `2000(600)` | `1.36(23)*` / `3200(600)` | same; `228Ra` asterisk means coupled |
| `2+ → 3−` | `−0.9(5)` / `2100(1200)` | `−0.06(+0.23/−0.16)*` / `150(+360/−500)` | critical near-zero `228Ra` link; coupled in 228Ra |
| `2+ → 5−` | `1.79(20)` / `3100(400)` | `1.71(23)*` / `3000(400)` | same; 228Ra coupled |
| `4+ → 1−` | `−2.1(5)*` / `4400(1000)` | `0.4(+0.7/−1.1)*` / `−800(+2300/−1400)` | asterisk means not fully independent |
| `4+ → 3−` | `2.6(+0.6/−0.9)*` / `5500(+1300/−1800)` | not tabulated | coupled in 222Ra |
| `4+ → 5−` | `−1.7(10)*` / `3200(1800)` | not tabulated | coupled in 222Ra |
| `4+ → 7−` | `3.3(+0.3/−0.5)*` / `4600(+500/−600)` | not tabulated | coupled in 222Ra |

The rotational-model fitted aggregate values are `Q3=3120(190) e fm^3` for `222Ra` and `2230(290) e fm^3` for `228Ra` (PRL PDF p.3 Table I). Figure 4 compares transition-specific `Q3` values for `222,224,226,228Ra` and `148Nd`; `222,224,226Ra` are approximately constant across the shown links, whereas `228Ra` has near-zero `Q3` for `2+→3−` and `1−→4+` (PRL PDF p.4 Fig.4 and text).

## Author Interpretation and Boundary

The authors explain the different E3 patterns as stable pear-like octupole deformation in `222Ra` and octupole-vibrator behavior in `228Ra`. They explicitly state that the rotational-like Q3 pattern is evidence supporting stable octupole deformation, while the near-zero links and aligned-angular-momentum behavior of `228Ra` are consistent with an octupole vibrator. They also caution that the energy-level behavior in `222,224,226Ra` is less obvious because pairing dominates near the ground state, and that rotationally aligned octupole phonons offer an alternative that does not require a permanent octupole distortion (PRL PDF p.5; arXiv PDF p.10).

## Evidence Claims

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BU20-1 | Multistep Coulomb excitation determined E3 matrix elements for `222Ra` and `228Ra`. | experimental-result | direct | PRL pp.1–3, Table I | true |
| BU20-2 | `222Ra` shows an approximately constant multi-transition Q3 pattern, while `228Ra` has near-zero Q3 for selected links. | experimental-result | direct | PRL pp.3–5, Fig.4, Table I | true |
| BU20-3 | The authors interpret the pattern as stable octupole deformation in `222Ra` and octupole vibration in `228Ra`. | author-interpretation | direct-to-source | PRL p.1 abstract, p.5 | true |
| BU20-4 | Higher E3 matrix elements marked `*` are coupled through rotational assumptions and are not fully independent measurements. | fit-boundary | direct | PRL p.3; arXiv p.6 | true |
| BU20-5 | A complete E3 pattern provides stronger static-versus-vibrational discrimination than a single large `0+→3−` strength, but the inference remains model and coupling dependent. | synthesis-boundary | mixed | PRL pp.2–5, Table I/Fig.4 | true |

## Supplemental Material Coverage

The appended arXiv pages 7–16 include partial level schemes (Fig.6, p.13), selected fitted yields (Fig.7, p.14), an E2-systematics compilation (Fig.8, p.15), and Table II E1 matrix elements (p.16). They do not provide the original event-level GOSIA covariance or a closure-complete E3 sum over all negative-parity states. The publication's SI endpoint was not independently downloaded through the browser-dependent route; the arXiv-appended material is the actual read coverage.

## Limitations and Review State

The GOSIA fit includes model couplings, phase choices and systematic variations. The starred E3 entries are correlated with higher matrix elements. `Q3` is a rotor-convention conversion of matrix elements, not a direct density image. This page is Codex self-audited and remains `unreviewed`.

## Summary

Butler *et al.* provide a multi-transition E3 pattern for `222Ra` and `228Ra`. The near-constant `Q3` pattern in `222Ra` is interpreted by the authors as stable octupole deformation, while selected near-zero links in `228Ra` are consistent with an octupole vibrator. This is stronger shape discrimination than a single large E3 line, while retaining fit and model boundaries.

## Key Results

- `222Ra`: `0+→3−` E3 matrix element `1.13(9) e b^(3/2)`, with rotational-model aggregate `Q3=3120(190) e fm^3`.
- `228Ra`: `0+→3−` E3 matrix element `0.87(15) e b^(3/2)`, with rotational-model aggregate `Q3=2230(290) e fm^3`; `2+→3−` is `−0.06(+0.23/−0.16)*`, giving a near-zero Q3 within large uncertainty.
- Higher entries marked `*` are coupled through rotational assumptions and do not form an independent closure-complete E3 sum.

## Competing Interpretations and Limitations

The author interpretation separates stable pear-like collectivity from an octupole vibrator, but rotationally aligned octupole phonons, pairing effects and model-coupled GOSIA fits remain alternatives or limitations. A single `0+→3−` strength cannot distinguish these cases. The measured transition set is not a complete energy-weighted or non-energy-weighted sum over all negative-parity states.

## Extracted Pages

- Published PDF pages 1–6: experiment, Table I, Figs. 1–5 and conclusions.
- ArXiv v1 pages 7–16: supplemental level schemes, selected yield fits, E2 systematics and E1 Table II.
- Local raw copy: `raw/papers/gpt/day26-20261028/butler-2020-prl124-042503.pdf`, 6 pages, SHA-256 recorded in frontmatter.

## Related Research Note

See [[octupole-sum-rule-static-dynamic-identifiability]] for the closure relation, partial-sum diagnostic and static-versus-vibrational identifiability boundary.
