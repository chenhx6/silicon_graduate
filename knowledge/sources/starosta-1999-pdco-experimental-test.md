---
type: source
title: "Starosta et al. 1999 - Experimental test of the polarization direction correlation method"
aliases: [Starosta 1999 PDCO]
created: 2026-09-20
updated: 2026-10-17
status: ai-draft
review_status: unreviewed
source_type: method-paper-and-application
reading_depth: deep-read
title_original: "Experimental test of the polarization direction correlation method (PDCO)"
authors: [K. Starosta, T. Morek, Ch. Droste, S. G. Rohozinski, J. Srebrny, A. Wierzchucka, M. Bergström, B. Herskind, E. Melby, T. Czosnyka, P. J. Napiorkowski]
journal: "Nuclear Instruments and Methods in Physics Research A"
year: 1999
doi: "10.1016/S0168-9002(98)01220-0"
citation_key: starosta_1999_Experimental
volume: 423
pages: "16-26"
pii: "S0168-9002(98)01220-0"
canonical_source: "Starosta et al., NIM A 423, 16-26 (1999)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1999_Starosta et al_Experimental test of the polarization direction correlation method (PDCO).pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1999_Starosta et al_Experimental test of the polarization direction correlation method (PDCO).pdf"
raw_sha256: "883fdd7b08831efefe25f5df610e84b95bb1acbcd7b8e7f684b1a1b31bf8030b"
nuclei: [164Yb, 126Ba, 114Cd, 118Sn]
reactions: [138Ba-30Si-4n, 114Cd-16O-4n, 114Cd-16O-Coulomb-excitation, 118Sn-16O-Coulomb-excitation]
experiments: [EUROGAM-II, NORDBALL-clover-calibration]
models: [PDCO, DCO, integrated-PDCO, polarization-angular-distribution]
observables: [linear-polarization, Compton-asymmetry, DCO-ratio, spin-alignment, multipole-assignment]
methods: [Compton-polarimetry, PDCO, DCO-ratio, gamma-gamma-angular-correlation]
tags: [PDCO, CLOVER, EUROGAM-II, polarization, DCO, multipolarity]
---

# Experimental test of the polarization direction correlation method (PDCO)

## Bibliographic Record

