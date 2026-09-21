---
type: source
title: "Starosta et al. 1999 - Experimental test of the polarization direction correlation method"
aliases: [Starosta 1999 PDCO]
created: 2026-09-20
updated: 2026-09-20
status: ai-draft
review_status: unreviewed
source_type: method-paper-and-application
reading_depth: deep-read
title_original: "Experimental test of the polarization direction correlation method (PDCO)"
authors: [K. Starosta, T. Morek, Ch. Droste, S. G. Rohozinski, J. Srebrny, A. Wierzchucka, M. Bergström, B. Herskind, E. Melby, T. Czosnyka, P. J. Napiorkowski]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1999
citation_key: starosta_1999_Experimental
volume: 423
pages: "16-26"
pii: "S0168-9002(98)01220-0"
canonical_source: "Starosta et al., NIM A 423, 16-26 (1999)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1999_Starosta et al_Experimental test of the polarization direction correlation method (PDCO).pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1999_Starosta et al_Experimental test of the polarization direction correlation method (PDCO).pdf"
raw_sha256: "883fdd7b08831efefe25f5df610e84b95bb1acbcd7b8e7f684b1a1b31bf8030b"
nuclei: [162Yb, 152Ba, 130Cd, 132Sn]
reactions: [136Ba-30Si-4n, 112Cd-16O-4n, 112Cd-16O-Coulomb-excitation, 114Sn-16O-Coulomb-excitation]
experiments: [EUROGAM-II, NORDBALL-clover-calibration]
models: [PDCO, DCO, integrated-PDCO, polarization-angular-distribution]
observables: [linear-polarization, Compton-asymmetry, DCO-ratio, spin-alignment, multipole-assignment]
methods: [Compton-polarimetry, PDCO, DCO-ratio, gamma-gamma-angular-correlation]
tags: [PDCO, CLOVER, EUROGAM-II, polarization, DCO, multipolarity]
---

# Experimental test of the polarization direction correlation method (PDCO)

## Bibliographic Record

- K. Starosta *et al.*, *NIM A* **423**, 16–26 (1999), PII `S0168-9002(98)01220-0`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1999_Starosta et al_Experimental test of the polarization direction correlation method (PDCO).pdf`。

## Scope and Reading Depth

- PDF pp.16–26 fully read: EUROGAM-II geometry, NORDBALL CLOVER calibration, `Q(E)` fit, DCO alignment extraction, integrated-PDCO asymmetry, four detector-pair geometries, Tables 1–4, Figs.1–7 and conclusions.
- Not covered: the cited original level-scheme papers, PDCO program source code and raw coincidence matrices.

## Key Results

- The paper tests PDCO in EUROGAM-II (30 coaxial Ge plus 24 CLOVER detectors) using a `162Yb` fusion-evaporation case; a single CLOVER/NORDBALL calibration is used as an approximation for the array response (PDF pp.16–18).
- The CLOVER asymmetry is related to physical polarization by `A=QP`; calibration reactions give `Q=0.30(3)` at 256 keV down to `0.15(1)` at 1230 keV, and the fitted response is `Q=Q0(0.31(2)+7(2)×10^-4 Eγ)` (PDF pp.18–19, Table 1, Eq.5).
- For the 490-keV `16+→14+` candidate, integrated mode gives `A=+0.120(12)` and estimated `P=+0.50(5)`, while `R_DCO=0.96(2)`; the combined `(P,R_DCO)` contours exclude most hypotheses but retain stretched E2 and an `M1/E2, ΔI=0, arctanδ≈−21°` solution (PDF pp.20–24, Figs.5–6, Tables 2–3).
- For the 647-keV `11−→10+` transition, `R_DCO=0.51(3)` and the PDCO fit uniquely favors `ΔI=1` E1 among the tested hypotheses (PDF pp.24–25, Table 4).
- The authors conclude that intensity as low as about 15–20% of the strongest transition can be useful, but integrated-PDCO comparisons are qualitative unless detector solid-angle and efficiency corrections are known (PDF pp.25–26).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST99-1 | PDCO combines a direction-sensitive CLOVER polarization measurement with a coincident-gamma DCO ratio to reduce multipolarity ambiguity. | method-result | direct | PDF pp.16–17, 22–25 | true |
| ST99-2 | The 490-keV case remains non-unique between stretched E2 and a ΔI=0 M1/E2 branch after the combined fit. | assignment-boundary | direct | PDF pp.22–25, Tables 2–3 | true |
| ST99-3 | The 647-keV transition is assigned as ΔI=1 E1 within the tested hypotheses. | assignment-result | direct | PDF pp.24–25, Table 4 | true |
| ST99-4 | `Q`, detector geometry, solid-angle coverage, efficiencies and assumed alignment are setup-specific inputs. | limitation | direct | PDF pp.18–20, 21–26 | false |

## Summary

Starosta *et al.* provide a practical validation of PDCO for modern CLOVER arrays. The experiment demonstrates the value of combining polarization and DCO information, while its unresolved 490-keV branch is a counterexample to treating a clean `R_DCO` or polarization sign as a unique spin assignment.

## Competing Interpretations and Limitations

- Integrated mode smears directional information over a large solid angle. Without correction for detector coverage and relative efficiency, its polarization should be treated as qualitative (PDF pp.21–22, 26).
- The assumed spin-alignment parameter `p/I=0.26(5)` is inferred from a different 647-keV cascade and transferred to the 490-keV transition; this is a model assumption.
- The single-CLOVER NORDBALL calibration is used as a proxy for the 24-CLOVER EUROGAM response. Thresholds, geometry and asymmetry correction `a` may alter `Q` and `P`.
- The remaining E2 versus mixed M1/E2 ambiguity requires additional evidence such as conversion coefficients or an independent level assignment.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| ST99-AR-1 | Response chain | Unpolarized asymmetry correction `a` → measured Compton asymmetry `A` → detector sensitivity `Q(E)` → physical `P`; DCO supplies alignment/multipole constraints. | PDF Eqs.1–6, pp.18–20 | self-checking |
| ST99-AR-2 | Joint-fit chain | Four polarimeter/geometries plus DCO are compared with polarization-angular-distribution calculations through the reduced `s_J²` fit. | PDF Eq.7, Figs.6–7, Tables 2–4 | self-checking |
| ST99-AR-3 | Transfer condition | `Q`, `p/I`, gate cascade, detector positions and convention must be re-established before reusing a PDCO contour. | PDF pp.18–24 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]] and the DCO/PDCO evidence map.
- New reusable rule: a combined polarization–DCO fit can narrow, but need not eliminate, spin/mixing-ratio branches; retain a branch table until independent conversion/lifetime/configuration evidence closes it.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `ST99-P0-1`: Do not transfer the reported `Q(E)`, `p/I`, `P` or `s_J²` contours to another CLOVER array without geometry, threshold, asymmetry-correction and alignment recalibration.

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]]。
