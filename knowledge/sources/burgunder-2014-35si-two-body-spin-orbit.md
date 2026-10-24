---
type: source
title: "Burgunder2014：35Si (d,p) 反应、双体自旋-轨道力与中心气泡效应争论"
title_original: "Experimental Study of the Two-Body Spin-Orbit Force in Nuclei"
aliases: [Burgunder 2014 35Si spin-orbit, 35Si自旋轨道劈裂实验]
created: 2026-10-23
updated: 2026-10-24
status: ai-draft
review_status: unreviewed
source_type: experiment-and-model
reading_depth: deep-read
authors: [G. Burgunder, O. Sorlin, F. Nowacki, S. Giron, F. Hammache, M. Moukaddam, N. de Séréville, D. Beaumel, L. Càceres, E. Clément, G. Duchêne, J. P. Ebran, B. Fernandez-Dominguez, F. Flavigny, S. Franchoo, J. Gibelin, A. Gillibert, S. Grévy, J. Guillot, A. Lepailleur, I. Matea, A. Matta, L. Nalpas, A. Obertelli, T. Otsuka, J. Pancin, A. Poves, R. Raabe, J. A. Scarpaci, I. Stefan, C. Stodel, T. Suzuki, J. C. Thomas]
journal: Physical Review Letters
year: 2014
volume: "112"
pages: "042502"
doi: "10.1103/PhysRevLett.112.042502"
arxiv: "1401.1593v1"
citation_key: Burgunder_2014
citation_key_origin: locally-assigned-from-verified-DOI
canonical_source: "https://doi.org/10.1103/PhysRevLett.112.042502"
source_url: "https://arxiv.org/abs/1401.1593v1"
raw_file: "raw/papers/day21-20261023/burgunder-2014-35si-two-body-spin-orbit.pdf"
raw_sha256: "c8db651c453428630b450c53a38c28fba05ed7c0fa0dda3023383213c0e53aef"
raw_storage_status: verified-raw-archive
raw_archive_verified_at: 2026-10-23
raw_version: publisher-final-PRL-2014
public_staging_file: "tmp/burgunder2014/spin-orbit_SM_last.tex"
source_independence: GANIL-MUST2-EXOGAM-transfer-experiment-with-reused-37S-reference
nuclei: [34Si, 35Si, 36S, 37S, 40Ca, 41Ca]
reactions: ["34Si(d,p)35Si"]
experiments: [GANIL-MUST2-EXOGAM]
models: [ADWA, TWOFNR, SDPF-U-shell-model, M3Y, N3LO, KLS]
observables: [proton-angular-distribution, spectroscopic-factor, single-particle-splitting, monopole-matrix-elements]
methods: [transfer-reaction, inverse-kinematics, particle-gamma-coincidence, spin-tensor-decomposition]
tags: [a34, a35, spin-orbit, two-body-force, bubble-nucleus, monopole-interaction, evidence-boundary]
---

# 从 (d,p) 转移反应到双体自旋-轨道力与气泡核争论

> Day21 checkpoint042 审计边界：本页本轮001–041新增的“核准/全绿/排他性证伪”等认证，在未列入本轮直接原件核验账本前均为待复核草稿；历史passed或文本锚点命中不认证科学主张。Day19/Day20既有撤回继续有效；原始source claims、review_status与needs_review不因本声明改变。 本审计边界的原件反例见[[biswas-2019-longitudinal-wobbling-133la]]的BI19-D21-R42-2；此链接只支持方法边界，不认证本页其它具体核物理主张。

> checkpoint106为当前限定原件入口。完整VoR5页主线及三图/Table I已实际核；旧056“全部物理效应/严格对偶/原样打印迹为零”认证由R106替代。原Key Results未逐条复核的部分仍待核，原review/flags不提升。旧完整页面存superseded-106。

## Bibliographic Record

