---
type: source
title: "Warda–Robledo 2011：锕系团簇放射性的 Gogny-HFB 非对称裂变通道"
aliases: [Warda 2011 cluster radioactivity, Microscopic description of cluster radioactivity in actinide nuclei]
created: 2026-10-29
updated: 2026-10-29
status: ai-draft
review_status: unreviewed
source_type: journal-article-theory
reading_depth: skimmed
canonical_source: "Phys. Rev. C 84, 044608 (2011); arXiv:1107.1478v1"
raw_file: "raw/papers/gpt/day26-20261028/warda-2011-actinide-cluster-radioactivity-arxiv1107.1478v1.pdf"
raw_sha256: "632768452a96e8fdc9f9abc45caebbdfef154796962ee6cac41e31c360d54aa9"
title_original: "Microscopic description of cluster radioactivity in actinide nuclei"
authors: [M. Warda, L. M. Robledo]
year: 2011
journal: Physical Review C
volume: "84"
pages: "044608"
doi: "10.1103/PhysRevC.84.044608"
source_url: "https://arxiv.org/abs/1107.1478v1"
raw_storage_status: "raw-pdf-archived-new-original"
staging_file: "tmp/day26-cluster/1107.1478.pdf"
staging_sha256: "632768452a96e8fdc9f9abc45caebbdfef154796962ee6cac41e31c360d54aa9"
nuclei: [222Ra, 224Ra, 226Ra, 226Th, 228Th]
observables: [cluster-decay-half-life, Q30, neck-density, fission-barrier]
methods: [Gogny-D1S-HFB, constrained-mean-field, ATDHFB-cranking-inertia, WKB]
tags: [cluster-radioactivity, octupole, hyper-asymmetric-fission, pairing, source-boundary]
---

# 锕系团簇放射性的微观非对称裂变描述

## Bibliographic Record

Crossref 的题名、两位作者和 DOI 与取得的 arXiv:1107.1478v1 首页相符；该预印本19页、3434371 bytes、文件签名 `%PDF-`，已核验上述 SHA-256。PDF首页2018年排版日期不改变2011年 arXiv 版本/期刊年份。已逐文件核验后以新增原件归档至frontmatter所列raw路径；没有覆盖既有文件。官方检索地址和哈希见frontmatter与审计JSON。

## Scope and Reading Depth

定向阅读 PDF1–5、10–13、15–17：模型与约束、Eqs2–7、224Ra势能面与密度、颈约束、Table I、EDF/零点修正局限；未逐项重算15个核素的HFB网格、惯性或最小作用量路径。Table I 的“实验值”是本文引用的既有实验，不构成独立测量。

## Summary

通过Gogny-HFB的八极/颈约束与WKB作用量，将团簇放射性描述为超非对称裂变；低能八极强度不是独立P0测量。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| WR11-1 | 轴对称Gogny-D1S HFB以四极、八极及颈约束寻找团簇放射性的超非对称裂变通道；Q30比常规Q20更适合作为此类通道的主坐标。 | model-method | direct-original-preprint | PDF1–4, Eqs2–7 | true |
| WR11-2 | 224Ra基态约Q20=8.3 b、beta2=0.18、Q30=4.2 b^(3/2)、beta3=0.14；团簇通道涉及更大Q30和颈缩，不能与低能beta3振动直接等同。 | model-result | direct-original-preprint | PDF5, SecIII | true |
| WR11-3 | 224Ra颈裂前已有近球形208Pb和14C样的局域密度；在Q30=28 b^(3/2)附近，比较的颈密度约0.09 fm^-3，颈至片段重分配约4.9个核子。 | model-density-analysis | direct-original-preprint | PDF12–13, Fig10 | true |
| WR11-4 | WKB作用量同时依赖V(Q30)、ATDHFB近似惯性、转动修正、零点修正和E0；不是只由基态beta3决定。 | model-method | direct-original-preprint | PDF3–4, Eqs2–7 | true |
| WR11-5 | Table I给出222/224/226Ra的14C计算log10(T/s)=8.90/15.06/18.98，228Th的20O为19.53；与当期实验比较存在约一个至数个数量级差异。 | model-result-and-limit | direct-original-preprint | PDF13 Table I, PDF15–17 | true |
| WR11-6 | 226Th在本文的实验对照是18O+208Pb且仅下限log10(T/s)>16.76；不是已正测的226Th→20O+206Pb。226Th的18O计算值为17.31。 | channel-identification-and-limit | direct-original-preprint | PDF3 scope; PDF13 Table I | true |
| WR11-7 | 226Ra可出现14C与20O两条通道，计算中已观测的14C通道更快；不能把任意最深HFB谷中的碎片直接当成唯一实测团簇。 | competing-channel-model | direct-original-preprint | PDF15–16, Fig13 and text | true |

## Competing Interpretations and Limitations

本工作把团簇衰变视为超非对称裂变，未报告独立的微观团簇通道投影概率P0，也没有完整角动量/粒子数投影GCM的团簇衰变计算。增大变分空间可降低同一约束下的最低势能，但惯性、零点修正和通道选择会改变作用量。文中对14C或20O的标记来自模型密度和碎片数，不是直接测得的基态团簇概率。本文没有可供本轮可靠引用的beta5/beta7逐阶增强因子。

## Knowledge Impact and Learning Decision

为 [[octupole-cluster-radioactivity-preformation-boundary]] 提供统一HFB形变—颈缩—WKB路径，修正“已测低能八极强度即可推出团簇P0”和“226Th20O已正测”的过强读法。

## Extracted Pages

- [[octupole-cluster-radioactivity-preformation-boundary]]

## Review Status

Codex source self-audit；新claim保留needs_review，不标为human-reviewed。
