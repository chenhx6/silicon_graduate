---
type: source
title: "NNDC 225Ac Adopted：低能交替宇称伙伴与40.09-keV E1"
aliases: [NNDC225Ac parity doublet adopted, Ac225 40.09 keV E1]
created: 2026-10-28
updated: 2026-10-28
status: ai-draft
review_status: unreviewed
source_type: evaluated-nuclear-data
reading_depth: skimmed
title_original: "225AC ADOPTED LEVELS, GAMMAS"
authors: [Balraj Singh]
journal: ENSDF evaluation
year: 2022
volume: "2022-07 evaluation"
pages: "not applicable"
citation_key: NNDC225AcAdopted2022
citation_key_origin: ENSDF-header-local-key
canonical_source: "NNDC ENSDF 225089001,225AC, ADOPTED LEVELS GAMMAS"
source_url: "https://www.nndc.bnl.gov/ensdf/"
data_version: "2022-07 listing; cutoff 25-Oct-2019"
raw_storage_status: "official-response-archived-as-retrieved-html-wrapper"
raw_file: "raw/data/gpt/learning-daily/20261028-DAY26-octupole-correlation-e1-e3-magnetic-rotation/225ac-adopted-225089001-028.html"
raw_sha256: "fb3d87428e000397881227c3dc96973c1765310a7811062cc8c297259872a817"
nuclei: [225Ac]
observables: [level-energy, spin-parity, B(E1), half-life, gamma-branch-intensity]
methods: [ENSDF-evaluated-fixed-column, alpha-decay-and-beta-decay-spectroscopy]
tags: [parity-doublet, odd-A, actinium, octupole, evaluated-data, source-lineage]
---

# $^{225}$Ac 的评价能级与 E1 记录

## Bibliographic Record

NNDC `DatasetFetchServlet(nuc=225Ac,searchType=quick,datasource=ensdf)` 列出 `225089001,225AC` Adopted；以 `EnsdfDispatcherServlet(dbclass=ensdf,page-source=singular,datasetcheck=225089001,225AC,chooseit=ENSDF text format)` 获取固定栏对象。H 行标记 Balraj Singh、2022-07 评价、cutoff 25-Oct-2019。归档文件为官方响应的 HTML 包裹 ENSDF `<pre>` 文本，SHA-256 记录于 frontmatter。

## Scope and Reading Depth

定向读取低能 0–257 keV 的 L/G/B 记录、带标签、Jπ 注释和 40.09-keV E1 的评价字段。未重读原始 1973Ag01、1985Is03 等实验论文；本页的数值是评价对象，不能写成新采集的原实验数据。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| AC225-1 | 评价基态为 $(3/2^-)$；低能 A 带列 $(5/2^-)$ 29.91、$(7/2^-)$ 77.13 keV，另有 C 带 $(5/2^-)$ 120.81、$(7/2^-)$ 170.75、$(9/2^-)$ 235.53 keV。B/D 正宇称带列 $(3/2^+)$ 40.10、$(5/2^+)$ 64.69、$(7/2^+)$ 105.01、$(9/2^+)$ 144.96、$(5/2^+)$ 155.64、$(7/2^+)$ 199.86、$(9/2^+)$ 256.97 keV。多数 Jπ 加括号，带归属依赖评价。 | evaluated-level-data | direct-evaluated-object | archived ENSDF lines 65–161; BAND(A–D) comments | true |
| AC225-2 | $40.10(4)$-keV $(3/2^+)$ level decays by $40.09(5)$-keV E1 to $(3/2^-)$ ground state; evaluation gives $B(E1)=0.00171(15)$ W.u. from conversion-electron subshell ratios in $^{225}$Ra β− decay. | evaluated-transition-strength | direct-evaluated-object | L96–103, G40.09, B `BE1W=0.00171 15` | true |
| AC225-3 | Same-spin energy differences are non-unique because several levels share $5/2^+$, $7/2^+$ and $9/2^+$ labels: e.g. $E(5/2^-_{A})-E(5/2^+_{B})=-34.78$ keV, $E(5/2^-_{C})-E(5/2^+_{B})=+56.12$ keV; $E(7/2^-_{A})-E(7/2^+_{B})=-27.88$ keV and $E(7/2^-_{C})-E(7/2^+_{B})=+65.74$ keV. These are evaluated level differences, not a unique parity-doublet splitting. | derived-from-evaluated-levels | evaluated-object-arithmetic | L90–170 paired level entries | true |
| AC225-4 | A conditional axial $K=3/2$ rotor extraction from the $I=3/2\to I=3/2$ E1 line gives $D_0\approx0.169\pm0.007$ e fm using $1.2A^{1/3}$ E1 Weisskopf units and $|\langle IK10|IK\rangle|^2=K^2/[I(I+1)]=0.6$. This is a convention-dependent inference, not an evaluated $D_0$. | conditional-model-inference | derived-from-evaluated-object | AC225-2 plus stated rotor convention | true |

## Summary

The evaluated $^{225}$Ac scheme contains a low-energy $3/2^-$–$3/2^+$ pair separated by 40.10 keV and an evaluated E1 strength $0.00171(15)$ W.u. Several additional same-spin levels occur in different bands, so a single $ΔE(I)$ sequence cannot be declared without a band and configuration selection. The E1 line is an evaluated transition record; its source chain includes conversion-electron data in $^{225}$Ra β decay.

## Competing Interpretations and Limitations

The ground-state and low-band Jπ labels are often tentative (parentheses), and the A–D band labels are adopted Nilsson/systematics assignments. A 40-keV separation alone does not establish a static octupole shape or a rigid parity doublet. The $B(E1)$ value does not provide a model-independent $D_0$; the conditional extraction assumes axial $K=3/2$, a shared intrinsic dipole, the stated Weisskopf radius, and no unresolved branch contribution. Original experiment papers and full covariance were not reread.

## Knowledge Impact and Learning Decision

`supports` a direct evaluated benchmark for odd-A actinium; `limits` claims of a unique parity-doublet ladder and universal E1 scale. It provides a concrete comparison target for $^{225}$Ra while preserving evaluation-versus-primary-source boundaries.

## Extracted Pages

- [[odd-a-parity-doublet-blocking-audit]]: conditional two-state and E1/E2 geometry.
- [[nndc-2009-ra225-adopted-parity-doublet]]: neighboring evaluated Ra scheme.

## Sources

- NNDC ENSDF `225089001,225AC`, official response archived under the raw path above.
- Original source keys cited by evaluation include 1973Ag01 and 1985Is03; full papers not reread in this task.