Burgunder 等，*Physical Review Letters* **112**, 042502 (2014)，DOI: 10.1103/PhysRevLett.112.042502。本篇为法国 GANIL 开展的放射性束反演运动学 (d,p) 转移反应实验，结合 MUST2 硅探测器阵列与 EXOGAM 锗探测器阵列，首次测定中子富余核 ³⁵Si 中中子单粒子态能量与谱因子。arXiv 预印本版本为 1401.1593v1（TeX 源文件为 `spin-orbit_SM_last.tex`）。106实际核对已有归档的 Physical Review Letters 正式版 PDF，已归档至 `raw/papers/day21-20261023/burgunder-2014-35si-two-body-spin-orbit.pdf`；SHA-256 与正文题名页/DOI一致。`tmp/burgunder2014/` 中的 arXiv TeX 仍作为阅读来源记录保留。

## Scope and Reading Depth

106实际读已归档VoR全部5页主线，视觉核pp2–4的三图/Table I；refs只核所需角色，不称全部被引文已独立复核。对旧预印本TeX本次只另查看Table I的N3LO第一行版本差；早期001/056“22段/定理核准”记录不作为本轮科学认证。原raw版本与哈希保留，未改raw/Bib。

## Summary

VoR报告35Si(d,p)的能谱、γ符合和ADWA分析，据此结合壳模型提出p轨道SO劈裂变化约25%。这与直接主碎片间距约1.134MeV及37S约2MeV的比较属于不同层次。

表I所选2s质子–2p中子单极分解中，K2列为零、打印K0相同，K1承担所列差分；这是该相互作用/空间的分解，不是所有真实核张量贡献都被实验量成零。作者保留其它贡献likely suppressed or modest，并以受约束平均场估算连续谱/束缚能影响小于5%。

经验约束的单极差、同一SM的Baranger结果与现实NN力的理论比较应分开；保作者关于双体SO的支持，不把25%或SF写成直接空间密度测量。本文没有给出“一体气泡势与两体力严格理论等价”的证明。

## Experimental Setup and Method

原件printed042502-2：34Si由55 AMeV的36S碎片化，经LISE3/降能器以20.5 AMeV运输，36S比较束为19 AMeV；CD2反应靶为2.6(1)mg/cm²。旧15.4 AMeV在已读本文无对应输入，不据此补靶内平均反应能；旧0.5mg/cm²不是本文CD2厚度。

四个MUST2模块在约10cm覆盖105°–150°，另有16条环形Si在11.3cm覆盖157°–168°。四个EXOGAM探测器垂直于束轴、中心沿束下移9cm避免遮挡；作者给γ效率3.8(2)% at 1MeV，不能改写为1.33MeV。

printed042502-3：TWOFNR/ADWA及指定全局光学势、非局域修正用于ℓ/SF提取；更换全局势带来约15%附加SF不确定性，本文所列SF误差不含这部分完整处理。两核使用相同势有比较意义，但未给实际jointCov，不默认系统误差全相消。

## Key Results

