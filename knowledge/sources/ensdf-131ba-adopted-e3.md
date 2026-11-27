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
