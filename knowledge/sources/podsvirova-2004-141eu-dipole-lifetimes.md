---
type: source
title: "Investigation of lifetimes in dipole bands of 141Eu"
aliases: [podsvirova-2004-141eu-dipole-lifetimes]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: "Investigation of lifetimes in dipole bands of 141Eu"
authors: ["E. O. Podsvirova", "R. M. Lieder", "A. A. Pasternak", "S. Chmel", "W. Gast"]
year: 2004
journal: "European Physical Journal A"
volume: "21"
pages: "1-6"
doi: "10.1140/epja/i2004-10034-8"
canonical_source: "Eur. Phys. J. A 21, 1-6 (2004); DOI:10.1140/epja/i2004-10034-8"
source_url: "https://link.springer.com/article/10.1140/epja/i2004-10034-8"
raw_file: "raw/papers/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/2004-podsvirova-141eu.pdf"
raw_storage_status: raw-pdf-archived
raw_sha256: "31dd323d75f9a178e653bc88426482e3970a27183770dfd1771b514bbccdd503"
nuclei: [141Eu]
observables: [lifetime, B(M1), B(E2), B(M1)/B(E2)]
methods: [DSAM, EUROBALL-IV, SPAC, TAC]
tags: [141Eu, magnetic-rotation, DSAM, SPAC, TAC, band-crossing, multi-band]
---

# Investigation of lifetimes in dipole bands of 141Eu

## Bibliographic Record

E. O. Podsvirova et al., *Eur. Phys. J. A* **21**, 1–6 (2004), DOI `10.1140/epja/i2004-10034-8`. Published online 13 July 2004. Crossref identity and first-page title/author/DOI agree. The author field above is abbreviated; the complete 19-author list is retained in the downloaded paper and Crossref audit artifact.

Publisher PDF archived in `outputs/learning-daily/20261028-DAY26-octupole-e1-e3-magnetic-antimagnetic-rotation-run-01/multi-band-shears/141eu-springer.pdf` because this worker is not authorized to modify `raw/`. SHA-256: `31dd323d75f9a178e653bc88426482e3970a27183770dfd1771b514bbccdd503`; 717914 bytes; `%PDF-1.4`; 6 pages. Temporary extraction: same stem `.txt`. Retrieval details and rejected identity candidate are recorded in `retrieval-manifest.json`; the rejected unrelated paper is excluded from all claims.

## Summary

本工作利用 EUROBALL IV 阵列测量了 $^{141}\text{Eu}$ 中两条偶极带（DB1 与 DB2）的激发态能级寿命，提取了绝对 $B(M1)$ 与 $B(E2)$ 强度。研究展示了多重磁转动带在同一原子核中共存的特征，并利用考虑核芯演化的推转剪刀模型（SPAC）分析了背弯与初始剪刀开角排列。

## Scope and Reading Depth

Read PDF pp.1–6, including Table 1 and Figs.1–4. Table values below are transcribed from the paper's text layer; asymmetric uncertainties and inequality bounds are preserved. No supplementary file link was identified in the paper; publisher attachment inventory was not exhaustively audited. No raw spectra, code or numerical TAC/SPAC parameter table was obtained.

This paper measures **two** dipole bands, DB1 and DB2, with three lifetimes in each. A statement about three semiclassical branches from alternative initial orientations on p.4 describes a model possibility; it is not evidence that this experiment measured three lifetime bands.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| PO04-1 | EUROBALL IV DSAM uses the `114Sn(32S,3p2n)` reaction at 160 MeV; the level scheme also uses EUROBALL III `99Ru(48Ti,3p3n)` at 240 MeV. Three level lifetimes are reported in each of DB1 and DB2. | experimental-report | primary | pp.2–3,5; Table 1 | true |
| PO04-2 | DB2 reverses the previous placement of the 336.3 and 466.3 keV transitions; the latter is approximately 50% stronger. The adopted order is constrained by intensities and DSAM: reversing it gives a lifetime `≤0.05 ps` for the 336.3-keV transition and an inferred M1 strength about 20 times the other values. This is an author consistency argument. | experiment-and-interpretation | primary | pp.2–3; Figs.1–2 | true |
| PO04-3 | TAC assumes DB1 `πh11/2 ⊗ νh11/2^-2` and DB2 `πh11/2 ⊗ νh11/2^-4`, with `ε2=-0.07,-0.09`, respectively; `ε4=γ=0`, `Δπ=1.16 MeV`, `Δν=0.59 MeV`. Deformations were chosen to reproduce B(E2). | model-assumption | primary-model | p.5; Fig.4 | true |
| PO04-4 | The SPAC inverse initial alignment is energetically favored in the model. A change in collectivity at `Itr=18.7 ħ` is assumed to describe the backbend; the authors also tried a mixed-band crossing prescription and report that it describes the results less well. | competing-model-comparison | primary-model | pp.4–5; Figs.3–4 | true |
| PO04-5 | Lifetime/intensity uncertainties are propagated by Monte Carlo; the paper reports modes with 68% intervals, which differ from plugging central inputs into nonlinear formulas. Ratios from branching intensities are independent derived quantities. | statistical-method | primary | p.4 | true |