BU14-1至6为早期混合摘录；当前复核入口为下方R106，尤其SF归反应模型提取、378/380归同源SM。原needs_review保持。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BU14-1 | GANIL 反演运动学 ³⁴Si(d,p) 反应测得 ³⁵Si 基态 7/2⁻ (SF=0.56(6))、910 keV 态 (3/2⁻, SF=0.69(10)) 与 2044 keV 态 (1/2⁻, SF=0.73(10))。 | experimental-fact | direct | PDF p.2, Fig.1-2 | true |
| BU14-2 | 5.5 MeV 附近的连续谱宽结构拟合为 ℓ=3 态，提取 SF=0.32(2)，归属于部分 f₅/₂ 单粒子强度，与 ³⁷S 中 5.6 MeV 处 f₅/₂ 强度 (SF=0.36) 幅度相当。 | experimental-fact | direct | PDF p.2, right col | true |
| BU14-3 | ³⁵Si 中 3/2⁻ 与 1/2⁻ 主碎片能量间距为 1.134 MeV，显著低于 ³⁷S (1.992 MeV) 与 ⁴¹Ca (~2.0 MeV) 中的劈裂，表观减小 858 keV (43%)。 | derived-observable | direct | PDF p.2-3, Fig.3 | true |
| BU14-4 | 大空间 sd-pf 壳模型计算表明，扣除组态混合与多体关联后，真实中子 2p 自旋-轨道单粒子劈裂减小量 ΔSO(p) 为 378 keV (Baranger 质心为 380 keV)，降幅约为 25%。 | model-result | direct | PDF p.3, Eq.(1) | true |
| BU14-5 | 从 ³⁷S 到 ³⁵Si，移走质子主要来自于 2s₁/₂ 轨道 (Δn(2s₁/₂) = 1.47)；因 ℓ=0，质子-中子单极矩阵元的张量力分量 (K=2) 严格为零，排除了张量力主导劈裂减小的假设。 | model-result | direct | PDF p.3-4, Table 1 | true |
| BU14-6 | 单极矩阵元差值完全由双体自旋-轨道分量 (K=1) 承载：实验拟合的单极差 V(2s₁/₂, 2p₁/₂) - V(2s₁/₂, 2p₃/₂) = +0.257 MeV，与现实 M3Y (+0.267 MeV) 及 N3LO/KLS (~0.300 MeV) 微观两体自旋-轨道力计算优良吻合。 | model-result | direct | PDF p.3-4, Table 1 | true |
| BU14-7 | superseded：旧推定−.0965来强制迹为零的认证撤回；VoR打印−.096及有限舍入见BU14-D21-R106-4；旧全文保存在superseded-106。 | withdrawn-task-certification | rejected-and-replaced | PDF p.4, Table 1; audit-002 | true |
| BU14-8 | superseded：旧将严格理论对偶归到Conclusions的认证撤回；原作者限定结论见BU14-D21-R106-5；旧全文保存在superseded-106。 | withdrawn-task-certification | rejected-and-replaced | PDF p.4, Conclusions | true |

## Competing Interpretations and Limitations

主要碎片间距、反应模型提取SF、壳模型ESPE/质心和密度解释各有不同输入。作者通过合适核对尽量压低其它力分量的作用，并非由转移截面无条件测出核内每项力。

Eq.(1)与Baranger质心来自同一套计算的粒子/空穴能量加权强度；其相容是模型内部一致性，不能计作两次独立采集。与M3Y/N3LO/KLS的比较仍有理论信息，但也不是新增核实验；KLS部分还用于SDPF-U跨壳矩阵元。

结论说结果可检验平均场SO的密度/同位旋依赖；不能替作者改成两类模型已严格等价，也不能凭没测密度否定其双体SO支持。还需关联/碎裂、反应响应与独立密度敏感观测，才可裁决更强的排他机制主张。

## Extracted Pages

- Nuclei: [[mutschler-2017-34si-proton-density-bubble]], [[yao-2012-34si-beyond-mean-field-bubble]]
- Methods: [[experimental-claim-boundaries]]
- Synthesis: [[high-spin-lifetime-strength-deformation]]


## Day21 checkpoint056：双体自旋-轨道单极矩阵元与质心展开原件审计

在冻结前置回忆后，重新精读Burgunder等2014年PRL 112, 042502原件全文5页及Table I、Fig. 3。原文BibTeX为`Burgunder_2014`，本地raw文件SHA-256匹配为`c8db651c453428630b450c53a38c28fba05ed7c0fa0dda3023383213c0e53aef`。原BU14-1至8、review_status与needs_review保持。以下为本检查点补充的定向审计声明：

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BU14-D21-R56-1 | superseded：以BU14-D21-R106-4的指定分解/舍入范围取代普遍严格定理认证；旧全文保存在superseded-106。 | withdrawn-task-certification | rejected-and-replaced | PRL 112, 042502 Table I | true |
| BU14-D21-R56-2 | superseded：25%/378keV来自关联处理与模型约束，不是裸实验真值；用BU14-D21-R106-3；旧全文保存在superseded-106。 | withdrawn-task-certification | rejected-and-replaced | PRL 112, 042502 p. 4 Eq.(1)及前段 | true |
| BU14-D21-R56-3 | superseded：原结论保likely suppressed or modest，不证明严格模型对偶或排尽其它机制；用BU14-D21-R106-5；旧全文保存在superseded-106。 | withdrawn-task-certification | rejected-and-replaced | PRL 112, 042502 p. 5 Conclusions | true |

