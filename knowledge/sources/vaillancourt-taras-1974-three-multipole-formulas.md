---
type: source
title: "Vaillancourt and Taras 1974 - Polarization and angular-distribution formulas for three multipoles"
aliases: [Vaillancourt Taras 1974 three multipoles]
created: 2026-09-21
updated: 2026-10-20
status: ai-draft
review_status: unreviewed
source_type: theory-method
reading_depth: deep-read
title_original: "Gamma-ray linear-polarization and angular-distribution formulas for mixtures of three multipoles"
authors: [R. Vaillancourt, P. Taras]
journal: "Nuclear Instruments and Methods"
year: 1974
citation_key: vaillancourt_1974_Gammaray
volume: 114
pages: "333-340"
pii: "0029-554X(74)90552-7"
canonical_source: "Vaillancourt & Taras, Nucl. Instr. Meth. 114, 333-340 (1974)"
library_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1974_Vaillancourt et al_Gamma-ray linear-polarization and angular-distribution formulas for mixtures of three multipoles.pdf"
raw_file: "raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1974_Vaillancourt et al_Gamma-ray linear-polarization and angular-distribution formulas for mixtures of three multipoles.pdf"
raw_sha256: "dbdb5bc9bc7aaa99079f2443e4b2e62d3b84e09d4bf1355942dae4e4ce79218f"
nuclei: [35Cl, 37Ar]
reactions: [generic-alignment-reaction]
experiments: [gamma-angular-distribution, gamma-polarization]
models: [Rose-Brink-phase-defined-matrix-elements]
observables: [angular-distribution, linear-polarization, three-multipole-mixing]
methods: [Method-II-particle-gamma, polarization-formalism]
tags: [three-multipole, polarization, angular-distribution, phase-convention]
---

# Angular-distribution and polarization formulas for mixtures of three multipoles

## Bibliographic Record

- R. Vaillancourt & P. Taras, *Nucl. Instr. Meth.* **114**, 333–340 (1974), PII `0029-554X(74)90552-7`.
- 规范文件：`raw/papers/gpt/high-spin-20260920/multipolarity/mixing ratio/1974_Vaillancourt et al_Gamma-ray linear-polarization and angular-distribution formulas for mixtures of three multipoles.pdf`。

## Scope and Reading Depth

- PDF pp.333–340 (8 pages) fully read: Rose–Brink phases, angular-distribution Eq.13/21, linear-polarization Eq.27/31, general substitution recipe Eq.32, three-multipole Eq.39 and `E1/M2/E3` mixing ratios.
- Not covered: numerical coefficient tables and later software implementations.

## Key Results

- The paper derives phase-consistent angular-distribution and polarization formulas for three multipoles using Rose–Brink reduced matrix elements and explicitly corrects a matrix-element relation/sign issue in the earlier formalism (PDF pp.333–335, Eqs.1–6).
- For mixtures, the angular distribution sums statistical tensors `B_K`, Rose–Brink `R_K` coefficients and all diagonal/interference terms; for three multipoles two independent δ ratios enter the normalized expression (PDF pp.334–338, Eqs.13–21, 37–40).
- A general recipe transforms any angular-distribution term `P_K(cosθ)` into a linear-polarization term by adding `(-1)^π K_K(L,L') cos2φ P_K^2(cosθ)` (Eq.32), extending the earlier two-multipole recipe to arbitrary mixtures (PDF pp.335–337).
- The formulas apply to simple angular distributions and particle–γ Method II correlations, including the practical `E1/M2/E3` case motivating `35Cl` and `37Ar` assignments (PDF pp.333–338).

## Key Results

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| VT74-1 | Three-multipole angular distributions require two independent mixing ratios and all diagonal/interference terms. | formalism-result | direct | PDF pp.334–338, Eqs.13–21, 37–40 | true |
| VT74-2 | A general substitution maps angular-distribution Legendre terms to linear-polarization terms for arbitrary multipole mixtures. | formalism-result | direct | PDF pp.335–337, Eq.32 | false |
| VT74-3 | Phase/state-order conventions must be fixed before comparing calculated and measured mixing-ratio signs. | convention-boundary | direct | PDF pp.333–335 | false |