- K. Starosta *et al.*, *NIM A* **423**, 16–26 (1999), PII `S0168-9002(98)01220-0`.
- 2026-10-17 Crossref exact DOI核题名、11作者、423(1)、16–26及1999年2月：`10.1016/S0168-9002(98)01220-0`；它是元数据交叉核验，正文证据仍取本地原PDF。
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1999_Starosta et al_Experimental test of the polarization direction correlation method (PDCO).pdf`。

## Scope and Reading Depth

- PDF pp.16–26 fully read: EUROGAM-II geometry, NORDBALL CLOVER calibration, `Q(E)` fit, DCO alignment extraction, integrated-PDCO asymmetry, four detector-pair geometries, Tables 1–4, Figs.1–7 and conclusions.
- Not covered: the cited original level-scheme papers, PDCO program source code and raw coincidence matrices.

## Key Results

- 原实验为 `164Yb`，由 `138Ba(30Si,4n)` 在150/155 MeV布居；阵列有30 coaxial Ge及24 CLOVER，实际选18 CLOVER作本分析polarimeter。NORDBALL的单CLOVER标定只是移用近似（printed17–18,21；ST99-5/7）。旧Wiki核素/反应转录有误，已按原件纠正。
- `A=QP`；原式为 `Q=Q0[0.31(2)+7(2)×10^-5 Eγ(keV)]`，`Q0=(1+x)/(1+x+x²), x=Eγ/511keV`（printed19 Table1 Eq5/6）。旧Wiki的10^-4是转录错误；原式及Table1不支持将该曲线无校准移用其它仪器。
- For the 490-keV `16+→14+` candidate, integrated mode gives `A=+0.120(12)` and estimated `P=+0.50(5)`, while `R_DCO=0.96(2)`; the combined `(P,R_DCO)` contours exclude most hypotheses but retain stretched E2 and an `M1/E2, ΔI=0, arctanδ≈−21°` solution (PDF pp.20–24, Figs.5–6, Tables 2–3).
- 647 keV的 `R_DCO=.51(3)` 与PDCO在测试假设中支持 `|ΔI|=1 E1` 类别；Table4仍列 `11−→10+` 和 `9−→10+` 两个低score候选，不能将类别选择写成PDCO独立唯一选定11−（printed24–25；ST99-11）。
- The authors conclude that intensity as low as about 15–20% of the strongest transition can be useful, but integrated-PDCO comparisons are qualitative unless detector solid-angle and efficiency corrections are known (PDF pp.25–26).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| ST99-1 | PDCO combines a direction-sensitive CLOVER polarization measurement with a coincident-gamma DCO ratio to reduce multipolarity ambiguity. | method-result | direct | PDF pp.16–17, 22–25 | true |
| ST99-2 | The 490-keV case remains non-unique between stretched E2 and a ΔI=0 M1/E2 branch after the combined fit. | assignment-boundary | direct | PDF pp.22–25, Tables 2–3 | true |
| ST99-3 | The 647-keV transition is assigned as ΔI=1 E1 within the tested hypotheses. | assignment-result | direct | PDF pp.24–25, Table 4 | true |
| ST99-4 | `Q`, detector geometry, solid-angle coverage, efficiencies and assumed alignment are setup-specific inputs. | limitation | direct | PDF pp.18–20, 21–26 | false |
| ST99-5 | 主数据为138Ba(30Si,4n)164Yb、150/155MeV；NORDBALL标定为114Cd(16O,4n)126Ba、83MeV，另以44MeV16O Coulomb excitation产生114Cd558keV及118Sn1230keV校准线。旧Wiki的162Yb/152Ba/130Cd/132Sn等身份不符原件，已纠正。 | source-identity-correction | direct-and-self-audit | printed17 Sec2；printed18–19 Sec3 Table1 | true |
| ST99-6 | Eq5线性项为7(2)×10^-5 Eγ(keV)，不是旧Wiki的10^-4；Eq6的ideal Q0使用x=Eγ/511。490keV作者采用近似Q=.24，A=.120(12)给P=.50(5)；代印刷central curve得Q=.234314/P=.512133属于另一次受限核算，不能强制等于近似值或补出校准Cov。 | calibration-correction-and-replay | direct-and-task-calculation | printed19 Eq5–6 Table1；printed21 Sec5 | true |
| ST99-7 | Q由NORDBALL79°单CLOVER移用；EUROGAM-II实际选18/24 polarimeters，个体.95<a<1.05，合并.99<a<1.01后采用a=1。四组PDCO配对A/B按相对phi，C/D按coaxial ring区分，不能由single-gamma Q补成完整joint response。 | response-and-transfer-boundary | direct | printed18 Sec3 Fig2；printed21 Sec5；printed22 Sec6 | true |
| ST99-8 | 脚注1更正D96 Eq4广义polarization系数的磁项相位：应为(-1)^(delta_(Tprime,M))，非印刷的(-1)^(delta_(T,M))。作者称其程序无此错误；本session未取得程序，不能将声明写成代码验证，也不能与delta基底坐标换号合并。 | published-print-correction | direct | printed17 footnote1 (PDF2) | true |
| ST99-9 | Eq7对四个P与一个RDCO组成的五点作对角reduced chi²：固定sigma/I时NDF为pure5/mixed4；浮动sigma/I时Table3为pure4/mixed3、Table4全为3。integrated P非第六独立点；.26(5)由647同一DCO在先验已知E1路径下求得，再移用于490，不是独立新alignment测量。 | fit-definition-and-dependence | direct | printed20 Sec4 Fig4；printed23 Eq7；printed24 Table3 footnote Sec7 | true |
| ST99-10 | 字面重算13行印刷理论/观测/误差时，Table2 15+→14+为108.91145，与原表79.5不同；在明确的每个mean/theory/sigma末位±.005模型下rowwise包络92.2430–132.7572仍不含79.5±.05。保留原表值；unrounded theory、fit minimum/program与误差预算未得，只立replay boundary，不判作者计算错误。 | bounded-table-replay | task-calculation-from-source | printed23 Table2 Eq7 | true |
| ST99-11 | Table4的11−→10+和9−→10+分别报score.6/1.2及sigma/I .27/.11；支持的共同类别为|ΔI|=1 E1，非仅凭该表唯一固定初态11−。.26(5)先前从已知647路径校准，不能作独立prior再次计数。 | assignment-and-calibration-boundary | direct-and-self-audit | printed25 Table4；printed20 Fig4 Sec4 | true |
| ST99-12 | 原文为490keV两候选预测写alpha_κ=.012/.033（保留其下标，不补成总ICC或在未核定义前指定壳层），不是测得转换系数。E1/M2排除还用Weisskopf/强度上限推得≥4ns、无预期Doppler偏移/展宽及约400ps飞行比较；不是独立直接寿命测量。 | companion-observable-and-model-boundary | direct | printed20–21 Sec4；printed26 conclusion (PDF11) | true |
| ST99-13 | integrated PDCO缺失立体角/效率修正时作者只主张定性使用；它与四组PDCO、RDCO复用同一主采集而非新增独立实验。Q标定另采集但仍与核polarization模型输入相依；full event/correction covariance未给。 | evidence-independence-boundary | direct-and-self-audit | printed21 Sec5；printed25 conclusion | true |

## Summary

Starosta *et al.* provide a practical validation of PDCO for modern CLOVER arrays. The experiment demonstrates the value of combining polarization and DCO information, while its unresolved 490-keV branch is a counterexample to treating a clean `R_DCO` or polarization sign as a unique spin assignment.

## Competing Interpretations and Limitations

- Integrated mode smears directional information over a large solid angle. Without correction for detector coverage and relative efficiency, its polarization should be treated as qualitative (PDF pp.21–22, 26).
- 取向宽度符号为 `sigma/I=0.26(5)`，不是OCR误读的Latin p/I。它由647keV的同一DCO配合既有11−→10+ E1指认求得，再移用于490keV；不能将它与647拟合当两份独立证据。
- The single-CLOVER NORDBALL calibration is used as a proxy for the 24-CLOVER EUROGAM response. Thresholds, geometry and asymmetry correction `a` may alter `Q` and `P`.
- The remaining E2 versus mixed M1/E2 ambiguity requires additional evidence such as conversion coefficients or an independent level assignment.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| ST99-AR-1 | Response chain | Unpolarized asymmetry correction `a` → measured Compton asymmetry `A` → detector sensitivity `Q(E)` → physical `P`; DCO supplies alignment/multipole constraints. | PDF Eqs.1–6, pp.18–20 | self-checking |
| ST99-AR-2 | Joint-fit chain | Four polarimeter/geometries plus DCO are compared through reduced `chi²_nu`, Eq7；字面印刷表重算边界见ST99-10，不宣称完整重放。 | PDF Eq.7, Figs.6–7, Tables 2–4 | self-checking |
| ST99-AR-3 | Transfer condition | `Q`, `sigma/I`, gate cascade, detector positions and convention must be re-established before reusing a PDCO contour. | PDF pp.18–24 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]] and the DCO/PDCO evidence map.
- New reusable rule: a combined polarization–DCO fit can narrow, but need not eliminate, spin/mixing-ratio branches; retain a branch table until independent conversion/lifetime/configuration evidence closes it.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `ST99-P0-1`: Do not transfer the reported `Q(E)`, `sigma/I`, `P` or `chi²_nu` contours to another CLOVER array without geometry, threshold, asymmetry-correction and alignment recalibration.

## 2026-10-17原件复核：校准、勘误与五点重放边界

本session先冻结注明priming的回忆，再重核11页原件hash；沿主线完整读printed16–26，视觉复核Fig1–7、Eq1–7及Table1–4，特别检查printed17脚注、printed19指数、printed23–25表格和printed26下标。旧ST99-1–4逐字/flags及page review保留；元数据和summary的错误转录按直接原件更正，不新增human review。D96为共享理论/程序链，旧Yb论文[6]与[14]提供先前能级/assignment，不把本篇复用内容再计新采集。

原文polarization为`P=(W_parallel−W_perp)/(W_parallel+W_perp)`（电场方向），计数asymmetry为`A=(aN_perp−N_parallel)/(aN_perp+N_parallel)`（Compton散射方向），且`a=N_parallel(unpolarized)/N_perp(unpolarized)`。两种parallel不可混为同一个计数。Eq6的能量变量在原文也写alpha，与此几何a和nuclear alignment均不同。

定量、原表全部13行、舍入假设和chosenCov敏感性保存在[[st99-pdco-calibration-table-replay]]；该页列出冻结输入/hash、脚本及失败控制。Table2的15+行不闭合是有记录的复现缺口，不能由未知Cov随意补拟或改原表数值。未得到unrounded producer output、event matrices、完整joint response和实际Sigma；L4实际重分析仍not-ready。

## Extracted Pages

- Methods: [[compton-polarimetry]], [[linear-polarization-asymmetry]], [[angular-correlation]]。
