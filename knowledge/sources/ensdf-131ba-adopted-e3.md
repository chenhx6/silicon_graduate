---
type: source
title: "ENSDF adopted levels and gammas for 131Ba"
aliases: [131Ba ENSDF adopted levels, 131Ba 79.918 keV E3, 131Ba weak E3 control]
created: 2026-11-01
archive_required: true
updated: 2026-11-27
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
title_original: "Adopted Levels, Gammas"
authors: ["Yu. Khazov", "I. Mitropolsky", "A. Rodionov"]
journal: "Nuclear Data Sheets"
year: 2006
volume: 107
pages: 2715
language: en
canonical_source: "https://www.nndc.bnl.gov/ensnds/131/Ba/adopted.pdf"
source_url: "https://www.nndc.bnl.gov/ensnds/131/Ba/adopted.pdf"
citation_key: Khazov2006BA131
raw_file: "raw/papers/gpt/learning-daily/20261101-day29-131ba-e3/131ba-adopted.pdf"
raw_sha256: 11bdfe04709d0652640b1d4af1f33ea9d26e1855d881a5a0f8be56cf24a80ee3
raw_storage_status: verified-public-web-archive
retrieval_date: 2026-11-01
ensdf_cutoff: 2006-07-17
nuclei: [131ba]
reactions: ["122Sn(13C,4nγ)", "122Sn(12C,3nγ)", "130Ba(d,p)"]
experiments: [ensdf-evaluation]
models: [evaluated-level-data]
observables: [excitation-energy, spin-parity, e3-transition-strength, internal-conversion]
methods: [evaluated-level-data, gamma-spectroscopy]
tags: [131ba, e3, octupole, ensdf, weak-e3-control]
---

# ENSDF adopted levels and gammas for `131Ba`

## Bibliographic Record

The archived NNDC/ENSDF PDF identifies the full evaluation by Yu. Khazov,
I. Mitropolsky and A. Rodionov, *Nuclear Data Sheets* 107, 2715 (2006), with a
17-Jul-2006 literature cutoff. The public PDF was downloaded from the NNDC ENSDF
endpoint and its SHA-256 is recorded above.

## Scope and Reading Depth

The adopted-level and gamma tables, XREF flags and the `79.918-keV` transition row
were read. This is an evaluated data record, not a new experiment and not a
reanalysis of the raw `122Sn(13C,4nγ)` data.

## Key Results

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ENSDF131BA-1 | 187.995(9) keV 态的 T₁/₂=14.6(2) min，表中归 1963Ho05。与 108.077(5) keV 相连的 79.918 keV E3 用这对能级识别。 | evaluated-level-and-transition | direct | PDF p.1 level table; PDF p.5 gamma table | true |
| ENSDF131BA-2 | 该 79.918 keV E3 的 α=80.1 为 frozen-orbital BrIcc 总内转换系数，Iγ=100 和 %IT=100 有不同含义。 | evaluated-transition-strength | direct | PDF p.5, `γ(131Ba)` table row for `Ei=187.995`, `Eγ=79.918` | true |
| ENSDF131BA-3 | 187.995(9)→108.077(5) keV 这一评估跃迁应和另一个 79.918 keV 条目分开。XREF C 把相关能级关联至 Sn 反应。 | source-and-independence-boundary | direct | PDF p.1 XREF legend; PDF p.5 gamma-table provenance | true |
| ENSDF131BA-4 | 由评估半衰期、分支和 BrIcc 可求条件辐射寿命，需注明取的是平均寿命或半衰期及强度归一。 | derived-response-consistency | conditional derivation | PDF p.1 adopted half-life; PDF p.5 E3 row; E3 rate convention in `actinide-isomers-k-mixing-and-octupole-selection-rules` | true |
| ENSDF131BA-5 | 812 s 是按选定寿命、分支和转换约定做的条件重构。 | derived-response-budget | conditional derivation | PDF p.1 `%IT=100`; PDF p.5 E3 row; `fγ=1/(1+α)` | true |

## Summary

The evaluated table supplies a real weak E3 transition that can serve as a response and
negative-control anchor. It does not close a strong collective E3 interpretation for the
high-spin E1-linked bands.

## Competing Interpretations and Limitations

The adopted `B(E3)` is an evaluated strength with source dependence and no event-level
producer, efficiency ledger, feeding covariance or lifetime reanalysis in this task.
The weak transition may be useful for calibration without implying that the high-spin
E1 network has the same structure. A strong high-spin E3 branch, if sought, requires a
separate state-identity, lifetime and absolute-strength measurement.