### Day17原件新增自审

| ID | 陈述 | claim_kind | evidence_level | locator | needs_review |
|---|---|---|---|---|---|
| VT74-D17-1 | 本篇是形式推导；35Cl3162/37Ar1612的旧Jπ与E1inhibition>10^7/约10^6是动机，不报告新的三混合实验fit/重赋Jπ。 | source-scope | direct-and-self-audit | printed333 Introduction; printed340 Conclusions | true |
| VT74-D17-2 | RB T的initialstate写左、final右，time-reversal/CondonShortley相位和αmag=−iαelec明确。Eq5修RB对BM关系，含sqrt[(2L+1)(2Ji+1)/(4π)]的G算符转换；不能当现代相反顺序RME裸桥。 | phase-and-operator-contract | direct-and-self-audit | printed333 Eq1–4; printed334 Eq5–6 | true |
| VT74-D17-3 | Eq16/38 δ为signed T_L/sqrt(2L+1)相对lowestamplitude，两个δ用共同基准，E1M2E3分别sqrt(3/5)T_M2/T_E1、sqrt(3/7)T_E3/T_E1。width只给绝对值，不提供signedphase。 | mixing-convention | direct-and-self-audit | printed335 Eq16; printed337 Eq38–40 | true |
| VT74-D17-4 | Eq7/8起点为cylindrical环境/diagonalM布居，Eq21假定definiteparity且不测circular，只evenK，即使初态有oddB；不将文中general措辞扩成任意coherent3Dρ。 | domain-boundary | direct-and-self-audit | printed334 Eq7–9; printed335 Eq20–21 | true |
| VT74-D17-5 | Eq26 Kcal=−sqrt[(K−2)!/(K+2)!] CG(L1,L′1→K2)/CG(L1,L′−1→K0)，Eq32还带(−1)^π′、secondmultipole的EM标记；不是核角接受Qk或polarimeterQ。 | formalism-contract | direct-and-self-audit | printed336 Eq26–31; printed337 Eq32 | true |
| VT74-D17-6 | R_K与Kcal的CG分母可先消，保存finiteproduct；L3/L′5/K6 CGq0=0而CGq2非零，在Ji3→Jf2得R*Kcal=sqrt(1155)/1980。只把R=0项删除会丢P；不是sourceerratum或认证旧publicproducer。 | task-calculation | direct-and-self-audit | printed335 Eq15; printed336 Eq26; printed337 Eq32 | true |
| VT74-D17-7 | Eq39的三multipole分母1+δ1²+δ2²和三干涉项2δ1/2δ2/2δ1δ2完整；Table1是九orderedpairs，不是九独立核观测。δ2=0回两multipole是坐标极限。 | formalism-and-information | direct-and-self-audit | printed337 Table1 Eq39–40; printed339 Eq49–51 | true |
| VT74-D17-8 | 原Eq52明确ADisotropic仍可能linearP，不能把aK=0时的0/0定义成0；本sessionpositive±1/2布居的3/2→1/2 M1/E2有δ=√3±2两根，使a2=0且P90=±√3/2。 | source-warning-and-task-counterexample | direct-and-self-audit | printed339 Eq52 andfollowingparagraph | true |
| VT74-D17-9 | 新独立Eq9/22 photonamplitude与Eq14/15/26rank展开在三声明case/五θexactI/S交核，含E1M2E3及E3M4E5zeroCG；EM全flip I不变/S反、unoriented I1/S0及δthirdzero极限过，不借旧Day16模型授分。 | task-calculation | direct-and-self-audit | printed334 Eq9; printed335 Eq14–15; printed336 Eq22–26 | true |
| VT74-D17-10 | Eq42–45对完整unobservedγtrace，Uk按γmultipole幅度平方加权且无interference；不是finiteγgate接受，也不能未经分支/ICC合同换totaltransition强度。 | unobserved-feeding-boundary | direct-and-self-audit | printed338 Fig1 Eq42–45 | true |
| VT74-D17-11 | Eq30的lineardistribution和AD均归一K0=1，故W(θ,0)+W(θ,90)=2W(θ)，不是未说明half切换；boundedP由差和得，单独线分布不同仪器A。 | normalization-contract | direct-and-self-audit | printed336 Eq29–31; printed339 Eq53 | true |
| VT74-D17-12 | 本篇p=J0/J90是强度比，末段p′才差和；N=N90/N0、R=σ90/σ0，Eq56经转换精确得A=QP，Q=(R−1)/(R+1)。与EW69 ratio解释相容但不证明EW69作者意图/Ref9body。 | observable-dictionary | direct-and-self-audit | printed339 Eq53–56 | true |
| VT74-D17-13 | Eq54全EM互换对应p倒数、p′反号；不在字面ratio上直接负号。不称纯/混合P正负能自动唯一δ/Jπ。 | convention-control | direct-and-self-audit | printed339 Eq54 | true |
| VT74-D17-14 | MethodII须particle detector沿symmetryaxis、P和correlation用同statisticaltensor，作者normallyunique属于有条件预期，不是原数据已消所有branch或universality定理。 | companion-and-identifiability-boundary | direct-and-self-audit | printed339–340 Conclusions | true |

