---
type: source
title: "Hauschild1995：133Ce超形变带与高自旋组态线索"
aliases: [Hauschild 1995 133Ce SD bands, 133Ce superdeformed 1995]
created: 2026-10-27
updated: 2026-10-27
status: ai-draft
review_status: unreviewed
source_type: experimental-paper-with-model-comparison
reading_depth: deep-read
title_original: "Neutron orbitals above the N = 74 shell gap at large deformation: spectroscopy in the superdeformed minimum of 133Ce"
authors: [K. Hauschild, R. Wadsworth, R. M. Clark, P. Fallon, D. B. Fossan, I. M. Hibbert, A. O. Macchiavelli, P. J. Nolan, H. Schnare, A. T. Semple, I. Thorslund, L. Walker, W. Satuła, R. Wyss]
year: 1995
journal: Physics Letters B
volume: 353
pages: 438–443
doi: 10.1016/0370-2693(95)00601-G
canonical_source: https://doi.org/10.1016/0370-2693(95)00601-G
citation_key: ""
raw_file: raw/papers/1995_Hauschild_133Ce_superdeformed_bands.pdf
raw_sha256: ce219bb983b42a15cb634f95e9ad99bcfbc8442bc179a5e5f0e613b9ac9958fb
raw_storage_status: public-staging-not-archived
actual_body_file: tmp/day24-ce133-primary-followup-081/1995Ha34-full.pdf
nuclei: [133Ce, 132Ce, 136Nd]
reactions: [116Cd-22Ne-5n-133Ce]
experiments: [gammasphere-superdeformed-133Ce-1995]
models: [extended-pairing-deformation, cranked-shell, total-routhian-surface]
methods: [gamma-gamma-gamma-coincidence, variable-spaced-lattice-search, dynamic-moment-of-inertia]
observables: [superdeformed-band, J2, alignment, transition-energy]
tags: [133Ce-analysis-blueprint, high-spin-superdeformed, configuration-boundary]
---

# 超形变带是真实观测节点，构型和形状仍需条件化

## Bibliographic Record

K.Hauschild等，PLB353(1995)438–443，DOI10.1016/0370-2693(95)00601-G。081通过NNDC adopted reference identity及Elsevier MAIN object取得真6页、690165bytes、SHA见frontmatter。本文与Gizon低spin、Emediato低spin RDDS和Joss高spin normal-triaxial DSAM均为不同反应/观测合同。

## Scope and Reading Depth

全文6页、Figs1–3、Table1和结论均读及视觉核。原件无τ/Qt/绝对B、linking transitions或DCO；SI入口未识别补充材料。未运行模型producer或重拟J(2)。

## Summary

Hauschild等在独立Gammasphere反应中识别三条133Ce超形变带，并给出J(2)、alignment和条件性PES/构型解释；缺 linking、τ、Qt、绝对B和DCO，不能把高自旋SD节点直接等同低自旋三轴或手征伙伴。

## Key Results

新claims全needs_review:true。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| HA95-D24-001 | 116Cd(22Ne,5n)120MeV、Gammasphere早期31个大HPGe、约1.5×10^9 suppressed-fold events和3.5×10^9 triples，得到133Ce高自旋SD谱。 | direct-experimental-setup | direct-original | PDF1–2/438–439 | true |
| HA95-D24-002 | 三条弱SD带由变间距晶格搜索和三重符合识别，relative populations约3%、1.5%、.6%。 | direct-band-observation | direct-original | PDF2–3/Fig1 | true |
| HA95-D24-003 | 未观察到SD→normal linking，Jπ未知；约4ħ unseen links给初始估计43/2、37/2、45/2，Band2后续按6ħ link采纳41/2以匹配132Ce。 | spin-identity-boundary | direct-original | PDF3, PDF5 | true |
| HA95-D24-004 | 带内间距约70keV、E2为工作假设；90°统计不足不能作方向关联。 | multipolarity-boundary | direct-original | PDF3 | true |
| HA95-D24-005 | Bands1/2的J(2)接近132Ce yrast SD、约ħω.4MeV外流；Band3在约.70MeV有J(2) hump。 | derived-rotational-observable | direct-original | PDF3–4/Fig2 | true |
| HA95-D24-006 | extended-pairing/deformation calculation给SD β2≈.40 β4≈.01 γ≈0，且一signature有β2≈.30低形变共存minimum；均为模型PES。 | model-PES-result | model-result | PDF4/Fig3 | true |
| HA95-D24-007 | Band1在1132–1570keV与132Ce yrast identical，rms1.0keV；[530]1/2− alignment计算1.6(1)ħ。 | literal-band-comparison | direct-plus-model | PDF4/Fig3c | true |
| HA95-D24-008 | Bands1/2 tentative [530]1/2− coupled to π(h11/2)^4ν(i13/2)^2；Band3 tentative π(h11/2)^4ν(i13/2)^3/[530] pair alignment。 | conditional-configuration | author-model | PDF4–6/Fig3 | true |
| HA95-D24-009 | Band3 Δix约3.9ħ measured vs3.5ħ single-particle diagram；νi13/2 mixing解释为tentative。 | alignment-model-comparison | derived-and-interpretation | PDF5–6 | true |
| HA95-D24-010 | 新SD节点无τ、Qt、absolute B(E2)、linking transitions或DCO；不把J(2)/E2 assumption升级配置/静态形状/手征证据。 | explicit-companion-observable-gap | direct-boundary | PDF3–6 | true |

## Competing Interpretations and Limitations

Reaction/campaign differs from Joss 1998 (100Mo(36S,xn) DSAM normal triaxial band), Gizon 1974 (120Sn(16O,3n) low-spin), and Emediato 1997 (120Sn(16O,3n) RDDS). Author/model lineage overlaps with later literature, but events and principal observables are distinct. High-spin SD bands are a new evidence node; they do not fill missing lifetimes or low-spin 582 references, and conditional spin/configuration labels cannot be merged with modern BandF by name alone.

## Extracted Pages

- [[133ce-thesis-analysis-blueprint]]
- [[joss-1998-133ce-triaxial-band-lifetimes]]
- [[gizon-1974-deformed-states-cerium-neodymium]]


Day24 SD primary link: [[hauschild-1995-133ce-superdeformed-bands]]