## Extracted Pages

- PDF p.1: evaluation identity, cutoff, XREF flags and adopted levels.
- PDF p.5: `γ(131Ba)` table row for `187.995-keV → 108.077-keV`, `79.918-keV`
  E3, `α=80.1` and `B(E3)=0.00087(3) W.u.`.

## Interpretation Boundary

The weak adopted E3 is useful as a low-energy conversion-electron/γ response and
negative-control anchor for a future `131Ba` experiment. Its very small strength does
not support a strong static-octupole claim. It also does not close the high-spin
`D7→D3–D6` E1-network question, for which the Guo source still lacks an absolute
E3/lifetime matrix.

The evaluated `B(E3)` should therefore be used in the prospectus as a calibration
or falsification control: a new setup must reproduce the low-energy E3 response and
conversion treatment before interpreting a weak or strong high-spin branch.

The conditional rate cross-check is close enough to support use as a response sanity
test, but its agreement is not independent evidence: it reuses the adopted strength,
conversion coefficient and half-life, and depends on the Weisskopf radius and practical
rate convention.

The large `α` also makes this line electron dominated under the stated complete-branch
condition. A future response study should therefore calibrate the electron transport
and threshold before using the weak γ line as an efficiency anchor; the `98.8%` value
is a conditional branching fraction from the adopted coefficient, not a measured new
electron yield.

## Knowledge Impact and Learning Decision

`supports`: a `131Ba` direct-E3 proposal can include a real weak-E3 control line and
an explicit conversion-electron/γ response test.

`revises`: the statement “no E3 information exists in A≈130 `131Ba`” is too broad.
The accurate boundary is that an evaluated weak E3 exists, while a strong,
state-resolved collective E3 matrix for the high-spin E1 network remains missing.

`limits`: this page does not provide event-level counts, raw efficiency, feeding,
lifetime producer or joint covariance.

## Human Review

This page is a Codex self-audit and remains `unreviewed`; it does not set
`human-reviewed`.

## 2026-11-27 — 馆藏原件与覆盖核对

Scientific content audited at PDF 1, 5 and 11 footnote c; document mapped at PDF 1–4 levels, 5–11 γ tables, 12–18 level-scheme panels, 19–20 band drawings. Remaining rows and panels lack point-by-point review.

- Specify 187.995(9)→108.077(5) keV as a second 79.918-keV entry has different multipolarity. Isomer T₁/₂=14.6(2) min is explicitly credited to 1963Ho05. XREF C associates the level with the Sn reactions. 原页 PDF 1 level comments; PDF 5 γ rows。
- Use calculated total BrIcc (frozen orbital) α=80.1. Keep 812 s as a convention-dependent conditional reconstruction and distinguish Iγ=100 from %IT=100. 原页 PDF 11 footnote c; PDF 5 E3 γ row; PDF 1 level comments。

## 2026-11-27 — 本地关联载体核对

本地 20 页 NNDC 评价导出全部核定。母评价和底层反应各有独立身份。

- 路径 `raw/papers/gpt/learning-daily/20261101-day29-131ba-e3/131ba-adopted.pdf`
- SHA-256 `11bdfe04709d0652640b1d4af1f33ea9d26e1855d881a5a0f8be56cf24a80ee3`
- 实读 PDF 2–20 与旧已核的 PDF 1、5、11 证据合并。

