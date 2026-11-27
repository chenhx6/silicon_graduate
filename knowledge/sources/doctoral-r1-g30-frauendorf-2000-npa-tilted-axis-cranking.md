---
type: source
title: 'Frauendorf 2000: 倾斜轴推转模型描述多准粒子带与轴对称进动理论 (NPA全文56页)'
aliases: [Frauendorf 2000 NPA TAC, Nucl. Phys. A 677 115, 10.1016/S0375-9474(00)00308-0]
created: 2026-11-08
updated: 2026-11-27
status: active
review_status: unreviewed
source_type: journal-article
reading_depth: read
title_original: Description of multi-quasiparticle bands by the tilted axis cranking model
authors: [S. Frauendorf]
journal: Nuclear Physics A
year: 2000
volume: 677
pages: 115-170
doi: 10.1016/S0375-9474(00)00308-0
canonical_source: https://doi.org/10.1016/S0375-9474(00)00308-0
citation_key: ''
raw_file: raw/papers/gpt/query/20261108-foundations-G30/frauendorf-2000-npa677-tilted-axis-cranking.pdf
raw_sha256: c7487e240ab561d9fafa089ce449a864fe892efbdc880845bf2355eeb848c135
raw_storage_status: archived-local
archive_required: true
learning_candidate: true
nuclei: []
models: [tilted-axis-cranking, pairing-plus-quadrupole, strutinsky-renormalization]
observables: [rotational-energy, b(m1), b(e2), mixing-ratio, tilt-angle]
methods: [cranked-mean-field, semiclassical-quantization, diabatic-tracing]
tags: [tilted-axis-cranking, tac, high-k-bands, precession, wobbling-boundary, multiquasiparticle, rare-earth, fulltext-read]
---

# Frauendorf2000：多准粒子带的TAC理论与带内电磁算符

## Bibliographic Record

S. Frauendorf，*Description of multi-quasiparticle bands by the tilted axis cranking model*，NPA677,115–170(2000)，DOI `10.1016/S0375-9474(00)00308-0`。
实际出版PDF为56页，哈希见frontmatter。

## Scope and Reading Depth

G30报告读取理论主线；总控独立核PDF1、5、10–11/printed115、119、124–125。
本页只保留已定位的自洽关系、参数化与带内EM，不声称总控重读全部56页或复算全套多准粒子带。
作者主要实例范围为N=102,103、Z=71,72,73；178W的具体实验来自另一个source，不能归作本文新测。

## Summary

TAC是自洽倾斜均场及半经典离散谱对应的方法。
带内ΔI=1 E2振幅可因倾角非零而存在，因此“存在E2”本身不唯一识别正交摆动伴带。
形状、角速度/角动量和电磁算符约定须共同使用。

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| F00-1 | 自洽定态的E′、E及dE′/dω=−J、dE/dJ=ω；角速度向量与角动量期望平行 | mean-field-theory | direct-original | PDF5/printed119 Eqs.15–24 | false |
| F00-2 | SCTAC中总Routhian对形变等变量求定态；在良好形变带中冻结形变只是精度/代价相关近似 | model-construction | direct-original | PDF10/printed124 Eqs.38–39及末段 | false |
| F00-3 | 带内M1振幅涉及μ₃sinϑ−μ₁cosϑ；磁矩有指定有效自旋因子和量子修正 | operator-convention | direct-original | PDF10–11 Eqs.40–43 | false |
| F00-4 | Eq.45的带内ΔI=1 E2振幅为√(5/4π)(eZ/A)sinϑcosϑ[√(3/2)⟨Q′₀⟩−(⟨Q′₂+Q′₋₂⟩)/2] | operator-convention | direct-original | PDF11/printed125 Eq.45 | false |

Eq.45按本文Q′定义保留(eZ/A)，不擅自丢失电荷/质量归一。
Eq.43采用η=0.7，作者明确其它质量区可不同、质中也可不同；没有原文依据的±15%误差已删。

## Competing Interpretations and Limitations

均场倾斜解不自动给正交多声子伴带；带内半经典矩阵元不是所有带间跃迁的通用公式。
本页不由电荷轴对称推出真实K严格守恒或Pauli普适零惯量。
自洽条件、离散自旋对应、假态消除须按作者约定和具体解检验，不能写“高自旋精确等同”。

## Extracted Pages

[[doctoral-r1-g30-a160-precession-wobbling-20261108]]区分三个对称模型合同，
另用Purry论文核178W实验。跨区使用须重建实际组态和算符。

## Agent Self-audit Triage