## Table 1 transcribed values

Units: `τ` ps; `B(M1)` μN²; `B(E2)` e²b²; ratio μN²/(e²b²). The original E2 column is in `10^-2 e²b²`; that scale is applied here.

| Band | Initial spin | τ | B(M1) | B(E2) | B(M1)/B(E2) |
|---|---|---|---|---|---|
| DB1 | 29/2− | 1.1 +0.4/−0.3 | 0.79 +0.51/−0.14 | not reported | not reported |
| DB1 | 31/2− | 2.5 +1.0/−0.5 | 0.75 +0.38/−0.15 | 0.041 +0.023/−0.009 | 17 +3/−2 |
| DB1 | 33/2− | 1.1 +0.4/−0.3 | 0.37 +0.24/−0.06 | 0.023 +0.017/−0.005 | 16 +8/−3 |
| DB1 | 35/2− | not reported | not reported | not reported | 11 +3/−1 |
| DB2 | 37/2− | not reported | not reported | not reported | 299 +178/−54 |
| DB2 | 41/2− | 0.55 +0.25/−0.20 | 0.77 +0.76/−0.13 | ≤0.045 | ≥17 |
| DB2 | 43/2− | 0.8 ±0.2 | 1.32 +0.69/−0.22 | 0.064 +0.041/−0.020 | 17 +15/−2 |
| DB2 | 45/2− | 0.29 +0.20/−0.15 | 0.50 +0.84/−0.07 | not reported | not reported |

The 41/2− bounds follow a transition-intensity limit with a 68% confidence interval; they are not detected finite crossover strengths. The `37/2−` ratio of 299 is reported without an absolute lifetime, so it is not an absolute M1 enhancement measurement.

For the 43/2− example, the paper uses relative intensities `2.7±0.3` for 336.3 keV and `0.8±0.3` for 802.6 keV. Plugging central values into its standard formulas yields `B(M1)=1.44±0.42` and ratio `20±8`; Monte Carlo mode estimates give `1.32 +0.69/−0.22` and `17 +15/−2`. Dividing the separately reported modal M1 and E2 values is therefore not expected to recover exactly the reported modal ratio. The study does not publish the full joint likelihood or raw Monte Carlo samples.

## Model and Claim Boundaries

SPAC treats the core vector along the principal rotation axis and minimizes the energy over two blade angles. In general the vector identity is `I = j1 + j2 + R`; a scalar `I=Js+R` holds only under the extra assumption that the core and resultant shears vectors are parallel. The paper explicitly distinguishes its SPAC geometry from that collinear approximation (p.4).

The paper supports coexisting dipole sequences with different assumed neutron-hole configurations and a structural change. It does not report a measured off-diagonal band-mixing matrix element `W`, nor does it establish that a two-level avoided-crossing model is the preferred explanation of its backbend. Its inverse-alignment solution and spin-dependent collectivity must remain visible as alternatives.

The decline of B(M1) is not established as a universal monotonic law over all its data: the DB2 central values `0.77 → 1.32 → 0.50` are nonmonotonic and have broad overlapping intervals. These six lifetimes do not measure a unique continuous shears-angle trajectory or V2 for each band.

## Competing Interpretations and Limitations

实验直接测得的是 DB1 和 DB2 两条带的能级寿命与光子分支比；两带之间的能带排斥、避免交叉以及两态混合矩阵元属于模型唯象假设，而非直接实验观测。非对角跃迁矩阵元未测，两带的非单调跃迁比亦不能单独反演唯一的连续剪刀角轨迹。

## Extracted Pages

- [[multi-band-shears-coexistence-pb-141eu-139sm-boundary]]

## Connections

- [[magnetic-rotation]]
- [[multi-band-shears-coexistence-pb-141eu-139sm-boundary]]
- [[hubel-2005-magnetic-rotation-review]] — review context, not an independent repeat of this measurement.

Self-audit only; no human review, paper-level approval or independent experimental replication is claimed.