- {'title': 'Low-lying electromagnetic benchmark', 'claim': 'The 108.077-keV 3/2⁺ level decays to 0.0 keV, 1/2⁺, by 108.081(5)-keV M1+E2 with δ=+0.127(14), total α=0.812(3), B(M1)=0.027(4) W.u. and B(E2)=24(7) W.u. The schemes label the level half-life 0.35(5) ns.', 'locator': 'PDF 5 first γ row; PDF 15–18 level labels, PDF 18 low-lying panel and PDF 19 Band A; PDF 11 notes b–c for δ and α conventions.', 'boundary': 'Useful same-export low-energy mixed-transition anchor. The two B values share a mixed transition and evaluated inputs; the diagram repeats the same adoption.'}
- {'title': 'Yrast negative-parity E2 backbone', 'claim': 'The evaluated yrast Band C has a ΔJ=2 E2 chain in descending energy 3717.7 (27/2⁻) → 2611.53 (23/2⁻) → 1683.01 (19/2⁻) → 898.72 (15/2⁻) → 287.52 (11/2⁻), with Eγ=1106.2(3), 928.5(3), 784.4(3) and 611.3(3) keV. The opposite signature branch includes 899.5(3) keV flagged as a ¹³²Ba doublet and 752.2(3) keV reported at Iγ<69.', 'locator': 'PDF 6 Ei=898.72, 1458.67; PDF 7 Ei=1683.01; PDF 8 Ei=2358.10, 2611.53; PDF 9 Ei=3717.7; PDF 11 note @; PDF 19 Band C.', 'boundary': 'Energies, placements and adopted multipolarities provide a comparison backbone. The relative-intensity limits, doublet flag and absence of absolute high-spin strengths remain explicit. The νh₁₁/₂ assignment is an evaluated interpretation.'}
- {'title': 'Parity-changing links and confidence', 'claim': 'The 1403.0(3) and 1421.4(3) keV rows give (E1+M2), δ=−0.03(6) and −0.05(5), for 2109.4→706.45 and 2320.10→898.72. At 2561.28→1458.67, 1102.5(3) keV is (E1+M2) with δ=+0.04(12). The 680.5(3) keV G→F and 699.4(3) keV 3057.40→2358.10 links are (E1); 1075(1) keV at 2533.9→1458.67 is tabulated E1 with Iγ<24.', 'locator': 'PDF 2 Jπ comments; PDF 7 Ei=2109.4, PDF 8 Ei=2320.10, 2533.9, 2561.28, 2725.38; PDF 9 Ei=3057.40; schematics PDF 13–15 and 19–20.', 'boundary': 'Keep parentheses, signed uncertainties and bounds. These are adopted character/placement constraints, with no absolute B(E1) or collective E3 strength inferred from them.'}
- {'title': 'Two 2795-keV levels with separate branches', 'claim': 'PDF 3 lists 2795.43(22) keV (21/2⁺) and 2795.51(24) keV (23/2⁻). The final fit fixed both energies. For example, the lower nominal Ei has 234.1(3)-keV M1+E2 to 2561.28, while the upper nominal Ei has 750.5(3)-keV E2 to 2045.24. The nearby 750(1)-keV row from 2795.43 also feeds 2045.24 and has no adopted multipolarity in the table.', 'locator': 'PDF 3 two level rows; PDF 4 level footnote b; PDF 8 separate parent blocks; PDF 13–14, Band B on PDF 19 and Band F on PDF 20.', 'boundary': 'The 0.08-keV difference of the listed central values is smaller than either quoted marginal uncertainty. Use branch topology, adopted Jπ and endpoint IDs. PDF 4 footnote b prints 1795.51; the tables and drawings agree on 2795.51.'}
- {'title': 'Band assignments and limits', 'claim': 'The export groups A–E on PDF 19 and F–J on PDF 20. A has a probable configuration, E/F are ΔJ=2 candidates with caption γ=−40°/−80°, and H/I/J are possible rotational sequences. The highest listed parent energies 6174.4?, 6235.6?, 6365.0? and 6440.9? keV carry question marks and their Jπ are parenthesized.', 'locator': 'PDF 4 notes c–l and a; PDF 10 final γ blocks; PDF 12 high-energy panel; PDF 19–20 band captions and dashed endpoints.', 'boundary': 'The triaxial parameters and configurations are assignments in the evaluation. The fit and drawings do not give independent shape or chirality measurements.'}
- {'title': 'Photon branch and notation rules', 'claim': 'Iγ is relative photon branching from each parent level, so 100s from different parents have separate normalizations. PDF 11 records weighted averaging and selection of ε-decay branching for # rows when datasets disagree. @ flags a ¹³²Ba doublet, & a multiplet, and d an uncertain placement. The mult column distinguishes a printed mixture such as M1+E2 from alternatives such as M1,E2 and generic D. Adopted character uses α(exp), angular and DCO information with the stated E2 and in-band D+Q assumptions.', 'locator': 'PDF 11 notes †, ‡, #, @, &, a–d and diagram legends PDF 12–18. Examples PDF 5 542.89-keV weighted branch comments and PDF 8 2795-keV blocks.', 'boundary': 'No absolute photon yield or total branch fraction follows from Iγ alone; conversion, full branching and consistent normalization would be needed.'}