### 科学判定与学习决策

旧056“普遍定理/严格理论对偶”等判定由106替代。保原作者对双体SO的有条件支持；当前提取、模型分解与舍入边界见R106-1至6，不把尚未测定的完整密度或其它力贡献补成排他实验事实。

## Day21 checkpoint106：正式版的推断层次与模型条件

本次实际读VoR5页全部主线文本，视觉核pp2–4三图及Table I；原raw SHA256 `c8db651c453428630b450c53a38c28fba05ed7c0fa0dda3023383213c0e53aef`匹配，未写raw/Bib。Refs只按所需角色核对，不声称独立读完全部被引文。对预印本TeX仅另核Table I的两行版本差，未把TeX替代已核VoR。

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| BU14-D21-R106-1 | 本文34Si运输束20.5AMeV、比较36S束19AMeV，CD2靶2.6(1)mg/cm²；γ效率3.8(2)% at1MeV。旧15.4/0.5靶厚/1.33MeV校准点不作为本篇原输入。 | setup-identity-correction | direct-VoR | 042502-2 Experiment | true |
| BU14-D21-R106-2 | γ峰910(3)与1134(6)keV给2044(7)级联；SF来自ADWA/光学势拟合，更换全局势约15%附加不确定性。f5/2的SF中心.32在Fig2/段落处误差打印不一（Fig2 .32(4)、p3 .32(2)、p4比较.32(3)），不合并为新CI。 | observed-spectra-and-model-extraction | direct-VoR | 042502-3 Fig.2 and ADWA paragraphs | true |
| BU14-D21-R106-3 | 两个sp单极项被约束以匹配关联处理后的主要碎片，得到−.844/−1.101MeV；计算占据1.66→.19，Δn=1.47。Eq1约378keV与Baranger380keV均来自同一SM计算强度，非两套独立实验；旧“真实25%”收窄为作者的模型辅助提取。 | calibrated-model-and-internal-consistency | direct-VoR | 042502-4 Eq.1 | true |
| BU14-D21-R106-4 | TableI是指定KLS/N3LO/M3Y单极分解，K2为零、打印K0相同；N3LO裸为V1/2(K1)=.193、V3/2(K1)=−.096MeV。打印加权迹2V1/2+4V3/2=.002MeV，不能据此改成−.0965的“真值”；近.001MeV舍入的相容性不是实验误差。 | model-table-and-rounding-boundary | direct-VoR-and-task-algebra | 042502-4 Table I | true |
| BU14-D21-R106-5 | 作者称该情形其它力贡献likely suppressed or modest；结论保密度/同位旋依赖检验潜力，不给严格理论对偶或普遍排他证明。 | author-interpretation-and-transfer-limits | direct-VoR | 042502-5 Conclusions | true |
| BU14-D21-R106-6 | M3Y单极SO差.178−(−.089)=.267MeV，与经验约束.257比较是不同理论输入的中央量比较；KLS也用于SDPF-U跨壳矩阵元，诸模型比较不能按引文数计成独立核实验，未得误差前不报匹配sigma。 | theoretical-comparison-and-dependence | direct-VoR-and-task-synthesis | 042502-4 Realistic two-body SO interactions | true |

### 106判断与下一步

`revises`：修输入/分层与过强量词；`supports`：保作者对双体SO的有条件支持，不把模型依赖本身说成实验无效。`limits`：未得原TWOFNR/SM作业、碎裂库存与jointCov；本次只有打印表算术/条件舍入和来源分类，未生成新实验CI、密度或原力分解。

必要companion为同核/比较核的匹配反应响应、遗漏碎片强度与独立密度敏感约束；若不同合理反应/关联模型改变该单极提取，应修订其模型稳定性。尚未完成这种实际联合检验，不把它登记为已证伪。原review与needs_review均保留。