## Summary

Vaillancourt and Taras extend the Rose–Brink formalism beyond two multipoles and provide a practical angular-to-polarization transformation. The result is a method backbone for rare `E1/M2/E3` and other three-component transitions, but it increases rather than removes identifiability and convention requirements.

## Competing Interpretations and Limitations

- Two measured angular coefficients may not identify two δ ratios plus alignment; polarization or independent multipolarity information is often required.
- The formula assumes cylindrical alignment and definite parity in the simplified forms; general expressions are needed otherwise.
- The corrected Rose–Brink relation must be distinguished from experimental Biedenharn/Taras conventions.

## Analytical Reconstruction and Self-Audit

| ID | 审核项 | Agent 判断 | Evidence / locator | 审核状态 |
|---|---|---|---|---|
| VT74-AR-1 | Formal chain | Rose–Brink operators → three-multipole angular distribution → two δ ratios → polarization substitution. | PDF Eqs.13–40 | self-checking |
| VT74-AR-2 | Identifiability | Alignment, two δ ratios and detector response are coupled; retain branch sets. | PDF pp.334–338 | active-L3 |

## Knowledge Impact and Learning Decision

- Effect: `supports` [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]], [[rose-brink-1967-phase-defined-angular-distributions]] and three-multipole method audits.
- Review state: Codex self-audited; not `human-reviewed`.

## Human Review Triage

### P0

- `VT74-P0-1`: Preserve corrected phase convention, two-δ identifiability and alignment boundaries before applying the formulas to level assignments.

## Extracted Pages

- Methods/observables: [[angular-distribution]], [[angular-correlation]], [[multipole-mixing-ratio]]。

## Day17原件复核：finiteproduct与isotropicAD的偏振反例

先冻vaillancourt1974-before/exercise并声明旧VT74/Day16finiteStokes与phase priming，原8页333–340完整text/visual；Eq1–56（含4a/b）、Table1九pair、Fig1及11refs全核。548901bytes/hash `dbdb5bc9bc7aaa99079f2443e4b2e62d3b84e09d4bf1355942dae4e4ce79218f`保持，旧VT74-1–3/flags与citationkey保，14新待审，不晋人审。旧scope的39/40并非全文式末端，本次实际覆盖到56。

[[three-multipole-polarization-response-contract]]保存原phase/operatororder、finiteR*K、positiveisotropicAD反例、完整trace/有限门边界及p/N/R字典。新script独立直接Eq9amplitude与rank两路交核，不调旧UCproducer或Day16fullfinite；只在声明axisymmetricdiagonalρ/definiteparity/pure或realmixture域，非general3DStokes或actual35Cl/37Arfit。

本篇明确p为J0/J90，支持ratio与boundedP分离的历史命名存在；它不是EW69未取得Ref9/作者意图的替代primary，EW69-D17-5/11撤回旧>1即failure的修订保持且不升级作者解释。决定`supports`physicalP与响应合同，`limits`ADisotropic→P0、CG0就删偏振项、三分量能无条件唯一识别的简写。没有新核Jπ/δ实验或instrumentQ/Σ/CI。