P0：原件与算符归一核查已完成；旧稿遗漏eZ/A及惯量普适化已撤回。
P1：作者代码、全带数值与全部离散量子化细节未重放。

## 2026-11-27 — 馆藏原件与覆盖核对

- {"pdf_start": 1, "pdf_end": 12, "sections": "题头、§1引言、§§2.1–2.6均场及带内电磁算符，§2.7开头"}
- {"pdf_start": 13, "pdf_end": 24, "sections": "§§2.7–2.12半经典量子化、非绝热追踪、配对近似、准粒子图及 PAC 比较"}
- {"pdf_start": 25, "pdf_end": 50, "sections": "§2.12末段，§§3.1–3.10组态、假态、带头与四核实例，§4开头"}
- {"pdf_start": 51, "pdf_end": 56, "sections": "§4规则续，§5结论、致谢和参考文献"}
- 本次获取的具体覆盖：逐页读完实页1–56的所供文本，包括§§1–5、表1的抽取文字、图1–28的题注、致谢及参考文献[1]–[77]。按正文与题注辨认计算和实验资料，未查看图像、追读引文原件或重跑计算。

| ID | Statement | claim_kind | evidence_level | locator | needs_review |
| --- | --- | --- | --- | --- | --- |
| A21-1 | 自洽定态满足 dE′/dω=−J、dE/dJ=ω，且角速度与角动量期望向量平行。SCTAC 对总 Routhian 寻找定态。良形变带内冻结形变是作者按所需精度采用的近似。 | 模型构造 | source-reported | PDF 实页5–6（印刷119–120），式(15)–(26)；实页8–9（122–123），式(34)–(35)；实页10（124），式(38)–(39)及§2.5末段。 | true |
| A21-2 | 半经典带内 M1 振幅含 μ₃sinϑ−μ₁cosϑ。带内 ΔI=1 E2 振幅含 sinϑcosϑ，在质量四极矩约定下保留 eZ/A。式(45)的根号与括号须查实页11。作者采用 η=0.7，并允许其他质量区及质子、中子使用不同衰减。 | 理论算符约定 | source-reported | PDF 实页10–12（印刷124–126），式(40)–(45)、(48)–(51)及§2.6末段。 | true |
| A21-3 | 作者转引的 ¹⁷⁴Hf 数据中，18⁺带的分支比在低转动频率区呈上升趋势。该趋势据正文转述，数据点和坐标须查实页50图28。 | 引述实验观察 | source-reported | PDF 实页48（印刷162），§3.10分支比讨论；实页50（164），图28及题注，数据来自[66,67]。 | true |
| A21-4 | 作者报告，有限中子配对和零中子配对计算对 ¹⁷⁴Hf 的14⁺带给出相近分支比。零中子配对计算再现18⁺带的低频上升趋势，但低估实验比值。两组曲线及图例须查实页50图28。 | 模型与数据比较 | source-reported | PDF 实页48（印刷162），§3.10；实页50（164），图28及题注。 | true |

与 Wiki 的归档路径及 SHA-256 一致。建议接受既有 G30 对实页1、5、10–11的同版定点覆盖，以及自洽关系、SCTAC 和带内算符的定性摘要。式(45)的整式转录待核实页11。既有记录的覆盖粒度维持为定点核读，本次另有实页1–56的逐页文字审计。

- 将 F00-1 的定位扩至实页6式(25)–(26)，以包含平行条件的结论。F00-4 保留 eZ/A，并将式(45)整式的复核状态改为待查实页11。实页11式(46)的量子修正分母在抽文中互异，实页12式(50)–(51)后的均方半径近似单位残损，暂缓转录。维持撤回无出处的 η ±15% 和惯量普适化。
- 实页35图16题注对两类实验 Routhian 重复写式(52)–(53)。核对原版题注，Wiki 的计算口径按实页13§2.7注明，有 signature 分裂的 ΔI=2 支使用式(54)–(55)。
- 实页43图22和实页44图23题注把 ¹⁷⁴₇₂Hf 的中子下标抽为104。按实页25的核素范围、实页41正文及质量数与质子数关系，Wiki 应记 N=102。两处原版下标分别核图。
- 实页23在式(67)后抽出 cosϑ=K/J₁，与实页8式(34)和实页22式(62)合读应为 K/J。实页27§3.2抽出的镜像角 90°−ϑ₀ 与实页51规则12及实页29的续述冲突，Wiki 采用绕90°反射的 180°−ϑ₀。分别核实页23及27的印刷写法。
